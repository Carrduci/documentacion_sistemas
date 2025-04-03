### [< Directorio](../directorio.md)

Antes se debió seguir [generación certificados](./1-generacion-certificados.md).
# Instalar certificado de CARRDUCIsys en computadora de usuario
De preferencia, CARRDUCIsys debe ser usado en navegadores basados en Chromium: **Chrome**, **Edge**, **Brave**. La instalación es muy similar en los 3, pero solo se mostrará cómo hacerlo en Edge.
## Instalación en Edge
Una vez abierto el navegador, agregar la siguiente url en la barra de direcciones:
```
<navegador>://settings/privacy
```
Reemplazar la primera palabra dependiendo del navegador:
- Chrome: `chrome`
- Edge `edge`
- Brave: `brave`

![](../assets/imagenes/certificado_edge_config.png)

Moverse hacia abajo hasta la parte de **Seguridad** y dar clic en **Administrar certificados**.

![](../assets/imagenes/certificado_edge_abrir.png)

Se debe abrir un recuadro. En ese recuadro, asegurarse de tener seleccionada la pestaña **`Entidades de certificación raíz de confianza`**. Luego dar clic en **Importar**. 

![](../assets/imagenes/certificado_edge_panel_importar.png)

Luego aparece esta otro recuadro. Dar clic en siguiente.

![](../assets/imagenes/certificado_edge_siguiente.png)

En el siguiente recuadro, dar clic en **Examinar**.

![](../assets/imagenes/certificado_edge_panel_examinar.png)

Una vez seleccionado el archivo, dar clic en siguiente.

![](../assets/imagenes/certificado_edge_archivo_seleccionado.png)

En la siguiente vista dejar todo igual y dar clic en siguiente.

![](../assets/imagenes/certificado_edge_archivo_dejar_todo_igual.png)

Y dar clic en finalizar.certificado_edge_instalar_si.png

![](../assets/imagenes/certificado_edge_finalizar.png)

Después debe aparecer este recuadro. Va a preguntar si instalar certificado. Asegurarse que diga "CARRDUCIsys" y dar clic en sí.

![](../assets/imagenes/certificado_edge_instalar_si.png)

Se mostrará entonces una confirmación de que se completó el proceso. Dar clic en aceptar.

![](../assets/imagenes/certificado_edge_terminado_aceptar.png)

De vuelta al recuadro de Certificados, solo falta comprobar que en la tabla de la pestaña **`Entidades de certificación raíz de confianza`** halla una fila que diga **CARRDUCIsys**.

![](../assets/imagenes/certificado_edge_terminado_comprobar.png)

Entonces se puede dar clic en **Cerrar**, quedando completado este procedimiento.