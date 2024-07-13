### [< Directorio](../directorio.md)

# Catálogo de archivos por por módulo (GUI)
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




## Índice basado en el menú lateral
### 1. Avisos
1. Dasboard

| DESCRIPCIÓN | ARCHIVO     |
| ----------- | ----------- |
| Principal   | `dashboard` |
### 2. Almacén
1. Producción

| DESCRIPCIÓN              | ARCHIVO                         |
| ------------------------ | ------------------------------- |
| Principal                | `almacen-produccion`            |
| Generador reportes E/S   | `reporte-es-almacen-produccion` |
| Crear-modificar artículo | `articulo-crear-modificar`      |
| Servicio de art          |                                 |
|                          |                                 |
|                          |                                 |
1. Producción - ES

| DESCRIPCIÓN   | ARCHIVO                                                          |
| ------------- | ---------------------------------------------------------------- |
| Principal     | `almacen-es`                                                     |
| Crear Salida  | `almacen-de-materia-prima-yherramientas-crear-modificar-salida`  |
| Crear Entrada | `almacen-de-materia-prima-yherramientas-crear-modificar-entrada` |


1. Producción - IAP
1. Producto terminado
2. Reportes personalizados
3. Requisiciones

### 3. Administrador
1. Almacen descripcion
2. Areas
3. Clientes
4. Departamentos
5. Indexador
6. Usuarios
### 4. Compras
1. Divisas
2. Proveedores
### 5. Control de Producción
1. Asignar ordenes
2. Material no conforme
3. Reportes escaneres
4. Revision de folios
5. Seguimientos
### 6. Dispositivos Electrónicos
1. Dispositivos asistencia
### 7. Gráficos
1. Ordenes Trabajando
### 8. Ingeniería
1. Colores
2. Maquinas
3. Modelos
4. Procesos
5. Procesos - Familias
6. SKU - Produccion
7. Tamanos
8. Terminados
### 9. Mantenimiento
1. Bitácora
2. Maquinas
3. Tipos Maquinas
### 10. Parametros
1. Ajustes Control Scrap
2. Ajustes Mantenimientos Maquinas
3. Clientes especiales
4. Crear estaciones de escaneo
5. Localizacion de ordenes
6. Procesos Especiales
7. Restablecer o cambiar administrador
### 11. RH
1. Checadores
2. Checadores - Areas
3. Checadores - Usuarios
4. Cursos
5. Empleados
6. Horarios
7. Puestos
### 12. Reportes
1. Faltante producto terminado
2. Faltantes almacen de produccion
3. Personalizados
4. Seguimiento Ordenes
5. Transformacion
### 13. Ventas
1. Aprobado Cotizaciones
2. Mis Cotizaciones
3. Mis Folios
4. Revisión Crédito Y Cobranza
5. Supervisión Cotizaciones
### 14. Registros


## Componentes y servicios de utilidades

### 1. Componentes
1. Paginadores
2. Tabla Genérica
3. Modal
4. Buscador Paciente
5. Validación Inputs
### 2. Servicios

