# Carga de imágenes

La carga de imágenes implica el uso de un componente en la GUI y un servicio en el API.

## Componente de la GUI.

Para usar el input de carga de imágenes, importarlo en el módulo del componente en el que se está trabajando.

```ts
import {CalendarioGenericoModule} from 'src/app/components/utiles/calendario-generico/calendario-generico.module';

@NgModule(
    {
        declarations: [TalComponenteComponent],
        imports: [
            CommonModule,
            CalendarioGenericoModule,
        ],
        export: [TalComponenteComponent],
    }
)
export class TalComponenteModule {
}
```

Y usar el componente de la siguiente manera. En la vista (`.html`) llamar al selector así.

```angular17html

<app-carga-de-imagenes
        [transformarFileAObjetoPlano]="true"
        [limiteImagenes]="3"
        (imagenesParaSubir)="datosImagenes($event)"
        (error)="errorImagenes($event)"
></app-carga-de-imagenes>
```

En el controlador (`.ts`) estarían las siguientes funciones:

```ts
import {Component} from "@angular/core";
import {CargaDeImagenesTransporte} from "./carga-de-imagenes-transporte";

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
|:--------------------------------|:-------|:------------------------------|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
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

## Servicio del API

