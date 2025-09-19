# Auto increment

Este es un componente del API y es más concretamente un plugin. Es una librería llamada `mongoose-sequence`. Sirve para agregar una serie a los documentos de una colección, es decir, que tengan un consecutivo.

Para usarlo, en el modelo del API que se desa aplicar, poner la siguiente importación.

```js
const Mongoose = require('mongoose');
const AutoIncrement = require('mongoose-sequence')(Mongoose);
```

Y luego, bajo de la declaración del esquema, hay que agregar el plugin.

```js
const SCHEMA = Mongoose.Schema(
    {
        folio: {
            type: Number,
            unique: true
        }

        // ... campos del schema
    },
    {
        timestamps: true,
        collection: 'unaColeccion'
    }
);

// Esta es la implementación del plugin.
SCHEMA.index(AutoIncrement, {
    id: 'folio_elemento',
    inc_field: 'folio'
});
```

Esto va a generar una colección (si no existe) llamada `counters`. Cuando se cree el primer documento de la colección `unaColeccion` se creará también un documento en `counters` parecido a el siguiente.

```json
{
    "_id": "5ce71f3bba659084e7b56ebd",
    "id": "folio_elemento",
    "reference_value": null,
    "seq": 1
}
```

Y el documento de `unaColeccion` tendrá el siguiente valor en el campo `folio`.

```json
{
    "_id": "65abdf30886e34dcdb7308ff",
    "folio": 1

    // ... campos del documento
}
```

Para ver la documentación completa, dirigirse [aquí](https://www.npmjs.com/package/mongoose-sequence/v/5.2.2).

## Servicio de counters

?> Este proceso se puede hacer aunque el counter (plugin) no esté agregado a un modelo, es decir, se puede crear un counter sin referencia en ningún esquema, pero solo podrá ser usado a través del servicio.

También se puede usar un servicio que permite incrementar manualmente los contadores la cantidad que se desee.

Usando el counter del ejemplo anterior para demostrar su uso con el servicio, lo agregaremos a los counters permitidos en el archivo `counters.service.js`, buscando al inicio del archivo la propiedad `servicio.COUNTERS_MODIFICABLES`.

```js
// ...

const servicio = {};

servicio.COUNTERS_MODIFICABLES = {
    // ...

    // Agregar al final del objeto. Usar el mismo nombre
    // tanto para la llave como para el valor.
    folio_elemento: 'folio_elemento'
};

// ...
```

Luego, para incrementar, llamar a la función `usarCounter` donde se requiera.

```js
// La importación puede variar. Los "..." son solo demostrativos.
const SERVICIO_COUNTER = require('.../services/counters/counters.service');
const UN_MODELO = require('.../models/unModeloCualquiera.model');

const SERVICIO = {};

SERVICIO.operacionTal = async function ({
    // ...
    idUsuario
}) {
    // Como en el ejemplo anterior ya existe un documento que usa este
    // contador, el valor del NUEVO_FOLIO será 4.
    const NUEVO_FOLIO = await SERVICIO_COUNTER.usarCounter(
        'folio_elemento',
        undefined,
        3
    );

    const NUEVO_ELEMENTO = new UN_MODELO({
        // ...
        folio: NUEVO_FOLIO
    });

    NUEVO_ELEMENTO.metadata = {
        idUsuario,
        descripcion: 'elemento creado'
    };

    return await NUEVO_ELEMENTO.save();
};
```
