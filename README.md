# Documentación de SISTEMAS

Este repositorio tiene el objetivo de ir agregando la documentación de los distintos procesos que se llevan a cabo en el departamento de Sistemas.

Funciona con github pages.

Para leer esta documentación vasta con dirigirse a [esta página](https://carrduci.github.io/documentacion_sistemas/).

## Instalación y modificación

Para modificar esta documentación se recomienda usar visual studio code porque incluye una vista previa de archivos en Markdown. Se asume que ya se tiene instalado.

También se necesita instalar `node`, a través de (como recomendación) `nvm`, en su versión para [Linux](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script) o para [Windows](https://github.com/coreybutler/nvm-windows?tab=readme-ov-file).

Se debe tener una cuenta de github, y esta cuenta debe estar agregada a la [organización](https://github.com/Carrduci). Se recomienda autenticarse con [github cli](https://cli.github.com/) para que no esté solicitando un token cada vez que se haga commit.

Además se requiere tener instalado python 3 para generar el menú (barra lateral).

Y por último es necesario tener instalado git para poder clonar el repositorio.

```
git clone https://github.com/Carrduci/documentacion_sistemas
```

En windows dar click derecho a la carpeta que se generó y seleccionar la opción **Abrir con Code**. En caso de tener subsistema de linux, entrar al directorio y escribir `code .`

El directorio que podrá ser modificado es el que se llama `/docs`, ahí es donde se crearán todas las carpetas o sub-carpetas de la documentación. Los archivos siempre deben ser de tipo MarkDown (extensión `.md`).

!> <span style="margin-right: 15px">**IMPORTANTE**</span> TODOS los nombres, tanto de archivos como carpetas deben escribirse con caracteres en minúscula y con "-" (guiones) en lugar de espacios. Ejemplo: `esta-es-una-carpeta` `archivo-tal.md`

El markdown que se usa aquí es una versión con extra herramientas, que es parte de [docsify](https://docsify.js.org), la herramienta que se usa para generar el sitio estático de esta documentación.

## Servidor de pruebas

Estando dentro del directorio se puede correr el comando `npm run start`, que iniciará un servidor local donde se podrá previsualizar la página de documentación.

Cada vez que se quiera visualizar un cambio en la estructura de archivos, hay que ejecutar la script [generar_directorio.py](./generar_directorio.py) **dentro de la carpeta del repositorio**.

## Subir cambios

Una vez terminados los cambios, hay que utilizar nuevamente git. Ejecutar los siguientes comandos:

```sh
git add .
git commit -m "cambios en la documentación"
git push -u origin main

```
