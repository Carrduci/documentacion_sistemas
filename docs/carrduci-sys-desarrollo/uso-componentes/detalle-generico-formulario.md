# Detalle Genérico Formulario

## Descripción

El componente **Detalle Genérico Formulario** (`DetalleGenericoFormularioComponent`) permite construir vistas de detalle altamente configurables a partir de un solo objeto (`documento`). Cada campo a mostrar se declara mediante una especificación (`EspecificacionUnCampoDetalle`) con la que se controlan clases, iconos, colores, pipes dinámicos, callbacks, plantillas externas (`TemplateRef`) y reglas de visualización. Es el componente estándar para detallar registros en módulos como conteos, bitácoras de mantenimiento, folios y layouts reutilizables.

Características clave:

-   **Render dinámico**: resuelve rutas anidadas en el `documento` (con `UtilidadesService.seleccionarCampoCualquierNivelProfundo`) y permite valores externos.
-   **Personalización completa**: soporta clases dinámicas, prefijos, sufijos, iconos, badges de color, templates personalizados y `datosExtra` de libre uso.
-   **Despliegue controlado**: alterna secciones colapsables por campo, con modo exclusivo (`soloUnDespliegue`) o múltiple.
-   **Pipes internos**: integra un set de pipes auxiliares (`mostrarCampo`, `llamarCallback`, `simboloAUsar`, `estaDesplegado`, `obtenerDescripcionCampo`) que automatizan el comportamiento sin intervención manual del desarrollador.

## Ubicación de Archivos

```
carrduci-sys-gui/src/app/components/utiles/detalle-generico-formulario/
├── detalle-generico-formulario.component.ts
├── detalle-generico-formulario.component.html
├── detalle-generico-formulario.component.css
├── detalle-generico-formulario.module.ts
└── -pipes-detalle-generico-formulario/
    ├── llamar-callback/
    ├── mostrar-campo/
    ├── obtener-descripcion-campo/
    ├── esta-desplegado/
    └── simbolo-a-usar/
```

> Los pipes viven en el subdirectorio `-pipes-detalle-generico-formulario/` y se exportan mediante `PipesDetalleGenericoFormularioModule`, pero **no están pensados para ser consumidos directamente**: el componente los utiliza internamente para resolver la configuración declarativa.

## Módulo

Antes de usar el componente, importa su módulo en el módulo del componente que lo requiera:

```typescript
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DetalleGenericoFormularioModule } from 'src/app/components/utiles/detalle-generico-formulario/detalle-generico-formulario.module';

@NgModule({
	declarations: [MiComponenteDetalle],
	imports: [CommonModule, DetalleGenericoFormularioModule],
})
export class MiComponenteDetalleModule {}
```

Al importar `DetalleGenericoFormularioModule` también se exportan los pipes auxiliares necesarios, por lo que no se requieren importaciones adicionales.

## API del Componente

| `@Input`               | Tipo                             | Requerido | Valor por defecto | Descripción                                                                                 |
| ---------------------- | -------------------------------- | --------- | ----------------- | ------------------------------------------------------------------------------------------- |
| `especificacionCampos` | `EspecificacionUnCampoDetalle[]` | ✅        | `[]`              | Lista de campos a generar. Se normaliza para garantizar `ocultarSiVacio`.                   |
| `documento`            | `any`                            | ✅        | `undefined`       | Objeto fuente del cual se extraen los valores de cada campo.                                |
| `soloUnDespliegue`     | `boolean`                        | ❌        | `true`            | Si es `true`, solo un campo puede estar desplegado a la vez.                                |
| `usarContenedor`       | `boolean`                        | ❌        | `true`            | Envuelve el detalle en un `<div class="container">`. Útil para incrustarlo en grid propios. |

## Especificación de Campos (`EspecificacionUnCampoDetalle`)

Cada elemento del arreglo `especificacionCampos` permite controlar el renderizado de un recuadro. A continuación, los atributos disponibles más relevantes:

-   **`campo`** (`string`): ruta dentro de `documento` (soporta niveles con `.`). Si se omite, se pasa el `documento` completo al callback/pipe.
-   **`valorExterno`** (`any`): valor fijo que sustituye al obtenido desde `documento`.
-   **`medidaClases`** (`string | (valor) => string`): clases de Bootstrap para definir el ancho (ej. `'col-lg-6'`).
-   **`renombrar`** (`string`): título a mostrar en lugar del nombre del campo.
-   **`claseTitulo` / `claseContenido` / `claseSimbolo` / `claseRecuadro`** (`string | (valor) => string`): permiten aplicar estilos condicionales al título, contenido, ícono o recuadro.
-   **`color`** (`'success' | 'warning' | 'danger' | 'info' | 'primary' | ''` o función): aplica la paleta predefinida del recuadro y determina el ícono por defecto.
-   **`simbolo`** (`boolean | (valor) => boolean`): habilita o deshabilita el ícono del título.
-   **`nombreSimbolo`** (`string | (valor) => string`): ícono específico (clase FontAwesome). Si se omite y `color` tiene un valor, el pipe interno `simboloAUsar` genera uno acorde.
-   **`prefijo` / `sufijo`** (`string | (valor) => string`): valores concatenados antes/después del contenido (ej. unidades, signos monetarios).
-   **`callback`** (`(valor: any) => any`): transforma el valor antes de renderizarlo (se aplica previo a `pipe`).
-   **`pipe`** (`Pipe` o `(valor) => Pipe`): pipe Angular a aplicar sobre el resultado del callback (ej. `FechaPipe`).
-   **`pipeArgs`** (`any[]` o `(valor) => any[]`): argumentos para el pipe. Pueden ser calculados mediante función.
-   **`descripcionCampo` / `descripcionCampoValorExterno`**: texto opcional que se muestra dentro de un panel colapsable, controlado con `soloUnDespliegue`.
-   **`ocultarSiVacio`** (`boolean | (valor) => boolean`): por defecto `true` cuando no hay `template`; el componente lo ajusta automáticamente para evitar recuadros sin valor.
-   **`ocultarForzado`** (`boolean | (valor) => boolean`): permite ocultar el campo incluso si hay valor (por ejemplo, cuando depende de un permiso).
-   **`template`** (`TemplateRef | (valor) => TemplateRef`): sustituye el contenido estándar por un template externo. El contexto expone `{ datosCampo, valorCampo, indiceRecuadro, idRecuadro }`.
-   **`datosExtra`** (`any`): espacio libre para pasar metadatos al template o a otras funciones.

> Siempre que se use `callback` o cualquier propiedad con función, se recibe el valor calculado del campo (`documento.campo` o `valorExterno`). Los pipes internos ejecutan estas funciones de forma segura mediante `LlamarCallbackPipe` para evitar errores si el método no existe.

### Propiedades que aceptan funciones de forma nativa

`EspecificacionUnCampoDetalle` (definida en `components/utiles/detalle-generico-formulario/detalle-generico-formulario.component.ts`) permite declarar la mayoría de atributos como **valor estático o callback**. El callback recibe el valor del campo (ya transformado por `valorExterno` o `callback` previos) y debe regresar el tipo esperado.

| Propiedad            | Firma esperada del callback                                                       |
| -------------------- | --------------------------------------------------------------------------------- |
| `medidaClases`       | `(valor: any) => string`                                                          |
| `claseTitulo`        | `(valor: any) => string`                                                          |
| `claseContenido`     | `(valor: any) => string`                                                          |
| `claseSimbolo`       | `(valor: any) => string`                                                          |
| `claseRecuadro`      | `(valor: any) => string`                                                          |
| `color`              | `(valor: any) => 'success' \| 'warning' \| 'danger' \| 'info' \| 'primary' \| ''` |
| `simbolo`            | `(valor: any) => boolean`                                                         |
| `nombreSimbolo`      | `(valor: any) => string`                                                          |
| `prefijo` / `sufijo` | `(valor: any) => string`                                                          |
| `pipe`               | `(valor: any) => Pipe`                                                            |
| `pipeArgs`           | `(valor: any) => any[]`                                                           |
| `ocultarSiVacio`     | `(valor: any) => boolean`                                                         |
| `ocultarForzado`     | `(valor: any) => boolean`                                                         |
| `template`           | `(valor: any) => TemplateRef<any>`                                                |

## Funcionamiento interno y pipes auxiliares

El componente encapsula la lógica mediante un conjunto de pipes internos. No se consumen directamente, pero comprender su objetivo ayuda a definir correctamente cada campo:

-   **`mostrarCampo`**: decide si el recuadro se renderiza. Valida `ocultarForzado`, `ocultarSiVacio`, longitud del valor y considera `0 / false` como valores válidos.
-   **`llamarCallback`**: ejecuta funciones declaradas (ej. `callback`, `prefijo`, `pipe`, `pipeArgs`, `nombreSimbolo`) con el valor actual y devuelve un fallback seguro cuando ocurre un error.
-   **`simboloAUsar`**: determina la clase FontAwesome del ícono según `color` o `nombreSimbolo` personalizado.
-   **`estaDesplegado`**: controla el estado abierto/cerrado de cada descripción con base en `soloUnDespliegue` y el mapa interno `despliegues`.
-   **`obtenerDescripcionCampo`**: resuelve la descripción usando `descripcionCampo` o `descripcionCampoValorExterno`, admitiendo rutas anidadas.

## Uso de Templates (`TemplateRef`)

Al configurar `template`, se puede incrustar contenido rico desde el componente padre. El contexto disponible dentro del `ng-template` es:

```typescript
interface ContextoTemplateDetalle {
	datosCampo: EspecificacionUnCampoDetalle; // Referencia a la especificación original del campo (objeto)
	valorCampo: any; // Valor calculado tras callbacks/pipes
	indiceRecuadro: number; // Índice dentro del *ngFor
	idRecuadro: string; // Id generado (por ejemplo, "recuadro_0")
}
```

## Comportamiento de despliegue

-   `soloUnDespliegue = true` (por defecto) mantiene un único panel descriptivo abierto; clics sucesivos alternan el campo activo.
-   `soloUnDespliegue = false` permite múltiples campos abiertos simultáneamente, utilizando el mapa `despliegues`.
-   `todoDesplegado` (interno) puede activarse desde el componente padre mediante `datosExtra` y lógica personalizada para abrir todo el detalle.

## Ejemplos de Uso

### Caso básico: detalle compacto

```typescript
// detalle-basico.component.ts
import { Component, Input } from '@angular/core';
import { EspecificacionUnCampoDetalle } from 'src/app/components/utiles/detalle-generico-formulario/detalle-generico-formulario.component';

@Component({
	selector: 'app-detalle-basico',
	templateUrl: './detalle-basico.component.html',
})
export class DetalleBasicoComponent {
	@Input() pedido: any;

	especificacion(): EspecificacionUnCampoDetalle[] {
		return [
			{
				campo: 'folio',
				renombrar: 'Folio',
				medidaClases: 'col-12 col-md-6',
				simbolo: true,
				nombreSimbolo: 'fas fa-hashtag',
			},
			{
				campo: 'cliente.nombre',
				renombrar: 'Cliente',
				medidaClases: 'col-12 col-md-6',
			},
			{
				campo: 'estatus',
				renombrar: 'Estatus',
				medidaClases: 'col-12',
				color: 'info',
			},
		];
	}
}
```

```html
<!-- detalle-basico.component.html -->
<app-detalle-generico-formulario
	[documento]="pedido"
	[especificacionCampos]="especificacion()"
></app-detalle-generico-formulario>
```

### Caso intermedio: callbacks, prefijos y pipes

```typescript
// detalle-intermedio.component.ts
import { Component, Input } from '@angular/core';
import { FechaPipe } from 'src/app/pipes/fecha.pipe';
import { EspecificacionUnCampoDetalle } from 'src/app/components/utiles/detalle-generico-formulario/detalle-generico-formulario.component';

@Component({
	selector: 'app-detalle-intermedio',
	templateUrl: './detalle-intermedio.component.html',
})
export class DetalleIntermedioComponent {
	@Input() venta: any;

	especificacionVenta: EspecificacionUnCampoDetalle[] = [
		{
			campo: 'total',
			renombrar: 'Total facturado',
			medidaClases: 'col-12 col-md-4',
			prefijo: '$',
			pipe: Number,
			pipeArgs: [],
		},
		{
			campo: 'fecha',
			renombrar: 'Fecha de emisión',
			medidaClases: 'col-12 col-md-4',
			simbolo: true,
			nombreSimbolo: 'far fa-calendar',
			pipe: FechaPipe,
			pipeArgs: ['DD/MM/YYYY HH:mm'],
		},
		{
			campo: 'vendedor',
			renombrar: 'Vendedor asignado',
			medidaClases: 'col-12 col-md-4',
			callback: (usuario: any) =>
				usuario?.nombreCompleto ?? 'Sin asignar',
			ocultarSiVacio: false,
		},
	];
}
```

```html
<!-- detalle-intermedio.component.html -->
<app-detalle-generico-formulario
	[documento]="venta"
	[especificacionCampos]="especificacionVenta"
	[soloUnDespliegue]="false"
></app-detalle-generico-formulario>
```

### Caso avanzado: plantillas, datos extra y despliegue controlado

```typescript
// detalle-avanzado.component.ts
import { Component, Input, TemplateRef, ViewChild } from '@angular/core';
import { EspecificacionUnCampoDetalle } from 'src/app/components/utiles/detalle-generico-formulario/detalle-generico-formulario.component';

@Component({
	selector: 'app-detalle-avanzado',
	templateUrl: './detalle-avanzado.component.html',
})
export class DetalleAvanzadoComponent {
	@Input() proyecto: any;
	@ViewChild('detalleTareas', { static: true })
	detalleTareas: TemplateRef<any>;
	@ViewChild('detalleHistorial', { static: true })
	detalleHistorial: TemplateRef<any>;

	get especificacionProyecto(): EspecificacionUnCampoDetalle[] {
		return [
			{
				campo: 'nombre',
				renombrar: 'Nombre del proyecto',
				medidaClases: 'col-12',
				claseContenido: 'h4',
				color: 'primary',
				simbolo: true,
			},
			{
				campo: 'resumen',
				renombrar: 'Resumen ejecutivo',
				medidaClases: 'col-12',
				descripcionCampoValorExterno: 'Descripción general y objetivos',
				ocultarSiVacio: false,
			},
			{
				campo: 'tareas',
				renombrar: 'Tareas registradas',
				medidaClases: 'col-12 col-xl-6',
				template: this.detalleTareas,
				datosExtra: {
					minimoParaMostrar: 1,
				},
				ocultarSiVacio: false,
			},
			{
				campo: 'historialEventos',
				renombrar: 'Historial de eventos',
				medidaClases: 'col-12 col-xl-6',
				template: this.detalleHistorial,
				datosExtra: {
					desplegarTodo: true,
				},
				ocultarSiVacio: false,
			},
		];
	}

	obtenerColorLinea(completada: boolean): string {
		return completada ? 'text-success' : 'text-warning';
	}
}
```

```html
<!-- detalle-avanzado.component.html -->
<ng-template #detalleTareas let-context>
	<div
		*ngIf="(context.valorCampo?.length ?? 0) >= context.datosCampo.datosExtra.minimoParaMostrar"
	>
		<ul class="list-group list-group-flush">
			<li
				class="list-group-item d-flex justify-content-between"
				*ngFor="let tarea of context.valorCampo"
			>
				<span>{{ tarea.titulo }}</span>
				<span [ngClass]="obtenerColorLinea(tarea.completada)">
					{{ tarea.completada ? 'Listo' : 'Pendiente' }}
				</span>
			</li>
		</ul>
	</div>
</ng-template>

<ng-template #detalleHistorial let-context>
	<div class="timeline">
		<div class="timeline-item" *ngFor="let evento of context.valorCampo">
			<div class="timeline-time">{{ evento.fecha | date: 'short' }}</div>
			<div class="timeline-content">
				<strong>{{ evento.usuario }}</strong>
				<p class="mb-0">{{ evento.descripcion }}</p>
			</div>
		</div>
	</div>
</ng-template>

<app-detalle-generico-formulario
	[documento]="proyecto"
	[especificacionCampos]="especificacionProyecto"
	[soloUnDespliegue]="false"
>
</app-detalle-generico-formulario>
```

### Callbacks avanzados en distintas propiedades

```typescript
// detalle-callbacks.component.ts
import { Component, Input, TemplateRef, ViewChild } from '@angular/core';
import { EspecificacionUnCampoDetalle } from 'src/app/components/utiles/detalle-generico-formulario/detalle-generico-formulario.component';

@Component({
	selector: 'app-detalle-callbacks',
	templateUrl: './detalle-callbacks.component.html',
})
export class DetalleCallbacksComponent {
	@Input() orden: any;
	@ViewChild('montoPositivo', { static: true })
	montoPositivo: TemplateRef<any>;
	@ViewChild('montoNegativo', { static: true })
	montoNegativo: TemplateRef<any>;

	especificacion(): EspecificacionUnCampoDetalle[] {
		return [
			{
				campo: 'estatus',
				renombrar: 'Estatus de la orden',
				medidaClases: (valor) =>
					valor === 'FINALIZADA' ? 'col-12 col-lg-4' : 'col-12',
				color: (valor) =>
					valor === 'FINALIZADA'
						? 'success'
						: valor === 'EN_PROCESO'
						? 'info'
						: 'warning',
				nombreSimbolo: (valor) =>
					valor === 'FINALIZADA'
						? 'fas fa-check-circle'
						: 'fas fa-hourglass-half',
				claseContenido: (valor) =>
					valor === 'FINALIZADA'
						? 'text-success font-weight-bold'
						: 'text-warning font-weight-bold',
				simbolo: (valor) => valor !== 'PENDIENTE',
			},
			{
				campo: 'totales.subtotal',
				renombrar: 'Subtotal ajustado',
				medidaClases: 'col-12 col-lg-4',
				valorExterno: (documento) =>
					documento.totales.subtotal -
					(documento.totales.descuento ?? 0),
				prefijo: (valor) => (valor < 0 ? '-$' : '$'),
				sufijo: (valor) => (valor < 0 ? ' (saldo)' : ''),
				claseContenido: (valor) =>
					valor < 0
						? 'text-danger font-weight-bold'
						: 'text-success font-weight-bold',
				pipeArgs: (valor) => (valor < 1000 ? ['1.0-0'] : ['1.2-2']),
				pipe: (valor) =>
					valor < 1000 ? Intl.NumberFormat : Intl.NumberFormat,
			},
			{
				campo: 'totales.detalleMontos',
				renombrar: 'Detalle de montos',
				medidaClases: 'col-12 col-lg-4',
				template: (valor) =>
					(valor?.neto ?? 0) >= 0
						? this.montoPositivo
						: this.montoNegativo,
				datosExtra: {
					mostrarHistorial: true,
				},
				ocultarSiVacio: (valor) =>
					!valor || Object.keys(valor).length === 0,
			},
		];
	}
}
```

```html
<!-- detalle-callbacks.component.html -->
<ng-template #montoPositivo let-context>
	<div class="alert alert-success mb-0">
		<strong>Ingresos:</strong>
		{{ context.valorCampo.neto | number: '1.2-2' }}
		<span
			class="badge badge-light ml-2"
			*ngIf="context.datosCampo.datosExtra.mostrarHistorial"
		>
			Historial activo
		</span>
	</div>
</ng-template>

<ng-template #montoNegativo let-context>
	<div class="alert alert-danger mb-0">
		<strong>Saldo pendiente:</strong>
		{{ context.valorCampo.neto | number: '1.2-2' }}
	</div>
</ng-template>

<app-detalle-generico-formulario
	[documento]="orden"
	[especificacionCampos]="especificacion()"
	[soloUnDespliegue]="false"
></app-detalle-generico-formulario>
```

## Mejores Prácticas

-   **Centraliza la especificación**: crea métodos dedicados (por ejemplo, `generarDetalle()`) que devuelvan el arreglo `EspecificacionUnCampoDetalle[]` para mantener el código legible y testeable.
-   **Controla valores nulos**: si el campo puede ser `undefined`, usa `ocultarSiVacio: false` o callbacks que retornan cadenas amigables (`'Sin dato'`).
-   **Reutiliza templates**: declara `ng-template` con `#identificador` y asigna el `TemplateRef` desde `ViewChild` para campos que requieren contenido enriquecido (botones, listas, componentes anidados).
-   **Separación de responsabilidades**: usa `datosExtra` para compartir metainformación con el template sin sobrecargar el objeto original.
-   **Evita depender de los pipes internos**: la API declarativa cubre la mayoría de casos. Úsalos indirectamente mediante la configuración y deja que el componente gestione su ciclo de vida.

## Checklist de Integración

-   **Importa** `DetalleGenericoFormularioModule` en el módulo donde se utilizará el componente.
-   **Declara** una función o propiedad que devuelva la especificación de campos.
-   **Entrega** el `documento` con la información a detallar (puede provenir de servicios, selectores o inputs).
-   **Opcional**: define templates adicionales para contenido complejo y obtén los `TemplateRef` con `@ViewChild`.

Siguiendo estas pautas el componente mantiene un comportamiento consistente con el resto del ecosistema CARRDUCI, maximizando la reutilización y reduciendo código repetido en las vistas de detalle.
