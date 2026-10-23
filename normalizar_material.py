#!/usr/bin/env python3
"""Lleva los grises y pasteles de Material/Icons8 de Kit_semantico a la paleta (ver PALETA.md).

normalizar_colores.py no los toca (grises, blancos y tintes claros se respetan); aqui se remapean
uno a uno porque el criterio es por significado: oscuros -> azul marino, grises medios -> gris del kit,
pasteles -> tintes documentados en la seccion 7 de PALETA.md.

Uso:  python normalizar_material.py            # simula y muestra el resumen
      python normalizar_material.py --aplicar  # copia de seguridad + cambios
"""
import os
import re
import shutil
import sys
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
SVG = os.path.join(AQUI, "simulador de control ganadero", "Kit_semantico", "svg")
RESPALDO = os.path.join(AQUI, "Respaldos", "antes_de_normalizar_material")

MARINO, GRIS, AZUL_CLARO, AZUL_VIDRIO = "24465B", "8A949E", "9CC6F2", "CFE3FA"
CLARO, NEUTRO = "E2F2F5", "CFD8DC"

# color de origen -> color de la paleta
MAPA = {
    "263238": MARINO, "37474F": MARINO, "424242": MARINO, "455A64": MARINO, "546E7A": MARINO,
    "607D8B": GRIS, "616161": GRIS, "BDBDBD": NEUTRO, "E0E0E0": NEUTRO,
    "90CAF9": AZUL_CLARO, "BBDEFB": AZUL_VIDRIO, "E3F2FD": CLARO, "E8EAF6": CLARO, "C5CAE9": "D3E2F4",
    "FFCC80": "F7E3BE", "FFCCBC": "F6D9D6", "FFAB91": "F6D9D6", "DCEDC8": "D6EBDD",
    "CCFF90": CLARO, "B39DDB": "8870D4",
}
# excepciones por icono (color de origen -> destino)
POR_ICONO = {"Rechazar": {"FFCC80": "F3AD43"}}


def main():
    aplicar = "--aplicar" in sys.argv
    cambios, tocados = Counter(), {}
    for nombre in sorted(os.listdir(SVG)):
        if not nombre.endswith(".svg"):
            continue
        icono = nombre[:-4]
        ruta = os.path.join(SVG, nombre)
        texto = open(ruta, encoding="utf-8", newline="").read()
        mapa = {**MAPA, **POR_ICONO.get(icono, {})}

        def cambia(m):
            origen = m.group(0)[1:].upper()
            if origen in mapa:
                cambios[(origen, mapa[origen])] += 1
                return "#" + mapa[origen]
            return m.group(0)

        nuevo = re.sub(r"#[0-9a-fA-F]{6}\b", cambia, texto)
        if nuevo != texto:
            tocados[icono] = nuevo
    print(f"{len(tocados)} archivos cambiarian; {len(cambios)} remapeos distintos")
    for (a, b), n in sorted(cambios.items()):
        print(f"  #{a} -> #{b}  ({n})")
    if not aplicar:
        print("(simulacion; usa --aplicar para escribir)")
        return
    if os.path.exists(RESPALDO):
        sys.exit(f"ya existe {RESPALDO}: revisalo o renombralo antes de aplicar de nuevo")
    os.makedirs(RESPALDO)
    for icono, nuevo in tocados.items():
        shutil.copy2(os.path.join(SVG, icono + ".svg"), RESPALDO)
        with open(os.path.join(SVG, icono + ".svg"), "w", encoding="utf-8", newline="") as f:
            f.write(nuevo)
    print("aplicado; respaldo en", RESPALDO)


if __name__ == "__main__":
    main()
