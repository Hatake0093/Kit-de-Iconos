#!/usr/bin/env python3
"""Audita que los iconos de Kit_semantico/svg no se vean de origenes distintos.

Detecta tres cosas:
  1. estilo de linea: SVG cuya raiz dibuja con trazo (stroke) en vez de relleno plano
  2. degradados
  3. colores fuera del sistema: tonos saturados que no estan cerca de ningun color de PALETA.md

Un color "cerca" no tiene que ser identico: basta con que sea un tono de la misma familia y
brillo razonable (distancia < UMBRAL en RGB). Los grises, blancos y tintes claros se aceptan.

Uso: python auditar_coherencia.py
"""
import colorsys
import math
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
SVG = os.path.join(AQUI, "simulador de control ganadero", "Kit_semantico", "svg")
UMBRAL = 55  # distancia RGB maxima a un color del sistema

SISTEMA = {
    # paleta base y derivadas
    "24465B", "378CE7", "24AC88", "F3AD43", "E56876", "8870D4", "E2F2F5", "1B7F65", "C98A1B", "B94A58",
    # vaca brahman
    "B9472B", "F4E1CF", "8A949E", "EDE6D6",
    # cria de la vaca brahman (tonos aclarados)
    "DE9477", "FBF1E6", "F19EA8",
    # calendario
    "F44336", "B71C1C", "CFD8DC", "B0BEC5", "90A4AE",
}


def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def es_neutro_o_tinte(h):
    r, g, b = (c / 255 for c in rgb(h))
    _, luz, sat = colorsys.rgb_to_hls(r, g, b)
    return sat < 0.25 or luz > 0.72 or luz < 0.10


def distancia_minima(h):
    return min(math.dist(rgb(h), rgb(s)) for s in SISTEMA)


def main():
    linea, degradado, fuera = [], [], {}
    total = 0
    for nombre in sorted(os.listdir(SVG)):
        if not nombre.endswith(".svg"):
            continue
        total += 1
        t = open(os.path.join(SVG, nombre), encoding="utf-8", errors="replace").read()
        raiz = re.search(r"<svg[^>]*>", t).group(0)
        if re.search(r'\sstroke="#[0-9A-Fa-f]{6}"', raiz):
            linea.append(nombre[:-4])
        if "Gradient" in t:
            degradado.append(nombre[:-4])
        malos = sorted({c.upper() for c in re.findall(r"#([0-9A-Fa-f]{6})\b", t)
                        if c.upper() not in SISTEMA and not es_neutro_o_tinte(c) and distancia_minima(c.upper()) > UMBRAL})
        if malos:
            fuera[nombre[:-4]] = malos
    print(f"{total} iconos")
    print(f"\n1) Estilo de linea (trazo en la raiz): {len(linea)}\n   " + ", ".join(linea))
    print(f"\n2) Con degradado: {len(degradado)}\n   " + ", ".join(degradado))
    print(f"\n3) Con colores fuera del sistema (distancia > {UMBRAL}): {len(fuera)}")
    for n, c in fuera.items():
        print(f"   {n}: " + " ".join("#" + x for x in c))
    sin_problema = total - len(set(linea) | set(degradado) | set(fuera))
    print(f"\nCoherentes (sin ninguno de los tres): {sin_problema} de {total}")


if __name__ == "__main__":
    main()
