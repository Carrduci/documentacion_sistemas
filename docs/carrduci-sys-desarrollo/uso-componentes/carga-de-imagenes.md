# Carga de imágenes

La carga de imágenes implica el uso de un componente en la GUI y un servicio en el API.

<hr class='hr-secundario'>

## Componente de la GUI.

Para usar el input de carga de imágenes, importarlo en el módulo del componente en el que se está trabajando.

```ts
import { CalendarioGenericoModule } from 'src/app/components/utiles/calendario-generico/calendario-generico.module';

@NgModule({
    declarations: [TalComponenteComponent],
    imports: [CommonModule, CalendarioGenericoModule],
    export: [TalComponenteComponent]
})
export class TalComponenteModule {}
```

Y usar el componente de la siguiente manera. En la vista (`.html`) llamar al selector así.

```html
<app-carga-de-imagenes
    [transformarFileAObjetoPlano]="true"
    [limiteImagenes]="3"
    (imagenesParaSubir)="datosImagenes($event)"
    (error)="errorImagenes($event)"
></app-carga-de-imagenes>
```

En el controlador (`.ts`) estarían las siguientes funciones:

```ts
import { Component } from '@angular/core';
import { CargaDeImagenesTransporte } from './carga-de-imagenes-transporte';

@Component({
    // ...
})
class TalCmponent {
    // ...

    datosImagenes(imagenes: CargaDeImagenesTransporte[]) {
        console.log(imagenes);
    }

    errorImagenes(err: any) {
        console.log(err);
    }
}
```

Explicación de las propiedades:

| PROPIEDAD                       | I/O    | TIPO                          | VALORES ACEPTADOS                                                       | DESCRIPCIÓN                                                                                                                           |
| :------------------------------ | :----- | :---------------------------- | :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| `[activeColor]`                 | INPUT  | string                        | Cadena para [color](./docs/carrduci-sys-desarrollo/css/colores-css.md). | <span class='text-warning'>NO USADO</span>                                                                                            |
| `[baseColor]`                   | INPUT  | string                        | Cadena para [color](./docs/carrduci-sys-desarrollo/css/colores-css.md). | Cambia el color del recuadro y símbolo del recuadro de carga de imágenes.                                                             |
| `[overlayColor]`                | INPUT  | string                        | Cadena para [color](./docs/carrduci-sys-desarrollo/css/colores-css.md). | <span class='text-warning'>NO USADO</span>                                                                                            |
| `[multiple]`                    | INPUT  | boolean                       | `true`, `false`. Por defecto `true`.                                    | Si es verdadero, se permite seleccionar varias imágenes.                                                                              |
| `[limiteImagenes]`              | INPUT  | number                        | Número del 1 en adelante.                                               | Si es múltiple, limita la cantidad de imágenes seleccionables. <span class='text-info'>SE RECOMIENDA SIEMPRE USAR ESTA OPCIÓN</span>. |
| `[transformarFileAObjetoPlano]` | INPUT  | boolean                       | `true`, `false`                                                         | Convierte el objeto de la imágen a un JSON plano. <span class='text-info'>SE RECOMIENDA SIEMPRE USAR ESTA OPCIÓN</span>.              |
| `(error)`                       | OUTPUT | string                        |                                                                         | Emite una cadena de texto describiendo posibles errores.                                                                              |
| `(imagenesParaSubir)`           | OUTPUT | `CargaDeImagenesTransporte[]` |                                                                         | Emite un objeto o un arreglo de objetos que describen la imágen.                                                                      |
| `(esteComponente)`              | OUTPUT | `CargaDeImagenesComponent`    |                                                                         | Emite la clase misma del componente por si se desea acceder a sus métodos o propiedades.                                              |

Este es un ejemplo visual del componente.

<figure>
  <img src="../../../assets/gifs/componentes__carga_de_imagenes.gif" alt="radio">
  <figcaption>No se pueden cargar más imágenes de las permitidas</figcaption>
</figure>

Y este es un ejemplo de arreglo que el componente emite:

```json
[
    {
        "file": {
            "lastModified": 1711491528372,
            "name": "660791 - copia.jpg",
            "size": 377638,
            "type": "image/jpeg",
            "webkitRelativePath": ""
        },
        "src": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQg..."
    },
    {
        "file": {
            "lastModified": 1711491999000,
            "name": "45412.jpg",
            "size": 2540812,
            "type": "image/jpeg",
            "webkitRelativePath": ""
        },
        "src": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIB..."
    },
    {
        "file": {
            "lastModified": 1741722504615,
            "name": "aurora-borealis-beautiful-4k-2c.jpg",
            "size": 2526714,
            "type": "image/jpeg",
            "webkitRelativePath": ""
        },
        "src": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEBLAEsAAD/4SXqRXhpZgAASUkqAAgAAAANAA4BA..."
    }
]
```

Este objeto debe ser pasado a un servicio que acepte un objeto con un campo de imágenes parecido al siguiente.

```ts
import {CargaDeImagenesTransporte} from "./carga-de-imagenes-transporte";

export class UnModeloCualquiera {
    // ...
    imagenes: CargaDeImagenesTransporte[]

    // ...

    constructor(params: ParamsUnModeloCualquiera) {
        /...
    }
}

export interface ParamsUnModeloCualquiera {
    // ...
    imagenes: CargaDeImagenesTransporte[]
    // ...
}
```

y en el servicio se debe esperar recibir esta misma clase

```ts
import { Injectable } from '@angular/core';

@Injectable({
    // ...
})
class AlgunServicioService {
    crearDocumentoConImagenes(documento: UnModeloCualquiera) {
        // ...
    }
}
```

<hr class='hr-secundario'>

## Crear un tipo de imágen

Las imágenes se clasifican por tipo, dependiendo de a qué módulo están relacionadas.

Para guardar imágenes de un nuevo tipo, hay que registrarlo en varios lugares.

Suponiendo que se tiene el siguiente modelo en el API.

```js
/* IMPORTACIONES EXTERNAS */
const Mongoose = require('mongoose');
const Schema = Mongoose.Schema;
const ObjectId = Schema.Types.ObjectId;
const UNIQUE_VALIDATOR = require('mongoose-unique-validator');
const AUTO_INCREMENT = require('mongoose-sequence')(Mongoose);

/* UTILIDADES */
const HISTORIAL = require('.../plugins/historial/historial.plugin');
const BUSQUEDA = require('.../plugins/busqueda-texto/busqueda-texto.plugin');
const UTILES = require('.../utils/varios');
const CAMPOS_BUSQUEDA = require('.../utils/camposBusquedaTodosLosModelos.utils');

const UN_ELEMENTO_SCHEMA = Mogoose.Schema(
    {
        folio: {
            type: Number,
            unique: true,
            inmutable: true,
            min: [0, 'El mínimo posible del folio es 0']
        },
        busqueda: String,

        nombre: String,
        descripcion: String,
        imagenes: [
            {
                fecha: Date,
                imagen: String
            }
        ]
    },
    {
        collection: 'elementos',
        timestamps: true
    }
);

UN_ELEMENTO_SCHEMA.plugin(AUTO_INCREMENT, {
    id: 'elemento',
    inc_field: 'folio'
});
UN_ELEMENTO_SCHEMA.plugin(UNIQUE_VALIDATOR, {
    message: "El campo '{PATH}' debe ser único."
});
UN_ELEMENTO_SCHEMA.plugin(BUSQUEDA.text_search_index, {
    fields: CAMPOS_BUSQUEDA.ELEMENTOS
});
UN_ELEMENTO_SCHEMA.plugin(HISTORIAL.hystory_log_plugin);

const ELEMENTO_MODEL = Mongoose.model('Elemento', UN_ELEMENTO_SCHEMA);
module.exports = ELEMENTO_MODEL;
ELEMENTO_MODEL.createCollection();
```

### 1. En el servicio de imágenes (API)

En el archivo `imagenesAdministracion.service.js` es el primer lugar donde agregar el nuevo tipo.

```js
// ...

const SERVICIO = {};

SERVICIO.RELACION_CARPETAS_COLECCIONES = {
    // ...

    // La relación de la carpeta del nuevo tipo con su coleccion.
    // Aquí se usa el nombre de la colección del modelo mencionado anteriormente.
    elementos: 'elementos'
};

// No tocar esto
SERVICIO.DIRECTORIO_IMGS = '/carrduci-sys-app-data/uploads';

SERVICIO.DIRECTORIOS_IMAGENES = {
    // ...

    // El nombre de la carpeta que se usara.
    elementos: `${SERVICIO.DIRECTORIO_IMGS}/elementos`
};

SERVICIO.TIPOS = {
    // ...

    // El nombre dle nuevo tipo.
    elementos: 'elementos'
};

// ...
```

###

<hr class='hr-secundario'>

## Uso del servicio del API

### Guardar imágenes

En el API, suponiendo que ya está lista una ruta y un controlador, hay que crear el documento y guardar las imágenes de
la siguiente forma.

```javascript
const SERVICIO_IMAGENES = require('/services/imagenesAdministracion/imagenesAdministracion.service.js');

const SERVICIO = {};

SERVICIO.crearDocumentoConImagenes = async function ({
    nombre,
    descripcion,
    imagenes
}) {
    let imagenesGuardadas = [];
    if (imagenes.length > 0) {
        imagenesGuardadas = await SERVICIO_IMAGENES.cargarGrupoDeImagenes(
            imagenes
            // SERVICIO_IMAGENES.TIPOS.
        );
    }
};
```

### Eliminar imágenes
