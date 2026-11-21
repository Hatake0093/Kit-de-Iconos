#!/usr/bin/env python3
"""Lleva los colores de Kit_semantico/svg a la paleta del kit B.

Cada color saturado se clasifica por tono (azul, rojo, verde, ambar, morado) y luego por
luminosidad (oscuro / medio) y se sustituye por el color de la paleta. No toca: los colores
que ya son de la paleta, grises/blancos, tintes claros, magenta (degradados Fluent, pendientes)
ni los archivos calendario*, vaca*, crianza* y carnic* (paletas propias, ver PALETA.md).

Uso:  python normalizar_colores.py            # simula y muestra el resumen
      python normalizar_colores.py --aplicar  # copia de seguridad + cambios
"""
import colorsys
import os
import re
import shutil
import sys
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
SVG = os.path.join(AQUI, "simulador de control ganadero", "Kit_semantico", "svg")
RESPALDO = os.path.join(AQUI, "Respaldos", "antes_de_normalizar_color")
EXCLUIR_PREFIJOS = ("calendario", "vaca", "crianza", "carnic")

# paleta de B (azul oscuro = contorno / detalle)
AZUL_OSCURO, AZUL, VERDE, VERDE_OSCURO = "24465B", "378CE7", "24AC88", "1B7F65"
AMBAR, AMBAR_OSCURO, ROSA, ROSA_OSCURO, MORADO = "F3AD43", "C98A1B", "E56876", "B94A58", "8870D4"
# colores que ya forman parte del sistema: nunca se tocan
INTOCABLES = {AZUL_OSCURO, AZUL, VERDE, AMBAR, ROSA, MORADO, "E2F2F5", "FFFFFF", "000000",
              "907B6C", "B9472B", "8A949E", "F4E1CF", "EDE6D6",
              # variantes oscuras declaradas en PALETA.md
              "1F6FC4", "B94A58", "1B7F65", "C98A1B"}


def destino(hex6):
    h = hex6.upper()
    if h in INTOCABLES:
        return h
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    tono, luz, sat = colorsys.rgb_to_hls(r, g, b)
    tono *= 360
    if sat < 0.25 or luz > 0.72 or luz < 0.10:  # grises, tintes claros, casi negro
        return h
    if tono < 15 or tono >= 345:   # rojo
        return ROSA_OSCURO if luz < 0.50 else ROSA
    if tono < 70:                  # naranja y amarillo
        return AMBAR_OSCURO if luz < 0.45 else AMBAR
    if tono < 200:                 # verde y turquesa
        return VERDE_OSCURO if luz < 0.36 else VERDE
    if tono < 255:                 # azul e indigo
        return AZUL_OSCURO if luz < 0.33 or tono > 228 else AZUL
    if tono < 290:                 # morado
        return MORADO
    return h                       # magenta / rosa: degradados Fluent, se tratan aparte


def main():
    aplicar = "--aplicar" in sys.argv
    cambios = Counter()
    archivos = 0
    nuevos = {}
    for nombre in sorted(os.listdir(SVG)):
        if not nombre.endswith(".svg") or nombre.lower().startswith(EXCLUIR_PREFIJOS):
            continue
        ruta = os.path.join(SVG, nombre)
        texto = open(ruta, encoding="utf-8", errors="replace").read()

        def cambiar(m):
            nuevo = destino(m.group(1))
            if nuevo.upper() != m.group(1).upper():
                cambios[(m.group(1).upper(), nuevo)] += 1
            return "#" + nuevo
        resultado = re.sub(r"#([0-9A-Fa-f]{6})\b", cambiar, texto)
        if resultado != texto:
            archivos += 1
            nuevos[ruta] = resultado
    print(f"{archivos} archivos cambiarian; {len(cambios)} colores distintos remapeados")
    for (a, b), n in sorted(cambios.items(), key=lambda kv: -kv[1])[:25]:
        print(f"  #{a} -> #{b}  ({n})")
    if not aplicar:
        print("(simulacion; usa --aplicar para escribir)")
        return
    if os.path.exists(RESPALDO):
        sys.exit("ya existe " + RESPALDO + ": revisalo o renombralo antes de aplicar de nuevo")
    shutil.copytree(SVG, RESPALDO)
    for ruta, resultado in nuevos.items():
        open(ruta, "w", encoding="utf-8").write(resultado)
    print("aplicado. copia de seguridad en", RESPALDO)


if __name__ == "__main__":
    main()
