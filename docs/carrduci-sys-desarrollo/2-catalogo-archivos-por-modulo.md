# Explicación de los nombres (GUI)

#docs #catalogo

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
    PRUEBAS:      unComponente.component.spec.ts
    -----------------------------------------------
    MODULO:       unComponente.module.ts
```

> ! Lo ideal es que todos los componentes tengan su módulo, pero como la implementación de esto comenzó en una etapa tardía del sistema, no todos lo tienen. Muchos componentes están agrupados en un módulo compartido o en el módulo general de `pages.module.ts`.

Hay dos tipos de archivos más, el `model`, el `service`. El `model` es para poner las clases e interfaces que servirán para modelar los datos que se reciban desde el api, el `service` es para poner todas las funciones que nos sirvan para transferir datos o calcularlos, por ejemplo, las funciones que consultan al api, o cálculos específicos como el estatus de algo y por lo general se relacionan con un modelo (comparten nombre), pero se pueden nombrar como la situación lo demande.

```
    MODELO: usuario.model.ts
    SERVICIO: usuario.service.ts
```

# Explicación de los nombres (API)

## PENDIENTE

# Índice de archivos

Este índice servirá para identificar qué componentes (y sus archivos) pertenecen

[Catálogo completo en esta dirección.](https://docs.google.com/spreadsheets/d/1Avh_WMtHkZquh4DFFig7k7eYxV8H9e3UFMLI6xUjikY/edit?gid=2022342688#gid=2022342688)
