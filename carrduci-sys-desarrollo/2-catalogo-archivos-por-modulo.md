### [< Directorio](../directorio.md)

# Explicación de los nombres (GUI)
#docs #catalogo

Este catálogo busca asistir la búsqueda de archivos que se requieren tener en cuenta para modificar los componentes de la interfaz (GUI) de CARRDUCIsys.

>La separación del catálogo se basa en los apartados y títulos de la barra lateral del sistema, que es el único punto de acceso para los usuarios. Los demás componentes y servicios de utilidades se listan por separado

Los componentes en angular se basan en el modelo `VISTA - CONTROLADOR`, y usan una notación para nombrar los archivos:

```
<nombre_componente>.component.<extension>
```

Ejemplo de archivos varios de un componente. Aquí se incluye el modulo, que es otro tipo de archivo, porque se tiene la intención de que cada componente tenga su módulo (más adelante que sean standalone).

``` 
    CONTROLADOR:  unComponente.component.ts
    VISTA:        unComponente.component.html
    HOJA ESTILOS: unComponente.component.css
    PRUEBAS:      unComponente.component.spec.ts
    -----------------------------------------------
    MODULO:       unComponente.module.ts
```

En este índice se usara solo el nombre antes del primer punto, para que se puedan buscar componentes, módulos, servicios y modelos.

Hay tres tipos de archivos más, el `model`, el `service` y el `parametrosIndexacion`. El `model` es para poner las clases e interfaces que servirán para modelar los datos que se reciban desde el api, el `service` es para poner todas las funciones que nos sirvan para transferir datos o calcularos, por ejemplo, las funciones que consultan al api, o cálculos específicos como el estatus de algo y por lo general se relacionan con un modelo (comparten nombre), pero se pueden nombrar como la situación lo demande. y el `parametrosIndexacion` es para guardar un objeto que le indica a un indexador que hay en el sistema cómo indexar alguna colección de MongoDB en específico.

```
    MODELO: usuario.model.ts
    SERVICIO: usuario.service.ts
    PARAMETROS INDEXACION: usuario.parametrosIndexacion.ts
```


# Explicación de los nombres (API)

# Índice basado en el menú lateral
