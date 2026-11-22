#!/usr/bin/env python3
"""Audita que los iconos de Kit_semantico/svg no se vean de origenes distintos.

Detecta tres cosas:
  1. estilo de linea: SVG cuya raiz dibuja con trazo (stroke) en vez de relleno plano
  2. degradados
  3. colores fuera del sistema: tonos saturados que no estan cerca de ningun color de PALETA.md

La distancia RGB se complementa con una revisión de tonos no declarados y una
detección específica del terracota, incluso cuando es próximo a un color aprobado.

Uso: python auditar_coherencia.py
"""
import colorsys
import math
import os
import re
from collections import defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
SVG = os.path.join(AQUI, "simulador de control ganadero", "Kit_semantico", "svg")
UMBRAL = 55  # distancia RGB maxima a un color del sistema

SISTEMA = {
    # paleta base y derivadas
    "24465B", "378CE7", "24AC88", "F3AD43", "E56876", "8870D4", "E2F2F5", "1B7F65", "C98A1B", "B94A58",
    # vaca brahman
    "907B6C", "F4E1CF", "8A949E", "EDE6D6",
    # cria de la vaca brahman (tonos aclarados)
    "B19D8D", "FBF1E6", "D3BFAE",
    # neutros de Material, tintes declarados y pantalla azul
    "CFD8DC", "B0BEC5", "90A4AE", "1F6FC4", "CFE3FA", "D3E2F4", "F6D9D6",
    "F7E3BE", "D6EBDD", "D1C4E9", "9CC6F2", "7AD3B8",
    # ámbar claro: trasera de carpeta-abierta
    "F6C272",
}
EXCEPCIONES = {"calendario": {"F44336", "B71C1C"}, "carnic": {"E82126", "009449"}}
HEX = re.compile(r"#([0-9a-f]{8}|[0-9a-f]{6}|[0-9a-f]{4}|[0-9a-f]{3})\b", re.I)


def colores_svg(texto):
    """Unifica las notaciones hexadecimales SVG; el alfa no cambia el matiz."""
    colores = set()
    for valor in HEX.findall(texto.upper()):
        if len(valor) <= 4:
            valor = "".join(c * 2 for c in valor)
        colores.add(valor[:6])
    return colores


def es_terracota(h):
    tono, luz, sat = colorsys.rgb_to_hls(*(c / 255 for c in rgb(h)))
    return 8 <= tono * 360 <= 26 and 0.15 <= luz <= 0.80 and sat >= 0.28


def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def es_neutro_o_tinte(h):
    r, g, b = (c / 255 for c in rgb(h))
    _, luz, sat = colorsys.rgb_to_hls(r, g, b)
    return sat < 0.25 or luz > 0.72 or luz < 0.10


def distancia_minima(h, permitidos):
    return min(math.dist(rgb(h), rgb(s)) for s in permitidos)


def main():
    linea, degradado, fuera = [], [], {}
    terracotas, revisar = defaultdict(list), defaultdict(list)
    inventario = set()
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
        icono = nombre[:-4]
        permitidos = SISTEMA | EXCEPCIONES.get(icono.split("-")[0], set())
        colores = colores_svg(t)
        inventario.update(colores)
        malos = []
        for c in sorted(colores - permitidos):
            if es_terracota(c):
                terracotas[c].append(icono)
                malos.append(c)
            elif not es_neutro_o_tinte(c) and distancia_minima(c, permitidos) > UMBRAL:
                malos.append(c)
            elif len(set(rgb(c))) > 1:
                revisar[c].append(icono)
        if malos:
            fuera[nombre[:-4]] = malos
    print(f"{total} iconos; {len(inventario)} colores hexadecimales distintos")
    print(f"\n1) Estilo de linea (trazo en la raiz): {len(linea)}\n   " + ", ".join(linea))
    print(f"\n2) Con degradado: {len(degradado)}\n   " + ", ".join(degradado))
    print(f"\n3) Con terracota o colores fuera de tolerancia: {len(fuera)}")
    for n, c in fuera.items():
        print(f"   {n}: " + " ".join("#" + x for x in c))
    sin_problema = total - len(set(linea) | set(degradado) | set(fuera))
    print(f"\nCoherentes (sin ninguno de los tres): {sin_problema} de {total}")
    print(f"Terracotas detectados: {len(terracotas)}")
    for c, nombres in sorted(terracotas.items()):
        print(f"   #{c}: " + ", ".join(nombres))
    print(f"Otros tonos sin documentar para revisión visual: {len(revisar)}")
    for c, nombres in sorted(revisar.items()):
        print(f"   #{c}: " + ", ".join(nombres))
    return bool(linea or degradado or fuera)


if __name__ == "__main__":
    raise SystemExit(main())
