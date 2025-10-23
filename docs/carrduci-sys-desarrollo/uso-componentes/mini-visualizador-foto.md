# Mini Visualizador Foto

## Descripción

`MiniVisualizadorFotoComponent` renderiza miniaturas interactivas que muestran una imagen individual o una galería completa mediante `VisorDeImagenesService`. Se usa en perfiles de usuario, bitácoras de mantenimiento y módulos de evidencia para ofrecer previsualización rápida sin abandonar la vista actual.

> **Aviso de seguridad:** `ImagenPipe` construye URLs hacia `/img/<carpeta>/<archivo>` que son **públicas**. Esas rutas no exigen sesión ni validan permisos, por lo que cualquier persona con el enlace puede ver la imagen. Evita exponer información sensible o coloca la imagen detrás de proxys/autorización adicional.

## Ubicación de archivos

```
carrduci-sys-gui/src/app/components/utiles/mini-visualizador-foto/
├── mini-visualizador-foto.component.ts
├── mini-visualizador-foto.component.html
├── mini-visualizador-foto.component.css
└── mini-visualizador-foto.module.ts
```

## Dependencias principales

-   `VisorDeImagenesService` (`src/app/services/visorDeImagenes/visor-de-imagenes.service.ts`): controla la vista modal y la navegación entre imágenes.
-   `ImagenPipe` (`src/app/pipes/imagen.pipe.ts`): genera la URL pública con cache busting para cada imagen.
-   `PipesModule`: requerido por `MiniVisualizadorFotoModule` para que el pipe esté disponible en la plantilla.
-   `CARPETAS_IMGS`: enumeración exportada junto al componente para tipar las carpetas soportadas.

## Importación del módulo

```typescript
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MiniVisualizadorFotoModule } from 'src/app/components/utiles/mini-visualizador-foto/mini-visualizador-foto.module';

@NgModule({
    imports: [CommonModule, MiniVisualizadorFotoModule]
})
export class PerfilUsuarioModule {}
```

## API del componente

### Entradas (`@Input`)

| Propiedad                | Tipo                                                             | Requerido | Valor por defecto | Descripción                                                                                             |
| ------------------------ | ---------------------------------------------------------------- | --------- | ----------------- | ------------------------------------------------------------------------------------------------------- |
| `datosImagen`            | `{ nombre: string; carpeta: string; grupoDeNombres?: string[] }` | ✅        | `undefined`       | Define la ruta de la imagen base. `carpeta` debe existir en `VisorDeImagenesService.RUTAS_VALIDAS`.     |
| `imagenSrc`              | `any`                                                            | ❌        | `undefined`       | Permite inyectar una URL ya resuelta (blob, CDN, base64). Si se define, se ignora `datosImagen.nombre`. |
| `mostrarImagenConClick`  | `boolean`                                                        | ❌        | `true`            | Abre automáticamente el visor al hacer click.                                                           |
| `medida`                 | `string`                                                         | ❌        | `'3rem'`          | Tamaño de la miniatura asignado a la variable CSS `--medida`.                                           |
| `margin`                 | `string`                                                         | ❌        | `'.2rem'`         | Margen exterior (`--margin`).                                                                           |
| `borderRadius`           | `string`                                                         | ❌        | `'.6rem'`         | Radio de borde (`@Input('border-radius')`).                                                             |
| `simboloMostrarHover`    | `string`                                                         | ❌        | `undefined`       | Clase FontAwesome que se muestra sobre la imagen al pasar el cursor.                                    |
| `claseContenedorSimbolo` | `string`                                                         | ❌        | `undefined`       | Estilos adicionales para el contenedor del símbolo (ej. `badge badge-light`).                           |
| `claseImagen`            | `string`                                                         | ❌        | `undefined`       | Clases CSS adicionales aplicadas al `<img>`.                                                            |

### Salidas (`@Output`)

| Evento          | Tipo                                                        | Descripción                                                                                         |
| --------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `clickImagen`   | `EventEmitter<{ nombre: string; carpeta: string } \| void>` | Se dispara al hacer click. Emite `void` si se usa `imagenSrc`; de lo contrario envía `datosImagen`. |
| `imagenCargada` | `EventEmitter<void>`                                        | Notifica cuando la miniatura terminó de cargarse (evento `load`).                                   |

## Funcionamiento interno

-   `manejarClick()` verifica `mostrarImagenConClick`; si está activo, abre el visor y luego emite `clickImagen` con el payload adecuado.
-   `mostrarImagen()` delega en `VisorDeImagenesService`. Si se entregó `grupoDeNombres`, transforma cada nombre con `ImagenPipe` y muestra la galería; en otro caso abre una imagen única usando `imagenSrc` o `imagenPipe.transform`.
-   `ImagenPipe` concatena `URL_SERVICIOS` con `/img/<carpeta>/<archivo>` y añade un número aleatorio para evitar cache.

## Consideraciones de seguridad

-   Las rutas `/img/**` en backend son **abiertas**. Cualquier persona con el link puede acceder al archivo sin autenticación.
-   Evita subir archivos con información confidencial a estas carpetas o usa nombres ofuscados y políticas de expiración externas.
-   Limítate a las carpetas definidas en `RUTAS_VALIDAS`; valores no contemplados provocan error y previenen accesos arbitrarios.

## Ejemplos de uso

### Caso básico: miniatura por defecto

```typescript
import { Component } from '@angular/core';
import { CARPETAS_IMGS } from 'src/app/components/utiles/mini-visualizador-foto/mini-visualizador-foto.component';

@Component({
    selector: 'app-ficha-empleado',
    templateUrl: './ficha-empleado.component.html'
})
export class FichaEmpleadoComponent {
    imagenEmpleado = {
        nombre: '656f0b8d-20231018.jpg',
        carpeta: CARPETAS_IMGS.empleados
    };
}
```

```html
<!-- ficha-empleado.component.html -->
<app-mini-visualizador-foto
    [datosImagen]="imagenEmpleado"
></app-mini-visualizador-foto>
```

### Caso intermedio: estilos personalizados y listeners

```typescript
import { Component } from '@angular/core';
import { CARPETAS_IMGS } from 'src/app/components/utiles/mini-visualizador-foto/mini-visualizador-foto.component';

@Component({
    selector: 'app-credencial-empleado',
    templateUrl: './credencial-empleado.component.html'
})
export class CredencialEmpleadoComponent {
    foto = {
        nombre: 'credencial-2025.png',
        carpeta: CARPETAS_IMGS.empleados
    };

    onClickImagen(payload?: { nombre: string; carpeta: string }): void {
        console.log('Click en miniatura', payload);
    }

    onImagenCargada(): void {
        console.log('Miniatura con overlay lista');
    }
}
```

```html
<!-- credencial-empleado.component.html -->
<app-mini-visualizador-foto
    [datosImagen]="foto"
    [medida]="'5rem'"
    [margin]="'0.5rem auto'"
    [borderRadius]="'50%'"
    [simboloMostrarHover]="'fas fa-search-plus'"
    [claseContenedorSimbolo]="'badge badge-light shadow-sm'"
    [claseImagen]="'rounded-circle shadow-lg border border-light'"
    (clickImagen)="onClickImagen($event)"
    (imagenCargada)="onImagenCargada()"
></app-mini-visualizador-foto>
```

### Caso avanzado: galería controlada manualmente

```typescript
import { Component } from '@angular/core';
import { ImagenPipe } from 'src/app/pipes/imagen.pipe';
import { VisorDeImagenesService } from 'src/app/services/visorDeImagenes/visor-de-imagenes.service';
import { CARPETAS_IMGS } from 'src/app/components/utiles/mini-visualizador-foto/mini-visualizador-foto.component';

@Component({
    selector: 'app-reporte-mantenimiento',
    templateUrl: './reporte-mantenimiento.component.html',
    providers: [ImagenPipe]
})
export class ReporteMantenimientoComponent {
    readonly carpeta = CARPETAS_IMGS.evidenciasBitacoraMtto;
    readonly imagenes = [
        'evidencia-01.jpg',
        'evidencia-02.jpg',
        'evidencia-03.jpg'
    ];
    readonly miniaturaTemporal =
        'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD...';

    constructor(
        private readonly visorDeImagenes: VisorDeImagenesService,
        private readonly imagenPipe: ImagenPipe
    ) {}

    abrirGaleria(): void {
        const urls = this.imagenes.map((nombre) =>
            this.imagenPipe.transform(nombre, this.carpeta)
        );
        this.visorDeImagenes.mostrarGrupoDeImagenes(urls);
    }

    manejarCarga(): void {
        console.log('Miniatura temporal disponible para patrones de QA');
    }
}
```

```html
<!-- reporte-mantenimiento.component.html -->
<app-mini-visualizador-foto
    [datosImagen]="{
        nombre: imagenes[0],
        carpeta: carpeta,
        grupoDeNombres: imagenes
    }"
    [imagenSrc]="miniaturaTemporal"
    [mostrarImagenConClick]="true"
    [medida]="'3rem'"
    [borderRadius]="'1rem'"
    [simboloMostrarHover]="'fas fa-external-link-alt'"
    [claseContenedorSimbolo]="'badge bg-primary text-white position-absolute top-0 end-0'"
    [claseImagen]="'shadow'"
></app-mini-visualizador-foto>
```

## Buenas prácticas

-   **Valida** que el archivo exista antes de renderizar el componente para evitar múltiples 404.
-   **Reutiliza** `CARPETAS_IMGS` para prevenir errores tipográficos en `carpeta`.
-   **Desactiva** `mostrarImagenConClick` si necesitas controlar el visor desde afuera y usa `clickImagen` para tu lógica.
-   **Optimiza** el peso de las imágenes en el backend; el componente no las reescala.
-   **Sincroniza** loaders con `imagenCargada` cuando sea crítico saber que la miniatura terminó de cargarse.

## Checklist de integración

-   **Importa** `MiniVisualizadorFotoModule` en el módulo consumidor.
-   **Configura** `datosImagen` con `carpeta` válida y, si corresponde, `grupoDeNombres` para galerías.
-   **Personaliza** estilos (`claseImagen`, `claseContenedorSimbolo`, `borderRadius`, `medida`) para alinear el layout.
-   **Evalúa** el riesgo de compartir URLs abiertas y aplica mitigaciones si se manejan documentos sensibles.
