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

para restaurar respaldos, ir [aquí](restauracion_respaldos.md).
