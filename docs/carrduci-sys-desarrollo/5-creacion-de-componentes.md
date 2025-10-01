# Creación de Componentes en CARRDUCI

Este documento es la guía **completa y detallada** para crear componentes en el sistema CARRDUCI. Está diseñado para desarrolladores nuevos que necesitan entender **todo el proceso** desde cero, incluyendo tanto la interfaz gráfica (GUI) como la API (backend).

!> **IMPORTANTE**: Esta guía asume que tienes conocimientos básicos de Angular, TypeScript, Node.js, Express y MongoDB. Si eres completamente nuevo, revisa primero la documentación de instalación y estructura del proyecto.

!> **⚠️ CAMBIO ARQUITECTURAL IMPORTANTE**

**A partir de ahora, la carpeta `pages/` ya NO se utiliza para nuevos desarrollos.** Todo se crea directamente en `components/`, incluyendo:

-   ✅ **Servicios** (`src/app/services/`)
-   ✅ **Modelos** (`src/app/models/`)
-   ✅ **Componentes de vista** (`src/app/components/`)
-   ✅ **Pipes** (`src/app/components/[dominio]/pipes-[dominio]/`)
-   ✅ **Utilidades** (`src/app/utils/`)

### Estructura Actualizada (Nueva Arquitectura)

```
carrduci-sys-gui/src/app/
├── components/                                           # 🏗️ NUEVO: Todo se crea aquí
│   ├── utiles/                                           # Componentes reutilizables
│   ├── [dominio-nuevo]/                                  # Nuevos módulos aquí
│   │   ├── vista-[dominio]-gestion/                      # ✅ Cada componente SU módulo
│   │   │   ├── vista-[dominio]-gestion.component.ts
│   │   │   ├── vista-[dominio]-gestion.component.html
│   │   │   ├── vista-[dominio]-gestion.component.css
│   │   │   └── vista-[dominio]-gestion.module.ts         # ✅ Cada componente SU módulo
│   │   ├── [dominio]-filtros/                            # ✅ Cada componente SU módulo
│   │   │   ├── [dominio]-filtros.component.ts
│   │   │   ├── [dominio]-filtros.component.html
│   │   │   ├── [dominio]-filtros.component.css
│   │   │   └── [dominio]-filtros.module.ts
│   │   ├── pipes-[dominio]/                              # ✅ Pipes específicos
│   │   │   ├── pipes-[dominio].module.ts
│   │   │   └── pipe-[dominio]-[desc].pipe/               # ✅ Cada pipe: pipe-[dominio]-[desc].pipe
│   │   ├── servicios-[dominio]/                          # ✅ Servicios del dominio
│   │   └── modelos-[dominio]/                            # ✅ Modelos del dominio
│   └── [módulos existentes]/
├── services/                                             # Servicios HTTP globales
├── models/                                               # Interfaces TypeScript globales
├── pages/                                                # ⚠️ DEPRECATED: Solo para compatibilidad
├── pipes/                                                # Pipes globales (si aplica)
└── [otros directorios]/
```

### Arquitectura de Rutas Futura (Lazy Loading por Dominio)

**⚠️ IMPORTANTE: Esta sección describe la arquitectura objetivo A FUTURO. Actualmente NO está implementada y se mantiene la estructura actual.**

#### Visión General de Lazy Loading

En una siguiente fase de optimización, se implementará un sistema de lazy loading más granular que organizará las rutas por niveles jerárquicos (menú → dominio → funcionalidad), permitiendo una carga más eficiente de los módulos según sea necesario.

#### Estructura Conceptual Futura

```
carrduci-sys-gui/src/app/
├── components/
│   ├── [dominio]/                    # Dominio completo
│   │   ├── [dominio].routes.ts       # Rutas específicas del dominio
│   │   ├── vista-[dominio]-*         # Vistas específicas
│   │   └── [dominio]-*               # Componentes auxiliares
│   └── [otros-dominios]/
├── pages/
│   ├── [menu].routes.ts              # Rutas del menú principal
│   └── pages.routes.ts               # Solo importa rutas de menús
└── [estructura actual mantenida]
```

##### Rutas en `pages.routes.ts` (Futuro)

```typescript
// pages.routes.ts - Futuro
{
    path: 'administracion',
    canActivate: [VerificaTokenGuard, PermisosGuard],
    loadChildren: () => import('./components/administracion/administracion.routes').then(m => m.AdministracionRoutes),
    data: {
        titulo: 'Administración',
    }
}
```

##### Rutas en `login.menus.js` (Futuro)

```javascript
// login.menus.js - Futuro
function administracion() {
	const menu = {
		permiso: permisos.$('menu:administracion', false),
		titulo: 'Administración',
		icono: 'fas fa-cogs',
		submenu: [
			{
				titulo: 'Proveedores',
				url: '/administracion/proveedores',
				permiso: permisos.$('menu:administracion:proveedores', false),
			},
			// ... otros submenús de administración
		],
	};
	return menu;
}
```

-   **Lazy Loading por dominio**: Las rutas apuntan a módulos específicos que se cargan bajo demanda
-   **Rutas jerárquicas**: Organización clara por dominio (administracion/proveedores)
-   **Permisos granulares**: Cada submódulo tiene sus propios permisos
-   **Mantenibilidad**: Fácil agregar nuevos submenús sin afectar la estructura existente

### Notas sobre la Transición

-   **📁 Carpeta `pages/` existente**: Se mantiene por **compatibilidad hacia atrás** con código existente
-   **🚫 NO crear nuevos archivos** en `pages/` bajo ninguna circunstancia
-   **🔄 Migración futura**: El código existente en `pages/` se migrará gradualmente a `components/`
-   **⚡ Desarrollo inmediato**: Todos los nuevos módulos van directamente en `components/`

### Ejemplo de Nueva Estructura Completa (Sin Lazy Loading)

Para un nuevo módulo de **"gestión de proveedores"**:

```
components/proveedores/                                                        # ❌ NO proveedores.module.ts
├── vista-proveedores-gestion/                                                 # ✅ Cada componente SU módulo
│   ├── vista-proveedores-gestion.component.ts
│   ├── vista-proveedores-gestion.component.html
│   ├── vista-proveedores-gestion.component.css
│   └── vista-proveedores-gestion.module.ts
├── proveedores-filtros/                                                      # ✅ Cada componente SU módulo
│   ├── proveedores-filtros.component.ts
│   ├── proveedores-filtros.component.html
│   ├── proveedores-filtros.component.css
│   └── proveedores-filtros.module.ts
├── pipes-proveedores/                                                        # ✅ Directorio principal de pipes
│   ├── pipes-proveedores.module.ts                                           # ✅ Módulo que agrupa todos los pipes
│   ├── pipes-estado/                                                         # ✅ Subdirectorio por funcionalidad
│   │   ├── obtener-estado-proveedor/                                         # ✅ Cada pipe SU directorio
│   │   │   ├── obtener-estado-proveedor.pipe.ts                              # ✅ Archivo del pipe
│   │   │   └── obtener-estado-proveedor.pipe.spec.ts                         # ✅ Archivo de pruebas
│   │   └── formatear-estado-proveedor/                                       # ✅ Otro pipe SU directorio
│   │       ├── formatear-estado-proveedor.pipe.ts
│   │       └── formatear-estado-proveedor.pipe.spec.ts
│   └── pipes-formato/                                                        # ✅ Otro subdirectorio funcional
│       ├── formatear-fecha-proveedor/                                        # ✅ Pipe individual SU directorio
│       │   ├── formatear-fecha-proveedor.pipe.ts
│       │   └── formatear-fecha-proveedor.pipe.spec.ts
│       └── formatear-telefono-proveedor/                                     # ✅ Otro pipe individual
│           ├── formatear-telefono-proveedor.pipe.ts
│           └── formatear-telefono-proveedor.pipe.spec.ts
├── proveedores.service.ts                                                    # ✅ Servicio del dominio
└── proveedores.model.ts                                                      # ✅ Modelos del dominio
```

### Arquitectura de Módulos (CORREGIDA)

**❌ NO crear módulos principales por dominio.** Cada componente debe tener su propio módulo independiente:

```typescript
// ❌ NO HACER - Módulo principal por dominio
@NgModule({
	declarations: [TodosLosComponentesDelDominio],
	imports: [CommonModule],
})
export class DominioModule {} // ❌ NO CREAR ESTO

// ✅ CORRECTO - Cada componente su módulo
@NgModule({
	declarations: [VistaAdministracionProveedoresComponent],
	imports: [CommonModule],
	exports: [VistaAdministracionProveedoresComponent],
})
export class VistaAdministracionProveedoresModule {} // ✅ SÍ CREAR ESTO
```

### Módulos por Componente (Regla Estricta)

**Cada componente individual debe tener su propio módulo**:

-   ✅ `vista-administracion-proveedores.module.ts` (módulo del componente de vista)
-   ✅ `proveedores-filtros.module.ts` (módulo del componente auxiliar)
-   ✅ `pipes-para-proveedores.module.ts` (módulo de pipes compartidos)
-   ❌ `proveedores.module.ts` (módulo principal del dominio - NO CREAR)

```typescript
// components/proveedores/proveedores.service.ts
@Injectable({
	providedIn: 'root', // Servicio global o módulo específico
})
export class ProveedoresService {
	// Lógica del servicio aquí
}

// components/proveedores/proveedores.model.ts
export interface Proveedor {
	id: string;
	nombre: string;
	contacto: string;
	// ... otros campos
}
```

### Registro de Rutas (Actualizado)

Para componentes creados en `components/`, el registro de rutas cambia significativamente. Dado que cada componente tiene su propio módulo independiente (regla estricta: "cada componente su módulo"), se debe usar **`loadComponent`** en lugar de `loadChildren`.

#### ¿Por qué `loadComponent` en lugar de `loadChildren`?

-   **`loadComponent`**: Ideal para componentes individuales con módulos independientes. Carga el componente directamente sin necesidad de módulos complejos.
-   **`loadChildren`**: Se usa para cargar módulos completos que contienen múltiples rutas y componentes (lazy loading por dominio completo).

En CARRDUCI, como **NO creamos módulos principales por dominio**, cada componente es independiente y debe cargarse con `loadComponent`.

**Sin embargo, para el futuro lazy loading por dominio**, `loadChildren` SÍ se puede usar para cargar archivos de rutas directamente:

#### ✅ Futuro: `loadChildren` con archivos `.routes.ts`

```typescript
// ✅ CORRECTO para lazy loading FUTURO por dominio
{
    path: 'administracion',
    loadChildren: () => import('./components/administracion/administracion.routes').then(m => m.ADMINISTRACION_ROUTES),
    canActivate: [VerificaTokenGuard, PermisosGuard],
    data: {
        titulo: 'Administración',
    }
}

// Archivo: components/administracion/administracion.routes.ts
import { Routes } from '@angular/router';

export const ADMINISTRACION_ROUTES: Routes = [
    {
        path: '',
        pathMatch: 'full',
        redirectTo: 'proveedores'
    },
    {
        path: 'proveedores',
        loadComponent: () => import('./vista-administracion-proveedores/vista-administracion-proveedores.component').then(m => m.VistaAdministracionProveedoresComponent),
        canActivate: [VerificaTokenGuard, PermisosGuard],
        data: {
            titulo: 'Administración de proveedores',
            permissions: permisosKeysConfig['menu:administracion:proveedores']
        }
    },
    // ... más rutas del dominio administración
];
```

**Ventajas del enfoque híbrido futuro:**

-   ✅ **Lazy loading por dominio**: Carga todas las rutas de un dominio bajo demanda
-   ✅ **Componentes individuales**: Dentro del dominio, cada componente se carga individualmente
-   ✅ **Arquitectura escalable**: Fácil agregar nuevos componentes al dominio
-   ✅ **Mantenibilidad**: Separación clara entre configuración de dominio y componentes individuales

#### 🕐 **Actualidad: `loadComponent` para componentes individuales**

En la **actualidad**, siguiendo la regla estricta de CARRDUCI ("cada componente su módulo"), todos los componentes se cargan individualmente usando `loadComponent`.

⚠️ **IMPORTANTE**: Actualmente en `pages.routes.ts` NO se está usando `loadComponent` (todas las rutas usan `component:` directamente). Sin embargo, **de ahora en adelante** todas las rutas nuevas DEBEN usar `loadComponent` para mantener consistencia y preparar el terreno para futuras migraciones de lazy loading.

Esto significa que cada ruta en `pages.routes.ts` carga directamente su componente específico:

```typescript
// pages.routes.ts - Ejemplo ACTUAL para componente en components/
{
    path: 'administracion/proveedores',
    canActivate: [VerificaTokenGuard, PermisosGuard],
    loadComponent: () => import('./components/proveedores/vista-administracion-proveedores/vista-administracion-proveedores.component').then(m => m.VistaAdministracionProveedoresComponent),
    data: {
        titulo: 'Administración de proveedores',
        permissions: permisosKeysConfig['menu:administracion:proveedores']
    }
}
```

**Características de la implementación actual:**

-   ✅ **Componentes independientes**: Cada vista tiene su propio módulo y se carga individualmente
-   ✅ **Rutas directas**: No hay intermediarios entre la ruta y el componente
-   ✅ **Mantenibilidad inmediata**: Fácil agregar/modificar rutas sin afectar otras
-   ✅ **Transición preparada**: Estructura actual facilita migración futura al lazy loading por dominio

#### ❌ **Incorrecto - NO usar `loadChildren` para componentes individuales**

```typescript
// pages.routes.ts - Ejemplo para componente en components/
// ❌ INCORRECTO - NO usar loadChildren para componentes individuales
{
    path: 'administracion/proveedores',
    component: VistaAdministracionProveedoresComponent,
    canActivate: [VerificaTokenGuard, PermisosGuard],
    loadChildren: () => import('./components/proveedores/vista-administracion-proveedores/vista-administracion-proveedores.module').then(m => m.VistaAdministracionProveedoresModule), // ❌ NO USAR
    data: {
        titulo: 'Administración de proveedores',
        permissions: permisosKeysConfig['menu:administracion:proveedores']
    }
}
```

#### Beneficios de `loadComponent`:

-   ✅ **Bundle más pequeño**: Solo carga el componente específico cuando se necesita
-   ✅ **Arquitectura más simple**: No requiere módulos complejos por dominio
-   ✅ **Mejor mantenibilidad**: Cada componente es independiente
-   ✅ **Performance óptima**: Lazy loading a nivel de componente individual

#### Organización de `pages.routes.ts` con Separadores de Sección

El archivo `pages.routes.ts` debe estar organizado usando los separadores de sección definidos en [`4-estructuras-de-documentacion.md`](./docs/carrduci-sys-desarrollo/4-estructuras-de-documentacion.md). Esto debe implementarse **antes del lazy loading** para mantener el orden durante la transición.

##### Estructura Recomendada para `pages.routes.ts`:

```typescript
// (o==================================================================o)
//   #region IMPORTS
// (o-----------------------------------------------------------\/-----o)

// Importaciones externas
import { Routes } from '@angular/router';
import { VerificaTokenGuard } from '../guards/verifica-token.guard';
import { PermisosGuard } from '../guards/permisos.guard';

// Importaciones de configuración
import permisosKeysConfig from 'src/app/config/permisosKeys.config';

// (o-----------------------------------------------------------/\-----o)
//   #endregion IMPORTS
// (o==================================================================o)

// (o==================================================================o)
//   #region ALMACEN
// (o-----------------------------------------------------------\/-----o)

// (o,,,,,,,,,,,CONTEOS,,,,,,,,,,o)
//   #region    conteos
// (o'''''''''''CONTEOS''''v'''''o)

export const rutasAlmacenConteos: Routes = [
	{
		path: 'almacen/conteos/supervision',
		canActivate: [VerificaTokenGuard, PermisosGuard],
		loadComponent: () =>
			import(
				'./components/conteos/vista-supervision-conteos/vista-supervision-conteos.component'
			).then((m) => m.VistaSupervisionConteosComponent),
		data: {
			titulo: 'Gestión de conteos (inventarios)',
			permissions: permisosKeysConfig['menu:almacen:supervisionConteos'],
		},
	},
	{
		path: 'almacen/conteos/produccion',
		canActivate: [VerificaTokenGuard, PermisosGuard],
		loadComponent: () =>
			import(
				'./components/conteos/vista-produccion-conteos/vista-produccion-conteos.component'
			).then((m) => m.VistaProduccionConteosComponent),
		data: {
			titulo: 'Conteos de producción',
			permissions: permisosKeysConfig['menu:almacen:produccionConteos'],
		},
	},
	// ... más rutas de conteos
];

// (o,,,,,,,,,,,CONTEOS,,,,^,,,,,o)
//   #endregion conteos
// (o'''''''''''CONTEOS''''''''''o)

// (o,,,,,,,,,,,MATERIA PRIMA,,,,,,,,,,o)
//   #region    materia prima
// (o'''''''''''MATERIA PRIMA''''v'''''o)

export const rutasAlmacenMateriaPrima: Routes = [
	// Rutas de materia prima aquí
];

// (o,,,,,,,,,,,MATERIA PRIMA,,,,^,,,,,o)
//   #endregion materia prima
// (o'''''''''''MATERIA PRIMA''''''''''o)

// (o-----------------------------------------------------------/\-----o)
//   #endregion ALMACEN
// (o==================================================================o)

// (o==================================================================o)
//   #region ADMINISTRACION
// (o-----------------------------------------------------------\/-----o)

export const rutasAdministracion: Routes = [
	{
		path: 'administracion/proveedores',
		canActivate: [VerificaTokenGuard, PermisosGuard],
		loadComponent: () =>
			import(
				'./components/proveedores/vista-administracion-proveedores/vista-administracion-proveedores.component'
			).then((m) => m.VistaAdministracionProveedoresComponent),
		data: {
			titulo: 'Administración de proveedores',
			permissions: permisosKeysConfig['menu:administracion:proveedores'],
		},
	},
	// ... más rutas de administración
];

// (o-----------------------------------------------------------/\-----o)
//   #endregion ADMINISTRACION
// (o==================================================================o)

// (o==================================================================o)
//   #region EXPORT
// (o-----------------------------------------------------------\/-----o)

// Exportar todas las rutas agrupadas por dominio
export const pagesRoutes: Routes = [
	...rutasAlmacenConteos,
	...rutasAlmacenMateriaPrima,
	...rutasAdministracion,
	// ... otras rutas agrupadas
];

// (o-----------------------------------------------------------/\-----o)
//   #endregion EXPORT
// (o==================================================================o)
```

##### Beneficios de esta organización:

-   ✅ **Navegación clara**: Fácil encontrar rutas por dominio
-   ✅ **Mantenimiento eficiente**: Modificar rutas sin afectar otros dominios
-   ✅ **Escalabilidad**: Agregar nuevos dominios sin desorganizar el archivo
-   ✅ **Transición ordenada**: Preparado para lazy loading futuro por dominio
-   ✅ **Consistencia**: Sigue estándares de documentación CARRDUCI

### Impacto en Desarrollo

**Beneficios inmediatos**:

-   ✅ **Localización rápida** del código por dominio
-   ✅ **Menos navegación** entre carpetas
-   ✅ **Dependencias claras** entre componentes relacionados
-   ✅ **Mantenimiento más eficiente**

**Para desarrolladores existentes**:

-   ✅ **Continuar trabajando** con código existente en `pages/`
-   ✅ **Crear nuevos módulos** directamente en `components/`
-   ✅ **Referenciar ambos** durante la transición

**Para nuevos desarrolladores**:

-   ✅ **Enfocarse únicamente** en `components/` para nuevos desarrollos
-   ✅ **No tocar** código existente en `pages/`

## 1. Planificación Inicial

### 1.1 Identificar el Dominio

**Paso crítico**: Antes de crear cualquier componente, identifica claramente:

-   **¿Qué dominio maneja?** (almacenes, ventas, producción, etc.)
-   **¿Qué funcionalidad específica?** (inventarios, reportes, supervision, etc.)
-   **¿Qué usuarios lo usarán?** (almacén, ventas, administración, etc.)

### 1.2 Estructura de Carpetas Recomendada

```
components/[dominio-principal]/
├── pipes-[dominio-principal]/                                                 # Pipes específicos del dominio (puede haber múltiples)
│   ├── pipes-[dominio-principal].module.ts
│   └── [pipes específicos]/
├── vista-[dominio-principal]-[vista-principal]/                               # Componente de vista principal
│   ├── vista-[dominio-principal]-[vista-principal].component.ts
│   ├── vista-[dominio-principal]-[vista-principal].component.html
│   ├── vista-[dominio-principal]-[vista-principal].component.css
│   └── vista-[dominio-principal]-[vista-principal].module.ts                  # ✅ Módulo individual del componente
├── vista-[dominio-principal]-[vista-secundaria]/                              # Componentes de vista adicionales (puede haber múltiples)
│   ├── vista-[dominio-principal]-[vista-secundaria].component.ts
│   ├── vista-[dominio-principal]-[vista-secundaria].component.html
│   ├── vista-[dominio-principal]-[vista-secundaria].component.css
│   └── vista-[dominio-principal]-[vista-secundaria].module.ts                 # ✅ Módulo individual del componente
├── [dominio-principal]-[funcionalidad-secundaria]/                            # Componentes auxiliares del dominio (puede haber múltiples)
│   ├── [dominio-principal]-[funcionalidad-secundaria].component.ts
│   ├── [dominio-principal]-[funcionalidad-secundaria].component.html
│   ├── [dominio-principal]-[funcionalidad-secundaria].component.css
│   └── [dominio-principal]-[funcionalidad-secundaria].module.ts               # ✅ Módulo individual del componente
└── [otros-submodulos]/                                                        # Otros submodulos del dominio (puede haber múltiples)
```

**Reglas de nomenclatura estrictas:**

-   **Componentes de vista**: `vista-[dominio]-[nombre-vista].component`
-   **Componentes auxiliares**: `[dominio]-[funcionalidad-secundaria].component`
-   **Pipes**: `[dominio]-[descripcion].pipe`
-   **Servicios**: `[dominio]-[funcionalidad].service`
-   **Modelos**: `[dominio]-[entidad].model`

**⚠️ REGLA CRÍTICA CARRDUCI: NO crear módulos principales por dominio**

Cada componente debe tener su propio módulo independiente. **NO** se crea `[dominio-principal].module.ts` como módulo "principal" del dominio. Cada vista y componente auxiliar tiene su propio módulo individual.

**Ejemplo real de conteos**:

```
components/conteos/
├── pipes-para-conteos/
│   ├── pipes-para-conteos.module.ts
│   └── pipes-detalle/, pipes-estatus/, etc.
├── vista-conteos-supervision/
│   ├── vista-conteos-supervision.component.ts
│   ├── vista-conteos-supervision.component.html
│   ├── vista-conteos-supervision.component.css
│   └── vista-conteos-supervision.module.ts         # ✅ Módulo individual de este componente
├── vista-conteos-informes/
│   ├── vista-conteos-informes.component.ts
│   ├── vista-conteos-informes.component.html
│   ├── vista-conteos-informes.component.css
│   └── vista-conteos-informes.module.ts            # ✅ Módulo individual de este componente
├── conteos-filtros/
│   ├── conteos-filtros.component.ts
│   ├── conteos-filtros.component.html
│   ├── conteos-filtros.component.css
│   └── conteos-filtros.module.ts                   # ✅ Módulo individual de este componente
├── conteos-detalle/
├── conteos-estatus/
├── conteos-formulario-creacion/
└── [otros componentes auxiliares]/
```

## 2. Creación de Componentes GUI

### 2.1 Tipos de Componentes

#### Componentes de Vista (Vista Components)

-   **Nombre**: `vista-[dominio]-[nombre-vista].component` (ej: `vista-conteos-supervision.component`, `vista-almacen-producto-terminado.component`)
-   **Propósito**: Páginas principales que aparecen en el menú lateral
-   **Características**:
    -   Requieren permisos específicos del sistema
    -   Se registran en `login.menus.js` para aparecer en el menú
    -   Manejan funcionalidades completas del módulo
    -   Generalmente tienen rutas asociadas en `pages.routes.ts`

#### Componentes Auxiliares (Auxiliary Components)

-   **Nombre**: `[dominio]-[funcionalidad-secundaria].component` (ej: `conteos-filtros.component`, `almacen-detalle.component`, `produccion-estatus.component`)
-   **Propósito**: Componentes reutilizables dentro de un dominio
-   **Características**:
    -   No requieren permisos independientes
    -   Se usan dentro de componentes de vista
    -   Funcionalidades específicas y reutilizables
    -   Siempre incluyen el nombre del dominio como prefijo

### 2.2 Creación Paso a Paso

#### Paso 1: Generar el Componente

```bash
# Navegar al directorio del proyecto GUI
cd carruci-sys-gui

# Crear componente de vista (ejemplo para supervision de conteos)
ng generate component components/conteos/vista-conteos-supervision

# Crear componente auxiliar (ejemplo para filtros)
ng generate component components/conteos/conteos-filtros
```

#### Paso 2: Crear el Módulo del Componente

Cada componente debe tener su propio módulo independiente:

```typescript
// vista-conteos-supervision.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VistaConteosSupervisionComponent } from './vista-conteos-supervision.component';

// Importar componentes reutilizables que usarás
import { TablaGenericaModule } from 'src/app/components/utiles/tabla-generica/tabla-generica.module';
import { FormularioDinamicoModule } from 'src/app/components/utiles/formulario-dinamico/formulario-dinamico.module';
import { ModalModule } from 'src/app/pages/utilidadesPages/utilidades-tipo-crud-para-GUI/plantillas/modal.module';

@NgModule({
	declarations: [
		VistaConteosSupervisionComponent,
		// Declarar aquí otros componentes internos si los tienes
	],
	imports: [
		CommonModule,
		TablaGenericaModule, // Para tablas paginadas
		FormularioDinamicoModule, // Para formularios reactivos
		ModalModule, // Para modales (siempre con [modalFalso]="true")
		// Otros módulos necesarios
	],
	exports: [
		VistaConteosSupervisionComponent,
		// Exportar componentes que otros módulos puedan usar
	],
})
export class VistaConteosSupervisionModule {}
```

#### Paso 3: Implementar el Componente

```typescript
// vista-conteos-supervision.component.ts
import { Component, OnInit } from '@angular/core';
import { ConteosService } from 'src/app/services/conteos/conteos.service';

@Component({
	selector: 'app-vista-conteos-supervision',
	templateUrl: './vista-conteos-supervision.component.html',
	styleUrls: ['./vista-conteos-supervision.component.css'],
})
export class VistaConteosSupervisionComponent implements OnInit {
	// Propiedades del componente
	conteos: any[] = [];
	cargando = false;
	filtros: any = {};

	constructor(private conteosService: ConteosService) {}

	ngOnInit(): void {
		this.cargarConteos();
	}

	cargarConteos() {
		this.cargando = true;

		// Ejemplo de búsqueda unificada (como se usa en el sistema real)
		this.conteosService
			.buscar({
				filtros: this.filtros,
				termino: '', // término de búsqueda
				pagina: 1,
				limite: 10,
				orden: { createdAt: -1 }, // más reciente primero
			})
			.subscribe({
				next: (resultado) => {
					this.conteos = resultado.datos;
					this.cargando = false;
				},
				error: (error) => {
					console.error('Error al cargar conteos:', error);
					this.cargando = false;
				},
			});
	}

	aplicarFiltros(filtros: any) {
		this.filtros = filtros;
		this.cargarConteos();
	}
}
```

#### Paso 4: Template HTML

```html
<!-- vista-conteos-supervision.component.html -->
<div class="container-fluid">
	<div class="row">
		<div class="col-12">
			<h2 class="mb-4">
				<i class="fas fa-clipboard-check"></i>
				Supervisión de Conteos
			</h2>
		</div>
	</div>

	<!-- Filtros -->
	<div class="row mb-3">
		<div class="col-12">
			<app-conteos-filtros
				[filtrosIniciales]="filtros"
				(filtrosAplicados)="aplicarFiltros($event)"
			>
			</app-conteos-filtros>
		</div>
	</div>

	<!-- Tabla de conteos -->
	<div class="row">
		<div class="col-12">
			<app-tabla-generica
				[datos]="conteos"
				[cargando]="cargando"
				[columnas]="columnasTabla"
				[acciones]="accionesTabla"
				[paginacion]="true"
				(accionEjecutada)="ejecutarAccion($event)"
			>
			</app-tabla-generica>
		</div>
	</div>
</div>
```

#### Paso 5: Estilos CSS

```css
/* vista-conteos-supervision.component.css */
.container-fluid {
	padding: 20px;
}

.card {
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	border: none;
	margin-bottom: 20px;
}

/* Estados de los conteos */
.estado-borrador {
	background-color: #fff3cd;
	color: #856404;
}

.estado-revision {
	background-color: #d1ecf1;
	color: #0c5460;
}

.estado-aprobado {
	background-color: #d4edda;
	color: #155724;
}

.estado-finalizado {
	background-color: #f8f9fa;
	color: #6c757d;
}
```

### 2.3 Sistema de Pipes

#### Organización de Pipes

Los pipes se organizan por dominio y se comparten entre componentes del mismo objetivo. Cada pipe debe seguir la convención de nomenclatura: `pipe-[dominio]-[descripcion].pipe.ts`

> ⚠️ **NOTA**: Los pipes en este ejemplo están mal nombrados según las reglas de nomenclatura CARRDUCI. Se muestran para mantener consistencia con el sistema existente, pero **NO deben usarse como referencia para nuevos pipes**.

```
components/conteos/
└── pipes-para-conteos/
    ├── pipes-para-conteos.module.ts
    ├── pipes-estatus/
    │   ├── conteo/
    │   │   ├── obtener-estatus-conteo/                        # ✅ Cada pipe SU directorio
    │   │   │   ├── obtener-estatus-conteo.pipe.ts
    │   │   │   └── obtener-estatus-conteo.pipe.spec.ts
    │   │   ├── obtener-clase-badge-estatus-conteo/
    │   │   │   ├── obtener-clase-badge-estatus-conteo.pipe.ts
    │   │   │   └── obtener-clase-badge-estatus-conteo.pipe.spec.ts
    │   │   └── [otros pipes de conteo]/
    │   └── linea-conteo/
    │       ├── obtener-estatus-linea-conteo/
    │       │   ├── obtener-estatus-linea-conteo.pipe.ts
    │       │   └── obtener-estatus-linea-conteo.pipe.spec.ts
    │       └── [otros pipes de línea de conteo]/
    └── pipes-detalle/
        ├── obtener-especificacion-detalle-contada/
        │   ├── obtener-especificacion-detalle-contada.pipe.ts
        │   └── obtener-especificacion-detalle-contada.pipe.spec.ts
        └── obtener-especificacion-detalle-linea-conteo/
            ├── obtener-especificacion-detalle-linea-conteo.pipe.ts
            └── obtener-especificacion-detalle-linea-conteo.pipe.spec.ts
```

#### Ejemplo de Pipe

```typescript
// pipes-conteos/pipe-conteos-estado.pipe.ts  ❌ NOMBRE INCORRECTO
// pipes-para-conteos/pipes-estatus/estado-conteo.pipe.ts  ❌ NOMBRE INCORRECTO
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
	name: 'estadoConteo',
})
export class EstadoConteoPipe implements PipeTransform {
	transform(estado: string): string {
		const estados = {
			borrador: 'Borrador',
			revision: 'En Revisión',
			aprobado: 'Aprobado',
			finalizado: 'Finalizado',
			cancelado: 'Cancelado',
		};

		return estados[estado] || estado;
	}
}
```

#### ✅ Nomenclatura Correcta para Pipes (Futuras Creaciones)

```typescript
// ✅ NOMBRE CORRECTO según reglas CARRDUCI
// pipes-para-conteos/conteos-estado.pipe.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
	name: 'conteosEstado', // ✅ Nombre siguiendo convención [dominio][Descripcion]
})
export class ConteosEstadoPipe implements PipeTransform {
	transform(estado: string): string {
		const estados = {
			borrador: 'Borrador',
			revision: 'En Revisión',
			aprobado: 'Aprobado',
			finalizado: 'Finalizado',
			cancelado: 'Cancelado',
		};

		return estados[estado] || estado;
	}
}
```

**Estructura recomendada para nuevos pipes:**

```
components/[dominio]/
└── pipes-[dominio]/
    ├── pipes-[dominio].module.ts
    ├── [dominio]-[descripcion]/
    │   ├── [dominio]-[descripcion].pipe.ts        # ✅ Cada pipe en SU PROPIA carpeta
    │   └── [dominio]-[descripcion].pipe.spec.ts   # ✅ Test correspondiente
    └── [otros pipes del dominio]/
        ├── [dominio]-[otra-descripcion]/
        │   ├── [dominio]-[otra-descripcion].pipe.ts
        │   └── [dominio]-[otra-descripcion].pipe.spec.ts
```

#### Módulo de Pipes

```typescript
// pipes-para-conteos/pipes-para-conteos.module.ts
import { NgModule } from '@angular/core';
import { ConteosEstadoPipe } from './conteos-estado/conteos-estado.pipe'; // ✅ Desde carpeta individual
import { ConteosBadgeEstadoPipe } from './conteos-badge-estado/conteos-badge-estado.pipe'; // ✅ Desde carpeta individual
import { ConteosFormatoFechaPipe } from './conteos-formato-fecha/conteos-formato-fecha.pipe'; // ✅ Desde carpeta individual

@NgModule({
	declarations: [
		ConteosEstadoPipe, // ✅ Nombres correctos
		ConteosBadgeEstadoPipe,
		ConteosFormatoFechaPipe,
		// Todos los pipes del dominio conteos
	],
	exports: [
		ConteosEstadoPipe, // ✅ Nombres correctos
		ConteosBadgeEstadoPipe,
		ConteosFormatoFechaPipe,
		// Exportar todos los pipes para que otros módulos los usen
	],
})
export class PipesParaConteosModule {}
```

## 3. Registro en el Sistema

### 3.1 Rutas (`pages.routes.ts`)

Agregar la ruta de la nueva vista con lazy loading:

```typescript
// En pages.routes.ts
import permisosKeysConfig from 'src/app/config/permisosKeys.config';

{
    path: 'almacen/conteos/supervision',
    canActivate: [VerificaTokenGuard, PermisosGuard],
    loadComponent: () => import('./components/conteos/vista-conteos-supervision/vista-conteos-supervision.component').then(m => m.VistaConteosSupervisionComponent),
    data: {
        titulo: 'Gestión de conteos (inventarios)',
        permissions: permisosKeysConfig['menu:almacen:supervisionConteos']
    }
}
```

### 3.2 Sistema de Permisos

#### Estructuras de Permisos CARRDUCI

Los permisos siguen una jerarquía estricta y convención de nomenclatura unificada para GUI y API:

##### Permisos de Menú (Vista/Acceso)

```
menu:[contexto-mas-amplio]
menu:[contexto-mas-amplio]:[sub-menu(dominio)]  // ⚠️ DEPRECIADO para nuevos permisos - Los permisos de "leer" del dominio otorgan acceso a sub-menús
```

-   `menu:compras` - Acceso al módulo compras (abarca múltiples dominios: proveedores, pedidos, etc.)
-   `menu:compras:proveedores` - ⚠️ DEPRECIADO para nuevos permisos: Usar `proveedor:leer` para acceso al sub-menú
-   `menu:administrador` - Acceso al módulo administrador (usuarios, áreas, etc.)

##### Permisos de Acciones/Consulta

```
[dominio]:[accion-crud]
[dominio]:acciones:[acciones-varias-de-negocio]
```

-   `almacen:conteos:leer` - Leer conteos
-   `cliente:crear` - Crear clientes
-   `usuario:modificar` - Modificar usuarios
-   `folio:acciones:aprobar` - Aprobar folios
-   `empleado:evento:amonestacion` - Registrar amonestación

##### Permisos Especiales

```
[entidad]:[accion]
parametros:[modulo]:[accion]
```

-   `login` - Permiso de login
-   `parametros:departamentoTransformacion` - Configurar departamento

#### Estructura General Unificada

Todos los permisos siguen patrones consistentes pero flexibles según el tipo:

```
[contexto]:[entidad]:[accion]:[subaccion-opcional]
```

**Ejemplos de aplicación:**

-   **Menús:** `menu:compras` (contexto + entidad)
-   **CRUD básico:** `proveedor:leer` (contexto + acción)
-   **Acciones específicas:** `proveedor:acciones:activar` (contexto + acción + subacción)
-   **Reportes:** `articulo:reportes:existencias` (contexto + acción + subacción)
-   **Eventos:** `empleado:evento:amonestacion` (contexto + acción + subacción)
-   **Parámetros:** `parametros:departamentoTransformacion` (contexto + entidad)
-   **Globales:** `login` (solo entidad/acción)

> **⚠️ NOTA IMPORTANTE:** Los 3 archivos de permisos (`permisosKeys.config.ts`, `permisos.config.ts`, `permisos.config.js`) deben contener exactamente la misma cantidad de permisos, ya que son copias entre sí con diferentes formatos de configuración. Si un permiso existe en uno, debe existir en los otros dos.

#### Archivo 1: `permisosKeys.config.ts`

```typescript
// En permisosKeys.config.ts
export const permisosKeysConfig = {
	// ... permisos existentes

	// Permiso de menú para vista específica
	'menu:compras': 'menu:compras',

	// Permisos de negocio unificados para GUI y API
	'proveedor:leer': 'proveedor:leer',
	'proveedor:crear': 'proveedor:crear',
	'proveedor:modificar': 'proveedor:modificar',
	'proveedor:eliminar': 'proveedor:eliminar',
};
```

#### Archivo 2: `permisos.config.ts`

Configurar permisos con valores NO_DEFINIDO:

```typescript
// En permisos.config.ts
export const permisosConfig = {
	// ... otros permisos

	// Permisos de menú
	'menu:compras': NO_DEFINIDO,

	// Permisos de negocio unificados para GUI y API
	'proveedor:leer': NO_DEFINIDO,
	'proveedor:crear': NO_DEFINIDO,
	'proveedor:modificar': NO_DEFINIDO,
	'proveedor:eliminar': NO_DEFINIDO,
};
```

#### Archivo API: `permisos.config.js`

Agregar permisos correspondientes en el backend:

```javascript
// En permisos.config.js
module.exports = {
	// ... permisos existentes

	// Permisos unificados para GUI y API
	'proveedor:leer': NO_DEFINIDO,
	'proveedor:crear': NO_DEFINIDO,
	'proveedor:modificar': NO_DEFINIDO,
	'proveedor:eliminar': NO_DEFINIDO,

	// Permisos más específicos si son necesarios
	'proveedor:acciones:activar': NO_DEFINIDO,
	'proveedor:acciones:suspender': NO_DEFINIDO,
};
```

#### Convenciones para Nuevos Permisos

1. **Estructura Unificada**: `[contexto]:[entidad]:[accion]:[subaccion-opcional]` para todos los permisos
2. **Contextos Principales**:
    - `[modulo]:` para permisos de negocio (ej: `proveedor:leer`)
    - `menu:[contexto-mas-amplio]:` para menús principales que abarcan múltiples dominios (ej: `menu:compras`)
    - `menu:[contexto-mas-amplio]:[sub-menu]:` ⚠️ DEPRECIADO - usar `[dominio]:leer` para sub-menús
    - `parametros:` para configuración (ej: `parametros:departamentoTransformacion`)
    - Sin contexto para globales (ej: `login`)
3. **Entidades**: Objetos del dominio (proveedores, usuarios, empleados, etc.)
4. **Acciones Principales**: `leer`, `crear`, `modificar`, `eliminar` ⚠️, `acciones`, `reportes`, `evento`
    - **Nota sobre "eliminar"**: Este permiso es poco común. Se prefiere `cancelar` o `desactivar` con cambios de estatus bajo permisos específicos para mantener integridad de datos y auditoría.
5. **Subacciones**: Para especificar operaciones detalladas (ej: `acciones:aprobar`, `reportes:existencias`)
6. **Consistencia Total**: GUI y API usan idéntica estructura de permisos
7. **Configuración de Archivos**:
    - `permisosKeys.config.ts`: valor = misma cadena que la llave
    - `permisos.config.ts`: valor = `NO_DEFINIDO`
    - `permisos.config.js`: valor = `NO_DEFINIDO`

### 3.3 Menú Lateral (`login.menus.js`)

#### Agregar Menú Principal

```javascript
function compras() {
	const menu = {
		permiso: permisos.$('menu:compras', false),
		titulo: 'Compras',
		icono: 'fas fa-shopping-cart',
		submenu: [
			{
				titulo: 'Proveedores',
				url: '/compras/proveedores',
				permiso: permisos.$('proveedor:leer', false),
			},
			{
				titulo: 'Pedidos',
				url: '/compras/pedidos',
				permiso: permisos.$('pedido:leer', false),
			},
			{
				titulo: 'Facturas',
				url: '/compras/facturas',
				permiso: permisos.$('factura:leer', false),
			},
		],
	};
	return menu;
}
```

<hr class="hr-secundario">

## 4. Desarrollo de la API

---

### 4.1 Estructura de Archivos

```

carrduci-sys-api/
├── routes/proveedores/
│ └── proveedores.route.js # Endpoints HTTP
├── controllers/proveedores/
│ └── proveedores.controller.js # Lógica de controladores
├── services/proveedores/
│ └── proveedores.service.js # Lógica de negocio
└── models/proveedores/
└── proveedores.model.js # Modelo de MongoDB

```

> **📋 NOTA IMPORTANTE - Cambio a futuro en la estructura del API**
>
> **Motivación**: Para mantener consistencia con la arquitectura de la GUI y facilitar el desarrollo, próximamente se reorganizará la estructura del API siguiendo el mismo patrón modular.
>
> **Nueva estructura propuesta**:
>
> ```
> carrduci-sys-api/
> ├── components/                    # 📁 Carpeta principal de módulos (similar a GUI)
> │   ├── compras/                   # 📁 Grupo de dominios relacionados
> │   │   ├── proveedores/           # 🔧 Dominio individual
> │   │   │   ├── proveedores.route.js       # Endpoints HTTP
> │   │   │   ├── proveedores.controller.js  # Lógica de controladores
> │   │   │   ├── proveedores.service.js     # Lógica de negocio
> │   │   │   └── proveedores.model.js       # Modelo de MongoDB
> │   │   └── pedidos/               # 🔧 Otro dominio en el grupo compras
> │   │       ├── pedidos.route.js
> │   │       ├── pedidos.controller.js
> │   │       ├── pedidos.service.js
> │   │       └── pedidos.model.js
> │   ├── ventas/                    # 📁 Otro grupo de dominios
> │   │   ├── clientes/
> │   │   └── productos/
> │   └── administracion/            # 📁 Grupo de administración
> │       ├── usuarios/
> │       └── permisos/
> ├── utiles/                        # 🛠️ Utilidades del sistema
> │   ├── response.utils.js
> │   ├── validation.utils.js
> │   └── crypto.utils.js
> ├── plugins/                       # 🔌 Plugins de Mongoose
> │   ├── historial.plugin.js
> │   └── busqueda-texto.plugin.js
> ├── middlewares/                   # 🎯 Middlewares personalizados
> │   ├── autenticacion.js
> │   └── autorizacion.js
> └── config/                        # ⚙️ Configuraciones
> ```
>
> **Principales cambios**:
>
> -   **Carpeta `components/`**: Centraliza todos los módulos de negocio, similar a la GUI
> -   **Agrupación por contexto**: Dominios relacionados se agrupan en carpetas (compras, ventas, administracion)
> -   **Archivos en raíz del dominio**: Cada dominio tiene sus 4 archivos principales directamente en la carpeta, sin subcarpetas separadas
> -   **Separación clara**: Utilidades, plugins y middlewares tienen sus propias carpetas dedicadas
>
> **Beneficios**:
>
> -   🔄 **Consistencia**: Arquitectura idéntica entre GUI y API
> -   🎯 **Navegación**: Más fácil encontrar componentes relacionados
> -   📦 **Mantenimiento**: Estructura más intuitiva para nuevos desarrolladores
> -   ⚡ **Desarrollo**: Menos carpetas anidadas, acceso directo a archivos
>
> **Esta reorganización se implementará de forma gradual para no afectar el funcionamiento actual del sistema.**

### 4.2 Modelo con Plugins Estándar

```javascript
// models/proveedores/proveedores.model.js
const mongoose = require('mongoose');
const { historialPlugin } = require('../../plugins/historial/historial.plugin');
const {
	textSearchPlugin,
} = require('../../plugins/busqueda-texto/busqueda-texto.plugin');

const proveedorSchema = new mongoose.Schema(
	{
		// Campos básicos del modelo
		nombre: {
			type: String,
			required: [true, 'El nombre es obligatorio'],
			trim: true,
		},
		contacto: {
			nombre: {
				type: String,
				required: [true, 'El nombre de contacto es obligatorio'],
			},
			email: {
				type: String,
				lowercase: true,
				trim: true,
			},
			telefono: {
				type: String,
				trim: true,
			},
		},
		direccion: {
			calle: String,
			numero: String,
			colonia: String,
			ciudad: String,
			estado: String,
			codigoPostal: String,
			pais: {
				type: String,
				default: 'México',
			},
		},
		tipoProveedor: {
			type: String,
			enum: [
				'materiaPrima',
				'servicios',
				'equipo',
				'consumibles',
				'otros',
			],
			default: 'otros',
		},
		estado: {
			type: String,
			enum: ['activo', 'inactivo', 'suspendido'],
			default: 'activo',
		},

		// Campo para búsqueda de texto
		busqueda: String,
	},
	{
		collection: 'proveedores',
		timestamps: true,
	}
);

// Índices para optimización
proveedorSchema.index({ nombre: 1 });
proveedorSchema.index({ 'contacto.email': 1 });
proveedorSchema.index({ tipoProveedor: 1, estado: 1 });
proveedorSchema.index({ estado: 1 });

// Aplicar plugins estándar
proveedorSchema.plugin(historialPlugin);
proveedorSchema.plugin(textSearchPlugin);

module.exports = mongoose.model('Proveedor', proveedorSchema);
```

### 4.3 Servicio con CRUD Unificado

```javascript
// services/proveedores/proveedores.service.js
const Proveedor = require('../../models/proveedores/proveedores.model');

class ProveedoresService {
	/**
	 * Función de búsqueda UNIFICADA
	 * Maneja: filtros, término, ID específico, paginación
	 * Reemplaza: buscarPorTérmino, buscar, buscarPorId
	 */
	static async buscar({
		filtros = {},
		termino = '',
		id = null,
		desde = 0,
		limite = 10,
		sort = -1,
		campo = 'createdAt',
	} = {}) {
		// ⚠️ IMPORTANTE: = {} permite llamar la función sin argumentos
		desde = Number(desde ?? 0);
		limite = Number(limite ?? 10);
		sort = Number(sort ?? -1);
		campo = String(campo ?? 'createdAt');
		filtros = filtros ?? {};
		termino = !!termino ? String(termino).replace(/\\/gm, '') : undefined;

		// Si se proporciona un ID específico, filtrar solo por ese ID
		if (id) {
			const proveedor = await Proveedor.findOne({ _id: id })
				.select('-busqueda -__v')
				.lean();

			return {
				resultado: proveedor ? [proveedor] : [],
				total: proveedor ? 1 : 0,
			};
		}

		let filtrosProcesar = {
			...filtros,
			terminoTextSearch: termino,
		};
		let queryFiltros = this.queryFiltrosProveedores(filtrosProcesar);
		let total = await Proveedor.countDocuments(queryFiltros);

		if (total === 0) {
			filtrosProcesar.terminoRegex = termino;
			delete filtrosProcesar.terminoTextSearch;
			queryFiltros = this.queryFiltrosProveedores(filtrosProcesar);
			total = await Proveedor.countDocuments(queryFiltros);
		}

		const ES_BUSQUEDA_TEXTO = !!queryFiltros.$text;
		const PROJECTION = ES_BUSQUEDA_TEXTO
			? { score: { $meta: 'textScore' } }
			: {};
		const CRITERIOS_SORT = ES_BUSQUEDA_TEXTO
			? { [campo]: sort, _id: sort, score: { $meta: 'textScore' } }
			: { [campo]: sort, _id: sort };

		const resultado = await Proveedor.find(queryFiltros, PROJECTION)
			.skip(desde)
			.limit(limite)
			.sort(CRITERIOS_SORT)
			.select('-busqueda -__v -score')
			.lean();

		return { resultado, total };
	}

	/**
	 * Crear nuevo proveedor
	 */
	static async crear(datos) {
		const nuevoProveedor = new Proveedor(datos);

		// Agregar metadata para historial
		nuevoProveedor.metadata = {
			idUsuario: datos.usuario,
			descripcion: 'Proveedor creado',
		};

		return await nuevoProveedor.save();
	}

	/**
	 * Actualizar proveedor
	 * ⚠️ IMPORTANTE: Eliminar campos que se modifican en métodos específicos del negocio
	 * (ej: campos de estatus, campos calculados, etc.)
	 */
	static async actualizar(id, datos) {
		// Destructuring para excluir campos que se manejan en métodos específicos:
		// - { estado, ...datosLimpios } extrae 'estado' del objeto 'datos'
		// - ...datosLimpios crea nuevo objeto con TODAS las demás propiedades
		// - Resultado: 'estado' queda excluido del objeto que se actualiza
		const { estado, ...datosLimpios } = datos; // Ejemplo: estado se modifica en métodos específicos

		return await Proveedor.findOneAndUpdate({ _id: id }, datosLimpios, {
			new: true,
			runValidators: true,
			context: 'query',
			metadata: {
				idUsuario: datos.usuario,
				descripcion: 'Proveedor actualizado',
			},
		});
	}

	// Función helper para filtros (se pueden agregar más según necesidades del negocio)
	// Ejemplos comunes de filtros en CARRDUCI:
	// - Filtros exactos: folio, usuario, activo, etc.
	// - Filtros booleanos: prioridad, estado, etc.
	// - Filtros de fecha: updatedAt >= fecha, createdAt <= fecha
	// - Filtros de subdocumentos: 'estatus.aprobado', 'contacto.email'
	// - Filtros de existencia: campo: { $exists: true/false }
	static queryFiltrosProveedores({ terminoTextSearch, terminoRegex }) {
		let filtros = {};
		if (!!terminoTextSearch) {
			filtros.$text = {
				$search: `${terminoTextSearch} "${terminoTextSearch}"`,
			};
		}
		if (!!terminoRegex) {
			filtros.busqueda = { $regex: terminoRegex, $options: 'i' };
		}

		// Ejemplos de filtros adicionales que se pueden agregar:
		// if (filtros.activo !== undefined) filtros.activo = filtros.activo;
		// if (filtros.fecha) filtros.updatedAt = { $gte: filtros.fecha };
		// if (filtros.estado) filtros['estatus.estado'] = filtros.estado;
		// if (filtros.existeContacto) filtros.contacto = { $exists: true };

		return filtros;
	}

	// Otros métodos específicos del negocio...
}
```

### 4.4 Controlador

```javascript
// controllers/proveedores/proveedores.controller.js
const { response } = require('../../utils/response.utils');
const ProveedoresService = require('../../services/proveedores/proveedores.service');

class ProveedoresController {
	/**
	 * Obtener proveedores con filtros y paginación
	 */
	static async obtener(req, res) {
		try {
			const { filtros, termino, desde, limite, sort, campo } = req.query;

			// ⚠️ IMPORTANTE: Crear nueva instancia para evitar race conditions
			// En entornos concurrentes, métodos estáticos comparten estado entre requests
			// Crear instancias asegura aislamiento entre peticiones concurrentes
			const { resultado, total } = await new ProveedoresService().buscar({
				filtros: filtros ? JSON.parse(filtros) : {},
				termino,
				desde: parseInt(desde) || 0,
				limite: parseInt(limite) || 10,
				sort: parseInt(sort) || -1,
				campo: campo || 'createdAt',
			});

			// Crear instancia de respuesta y enviar
			const resp = new response(res, __filename, {
				mensaje: 'Proveedores obtenidos exitosamente',
				datos: {
					proveedores: resultado,
					total,
				},
			});
			return resp._200_ok();
		} catch (error) {
			// Crear instancia de respuesta de error
			const resp = new response(res, __filename, {
				mensaje: 'Error al obtener proveedores',
				error: error,
			});
			return resp._500_internal_server_error();
		}
	}

	/**
	 * Crear nuevo proveedor
	 */
	static async crearProveedor(req, res) {
		try {
			const resultado = await new ProveedoresService().crear({
				...req.body,
				usuario: req.user._id,
			});

			const resp = new response(res, __filename, {
				mensaje: 'Proveedor creado exitosamente',
				datos: resultado,
			});
			return resp._201_created();
		} catch (error) {
			const resp = new response(res, __filename, {
				mensaje: 'Error al crear proveedor',
				error: error,
			});
			return resp._500_internal_server_error();
		}
	}

	/**
	 * Actualizar proveedor
	 */
	static async actualizarProveedor(req, res) {
		try {
			const { id } = req.params;
			const resultado = await new ProveedoresService().actualizar(id, {
				...req.body,
				usuario: req.user._id,
			});

			const resp = new response(res, __filename, {
				mensaje: 'Proveedor actualizado exitosamente',
				datos: resultado,
			});
			return resp._200_ok();
		} catch (error) {
			const resp = new response(res, __filename, {
				mensaje: 'Error al actualizar proveedor',
				error: error,
			});
			return resp._500_internal_server_error();
		}
	}

	/**
	 * Obtener proveedor específico por ID
	 */
	static async obtenerPorId(req, res) {
		try {
			const { id } = req.params;
			const { resultado } = await new ProveedoresService().buscar({ id });

			if (!resultado[0]) {
				const resp = new response(res, __filename, {
					mensaje: 'Proveedor no encontrado',
					error: new Error('Proveedor no encontrado'),
				});
				return resp._404_not_found();
			}

			const resp = new response(res, __filename, {
				mensaje: 'Proveedor encontrado',
				datos: resultado[0],
			});
			return resp._200_ok();
		} catch (error) {
			const resp = new response(res, __filename, {
				mensaje: 'Error al obtener proveedor',
				error: error,
			});
			return resp._500_internal_server_error();
		}
	}

	// Otros métodos del controlador...
}
```

### 4.5 Rutas

```javascript
// routes/proveedores/proveedores.route.js
const express = require('express');
const router = express.Router();
const ProveedoresController = require('../../controllers/proveedores/proveedores.controller');
const permisos = require('../../config/permisos.config');

// Crear nuevo proveedor
router.post(
	'/',
	permisos.$('proveedores:crear'),
	new ProveedoresController().crearProveedor
);

// Obtener proveedores con filtros y paginación
router.get(
	'/',
	permisos.$('proveedores:leer'),
	new ProveedoresController().obtener
);

// Obtener proveedor específico por ID
router.get(
	'/id/:id',
	permisos.$('proveedores:leer'),
	new ProveedoresController().obtenerPorId
);

// Actualizar proveedor
router.put(
	'/id/:id',
	permisos.$('proveedores:actualizar'),
	new ProveedoresController().actualizarProveedor
);

// Otros endpoints específicos...

module.exports = router;
```

## 5. Documentación Estándar

La documentacion en CARRDUCI sigue reglas estrictas definidas en el archivo [`4-estructuras-de-documentacion.md`](./4-estructuras-de-documentacion.md). Todos los archivos deben estar completamente documentados siguiendo estos estandares.

### 5.1 Reglas Generales de Documentación

#### ✅ **Comentarios JSDoc Obligatorios:**

-   **Funciones y metodos**: Siempre usar `@param`, `@returns`, `@throws`
-   **Clases**: Documentar con `@class` y descripcion completa
-   **Propiedades**: Usar `@type` y descripcion

#### ✅ **Separadores de Sección:**

-   **Archivos grandes**: Usar separadores de seccion con `#region`
-   **Funciones complejas**: Usar sub-separadores dentro de funciones

#### ✅ **Estructura de Archivos:**

-   **Comentarios arriba** de lineas, nunca al lado
-   **Sin acentos** ni caracteres especiales en comentarios de codigo
-   **Espacios** antes y despues de bloques comentados

### 5.2 Documentación por Tipo de Archivo

#### 5.2.1 Modelos de API (`models/*.model.js`)

**Estructura obligatoria:**

```javascript
// (o==================================================================o)
//   #region IMPORTACIONES
// (o-----------------------------------------------------------\/-----o)

/* IMPORTACIONES EXTERNAS */
const mongoose = require('mongoose');

/* OTROS MODELOS */
/* SERVICIOS */
/* UTILIDADES */

// (o-----------------------------------------------------------/\-----o)
//   #endregion IMPORTACIONES
// (o==================================================================o)

// (o==================================================================o)
//   #region ESQUEMA
// (o-----------------------------------------------------------\/-----o)

/** -----------------------------------------------------
  - NOMBRE: `Nombre del Esquema`
  - Fecha documentacion: 01, October 2025
  - Archivo: models/ejemplo.model.js

  - Descripcion:
  Descripcion completa del esquema y su proposito
  en el sistema CARRDUCI.
----------------------------------------------------- */

const ejemploSchema = new mongoose.Schema(
	{
		// Documentar cada campo con JSDoc
		/** @type {String} Nombre del elemento */
		nombre: {
			type: String,
			required: true,
			trim: true,
		},

		/** @type {Boolean} Estado activo/inactivo */
		activo: {
			type: Boolean,
			default: true,
		},
	},
	{
		timestamps: true,
		collection: 'ejemplos',
	}
);

// (o-----------------------------------------------------------/\-----o)
//   #endregion ESQUEMA
// (o==================================================================o)

// (o==================================================================o)
//   #region PLUGINS Y METODOS
// (o-----------------------------------------------------------\/-----o)

// Aplicar plugins con comentarios
ejemploSchema.plugin(historialPlugin); // Plugin de historial de cambios
ejemploSchema.plugin(textSearchPlugin); // Plugin de busqueda de texto

// Indices con documentacion
ejemploSchema.index({ nombre: 1 }); // Indice para busqueda por nombre
ejemploSchema.index({ activo: 1 }); // Indice para filtrado por estado

// (o-----------------------------------------------------------/\-----o)
//   #endregion PLUGINS Y METODOS
// (o==================================================================o)

// (o==================================================================o)
//   #region EXPORTACIONES
// (o-----------------------------------------------------------\/-----o)

// Crear instancia del modelo (OBLIGATORIO en este nivel)
const EJEMPLO_MODEL = mongoose.model('Ejemplo', ejemploSchema);

module.exports = EJEMPLO_MODEL;

// (o-----------------------------------------------------------/\-----o)
//   #endregion EXPORTACIONES
// (o==================================================================o)
```

#### 5.2.2 Servicios de API (`services/**/*.service.js`)

**Estructura obligatoria:**

```javascript
// (o==================================================================o)
//   #region IMPORTACIONES
// (o-----------------------------------------------------------\/-----o)

const EJEMPLO_MODEL = require('../models/ejemplo.model');

/* IMPORTACIONES EXTERNAS */
/* OTROS MODELOS */
/* UTILIDADES */

// (o-----------------------------------------------------------/\-----o)
//   #endregion IMPORTACIONES
// (o==================================================================o)

class EjemploService {
	/**
	 * Función de búsqueda unificada
	 * @param {Object} params - Parametros de busqueda
	 * @param {Object} params.filtros - Filtros adicionales
	 * @param {string} params.termino - Termino de busqueda
	 * @param {string} params.id - ID especifico para buscar
	 * @param {number} params.desde - Indice desde donde buscar
	 * @param {number} params.limite - Limite de resultados
	 * @param {number} params.sort - Orden de resultados
	 * @param {string} params.campo - Campo por el cual ordenar
	 * @returns {Promise<{resultado: Array, total: number}>}
	 */
	buscar({
		filtros = {},
		termino = '',
		id = null,
		desde = 0,
		limite = 10,
		sort = -1,
		campo = 'createdAt',
	} = {}) {
		desde = Number(desde ?? 0);
		limite = Number(limite ?? 10);
		sort = Number(sort ?? -1);
		campo = String(campo ?? 'createdAt');
		filtros = filtros ?? {};
		termino = !!termino ? String(termino).replace(/\\/gm, '') : undefined;

		// Si se proporciona un ID específico, filtrar solo por ese ID
		if (id) {
			const elemento = EJEMPLO_MODEL.findOne({ _id: id })
				.select('-busqueda -__v')
				.lean();

			return {
				resultado: elemento ? [elemento] : [],
				total: elemento ? 1 : 0,
			};
		}

		let filtrosProcesar = {
			...filtros,
			terminoTextSearch: termino,
		};
		let queryFiltros = this.queryFiltrosEjemplo(filtrosProcesar);
		let total = EJEMPLO_MODEL.countDocuments(queryFiltros);

		if (total === 0) {
			filtrosProcesar.terminoRegex = termino;
			delete filtrosProcesar.terminoTextSearch;
			queryFiltros = this.queryFiltrosEjemplo(filtrosProcesar);
			total = EJEMPLO_MODEL.countDocuments(queryFiltros);
		}

		const ES_BUSQUEDA_TEXTO = !!queryFiltros.$text;
		const PROJECTION = ES_BUSQUEDA_TEXTO
			? { score: { $meta: 'textScore' } }
			: {};
		const CRITERIOS_SORT = ES_BUSQUEDA_TEXTO
			? { [campo]: sort, _id: sort, score: { $meta: 'textScore' } }
			: { [campo]: sort, _id: sort };

		const resultado = EJEMPLO_MODEL.find(queryFiltros, PROJECTION)
			.skip(desde)
			.limit(limite)
			.sort(CRITERIOS_SORT)
			.select('-busqueda -__v -score')
			.lean();

		return { resultado, total };
	}

	/**
	 * Crear nuevo elemento
	 * @param {Object} datos - Datos del elemento a crear
	 * @returns {Promise<Object>} Elemento creado
	 */
	async crear(datos) {
		const nuevoElemento = new EJEMPLO_MODEL(datos);

		// Agregar metadata para historial
		nuevoElemento.metadata = {
			idUsuario: datos.usuario,
			descripcion: 'Elemento creado',
		};

		return await nuevoElemento.save();
	}

	/**
	 * Actualizar elemento
	 * @param {string} id - ID del elemento
	 * @param {Object} datos - Datos actualizados
	 * @returns {Promise<Object>} Elemento actualizado
	 */
	async actualizar(id, datos) {
		// Destructuring para excluir campos que se manejan en métodos específicos
		const { estado, ...datosLimpios } = datos; // Ejemplo: estado se modifica en métodos específicos

		return await EJEMPLO_MODEL.findOneAndUpdate({ _id: id }, datosLimpios, {
			new: true,
			runValidators: true,
			context: 'query',
			metadata: {
				idUsuario: datos.usuario,
				descripcion: 'Elemento actualizado',
			},
		});
	}

	// Función helper para filtros
	queryFiltrosEjemplo({ terminoTextSearch, terminoRegex }) {
		let filtros = {};
		if (!!terminoTextSearch) {
			filtros.$text = {
				$search: `${terminoTextSearch} "${terminoTextSearch}"`,
			};
		}
		if (!!terminoRegex) {
			filtros.busqueda = { $regex: terminoRegex, $options: 'i' };
		}

		// Ejemplos de filtros adicionales que se pueden agregar:
		// if (filtros.activo !== undefined) filtros.activo = filtros.activo;
		// if (filtros.fecha) filtros.updatedAt = { $gte: filtros.fecha };
		// if (filtros.estado) filtros['estatus.estado'] = filtros.estado;
		// if (filtros.existeContacto) filtros.contacto = { $exists: true };

		return filtros;
	}
}

module.exports = EjemploService;
```

#### 5.2.3 Controladores de API (`controllers/**/*.controller.js`)

**Estructura obligatoria:**

```javascript
// (o==================================================================o)
//   #region IMPORTACIONES
// (o-----------------------------------------------------------\/-----o)

const { response } = require('../../utils/response.utils');
const EJEMPLO_SERVICE = require('../services/ejemplo.service');

/* IMPORTACIONES EXTERNAS */
/* UTILIDADES */

// (o-----------------------------------------------------------/\-----o)
//   #endregion IMPORTACIONES
// (o==================================================================o)

class EjemploController {
    /**
     * Obtener elementos con filtros y paginacion
     * @param {Object} req - Request object
     * @param {Object} res - Response object
     */
    static async obtener(req, res) {
        try {
            // Implementacion con manejo de errores
            const { resultado, total } = await new EJEMPLO_SERVICE().buscar({...});

            const resp = new response(res, __filename, {
                mensaje: 'Elementos obtenidos exitosamente',
                datos: { elementos: resultado, total }
            });
            return resp._200_ok();
        } catch (error) {
            const resp = new response(res, __filename, {
                mensaje: 'Error al obtener elementos',
                error: error
            });
            return resp._500_internal_server_error();
        }
    }

    // Otros metodos documentados...
}

module.exports = EjemploController;
```

#### 5.2.4 Rutas de API (`routes/**/*.route.js`)

**Estructura obligatoria:**

```javascript
// (o==================================================================o)
//   #region IMPORTACIONES
// (o-----------------------------------------------------------\/-----o)

const express = require('express');
const EJEMPLO_CONTROLLER = require('../controllers/ejemplo.controller');
const permisos = require('../config/permisos.config');

/* MIDDLEWARES */
/* UTILIDADES */

// (o-----------------------------------------------------------/\-----o)
//   #endregion IMPORTACIONES
// (o==================================================================o)

const router = express.Router();

// (o==================================================================o)
//   #region ENDPOINTS CRUD
// (o-----------------------------------------------------------\/-----o)

// Crear elemento
router.post(
	'/',
	permisos.$('ejemplo:crear'),
	new EJEMPLO_CONTROLLER().crearElemento
);

// Obtener elementos
router.get('/', permisos.$('ejemplo:leer'), new EJEMPLO_CONTROLLER().obtener);

// Obtener elemento especifico
router.get(
	'/:id',
	permisos.$('ejemplo:leer'),
	new EJEMPLO_CONTROLLER().obtenerPorId
);

// Actualizar elemento
router.put(
	'/:id',
	permisos.$('ejemplo:actualizar'),
	new EJEMPLO_CONTROLLER().actualizarElemento
);

// (o-----------------------------------------------------------/\-----o)
//   #endregion ENDPOINTS CRUD
// (o==================================================================o)

module.exports = router;
```

#### 5.2.5 Componentes de GUI - TypeScript (`components/**/*.component.ts`)

**Estructura obligatoria:**

```typescript
// (o==================================================================o)
//   #region IMPORTACIONES
// (o-----------------------------------------------------------\/-----o)

import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';

/* SERVICIOS */
/* MODELOS */
/* UTILIDADES */

// (o-----------------------------------------------------------/\-----o)
//   #endregion IMPORTACIONES
// (o==================================================================o)

/**
 * Componente de administracion de ejemplos
 * Gestiona el CRUD completo de elementos de ejemplo
 */
@Component({
	selector: 'app-vista-administracion-ejemplos',
	templateUrl: './vista-administracion-ejemplos.component.html',
	styleUrls: ['./vista-administracion-ejemplos.component.css'],
})
export class VistaAdministracionEjemplosComponent implements OnInit {
	// (o==================================================================o)
	//   #region PROPIEDADES
	// (o-----------------------------------------------------------\/-----o)

	/** Formulario reactivo para creacion/edicion */
	formulario: FormGroup;

	/** Listado de elementos */
	elementos: any[] = [];

	/** Estado de carga */
	cargando = false;

	// (o-----------------------------------------------------------/\-----o)
	//   #endregion PROPIEDADES
	// (o==================================================================o)

	/**
	 * Constructor del componente
	 * @param fb FormBuilder para crear formularios reactivos
	 * @param route ActivatedRoute para obtener parametros de ruta
	 */
	constructor(private fb: FormBuilder, private route: ActivatedRoute) {
		this.crearFormulario();
	}

	// (o==================================================================o)
	//   #region CICLO DE VIDA
	// (o-----------------------------------------------------------\/-----o)

	/**
	 * Inicializacion del componente
	 */
	ngOnInit(): void {
		this.cargarElementos();
	}

	// (o-----------------------------------------------------------/\-----o)
	//   #endregion CICLO DE VIDA
	// (o==================================================================o)

	// (o==================================================================o)
	//   #region METODOS PUBLICOS
	// (o-----------------------------------------------------------\/-----o)

	/**
	 * Carga la lista de elementos desde el API
	 */
	cargarElementos(): void {
		this.cargando = true;
		// Implementacion
		this.cargando = false;
	}

	// (o-----------------------------------------------------------/\-----o)
	//   #endregion METODOS PUBLICOS
	// (o==================================================================o)

	// (o==================================================================o)
	//   #region METODOS PRIVADOS
	// (o-----------------------------------------------------------\/-----o)

	/**
	 * Crea el formulario reactivo con validaciones
	 */
	private crearFormulario(): void {
		this.formulario = this.fb.group({
			nombre: [''],
			descripcion: [''],
		});
	}

	// (o-----------------------------------------------------------/\-----o)
	//   #endregion METODOS PRIVADOS
	// (o==================================================================o)
}
```

_*Archivos HTML relacionados (`components/**/\*.component.html`):*_

```html
<!--================================================================o)
  #region ESTRUCTURA PRINCIPAL (INICIO)
(o-----------------------------------------------------------\/------>

<div [ngSwitch]="enMovil">
	<div *ngSwitchCase="false">
		<div [ngClass]="{ row: !enMovil }">
			<div [ngClass]="{ 'col-12': !enMovil }">
				<div [ngClass]="{ card: !enMovil }">
					<div [ngClass]="{ 'card-body': !enMovil }">
						<!-- Contenido principal aquí -->
					</div>
				</div>
			</div>
		</div>
	</div>
	<div *ngSwitchCase="true">
		<!-- Contenido para móvil aquí -->
	</div>
</div>

<!-----------------------------------------------------------/\-----o)
  #endregion ESTRUCTURA PRINCIPAL (FIN)
(o=================================================================-->

<!--================================================================o)
  #region TEMPLATES ESTRUCTURA PRINCIPAL (INICIO)
(o-----------------------------------------------------------\/------>

<ng-template #botonesPrincipales>
	<div class="dis-flex">
		<button class="btn btn-success mr-1 mb-1" (click)="crearElemento()">
			<i class="fas fa-plus mr-1"></i>
			Crear
		</button>
	</div>
</ng-template>

<!-----------------------------------------------------------/\-----o)
  #endregion TEMPLATES ESTRUCTURA PRINCIPAL (FIN)
(o=================================================================-->

<!--================================================================o)
  #region TEMPLATES FLOTANTES Y MODALES (INICIO)
(o-----------------------------------------------------------\/------>

<ng-template #formularioCreacion>
	<app-formulario-creacion
		(formularioValido)="procesarCreacion($event)"
		(cancelado)="cerrarModal()"
	></app-formulario-creacion>
</ng-template>

<!-----------------------------------------------------------/\-----o)
  #endregion TEMPLATES FLOTANTES Y MODALES (FIN)
(o=================================================================-->
```

#### 5.2.7 Guards de Angular (`guards/**/*.guard.ts`)

**Estructura obligatoria:**

```typescript
// (o==================================================================o)
//   #region IMPORTACIONES
// (o-----------------------------------------------------------\/-----o)

import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

/* SERVICIOS */
/* UTILIDADES */

// (o-----------------------------------------------------------/\-----o)
//   #endregion IMPORTACIONES
// (o==================================================================o)

/**
 * Guard para verificar permisos de acceso
 * Protege rutas que requieren permisos especificos
 */
@Injectable({
	providedIn: 'root',
})
export class PermisosGuard implements CanActivate {
	/**
	 * Constructor del guard
	 * @param router Router de Angular para navegacion
	 */
	constructor(private router: Router) {}

	/**
	 * Verifica si el usuario puede acceder a la ruta
	 * @param route Ruta que se intenta acceder
	 * @param state Estado del router
	 * @returns true si tiene acceso, false si no
	 */
	canActivate(route: any, state: any): boolean {
		// Implementacion de verificacion de permisos
		return true; // o false con redireccion
	}
}
```

#### 5.2.8 Archivos CSS/SCSS del componente (`components/**/*.component.css`)

**Estructura obligatoria con separadores de sección:**

```css
/*================================================================o)
  #region VARIABLES Y CONSTANTES (INICIO)
(o-----------------------------------------------------------\/------*/

/* Variables de colores */
:root {
	--color-primario: #007bff;
	--color-secundario: #6c757d;
	--color-exito: #28a745;
	--color-peligro: #dc3545;
	--color-advertencia: #ffc107;
	--color-info: #17a2b8;
}

/* Variables del componente */
.vista-administracion-ejemplos {
	--altura-header: 60px;
	--ancho-sidebar: 250px;
	--espacio-elementos: 1rem;
}

/*<!-----------------------------------------------------------/\-----o)
  #endregion VARIABLES Y CONSTANTES (FIN)
(o=================================================================*/

/*================================================================o)
  #region ESTILOS GENERALES (INICIO)
(o-----------------------------------------------------------\/------*/

/* Contenedor principal */
.vista-administracion-ejemplos {
	padding: var(--espacio-elementos);
	background-color: #f8f9fa;
	min-height: 100vh;
}

/*<!-----------------------------------------------------------/\-----o)
  #endregion ESTILOS GENERALES (FIN)
(o=================================================================*/

/*================================================================o)
  #region CABECERA (INICIO)
(o-----------------------------------------------------------\/------*/

/* Estilos para la cabecera */
.titulo-principal {
	font-size: 2rem;
	font-weight: 600;
	color: #495057;
	margin-bottom: var(--espacio-elementos);
}

/* Barra de herramientas */
.toolbar {
	display: flex;
	gap: var(--espacio-elementos);
	margin-bottom: var(--espacio-elementos);
	flex-wrap: wrap;
}

/*<!-----------------------------------------------------------/\-----o)
  #endregion CABECERA (FIN)
(o=================================================================*/

/*================================================================o)
  #region FILTROS (INICIO)
(o-----------------------------------------------------------\/------*/

/* Panel de filtros */
.filtros-panel {
	background: white;
	padding: var(--espacio-elementos);
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	margin-bottom: var(--espacio-elementos);
}

/* Grupo de filtros */
.filtro-grupo {
	display: flex;
	flex-direction: column;
	margin-bottom: var(--espacio-elementos);
}

.filtro-grupo:last-child {
	margin-bottom: 0;
}

.filtro-grupo label {
	font-weight: 500;
	margin-bottom: 0.5rem;
	color: #495057;
}

.filtro-grupo input,
.filtro-grupo select {
	padding: 0.5rem;
	border: 1px solid #ced4da;
	border-radius: 4px;
	font-size: 1rem;
	transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.filtro-grupo input:focus,
.filtro-grupo select:focus {
	outline: 0;
	border-color: var(--color-primario);
	box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

/*<!-----------------------------------------------------------/\-----o)
  #endregion FILTROS (FIN)
(o=================================================================*/

/*================================================================o)
  #region TABLA (INICIO)
(o-----------------------------------------------------------\/------*/

/* Contenedor de tabla */
.tabla-contenedor {
	background: white;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	overflow-x: auto;
	margin-bottom: var(--espacio-elementos);
}

/* Tabla */
.tabla-elementos {
	width: 100%;
	border-collapse: collapse;
	font-size: 0.9rem;
}

.tabla-elementos th,
.tabla-elementos td {
	padding: 0.75rem;
	text-align: left;
	border-bottom: 1px solid #dee2e6;
}

.tabla-elementos th {
	background-color: #f8f9fa;
	font-weight: 600;
	color: #495057;
	white-space: nowrap;
}

.tabla-elementos tbody tr:hover {
	background-color: #f8f9fa;
}

/*<!-----------------------------------------------------------/\-----o)
  #endregion TABLA (FIN)
(o=================================================================*/

/*================================================================o)
  #region PAGINACIÓN (INICIO)
(o-----------------------------------------------------------\/------*/

/* Contenedor de paginación */
.paginacion {
	display: flex;
	justify-content: center;
	align-items: center;
	gap: 0.5rem;
	margin-top: var(--espacio-elementos);
}

/* Botones de paginación */
.btn-pagina {
	padding: 0.5rem 1rem;
	border: 1px solid #ced4da;
	background: white;
	color: var(--color-primario);
	border-radius: 4px;
	cursor: pointer;
	transition: all 0.15s ease-in-out;
}

.btn-pagina:hover:not(:disabled) {
	background-color: var(--color-primario);
	color: white;
	border-color: var(--color-primario);
}

.btn-pagina:disabled {
	opacity: 0.5;
	cursor: not-allowed;
}

/* Información de página */
.pagina-info {
	margin: 0 1rem;
	font-weight: 500;
	color: #495057;
}

/*<!-----------------------------------------------------------/\-----o)
  #endregion PAGINACIÓN (FIN)
(o=================================================================*/

/*================================================================o)
  #region MODALES (INICIO)
(o-----------------------------------------------------------\/------*/

/* Modal */
.modal {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.5);
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 1050;
}

/* Contenido del modal */
.modal-contenido {
	background: white;
	border-radius: 8px;
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	max-width: 90vw;
	max-height: 90vh;
	overflow-y: auto;
	width: 500px;
}

/* Header del modal */
.modal-header {
	padding: var(--espacio-elementos);
	border-bottom: 1px solid #dee2e6;
	display: flex;
	justify-content: space-between;
	align-items: center;
}

.modal-header h3 {
	margin: 0;
	font-size: 1.25rem;
	font-weight: 600;
	color: #495057;
}

/* Botón cerrar */
.btn-cerrar {
	background: none;
	border: none;
	font-size: 1.5rem;
	cursor: pointer;
	color: #6c757d;
	padding: 0;
	line-height: 1;
}

.btn-cerrar:hover {
	color: #495057;
}

/* Formulario del modal */
.modal-form {
	padding: var(--espacio-elementos);
}

.form-grupo {
	margin-bottom: var(--espacio-elementos);
}

.form-grupo:last-child {
	margin-bottom: 0;
}

.form-grupo label {
	display: block;
	font-weight: 500;
	margin-bottom: 0.5rem;
	color: #495057;
}

.form-grupo input,
.form-grupo textarea {
	width: 100%;
	padding: 0.5rem;
	border: 1px solid #ced4da;
	border-radius: 4px;
	font-size: 1rem;
	box-sizing: border-box;
}

.form-grupo input:focus,
.form-grupo textarea:focus {
	outline: 0;
	border-color: var(--color-primario);
	box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

/* Footer del modal */
.modal-footer {
	padding: var(--espacio-elementos);
	border-top: 1px solid #dee2e6;
	display: flex;
	justify-content: flex-end;
	gap: 0.5rem;
}

/*<!-----------------------------------------------------------/\-----o)
  #endregion MODALES (FIN)
(o=================================================================*/

/*================================================================o)
  #region ESTADOS DE CARGA (INICIO)
(o-----------------------------------------------------------\/------*/

/* Overlay de carga */
.loading-overlay {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(255, 255, 255, 0.8);
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 1060;
}

/* Spinner */
.spinner {
	text-align: center;
}

.spinner i {
	font-size: 2rem;
	color: var(--color-primario);
	margin-bottom: 0.5rem;
}

/* Mensaje sin datos */
.no-datos {
	text-align: center;
	padding: 2rem;
	color: #6c757d;
}

.no-datos i {
	font-size: 3rem;
	margin-bottom: 1rem;
	display: block;
}

/*<!-----------------------------------------------------------/\-----o)
  #endregion ESTADOS DE CARGA (FIN)
(o=================================================================*/

/*================================================================o)
  #region RESPONSIVE (INICIO)
(o-----------------------------------------------------------\/------*/

/* Mobile */
@media (max-width: 768px) {
	.vista-administracion-ejemplos {
		padding: 0.5rem;
	}

	.titulo-principal {
		font-size: 1.5rem;
	}

	.toolbar {
		flex-direction: column;
		align-items: stretch;
	}

	.toolbar button {
		width: 100%;
		margin-bottom: 0.5rem;
	}

	.filtros-panel {
		padding: 0.5rem;
	}

	.tabla-contenedor {
		font-size: 0.8rem;
	}

	.tabla-elementos th,
	.tabla-elementos td {
		padding: 0.5rem;
	}

	.modal-contenido {
		width: 95vw;
		margin: 1rem;
	}

	.paginacion {
		flex-direction: column;
		gap: 0.25rem;
	}

	.pagina-info {
		margin: 0.5rem 0;
	}
}

/*<!-----------------------------------------------------------/\-----o)
  #endregion RESPONSIVE (FIN)
(o=================================================================*/
```

#### 5.2.9 Archivos de pruebas unitarias (`components/**/*.component.spec.ts`)

**Estructura obligatoria con separadores de sección:**

```typescript
// (o==================================================================o)
//   #region IMPORTACIONES
// (o-----------------------------------------------------------\/-----o)

import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { VistaAdministracionEjemplosComponent } from './vista-administracion-ejemplos.component';
import { EjemploService } from '../../services/ejemplo.service';

// (o-----------------------------------------------------------/\-----o)
//   #endregion IMPORTACIONES
// (o==================================================================o)

describe('VistaAdministracionEjemplosComponent', () => {
	// (o==================================================================o)
	//   #region CONFIGURACIÓN DE PRUEBAS
	// (o-----------------------------------------------------------\/-----o)

	let component: VistaAdministracionEjemplosComponent;
	let fixture: ComponentFixture<VistaAdministracionEjemplosComponent>;
	let ejemploService: EjemploService;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			declarations: [VistaAdministracionEjemplosComponent],
			imports: [
				HttpClientTestingModule,
				RouterTestingModule,
				FormsModule,
				ReactiveFormsModule,
			],
			providers: [EjemploService],
		}).compileComponents();

		fixture = TestBed.createComponent(VistaAdministracionEjemplosComponent);
		component = fixture.componentInstance;
		ejemploService = TestBed.inject(EjemploService);
		fixture.detectChanges();
	});

	// (o-----------------------------------------------------------/\-----o)
	//   #endregion CONFIGURACIÓN DE PRUEBAS
	// (o==================================================================o)

	// (o==================================================================o)
	//   #region PRUEBAS UNITARIAS
	// (o-----------------------------------------------------------\/-----o)

	it('debería crear el componente', () => {
		expect(component).toBeTruthy();
	});

	it('debería inicializar propiedades correctamente', () => {
		expect(component.elementos).toEqual([]);
		expect(component.cargando).toBeFalse();
	});

	it('debería crear el formulario correctamente', () => {
		component.ngOnInit();
		expect(component.formulario).toBeDefined();
		expect(component.formulario.get('nombre')).toBeDefined();
		expect(component.formulario.get('descripcion')).toBeDefined();
	});

	it('debería cargar elementos al inicializar', () => {
		spyOn(component, 'cargarElementos');
		component.ngOnInit();
		expect(component.cargarElementos).toHaveBeenCalled();
	});

	it('debería validar el formulario correctamente', () => {
		component.ngOnInit();
		component.formulario.get('nombre')?.setValue('');
		expect(component.formulario.valid).toBeFalse();

		component.formulario.get('nombre')?.setValue('Nombre válido');
		expect(component.formulario.valid).toBeTrue();
	});

	// (o-----------------------------------------------------------/\-----o)
	//   #endregion PRUEBAS UNITARIAS
	// (o==================================================================o)

	// (o==================================================================o)
	//   #region PRUEBAS DE INTEGRACIÓN
	// (o-----------------------------------------------------------\/-----o)

	it('debería llamar al servicio al cargar elementos', () => {
		const spy = spyOn(ejemploService, 'obtenerElementos').and.returnValue(
			of([])
		);
		component.cargarElementos();
		expect(spy).toHaveBeenCalled();
	});

	it('debería manejar errores del servicio correctamente', () => {
		const errorResponse = new HttpErrorResponse({
			error: 'Error del servidor',
			status: 500,
		});

		spyOn(ejemploService, 'obtenerElementos').and.returnValue(
			throwError(errorResponse)
		);
		spyOn(console, 'error');

		component.cargarElementos();

		expect(console.error).toHaveBeenCalled();
		expect(component.cargando).toBeFalse();
	});

	// (o-----------------------------------------------------------/\-----o)
	//   #endregion PRUEBAS DE INTEGRACIÓN
	// (o==================================================================o)
});
```

### 5.3 Checklist para Crear Componentes Nuevos

-   [ ] ✅ Planificar estructura de carpetas por dominio
-   [ ] ✅ Crear modelo API con documentacion JSDoc completa
-   [ ] ✅ Implementar servicio API con separadores de seccion
-   [ ] ✅ Desarrollar controlador API con manejo de errores
-   [ ] ✅ Crear rutas API con protecciones y documentacion
-   [ ] ✅ Crear archivos HTML con separadores de seccion
-   [ ] ✅ Crear archivos CSS/SCSS del componente (si necesario)
-   [ ] ✅ Crear servicio Angular con documentacion completa
-   [ ] ✅ Implementar componente Angular con estructura documentada
-   [ ] ✅ Configurar guards y permisos de acceso (si necesario)
-   [ ] ✅ Registrar rutas con lazy loading (si necesario)
-   [ ] ✅ Agregar al menú lateral con permisos (si necesario)
-   [ ] ✅ Crear archivos de pruebas unitarias (futuro)
-   [ ] ✅ Documentar siguiendo estandares de estructuras
-   [ ] ✅ Probar funcionalidades básicas
-   [ ] ✅ Validar permisos y seguridad
-   [ ] ✅ Verificar integración con sistema existente

## Conclusión

Este proceso asegura que todos los componentes nuevos sigan los mismos estandares de calidad, seguridad, mantenibilidad y **documentacion completa** que el resto del sistema CARRDUCI. La documentacion siguiendo las reglas de `4-estructuras-de-documentacion.md` facilita el mantenimiento y la incorporación de nuevos desarrolladores al proyecto.
