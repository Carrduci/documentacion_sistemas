# Búsqueda de texto

Para usar la búsqueda de texto, hay que llevar a cabo una serie de pasos tanto en el API como en la GUI.

## Usar el plugin en el modelo

Lo primero es incluir el plugin de búsqueda de texto en el modelo o modelos que se requiera.

Este plugin creara un campo en los documentos del modelo llamado `buqueda`, por lo que hay que incluirlo en el modelo. Ese campo sera indexado con un índice de texto en la base de datos y servirá para hacer búsquedas de texto

Por ejemplo.

```js
const Mongoose = require('mongoose');
const Schema = Mongoose.Schema;

// Importacion del plugin de busqueda de texto.
// La ruta de importacion puede variar.
const BUSQUDA_TEXTO = require('../../../busqueda-texto.plugin');

// Importacion de los campos de busqueda. En este archivo
// hay que especificar que campos del modelo se tomaran para
// generar el índice.
// La ruta puede variar.
const CAMPOS_BUSQUEDA = require('../../../utils/camposBusquedaTodosLosModelos.utils');

const ELEMENTO_SCHEMA = Schema(
    {
        nombre: String,
        etiquetas: [String],
        otroCampo: Object,

        // Campo que llenara el plugin de busqueda de texto.
        busqueda: String
    },
    {
        collection: 'elementos',
        timestamps: true
    }
);

// Así se conecta el plugin.
ELEMENTO_SCHEMA.plugin(BUSQUDA_TEXTO.text_search_index, {
    // Aquí se pasan los campos para usar en el índice.
    // Reemplazar "ELEMENTO" por el nombre deseado.
    fields: CAMPOS_BUSQUEDA.ELEMENTO
});

const ELEMENTO_MODEL = Mongoose.model('Elemento', ELEMENTO_SCHEMA);

module.exports = ELEMENTO_MODEL;

ELEMENTO_MODEL.createCollection();
```

Esto es lo que hay que agregar en le archivo `camposBusquedaTodosLosModelos.utils.js`.

```js
// Esto ya está en el archivo.
let camposBusqueda = {};

// ...

// Esto es lo nuevo por agregar. Reemplazar "ELEMENTO" por
// el nombre deseado. Los campos pueden cambiar según se necesite.
camposBusqueda.ELEMENTO = ['nombre', 'etiquetas'];

module.exports = camposBusqueda;
```

## Hacer uso del índice en el servicio del API

?> Para este paso ya debes tener una ruta y su controlador. Ver [estructura de archivos y código](./docs/carrduci-sys-desarrollo/3-estructura-de-archivos-y-codigo.md).

Para usar el índice, en la clase del servicio del API correspondiente, hacer lo siguiente.

```js
// Importar el modelo.
// La ruta es de ejemplo y puede variar.
const ELEMENTO_MODEL = require('../../../models/elementos/elemento.model');

const SERVICIO = {};

SERVICIO.obtenerElementos = async function({
    // Campos para paginacion.
    desde,
    limite,
    sort,
    campo,

    filtros,

    // Aqui debe llegar la cadena de texto que
    // el usuario escribe, con lo que se buscarán
    // elementos.
    termino
}) {
    desde = Number(desde ?? 0);
    limite = Number(limite ?? 5);
    sort = Number(sort ?? -1);
    campo = String(campo ?? '_id');
    filtros = filtros ?? {};

    // Limpiar las diagonales invertidas de la cadena
    // de texto.
    termino = !!termino ? String(termino).replace(/\\/gm, '') : undefined;

    let filtrosProcesar = {
        ...filtros,

        // La busqueda de texto se maneja como un filtro.
        terminoTextSearch: termino
    };

    // Aquí se genera la query que se le pasa al .find(). Si llega un valor
    // en el campo "termino", la query incluye lo necesario para hacer la
    // busqueda de texto con indices.
    let queryFiltros = this.queryFiltrosElementos(filtrosProcesar);

    // Luego se cuenta el total de documentos que tendría el resultado.
    let total = await ELEMENTO_MODEL.countDocuments(queryFiltros);

    // Si no hay resultados y se uso la busqueda por termino, intentar
    // la búsqueda por regex en lugar de índice. Si aún así el resultado
    // está vacío, pasa como tal.
    if (total === 0 && termino) {
        // Aquí se indica el cambio de indice a regex.
        filtrosProcesar.terminoRegex = termino;
        delete filtrosProcesar.terminoTextSearch;

        // Obtener la query de nuevo.
        queryFiltros = this.queryFiltrosElementos(filtrosProcesar);

        // Contar los documentos de nuevo.
        total = await ELEMENTO_MODEL.countDocuments(queryFiltros);
    }

    // Si la query incluye el campo "$text", es busqueda de indice.
    const ES_BUSQUEDA_INDICE = !!queryFiltros.$text;

    // Si es busqueda de indice, agregar el campo "score", que guarda
    // un valor numerico que, mientras mas alto, indica una mayor relacion
    // con la busqueda de texto realizada. Esto servirá para ordenar los
    // resultados por relevancia.
    // La proyección es para agregar o quitar campos del resultado de la
    // query, en este caso solo se agrega un campo (si es busqueda de
    // índice).
    const PROJECTION = ES_BUSQUEDA_INDICE
        ? { score: { $meta: 'textScore' } }
        : {};

    // Esto es para ordenar los resultados. En la llave del objeto se
    // indica el nombre del campo por el cual ordenar y el valor puede
    // ser 1, que significa descendiente, o -1, que significa ascendente.
    const CRITERIOS_SORT = ES_BUSQUEDA_INDICE
        ? {
                // Primero ordenar por el campo especificado en la GUI.
                [campo]: sort,

                // Luego siempre ordenar por _id.
                _id: sort,

                // Al final ordenar por relevancia respecto a la búsqueda
                // con índices de texto.
                score: { $meta: 'textScore' }
            }
        : {
                // Si no hay búsqueda de índices de texto, solo ordenar por
                // el campo de la GUI y por _id.
                [campo]: sort,
                _id: sort
            };

    // Esta es la ejecución de la query de búsqueda.
    const RESULTADO = await ELEMENTO_MODEL.find(
        queryFiltros, // La query que puede incluir la búsqueda de texto.
        PROJECTION // La proyección que puede agregar "score".
    )
        // Esto es la paginación.
        .skip(desde)
        .limit(limite)

        // Aquí se aplica el ordenamiento.
        .sort(CRITERIOS_SORT)

        // Estos campos se van a quitar del resultado final.
        .select('-busqueda -__v -score')

        // Esto convierte el resultado a un POJO, lo que lo que
        // lo hace más ligero.
        .lean();

    // Retornar un objeto con el resultado paginado y el total
    // de resultados sin paginar.
    return { resultado, total };
}

// Esta función es para generar la query de busqueda.
fucntion queryFiltrosElementos({ terminoTextSearch, terminoRegex }) {
    let filtros = {};
    if (!!terminoTextSearch) {
        filtros.$text = {
            $search: `${terminoTextSearch} "${terminoTextSearch}"`
        };
    }
    if (!!terminoRegex)
        filtros.busqueda = { $regex: terminoRegex, $options: 'i' };

    // Aquí se pueden agregar más filtros.

    return filtros;
}

module.exports = SERVICIO;
```

## Uso en el servicio de la GUI

En el servicio relacionado al módulo que se esté haciendo, se recomienda usar la siguiente estructura.

```ts
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { URL_BASE } from 'src/app/config/config';
import { ManejoDeMensajesService } from 'src/app/services/utilidades/manejo-de-mensajes.service';
import { PreLoaderService } from '../pre-loader/pre-loader.service';
import { ElementoRecibir } from './elementos.model';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { Paginacion } from 'src/app/utils/paginacion.util';

@Injectable({
    providedIn: 'root'
})
export class ElementoService {
    constructor(
        private http: HttpClient,
        private msjService: ManejoDeMensajesService,
        private preloader: PreLoaderService
    ) {}

    private URL_ELEMENTOS = (ruta: string = '') =>
        URL_BASE(`elementos${ruta.length > 0 ? '/' : ''}${ruta}`);

    TOTAL_ELEMENTOS: number = 0;

    // ... Otras funciones

    obtener(
        paginacion: Paginacion,

        // Aquí es donde se pasa el término (búsqueda de texto).
        termino?: string

        // Aquí se le pone el tipo "any" a los filtros por demostración,
        // pero lo ideal es que en el modelo de la GUI se especifique
        // una interfaz para los filtros.
        filtros?: any,
    ): Observable<ElementoRecibir[]> {
        // Esto es para mostrar un preloader.
        let idCarga = this.preloader.loading('Obteniendo elementos');

        let url = this.URL_ELEMENTOS(``)

            // Paginacion y ordenamiento.
            .concat(`?desde=${paginacion.desde}`)
            .concat(`&limite=${paginacion.limite}`)
            .concat(`&campo=${paginacion.campoDeOrdenamiento}`)
            .concat(`&sort=${paginacion.orden}`);

        // Tanto filtros como termino se mandan en la query de la url.
        if (!!filtros) {
            url = url.concat(`&filtros=${JSON.stringify(filtros)}`);
        }
        if (!!termino) {
            // Aquí es donde pasamos la búsqueda de texto, a través
            // de la URL.
            url = url.concat(`&termino=${termino}`);
        }

        // Esta es la consulta al API.
        return this.http.get(url).pipe(
            map((resp: any) => {
                // Cerrar el preloader.
                this.preloader.ok(idCarga);

                // Obtener el total de elementos.
                this.TOTAL_ELEMENTOS = resp.total;

                // Convertir todos los resultados al tipo "ElementoRecibir".
                const DATOS = resp.datos as any[];
                return DATOS.map((elemento) => new ElementoRecibir(elemento));
            }),
            catchError((err) => {
                // En caso de error, detener el preloader.
                this.preloader.err();

                // En caso de error, mandar un popup de error
                // a la pantalla.
                this.msjService.err(err);

                // Retornar el error usando el operador de rxjs
                // "throwError".
                return throwError(err);
            })
        );
    }

    // ... Otras funciones
}
```

## Uso en un componente

Para hacer búsquedas de texto, se pueden usar uno de dos componentes en la gui, la `vista-generica` o el `buscador-paciente`. Lo recomendado es usar la `vista-generica` pues ya incluye todo lo necesario para hacer una vista nueva, pero en caso de que se requiera, en esta explicación se usará el `buscador-paciente`.

En el módulo del componente que estamos creando, importar el módulo del buscador paciente.

```ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ElementoComponent } from './elemento.component';
import { BuscadorPacienteModule } from 'src/app/components/utiles/buscador-paciente/buscador-paciente.module';

@NgModule({
    declarations: [ElementoComponent],
    imports: [CommonModule, BuscadorPacienteModule],
    exports: [ElementoComponent]
})
export class ElementoModule {}
```

Luego, en la vista (`.html`) de nuestro componente, poner el siguiente selector con las siguientes propiedades

```html
<app-buscador-paciente
    [tiempoDeEspera]="1000"
    [cbObservable]="buscadorPorTermino"
    [debug]="false"
    [placeholder]="'Buscar elementos...'"
    [enModal]="false"
    [enMovil]="false"
    (resultado)="resultadosDeBusqeuda($event)"
    (cancelado)="cancelado()"
    (error)="error()"
></app-buscador-paciente>
```

Explicación de las propiedades del selector:

| PROPIEDAD          | I/O    | TIPO       | DESCRIPCIÓN                                                                                                                                                                                            |
| ------------------ | ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `[tiempoDeEspera]` | INPUT  | `number`   | Son los milisegundos que el componente espera después de la última presión de tecla para realizar la búsqueda. Si se vuelve a escribir algo antes de que el tiempo se termine, se reinica el contador. |
| `[cbObservable]`   | INPUT  | `function` | Es una función que debe retornar un observable de `rxjs`. Por lo general, sería retornar la llamada de la función de búsqueda del `service.ts` correspondiente.                                        |
| `[debug]`          | INPUT  | `boolean`  | Si se activa, se muestra un recuadro con los valores de la clase del componente.                                                                                                                       |
| `[placeholder]`    | INPUT  | `string`   | Es el mensaje que se va a mostrar en el input en el que escribe el usuario.                                                                                                                            |
| `[enModal]`        | INPUT  | `boolean`  | Activar esta opción si el buscador está en un modal, para estilizarlo acorde a.                                                                                                                        |
| `[enMovil]`        | INPUT  | `boolean`  | Activar esta opción cuando se desee pasar al modo móvil. Por lo general se usa una utilidad que detecta el tamaño de la pantalla.                                                                      |
| `(resultado)`      | OUTPUT | `any`      | Emite el resultado de la búsqueda al usar la función del servicio provehída.                                                                                                                           |
| `(cancelado)`      | OUTPUT | `void`     | Emite un valor vacío cuando se cancela la búsqueda (se borra el texto). Esta pensado para llamar una función cuando esto pasa.                                                                         |
| `(error)`          | OUTPUT | `void`     | Emite un valor vacío cuando la búsqueda da error. Esta pensado para llamar una función cuando esto pasa.                                                                                               |

Y en el controlador (`.ts`) basarse en lo siguiente.

```ts
import { Component } from '@angular/core';
import { Paginacion } from 'src/app/utils/paginacion.util';
import { iPaginadorData } from 'src/app/components/utiles/paginador/paginador.component';
import { ElementoService } from '.../elemento.service';
import { Elemento } from '.../elemento.model';

@Component({
    selector: 'elemento',
    templateUrl: './elemento.html',
    styleUrls: ['./elemento.css']
}) {
    constructor(
        private elementoService: ElementoService
    ) {}

    hayCargaEnProgreso: boolean = false;
    terminoBusqueda?: string;
    paginacion: Paginacion = new Paginacion(5, 0, -1, '_id');
    filtro: any = {};
    totalElementos: number = 0;
    elementos: Elemento[] = [];

    // ... Cosas varias del componente

    buscadorPorTermino = (termino: string) => {
        this.hayCargaEnProgreso = true;
        this.terminoBusqueda = termino;
        return this.elementoService.obtener(
            this.paginacion,
            this.terminoBusqueda,
            this.filtro,
        );
    }

    resultadosDeBusqueda(datos: Elemento[]) {
        this.totalElementos = this.elementoService.TOTAL_ELEMENTOS;
        this.elementos = datos;

        // En caso de estar usando la tabla genérica.
        this.crearTablaGenerica();
    }

    cancelado() {
        // Funcion de busqueda por paginación.
        this.encontrarElementos();
        delete this.terminoBusqueda
    }

    error() {

        // Funcion de busqueda por paginación.
        this.encontrarElementos();
    }

    // ... Cosas varias del componente
}
```
