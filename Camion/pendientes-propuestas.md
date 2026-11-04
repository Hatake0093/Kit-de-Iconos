# Propuestas de pendientes — 2026-10-25

19 SVG de 32 × 32, con `viewBox="0 0 64 64"`, en esta carpeta.

| Familia | Archivos | Diseño propuesto |
|---|---|---|
| `mixer` | Base, `mas`, `menos`, `check`, `x`, `lista`, `lupa`, `flecha`, `reloj`, `alerta` | Carro mezclador de alimento remolcado. Tolva verde `#24AC88`, alimento ámbar y bastidor marino. |
| `indicador` | Base, `abajo`, `arriba` | Indicador industrial revisado según la referencia: vista frontal con carcasa metálica, pantalla azul y teclado numérico; sin soporte ni conectores. |
| `camion` | Base, `mas`, `flecha`, `lista`, `usuario`, `descarga` | Caja ganadera ventilada ámbar, cabina azul y ruedas marinas; parte de la propuesta `camion-ganadero.svg`. |

Insignias: altas y confirmación en verde; bajas y cancelación en rosa; búsqueda, listados y traslados en azul; reloj y transportista en morado; alerta en ámbar. Las flechas de descarga de datos y descarga del camión son azules porque representan transferencia. La carga de alimentación al indicador es verde.

La interpretación de mixer como mezcladora de alimento es una propuesta basada en `pendientes.md`. Estos diseños quedan para revisión visual; la integración en el kit y el simulador corresponde a los puntos que siguen abiertos en ese archivo.

La lámina `pendientes-vista-previa.svg` muestra todos los diseños a 64 y 32 px. Se puede regenerar con `python Propuetas/generar_pendientes.py`, ejecutado desde la raíz del proyecto. Este script escribe únicamente en `Propuetas`.
