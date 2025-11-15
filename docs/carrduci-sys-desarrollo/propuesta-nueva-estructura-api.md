# Propuesta: Nueva Estructura Automática de API con Módulos Dinámicos

## Concepto General

Esta propuesta introduce una **arquitectura completamente automática** donde los módulos se detectan al iniciar la aplicación, generando permisos y menús dinámicamente sin escribir código manualmente. Los módulos se definen en archivos `.module.js` que se auto-registran en MongoDB.

## Arquitectura del Sistema

### Estructura de Carpetas Propuesta

```
carrduci-sys-api/
├── components/
│   ├── compras/
│   ├── proveedores/
│   ├── proveedores.module.js
│   ├── routes/
│   │   │   │   └── proveedores.route.js
│   ├── controllers/
│   │   │   │   └── proveedores.controller.js
│   ├── services/
│   │   │   │   └── proveedores.service.js
│   │   │   └── models/
│   │   │       └── proveedores.model.js
│   ├── pedidos/
│   ├── pedidos.module.js
│   │   │   ├── routes/
│   │   │   │   └── pedidos.route.js
│   │   │   ├── controllers/
│   │   │   │   └── pedidos.controller.js
│   │   │   ├── services/
│   │   │   │   └── pedidos.service.js
│   │   │   └── models/
│   │   │       └── pedidos.model.js
│   │   └── facturas/
│   │       ├── facturas.module.js
│   │       ├── routes/
│   │       │   └── facturas.route.js
│   │       ├── controllers/
│   │       │   └── facturas.controller.js
│   │       ├── services/
│   │       │   └── facturas.service.js
│   │       └── models/
│   │           └── facturas.model.js
│   ├── ventas/
│   ├── clientes/
│   │   └── productos/
│   ├── inventario/
│   ├── almacenes/
│   │   └── movimientos/
│   ├── administracion/
│   ├── usuarios/
│   │   └── permisos/
│   └── reportes/
│       ├── dashboard/
│       └── analisis/
├── core/
│   ├── module-registry/
│   │   ├── module.registry.js
│   │   ├── permission.generator.js
│   │   └── menu.generator.js
│   ├── utils/
│   │   ├── response.utils.js
│   │   └── varios.js
│   ├── plugins/
│   │   ├── busqueda-texto.plugin.js
│   │   ├── hisotrial.plugin.js
│   └── middleware/
│       ├── autenticacion.js
│       ├── busqueda/   #DEPRECADO
│       ├── conteos/
│       └── historial/ 	#DEPRECADO
├── config/
└── app.js
```

Cada componente tiene su propio archivo `.module.js` que define su configuración específica:

```javascript
// components/compras/proveedores/proveedores.module.js
const { Module } = require('../../core/module-registry/module.registry');

module.exports = new Module({
    // 🔧 Configuración específica del componente
    nombre: 'proveedores',
    descripcion: 'Gestión completa de proveedores',
    contexto: 'compras', // 👈 Contexto amplio para agrupar en menús
    dominio: 'proveedores', // 👈 Dominio específico del componente

    // 📍 Ruta base del componente
    rutaBase: '/api/proveedores',

    // 🎨 Configuración visual
    icono: 'fas fa-truck',
    color: '#28a745',

    // 📊 Metadata específica del componente
    metadata: {
        filename: __filename,
        tipoEntidad: 'proveedor',
        camposBusqueda: ['nombre', 'rfc', 'email'],
        camposOrdenamiento: ['nombre', 'fechaCreacion', 'estado']
    },

    // 🔗 Relaciones con otros componentes (opcional)
    relaciones: {
        pedidos: { tipo: 'hasMany', componente: 'pedidos' },
        facturas: { tipo: 'hasMany', componente: 'facturas' }
    }
});
```

```javascript
// components/compras/pedidos/pedidos.module.js
const { Module } = require('../../core/module-registry/module.registry');

module.exports = new Module({
    nombre: 'pedidos',
    descripcion: 'Gestión de pedidos de compra',
    contexto: 'compras', // 👈 Mismo contexto amplio
    dominio: 'pedidos', // 👈 Dominio específico

    rutaBase: '/api/pedidos',
    icono: 'fas fa-clipboard-list',
    color: '#007bff',

    metadata: {
        filename: __filename,
        tipoEntidad: 'pedidoCompra',
        camposBusqueda: ['numeroPedido', 'proveedor.nombre'],
        estados: ['borrador', 'aprobado', 'recibido', 'cancelado']
    },

    relaciones: {
        proveedores: { tipo: 'belongsTo', componente: 'proveedores' },
        facturas: { tipo: 'hasMany', componente: 'facturas' }
    }
});
```

```javascript
// components/compras/facturas/facturas.module.js
const { Module } = require('../../core/module-registry/module.registry');

module.exports = new Module({
    nombre: 'facturas',
    descripcion: 'Gestión de facturas de compra',
    contexto: 'compras', // 👈 Mismo contexto amplio
    dominio: 'facturas', // 👈 Dominio específico

    rutaBase: '/api/facturas',
    icono: 'fas fa-file-invoice',
    color: '#dc3545',

    metadata: {
        filename: __filename,
        tipoEntidad: 'facturaCompra',
        camposBusqueda: ['numeroFactura', 'proveedor.nombre', 'total'],
        requiereAprobacion: true
    },

    relaciones: {
        proveedores: { tipo: 'belongsTo', componente: 'proveedores' },
        pedidos: { tipo: 'belongsTo', componente: 'pedidos' }
    }
});
```

### Registro Automático en MongoDB

#### Modelo de Componente en Base de Datos

```javascript
// models/componente/componente.model.js
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const componenteSchema = new mongoose.Schema(
    {
        nombre: {
            type: String,
            required: true,
            unique: true,
            index: true
        },
        descripcion: String,
        contexto: {
            type: String,
            required: true,
            index: true // 👈 Para agrupar componentes en menús
        },
        dominio: {
            type: String,
            required: true,
            index: true // 👈 Dominio específico del componente
        },
        rutaBase: {
            type: String,
            required: true
        },
        icono: String,
        color: String,
        activo: {
            type: Boolean,
            default: true
        },

        // 📊 Metadata específica del componente
        metadata: Schema.Types.Mixed,

        // 🔗 Relaciones con otros componentes
        relaciones: [
            {
                nombre: String,
                tipo: {
                    type: String,
                    enum: ['belongsTo', 'hasMany', 'hasOne']
                },
                componente: String, // Referencia al nombre del componente relacionado
                opciones: Schema.Types.Mixed
            }
        ],

        // Información de auditoría
        registradoPor: String,
        fechaRegistro: { type: Date, default: Date.now },
        ultimaActualizacion: { type: Date, default: Date.now }
    },
    {
        collection: 'componentes',
        timestamps: true
    }
);

// Índices para consultas eficientes
componenteSchema.index({ contexto: 1, dominio: 1 });
componenteSchema.index({ 'relaciones.componente': 1 });

module.exports = mongoose.model('Componente', componenteSchema);
```

#### Modelo de Menú Dinámico

```javascript
// models/menu/menu.model.js
const mongoose = require('mongoose');

const menuSchema = new mongoose.Schema(
    {
        contexto: {
            type: String,
            required: true,
            index: true
        },
        titulo: {
            type: String,
            required: true
        },
        icono: String,
        orden: {
            type: Number,
            default: 999
        },
        grupo: String,
        visible: {
            type: Boolean,
            default: true
        },

        // Submenús generados automáticamente
        submenus: [
            {
                titulo: String,
                url: String,
                permiso: String,
                icono: String,
                orden: Number,
                activo: { type: Boolean, default: true }
            }
        ],

        metadata: mongoose.Schema.Types.Mixed,
        fechaCreacion: { type: Date, default: Date.now }
    },
    {
        collection: 'menus',
        timestamps: true
    }
);

module.exports = mongoose.model('Menu', menuSchema);
```

## Generación Automática de Permisos

### Sistema de Detección de Rutas

```javascript
// core/module-registry/route.detector.js
class RouteDetector {
    static detectarRutas(app) {
        // 🔍 Inspeccionar el router stack de Express
        return app._router.stack
            .filter((layer) => layer.route) // Solo rutas, no middleware
            .map((layer) => ({
                metodo: Object.keys(layer.route.methods)[0].toUpperCase(),
                ruta: layer.route.path,
                handlers: layer.route.stack.map((s) => s.handle),
                metadata: this.extraerMetadata(layer.route.stack)
            }));
    }

    static extraerMetadata(stack) {
        // 📋 Extraer información de permisos de los handlers
        const metadata = {};

        stack.forEach((layer) => {
            if (layer.handle.permiso) {
                metadata.permiso = layer.handle.permiso;
            }
            if (layer.handle.modulo) {
                metadata.modulo = layer.handle.modulo;
            }
        });

        return metadata;
    }
}
```

### Generador Automático de Permisos

```javascript
// core/module-registry/permission.generator.js
const Permiso = require('../../models/permiso/permiso.model');

class PermissionGenerator {
    static async generarPermisosDesdeRutas(app, modulos) {
        const rutas = RouteDetector.detectarRutas(app);
        const permisosGenerados = [];

        for (const ruta of rutas) {
            const permiso = await this.generarPermisoParaRuta(ruta, modulos);
            if (permiso) {
                permisosGenerados.push(permiso);
            }
        }

        // 💾 Bulk upsert de permisos
        if (permisosGenerados.length > 0) {
            await this.guardarPermisosBulk(permisosGenerados);
        }

        return permisosGenerados;
    }

    static async generarPermisoParaRuta(ruta, modulos) {
        // 🧩 Resolver el módulo correspondiente
        const moduloCorrespondiente = this.encontrarModuloParaRuta(
            ruta.ruta,
            modulos
        );

        if (!moduloCorrespondiente) {
            console.warn(`⚠️ No se encontró módulo para ruta: ${ruta.ruta}`);
            return null;
        }

        // 🔧 Generar clave de permiso basada en patrón
        const clavePermiso = this.generarClavePermiso(
            ruta,
            moduloCorrespondiente
        );

        // 📝 Crear permiso
        return {
            clave: clavePermiso,
            descripcion: this.generarDescripcionPermiso(
                ruta,
                moduloCorrespondiente
            ),
            modulo: moduloCorrespondiente.contexto,
            categoria: this.determinarCategoria(ruta.metodo),
            nivel: this.determinarNivel(ruta.metodo),
            metadata: {
                filename: __filename,
                ruta: ruta.ruta,
                metodo: ruta.metodo,
                modulo: moduloCorrespondiente.nombre,
                tipo: 'auto-generado',
                entidad: this.extraerEntidadDeRuta(ruta.ruta),
                accion: this.extraerAccionDeRuta(ruta.ruta, ruta.metodo)
            },
            creadoPor: 'sistema-auto',
            fechaCreacion: new Date()
        };
    }

    static encontrarModuloParaRuta(ruta, modulos) {
        // 🔍 Buscar el módulo que maneja esta ruta
        return modulos.find(
            (modulo) =>
                ruta.startsWith(modulo.rutaBase) ||
                modulo.submodulos.some((sub) => ruta.startsWith(sub.rutaBase))
        );
    }

    static generarClavePermiso(ruta, modulo) {
        // 📋 Patrón: [entidad]:[accion]
        const entidad = this.extraerEntidadDeRuta(ruta.ruta);
        const accion = this.extraerAccionDeRuta(ruta.ruta, ruta.metodo);

        return `${entidad}:${accion}`;
    }

    static extraerEntidadDeRuta(ruta) {
        // 🧩 Extraer entidad del patrón /api/[modulo]/[entidad]/...
        const partes = ruta.split('/').filter((p) => p);
        if (partes.length >= 3 && partes[0] === 'api') {
            return partes[2]; // ej: 'proveedores', 'pedidos'
        }
        return 'general';
    }

    static extraerAccionDeRuta(ruta, metodo) {
        // 🎯 Determinar acción basada en método HTTP y patrón de ruta
        if (metodo === 'GET') {
            return ruta.includes('/id/') ? 'leer' : 'listar';
        }
        if (metodo === 'POST') return 'crear';
        if (metodo === 'PUT') return 'modificar';
        if (metodo === 'DELETE') return 'eliminar';

        return 'acceder';
    }

    static determinarCategoria(metodo) {
        const categorias = {
            GET: 'lectura',
            POST: 'escritura',
            PUT: 'escritura',
            DELETE: 'escritura'
        };
        return categorias[metodo] || 'acceso';
    }

    static determinarNivel(metodo) {
        const niveles = {
            GET: 'basico',
            POST: 'medio',
            PUT: 'medio',
            DELETE: 'alto'
        };
        return niveles[metodo] || 'medio';
    }

    static generarDescripcionPermiso(ruta, modulo) {
        const entidad = this.extraerEntidadDeRuta(ruta.ruta);
        const accion = this.extraerAccionDeRuta(ruta.ruta, ruta.metodo);

        return `${modulo.descripcion} - ${accion} ${entidad}`;
    }

    static async guardarPermisosBulk(permisos) {
        const bulkOps = permisos.map((permiso) => ({
            updateOne: {
                filter: { clave: permiso.clave },
                update: permiso,
                upsert: true,
                setDefaultsOnInsert: { fechaCreacion: new Date() }
            }
        }));

        const resultado = await Permiso.bulkWrite(bulkOps);
        console.log(
            `✅ ${resultado.upsertedCount} permisos generados, ${resultado.modifiedCount} actualizados`
        );
    }
}
```

## Generación Automática de Menús

### Generador de Menús por Contexto

```javascript
// core/module-registry/menu.generator.js
const Menu = require('../../models/menu/menu.model');

class MenuGenerator {
    static async generarMenusDesdeComponentes(componentes) {
        // 👈 Componentes en lugar de módulos
        const contextos = this.agruparPorContexto(componentes);
        const menusGenerados = [];

        for (const [contexto, componentesContexto] of Object.entries(
            contextos
        )) {
            const menu = await this.generarMenuParaContexto(
                contexto,
                componentesContexto
            );
            if (menu) {
                menusGenerados.push(menu);
            }
        }

        // 💾 Guardar menús en bulk
        if (menusGenerados.length > 0) {
            await this.guardarMenusBulk(menusGenerados);
        }

        return menusGenerados;
    }

    static agruparPorContexto(componentes) {
        // 👈 Agrupar componentes por contexto para crear menús
        return componentes.reduce((contextos, componente) => {
            const contexto = componente.contexto;
            if (!contextos[contexto]) {
                contextos[contexto] = [];
            }
            contextos[contexto].push(componente);
            return contextos;
        }, {});
    }

    static async generarMenuParaContexto(contexto, componentes) {
        // 📋 Crear menú agrupando componentes por contexto
        const submenus = componentes.map((componente) =>
            this.generarSubmenuParaComponente(componente)
        );

        return {
            contexto: contexto,
            titulo: this.generarTituloContexto(contexto),
            icono: this.generarIconoContexto(contexto),
            orden: this.calcularOrdenContexto(contexto),
            grupo: 'operaciones',
            visible: true,
            submenus: submenus,
            metadata: {
                filename: __filename,
                componentes: componentes.length,
                tipo: 'auto-generado-contexto'
            }
        };
    }

    static generarSubmenuParaComponente(componente) {
        return {
            titulo: this.capitalizar(componente.nombre),
            url: `/app/${componente.contexto}/${componente.dominio}`,
            permiso: `${componente.dominio}:leer`, // 👈 Permiso generado automáticamente
            icono: componente.icono,
            orden: componente.orden || 0,
            activo: componente.activo
        };
    }

    static generarTituloContexto(contexto) {
        // 🎨 Generar títulos naturales para contextos
        const titulos = {
            compras: 'Compras',
            ventas: 'Ventas',
            inventario: 'Inventario',
            administracion: 'Administración',
            reportes: 'Reportes'
        };
        return titulos[contexto] || this.capitalizar(contexto);
    }

    static generarIconoContexto(contexto) {
        // 🎨 Generar iconos para contextos
        const iconos = {
            compras: 'fas fa-shopping-cart',
            ventas: 'fas fa-cash-register',
            inventario: 'fas fa-boxes',
            administracion: 'fas fa-cogs',
            reportes: 'fas fa-chart-bar'
        };
        return iconos[contexto] || 'fas fa-folder';
    }

    static calcularOrdenContexto(contexto) {
        // 📊 Orden estándar para contextos
        const ordenes = {
            compras: 1,
            ventas: 2,
            inventario: 3,
            administracion: 4,
            reportes: 5
        };
        return ordenes[contexto] || 999;
    }

    static capitalizar(texto) {
        return texto.charAt(0).toUpperCase() + texto.slice(1);
    }

    static async guardarMenusBulk(menus) {
        const bulkOps = menus.map((menu) => ({
            updateOne: {
                filter: { contexto: menu.contexto },
                update: menu,
                upsert: true
            }
        }));

        const resultado = await Menu.bulkWrite(bulkOps);
        console.log(
            `✅ ${resultado.upsertedCount} menús generados, ${resultado.modifiedCount} actualizados`
        );
    }
}
```

## Registro de Módulos - Sistema Principal

### Registry Principal de Componentes

```javascript
// core/module-registry/module.registry.js
const fs = require('fs').promises;
const path = require('path');
const Componente = require('../../models/componente/componente.model');
const PermissionGenerator = require('./permission.generator');
const MenuGenerator = require('./menu.generator');

class ModuleRegistry {
    constructor() {
        this.componentes = [];
        this.componentsPath = path.join(__dirname, '../../components'); // 👈 Cambiado de modules a components
    }

    async inicializar(app) {
        console.log('🔧 Inicializando sistema de componentes...');

        try {
            // 1. 🔍 Escanear archivos .module.js en cada directorio de componente
            const archivosComponente = await this.escanearArchivosComponente();
            console.log(
                `📁 Encontrados ${archivosComponente.length} archivos de componente`
            );

            // 2. 📋 Cargar configuraciones de componentes
            await this.cargarComponentes(archivosComponente);

            // 3. 💾 Registrar componentes en base de datos
            await this.registrarComponentesEnBD();

            // 4. 🔐 Generar permisos automáticamente desde rutas
            await PermissionGenerator.generarPermisosDesdeRutas(
                app,
                this.componentes
            );

            // 5. 📊 Generar menús automáticamente agrupando por contexto
            await MenuGenerator.generarMenusDesdeComponentes(this.componentes);

            console.log('✅ Sistema de componentes inicializado correctamente');
            console.log(
                `📊 Registrados ${this.componentes.length} componentes`
            );
        } catch (error) {
            console.error('❌ Error inicializando componentes:', error);
            throw error;
        }
    }

    async escanearArchivosComponente() {
        const archivos = [];

        try {
            // 🔍 Escanear grupos de componentes (compras, ventas, etc.)
            const gruposComponentes = await fs.readdir(this.componentsPath);

            for (const grupo of gruposComponentes) {
                const rutaGrupo = path.join(this.componentsPath, grupo);

                // Verificar si es un directorio de grupo
                const statGrupo = await fs.stat(rutaGrupo);
                if (!statGrupo.isDirectory()) continue;

                // 🔍 Escanear componentes dentro del grupo
                const componentes = await fs.readdir(rutaGrupo);

                for (const componente of componentes) {
                    const rutaComponente = path.join(rutaGrupo, componente);

                    // Verificar si es un directorio de componente
                    const statComponente = await fs.stat(rutaComponente);
                    if (!statComponente.isDirectory()) continue;

                    // Buscar archivo .module.js en el directorio del componente
                    const archivoComponente = path.join(
                        rutaComponente,
                        `${componente}.module.js`
                    );

                    try {
                        await fs.access(archivoComponente);
                        archivos.push({
                            ruta: archivoComponente,
                            grupo: grupo,
                            componente: componente,
                            nombre: `${componente}.module.js`
                        });
                    } catch (error) {
                        // Archivo no existe, continuar
                        console.warn(
                            `⚠️ Archivo de componente no encontrado: ${archivoComponente}`
                        );
                    }
                }
            }
        } catch (error) {
            console.error('❌ Error escaneando archivos de componente:', error);
        }

        return archivos;
    }

    async cargarComponentes(archivos) {
        for (const archivo of archivos) {
            try {
                const componente = require(archivo.ruta);

                // Validar que sea una instancia de Module
                if (!(componente instanceof Module)) {
                    console.warn(
                        `⚠️ ${archivo.ruta} no exporta una instancia de Module`
                    );
                    continue;
                }

                this.componentes.push(componente);
                console.log(`📦 Componente cargado: ${componente.nombre}`);
            } catch (error) {
                console.error(
                    `❌ Error cargando componente ${archivo.ruta}:`,
                    error
                );
            }
        }
    }

    async registrarComponentesEnBD() {
        const bulkOps = this.componentes.map((componente) => ({
            updateOne: {
                filter: { nombre: componente.nombre },
                update: {
                    ...componente,
                    ultimaActualizacion: new Date()
                },
                upsert: true,
                setDefaultsOnInsert: { fechaRegistro: new Date() }
            }
        }));

        const resultado = await Componente.bulkWrite(bulkOps);
        console.log(
            `✅ ${resultado.upsertedCount} componentes registrados, ${resultado.modifiedCount} actualizados`
        );
    }
}

// Clase base para componentes
class Module {
    constructor(config) {
        this.nombre = config.nombre;
        this.descripcion = config.descripcion;
        this.contexto = config.contexto;
        this.dominio = config.dominio || config.nombre;
        this.rutaBase = config.rutaBase;
        this.icono = config.icono;
        this.color = config.color;
        this.metadata = config.metadata || {};
        this.relaciones = config.relaciones || [];
        this.activo = config.activo !== false;
    }
}

module.exports = { ModuleRegistry, Module };
```

## Inicialización en el Startup

### app.js - Punto de Entrada con Sistema Automático

```javascript
// app.js
const express = require('express');
const mongoose = require('mongoose');
const { ModuleRegistry } = require('./core/module-registry/module.registry');

const app = express();

// Configuración básica
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

async function inicializarAplicacion() {
    try {
        // 1. 🔌 Conectar a MongoDB
        await mongoose.connect(process.env.MONGODB_URI);
        console.log('✅ Conectado a MongoDB');

        // 2. 🔧 Inicializar sistema de módulos (automático)
        const moduleRegistry = new ModuleRegistry();
        await moduleRegistry.inicializar(app);

        // 3. 🚀 Iniciar servidor
        const PORT = process.env.PORT || 3000;
        app.listen(PORT, () => {
            console.log(`🚀 Servidor ejecutándose en puerto ${PORT}`);
            console.log(`📊 Sistema de módulos CARRDUCI inicializado`);
        });
    } catch (error) {
        console.error('❌ Error inicializando aplicación:', error);
        process.exit(1);
    }
}

// Iniciar aplicación
inicializarAplicacion();
```

## Ejemplo de Implementación Completa

### Componente de Proveedores Independiente

```javascript
// components/compras/proveedores/proveedores.module.js
const { Module } = require('../../core/module-registry/module.registry');

module.exports = new Module({
    nombre: 'proveedores',
    descripcion: 'Gestión completa de proveedores',
    contexto: 'compras', // 👈 Agrupa con otros componentes de compras
    dominio: 'proveedores', // 👈 Dominio específico
    rutaBase: '/api/proveedores',
    icono: 'fas fa-truck',
    color: '#28a745',

    metadata: {
        filename: __filename,
        tipoEntidad: 'proveedor',
        camposBusqueda: ['nombre', 'rfc', 'email'],
        camposOrdenamiento: ['nombre', 'fechaCreacion', 'estado']
    },

    relaciones: {
        pedidos: { tipo: 'hasMany', componente: 'pedidos' },
        facturas: { tipo: 'hasMany', componente: 'facturas' }
    }
});
```

### Rutas que se Auto-Registran por Componente

```javascript
// modules/proveedores/routes/proveedores.route.js
const express = require('express');
const router = express.Router();
const ProveedoresController = require('../controllers/proveedores.controller');

// 📋 Estas rutas se detectarán automáticamente y generarán permisos
router.get('/', ProveedoresController.obtener); // 👈 Genera: proveedores:listar
router.get('/id/:id', ProveedoresController.obtenerPorId); // 👈 Genera: proveedores:leer
router.post('/', ProveedoresController.crear); // 👈 Genera: proveedores:crear
router.put('/id/:id', ProveedoresController.actualizar); // 👈 Genera: proveedores:modificar
router.delete('/id/:id', ProveedoresController.eliminar); // 👈 Genera: proveedores:eliminar

module.exports = router;
```

## Beneficios del Sistema

1. **Componentes Independientes**: Cada entidad es un componente modular con su propia configuración
2. **Agrupación por Contexto**: Componentes se agrupan automáticamente en menús por contexto amplio
3. **Escalabilidad Máxima**: Agregar nuevos componentes sin afectar otros
4. **Relaciones Explícitas**: Definir relaciones entre componentes de forma declarativa
5. **Configuración Específica**: Cada componente tiene metadata y configuración propia
6. **Detección Automática**: Cero código manual para permisos y menús

## Resultado Final Automático

### Componentes Registrados

```
📦 compras/
   ├── proveedores (contexto: compras, dominio: proveedores)
   ├── pedidos     (contexto: compras, dominio: pedidos)
   └── facturas    (contexto: compras, dominio: facturas)
📦 ventas/
   ├── clientes    (contexto: ventas, dominio: clientes)
   └── productos   (contexto: ventas, dominio: productos)
📦 inventario/
   ├── almacenes   (contexto: inventario, dominio: almacenes)
   └── movimientos (contexto: inventario, dominio: movimientos)
```

### Permisos Generados Automáticamente

```
proveedores:listar    (GET /api/proveedores)
proveedores:leer      (GET /api/proveedores/id/:id)
proveedores:crear     (POST /api/proveedores)
proveedores:modificar (PUT /api/proveedores/id/:id)
proveedores:eliminar  (DELETE /api/proveedores/id/:id)
pedidos:listar        (GET /api/pedidos)
pedidos:leer          (GET /api/pedidos/id/:id)
pedidos:crear         (POST /api/pedidos)
[etc...]
```

### Menú Generado Automáticamente por Contexto

```json
{
  "contexto": "compras",
  "titulo": "Compras",
  "icono": "fas fa-shopping-cart",
  "submenus": [
    {
      "titulo": "Proveedores",
      "url": "/app/compras/proveedores",
      "permiso": "proveedores:leer"
    },
    {
      "titulo": "Pedidos",
      "url": "/app/compras/pedidos",
      "permiso": "pedidos:leer"
    },
    {
      "titulo": "Facturas",
      "url": "/app/compras/facturas",
      "permiso": "facturas:leer"
  ]
```

```

```
