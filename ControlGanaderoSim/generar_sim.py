"""Extrae el ribbon de ControlGanadero (FrmMain) para el mockup HTML.

Lee FrmMain.designer.vb, FrmMain.resx y los SVG de Resources de una rama del proyecto
(con `git show`, sin cambiar el checkout) y escribe:
  - datos.js                 pestañas, grupos, botones y de dónde sale cada icono
  - iconos_proyecto/*.svg    los SVG de Resources que usa el ribbon, tal como están en la rama
  - iconos_embebidos/*       los iconos guardados dentro de FrmMain.resx (SVG o PNG)

Uso:
    python generar_sim.py                 # rama main (la que estaba compilada en las capturas)
    python generar_sim.py --rama feature/508-Analisis-Datos-Noviembre
    python generar_sim.py --trabajo       # archivos del checkout actual, sin git

La ruta del proyecto se toma de la variable CONTROLGANADERO o de ../../ControlGanadero.
"""
import argparse
import base64
import json
import os
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

AQUI = Path(__file__).resolve().parent
KIT_ROOT = AQUI.parent
KIT_SVG = KIT_ROOT / "simulador de control ganadero" / "Kit_semantico" / "svg"
PROYECTO = Path(os.environ.get("CONTROLGANADERO", KIT_ROOT.parent / "ControlGanadero"))
DESIGNER = "Globales/FrmMain.designer.vb"
RESX = "Globales/FrmMain.resx"
RESOURCES = "Resources"
DIR_PROYECTO = AQUI / "iconos_proyecto"
DIR_EMBEBIDOS = AQUI / "iconos_embebidos"

ID = r"[\wñÑáéíóúÁÉÍÓÚ]+"


class Proyecto:
    """Lee archivos del proyecto desde una rama de git o desde el checkout."""

    def __init__(self, rama):
        self.rama = rama

    def git(self, *args):
        return subprocess.run(["git", "-C", str(PROYECTO), *args], capture_output=True, check=True).stdout

    def leer(self, ruta):
        datos = self.git("show", f"{self.rama}:{ruta}") if self.rama else (PROYECTO / ruta).read_bytes()
        return datos.decode("utf-8-sig", errors="replace")

    def svgs_resources(self):
        if self.rama:
            nombres = self.git("ls-tree", "--name-only", self.rama, RESOURCES + "/").decode().split("\n")
        else:
            nombres = [f"{RESOURCES}/{f.name}" for f in (PROYECTO / RESOURCES).iterdir()]
        return [n for n in nombres if n.lower().endswith(".svg")]

    def version(self):
        if not self.rama:
            return "checkout actual (sin git)"
        return self.git("log", "-1", "--format=%h del %ci", self.rama).decode().strip()


def rel(ruta):
    """Ruta relativa a index.html, con / para el navegador."""
    return os.path.relpath(ruta, AQUI).replace(os.sep, "/")


def recurso_vb(nombre):
    """Nombre con el que Visual Basic expone un archivo en My.Resources."""
    return re.sub(r"[^\w]", "_", nombre)


def normalizar(svg):
    """Contenido comparable de un SVG: sin declaración XML, BOM ni espacios."""
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg.lstrip("﻿"))
    return re.sub(r"\s+", "", svg)


def imagenes_resx(texto_resx):
    """{nombre del dato: (extension, bytes)} de los iconos guardados en FrmMain.resx."""
    salida = {}
    for d in ET.fromstring(texto_resx.encode("utf-8")).findall("data"):
        nombre, valor = d.get("name", ""), d.find("value")
        if valor is None or not nombre.endswith(("SvgImage", "LargeImage", "Image")):
            continue
        try:
            crudo = base64.b64decode(valor.text or "")
        except ValueError:
            continue
        ini = crudo.find(b"<?xml")
        ini = ini if ini >= 0 else crudo.find(b"<svg")
        fin = crudo.rfind(b"</svg>")
        if ini >= 0 and fin > ini:
            salida[nombre] = ("svg", crudo[ini:fin + 6])
            continue
        ini, fin = crudo.find(b"\x89PNG"), crudo.find(b"IEND")
        if ini >= 0 and fin > ini:
            salida[nombre] = ("png", crudo[ini:fin + 8])
    return salida


def main():
    args = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    args.add_argument("--rama", default="main", help="rama o commit de ControlGanadero (por defecto main)")
    args.add_argument("--trabajo", action="store_true", help="leer el checkout actual en vez de una rama")
    args = args.parse_args()
    proyecto = Proyecto(None if args.trabajo else args.rama)

    texto = proyecto.leer(DESIGNER)
    embebidos = imagenes_resx(proyecto.leer(RESX))
    kit = {recurso_vb(f.stem): f for f in sorted(KIT_SVG.glob("*.svg"))}
    kit_por_contenido = {}
    for f in kit.values():
        kit_por_contenido.setdefault(normalizar(f.read_text(encoding="utf-8-sig")), f.stem)
    resources = {recurso_vb(Path(r).stem): r for r in proyecto.svgs_resources()}

    for carpeta in (DIR_PROYECTO, DIR_EMBEBIDOS):
        carpeta.mkdir(exist_ok=True)
        for viejo in carpeta.iterdir():
            viejo.unlink()

    def prop(obj, nombre):
        m = re.search(rf"Me\.{obj}\.{nombre} = (.+)", texto)
        return m.group(1).strip() if m else None

    def lista(obj, nombre):
        """Controles de una llamada Me.obj.nombre.AddRange(New X() {Me.a, Me.b})."""
        m = re.search(rf"Me\.{obj}\.{nombre}\.AddRange\((.+)\)", texto)
        return re.findall(rf"Me\.({ID})", m.group(1)) if m else []

    def cadena(valor):
        return json.loads(valor) if valor and valor.startswith('"') else valor

    def icono_recurso(recurso):
        archivo_kit, ruta_res = kit.get(recurso), resources.get(recurso)
        icono = {"tipo": "recurso", "nombre": Path(ruta_res).stem if ruta_res else recurso,
                 "kit": rel(archivo_kit) if archivo_kit else None, "proyecto": None, "cambia": False}
        if ruta_res:
            svg = proyecto.leer(ruta_res)
            destino = DIR_PROYECTO / Path(ruta_res).name
            destino.write_text(svg, encoding="utf-8")
            icono["proyecto"] = rel(destino)
            if archivo_kit:
                icono["cambia"] = normalizar(svg) != normalizar(archivo_kit.read_text(encoding="utf-8-sig"))
        return icono

    def icono(obj):
        """Origen del icono de un control: SvgImage (recurso o embebido) o, si no hay, imagen raster."""
        valor = prop(obj, r"ImageOptions\.SvgImage")
        m = re.search(r"My\.Resources\.Resources\.(\w+)", valor or "")
        if m:
            return icono_recurso(m.group(1))
        for clave in ("SvgImage", "LargeImage", "Image"):
            dato = f"{obj}.ImageOptions.{clave}"
            if dato in embebidos and prop(obj, rf"ImageOptions\.{clave}"):
                ext, contenido = embebidos[dato]
                archivo = DIR_EMBEBIDOS / f"{obj}.{ext}"
                archivo.write_bytes(contenido)
                copia = kit_por_contenido.get(normalizar(contenido.decode("utf-8", "replace"))) if ext == "svg" else None
                return {"tipo": "embebido" if ext == "svg" else "raster", "nombre": obj,
                        "embebido": rel(archivo), "copiaDeKit": copia}
        return None

    def item(obj):
        tipo = re.search(rf"Me\.{obj} = New DevExpress\.XtraBars\.(\w+)\(\)", texto)
        return {"id": obj, "tipo": tipo.group(1) if tipo else "?",
                "texto": cadena(prop(obj, "Caption")) or obj,
                "icono": icono(obj),
                "menu": [item(s) for s in lista(obj, "LinksPersistInfo")]}

    paginas = []
    for pag in lista("ribbonControl", "Pages"):
        grupos = []
        for g in lista(pag, "Groups"):
            links = re.findall(rf"Me\.{g}\.ItemLinks\.Add\(Me\.({ID})(, True)?\)", texto)
            grupos.append({"id": g, "texto": cadena(prop(g, "Text")) or "",
                           "visible": prop(g, "Visible") != "False",
                           "items": [dict(item(i), separador=bool(t)) for i, t in links]})
        paginas.append({"id": pag, "texto": cadena(prop(pag, "Text")) or pag,
                        "icono": icono(pag), "grupos": grupos})

    datos = {"rama": proyecto.rama or "checkout", "version": proyecto.version(), "paginas": paginas}
    (AQUI / "datos.js").write_text(
        "// Generado por generar_sim.py a partir de FrmMain.designer.vb. No editar a mano.\n"
        "window.SIM = " + json.dumps(datos, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")

    controles = [i for p in paginas for g in p["grupos"] for i in g["items"]]
    controles += [s for i in controles for s in i["menu"]]
    iconos = [p["icono"] for p in paginas] + [c["icono"] for c in controles]
    print(f"{proyecto.version()} | {len(paginas)} pestañas, "
          f"{sum(len(p['grupos']) for p in paginas)} grupos, {len(controles)} controles")
    for t in ("recurso", "embebido", "raster"):
        print(f"  {t}: {sum(bool(i) and i['tipo'] == t for i in iconos)}")
    print(f"  sin icono: {sum(i is None for i in iconos)}")
    print(f"  con cambios en el kit que el proyecto aún no tiene: {sum(bool(i and i.get('cambia')) for i in iconos)}")


if __name__ == "__main__":
    main()
