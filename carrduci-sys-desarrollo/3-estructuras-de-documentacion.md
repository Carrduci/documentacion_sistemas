### [< Directorio](../directorio.md)
# Estructuras para documentar el CARRDUCIsys
#docs #estandar
Para documentar, se sugiere usar ciertas estructuras y métodos para mantener persistente la forma en la que se hace. La siguiente es una lista de casos en los cuales usar ciertos comentarios y procedimientos; lo más fácil sería usarlos en Visual Studio Code, en forma de [snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets).

Ver [agregar snippets a visual studio code](../visual-studio-code/1-agregar-snippets.md).

Modificar snippets como se desee.
## Establecimientos

1. Siempre preferir comentario de bloque sobre comentario de línea; este es fácilmente escalable, es decir, puede crecer hacia abajo sin tener que agregar caracteres. En caso de comentar variables, funciones, clases, etc., usar comentario [JSDoc](https://jsdoc.app/), en Visual Studio Code, IntelliSense va a mostrar lo que este dentro del comentario al hacer hover sobre alguna referencia a lo que se comentó.
2. Los comentarios siempre van arriba de la línea o el bloque de líneas a la/s que se hace referencia, no a un lado.
3. Opcionalmente se puede agregar un espacio antes del comentario y otro luego de la línea o bloque de líneas que se comenta, para dar a entender que el comentario es para esa línea o bloque.
4. Nunca usar acentos ni caracteres como la **ñ** en la documentación que se hace en el mismo código. Los caracteres especiales si son permitidos, pero solo los que ya se usan en el lenguaje de programación.
5. Usar el separador de sección mostrado en el apartado **Estructuras Generales (snippets)** y poner el código entre las estructuras resultantes cuando se indique que se debe seguir un orden de secciones. A manera de sub-secciones, se puede usar el separador de línea dentro del separador de sección.
## Estructuras Generales (snippets)
### 1. Separador de sección
#### TypeScript, JavaScript
```
    "Separador de seccion": {
        "prefix": "__separador-seccion",
        "body": [
            "// (o==================================================================o)",
            "//   #region ${1:TITULO SECCION}",
            "// (o-----------------------------------------------------------\\/-----o)",
            "",
            "${0:}",
            "",
            "// (o-----------------------------------------------------------/\\-----o)",
            "//   #endregion ${1:TITULO SECCION}",
            "// (o==================================================================o)",
        ],
        "description": "Grandes marcadores de sección."
    },
```
#### HTML
```
    "Separador de seccion": {
        "prefix": "__separador-seccion",
        "body": [
            "<!--===============================================================-->",
            "<!-- #region #MARK: ${1:TITULO SECCION} -->",
            "<!-----------------------------------------------------------\\/------>",
            "",
            "${0:}",
            "",
            "<!-----------------------------------------------------------/\\------>",
            "<!-- #endregion ${1:TITULO SECCION} -->",
            "<!--===============================================================-->",
        ],
        "description": "Grandes marcadores de sección."
    },
```
#### Python
```
    "Section markers": {
        "prefix": "__separador-seccion",
        "body": [
            "# (o==================================================================o)",
            "#   #region ${1:TITULO SECCION}",
            "# (o-----------------------------------------------------------\\/-----o)",
            "",
            "${0:}",
            "",
            "# (o-----------------------------------------------------------/\\-----o)",
            "#   #endregion ${1:TITULO SECCION}",
            "# (o==================================================================o)",
        ],
        "description": "Grandes marcadores de sección."
    },
```
### 2. Separadores de línea
#### TypeScript, JavaScript
```
    "Separador de linea": {
        "prefix": "__separador-linea",
        "body": [
            "// (o-----------------------------------------( ${1:TITULO} ))",
            "${0:}"
        ],
        "description": "Pequeño separador de una línea."
    }
```
#### HTML
```
    "Separador de linea": {
        "prefix": "__separador-linea",
        "body": [
            "<!-----------------------------------------( ${1:TITULO} ))-->",
            "${0:}"
        ],
        "description": "Pequeño separador de una línea."
    }
```
#### Python
```
    "Separador de linea": {
        "prefix": "__separador-linea",
        "body": [
            "# (o-----------------------------------------( ${1:TITULO} ))",
            "${0:}"
        ],
        "description": "Pequeño separador de una línea."
    }
```

## Estructuras para el API (snippets y procedimientos)
### Para documentar modelos (esquemas de mongo) del API
Los archivos del API están hechos en JavaScript, por lo que las snippets que se listen a continuación se deben agregar en el `javascript.json`.

Acomodar todos los elementos de manera seccionado en el orden en el que se muestran los títulos siguientes.
#### 1. Importaciones

Siempre comentar y separar el área de importaciones. Las importaciones Isiempre deben ir hasta arriba y se deben separar, preferentemente de la siguiente manera.

| ORDEN | DESCRIPCIÓN                                                         | COMENTARIO PARA AGREGAR        |
| ----- | ------------------------------------------------------------------- | ------------------------------ |
| 1     | Importaciones externas (librerías).                                 | `/* IMPORTACIONES EXTERNAS */` |
| 2     | Importaciones de modelos o esquemas desde otros archivos de modelo. | `/* OTROS MODELOS */`          |
| 3     | Importaciones de servicios internos.                                | `/* SERVICIOS */`              |
| 4     | Importaciones de utilidades internas, middlewares, etc.             | `/* UTILIDADES */`             |
#### 2. Esquema
Usar la siguiente snippet para poner un comentario arriba de la declaración del esquema:
```
    "Documentacion modelo API": {
        "prefix": "__doc_api_modelo",
        "body": [
            "/** -----------------------------------------------------",
            "  - NOMBRE: `${1:NOMBRE ESQUEMA}`",
            "  - Fecha documentacion: $CURRENT_DATE, $CURRENT_MONTH_NAME $CURRENT_YEAR",
            "  - Archivo: $RELATIVE_FILEPATH",
            "",
            "  - Descripcion:",
            "  ${0:DESCRIPCION}",
            "----------------------------------------------------- */",
        ],
        "description": "Un esquema o modelo de Mongo"
    },
```
Se ve así (usando un ejemplo):
```
/** -----------------------------------------------------
  - NOMBRE: `Modelo Schema`
  - Fecha documentacion: 16, July 2024
  - Archivo: models/modelo.js
  
  - Descripcion:
  Es para dar nombre a una de las partes del SKU. El
  modelo determinad la numeracion inicial o nombre del
  SKU, que podria servir como metodo rapido de
  identificacion.
----------------------------------------------------- */
```
Los campos del modelo serán documentados con comentarios de JSDoc, sin estructura específica.

#### 3. Plugins, métodos, validadores
Usar el comentario de bloque. No hay una estructura definida.
#### 4. Middleware
Usar el comentario JSDoc. No hay una estructura definida.
#### 5. Exportaciones
En este nivel (fuera de la instancia del esquema) se **DEBE** generar la instancia del modelo de mongoose, preferiblemente en una constante, ejemplo:
```
const MODELO_SCHEMA = mongoose.model('Modelo', modeloSchema)
```
> **ADVERTENCIA: ** Es muy importante que la instancia se genere en este nivel y no en NINGÚN otro. Hacerlo en otro puede ocasionar errores extraños.

Aquí es donde se exporta la instancia del modelo de mongoose generada. Como en el API se usa JavaScript, las exportaciones son del modo:
```
module.exports = ALGO
```
Si se desea comentar, usar comentario de bloque