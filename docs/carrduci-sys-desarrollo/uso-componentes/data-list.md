# Data List

## Descripción

El componente **Data List** provee un campo de búsqueda con lista desplegable para seleccionar elementos a partir de un término introducido por la persona usuaria. Gestiona la interacción completa: emitirá un evento para ejecutar la búsqueda, mostrará los resultados usando `flotante-generico`, permitirá seleccionar un elemento y enviará el `Dato` elegido al exterior. Actualmente es el **datalist oficial** utilizado por el _Formulario Dinámico_ para todos los campos de tipo `DATALIST`.

Características principales:

-   **Evento de búsqueda**: emite `ejecutarBusquedaDeItems` con el término y la referencia al componente, evitando suscripciones manuales dentro del componente hijo.
-   **Autocompletado controlado**: aplica `autoSeleccionar` cuando solo queda un resultado y permite reutilizar un elemento previo con `cargarModifcacion`.
-   **Integración con Flotante Genérico**: despliega el resultado usando el contenedor estándar definido en `components/utiles/flotante-generico/`.
-   **Estados consistentes**: expone banderas y eventos para marcar el campo como _valid/invalid_, cancelar la búsqueda y limpiar la selección.
-   **Uso intensivo**: más de 450 implementaciones reales en filtros, formularios de captura y vistas administrativas.
-   **Formulario Dinámico**: el tipo `DATALIST` desde `components/utiles/formulario-dinamico/` construye internamente la configuración y delega en este componente la búsqueda, renderizado y selección.

## Ubicación de Archivos

```
carrduci-sys-gui/src/app/components/utiles/data-list/
├── data-list.component.ts       # Clase del componente
├── data-list.component.html     # Plantilla con flotante
├── data-list.component.css      # Estilos (scroll, estados)
├── data-list.module.ts          # Módulo y exports
└── dato.model.ts                # Modelo Dato utilizado en la lista
```

## API del Componente

### Propiedades de Entrada (`@Input`)

| Propiedad                      | Tipo      | Requerido | Valor por defecto       | Descripción                                                                       |
| ------------------------------ | --------- | --------- | ----------------------- | --------------------------------------------------------------------------------- |
| `id`                           | `string`  | ❌        | auto-generado           | Identificador único interno para enlazar elementos del flotante.                  |
| `placeholder`                  | `string`  | ❌        | `'Escribe para buscar'` | Texto mostrado en el input mientras no hay valor.                                 |
| `autoSeleccionar`              | `boolean` | ❌        | `true`                  | Selecciona automáticamente el único resultado disponible al terminar la búsqueda. |
| `tiempoDeEsperaParaBusqueda`   | `number`  | ❌        | `1000`                  | Tiempo (ms) usado en el `debounceTime` antes de disparar la búsqueda.             |
| `desactivarInputTexto`         | `boolean` | ❌        | `false`                 | Bloquea el input para que quede solo lectura.                                     |
| `mensajeInputTextoDesactivado` | `string`  | ❌        | `''`                    | Mensaje mostrado cuando `desactivarInputTexto = true`.                            |
| `valid`                        | `boolean` | ❌        | `undefined`             | Fuerza estilos de campo válido (`is-valid`).                                      |
| `invalid`                      | `boolean` | ❌        | `undefined`             | Fuerza estilos de campo inválido (`is-invalid`).                                  |
| `cargarModifcacion`            | `Dato`    | ❌        | `undefined`             | Precarga un `Dato` para mostrarlo como leyenda seleccionada (modificaciones).     |
| `forzarUsoDeFlotanteGenerico`  | `boolean` | ❌        | `true`                  | Obliga a renderizar los resultados dentro del flotante genérico.                  |
| `_tabindex`                    | `number`  | ❌        | `0`                     | Orden de tabulación del input visible.                                            |

### Propiedades de Salida (`@Output`)

| Evento                    | Tipo                                                             | Descripción                                                                                                                                             |
| ------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ejecutarBusquedaDeItems` | `EventEmitter<{ termino: string; dataList: DataListComponent }>` | Se emite después del `debounce`. Envía el término limpio (sin espacios sobrantes) y la referencia al componente para que el padre llene los resultados. |
| `elementoSeleccionado`    | `EventEmitter<Dato>`                                             | Notifica el `Dato` seleccionado (o `null` en `limpiarParaNuevo`).                                                                                       |
| `cancelado`               | `EventEmitter<null>`                                             | Se dispara cuando se cancela manualmente o se cierra la lista sin resultado.                                                                            |
| `touched`                 | `EventEmitter<null>`                                             | Permite marcar el control externo como tocado (`FormControl.markAsTouched`).                                                                            |
| `esteComponente`          | `EventEmitter<this>`                                             | Expone la instancia completa para usos avanzados (ej. `terminoBusqueda`).                                                                               |
| `clickInput`              | `EventEmitter<null>`                                             | Se lanza al hacer click sobre el input visible.                                                                                                         |

### Métodos Públicos Relevantes

Estos métodos pueden invocarse desde el padre al recibir `esteComponente`.

| Método                          | Firma                     | Descripción                                                                                    |
| ------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------- |
| `terminoBusqueda`               | `(datos: Dato[]) => void` | Carga los resultados recibidos, muestra el flotante y maneja la autoselección.                 |
| `limpiarParaNuevo`              | `() => void`              | Limpia el estado, emite `elementoSeleccionado(null)` y deja el input listo para otra búsqueda. |
| `reiniciar`                     | `() => void`              | Limpia el estado sin emitir eventos (para reset programático desde el exterior).               |
| `cargarElementoPorModificacion` | `(dato: Dato) => void`    | Muestra un dato sin emitir eventos (usado cuando se edita un registro existente).              |

## Integración con el Formulario Dinámico

El campo `DATALIST` definido en `components/utiles/formulario-dinamico/formulario-dinamico.component.ts` utiliza internamente `DataListComponent`. La clase especial `CLASES_ESPECIALES_FORM_DINAMICO.DATALIST<T>` prepara automáticamente:

-   La vinculación del evento `ejecutarBusquedaDeItems` para ejecutar el observable de búsqueda definido en el formulario.
-   La transformación de los elementos obtenidos al modelo `Dato` (llaves `leyendaPrincipal`, `leyendaSecundaria`, `descripcionPrincipal`, `descripcionSecundaria` y `objeto`).
-   Los callbacks `callbackSeleccionarElemento` y `callbackDeseleccionarElemento` para reaccionar ante selección/deselección desde el componente principal.
-   La recarga inicial mediante `cargarModifcacion` cuando el formulario se abre en modo edición.

### Ejemplo dentro de un Formulario Dinámico

```typescript
import { CampoFormulario } from 'src/app/components/utiles/formulario-dinamico/models/campo-formulario.model';
import { CLASES_ESPECIALES_FORM_DINAMICO } from 'src/app/components/utiles/formulario-dinamico/formulario-dinamico.helpers';
import { DataListComponent } from 'src/app/components/utiles/data-list/data-list.component';
import { Dato } from 'src/app/components/utiles/data-list/dato.model';

camposFormulario = () => ({
	proveedor: new CampoFormulario({
		tipo: 'DATALIST',
		label: 'Proveedor',
		claseEspecial: new CLASES_ESPECIALES_FORM_DINAMICO.DATALIST<Proveedor>({
			autoSeleccionar: true,
			campoSeleccionarElemento: '_id',
			leyendaPrincipal: 'razonSocial',
			descripcionPrincipal: (elem) => `RFC: ${elem.rfc}`,
			descripcionSecundaria: (elem) =>
				`Crédito: ${elem.condiciones.credito} días`,
			observadorBusquedaElementos: (termino) =>
				this.proveedorService.buscarPorTermino(termino),
			callbackSeleccionarElemento: (dato: Dato) => {
				this.form.patchValue({ proveedorId: dato.objeto._id });
			},
			callbackDeseleccionarElemento: () => {
				this.form.patchValue({ proveedorId: null });
			},
		}),
	}),
});
```

En el ejemplo anterior:

-   El servicio `proveedorService.buscarPorTermino` retorna un observable. Cuando llega la data, se construye cada `Dato` y se envía mediante `dataList.terminoBusqueda(datos)`.
-   El campo oculto `proveedorId` se sincroniza con la selección.
-   Si el formulario se abre en modo edición, el propio helper llama `cargarModifcacion` con el `Dato` previamente guardado.

## Ejemplo Manual (sin Formulario Dinámico)

```html
<!-- data-list.component.html -->
<app-data-list
	[placeholder]="'Buscar artículos...'"
	[autoSeleccionar]="true"
	(ejecutarBusquedaDeItems)="buscarArticulos($event)"
	(elementoSeleccionado)="articuloSeleccionado($event)"
	(cancelado)="limpiarArticulo()"
	(esteComponente)="guardarReferencia($event)"
></app-data-list>
```

```typescript
import { DataListComponent } from 'src/app/components/utiles/data-list/data-list.component';
import { Dato } from 'src/app/components/utiles/data-list/dato.model';

export class InventarioComponent {
	private dataList!: DataListComponent;

	guardarReferencia(dataList: DataListComponent) {
		this.dataList = dataList;
	}

	buscarArticulos({
		termino,
		dataList,
	}: {
		termino: string;
		dataList: DataListComponent;
	}) {
		this.articuloService.buscar(termino).subscribe((articulos) => {
			const datos = articulos.map(
				(art) =>
					new Dato(
						art.nombre,
						`${art.existencia} unidades`,
						art.descripcion,
						`Categoría: ${art.categoria}`,
						art
					)
			);
			dataList.terminoBusqueda(datos);
		});
	}

	articuloSeleccionado(dato: Dato) {
		this.articuloActual = dato?.objeto ?? null;
	}

	limpiarArticulo() {
		this.articuloActual = null;
	}
}
```

## Buenas Prácticas

-   **Normaliza espacios**: el componente ya hace `trim`, pero evita enviar términos vacíos en el observable.
-   **Maneja cancelaciones**: libera recursos o resetea estados cuando recibas el evento `cancelado`.
-   **Reutiliza `Dato`**: centraliza la construcción de `Dato` en un helper para evitar repetir la misma lógica en múltiples formularios.
-   **Evita múltiples suscripciones**: al recibir `ejecutarBusquedaDeItems`, realiza la inyección del observable una sola vez y utiliza `take(1)` si necesitas completar la suscripción automáticamente.

## Relacionados

-   **Flotante Genérico:** [Uso del flotante genérico](./docs/carrduci-sys-desarrollo/uso-componentes/flotante-generico.md)
-   **Formulario Dinámico:** [Configuración del formulario dinámico](./docs/carrduci-sys-desarrollo/uso-componentes/formulario-dinamico.md)

## Resumen

-   Se usa como datalist oficial en todos los formularios y filtros de CARRDUCI.
-   Expone eventos suficientes para integrarse con el motor del Formulario Dinámico y con componentes personalizados.
-   Maneja autocompletado, limpieza y estados visuales consistentes.
-   Permite trabajar con datos complejos al entregar la instancia completa mediante `esteComponente`.
