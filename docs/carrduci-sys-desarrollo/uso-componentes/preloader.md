# PreLoader Service

## Descripción

`PreLoaderService` provee la capa de retroalimentación visual para cargas asincrónicas en la GUI CARRDUCI. Controla la superposición global (`app-pre-loader`) que indica al usuario que una acción en segundo plano está en progreso, evitando la interacción accidental y alineando la experiencia con `ManejoDeMensajesService` y procesos HTTP.

**Objetivos principales:**

-   Centralizar el manejo de estados de carga con mensajes acumulables.
-   Sincronizar el cierre de loaders con la comunicación visual (toasts, modales).
-   Ofrecer soporte para barras de progreso (`BarraDeProgresoTransporte`) en cargas de archivos o procesos largos.
-   Facilitar la limpieza automática tras errores (`err()`) y al finalizar la cola (`ok()`).
-   Respetar la regla de un preloader global compartido por todos los servicios y componentes.

## Guía rápida (uso mínimo)

-   **[Abrir loader y cerrarlo en `finalize`]**

    ```typescript
    const id = this.preloader.loading('Guardando cambios');
    this.miServicio
        .guardar(payload)
        .pipe(finalize(() => this.preloader.ok(id)))
        .subscribe({
            next: () => this.msjService.toastCorrecto('Guardado'),
            error: (err) => this.msjService.err(err)
        });
    ```

-   **[Cancelar por error global]**

    ```typescript
    const id = this.preloader.loading('Consultando datos');
    this.miServicio.obtener().subscribe({
        next: () => this.preloader.ok(id),
        error: (err) => {
            this.preloader.err();
            this.msjService.err(err);
        }
    });
    ```

-   **[Mostrar progreso durante un upload]**

    ```typescript
    const id = this.preloader.loading('Subiendo archivos');
    this.preloader.progreso(id, 0, 'Preparando carga');
    // Actualiza progreso desde HttpEventType.UploadProgress
    ```

## Ubicación de Archivos

```
carrduci-sys-gui/src/app/components/pre-loader/
├── pre-loader.component.ts
├── pre-loader.component.html
├── pre-loader.component.css
├── pre-loader.service.ts
└── pre-loader_barraDeProgresoTransporte.ts
```

El componente es declarado y expuesto desde `SharedModule` y se inyecta en `app.component.html`.

## Arquitectura general

-   **Servicio (`pre-loader.service.ts`)**: singleton en `root` con estado compartido (`cargando`, `mostrar`, `registro` de mensajes y barras de progreso).
-   **Componente (`pre-loader.component.*`)**: observa el servicio y pinta la superposición. Usa timers para transiciones suaves (`usarClaseSpinner`, `cambiarClaseSpinner`).
-   **Modelo (`pre-loader_barraDeProgresoTransporte.ts`)**: encapsula la metadata de cada barra (`id`, `progreso`, `msj`, `upload`).
-   **Consumo**: cualquier servicio/component puede inyectar `PreLoaderService` para iniciar/cerrar cargas. El overlay es único para toda la aplicación.

## API del Servicio

| Método/propiedad                                       | Tipo      | Descripción                                                                                                                                                                     |
| ------------------------------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `loading(msj: string): number`                         | Método    | Registra una nueva carga y devuelve un `id` único. Si es la primera carga activa, muestra el overlay tras `tiempoDeEsperaAntesDePrecarga` (400 ms) y resetea banderas visuales. |
| `ok(idPreLoader: number)`                              | Método    | Finaliza la carga identificada por `id`. Si no quedan cargas activas limpia flags, desvanecimiento y mensajes. Elimina barras de progreso asociadas.                            |
| `err()`                                                | Método    | Cancela todos los loaders por error (`canceladoPorError = true`) y limpia todo inmediatamente.                                                                                  |
| `limpiar()`                                            | Método    | Reset completo: oculta overlay (`mostrar=false`), limpia `registro`, `barrasDeProgresoActivas` y banderas. Se usa internamente.                                                 |
| `progreso(id, progreso, msj, upload?)`                 | Método    | Actualiza/crea una barra de progreso vinculada al `id` de `loading()`. Usado para cargas de archivos con progreso.                                                              |
| `leyenda: string[]`                                    | Propiedad | Mensajes acumulados para mostrar en el overlay. Los ids de `registro` apuntan a estas leyendas.                                                                                 |
| `cargando: boolean`                                    | Propiedad | Bandera global; indica si hay cargas activas.                                                                                                                                   |
| `mostrar: boolean`                                     | Propiedad | Controla la visibilidad del overlay.                                                                                                                                            |
| `barrasDeProgresoActivas: BarraDeProgresoTransporte[]` | Propiedad | Registro de barras activas con `id`, `progreso`, `msj`, `upload` (bool).                                                                                                        |
| `miniCarga: boolean`                                   | Propiedad | Flag para mini loaders (usado en contenedores específicos).                                                                                                                     |
| `tiempoDeEsperaAntesDePrecarga`                        | Propiedad | Delay (ms) para evitar parpadeos en operaciones instantáneas. Default 400.                                                                                                      |

### Ciclo visual

1. `loading()` empuja mensaje y activa `cargando`. Tras delay muestra overlay (`mostrar=true`).
2. Mientras existan ids registrados, el overlay persiste y los mensajes aparecen en `pre-loader.component.html` con animaciones.
3. `ok(id)` elimina el mensaje y, si no hay más registros, llama `limpiar()` para cerrar overlay.
4. `err()` o `limpiar()` resetean todo inmediatamente.

### Relaciones con otros servicios

-   `ManejoDeMensajesService`: normalmente se invoca tras `ok()` o dentro de `catchError` para brindar feedback textual.
-   Servicios HTTP (`HttpClient`): el patrón `loading → map → ok / catchError → err` está presente en más de 70 servicios (`conteos`, `desarrollos-tapon`, `folios-vendedor`, etc.).
-   `SubirArchivoService`: único consumidor del API de progreso.
-   Componentes de tablas genéricas y dashboards consultan `preloader.cargando` para bloquear interacciones temporales.

## Integración UI

### `pre-loader.component.html`

Renderiza un overlay fijo con spinner `spinner-boton`. Se apoya en getters que aplican clases transitorias para animar blur y opacidad.

```html
<div
    *ngIf="_s.mostrar"
    [ngClass]="clasePrecarga"
>
    <div [ngClass]="classCentradoVerticalHorizontal">
        <div
            [ngClass]="claseSpinner"
            class="antes-de-mostrar-spinner"
        >
            <div class="text-center">
                <spinner-boton
                    [invertido]="true"
                    [escala]="1.3"
                ></spinner-boton>
            </div>
            <div class="text-center">
                <div
                    *ngFor="let ley of _s.Object.keys(_s.registro); let i = index"
                    [class]="'text-center fadeIn animated delay-0-' + (i + 1) + 's'"
                >
                    <h5 class="text-white">
                        <span class="etiqueta-carga">
                            {{ _s.registro[ley] }}
                        </span>
                    </h5>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Estilos relevantes `pre-loader.component.css`

-   `.precarga`/`.antes-precarga`: transiciones de blur/opacity y pointer-events.
-   `.despues-de-mostrar-spinner`: blur 0 con fade-in.
-   `.etiqueta-carga`: animación `parpadeo-etiqueta` para mensajes.

Estas clases se manipulan desde `PreLoaderComponent` usando timers que alternan `usarClaseSpinner`, `cambiarClaseSpinner`, etc.

### Inserción en la aplicación

-   `app.component.html` incluye `<router-outlet>` y, en versiones anteriores, tenía hooks comentados para lanzar el preloader durante transiciones de ruta (`NavigationStart`, `NavigationEnd`, `NavigationError`). Puedes reactivarlos siguiendo el patrón:

    ```typescript
    this.router.events.subscribe((event) => {
        if (event instanceof NavigationStart) {
            this.idPreloader = this.preloader.loading('Cargando pantalla');
        }
        if (event instanceof NavigationEnd) {
            this.preloader.ok(this.idPreloader);
        }
        if (event instanceof NavigationError) {
            this.preloader.err();
        }
    });
    ```

-   Se recomienda declarar `<app-pre-loader></app-pre-loader>` en el layout principal para que quede sobre toda la interfaz.

## Patrones de uso

### CRUD sincrónico con mensajes (`conteos.service.ts`)

```typescript
const idCarga = this.preloader.loading('Creando conteo...');
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

-   **Inicio:** `loading()` con mensaje descriptivo.
-   **Éxito:** `ok(id)` + `toastCorrecto()`.
-   **Error:** `err()` + `msjService.err(err)`.

### Procesos paginados (`desarrollos-tapon.service.ts`)

```typescript
const idCarga = this.preloader.loading('Obteniendo desarrollos de tapón');
return this.http.get(url).pipe(
    map((resp: any) => {
        this.total = resp.total ?? 0;
        this.preloader.ok(idCarga);
        return resp.datos.map(
            (registro) => new DesarrolloTaponRecibir(registro)
        );
    }),
    catchError((err) => {
        this.preloader.err();
        this.msjService.err(err);
        return throwError(err);
    })
);
```

Patrón recurrente en servicios: el loader abarca toda la llamada y se cierra en `map()`. `ok()` nunca debe omitirse tras un `loading()`.

### Notificación de progreso (ejemplo de método modificado)

Este sería un ejemplo de carga de documento con imágenes incluidas. El método existe en `proceso-material-virgen-metalizado.service.ts`, pero lo que se muestra aquí se modificó para incluir una muestra del elemento de progreso.

```typescript
EMBARQUES_crear(campos: {
	numeroFolioProduccionRelacionado: number;
	cantidad: number;
	descripcionEmbarque: string;
	folioFactura: string;
	loteDeCliente: string;
	folioHojaDeMezclasRelacionada: number[];
	scrapEmbarcado: number;
	folioDeCC: string;
	ordenDeCompra: string;
	imagenes: CargaDeImagenesTransporte[];
}) {
	const idCarga = this.preloader.loading('Generando embarque');
	const url = this.URL_EMBARQUES(``);
	return this.http
		.post(url, campos, { reportProgress: true, observe: 'events' })
		.pipe(

			// Con tap podemos "ver" en el proceso intermedio del request
			// para generar notificaciones. Aquí es donde se muestra el
			// progreso.
			tap((event: any) => {
				const progress = Math.round(
					(100 * event.loaded) / event.total
				);

				// Este sería el evento para progreso de carga.
				if (event.type === HttpEventType.UploadProgress) {
					this.preloader.progreso(
						idCarga,
						progress || 100,
						'Cargando datos e imágenes...'
					);
				}

				// Este sería el evento para progreso de descarga.
				if (event.type === HttpEventType.DownloadProgress) {
					this.preloader.progreso(
						idCarga,
						progress || 100,
						'Cargando datos e imágenes...'
					);
				}
			}),

			// Con esto le indicamos al observable que solo emita respuesta
			// cuando el tipo de evento sea una respuesta (carga completa).
			filter((event) => event.type === HttpEventType.Response),

			// Procesar la respuesta
			map((event: any) => {
				this.preloader.ok(idCarga);
				this.msjService.toastCorrecto(event.body.mensaje, 'Listo');
				return event.body.datos;
			}),

			// Procesar los errores
			catchError((err) => {
				this.preloader.err();
				this.msjService.err(err);
				return throwError(err);
			})
		);
}
```

### 1. Cadena de loaders simultáneos

Multiples peticiones pueden compartir el overlay. Cada `loading()` genera un `id` distinto. Ejemplo simplificado:

```typescript
const ids = [
    this.preloader.loading('Validando datos'),
    this.preloader.loading('Guardando registro'),
    this.preloader.loading('Sincronizando con ERP')
];

forkJoin([this.validar(), this.guardar(), this.sincronizar()]).subscribe({
    next: () => ids.forEach((id) => this.preloader.ok(id)),
    error: () => this.preloader.err()
});
```

Mientras algún `id` siga vivo en `registro`, el overlay permanece. Evita cerrar el preloader antes de que todas las tareas terminen.

### 2. Control manual en componentes

```typescript
const ID = this.preloader.loading('Preparando tablero');
// ... acciones propias ...
this.preloader.ok(ID);
```

Uso esporádico cuando no se emplean servicios HTTP pero se necesita feedback manual (ej. cálculos locales).

### 3. Etiquetas encadenadas

`leyenda` acumula mensajes en orden de llegada. Algunos servicios añaden mensajes para guiar al operador:

```typescript
const id = this.preloader.loading('Cargando partidas');
this.preloader.loading('Calculando totales');
```

Al resolverse la operación asociada a `id`, se deben eliminar los mensajes en el mismo orden. `ok(id)` limpia ambos.

## Buenas prácticas

-   **Describir cargas con verbos:** usa mensajes precisos (`'Obteniendo prefacturas'`, `'Generando reporte'`).
-   **Cierra siempre con `ok()` o `err()`:** evita loaders colgados.
-   **Coordina con `ManejoDeMensajesService`:** tras `ok()` muestra toasts/confirmaciones según la respuesta.
-   **Reutiliza un solo servicio:** no crees instancias locales; está registrado en raíz.
-   **Evita paralelizar `loading()` sin necesidad:** agrupa procesos relacionados y reutiliza mensajes cuando se trate del mismo flujo.
-   **En uploads usa `progreso()`:** da contexto al usuario sobre el avance real.
-   **Usa `finalize`:** garantiza cierre del preloader aunque la suscripción termine por error o cancelación.
-   **Evita mutar internamente `registro`:** siempre opera con los métodos públicos (`loading`, `ok`, `err`).
