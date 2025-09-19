# Carrusel de imágenes genérico

Este componente es para mostrar las imágenes que pueda tener referenciadas un documento.

Para usarlo, incluir en el módulo del componente que se esté creando el módulo del carrusel.

```ts
@NgModule({
    declarations: [unComponenteComponent],
    imports: [
        CommonModule,
        CarruselImagenesGenericoModule
        // ...
    ],
    exports: [unComponenteComponent]
})
export class unComponenteModule {}
```

Y en la vista `.html` del componente, usar el siguiente selector.

```html
<app-carrusel-imagenes-generico
    [imagenes]="documentoTal.imagenes"
    [tipo]="imagenesService.TIPOS_DE_IMAGENES.__procesoMetalizado_recetas"
    [usarNuevo]="true"
    [mostrarFecha]="true"
    [mostrarTitulo]="true"
    [tamTituloSinImagenes]="'h1'"
    [tituloSinImagenes]="'No hay ninguna imágen'"
    [ancho-xl]="'20vw'"
    [alto-xl]="'20vw'"
    [ancho-lg]="'25vw'"
    [alto-lg]="'25vw'"
    [ancho-md]="'35vw'"
    [alto-md]="'35vw'"
    [ancho-sm]="'40vw'"
    [alto-sm]="'40vw'"
    [ancho-xs]="'60vw'"
    [alto-xs]="'60vw'"
></app-carrusel-imagenes-generico>
```

Explicación de los atributos del componente.

| PROPIEDAD                | OPCIONAL | TIPO    | VALORES ACEPTADOS                                                                                        | DESCRIPCIÓN                                                                                                                                                                    |
| ------------------------ | -------- | ------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `[imagenes]`             | NO       | array   | Arreglo del tipo `{imagen: string, fecha: Date}[]`                                                       | El arreglo de objetos que incluyen el nombre de las imágenes a mostrar.                                                                                                        |
| `[tipo]`                 | NO       | string  | Alguno de los valores especificados en `TIPOS_DE_IMAGENES` en el servicio `visor-de-imagenes.service.ts` | Indica el tipo de imágen que se está mostrando. Esto le indica al API en qué directorio buscar.                                                                                |
| `[usarNuevo]`            | NO       | boolean | `true`, `false`                                                                                          | Si se pone como `false`, permite usar una versión anterior. En nuevas implementaciones usarlo con `true`.                                                                      |
| `[mostrarFecha]`         | SI       | boolean | `true`, `false`                                                                                          | <span style='color: red; font-weight: 900;'>DEPRECADO</span> Solo funciona con la versión anterior. Muestra la fecha de la imágen.                                             |
| `[mostrarTitulo]`        | SI       | boolean | `true`, `false`                                                                                          | <span style='color: red; font-weight: 900;'>DEPRECADO</span> Solo funciona con la versión anterior. Muestra un título genérico para la imágen, pero no hay forma de cambiarlo. |
| `[tamTituloSinImagenes]` | SI       | string  | `'h1'`, `'h2'`, `'h3'`, `'h4'`, `'h5'`, `'h6'`                                                           | Indica el tamaño del título que se muestra si no hay imágenes.                                                                                                                 |
| `[tituloSinImagenes]`    | SI       | string  | Cualquier cadena de texto.                                                                               | Es el texto que se mostrará como título cuando no hay imágenes en el arreglo.                                                                                                  |
| `[ancho-xl]`             | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El ancho del recuadro de imágenes cuando la pantalla es de `1200px` o más.                                                                                                     |
| `[alto-xl]`              | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El alto del recuadro de imágenes cuando la pantalla es de `1200px` o más.                                                                                                      |
| `[ancho-lg]`             | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El ancho del recuadro de imágenes cuando la pantalla es de `992px` a `1199px`.                                                                                                 |
| `[alto-lg]`              | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El alto del recuadro de imágenes cuando la pantalla es de `992px` a `1199px`.                                                                                                  |
| `[ancho-md]`             | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El ancho del recuadro de imágenes cuando la pantalla es de `768px` a `991px`.                                                                                                  |
| `[alto-md]`              | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El alto del recuadro de imágenes cuando la pantalla es de `768px` a `991px`.                                                                                                   |
| `[ancho-sm]`             | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El ancho del recuadro de imágenes cuando la pantalla es de `576px` a `768px`.                                                                                                  |
| `[alto-sm]`              | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El alto del recuadro de imágenes cuando la pantalla es de `576px` a `768px`.                                                                                                   |
| `[ancho-xs]`             | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El ancho del recuadro de imágenes cuando la pantalla es de `0px` a `575px`.                                                                                                    |
| `[alto-xs]`              | SI       | string  | [Cualquier unidad de dimensión css](./docs/carrduci-sys-desarrollo/css/valores-dimensiones-css.md).      | El alto del recuadro de imágenes cuando la pantalla es de `0px` a `575px`.                                                                                                     |

El atributo `[imagenes]` espera un arreglo como el siguiente. Por lo menos con el campo `imagen`.

```json
[
    {
        "imagen": "68b7177c9604860034477176-1756829798869_8555.png",
        "fecha": "2025-09-02T16:16:40.072Z"
    },
    {
        "imagen": "68b7177c9604860034477176-1756829799874_6352.png",
        "fecha": "2025-09-02T16:16:40.072Z"
    }
]
```

Este es un ejemplo del componente poniendo `[usarNuevo]` como `true` (que es el que se debe usar):

![](../../../assets/gifs/componentes__carrusel_imagenes_generico_nuevo.gif)

Cuando se da click en la imágen actual, se abre un visualizador que permite hacer zoom con la rueda del ratón.

![](../../../assets/gifs/componentes__carrusel_imagenes_generico_visor.gif)

Y así se ve la versión <span style="color: red; font-weight: 900">deprecada</span>, que aún se usa en algunas partes del sistema. Como se nota, se redimensiona al tamaño de cada imágen.

![](../../../assets/gifs/componentes__carrusel_imagenes_generico_antiguo.gif)
