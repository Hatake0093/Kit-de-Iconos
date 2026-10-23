#!/usr/bin/env python3
"""Juego de prueba 16x16 para botones pequeños. No toca svg/ (32x32).

Uso:  python generar_iconos16.py
Salida: svg16/<control>.svg
"""
import os

from generar_iconos import CAT

AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(AQUI, "svg16")
BLANCO = "#fff"

# Insignias simplificadas: centro (12, 12), radio 3.5, trazo 1.6.
INSIGNIAS = {
    "plus": "M12 10.3 V13.7 M10.3 12 H13.7",
    "up": "M12 13.2 V10.8 M10.8 12 L12 10.8 L13.2 12",
    "down": "M12 10.8 V13.2 M10.8 12 L12 13.2 L13.2 12",
    "star": ('<polygon points="12,8.8 12.82,10.87 15.04,11.01 13.33,12.43 13.88,14.59 '
             '12,13.4 10.12,14.59 10.67,12.43 8.96,11.01 11.18,10.87" fill="{A}" stroke="none"/>'),
}

# Vaca de contorno grueso: cabeza, cuernos, orejas, hocico y dos ojos.
VACA = (
    '<path d="M4 4 L2.5 1.5 M12 4 L13.5 1.5"/>'
    '<path d="M3.5 4.5 L1 5.5 L1.5 7.5 L3.5 7 Z M12.5 4.5 L15 5.5 L14.5 7.5 L12.5 7 Z" fill="{T}" stroke-width="1.2"/>'
    f'<path d="M4 3.5 H12 L12.5 9 C12.5 12 10.5 13.5 8 13.5 C5.5 13.5 3.5 12 3.5 9 Z" fill="{BLANCO}"/>'
    '<ellipse cx="8" cy="11" rx="2.6" ry="1.7" fill="{T}" stroke="none"/>'
    '<circle cx="6" cy="7.5" r="1" fill="{A}" stroke="none"/>'
    '<circle cx="10" cy="7.5" r="1" fill="{A}" stroke="none"/>'
)

# Control -> insignia (None = solo vaca).
ICONOS16 = [
    ("bbiListaReses", None),
    ("bbiListaResesCrianza", "plus"),
    ("bbiListaResesDesarrollo", "up"),
    ("bbiNacimientos", "star"),
    ("bbiAltasDestete", "down"),
]


def icono16(cat, insignia):
    A, T = CAT[cat]
    cuerpo = VACA
    if insignia:
        marca = INSIGNIAS[insignia]
        if marca.startswith("<"):
            detalle = marca
        else:
            detalle = f'<path d="{marca}" stroke-width="1.6"/>'
        cuerpo += (f'<circle cx="12" cy="12" r="3.5" fill="{BLANCO}" stroke-width="1.6"/>'
                   + detalle)
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" '
           'fill="none" stroke="{A}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
           + cuerpo + '</svg>')
    return svg.replace("{A}", A).replace("{T}", T)


def main():
    os.makedirs(OUT, exist_ok=True)
    for ctl, insignia in ICONOS16:
        ruta = os.path.join(OUT, ctl + ".svg")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(icono16("ganado", insignia))
    print(f"{len(ICONOS16)} iconos 16x16 generados en {OUT}")


if __name__ == "__main__":
    main()
