# Respaldo manual

Si se presenta la necesidad de crear un respaldo manualmente, se puede usar una script en el repositorio `utilidades_carrduci_sys`.
Conectarse al servidor usando ssh.

```
ssh <usuario>@<ip_servidor>
```

!> Ya debiste haber clonado el repositorio `utilidades_carrduci_sys` en la ruta `~`.

Ejecutar el siguiente comando.

?> La ejecución de esta script puede tardar varios minutos. se puede reemplazar "RESPALDO_MANUAL" por un nombre que se le desee dar al respaldo.

```
~/utilidades_carrduci_sys/mongo/crear_respaldo_manual.sh RESPALDO_MANUAL
```

?> Es posible usar este último respaldo generado para alimentar una base de datos local, como se indica [aquí](./docs/carrduci-sys-desarrollo/2-entorno-desarollo?id=_7-alimentar-la-base-de-datos-local).
