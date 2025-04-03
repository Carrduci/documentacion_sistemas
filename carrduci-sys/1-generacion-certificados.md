**NOTA:** No es necesario generar certificados si ya existen y no están vencidos.
# Generar certificados para CARRDUCIsys
Para llevar a cabo esto, es necesario hacer dos cosas:
1. [[#Crear una entidad de certificación (CA)]] si no hay una.
2. [[#Crear un CSR (Certificate Sign Request)]].
## Crear una entidad de certificación (CA)
### Paso 1: Instalar `easy-rsa` y `openssl`
```
sudo apt update
sudo apt install easy-rsa
sudo apt install openssl
```
### Paso 2: Preparar un directorio para la infraestructura de la clave pública (PKI - Public Key Infrastructure)
Crear un directorio en la carpeta de inicio para que contenga unos enlaces simbólicos (soft links) que se crearan más adelante. Estos van a apuntar a los archivos del paquete easy-rsa que se encuentran en `/usr/share/easy-rsa`.
```
mkdir ~/easy-rsa
```
Crear los enlaces simbólicos con el comando `ln`:
```
ln -s /usr/share/easy-rsa/* ~/easy-rsa/
```
Restringir acceso al nuevo directorio de la PKI, para que solo el propietario pueda acceder:
```
chmod 700 ~/easy-rsa
```
Iniciar la PKI dentro del directorio easy-rsa:
```
cd ~/easy-rsa
./easyrsa init-pki
```
Que debe resultar en algo como:
```

init-pki complete; you may now create a CA or requests.
Your newly created PKI dir is: /home/<usuario>/easy-rsa/pki


```
### Paso 3: Crear una entidad de certificación
Crear el archivo `vars` en el directorio `~/easy-rsa`:
```
cd ~/easy-rsa
nano vars
```
Pegar lo siguiente en el archivo reemplazando los campos que estén rodeados por `<>` (hay que borrar los <>, solo dejar las ""):
```
set_var EASYRSA_REQ_COUNTRY    "<US>"
set_var EASYRSA_REQ_PROVINCE   "<NewYork>"
set_var EASYRSA_REQ_CITY       "<New York City>"
set_var EASYRSA_REQ_ORG        "<DigitalOcean>"
set_var EASYRSA_REQ_EMAIL      "<admin@example.com>"
set_var EASYRSA_REQ_OU         "<Community>"
set_var EASYRSA_ALGO           "ec"
set_var EASYRSA_DIGEST         "sha512"
```
Ejecutar el siguiente comando para crear el certificado root público y el par de claves privadas para la entidad de certificación:
```
./easyrsa build-ca
```
Se solicitará ingresar una contraseña. Asegurarse de elegir una frase de contraseña segura y anotarla en algún lugar resguardado porque se debe ingresar siempre que se interactúe con el CA para, por ejemplo, firmar o revocar un certificado.

También se va a solicitar confirmar el nombre común (CN) de la CA. Es el que se usa para hacer referencia a esta máquina en el contexto de la entidad de certificación. Se puede ingresar cualquier texto, pero se recomienda poner CARRDUCIsys o CARRDUCI.

El resultado debería verse como lo siguiente:
```
Using SSL: openssl OpenSSL 3.0.2 15 Mar 2022 (Library: OpenSSL 3.0.2 15 Mar 2022)

Enter New CA Key Passphrase: 
Re-Enter New CA Key Passphrase: 
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Common Name (eg: your user, host, or server name) [Easy-RSA CA]:CARRDUCI

CA creation complete and you may now import and sign cert requests.
Your new CA certificate file for publishing is at:
/home/<usuario>/easy-rsa/pki/ca.crt
```

## Crear un CSR (Certificate Sign Request)
Crear un script con nano de la siguiente forma:
```
cd ~/easy-rsa
nano generar_certificado.sh
```
Y pegar dentro lo siguiente:
```
#! /bin/bash
set -e
NOMBRE="$1"
IP="$2"
DNS="$3"
RAIZ_CERT=~/generacion-certificados
DIRECTORIO="$RAIZ_CERT"/CERTIFICADO_"$NOMBRE"
#Crear raiz para guardar certificados
{ #try
    mkdir "$RAIZ_CERT"
} || { #catch
    echo Directorio "$RAIZ_CERT" ya existe... continuando
}
if [ -z $NOMBRE ]; then
    echo "[ Error ] No has definido el nombre"
    exit 1
fi
if [ -z $IP ]; then
	echo "[ Error ] Debes definir la ip. Ejemplo: X.X.X.X"
    exit 1
fi
TAM_STR_DNS=${#DNS}
if [ "$TAM_STR_DNS" -gt "0" ]; then
    DNS=",DNS:$DNS"
fi
#Crear directorio certificado
mkdir "$DIRECTORIO"
LLAVE="$NOMBRE.key"
SOLICITUD="$NOMBRE.req"
#Limpiar solicitud existente con mismo nombre (si hay)
{ #try
    rm ~/easy-rsa/pki/reqs/$SOLICITUD
} || { #catch
    echo "~/easy-rsa/pki/reqs/$SOLICITUD" no existe... continuando
}
openssl genrsa -out $DIRECTORIO/$LLAVE
openssl req -new -key $DIRECTORIO/$LLAVE -out $DIRECTORIO/$SOLICITUD
cd ~/easy-rsa
./easyrsa import-req $DIRECTORIO/$SOLICITUD "$NOMBRE" build-server-full nopass
./easyrsa  --batch --subject-alt-name="IP:$IP$DNS" sign-req server "$NOMBRE"
cp ~/easy-rsa/pki/issued/"$NOMBRE".crt $DIRECTORIO/"$NOMBRE".crt
cp ~/easy-rsa/pki/ca.crt  $DIRECTORIO/"$NOMBRE"_ca.crt
```
Después salir presionando `CTRL+X` y luego `Y`.

Agregar permisos de ejecución al archivo con el siguiente comando:
```
chmod +x ~/easy-rsa/generar_certificado.sh
```
Después ya se pueden generar certificados utilizando, dentro de la carpeta `~/easy-rsa` la siguiente estructura de comando (más adelante se explica cómo hacer para desarrollo y producción):
```
./generar_certificado.sh <nombre> <ip> <dns-opcional>
```
### Certificado para desarrollo
Para generar el certificado de desarrollo, aún en la carpeta `~/easy-rsa`, usar el siguiente comando:
```
./generar_certificado.sh desarrollo 127.0.0.1
```
Rellenar los campos que solicita con estos datos recomendados:
```
Country Name (2 letter code) [AU]:MX
State or Province Name (full name) [Some-State]:Jalisco
Locality Name (eg, city) []:Zapotlanejo
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Carrduci
Organizational Unit Name (eg, section) []:Sistemas
Common Name (e.g. server FQDN or YOUR name) []:CARRDUCIsys-desarrollo
Email Address []:sistemas.ti@carrduci.com

Please enter the following 'extra' attributes
A challenge password []:   #Alguna contraseña guardada en algún lugar seguro
An optional company name []:
```
Después va a pedir la contraseña de la CA (si se le puso). Ingresarla para obtener el siguiente resultado:
```
Enter pass phrase for /home/mentalselfthink/easy-rsa/pki/private/ca.key:
40576E71CE7F0000:error:0700006C:configuration file routines:NCONF_get_string:no value:../crypto/conf/conf_lib.c:315:group=<NULL> name=unique_subject
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
countryName           :PRINTABLE:'MX'
stateOrProvinceName   :ASN.1 12:'Jalisco'
localityName          :ASN.1 12:'Zapotlanejo'
organizationName      :ASN.1 12:'Carrduci'
organizationalUnitName:ASN.1 12:'Sistemas'
commonName            :ASN.1 12:'CARRDUCIsys-desarrollo'
emailAddress          :IA5STRING:'sistemas.ti@carrduci.com'
Certificate is to be certified until Apr 28 15:08:47 2026 GMT (825 days)

Write out database with 1 new entries
Data Base Updated

```
que nos debe dar una estructura así:
```
~/generacion-certificados/CERTIFICADO_desarrollo
	desarrollo_ca.crt 
	desarrollo.crt 
	desarrollo.key 
	desarrollo.req
```
### Certificado para producción
Para generar el certificado de producción, aún en la carpeta `~/easy-rsa`, usar el siguiente comando:
```
./generar_certificado.sh api.192.168.1.149 192.168.1.149
```
Rellenar los campos que solicita con estos datos recomendados:
```
Country Name (2 letter code) [AU]:MX
State or Province Name (full name) [Some-State]:Jalisco
Locality Name (eg, city) []:Zapotlanejo
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Carrduci
Organizational Unit Name (eg, section) []:Sistemas
Common Name (e.g. server FQDN or YOUR name) []:CARRDUCIsys
Email Address []:sistemas.ti@carrduci.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:   #Alguna contraseña guardada en algún lugar seguro
An optional company name []:
```
Después va a pedir la contraseña de la CA (si se le puso). Ingresarla para obtener el siguiente resultado:
```
Enter pass phrase for /home/mentalselfthink/easy-rsa/pki/private/ca.key:
Check that the request matches the signature
Signature ok
The Subject's Distinguished Name is as follows
countryName           :PRINTABLE:'MX'
stateOrProvinceName   :ASN.1 12:'Jalisco'
localityName          :ASN.1 12:'Zapotlanejo'
organizationName      :ASN.1 12:'Carrduci'
organizationalUnitName:ASN.1 12:'Sistemas'
commonName            :ASN.1 12:'CARRDUCIsys'
emailAddress          :IA5STRING:'sistemas.ti@carrduci.com'
Certificate is to be certified until Apr 28 15:52:06 2026 GMT (825 days)

Write out database with 1 new entries
Data Base Updated

```
que nos debe dar una estructura así:
```
~/generacion-certificados/CERTIFICADO_desarrollo
	api.192.168.1.149_ca.crt 
	api.192.168.1.149.crt 
	api.192.168.1.149.key 
	api.192.168.1.149.req
```
## Utilización de los archivos generados
Los archivos siempre se van a guardar en la carpeta `~/generacion-certificados`. Cada firma nueva se guarda en una carpeta con el siguiente formato: `CERTIFICADO_<nombre>` (más adelante se mostrará de donde viene `<nombre>`). Dentro de estas carpetas, debe haber 4 archivos más o menos como los siguientes:
```
CERTIFICADO_ejemplo/
	ejemplo_ca.crt 
	ejemplo.crt 
	ejemplo.key 
	ejemplo.req
```
En este caso, se necesitan 2 archivos para el API y la GUI: `ejemplo.crt` y `ejemplo.key`. Dichos archivos se deben colocar en 2 ubicaciones:
 - La primera es en el repositorio [carrduci-sys-api](https://github.com/Carrduci/carrduci-sys-api/tree/carrduci-master/certificado), reemplazando los 4 archivos por los 2 que se corresponden con los de este ejemplo en [[#Certificado para desarrollo]] y los otros dos en [[#Certificado para producción]].
 - La segunda es en el repositorio [utilidades-carrduci-sys](https://github.com/Carrduci/utilidades_carrduci_sys) (en la raíz), donde solo hay que reemplazar los dos archivos para producción, que se generan en el ejemplo [[#Certificado para producción]].
 - ****IMPORTANTE: para hacer este cambio, hay que clonar los repositorios, reemplazar los archivos como se indicó y después hacer `git push` en estos mismos. En la computadora donde se vayan a generar nuevas imágenes de docker, se debe hacer `pull` a los repositorios (si ya estaban clonados). Si alguno de los repositorios están clonados en el servidor donde se aloja CARRDUCIsys, también se debe hacer `git pull` ahí***.

El archivo que tiene la terminación `_ca.crt` es el que se debe usar para **instalar en los equipos donde se quiere tener acceso al sistema**. Ver [¿Cómo instalar certificados en compus de usuarios?](./5-instalar-certificado-en-computadora-usuario.md).



