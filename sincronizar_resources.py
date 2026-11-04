"""Sincroniza los SVG del Kit semantico con ControlGanadero/Resources y los registra.

Paso 1 - copia: borra de Resources los SVG que pertenecen al kit y vuelve a
copiarlos desde Kit_semantico/svg, de modo que se actualizan dibujos y se
anaden los nuevos.

Paso 2 - registro: deja cada SVG del kit disponible como recurso del proyecto
(asi aparece en el selector de imagenes de Visual Studio), en tres sitios:
  - My Project/Resources.resx          (<data ... ResXFileRef>)
  - My Project/Resources.Designer.vb   (propiedad Friend ReadOnly ... SvgImage)
  - ControlGanaderoPro.vbproj          (<None Include="Resources\\X.svg" />)
Tambien quita el registro de los que ya no tienen archivo, para que el proyecto
no quede apuntando a SVG inexistentes. Es idempotente: lo ya registrado no se
duplica.

"Pertenecen al kit" = su nombre esta en Kit_semantico/svg  o  figura en el
manifiesto .kit_manifest.txt (lo pegado en una corrida anterior; asi tambien
se limpian iconos que ya se quitaron del kit).
Los demas SVG de Resources (DevExpress, referenciados desde Resources.resx,
about.svg, actions_*.svg...) NO se tocan.

Uso:
    python sincronizar_resources.py                    # simulacion (no cambia nada)
    python sincronizar_resources.py --aplicar          # copia + registro
    python sincronizar_resources.py --aplicar --solo-registrar   # solo el registro
    python sincronizar_resources.py --aplicar --sin-registro     # solo la copia
"""
import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
KIT = AQUI / "simulador de control ganadero" / "Kit_semantico" / "svg"
PROYECTO = AQUI.parent / "ControlGanadero"
RES = PROYECTO / "Resources"
MANIFIESTO = RES / ".kit_manifest.txt"
RESX = PROYECTO / "My Project" / "Resources.resx"
DESIGNER = PROYECTO / "My Project" / "Resources.Designer.vb"
VBPROJ = PROYECTO / "ControlGanaderoPro.vbproj"
RETIRADOS = AQUI / "retirados.txt"
RESPALDO = AQUI / "Respaldos" / "resources_svg"
RESPALDO_REGISTRO = AQUI / "Respaldos" / "registro_recursos"

TIPO_SVG = ("DevExpress.Utils.Svg.SvgImage, DevExpress.Data.v24.1, Version=24.1.3.0, "
            "Culture=neutral, PublicKeyToken=b88d1754d700e49a")
BS = chr(92)  # barra invertida
NOMBRE_VALIDO = re.compile(r"[A-Za-z0-9_-]+")


def leer(path):
    """Devuelve (texto, tiene_bom, salto_de_linea) para reescribir sin alterar el formato."""
    crudo = path.read_bytes()
    texto = crudo.decode("utf-8-sig")
    return texto, crudo.startswith(b"\xef\xbb\xbf"), ("\r\n" if "\r\n" in texto else "\n")


def escribir(path, texto, tiene_bom):
    path.write_bytes((b"\xef\xbb\xbf" if tiene_bom else b"") + texto.encode("utf-8"))


def nombre_propiedad(base):
    prop = base.replace("-", "_")
    return "_" + prop if prop[0].isdigit() else prop


def planear_registro(kit_o_manifiesto, archivos_finales):
    """Que registrar y que des-registrar, segun lo que quedara en Resources."""
    resx, _, _ = leer(RESX)
    proj, _, _ = leer(VBPROJ)
    designer, _, _ = leer(DESIGNER)

    en_resx = lambda b: ('<data name="%s"' % b) in resx
    en_proj = lambda b: ('Resources' + BS + b + '.svg"') in proj
    en_des = lambda b: ('GetObject("%s"' % b) in designer

    altas, bajas, omitidos = [], [], []
    for archivo in sorted(kit_o_manifiesto):
        base = archivo[:-4]
        if not NOMBRE_VALIDO.fullmatch(base):
            omitidos.append(archivo)
            continue
        if archivo in archivos_finales:
            falta = [s for s, ok in (("resx", en_resx(base)), ("vbproj", en_proj(base)),
                                     ("designer", en_des(base))) if not ok]
            if falta:
                altas.append((base, falta))
        elif en_resx(base) or en_proj(base) or en_des(base):
            bajas.append(base)
    return altas, bajas, omitidos


def usados_en_codigo(bases):
    """Archivos .vb que usan Resources.<base>; ignora el propio Designer de recursos y bin/obj."""
    patron = re.compile(r"\bResources\.(%s)\b" % "|".join(re.escape(nombre_propiedad(b)) for b in bases))
    inverso = {nombre_propiedad(b): b for b in bases}
    usos = {}
    for f in PROYECTO.rglob("*.vb"):
        partes = set(f.relative_to(PROYECTO).parts)
        if f == DESIGNER or partes & {"bin", "obj", ".claude", "packages"}:
            continue
        try:
            texto = f.read_text(encoding="utf-8-sig", errors="ignore")
        except OSError:
            continue
        for m in set(patron.findall(texto)):
            usos.setdefault(inverso[m], []).append(f.name)
    return usos


def aplicar_registro(altas, bajas):
    # --- resx ---
    resx, bom, nl = leer(RESX)
    m = re.search(r"<value>[.][.]" + re.escape(BS) + "Resources" + re.escape(BS)
                  + r"[^;<]+[.]svg;(DevExpress[.]Utils[.]Svg[.]SvgImage[^<]*)</value>", resx)
    tipo = m.group(1) if m else TIPO_SVG
    for base in bajas:
        resx = re.sub(r'  <data name="%s" type="System[.]Resources[.]ResXFileRef[^>]*>%s'
                      r"    <value>[^<]*</value>%s  </data>%s" % (re.escape(base), nl, nl, nl),
                      "", resx)
    nuevos = ""
    for base, falta in altas:
        if "resx" in falta:
            nuevos += ('  <data name="%s" type="System.Resources.ResXFileRef, System.Windows.Forms">%s'
                       '    <value>..%sResources%s%s.svg;%s</value>%s  </data>%s'
                       % (base, nl, BS, BS, base, tipo, nl, nl))
    if nuevos:
        resx = resx.replace("</root>", nuevos + "</root>")
    escribir(RESX, resx, bom)

    # --- Designer.vb ---
    des, bom, nl = leer(DESIGNER)
    for base in bajas:
        des = re.sub(r"(?:        %s)?        '''<summary>%s        '''  Looks up a localized resource of "
                     r"type [^\r\n]*%s        '''</summary>%s        Friend ReadOnly Property \w+[(][)] As "
                     r"[^\r\n]*%s            Get%s                Dim obj As Object = ResourceManager"
                     r'[.]GetObject\("%s", resourceCulture\)%s.*?        End Property%s'
                     % (nl, nl, nl, nl, nl, nl, re.escape(base), nl, nl), "", des, count=1, flags=re.S)
    bloques = ""
    for base, falta in altas:
        if "designer" in falta:
            bloques += ("        %s        '''<summary>%s        '''  Looks up a localized resource of type "
                        "DevExpress.Utils.Svg.SvgImage.%s        '''</summary>%s"
                        "        Friend ReadOnly Property %s() As DevExpress.Utils.Svg.SvgImage%s"
                        '            Get%s                Dim obj As Object = ResourceManager.GetObject("%s", '
                        "resourceCulture)%s                Return CType(obj,DevExpress.Utils.Svg.SvgImage)%s"
                        "            End Get%s        End Property%s"
                        % (nl, nl, nl, nl, nombre_propiedad(base), nl, nl, base, nl, nl, nl, nl))
    if bloques:
        i = des.rindex("    End Module")
        des = des[:i] + bloques + des[i:]
    escribir(DESIGNER, des, bom)

    # --- vbproj ---
    proj, bom, nl = leer(VBPROJ)
    for base in bajas:
        proj = re.sub(r'    <None Include="Resources%s%s[.]svg" />%s' % (re.escape(BS), re.escape(base), nl),
                      "", proj)
    lineas = "".join('    <None Include="Resources%s%s.svg" />%s' % (BS, base, nl)
                     for base, falta in altas if "vbproj" in falta)
    if lineas:
        ultimos = list(re.finditer(r'    <None Include="Resources' + re.escape(BS) + r'[^"]+[.]svg" />'
                                   + nl, proj))
        if not ultimos:
            sys.exit("No encontre donde insertar los <None Include> en el vbproj; "
                     "resx y Designer ya se cambiaron, el vbproj no.")
        fin = ultimos[-1].end()
        proj = proj[:fin] + lineas + proj[fin:]
    escribir(VBPROJ, proj, bom)


TIPO_BYTE = "System.Byte[], mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"


def svg_tipados_byte():
    """Recursos svg registrados como Byte[]: el compilador los convierte a SvgImage, el disenador de VS no."""
    resx, _, _ = leer(RESX)
    patron = (r'<data name="([^"]+)"[^>]*>\s*<value>[.][.]' + re.escape(BS) + "Resources" + re.escape(BS)
              + r"[^;<]+[.]svg;" + re.escape(TIPO_BYTE))
    return re.findall(patron, resx)


def normalizar_tipos(nombres):
    """Pasa esos recursos de Byte[] a SvgImage, en el resx y en el Designer."""
    resx, bom, nl = leer(RESX)
    resx = re.sub(r"(<value>[.][.]" + re.escape(BS) + "Resources" + re.escape(BS) + r"[^;<]+[.]svg;)"
                  + re.escape(TIPO_BYTE) + "(</value>)", r"\g<1>" + TIPO_SVG + r"\g<2>", resx)
    escribir(RESX, resx, bom)

    des, bom, nl = leer(DESIGNER)
    for nombre in nombres:
        des = re.sub(r"(        '''  Looks up a localized resource of type )System[.]Byte\[\][.](%s"
                     r"        '''</summary>%s        Friend ReadOnly Property \w+[(][)] As )Byte[(][)](%s"
                     r"            Get%s                Dim obj As Object = ResourceManager[.]GetObject\(\"%s\", "
                     r"resourceCulture\)%s                Return CType[(]obj,)Byte[(][)]([)])"
                     % (nl, nl, nl, nl, re.escape(nombre), nl),
                     r"\g<1>DevExpress.Utils.Svg.SvgImage.\g<2>DevExpress.Utils.Svg.SvgImage\g<3>"
                     r"DevExpress.Utils.Svg.SvgImage\g<4>", des)
    escribir(DESIGNER, des, bom)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aplicar", action="store_true", help="ejecutar (sin esto solo simula)")
    ap.add_argument("--sin-respaldo", action="store_true", help="no guardar respaldos")
    ap.add_argument("--solo-registrar", action="store_true", help="no copiar SVG; solo el registro")
    ap.add_argument("--sin-registro", action="store_true", help="no tocar resx / Designer / vbproj")
    args = ap.parse_args()
    if args.solo_registrar and args.sin_registro:
        sys.exit("--solo-registrar y --sin-registro se contradicen.")

    for p in (KIT, RES):
        if not p.is_dir():
            sys.exit(f"No existe: {p}")
    if not args.sin_registro:
        for p in (RESX, DESIGNER, VBPROJ):
            if not p.is_file():
                sys.exit(f"No existe: {p}")

    kit = {f.name: f for f in KIT.glob("*.svg")}
    previos = set()
    if MANIFIESTO.exists():
        previos = {l.strip() for l in MANIFIESTO.read_text(encoding="utf-8").splitlines() if l.strip()}

    # retirados.txt: nombres viejos (renombrados / eliminados) que hay que limpiar aunque
    # ya no esten en el kit ni en el manifiesto
    if RETIRADOS.exists():
        for linea in RETIRADOS.read_text(encoding="utf-8").splitlines():
            nombre = linea.split("#")[0].strip()
            if nombre:
                previos.add(nombre if nombre.lower().endswith(".svg") else nombre + ".svg")

    # nombres a borrar: los del kit + los pegados antes, solo si existen en Resources
    existentes = {f.name: f for f in RES.glob("*.svg")}
    a_borrar = sorted(n for n in existentes if n in kit or n in previos)
    nuevos = sorted(n for n in kit if n not in existentes)
    huerfanos = sorted(n for n in a_borrar if n not in kit)  # ya no estan en el kit
    intactos = len(existentes) - len(a_borrar)

    if not args.solo_registrar:
        print(f"Kit:        {len(kit)} svg")
        print(f"Resources:  {len(existentes)} svg  ({intactos} ajenos al kit, no se tocan)")
        print(f"A reemplazar: {len(a_borrar) - len(huerfanos)}  |  nuevos: {len(nuevos)}  |  "
              f"quitados del kit (se borran): {len(huerfanos)}")
        if nuevos:
            print("  Nuevos:", ", ".join(nuevos[:15]) + (" ..." if len(nuevos) > 15 else ""))
        if huerfanos:
            print("  Quitados:", ", ".join(huerfanos[:15]) + (" ..." if len(huerfanos) > 15 else ""))

    # lo que habra en Resources al terminar, para planear el registro
    if args.solo_registrar:
        finales = set(existentes)
    else:
        finales = (set(existentes) - set(a_borrar)) | set(kit)
    altas, bajas, byte_t = [], [], []
    if not args.sin_registro:
        altas, bajas, omitidos = planear_registro(set(kit) | previos, finales)
        byte_t = svg_tipados_byte()
        print(f"Registro:   {len(altas)} por registrar  |  {len(bajas)} por quitar del registro")
        if byte_t:
            print(f"Tipos:      {len(byte_t)} svg registrados como Byte[] (el disenador de VS falla con ellos); "
                  f"se pasan a SvgImage")
        for base, falta in altas[:10]:
            print(f"  + {base}  (falta en: {', '.join(falta)})")
        if len(altas) > 10:
            print(f"  + ... y {len(altas) - 10} mas")
        if bajas:
            print("  - Quitar:", ", ".join(bajas[:15]) + (" ..." if len(bajas) > 15 else ""))
        if omitidos:
            print("  ! Nombres no validos para recurso (se omiten):", ", ".join(omitidos))

    # lo que se va a quitar no debe seguir usandose en el codigo (My.Resources.<nombre>)
    quitar = {n[:-4] for n in huerfanos} | set(bajas)
    en_uso = usados_en_codigo(quitar) if quitar else {}
    if en_uso:
        print("  ! Se quitan iconos que el codigo todavia usa:")
        for base, archivos in sorted(en_uso.items()):
            print(f"    {base}: {', '.join(archivos[:4])}")
        if args.aplicar:
            sys.exit("No se aplico nada. Cambia esas referencias al icono nuevo y vuelve a ejecutar.")

    if not args.aplicar:
        print("\nSimulacion: no se cambio nada. Usa --aplicar para ejecutar.")
        return

    if not args.solo_registrar:
        if not args.sin_respaldo and a_borrar:
            dest = RESPALDO / datetime.now().strftime("%Y%m%d_%H%M%S")
            dest.mkdir(parents=True)
            for n in a_borrar:
                shutil.copy2(existentes[n], dest / n)
            print(f"Respaldo de lo borrado: {dest}")

        for n in a_borrar:
            existentes[n].unlink()
        for n, src in sorted(kit.items()):
            shutil.copy2(src, RES / n)

        MANIFIESTO.write_text("\n".join(sorted(kit)) + "\n", encoding="utf-8")
        print(f"Listo: {len(kit)} svg copiados a {RES}")

    if not args.sin_registro and (altas or bajas or byte_t):
        if not args.sin_respaldo:
            dest = RESPALDO_REGISTRO / datetime.now().strftime("%Y%m%d_%H%M%S")
            dest.mkdir(parents=True)
            for p in (RESX, DESIGNER, VBPROJ):
                shutil.copy2(p, dest / p.name)
            print(f"Respaldo de resx / Designer / vbproj: {dest}")
        if altas or bajas:
            aplicar_registro(altas, bajas)
            print(f"Registro aplicado: +{len(altas)} / -{len(bajas)} en Resources.resx, "
                  f"Resources.Designer.vb y ControlGanaderoPro.vbproj")
        pendientes = svg_tipados_byte()
        if pendientes:
            normalizar_tipos(pendientes)
            print(f"Tipos normalizados: {len(pendientes)} svg de Byte[] a SvgImage")
        print("Si Visual Studio tiene el proyecto abierto, acepta 'Recargar' cuando lo pida.")
    elif not args.sin_registro:
        print("Registro: ya estaba todo al dia.")


if __name__ == "__main__":
    main()
