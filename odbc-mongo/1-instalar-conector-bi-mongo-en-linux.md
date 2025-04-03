# Instalar Mongo BI conector

#### 1. Asegurarse de tener instalado **OpenSSL**
```
sudo apt update
sudo apt install openssl
```
#### 2. Asegurarse de tener instalado Curl
```
sudo apt install curl
```
#### 3. Crear una carpeta en el directorio del usuario e ingresar a ella
```
mkdir ~/mongo-bi-conector
cd ~/mongo-bi-conector
```
#### 4. Descargar el archivo contenedor ejecutando el siguiente comando
```
curl -O https://info-mongodb-com.s3.amazonaws.com/mongodb-bi/v2/mongodb-bi-linux-x86_64-ubuntu2204-v2.14.14.tgz
```
#### 5. Descargar el siguiente archivo para verificar la integridad el paquete descargado en el paso anterior
```
curl -LO https://info-mongodb-com.s3.amazonaws.com/mongodb-bi/v2/mongodb-bi-linux-x86_64-ubuntu2204-v2.14.14.tgz.sig
```
#### 6. Ejecutar el siguiente comando para descargar e importar el archivo key
```
curl -LO https://pgp.mongodb.com/bi-connector.asc
gpg --import bi-connector.asc
```
Que debe resultar en lo siguiente
```
gpg: key 1CCF1A1263CDD699: public key "MongoDB BI Connector Release Signing Key <packaging@mongodb.com>" imported
gpg: Total number processed: 1
gpg: imported: 1
```
#### 7. Verificar el archivo de instalación con el siguiente comando
```
gpg --verify tar -xvzf mongodb-bi-linux-x86_64-ubuntu2204-v2.14.14.tgz.sig tar -xvzf mongodb-bi-linux-x86_64-ubuntu2204-v2.14.14.tgz
```
Que debe resultar en lo siguiente:
```
gpg: Signature made Thu Jun 13 10:17:03 2024 PDT
gpg:                using RSA key BD66803ABD3EB56953142EE51CCF1A1263CDD699
gpg: Good signature from "MongoDB BI Connector Release Signing Key <packaging@mongodb.com>" [unknown]
```
Si además de lo anterior, arroja la siguiente advertencia, no pasa nada, solo significa que no se ha agregado la llave como una de confianza. Se puede dejar así.
```
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: BD66 803A BD3E B569 5314  2EE5 1CCF 1A12 63CD D699
```
Pero si se recibe el siguiente mensaje, hay que verificar el paso **6**.
```
gpg: Can't check signature: public key not found
```
#### 8. Extraer los archivos descargados e instalarlos en un directorio que esté en el **PATH**
```
tar -xvzf mongodb-bi-linux-x86_64-ubuntu2204-v2.14.14.tgz
sudo install -m755 bin/mongo* /usr/local/bin/
```
### 9. Ejecutar el conector BI de Mongo
Simplemente ejecutar:
```
mongosqld
```
Esto va a buscar la conexión de Mongo en el puerto por defecto (**27017**), en el localhost. Como se está desplegando en el servidor donde ya está alojada la BD, no se necesita hacer mucho más.

**Mongosqld** va a usar automáticamente el puerto 3307, que es el que se debe redirigir remotamente como se muestra [aquí](2-conectar-a-bi-de-mongo-remotamente-desde-windows.md).

El resultado de llamara a **mongosqld** es el siguiente:
```
2024-07-13T09:10:57.984-0600 I CONTROL    [initandlisten] mongosqld starting: version=v2.14.14 pid=261532 host=carrduci
2024-07-13T09:10:57.984-0600 I CONTROL    [initandlisten] git version: c1576430c59f4a6ba7393080dd095ffd28dbddda
2024-07-13T09:10:57.984-0600 I CONTROL    [initandlisten] OpenSSL version OpenSSL 3.0.2 15 Mar 2022 (built with OpenSSL 3.0.2 15 Mar 2022)
2024-07-13T09:10:57.984-0600 I CONTROL    [initandlisten] options: {}
2024-07-13T09:10:57.984-0600 I CONTROL    [initandlisten] ** WARNING: Access control is not enabled for mongosqld.
2024-07-13T09:10:57.984-0600 I CONTROL    [initandlisten]
2024-07-13T09:10:57.993-0600 I NETWORK    [initandlisten] waiting for connections at 127.0.0.1:3307
2024-07-13T09:10:57.993-0600 I NETWORK    [initandlisten] waiting for connections at /tmp/mysql.sock
2024-07-13T09:10:57.995-0600 I SCHEMA     [sampler] sampling MongoDB for schema...
2024-07-13T09:11:20.005-0600 I SCHEMA     [sampler] mapped schema for 42 namespaces: "carrduci" (42): ["reportesPersonalizadosAlmacenProduccion", "__codigos_numericos_autorizacion", "acendescripcions", "parametrosDeTrabajo", "reparacionesMaquina", "comentariosPedidos", "registroIndexacion", "registroshistorial", "familiadeprocesos", "horariosEmpleados", "modelosCoosMaquina", "asistencias", "proveedores", "terminados", "articulos", "changelog", "empleados", "clientes", "counters", "defaults", "maquinas", "procesos", "usuarios", "Divisas", "area
```
