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

## PENDIENTE

# Índice basado en el menú lateral
[Catálogo completo en esta dirección.](https://docs.google.com/spreadsheets/d/1Avh_WMtHkZquh4DFFig7k7eYxV8H9e3UFMLI6xUjikY/edit?gid=2022342688#gid=2022342688)

| MENÚ                      | SUB MENÚ                            | APP | ARCHIVO                                                                       |
| ------------------------- | ----------------------------------- | --- | ----------------------------------------------------------------------------- |
|                           |                                     | GUI | styles.scss                                                                   |
|                           |                                     | GUI | app.component.ts                                                              |
|                           |                                     | GUI | app.component.html                                                            |
|                           |                                     | GUI | app.component.css                                                             |
|                           |                                     | GUI | app.module.ts                                                                 |
|                           |                                     | GUI | app.routes.ts                                                                 |
|                           |                                     | API | app.js                                                                        |
|                           |                                     | API | routes.js                                                                     |
|                           |                                     | GUI | pages.component.ts                                                            |
|                           |                                     | GUI | pages.component.html                                                          |
|                           |                                     | GUI | pages.component.css                                                           |
|                           |                                     | GUI | pages.module                                                                  |
|                           |                                     | GUI | pages.routes.ts                                                               |
|                           |                                     | GUI | nopagefound.component.ts                                                      |
|                           |                                     | GUI | nopagefound.component.html                                                    |
|                           |                                     | GUI | breadcrumbs.component.ts                                                      |
|                           |                                     | GUI | breadcrumbs.component.html                                                    |
|                           |                                     | GUI | header.component.module                                                       |
|                           |                                     | GUI | header.component.ts                                                           |
|                           |                                     | GUI | header.component.html                                                         |
|                           |                                     | GUI | header.component.css                                                          |
|                           |                                     | GUI | login.component.ts                                                            |
|                           |                                     | GUI | login.component.html                                                          |
|                           |                                     | GUI | login.component.css                                                           |
| Perfil                    | Perfil                              | GUI | profile.component.ts                                                          |
| Perfil                    | Perfil                              | GUI | profile.component.html                                                        |
| Perfil                    | Configuraciones de la cuenta        | GUI | account-settings.component.ts                                                 |
| Perfil                    | Configuraciones de la cuenta        | GUI | account-settings.component.html                                               |
| Avisos                    | Dashboard                           | GUI | dashboard.component.ts                                                        |
| Avisos                    | Dashboard                           | GUI | dashboard.component.html                                                      |
| Almacen                   | Produccion                          | GUI | almacen-produccion.component.ts                                               |
| Almacen                   | Produccion                          | GUI | almacen-produccion.component.html                                             |
| Almacen                   | Produccion                          | GUI | articulo-crear-modificar.component.ts                                         |
| Almacen                   | Produccion                          | GUI | articulo-crear-modificar.component.html                                       |
| Almacen                   | Produccion                          | GUI | articulo-detalle.component.ts                                                 |
| Almacen                   | Produccion                          | GUI | articulo-detalle.component.html                                               |
| Almacen                   | Produccion                          | GUI | reporte-es-almacen-produccion.component.ts                                    |
| Almacen                   | Produccion                          | GUI | reporte-es-almacen-produccion.component.html                                  |
| Almacen                   | Produccion                          | GUI | articulo-detalle-imprimir.component.ts                                        |
| Almacen                   | Produccion                          | GUI | articulo-detalle-imprimir.component.html                                      |
| Almacen                   | Produccion                          | GUI | articulo-detalle-imprimir.component.css                                       |
| Almacen                   | Almacen - ES                        | GUI | almacen-es.component.ts                                                       |
| Almacen                   | Almacen - ES                        | GUI | almacen-es.component.html                                                     |
| Almacen                   | Almacen - ES                        | GUI | almacen-es.component.css                                                      |
| Almacen                   | Almacen - ES                        | GUI | almacen-de-materia-prima-yherramientas-crear-modificar-entrada.component.ts   |
| Almacen                   | Almacen - ES                        | GUI | almacen-de-materia-prima-yherramientas-crear-modificar-entrada.component.html |
| Almacen                   | Almacen - ES                        | GUI | almacen-de-materia-prima-yherramientas-crear-modificar-salida.component.ts    |
| Almacen                   | Almacen - ES                        | GUI | almacen-de-materia-prima-yherramientas-crear-modificar-salida.component.html  |
| Almacen                   | Almacen - IAP                       | GUI | inventario-almacen-de-materia-prima-yherramientas.component.ts                |
| Almacen                   | Almacen - IAP                       | GUI | inventario-almacen-de-materia-prima-yherramientas.component.html              |
| Almacen                   | Almacen - IAP                       | GUI | inventario-almacen-de-materia-prima-yherramientas.component.css               |
| Almacen                   | Almacen - IAP                       | GUI | inventario-alma-mate-prima-herr-detalle.component.ts                          |
| Almacen                   | Almacen - IAP                       | GUI | inventario-alma-mate-prima-herr-detalle.component.html                        |
| Almacen                   | Almacen - IAP                       | GUI | inventario-alma-mate-prima-herr-detalle.component.css                         |
|                           |                                     | GUI | articulo.modelo.ts                                                            |
|                           |                                     | GUI | entradaArticulo.model.ts                                                      |
|                           |                                     | GUI | salidaArticulo.model.ts                                                       |
|                           |                                     | GUI | articulo.service.ts                                                           |
|                           |                                     | GUI | articulo.parametrosIndexacion.ts                                              |
|                           |                                     | API | articulo.parametrosIndexacion.js                                              |
|                           |                                     | API | articulo.model.js                                                             |
|                           |                                     | API | articulo.route.js                                                             |
|                           |                                     | API | salidaArticulo.model.js                                                       |
|                           |                                     | API | entradaArticulo.model.js                                                      |
| Almacen                   | Producto terminado                  | GUI | almacen-de-producto-terminado.component.ts                                    |
| Almacen                   | Producto terminado                  | GUI | almacen-de-producto-terminado.component.html                                  |
| Almacen                   | Producto terminado                  | GUI | almacen-de-producto-terminado.component.css                                   |
| Almacen                   | Producto terminado                  | GUI | almacen-de-producto-terminado-crear-modificar.component.ts                    |
| Almacen                   | Producto terminado                  | GUI | almacen-de-producto-terminado-crear-modificar.component.html                  |
| Almacen                   | Producto terminado                  | GUI | almacen-de-producto-terminado-crear-modificar-salida.component.ts             |
| Almacen                   | Producto terminado                  | GUI | almacen-de-producto-terminado-crear-modificar-salida.component.html           |
| Almacen                   | Producto terminado                  | GUI | almacen-de-producto-terminado-crear-modificar-entrada.component.ts            |
| Almacen                   | Producto terminado                  | GUI | almacen-de-producto-terminado-crear-modificar-entrada.component.html          |
| Almacen                   | Producto terminado                  | GUI | reporte-es-almacen-producto-terminado.component.ts                            |
| Almacen                   | Producto terminado                  | GUI | reporte-es-almacen-producto-terminado.component.html                          |
| Almacen                   | Producto terminado                  | GUI | reporte-negados-almacen-producto-terminado.component.ts                       |
| Almacen                   | Producto terminado                  | GUI | reporte-negados-almacen-producto-terminado.component.html                     |
|                           |                                     | GUI | modelo-completo.service.ts                                                    |
|                           |                                     | GUI | modeloCompleto.modelo.ts                                                      |
|                           |                                     | API | modeloCompleto.js                                                             |
|                           |                                     | API | modeloCompleto.js                                                             |
|                           |                                     | API | modeloCompletoAutorizacion.js                                                 |
|                           |                                     | API | lote.js                                                                       |
|                           |                                     | API | lote.js                                                                       |
|                           |                                     | API | entradaLote.model.js                                                          |
|                           |                                     | API | salidaLote.js                                                                 |
| Almacen                   | Reportes personalizados             | GUI | reporte-personalizado-almacen-produccion.component.ts                         |
| Almacen                   | Reportes personalizados             | GUI | reporte-personalizado-almacen-produccion.component.html                       |
| Almacen                   | Reportes personalizados             | GUI | reporte-personalizado-almacen-produccion.component.css                        |
| Almacen                   | Reportes personalizados             | GUI | reporte-personalizado-almacen-produccion-crear-modificar.component.ts         |
| Almacen                   | Reportes personalizados             | GUI | reporte-personalizado-almacen-produccion-crear-modificar.component.html       |
| Almacen                   | Reportes personalizados             | GUI | reporte-personalizado-almacen-produccion-crear-modificar.component.css        |
| Almacen                   | Reportes personalizados             | GUI | reporte-personalizado-almacen-produccion-detalle.component.ts                 |
| Almacen                   | Reportes personalizados             | GUI | reporte-personalizado-almacen-produccion-detalle.component.html               |
| Almacen                   | Reportes personalizados             | GUI | reporte-personalizado-almacen-produccion-detalle.component.css                |
| Almacen                   | Reportes personalizados             | GUI | r-personalizado-almacen-produccion.component.ts                               |
| Almacen                   | Reportes personalizados             | GUI | r-personalizado-almacen-produccion.component.html                             |
| Almacen                   | Reportes personalizados             | GUI | r-personalizado-almacen-produccion.component.css                              |
| Almacen                   | Reportes personalizados             | GUI | r-personalizado-almacen-produccion-imprimible.component.ts                    |
| Almacen                   | Reportes personalizados             | GUI | r-personalizado-almacen-produccion-imprimible.component.html                  |
| Almacen                   | Reportes personalizados             | GUI | r-personalizado-almacen-produccion-imprimible.component.css                   |
|                           |                                     | GUI | reportes-personalizados-almacen-produccion.service.ts                         |
|                           |                                     | GUI | reportePersonalizadoAlmacenProduccion.model.ts                                |
|                           |                                     | GUI | reportePersonalizadoAlmacenProduccion.parametrosIndexacion.ts                 |
|                           |                                     | API | reportePersonalizadoAlmacenProduccion.parametrosIndexacion.js                 |
|                           |                                     | API | reportePersonalizadoAlmacenProduccion.route.js                                |
|                           |                                     | API | reportePersonalizadoAlmacenProduccion.model.js                                |
| Almacen                   | Requisiciones                       | GUI | requisicion.component.ts                                                      |
| Almacen                   | Requisiciones                       | GUI | requisicion.component.html                                                    |
| Almacen                   | Requisiciones                       | GUI | requisicion-detalle.component.ts                                              |
| Almacen                   | Requisiciones                       | GUI | requisicion-detalle.component.html                                            |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-general.component.ts                                      |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-general.component.html                                    |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-requisicion.component.ts                               |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-requisicion.component.html                             |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-orden-de-compra.component.ts                           |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-orden-de-compra.component.html                         |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-entrega-parcial.component.ts                           |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-entrega-parcial.component.html                         |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-terminada.component.ts                                 |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-terminada.component.html                               |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-cancelada.component.ts                                 |
| Almacen                   | Requisiciones                       | GUI | requisicion-estatus-es-cancelada.component.html                               |
| Almacen                   | Requisiciones                       | GUI | requisicion-crear-modificar.component.ts                                      |
| Almacen                   | Requisiciones                       | GUI | requisicion-crear-modificar.component.html                                    |
| Almacen                   | Requisiciones                       | GUI | recibir-cancelacion.component.ts                                              |
| Almacen                   | Requisiciones                       | GUI | recibir-cancelacion.component.html                                            |
| Almacen                   | Requisiciones                       | GUI | recibir-terminacion.component.ts                                              |
| Almacen                   | Requisiciones                       | GUI | recibir-terminacion.component.html                                            |
| Almacen                   | Requisiciones                       | GUI | recibir-parcialidad.component.ts                                              |
| Almacen                   | Requisiciones                       | GUI | recibir-parcialidad.component.html                                            |
| Almacen                   | Requisiciones                       | GUI | requisicion-filtros.component.ts                                              |
| Almacen                   | Requisiciones                       | GUI | requisicion-filtros.component.html                                            |
|                           |                                     | GUI | requisicion-campos-para-mostrar-en-filtro.ts                                  |
|                           |                                     | GUI | requisicion.filtro.ts                                                         |
|                           |                                     | GUI | requisicion.model.ts                                                          |
|                           |                                     | GUI | imagenesFacturas.model.ts                                                     |
|                           |                                     | GUI | requisicion.servicte.ts                                                       |
|                           |                                     | GUI | requisicion.parametrosIndexacion.ts                                           |
|                           |                                     | API | requisicion.parametrosIndexacion.js                                           |
|                           |                                     | API | requisicion.model.js                                                          |
|                           |                                     | API | requisicion.route.js                                                          |
| Administrador             | Almacen descripcion                 | GUI | almacen-descripcion.component.ts                                              |
| Administrador             | Almacen descripcion                 | GUI | almacen-descripcion.component.html                                            |
| Administrador             | Almacen descripcion                 | GUI | almacen-descripcion-crear-modificar.component.ts                              |
| Administrador             | Almacen descripcion                 | GUI | almacen-descripcion-crear-modificar.component.html                            |
| Administrador             | Almacen descripcion                 | GUI | almacen-descripcion-detalle.component.ts                                      |
| Administrador             | Almacen descripcion                 | GUI | almacen-descripcion-detalle.component.html                                    |
|                           |                                     | GUI | almacen-descripcion.model.ts                                                  |
|                           |                                     | GUI | almacen-descripcion.service.ts                                                |
|                           |                                     | API | almacenDescripcion.model.js                                                   |
|                           |                                     | API | almacenDescripcion.route.js                                                   |
| Administrador             | Areas                               | GUI | areas.component.ts                                                            |
| Administrador             | Areas                               | GUI | areas.component.html                                                          |
| Administrador             | Areas                               | GUI | areas-crear-modificar.component.ts                                            |
| Administrador             | Areas                               | GUI | areas-crear-modificar.component.html                                          |
| Administrador             | Areas                               | GUI | areas-detalle.component.ts                                                    |
| Administrador             | Areas                               | GUI | areas-detalle.component.html                                                  |
|                           |                                     | GUI | areaRH.model.ts                                                               |
|                           |                                     | GUI | area.service.ts                                                               |
|                           |                                     | API | areaRH.model.js                                                               |
|                           |                                     | API | area.route.js                                                                 |
| Administrador             | Clientes                            | GUI | clientes.component.ts                                                         |
| Administrador             | Clientes                            | GUI | clientes.component.html                                                       |
| Administrador             | Clientes                            | GUI | clientes-crear-modificar.component.ts                                         |
| Administrador             | Clientes                            | GUI | clientes-crear-modificar.component.html                                       |
| Administrador             | Clientes                            | GUI | clientes-detalle.component.ts                                                 |
| Administrador             | Clientes                            | GUI | clientes-detalle.component.html                                               |
|                           |                                     | GUI | cliente.models.ts                                                             |
|                           |                                     | GUI | cliente.service.ts                                                            |
|                           |                                     | API | cliente.js                                                                    |
|                           |                                     | API | cliente.js                                                                    |
| Administrador             | Departametos                        | GUI | departamento                                                                  |
| Administrador             | Departametos                        | GUI | departamento                                                                  |
| Administrador             | Departametos                        | GUI | departamento-crear-modificar                                                  |
| Administrador             | Departametos                        | GUI | departamento-crear-modificar                                                  |
| Administrador             | Departametos                        | GUI | departamento-detalle                                                          |
| Administrador             | Departametos                        | GUI | departamento-detalle                                                          |
|                           |                                     | GUI | departamento.models.ts                                                        |
|                           |                                     | GUI | departamento.service.ts                                                       |
|                           |                                     | GUI | departamentos.ts                                                              |
|                           |                                     | GUI | departamentosConfig.ts                                                        |
|                           |                                     | GUI | gestion-departamento.component.ts                                             |
|                           |                                     | GUI | gestion-departamento.component.html                                           |
|                           |                                     | API | departamento.js                                                               |
|                           |                                     | API | departamento.js                                                               |
| Administrador             | Indexador                           | GUI | indexador.component.ts                                                        |
| Administrador             | Indexador                           | GUI | indexador.component.html                                                      |
|                           |                                     | GUI | indexador.service.ts                                                          |
|                           |                                     | API | registroIndexacion.model.js                                                   |
|                           |                                     | API | registroIndexacion.route.js                                                   |
|                           |                                     | API | registroIndexacion.service.js                                                 |
| Administrador             | Usuarios                            | GUI | usuario-leer.component.ts                                                     |
| Administrador             | Usuarios                            | GUI | usuario-leer.component.html                                                   |
| Administrador             | Usuarios                            | GUI | usuario-leer.component.css                                                    |
| Administrador             | Usuarios                            | GUI | usuario-crear.component.ts                                                    |
| Administrador             | Usuarios                            | GUI | usuario-crear.component.html                                                  |
| Administrador             | Usuarios                            | GUI | usuario-crear.component.css                                                   |
| Administrador             | Usuarios                            | GUI | usuario-detalle.component.ts                                                  |
| Administrador             | Usuarios                            | GUI | usuario-detalle.component.html                                                |
| Administrador             | Usuarios                            | GUI | usuario-detalle.component.css                                                 |
| Administrador             | Usuarios                            | GUI | usuario.model.ts                                                              |
| Administrador             | Usuarios                            | GUI | usuario.service.ts                                                            |
|                           |                                     | API | usuario.js                                                                    |
|                           |                                     | API | usuario.service.js                                                            |
|                           |                                     | API | usuario.route.js                                                              |
| Compras                   | Divisas                             | GUI | divisa.component.ts                                                           |
| Compras                   | Divisas                             | GUI | divisa.component.html                                                         |
| Compras                   | Divisas                             | GUI | divisa-crear-modificar.component.ts                                           |
| Compras                   | Divisas                             | GUI | divisa-crear-modificar.component.html                                         |
| Compras                   | Divisas                             | GUI | divisa-detalle.componen.ts                                                    |
| Compras                   | Divisas                             | GUI | divisa-detalle.componen.html                                                  |
| Compras                   | Divisas                             | GUI | divisa.model.ts                                                               |
| Compras                   | Divisas                             | GUI | divisa.service.ts                                                             |
| Compras                   | Divisas                             | GUI | FiltrosDivisas.ts                                                             |
|                           |                                     | API | divisa.model.js                                                               |
|                           |                                     | API | divisa.route.js                                                               |
| Compras                   | Proveedores                         | GUI | proveedor.component.ts                                                        |
| Compras                   | Proveedores                         | GUI | proveedor.component.html                                                      |
| Compras                   | Proveedores                         | GUI | proveedor-detalle.component.ts                                                |
| Compras                   | Proveedores                         | GUI | proveedor-detalle.component.html                                              |
| Compras                   | Proveedores                         | GUI | proveedor-crear-modificar.component.ts                                        |
| Compras                   | Proveedores                         | GUI | proveedor-crear-modificar.component.html                                      |
| Compras                   | Proveedores                         | GUI | proveedor.model.ts                                                            |
| Compras                   | Proveedores                         | GUI | proveedor.service.ts                                                          |
| Compras                   | Proveedores                         | GUI | proveedor.filtros.ts                                                          |
|                           |                                     | API | proveedor.model.js                                                            |
|                           |                                     | API | proveedor.route.js                                                            |
| Control de Producción     | Asignar ordenes                     | GUI | programacion-transformacion.component.ts                                      |
| Control de Producción     | Asignar ordenes                     | GUI | programacion-transformacion.component.html                                    |
| Control de Producción     | Asignar ordenes                     | GUI | programacion-transformacion.component.css                                     |
|                           |                                     | API | programacionTransformacion.route.js                                           |
| Control de Producción     | Material no conforme                | GUI | vista-reportes-material-no-conforme.module.ts                                 |
| Control de Producción     | Material no conforme                | GUI | vista-reportes-material-no-conforme.component.ts                              |
| Control de Producción     | Material no conforme                | GUI | vista-reportes-material-no-conforme.component.html                            |
| Control de Producción     | Material no conforme                | GUI | vista-reportes-material-no-conforme.component.css                             |
| Control de Producción     | Material no conforme                | GUI | detalle-reporte-material-no-conforme.module.ts                                |
| Control de Producción     | Material no conforme                | GUI | detalle-reporte-material-no-conforme.component.ts                             |
| Control de Producción     | Material no conforme                | GUI | detalle-reporte-material-no-conforme.component.html                           |
| Control de Producción     | Material no conforme                | GUI | detalle-reporte-material-no-conforme.component.css                            |
| Control de Producción     | Material no conforme                | GUI | estatus-reporte-material-no-conforme.module.ts                                |
| Control de Producción     | Material no conforme                | GUI | estatus-reporte-material-no-conforme.component.ts                             |
| Control de Producción     | Material no conforme                | GUI | estatus-reporte-material-no-conforme.component.html                           |
| Control de Producción     | Material no conforme                | GUI | estatus-reporte-material-no-conforme.component.css                            |
| Control de Producción     | Material no conforme                | GUI | formulario-creacion-reporte-material-no-conforme.module.ts                    |
| Control de Producción     | Material no conforme                | GUI | formulario-creacion-reporte-material-no-conforme.component.ts                 |
| Control de Producción     | Material no conforme                | GUI | formulario-creacion-reporte-material-no-conforme.component.html               |
| Control de Producción     | Material no conforme                | GUI | formulario-creacion-reporte-material-no-conforme.component.css                |
|                           |                                     | GUI | reportes-material-no-conforme-control-scrap.model.ts                          |
|                           |                                     | GUI | control-scrap.service                                                         |
|                           |                                     | GUI | contenido-dropdown-notificaciones.module.ts                                   |
|                           |                                     | GUI | contenido-dropdown-notificaciones.component.ts                                |
|                           |                                     | GUI | contenido-dropdown-notificaciones.component.html                              |
|                           |                                     | GUI | contenido-dropdown-notificaciones.component.css                               |
|                           |                                     | GUI | notificacionesControlScrap.model.js                                           |
|                           |                                     | GUI | notificacionesControlScrap.route.js                                           |
|                           |                                     | GUI | notificacionesControlScrap.service.js                                         |
|                           |                                     | GUI | notificacionesControlScrap.controller.js                                      |
|                           |                                     | API | reporteMaterialNoConformeControlScrap.model.js                                |
|                           |                                     | API | reporteMaterialNoConformeControlScrap.route.js                                |
|                           |                                     | API | reporteMaterialNoConformeControlScrap.service.js                              |
|                           |                                     | API | reporteMaterialNoConformeControlScrap.controller.js                           |
| Control de Producción     | Reportes escaneres                  | GUI | reportes-escaneres.component.ts                                               |
| Control de Producción     | Reportes escaneres                  | GUI | reportes-escaneres.component.html                                             |
| Control de Producción     | Revision de folios                  | GUI | revision-de-folios.component.ts                                               |
| Control de Producción     | Revision de folios                  | GUI | revision-de-folios.component.html                                             |
| Control de Producción     | Revision de folios                  | GUI | revision-de-ordenes-abstracto.component.ts                                    |
| Control de Producción     | Revision de folios                  | GUI | revision-de-ordenes-abstracto.component.html                                  |
| Control de Producción     | Revision de folios                  | GUI | revision-de-ordenes-abstracto.component.css                                   |
| Control de Producción     | Revision de folios                  | GUI | modelo-completo-gestor-de-procesos-especiales.component.ts                    |
| Control de Producción     | Revision de folios                  | GUI | modelo-completo-gestor-de-procesos-especiales.component.html                  |
| Control de Producción     | Seguimientos                        | GUI | folios-seguimiento.component.ts                                               |
| Control de Producción     | Seguimientos                        | GUI | folios-seguimiento.component.html                                             |
| Control de Producción     | Seguimientos                        | GUI | folios-detalle-abstracto.component.ts                                         |
| Control de Producción     | Seguimientos                        | GUI | folios-detalle-abstracto.component.html                                       |
| Control de Producción     | Seguimientos                        | GUI | pedidos-detalle-abstracto.component.ts                                        |
| Control de Producción     | Seguimientos                        | GUI | pedidos-detalle-abstracto.component.html                                      |
| Control de Producción     | Seguimientos                        | GUI | ordenes-detalle-abstracto.component.ts                                        |
| Control de Producción     | Seguimientos                        | GUI | ordenes-detalle-abstracto.component.html                                      |
| Control de Producción     | Seguimientos                        | GUI | orden-detalle-imprimir.component.ts                                           |
| Control de Producción     | Seguimientos                        | GUI | orden-detalle-imprimir.component.html                                         |
| Control de Producción     | Seguimientos                        | GUI | orden-detalle-imprimir.component.css                                          |
| Control de Producción     | Seguimientos                        | GUI | orden-detalle-avance2.component.ts                                            |
| Control de Producción     | Seguimientos                        | GUI | orden-detalle-avance2.component.html                                          |
| Control de Producción     | Seguimientos                        | GUI | orden-detalle-avance2.component.css                                           |
|                           |                                     |     | reportes-produccion.service                                                   |
| Control de Producción     | Seguimientos                        | GUI | pedidos-comentarios-crear-modificar-ver.component.ts                          |
| Control de Producción     | Seguimientos                        | GUI | pedidos-comentarios-crear-modificar-ver.component.html                        |
|                           |                                     | GUI | comentarioPedidoSeguimiento.model.ts                                          |
|                           |                                     | GUI | comentario-pedidio-seguimiento.service.ts                                     |
|                           |                                     | API | comentarioPedidoSeguimiento.model.js                                          |
|                           |                                     | API | comentariosPedido.route.js                                                    |
| Dispositivos Electrónicos | Dispositivos asistencia             | GUI | dispositivos-asistencia.component.ts                                          |
| Dispositivos Electrónicos | Dispositivos asistencia             | GUI | dispositivos-asistencia.component.html                                        |
|                           |                                     | GUI | checador.model.ts                                                             |
|                           |                                     | GUI | dispositivos-asistencia.service.ts                                            |
| Gráficos                  | Ordenes Trabajando                  | GUI | grafico-ordenes-trabajando-por-escaner.component.ts                           |
| Gráficos                  | Ordenes Trabajando                  | GUI | grafico-ordenes-trabajando-por-escaner.component.html                         |
| Ingenieria                | Colores                             | GUI | colores.component.ts                                                          |
| Ingenieria                | Colores                             | GUI | colores.component.html                                                        |
| Ingenieria                | Colores                             | GUI | colores-crear-modificar.component.ts                                          |
| Ingenieria                | Colores                             | GUI | colores-crear-modificar.component.html                                        |
| Ingenieria                | Colores                             | GUI | colores-detalle.component.ts                                                  |
| Ingenieria                | Colores                             | GUI | colores-detalle.component.html                                                |
|                           |                                     | GUI | color.models.ts                                                               |
|                           |                                     | GUI | color.service.ts                                                              |
|                           |                                     | API | color.js                                                                      |
|                           |                                     | API | color.js                                                                      |
| Ingenieria                | Maquinas                            | GUI | maquinas.component.ts                                                         |
| Ingenieria                | Maquinas                            | GUI | maquinas.component.html                                                       |
| Ingenieria                | Maquinas                            | GUI | maquinas-crear-modificar.component.ts                                         |
| Ingenieria                | Maquinas                            | GUI | maquinas-crear-modificar.component.html                                       |
| Ingenieria                | Maquinas                            | GUI | maquinas-detalle.component.ts                                                 |
| Ingenieria                | Maquinas                            | GUI | maquinas-detalle.component.html                                               |
|                           |                                     | GUI | maquina.model.ts                                                              |
|                           |                                     | GUI | maquina.service.ts                                                            |
|                           |                                     | GUI | maquina.parametrosIndexacion.ts                                               |
|                           |                                     | API | maquina.parametrosIndexacion.js                                               |
|                           |                                     | API | maquina.js                                                                    |
|                           |                                     | API | nombreAnteriorMaquina.js                                                      |
|                           |                                     | API | maquina.js                                                                    |
| Ingenieria                | Modelos                             | GUI | modelos.component.ts                                                          |
| Ingenieria                | Modelos                             | GUI | modelos.component.html                                                        |
| Ingenieria                | Modelos                             | GUI | modelos-crear-modificar.component.ts                                          |
| Ingenieria                | Modelos                             | GUI | modelos-crear-modificar.component.html                                        |
| Ingenieria                | Modelos                             | GUI | modelos-detalle.component.ts                                                  |
| Ingenieria                | Modelos                             | GUI | modelos-detalle.component.html                                                |
|                           |                                     | GUI | modelo.models.ts                                                              |
|                           |                                     | GUI | modelo.service.ts                                                             |
|                           |                                     | API | modelo.js                                                                     |
|                           |                                     | API | modelo.js                                                                     |
| Ingenieria                | Procesos                            | GUI | procesos.component.ts                                                         |
| Ingenieria                | Procesos                            | GUI | procesos.component.html                                                       |
| Ingenieria                | Procesos                            | GUI | procesos-crear-modificar.component.ts                                         |
| Ingenieria                | Procesos                            | GUI | procesos-crear-modificar.component.html                                       |
| Ingenieria                | Procesos                            | GUI | procesos-crear-modificar.component.css                                        |
| Ingenieria                | Procesos                            | GUI | procesos-detalle.component.ts                                                 |
| Ingenieria                | Procesos                            | GUI | procesos-detalle.component.html                                               |
|                           |                                     | GUI | procesos.model.ts                                                             |
|                           |                                     | GUI | proceso.service.ts                                                            |
|                           |                                     | API | proceso.js                                                                    |
|                           |                                     | API | proceso.js                                                                    |
| Ingenieria                | Procesos - Familias                 | GUI | familia-de-procesos.component.ts                                              |
| Ingenieria                | Procesos - Familias                 | GUI | familia-de-procesos.component.html                                            |
| Ingenieria                | Procesos - Familias                 | GUI | familia-de-procesos-crear-modificar.component.ts                              |
| Ingenieria                | Procesos - Familias                 | GUI | familia-de-procesos-crear-modificar.component.html                            |
| Ingenieria                | Procesos - Familias                 | GUI | familia-de-procesos-detalle.component.ts                                      |
| Ingenieria                | Procesos - Familias                 | GUI | familia-de-procesos-detalle.component.html                                    |
|                           |                                     | GUI | familiaDeProcesos.model.ts                                                    |
|                           |                                     | GUI | familia-de-procesos.service.ts                                                |
|                           |                                     | GUI | familiaDeProcesos.parametrosIndexacion.ts                                     |
|                           |                                     | API | familiaDeProcesos.parametrosIndexacion.js                                     |
|                           |                                     | API | familiaDeProcesos.js                                                          |
|                           |                                     | API | familiaDeProcesos.js                                                          |
| Ingenieria                | SKU - Produccion                    | GUI | modelos-completos.component.ts                                                |
| Ingenieria                | SKU - Produccion                    | GUI | modelos-completos.component.html                                              |
| Ingenieria                | SKU - Produccion                    | GUI | modelos-completos-crear-modificar.component.ts                                |
| Ingenieria                | SKU - Produccion                    | GUI | modelos-completos-crear-modificar.component.html                              |
| Ingenieria                | SKU - Produccion                    | GUI | modelos-completos-detalle.component.ts                                        |
| Ingenieria                | SKU - Produccion                    | GUI | modelos-completos-detalle.component.html                                      |
|                           |                                     | GUI | modeloCompleto.modelo.ts                                                      |
|                           |                                     | GUI | modelo-completo.service.ts                                                    |
|                           |                                     | GUI | modeloCompleto.parametrosIndexacion.ts                                        |
|                           |                                     | API | modeloCompleto.parametrosIndexacion.js                                        |
|                           |                                     | API | modeloCompleto.js                                                             |
|                           |                                     | API | modeloCompletoAutorizacion.js                                                 |
|                           |                                     | API | modeloCompleto.js                                                             |
| Ingenieria                | Tamanos                             | GUI | tamanos.component.ts                                                          |
| Ingenieria                | Tamanos                             | GUI | tamanos.component.html                                                        |
| Ingenieria                | Tamanos                             | GUI | tamanos-crear-modificar.component.ts                                          |
| Ingenieria                | Tamanos                             | GUI | tamanos-crear-modificar.component.html                                        |
| Ingenieria                | Tamanos                             | GUI | tamanos-detalle.component.ts                                                  |
| Ingenieria                | Tamanos                             | GUI | tamanos-detalle.component.html                                                |
|                           |                                     | GUI | tamano.models.ts                                                              |
|                           |                                     | GUI | tamano.service                                                                |
|                           |                                     | API | tamano.js                                                                     |
|                           |                                     | API | tamano.js                                                                     |
| Ingenieria                | Terminados                          | GUI | terminados.component.ts                                                       |
| Ingenieria                | Terminados                          | GUI | terminados.component.html                                                     |
| Ingenieria                | Terminados                          | GUI | terminados-crear-modificar.component.ts                                       |
| Ingenieria                | Terminados                          | GUI | terminados-crear-modificar.component.html                                     |
| Ingenieria                | Terminados                          | GUI | terminados-detalle.component.ts                                               |
| Ingenieria                | Terminados                          | GUI | terminados-detalle.component.html                                             |
|                           |                                     | GUI | terminado.models.ts                                                           |
|                           |                                     | GUI | terminado.service.ts                                                          |
|                           |                                     | API | terminado.js                                                                  |
|                           |                                     | API | terminado.js                                                                  |
| Mantenimiento             | Bitácora                            | GUI | bitacora-mantenimiento.module.ts                                              |
| Mantenimiento             | Bitácora                            | GUI | bitacora-mantenimiento.component.ts                                           |
| Mantenimiento             | Bitácora                            | GUI | bitacora-mantenimiento.component.html                                         |
| Mantenimiento             | Bitácora                            | GUI | bitacora-mantenimiento.component.css                                          |
| Mantenimiento             | Bitácora                            | GUI | detalle-bitacora-mantenimiento.module.ts                                      |
| Mantenimiento             | Bitácora                            | GUI | detalle-bitacora-mantenimiento.component.ts                                   |
| Mantenimiento             | Bitácora                            | GUI | detalle-bitacora-mantenimiento.component.html                                 |
| Mantenimiento             | Bitácora                            | GUI | detalle-bitacora-mantenimiento.component.css                                  |
| Mantenimiento             | Bitácora                            | GUI | filtros-bitacora-mantenimiento.module.ts                                      |
| Mantenimiento             | Bitácora                            | GUI | filtros-bitacora-mantenimiento.component.ts                                   |
| Mantenimiento             | Bitácora                            | GUI | filtros-bitacora-mantenimiento.component.html                                 |
| Mantenimiento             | Bitácora                            | GUI | filtros-bitacora-mantenimiento.component.css                                  |
| Mantenimiento             | Bitácora                            | GUI | estatus-registro-bitacora-mantenimiento.module.ts                             |
| Mantenimiento             | Bitácora                            | GUI | estatus-registro-bitacora-mantenimiento.component.ts                          |
| Mantenimiento             | Bitácora                            | GUI | estatus-registro-bitacora-mantenimiento.component.html                        |
| Mantenimiento             | Bitácora                            | GUI | estatus-registro-bitacora-mantenimiento.component.css                         |
| Mantenimiento             | Bitácora                            | GUI | formulario-edicion-bitacora-mantenimiento.module.ts                           |
| Mantenimiento             | Bitácora                            | GUI | formulario-edicion-bitacora-mantenimiento.component.ts                        |
| Mantenimiento             | Bitácora                            | GUI | formulario-edicion-bitacora-mantenimiento.component.html                      |
| Mantenimiento             | Bitácora                            | GUI | formulario-edicion-bitacora-mantenimiento.component.css                       |
| Mantenimiento             | Bitácora                            | GUI | formulario-creacion-bitacora-mantenimiento.module.ts                          |
| Mantenimiento             | Bitácora                            | GUI | formulario-creacion-bitacora-mantenimiento.component.ts                       |
| Mantenimiento             | Bitácora                            | GUI | formulario-creacion-bitacora-mantenimiento.component.html                     |
| Mantenimiento             | Bitácora                            | GUI | formulario-creacion-bitacora-mantenimiento.component.css                      |
| Mantenimiento             | Bitácora                            | GUI | modificar-imagenes-un-registro-bitacora-mantenimiento.module.ts               |
| Mantenimiento             | Bitácora                            | GUI | modificar-imagenes-un-registro-bitacora-mantenimiento.component.ts            |
| Mantenimiento             | Bitácora                            | GUI | modificar-imagenes-un-registro-bitacora-mantenimiento.component.html          |
| Mantenimiento             | Bitácora                            | GUI | modificar-imagenes-un-registro-bitacora-mantenimiento.component.css           |
| Mantenimiento             | Bitácora                            | GUI | modificar-articulos-un-registro-bitacora-mantenimiento.module.ts              |
| Mantenimiento             | Bitácora                            | GUI | modificar-articulos-un-registro-bitacora-mantenimiento.component.ts           |
| Mantenimiento             | Bitácora                            | GUI | modificar-articulos-un-registro-bitacora-mantenimiento.component.html         |
| Mantenimiento             | Bitácora                            | GUI | modificar-articulos-un-registro-bitacora-mantenimiento.component.css          |
|                           |                                     | GUI | bitacora-mantenimiento.model.ts                                               |
|                           |                                     | GUI | bitacora-mantenimiento.service.ts                                             |
|                           |                                     | API | registroBitacoraMantenimiento.model.js                                        |
|                           |                                     | API | registroBitacoraMantenimiento.route.js                                        |
|                           |                                     | API | registroBitacoraMantenimiento.service.js                                      |
|                           |                                     | API | registroBitacoraMantenimiento.controller.js                                   |
| Mantenimiento             | Maquinas                            | GUI | mantenimiento-maquinas.component.ts                                           |
| Mantenimiento             | Maquinas                            | GUI | mantenimiento-maquinas.component.html                                         |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-formulario-mantenimiento.module.ts                              |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-formulario-mantenimiento.component.ts                           |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-formulario-mantenimiento.component.html                         |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-formulario-mantenimiento.component.css                          |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-detalle.module.ts                                            |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-detalle.component.ts                                         |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-detalle.component.html                                       |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-detalle.component.css                                        |
| Mantenimiento             | Maquinas                            | GUI | seleccion-formularios-mantenimiento.module.ts                                 |
| Mantenimiento             | Maquinas                            | GUI | seleccion-formularios-mantenimiento.component.ts                              |
| Mantenimiento             | Maquinas                            | GUI | seleccion-formularios-mantenimiento.component.html                            |
| Mantenimiento             | Maquinas                            | GUI | seleccion-formularios-mantenimiento.component.css                             |
| Mantenimiento             | Maquinas                            | GUI | filtro-maquinas-mantenimiento.module.ts                                       |
| Mantenimiento             | Maquinas                            | GUI | filtro-maquinas-mantenimiento.component.ts                                    |
| Mantenimiento             | Maquinas                            | GUI | filtro-maquinas-mantenimiento.component.html                                  |
| Mantenimiento             | Maquinas                            | GUI | filtro-maquinas-mantenimiento.component.css                                   |
| Mantenimiento             | Maquinas                            | GUI | estatus-maquinas.component.ts                                                 |
| Mantenimiento             | Maquinas                            | GUI | estatus-maquinas.component.html                                               |
| Mantenimiento             | Maquinas                            | GUI | estatus-maquinas.component.css                                                |
| Mantenimiento             | Maquinas                            | GUI | mantenimiento-maquina-detalle.component.ts                                    |
| Mantenimiento             | Maquinas                            | GUI | mantenimiento-maquina-detalle.component.html                                  |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-mantenimiento.module.ts                                         |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-mantenimiento.component.ts                                      |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-mantenimiento.component.html                                    |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-mantenimiento.component.css                                     |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-mantenimiento-solo-lectura.module.ts                           |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-mantenimiento-solo-lectura.component.ts                        |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-mantenimiento-solo-lectura.component.html                      |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-mantenimiento-solo-lectura.component.css                       |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-mantenimiento-editable.module.ts                               |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-mantenimiento-editable.component.ts                            |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-mantenimiento-editable.component.html                          |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-mantenimiento-editable.component.css                           |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-mantenimiento-solo-lectura.module.ts                         |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-mantenimiento-solo-lectura.component.ts                      |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-mantenimiento-solo-lectura.component.html                    |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-mantenimiento-solo-lectura.component.css                     |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-mantenimiento-editable.module.ts                             |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-mantenimiento-editable.component.ts                          |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-mantenimiento-editable.component.html                        |
| Mantenimiento             | Maquinas                            | GUI | vista-formulario-mantenimiento-editable.component.css                         |
| Mantenimiento             | Maquinas                            | GUI | detalle-mantenimiento-formulario-solo-lectura.module.ts                       |
| Mantenimiento             | Maquinas                            | GUI | detalle-mantenimiento-formulario-solo-lectura.component.ts                    |
| Mantenimiento             | Maquinas                            | GUI | detalle-mantenimiento-formulario-solo-lectura.component.html                  |
| Mantenimiento             | Maquinas                            | GUI | detalle-mantenimiento-formulario-solo-lectura.component.css                   |
| Mantenimiento             | Maquinas                            | GUI | detalle-mantenimiento-formulario-editable.module.ts                           |
| Mantenimiento             | Maquinas                            | GUI | detalle-mantenimiento-formulario-editable.component.ts                        |
| Mantenimiento             | Maquinas                            | GUI | detalle-mantenimiento-formulario-editable.component.html                      |
| Mantenimiento             | Maquinas                            | GUI | detalle-mantenimiento-formulario-editable.component.css                       |
| Mantenimiento             | Maquinas                            | GUI | mantenimiento-maquina-generar.component.ts                                    |
| Mantenimiento             | Maquinas                            | GUI | mantenimiento-maquina-generar.component.html                                  |
| Mantenimiento             | Maquinas                            | GUI | datos-extendidos-mantenimiento-creacion.module.ts                             |
| Mantenimiento             | Maquinas                            | GUI | datos-extendidos-mantenimiento-creacion.component.ts                          |
| Mantenimiento             | Maquinas                            | GUI | datos-extendidos-mantenimiento-creacion.component.html                        |
| Mantenimiento             | Maquinas                            | GUI | datos-extendidos-mantenimiento-creacion.component.css                         |
| Mantenimiento             | Maquinas                            | GUI | reparacion-maquina-generar.component.ts                                       |
| Mantenimiento             | Maquinas                            | GUI | reparacion-maquina-generar.component.html                                     |
| Mantenimiento             | Maquinas                            | GUI | reparacion-maquina-detalle.component.ts                                       |
| Mantenimiento             | Maquinas                            | GUI | reparacion-maquina-detalle.component.html                                     |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-reparacion-solo-lectura.module.ts                              |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-reparacion-solo-lectura.component.ts                           |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-reparacion-solo-lectura.component.html                         |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-reparacion-solo-lectura.component.css                          |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-reparacion-editable.module.ts                                  |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-reparacion-editable.component.ts                               |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-reparacion-editable.component.html                             |
| Mantenimiento             | Maquinas                            | GUI | titulo-detalle-reparacion-editable.component.css                              |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-reparacion.module.ts                                            |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-reparacion.component.ts                                         |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-reparacion.component.html                                       |
| Mantenimiento             | Maquinas                            | GUI | datos-basicos-reparacion.component.css                                        |
| Mantenimiento             | Maquinas                            | GUI | vista-reparacion-solo-lectura.module.ts                                       |
| Mantenimiento             | Maquinas                            | GUI | vista-reparacion-solo-lectura.component.ts                                    |
| Mantenimiento             | Maquinas                            | GUI | vista-reparacion-solo-lectura.component.html                                  |
| Mantenimiento             | Maquinas                            | GUI | vista-reparacion-solo-lectura.component.css                                   |
| Mantenimiento             | Maquinas                            | GUI | formularios-mantenimiento-para-contestar-imprimir.module.ts                   |
| Mantenimiento             | Maquinas                            | GUI | formularios-mantenimiento-para-contestar-imprimir.component.ts                |
| Mantenimiento             | Maquinas                            | GUI | formularios-mantenimiento-para-contestar-imprimir.component.html              |
| Mantenimiento             | Maquinas                            | GUI | formularios-mantenimiento-para-contestar-imprimir.component.css               |
| Mantenimiento             | Maquinas                            | GUI | formularios-mantenimiento-contestados-imprimir.module.ts                      |
| Mantenimiento             | Maquinas                            | GUI | formularios-mantenimiento-contestados-imprimir.component.ts                   |
| Mantenimiento             | Maquinas                            | GUI | formularios-mantenimiento-contestados-imprimir.component.html                 |
| Mantenimiento             | Maquinas                            | GUI | formularios-mantenimiento-contestados-imprimir.component.css                  |
| Mantenimiento             | Maquinas                            | GUI | detalle-reparaciones-imprimir.module.ts                                       |
| Mantenimiento             | Maquinas                            | GUI | detalle-reparaciones-imprimir.component.ts                                    |
| Mantenimiento             | Maquinas                            | GUI | detalle-reparaciones-imprimir.component.html                                  |
| Mantenimiento             | Maquinas                            | GUI | detalle-reparaciones-imprimir.component.css                                   |
|                           |                                     | GUI | mantenimientoMaquina.model.ts                                                 |
|                           |                                     | GUI | formulariosAContestarMant.model.ts                                            |
|                           |                                     | GUI | parteMantenimiento.model.ts                                                   |
|                           |                                     | GUI | seccionMantenimiento.model.ts                                                 |
|                           |                                     | GUI | mantenimiento-maquina.service.ts                                              |
|                           |                                     | API | mantenimientoMaquina.js                                                       |
|                           |                                     | API | MantenimientoMaquina.route.js                                                 |
|                           |                                     | GUI | reparacionMaquina.model.ts                                                    |
|                           |                                     | GUI | reparacion-maquina.service.ts                                                 |
|                           |                                     | API | reparacionMaquina.js                                                          |
|                           |                                     | API | reparacionMaquina.route.js                                                    |
| Mantenimiento             | Tipos Maquinas                      | GUI | tipos-maquinas.component.ts                                                   |
| Mantenimiento             | Tipos Maquinas                      | GUI | tipos-maquinas.component.html                                                 |
| Mantenimiento             | Tipos Maquinas                      | GUI | detalle-tipo-maquina-abstracto.component.ts                                   |
| Mantenimiento             | Tipos Maquinas                      | GUI | detalle-tipo-maquina-abstracto.component.html                                 |
| Mantenimiento             | Tipos Maquinas                      | GUI | tipos-maquinas-crear.component.ts                                             |
| Mantenimiento             | Tipos Maquinas                      | GUI | tipos-maquinas-crear.component.html                                           |
|                           |                                     | GUI | tipoMaquina.model.ts                                                          |
|                           |                                     | GUI | formularioMantenimiento.model.ts                                              |
|                           |                                     | GUI | parteFormularioMantenimiento.model.ts                                         |
|                           |                                     | GUI | seccionParteFormularioMantenimiento.model.ts                                  |
|                           |                                     | GUI | tipo-maquina.service.ts                                                       |
|                           |                                     | API | tipoMaquina.js                                                                |
|                           |                                     | API | tipoMaquina.route.js                                                          |
| Parametros                | Ajustes Control Scrap               | GUI | ajustes-control-scrap-produccion.module.ts                                    |
| Parametros                | Ajustes Control Scrap               | GUI | ajustes-control-scrap-produccion.component.ts                                 |
| Parametros                | Ajustes Control Scrap               | GUI | ajustes-control-scrap-produccion.component.html                               |
| Parametros                | Ajustes Control Scrap               | GUI | ajustes-control-scrap-produccion.component.css                                |
| Parametros                | Ajustes Mantenimientos Maquinas     | GUI | ajustes-mantenimientos-maquinas.component.ts                                  |
| Parametros                | Ajustes Mantenimientos Maquinas     | GUI | ajustes-mantenimientos-maquinas.component.html                                |
| Parametros                | Clientes especiales                 | GUI | definir-clientes-especiales.component.ts                                      |
| Parametros                | Clientes especiales                 | GUI | definir-clientes-especiales.component.html                                    |
| Parametros                | Crear estaciones de escaneo         | GUI | estaciones-de-escaneo.component.ts                                            |
| Parametros                | Crear estaciones de escaneo         | GUI | estaciones-de-escaneo.component.html                                          |
| Parametros                | Crear estaciones de escaneo         | GUI | estaciones-de-escaneo.component.css                                           |
| Parametros                | Crear estaciones de escaneo         | GUI | creador-de-formularios.component.ts                                           |
| Parametros                | Crear estaciones de escaneo         | GUI | creador-de-formularios.component.html                                         |
| Parametros                | Crear estaciones de escaneo         | GUI | creador-de-formularios.component.css                                          |
| Parametros                | Localizacion de ordenes             | GUI | procesos-iniciales-yfinales.component.ts                                      |
| Parametros                | Localizacion de ordenes             | GUI | procesos-iniciales-yfinales.component.html                                    |
| Parametros                | Localizacion de ordenes             | GUI | procesos-iniciales-yfinales.component.css                                     |
| Parametros                | Procesos Especiales                 | GUI | procesos-especiales.component.ts                                              |
| Parametros                | Procesos Especiales                 | GUI | procesos-especiales.component.html                                            |
| Parametros                | Procesos Especiales                 | GUI | procesos-especiales.component.css                                             |
| Parametros                | Restablecer o cambiar administrador | GUI | administrador.component.ts                                                    |
| Parametros                | Restablecer o cambiar administrador | GUI | administrador.component.html                                                  |
| Parametros                | Restablecer o cambiar administrador | GUI | administrador.component.css                                                   |
|                           |                                     | API | parametros.model.js                                                           |
|                           |                                     | API | parametros.route.js                                                           |
|                           |                                     | API | parametros.service.js                                                         |
| RH                        | Checadores                          | GUI | panel-control-checadores-rh.component.ts                                      |
| RH                        | Checadores                          | GUI | panel-control-checadores-rh.component.html                                    |
| RH                        | Checadores                          | GUI | panel-control-checadores-rh.component.css                                     |
|                           |                                     | GUI | usuariosChecador.model.ts                                                     |
|                           |                                     | GUI | asistencia.model.ts                                                           |
|                           |                                     | GUI | checador.model.ts                                                             |
|                           |                                     | GUI | dispositivos-asistencia.service.ts                                            |
|                           |                                     | API | checador.model.js                                                             |
|                           |                                     | API | checador.route.js                                                             |
|                           |                                     | API | checador.service.js                                                           |
|                           |                                     | API | checador.controller.js                                                        |
|                           |                                     | API | control.zkteco.py                                                             |
| RH                        | Checadores - Areas                  | GUI | areas-checadores.component.ts                                                 |
| RH                        | Checadores - Areas                  | GUI | areas-checadores.component.html                                               |
| RH                        | Checadores - Areas                  | GUI | areas-checadores.component.css                                                |
| RH                        |                                     | GUI | areas-checadores.service.ts                                                   |
| RH                        |                                     | GUI | areaChecador.model.ts                                                         |
|                           |                                     | API | areaChecador.model.js                                                         |
|                           |                                     | API | areaChecador.route.js                                                         |
| RH                        | Checadores - Usuarios               | GUI | usuarios-checadores.componen.ts                                               |
| RH                        | Checadores - Usuarios               | GUI | usuarios-checadores.component.html                                            |
| RH                        | Checadores - Usuarios               | GUI | usuarios-checadores.component.css                                             |
| RH                        | Checadores - Usuarios               | GUI | usuarios-checadores-detalle.componen.ts                                       |
| RH                        | Checadores - Usuarios               | GUI | usuarios-checadores-detalle.component.html                                    |
| RH                        | Checadores - Usuarios               | GUI | usuarios-checadores-detalle.component.css                                     |
| RH                        | Checadores - Usuarios               | GUI | usuarios-checadores-asistencias.componen.ts                                   |
| RH                        | Checadores - Usuarios               | GUI | usuarios-checadores-asistencias.component.html                                |
| RH                        | Checadores - Usuarios               | GUI | usuarios-checadores-asistencias.component.css                                 |
|                           |                                     | API | usuarioChecador.model.js                                                      |
|                           |                                     | API | asistencia.model.js                                                           |
|                           |                                     | API | controlChecador.route.js                                                      |
|                           |                                     | API | conrtolChecador.service.js                                                    |
|                           |                                     | API | controlChecador.controller.js                                                 |
| RH                        | Cursos                              | GUI | cursos.component.ts                                                           |
| RH                        | Cursos                              | GUI | cursos.component.html                                                         |
| RH                        | Cursos                              | GUI | cursos-crear-modificar.component.ts                                           |
| RH                        | Cursos                              | GUI | cursos-crear-modificar.component.html                                         |
| RH                        | Cursos                              | GUI | cursos-detalle.component.ts                                                   |
| RH                        | Cursos                              | GUI | cursos-detalle.component.html                                                 |
| RH                        |                                     | GUI | curso.model.ts                                                                |
| RH                        |                                     | GUI | curso.service.ts                                                              |
| RH                        |                                     | GUI | curso.filtros.ts                                                              |
|                           |                                     | API | curso.model.js                                                                |
|                           |                                     | API | curso.route.js                                                                |
| RH                        | Empleados                           | GUI | empleado.component.ts                                                         |
| RH                        | Empleados                           | GUI | empleado.component.html                                                       |
| RH                        | Empleados                           | GUI | empleado-crear-modificar.component.ts                                         |
| RH                        | Empleados                           | GUI | empleado-crear-modificar.component.html                                       |
| RH                        | Empleados                           | GUI | empleado-detalle.component.ts                                                 |
| RH                        | Empleados                           | GUI | empleado-detalle.component.html                                               |
| RH                        | Empleados                           | GUI | empleado-eventos-crear-modal.component.ts                                     |
| RH                        | Empleados                           | GUI | empleado-eventos-crear-modal.component.html                                   |
| RH                        | Empleados                           | GUI | empleado-agregar-amonestacion-por-escrito.component.html                      |
| RH                        | Empleados                           | GUI | empleado-agregar-amonestacion-por-escrito.component.ts                        |
| RH                        | Empleados                           | GUI | empleado-agregar-bono.component.html                                          |
| RH                        | Empleados                           | GUI | empleado-agregar-bono.component.ts                                            |
| RH                        | Empleados                           | GUI | empleado-agregar-cambios-de-sueldo.component.html                             |
| RH                        | Empleados                           | GUI | empleado-agregar-cambios-de-sueldo.component.ts                               |
| RH                        | Empleados                           | GUI | empleado-agregar-castigo.component.html                                       |
| RH                        | Empleados                           | GUI | empleado-agregar-castigo.component.ts                                         |
| RH                        | Empleados                           | GUI | empleado-agregar-estatus-laboral.component.html                               |
| RH                        | Empleados                           | GUI | empleado-agregar-estatus-laboral.component.ts                                 |
| RH                        | Empleados                           | GUI | empleado-agregar-felicitacion-por-escrito.component.html                      |
| RH                        | Empleados                           | GUI | empleado-agregar-felicitacion-por-escrito.component.ts                        |
| RH                        | Empleados                           | GUI | empleado-agregar-permiso.component.html                                       |
| RH                        | Empleados                           | GUI | empleado-agregar-permiso.component.ts                                         |
| RH                        | Empleados                           | GUI | empleado-agregar-puesto.component.html                                        |
| RH                        | Empleados                           | GUI | empleado-agregar-puesto.component.ts                                          |
| RH                        | Empleados                           | GUI | empleado-agregar-quitar-horario.component.html                                |
| RH                        | Empleados                           | GUI | empleado-agregar-quitar-horario.component.ts                                  |
| RH                        | Empleados                           | GUI | empleado-agregar-vacaciones.component.html                                    |
| RH                        | Empleados                           | GUI | empleado-agregar-vacaciones.component.ts                                      |
| RH                        | Empleados                           | GUI | empleado-evento-agregar-curso.component.html                                  |
| RH                        | Empleados                           | GUI | empleado-evento-agregar-curso.component.ts                                    |
| RH                        | Empleados                           | GUI | empleado-ingresar-eliminar-de-checador.component.html                         |
| RH                        | Empleados                           | GUI | empleado-ingresar-eliminar-de-checador.component.ts                           |
| RH                        | Empleados                           | GUI | empleado-evento-plantilla.component.html                                      |
| RH                        | Empleados                           | GUI | empleado-evento-plantilla.component.ts                                        |
| RH                        | Empleados                           | GUI | empleado-evento-amonestaciones-por-escrito.component.html                     |
| RH                        | Empleados                           | GUI | empleado-evento-amonestaciones-por-escrito.component.ts                       |
| RH                        | Empleados                           | GUI | empleado-evento-bono.component.html                                           |
| RH                        | Empleados                           | GUI | empleado-evento-bono.component.ts                                             |
| RH                        | Empleados                           | GUI | empleado-evento-cambio-checador.component.html                                |
| RH                        | Empleados                           | GUI | empleado-evento-cambio-checador.component.ts                                  |
| RH                        | Empleados                           | GUI | empleado-evento-cambio-de-sueldo.component.html                               |
| RH                        | Empleados                           | GUI | empleado-evento-cambio-de-sueldo.component.ts                                 |
| RH                        | Empleados                           | GUI | empleado-evento-castigo.component.html                                        |
| RH                        | Empleados                           | GUI | empleado-evento-castigo.component.ts                                          |
| RH                        | Empleados                           | GUI | empleado-evento-curso.component.html                                          |
| RH                        | Empleados                           | GUI | empleado-evento-curso.component.ts                                            |
| RH                        | Empleados                           | GUI | empleado-evento-estatus-laboral.component.html                                |
| RH                        | Empleados                           | GUI | empleado-evento-estatus-laboral.component.ts                                  |
| RH                        | Empleados                           | GUI | empleado-evento-felicitaciones-por-escrito.component.html                     |
| RH                        | Empleados                           | GUI | empleado-evento-felicitaciones-por-escrito.component.ts                       |
| RH                        | Empleados                           | GUI | empleado-evento-horario.component.html                                        |
| RH                        | Empleados                           | GUI | empleado-evento-horario.component.ts                                          |
| RH                        | Empleados                           | GUI | empleado-evento-manejador.component.html                                      |
| RH                        | Empleados                           | GUI | empleado-evento-manejador.component.ts                                        |
| RH                        | Empleados                           | GUI | empleado-evento-permiso.component.html                                        |
| RH                        | Empleados                           | GUI | empleado-evento-permiso.component.ts                                          |
| RH                        | Empleados                           | GUI | empleado-evento-puesto.component.html                                         |
| RH                        | Empleados                           | GUI | empleado-evento-puesto.component.ts                                           |
| RH                        | Empleados                           | GUI | empleado-evento-vacaciones.component.html                                     |
| RH                        | Empleados                           | GUI | empleado-evento-vacaciones.component.ts                                       |
|                           |                                     | GUI | empleado.model.ts                                                             |
|                           |                                     | GUI | empleado.service.ts                                                           |
| RH                        | Empleados                           | GUI | empleado-filtros.component.ts                                                 |
| RH                        | Empleados                           | GUI | empleado-filtros.component.html                                               |
|                           |                                     | GUI | empleado.filtros.ts                                                           |
|                           |                                     | GUI | EmpleadoAgregarEventosGeneral.ts                                              |
|                           |                                     | API | empleado.eliminarEvento.route.js                                              |
|                           |                                     | API | empleado.modificarEstatusLaboral.route.js                                     |
|                           |                                     | API | empleado.modificarPuesto.route.js                                             |
|                           |                                     | API | empleado.modificarSueldo.route.js                                             |
|                           |                                     | API | empleado.registrarActa.route.js                                               |
|                           |                                     | API | empleado.registrarAmonestacion.route.js                                       |
|                           |                                     | API | empleado.registrarBono.route.js                                               |
|                           |                                     | API | empleado.registrarChecador.route.js                                           |
|                           |                                     | API | empleado.registrarCurso.route.js                                              |
|                           |                                     | API | empleado.registrarFelicitacion.route.js                                       |
|                           |                                     | API | empleado.registrarHorario.route.js                                            |
|                           |                                     | API | empleado.registrarPermiso.route.js                                            |
|                           |                                     | API | empleado.registrarVacaciones.route.js                                         |
|                           |                                     | API | empleado.route.js                                                             |
|                           |                                     | API | eventosRH.model.js                                                            |
|                           |                                     | API | empleado.model.js                                                             |
| RH                        | Horarios                            | GUI | horario-empleado.component.ts                                                 |
| RH                        | Horarios                            | GUI | horario-empleado.component.html                                               |
| RH                        | Horarios                            | GUI | horario-empleado.component.css                                                |
|                           |                                     | GUI | horarioEmpleado.model.ts                                                      |
|                           |                                     | GUI | horaio-empleado.service.ts                                                    |
|                           |                                     | GUI | horarioEmpleado.parametrosIndexacion.ts                                       |
|                           |                                     | API | horarioEmpleado.parametrosIndexacion.js                                       |
|                           |                                     | API | horarioEmpleado.model.js                                                      |
|                           |                                     | API | horarioEmpleado.route.js                                                      |
|                           |                                     | API | horarioEmpleado.service.js                                                    |
| RH                        | Puestos                             | GUI | puestos.component.ts                                                          |
| RH                        | Puestos                             | GUI | puestos.component.html                                                        |
| RH                        | Puestos                             | GUI | puestos-crear-modificar.component.ts                                          |
| RH                        | Puestos                             | GUI | puestos-crear-modificar.component.html                                        |
| RH                        | Puestos                             | GUI | puestos-detalle.component.ts                                                  |
| RH                        | Puestos                             | GUI | puestos-detalle.component.html                                                |
|                           |                                     | GUI | puesto.model.ts                                                               |
|                           |                                     | GUI | puesto.service.ts                                                             |
|                           |                                     | GUI | puesto.filtros.ts                                                             |
|                           |                                     | API | puesto.model.js                                                               |
|                           |                                     | API | puesto.route.js                                                               |
|                           |                                     | API | puesto.route.aggregate.js                                                     |
| Reportes                  | Faltante producto terminado         | GUI | reporte-de-faltantes-producto-terminado.component.ts                          |
| Reportes                  | Faltante producto terminado         | GUI | reporte-de-faltantes-producto-terminado.component.html                        |
| Reportes                  | Faltante producto terminado         | GUI | reporte-de-faltantes-producto-terminado.component.css                         |
| Reportes                  | Faltante producto terminado         | GUI | reporte-de-faltantes-producto-terminado-base-imprimible.component.ts          |
| Reportes                  | Faltante producto terminado         | GUI | reporte-de-faltantes-producto-terminado-base-imprimible.component.html        |
| Reportes                  | Faltante producto terminado         | GUI | reporte-de-faltantes-producto-terminado-base-imprimible.component.css         |
|                           |                                     | GUI | reporte.faltantes.productoTerminado.ts                                        |
|                           |                                     | API | reportes.faltanteProductoTerminado.js                                         |
| Reportes                  | Faltantes de almacen de produccion  | GUI | reporte-de-faltantes-almacen-de-produccion.component.ts                       |
| Reportes                  | Faltantes de almacen de produccion  | GUI | reporte-de-faltantes-almacen-de-produccion.component.html                     |
| Reportes                  | Faltantes de almacen de produccion  | GUI | reporte-de-faltantes-almacen-de-produccion.component.css                      |
| Reportes                  | Faltantes de almacen de produccion  | GUI | reporte-de-faltantes-alamcen-de-produccion-base-imprimible.component.ts       |
| Reportes                  | Faltantes de almacen de produccion  | GUI | reporte-de-faltantes-alamcen-de-produccion-base-imprimible.component.html     |
| Reportes                  | Faltantes de almacen de produccion  | GUI | reporte-de-faltantes-alamcen-de-produccion-base-imprimible.component.css      |
|                           |                                     | GUI | reporte.faltantes.almacenProduccion.ts                                        |
|                           |                                     | API | reporte.faltanteAlmacenProduccion.js                                          |
| Reportes                  | Seguimiento Ordenes                 | GUI | vista-seguimiento-ordenes.module.component.ts                                 |
| Reportes                  | Seguimiento Ordenes                 | GUI | vista-seguimiento-ordenes.component.ts                                        |
| Reportes                  | Seguimiento Ordenes                 | GUI | vista-seguimiento-ordenes.component.html                                      |
| Reportes                  | Seguimiento Ordenes                 | GUI | vista-seguimiento-ordenes.component.css                                       |
| Reportes                  | Seguimiento Ordenes                 | GUI | linea-tiempo-pildoras-seguimiento-ordenes.module.component.ts                 |
| Reportes                  | Seguimiento Ordenes                 | GUI | linea-tiempo-pildoras-seguimiento-ordenes.component.ts                        |
| Reportes                  | Seguimiento Ordenes                 | GUI | linea-tiempo-pildoras-seguimiento-ordenes.component.html                      |
| Reportes                  | Seguimiento Ordenes                 | GUI | linea-tiempo-pildoras-seguimiento-ordenes.component.css                       |
| Reportes                  | Seguimiento Ordenes                 | GUI | detalle-paso-linea-tiempo-pildoras.module.component.ts                        |
| Reportes                  | Seguimiento Ordenes                 | GUI | detalle-paso-linea-tiempo-pildoras.component.ts                               |
| Reportes                  | Seguimiento Ordenes                 | GUI | detalle-paso-linea-tiempo-pildoras.component.html                             |
| Reportes                  | Seguimiento Ordenes                 | GUI | detalle-paso-linea-tiempo-pildoras.component.css                              |
| Reportes                  | Seguimiento Ordenes                 | GUI | filtros-seguimiento-ordenes.module.component.ts                               |
| Reportes                  | Seguimiento Ordenes                 | GUI | filtros-seguimiento-ordenes.component.ts                                      |
| Reportes                  | Seguimiento Ordenes                 | GUI | filtros-seguimiento-ordenes.component.html                                    |
| Reportes                  | Seguimiento Ordenes                 | GUI | filtros-seguimiento-ordenes.component.css                                     |
| Reportes                  | Transformacion                      | GUI | programacion-transformacion-reporte.component.ts                              |
| Reportes                  | Transformacion                      | GUI | programacion-transformacion-reporte.component.html                            |
| Reportes                  | Transformacion                      | GUI | programacion-transformacion-reporte.component.css                             |
| Reportes                  | Transformacion                      | GUI | programacion-transformacion-imprimir.component.ts                             |
| Reportes                  | Transformacion                      | GUI | programacion-transformacion-imprimir.component.html                           |
| Reportes                  | Transformacion                      | GUI | programacion-transformacion-imprimir.component.css                            |
|                           |                                     | API | programacionTransformacion.route.js                                           |
|                           |                                     | API | reportes.js                                                                   |
| Ventas                    | Aprobado Cotizaciones               | GUI | aprobado-folios-vendedor.module.ts                                            |
| Ventas                    | Aprobado Cotizaciones               | GUI | aprobado-folios-vendedor.component.ts                                         |
| Ventas                    | Aprobado Cotizaciones               | GUI | aprobado-folios-vendedor.component.html                                       |
| Ventas                    | Aprobado Cotizaciones               | GUI | aprobado-folios-vendedor.component.css                                        |
|                           |                                     | API | aprobadoFolioVendedor.route.js                                                |
|                           |                                     | API | aprobadoFolioVendedor.controller.js                                           |
| Ventas                    | Mis Cotizaciones                    | GUI | folios-vendedor.module.ts                                                     |
| Ventas                    | Mis Cotizaciones                    | GUI | folios-vendedor.component.ts                                                  |
| Ventas                    | Mis Cotizaciones                    | GUI | folios-vendedor.component.html                                                |
| Ventas                    | Mis Cotizaciones                    | GUI | folios-vendedor.component.css                                                 |
| Ventas                    | Mis Cotizaciones                    | GUI | formulario-creacion-folio-vendedor.module.ts                                  |
| Ventas                    | Mis Cotizaciones                    | GUI | formulario-creacion-folio-vendedor.component.ts                               |
| Ventas                    | Mis Cotizaciones                    | GUI | formulario-creacion-folio-vendedor.component.html                             |
| Ventas                    | Mis Cotizaciones                    | GUI | formulario-creacion-folio-vendedor.component.css                              |
|                           |                                     | API | folioVendedor.model.js                                                        |
|                           |                                     | API | folioVendedor.route.js                                                        |
|                           |                                     | API | folioVendedor.controller.js                                                   |
|                           |                                     | API | folioVendedor.service.js                                                      |
| Ventas                    | Mis folios                          | GUI | prueba-para-detalles.component.ts                                             |
| Ventas                    | Mis folios                          | GUI | prueba-para-detalles.component.html                                           |
| Ventas                    | Mis folios                          | GUI | folios.component.ts                                                           |
| Ventas                    | Mis folios                          | GUI | folios.component.html                                                         |
| Ventas                    | Mis folios                          | GUI | folios.component.css                                                          |
| Ventas                    | Mis folios                          | GUI | folios-crear-modificar.component.ts                                           |
| Ventas                    | Mis folios                          | GUI | folios-crear-modificar.component.html                                         |
| Ventas                    | Mis folios                          | GUI | folios-crear-modificar.component.html.back.html                               |
| Ventas                    | Mis folios                          | GUI | folios-crear-modificar-abstracto.component.ts                                 |
| Ventas                    | Mis folios                          | GUI | folios-crear-modificar-abstracto.component.html                               |
|                           |                                     | API | folio.js                                                                      |
|                           |                                     | API | folioLinea.js                                                                 |
|                           |                                     | API | orden.js                                                                      |
|                           |                                     | API | folio.route.js                                                                |
|                           |                                     | API | folio.service.js                                                              |
|                           |                                     | API | orden.js                                                                      |
|                           |                                     | API | procesos.js                                                                   |
| Ventas                    | Revisión Crédito Y Cobranza         | GUI | revision-credito-y-cobranza.module.ts                                         |
| Ventas                    | Revisión Crédito Y Cobranza         | GUI | revision-credito-y-cobranza.component.ts                                      |
| Ventas                    | Revisión Crédito Y Cobranza         | GUI | revision-credito-y-cobranza.component.html                                    |
| Ventas                    | Revisión Crédito Y Cobranza         | GUI | revision-credito-y-cobranza.component.css                                     |
|                           |                                     | API | revisionCreditoYCobranzaFolioVendedor.route.js                                |
|                           |                                     | API | revisionCreditoYCobranzaFolioVendedor.controller.js                           |
|                           |                                     | API | revisionCreditoYCobranzaFolioVendedor.service.js                              |
| Ventas                    | Supervisión Cotizaciones            | GUI | supervision-folios-vendedor.module.ts                                         |
| Ventas                    | Supervisión Cotizaciones            | GUI | supervision-folios-vendedor.component.ts                                      |
| Ventas                    | Supervisión Cotizaciones            | GUI | supervision-folios-vendedor.component.html                                    |
| Ventas                    | Supervisión Cotizaciones            | GUI | supervision-folios-vendedor.component.css                                     |
|                           |                                     | API | supervisionFolioVendedor.route.js                                             |
|                           |                                     | API | supervisionFolioVendedor.controller.js                                        |
| Ventas                    |                                     | GUI | estatus-folios-vendedor.module.ts                                             |
| Ventas                    |                                     | GUI | estatus-folios-vendedor.component.ts                                          |
| Ventas                    |                                     | GUI | estatus-folios-vendedor.component.html                                        |
| Ventas                    |                                     | GUI | estatus-folios-vendedor.component.css                                         |
| Ventas                    |                                     | GUI | detalle-folio-vendedor.module.ts                                              |
| Ventas                    |                                     | GUI | detalle-folio-vendedor.component.ts                                           |
| Ventas                    |                                     | GUI | detalle-folio-vendedor.component.html                                         |
| Ventas                    |                                     | GUI | detalle-folio-vendedor.component.css                                          |
| Ventas                    |                                     | GUI | filtros-folios-vendedor.module.ts                                             |
| Ventas                    |                                     | GUI | filtros-folios-vendedor.component.ts                                          |
| Ventas                    |                                     | GUI | filtros-folios-vendedor.component.html                                        |
| Ventas                    |                                     | GUI | filtros-folios-vendedor.component.css                                         |
| Ventas                    |                                     | GUI | impresion-folios-vendedor.module.ts                                           |
| Ventas                    |                                     | GUI | impresion-folios-vendedor.component.ts                                        |
| Ventas                    |                                     | GUI | impresion-folios-vendedor.component.html                                      |
| Ventas                    |                                     | GUI | impresion-folios-vendedor.component.css                                       |
| Registros                 |                                     | GUI | scanner-formulario-dinamico.component.ts                                      |
| Registros                 |                                     | GUI | scanner-formulario-dinamico.component.html                                    |
| Registros                 |                                     | GUI | scanner-formulario-dinamico.component.css                                     |
| Registros                 |                                     | GUI | scanner-formulario-dinamico-maquinas.component.ts                             |
| Registros                 |                                     | GUI | scanner-formulario-dinamico-maquinas.component.html                           |
| Registros                 |                                     | GUI | scanner-formulario-dinamico-maquinas.component.css                            |
| Registros                 |                                     | GUI | dynamic-form.component.ts                                                     |
| Registros                 |                                     | GUI | dynamic-form.component.html                                                   |
| Registros                 |                                     | GUI | dynamic-form.component.css                                                    |
| Registros                 |                                     | GUI | dynamic-form-question.component.ts                                            |
| Registros                 |                                     | GUI | dynamic-form-question.component.html                                          |
| Registros                 |                                     | GUI | dynamic-form-question.component.css                                           |
| Registros                 |                                     | GUI | question.service.ts                                                           |
| Registros                 |                                     | GUI | ordenes-por-departamento-en-procesos.component.ts                             |
| Registros                 |                                     | GUI | ordenes-por-departamento-en-procesos.component.html                           |
| Registros                 |                                     | GUI | ordenes-por-departamento-en-procesos.component.css                            |
|                           |                                     | GUI | socket.service.ts                                                             |
|                           |                                     | API | socket.service.js                                                             |
|                           |                                     | API | whatsapp.service.js                                                           |
|                           |                                     | API | colors.js                                                                     |
|                           |                                     | API | constantes.js                                                                 |
|                           |                                     | API | extencionesFicherosValidas.utils.js                                           |
|                           |                                     | API | parsearBody.js                                                                |
|                           |                                     | API | parsearMarkdown.js                                                            |
|                           |                                     | API | respStatus.js                                                                 |
|                           |                                     | API | validaciones.js                                                               |
|                           |                                     | API | varios.js                                                                     |
|                           |                                     | API | reportesControlScrap.service.js                                               |
|                           |                                     | API | reporte.js                                                                    |
|                           |                                     | GUI | config.prod.ts                                                                |
|                           |                                     | GUI | config.ts                                                                     |
|                           |                                     | GUI | defaultModelData.ts                                                           |
|                           |                                     | GUI | departamentos.ts                                                              |
|                           |                                     | GUI | departamentosConfig.ts                                                        |
|                           |                                     | GUI | nivelesDeUrgencia.ts                                                          |
|                           |                                     | GUI | permisos.config.ts                                                            |
|                           |                                     | GUI | permisosKeys.config.ts                                                        |
|                           |                                     | GUI | procesos.ts                                                                   |
|                           |                                     | GUI | roles.const.ts                                                                |
|                           |                                     | GUI | roles.model.ts                                                                |
|                           |                                     | GUI | contiene-el-permiso.pipe.ts                                                   |
|                           |                                     | GUI | fecha-diferencia.pipe.ts                                                      |
|                           |                                     | GUI | fecha.pipe.ts                                                                 |
|                           |                                     | GUI | imagen.pipe.ts                                                                |
|                           |                                     | GUI | modelo-completo.pipe.ts                                                       |
|                           |                                     | GUI | parsear-camelcase.pipe.ts                                                     |
|                           |                                     | GUI | parsear-fecha.pipe.ts                                                         |
|                           |                                     | GUI | pipe-dinamico.pipe.ts                                                         |
|                           |                                     | GUI | pipes.module.ts                                                               |
|                           |                                     | GUI | tiempo-faltante.pipe.ts                                                       |
|                           |                                     | GUI | tiempo-transcurrido-informal.pipe.ts                                          |
|                           |                                     | GUI | elastic-textarea.directive.ts                                                 |
|                           |                                     | GUI | elastic-textarea.module.ts                                                    |
|                           |                                     | GUI | sort.service.ts                                                               |
|                           |                                     | GUI | sortable-table.directive.ts                                                   |
|                           |                                     | GUI | ordenador-de-columnas.directive.ts                                            |
|                           |                                     | GUI | carga-de-imagenes.component.ts                                                |
|                           |                                     | GUI | carga-de-imagenes.component.html                                              |
|                           |                                     | GUI | carga-de-imagenes.component.css                                               |
|                           |                                     | GUI | carga-de-imagenes.transporte.ts                                               |
|                           |                                     | GUI | toFormData.ts                                                                 |
|                           |                                     | GUI | toResponseBody.ts                                                             |
|                           |                                     | GUI | uploadProgress.ts                                                             |
|                           |                                     | GUI | visor-de-imagenes-general.component.ts                                        |
|                           |                                     | GUI | visor-de-imagenes-general.component.html                                      |
|                           |                                     | GUI | visor-de-imagenes-general.component.css                                       |
|                           |                                     | GUI | spinner-boton.component.ts                                                    |
|                           |                                     | GUI | spinner-boton.component.html                                                  |
|                           |                                     | GUI | spinner-boton.component.css                                                   |
|                           |                                     | GUI | sidebar.component.ts                                                          |
|                           |                                     | GUI | sidebar.component.html                                                        |
|                           |                                     | GUI | validacion-inputs.module.ts                                                   |
|                           |                                     | GUI | validacion-inputs.component.ts                                                |
|                           |                                     | GUI | validacion-inputs.component.html                                              |
|                           |                                     | GUI | historial-elemento.module.ts                                                  |
|                           |                                     | GUI | historial-elemento.component.ts                                               |
|                           |                                     | GUI | historial-elemento.component.html                                             |
|                           |                                     | GUI | historial-elemento.component.css                                              |
|                           |                                     | GUI | historial-elemento.model.ts                                                   |
|                           |                                     | API | historial.js                                                                  |
|                           |                                     | API | registroHistorial.model.js                                                    |
|                           |                                     | GUI | seleccionador-rango-fecchas.component.ts                                      |
|                           |                                     | GUI | seleccionador-rango-fecchas.component.html                                    |
|                           |                                     | GUI | seleccionador-rango-fecchas.component.css                                     |
|                           |                                     | GUI | buscador-paciente.component.ts                                                |
|                           |                                     | GUI | buscador-paciente.component.html                                              |
|                           |                                     | GUI | buscador-rapido.component.ts                                                  |
|                           |                                     | GUI | buscador-rapido.component.html                                                |
|                           |                                     | GUI | buscador-rapido.service.ts                                                    |
|                           |                                     | GUI | buscador-rapido.ts                                                            |
|                           |                                     | GUI | paginador.component.ts                                                        |
|                           |                                     | GUI | paginador.component.html                                                      |
|                           |                                     | GUI | paginador.component.css                                                       |
|                           |                                     | GUI | paginacion.util.ts                                                            |
|                           |                                     | GUI | paginador.service.ts                                                          |
|                           |                                     | GUI | paginador.component.ts                                                        |
|                           |                                     | GUI | paginador.component.html                                                      |
|                           |                                     | GUI | utilidades.service.ts                                                         |
|                           |                                     | GUI | elemento-desplegable.module.ts                                                |
|                           |                                     | GUI | elemento-desplegable.component.ts                                             |
|                           |                                     | GUI | elemento-desplegable.component.html                                           |
|                           |                                     | GUI | elemento-desplegable.component.css                                            |
|                           |                                     | GUI | pre-loader.component.ts                                                       |
|                           |                                     | GUI | pre-loader.component.html                                                     |
|                           |                                     | GUI | pre-loader.component.css                                                      |
|                           |                                     | GUI | pre-loader.service                                                            |
|                           |                                     | GUI | sidebar-modal.module.ts                                                       |
|                           |                                     | GUI | sidebar-modal.component.ts                                                    |
|                           |                                     | GUI | sidebar-modal.component.html                                                  |
|                           |                                     | GUI | sidebar-modal.component.css                                                   |
|                           |                                     | GUI | modal.module.ts                                                               |
|                           |                                     | GUI | modal.component.ts                                                            |
|                           |                                     | GUI | modal.component.html                                                          |
|                           |                                     | GUI | carrusel-imagenes-generico.module.ts                                          |
|                           |                                     | GUI | carrusel-imagenes-generico.component.ts                                       |
|                           |                                     | GUI | carrusel-imagenes-generico.component.html                                     |
|                           |                                     | GUI | carrusel-imagenes-generico.component.css                                      |
|                           |                                     | GUI | lector-plantillas-excel-generico.module.ts                                    |
|                           |                                     | GUI | lector-plantillas-excel-generico.component.ts                                 |
|                           |                                     | GUI | lector-plantillas-excel-generico.component.html                               |
|                           |                                     | GUI | lector-plantillas-excel-generico.component.css                                |
|                           |                                     | GUI | detalle-generico-formulario.module.ts                                         |
|                           |                                     | GUI | detalle-generico-formulario.component.ts                                      |
|                           |                                     | GUI | detalle-generico-formulario.component.html                                    |
|                           |                                     | GUI | detalle-generico-formulario.component.css                                     |
|                           |                                     | GUI | tabla-generica.module.ts                                                      |
|                           |                                     | GUI | tabla-generica.component.ts                                                   |
|                           |                                     | GUI | tabla-generica.component.html                                                 |
|                           |                                     | GUI | tabla-generica.servicio.ts                                                    |
|                           |                                     | GUI | tiempo-transcurrido.module.ts                                                 |
|                           |                                     | GUI | tiempo-transcurrido.component.ts                                              |
|                           |                                     | GUI | tiempo-transcurrido.component.html                                            |
|                           |                                     | GUI | tiempo-transcurrido.component.css                                             |
|                           |                                     | GUI | boton-para-imprecion.component.ts                                             |
|                           |                                     | GUI | boton-para-imprecion.component.html                                           |
|                           |                                     | GUI | boton-para-imprecion.component.css                                            |
|                           |                                     | GUI | gestor-de-impresiones.component.ts                                            |
|                           |                                     | GUI | gestor-de-impresiones.component.html                                          |
|                           |                                     | GUI | gestor-de-impresiones.component.css                                           |
|                           |                                     | GUI | impresion.service.ts                                                          |
|                           |                                     | GUI | selector-fechas-generico.module.ts                                            |
|                           |                                     | GUI | selector-fechas-generico.component.ts                                         |
|                           |                                     | GUI | selector-fechas-generico.component.html                                       |
|                           |                                     | GUI | selector-fechas-generico.component.css                                        |
|                           |                                     | GUI | selector-fechas-modal.module.ts                                               |
|                           |                                     | GUI | selector-fechas-modal.component.ts                                            |
|                           |                                     | GUI | selector-fechas-modal.component.html                                          |
|                           |                                     | GUI | selector-fechas-modal.component.css                                           |
|                           |                                     | GUI | crud.ts                                                                       |
|                           |                                     | GUI | camposParaMostrarFiltrosGeneral.ts                                            |
|                           |                                     | GUI | visor-de-imagenes-con-paginacion.component.ts                                 |
|                           |                                     | GUI | visor-de-imagenes-con-paginacion.component.html                               |
|                           |                                     | GUI | visor-de-imagenes-con-paginacion.component.css                                |
|                           |                                     | GUI | data-list.component.ts                                                        |
|                           |                                     | GUI | data-list.component.html                                                      |
|                           |                                     | GUI | data-list.component.css                                                       |
|                           |                                     | GUI | data-list.module.ts                                                           |
|                           |                                     | GUI | escaner-generico-qr.component.ts                                              |
|                           |                                     | GUI | escaner-generico-qr.component.html                                            |
|                           |                                     | GUI | escaner-generico-qr.component.css                                             |
|                           |                                     | GUI | escaner-generico-qr.service.ts                                                |