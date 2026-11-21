# Kit de Iconos – Control Ganadero

Espacio de trabajo donde se genera, normaliza y prueba el kit de iconos **antes** de llevarlo a la versión oficial de ControlGanadero.

## Carpeta principal: `simulador de control ganadero/`

Es lo único que se entrega/prueba; todo lo demás de este directorio es herramienta de producción.

| Elemento | Qué es |
|---|---|
| `index.html` | Mockup del simulador (HTML autocontenido, tema claro/oscuro). Carga los iconos desde `Kit_semantico/svg/`. |
| `Kit_semantico/svg/` | Kit de iconos 32×32 en SVG (≈400 archivos, 21 familias): iconos base y variantes con insignia (`-mas`, `-menos`, `-check`, `-x`, `-lista`, `-lupa`, `-flecha`, `-alerta`, `-reloj`, …). |
| `Kit_semantico/mapa_controles.csv` | Mapa `control → texto del botón → icono → origen_kit` (108 controles; origen **A** = 43, **B** = 65). |
| `Kit_semantico/vista_previa.html` | Hoja de contacto del kit, agrupada por familia de nombre. |
| `Kit_semantico/*.png` | Imágenes de prueba (`vacas_colores.png`, `gota-agua-preview.png`). |

Para ver el mockup basta abrir `simulador de control ganadero/index.html` en el navegador.

## Mockup del sistema real: `ControlGanaderoSim/`

Réplica en HTML del ribbon de ControlGanadero para ver las correcciones del kit sin compilar para Windows.
`generar_sim.py` lee `FrmMain.designer.vb`, `FrmMain.resx` y `Resources/` de una rama del proyecto
(con `git show`, sin cambiar el checkout) y genera `datos.js` más las carpetas `iconos_proyecto/` e `iconos_embebidos/`.

```
python ControlGanaderoSim/generar_sim.py              # rama main (por defecto)
python ControlGanaderoSim/generar_sim.py --rama feature/508-Analisis-Datos-Noviembre
python ControlGanaderoSim/generar_sim.py --trabajo    # checkout actual
```

Después se abre `ControlGanaderoSim/index.html` en el navegador. El selector **Iconos** cambia entre:

- **Proyecto:** los SVG que hoy tiene la rama, o sea, lo que se ve al compilar.
- **Kit actual:** lo que se verá después de `sincronizar_resources.py --aplicar`.
- **Kit + propuestas:** el kit más los cambios de `propuestas.js`, que se edita a mano para probar otros iconos.

**Marcar origen** pone un punto en cada icono según su origen: del kit, con cambios sin sincronizar, fuera del kit o embebido en `FrmMain.resx`. Los embebidos el kit no puede actualizarlos.

## Documentación y referencias

- [`PALETA.md`](PALETA.md) / [`paleta.svg`](paleta.svg): paleta de color, criterio de coherencia visual y variantes derivadas.
- [`notice.md`](notice.md): repositorios tomados como inspiración para el kit (Icons8 Flat Color Icons, Microsoft Fluent, Tabler, Phosphor).

## Scripts (Python)

| Script | Función |
|---|---|
| `generar_iconos.py`, `crear_kit.py` | Generación inicial del kit a partir de los controles de `FrmMain.designer.vb`. |
| `generar_faltantes.py` | Completa `Kit_semantico` con variantes con insignia en el estilo plano del kit B. **Para añadir una variante:** una línea en la lista `NUEVOS` (`(nombre, base, simbolo)`); los símbolos de insignia están en `SIMBOLOS` y su color en `COLORES_INSIGNIAS_VACA`. |
| `sincronizar_resources.py` | Lleva el kit a `ControlGanadero/Resources` y lo registra (ver más abajo). |
| `normalizar_colores.py` | Lleva los colores a la paleta (`--aplicar` para modificar; sin él solo simula). |
| `auditar_coherencia.py` | Detecta trazos, degradados y colores fuera de la paleta. |
| `generar_vista_previa.py` | Rasteriza y regenera `vista_previa.html`. |
| `generar_familias_corrales.py` | Genera las 13 variantes de `corral-frontal`, `corral-perspectiva` y `corral-manga` desde sus bases aprobadas, y la lámina `familias-corrales.svg`. |

Flujo habitual: `generar_faltantes.py` → `normalizar_colores.py --aplicar` → `auditar_coherencia.py` → `generar_vista_previa.py` → `sincronizar_resources.py --aplicar`.

## Llevar el kit a ControlGanadero

```
python sincronizar_resources.py                    # simulación: muestra qué haría
python sincronizar_resources.py --aplicar          # copia + registro
python sincronizar_resources.py --aplicar --solo-registrar   # solo el registro
python sincronizar_resources.py --aplicar --sin-registro     # solo la copia
```

1. **Copia:** borra de `ControlGanadero/Resources` los SVG del kit y los vuelve a copiar (actualiza dibujos, añade nuevos). Los SVG ajenos al kit (DevExpress, referenciados desde `Resources.resx`) **no se tocan**. Lo pegado se anota en `Resources/.kit_manifest.txt`.
2. **Registro:** da de alta los nuevos en `My Project/Resources.resx`, `Resources.Designer.vb` y `ControlGanaderoPro.vbproj`, y da de baja los que ya no existen. Es idempotente.
3. **Respaldos:** antes de cambiar algo guarda copia en `Respaldos/resources_svg/<fecha>` y `Respaldos/registro_recursos/<fecha>`.

**Renombrar o eliminar un icono del kit:** anota el nombre *viejo* en [`retirados.txt`](retirados.txt) y vuelve a ejecutar `--aplicar`; si no, queda colgado en el proyecto (le pasó a `corral` → `cerca`). Si el código aún usa `My.Resources.<viejo>`, el script avisa y no aplica nada.

Después, en Visual Studio, aceptar «Recargar» si el proyecto estaba abierto.

## Otras carpetas

- `flat-color-icons/`, `phosphor-core/`, `icons/`: repositorios descargados como material de inspiración.
- `Respaldos/`: copias de seguridad automáticas previas a cada cambio masivo (antes de normalizar, de regenerar, etc.).
- `__pycache__/`: caché de Python, ignorable.
