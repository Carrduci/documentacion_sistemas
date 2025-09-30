# Personalización avanzada del sistema de documentación

Esta guía describe características avanzadas y opciones de personalización del sistema de documentación basado en Docsify.

## Configuración de Docsify

La configuración principal se encuentra en `index.html` dentro del objeto `window.$docsify`.

### Opciones actuales

```javascript
window.$docsify = {
    loadNavbar: true,
    repo: 'Carrduci/documentacion_sistemas',
    coverpage: '_coverpage.md',
    loadSidebar: '_sidebar.md',
    maxLevel: 6,              // Niveles máximos de encabezados
    subMaxLevel: 6,           // Subniveles en el sidebar
    name: 'Docs Sistemas Carrduci',
    auto2top: true,           // Scroll automático al inicio
    search: {                 // Configuración del buscador
        localSearch: true,
        placeholder: 'Buscar...',
        noData: 'No se encontró nada',
        depth: 6,
        hideOtherSidebarContent: true,
        paths: 'auto'
    },
    tabs: {                   // Soporte para tabs
        persist: true,
        sync: true,
        theme: 'classic',
        tabComments: true,
        tabHeadings: true
    }
};
```

## Personalización de estilos

### Estilos personalizados actuales

El archivo `index.html` incluye CSS personalizado para:

#### 1. Badges de títulos
```css
.title-badge {
    color: rgb(0, 116, 217);
    padding-left: 3px;
    padding-right: 3px;
    padding-top: 1px;
    padding-bottom: 1px;
    font-weight: 900;
}
```

#### 2. Separadores personalizados
```css
hr.hr-secundario {
    border-bottom: dashed 0.5px rgb(180 180 180);
    margin-top: 50px;
    margin-bottom: 50px;
    border-top: none;
}

hr.hr-principal {
    border-bottom: dashed 1px rgb(80, 80, 80);
    margin-top: 80px;
    margin-bottom: 50px;
    border-top: none;
}
```

#### 3. Figuras con caption
```css
figure {
    width: fit-content;
    align-items: center;
    border: solid 1px rgb(180 180 180);
    padding: 0px;
}

figcaption {
    padding: 8px;
    border-top: solid 1px rgb(180 180 180);
}
```

#### 4. Clases de texto
```css
.text-warning {
    color: orange !important;
    font-weight: 900 !important;
}

.text-danger {
    color: red !important;
    font-weight: 900 !important;
}

.text-success {
    color: green !important;
    font-weight: 900 !important;
}

.text-info {
    color: cadetblue !important;
    font-weight: 900 !important;
}
```

### Tablas responsivas

El sistema incluye JavaScript personalizado que convierte tablas en cards en dispositivos móviles:

```javascript
const HACER_TABLAS_DE_MOVIL = () => {
    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
        const rows = table.querySelectorAll('tr');
        const headers = Array.from(rows[0].querySelectorAll('th'))
            .map(th => th.textContent);

        if (window.innerWidth <= 768) {
            // Convierte filas en cards
            // ...
        }
    });
}
```

## Plugins de Docsify instalados

### 1. Búsqueda local
```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
```

Permite búsqueda en todo el contenido sin necesidad de servidor.

### 2. Zoom de imágenes
```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/zoom-image.min.js"></script>
```

Las imágenes se pueden hacer zoom al hacer clic.

### 3. Paginación
```html
<script src="//cdn.jsdelivr.net/npm/docsify-pagination/dist/docsify-pagination.min.js"></script>
```

Navegación anterior/siguiente al final de cada página.

### 4. Sidebar colapsable
```html
<link href="https://cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/sidebar.min.css" rel="stylesheet"/>
<script src="https://cdn.jsdelivr.net/npm/docsify-sidebar-collapse/dist/docsify-sidebar-collapse.min.js"></script>
```

Permite colapsar secciones del sidebar.

### 5. Resaltado de sintaxis (Prism)
Soporta múltiples lenguajes:
- Bash
- Docker
- Git
- TypeScript
- Python
- JSON

Con características adicionales:
- Mostrar lenguaje en el bloque de código
- Copiar al portapapeles
- Barra de herramientas en bloques de código

## Agregar nuevo lenguaje de programación

Para agregar soporte de sintaxis para un nuevo lenguaje:

1. Buscar el componente en [Prism CDN](https://cdn.jsdelivr.net/npm/prismjs@1/components/)
2. Agregar el script en `index.html`:

```html
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-[lenguaje].min.js"></script>
```

**Ejemplo para agregar PHP**:
```html
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-php.min.js"></script>
```

## Modificar el script generador de sidebar

El archivo `generar_directorio.py` puede modificarse para cambiar cómo se genera el sidebar.

### Estructura actual

```python
def tree(dir_path: Path):
    contents = sorted(dir_path.iterdir(), key=lambda x: x.name)
    pointers = [tee] * (len(contents) - 1) + [last]
    
    for pointer, path in zip(pointers, contents):
        # Ignorar ciertos archivos/carpetas
        if path.name not in ['assets', 'generar_directorio.py', ...]:
            # Procesar directorios
            if path.is_dir():
                folder_name = ' '.join(path.name.split('-')).title()
                # ...
            # Procesar archivos
            else:
                file_name = ' '.join(path.name.split('-')).split('.')[0].title()
                # ...
```

### Agregar carpetas a ignorar

Modificar la lista de exclusión:

```python
if path.name not in [
    'assets',
    'generar_directorio.py',
    '.obsidian',
    'nueva-carpeta-a-ignorar',  # Agregar aquí
    # ...
]:
```

### Cambiar formato de nombres

Para cambiar cómo se formatean los nombres (por ejemplo, usar UPPERCASE en lugar de Title Case):

```python
# Para carpetas
folder_name = ' '.join(path.name.split('-')).upper()

# Para archivos
file_name = ' '.join(path.name.split('-')).split('.')[0].upper()
```

## Personalizar la portada

El archivo `_coverpage.md` controla el contenido de la página de inicio:

```markdown
# CARRDUCI
# Documentación de Sistemas

> Procesos de desarrollo

- Despliegue de CARRDUCIsys
- Guías de desarrollo

[Comenzar](./README) | [GitHub](https://github.com/Carrduci/documentacion_sistemas)
```

### Agregar logo

```markdown
![logo](assets/imagenes/logo.png)

# CARRDUCI
# Documentación de Sistemas
```

### Cambiar color de fondo

Agregar en `index.html`:

```css
.cover {
    background: linear-gradient(to bottom, #1e3a8a, #3b82f6) !important;
}
```

## Agregar nuevo plugin de Docsify

1. Buscar el plugin en [Awesome Docsify](https://docsify.js.org/#/awesome)
2. Agregar el CDN en `index.html`
3. Configurar si es necesario en `window.$docsify`

**Ejemplo: Agregar plugin de emojis**:

```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/emoji.min.js"></script>
```

## Temas de Docsify

Para cambiar el tema, modificar el enlace CSS en `index.html`:

### Temas disponibles
```html
<!-- Vue (actual: buble) -->
<link href="//cdn.jsdelivr.net/npm/docsify/themes/vue.css" rel="stylesheet"/>

<!-- Dark -->
<link href="//cdn.jsdelivr.net/npm/docsify/themes/dark.css" rel="stylesheet"/>

<!-- Buble -->
<link href="//cdn.jsdelivr.net/npm/docsify/themes/buble.css" rel="stylesheet"/>

<!-- Pure -->
<link href="//cdn.jsdelivr.net/npm/docsify/themes/pure.css" rel="stylesheet"/>
```

## Integración con Obsidian

El repositorio incluye configuración para Obsidian (`.obsidian/app.json`):

```json
{
  "alwaysUpdateLinks": true
}
```

Esto permite:
- Editar documentación en Obsidian
- Actualización automática de enlaces al renombrar archivos
- Vista previa enriquecida de Markdown

### Configurar Obsidian

1. Abrir Obsidian
2. "Open folder as vault"
3. Seleccionar la carpeta `documentacion_sistemas`
4. Trabajar con vista previa y editor lado a lado

## Configuración de GitHub Pages

Para desplegar en GitHub Pages:

1. Ir a Settings → Pages en el repositorio
2. Source: Deploy from a branch
3. Branch: `main` / `(root)`
4. El archivo `.nojekyll` evita que GitHub intente procesar con Jekyll

## Variables de entorno para desarrollo

Crear `.env` en la raíz (no hacer commit):

```bash
PORT=3000
HOST=localhost
```

Modificar `package.json`:

```json
{
  "scripts": {
    "start": "bash -i -c 'nvm use lts/*' && npx serve -p $PORT"
  }
}
```

## Consejos de rendimiento

### Optimizar imágenes

Antes de agregar imágenes a `assets/`:

```bash
# Instalar imagemagick
sudo apt install imagemagick

# Optimizar imagen
convert imagen.png -quality 85 -resize 1200x imagen-optimizada.png
```

### Lazy loading de imágenes

Agregar en `index.html`:

```javascript
window.$docsify = {
    // ...
    plugins: [
        function(hook, vm) {
            hook.doneEach(function() {
                document.querySelectorAll('img').forEach(img => {
                    img.loading = 'lazy';
                });
            });
        }
    ]
};
```

## Mantenimiento

### Actualizar dependencias

Revisar periódicamente las versiones de CDN en `index.html` para actualizaciones de seguridad.

### Limpieza de archivos huérfanos

Buscar archivos `.md` que no están referenciados:

```bash
# Listar todos los archivos .md
find docs -name "*.md" > archivos.txt

# Buscar enlaces en _sidebar.md
grep -o "docs/[^)]*\.md" _sidebar.md > referenciados.txt

# Comparar
comm -23 <(sort archivos.txt) <(sort referenciados.txt)
```

### Validar enlaces

Usar herramientas como `markdown-link-check`:

```bash
npm install -g markdown-link-check
find docs -name "*.md" -exec markdown-link-check {} \;
```

## Recursos adicionales

- [Documentación de Docsify](https://docsify.js.org)
- [Lista de plugins de Docsify](https://docsify.js.org/#/awesome)
- [Prism - Temas y lenguajes](https://prismjs.com/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
