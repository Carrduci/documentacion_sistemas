# Estructura y organización del repositorio de documentación

Este documento describe cómo está estructurado el repositorio de documentación, sus convenciones y cómo agregar nueva documentación siguiendo los estándares establecidos.

## Stack tecnológico

### Framework de documentación
La documentación utiliza [Docsify](https://docsify.js.org), un generador de sitios de documentación estáticos que renderiza archivos Markdown en tiempo real.

### Características principales
- **Despliegue**: GitHub Pages
- **Edición**: Visual Studio Code + soporte para Obsidian
- **Formato de contenido**: Archivos Markdown (`.md`)
- **Servidor de previsualización**: Node.js con `npx serve`

## Archivos principales y su propósito

| Archivo | Propósito |
|---------|-----------|
| `index.html` | Configuración de Docsify y estilos personalizados (CSS para tablas responsivas, bloques de código, etc.) |
| `_sidebar.md` | **Auto-generado** - Estructura del menú lateral |
| `_coverpage.md` | Contenido de la página de portada |
| `README.md` | Introducción del repositorio e instrucciones de uso |
| `generar_directorio.py` | **CRÍTICO**: Script Python que auto-genera `_sidebar.md` desde la estructura de `docs/` |
| `package.json` | Dependencias de Node y script de inicio |
| `subir_cambios.ps1` | Script PowerShell para hacer commit de cambios |

## Organización de la documentación

### Categorías principales (bajo `/docs/`)

#### 1. `carrduci-sys/`
Documentación de despliegue en producción:
- Generación de certificados
- Despliegue del sistema
- Administración de respaldos
- Configuración del servidor

#### 2. `carrduci-sys-desarrollo/`
Documentación de desarrollo:
- Instalación de WSL
- Configuración del entorno de desarrollo
- Guías de estructura de archivos y código
- **`css/`** - Estándares de CSS (colores, dimensiones)
- **`uso-componentes/`** - Guías de uso de componentes (más de 20 componentes)

#### 3. `docker/`
Guías de uso de Docker

#### 4. `odbc-mongo/`
Documentación del conector BI de MongoDB

#### 5. `ubuntu-server/`
Administración del servidor (SSH, configuración)

#### 6. `visual-studio-code/`
Snippets y configuración de VS Code

#### 7. `windows/`
Procedimientos específicos de Windows

## Convenciones y estándares

### Convenciones de nomenclatura (CRÍTICO)

!> **IMPORTANTE** - Estas reglas son obligatorias para que el sistema funcione correctamente.

- ✅ **Solo letras minúsculas**
- ✅ **Guiones (`-`) en lugar de espacios**
- ✅ **Sin acentos ni caracteres especiales (ñ, á, é, etc.)**

**Ejemplos correctos**:
- `instalacion-wsl.md`
- `uso-componentes/`
- `generacion-certificados.md`

**Ejemplos incorrectos**:
- ❌ `Instalación-WSL.md` (mayúsculas)
- ❌ `uso_componentes/` (guion bajo)
- ❌ `generación-certificados.md` (acento)

### Sistema de numeración de archivos

Los archivos secuenciales usan prefijos numéricos:
```
1-instalacion-wsl.md
2-entorno-desarollo.md
3-estructura-de-archivos-y-codigo.md
```

### Estilo de contenido

#### Encabezados
```markdown
# Título principal (H1)
## Sección principal (H2)
### Subsección (H3)
```

#### Bloques de código
Siempre especificar el lenguaje:

````markdown
```javascript
const ejemplo = 'código JavaScript';
```

```typescript
const ejemplo: string = 'código TypeScript';
```

```bash
npm run start
```
````

#### Referencias cruzadas
Usar el formato de enlaces de Docsify:
```markdown
[texto del enlace](./docs/ruta/archivo.md)
```

#### Anclas de ID
Para enlaces internos en el mismo documento:
```markdown
## Título de sección :id=nombre-ancla

[Ir a la sección](#nombre-ancla)
```

#### Imágenes
Las imágenes se almacenan en `assets/imagenes/` o `assets/gifs/`:
```markdown
![texto alternativo](../../assets/imagenes/nombre-imagen.png)
```

Con caption usando `<figure>`:
```html
<figure>
  <img src="../../assets/imagenes/ejemplo.png" alt="descripción">
  <figcaption>Descripción de la imagen</figcaption>
</figure>
```

#### Elementos personalizados

**Separadores**:
```html
<!-- Separador secundario -->
<hr class='hr-secundario'>

<!-- Separador principal -->
<hr class='hr-principal'>
```

**Clases de texto**:
```html
<span class='text-warning'>Texto de advertencia</span>
<span class='text-danger'>Texto de peligro</span>
<span class='text-success'>Texto de éxito</span>
<span class='text-info'>Texto informativo</span>
```

**Badges**:
```html
<b class="title-badge">Texto del badge</b>
```

### Características especiales de Markdown (Docsify)

**Alertas**:
```markdown
!> Esto es una advertencia importante
```

**Tips**:
```markdown
?> Esto es un consejo útil
```

**Tablas**:
```markdown
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
```

## Flujo de trabajo para agregar documentación

### Proceso paso a paso

#### 1. Crear archivo(s) markdown
Crear los archivos `.md` en el subdirectorio apropiado de `docs/`:
- Seguir las convenciones de nomenclatura (minúsculas, guiones)
- Usar prefijo numérico si es parte de una secuencia
- No incluir acentos ni caracteres especiales

#### 2. Escribir el contenido
Seguir la guía de estilo:
- Usar encabezados apropiados
- Agregar bloques de código con etiquetas de lenguaje
- Incluir referencias cruzadas
- Agregar imágenes a `assets/` si es necesario

#### 3. Generar el sidebar

⚠️ **PASO CRÍTICO** - Este paso es obligatorio:

```bash
/bin/python3 /home/sistemas/carrduci-dev/carrduci_sys_workspace/documentacion_sistemas/generar_directorio.py
```

Este script actualiza automáticamente `_sidebar.md` basándose en la estructura de carpetas.

#### 4. Previsualizar localmente
```bash
cd /home/sistemas/carrduci-dev/carrduci_sys_workspace/documentacion_sistemas
npm run start
```

Esto iniciará un servidor local en `http://localhost:3000` (o el puerto que esté disponible).

#### 5. Hacer commit y push
```bash
git add .
git commit -m "docs: agregar documentación de [tema]"
git push -u origin main
```

Los cambios se desplegarán automáticamente en GitHub Pages.

## Cómo funciona `generar_directorio.py`

Este script de Python:

1. **Escanea** el directorio `docs/` recursivamente
2. **Convierte** nombres de carpetas: `mi-carpeta` → **"Mi Carpeta"** (title case con badge)
3. **Convierte** nombres de archivos: `mi-archivo.md` → **"Mi Archivo"** (title case, sin extensión)
4. **Crea** estructura de lista anidada
5. **Ignora** carpetas específicas: `assets/`, `.obsidian/`, `.vscode/`, etc.
6. **Genera** formato de sidebar de Docsify con badges

### Ejemplo de transformación

**Estructura de archivos**:
```
docs/
  └── mi-categoria/
      ├── 1-introduccion.md
      ├── 2-configuracion.md
      └── subcategoria/
          └── guia-avanzada.md
```

**Resultado en `_sidebar.md`**:
```markdown
- <b class="title-badge">Mi Categoria</b>
  - [1 Introduccion](./docs/mi-categoria/1-introduccion.md)
  - [2 Configuracion](./docs/mi-categoria/2-configuracion.md)
  - <b class="title-badge">Subcategoria</b>
    - [Guia Avanzada](./docs/mi-categoria/subcategoria/guia-avanzada.md)
```

## Estrategias para agregar nueva documentación

### Opción A: Nuevo tema independiente

1. Crear nueva carpeta: `docs/nuevo-tema/`
2. Agregar archivos markdown: `1-intro.md`, `2-configuracion.md`, etc.
3. Ejecutar `generar_directorio.py`
4. Aparecerá como nueva sección en el sidebar con badge

**Ejemplo**:
```bash
mkdir docs/nuevo-tema
touch docs/nuevo-tema/1-introduccion.md
# ... agregar contenido ...
python3 generar_directorio.py
```

### Opción B: Agregar a categoría existente

1. Navegar a carpeta existente (ej: `docs/carrduci-sys-desarrollo/`)
2. Agregar nuevo archivo `.md` siguiendo convenciones de nomenclatura
3. Ejecutar `generar_directorio.py`
4. Aparecerá en la sección existente

**Ejemplo**:
```bash
cd docs/carrduci-sys-desarrollo
touch 6-nueva-guia.md
# ... agregar contenido ...
cd ../..
python3 generar_directorio.py
```

### Opción C: Nueva subsección

1. Crear subcarpeta en categoría existente
2. Agregar archivos markdown dentro
3. Ejecutar `generar_directorio.py`
4. Aparecerá como sección anidada con badge

**Ejemplo**:
```bash
mkdir docs/carrduci-sys-desarrollo/nueva-seccion
touch docs/carrduci-sys-desarrollo/nueva-seccion/guia-1.md
# ... agregar contenido ...
python3 generar_directorio.py
```

## Mejores prácticas

### Antes de hacer commit

- ✅ Siempre ejecutar `generar_directorio.py` antes de hacer commit
- ✅ Probar localmente con `npm run start`
- ✅ Verificar que los enlaces funcionen correctamente
- ✅ Revisar que las imágenes se muestren correctamente

### Al escribir contenido

- ✅ Usar enlaces relativos para referencias cruzadas
- ✅ Seguir el estilo de documentación de temas similares
- ✅ Agregar capturas de pantalla/GIFs a `assets/` para guías visuales
- ✅ Ser consistente con el nivel de detalle
- ✅ Incluir ejemplos de código cuando sea relevante

### Organización de contenido

- ✅ Un tema por archivo
- ✅ Usar archivos numerados para secuencias lógicas
- ✅ Crear subcarpetas cuando haya más de 5 archivos relacionados
- ✅ Mantener nombres de archivo descriptivos pero concisos

## Solución de problemas comunes

### El sidebar no se actualiza

**Problema**: Los nuevos archivos no aparecen en el menú lateral.

**Solución**: Ejecutar `generar_directorio.py` y hacer commit de `_sidebar.md`.

### Enlaces rotos

**Problema**: Los enlaces no funcionan o muestran 404.

**Solución**: 
- Verificar que la ruta sea correcta y relativa
- Asegurarse de usar `./docs/` al inicio de la ruta
- Verificar que el archivo exista y tenga el nombre correcto

### Imágenes no se muestran

**Problema**: Las imágenes aparecen como enlace roto.

**Solución**:
- Verificar que la imagen esté en `assets/imagenes/` o `assets/gifs/`
- Revisar que la ruta relativa sea correcta (`../../assets/imagenes/`)
- Confirmar que el nombre del archivo no tenga espacios

### Caracteres especiales causan errores

**Problema**: Los archivos con acentos o ñ no se procesan correctamente.

**Solución**:
- Renombrar archivos siguiendo las convenciones (solo minúsculas, sin acentos)
- El contenido DENTRO de los archivos sí puede tener acentos y caracteres especiales

## Recursos adicionales

- [Documentación oficial de Docsify](https://docsify.js.org)
- [Guía de Markdown](https://www.markdownguide.org/)
- [Repositorio en GitHub](https://github.com/Carrduci/documentacion_sistemas)
