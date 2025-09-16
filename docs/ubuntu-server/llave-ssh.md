# Generar llave SSH

Para poder establecer conexiones ssh con el servidor sin usar autenticación por contraseña, hay que generar un par de llaves especiales, una pública, que se coloca en el servidor y sirve para autenticar usuarios y encriptación, y una privada, que el usuario debe resguardar y sirve para desencriptar la información encriptada con la llave pública.

Para generar un par de llaves, ejecutar lo siguiente en la terminal de linux (o del subsistema) en tu computadora, **NO** en el servidor:

```sh
ssh-keygen
```

Se pedirá la ubicación y nombre del archivo, así como una contraseña para protejer la llave (opcional).

Si no se le pone contraseña a la llave, cualquiera con acceso a la computadora tiene acceso a las llaves, y por consecuente al servidor que tenga las llaves agregadas.

```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/<usuario>/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

Por ejemplo, para el servidor de carrduci-sys, se podría usar el siguiente nombre.

?> Reemplazar `<usuario>` por tu nombre de usuario de linux.

```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/<usuario>/.ssh/id_rsa): /home/<usuario>/.ssh/login_csys
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

Entonces se generarán los archivos:

```
  home/<usuario>/
    |
    +- .ssh/
        |
        +- login_csys       # Llave privada
        +- login_csys.pub   # Llave pública
```

# Insertar llave pública en el servidor

Una vez generado el par de llaves, para que el servidor al que deseamos conectarnos nos permita usar la llave, necesitamos insertarla en su directorio de las llaves permitidas.

Para ello, usar este comando.

?> Reemplazar `<ruta_llave_publica>` con la ruta de la llave generada, incluyendo su nombre al final. Reemplazar `<usuario_host>` por el nombre del usuario en el servidor e `<ip_host>` con la ip del servidor.

!> **EL arhivo al final de la `<ruta_llave_publica>` _DEBE_ terminar en `.pub`, pues lo que se quiere insertar es la llave pública.**

```
ssh-copy-id -i <ruta_llave_publica> <usuario_host>@<ip_host>
```

El servidor solicitará autenticarse con la contraseña.

# Configurar uso automático de llave

Para usar comandos como `ssh` y `scp` en el servidor sin tener que especificar el archivo de llave ni la contraseña del servidor, en la ruta `~/.ssh/` agregar un archivo de la siguiente forma.

```
touch ~/.ssh/config
nano ~/.ssh/config
```

y dentro del archivo, pegar lo siguiente usando `Ctrl` + `Shift` + `V`:

?> Reemplaza `<llave>` por el la ruta de la llave que acabas de crear (incluyendo su nombre al final) y `<host>` con la ip del servidor deseado.

!> **El nombre de la `<llave>` no debe terminar con `.pub`, pues esa es la llave pública**

```
Host <host>
        IdentityFile <llave>
```

Presionar `Ctrl` + `X` y en seguida `Y`.
