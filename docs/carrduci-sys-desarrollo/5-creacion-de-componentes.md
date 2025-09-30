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

> ⚠️ **NOTA**: Los pipes en este ejemplo están mal nombrados según las reglas de nomenclatura CARRDUCI. Se muestran para mantener consistencia con el sistema existente, pero **NO deben usarse como referencia para nuevos pipes**.

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
    ├── [dominio]-[descripcion].pipe.ts        # ✅ Nomenclatura correcta
    ├── [dominio]-[descripcion].pipe.spec.ts   # ✅ Test correspondiente
    └── [otros pipes del dominio]/
```

#### Módulo de Pipes

```typescript
// pipes-para-conteos/pipes-para-conteos.module.ts
import { NgModule } from '@angular/core';
import { ConteosEstadoPipe } from './conteos-estado.pipe'; // ✅ NOMBRE CORRECTO
import { ConteosBadgeEstadoPipe } from './conteos-badge-estado.pipe'; // ✅ NOMBRE CORRECTO
import { ConteosFormatoFechaPipe } from './conteos-formato-fecha.pipe'; // ✅ NOMBRE CORRECTO

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
const { response } = require('../../utils/response.utils');
const Proveedor = require('../../models/proveedores/proveedores.model');

class ProveedoresService {
	/**
	 * Función de búsqueda UNIFICADA
	 * Reemplaza: buscarPorTérmino, buscar, buscarPorId
	 * Engloba: filtros, término, ID, paginación
	 */
	static async buscar({
		filtros = {},
		termino = '',
		id = null,
		pagina = 1,
		limite = 10,
		orden = { createdAt: -1 },
	}) {
		try {
			let query = {};

			// Aplicar filtros básicos
			if (Object.keys(filtros).length > 0) {
				query = { ...filtros };
			}

			// Búsqueda por término de texto
			if (termino) {
				query.$text = { $search: termino };
			}

			// Búsqueda específica por ID
			if (id) {
				query._id = id;
			}

			const opciones = {
				page: pagina,
				limit: limite,
				sort: orden,
				populate: [
					// populate necesarios para proveedores
				],
			};

			const resultado = await Proveedor.paginate(query, opciones);

			return response.success({
				datos: resultado.docs,
				paginacion: {
					total: resultado.totalDocs,
					pagina: resultado.page,
					paginas: resultado.totalPages,
					limite: resultado.limit,
					hasNext: resultado.hasNextPage,
					hasPrev: resultado.hasPrevPage,
				},
			});
		} catch (error) {
			return response.error(error.message);
		}
	}

	/**
	 * Crear nuevo proveedor
	 */
	static async crear(datos) {
		try {
			const nuevoProveedor = new Proveedor(datos);

			// Agregar metadata para historial
			nuevoProveedor.metadata = {
				idUsuario: datos.usuario,
				descripcion: 'Proveedor creado',
			};

			const proveedorGuardado = await nuevoProveedor.save();
			return response.success(proveedorGuardado);
		} catch (error) {
			return response.error(error.message);
		}
	}

	/**
	 * Actualizar proveedor
	 */
	static async actualizar(id, datos) {
		try {
			const resultado = await Proveedor.findByIdAndUpdate(id, datos, {
				new: true,
				runValidators: true,
				metadata: {
					idUsuario: datos.usuario,
					descripcion: 'Proveedor actualizado',
				},
			});

			if (!resultado) {
				return response.error('Proveedor no encontrado');
			}

			return response.success(resultado);
		} catch (error) {
			return response.error(error.message);
		}
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
			const { filtros, termino, pagina, limite, orden } = req.query;

			const resultado = await ProveedoresService.buscar({
				filtros: filtros ? JSON.parse(filtros) : {},
				termino,
				pagina: parseInt(pagina) || 1,
				limite: parseInt(limite) || 10,
				orden: orden ? JSON.parse(orden) : { createdAt: -1 },
			});

			return response.send(res, resultado);
		} catch (error) {
			return response.error(res, error.message);
		}
	}

	/**
	 * Crear nuevo proveedor
	 */
	static async crearProveedor(req, res) {
		try {
			const resultado = await ProveedoresService.crear({
				...req.body,
				usuario: req.user._id,
			});

			return response.send(res, resultado);
		} catch (error) {
			return response.error(res, error.message);
		}
	}

	/**
	 * Actualizar proveedor
	 */
	static async actualizarProveedor(req, res) {
		try {
			const { id } = req.params;
			const resultado = await ProveedoresService.actualizar(id, {
				...req.body,
				usuario: req.user._id,
			});

			return response.send(res, resultado);
		} catch (error) {
			return response.error(res, error.message);
		}
	}

	/**
	 * Obtener proveedor específico por ID
	 */
	static async obtenerPorId(req, res) {
		try {
			const { id } = req.params;
			const resultado = await ProveedoresService.buscar({ id });

			return response.send(res, resultado);
		} catch (error) {
			return response.error(res, error.message);
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
	ProveedoresController.crearProveedor
);

// Obtener proveedores con filtros y paginación
router.get('/', permisos.$('proveedores:leer'), ProveedoresController.obtener);

// Obtener proveedor específico por ID
router.get(
	'/id/:id',
	permisos.$('proveedores:leer'),
	ProveedoresController.obtenerPorId
);

// Actualizar proveedor
router.put(
	'/id/:id',
	permisos.$('proveedores:actualizar'),
	ProveedoresController.actualizarProveedor
);

// Otros endpoints específicos...

module.exports = router;
```

## 5. Documentación Estándar

### 5.1 Rutas (`pages.routes.ts`)

Agregar entrada con lazy loading usando `loadComponent`:

```typescript
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

### 5.2 Sistema de Permisos

#### Archivo 1: `permisosKeys.config.ts`

Agregar la clave del permiso:

```typescript
// En permisosKeys.config.ts
'menu:administracion:proveedores': 'menu:administracion:proveedores',
```

#### Archivo 2: `permisos.config.ts`

Configurar permisos descriptivos:

```typescript
// En permisos.config.ts
export const permisosConfig = {
	// ... otros permisos
	'menu:administracion:proveedores': {
		descripcion: 'Administración de proveedores',
		modulo: 'administracion',
	},
};
```

#### Archivo API: `permisos.config.js`

Agregar el permiso correspondiente:

```javascript
// En permisos.config.js
'proveedores:leer': NO_DEFINIDO,
'proveedores:crear': NO_DEFINIDO,
'proveedores:actualizar': NO_DEFINIDO,
// ... otros permisos específicos de proveedores
```

### 5.3 Menú Lateral (`login.menus.js`)

#### Agregar Menú Principal

```javascript
function administracion() {
	const menu = {
		permiso: permisos.$('menu:administracion', false),
		titulo: 'Administración',
		icono: 'fas fa-cogs',
		submenu: [
			// ... otros submenús
			{
				titulo: 'Proveedores',
				url: '/administracion/proveedores',
				permiso: permisos.$('menu:administracion:proveedores', false),
			},
		],
	};
	return menu;
}
```

## Checklist para Crear Componentes Nuevos

-   [ ] ✅ Planificar estructura de carpetas por dominio
-   [ ] ✅ Crear componentes con módulos independientes
-   [ ] ✅ Implementar pipes para lógica de templates
-   [ ] ✅ Configurar permisos en GUI y API
-   [ ] ✅ Registrar rutas con lazy loading
-   [ ] ✅ Agregar al menú lateral
-   [ ] ✅ Crear modelo con plugins estándar (historial + búsqueda)
-   [ ] ✅ Implementar servicio con búsqueda unificada
-   [ ] ✅ Desarrollar controlador usando response.utils
-   [ ] ✅ Crear rutas con protecciones
-   [ ] ✅ Documentar siguiendo estándares
-   [ ] ✅ Probar funcionalidades básicas
-   [ ] ✅ Validar permisos y seguridad
-   [ ] ✅ Verificar integración con sistema existente

## Conclusión

Este proceso asegura que todos los componentes nuevos sigan los mismos estándares de calidad, seguridad y mantenibilidad que el resto del sistema CARRDUCI. La consistencia en la estructura y patrones facilita el mantenimiento y la incorporación de nuevos desarrolladores al proyecto.
