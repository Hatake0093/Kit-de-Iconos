# Pendientes del kit de iconos

Trabajo por hacer en `Kit_semantico`. Al terminar un punto, muévalo a la sección "Hecho" con la fecha.

## Por hacer

### Iconos que faltan para sustituir los embebidos de FrmMain

Meta: ningún control de `FrmMain` con icono embebido en `FrmMain.resx`. Los 43 que hay en `main`
ya tienen propuesta en `ControlGanaderoSim/propuestas.js`. Queda un control con hueco punteado en el modo «Kit + propuestas».

Diseño nuevo:

- [ ] `temas` — **Temas** (`rgbiSkins`, Ajustes). Paleta de pintor plana con manchas azul, verde, ámbar y rosa del kit y contorno marino.

Al terminar cada uno: cambiar su entrada en `propuestas.js` de `falta` a `icono` y revisarlo en el mockup.

### Revisar el rediseño de la familia `camion-*`

Revisar el rediseño del camión y sus variantes. Hoy son seis archivos: `camion`, `camion-mas`, `camion-flecha`, `camion-lista`, `camion-usuario` y `camion-descarga`.

- [ ] Definir qué se revisa: forma del camión, colores o la insignia de cada variante.
- [x] Aplicar el color por significado a las insignias (`PALETA.md`, sección 4). Hecho el 2026-11-21: `camion-mas` y `camion-descarga` verdes, `camion-flecha` y `camion-lista` azules; `camion-mas` y `camion-flecha` pasan a `generar_faltantes.py`.
- [ ] Revisar los controles que lo usan en `mapa_controles.csv`: `Remisiones` (`camion`), `Reparto` y `Salida a Matadero` (`camion-flecha`), `Lista de Recepcion` (`camion-mas`), `Transportistas` (`camion-usuario`), `Programacion de Salidas` e `Indicadores/Ver Servicios` (`camion-lista`). `camion-descarga` no lo usa ningún control. En el mockup se proponen `camion-descarga` para Remisiones de Entrada (hoy «Lista de Recepcion») y `camion-flecha` para Remisiones de Salida (hoy «Remisiones»).
- [ ] Pasar `python auditar_coherencia.py` y regenerar la vista previa con `python generar_vista_previa.py`.

### Iconos de zoom (`zoom-mas`, `zoom-menos` y lupa única)

Hoy el kit solo tiene `Buscar.svg` y las variantes `*-lupa` (que significan "buscar/consultar", no "acercar"). Faltan iconos de zoom para visores, croquis y vistas previas.

- [ ] Dibujar `zoom-mas.svg`: lupa con **+** (acercar).
- [ ] Dibujar `zoom-menos.svg`: lupa con **−** (alejar).
- [ ] Valorar una **lupa única** (`zoom.svg`, lupa sola) como icono base de la familia, o reutilizar la lupa de `Buscar.svg`; decidir si hace falta distinguirla de "buscar".
- [ ] Mantener el sistema: 32×32, `viewBox="0 0 64 64"`, relleno plano, sin degradados ni trazos finos; el **+** y el **−** como insignia con color por significado (`PALETA.md`, sección 4).
- [ ] Anotar el color base en la tabla de la sección 5 de `PALETA.md`.
- [ ] Registrar la familia en `generar_faltantes.py` (`BASES` + `NUEVOS`) y añadirla a `generar_vista_previa.py` con sus palabras clave (zoom, acercar, alejar, ampliar, lupa).
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

### 2026-11-21 — Propuestas para Implantes y Lista de Equipos

- Asignados `implante` (cartucho con tres cavidades) y `equipo` (cargador frontal) en «Kit + propuestas». Pendiente de validar con los operadores si reconocen las siluetas en sus catálogos.

### 2026-11-21 — Variantes de usuario para Programadores y Dueños

- Generados con `generar_faltantes.py` `usuario-reloj` (insignia morada) para **Programadores** y `usuario-estrella` (insignia ámbar) para **Dueños**.
- Asignados en `ControlGanaderoSim/propuestas.js`. Falta reasignarlos en `FrmMain` del proyecto.

### 2026-10-25 — Propuestas visuales preparadas

- Creados en `Propuetas/` los 10 SVG de `mixer` (base y nueve variantes), interpretado como carro mezclador de alimento y con cuerpo verde.
- Creados los 3 SVG propuestos de `indicador` (base, descarga y carga), con nuevo diseño de pantalla digital.
- Creados los 6 SVG propuestos de `camion`, con caja ganadera ventilada e insignias diferenciadas por función.
- Añadida la lámina `Propuetas/pendientes-vista-previa.svg` y su PNG para comparar los 19 iconos a 64 y 32 px. Criterios de diseño en `Propuetas/pendientes-propuestas.md`.

Esta entrega completa la preparación de propuestas solicitada. La elección definitiva y su incorporación a `Kit_semantico`, generadores, mapa de controles y simulador siguen pendientes en las listas anteriores.

### 2026-10-26 — Camión mixer aprobado e incorporado

- Incorporado `camion-mixer.svg` con la tolva reducida a la altura de la cabina, según la versión aprobada.
- Registrado en el buscador bajo Alimentación y en el simulador, Alimentación → Mezclado → Camión mixer.
- Se conserva el original en `Propuetas/`. Las demás propuestas de mixer, tractor-mixer, indicador y camión mantienen su estado anterior.

### 2026-10-26 — Indicador industrial: propuesta revisada

- Redibujadas en `Propuetas/` las tres variantes de indicador siguiendo la nueva referencia: carcasa metálica inclinada, pantalla amplia, teclado y soporte en U.
- Versiones anteriores conservadas en `Propuetas/Versiones/indicador-anterior/`. La nueva propuesta aún no está incorporada al kit.

### 2026-10-26 — Indicador frontal aprobado y familia completada

- Sustituido el indicador anterior por el frontal aprobado, sin soporte ni entradas de cable.
- Generados 12 iconos: base, arriba, abajo, mas, menos, check, x, lista, lupa, flecha, reloj y alerta.
- Actualizados el generador, la paleta, el buscador y el simulador (Finanzas → Indicadores). Conservadas las asignaciones de cargar alimentación y descargar.
- Respaldo de la familia anterior en `Respaldos/indicador-antes-frontal-2026-10-26/`.
- Comprobadas la equivalencia visual estructural de las tres propuestas aprobadas y la regeneración de la familia. Auditoría completa: 399 de 399 iconos coherentes; vista previa regenerada.

### 2026-10-26 — Familia `camion-mixer-*` y `comedero-arribaYabajo`

- Completada la familia del camión mixer aprobado: 10 variantes con insignia (`mas`, `menos`, `check`, `x`, `lista`, `lupa`, `flecha`, `reloj`, `alerta`, `documento`). Cuerpo de `camion-mixer.svg` reutilizado tal cual, escalado a .78 cuando lleva insignia.
- Nuevos símbolos de insignia `documento` (hoja con dos renglones) y `arribaYabajo` (dos flechas opuestas), ambos en azul por significado (consultar / ajustar).
- Añadido `comedero-arribaYabajo` a la familia `comedero-*`.
- Registrado en `generar_faltantes.py` (`BASES`, `NUEVOS`, `BASES_64`), en la sección Alimentación del buscador (`generar_vista_previa.py`) y en `PALETA.md`.
- Añadida la variante `-reporte` (hoja con línea de tendencia, insignia azul) a 29 familias con `generar_reportes.py`, p. ej. `implantador-reporte`, `camion-mixer-reporte`, `comedero-reporte`. Se omiten `documento` y las sueltas con una sola variante (`mapa`, `lapida`, `moneda`, `botiquin`…).
- Pendiente: llevar los 12 + 29 iconos al simulador (`index.html`, `mapa_controles.csv`) y a `ControlGanadero/Resources` con `sincronizar_resources.py`.
