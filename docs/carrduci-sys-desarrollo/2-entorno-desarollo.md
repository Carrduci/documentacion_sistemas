# Desplegar el entorno de desarrollo de CARRDUCI sys

Para poder desarrollar sobre el código de carrduci sys, es necesario llevar a cabo los siguientes pasos.

## 1. Instalar VsCode en Windows

Descargar el instalable desde la [página oficial](https://code.visualstudio.com/docs/?dv=win64user).

Ejecutar el instalador y seguir los pasos de instalación, pero al llegar al punto de "Seleccione las Tareas Adicionales", asegurarse de que estas 4 opciones estén marcadas.

![](../../assets/imagenes/instalacion_vscode_4opciones.png)

Al finalizar, ejecutar VsCode al menos una vez, y cerrarlo.

## 2. Instalar el Subsistema de Linux en Windows

Ver [Instalación WSL](./docs/carrduci-sys-desarrollo/1-instalacion-wsl.md).

## 3. Instalar el GitHub CLI (Command Line) e iniciar sesión

!> Debes tener una cuenta de GitHub y debe estar añadida a la organización (Carrduci). Inicia sesión con esa cuenta en el navegador principal de la computadora (puedes cambiar el navegador principal si quieres).

Ejecutar el siguiente comando (pegar con `Ctrl` + `Shift` + `V`):

```sh
(type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y
```

Luego comprobar que se instaló el cli ejecutando:

```sh
gh version
```

Y debe arrojar un resultado similar al siguiente:

```
gh version 2.54.0 (2024-08-01)
https://github.com/cli/cli/releases/tag/v2.54.0
```

Ahora hay que autenticarse en GitHub con el siguiente comando:

```sh
gh auth login
```

Y se abrirá una terminal interactiva. Ahí, seleccionar las siguientes opciones:

![](../../assets/imagenes/gh_cli_seleccionar_github.png)

![](../../assets/imagenes/gh_cli_seleccionar_https.png)

![](../../assets/imagenes/gh_cli_seleccionar_browser.png)

Copiar el código usando `Ctrl` + `Shift` + `C` y dar `Ctrl` + `Click` en la url que se muestra.

![](../../assets/imagenes/gh_cli_abrir_github_en_browser.png)

En el navegador se abrirá esta página. Dar click en "Continue".

![](../../assets/imagenes/gh_cli_cuenta_github.png)

En la siguiente vista pegar el código copiado y dar click en "Continue".

![](../../assets/imagenes/gh_cli_pegar_codigo.png)

Luego pedirá que se autentique de nuevo la cuenta. Al terminar de autenticar, dar click en autorizar.

![](../../assets/imagenes/gh_cli_autorizar_cuenta.png)

Al terminar, dar `ENTER` en la consola. Debe aparecer esto en la página.

![](../../assets/imagenes/gh_cli_listo_pagina.png)

Y en la terminal se debe ver así.

![](../../assets/imagenes/gh_cli_list_terminal.png)

## 4. Añadir usuario a git

Para poder hacer commits, es necesario indicarle a git el correo y usuario.

!> Deben ser los mismos que se tienen en la guenta de GitHub que usaras

Ejecutar los siguientes comandos (reemplazando `<correo>` y `<usuario>` por los tuyos, dejando las comillas):

```sh
git config --global user.email "<correo>"
git config --global user.name "<usuario>"
```

## 5. Ejecutar la script de despliegue y comandos iniciales

!> Antes debiste haber iniciado sesión con GitHub CLI

Ejecutar el siguiente script en la terminal de subsistema. Puede tardar varios minutos. Esto instalará todo lo necesario
para empezar a desarrollar. Podría pedirte la contraseña del usuario de subsistema que se creó anteriormente de nuevo.

```sh
code --version && sudo curl -s -H "Authorization: token $(gh auth token)" -H "Accept: application/vnd.github.v3.raw" https://api.github.com/repos/Carrduci/utilidades_carrduci_sys/contents/instalar-dev-carrdyci-sys.sh | bash
```

> Al finalizar, cerrar la terminal y volverla a abrir.

Luego copiar todo esto y pegarlo en la consola, presionando `ENTER`.

```sh
code --install-extension ms-vscode-remote.remote-wsl \
&& code --install-extension ms-python.python \
&& code --install-extension ms-python.vscode-pylance \
&& code --install-extension ms-python.debugpy \
&& code --install-extension ms-python.vscode-python-envs \
&& code --install-extension esbenp.prettier-vscode \
&& code --install-extension ms-azuretools.vscode-docker \
&& code --install-extension mongodb.mongodb-vscode \
&& code --install-extension sp90.angular-control-flow-snippets \
&& code --install-extension angular.ng-template \
&& code --install-extension cyrilletuzi.angular-schematics \
&& code --install-extension johnpapa.angular2 \
&& code --install-extension hossaini.bootstrap-intellisense \
&& code --install-extension mhutchie.git-graph \
&& code --install-extension ecmel.vscode-html-css \
&& code --install-extension bianxianyang.htmlplay \
&& code --install-extension jasonlhy.hungry-delete \
&& code --install-extension kuone.sequence-number \
&& code --install-extension zignd.html-css-class-completion \
&& code --install-extension muhammedrashid.stain \
&& code --install-extension bradlc.vscode-tailwindcss \
&& code --install-extension dbaeumer.vscode-eslint \
&& cd ~/carrduci-dev/carrduci_sys_workspace/queries_mongosh && git restore . \
&& cd ~/carrduci-dev/carrduci_sys_workspace/documentacion_sistemas && git restore . \
&& cd ~/carrduci-dev/carrduci_sys_workspace/utilidades_carrduci_sys && git restore . \
&& nvm use 14.20.1 \
&& cd ~/carrduci-dev/carrduci_sys_workspace/carrduci-sys-api && git restore . && git checkout carrduci-dev && npm install \
&& cd ~/carrduci-dev/carrduci_sys_workspace/carrduci-sys-gui && git restore . && git checkout carrduci-dev && npm install \
&& nvm use lts/* \
&& cd ~/carrduci-dev/carrduci_sys_workspace/carrduci-sys-online && git restore . && npm install \
&& cd ~/carrduci-dev/carrduci_sys_workspace/api-gateway-carrduci && git restore . && npm install \
&& cd ~/carrduci-dev/carrduci_sys_workspace
```

Luego, para abrir el espacio de trabajo, en la terminal se usará este comando.

```sh
code ~/carrduci-dev/carrduci_sys_workspace/carrduci_sys_workspace.code-workspace
```

## 6. Agregar el servidor de carrduci sys al registro de ssh

Para el siguiente paso, es necesario haberse conectado al menos una vez por ssh al servidor de carrduci. Para ello, ejecutar el siguiente comando.

```sh
ssh <usuario>@<ip_servidor> ls

```

Si es la primera vez que se hace la conexión, pedirá confirmar que el equipo es de confianza, luego solicitará la contraseña y al final imprimirá las carpetas del directorio `~` en el servidor. Ahora se puede pasar al último paso.

## 7. Alimentar la base de datos local

Ahora es necesario alimentar la base de datos local. Para ello, hay que usar el siguiente comando que copia el último
respaldo generado en el servidor.

!> Es importante que tenga un espacio al inicio para que no se guarde en el historial de comandos, porque se escribe la contraseña del servidor diréctamente

```sh
 ~/carrduci-dev/carrduci_sys_workspace/utilidades_carrduci_sys/bd-local/restaurar-respaldo-bd-local.sh <ip_servidor> <password_servidor>
```

# Recomendaciones finales

Para manipular la base de datos se puede usar la extensión de visual studio que se instaló automáticamente en los pasos anteriores ([ver doc.](https://www.mongodb.com/docs/mongodb-vscode/connect/)), o se puede usar [compass](https://www.mongodb.com/products/tools/compass), una GUI para mongodb.

Para hacer pruebas en el API, usamos [postman](https://www.postman.com/downloads/).
