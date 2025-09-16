# Uso de SSH para conectarse y copiar archivos al servidor de CARRDUCIsys

Para comunicarse con el servidor, usaremos el protocolo [`Secure Shell (SSH)`](https://blog.devops.dev/a-beginners-guide-to-ssh-what-it-is-and-how-to-use-it-27c118fec3d4).

Para conectarse al servidor y ejecutar comandos en el, se debe usar la siguiente estructura.

```
ssh <usuario>@<host>
```

Pero al hacer esto se pedirá la contraseña del usuario en el host, así que tenla a la mano.

Para copiar diréctamente desde o hacie el servidor, se usa el comando `scp`, que puede ser de las siguientes formas:

```
scp /ruta/a/archivo/local user@host:/ruta/a/archivo/remoto
```

```
scp user@host:/ruta/a/archivo/remoto /ruta/a/archivo/local
```

!> Esto requiere autenticación con contraseña, la cuál es insegura. Para ver una forma más segura, ira a [llave ssh](./docs/ubuntu-server/llave-ssh.md)
