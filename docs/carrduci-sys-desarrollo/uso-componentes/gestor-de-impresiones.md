# Gestor de Impresiones

## Descripción

El **Gestor de Impresiones** es un sistema centralizado que permite imprimir diferentes tipos de documentos y reportes en el sistema CARRDUCI. Utiliza un patrón de **API Fluida** (Fluent API) para configurar y ejecutar impresiones de manera sencilla y consistente.

### Características principales

-   **API Fluida**: Encadenamiento de métodos para configuración intuitiva
-   **Múltiples formatos**: Soporta reportes, etiquetas, folios, QR, formularios y más
-   **Componente centralizado**: Un solo componente HTML maneja todas las impresiones
-   **Window.print()**: Usa la API nativa del navegador para imprimir
-   **Limpieza automática**: Limpia datos después de cada impresión
-   **Estilos @media print**: CSS optimizado para impresión

<hr class='hr-principal'>

## Ubicación de Archivos

### Servicio Principal

```
carrduci-sys-gui/src/app/services/
└── impresion.service.ts
```

### Componente Gestor

```
carrduci-sys-gui/src/app/shared/gestor-de-impresiones/
├── gestor-de-impresiones.component.ts
├── gestor-de-impresiones.component.html
└── gestor-de-impresiones.component.css
```

### Componentes de Impresión Específicos

```
carrduci-sys-gui/src/app/
├── pages/reportes/
│   ├── reporte-de-faltantes-producto-terminado/
│   │   └── reporte-de-faltantes-producto-terminado-base-imprimible/
│   └── reporte-de-faltantes-almacen-de-produccion/
│       └── reporte-de-faltantes-alamcen-de-produccion-base-imprimible/
├── components/folios-vendedor/
│   ├── impresion-folios-vendedor/
│   └── impresion-etiquetas-lineas-folios-vendedor/
├── components/desarrollos/tapon/
│   ├── desarrollos-tapon-impresion-formato/
│   └── desarrollos-tapon-impresion-orden-qr-produccion/
└── components/requisiciones/
    └── impresion-etiquetas-trazabilidad-recepcion-articulo/
```

<hr class='hr-principal'>

## Uso Básico

### Patrón de Uso

El gestor de impresiones sigue un patrón simple de 3 pasos:

1. **Configurar** → Seleccionar tipo de impresión y pasar datos
2. **Personalizar** (opcional) → Configurar título, pie, encabezado
3. **Imprimir** → Ejecutar `imprimir()`

```typescript
// Paso 1: Inyectar el servicio
constructor(private impresionService: ImpresionService) {}

// Paso 2: Configurar e imprimir
imprimirDocumento() {
    this.impresionService
        .folioVendedor(folioData)  // ← Configurar tipo y datos
        .imprimir();                // ← Ejecutar impresión
}
```

<hr class='hr-secundario'>

## Tipos de Impresión

### 1. Folios de Vendedor

Imprime folios completos con todas sus líneas y detalles.

```typescript
imprimirFolio(folio: FolioVendedorRecibir) {
    this.impresionService
        .folioVendedor(folio)
        .imprimir();
}

// Con parámetro adicional para almacén
imprimirFolioAlmacen(folio: FolioVendedorRecibir) {
    this.impresionService
        .folioVendedor(folio, true)  // true = imprimiendo en almacén
        .imprimir();
}
```

**Componente renderizado**: `<app-impresion-folios-vendedor>`  
**Título automático**: `Folio [ #{numero} ] del vendedor {nombre}`  
**Pie automático** (si es tapón): `FO-VE-002-REV.A`

### 2. Etiquetas de Líneas de Folio

Imprime etiquetas con código de barras para líneas individuales.

```typescript
imprimirEtiquetaLinea(linea: FolioLineaVendedorRecibir, folio: FolioVendedorRecibir) {
    this.impresionService
        .etiqetaLineaVendedor(linea, folio)
        .imprimir();
}
```

**Componente renderizado**: `<app-impresion-etiquetas-lineas-folios-vendedor>`  
**Sin encabezado**: Muestra solo la etiqueta

### 3. Órdenes de Producción

Imprime múltiples órdenes con sus detalles.

```typescript
imprimirOrdenes(ordenes: OrdenImpresion[]) {
    this.impresionService
        .ordenesVariosPedidos(ordenes)
        .imprimir();
}
```

**Componente renderizado**: `<app-orden-detalle-imprimir>` (múltiples)  
**Sin encabezado**: Se renderiza una por orden

### 4. Códigos QR de Almacén

Imprime etiquetas QR para artículos del almacén.

```typescript
imprimirQRArticulos(articulos: Articulo[]) {
    this.impresionService
        .qrAlmacenVarios(articulos)
        .imprimir();
}
```

**Componente renderizado**: `<app-articulo-detalle-imprimir>` (grid)  
**Layout**: Grid responsive (2-6 columnas según tamaño)

### 5. Formularios de Mantenimiento en Blanco

Imprime formularios vacíos para contestar manualmente.

```typescript
imprimirFormulariosBlanco(
    formularios: FormularioMantenimiento[],
    maquina: Maquina
) {
    this.impresionService
        .formulariosEnBlancoMttoVarios(formularios, maquina)
        .imprimir();
}
```

**Componente renderizado**: `<app-formularios-mantenimiento-para-contestar-imprimir>`  
**Título automático**: `Formulario/s de mantenimiento de {NOMBRE} [{CLAVE}]`

### 6. Formularios de Mantenimiento Contestados

Imprime mantenimientos ya realizados con sus respuestas.

```typescript
imprimirMantenimientos(
    mantenimientos: MantenimientoMaquina[],
    maquina: Maquina
) {
    this.impresionService
        .formulariosContestadosMttoVarios(mantenimientos, maquina)
        .imprimir();
}
```

**Componente renderizado**: `<app-formularios-mantenimiento-contestados-imprimir>`  
**Título automático**: `Mantenimiento/s de {NOMBRE} [{CLAVE}]`

### 7. Reparaciones de Máquinas

Imprime historial de reparaciones.

```typescript
imprimirReparaciones(
    reparaciones: ReparacionMaquina[],
    maquina: Maquina
) {
    this.impresionService
        .reparacionesVarias(reparaciones, maquina)
        .imprimir();
}
```

**Componente renderizado**: `<app-detalle-reparaciones-imprimir>`  
**Título automático**: `Reparación/es de {NOMBRE} [{CLAVE}]`

### 8. Desarrollos de Tapón - Órdenes de Producción

Imprime órdenes de producción con QR para desarrollos de tapones.

```typescript
imprimirDesarrollosTapon(desarrollos: DesarrolloTaponRecibir[]) {
    this.impresionService
        .desarrollosTapon(desarrollos)
        .imprimir();
}
```

**Componente renderizado**: `<app-desarrollos-tapon-impresion-orden-qr-produccion>` (múltiples)  
**Título automático**: `Ordenes de producción de desarrollos de tapón`

### 9. Desarrollos de Tapón - Formato

Imprime formato detallado de desarrollo.

```typescript
imprimirFormatoDesarrollo(desarrollo: DesarrolloTaponRecibir) {
    this.impresionService
        .desarrolloTaponFormato(desarrollo)
        .imprimir();
}
```

**Componente renderizado**: `<app-desarrollos-tapon-impresion-formato>`  
**Título automático**: `Formato de desarrollo de tapón`

### 10. Etiquetas de Trazabilidad

Imprime etiquetas de trazabilidad para recepción de artículos.

```typescript
// Para requisiciones
imprimirTrazabilidadRequisicion(requisicion: Requisicion, idGenerado?: number) {
    this.impresionService
        .etiquetaTrazabilidadRecepcionArticulo(requisicion, idGenerado)
        .imprimir();
}

// Para insumos de metalizado
imprimirTrazabilidadInsumo(
    requisicion: Requisicion,
    idGenerado: number,
    insumo: InsumoMetalizadoRecibir,
    folioEntrada: number
) {
    this.impresionService
        .etiquetaTrazabilidadRecepcionArticulo(
            requisicion,
            idGenerado,
            insumo,
            folioEntrada
        )
        .imprimir();
}
```

**Componente renderizado**: `<app-impresion-etiquetas-trazabilidad-recepcion-articulo>`  
**Sin encabezado**: Solo etiqueta

### 11. Reportes de Faltantes - Producto Terminado

```typescript
imprimirFaltantesPT(reportes: ReporteFaltantesProductoTerminado[]) {
    this.impresionService
        .productoTerminadoFaltantes(reportes)
        .imprimir();
}
```

**Componente renderizado**: `<app-reporte-de-faltantes-producto-terminado-base-imprimible>`  
**Título automático**: `Reporte de faltantes. Producto terminado`

### 12. Reportes de Faltantes - Almacén de Producción

```typescript
imprimirFaltantesAlmacen(reportes: ReporteFaltantesAlmacenProduccion[]) {
    this.impresionService
        .almacenProduccionFaltantes(reportes)
        .imprimir();
}
```

**Componente renderizado**: `<app-reporte-de-faltantes-alamcen-de-produccion-base-imprimible>`  
**Título automático**: `Reporte de faltantes. Almacen de produccion`

### 13. Reportes Personalizados - Almacén de Producción

```typescript
imprimirReportePersonalizado(articulos: any[], nombreReporte: string) {
    this.impresionService
        .almacenProduccionPersonalizado(articulos, nombreReporte)
        .imprimir();
}
```

**Componente renderizado**: `<app-r-personalizado-almacen-produccion-imprimible>`  
**Título automático**: `{nombreReporte} Almacen de produccion`

### 14. Programación de Transformación

```typescript
imprimirProgramacion(maquinas: Maquina[], nombreReporte: string) {
    this.impresionService
        .programacionTransformacion(maquinas, nombreReporte)
        .imprimir();
}
```

**Componente renderizado**: `<app-programacion-transformacion-imprimir>`  
**Título automático**: `{nombreReporte} Control de produccion`

<hr class='hr-principal'>

## Crear un Nuevo Tipo de Impresión

### Paso 1: Agregar Método al Servicio

Edita `impresion.service.ts`:

```typescript
// impresion.service.ts
export class ImpresionService {
	// 1. Agregar propiedad para los datos
	miNuevoReporteDatos: MiTipoDato[] = [];

	// 2. Agregar método de configuración con API fluida
	miNuevoReporte(datos: MiTipoDato[], titulo?: string): this {
		this.miNuevoReporteDatos = datos;
		this.mostrarEncabezado = true;
		this.titulo = titulo || 'Mi Nuevo Reporte';
		return this; // ← Importante: retornar this para API fluida
	}

	// 3. Actualizar método limpiar()
	private limpiar() {
		// ... código existente ...
		this.miNuevoReporteDatos = []; // ← Agregar limpieza
	}
}
```

### Paso 2: Crear Componente de Impresión

```bash
ng generate component shared/mi-nuevo-reporte-imprimible
```

```typescript
// mi-nuevo-reporte-imprimible.component.ts
import { Component, Input } from '@angular/core';
import { MiTipoDato } from './mi-tipo-dato.model';

@Component({
	selector: 'app-mi-nuevo-reporte-imprimible',
	templateUrl: './mi-nuevo-reporte-imprimible.component.html',
	styleUrls: ['./mi-nuevo-reporte-imprimible.component.css'],
})
export class MiNuevoReporteImprimibleComponent {
	@Input() datos: MiTipoDato[];
}
```

#### Template HTML

```html
<!--mi-nuevo-reporte-imprimible.component.html-->
<div class="reporte-container">
	<table class="table">
		<thead>
			<tr>
				<th>Columna 1</th>
				<th>Columna 2</th>
				<th>Columna 3</th>
			</tr>
		</thead>
		<tbody>
			<tr *ngFor="let item of datos">
				<td>{{ item.campo1 }}</td>
				<td>{{ item.campo2 }}</td>
				<td>{{ item.campo3 }}</td>
			</tr>
		</tbody>
	</table>
</div>
```

### Paso 3: Agregar CSS de Impresión

```css
/* mi-nuevo-reporte-imprimible.component.css */
:host {
	display: block;
}

@media print {
	/* Ocultar elementos no deseados */
	.no-imprimir {
		display: none !important;
	}

	/* Saltos de página */
	.salto-pagina {
		page-break-after: always;
	}

	/* Optimizar tabla */
	table {
		width: 100%;
		border-collapse: collapse;
	}

	th,
	td {
		border: 1px solid #000;
		padding: 8px;
		font-size: 12px;
	}

	/* Colores exactos */
	* {
		-webkit-print-color-adjust: exact;
		print-color-adjust: exact;
	}
}
```

### Paso 4: Agregar al Gestor

Edita `gestor-de-impresiones.component.html`:

```html
<!--gestor-de-impresiones.component.html-->
<tbody>
	<tr>
		<td colspan="2">
			<!--Componentesexistentes...-->

			<!--Agregarelnuevo-->
			<app-mi-nuevo-reporte-imprimible
				*ngIf="s.miNuevoReporteDatos.length > 0"
				[datos]="s.miNuevoReporteDatos"
			></app-mi-nuevo-reporte-imprimible>
		</td>
	</tr>
</tbody>
```

### Paso 5: Usar el Nuevo Tipo

```typescript
// En cualquier componente
imprimirMiReporte(datos: MiTipoDato[]) {
    this.impresionService
        .miNuevoReporte(datos, 'Título Personalizado')
        .imprimir();
}
```

### Paso 6: (Opcional) Agregar al Módulo

Si creaste un módulo nuevo, asegúrate de declararlo:

```typescript
// app.module.ts o shared.module.ts
import { MiNuevoReporteImprimibleComponent } from './shared/mi-nuevo-reporte-imprimible/mi-nuevo-reporte-imprimible.component';

@NgModule({
	declarations: [
		// ... otros componentes
		MiNuevoReporteImprimibleComponent,
	],
})
export class AppModule {}
```

<hr class='hr-principal'>

## Resumen

El **Gestor de Impresiones** proporciona:

✅ **API Fluida** para configuración intuitiva  
✅ **14+ tipos** de impresión diferentes  
✅ **Componente centralizado** que maneja todo  
✅ **Limpieza automática** de datos  
✅ **CSS optimizado** para @media print  
✅ **Extensible** para nuevos tipos  
✅ **Consistente** en toda la aplicación

Este sistema centraliza toda la lógica de impresión, facilitando el mantenimiento y asegurando una experiencia consistente en todo CARRDUCI.
