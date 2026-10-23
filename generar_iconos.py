#!/usr/bin/env python3
"""Generador del kit de iconos 32x32 de ControlGanadero.

Cada icono = pictograma base + insignia opcional (esquina inferior derecha),
coloreado segun la categoria del modulo. Salida:
    svg/<control>.svg        (fuente vectorial editable)
    png/<control>.png        (32x32, via Inkscape)
    vista_previa.html        (hoja de contacto)

Uso:  python generar_iconos.py
Los archivos se nombran igual que el control DevExpress (ej. bbiListaReses).
"""
import html
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
INKSCAPE = r"C:\Program Files\Inkscape\bin\inkscape.exe"

# categoria -> (color principal, tinte claro)
CAT = {
    "ganado":   ("#2F7D4A", "#D6EBDD"),
    "sanidad":  ("#C23B35", "#F6D9D6"),
    "alimento": ("#C47A12", "#F7E3BE"),
    "reporte":  ("#2F6DB5", "#D3E2F4"),
    "comercial": ("#1F8A8A", "#CDEBEB"),
    "sistema":  ("#5A6B7E", "#DDE3EA"),
}
CAT_NOMBRE = {
    "ganado": "Ganado y corrales", "sanidad": "Sanidad e implantes",
    "alimento": "Alimentación y planta", "reporte": "Reportes e indicadores",
    "comercial": "Compras y ventas", "sistema": "Sistema y catálogos",
}

# ---------------------------------------------------------------- pictogramas
# {A} = color principal, {T} = tinte. Rejilla 32x32, trazo 2 redondeado.
def _gear():
    dientes = "".join(
        f'<path d="M16 3.5 V8" transform="rotate({a} 16 16)" stroke-width="4.5" stroke-linecap="butt"/>'
        for a in range(0, 360, 45))
    return dientes + '<circle cx="16" cy="16" r="9" fill="{T}"/><circle cx="16" cy="16" r="3.5"/>'

BASES = {
    "cow": ('<path d="M8 10 C4 9 3 6 4 4 M24 10 C28 9 29 6 28 4"/>'
            '<path d="M8 12 L2.5 12 L4 16.5 L9 16 M24 12 L29.5 12 L28 16.5 L23 16" fill="{T}"/>'
            '<path d="M9 8 H23 L24 18 C24 23 21 27 16 27 C11 27 8 23 8 18 Z" fill="#fff"/>'
            '<ellipse cx="16" cy="22" rx="5.5" ry="3.8" fill="{T}"/>'
            '<path d="M14 22 H14.2 M18 22 H18.2 M12 15 H12.2 M20 15 H20.2" stroke-width="2.6"/>'),
    "list": ('<path d="M11 8 H27 M11 16 H27 M11 24 H27"/>'
             '<circle cx="5.5" cy="8" r="1.6" fill="{A}"/><circle cx="5.5" cy="16" r="1.6" fill="{A}"/>'
             '<circle cx="5.5" cy="24" r="1.6" fill="{A}"/>'),
    "doc": ('<path d="M8 3 H20 L26 9 V29 H8 Z" fill="#fff"/><path d="M20 3 V9 H26" fill="{T}"/>'
            '<path d="M12 15 H22 M12 20 H22 M12 25 H18"/>'),
    "bars": ('<path d="M4 28 H28"/><rect x="6" y="16" width="5" height="12" fill="{T}"/>'
             '<rect x="13.5" y="7" width="5" height="21" fill="{A}"/><rect x="21" y="12" width="5" height="16" fill="{T}"/>'),
    "line": ('<path d="M4 4 V28 H28"/><path d="M8 22 L14 15 L19 19 L27 8"/>'
             '<circle cx="14" cy="15" r="1.8" fill="{T}"/><circle cx="19" cy="19" r="1.8" fill="{T}"/>'
             '<circle cx="27" cy="8" r="1.8" fill="{T}"/>'),
    "pie": ('<circle cx="16" cy="16" r="12" fill="{T}"/><path d="M16 16 V4 A12 12 0 0 1 28 16 Z" fill="{A}"/>'),
    "gauge": ('<path d="M4 24 A12 12 0 0 1 28 24" fill="{T}"/><path d="M4 24 H28"/>'
              '<path d="M16 24 L21 13"/><circle cx="16" cy="24" r="2" fill="{A}"/>'),
    "fence": ('<path d="M3 12 H29 M3 21 H29"/><path d="M7 6 V28 M16 6 V28 M25 6 V28" stroke-width="3" fill="none"/>'
              '<path d="M7 6 V28 M16 6 V28 M25 6 V28" stroke="{T}" stroke-width="1" fill="none"/>'),
    "syringe": ('<g transform="rotate(45 16 16)"><path d="M11 9 H21 V23 H11 Z" fill="#fff"/>'
                '<path d="M13 15 H19 V21 H13 Z" fill="{T}"/><path d="M16 3 V9 M12 3 H20"/>'
                '<path d="M16 23 V30"/><path d="M11 13 H14 M11 17 H14" stroke-width="1.4"/></g>'),
    "bottle": ('<path d="M10 4 H22 V9 H10 Z" fill="{T}"/><path d="M9 9 H23 V28 H9 Z" fill="#fff"/>'
               '<path d="M9 15 H23 V24 H9 Z" fill="{T}"/><path d="M16 16.5 V22.5 M13 19.5 H19" stroke-width="1.8"/>'),
    "cross": ('<path d="M12 4 H20 V12 H28 V20 H20 V28 H12 V20 H4 V12 H12 Z" fill="{T}"/>'),
    "scale": ('<path d="M3 22 H29 V28 H3 Z" fill="{T}"/><path d="M8 22 V18 A8 8 0 0 1 24 18 V22" fill="#fff"/>'
              '<path d="M16 18 L19.5 11.5"/><circle cx="16" cy="18" r="1.6" fill="{A}"/>'),
    "sack": ('<path d="M11 4 H21 L19 9 C26 12 27.5 20 25.5 25 C24.5 27.5 22.5 28.5 20 28.5 H12 C9.5 28.5 7.5 27.5 6.5 25 '
             'C4.5 20 6 12 13 9 Z" fill="{T}"/><path d="M12.5 8 H19.5"/>'
             '<path d="M9 17 H23 V24 H9 Z" fill="#fff" stroke-width="1.6"/>'),
    "trough": ('<path d="M3 15 H29 L25.5 27 H6.5 Z" fill="#fff"/>'
               '<path d="M6 15 C8 8 13 9 16 11 C19 9 24 8 26 15 Z" fill="{T}"/>'),
    "truck": ('<path d="M2 9 H18 V23 H2 Z" fill="{T}"/><path d="M18 13 H25 L30 18 V23 H18 Z" fill="#fff"/>'
              '<circle cx="8" cy="24" r="3.2" fill="#fff"/><circle cx="24" cy="24" r="3.2" fill="#fff"/>'),
    "coin": ('<circle cx="16" cy="16" r="12.5" fill="{T}"/>'
             '<path d="M20 12 C20 8.5 12 8.5 12 12.7 C12 16.5 20 15.5 20 19.5 C20 23.5 12 23.5 12 20 M16 6.5 V25.5"/>'),
    "user": ('<circle cx="16" cy="10.5" r="5.5" fill="{T}"/>'
             '<path d="M5.5 28.5 C5.5 20.5 10.5 18 16 18 C21.5 18 26.5 20.5 26.5 28.5 Z" fill="#fff"/>'),
    "users": ('<path d="M20 5.5 A4.5 4.5 0 1 1 20 14 M21 17 C26 17 29.5 20 29.5 27" />'
              '<circle cx="12" cy="11" r="4.8" fill="{T}"/>'
              '<path d="M2.5 28 C2.5 21 7 18 12 18 C17 18 21.5 21 21.5 28 Z" fill="#fff"/>'),
    "shield": ('<path d="M16 3 L27 7 V15 C27 22 22 27 16 29 C10 27 5 22 5 15 V7 Z" fill="{T}"/>'
               '<path d="M11 16 L15 20 L22 12"/>'),
    "gear": _gear(),
    "pin": ('<path d="M16 29.5 C16 29.5 6.5 20 6.5 13 A9.5 9.5 0 0 1 25.5 13 C25.5 20 16 29.5 16 29.5 Z" fill="{T}"/>'
            '<circle cx="16" cy="13" r="3.5" fill="#fff"/>'),
    "map": ('<path d="M3 7 L11 4 L21 8 L29 5 V25 L21 28 L11 24 L3 27 Z" fill="#fff"/>'
            '<path d="M11 4 V24 M21 8 V28"/><path d="M11 4 L21 8 V28 L11 24 Z" fill="{T}" stroke="none"/>'
            '<path d="M11 4 V24 M21 8 V28"/>'),
    "calendar": ('<rect x="4" y="6" width="24" height="22" rx="2.5" fill="#fff"/><path d="M4 12.5 H28" />'
                 '<path d="M4 8.5 A2.5 2.5 0 0 1 6.5 6 H25.5 A2.5 2.5 0 0 1 28 8.5 V12.5 H4 Z" fill="{T}"/>'
                 '<path d="M10 3 V8 M22 3 V8"/>'
                 '<path d="M9 18 H9.2 M16 18 H16.2 M23 18 H23.2 M9 23 H9.2 M16 23 H16.2" stroke-width="2.6"/>'),
    "eartag": ('<circle cx="16" cy="6" r="2.5" fill="#fff"/><path d="M16 8.5 V11"/>'
               '<rect x="7" y="11" width="18" height="17" rx="3.5" fill="{T}"/>'
               '<path d="M12 17 H20 M12 22 H20" stroke-width="1.8"/>'),
    "cart": ('<path d="M2.5 5 H7.5 L11 20 H25.5"/><path d="M9 9 H29 L25.5 20 H11 Z" fill="{T}"/>'
             '<circle cx="13" cy="26" r="2.2" fill="#fff"/><circle cx="23" cy="26" r="2.2" fill="#fff"/>'),
    "flask": ('<path d="M12 3 H20 M14 3 V13 L6 25.5 C4.8 27.5 6 29 8 29 H24 C26 29 27.2 27.5 26 25.5 L18 13 V3" fill="#fff"/>'
              '<path d="M9.2 21.5 H22.8 L26 26 C27 27.8 26 29 24 29 H8 C6 29 5 27.8 6 26 Z" fill="{T}"/>'),
    "tomb": ('<path d="M7.5 28 V14 A8.5 8.5 0 0 1 24.5 14 V28 Z" fill="{T}"/><path d="M3.5 28 H28.5"/>'
             '<path d="M16 11 V21 M12 15 H20"/>'),
    "drop": ('<path d="M16 3 C16 3 6.5 13.5 6.5 19.5 A9.5 9.5 0 0 0 25.5 19.5 C25.5 13.5 16 3 16 3 Z" fill="{T}"/>'
             '<path d="M11.5 20.5 A4.5 4.5 0 0 0 15 25"/>'),
    "cloud": ('<path d="M9 26 A6.5 6.5 0 0 1 9 13 A8.5 8.5 0 0 1 25 12.5 A6.8 6.8 0 0 1 23.5 26 Z" fill="{T}"/>'),
    "clock": ('<circle cx="16" cy="16" r="12.5" fill="{T}"/><path d="M16 8.5 V16 L21.5 19.5"/>'),
    "pause": ('<circle cx="16" cy="16" r="12.5" fill="{T}"/><path d="M12.5 11 V21 M19.5 11 V21" stroke-width="3"/>'),
    "ruler": ('<path d="M2.5 11 H29.5 V21 H2.5 Z" fill="{T}"/><path d="M8 11 V16 M13 11 V15 M18 11 V16 M23 11 V15"/>'),
    "percent": ('<circle cx="9.5" cy="9.5" r="4" fill="{T}"/><circle cx="22.5" cy="22.5" r="4" fill="{T}"/>'
                '<path d="M25 6 L7 26"/>'),
    "ban": ('<circle cx="16" cy="16" r="12.5" fill="{T}"/><path d="M7.2 7.2 L24.8 24.8"/>'),
    "transfer": ('<path d="M4 11 H26 M20.5 5.5 L26 11 L20.5 16.5 M28 21 H6 M11.5 15.5 L6 21 L11.5 26.5"/>'),
    "tag": ('<path d="M4 4 H16.5 L28 15.5 L15.5 28 L4 16.5 Z" fill="{T}"/><circle cx="10" cy="10" r="2.2" fill="#fff"/>'),
    "folder": ('<path d="M3 7 H12 L15 10.5 H29 V26 H3 Z" fill="{T}"/><path d="M3 14 H29"/>'),
    "db": ('<path d="M5.5 8 V24 C5.5 28 26.5 28 26.5 24 V8" fill="{T}"/>'
           '<ellipse cx="16" cy="8" rx="10.5" ry="4" fill="#fff"/>'
           '<path d="M5.5 16 C5.5 20 26.5 20 26.5 16"/>'),
    "exit": ('<path d="M13 4 H5 V28 H13"/><path d="M12 16 H28 M23 11 L28 16 L23 21"/>'),
    "help": ('<circle cx="16" cy="16" r="12.5" fill="{T}"/>'
             '<path d="M12 13 C12 8 20 8 20 13 C20 16.5 16 16 16 19.5 M16 23.5 H16.2"/>'),
}

# --------------------------------------------------------------- insignias
# Simbolos centrados en (0,0), caben en radio ~4.
BADGES = {
    "plus": "M0 -3.2 V3.2 M-3.2 0 H3.2", "minus": "M-3.2 0 H3.2",
    "check": "M-3.2 0.5 L-1 2.7 L3.2 -2.6", "x": "M-2.6 -2.6 L2.6 2.6 M2.6 -2.6 L-2.6 2.6",
    "exclam": "M0 -3.6 V0.8 M0 3.2 V3.3",
    "dollar": "M2.2 -2 C2.2 -4.2 -2.2 -4.2 -2.2 -1.4 C-2.2 1.2 2.2 0.2 2.2 2.8 C2.2 4.8 -2.2 4.8 -2.2 2.6 M0 -5 V5",
    "arrow": "M-3.2 0 H3.2 M0.6 -2.6 L3.2 0 L0.6 2.6",
    "up": "M0 3.2 V-3.2 M-2.6 -0.6 L0 -3.2 L2.6 -0.6", "down": "M0 -3.2 V3.2 M-2.6 0.6 L0 3.2 L2.6 0.6",
    "search": "M0.9 0.9 L3.4 3.4",   # + circulo, ver abajo
    "list": "M-3 -2.6 H3 M-3 0 H3 M-3 2.6 H3",
    "code": "M-1.6 -2.6 L-3.6 0 L-1.6 2.6 M1.6 -2.6 L3.6 0 L1.6 2.6",
}

def badge_svg(nombre):
    if nombre is None:
        return ""
    if nombre == "star":
        return ('<path d="M24.5 17.5 L26.4 22.6 L31.5 24.5 L26.4 26.4 L24.5 31.5 L22.6 26.4 L17.5 24.5 L22.6 22.6 Z" '
                'fill="{A}" stroke="#fff" stroke-width="1.2"/>')
    extra = '<circle cx="-0.9" cy="-0.9" r="2.5" fill="none"/>' if nombre == "search" else ""
    return ('<circle cx="24.5" cy="24.5" r="6.7" fill="#fff" stroke="{A}" stroke-width="1.8"/>'
            f'<g transform="translate(24.5 24.5)" stroke-width="1.8">{extra}<path d="{BADGES[nombre]}"/></g>')

def icono_svg(cat, base, badge):
    A, T = CAT[cat]
    cuerpo = BASES[base]
    if badge:
        cuerpo = f'<g transform="translate(0.4 0.4) scale(0.86)">{cuerpo}</g>'
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" '
           'fill="none" stroke="{A}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
           + cuerpo + badge_svg(badge) + '</svg>')
    return svg.replace("{A}", A).replace("{T}", T)

# ------------------------------------------------- botones (control, texto, categoria, base, insignia)
ICONOS = [
    # Ganado y corrales
    ("bbiListaReses", "Lista de Reses", "ganado", "cow", "list"),
    ("bbiBuscadorReses", "Buscador de Reses", "ganado", "cow", "search"),
    ("bbiListaResesInactivos", "Reses Inactivas", "ganado", "cow", "minus"),
    ("bbiListaResesSinRegistro", "Reses sin Registrar", "ganado", "cow", "exclam"),
    ("bbiResesSinRegistro", "Reses Sin Registro", "ganado", "cow", "exclam"),
    ("bbiListaResesFeedLot", "Reses Feedlot", "ganado", "trough", "up"),
    ("bbiListaResesCrianza", "Reses Crianza", "ganado", "cow", "plus"),
    ("bbiListaResesDesarrollo", "Reses Desarrollo", "ganado", "cow", "up"),
    ("bbiListaResesMaquila", "Reses Maquila", "ganado", "cow", "arrow"),
    ("bbiExistenciaGanado", "Existencia Ganado", "ganado", "cow", "check"),
    ("bbiNacimientos", "Nacimientos", "ganado", "cow", "star"),
    ("bbiAltasDestete", "Altas por Destete", "ganado", "cow", "down"),
    ("bbiLoteCrianza", "Lote de Crianza", "ganado", "fence", "star"),
    ("bbiFormacionCorrales", "Formacion de Corrales", "ganado", "fence", "plus"),
    ("bbiListaCorrales", "Lista de Corrales", "ganado", "fence", "list"),
    ("bbiResumenCorrales", "Resumen Corrales", "ganado", "fence", "search"),
    ("bbiCorralesAux", "Corrales Auxiliares", "ganado", "fence", "minus"),
    ("bbiMovimientoCorrales", "Movimiento en Corrales", "ganado", "fence", "arrow"),
    ("btnCierreFormacion", "Cierres de Formacion", "ganado", "fence", "check"),
    ("bbiMovimientosPorLote", "Movimientos por Lote", "ganado", "transfer", None),
    ("bbiTraslado", "Traslado", "ganado", "transfer", "arrow"),
    ("btnAreasTrabajo", "Areas de Trabajo", "ganado", "pin", None),
    ("bbiZonas", "Zonas", "ganado", "map", None),
    ("bbiDistancias", "Distancias", "ganado", "ruler", None),
    ("BarButtonItem185", "Calendario", "ganado", "calendar", None),
    ("bbiPlanDietas", "Plan de Dietas", "ganado", "calendar", "plus"),
    ("bbiDeteccionesElectronicos", "Detecciones de Aretes", "ganado", "eartag", "search"),
    ("bbiMortalidadReses", "Mortalidad de Reses", "ganado", "tomb", None),
    ("bbiReparto", "Reparto", "ganado", "truck", "down"),
    ("bbiListaRecepciones", "Lista de Recepcion", "ganado", "truck", "list"),
    ("bbiTransportistas", "Transportistas", "ganado", "truck", None),
    # Sanidad e implantes
    ("bbiDeteccion", "Detección", "sanidad", "cross", "search"),
    ("bbiEvaluacionDeteccion", "Evaluacion de Deteccion", "sanidad", "cross", "check"),
    ("bbiEnfermeria", "Enfermeria", "sanidad", "cross", None),
    ("BarButtonItem207", "Enfermeria", "sanidad", "cross", None),
    ("bbiSanidadCrianza", "Sanidad (Crianza)", "sanidad", "cross", "plus"),
    ("bbiProductos", "Productos", "sanidad", "bottle", None),
    ("bbiProtocolos", "Protocolos", "sanidad", "doc", "check"),
    ("btnProtocolosInicio", "Protocolos de Inicio", "sanidad", "doc", "arrow"),
    ("bbiCausasSanidad", "Causas de Deteccion", "sanidad", "doc", "exclam"),
    ("BarButtonItem203", "Causas", "sanidad", "doc", "exclam"),
    ("BarButtonItem204", "Causas", "sanidad", "doc", "exclam"),
    ("BarButtonItem205", "Causas", "sanidad", "doc", "exclam"),
    ("bbiCausasMuerte", "Causas de Muerte", "sanidad", "tomb", "exclam"),
    ("bbiCausaOrdinarioVenta", "Causas de Ordinarios/Venta", "sanidad", "tag", "exclam"),
    ("bbiImplantes", "Implantes", "sanidad", "syringe", None),
    ("BarButtonItem193", "Reeimplantes", "sanidad", "syringe", "arrow"),
    ("bbiImplantadores", "Implantadores", "sanidad", "user", "plus"),
    ("bbiEvaluacionImplantes", "Evaluacion de Implantes", "sanidad", "syringe", "check"),
    ("bbiHistoricoImplantes", "Historico de Implantes", "sanidad", "syringe", "list"),
    ("bbiReporteImplantes", "Reporte de Implantes", "sanidad", "doc", "plus"),
    ("bbiReporteRechazos", "Reporte de Rechazos", "sanidad", "ban", None),
    ("bbiImproductivos", "Reporte de Ordinarios", "sanidad", "doc", "down"),
    ("bbiCalidadAgua", "Calidad de Agua", "sanidad", "drop", None),
    ("bbiControlCalidad", "Control de Calidad", "sanidad", "flask", "check"),
    ("bbiReporteCalidad", "Pruebas a Formulas", "sanidad", "flask", "search"),
    # Alimentación y planta
    ("bbiAlimentos", "Alimentos", "alimento", "sack", None),
    ("bbiDietas", "Lista de Dietas", "alimento", "sack", "list"),
    ("bbiListaRutasDieta", "Rutas de Dietas", "alimento", "sack", "arrow"),
    ("bbiAlimentacion", "Alimentación", "alimento", "trough", None),
    ("BarButtonItem181", "Alimentación", "alimento", "trough", None),
    ("bbiConsumo", "Consumo", "alimento", "trough", "down"),
    ("bbiListaLecturas", "Lecturas", "alimento", "trough", "search"),
    ("bbiGraficoAlimentacion", "Grafico de Alimentacion", "alimento", "line", None),
    ("bbiGraficaAlimento", "Graficas (Alimento)", "alimento", "line", None),
    ("bbiPesajeMateriaPrima", "Pesaje de Materia Prima", "alimento", "scale", None),
    ("bbiReportePesaje", "Reporte de Pesaje", "alimento", "scale", "list"),
    ("BarButtonItem196", "Reporte de Pesaje", "alimento", "scale", "list"),
    ("bbiCalibraciones", "Calibraciones", "alimento", "scale", "check"),
    ("bbiPorcentajes", "Porcentajes de Servicio", "alimento", "percent", None),
    ("bbiListaEquipos", "Lista de Equipos", "alimento", "gear", "list"),
    ("bbiParoEquipos", "Paro de Equipos", "alimento", "pause", None),
    ("bbiOperadores", "Operadores", "alimento", "user", "check"),
    # Reportes e indicadores
    ("bbiCentroReportes", "Centro de Reportes", "reporte", "pie", None),
    ("bbiReporteGerencial", "Reporte Gerencial", "reporte", "bars", "up"),
    ("bbiGraficasGerencial", "Graficas Gerenciales", "reporte", "bars", None),
    ("bbiGraficas", "Graficas", "reporte", "line", None),
    ("bbiListaIndicadores", "Indicadores", "reporte", "gauge", None),
    ("bbiReporteReparto", "Reporte de Reparto", "reporte", "doc", "arrow"),
    ("bbiReporteCrianza", "Reporte de Crianza", "reporte", "doc", "plus"),
    ("bbiConsolidado", "Consolidado", "reporte", "bars", "plus"),
    ("bbiFormatosBA", "Formatos BA", "reporte", "doc", None),
    ("bbi", "Archivos XML", "reporte", "doc", "code"),
    ("bbiRemisiones", "Remisiones", "reporte", "doc", "arrow"),
    # Compras y ventas
    ("bbiCompras", "Compras de Ganado", "comercial", "cart", None),
    ("bbiComprasProgramadores", "Compras de Programadores", "comercial", "cart", "check"),
    ("bbiDinamicoCompras", "Dinamico de Compras", "comercial", "bars", "dollar"),
    ("bbiCompradores", "Compradores", "comercial", "user", "dollar"),
    ("bbiDueños", "Dueños", "comercial", "users", None),
    ("bbiLiquidaciones", "Liquidaciones", "comercial", "coin", "check"),
    ("bbiReciboPagos", "Recibo de Pagos", "comercial", "doc", "dollar"),
    ("bbiVentas", "Venta de Ordinarios", "comercial", "tag", "dollar"),
    ("bbiResesVenta", "Reses Vendidas", "comercial", "cow", "dollar"),
    # Sistema y catálogos
    ("bbiUsers", "Users", "sistema", "user", None),
    ("bbiRoles", "Roles", "sistema", "shield", None),
    ("sRol", "Rol", "sistema", "shield", None),
    ("sBase", "Base datos", "sistema", "db", None),
    ("bsiC_Sanidad", "Catalogos (Sanidad)", "sistema", "folder", None),
    ("bsiC_PlantaAlimentos", "Catalogos (Planta)", "sistema", "folder", None),
    ("bsiC_Procesos", "Catalogos (Procesos)", "sistema", "folder", None),
    ("BarSubItem1", "Catalogos", "sistema", "folder", None),
    ("BarSubItem2", "Catalogos", "sistema", "folder", None),
    ("BarSubItem3", "Catalogos", "sistema", "folder", None),
    ("bbiConfigurarOffline", "Configurar Offline", "sistema", "cloud", "check"),
    ("bbiSistemaOffline", "Sistema Offline", "sistema", "cloud", "x"),
    ("siStatus", "Conexion Servidor", "sistema", "cloud", "arrow"),
    ("iHelp", "Help", "sistema", "help", None),
    ("iExit", "Exit", "sistema", "exit", None),
]


def main():
    nombres = [i[0] for i in ICONOS]
    assert len(nombres) == len(set(nombres)), "controles duplicados"
    for d in ("svg", "png"):
        os.makedirs(os.path.join(AQUI, d), exist_ok=True)

    rutas = []
    for ctl, _txt, cat, base, badge in ICONOS:
        ruta = os.path.join(AQUI, "svg", ctl + ".svg")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(icono_svg(cat, base, badge))
        rutas.append(ruta)

    if os.path.exists(INKSCAPE):
        for k in range(0, len(rutas), 25):
            subprocess.run([INKSCAPE, "--export-type=png", "--export-width=32", "--export-height=32",
                            "--export-filename=-" if False else "--export-overwrite"] + rutas[k:k + 25],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Inkscape deja el PNG junto al SVG: moverlo a png/
        for r in rutas:
            png = r[:-4] + ".png"
            os.replace(png, os.path.join(AQUI, "png", os.path.basename(png)))
    else:
        print("Inkscape no encontrado: solo se generaron los SVG", file=sys.stderr)

    # hoja de contacto
    secciones = []
    for cat, titulo in CAT_NOMBRE.items():
        celdas = "".join(
            f'<figure><img src="png/{c}.png" width="32" height="32" alt="{html.escape(t)}">'
            f'<figcaption><b>{html.escape(t)}</b><br><code>{html.escape(c)}</code></figcaption></figure>'
            for c, t, ct, _b, _g in ICONOS if ct == cat)
        secciones.append(f'<h2 style="border-color:{CAT[cat][0]}">{titulo}</h2><div class="g">{celdas}</div>')
    with open(os.path.join(AQUI, "vista_previa.html"), "w", encoding="utf-8") as f:
        f.write('<!doctype html><meta charset="utf-8"><title>Kit de iconos ControlGanadero</title>'
                '<style>body{font:13px Segoe UI,sans-serif;margin:24px;background:#fafafa;color:#222}'
                'h2{border-bottom:3px solid;padding-bottom:4px;margin-top:32px}'
                '.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px}'
                'figure{margin:0;display:flex;gap:10px;align-items:center;background:#fff;border:1px solid #e3e3e3;'
                'border-radius:6px;padding:8px}img{flex:none}figcaption{line-height:1.3}code{color:#777;font-size:11px}'
                '</style><h1>Kit de iconos 32×32 — ControlGanadero</h1>'
                f'<p>{len(ICONOS)} iconos. Nombre de archivo = nombre del control en FrmMain.</p>' + "".join(secciones))
    print(f"{len(ICONOS)} iconos generados en {AQUI}")


if __name__ == "__main__":
    main()
