"""Genera las variantes de los tres corrales aprobados desde sus SVG base.

Uso: python generar_familias_corrales.py
Las bases viven en Kit_semantico/svg; no se regeneran ni se sobrescriben.
"""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parent
SVG = ROOT / "simulador de control ganadero" / "Kit_semantico" / "svg"
FAMILIAS = {
    "corral-frontal": "Corral frontal",
    "corral-perspectiva": "Corral perspectiva",
    "corral-manga": "Corral manga",
}
ACCIONES = {
    "mas": ("Agregar", "#24AC88"),
    "menos": ("Quitar", "#E56876"),
    "check": ("Confirmar", "#24AC88"),
    "x": ("Cerrar", "#E56876"),
    "lupa": ("Buscar", "#378CE7"),
    "lista": ("Listado", "#378CE7"),
    "flecha": ("Trasladar", "#378CE7"),
    "reloj": ("Historial", "#8870D4"),
    "intercambio": ("Intercambio", "#378CE7"),
    "pin": ("Ubicación", "#E56876"),
    "estrella": ("Destacado", "#F3AD43"),
    "circulo": ("Sectores", "#8870D4"),
    "alerta": ("Alerta", "#F3AD43"),
}


def entradas():
    for familia, titulo in FAMILIAS.items():
        yield familia, titulo, "Base"
        for sufijo, (accion, _) in ACCIONES.items():
            yield f"{familia}-{sufijo}", titulo, accion


def vista_familias():
    partes = ['<svg xmlns="http://www.w3.org/2000/svg" width="1260" height="450" viewBox="0 0 1260 450">',
              '<rect width="1260" height="450" fill="#F7F9FB"/>']
    for fila, (familia, titulo) in enumerate(FAMILIAS.items()):
        y = fila * 150
        partes.append(f'<text x="16" y="{y + 25}" font-family="Segoe UI,sans-serif" font-size="17" fill="#24465B">{titulo}</text>')
        for col, sufijo in enumerate([""] + list(ACCIONES)):
            nombre = familia + ("-" + sufijo if sufijo else "")
            dibujo = (SVG / f"{nombre}.svg").read_text(encoding="utf-8")
            dibujo = re.search(r"<svg[^>]*>(.*)</svg>", dibujo, re.S).group(1)
            dibujo = re.sub(r"<title\b[^>]*>.*?</title>", "", dibujo, flags=re.S)
            x = 16 + col * 88
            partes.append(f'<g transform="translate({x} {y + 39})">{dibujo}</g>')
            partes.append(f'<text x="{x + 32}" y="{y + 125}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" fill="#24465B">{sufijo or "base"}</text>')
    partes.append('</svg>')
    (SVG.parent / 'familias-corrales.svg').write_text('\n'.join(partes), encoding='utf-8')


def main():
    from generar_faltantes import insignia

    cantidad = 0
    for familia, titulo in FAMILIAS.items():
        base = (SVG / f"{familia}.svg").read_text(encoding="utf-8")
        cuerpo = re.search(r"<svg[^>]*>(.*)</svg>", base, re.S).group(1)
        cuerpo = re.sub(r"<title\b[^>]*>.*?</title>", "", cuerpo, flags=re.S)
        for sufijo, (accion, color) in ACCIONES.items():
            # La puerta queda por encima del aro; insignia estándar en (25.5,25.5).
            contenido = '<g transform="translate(0 -1) scale(.82)">' + cuerpo + '</g>'
            contenido += '<g transform="scale(2)">' + insignia(sufijo, color) + '</g>'
            salida = ('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" '
                      'viewBox="0 0 64 64" role="img" aria-labelledby="title">\n'
                      f'<title id="title">{html.escape(titulo + ": " + accion)}</title>\n'
                      + contenido + '\n</svg>\n')
            (SVG / f"{familia}-{sufijo}.svg").write_text(salida, encoding="utf-8")
            cantidad += 1
    vista_familias()
    print(f"{cantidad} variantes generadas; 3 bases conservadas.")


if __name__ == "__main__":
    main()
