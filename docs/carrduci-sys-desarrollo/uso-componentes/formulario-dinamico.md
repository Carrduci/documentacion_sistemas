# Formulario dinámico

EL formulario dinámico es una forma compacta de generar un formulario reactivo de ángular.

Para empezar, importarlo en el módulo del componente que se está trabajando.

```ts
@NgModule({
    declarations: [TalComponenteComponent],
    imports: [
        CommonModule,

        // Importación del módulo.
        FormularioDinamicoModule
    ],
    exports: [TalComponenteComponent],
    providers: [TalComponenteComponent]
})
export class TalComponenteModule {}
```

Para definir un formulario con este componente de la forma más sencilla, hay que crear un objeto. Opcionalmente se podrá usar una función para revisir el resultado del `submit` o `envío` del formulario.

En la vista (`.html`) del componente, se llama al componente de la siguiente forma.

```html
<app-formulario-dinamico
    [especificacionFormulario]="especificacionFormulario"
    (onSubmit)="onSubmit($event)"
></app-formulario-dinamico>
```

En el controlador (`.ts`) haríamos los siguiente.

```ts
import { Component, OnInit } from '@angular/core';
import {
    CampoFormulario,
    EspecificacionFormularioDinamico
} from 'src/app/components/utiles/formulario-dinamico/formulario-dinamico.model';

@Component({
    selector: 'app-tal-componente',
    templateUrl: './tal-componente.component.html',
    styleUrls: ['./tal-componente.component.css']
})
export class TalComponente implements OnInit {
    constructor(formBuilder: FormBuilder) {}

    ngOnInit() {
        this.crearFormulario();
    }

    especificacionFormulario!: EspecificacionFormularioDinamico<
        ReturnType<typeof this.camposFormulario>
    >;

    camposFormulario = () => {
        return {
            nombre: new CampoFormulario({
                tipo: 'text',
                label: 'Nombre',
                claseColumna: 'col-12',
                orden: 0
            }),
            descripcion: new CampoFormulario({
                tipo: 'text',
                label: 'Descripción',
                claseColumna: 'col-12',
                orden: 0
            })
        };
    };

    crearFormulario() {
        this.especificacionFormulario = new EspecificacionFormularioDinamico(
            this.camposFormulario(),
            false,
            true,
            true,
            true
        );
    }

    onSubmit(formulario: any) {
        // Lógica para procesar el formulario
    }
}
```

Lo cuál resulta en algo como lo siguiente.

![](../../../assets/imagenes/componentes__form_dinamico_basico.png)

Esta es una explicación de los atributos del componente.

Y esta de las propiedades generales de un `CampoFormulario`.

---

# Tipos de campo

## Componente

### Clase especial

## Checkbox

## Arreglo de checkbox

### Clase especial

## Radio (tipo de checkbox)

### Clase especial

## Color

## Fecha

## Fecha y hora (`datetime-local`)

## Mes

## Semana

## Hora

## Rango Fechas

### Clase especial

## Número

## Rango

## Texto

### Clase especial

## Área de texto

## Seleccionable

### Clase especial

## Datalist (no confundir con el de `Texto`)

### Clase especial

## Archivo de excel (como JSON)

### Clase especial

## Imágenes

### Clase especial
