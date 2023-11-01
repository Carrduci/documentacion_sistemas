### [< Directorio](../directorio.md)

# Desplegar CARRDUCIsys

El propósito es proveer información sobre el despliegue de las scripts o tareas 
programadas que llevan a cabo la implementación de CARRDUCIsys. Los respaldos de las **bases de datos** y 
**fotografías** vienen integrados y no se necesita ver por separado, solo programar una tarea para copiarlos
en la ubicación (fuera del servidor) donde se van a almacenar.
## Requerimientos

1. El repositorio utilidades_carrduci_sys

Ver [utilidades_carrduci_sys](https://github.com/Carrduci/utilidades_carrduci_sys)

  > Al ser un repositorio privado, se requiere una cuenta de GitHub, que esta esté en la organización 
  > [Carrduci](https://github.com/orgs/Carrduci) y tener un token de GitHub generado (GitHub no permite iniciar 
  > sesión en la terminal con contraseña). En caso de no tener acceso, solicitárselo al administrador de la organización.
  
1. Instalar el Sub Sistema  de Linux

Ver [Subsistema De Linux](https://learn.microsoft.com/es-es/windows/wsl/install).

3.  Saber establecer una conexión ssh a un equipo remoto con Linux

  >En este caso es `ubuntu server`

Ver [coneccion-ssh.md](../ubuntu-serverr/conexion-ssh.md) y 
[configurar-ubuntu-server.md](../ubuntu-serverr/configurar-ubuntu-server.md)

4. Tener Docker instalado y haber iniciado sesión

Ver [uso-docker.md](../docker/uso-docker.md)
  
## Procedimiento

### 1. Establecer conexión con el servidor
> Para este paso ya debe existir un servidor configurado (con ip fija) y tener acceso a la red 
> interna. El equipo desde el que se hará el procedimiento también debe contar con acceso a la
> red.

Asegurarse de que el equipo esté en la misma red que el servidor de CARRDUCIsys e ingresar el 
siguiente comando en la terminal de wsl:

```
ssh <usuario_servidor>@<direccion.ip.servidor>
```
Ejemplo: `ssh carrduci@192.168.149`

A continuación nos pedirá la contraseña que el usuario al que estamos accediendo tiene

### 2. Clonar `utilidades_carrduci_sys`
> Esto ocurre una vez que hay una conexión al servidor, es decir, dentro de.
> Realizar este paso solamente si el repositorio no se encuentra ya clonado en la ruta `~`

Se debe ejecutar el siguiente comando en la terminal, ubicándose en la ruta `~` (asumiendo configuraciones de git realizadas):

```
git clone https://github.com/Carrduci/utilidades_carrduci_sys
```

Esto hará que git pida usuario y contraseña:
```
Cloning into 'utilidades_carrduci_sys'...
Username for 'https://github.com': Usuario
Password for 'https://Usuario@github.com':
```

Ingresar los datos para poder realizar la clonación, lo que debe concluir con algo parecido a:
```
remote: Enumerating objects: 102, done.
remote: Counting objects: 100% (102/102), done.
remote: Compressing objects: 100% (67/67), done.
remote: Total 102 (delta 43), reused 88 (delta 32), pack-reused 0
Receiving objects: 100% (102/102), 13.16 KiB | 6.58 MiB/s, done.
Resolving deltas: 100% (43/43), done.
```

### 3. Ejecutar la script de actualización

```
~/utilidades_carrduci_sys/docker-carrduci-sys/aplicar-actualizacion-docker-servidor.sh
```

Lo que debe resultar en algo así:
![](../assets/gifs/desplegar_actualizacion_carrduci_sys.gif)
## Respaldos

Aunque los respaldos vienen integrados en la script anterior, es necesario configurar la
carpeta donde se guardan para que sea accesible desde la red. Esto se logra desplegando
un servidor samba simple. [¿Cómo desplegar el servidor samba?](servidor-samba-carpeta-respaldos.md)

### Restaurar último respaldo

Para restaurar la base de datos e imágenes, lo ideal es buscar el último respaldo generado. para ello hay dos opciones, copiar el respaldo desde Windows al servidor y luego restaurarlo (en caso de que no haya respaldos disponibles en este mismo) u obtener el último respaldo y restaurarlo.

#### 1. Copiar desde Windows y restaurar 

Es necesario utilizar el comando `scp` que se refiere en inglés a **Secure Copy**. Este comando nos permite copiar archivos a través de una conexión remota a Linux, pero si se debe hacer desde Windows, es requerido usar el subsistema de Linux (wsl) y  es preferible que el servidor al que se va a conectar tenga una ip fija.

Asumiendo que ya está abierta una instancia de wsl y que la carpeta a la que se, hay que escribir un comando con la siguiente estructura:
```
scp <archivo_a_copiar> <usuario_linux>@<direccion_ip_computadora>:<direccion_carpeta_respaldos>
```

Este ejemplo asumo que la carpeta que va a recibir los respaldos tiene los permisos de escritura correspondientes para poder copiar desde una fuente externa:
```
scp /mnt/d/RESPALDOS_CSYS/respaldo_carrduci_sys_bd-1698775200_10-31-23_12.10.tgz carrduci@192.168.1.149:~/respaldos_csys/
```

>En este caso se accede a la carpeta `/mnt/d` porque se requiere acceder al disco D: de la computadora donde se realizó la muestra. Lo importante es poner el directorio donde estén almacenados los respaldos y que estos sean accesibles. El nombre del archivo `.tgz` también puede cambiar dependiendo de la fecha en que se haya generado el respaldo. La carpeta `~/respaldos_csys/ ` es la que se va a generar siempre que se **despliegue CARRDUCIsys correctamente**.

Una vez copiado el archivo, hay que asegurarse que sea el único en la carpeta del servidor Linux en la que se acaba de copiar.

Por último, para restaurar, ver la opción **2**.

#### 2. Obtener el último respaldo y restaurarlo

Para esto hay que recurrir nuevamente a `utilidadades_carrrduci`.  Basta con ejecutar lo siguiente:
```
~/utilidades_carrduci_sys/mongo/restaurar_respaldo.sh ~/respaldos_csys
```

Lo que debe tener un resultado algo así:
