### [< Directorio](./directorio.md)

# Documentación de SISTEMAS
Este repositorio tiene el objetivo de ir agregando la documentación de los distintos procesos que se llevan a cabo en el departamento de Sistemas.

Está pensado para leerse y editarse con [obsidian](https://obsidian.md/), y cuenta con una serie de scripts con los cuales subir cambios y actualizar automáticamente el [directorio](../directorio.md).
## Instalación
1. Descargar e instalar [obsidian](https://obsidian.md/) para Windows. Al abrir, la pantalla inicial debe ser algo parecido a esto:
![](../assets/imagenes/vista_inicial_obsidian.png)
2. Clonar este [mismo repositorio](https://github.com/Carrduci/documentacion_sistemas) en cualquier ruta deseada en Windows utilizando git.
3. Dar clic en la opción **Open folder as vault** y abrir la carpeta resultante de clonar el repositorio.
![](../assets/imagenes/open_folder_as_vault_obsidian.png)
## Uso de las scripts
**Estas scripts se deben ejecutar desde PowerShell como administrador**.
### Actualizar directorio
Para esta se requiere tener instalado Python 3 en Windows. Suponiendo que se tiene instalado, en el directorio raíz del repositorio clonado, ejecutar el siguiente comando:
```
./generar_directorio.py
```
### Subir cambios
Para subir los cambios a GitHub es necesario primero cambiar la política de ejecución en PowerShell. Ejecutar el siguiente comando:
```
set-executionpolicy remotesigned
```
Este va a establecer una política que permite ejecutar scripts no firmadas solo localmente, las remotas aún deben ser firmadas, lo cuál es suficiente para este caso.

Cerciorarse de que se halla establecido la política correctamente con el siguiente comando:
```
Get-ExecutionPolicy
```
Que debe resultar exactamente en los siguiente:
```
RemoteSigned
```
Luego de esto, basta con ejecutar el siguiente comando para subir los cambios (asumiendo que Git ya esté configurado correctamente):
```
.\subir_cambios.ps1
```
### Descargar cambios
Para hacer esto simplemente hay que usar el comando de git:
```
git pull
```

