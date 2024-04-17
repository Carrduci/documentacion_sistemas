### [< Directorio](../directorio.md)

# Catálogo de archivos por por módulo
Este catálogo busca asistir la búsqueda de archivos que se requieren tener
en cuenta para modificar los componentes de CARRDUCIsys.

>La separación del catálogo se basa en los apartados y títulos de la barra lateral
del sistema, que es el único punto de acceso para los usuarios.

Los componentes en angular se basan en el modelo `VISTA - CONTROLADOR`, y usan
una notacion para nombrar los archivos:

```
<nombre_componente>.component.<extension>
```
Ejemplo de archivos varios de un componente. Aqui se incluye el modulo, que es otro tipo
de archivo, porque se tiene la intención de que cada componente tenga su módulo (más adelante
que sean standalone).

``` 
    CONTROLADOR:  unComponente.component.ts
    VISTA:        unComponente.component.html
    HOJA ESTILOS: unComponente.component.css
    PRUEBAS:      unComponente.component.spec.ts
    -----------------------------------------------
    MODULO:       unComponente.module.ts
```

Lo unico que cambia es la extension, por lo que para nombrar un componente en este índice, se omitirá
esta última.

Hay dos tipos de archivos más, el `model` y el `service`. El `model` es para poner las clases e interfaces que servirán para modelar los datos que se reciban desde el api, y el `service` es para
poner todas las funciones que nos sirvan para transferir datos o calcularos, por ejemplo, las funciones
que consultan al api, o calculos especificos como el estatus de algo y por lo general se relacionan
con un modelo (comparten nombre), pero se pueden nombrar como la situación lo demande:

```
    MODELO: usuario.model.ts
    SERVICIO: usuario.service.ts
```




## Índice
### 1. Avisos
1. Dasboard
    | DESCRIPCIÓN | ARCHIVO               |
    | ----------- | --------------------- |
    | Principal   | `dashboard.component` |
### 2. Almacen
1. Produccion
    | DESCRIPCIÓN              | ARCHIVO                                   |
    | ------------------------ | ----------------------------------------- |
    | Principal                | `almacen-produccion.component`            |
    | Generador Reportes E/S   | `reporte-es-almacen-produccion.component` |
    | Crear-Modificar Artículo | `articulo-crear-modificar.component`      |
2. Produccion - ES
    | DESCRIPCIÓN   | ARCHIVO                                                                       |
    | ------------- | ----------------------------------------------------------------------------- |
    | Principal     | `almacen-es.component`                                                        |
    | Crear Salida  | `almacen-de-materia-prima-yherramientas-crear-modificar-salida.component`     |
    | Crear Entrada | `almacen-de-materia-prima-yherramientas-crear-modificar-entrada.component.ts` |
3. Producción - IAP
    #### PENDIENTE
4. Producto terminado
5. Reportes personalizados
6. Requisiciones
### 3. Administrador
### 4. Compras
### 5. Control de Producción
### 6. Dispositivos Electrónicos
### 7. Gráficos
### 8. Ingeniería
### 9. Mantenimiento
### 10. Parametros
### 11. RH
### 12. Reportes
### 13. Ventas
### 14. Registros

