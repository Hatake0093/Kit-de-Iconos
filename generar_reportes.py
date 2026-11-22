#!/usr/bin/env python3
"""Agrega la variante `-reporte` (hoja con linea de tendencia, insignia azul) a cada familia con insignia.

No redibuja el cuerpo: parte de una variante ya generada de la familia (`-mas` si existe), le quita la
insignia y pone la de reporte. Asi respeta la escala de cada familia (implantador .86, indicador .78,
corrales .82, bases de 64 x 64...). Correr despues de generar_faltantes.py y generar_familias_corrales.py;
generar_faltantes.py lo llama al final.

Uso: python generar_reportes.py
"""
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
SVG = os.path.join(AQUI, "simulador de control ganadero", "Kit_semantico", "svg")
AZUL = "#378CE7"
# familias con insignia que reciben `-reporte` (documento ya es el reporte; las sueltas con una sola variante no)
FAMILIAS = ("BaseDatos arete arete-rfid barras bascula billete calendario camion camion-mixer cerca "
            "comedero corral-frontal corral-manga corral-perspectiva cruz engranaje espiga etiqueta hoja "
            "implantador indicador jeringa matraz medidor nube saco usuario vaca").split()
ARO = '<ellipse cx="25.5" cy="25.5" rx="6.5" ry="6.5" fill="#FFFFFF"/>'
ENVUELTA = '<g transform="scale(2)">'


def origen(familia):
    """Variante con insignia de la familia: `-mas` si existe; si no, la primera que lleve aro."""
    candidatas = [f"{familia}-mas"] + sorted(
        n[:-4] for n in os.listdir(SVG)
        if n.startswith(familia + "-") and n.endswith(".svg") and "-" not in n[len(familia) + 1:-4])
    for nombre in candidatas:
        ruta = os.path.join(SVG, nombre + ".svg")
        if os.path.exists(ruta) and ARO in open(ruta, encoding="utf-8").read():
            return nombre
    raise SystemExit(f"{familia}: no hay ninguna variante con insignia de la que partir")


def reporte(familia, insignia):
    texto = open(os.path.join(SVG, origen(familia) + ".svg"), encoding="utf-8").read()
    i = texto.index(ARO)
    envuelta = texto[:i].endswith(ENVUELTA)
    cuerpo = texto[:i - len(ENVUELTA)] if envuelta else texto[:i]
    nueva = insignia("reporte", AZUL)
    if envuelta:
        nueva = ENVUELTA + nueva + "</g>"
    cierre = "</svg>" + ("\n" if texto.endswith("\n") else "")
    salida = cuerpo + nueva + cierre
    # los SVG de 64 x 64 llevan <title>: "Familia: accion" -> "Familia: reporte"
    return re.sub(r"(<title[^>]*>[^<:]*: )([A-Za-z])[^<]*(</title>)",
                  lambda m: m.group(1) + ("R" if m.group(2).isupper() else "r") + "eporte" + m.group(3), salida)


def main():
    from generar_faltantes import insignia
    for familia in FAMILIAS:
        with open(os.path.join(SVG, familia + "-reporte.svg"), "w", encoding="utf-8") as f:
            f.write(reporte(familia, insignia))
    print(len(FAMILIAS), "variantes -reporte generadas")


if __name__ == "__main__":
    main()
