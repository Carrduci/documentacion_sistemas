# Guía Completa de Valores y Unidades de Dimensiones en CSS

CSS (Cascading Style Sheets) es un lenguaje que se usa para dar estilo a páginas web, como el tamaño, posición, espaciado o diseño de elementos como botones, imágenes o texto. Esta guía explica de manera **ultra detallada**, con ejemplos prácticos para cada concepto, todas las formas de especificar dimensiones (como ancho, alto, márgenes, etc.) y las unidades disponibles. Está pensada para alguien con poca o ninguna experiencia en CSS, asegurando que cada unidad y valor sea explicado individualmente, con un ejemplo claro y un resultado descrito.

---

## 1. Unidades de Longitud

Las unidades de longitud se usan para definir tamaños como el ancho (`width`), alto (`height`), márgenes (`margin`), espacio interno (`padding`), tamaño de fuente (`font-size`), entre otros. Hay dos tipos principales: **absolutas** (tamaños fijos) y **relativas** (dependen de algo, como el tamaño de la fuente o la pantalla).

### 1.1 Unidades Absolutas

Estas unidades tienen un tamaño fijo que no cambia según el contexto. Son útiles cuando necesitas un tamaño exacto, como en diseños impresos.

-   **`px` (píxeles)**: Un píxel es una unidad pequeña, definida como 1/96 de una pulgada en pantallas estándar. Es la unidad más común en diseño web porque es precisa para pantallas.  
    **Ejemplo**: Una caja de 200 píxeles de ancho y 100 píxeles de alto.

    ```css
    .caja {
        width: 200px;
        height: 100px;
        background-color: lightblue;
    }
    ```

    **Resultado**: La caja tiene un ancho fijo de 200 píxeles y un alto de 100 píxeles, sin importar si la ventana del navegador se redimensiona o el dispositivo cambia.

-   **`cm` (centímetros)**: Representa centímetros reales en el mundo físico. Útil para diseños que se imprimen o necesitan medidas absolutas en pantalla calibrada.  
    **Ejemplo**: Un botón de 3 centímetros de ancho con 0.5 centímetros de padding interno.

    ```css
    .boton {
        width: 3cm;
        padding: 0.5cm;
        background-color: coral;
    }
    ```

    **Resultado**: El botón mide exactamente 3 cm de ancho en una pantalla calibrada, con 0.5 cm de espacio interno alrededor del texto o contenido.

-   **`mm` (milímetros)**: Un milímetro es 1/10 de un centímetro, ofreciendo precisión para medidas pequeñas.  
    **Ejemplo**: Un margen de 10 milímetros alrededor de una imagen con un borde sólido.

    ```css
    .imagen {
        margin: 10mm;
        border: 1px solid black;
    }
    ```

    **Resultado**: La imagen tiene 10 mm de espacio exterior en todos los lados, separándola de otros elementos.

-   **`Q` (cuarto de milímetro)**: Un cuarto de milímetro (0.25 mm o 1/40 de cm). Es una unidad muy precisa para detalles finos en diseños de alta resolución.  
    **Ejemplo**: Un borde fino de 2Q de grosor con estilo sólido y color verde.

    ```css
    .borde-fino {
        border-width: 2Q;
        border-style: solid;
        border-color: green;
    }
    ```

    **Resultado**: El borde mide 0.5 mm de grosor (2 \* 0.25 mm), ideal para líneas sutiles.

-   **`in` (pulgadas)**: Una pulgada equivale a 2.54 cm. Común en diseños para impresión donde las medidas imperiales son estándar.  
    **Ejemplo**: Una caja de 2 pulgadas de alto con fondo amarillo.

    ```css
    .caja-alta {
        height: 2in;
        background-color: yellow;
    }
    ```

    **Resultado**: La caja mide exactamente 2 pulgadas de alto en pantalla o impresión.

-   **`pc` (picas)**: Una pica es 1/6 de una pulgada (aproximadamente 4.23 mm) o 12 puntos. Usada tradicionalmente en tipografía impresa.  
    **Ejemplo**: Un texto con tamaño de fuente de 2 picas.

    ```css
    .texto {
        font-size: 2pc;
    }
    ```

    **Resultado**: El texto tiene un tamaño de fuente de 2 picas, equivalente a aproximadamente 24 puntos o 8.46 mm.

-   **`pt` (puntos)**: Un punto es 1/72 de una pulgada (aproximadamente 0.35 mm). Muy usado en tipografía para tamaños de fuente.  
    **Ejemplo**: Un título con 18 puntos de tamaño de fuente.
    ```css
    .titulo {
        font-size: 18pt;
    }
    ```
    **Resultado**: El texto del título mide 18 puntos, que es un tamaño estándar para encabezados en documentos impresos.

### 1.2 Unidades Relativas - Basadas en la Fuente

Estas unidades dependen del tamaño de la fuente del texto, lo que las hace ideales para diseños que se adaptan al texto y mantienen proporciones.

-   **`cap`**: Representa la altura de las letras mayúsculas (como "A" o "B") en la fuente actual del elemento. Útil para alinear elementos con mayúsculas.  
    **Ejemplo**: Una caja con altura igual a dos veces la altura de una mayúscula, con tamaño de fuente de 16px.

    ```css
    .caja-texto {
        font-size: 16px;
        height: 2cap;
        background-color: pink;
    }
    ```

    **Resultado**: La caja tiene una altura equivalente a dos veces la altura de una mayúscula en la fuente de 16px, ajustándose si el tamaño de fuente cambia.

-   **`ch`**: Representa el ancho del carácter "0" (cero) en la fuente actual del elemento. Ideal para diseños con texto monoespaciado o para estimar anchos de texto.  
    **Ejemplo**: Un campo de texto de 10 ceros de ancho, usando una fuente monoespaciada.

    ```css
    .campo-texto {
        font-family: monospace;
        width: 10ch;
        border: 1px solid gray;
    }
    ```

    **Resultado**: El campo tiene el ancho exacto de 10 caracteres "0" en la fuente monoespaciada, útil para formularios.

-   **`em`**: Representa el tamaño de la fuente del elemento actual. Si el elemento tiene `font-size: 16px`, `1em` equivale a 16 píxeles.  
    **Ejemplo**: Un margen de 2 veces el tamaño de fuente de un párrafo con `font-size: 20px`.

    ```css
    .parrafo {
        font-size: 20px;
        margin: 2em;
    }
    ```

    **Resultado**: El párrafo tiene un margen de 40 píxeles (2 \* 20px) en todos los lados, escalando si el tamaño de fuente cambia.

-   **`ex`**: Representa la altura de la letra "x" minúscula en la fuente actual del elemento. Útil para alinear con letras minúsculas.  
    **Ejemplo**: Un ícono con altura igual a la de una "x" minúscula, con tamaño de fuente de 14px.

    ```css
    .icono {
        font-size: 14px;
        height: 1ex;
        background-color: blue;
    }
    ```

    **Resultado**: El ícono tiene la altura de una "x" minúscula en la fuente de 14px, perfecto para alineación baseline.

-   **`ic`**: Representa el ancho del carácter chino "水" (agua) en la fuente actual del elemento. Usado en diseños para idiomas asiáticos como chino, japonés o coreano para consistencia tipográfica.  
    **Ejemplo**: Un contenedor de 5 caracteres "水" de ancho, usando una fuente compatible con CJK.

    ```css
    .contenedor-asiatico {
        font-family: 'Noto Sans CJK JP';
        width: 5ic;
        background-color: lightgreen;
    }
    ```

    **Resultado**: El contenedor tiene el ancho de 5 caracteres "水" en la fuente especificada, asegurando compatibilidad con texto asiático.

-   **`lh`**: Representa la altura de una línea de texto (definida por `line-height`) en el elemento actual. Útil para alinear con líneas de texto.  
    **Ejemplo**: Una caja con altura de 2 líneas, con `line-height: 1.5em`.

    ```css
    .caja-linea {
        line-height: 1.5em;
        height: 2lh;
        background-color: orange;
    }
    ```

    **Resultado**: La caja tiene una altura igual a dos veces la altura de una línea de texto, ajustándose a cambios en `line-height`.

-   **`rcap`**: Representa la altura de las letras mayúsculas en la fuente del elemento raíz (`<html>`). No depende del elemento actual, sino del raíz.  
    **Ejemplo**: Una caja con altura de 3 veces la altura de mayúscula raíz, con raíz en 16px.

    ```css
    html {
        font-size: 16px;
    }
    .caja-raiz {
        height: 3rcap;
        background-color: violet;
    }
    ```

    **Resultado**: La caja tiene una altura basada en la fuente raíz, manteniendo consistencia global.

-   **`rch`**: Representa el ancho del carácter "0" en la fuente del elemento raíz. Útil para anchos consistentes en toda la página.  
    **Ejemplo**: Un contenedor de 15 ceros raíz de ancho.

    ```css
    html {
        font-size: 16px;
    }
    .contenedor-raiz {
        width: 15rch;
        background-color: indigo;
    }
    ```

    **Resultado**: El contenedor tiene el ancho de 15 "0" basado en la fuente raíz, independiente de fuentes locales.

-   **`rem`**: Representa el tamaño de la fuente del elemento raíz. Es la unidad relativa más común para escalabilidad.  
    **Ejemplo**: Un margen de 1.5 veces el tamaño de fuente raíz.

    ```css
    html {
        font-size: 16px;
    }
    .elemento {
        margin: 1.5rem;
    }
    ```

    **Resultado**: El elemento tiene un margen de 24 píxeles (1.5 \* 16px), escalando si se cambia el tamaño raíz.

-   **`rex`**: Representa la altura de la "x" minúscula en la fuente del elemento raíz.  
    **Ejemplo**: Un padding de 2 veces la altura de "x" raíz.

    ```css
    html {
        font-size: 16px;
    }
    .padding-raiz {
        padding: 2rex;
    }
    ```

    **Resultado**: El padding es dos veces la altura de "x" en la fuente raíz, para consistencia global.

-   **`ric`**: Representa el ancho del carácter "水" en la fuente del elemento raíz. Usado para diseños asiáticos globales.  
    **Ejemplo**: Un ancho de 4 "水" raíz.

    ```css
    html {
        font-size: 16px;
    }
    .asiatico-raiz {
        width: 4ric;
        background-color: teal;
    }
    ```

    **Resultado**: El elemento tiene el ancho de 4 "水" basado en la fuente raíz.

-   **`rlh`**: Representa la altura de línea en el elemento raíz.  
    **Ejemplo**: Una altura de 4 líneas raíz.
    ```css
    html {
        font-size: 16px;
        line-height: 1.5;
    }
    .linea-raiz {
        height: 4rlh;
        background-color: maroon;
    }
    ```
    **Resultado**: La altura es 4 veces la altura de línea raíz, para layouts consistentes.

### 1.3 Unidades Relativas - Basadas en el Viewport

El "viewport" es el área visible del navegador. Estas unidades cambian según el tamaño de la ventana, haciendo diseños responsivos.

-   **`vh`**: 1% de la altura del viewport.  
    **Ejemplo**: Una caja que ocupa el 50% de la altura de la pantalla.

    ```css
    .caja-alta {
        height: 50vh;
        background-color: teal;
    }
    ```

    **Resultado**: La caja mide la mitad de la altura de la ventana del navegador, ajustándose al redimensionar.

-   **`vw`**: 1% del ancho del viewport.  
    **Ejemplo**: Un banner que ocupa el 80% del ancho de la pantalla.

    ```css
    .banner {
        width: 80vw;
        background-color: navy;
        color: white;
    }
    ```

    **Resultado**: El banner ocupa el 80% del ancho de la ventana, ideal para diseños móviles.

-   **`vmax`**: 1% del valor más grande entre el ancho y la altura del viewport.  
    **Ejemplo**: Un título con tamaño de fuente del 5% del mayor dimension.

    ```css
    .titulo-grande {
        font-size: 5vmax;
    }
    ```

    **Resultado**: El tamaño del texto es el 5% del ancho o alto de la pantalla, el que sea mayor, para visibilidad en orientaciones diferentes.

-   **`vmin`**: 1% del valor más pequeño entre el ancho y la altura.  
    **Ejemplo**: Un cuadrado del 20% del menor dimension.

    ```css
    .cuadrado {
        width: 20vmin;
        height: 20vmin;
        background-color: red;
    }
    ```

    **Resultado**: El cuadrado mide el 20% de la dimensión más pequeña, manteniéndose cuadrado en cualquier pantalla.

-   **`vb`**: 1% del eje de bloque del viewport (normalmente altura en escritura horizontal, pero adaptable a direcciones de texto).  
    **Ejemplo**: Un contenedor con altura del 30% del eje de bloque.

    ```css
    .contenedor-bloque {
        height: 30vb;
        background-color: purple;
    }
    ```

    **Resultado**: El contenedor mide el 30% de la altura del viewport en modos horizontales.

-   **`vi`**: 1% del eje en línea del viewport (normalmente ancho).  
    **Ejemplo**: Un contenedor con ancho del 40% del eje en línea.

    ```css
    .contenedor-linea {
        width: 40vi;
        background-color: olive;
    }
    ```

    **Resultado**: El contenedor mide el 40% del ancho del viewport.

-   **`svh`**: 1% de la altura del viewport pequeño (excluye barras de herramientas o desplazamiento).  
    **Ejemplo**: Una caja con altura del 100% del viewport pequeño.

    ```css
    .caja-pequena {
        height: 100svh;
        background-color: cyan;
    }
    ```

    **Resultado**: La caja ocupa toda la altura visible, ignorando barras.

-   **`svw`**: 1% del ancho del viewport pequeño.  
    **Ejemplo**: Un elemento con ancho del 90% del viewport pequeño.

    ```css
    .elemento-pequeno {
        width: 90svw;
        background-color: lightpink;
    }
    ```

    **Resultado**: El elemento ocupa el 90% del ancho visible sin barras.

-   **`svi`**: 1% del eje en línea del viewport pequeño.  
    **Ejemplo**: Un contenedor con ancho del 50% del eje en línea pequeño.

    ```css
    .contenedor-svi {
        width: 50svi;
        background-color: lightsalmon;
    }
    ```

    **Resultado**: Similar a svw en horizontal, pero adaptable.

-   **`svb`**: 1% del eje de bloque del viewport pequeño.  
    **Ejemplo**: Una caja con altura del 60% del eje de bloque pequeño.

    ```css
    .caja-svb {
        height: 60svb;
        background-color: lightyellow;
    }
    ```

    **Resultado**: Mide el 60% de la altura visible sin barras.

-   **`svmin`**: 1% del menor dimension del viewport pequeño.  
    **Ejemplo**: Un elemento del 10% del menor dimension pequeño.

    ```css
    .elemento-svmin {
        font-size: 10svmin;
    }
    ```

    **Resultado**: El tamaño es el 10% de la dimensión más pequeña visible.

-   **`svmax`**: 1% del mayor dimension del viewport pequeño.  
    **Ejemplo**: Un fondo del 20% del mayor dimension pequeño.

    ```css
    .fondo-svmax {
        width: 20svmax;
        background-color: lightgray;
    }
    ```

    **Resultado**: Mide el 20% de la dimensión más grande visible.

-   **`lvh`**: 1% de la altura del viewport grande (incluye barras).  
    **Ejemplo**: Una caja con altura del 100% del viewport grande.

    ```css
    .caja-grande {
        height: 100lvh;
        background-color: darkcyan;
    }
    ```

    **Resultado**: La caja ocupa toda la altura, incluyendo barras.

-   **`lvw`**: 1% del ancho del viewport grande.  
    **Ejemplo**: Un elemento con ancho del 100% del viewport grande.

    ```css
    .elemento-grande {
        width: 100lvw;
        background-color: darkblue;
    }
    ```

    **Resultado**: Ocupa todo el ancho, incluyendo barras.

-   **`lvi`**: 1% del eje en línea del viewport grande.  
    **Ejemplo**: Un contenedor con ancho del 70% del eje en línea grande.

    ```css
    .contenedor-lvi {
        width: 70lvi;
        background-color: darkgreen;
    }
    ```

    **Resultado**: Mide el 70% del ancho grande.

-   **`lvb`**: 1% del eje de bloque del viewport grande.  
    **Ejemplo**: Una caja con altura del 80% del eje de bloque grande.

    ```css
    .caja-lvb {
        height: 80lvb;
        background-color: darkred;
    }
    ```

    **Resultado**: Mide el 80% de la altura grande.

-   **`lvmin`**: 1% del menor dimension del viewport grande.  
    **Ejemplo**: Un elemento del 15% del menor dimension grande.

    ```css
    .elemento-lvmin {
        font-size: 15lvmin;
    }
    ```

    **Resultado**: El 15% de la dimensión más pequeña incluyendo barras.

-   **`lvmax`**: 1% del mayor dimension del viewport grande.  
    **Ejemplo**: Un fondo del 25% del mayor dimension grande.

    ```css
    .fondo-lvmax {
        width: 25lvmax;
        background-color: darkviolet;
    }
    ```

    **Resultado**: El 25% de la dimensión más grande incluyendo barras.

-   **`dvh`**: 1% de la altura del viewport dinámico (se ajusta a cambios como barras que aparecen).  
    **Ejemplo**: Una caja con altura del 50% del viewport dinámico.

    ```css
    .caja-dinamica {
        height: 50dvh;
        background-color: magenta;
    }
    ```

    **Resultado**: La caja mide la mitad de la altura, ajustándose dinámicamente.

-   **`dvw`**: 1% del ancho del viewport dinámico.  
    **Ejemplo**: Un banner con ancho del 60% del viewport dinámico.

    ```css
    .banner-dinamico {
        width: 60dvw;
        background-color: brown;
    }
    ```

    **Resultado**: Ocupa el 60% del ancho, ajustándose a cambios.

-   **`dvi`**: 1% del eje en línea del viewport dinámico.  
    **Ejemplo**: Un contenedor con ancho del 45% del eje en línea dinámico.

    ```css
    .contenedor-dvi {
        width: 45dvi;
        background-color: slategray;
    }
    ```

    **Resultado**: Mide el 45% del ancho dinámico.

-   **`dvb`**: 1% del eje de bloque del viewport dinámico.  
    **Ejemplo**: Una caja con altura del 70% del eje de bloque dinámico.

    ```css
    .caja-dvb {
        height: 70dvb;
        background-color: sienna;
    }
    ```

    **Resultado**: Mide el 70% de la altura dinámica.

-   **`dvmin`**: 1% del menor dimension del viewport dinámico.  
    **Ejemplo**: Un elemento del 12% del menor dimension dinámico.

    ```css
    .elemento-dvmin {
        font-size: 12dvmin;
    }
    ```

    **Resultado**: El 12% de la dimensión más pequeña dinámica.

-   **`dvmax`**: 1% del mayor dimension del viewport dinámico.  
    **Ejemplo**: Un fondo del 18% del mayor dimension dinámico.
    ```css
    .fondo-dvmax {
        width: 18dvmax;
        background-color: midnightblue;
    }
    ```
    **Resultado**: El 18% de la dimensión más grande dinámica.

### 1.4 Unidades de Consulta de Contenedor

Estas unidades miden respecto al contenedor padre (no el viewport), usadas en "container queries" para diseños responsivos basados en el tamaño del contenedor.

-   **`cqw`**: 1% del ancho del contenedor padre.  
    **Ejemplo**: Un elemento con 50% del ancho de su contenedor.

    ```css
    .contenedor {
        container-type: inline-size;
    }
    .elemento {
        width: 50cqw;
        background-color: lightcoral;
    }
    ```

    **Resultado**: El elemento mide la mitad del ancho del contenedor padre, ajustándose si el contenedor cambia.

-   **`cqh`**: 1% de la altura del contenedor padre.  
    **Ejemplo**: Un elemento con 75% de la altura del contenedor de 200px.

    ```css
    .contenedor {
        container-type: block-size;
        height: 200px;
    }
    .elemento {
        height: 75cqh;
        background-color: lightseagreen;
    }
    ```

    **Resultado**: El elemento mide 150px (75% de 200px), basado en el contenedor.

-   **`cqi`**: 1% del eje en línea del contenedor (normalmente ancho).  
    **Ejemplo**: Un elemento con 30% del eje en línea del contenedor.

    ```css
    .contenedor {
        container-type: inline-size;
    }
    .elemento {
        width: 30cqi;
        background-color: gold;
    }
    ```

    **Resultado**: El elemento mide el 30% del ancho del contenedor.

-   **`cqb`**: 1% del eje de bloque del contenedor (normalmente altura).  
    **Ejemplo**: Un elemento con 40% del eje de bloque del contenedor de 300px.

    ```css
    .contenedor {
        container-type: block-size;
        height: 300px;
    }
    .elemento {
        height: 40cqb;
        background-color: darkblue;
    }
    ```

    **Resultado**: El elemento mide 120px (40% de 300px).

-   **`cqmin`**: 1% de la dimensión más pequeña del contenedor (ancho o altura).  
    **Ejemplo**: Un cuadrado del 50% de la dimensión menor en un contenedor de 400px ancho y 200px alto.

    ```css
    .contenedor {
        container-type: size;
        width: 400px;
        height: 200px;
    }
    .cuadrado {
        width: 50cqmin;
        height: 50cqmin;
        background-color: salmon;
    }
    ```

    **Resultado**: El cuadrado mide 100px (50% de 200px, la menor).

-   **`cqmax`**: 1% de la dimensión más grande del contenedor.  
    **Ejemplo**: Un elemento del 25% de la dimensión mayor en un contenedor de 400px ancho y 200px alto.

    ```css
    .contenedor {
        container-type: size;
        width: 400px;
        height: 200px;
    }
    .elemento {
        width: 25cqmax;
        background-color: darkgreen;
    }
    ```

    **Resultado**: El elemento mide 100px (25% de 400px, la mayor).

-   **`fr`**: Fracción flexible, usada exclusivamente en CSS Grid para dividir el espacio disponible en fracciones. No es una unidad de longitud general, sino específica para tracks en grid.  
    **Ejemplo**: Dos columnas en grid, una con 1fr (1/3) y otra con 2fr (2/3).
    ```css
    .grid {
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 10px;
    }
    .columna1,
    .columna2 {
        background-color: lightgray;
    }
    ```
    **Resultado**: La primera columna ocupa 1/3 del espacio disponible después de gaps, la segunda 2/3, ajustándose al contenedor.

---

## 2. Valores de Dimensión

Además de unidades, puedes usar valores especiales para definir tamaños de elementos como `width`, `height`, `min-width`, etc.

-   **`<length>`**: Cualquier unidad de longitud mencionada arriba (como px, cm, em, vw). Representa un valor fijo o relativo directo.  
    **Ejemplo**: Un contenedor con ancho de 300 píxeles y fondo beige.

    ```css
    .contenedor {
        width: 300px;
        background-color: beige;
    }
    ```

    **Resultado**: El contenedor tiene un ancho fijo de 300 píxeles, independientemente del contenido.

-   **`<percentage>`**: Un porcentaje (%) del tamaño del contenedor padre. Ideal para diseños responsivos.  
    **Ejemplo**: Una imagen que ocupa el 50% del ancho de un contenedor de 500px.

    ```css
    .contenedor {
        width: 500px;
    }
    .imagen {
        width: 50%;
    }
    ```

    **Resultado**: La imagen mide 250 píxeles (50% de 500px), escalando si el contenedor cambia.

-   **`auto`**: El navegador calcula automáticamente el tamaño basado en el contexto, como contenido o espacio disponible. Común para centrar elementos.  
    **Ejemplo**: Un contenedor centrado con márgenes automáticos left y right.

    ```css
    .contenedor {
        width: 200px;
        margin-left: auto;
        margin-right: auto;
        background-color: skyblue;
    }
    ```

    **Resultado**: El contenedor se centra horizontalmente en su padre, con ancho fijo de 200px.

-   **`max-content`**: El elemento usa el tamaño máximo que necesita su contenido sin restricciones (como el ancho de la línea más larga).  
    **Ejemplo**: Un botón que se ajusta al ancho máximo de su texto.

    ```css
    .boton {
        width: max-content;
        background-color: tomato;
        padding: 10px;
    }
    ```

    **Resultado**: El botón tiene el ancho exacto del texto más largo más el padding, sin envolver líneas innecesariamente.

-   **`min-content`**: El elemento usa el tamaño mínimo posible (como el ancho de la palabra más larga sin romper).  
    **Ejemplo**: Una caja con ancho mínimo basado en contenido.

    ```css
    .caja {
        width: min-content;
        background-color: lavender;
    }
    ```

    **Resultado**: La caja es tan ancha como la palabra o elemento más ancho en su contenido, minimizando el espacio.

-   **`fit-content`**: Ajusta el tamaño al contenido disponible, comportándose como `max-content` si hay espacio, o envolviendo si no.  
    **Ejemplo**: Un contenedor que se ajusta a su contenido sin exceder el padre.

    ```css
    .contenedor {
        width: fit-content;
        background-color: peachpuff;
        padding: 10px;
    }
    ```

    **Resultado**: El contenedor se ajusta al ancho de su contenido, pero respeta los límites del elemento padre.

-   **`fit-content(<length-percentage>)`**: Como `fit-content`, pero con un límite máximo especificado en longitud o porcentaje.  
    **Ejemplo**: Un contenedor que se ajusta al contenido pero no excede 200px.

    ```css
    .contenedor {
        width: fit-content(200px);
        background-color: aquamarine;
    }
    ```

    **Resultado**: El contenedor se ajusta al contenido si es menor a 200px, o se limita a 200px si es mayor.

-   **`stretch`**: El elemento se estira para llenar todo el espacio disponible en su contenedor, común en flexbox o grid.  
    **Ejemplo**: Una caja en flexbox que estira para llenar el ancho.
    ```css
    .contenedor {
        display: flex;
    }
    .caja {
        width: stretch;
        background-color: indigo;
    }
    ```
    **Resultado**: La caja ocupa todo el ancho disponible en el contenedor flex, ignorando su contenido natural.

---

## 3. Palabras Clave Globales

Estas palabras clave se usan para controlar la herencia o reset de valores en propiedades CSS, aplicables a dimensiones y otros estilos.

-   **`inherit`**: El elemento usa exactamente el valor calculado de la propiedad en su elemento padre.  
    **Ejemplo**: Un hijo que hereda el tamaño de fuente del padre.

    ```css
    .padre {
        font-size: 20px;
    }
    .hijo {
        font-size: inherit;
    }
    ```

    **Resultado**: El texto del hijo tiene 20 píxeles, copiando directamente del padre.

-   **`initial`**: Resetea la propiedad al valor inicial por defecto definido en la especificación CSS.  
    **Ejemplo**: Un contenedor con ancho inicial (equivalente a `auto` para width).

    ```css
    .contenedor {
        width: initial;
        background-color: silver;
    }
    ```

    **Resultado**: El contenedor usa el ancho por defecto del navegador, como si no se hubiera definido.

-   **`revert`**: Revierte la propiedad al valor que tendría si no se hubiera aplicado ningún estilo del autor, usando el del user-agent (navegador).  
    **Ejemplo**: Un botón con margen revertido al default del navegador.

    ```css
    .boton {
        margin: revert;
    }
    ```

    **Resultado**: El botón usa los márgenes predeterminados del navegador, ignorando estilos personalizados.

-   **`revert-layer`**: Revierte la propiedad al valor de la capa de cascada anterior, útil en sistemas con @layer para modular estilos.  
    **Ejemplo**: Revertir un ancho en una capa custom a la base.

    ```css
    @layer base {
        .caja {
            width: 100px;
        }
    }
    @layer custom {
        .caja {
            width: revert-layer;
        }
    }
    ```

    **Resultado**: La caja usa el ancho de 100px de la capa base, ignorando cambios en custom.

-   **`unset`**: Si la propiedad es heredable, usa `inherit`; si no, usa `initial`.  
    **Ejemplo**: Un hijo con tamaño de fuente unset, heredando del padre.
    ```css
    .padre {
        font-size: 18px;
    }
    .hijo {
        font-size: unset;
    }
    ```
    **Resultado**: El hijo hereda los 18px del padre, ya que font-size es heredable.

---

## 4. Funciones

Las funciones permiten cálculos dinámicos o comportamientos especiales en valores de dimensiones.

-   **`calc()`**: Permite expresiones matemáticas con unidades mixtas, como sumas, restas, multiplicaciones o divisiones.  
    **Ejemplo**: Un contenedor con ancho del 100% menos 50 píxeles.

    ```css
    .contenedor {
        width: calc(100% - 50px);
        background-color: khaki;
    }
    ```

    **Resultado**: El contenedor ocupa todo el ancho del padre menos 50 píxeles fijos.

-   **`minmax()`**: Define un rango mínimo y máximo para tamaños, comúnmente en grid-template-columns/rows.  
    **Ejemplo**: Una columna en grid con mínimo 100px y máximo 1fr (fracción flexible).

    ```css
    .grid {
        display: grid;
        grid-template-columns: minmax(100px, 1fr);
    }
    .columna {
        background-color: orchid;
    }
    ```

    **Resultado**: La columna tiene al menos 100 píxeles, pero se expande para llenar el espacio disponible como 1fr.

-   **`anchor-size()`**: Define tamaños basados en el tamaño de un elemento ancla (anchor), una función nueva para posicionamiento anclado (soporte limitado en navegadores).  
    **Ejemplo**: Un elemento con ancho igual al ancho de su ancla.

    ```css
    .ancla {
        width: 200px;
    }
    .elemento {
        width: anchor-size(width);
        background-color: maroon;
    }
    ```

    **Resultado**: El elemento tiene el mismo ancho que la ancla (200px), útil para overlays.

-   **`fit-content()`**: Similar al valor `fit-content`, pero como función permite argumentos. Ajusta al contenido con límite.  
    **Ejemplo**: Un contenedor que se ajusta al contenido hasta un máximo de 300px.
    ```css
    .contenedor {
        width: fit-content(300px);
        background-color: turquoise;
    }
    ```
    **Resultado**: El contenedor se ajusta al contenido si es menor, o se limita a 300px si es mayor.

---

## Ejemplo Completo de Página Web

Aquí un ejemplo HTML/CSS completo que usa varias unidades y valores para demostrar en práctica.

```html
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Ejemplo CSS Dimensiones</title>
        <style>
            html {
                font-size: 16px;
                line-height: 1.5;
            }
            body {
                margin: 0;
                padding: 1rem;
            }
            .contenedor {
                width: 80vw;
                height: 50vh;
                background-color: lightgray;
                padding: 1rem;
                margin: 10px auto;
                display: grid;
                grid-template-columns: 1fr minmax(100px, 2fr);
                gap: 10px;
            }
            .elemento1 {
                width: 50%;
                height: 2lh;
                background-color: coral;
                font-size: 1.2rem;
            }
            .elemento2 {
                width: fit-content(200px);
                background-color: skyblue;
                margin: auto;
            }
            .texto {
                font-size: 18pt;
                margin: 2em;
            }
        </style>
    </head>
    <body>
        <div class="contenedor">
            <div class="elemento1">Elemento 1 con 50% ancho y 2lh alto</div>
            <div class="elemento2">Elemento 2 fit-content limitado a 200px</div>
        </div>
        <p class="texto">Texto con 18pt y margen 2em</p>
    </body>
</html>
```

**Resultado**: Una página con un contenedor responsivo (80vw ancho, 50vh alto) que contiene dos elementos en grid. Elemento1 ocupa 50% de su track con alto basado en líneas. Elemento2 se ajusta a su texto hasta 200px. Un párrafo con tamaño impreso y margen relativo.

---

## Resumen Conciso de Todas las Unidades

Aquí un listado rápido de todas las unidades para referencia:

-   **Absolutas**: px (píxeles), cm (centímetros), mm (milímetros), Q (cuarto mm), in (pulgadas), pc (picas), pt (puntos).
-   **Relativas - Fuente**: cap (altura mayúscula), ch (ancho "0"), em (tamaño fuente elemento), ex (altura "x"), ic (ancho "水"), lh (altura línea), rcap (raíz cap), rch (raíz ch), rem (raíz em), rex (raíz ex), ric (raíz ic), rlh (raíz lh).
-   **Relativas - Viewport**: vh (1% altura), vw (1% ancho), vmax (1% mayor), vmin (1% menor), vb (1% bloque), vi (1% línea), svh/svw/svi/svb/svmin/svmax (viewport pequeño), lvh/lvw/lvi/lvb/lvmin/lvmax (viewport grande), dvh/dvw/dvi/dvb/dvmin/dvmax (viewport dinámico).
-   **Consulta Contenedor**: cqw (1% ancho contenedor), cqh (1% altura), cqi (1% línea), cqb (1% bloque), cqmin (1% menor), cqmax (1% mayor).
-   **Otras**: fr (fracción grid).

---

## Recursos para Consultar Más Información

-   [MDN Web Docs - Valores y Unidades CSS (en español)](https://developer.mozilla.org/es/docs/Learn_web_development/Core/Styling_basics/Values_and_units): Guía interactiva con ejemplos y soporte de navegadores.
-   [W3C CSS Values and Units Module Level 4](https://www.w3.org/TR/css-values-4/): Especificación oficial detallada (en inglés).
-   [CSS-Tricks - A Complete Guide to CSS Units](https://css-tricks.com/the-lengths-of-css/): Artículo práctico con visuales (en inglés).
-   [Can I Use - CSS Units](https://caniuse.com/?search=css%20units): Ver compatibilidad en navegadores para unidades específicas.
