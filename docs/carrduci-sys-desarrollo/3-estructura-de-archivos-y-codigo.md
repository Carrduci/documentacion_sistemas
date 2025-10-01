# Estructura de Archivos y Código CARRDUCI-sys

Esta documentación establece la **estructura oficial de archivos y código** para el desarrollo en CARRDUCI-sys. Está basada en la **"Component Domain Architecture"** (Arquitectura de Componentes por Dominios) implementada en el sistema.

!> **IMPORTANTE**: Esta documentación refleja la estructura actualizada a 2025. Todos los nuevos desarrollos deben seguir estrictamente estos patrones.

---

## 🏗️ Arquitectura General: Component Domain Architecture

**CARRDUCI-sys** implementa una **arquitectura modular escalable** organizada por dominios de negocio, con componentes independientes y lazy loading granular.

### Estructura por Capas:

```
🏗️ Frontend (Angular) → Componentes modulares con lazy loading
🔧 Backend (Node.js) → Clases con métodos estáticos para servicios
💾 Persistencia → Modelos Mongoose con plugins estándar
🔐 Seguridad → Permisos jerárquicos unificados
```

---

## 1. Estructura Frontend (GUI) - Angular

### 1.1 Arquitectura Actualizada (2025)

**A partir de ahora, la carpeta `pages/` ya NO se utiliza para nuevos desarrollos.** Todo se crea directamente en `components/`.

```
carrduci-sys-gui/src/app/
├── components/                                           # 🏗️ NUEVO: Todo se crea aquí
│   ├── utiles/                                           # Componentes reutilizables
│   ├── [dominio-nuevo]/                                  # Nuevos módulos aquí
│   │   ├── vista-[dominio-principal]-gestion/            # ✅ Cada componente SU módulo
│   │   │   ├── vista-[dominio-principal]-gestion.component.ts
│   │   │   ├── vista-[dominio-principal]-gestion.component.html
│   │   │   ├── vista-[dominio-principal]-gestion.component.css
│   │   │   └── vista-[dominio-principal]-gestion.module.ts # ✅ Módulo individual del componente
│   │   ├── [dominio-principal]-filtros/                   # ✅ Cada componente SU módulo
│   │   │   ├── [dominio-principal]-filtros.component.ts
│   │   │   ├── [dominio-principal]-filtros.component.html
│   │   │   ├── [dominio-principal]-filtros.component.css
│   │   │   └── [dominio-principal]-filtros.module.ts
│   │   ├── pipes-[dominio-principal]/                      # ✅ Pipes específicos
│   │   │   ├── pipes-[dominio-principal].module.ts
│   │   │   └── pipe-[dominio-principal]-[desc].pipe/      # ✅ Cada pipe: pipe-[dominio-principal]-[desc].pipe
│   │   ├── [dominio-principal].service.ts                 # ✅ Servicio del dominio
│   │   └── [dominio-principal].model.ts                   # ✅ Modelos del dominio
│   └── [módulos existentes]/
├── services/                                             # Servicios HTTP globales
├── models/                                               # Interfaces TypeScript globales
├── pages/                                                # ⚠️ DEPRECATED: Solo para compatibilidad
├── pipes/                                                # Pipes globales (si aplica)
└── [otros directorios]/
```

### 1.2 Tipos de Componentes

#### Componentes de Vista (Vista Components)

**Nombre**: `vista-[dominio]-[nombre-vista].component`
**Archivos**:

```
vista-[name].component.ts     # Controlador (lógica TypeScript)
vista-[name].component.html   # Vista (template HTML)
vista-[name].component.css    # Estilos CSS/SCSS
vista-[name].module.ts        # Módulo independiente
vista-[name].component.spec.ts # Pruebas unitarias (futuro)
```

#### Componentes Auxiliares (Auxiliary Components)

**Nombre**: `[dominio]-[funcionalidad-secundaria].component`
**Archivos**:

```
[component]-[desc].component.ts     # Controlador
[component]-[desc].component.html   # Vista
[component]-[desc].component.css    # Estilos
[component]-[desc].module.ts        # Módulo independiente
[component]-[desc].component.spec.ts # Pruebas unitarias (futuro)
```

### 1.3 Otros Tipos de Archivos

#### Modelos

**Nombre**: `[dominio]-[entidad].model.ts`
**Propósito**: Interfaces TypeScript para modelar datos del API

```typescript
export interface Proveedor {
	id: string;
	nombre: string;
	contacto: Contacto;
	// ... otros campos
}
```

#### Servicios

**Nombre**: `[dominio]-[funcionalidad].service.ts`
**Propósito**: Comunicación HTTP con el API

```typescript
@Injectable({
	providedIn: 'root',
})
export class ProveedoresService {
	// Lógica de comunicación HTTP
}
```

#### Pipes

**Nombre**: `[dominio]-[descripcion].pipe.ts`
**Propósito**: Transformaciones de datos en templates

```typescript
@Pipe({
	name: 'conteosEstado',
})
export class ConteosEstadoPipe implements PipeTransform {
	transform(estado: string): string {
		// Lógica de transformación
	}
}
```

#### Guards

**Nombre**: `[funcionalidad].guard.ts`
**Propósito**: Protección de rutas por permisos

```typescript
@Injectable({
	providedIn: 'root',
})
export class PermisosGuard implements CanActivate {
	canActivate(route: any, state: any): boolean {
		// Lógica de verificación de permisos
	}
}
```

### 1.4 Sistema de Pipes

#### Organización por Dominio

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

---

## 2. Estructura Backend (API) - Node.js/Express

### 2.1 Arquitectura de Clases (2025)

**De ahora en adelante en el API se usarán clases en los controladores y en las rutas.**

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

### 2.2 Tipos de Archivos

#### Rutas (Routes)

**Nombre**: `[dominio].route.js`
**Propósito**: Definición de endpoints HTTP

```javascript
const express = require('express');
const router = express.Router();
const ProveedoresController = require('../../controllers/proveedores/proveedores.controller');
const permisos = require('../config/permisos.config');

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

module.exports = router;
```

#### Controladores (Controllers)

**Nombre**: `[dominio].controller.js`
**Propósito**: Manejo de requests/responses y lógica de control

```javascript
const { response } = require('../../utils/response.utils');
const ProveedoresService = require('../services/proveedores/proveedores.service');

class ProveedoresController {
	/**
	 * Obtener proveedores con filtros y paginación
	 */
	static async obtener(req, res) {
		try {
			const { filtros, termino, desde, limite, sort, campo } = req.query;

			const { resultado, total } = await new ProveedoresService().buscar({
				filtros: filtros ? JSON.parse(filtros) : {},
				termino,
				desde: parseInt(desde) || 0,
				limite: parseInt(limite) || 10,
				sort: parseInt(sort) || -1,
				campo: campo || 'createdAt',
			});

			const resp = new response(res, __filename, {
				mensaje: 'Proveedores obtenidos exitosamente',
				datos: {
					proveedores: resultado,
					total,
				},
			});
			return resp._200_ok();
		} catch (error) {
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
}

module.exports = ProveedoresController;
```

#### Servicios (Services)

**Nombre**: `[dominio].service.js`
**Propósito**: Lógica de negocio y operaciones con base de datos

```javascript
const Proveedor = require('../models/proveedores/proveedores.model');

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
		desde = Number(desde ?? 0);
		limite = Number(limite ?? 10);
		sort = Number(sort ?? -1);
		campo = String(campo ?? 'createdAt');
		filtros = filtros ?? {};
		termino = !!termino ? String(termino).replace(/\\/gm, '') : undefined;

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

		nuevoProveedor.metadata = {
			idUsuario: datos.usuario,
			descripcion: 'Proveedor creado',
		};

		return await nuevoProveedor.save();
	}

	/**
	 * Actualizar proveedor
	 */
	static async actualizar(id, datos) {
		const { estado, ...datosLimpios } = datos;

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

	// Función helper para filtros
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

		return filtros;
	}
}

module.exports = ProveedoresService;
```

#### Modelos (Models)

**Nombre**: `[dominio].model.js`
**Propósito**: Esquemas de MongoDB con plugins estándar

```javascript
const mongoose = require('mongoose');
const { historialPlugin } = require('../plugins/historial/historial.plugin');
const {
	textSearchPlugin,
} = require('../plugins/busqueda-texto/busqueda-texto.plugin');

const proveedorSchema = new mongoose.Schema(
	{
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

---

## 3. Convenciones de Nomenclatura

### 3.1 Componentes de Vista

```
vista-[dominio]-[funcion-principal].component.ts
vista-[dominio]-[funcion-principal].component.html
vista-[dominio]-[funcion-principal].component.css
vista-[dominio]-[funcion-principal].module.ts
```

### 3.2 Componentes Auxiliares

```
[dominio]-[funcion-secundaria].component.ts
[dominio]-[funcion-secundaria].component.html
[dominio]-[funcion-secundaria].component.css
[dominio]-[funcion-secundaria].module.ts
```

### 3.3 Pipes

```
[dominio]-[descripcion].pipe.ts
[dominio]-[descripcion].pipe.spec.ts
```

### 3.4 Servicios y Modelos

```
[dominio].service.ts
[dominio].model.ts
```

### 3.5 API (Backend)

```
[dominio].route.js
[dominio].controller.js
[dominio].service.js
[dominio].model.js
```

---

## 4. Arquitectura de Rutas

### 4.1 Lazy Loading por Componente

**Regla estricta**: Cada componente tiene su propio módulo independiente y se carga individualmente.

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

### 4.2 Organización de `pages.routes.ts`

El archivo usa separadores de sección para organizar rutas por dominio:

```typescript
// (o==================================================================o)
//   #region ALMACEN
// (o-----------------------------------------------------------\/-----o)

// (o,,,,,,,,,,,CONTEOS,,,,,,,,,,o)
//   #region    conteos
// (o'''''''''''CONTEOS''''v'''''o)

export const rutasAlmacenConteos: Routes = [
	// Rutas de conteos aquí
];

// (o,,,,,,,,,,,CONTEOS,,,,^,,,,,o)
//   #endregion conteos
// (o'''''''''''CONTEOS''''''''''o)

// (o-----------------------------------------------------------/\-----o)
//   #endregion ALMACEN
// (o==================================================================o)
```

---

## 5. Sistema de Permisos

### 5.1 Estructura Jerárquica Unificada

```
[contexto]:[entidad]:[accion]:[subaccion-opcional]
```

**Ejemplos:**

-   `proveedor:leer` - Leer proveedores
-   `proveedor:acciones:activar` - Activar proveedores
-   `menu:compras` - Acceso al módulo compras

### 5.2 Archivos de Configuración

**Tres archivos sincronizados:**

-   `permisosKeys.config.ts` - Claves de permisos
-   `permisos.config.ts` - Configuración NO_DEFINIDO
-   `permisos.config.js` - Configuración backend

---

## 6. Sistema de Pipes

### 6.1 Organización por Dominio

Cada dominio tiene su propio directorio de pipes:

```
components/[dominio]/
└── pipes-[dominio]/
    ├── pipes-[dominio].module.ts
    ├── [dominio]-[descripcion]/
    │   ├── [dominio]-[descripcion].pipe.ts
    │   └── [dominio]-[descripcion].pipe.spec.ts
    └── [otros pipes]/
        ├── [dominio]-[otra-descripcion]/
        │   ├── [dominio]-[otra-descripcion].pipe.ts
        │   └── [dominio]-[otra-descripcion].pipe.spec.ts
```

### 6.2 Módulo de Pipes

```typescript
@NgModule({
    declarations: [/* Todos los pipes del dominio */],
    exports: [/* Todos los pipes del dominio */],
})
export class PipesPara[Domino]Module {}
```

---

## 7. Documentación Estandarizada

### 7.1 Separadores de Sección

```typescript
// (o==================================================================o)
//   #region IMPORTACIONES
// (o-----------------------------------------------------------\/-----o)

// Código aquí

// (o-----------------------------------------------------------/\-----o)
//   #endregion IMPORTACIONES
// (o==================================================================o)
```

### 7.2 Comentarios JSDoc Obligatorios

```javascript
/**
 * Descripción de la función
 * @param {Tipo} parametro - Descripción del parámetro
 * @returns {Tipo} - Descripción del retorno
 */
```

---

# Índice de archivos

Este índice servirá para identificar a qué componentes pertenecen los archivos (necesitas tener una cuenta de google con acceso al catálogo).

[Catálogo completo en esta dirección.](https://docs.google.com/spreadsheets/d/1Avh_WMtHkZquh4DFFig7k7eYxV8H9e3UFMLI6xUjikY/edit?gid=2022342688#gid=2022342688)
