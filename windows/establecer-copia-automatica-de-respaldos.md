### [< Directorio](../directorio.md)

# Establecer copia automática de respaldo en Windows

Para que los respaldos se puedan copiar automáticamente desde cualquier ubicación,
se recomienda generar una tarea automatizada que haga uso de scripts que se
mencionarán más adelante.

También es importante recalcar que, para llevar a cabo el procedimiento, se debe
configurar el BIOS para que encienda la computadora donde se planea guardar el
respaldo (en caso de que sea una computadora y no un servidor y que esta se apague 
regularmente).
## Requisitos

1. Programar auto-encendido en BIOS (opcional)

Ver [búsqueda de cómo programar auto-encendido](https://www.google.com.mx/search?q=BIOS+auto+encendido&sca_esv=577233357&source=hp&ei=nAg8ZaexKOrHkPIPtZO_sAg&iflsig=AO6bgOgAAAAAZTwWrDgB9y9a7h8c-l2c7rcZrgTAduIl&ved=0ahUKEwin76HT9JaCAxXqI0QIHbXJD4YQ4dUDCAo&uact=5&oq=BIOS+auto+encendido&gs_lp=Egdnd3Mtd2l6IhNCSU9TIGF1dG8gZW5jZW5kaWRvMgUQIRigATIFECEYoAFI3lZQ8wRYqTdwA3gAkAEAmAHTAaABzRiqAQYwLjIwLjG4AQPIAQD4AQGoAgrCAhAQABgDGI8BGOUCGOoCGIwDwgIQEC4YAxiPARjlAhjqAhiMA8ICBRAuGIAEwgIREC4YgAQYsQMYgwEYxwEY0QPCAgsQABiABBixAxiDAcICCBAAGIAEGLEDwgIIEC4YgAQYsQPCAgsQABiKBRixAxiDAcICCxAuGIoFGLEDGIMBwgIFEAAYgATCAgQQABgDwgIIEAAYigUYsQPCAg0QABiABBixAxiDARgKwgIHEAAYgAQYCsICBhAAGBYYHg&sclient=gws-wiz)

  > Depende del modelo y marca de la placa base.
  >
  > Está fuertemente recomendado que la hora de encendido sea ANTES de las 12:30 a. m.

2. El repositorio bwripts

Ver [bwripts](https://github.com/Carrduci/bwripts)

  > Al ser un repositorio privado, se requiere una cuenta de GitHub, que esta esté en la organización [Carrduci](https://github.com/orgs/Carrduci) y tener un token de GitHub generado (GitHub no permite iniciar 
  > sesión en la terminal con contraseña). En caso de no tener acceso, solicitárselo al administrador de la organización.
## Procedimiento

Se da por hecho que ya se configuró el auto-arranque en el BIOS. También que ya 
se tiene un usuario de GitHub con sesión iniciada y que está incluido en la
organización.

### 1. Obtener el repositorio

Clonar el repositorio en el lugar que se desee con el siguiente comando:

```
git clone https://github.com/Carrduci/bwripts
```
### 2. Establecer las tareas automáticas en Windows

Abrir el programador de tareas presionando `Win` + `R` y pegar el siguiente nombre:

```
taskschd.msc
```

![](../assets/imagenes/abrir_programador_tareas.png)

![](../assets/imagenes/ejemplo_programador_tareas.png)

Crear una nueva carpeta para crear una serie de tareas dando clic en `Biblioteca del Programador de tareas` y poner el nombre que se desee:
![](../assets/imagenes/crear_carpeta_en_programador_tareas.png)

Lo que debe resultar en algo parecido a esto
![](../assets/imagenes/nueva_carpeta_en_programador_tareas.png)

Presionar `Crear tarea básica...` en el panel lateral izquierdo

![](../assets/imagenes/nueva_tarea_en_programador_tareas.png)

Luego agregar un nombre a la tarea:

![](../assets/imagenes/nombre_tarea_creada.png)

Establecer entonces que se ejecute a diario:

![](../assets/imagenes/seleccion_diariamente_tarea_creada.png)

Y marcar en la casilla de hora lo siguiente (también seleccionar sincronizar zonas horarias):

![](../assets/imagenes/hora_fuertemente_recomendada_para_copiar_respaldo.png)

Asegurarse de que sea la misma hora y no tocar las otras casillas.

Seleccionar la acción que se desea realizar:

![](../assets/imagenes/seleccion_accion_tarea_creada.png)

Después va a solicitar la línea de comando. Poner los siguientes valores en sus casillas correspondientes:
##### Programa o script
```
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
```
##### Agregar argumentos (opcional) 

> No es que sea opcional, así se llama el campo

```
-NoLogo -NonInteractive -File "<ruta_del_repositorio>\bwripts\pwsh\respaldos_carrduci_sys_copia_windows\copiar_respaldo_csys.ps1"
```

Asegurarse de reemplazar `<ruta_del_repositorio>` con la ruta donde se clonó bwripts.

![](../assets/imagenes/seleccion_comandos_tarea_creada.png)

Seleccionar la siguiente casilla en el panel que sale en `Finalizar`:

![](../assets/imagenes/seleccion_cuadro_dialogo_tarea_creada.png)

También marcar las siguientes casillas en el panel que se abre para que la script se pueda ejecutar 
aunque no esté iniciada la sesión.

![](../assets/imagenes/seleccion_panel_usar_como_administrador_tarea_creada.png)

Y finalmente asegurarse que en la parte inferior (Configurar para:) diga `Windows 10`.

El resultado se debe ver como el siguiente:

![](../assets/imagenes/resultado_final_tarea_creada.png)

### Apagado automático (opcional)

En caso de que se programe encendido automático, es buena idea que también se apague la computadora luego de terminar. Para hacerlo, se puede programar una tarea automática usando el ejecutable `shutdown.exe`.

Se recomienda configurar la tarea a las 2:00 a. m. (no mover el campo de inicio):

![](../assets/imagenes/hora_tarea_apagado.png)

Seleccionar `Iniciar un programa` e ingresar los siguientes comandos:
##### Programa o script
```
C:\Windows\System32\shutdown.exe
```
##### Agregar argumentos (opcional) 

> No es que sea opcional, así se llama el campo

```
/s /f /t 0
```

![](../assets/imagenes/argumentos_tarea_apagar.png)

Y del mismo modo que en las tareas de copia de respaldo, en el apartado de finalizar, marcar la opción "**Abrir el diálogo Propiedades para esta tarea . . .**" para que se nos abra el cuadro de diálogo con el mismo nombre. En este cuadro de dialogo marcar también las opciones: "**Ejecutar tanto si el usuario inició sesión como si no**" y "**Ejecutar con los privilegios más altos**".
### IMPORTANTE

Se debe repetir el procedimiento anterior para crear una segunda tarea con la única diferencia
de que esté programada a las 12:30:00 p. m.

> La ejecución de la script de copia va a buscar dos discos para realizar la tarea, el `D:\RESPALDOS_CSYS\` y el `F:\RESPALDOS_CSYS\`