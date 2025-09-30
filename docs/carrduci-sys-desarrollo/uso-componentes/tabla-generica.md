# Tabla Genérica

## Descripción

La **Tabla Genérica** es el componente más completo y versátil del sistema CARRDUCI. Permite crear tablas dinámicas con funcionalidades avanzadas como selección múltiple, ordenamiento, filtrado, exportación, modo móvil responsivo, barras de progreso, desplegables y mucho más.

### Características principales

- **Generación dinámica**: Crea tablas desde arrays de objetos
- **54+ implementaciones** en el sistema
- **Modo selección múltiple**: Con botones de ayuda para gestionar selecciones
- **Columnas especiales**: Imágenes, botones, estatus, desplegables
- **Modo móvil responsivo**: Estilo masonry con breakpoints personalizables
- **Barras de progreso CSS**: Visualización de porcentajes en filas
- **Exportar/Copiar**: Copiar contenido a portapapeles o imprimir
- **Templates personalizados**: ng-template para contenido complejo
- **ngClass avanzado**: Sistema de grupos con bordes redondeados
- **Scroll automático**: Ajuste al máximo disponible en viewport
- **Pipes personalizados**: Para formatear datos (fecha, decimal, porcentaje, etc.)
- **Callbacks dinámicos**: routerLink, click, estilos, clases
- **Uso en modales**: Compatible con `app-modal`

## Instalación e Importación

### Importar el Módulo

```typescript
import { TablaGenericaModule } from 'src/app/components/utiles/tabla-generica/tabla-generica.module';

@NgModule({
    declarations: [TuComponenteComponent],
    imports: [
        // ... otros módulos
        TablaGenericaModule
    ]
})
export class TuModuloModule {}
```

### Servicios Requeridos

```typescript
import { TablaGenericaService } from 'src/app/services/tabla-generica.service';

constructor(private tablaService: TablaGenericaService) {}
```

<hr class='hr-principal'>

## Ejemplo de Uso Rápido

Si solo necesitas una tabla básica sin configuraciones avanzadas:

### TypeScript

```typescript
import { Component } from '@angular/core';
import { TablaGenericaService } from 'src/app/services/tabla-generica.service';
import { 
    DatosTablaGenerica, 
    DatosColumnaTablaGenerica 
} from 'src/app/components/utiles/tabla-generica/tabla-generica.component';

@Component({
    selector: 'app-mi-componente',
    templateUrl: './mi-componente.component.html'
})
export class MiComponente {
    datosTabla: DatosTablaGenerica;
    cargando = {};
    
    usuarios = [
        { nombre: 'Juan Pérez', edad: 30, email: 'juan@example.com' },
        { nombre: 'María García', edad: 25, email: 'maria@example.com' }
    ];
    
    constructor(private tablaService: TablaGenericaService) {}
    
    ngOnInit() {
        this.crearTabla();
    }
    
    crearTabla() {
        const columnas: DatosColumnaTablaGenerica[] = [
            {
                titulo: 'nombre',
                campoCelda: { funcion: (usuario) => usuario.nombre }
            },
            {
                titulo: 'edad',
                alineacion: 'center',
                campoCelda: { funcion: (usuario) => usuario.edad }
            },
            {
                titulo: 'email',
                campoCelda: { funcion: (usuario) => usuario.email }
            }
        ];
        
        this.datosTabla = this.tablaService.generarEstructura(
            'No se encontraron usuarios',
            this.usuarios,
            columnas
        );
    }
}
```

### HTML

```html
<app-tabla-generica
    [datos]="datosTabla"
    [cargando]="cargando"
></app-tabla-generica>
```

?> **NOTA**: Este ejemplo básico crea una tabla funcional con 3 columnas. Las secciones siguientes explican todas las funcionalidades avanzadas disponibles.

<hr class='hr-principal'>

## Arquitectura del Sistema

### Componentes

```
Tabla Genérica
├── Componente Principal
│   ├── tabla-generica.component.ts (1,147 líneas)
│   ├── tabla-generica.component.html
│   └── tabla-generica.component.css
├── Servicio
│   └── tabla-generica.service.ts (1,147 líneas)
├── Pipes
│   └── marcar-seleccion-fila.pipe.ts
└── Modelos TypeScript
    ├── DatosTablaGenerica
    ├── DatosFilaTablaGenerica
    ├── DatosColumnaTablaGenerica
    ├── DatosCeldaTablaGenerica
    ├── ContenidoCeldaTablaGenerica
    ├── DescripcionModalTablaGenerica
    ├── OpcionesLinksTablaGenerica
    └── EstiloMallaCantidadColumnasMoviles
```

### Ubicación de Archivos

```
carrduci-sys-gui/src/app/
├── components/utiles/tabla-generica/
│   ├── tabla-generica.component.ts
│   ├── tabla-generica.component.html
│   ├── tabla-generica.component.css
│   ├── tabla-generica.module.ts
│   └── pipes-tabla-generica/
│       └── marcar-seleccion-fila.pipe.ts
└── services/
    └── tabla-generica.service.ts
```

<hr class='hr-principal'>

## Propiedades del Componente

### Inputs

| Propiedad | Tipo | Descripción | Por Defecto |
|-----------|------|-------------|-------------|
| `[datos]` | `DatosTablaGenerica` | Datos estructurados de la tabla | - |
| `[cargando]` | `object` | Objeto con mensajes de carga | `{}` |
| `[modoSeleccion]` | `boolean` | Activa modo selección múltiple | `false` |
| `[campoSeleccion]` | `string` | Campo para identificar selección | `null` |
| `[seleccionOtrasPaginas]` | `any[]` | IDs seleccionados en otras páginas | - |
| `[ObjetosOtrasPaginas]` | `any` | Objetos seleccionados previamente | - |
| `[enMovil]` | `boolean` | Activa modo móvil | `false` |
| `[enModal]` | `boolean` | Dentro de modal | `false` |
| `[botonesCopiar]` | `boolean` | Muestra botones copiar/exportar | `true` |
| `[botonScrollTop]` | `boolean` | Muestra botón scroll arriba | `true` |
| `[ajustarTablaAlMaximoScrollPosible]` | `boolean` | Auto-ajustar altura | `false` |
| `[correccionAjusteScrollMaximoInferior]` | `string` | Corrección altura | `'60px'` |

### Outputs

| Emisor | Tipo | Descripción |
|--------|------|-------------|
| `(seleccionado)` | `EventEmitter<any[]>` | Emite array de IDs seleccionados |
| `(objetosSeleccionados)` | `EventEmitter<any>` | Emite objeto con elementos completos |

<hr class='hr-principal'>

## Servicio: generarEstructura()

El método principal del servicio que convierte arrays en estructura de tabla.

### Firma

```typescript
generarEstructura(
    mensajeSinDatos: string,
    elementos: any[],
    datosColumnas: DatosColumnaTablaGenerica[],
    datos?: { /* opciones */ }
): DatosTablaGenerica
```

### Uso Básico

```typescript
this.datosTabla = this.tablaService.generarEstructura(
    'No se encontraron elementos',
    this.miArray,
    this.columnas
);
```

### Opciones del 4to Parámetro

#### Columnas Especiales

```typescript
{
    // Imágenes (primera columna)
    imagen: this.templateImagen,
    tituloColumnaImagen: 'Foto',
    alineacionImagen: 'center',
    
    // Botones (última columna)
    botones: this.templateBotones,
    tituloColumnaBotones: 'Acciones',
    alineacionBotones: 'center',
    
    // Estatus
    estatus: this.templateEstatus,
    tituloEstatus: 'Estado',
    alineacionEstatus: 'center',
    
    // Desplegable
    desplegable: this.templateDesplegable,
    alineacionDesplegable: 'center'
}
```

#### Callbacks

```typescript
{
    routerLinkCallback: (elem) => `/detalle/${elem._id}`,
    clickCallback: (elem) => this.verDetalle(elem),
    ngClassCallback: this.clasesPorFila.bind(this),
    callbackObjetoRepresentado: this.prepararObjeto.bind(this),
    cualquierObjeto: { data: 'extra' }
}
```

#### Modo Móvil

```typescript
{
    campoAMostrarMovil: 'nombre',
    campoSecundario1Movil: 'categoria',
    campoSecundario2Movil: 'precio',
    PipeCampoSecundario2Movil: DecimalPipe,
    PipeArgsCampoSecundario2Movil: ['1.2-2'],
    tituloEnMovil: this.tituloMovil,
    buscadorEnMovil: true,
    paginadorEnMovil: true
}
```

<hr class='hr-principal'>

## Definición de Columnas

### Columna Simple

```typescript
{
    titulo: 'nombre',
    campoCelda: {
        funcion: (elem) => elem.nombre
    }
}
```

### Con Alineación

```typescript
{
    titulo: 'precio',
    alineacion: 'right',  // 'left' | 'center' | 'right'
    campoCelda: {
        funcion: (elem) => elem.precio
    }
}
```

### Con Pipe

```typescript
import { DatePipe, DecimalPipe, PercentPipe } from '@angular/common';

// Fecha
{
    titulo: 'fecha',
    campoCelda: {
        funcion: (elem) => elem.createdAt,
        pipe: DatePipe,
        pipeArgs: ['dd/MM/yyyy']
    }
}

// Decimal
{
    titulo: 'cantidad',
    campoCelda: {
        funcion: (elem) => elem.cantidad,
        pipe: DecimalPipe,
        pipeArgs: ['1.2-2']
    }
}

// Porcentaje
{
    titulo: 'avance',
    campoCelda: {
        funcion: (elem) => elem.porcentaje / 100,
        pipe: PercentPipe,
        pipeArgs: ['1.0-0']
    }
}
```

### Con Clase Dinámica

```typescript
{
    titulo: 'stock',
    campoCelda: {
        funcion: (elem) => elem.stock
    },
    funcionClassContenido: (elem, indice) => {
        if (elem.stock === 0) return 'badge badge-danger';
        if (elem.stock < 10) return 'badge badge-warning';
        return 'badge badge-success';
    }
}
```

### Con Template

```typescript
// TypeScript
@ViewChild('miTemplate') miTemplate: TemplateRef<any>;

// Columna
{
    titulo: 'custom',
    campoCelda: {
        template: this.miTemplate
    }
}
```

```html
<!-- HTML -->
<ng-template #miTemplate let-contexto>
    <div>{{ contexto.datos.nombre }}</div>
</ng-template>
```

### Con Tooltip

```typescript
{
    titulo: 'info',
    campoCelda: {
        funcion: (elem) => elem.codigo,
        tooltip: {
            funcion: (elem) => `Descripción: ${elem.descripcion}`
        }
    }
}
```

### Con Link

```typescript
// routerLink
{
    titulo: 'folio',
    campoCelda: {
        funcion: (elem) => elem.numeroFolio,
        link: (elem, indice) => ({
            routerLink: `/folios/${elem._id}`,
            _class: 'text-primary font-bold'
        })
    }
}
```

### Con Prefijo/Sufijo

```typescript
{
    titulo: 'peso',
    campoCelda: {
        funcion: (elem) => elem.peso,
        pipe: DecimalPipe,
        pipeArgs: ['1.2-2']
    },
    funcionPrefijo: () => 'Peso: ',
    funcionSufijo: () => ' kg'
}
// Resultado: "Peso: 25.50 kg"
```

<hr class='hr-principal'>

## Columnas Especiales

### 1. Columna de Imágenes

La forma recomendada es usar el componente `app-mini-visualizador-foto` que proporciona visor de imágenes con zoom.

#### Importar el Módulo del Mini Visualizador

```typescript
import { MiniVisualizadorFotoModule } from 'src/app/components/utiles/mini-visualizador-foto/mini-visualizador-foto.module';

@NgModule({
    declarations: [ProductosComponent],
    imports: [
        // ... otros módulos
        TablaGenericaModule,
        MiniVisualizadorFotoModule
    ]
})
export class ProductosModule {}
```

#### Con app-mini-visualizador-foto (Recomendado)

```typescript
import { Component, ViewChild, TemplateRef } from '@angular/core';

@Component({
    selector: 'app-productos',
    templateUrl: './productos.component.html'
})
export class ProductosComponent {
    @ViewChild('columnaImagen') columnaImagen: TemplateRef<any>;
    
    productos = [
        { 
            _id: '1', 
            nombre: 'Producto A', 
            imagen: 'prod-001.jpg',
            carpeta: 'productos' 
        }
    ];
    
    crearTabla() {
        const columnas: DatosColumnaTablaGenerica[] = [
            {
                titulo: 'imagen',
                tooltip: 'Visualización de la imagen',
                alineacion: 'center',
                campoCelda: {
                    template: this.columnaImagen
                }
            },
            {
                titulo: 'nombre',
                campoCelda: { funcion: (p) => p.nombre }
            }
        ];
        
        this.datosTabla = this.tablaService.generarEstructura(
            'No hay productos',
            this.productos,
            columnas
        );
    }
}
```

```html
<ng-template #columnaImagen let-contexto>
    <app-mini-visualizador-foto
        [datosImagen]="{
            nombre: contexto.datos.imagen,
            carpeta: contexto.datos.carpeta
        }"
        [medida]="'3rem'"
        [margin]="'0rem'"
    ></app-mini-visualizador-foto>
</ng-template>

<app-tabla-generica [datos]="datosTabla"></app-tabla-generica>
```

?> **NOTA**: El componente `app-mini-visualizador-foto` abre automáticamente un visor de imágenes al hacer click. Ver más en [Mini Visualizador Foto](./mini-visualizador-foto.md).

#### Con Grupo de Imágenes

```html
<ng-template #columnaImagen let-contexto>
    <app-mini-visualizador-foto
        [datosImagen]="{
            nombre: contexto.datos.imagenes[0].imagen,
            grupoDeNombres: contexto.datos.imagenes | extraerCampoDeArreglo: 'imagen',
            carpeta: 'defectos'
        }"
        [medida]="'3rem'"
        [margin]="'0rem'"
    ></app-mini-visualizador-foto>
</ng-template>
```

#### Con Imagen Directa (Sin Pipe)

```html
<ng-template #columnaImagen let-contexto>
    <app-mini-visualizador-foto
        [imagenSrc]="contexto.datos.urlCompleta"
        [medida]="'3rem'"
        [mostrarImagenConClick]="true"
    ></app-mini-visualizador-foto>
</ng-template>
```

### 2. Columna de Botones

```typescript
@ViewChild('botonesAcciones') botonesAcciones: TemplateRef<any>;

crearTabla() {
    this.datosTabla = this.tablaService.generarEstructura(
        'No hay datos',
        this.datos,
        this.columnas,
        {
            botones: this.botonesAcciones,
            tituloColumnaBotones: 'Acciones'
        }
    );
}

editar(elem: any) {
    console.log('Editar', elem);
}

eliminar(elem: any) {
    if (confirm('¿Eliminar?')) {
        // Lógica
    }
}
```

```html
<ng-template #botonesAcciones let-contexto>
    <div class="btn-group">
        <button 
            class="btn btn-sm btn-primary"
            (click)="editar(contexto.datos)"
        >
            <i class="fas fa-edit"></i>
        </button>
        <button 
            class="btn btn-sm btn-danger"
            (click)="eliminar(contexto.datos)"
        >
            <i class="fas fa-trash"></i>
        </button>
    </div>
</ng-template>
```

### 3. Columna de Estatus

```typescript
@ViewChild('estatusElemento') estatusElemento: TemplateRef<any>;

crearTabla() {
    this.datosTabla = this.tablaService.generarEstructura(
        'No hay órdenes',
        this.ordenes,
        this.columnas,
        {
            estatus: this.estatusElemento,
            tituloEstatus: 'Estado'
        }
    );
}
```

```html
<ng-template #estatusElemento let-contexto>
    <span 
        class="badge"
        [ngClass]="{
            'badge-success': contexto.datos.estado === 'COMPLETADO',
            'badge-warning': contexto.datos.estado === 'EN_PROCESO',
            'badge-danger': contexto.datos.estado === 'CANCELADO'
        }"
    >
        {{ contexto.datos.estado }}
    </span>
</ng-template>
```

### 4. Columna Desplegable

```typescript
@ViewChild('desplegable') desplegable: TemplateRef<any>;

crearTabla() {
    this.datosTabla = this.tablaService.generarEstructura(
        'No hay pedidos',
        this.pedidos,
        this.columnas,
        {
            desplegable: this.desplegable
        }
    );
}
```

```html
<ng-template #desplegable let-contexto>
    <div class="card">
        <div class="card-body">
            <h5>Detalles #{{ contexto.datos.numero }}</h5>
            <hr>
            <p><strong>Cliente:</strong> {{ contexto.datos.cliente }}</p>
        </div>
    </div>
</ng-template>
```

<hr class='hr-principal'>

## Modo Selección Múltiple

### Activación

```html
<app-tabla-generica
    [datos]="datosTabla"
    [modoSeleccion]="true"
    [campoSeleccion]="'_id'"
    [seleccionOtrasPaginas]="listaSeleccionados"
    [ObjetosOtrasPaginas]="objetosSeleccionados"
    (seleccionado)="cargarSeleccionados($event)"
    (objetosSeleccionados)="cargarObjetos($event)"
></app-tabla-generica>
```

### Implementación

```typescript
export class SelectorComponent {
    datosTabla: DatosTablaGenerica;
    modoSeleccion = true;
    listaSeleccionados: any[] = [];
    objetosSeleccionados: any = {};
    
    cargarSeleccionados(ids: any[]) {
        this.listaSeleccionados = ids;
    }
    
    cargarObjetos(objetos: any) {
        this.objetosSeleccionados = objetos;
    }
}
```

### Botones de Ayuda

Aparecen automáticamente:

- **❌ Limpiar todo** (rojo): Deselecciona toda la selección
- **🧹 Limpiar página** (naranja): Deselecciona solo página actual
- **✓ Seleccionar página** (verde): Selecciona toda la página actual

<hr class='hr-principal'>

## Barras de Progreso CSS

```typescript
clasesPorFila(elem: any, crearCallback: any, conteo: number, anterior: boolean) {
    return crearCallback(
        [
            {
                clase: 'barra-progreso-una-fila blanco-hover-primera-col',
                aplicar: elem.porcentaje > 0 && !this.enMovil,
                ngStyleNombre: '--barra',
                ngStyleValor: `${elem.porcentaje}%`
            }
        ],
        conteo,
        anterior,
        false  // false = sin agrupar, true = agrupar con bordes
    );
}

crearTabla() {
    this.datosTabla = this.tablaService.generarEstructura(
        'No hay datos',
        this.datos,
        this.columnas,
        {
            ngClassCallback: this.clasesPorFila.bind(this)
        }
    );
}
```

### Clases CSS Disponibles

- `barra-progreso-una-fila`: Barra horizontal
- `llenado-botella`: Efecto de llenado vertical
- `blanco-hover-primera-col`: Fondo blanco en hover

<hr class='hr-principal'>

## Modo Móvil Responsivo

### Configuración Básica

```typescript
{
    campoAMostrarMovil: 'nombre',
    campoSecundario1Movil: 'categoria',
    campoSecundario2Movil: 'precio',
    buscadorEnMovil: true,
    paginadorEnMovil: true
}
```

### Con Pipes y Estilos

```typescript
{
    campoAMostrarMovil: 'nombre',
    classCampoAMostrarMovilCallback: () => 'text-primary font-bold',
    
    campoSecundario2Movil: 'precio',
    PipeCampoSecundario2Movil: DecimalPipe,
    PipeArgsCampoSecundario2Movil: ['1.2-2'],
    sufijoCampoSecundario2MovilCallback: () => ' USD'
}
```

### Breakpoints Personalizados

```typescript
breakpointsTabla: EstiloMallaCantidadColumnasMoviles = {
    '--conteo-de-columnas-xs': 1,
    '--conteo-de-columnas-sm': 2,
    '--conteo-de-columnas-md': 3,
    '--conteo-de-columnas-lg': 4,
    '--conteo-de-columnas-xl': 5,
    '--conteo-de-columnas-xxl': 6
};
```

```html
<app-tabla-generica
    [datos]="datosTabla"
    [enMovil]="true"
    [breakPointsColumnasMoviles]="breakpointsTabla"
></app-tabla-generica>
```

<hr class='hr-principal'>

## Exportar y Copiar

### Botones Automáticos

Cuando `[botonesCopiar]="true"` (por defecto):

1. **Modo Tabla/Copiar**: Alterna entre modo normal y modo copiar
2. **Copiar con encabezados**: Copia toda la tabla
3. **Copiar sin encabezados**: Copia solo datos
4. **Imprimir**: Abre ventana de impresión

### Desactivar

```html
<app-tabla-generica
    [datos]="datosTabla"
    [botonesCopiar]="false"
></app-tabla-generica>
```

<hr class='hr-principal'>

## Uso en Modal

```typescript
@ViewChild('modalTabla') modalTabla: ModalComponent;

abrirModal() {
    this.modalTabla.mostrarModal();
}
```

```html
<app-modal
    #modalTabla
    [medida]="'gigante'"
    [usarModalFalso]="true"
>
    <ng-container encabezado>
        <h5><i class="fas fa-list"></i> Lista</h5>
    </ng-container>
    
    <ng-container contenido>
        <app-tabla-generica
            [datos]="datosTabla"
            [enModal]="true"
            [ajustarTablaAlMaximoScrollPosible]="true"
        ></app-tabla-generica>
    </ng-container>
</app-modal>
```

<hr class='hr-principal'>

## Componentes Relacionados

- **[Paginador](./paginacion-y-filtros.md)**: Para paginación de datos
- **[Modal](./modal.md)**: Para uso en modales
- **[Historial](./historial.md)**: Para ver cambios de elementos

<hr class='hr-principal'>

## Resumen

La **Tabla Genérica** es el componente más completo de CARRDUCI, con:

✅ **54+ implementaciones** reales  
✅ **Selección múltiple** con botones de ayuda  
✅ **Columnas especiales** (imágenes, botones, estatus, desplegables)  
✅ **Modo móvil** responsive estilo masonry  
✅ **Barras de progreso** CSS  
✅ **Exportar/Copiar**  
✅ **Templates personalizados**  
✅ **ngClass avanzado**  
✅ **Uso en modales**

Este componente es fundamental para mostrar datos tabulares en todo el sistema.
