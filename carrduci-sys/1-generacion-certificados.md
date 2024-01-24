### [< Directorio](../directorio.md)

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
## Paso 3: Crear una entidad de certificación
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

También se va a solicitar confirmar el nombre común (CN) de la CA. Es el que se usa para hacer referencia a esta máquina en el contexto de la entidad de certificación. Se puede ingresar cualquier texto o dejarlo como tal presionando ENTER.

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
Common Name (eg: your user, host, or server name) [Easy-RSA CA]:

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




