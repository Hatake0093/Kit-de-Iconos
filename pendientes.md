# Pendientes del kit de iconos

Trabajo por hacer en `Kit_semantico`. Al terminar un punto, muévalo a la sección "Hecho" con la fecha.

## Por hacer

### Familia `mixer-*`

Crear una familia de iconos de mixer (mezcladora de alimento) con el mismo sistema que las demás.

- [ ] Confirmar el significado: se asume el **mixer de alimento** (carro mezclador de ración para el ganado), que encaja con la sección "Alimentación" de la vista previa.
- [ ] Dibujar el icono base `mixer.svg` (32×32, `viewBox="0 0 64 64"`, relleno plano, sin degradados ni trazos finos).
- [ ] Definir variantes con insignia según el color por significado (`PALETA.md`, sección 4): `mixer-mas`, `mixer-menos`, `mixer-check`, `mixer-x`, `mixer-lista`, `mixer-lupa`, `mixer-flecha`, `mixer-reloj`, `mixer-alerta`.
- [ ] Elegir el color base del cuerpo dentro de la paleta (sección 1) y anotarlo en la tabla de la sección 5 de `PALETA.md`.
- [ ] Registrar la familia en `generar_faltantes.py` (`BASES` + `NUEVOS`).
- [ ] Añadir `mixer` a las familias de la sección "Alimentación" y sus palabras clave en `generar_vista_previa.py`.
- [ ] Pasar `python auditar_coherencia.py` y regenerar la vista previa con `python generar_vista_previa.py`.

### Rediseñar la familia `indicador-*`

Cambiar el diseño del icono `indicador` y sus variantes. Hoy son tres archivos: `indicador`, `indicador-abajo` e `indicador-arriba`.

- [ ] Definir qué se quiere cambiar del diseño actual (forma, colores o ambos) y qué debe transmitir.
- [ ] Redibujar `indicador.svg` y rehacer `indicador-abajo` e `indicador-arriba` a partir de él, con insignia de color por significado (`PALETA.md`, sección 4).
- [ ] Revisar los controles que lo usan en `mapa_controles.csv`: `Indicadores/Descargar` (`indicador-abajo`) e `Indicadores/Cargar Alimentacion` (`indicador-arriba`).
- [ ] Pasar `python auditar_coherencia.py` y regenerar la vista previa con `python generar_vista_previa.py`.

### Revisar el rediseño de la familia `camion-*`

Revisar el rediseño del camión y sus variantes. Hoy son seis archivos: `camion`, `camion-mas`, `camion-flecha`, `camion-lista`, `camion-usuario` y `camion-descarga`.

- [ ] Definir qué se revisa: forma del camión, colores o la insignia de cada variante.
- [ ] Aplicar el color por significado a las insignias (`PALETA.md`, sección 4). Hoy el camión usa insignia ámbar fija y la sección 5 ya lo deja como pendiente.
- [ ] Revisar los controles que lo usan en `mapa_controles.csv`: `Remisiones` (`camion`), `Reparto` y `Salida a Matadero` (`camion-flecha`), `Lista de Recepcion` (`camion-mas`), `Transportistas` (`camion-usuario`), `Programacion de Salidas` e `Indicadores/Ver Servicios` (`camion-lista`). `camion-descarga` no lo usa ningún control.
- [ ] Pasar `python auditar_coherencia.py` y regenerar la vista previa con `python generar_vista_previa.py`.

### Icono `adn` (helicoide de ADN)

Crear un icono de hélice de ADN (doble hélice) con el mismo sistema que las demás.

- [ ] Confirmar para qué se usa (genética / mejoramiento del hato, pruebas de ADN, linaje) y qué control o sección lo necesita.
- [ ] Dibujar `adn.svg` (32×32, `viewBox="0 0 64 64"`, relleno plano, sin degradados ni trazos finos): dos cintas entrelazadas con peldaños.
- [ ] Elegir el color base dentro de la paleta (`PALETA.md`, sección 1) y anotarlo en la tabla de la sección 5.
- [ ] Decidir si lleva variantes con insignia (`adn-mas`, `adn-lupa`, `adn-check`, ...) según el color por significado (sección 4).
- [ ] Registrarlo en `generar_faltantes.py` (`BASES` + `NUEVOS`) y añadirlo con sus palabras clave en `generar_vista_previa.py`.
- [ ] Pasar `python auditar_coherencia.py` y regenerar la vista previa con `python generar_vista_previa.py`.

## Hecho

_(vacío)_
