# Pendientes del kit de iconos

Trabajo por hacer en `Kit_semantico`. Al terminar un punto, muévalo a la sección "Hecho" con la fecha.

## Por hacer

### Revisar el rediseño de la familia `camion-*`

Revisar el rediseño del camión y sus variantes. Hoy son seis archivos: `camion`, `camion-mas`, `camion-flecha`, `camion-lista`, `camion-usuario` y `camion-descarga`.

- [ ] Definir qué se revisa: forma del camión, colores o la insignia de cada variante.
- [ ] Aplicar el color por significado a las insignias (`PALETA.md`, sección 4). Hoy el camión usa insignia ámbar fija y la sección 5 ya lo deja como pendiente.
- [ ] Revisar los controles que lo usan en `mapa_controles.csv`: `Remisiones` (`camion`), `Reparto` y `Salida a Matadero` (`camion-flecha`), `Lista de Recepcion` (`camion-mas`), `Transportistas` (`camion-usuario`), `Programacion de Salidas` e `Indicadores/Ver Servicios` (`camion-lista`). `camion-descarga` no lo usa ningún control.
- [ ] Pasar `python auditar_coherencia.py` y regenerar la vista previa con `python generar_vista_previa.py`.

## Hecho

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
