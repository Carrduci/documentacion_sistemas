# 🏗️ Documentación CARRDUCI-sys

**Documentación oficial del sistema CARRDUCI-sys**, una arquitectura modular escalable organizada por dominios de negocio con componentes independientes y lazy loading granular.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Online-blue)](https://carrduci.github.io/documentacion_sistemas/)
[![Arquitectura](https://img.shields.io/badge/Arquitectura-Component%20Domain%20Architecture-green)](#-arquitectura-component-domain-architecture)
[![Versión](https://img.shields.io/badge/Versión-2025-orange)](#-cambios-2025)

---

## 📋 Arquitectura Component Domain Driven Architecture

CARRDUCI-sys implementa una **"Component Domain Architecture"** (Arquitectura de Componentes por Dominios), una arquitectura modular escalable que organiza el código por dominios de negocio con componentes independientes.

### 🏗️ Características Principales

-   **Modular por Dominios**: Cada dominio de negocio (compras, ventas, almacén, etc.) tiene su estructura completa independiente
-   **Componentes Independientes**: Cada componente tiene su propio módulo individual (regla estricta: "cada componente su módulo")
-   **Lazy Loading por Componente**: Carga bajo demanda a nivel granular, no por módulos grandes
-   **Permisos Unificados**: Sistema de permisos consistente entre GUI y API
-   **Documentación Estandarizada**: Separadores de sección y reglas JSDoc obligatorias

### 🏛️ Estructura por Capas

```
🏗️ Frontend (Angular) → Componentes modulares con lazy loading
🔧 Backend (Node.js) → Rutas, controladores, servicios, utilidades y plugins
💾 Persistencia → Modelos Mongoose con plugins estándar
🔐 Seguridad → Permisos jerárquicos unificados
```

---

## 📚 Contenido de la Documentación

### 🏗️ **CARRDUCI-sys Desarrollo**

#### ⚙️ **Configuración del Entorno**

-   **[Instalación WSL](./docs/carrduci-sys-desarrollo/1-instalacion-wsl.md)** - Configuración del subsistema Linux en Windows
-   **[Entorno de Desarrollo](./docs/carrduci-sys-desarrollo/2-entorno-desarollo.md)** - Despliegue completo del entorno de desarrollo
-   **[Estructura de Archivos y Código](./docs/carrduci-sys-desarrollo/3-estructura-de-archivos-y-codigo.md)** - Arquitectura Component Domain Architecture
-   **[Estructuras de Documentación](./docs/carrduci-sys-desarrollo/4-estructuras-de-documentacion.md)** - Estándares de documentación JSDoc

#### 🧩 **Creación de Componentes**

-   **[Creación de Componentes](./docs/carrduci-sys-desarrollo/5-creacion-de-componentes.md)** - Guía completa para crear componentes GUI + API
-   **[Generar Versiones y Docker](./docs/carrduci-sys-desarrollo/6-generar-version-y-compilar-imagenes-docker.md)** - Empaquetado y despliegue

#### 🛠️ **Componentes Reutilizables**

| Componente                                                                                                       | Descripción                                       | Estado       | Última Actualización |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------ | -------------------- |
| **[Tabla Genérica](./docs/carrduci-sys-desarrollo/uso-componentes/tabla-generica.md)**                           | Listados paginados con filtros y acciones         | ✅ Completo  | -                    |
| **[Formulario Dinámico](./docs/carrduci-sys-desarrollo/uso-componentes/formulario-dinamico.md)**                 | Formularios reactivos tipados                     | ✅ Completo  | 2025-10-03           |
| **[Carga de Imágenes](./docs/carrduci-sys-desarrollo/uso-componentes/carga-de-imagenes.md)**                     | Upload y compresión de imágenes                   | ✅ Completo  | 2025-10-01           |
| **[Historial](./docs/carrduci-sys-desarrollo/uso-componentes/historial.md)**                                     | Sistema de auditoría automática                   | ✅ Completo  | 2025-10-01           |
| **[Claves de Autorización](./docs/carrduci-sys-desarrollo/uso-componentes/claves-autorizacion.md)**              | Sistema de autorizaciones críticas                | ✅ Completo  | 2025-10-01           |
| **[Flotante Genérico](./docs/carrduci-sys-desarrollo/uso-componentes/flotante-generico.md)**                     | Tooltips y popovers personalizados                | ✅ Completo  | -                    |
| **[Búsqueda de Texto](./docs/carrduci-sys-desarrollo/uso-componentes/busqueda-texto.md)**                        | Indexación y búsqueda avanzada                    | ✅ Completo  | 2025-10-01           |
| **[Carrusel de Imágenes](./docs/carrduci-sys-desarrollo/uso-componentes/carrusel-de-imagenes-generico.md)**      | Galerías de imágenes interactivas                 | ✅ Completo  | -                    |
| **[Gestor de Impresiones](./docs/carrduci-sys-desarrollo/uso-componentes/gestor-de-impresiones.md)**             | Sistema de impresión avanzado                     | ✅ Completo  | -                    |
| **[Calendario Genérico](./docs/carrduci-sys-desarrollo/uso-componentes/calendario-generico.md)**                 | Selectores de fecha personalizados                | ✅ Completo  | -                    |
| **[Auto Increment](./docs/carrduci-sys-desarrollo/uso-componentes/auto-increment.md)**                           | Generación automática de IDs                      | ✅ Completo  | -                    |
| **[Tabla Editable](./docs/carrduci-sys-desarrollo/uso-componentes/tabla-editable-generica.md)**                  | Tablas con edición inline                         | 🚧 Pendiente | -                    |
| **[Mini Visualizador Foto](./docs/carrduci-sys-desarrollo/uso-componentes/mini-visualizador-foto.md)**           | Previsualización de imágenes                      | 🚧 Pendiente | -                    |
| **[Modal Genérico](./docs/carrduci-sys-desarrollo/uso-componentes/modal.md)**                                    | Diálogos modales reutilizables                    | ✅ Completo  | -                    |
| **[Paginación y Filtros](./docs/carrduci-sys-desarrollo/uso-componentes/paginacion-y-filtros.md)**               | Sistema de paginación avanzado                    | 🚧 Pendiente | -                    |
| **[Permisos](./docs/carrduci-sys-desarrollo/uso-componentes/permisos.md)**                                       | Gestión de permisos de usuario                    | 🚧 Pendiente | -                    |
| **[Selector Fechas](./docs/carrduci-sys-desarrollo/uso-componentes/selector-fechas-generico.md)**                | Selectores de fecha avanzados                     | 🚧 Pendiente | -                    |
| **[Sockets](./docs/carrduci-sys-desarrollo/uso-componentes/sockets.md)**                                         | Comunicación en tiempo real                       | 🚧 Pendiente | -                    |
| **[Vista Genérica](./docs/carrduci-sys-desarrollo/uso-componentes/vista-generica.md)**                           | Layouts reutilizables                             | 🚧 Pendiente | -                    |
| **[Zona Comentarios](./docs/carrduci-sys-desarrollo/uso-componentes/zona-comentarios-generica.md)**              | Sistema de comentarios                            | 🚧 Pendiente | -                    |
| **[Data List](./docs/carrduci-sys-desarrollo/uso-componentes/data-list.md)**                                     | Listas de datos dinámicas                         | ✅ Completo  | -                    |
| **[Manejo de Mensajes](./docs/carrduci-sys-desarrollo/uso-componentes/manejo-de-mensajes.md)**                   | Sistema de notificaciones                         | ✅ Completo  | 2025-10-06           |
| **[Detalle Genérico Formulario](./docs/carrduci-sys-desarrollo/uso-componentes/detalle-generico-formulario.md)** | Es para mostrar el detalle de cualquier documento | 🚧 Pendiente | -                    |

### 🐳 **Docker**

-   **[Configuración Docker](./docs/docker/)** - Contenedores y despliegue

### 🖥️ **Sistemas**

-   **[Ubuntu Server](./docs/ubuntu-server/)** - Configuración de servidores Ubuntu
-   **[Windows](./docs/windows/)** - Configuración y utilidades Windows
-   **[Visual Studio Code](./docs/visual-studio-code/)** - Configuración del IDE
-   **[ODBC Mongo](./docs/odbc-mongo/)** - Conexiones ODBC con MongoDB

---

## ⚙️ Instalación y Configuración

Para instrucciones completas de instalación y configuración del entorno de desarrollo, consulta:

**[📚 Documentación de Desarrollo CARRDUCI-sys](./docs/carrduci-sys-desarrollo/2-entorno-desarollo.md)** - Entorno completo de desarrollo

**[🔧 Instalación WSL](./docs/carrduci-sys-desarrollo/1-instalacion-wsl.md)** - Configuración del subsistema Linux

---

## 📖 Uso de la Documentación

### 🌐 **Acceso Online**

La documentación está disponible en: **[https://carrduci.github.io/documentacion_sistemas/](https://carrduci.github.io/documentacion_sistemas/)**

### 🖥️ **Servidor Local**

```bash
# Iniciar servidor de desarrollo
cd ~/carrduci-dev/carrduci_sys_workspace/documentacion_sistemas
npm run start
```

### 📝 **Editar Documentación**

#### **Reglas de Nomenclatura**

-   ✅ **Archivos**: `minusculas-con-guiones.md`
-   ✅ **Carpetas**: `minusculas-con-guiones/`
-   ❌ **Espacios**: NO usar espacios en nombres

#### **Sintaxis Markdown**

Se usa **Docsify** con sintaxis Markdown extendida:

-   ✅ **Encabezados jerárquicos**
-   ✅ **Código con resaltado sintáctico**
-   ✅ **Tablas y listas**
-   ✅ **Imágenes y enlaces**
-   ✅ **Separadores de sección** con `#region`

#### **Generar Menú Lateral**

Cada vez que se modifica la estructura de archivos:

```bash
# Generar menú lateral automáticamente
/bin/python3 /home/sistemas/carrduci-dev/carrduci_sys_workspace/documentacion_sistemas/generar_directorio.py
```

---

## 🔄 Subir Cambios

### 📝 **Flujo de Trabajo**

```bash
# 1. Hacer cambios en archivos .md
# 2. Generar menú lateral si cambió la estructura
/bin/python3 ~/carrduci-dev/carrduci_sys_workspace/documentacion_sistemas/generar_directorio.py

# 3. Commit y push
git add .
git commit -m "Descripción de los cambios"
git push -u origin main
```

### 📋 **Convenciones de Commit**

-   ✅ **Commits descriptivos** en español
-   ✅ **Commits atómicos** por funcionalidad
-   ✅ **Referencias a issues** cuando aplique
-   ✅ **Siempre usar [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)**

---

## 🤝 Contribución

### 📚 **Estándares de Documentación**

-   ✅ **Idioma**: Español (México) obligatorio
-   ✅ **Formal pero accesible**: Para desarrolladores
-   ✅ **Términos técnicos**: Explicados en español
-   ✅ **Consistencia**: Seguir patrones establecidos

### 🎯 **Reglas Generales**

-   ✅ **Comentarios arriba** de líneas referenciadas
-   ✅ **Sin acentos** en comentarios de código
-   ✅ **Separadores de sección** obligatorios
-   ✅ **JSDoc** para todas las funciones

### 📖 **Estructura de Archivos**

Todos los archivos van en `/docs` organizados por categorías:

```
docs/
├── carrdduci-sys/           # Sistema CARRDUCI
├── carrdduci-sys-desarrollo/ # Desarrollo y arquitectura
├── docker/                   # Contenedores
├── ubuntu-server/           # Servidores Linux
├── windows/                 # Utilidades Windows
└── visual-studio-code/      # Configuración IDE
```

---

## 📈 Estado del Proyecto

### ✅ **Completado (2025)**

-   🧩 **14 componentes reutilizables** completamente documentados
-   ⚙️ **Entorno de desarrollo** completamente automatizado
-   🐳 **Docker y despliegue** documentado

### 🚧 **En Desarrollo**

-   🏗️ **Component Domain Architecture** - Implementación en progreso
-   📚 **Documentación estandarizada** con JSDoc - En proceso de completación
-   🔧 **9 componentes restantes** por documentar
-   📖 **Documentación de APIs** adicionales
-   🧪 **Guías de testing** avanzado
-   🔄 **Completar migración** de arquitectura legacy

---

## 🙏 Agradecimientos

Esta documentación es el resultado del trabajo colaborativo del **Equipo de Desarrollo CARRDUCI**. Gracias a todos los contribuidores que han hecho posible esta arquitectura modular escalable.

**¡Bienvenido al desarrollo del Sistema CARRDUCI!** 🚀✨
