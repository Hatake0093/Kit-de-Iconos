#!/usr/bin/env python3
"""Completa Kit_semantico con variantes en el estilo plano del kit B.

Cada icono = base plana existente en Kit_semantico/svg + insignia
(elipse blanca r7, circulo de color r5.5, simbolo blanco de trazo 1.5),
tal como lo hace el kit B. Uso: python generar_faltantes.py
"""
import csv
import html
import os
import re
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(AQUI, "simulador de control ganadero", "Kit_semantico")
INKSCAPE = r"C:\Program Files\Inkscape\bin\inkscape.exe"

VERDE, AMBAR, MORADO, ROJO, AZUL = "#24AC88", "#F3AD43", "#8870D4", "#E56876", "#378CE7"
# vaca: rojo brahman, cara crema, cuernos grises
BRAHMAN, CREMA, GRIS_CUERNO = "#B9472B", "#F4E1CF", "#8A949E"

COLORES_INSIGNIAS_VACA = {
    "vaca-dinero": VERDE,
    "vaca-mas": VERDE,
    "vaca-check": VERDE,
    "vaca-arriba": VERDE,
    "vaca-menos": ROJO,
    "vaca-abajo": ROJO,
    "vaca-alerta": AMBAR,
    "vaca-estrella": AMBAR,
    "vaca-lupa": AZUL,
    "vaca-lista": AZUL,
    "vaca-flecha": AZUL,
    "vaca-circulo": MORADO,
}
# mismo criterio de color por significado para el calendario
COLOR_POR_SIMBOLO = {"mas": VERDE, "check": VERDE, "menos": ROJO, "x": ROJO, "alerta": AMBAR,
                     "estrella": AMBAR, "lupa": AZUL, "lista": AZUL, "flecha": AZUL, "reloj": MORADO}
COLOR_POR_SIMBOLO.update({"dolar": VERDE, "circulo": MORADO, "arriba": VERDE, "abajo": ROJO, "codigo": AZUL, "gota": AZUL})
COLOR_POR_SIMBOLO.update({"documento": AZUL, "arribaYabajo": AZUL, "reporte": AZUL})
# los nombres usan "bajada/subida" y la tabla por simbolo usa "abajo/arriba": se asignan a mano
COLORES_INSIGNIAS_VACA.update({"documento-bajada": ROJO, "comedero-bajada": ROJO, "comedero-subida": VERDE})
for _familia in ("calendario", "etiqueta", "documento", "usuario", "barras", "comedero", "saco", "carrito",
                 "lapida", "matraz", "arete-rfid", "BaseDatos", "billete", "implantador", "indicador", "camion-mixer"):
    COLORES_INSIGNIAS_VACA.update({f"{_familia}-{s}": c for s, c in COLOR_POR_SIMBOLO.items()})


# glifo del dolar tomado de flat-color-icons/svg/currency_exchange.svg (caja 11.2x21.4, centro 30.1,30.0)
DOLAR_D = "M28.4,27c0.1,0.2,0.2,0.4,0.4,0.6c0.2,0.2,0.4,0.4,0.7,0.5c0.3,0.2,0.7,0.3,1.1,0.5c0.7,0.3,1.4,0.6,2,0.9 c0.6,0.3,1.1,0.7,1.5,1.1c0.4,0.4,0.8,0.9,1,1.4c0.2,0.5,0.4,1.2,0.4,1.9c0,0.7-0.1,1.3-0.3,1.8c-0.2,0.5-0.5,1-0.9,1.4 s-0.9,0.7-1.4,0.9c-0.6,0.2-1.2,0.4-1.8,0.5v2.2h-1.8v-2.2c-0.6-0.1-1.2-0.2-1.8-0.4s-1.1-0.5-1.5-1c-0.5-0.4-0.8-1-1.1-1.6 c-0.3-0.6-0.4-1.4-0.4-2.3h3.3c0,0.5,0.1,1,0.2,1.3c0.1,0.4,0.3,0.6,0.6,0.9c0.2,0.2,0.5,0.4,0.8,0.5c0.3,0.1,0.6,0.1,0.9,0.1 c0.4,0,0.7,0,0.9-0.1c0.3-0.1,0.5-0.2,0.7-0.4c0.2-0.2,0.3-0.4,0.4-0.6c0.1-0.2,0.1-0.5,0.1-0.8c0-0.3,0-0.6-0.1-0.8 c-0.1-0.2-0.2-0.5-0.4-0.7s-0.4-0.4-0.7-0.5c-0.3-0.2-0.7-0.3-1.1-0.5c-0.7-0.3-1.4-0.6-2-0.9c-0.6-0.3-1.1-0.7-1.5-1.1 c-0.4-0.4-0.8-0.9-1-1.4c-0.2-0.5-0.4-1.2-0.4-1.9c0-0.6,0.1-1.2,0.3-1.7c0.2-0.5,0.5-1,0.9-1.4c0.4-0.4,0.9-0.7,1.4-1 c0.5-0.2,1.2-0.4,1.8-0.5v-2.4h1.8v2.4c0.6,0.1,1.2,0.3,1.8,0.6c0.5,0.3,1,0.6,1.3,1.1c0.4,0.4,0.7,1,0.9,1.6c0.2,0.6,0.3,1.3,0.3,2 h-3.3c0-0.9-0.2-1.6-0.6-2c-0.4-0.4-0.9-0.7-1.5-0.7c-0.3,0-0.6,0.1-0.9,0.2c-0.2,0.1-0.4,0.2-0.6,0.4c-0.2,0.2-0.3,0.4-0.3,0.6 c-0.1,0.2-0.1,0.5-0.1,0.8C28.3,26.5,28.4,26.8,28.4,27z"


def dolar(cx, cy, alto, color="#FFFFFF"):
    """Dolar redondeado centrado en (cx, cy) con la altura pedida."""
    e = alto / 21.4
    return (f'<path transform="translate({cx} {cy}) scale({e:.3f}) translate(-30.1 -30)" '
            f'fill="{color}" d="{DOLAR_D}"/>')


def pl(puntos, ancho=1.5):
    return (f'<polyline points="{puntos}" fill="none" stroke="#FFFFFF" stroke-width="{ancho}" '
            'stroke-linecap="round" stroke-linejoin="round"/>')


SIMBOLOS = {
    "mas": pl("23,25.5 28,25.5") + pl("25.5,23 25.5,28"),
    "menos": pl("23,25.5 28,25.5"),
    "check": pl("22.5,25 25,27.5 28.5,23"),
    "flecha": pl("22.5,25.5 28.5,25.5 26,23") + pl("28.5,25.5 26,28"),
    "arriba": pl("25.5,28.5 25.5,22.5") + pl("23,25 25.5,22.5 28,25"),
    "abajo": pl("25.5,22.5 25.5,28.5") + pl("23,26 25.5,28.5 28,26"),
    "lista": pl("23,23.5 28,23.5") + pl("23,25.5 28,25.5") + pl("23,27.5 28,27.5"),
    "estrella": '<polygon points="25.5,22 26.5,24.5 29,25.5 26.5,26.5 25.5,29 24.5,26.5 22,25.5 24.5,24.5" fill="#FFFFFF"/>',
    "pausa": pl("24,23 24,28") + pl("27,23 27,28"),
    "dolar": dolar(25.5, 25.5, 8),
    # marcador de mapa: gota blanca con hueco (evenodd deja ver el color de la insignia)
    "pin": ('<path fill="#FFFFFF" fill-rule="evenodd" d="M25.5 29.7 C24 28.1 22.2 26.4 22.2 24.6 A3.3 3.3 0 0 1 28.8 24.6 '
            'C28.8 26.4 27 28.1 25.5 29.7 Z M24.2 24.6 a1.3 1.3 0 1 0 2.6 0 a1.3 1.3 0 1 0 -2.6 0 Z"/>'),
    "lupa": ('<ellipse cx="25" cy="25" rx="2.3" ry="2.3" fill="none" stroke="#FFFFFF" stroke-width="1.5"/>'
             + pl("26.7,26.7 28.7,28.7")),
    "x": pl("23,23 28,28") + pl("28,23 23,28"),
    # ajuste en ambos sentidos: flecha que sube y flecha que baja, lado a lado
    "arribaYabajo": (pl("23.6,28.5 23.6,22.5") + pl("22,24 23.6,22.5 25.2,24")
                     + pl("27.4,22.5 27.4,28.5") + pl("25.8,27 27.4,28.5 29,27")),
    # reporte: la misma hoja con una linea de tendencia marino en vez de renglones
    "reporte": ('<polygon points="23.2,22 26.4,22 28,23.6 28,29 23.2,29" fill="#FFFFFF"/>'
                '<polyline points="24.2,27.6 25.4,25.9 26.3,26.7 27.5,24.5" fill="none" stroke="#24465B" '
                'stroke-width="0.9" stroke-linecap="round" stroke-linejoin="round"/>'),
    # hoja con esquina cortada y dos renglones marino (como los ojos de "vaca")
    "documento": ('<polygon points="23.2,22 26.4,22 28,23.6 28,29 23.2,29" fill="#FFFFFF"/>'
                  '<polyline points="24.3,25.1 26.9,25.1" fill="none" stroke="#24465B" stroke-width="0.9" stroke-linecap="round"/>'
                  '<polyline points="24.3,27.1 26.9,27.1" fill="none" stroke="#24465B" stroke-width="0.9" stroke-linecap="round"/>'),
    "circulo": '<ellipse cx="25.5" cy="25.5" rx="1.5" ry="1.5" fill="#FFFFFF"/>',
    "alerta": pl("25.5,22.4 25.5,26.4") + pl("25.5,28.2 25.5,28.3", 1.8),
    "reloj": pl("25.2,22.3 25.2,25.8 28,25.8"),
    "copiar": ('<rect x="22.6" y="22.2" width="3.6" height="3.6" rx="0.6" fill="none" stroke="#FFFFFF" stroke-width="1.2"/>'
               '<rect x="24.8" y="24.4" width="3.6" height="3.6" rx="0.6" fill="#FFFFFF"/>'),
    # vaca de la insignia: los colores de la vaca del kit (cuernos grises, orejas y hocico brahman, cara crema)
    "vaca": ('<polyline points="23.4,23.3 22.4,21.9" fill="none" stroke="#8A949E" stroke-width="1.1" stroke-linecap="round"/>'
             '<polyline points="27.6,23.3 28.6,21.9" fill="none" stroke="#8A949E" stroke-width="1.1" stroke-linecap="round"/>'
             '<ellipse cx="22.2" cy="24.7" rx="1.5" ry="0.85" fill="#B9472B" transform="rotate(20 22.2 24.7)"/>'
             '<ellipse cx="28.8" cy="24.7" rx="1.5" ry="0.85" fill="#B9472B" transform="rotate(-20 28.8 24.7)"/>'
             '<ellipse cx="25.5" cy="25.4" rx="2.5" ry="2.9" fill="#F4E1CF"/>'
             '<ellipse cx="25.5" cy="27.4" rx="1.8" ry="1.1" fill="#B9472B"/>'
             '<ellipse cx="24.5" cy="24.8" rx="0.45" ry="0.45" fill="#24465B"/><ellipse cx="26.5" cy="24.8" rx="0.45" ry="0.45" fill="#24465B"/>'
             '<ellipse cx="24.8" cy="27.4" rx="0.3" ry="0.3" fill="#F4E1CF"/><ellipse cx="26.2" cy="27.4" rx="0.3" ry="0.3" fill="#F4E1CF"/>'),
    "arete": ('<path d="M24.3 22.2 H26.7 Q27.6 22.2 27.6 23.1 V27.3 Q27.6 28.4 26.5 28.4 H24.5 Q23.4 28.4 23.4 27.3 V23.1 '
              'Q23.4 22.2 24.3 22.2 Z" fill="#FFFFFF"/><ellipse cx="25.5" cy="23.5" rx="0.6" ry="0.6" fill="#F3AD43"/>'),
    "carrito": (pl("22.6,23 23.9,23 24.9,26.4 28,26.4 28.6,24", 1.3)
                + '<ellipse cx="25.3" cy="28.1" rx="0.8" ry="0.8" fill="#FFFFFF"/>'
                + '<ellipse cx="27.6" cy="28.1" rx="0.8" ry="0.8" fill="#FFFFFF"/>'),
    "separar": pl("22.8,25.5 25,25.5") + pl("25,25.5 26.5,23.2 28.5,23.2") + pl("25,25.5 26.5,27.8 28.5,27.8"),
    "intercambio": (pl("23,24 28,24") + pl("26.4,22.4 28,24 26.4,25.6")
                    + pl("28,27 23,27") + pl("24.6,25.4 23,27 24.6,28.6")),
    "salida": pl("25,22.8 23,22.8 23,28.2 25,28.2") + pl("24.5,25.5 28.5,25.5") + pl("26.9,23.9 28.5,25.5 26.9,27.1"),
    "gota": '<path d="M25.5 21.6 C24.6 23.2 22.9 24.7 22.9 26.4 A2.6 2.6 0 0 0 28.1 26.4 C28.1 24.7 26.4 23.2 25.5 21.6 Z" fill="#FFFFFF"/>',
    "codigo": pl("23.6,23.4 22,25.5 23.6,27.6") + pl("27.4,23.4 29,25.5 27.4,27.6") + pl("25.9,23 25.1,28", 1.2),
    # forraje: hoja blanca con rabito
    "hoja": ('<path d="M23.6 27.4 C22.6 24.6 24 22.4 28.2 22 C28.4 25.2 26.8 27.4 23.6 27.4 Z" fill="#FFFFFF"/>'
             + pl("22.6,28.5 24.6,26.2", 1.2)),
    # grano: espiga blanca con tres pares de granos y remate
    "espiga": (pl("25.5,22.8 25.5,29", 1.1)
               + "".join(f'<ellipse cx="{x}" cy="{y}" rx="0.9" ry="1.4" fill="#FFFFFF" transform="rotate({r} {x} {y})"/>'
                         for x, y, r in ((24.2, 27, -30), (26.8, 27, 30), (24.2, 24.9, -30), (26.8, 24.9, 30)))
               + '<ellipse cx="25.5" cy="22.4" rx="0.8" ry="1.3" fill="#FFFFFF"/>'),
}


def insignia(simbolo, color):
    return ('<ellipse cx="25.5" cy="25.5" rx="6.5" ry="6.5" fill="#FFFFFF"/>'
            f'<ellipse cx="25.5" cy="25.5" rx="5.5" ry="5.5" fill="{color}"/>' + SIMBOLOS[simbolo])


def interior(nombre):
    s = open(os.path.join(KIT, "svg", nombre + ".svg"), encoding="utf-8").read()
    return re.search(r"<svg[^>]*>(.*)</svg>", s, re.S).group(1)


# bases planas que no existen sueltas en el kit
# etiqueta / arete: placa ambar con ojal y marca blanca
ETIQUETA = ('<polygon points="3,5 17,5 29,17 17,29 3,15" fill="#F3AD43"/>'
            '<ellipse cx="9.5" cy="11.5" rx="2.5" ry="2.5" fill="#FFFFFF"/>'
            '<polyline points="17,14 23,20" fill="none" stroke="#FFFFFF" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round"/>')
# documento: hoja clara con esquina doblada azul y lineas de texto en azul marino
DOCUMENTO = ('<path d="M8 3 H20 L26 9 V27 A2 2 0 0 1 24 29 H8 A2 2 0 0 1 6 27 V5 A2 2 0 0 1 8 3 Z" '
             'fill="#E2F2F5" stroke="#9CC6F2" stroke-width="1"/>'
             '<polygon points="20,3 26,9 20,9" fill="#9CC6F2"/>'
             '<rect x="10" y="14" width="12" height="2" rx="1" fill="#24465B"/>'
             '<rect x="10" y="19" width="12" height="2" rx="1" fill="#24465B"/>'
             '<rect x="10" y="24" width="7" height="2" rx="1" fill="#24465B"/>')
# usuario: cabeza azul marino, hombros azules; usuarios suma una segunda persona mas clara detras
USUARIO = ('<circle cx="16" cy="10.5" r="5.5" fill="#24465B"/>'
           '<path d="M5.5 28.5 C5.5 21 10.5 18 16 18 C21.5 18 26.5 21 26.5 28.5 Z" fill="#378CE7"/>')
USUARIOS = ('<circle cx="22" cy="9.5" r="4" fill="#378CE7"/>'
            '<path d="M15 28 C15 22 18 17 22 17 C27 17 30 20 30 28 Z" fill="#9CC6F2"/>'
            '<circle cx="12" cy="12" r="4.8" fill="#24465B"/>'
            '<path d="M2.5 28.5 C2.5 21.5 7 19 12 19 C17 19 21.5 21.5 21.5 28.5 Z" fill="#378CE7"/>')
# comedero: cuerpo azul con borde marino y monton de pienso ambar
COMEDERO = ('<path d="M7 14 C9 8 13 9 16 11 C19 9 23 8 25 14 Z" fill="#F3AD43"/>'
            '<polygon points="5,17 27,17 24.5,27.5 7.5,27.5" fill="#378CE7"/>'
            '<rect x="3" y="14" width="26" height="3.4" rx="1.7" fill="#24465B"/>')
# comedero de concreto aprobado (viewBox 64, sin la barra de lectura): cuerpo de la familia comedero-*
COMEDERO_64 = ('<path d="M4 35L29 18L59 28V42L34 60L4 49Z" fill="#8A949E"/><path d="M4 35L29 18L59 28L34 46Z" fill="#E2F2F5"/><path d="M10 34L30 22L52 29L32 42Z" fill="#24465B"/><path d="M10 34L30 22L32 27L17 36Z" fill="#B0BEC5"/><path d="M18 35L35 26L46 30L31 39Z" fill="#F3AD43"/><path d="M4 35L34 46V60L4 49Z" fill="#B0BEC5"/><path d="M34 46L59 28V32L34 50Z" fill="#CFD8DC"/><path d="M45 42L47 40.5V51L45 52.5Z" fill="#B0BEC5"/>')
# saco de alimento: ambar con cuello atado y etiqueta clara con una espiga
SACO = ('<path d="M10 5 H22 L20.5 9.5 C26 12 27 20 25.5 25 C24.5 28 22 29 20 29 H12 C10 29 7.5 28 6.5 25 '
        'C5 20 6 12 11.5 9.5 Z" fill="#F3AD43"/>'
        '<path d="M11.5 9.5 H20.5" fill="none" stroke="#24465B" stroke-width="2" stroke-linecap="round"/>'
        '<rect x="10" y="15" width="12" height="9.5" rx="2" fill="#E2F2F5"/>'
        '<path d="M16 23 V17.5 M16 19.5 L14 18 M16 19.5 L18 18 M16 22 L14 20.5 M16 22 L18 20.5" fill="none" '
        'stroke="#24465B" stroke-width="1.2" stroke-linecap="round"/>')
# carrito: asa y ruedas marino, cesta verde
CARRITO = ('<polyline points="2.5,5 7,5 10.5,20 25,20" fill="none" stroke="#24465B" stroke-width="2.4" '
           'stroke-linecap="round" stroke-linejoin="round"/>'
           '<polygon points="9,9 29,9 25.5,19 11,19" fill="#24AC88"/>'
           '<circle cx="13" cy="25.5" r="2.6" fill="#24465B"/><circle cx="23" cy="25.5" r="2.6" fill="#24465B"/>')
# lapida: piedra gris con cruz marino sobre suelo marino
LAPIDA = ('<path d="M7 28 V14 A9 9 0 0 1 25 14 V28 Z" fill="#CFD8DC"/>'
          '<path d="M16 10 V20 M12 14 H20" fill="none" stroke="#24465B" stroke-width="2.4" stroke-linecap="round"/>'
          '<rect x="3" y="26.5" width="26" height="3.2" rx="1.6" fill="#24465B"/>')
# matraz: vidrio claro, borde marino y liquido morado
MATRAZ = ('<path d="M12 4 H20 V12 L28 25.5 A2.5 2.5 0 0 1 26 29 H6 A2.5 2.5 0 0 1 4 25.5 L12 12 Z" fill="#CFE3FA" '
          'stroke="#24465B" stroke-width="1.6" stroke-linejoin="round"/>'
          '<path d="M8.6 20 H23.4 L28 25.5 A2.5 2.5 0 0 1 26 29 H6 A2.5 2.5 0 0 1 4 25.5 Z" fill="#8870D4"/>'
          '<rect x="10" y="2" width="12" height="3.4" rx="1.7" fill="#24465B"/>'
          '<circle cx="11" cy="24" r="1.6" fill="#FFFFFF" fill-opacity=".8"/>')
CRUZ = f'<polygon points="12,4 20,4 20,12 28,12 28,20 20,20 20,28 12,28 12,20 4,20 4,12 12,12" fill="{ROJO}"/>'
NUBE = '<path d="M9 27 A6.5 6.5 0 0 1 9 14 A8.5 8.5 0 0 1 25 13 A7 7 0 0 1 24 27 Z" fill="#9CC6F2"/>'
# craneo de res: cuernos grises de la vaca, hueso, cuencas y nariz en azul marino
HUESO, MARINO = "#EDE6D6", "#24465B"
CRANEO = (f'<polyline points="9,10 5,8 3,3" fill="none" stroke="{GRIS_CUERNO}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<polyline points="23,10 27,8 29,3" fill="none" stroke="{GRIS_CUERNO}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<path d="M8 9 Q16 3.5 24 9 V17 Q24 20.5 21 22 V28 H11 V22 Q8 20.5 8 17 Z" fill="{HUESO}"/>'
          f'<ellipse cx="12.5" cy="15" rx="2.4" ry="3" fill="{MARINO}"/><ellipse cx="19.5" cy="15" rx="2.4" ry="3" fill="{MARINO}"/>'
          f'<path d="M16 19 L14.7 22.5 H17.3 Z" fill="{MARINO}"/>'
          f'<path d="M13.7 24.8 V28 M16 24.8 V28 M18.3 24.8 V28" stroke="{MARINO}" stroke-width="1" fill="none"/>')
MAPA = re.sub(r'<ellipse cx="17.0" cy="12.0" rx="7.0".*$', "", interior("mapa-pin"), flags=re.S)

# arete RFID: placa amarilla con ojal y simbolo de ondas azul centrado en el cuerpo
ARETE_RFID = ('<path d="M12 6 A4 4 0 0 1 20 6 V8 Q20 9.5 21.5 10 L26 11.5 Q27 12 27 13.5 V27 Q27 29.5 24.5 29.5 H7.5 '
              'Q5 29.5 5 27 V13.5 Q5 12 6 11.5 L10.5 10 Q12 9.5 12 8 Z" fill="#F7CF3D" stroke="#24465B" '
              'stroke-width="1.5" stroke-linejoin="round"/>'
              '<g transform="translate(16 19.7) scale(0.9) translate(-16 -21)">'
              f'<ellipse cx="11.9" cy="21" rx="1.8" ry="1.8" fill="{AZUL}"/>'
              f'<path d="M15.44 17.46 A5 5 0 0 1 15.44 24.54" fill="none" stroke="{AZUL}" stroke-width="2.2" stroke-linecap="round"/>'
              f'<path d="M18.26 14.64 A9 9 0 0 1 18.26 27.36" fill="none" stroke="{AZUL}" stroke-width="2.2" stroke-linecap="round"/></g>')
# iconos planos sueltos (sin insignia): contorno marino de 1.5-2.2 y colores de la paleta
D = "#24465B"
MEDIDOR = (f'<path d="M3 25 A13 13 0 0 1 9.5 13.74 L11.75 17.64 A8.5 8.5 0 0 0 7.5 25 Z" fill="{VERDE}"/>'
           f'<path d="M9.5 13.74 A13 13 0 0 1 22.5 13.74 L20.25 17.64 A8.5 8.5 0 0 0 11.75 17.64 Z" fill="{AMBAR}"/>'
           f'<path d="M22.5 13.74 A13 13 0 0 1 29 25 L24.5 25 A8.5 8.5 0 0 0 20.25 17.64 Z" fill="{ROJO}"/>'
           '<path d="M7.5 25 A8.5 8.5 0 0 1 24.5 25 Z" fill="#E2F2F5"/>'
           f'<line x1="16" y1="25" x2="20.6" y2="16.6" stroke="{D}" stroke-width="1.3" stroke-linecap="round"/>'
           f'<circle cx="16" cy="25" r="2.2" fill="{D}"/><rect x="3" y="25" width="26" height="3" rx="1.5" fill="{D}"/>')
ESCUDO_GRIS = (f'<path d="M16 3 L27 7 V15 C27 22 22 27 16 29 C10 27 5 22 5 15 V7 Z" fill="{GRIS_CUERNO}" stroke="{D}" '
               'stroke-width="1.5" stroke-linejoin="round"/>'
               '<polyline points="11,16 15,20 22,12" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
MONEDA = ('<circle cx="14" cy="14" r="11.5" fill="#F3AD43" stroke="#C98A1B" stroke-width="1.5"/>'
          '<circle cx="14" cy="14" r="7.5" fill="none" stroke="#C98A1B" stroke-width="1.2"/>'
          + dolar(14, 14, 12))
PROHIBIDO = (f'<circle cx="16" cy="16" r="13" fill="{ROJO}"/><circle cx="16" cy="16" r="9" fill="#FFFFFF"/>'
             f'<polyline points="9.6,9.6 22.4,22.4" fill="none" stroke="{ROJO}" stroke-width="3.6" stroke-linecap="round"/>')
REGLA = (f'<rect x="2.5" y="10" width="27" height="12" rx="2.5" fill="{AMBAR}"/>'
         f'<g stroke="{D}" stroke-width="1.8" stroke-linecap="round"><polyline points="8,10 8,16"/>'
         '<polyline points="13,10 13,14"/><polyline points="18,10 18,16"/><polyline points="23,10 23,14"/></g>')
TABLA_DATOS = (f'<rect x="3" y="3" width="26" height="26" rx="5" fill="{VERDE}"/>'
               '<g stroke="#FFFFFF" stroke-width="1.8"><line x1="3" y1="12" x2="29" y2="12"/><line x1="3" y1="20.5" x2="29" y2="20.5"/>'
               '<line x1="11.7" y1="12" x2="11.7" y2="29"/><line x1="20.3" y1="12" x2="20.3" y2="29"/></g>'
               '<path d="M3 8 A5 5 0 0 1 8 3 H24 A5 5 0 0 1 29 8 V12 H3 Z" fill="#1B7F65"/>')
_EJES = f'<path d="M4 3 V25 A3 3 0 0 0 7 28 H29" fill="none" stroke="{D}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
GRAFICA_TENDENCIA = (_EJES + f'<polyline points="8,21 14,14 18,18 27,8" fill="none" stroke="{VERDE}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
                     f'<polyline points="21,7.5 27,7.5 27,13.5" fill="none" stroke="{VERDE}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
GRAFICA_BARRAS_ASC = (_EJES + f'<rect x="8" y="19" width="5" height="6" rx="1" fill="{AZUL}"/><rect x="15" y="14" width="5" height="11" rx="1" fill="{VERDE}"/>'
                      f'<rect x="22" y="7" width="5" height="18" rx="1" fill="{AMBAR}"/>')
BARRAS_AZUL = (f'<g fill="{AZUL}"><rect x="4" y="16" width="7" height="13" rx="1"/><rect x="12.5" y="8" width="7" height="21" rx="1"/>'
               '<rect x="21" y="3" width="7" height="26" rx="1"/></g>')
GRAFICO_LINEAS_AMBAR = ('<path d="M4 3 V28 H29" fill="none" stroke="#24465B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
                        f'<polyline points="8,22 14,14 19,18 27,7" fill="none" stroke="{AMBAR}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
                        f'<circle cx="27" cy="7" r="2.6" fill="{AMBAR}"/>')
# guardar: disquete verde con etiqueta clara y marca marino
GUARDAR = (f'<polygon points="4,3 24,3 29,8 29,29 3,29 3,4" fill="{VERDE}"/>'
           '<rect x="8" y="3" width="15" height="9" rx="1" fill="#E2F2F5"/>'
           f'<rect x="19" y="5" width="2" height="5" rx="0" fill="{D}"/>'
           '<rect x="8" y="18" width="16" height="11" rx="1" fill="#E2F2F5"/>'
           f'<polyline points="12,22 20,22" fill="none" stroke="{D}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')
# billete: papel verde con medallon claro, dolar redondeado marino y dos puntos blancos
BILLETE = (f'<rect x="2" y="7" width="28" height="18" rx="3" fill="{VERDE}"/>'
           '<ellipse cx="16" cy="16" rx="5.6" ry="7" fill="#E2F2F5"/>'
           + dolar(16, 16, 10.5, D) +
           '<polyline points="6,16 7,16" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>'
           '<polyline points="25,16 26,16" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>')
# imprimir: impresora azul plana (como Guardar) con hoja de salida clara y lineas marino
IMPRIMIR = (f'<rect x="9" y="3" width="14" height="9" rx="1" fill="#E2F2F5"/>'
            f'<rect x="3" y="10" width="26" height="13" rx="3.5" fill="{AZUL}"/>'
            f'<circle cx="25" cy="14" r="1.4" fill="#E2F2F5"/>'
            f'<rect x="7" y="18" width="18" height="2.2" rx="1.1" fill="{D}"/>'
            f'<rect x="8" y="19.5" width="16" height="10" rx="1" fill="#E2F2F5"/>'
            f'<polyline points="11,23.5 21,23.5" fill="none" stroke="{D}" stroke-width="1.5" stroke-linecap="round"/>'
            f'<polyline points="11,26.8 17,26.8" fill="none" stroke="{D}" stroke-width="1.5" stroke-linecap="round"/>')
# enviar: avion de papel azul con pliegue marino
ENVIAR = (f'<polygon points="3,15 29,4 22,28 15.5,19.5" fill="{AZUL}"/>'
          f'<polygon points="15.5,19.5 29,4 12.5,22" fill="#1F6FC4"/>'
          f'<polyline points="15.5,19.5 12.5,26 12.5,22" fill="{D}" stroke="{D}" stroke-width="1.2" stroke-linejoin="round"/>')
GRAFICO_CIRCULAR = (f'<circle cx="16" cy="16" r="13" fill="{AZUL}"/><path d="M16 16 L16 3 A13 13 0 0 1 28.4 12 Z" fill="{AMBAR}"/>'
                    f'<path d="M16 16 L28.4 12 A13 13 0 0 1 24 25.5 Z" fill="{VERDE}"/>'
                    '<circle cx="16" cy="16" r="13" fill="none" stroke="#FFFFFF" stroke-width="1.2"/>')


SELECCIONAR_TODOS = ('<rect x="10" y="3" width="19" height="19" rx="4" fill="#CFE3FA"/>'
                     f'<rect x="3" y="10" width="19" height="19" rx="4" fill="{AZUL}"/>'
                     '<polyline points="7.5,19.5 11.5,23.5 18,15.5" fill="none" stroke="#FFFFFF" stroke-width="2.4" '
                     'stroke-linecap="round" stroke-linejoin="round"/>')

# Indicador industrial frontal aprobado: sin soporte ni conectores. Coordenadas 64 × 64.
INDICADOR = '<!-- Vista frontal limpia: carcasa, pantalla y teclado. -->\n<g transform="translate(-10.25 .15) scale(1.3)">\n<rect x="12" y="5" width="41" height="39" rx="2" fill="#8A949E"/>\n<rect x="13.5" y="6.5" width="38" height="36" rx="2" fill="#24465B"/>\n<rect x="17" y="11" width="31" height="16" rx="1" fill="#1F6FC4"/>\n<!-- Lectura digital 1280, trazada sin depender de una fuente. -->\n<path d="m20 18 2-2v7m4-7h4v3.5h-4V23h4m4-7h4v7h-4Zm0 3.5h4m4-3.5h4v7h-4Z" fill="none" stroke="#E2F2F5" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>\n<path d="M15 29h35" stroke="#8A949E" stroke-width="1.5"/>\n<!-- Teclas numéricas en tres columnas. -->\n<g fill="#E2F2F5">\n<circle cx="34" cy="32" r="1.3"/><circle cx="40" cy="32" r="1.3"/><circle cx="46" cy="32" r="1.3"/>\n<circle cx="34" cy="36" r="1.3"/><circle cx="40" cy="36" r="1.3"/><circle cx="46" cy="36" r="1.3"/>\n<circle cx="34" cy="40" r="1.3"/><circle cx="40" cy="40" r="1.3"/><circle cx="46" cy="40" r="1.3"/>\n<path d="m19 31-1.5 2h3Zm0 9-1.5-2h3Zm-5-4.5 2-1.5v3Zm10 0-2-1.5v3Z"/>\n</g>\n<circle cx="19" cy="35.5" r="1.8" fill="#E56876"/>\n<circle cx="28" cy="32" r="1.3" fill="#E56876"/>\n<circle cx="28" cy="36" r="1.3" fill="#378CE7"/>\n<circle cx="28" cy="40" r="1.3" fill="#F3AD43"/>\n<g fill="#E2F2F5"><circle cx="15.5" cy="8.5" r="1"/><circle cx="49.5" cy="8.5" r="1"/><circle cx="15.5" cy="40.5" r="1"/><circle cx="49.5" cy="40.5" r="1"/></g>\n</g>'

# forraje: dos hojas redondeadas (una en tinte claro) sobre un tallo corto
HOJA = (f'<path d="M16 24 C8 24 4 17 6 9 C14 9 18 16 16 24 Z" fill="#7AD3B8"/>'
        f'<path d="M16 22 C15 12 19 6 27 5 C28 13 24 21 16 22 Z" fill="{VERDE}"/>'
        f'<line x1="16" y1="29" x2="16" y2="21" stroke="{D}" stroke-width="2" stroke-linecap="round"/>'
        f'<line x1="16" y1="21" x2="24" y2="9" stroke="{D}" stroke-width="1.2" stroke-linecap="round"/>')
# grano: espiga de trigo con tres pares de granos y uno de remate
ESPIGA = (f'<line x1="16" y1="30" x2="16" y2="9" stroke="{D}" stroke-width="1.8" stroke-linecap="round"/>'
          + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.2" ry="3.6" fill="{AMBAR}" transform="rotate({r} {x} {y})"/>'
                    for x, y, r in ((12.4, 22, -30), (19.6, 22, 30), (12.4, 16, -30), (19.6, 16, 30),
                                    (13.2, 10.5, -30), (18.8, 10.5, 30)))
          + f'<ellipse cx="16" cy="6.5" rx="2" ry="3.4" fill="{AMBAR}"/>')

# Aplicador de implantes: aguja horizontal, cargador elevado y gatillo ancho.
# Silueta simplificada de la referencia; sin marca ni detalles diminutos.
IMPLANTADOR = (
    '<path fill="#8A949E" d="M1 10.5 2.3 9.8H7.7V11.2H2.3Z"/>'
    '<rect x="6.3" y="9" width="2" height="3" rx="0.7" fill="#24465B"/>'
    '<path fill="#24465B" d="M14 15H18.2L21 27.4Q18.5 29 14.4 28.7'
    'Q13.2 28.5 14.5 27.6Q15.4 27 15.3 25V23.1Q15.3 22.5 14.8 22'
    'Q14.1 21.4 14.8 20.7Q15.4 20 14.8 19.3Q14 18.6 14.7 17.8Q15.4 16.4 14 15Z"/>'
    '<path fill="#E56876" d="M8.9 4Q9.1 3 10.2 3H13.6Q14.5 3 14.5 4V6'
    'Q14.5 8 16.5 8H28.5Q29.5 8 30 9.2L30.6 10.7Q31 12 29.6 12.7'
    'L23 15.6Q20.5 16.6 21.3 19L24 26.4Q24.6 28.2 23.3 28.5L20.4 29'
    'Q19.5 29.2 19.2 28.1L16 18Q15.4 16 13.4 15.8L8.5 15.1'
    'Q7.5 14.9 7.5 13.6V9Z"/>'
    '<rect x="10.3" y="7.7" width="2" height="2.9" rx="0.6" fill="#24465B"/>'
    '<rect x="19.1" y="10.3" width="5.4" height="2.5" rx="0.5" fill="#E2F2F5"/>'
)

def interior_64(nombre):
    """Cuerpo de un SVG de 64 x 64 sin <title>, <desc> ni comentarios (los reescribe generar_svg)."""
    t = re.sub(r"<!--.*?-->|<title.*?</title>|<desc.*?</desc>", "", interior(nombre), flags=re.S)
    return re.sub(r">\s+<", "><", t).strip()


# camion mixer aprobado (viewBox 64): se reutiliza tal cual como cuerpo de la familia
CAMION_MIXER = interior_64("camion-mixer")

BASES = {
    "camion-mixer": (CAMION_MIXER, ROJO),
    "implantador": (IMPLANTADOR, ROJO),
    "hoja": (HOJA, VERDE), "espiga": (ESPIGA, AMBAR),
    "indicador": (INDICADOR, AZUL),
    "seleccionar-todos": (SELECCIONAR_TODOS, AZUL),
    "vaca": (interior("vaca"), BRAHMAN), "cerca": (interior("cerca"), VERDE),
    "camion": (interior("camion"), AMBAR), "calendario": (f'<g transform="scale(0.6667)">{interior("calendario")}</g>', "#F44336"),
    "jeringa": (interior("jeringa"), MORADO), "engranaje": (f'<g transform="scale(0.6667)">{interior("engranaje")}</g>', AZUL),
    "cruz": (CRUZ, ROJO), "nube": (NUBE, AZUL), "mapa": (MAPA, VERDE), "craneo": (CRANEO, BRAHMAN),
    "etiqueta": (ETIQUETA, AMBAR),
    "documento": (DOCUMENTO, AZUL), "usuario": (USUARIO, VERDE), "usuarios": (USUARIOS, VERDE),
    "barras": (f'<g transform="scale(0.6667)">{interior("GraficaBarras")}</g>', VERDE),
    "bascula": (interior("bascula"), AZUL),
    "comedero": (COMEDERO_64, AMBAR), "saco": (SACO, AMBAR), "carrito": (CARRITO, VERDE),
    "lapida": (LAPIDA, ROJO), "matraz": (MATRAZ, MORADO),
    "BaseDatos": (f'<g transform="scale(0.6667)">{interior("BaseDatos")}</g>', MORADO),
    "arete-rfid": (ARETE_RFID, AMBAR), "medidor": (MEDIDOR, AZUL),
    "escudo-gris": (ESCUDO_GRIS, GRIS_CUERNO), "moneda": (MONEDA, VERDE), "prohibido": (PROHIBIDO, ROJO),
    "regla": (REGLA, AMBAR), "tabla-datos": (TABLA_DATOS, VERDE), "grafica-tendencia": (GRAFICA_TENDENCIA, VERDE),
    "grafica-barras-asc": (GRAFICA_BARRAS_ASC, AZUL), "barras-azul": (BARRAS_AZUL, AZUL),
    "billete": (BILLETE, VERDE), "enviar": (ENVIAR, AZUL), "imprimir": (IMPRIMIR, AZUL), "guardar": (GUARDAR, VERDE), "grafico-lineas-ambar": (GRAFICO_LINEAS_AMBAR, AMBAR), "grafico-circular": (GRAFICO_CIRCULAR, AZUL),
}

# (nombre, base, simbolo)  -- simbolo None = base sola
NUEVOS = [
    ("implantador", "implantador", None),
    *[(f"implantador-{s}", "implantador", s)
      for s in ("mas", "menos", "check", "x", "lista", "lupa", "flecha", "reloj", "alerta")],
    ("vaca-calavera", "craneo", None),
    ("documento", "documento", None), ("documento-mas", "documento", "mas"), ("documento-flecha", "documento", "flecha"),
    ("documento-alerta", "documento", "alerta"), ("documento-bajada", "documento", "abajo"),
    ("documento-check", "documento", "check"), ("documento-codigo", "documento", "codigo"),
    ("documento-dinero", "documento", "dolar"),
    ("usuario", "usuario", None), ("usuarios", "usuarios", None), ("usuario-mas", "usuario", "mas"),
    ("usuario-check", "usuario", "check"), ("usuario-dinero", "usuario", "dolar"),
    ("barras-mas", "barras", "mas"), ("barras-dinero", "barras", "dolar"), ("barras-flecha", "barras", "flecha"),
    ("cerca-lupa", "cerca", "lupa"), ("cruz-check", "cruz", "check"), ("cruz-lupa", "cruz", "lupa"),
    ("bascula-lista", "bascula", "lista"),
    ("comedero", "comedero", None), ("comedero-bajada", "comedero", "abajo"),
    ("comedero-subida", "comedero", "arriba"), ("comedero-lupa", "comedero", "lupa"),
    ("saco-alimento", "saco", None), ("saco-flecha", "saco", "flecha"), ("saco-lista", "saco", "lista"),
    ("carrito", "carrito", None), ("carrito-check", "carrito", "check"),
    ("lapida", "lapida", None), ("lapida-alerta", "lapida", "alerta"),
    ("matraz-check", "matraz", "check"), ("matraz-lupa", "matraz", "lupa"), ("matraz-gota", "matraz", "gota"),
    ("matraz-hoja", "matraz", "hoja"), ("matraz-espiga", "matraz", "espiga"),
    ("vaca-x", "vaca", "x"), ("vaca-lupa", "vaca", "lupa"), ("vaca-alerta", "vaca", "alerta"),
    ("vaca-lista", "vaca", "lista"), ("vaca-check", "vaca", "check"), ("vaca-arriba", "vaca", "arriba"),
    ("vaca-abajo", "vaca", "abajo"), ("vaca-estrella", "vaca", "estrella"), ("vaca-dinero", "vaca", "dolar"),
    ("cerca-lista", "cerca", "lista"), ("cerca-menos", "cerca", "menos"),
    ("cerca-flecha", "cerca", "flecha"), ("cerca-pin", "cerca", "pin"), ("cerca-estrella", "cerca", "estrella"),
    ("cerca-reloj", "cerca", "reloj"), ("cerca-x", "cerca", "x"),
    ("cerca-intercambio", "cerca", "intercambio"), ("vaca-salida", "vaca", "salida"),
    ("cruz", "cruz", None), ("cruz-mas", "cruz", "mas"),
    ("jeringa-flecha", "jeringa", "flecha"), ("jeringa-lista", "jeringa", "lista"),
    ("seleccionar-todos", "seleccionar-todos", None), ("carrito-lupa", "carrito", "lupa"), ("vaca-separar", "vaca", "separar"), ("vaca-carrito", "vaca", "carrito"),
    ("documento-carrito", "documento", "carrito"), ("documento-vaca", "documento", "vaca"), ("documento-arete", "documento", "arete"),
    ("hoja", "hoja", None), ("hoja-mas", "hoja", "mas"), ("hoja-menos", "hoja", "menos"),
    ("hoja-check", "hoja", "check"), ("hoja-lupa", "hoja", "lupa"), ("hoja-flecha", "hoja", "flecha"),
    ("espiga", "espiga", None), ("espiga-mas", "espiga", "mas"), ("espiga-menos", "espiga", "menos"),
    ("espiga-check", "espiga", "check"), ("espiga-lupa", "espiga", "lupa"),
    ("vaca-intercambio", "vaca", "intercambio"), ("mapa-flecha", "mapa", "flecha"),
    ("documento-intercambio", "documento", "intercambio"), ("documento-estrella", "documento", "estrella"),
    ("cerca-circulo", "cerca", "circulo"),
    ("indicador", "indicador", None), ("indicador-abajo", "indicador", "abajo"), ("indicador-arriba", "indicador", "arriba"),
    ("medidor-abajo", "medidor", "abajo"), ("usuario-flecha", "usuario", "flecha"),
    ("documento-reloj", "documento", "reloj"), ("calendario-copiar", "calendario", "copiar"),
    ("camion-lista", "camion", "lista"), ("camion-descarga", "camion", "abajo"),
    ("etiqueta", "etiqueta", None), ("etiqueta-mas", "etiqueta", "mas"), ("etiqueta-menos", "etiqueta", "menos"),
    ("etiqueta-check", "etiqueta", "check"), ("etiqueta-x", "etiqueta", "x"),
    ("etiqueta-flecha", "etiqueta", "flecha"), ("etiqueta-lupa", "etiqueta", "lupa"),
    ("etiqueta-alerta", "etiqueta", "alerta"), ("etiqueta-dinero", "etiqueta", "dolar"),
    ("etiqueta-circulo", "etiqueta", "circulo"),
    ("calendario-mas", "calendario", "mas"), ("calendario-menos", "calendario", "menos"),
    ("calendario-reloj", "calendario", "reloj"), ("calendario-check", "calendario", "check"),
    ("calendario-x", "calendario", "x"), ("calendario-lista", "calendario", "lista"),
    ("calendario-flecha", "calendario", "flecha"), ("calendario-lupa", "calendario", "lupa"),
    ("calendario-alerta", "calendario", "alerta"), ("calendario-estrella", "calendario", "estrella"),
    ("mapa", "mapa", None),
    ("engranaje-lista", "engranaje", "lista"),
    ("engranaje-pausa", "engranaje", "pausa"),
    ("nube", "nube", None), ("nube-check", "nube", "check"),
    # los dos de nube ya existian en estilo de linea: se reemplazan por la version plana
    ("nube-x", "nube", "x"), ("nube-flecha", "nube", "flecha"),
    # arete RFID (base propia con las ondas centradas)
    ("arete-rfid", "arete-rfid", None), ("arete-rfid-alerta", "arete-rfid", "alerta"),
    ("arete-rfid-check", "arete-rfid", "check"), ("arete-rfid-flecha", "arete-rfid", "flecha"),
    ("arete-rfid-lista", "arete-rfid", "lista"), ("arete-rfid-lupa", "arete-rfid", "lupa"),
    ("arete-rfid-mas", "arete-rfid", "mas"), ("arete-rfid-menos", "arete-rfid", "menos"),
    ("arete-rfid-x", "arete-rfid", "x"),
    # base de datos (filas lilas): se genera desde BaseDatos.svg, que debe quedar sin insignia
    ("BaseDatos-mas", "BaseDatos", "mas"), ("BaseDatos-menos", "BaseDatos", "menos"),
    ("BaseDatos-check", "BaseDatos", "check"), ("BaseDatos-x", "BaseDatos", "x"),
    ("BaseDatos-lupa", "BaseDatos", "lupa"), ("BaseDatos-flecha", "BaseDatos", "flecha"),
    ("BaseDatos-lista", "BaseDatos", "lista"), ("BaseDatos-alerta", "BaseDatos", "alerta"),
    # documentos de reporte: insignia roja (sanidad / ordinarios) o azul (crianza / reparto)
    ("documento-mas-rojo", "documento", "mas"),
    ("documento-check-rojo", "documento", "check"), ("documento-flecha-rojo", "documento", "flecha"),
    ("documento-mas-azul", "documento", "mas"),
    # iconos planos normalizados (antes de linea o con degradado) y graficas del mockup
    ("medidor", "medidor", None), ("escudo-gris", "escudo-gris", None),
    ("moneda-check", "moneda", "check"), ("prohibido", "prohibido", None), ("regla", "regla", None),
    ("TablaDatos", "tabla-datos", None), ("tabla-dinero", "tabla-datos", "dolar"), ("GraficaTendencia", "grafica-tendencia", None),
    ("GraficaBarrasAscendentes", "grafica-barras-asc", None),
    ("billete", "billete", None), ("billete-mas", "billete", "mas"), ("billete-check", "billete", "check"),
    ("billete-flecha", "billete", "flecha"),
    ("Enviar", "enviar", None), ("Imprimir", "imprimir", None), ("Guardar", "guardar", None), ("GuardarCerrar", "guardar", "check"), ("barras-azul", "barras-azul", None), ("grafico-lineas-ambar", "grafico-lineas-ambar", None),
    ("grafico-circular", "grafico-circular", None),
    # variantes de indicador y medidor (arriba/abajo ya existian)
    *[(f"{b}-{s}", b, s)
      for b in ("indicador", "medidor")
      for s in ("mas", "menos", "check", "x", "lista", "lupa", "alerta", "reloj")],
    ("medidor-arriba", "medidor", "arriba"),
    ("indicador-flecha", "indicador", "flecha"),
    # camion mixer (base aprobada en camion-mixer.svg; no se regenera) y su familia
    *[(f"camion-mixer-{s}", "camion-mixer", s)
      for s in ("mas", "menos", "check", "x", "lista", "lupa", "flecha", "reloj", "alerta", "documento")],
    # comedero: ajuste en ambos sentidos
    ("comedero-arribaYabajo", "comedero", "arribaYabajo"),
]
# colores de insignia que no salen de la tabla por simbolo
COLORES_INSIGNIAS_VACA.update({
    "tabla-dinero": AMBAR, "jeringa-lista": AZUL, "carrito-lupa": AZUL, "vaca-separar": AZUL, "vaca-carrito": VERDE, "documento-carrito": VERDE, "documento-vaca": VERDE, "documento-arete": AMBAR, "hoja-mas": VERDE, "hoja-check": VERDE, "hoja-menos": ROJO, "hoja-lupa": AZUL,
    "espiga-mas": VERDE, "espiga-check": VERDE, "espiga-menos": ROJO, "espiga-lupa": AZUL, "vaca-intercambio": AZUL, "mapa-flecha": AZUL,
    "documento-intercambio": AZUL, "documento-estrella": AMBAR, "cerca-circulo": MORADO, "indicador-abajo": AZUL, "indicador-arriba": VERDE,
    "medidor-abajo": AZUL, "usuario-flecha": AZUL, "documento-reloj": MORADO, "calendario-copiar": AZUL, "cerca-reloj": MORADO, "cerca-x": ROJO, "cerca-intercambio": AZUL, "vaca-salida": AZUL,
    "documento-mas-rojo": ROJO, "documento-check-rojo": ROJO,
    "documento-flecha-rojo": ROJO, "documento-mas-azul": AZUL,
    "arete-rfid-x": "#B9472B",
    "matraz-hoja": VERDE, "matraz-espiga": AMBAR,  # insignia con el color del forraje / grano
    "cerca-pin": ROJO,  # pin blanco sobre circulo rojo (pedido de diseno)
    "GuardarCerrar": AZUL,  # insignia azul para distinguirla del cuerpo verde  # asi estaba en el kit; unificar con ROJO si se decide
})


# bases dibujadas en 64 x 64: (titulo, escala y desplazamiento del cuerpo cuando lleva insignia)
BASES_64 = {
    "comedero": ("Comedero de concreto", "translate(1 -6) scale(.78)"),
    "indicador": ("Indicador digital de pesaje", "translate(0 -1) scale(.78)"),
    "camion-mixer": ("Camión mixer de alimento", "translate(0 1) scale(.78)"),
}


def generar_svg(nombre, base, simbolo):
    cuerpo, color = BASES[base]
    if base == "implantador" and simbolo:
        cuerpo = '<g transform="translate(0 1) scale(0.86)">' + cuerpo + '</g>'
    color_insignia = MORADO if simbolo == "reloj" else COLORES_INSIGNIAS_VACA.get(nombre, color)
    extra = insignia(simbolo, color_insignia) if simbolo else ""
    if base in BASES_64:
        titulo, ajuste = BASES_64[base]
        if simbolo:
            cuerpo = f'<g transform="{ajuste}">' + cuerpo + '</g>'
            extra = '<g transform="scale(2)">' + extra + '</g>'
        titulo += (": " + simbolo if simbolo else "")
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 64 64" role="img" aria-labelledby="title">'
                + '<title id="title">' + titulo + '</title>' + cuerpo + extra + '</svg>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">'
            + cuerpo + extra + '</svg>')


def main():
    for nombre, base, simbolo in NUEVOS:
        svg = generar_svg(nombre, base, simbolo)
        ruta = os.path.join(KIT, "svg", nombre + ".svg")
        open(ruta, "w", encoding="utf-8").write(svg)

    # Importar viene de Icons8 con un rosa fuera de paleta: se lleva al rojo del kit
    ruta = os.path.join(KIT, "svg", "Importar.svg")
    texto = open(ruta, encoding="utf-8").read().replace("#E91E63", ROJO)
    open(ruta, "w", encoding="utf-8").write(texto)

    print(len(NUEVOS), "iconos generados")
    import generar_reportes  # -reporte de cada familia, a partir de sus variantes ya generadas
    generar_reportes.main()
    import generar_vista_previa  # la vista previa vive en su propio script
    generar_vista_previa.main()


if __name__ == "__main__":
    main()
