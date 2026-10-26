# Paleta de colores del kit de iconos

Guía de colores de `Kit_semantico` (iconos 32×32). La paleta base viene del **kit B**; el resto se
deriva de ella o es una excepción declarada. Los valores salen de `generar_faltantes.py` y
`normalizar_colores.py`: si cambia uno, cambie también el script.

## 0. Objetivo y criterio

El kit debe verse como **un solo sistema** y no como una colección de descargas de orígenes distintos.
No exige que todos los iconos usen exactamente los mismos colores: puede haber colores adicionales
(un verde más oscuro para un trazo, un tinte suave para un relleno) siempre que **no se vean
desubicados**. Un color adicional es aceptable si cumple lo siguiente:

- es de la **misma familia de tono** que un color de la paleta (no un magenta ni un cian nuevos);
- tiene un **brillo y una saturación parecidos** (ni neón ni apagado);
- aparece como **detalle o tinte**, no como el color dominante del icono.

Además del color cuentan el **estilo** (relleno plano, sin degradados ni trazos finos con relleno
tenue), el **peso visual** y el **vocabulario de formas** (bordes redondeados, insignia con aro blanco).

`python auditar_coherencia.py` revisa los dos primeros automáticamente: estilo de línea, degradados
y colores a más de 55 unidades RGB de cualquier color del sistema. El peso visual y las formas se
revisan a ojo en la vista previa.

## 1. Paleta base

![Muestras de color](paleta.svg)

| Rol | Hex | Uso |
|---|---|---|
| Azul marino | `#24465B` | Contornos, ruedas, cuencas, detalles oscuros. Es el hilo que une al kit |
| Azul | `#378CE7` | Acciones de consulta y navegación, flechas, gráficas, engranaje, nube |
| Verde | `#24AC88` | Sumar, confirmar, corral, mapa, gráficas |
| Ámbar | `#F3AD43` | Avisos, camión, etiqueta, carpetas |
| Rosa | `#E56876` | Quitar, cancelar, errores, sanidad (cruz) |
| Morado | `#8870D4` | Jeringa y el punto de "círculo" |
| Claro | `#E2F2F5` | Relleno claro (cara de la jeringa, cuerpos de papel) |
| Amarillo arete | `#F7CF3D` | Solo la familia `arete-*` y `arete-rfid-*` (placa amarilla, como la real). Distinto del ámbar a propósito |

### Variantes derivadas

Solo para trazos o detalles que necesitan más contraste sobre fondo blanco.

| Base | Oscuro | Hex |
|---|---|---|
| Verde | verde oscuro | `#1B7F65` |
| Ámbar | ámbar oscuro | `#C98A1B` |
| Rosa | rosa oscuro | `#B94A58` |
| Azul | azul oscuro | `#1F6FC4` (pliegue de `Enviar`) |

## 2. Vaca brahman (firma propia)

Toda la familia `vaca-*` usa esta paleta y **no se normaliza**.

| Parte | Hex |
|---|---|
| Cuerpo, orejas, hocico, insignia por defecto | `#B9472B` |
| Cara | `#F4E1CF` |
| Cuernos | `#8A949E` |
| Hueso (`vaca-calavera`) | `#EDE6D6` |

Los ojos y la nariz son azul marino `#24465B`.

### Cría (ternero)

El ternero se dibuja con los mismos tonos de la vaca pero **aclarados**, para que se distinga de la
madre en `crianza`. Solo se usan en la cría; la madre conserva la tabla de arriba.

| Parte | Hex | Equivale a |
|---|---|---|
| Manchas, orejas y hocico | `#DE9477` | `#B9472B` aclarado |
| Cara | `#FBF1E6` | `#F4E1CF` aclarado |
| Interior de las orejas | `#F19EA8` | `#E56876` aclarado |

`#DE9477` es de la familia del brahman (naranja-terracota), no del rosa `#E56876`, aunque en RGB quede
cerca de él. Los ojos y la nariz siguen en `#24465B`.

## 3. Calendario (excepción)

La base `calendario` es el calendario plano de `flat-color-icons` y **no se normaliza**: su cabecera
roja es parte del icono.

| Parte | Hex |
|---|---|
| Cabecera | `#F44336` |
| Anillas | `#B71C1C` |
| Cuerpo | `#CFD8DC` |
| Pasadores | `#B0BEC5` |
| Cuadrícula | `#90A4AE` |

Sus insignias sí siguen la regla de color por significado (sección 4).

## 4. Insignias: color por significado

Todas las familias con insignia usan el mismo recurso: círculo blanco de radio 6,5 (el aro), círculo de
color de radio 5,5 y símbolo blanco de trazo 1,5, **concéntricos en `(25.5, 25.5)`** de la rejilla de 32
(aro uniforme de 1 px). Antes el aro estaba en `(25, 25)` con radio 7 y quedaba descentrado.

| Color | Significado | Símbolos |
|---|---|---|
| Verde `#24AC88` | Sumar, confirmar, valor | `mas`, `check`, `arriba`, `dolar` |
| Rosa `#E56876` | Quitar, cancelar | `menos`, `x`, `abajo` |
| Ámbar `#F3AD43` | Atención, destacado | `alerta`, `estrella` |
| Azul `#378CE7` | Consultar, navegar | `lupa`, `lista`, `flecha`, `gota` |
| Morado `#8870D4` | Tiempo, historial, marca e identificador | `reloj`, `circulo` |

La regla está en `COLOR_POR_SIMBOLO` de `generar_faltantes.py` y se aplica a las familias listadas en
`COLORES_INSIGNIAS_VACA` (calendario, etiqueta, documento, usuario, barras, comedero, saco, carrito,
lápida, matraz, arete-rfid, BaseDatos…). Excepciones por icono: `arete-rfid-x` (`#B9472B`) y
`GuardarCerrar` (azul, para distinguirla del cuerpo verde). La familia `vaca-*` la tiene en su propia tabla (`COLORES_INSIGNIAS_VACA`).

## 5. Color base de cada familia

| Familia | Color del cuerpo | Insignia |
|---|---|---|
| `vaca-*` | Brahman `#B9472B` | Por significado |
| `calendario-*` | Cabecera `#F44336` | Por significado |
| `etiqueta-*` | Ámbar `#F3AD43` | Por significado |
| `cerca-*` | Azul marino y verde `#24AC88` | Verde |
| `camion-*` | Ámbar `#F3AD43` | Ámbar |
| `bascula-camion-*` | Camión ámbar y cabina marino sobre plataforma azul `#378CE7` | Por significado (`lista` azul) |
| `jeringa-*` | Morado `#8870D4` | Morado |
| `implantador-*` | Rosa `#E56876`, gatillo marino y aguja gris | Por significado |
| `cruz-*` | Rosa `#E56876` | Rosa |
| `engranaje-*` | Azul `#378CE7` | Azul |
| `nube-*` | Azul claro `#9CC6F2` | Azul |
| `mapa`, `mapa-pin` | Verde `#24AC88` | Verde |
| `arete-*`, `arete-rfid-*` | Amarillo `#F7CF3D` + contorno marino, ondas azules | Por significado |
| `documento-*` | Papel `#E2F2F5` con pliegue `#9CC6F2` | Por significado; `-rojo` / `-azul` según el reporte |
| `BaseDatos-*` | Lila `#D1C4E9` (tinte) | Por significado |
| `matraz-*` | Vidrio `#CFE3FA`, líquido morado `#8870D4` | Por significado (`gota` azul) |
| `Guardar`, `GuardarCerrar` | Verde `#24AC88` | Azul en `GuardarCerrar` |
| `Imprimir`, `Enviar` | Azul `#378CE7` | — |

Pendiente: las familias con una sola insignia de color (cerca, camión, jeringa, cruz, engranaje,
nube, mapa) todavía no usan el color por significado.

## 6. Reglas de normalización

`normalizar_colores.py` lleva cualquier SVG nuevo a la paleta. Clasifica cada color por **tono** y
luego por **luminosidad**:

| Tono | Medio → | Oscuro → |
|---|---|---|
| Rojo | `#E56876` | `#B94A58` (luz < 0,50) |
| Naranja y amarillo | `#F3AD43` | `#C98A1B` (luz < 0,45) |
| Verde y turquesa | `#24AC88` | `#1B7F65` (luz < 0,36) |
| Azul e índigo | `#378CE7` | `#24465B` (luz < 0,33 o tono > 228°) |
| Morado | `#8870D4` | `#8870D4` |

No toca: los colores que ya son de la paleta, los grises y blancos, los **tintes claros**
(luminosidad > 0,72), el magenta y los archivos `calendario*` y `vaca*`.

```bash
python normalizar_colores.py            # simula y muestra el resumen
python normalizar_colores.py --aplicar  # copia de seguridad en Respaldos/ y cambios
```

Los grises y pasteles de Material/Icons8 los remapea aparte `normalizar_material.py` (misma sintaxis,
respaldo en `Respaldos/antes_de_normalizar_material`). Su tabla `MAPA` es la referencia de qué color
de origen va a qué color de la paleta.

## 7. Tintes claros

Rellenos suaves de los iconos de línea. Son aceptados, pero **no forman parte de la paleta**.

`#CFE3FA` azul (vidrio del matraz) · `#D3E2F4` azul · `#F6D9D6` rosa · `#F7E3BE` ámbar · `#D6EBDD` verde · `#D1C4E9` lila · `#9CC6F2` azul de la nube

## 8. Excepciones y pendientes

| Tema | Estado |
|---|---|
| Iconos con **degradado** de Fluent | Resuelto: redibujados planos y sin «Fluent» en el nombre |
| Iconos de **estilo de línea** (`escudo-gris`, `medidor`, `moneda-check`, `prohibido`, `regla`) | Resuelto: redibujados planos |
| Magenta y rosa fuerte `#E91E63` de `Importar` | Resuelto: `Importar` usa `#E56876`; los magentas desaparecieron con los degradados |
| **Colores de Material / Icons8** | Resuelto con `normalizar_material.py`: grises oscuros → marino `#24465B`, grises medios → `#8A949E`, pasteles → tintes de la sección 7 (29 iconos) |
| Grises azulados de Material (`#CFD8DC`, `#90A4AE`, `#B0BEC5`) | Se conservan como neutros (los usa la base `calendario`) |

## 9. Cómo añadir un icono nuevo

1. Usar solo colores de la sección 1 (más los tintes de la 7 si hace falta un relleno suave).
2. Si es una variante con insignia, usar el símbolo y el color de la sección 4.
3. Registrar el icono en `generar_faltantes.py` (`BASES` + `NUEVOS`) para que se regenere con el resto; el nombre es por lo que dibuja (`objeto-accion`), sin el nombre del botón.
4. Pasar `python normalizar_colores.py` para detectar colores fuera de paleta.
5. Regenerar la vista previa: `python generar_vista_previa.py`.

## Carnic (excepción)

`carnic.svg` conserva los colores de la referencia aprobada: bovino rojo `#E82126` y tierra verde `#009449`. La familia `carnic*` queda excluida de la normalización de color.
