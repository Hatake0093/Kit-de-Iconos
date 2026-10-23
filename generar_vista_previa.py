#!/usr/bin/env python3
"""Vista previa de Kit_semantico: rasteriza los SVG que no tengan PNG y
escribe Kit_semantico/vista_previa.html agrupado por familia de nombre.

Uso: python generar_vista_previa.py
"""
import csv
import html
import json
import os
import re
import subprocess
import sys
from generar_familias_corrales import entradas as entradas_corrales

AQUI = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(AQUI, "simulador de control ganadero", "Kit_semantico")
INKSCAPE = r"C:\Program Files\Inkscape\bin\inkscape.exe"
# Secciones de la vista previa, en orden. Cada una lista las familias (primera palabra del nombre, sin
# plural) y/o los iconos sueltos que le pertenecen. Lo que no aparezca aqui queda en "Otros".
SECCIONES = {
    "Ganado": {"familias": "vaca arete etiqueta", "iconos": "lapida lapida-alerta AsignarArete carnic"},
    "Partos y reproducción": {"familias": "ternero huella crianza"},
    "Corrales y finca": {"familias": "corral cerca mapa"},
    "Alimentación": {"familias": "comedero saco hoja espiga"},
    "Medición y pesaje": {"familias": "bascula indicador medidor regla porcentaje"},
    "Sanidad": {"familias": "jeringa implantador botiquin cruz frasco"},
    "Laboratorio": {"familias": "laboratorio matraz"},
    "Compras, pagos y transporte": {"familias": "carrito billete moneda camion"},
    "Documentos": {"familias": "documento"},
    "Calendario y tiempo": {"familias": "calendario", "iconos": "LineaTiempo"},
    "Gráficas": {"familias": "grafica barra",
                 "iconos": "AgregarGrafica EditarGrafica TendenciaPositiva TendenciaNegativa"},
    "Datos y nube": {"familias": "base nube"},
    "Usuarios y seguridad": {"familias": "usuario escudo", "iconos": "Usuarios2"},
    "Configuración": {"familias": "engranaje"},
    "Flechas": {"familias": "flecha"},
    "Edición y acciones": {"familias": "agregar eliminar cambiar",
                           "iconos": "Actualizar Deshacer Duplicar Editar Nuevo Rehacer Sincronizar "
                                     "seleccionar-todos Enviar FlechaDeshacer FlechaRehacer FlechaDescargar FlechaSubir"},
    "Búsqueda, filtros y orden": {"familias": "ordenar", "iconos": "Buscar Filtrar FiltroVacio LimpiarFiltros"},
    "Estado y avisos": {"iconos": "Activar Aprobar Bloquear Cancelar Confirmar Desactivar Desbloquear Rechazar "
                                  "Advertencia Informacion Ayuda2 ayuda prohibido"},
    "Archivos y carpetas": {"iconos": "AbrirCarpeta Archivero Carpeta2 carpeta carpeta-verde Adjuntar Descargar Subir "
                                      "Exportar Importar Guardar GuardarCerrar Imprimir VistaPrevia Plantilla"},
    "Navegación y vistas": {"iconos": "Anterior Siguiente Contraer Expandir Inicio Historial VerDetalle Cuadricula "
                                      "Lista ListaTareas salida"},
    "Diagramas y flujos": {"iconos": "ArbolGenealogico DiagramaFlujo FlujoTrabajo gantt"},
}
# Iconos cuyo prefijo sugiere una familia distinta de la que les corresponde
FAMILIA_FORZADA = {"MapaCalor": "grafica", "MapaMental": "grafica",
                   "grafico-circular": "grafica", "grafico-lineas-ambar": "grafica"}
FAMILIA_FORZADA.update({n: "base" for n in (
    "AgregarBaseDatos AprobarBaseDatos CifrarBaseDatos ConfigurarBaseDatos ProtegerBaseDatos "
    "RespaldarDatos RestaurarDatos TablaDatos HojaDatos UsoDatos tabla-dinero").split()})
FAMILIA_FORZADA.update({n: "laboratorio" for n in "Calculadora gota-agua".split()})
SECCION_DE_ICONO = {n: s for s, d in SECCIONES.items() for n in d.get("iconos", "").split()}
SECCION_DE_FAMILIA = {f: s for s, d in SECCIONES.items() for f in d.get("familias", "").split()}
PALABRAS_CLAVE = {
    "carnic": "carnic bovino silueta roja ganado vaca tierra verde",
    "hoja-flecha": "cambiar dieta alimentación forraje hoja flecha",
    "crianza": "crianza madre cría vaca ternero familia nacimiento parto",
    "ternero": "cría bovino recién nacido nacimiento crianza",
    "ternero-mas": "registrar agregar alta ternero nacimiento parto crianza",
    "ternero-corazon": "ternero corazón cuidado cría sanidad bienestar crianza",
    "huella-luna-cuna": "historial partos nacimiento cría pezuña luna cuna pesebre nocturno",
    "ternero-reloj-registro": "registro nacimiento parto ternero gestación reloj arena confirmar",
}
PALABRAS_CLAVE.update({nombre: "cerca corral postes tablones cerramiento " + nombre.replace("-", " ")
                       for nombre in ['cerca-check', 'cerca-circulo', 'cerca-estrella', 'cerca-flecha', 'cerca-intercambio', 'cerca-lista', 'cerca-lupa', 'cerca-mas', 'cerca-menos', 'cerca-pin', 'cerca-reloj', 'cerca-x', 'cerca']})
PALABRAS_CLAVE.update({nombre: f"{titulo} {accion} corral cerca postes tablones puerta reja tierra sin ganado"
                       for nombre, titulo, accion in entradas_corrales()})


def rasterizar_todo():
    """Paso final opcional (--png): regenera png/ desde cero a partir de svg/."""
    svg_dir, png_dir = os.path.join(KIT, "svg"), os.path.join(KIT, "png")
    os.makedirs(png_dir, exist_ok=True)
    for n in os.listdir(png_dir):  # fuera PNG huerfanos o viejos
        os.remove(os.path.join(png_dir, n))
    faltan = [n[:-4] for n in sorted(os.listdir(svg_dir)) if n.endswith(".svg")]
    for k in range(0, len(faltan), 40):
        lote = [os.path.join(svg_dir, n + ".svg") for n in faltan[k:k + 40]]
        subprocess.run([INKSCAPE, "--export-type=png", "--export-width=32", "--export-height=32",
                        "--export-overwrite"] + lote, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for n in faltan[k:k + 40]:
            p = os.path.join(svg_dir, n + ".png")  # Inkscape lo deja junto al SVG
            if os.path.exists(p):
                os.replace(p, os.path.join(png_dir, n + ".png"))
    sin = [n for n in faltan if not os.path.exists(os.path.join(png_dir, n + ".png"))]
    return len(faltan), sin


def familia(nombre):
    """Primera palabra del nombre (CamelCase o con guiones), sin plural: Flechas -> flecha."""
    palabra = re.split(r"[-_]|(?<=[a-z0-9])(?=[A-Z])", nombre)[0].lower()
    return palabra[:-1] if palabra.endswith("s") and len(palabra) > 4 else palabra


def main():
    nuevos, sin_png = rasterizar_todo() if "--png" in sys.argv else (0, [])
    uso = {}
    with open(os.path.join(KIT, "mapa_controles.csv"), encoding="utf-8-sig") as f:
        for r in list(csv.reader(f))[1:]:
            uso.setdefault(r[2], []).append(r[0])

    svg_dir = os.path.join(KIT, "svg")
    nombres = sorted(n[:-4] for n in os.listdir(svg_dir) if n.endswith(".svg"))
    por_seccion = {}
    for n in nombres:
        s = SECCION_DE_ICONO.get(n) or SECCION_DE_FAMILIA.get(FAMILIA_FORZADA.get(n, familia(n)), "Otros")
        por_seccion.setdefault(s, []).append(n)
    grupos = [(s, por_seccion[s]) for s in list(SECCIONES) + ["Otros"] if s in por_seccion]

    datos = [{"t": t, "i": [[n, ", ".join(uso.get(n, [])), PALABRAS_CLAVE.get(n, "")] for n in v]} for t, v in grupos]
    pagina = PLANTILLA.replace("__DATA__", json.dumps(datos, ensure_ascii=False, separators=(",", ":")))
    pagina = pagina.replace("__TOTAL__", str(len(nombres)))
    with open(os.path.join(KIT, "vista_previa.html"), "w", encoding="utf-8") as f:
        f.write(pagina)
    print(f"{len(nombres)} iconos en {len(grupos)} familias; PNG nuevos: {nuevos - len(sin_png)}"
          + (f"; SIN PNG (no renderizan): {sin_png}" if sin_png else ""))


PLANTILLA = """<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kit semantico</title>
<style>
:root{--bg:#fafafa;--card:#fff;--line:#e3e3e3;--ink:#24465B;--mut:#777}
body.oscuro{--bg:#1b1f23;--card:#24292e;--line:#3a4048;--ink:#cfe3f0;--mut:#9aa5b1}
body{font:13px Segoe UI,sans-serif;margin:0;background:var(--bg);color:var(--ink)}
header{position:sticky;top:0;background:var(--bg);padding:10px 20px;border-bottom:1px solid var(--line);z-index:5;display:flex;gap:14px;flex-wrap:wrap;align-items:center}
h1{font-size:16px;margin:0}input[type=search]{padding:8px;width:260px;font-size:14px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--ink)}
label{color:var(--mut);cursor:pointer}main{padding:6px 20px 40px}h2{font-size:14px;margin:22px 0 8px;border-bottom:1px solid var(--line);padding-bottom:4px}
h2 small{color:var(--mut);font-weight:400}.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:6px}
figure{margin:0;display:flex;gap:10px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:6px;padding:6px 8px}
figure img{flex:none}figcaption{line-height:1.25;word-break:break-all}figcaption small{color:var(--mut)}
body.x2 figure img{width:64px;height:64px}
</style>
<header><h1>__TOTAL__ iconos</h1><input id="q" type="search" placeholder="buscar nombre, tema o control...">
<label><input type="checkbox" id="x2"> 64 px</label>
<label><input type="checkbox" id="osc"> fondo oscuro</label><label><input type="checkbox" id="sin"> solo sin control</label></header>
<main id="m"></main>
<script>
const D=__DATA__,m=document.getElementById('m'),q=document.getElementById('q');
const E=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const normalizar=s=>s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');
function draw(){const t=normalizar(q.value.trim()),sin=document.getElementById('sin').checked;let h='';
D.forEach(g=>{const it=g.i.filter(([n,u,k])=>(!t||normalizar(n+' '+u+' '+(k||'')+' '+g.t).includes(t))&&(!sin||!u));if(!it.length)return;
h+='<h2>'+E(g.t)+' <small>'+it.length+'</small></h2><div class="g">'+it.map(([n,u])=>
'<figure><img loading="lazy" width="32" height="32" src="svg/'+n+'.svg"><figcaption><b>'+E(n)+'</b><br><small>'+(u?E(u):'(sin control)')+'</small></figcaption></figure>').join('')+'</div>'});
m.innerHTML=h||'<p>Sin resultados</p>'}
q.oninput=draw;document.getElementById('sin').onchange=draw;
document.getElementById('x2').onchange=e=>document.body.classList.toggle('x2',e.target.checked);
document.getElementById('osc').onchange=e=>document.body.classList.toggle('oscuro',e.target.checked);draw();
</script></html>"""

if __name__ == "__main__":
    main()
