# Manejo de Mensajes

## Descripción

El servicio `ManejoDeMensajesService` centraliza la comunicación visual con el usuario en la GUI de CARRDUCI. Envuelve librerías de terceros para mostrar alertas, confirmaciones y notificaciones, asegurando estilos consistentes y cierres ordenados de flotantes.

Librerías utilizadas:

-   **SweetAlert2 (`sweetalert2`)**: cuadros de diálogo (modales, alertas, confirmaciones).
-   **ngx-toastr (`ngx-toastr`)**: notificaciones tipo toast.
-   **ControlDeFlotantesService** (`../flotantes/control-de-flotantes/control-de-flotantes.service`): cierra overlays flotantes antes de mostrar mensajes.
-   **PreLoaderService** (`components/pre-loader/pre-loader.service`): sincroniza el fin de cargas con mensajes de éxito/error.

## Ubicación de Archivos

```
carrduci-sys-gui/src/app/services/utilidades/manejo-de-mensajes.service.ts
```

## Guía rápida (uso básico)

-   **[Éxito inmediato]**

    ```typescript
    this.msjService.toastCorrecto('Guardado correctamente');
    ```

-   **[Error estándar]**

    ```typescript
    this.servicio.crear(data).subscribe({
        next: () => this.msjService.toastCorrecto('Listo'),
        error: (err) => this.msjService.err(err)
    });
    ```

-   **[Confirmación sencilla]**

    ```typescript
    this.msjService.confirmarAccion(
        '¿Aplicar cambios?',
        () => this.aplicar(),
        'Se mantuvo la configuración original.'
    );
    ```

-   **[Validación rápida]**

    ```typescript
    if (form.invalid) {
        this.msjService.invalido('Revisa los campos obligatorios.');
        return;
    }
    ```

-   **[Cerrar overlays antes de alertar]**

    !> Esto ya lo hace el servicio, pero se explica cómo hacerlo manualmente por si es necesario.

    ```typescript
    this.msjService.cerrarTodosLosFlotantes();
    this.msjService.toastCorrecto('Overlay limpio');
    ```

## API Pública

### Métodos principales

| Método                                                                                                    | Tipo de mensaje                   | Notas                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `err(err, callback?, mostrarBotonImprimir?)`                                                              | Alerta modal de error             | Usa SweetAlert2, mapea respuestas backend y permite imprimir detalles cuando aplica. Siempre invoca `cerrarTodosLosFlotantes()` y `PreLoaderService.err()`. |
| `toastCorrecto(msj, titulo?, timer?)`                                                                     | `ToastrService.success`           | Notifica acciones exitosas; se usa tras `PreLoaderService.ok()`. Ejemplo en `conteos.service.ts`.                                                           |
| `toastError(err)` / `toastErrorMensaje(msj)`                                                              | `ToastrService.error`             | El primero reusa `gestionarError` para mostrar errores de API.                                                                                              |
| `confirmarAccion(msj, callbackSuccess, msjCancelacion?, callbackCancel?, title?)`                         | Confirmación simple               | Botones estilizados con mixin SweetAlert y mensajes estándar.                                                                                               |
| `confirmarAccionExtendido(msj, callbackSuccess, msjCancelacion?, callbackCancel?, title?, opcionesExtra)` | Confirmación configurable         | Permite personalizar tipo, textos y clases de botones; muy usado en flujos críticos.                                                                        |
| `confirmacionDeEliminacion(msj, callback)`                                                                | Confirmación enfocada en eliminar | Mensajes predeterminados para operaciones destructivas.                                                                                                     |
| `solicitarPermiso(msj, callback)`                                                                         | Solicitar permiso/autorización    | Usa textos de advertencia y confirma acciones que requieren autorización.                                                                                   |
| `correcto(msj, titulo?, timer?)`                                                                          | Toast de éxito (SweetAlert)       | Alternativa a `toastCorrecto` para mostrar animaciones personalizadas.                                                                                      |
| `informar(msj, titulo?, timer?)`                                                                          | Toast informativo (SweetAlert)    | Animación `slideInRight` para avisos rápidos.                                                                                                               |
| `invalido(msj, titulo?, timer?)`                                                                          | Alerta modal de validación        | Útil para errores de formulario sin salida a backend.                                                                                                       |
| `ups(msj, titulo?, timer?)`                                                                               | Advertencia modal ligera          | Mensaje centrado sin botón de confirmación.                                                                                                                 |
| `eliminado(msj)`                                                                                          | Alias                             | Ejecuta `correcto(msj, 'Eliminado')`.                                                                                                                       |
| `limpiarTodosLosToast()`                                                                                  | Limpia toasts                     | Llama a `ToastrService.clear()`.                                                                                                                            |

### Parámetros clave de SweetAlert2

-   **`type` / `icon`**: valores usados en la base (`success`, `error`, `warning`, `info`, `question`).
-   **`confirmButtonClass` / `cancelButtonClass`**: clases Bootstrap personalizadas para respetar el diseño CARRDUCI.
-   **`buttonsStyling`**: se fuerza a `false` para mantener estilos personalizados.
-   **`toast`**: cuando se establece en `true`, convierte el modal en un toast (usado por `correcto()` e `informar()`).
-   **`timer`**: se usa para autocerrar alertas; recuerda combinarlo con `showConfirmButton: false` si no se requiere interacción.

### Parámetros clave de ngx-toastr

-   **`timeOut`**: controla la duración del toast. En `toastCorrecto()` su defecto es `3000 ms`.
-   **`positionClass`**: por defecto se utiliza la configuración global (superior derecha). Puede sobreescribirse en llamadas específicas.
-   **`closeButton` y `tapToDismiss`**: se suelen configurar al nivel del módulo `ToastrModule`. Ajusta estos valores si necesitas toasts persistentes.

## Catálogo completo de métodos (con ejemplos)

> Todos los ejemplos asumen una instancia inyectada `private msjService: ManejoDeMensajesService` y, cuando aplica, `private preloader: PreLoaderService` o servicios HTTP.

### `err(err, callback?, mostrarBotonImprimir?)`

-   **Propósito**: Mostrar errores de backend con detalle estructurado.
-   **Uso típico** (`conteos.service.ts`):

    ```typescript
    catchError((err) => {
        this.preloader.err();
        this.msjService.err(err);
        return throwError(err);
    });
    ```

-   **Versión con impresión** (botón imprimir activo):

    ```typescript
    this.msjService.err(errDeReporte, () => this.actualizarTabla(), true);
    ```

    Activa el botón imprimir y ejecuta `actualizarTabla()` al cerrar la alerta.

### `toastCorrecto(msj, titulo?, timer?)`

-   **Props clave**: `titulo` (por defecto "Acción realizada"), `timer` (3000 ms).
-   **Ejemplo**:

    ```typescript
    this.msjService.toastCorrecto(
        `Usuario ${usuario.nombre} creado`,
        'Operación exitosa',
        5000
    );
    ```

-   **Buenas prácticas**: Llamar justo después de `preloader.ok()` para mantener la percepción de completitud.

### `toastError(err)` y `toastErrorMensaje(msj)`

-   **`toastError(err)`**: procesa el error con `gestionarError()` y relanza la excepción para el flujo RxJS.
-   **`toastErrorMensaje(msj)`**: útil para validaciones locales.

    ```typescript
    try {
        await this.generarReporte();
    } catch (err) {
        this.msjService.toastError(err);
    }

    if (!tienePermiso) {
        this.msjService.toastErrorMensaje(
            'No cuentas con permisos suficientes'
        );
        return;
    }
    ```

### `confirmarAccion()` y `confirmarAccionExtendido()`

-   **Diferencias**: la versión extendida permite personalizar icono, clases de botones, impedir cerrar con `ESC`/click fuera, etc.

#### Ejemplo básico

```typescript
this.msjService.confirmarAccion(
    '¿Deseas sincronizar los datos?',
    () => this.sincronizar(),
    'La sincronización se omitió.'
);
```

#### Ejemplo extendido completo

```typescript
this.msjService.confirmarAccionExtendido(
    'Esto impactará a todos los almacenes asociados.',
    () => this.recalcularInventarios(),
    'Los inventarios siguieron igual.',
    () => this.registrarCancelacion(),
    '¿Aplicar recalculo masivo?',
    {
        _type: 'warning',
        confirmButton: ['Recalcular ahora', 'mr-3 btn btn-success-oscuro'],
        cancelButton: ['Cancelar', 'mr-3 btn btn-outline-light'],
        showCancelButton: true,
        reverseButtons: true,
        allowOutsideClick: false,
        allowEscapeKey: false,
        callbackCancelTitle: 'Cancelado',
        callbackCancelAnnounce: 'No se realizaron cambios',
        callbackCancelType: 'info'
    }
);
```

### `confirmacionDeEliminacion(msj, callback)`

-   **Propósito específico**: mensaje fijo "¿Estás seguro/a que quieres eliminar?" y respuesta "No se eliminó nada." en caso de cancelación.

```typescript
this.msjService.confirmacionDeEliminacion(
    `Eliminar folio ${folio.folio}?`,
    () => this.eliminarFolio(folio)
);
```

### `solicitarPermiso(msj, callback)`

-   **Uso**: pedir autorización adicional antes de ejecutar un proceso.

```typescript
this.msjService.solicitarPermiso(
    'Se solicitará autorización del supervisor.',
    () => this.abrirModalAutorizaciones()
);
```

### `correcto(msj, titulo?, timer?)` e `informar(msj, titulo?, timer?)`

-   **Modalidades SweetAlert tipo toast** (no `ngx-toastr`).
-   **`correcto`** se usa para celebraciones; **`informar`** para avisos.

```typescript
this.msjService.correcto('Se reindexó el catálogo');
this.msjService.informar('El proceso sigue ejecutándose...', 'Aviso');
```

### `invalido(msj, titulo?, timer?)`

```typescript
if (!this.form.valid) {
    this.msjService.invalido(
        'Completa los campos con asterisco (*).',
        'Datos incompletos',
        6000
    );
    return;
}
```

### `ups(msj, titulo?, timer?)`

```typescript
this.msjService.ups(
    'No se pudieron recuperar los datos en este momento.',
    'Servicio temporalmente no disponible',
    8000
);
```

### `eliminado(msj)`

-   Alias para `correcto(msj, 'Eliminado')`.

```typescript
this.msjService.eliminado('La cotización fue eliminada.');
```

### `limpiarTodosLosToast()`

-   Útil cuando se navega entre vistas y se desea limpiar la cola de notificaciones.

```typescript
ngOnDestroy(): void {
    this.msjService.limpiarTodosLosToast();
}
```

### `cerrarTodosLosFlotantes()`

-   Cierra overlays activos (popover, menús contextuales, etc.) antes de lanzar mensajes.

```typescript
this.msjService.cerrarTodosLosFlotantes();
this.msjService.confirmarAccion('¿Cerrar sesión?', () => this.logout());
```

### `ok_(datos, callback?, idPreLoader?, tipo?)`

-   Helper heredado que combina `preloader.ok()` con toasts.

```typescript
const id = this.preloader.loading('Guardando...');
this.http.post(url, payload).subscribe((resp: any) => {
    this.msjService.ok_(resp, () => this.recargarListado(), id);
});
```

> `tipo: 'success' | 'info'` decide si se muestra `toast.success` o `toast.info`.

### Utilidades internas destacadas

-   `gestionarError(err, soloTexto?, mostrarBotonImprimir?)`: traduce la respuesta del backend a `SweetAlertOptions`, construye footers con detalles y prepara botón de impresión (incluye `Renderer2` para manipular DOM y clonar nodos).
-   `recorrerErrores(errors)`: genera markup HTML con la lista de errores (`errorGeneral.errors`).
-   `cerrarTodosLosFlotantes()`: apoyo para evitar overlaps visuales antes de desplegar cualquier alerta.
-   `ok_(datos, callback?, idPreLoader?, tipo?)`: helper legacy que mezcla `PreLoaderService` y toasts.

## Patrones de Uso en el Sistema

### Resumen por flujo

-   **CRUD estándar**: `toastCorrecto()` + `err()` (`conteos.service.ts`, `listas-de-precios.service.ts`).
-   **Formularios complejos**: `informar()` para mensajes intermedios y `invalido()` para validaciones (`formulario-creacion-folio-vendedor.component.ts`).
-   **Procesos largos o batch**: `confirmarAccionExtendido()` con `allowOutsideClick: false` para evitar cierres accidentales (`vista-desarrollos-tapon-supervision.component.ts`).
-   **Sockets y notificaciones en vivo**: `toastCorrecto()` o `toastErrorMensaje()` según respuesta (`dashboard.component.ts`).
-   **Errores con detalle HTML**: `err(err, null, true)` para habilitar impresión de reportes (`manejo-de-mensajes.service.ts`).
-   **Operaciones con flotantes**: se invoca `cerrarTodosLosFlotantes()` antes de abrir cualquier alerta para liberar overlays (`flotante-generico.directive.ts`).

### Escenario combinado: CRUD + confirmación + follow-up

```typescript
guardarRegistro(registro: Registro) {
    if (this.form.invalid) {
        this.msjService.invalido('Revisa los campos obligatorios.');
        return;
    }

    this.msjService.confirmarAccionExtendido(
        'Se guardará el registro y se notificará al equipo.',
        () => {
            const id = this.preloader.loading('Guardando registro');
            this.registrosService.crear(registro).subscribe({
                next: (resp) => {
                    this.preloader.ok(id);
                    this.msjService.toastCorrecto(resp.mensaje, 'Guardado');
                    this.notificarEquipo(resp.datos);
                },
                error: (err) => {
                    this.preloader.err(id);
                    this.msjService.err(err, () => this.recuperarBorrador());
                }
            });
        },
        'No se enviaron notificaciones.'
    );
}
```

Este flujo encadena:

-   Validación del formulario.
-   Confirmación extendida previa al guardado.
-   Loader mientras se procesa la petición.
-   Toast de éxito y notificación posterior.
-   Manejo de error con callback de recuperación.

### Servicios de datos (ej. `conteos.service.ts`)

```typescript
return this.http.post(url, datosConteo).pipe(
    map((resp: any) => {
        this.preloader.ok(idCarga);
        this.msjService.toastCorrecto(resp.mensaje, 'Conteo creado!');
    }),
    catchError((err) => {
        this.preloader.err();
        this.msjService.err(err);
        return throwError(err);
    })
);
```

Patrón repetido en múltiples servicios:

-   Se muestra un loader con `PreLoaderService.loading()`.
-   En `map`, se cierra el loader (`ok`) y se lanza un toast de éxito con el mensaje del backend.
-   En `catchError`, se ejecuta `preloader.err()` y `msjService.err(err)` para mostrar los detalles del error.

### Componentes que requieren confirmaciones

Ejemplo en `components/folios-vendedor/folios-vendedor.component.ts`:

```typescript
this.msjService.confirmarAccionExtendido(
    'Solo las personas autorizadas pueden devolverlo.',
    () => this.confirmarEnviarAProcesoDeAprovado(folio),
    '',
    null,
    '¿Estás seguro?'
);
```

Características observadas:

-   `confirmarAccionExtendido` aporta control sobre textos, estilos y callbacks.
-   Se usa para operaciones críticas (enviar a producción, cancelar, terminar folios, etc.).
-   Se combina con permisos: la confirmación solo se muestra cuando el usuario tiene privilegios.

### Manejo de errores con detalle imprimible

Varias rutas backend retornan `error.data.errorGeneral` con HTML. Al usar `msjService.err(err, null, true)` se habilita el botón imprimir:

-   Se genera un div con clase `saltos-linea-tabs` y un botón `btn-warning-oscuro`.
-   El listener clona el contenido, lo marca como `print` y ejecuta `window.print()`.

### Notificaciones globales

-   `toastCorrecto` se utiliza también para mostrar respuestas de sockets (`pages/dashboard/dashboard.component.ts`).
-   `toastErrorMensaje` se usa para errores simples, por ejemplo al validar formularios en componentes.
-   `informar` y `ups` aparecen en flujos donde se requiere notificar sin interrumpir (aviso de tiempo, advertencias leves).

### Formularios dinámicos y validaciones

Ejemplo en `components/conteos/conteos-formulario-creacion/conteos-formulario-creacion.component.ts`:

```typescript
if (this.formulario.invalid) {
    this.msjService.invalido(
        'Revisa los campos marcados en rojo antes de continuar.',
        'Formulario incompleto',
        7000
    );
    return;
}

this.msjService.confirmarAccion(
    '¿Guardar el conteo con la información capturada?',
    () => this.guardar(formulario)
);
```

Patrón observado:

-   Validación rápida con `invalido()` cuando el formulario no pasa las reglas locales.
-   Confirmación inmediata antes de persistir cambios relevantes.

### Sockets y tiempo real

`pages/dashboard/dashboard.component.ts` utiliza toasts para confirmar que las conexiones siguen activas:

```typescript
this.socketPing.subscribe((pong) => {
    this.msjService.toastCorrecto(pong, 'Respuesta del servidor', 1500);
});

this.socketErrorMsjPruebaWhatsapp.subscribe((error) => {
    this.msjService.toastErrorMensaje(error);
});
```

Esto permite:

-   Confirmar con un toast corto (`1500 ms`) cada respuesta positiva (`pong`).
-   Mostrar errores de socket con un mensaje directo sin bloquear la vista.

### Coordinación con flotantes

Algunos componentes usan el `FlotanteGenericoDirective` para desplegar mini menús o tooltips. Antes de abrir un SweetAlert o toast se llama a `msjService.cerrarTodosLosFlotantes()` para evitar que el overlay quede visible por debajo:

```typescript
this.msjService.cerrarTodosLosFlotantes();
this.msjService.confirmacionDeEliminacion(
    '¿Eliminar el registro seleccionado?',
    () => this.eliminarSeleccionado()
);
```

### Configuraciones avanzadas sugeridas

-   **Toasts persistentes**: configura en `AppModule`:

    ```typescript
    ToastrModule.forRoot({
        timeOut: 0,
        extendedTimeOut: 0,
        closeButton: true,
        tapToDismiss: false
    });
    ```

    Luego invoca `toastCorrecto('Proceso iniciado', 'En curso', 0);` para información persistente.

-   **SweetAlert estilos globales**: se puede crear un mixin adicional en `ManejoDeMensajesService` para otros contextos (ej. alertas informativas).

## Buenas Prácticas

-   **Cerrar flotantes antes de alertar**: aprovecha `msjService.cerrarTodosLosFlotantes()` si abres overlays propios (modales falsos, flotantes genéricos).
-   **Sincronizar con loaders**: envuelve las llamadas HTTP con `PreLoaderService.loading()` y combina `msjService.toastCorrecto`/`msjService.err` para un feedback completo.
-   **Personalizar confirmaciones críticas**: usa `confirmarAccionExtendido` cuando necesitas ajustar texto/botones o bloquear salida (`allowOutsideClick: false`).
-   **Errores del backend**: pasa el error original a `msjService.err(err)` para mantener el formato uniforme y respetar los mensajes del backend.
-   **Logs necesarios**: el servicio imprime el error en consola (`console.log('err', err)`); úsalos para diagnóstico durante desarrollo.

## Ejemplos extendidos

### Confirmación con opciones extra (`vista-desarrollos-tapon-supervision.component.ts`)

```typescript
this.msjService.confirmarAccionExtendido(
    'Ya no se podrá enviar a revisión o modificar',
    () => this.pedirMotivoDeCancelacion(desarrollo),
    '',
    null,
    '¿Cancelar desarrollo?',
    {
        confirmButton: ['Confirmar cancelación', 'mr-3 btn btn-danger-oscuro'],
        cancelButton: ['Conservar', 'mr-3 btn btn-success-oscuro'],
        allowOutsideClick: false
    }
);
```

### Toast informativo (`dashboard.component.ts`)

```typescript
this.socketPing.subscribe((pong) => {
    this.msjService.toastCorrecto(pong, 'Respuesta del servidor');
});
```

### Error con impresión de detalles (`manejo-de-mensajes.service.ts`)

```typescript
try {
    await this.servicio.guardar(data);
} catch (err) {
    this.msjService.err(err, null, true);
}
```

### Confirmación de eliminación (`vista-folios-prefacturas.component.ts`)

```typescript
this.msjService.confirmacionDeEliminacion(
    '¿Deseas eliminar la prefactura seleccionada?',
    () => this.eliminarPrefactura(prefactura)
);
```

En este flujo se aprovecha el mensaje preconfigurado "¿Estás seguro/a que quieres eliminar?" y la respuesta "No se eliminó nada." cuando el usuario cancela.

### Solicitud de permiso (`vista-supervision-conteos.component.ts`)

```typescript
this.msjService.solicitarPermiso(
    'Se requiere una autorización para aprobar el último conteo.',
    () => this.abrirModalAutorizacion()
);
```

Se usa al combinar `ZonaComentariosGenericaComponent` con procesos de autorización, asegurando que el usuario confirme su intención antes de abrir el generador de códigos.

### Manejo de loader + toasts (`bitacora-mantenimiento.service.ts`)

```typescript
const idCarga = this.preloader.loading('Guardando movimiento...');
return this.http.post(url, registro).pipe(
    map((resp: any) => {
        this.preloader.ok(idCarga);
        this.msjService.toastCorrecto(resp.mensaje, 'Listo');
        return resp.bitacoraMantenimiento;
    }),
    catchError((err) => {
        this.preloader.err(idCarga);
        this.msjService.err(err);
        return throwError(err);
    })
);
```

Este patrón refuerza la sincronía entre loader, mensaje de éxito y manejo de errores.
