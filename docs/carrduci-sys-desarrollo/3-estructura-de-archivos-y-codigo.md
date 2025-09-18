# Estructura GUI

Este catálogo busca asistir la búsqueda de archivos que se requieren tener en cuenta para modificar los componentes de la interfaz (GUI) de CARRDUCIsys.

> La separación del catálogo se basa en los apartados y títulos de la barra lateral del sistema, que es el único punto de acceso para los usuarios. Los demás componentes y servicios de utilidades se listan por separado

Los componentes en angular usan una notación para identificar los archivos:

```
<nombre_componente>.<sufijo>.<extension>
```

Ejemplo de archivos varios de un componente. Aquí se incluye el modulo, que es otro tipo de archivo, porque se tiene la intención de que cada componente tenga su módulo (más adelante que sean standalone).

```
    CONTROLADOR:  unComponente.component.ts
    VISTA:        unComponente.component.html
    HOJA ESTILOS: unComponente.component.css
    PRUEBAS UNIT: unComponente.component.spec.ts
    MODULO:       unComponente.module.ts
```

!> Lo ideal es que todos los componentes tengan su módulo, pero como la implementación de esto comenzó en una etapa tardía del sistema, no todos lo tienen. Muchos componentes están agrupados en un módulo compartido o en el módulo general de `pages.module.ts`.

Hay varios tipos de archivos más, el `model`, el `service`, `pipe`, `directive` y `routes`.

```
    MODELO:       unNombre.model.ts
    SERVICIO:     unNombre.service.ts
    PIPE:         unNombre.pipe.ts
    DIRECTIVA:    unNombre.directive.ts
    RUTAS:        unNombre.routes.ts
```

El `model` es para poner las clases e interfaces que servirán para modelar los datos que se reciban desde el api.

El `service` es para poner todas las funciones que nos sirvan para transferir datos o calcularlos, por ejemplo, las funciones que consultan al api, o cálculos específicos como el estatus de algo y por lo general se relacionan con un modelo (comparten nombre), pero se pueden nombrar como la situación lo demande.

Los archivos `pipe` son clases que contienen una funcion especial. Estas clases se pueden llamar desde el HTML invocando el selector que tienen especificado en su decorador después de un caracter pipe `|`, y ejecutan la función especial, que se llama "transform". Un ejemplo de pipe es, en la interpolación de angular: `{{ 'nombre' | uppercase }}`, que convierte la cadena que se le pasa a una de puras mayúsculas.

Las directivas, con prefijo `directive`, son clases que tienen el proposito de agregar funcionalidades a elementos del html usando un selector css. Por ejemplo, si tenemos una directiva cuyo selector es `flotante-generico` que hace que en el elemento que se ponga se genere una ventana flotante al darle click, con el texto que se le asigne, entonces se usaría así:

```html
<button flotante-generico="Este es el detalle">Detalle</button>
```

Las rutas (`routes`) engloban las urls que darán acceso a las distintas vistas del sistema.

# Estructura API

En las aplicaciones de node y express, no hay una concesión para nombrar los archivos, pero en el API de carrduci sys se usa algo similar a la forma de Angular.

```
    RUTAS:        unNombre.routes.js
    CONTROLADOR:  unNombre.controller.js
    SERVICIO:     unNombre.service.js
    MODELO:       unNombre.model.js
    UTILES:       unNombre.utils.js
    MIDDLEWARE:   unNombre.middleware.js
    PLUGIN:       unNombre.plugin.js
```

Las `routes` guardan los endpoints de express para conectarse al api. En estas rutas se usa un middleware para definir el permiso que debe tener el usuario para usar esa ruta. Una ruta llama a su función correspondiente en el controlador. Un ejemplo de ruta es este:

```js
const APP = require('express')();
// Si, esto debería ser una archivo de middleware. Debe cambiarse
// en un futuro
const PERMISOS = require('/config/permisos.config');
const CONTROLADOR = require('./unNombre.controller');

// Observar que el callback es asíncrono
APP.post(
    '/',
    PERMISOS.funcionQueRetornaMiddleware('permiso:tal'),
    async (req, res) => await CONTROLADOR.crear(req, res)
);

module.exports = APP;
```

Los `controller` guardan las funciones que llaman las rutas. Estas funciones a su vez, llaman a las funciones correspondientes del servicio, pero manejan los errores y las respuestas usando un archivo de utilidades llamado `response.utils.js`. También pueden tener lógica que decida entre cuál función del servicio usar. Este es un ejemplo:

```js
const SERVICIO = require('../../services/unNombre/unNombre.service');
const { response } = require('../../../utiles/response.utiles');

const CONTROLADOR = {};

// Observar que la función es asíncrona.
CONTROLADOR.crear = async function (req, res) {
    try {
        // Puede cambiar según se requiera.
        const BODY = {
            ...req.params,
            ...req.body,
            idUsuario: req.user._id // El objeto request incluye el usuario actual.
        };

        // Puede retornar diferentes estructuras según se requiera.
        const respuesta = await SERVICIO.crear(BODY);

        return new response(res, __filename, {
            datos: respuesta,
            mensaje: 'Elemento creado',
            total: 0 // En caso de que la respuesta tenga varios elementos.
        })._201_created(); // Si no se está creando un elemento, usar _200_ok().
    } catch (error) {
        return new response(res, __filename, {
            error: error,
            mensaje: 'Error al crear'
        })._422_unprocessable();
    }
};

module.exports = CONTROLADOR;
```

Los `service` se encargan de toda la lógica del API. Originalmente las funciones de los servicios recibían el objeto `req` (request) y `res` (response) en sus parametros, pero eso tiene que ir cambiando, ya que solo deben tener en sus parámetros los que requieren para ejecutar so lógica, por ejemplo, un nombre, el id del usuario que ejecuta la ruta (esto casi siempre va a ser el caso, pues este es requerido para generar registros de historial), etc. Así se vería uno:

```js
const Mongoose = require('mongoose');
const ObjectId = Mongoose.Types.ObjectId; // Esto es para generar instancias de ObjectId, los ids que usa mongo para sus modelos.
const MODELO = require('../../models/unNombre/unNombre.model');

const SERVICIO = {};

// Usar asignación por desestructuración en los parámetros de la función,
// para así poder pasar un objeto y que la función solo tome lo que necesita,
// en cualquier orden.
SERVICIO.crear = async function ({ nombre, descripcion, idUsuario }) {
    let nuevoElemento = new MODELO({
        nombre: nombre,
        descripcion: descripcion
    });

    // Así se especifican los datos del historial cuando se crea un elemento.
    nuevoElemento.metadata = {
        idUsuario: idUsuario,
        descripcion: 'Elmento creado'
    };

    // Así se guarda en la BD
    return await nuevoElemento.save();
};

module.exports = SERVICIO;
```

# Índice de archivos

Este índice servirá para identificar a qué componentes pertenecen los archivos (necesitas tener una cuenta de google con acceso al catálogo).

[Catálogo completo en esta dirección.](https://docs.google.com/spreadsheets/d/1Avh_WMtHkZquh4DFFig7k7eYxV8H9e3UFMLI6xUjikY/edit?gid=2022342688#gid=2022342688)
