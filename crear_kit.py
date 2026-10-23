"""Genera iconos vectoriales originales y PNG transparentes para FrmMain."""
from pathlib import Path
import re, json, html, zipfile, math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Kit_frmMain_32"
SOURCE = Path(r"C:\Users\uhw30\Documents\PRODUCCION\ControlGanadero\Globales\FrmMain.designer.vb")
for folder in ("png32", "svg"):
    (OUT / folder).mkdir(parents=True, exist_ok=True)

INK="#24465B"
BLUE="#378CE7"
GREEN="#24AC88"
ORANGE="#F3AD43"
RED="#E56876"
PURPLE="#8870D4"
PALE="#E2F2F5"
WHITE="#FFFFFF"
S=4

class Icon:
    def __init__(self):
        self.im=Image.new("RGBA",(128,128))
        self.d=ImageDraw.Draw(self.im)
        self.svg=[]
    def rect(self, box, fill, radius=0, stroke=None):
        x,y,x2,y2=box
        self.svg.append(f'<rect x="{x}" y="{y}" width="{x2-x}" height="{y2-y}" rx="{radius}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="1.5"' if stroke else '')+'/>')
        self.d.rounded_rectangle(tuple(round(v*S) for v in box),radius=radius*S,fill=fill,outline=stroke,width=6)
    def ellipse(self,box,fill,stroke=None):
        x,y,x2,y2=box
        self.svg.append(f'<ellipse cx="{(x+x2)/2}" cy="{(y+y2)/2}" rx="{(x2-x)/2}" ry="{(y2-y)/2}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="1.5"' if stroke else '')+'/>')
        self.d.ellipse(tuple(round(v*S) for v in box),fill=fill,outline=stroke,width=6)
    def line(self,pts,color=INK,width=2):
        self.svg.append(f'<polyline points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')
        self.d.line([(round(x*S),round(y*S)) for x,y in pts],fill=color,width=round(width*S),joint="curve")
        r=width*S/2
        for x,y in pts:
            self.d.ellipse((x*S-r,y*S-r,x*S+r,y*S+r),fill=color)
    def poly(self,pts,fill):
        self.svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{fill}"/>')
        self.d.polygon([(round(x*S),round(y*S)) for x,y in pts],fill=fill)
    def save(self,name):
        self.im.resize((32,32),Image.Resampling.LANCZOS).save(OUT/"png32"/f"{name}.png")
        (OUT/"svg"/f"{name}.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">'+"".join(self.svg)+"</svg>",encoding="utf-8")

def draw_base(k,c):
    a=Icon()
    if k=="cow":
        a.poly([(8,10),(3,7),(4,14),(10,16)],c); a.poly([(24,10),(29,7),(28,14),(22,16)],c)
        a.line([(10,9),(7,5),(7,3)],ORANGE,2.5); a.line([(22,9),(25,5),(25,3)],ORANGE,2.5)
        a.rect((9,7,23,27),PALE,6)
        a.poly([(10,9),(16,8),(14,16),(9,17)],c)
        a.ellipse((7,19,25,28),c)
        for x in (12,20): a.ellipse((x-1,14,x+1,16),INK)
        for x in (12,20): a.ellipse((x-1,22,x+1,24),INK)
    elif k=="people":
        a.ellipse((17,5,26,14),c); a.rect((15,16,29,27),c,5)
        a.ellipse((5,3,17,15),INK); a.rect((2,17,21,29),c,6)
        a.poly([(10,18),(14,18),(12,25)],WHITE)
    elif k=="fence":
        a.rect((3,11,29,15),c,1); a.rect((3,21,29,25),c,1)
        for x in (5,14,23):
            a.poly([(x,6),(x+2,3),(x+4,6),(x+4,29),(x,29)],INK)
    elif k=="leaf":
        a.poly([(6,24),(3,17),(4,8),(15,11),(19,19),(16,26)],GREEN)
        a.poly([(14,24),(14,13),(20,5),(29,3),(28,14),(22,23)],c)
        a.line([(9,29),(23,10)],INK)
        a.line([(13,23),(8,16)],INK,1.5)
    elif k=="document":
        a.rect((6,3,26,29),PALE,3)
        a.rect((6,3,26,8),c,2)
        for y,w in ((13,15),(18,11),(23,13)): a.line([(10,y),(10+w-6,y)],INK,1.7)
    elif k=="chart":
        a.line([(4,4),(4,28),(29,28)],INK,2)
        for x,y,col in ((8,18,c),(15,12,BLUE),(22,5,c)): a.rect((x,y,x+5,25),col,1)
    elif k=="truck":
        a.rect((2,7,20,23),c,2)
        a.poly([(21,12),(26,12),(30,18),(30,24),(21,24)],INK)
        a.poly([(23,14),(25,14),(28,18),(23,18)],PALE)
        for x in (8,25): a.ellipse((x-4,21,x+4,29),INK); a.ellipse((x-1.5,23.5,x+1.5,26.5),WHITE)
    elif k=="scale":
        a.rect((5,11,27,28),c,3); a.ellipse((9,3,23,17),PALE,INK)
        a.line([(16,10),(20,6)],RED,2); a.line([(10,23),(22,23)],WHITE,2)
    elif k=="medical":
        a.rect((3,8,29,28),c,4); a.line([(11,8),(11,4),(21,4),(21,8)],INK)
        a.rect((13,12,19,24),WHITE,1); a.rect((10,15,22,21),WHITE,1)
    elif k=="syringe":
        a.line([(5,27),(10,22)],INK,2)
        a.poly([(8,20),(19,9),(25,15),(14,26)],PALE)
        a.poly([(8,20),(14,14),(20,20),(14,26)],c)
        a.line([(18,8),(26,16)],INK); a.line([(22,10),(26,6)],INK)
        a.line([(23,3),(29,9)],c,3)
    elif k=="search":
        a.ellipse((3,3,23,23),PALE,c)
        a.line([(21,21),(29,29)],INK,4)
        a.line([(8,13),(11,16),(18,9)],c,2)
    elif k=="money":
        a.rect((2,7,30,25),c,3); a.ellipse((11,9,21,23),PALE)
        a.line([(16,12),(13,12),(13,16),(19,16),(19,20),(16,20)],INK,1.5)
        a.line([(16,10),(16,22)],INK,1.2)
        a.line([(6,15),(7,15)],WHITE,2); a.line([(25,17),(26,17)],WHITE,2)
    elif k=="tag":
        a.poly([(3,5),(17,5),(29,17),(17,29),(3,15)],c)
        a.ellipse((7,9,12,14),WHITE); a.line([(17,14),(23,20)],WHITE,2)
    elif k=="arrows":
        a.line([(4,10),(27,10),(22,5)],c,3); a.line([(27,22),(4,22),(9,27)],INK,3)
    elif k=="gear":
        for i in range(8):
            t=i*math.pi/4
            a.line([(16+9*math.cos(t),16+9*math.sin(t)),(16+12*math.cos(t),16+12*math.sin(t))],c,5)
        a.ellipse((6,6,26,26),c); a.ellipse((11,11,21,21),WHITE); a.ellipse((14,14,18,18),INK)
    elif k=="calendar":
        a.rect((3,6,29,29),PALE,3); a.rect((3,6,29,12),c,2)
        for x in (9,23): a.line([(x,3),(x,8)],INK,2)
        for x in (9,16,23):
            for y in (17,23): a.rect((x-1.5,y-1.5,x+1.5,y+1.5),c,0.5)
    elif k=="map":
        a.poly([(2,7),(11,3),(21,7),(30,3),(30,25),(21,29),(11,25),(2,29)],PALE)
        a.line([(11,5),(11,24)],c); a.line([(21,8),(21,27)],c)
        a.ellipse((10,5,24,19),c); a.poly([(11,15),(23,15),(17,24)],c); a.ellipse((14,9,20,15),WHITE)
    elif k=="bottle":
        a.rect((11,3,21,7),INK,1); a.rect((12,7,20,10),PALE,1)
        a.rect((7,10,25,29),c,4); a.rect((8,16,24,24),PALE,1)
        a.line([(13,20),(19,20)],c,2); a.line([(16,17),(16,23)],c,2)
    elif k=="water":
        a.poly([(16,2),(5,17),(4,22),(8,28),(16,30),(24,28),(28,22),(27,17)],c)
        a.line([(10,20),(10,23),(14,26)],WHITE,2)
    elif k=="shield":
        a.poly([(16,2),(28,7),(26,21),(22,26),(16,30),(10,26),(6,21),(4,7)],c)
        a.line([(10,16),(14,20),(22,11)],WHITE,2.5)
    elif k=="folder":
        a.rect((3,5,15,13),c,2); a.rect((3,9,29,28),c,3)
        a.poly([(3,14),(29,14),(26,28),(6,28)],PALE)
        a.line([(10,19),(22,19)],c,2)
    elif k=="monitor":
        a.rect((2,3,30,23),INK,3); a.rect((5,6,27,19),c,1)
        a.line([(16,23),(16,28),(9,28),(23,28)],INK,2)
    elif k=="clock":
        a.ellipse((3,3,29,29),PALE,c); a.line([(16,8),(16,16),(22,19)],INK,2)
    elif k=="percent":
        a.line([(8,26),(24,6)],c,3); a.ellipse((4,4,14,14),c); a.ellipse((18,18,28,28),INK)
        a.ellipse((7,7,11,11),WHITE); a.ellipse((21,21,25,25),WHITE)
    elif k=="exit":
        a.rect((4,3,18,29),INK,2); a.rect((7,6,16,26),PALE,1)
        a.line([(14,16),(29,16),(24,11)],c,2.5); a.line([(29,16),(24,21)],c,2.5)
    elif k=="help":
        a.ellipse((3,3,29,29),c)
        a.line([(11,11),(13,8),(19,8),(21,11),(20,14),(16,17),(16,19)],WHITE,2)
        a.ellipse((15,23,17,25),WHITE)
    elif k=="align":
        for y,w in ((6,23),(12,16),(18,23),(24,16)): a.line([(4,y),(w+4,y)],c,2)
    elif k=="palette":
        a.ellipse((3,3,29,29),PALE,INK)
        for x,y,col in ((10,9,BLUE),(21,9,RED),(8,19,GREEN),(22,19,ORANGE)): a.ellipse((x-2,y-2,x+2,y+2),col)
    else: raise ValueError(k)
    return a

def badge(a,k,c):
    if not k: return
    a.ellipse((18,18,32,32),WHITE)
    a.ellipse((20,20,31,31),c)
    if k=="plus": a.line([(23,25.5),(28,25.5)],WHITE,1.5); a.line([(25.5,23),(25.5,28)],WHITE,1.5)
    elif k=="minus": a.line([(23,25.5),(28,25.5)],WHITE,1.5)
    elif k=="check": a.line([(22.5,25),(25,27.5),(28.5,23)],WHITE,1.5)
    elif k=="x": a.line([(23,23),(28,28)],WHITE,1.5); a.line([(28,23),(23,28)],WHITE,1.5)
    elif k=="arrow": a.line([(22.5,25.5),(28.5,25.5),(26,23)],WHITE,1.5); a.line([(28.5,25.5),(26,28)],WHITE,1.5)
    elif k=="pause": a.line([(24,23),(24,28)],WHITE,1.5); a.line([(27,23),(27,28)],WHITE,1.5)
    elif k=="clock": a.line([(25,22.5),(25,26),(28,26)],WHITE,1.5)
    elif k=="dot": a.ellipse((24,24,27,27),WHITE)

# Explicit semantic assignments: control = base, color family, optional action.
groups = {
 "cow": "bbiListaReses bbiExistenciaGanado bbiListaResesFeedLot bbiListaResesCrianza bbiListaResesMaquila bbiListaResesDesarrollo bbiResesVenta bbiListaResesInactivos bbiListaResesSinRegistro bbiResesSinRegistro bbiNacimientos bbiAltasDestete bbiMortalidadReses",
 "people": "bbiUsers bbiCompradores bbiDueños bbiImplantadores bbiOperadores",
 "fence": "bbiFormacionCorrales bbiListaCorrales bbiCorralesAux bbiLoteCrianza btnCierreFormacion",
 "leaf": "bbiAlimentos bbiConsumo bbiAlimentacion BarButtonItem181",
 "document": "bbiDietas bbiCentroReportes bbiReporteImplantes bbiReportePesaje BarButtonItem196 bbiProtocolos btnProtocolosInicio bbiReporteReparto bbiImproductivos bbiReporteGerencial bbiReporteCalidad bbiReporteRechazos bbiReporteCrianza bbiFormatosBA bbi",
 "chart": "bbiResumenCorrales bbiDinamicoCompras bbiListaIndicadores bbiGraficas bbiGraficaAlimento bbiGraficasGerencial bbiGraficoAlimentacion bbiConsolidado",
 "truck": "bbiRemisiones bbiReparto bbiTransportistas bbiListaRecepciones",
 "scale": "bbiPesajeMateriaPrima bbiCalibraciones",
 "medical": "bbiEnfermeria BarButtonItem207 bbiSanidadCrianza",
 "syringe": "bbiImplantes BarButtonItem193 bbiEvaluacionImplantes bbiHistoricoImplantes",
 "search": "bbiDeteccion bbiBuscadorReses bbiEvaluacionDeteccion bbiCausasSanidad BarButtonItem203 BarButtonItem204 BarButtonItem205",
 "money": "bbiCompras bbiComprasProgramadores bbiLiquidaciones bbiReciboPagos bbiVentas",
 "tag": "bbiListaLecturas bbiDeteccionesElectronicos bbiCausaOrdinarioVenta",
 "arrows": "bbiTraslado bbiMovimientoCorrales bbiMovimientosPorLote",
 "gear": "bbiParoEquipos bbiListaEquipos bbiConfigurarOffline",
 "calendar": "bbiPlanDietas BarButtonItem185",
 "map": "bbiZonas bbiDistancias bbiListaRutasDieta btnAreasTrabajo",
 "bottle": "bbiProductos",
 "water": "bbiCalidadAgua",
 "shield": "bbiControlCalidad bbiRoles bbiCausasMuerte",
 "folder": "bsiC_Sanidad bsiC_PlantaAlimentos bsiC_Procesos BarSubItem1 BarSubItem2 BarSubItem3",
 "monitor": "bbiSistemaOffline",
 "percent": "bbiPorcentajes",
 "exit": "iExit",
 "help": "iHelp",
 "align": "iLeftTextAlign iCenterTextAlign iRightTextAlign iBoldFontStyle iItalicFontStyle iUnderlinedFontStyle",
 "palette": "rgbiSkins",
}
mapping={name:base for base,names in groups.items() for name in names.split()}
colors={"cow":GREEN,"people":BLUE,"fence":GREEN,"leaf":GREEN,"document":BLUE,"chart":BLUE,"truck":ORANGE,"scale":BLUE,"medical":RED,"syringe":PURPLE,"search":BLUE,"money":GREEN,"tag":ORANGE,"arrows":BLUE,"gear":BLUE,"calendar":ORANGE,"map":GREEN,"bottle":RED,"water":BLUE,"shield":GREEN,"folder":ORANGE,"monitor":BLUE,"percent":PURPLE,"exit":RED,"help":BLUE,"align":BLUE,"palette":PURPLE}
badges={}
for mark,names in {
 "plus":"bbiNacimientos bbiAltasDestete bbiFormacionCorrales bbiCompras bbiListaRecepciones btnProtocolosInicio",
 "minus":"bbiListaResesInactivos bbiConsumo",
 "x":"bbiMortalidadReses bbiCausasMuerte bbiReporteRechazos",
 "check":"bbiEvaluacionImplantes bbiEvaluacionDeteccion bbiReciboPagos bbiCalibraciones bbiFormatosBA btnCierreFormacion",
 "arrow":"bbiResesVenta bbiVentas bbiListaRutasDieta bbiReparto bbiListaResesDesarrollo",
 "pause":"bbiParoEquipos bbiSistemaOffline",
 "clock":"bbiHistoricoImplantes bbiComprasProgramadores bbiPlanDietas",
 "dot":"bbiResesSinRegistro bbiListaResesSinRegistro bbiListaResesMaquila bbiDeteccionesElectronicos",
}.items():
    for name in names.split(): badges[name]=mark

src=SOURCE.read_text(encoding="utf-8-sig")
captions=dict(re.findall(r'Me\.(\w+)\.Caption = "([^"]*)"',src))
controls=set(re.findall(r'(?:Friend|Private|Public).*?WithEvents\s+(\w+)\s+As\s+(?:DevExpress\.XtraBars\.)?Bar(?:Button|Sub|Check)Item',src,re.I))
missing=[n for n in controls if n in captions and n not in mapping]
if missing: raise RuntimeError(f"Controles sin asignar: {missing}")
records=[]
for name,base in mapping.items():
    if name not in captions: continue
    color=colors[base]
    if any(word in name for word in ("Implant","Sanidad","Crianza")): color=PURPLE if "Implant" in name else GREEN
    a=draw_base(base,color)
    if name in ("iCenterTextAlign","iRightTextAlign"):
        a=Icon()
        for y,w in ((6,24),(12,16),(18,24),(24,16)):
            x=(32-w)/2 if name=="iCenterTextAlign" else 28-w
            a.line([(x,y),(x+w,y)],BLUE,2)
    if name in ("iBoldFontStyle","iItalicFontStyle","iUnderlinedFontStyle"):
        a=Icon()
        if name=="iBoldFontStyle":
            a.line([(9,27),(9,5),(19,5),(23,8),(23,12),(19,16),(9,16),(20,16),(24,19),(24,24),(20,27),(9,27)],INK,3)
        elif name=="iItalicFontStyle":
            a.line([(13,5),(25,5)],INK,2)
            a.line([(20,5),(12,27)],INK,3)
            a.line([(7,27),(19,27)],INK,2)
        else:
            a.line([(8,5),(8,20),(11,24),(21,24),(24,20),(24,5)],INK,2.5)
            a.line([(7,29),(25,29)],BLUE,2)
    mark=badges.get(name)
    badge(a,mark,RED if mark=="x" else color)
    a.save(name)
    records.append(dict(control=name,texto=captions[name],simbolo=base,distintivo=mark,png=f"png32/{name}.png",svg=f"svg/{name}.svg",enlace_en_designer=bool(re.search(r'(?:LinkPersistInfo|ItemLinks\.Add)\(Me\.'+re.escape(name)+r'[\),]',src))))
(OUT/"manifest.json").write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding="utf-8")
cards=''.join(f'<article><div class="icons"><img src="{r["png"]}" width="32" height="32"><img src="{r["svg"]}" width="64" height="64"><span class="dark"><img src="{r["png"]}" width="32" height="32"></span></div><h3>{html.escape(r["texto"])}</h3><code>{r["control"]}</code><p><a href="{r["png"]}" download>PNG · 32 px</a> <a href="{r["svg"]}" download>SVG</a></p></article>' for r in records)
(OUT/"catalogo.html").write_text('''<!doctype html><html lang="es"><meta charset="utf-8"><title>Kit frmMain · 32 px</title><style>
*{box-sizing:border-box}body{margin:0;padding:40px;background:#f2f6fa;color:#24465b;font:15px system-ui}header{max-width:850px;margin-bottom:30px}h1{font-size:36px;margin:6px 0}header p{line-height:1.6}input{padding:14px;border:1px solid #bdcfdc;border-radius:12px;width:100%;max-width:600px;font:inherit}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(245px,1fr));gap:16px}article{padding:20px;background:white;border:1px solid #dce6ed;border-radius:16px}h3{font-size:15px;margin-bottom:6px}code{font-size:11px;overflow-wrap:anywhere}.icons{height:84px;display:flex;align-items:center;justify-content:space-between;gap:12px}.dark{background:#193044;border-radius:10px;padding:12px;display:flex}a{font-size:12px;color:#227bb0;margin-right:16px}
</style><header><small>CONTROL GANADERO / RECURSOS DE INTERFAZ</small><h1>Un lenguaje visual para frmMain</h1><p>'''+str(len(records))+''' recursos · PNG transparente de 32 × 32 px y SVG editable. Cada tarjeta muestra tamaño real, vector ampliado y prueba sobre fondo oscuro. Los símbolos relacionados comparten una familia visual.</p><input id="search" placeholder="Buscar botón, función o nombre de control…" aria-label="Buscar iconos"></header><main>'''+cards+'''</main><script>document.getElementById('search').oninput=e=>document.querySelectorAll('article').forEach(a=>a.hidden=!a.textContent.toLowerCase().includes(e.target.value.toLowerCase()))</script></html>''',encoding="utf-8")

# Contact sheet with native-size PNG assets for visual verification.
font=ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf",12)
small=ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf",10)
cols=6; w=1200; cellh=100
sheet=Image.new("RGB",(w,60+math.ceil(len(records)/cols)*cellh),"#F2F6FA")
d=ImageDraw.Draw(sheet); d.text((20,15),"CONTROL GANADERO  /  frmMain  /  PNG 32 x 32",font=font,fill=INK)
for i,r in enumerate(records):
    x=(i%cols)*200; y=60+(i//cols)*cellh
    d.rounded_rectangle((x+5,y+3,x+195,y+95),radius=8,fill="white")
    im=Image.open(OUT/r["png"]); sheet.paste(im,(x+16,y+12),im)
    label=r["texto"]
    if len(label)>27: label=label[:25]+"…"
    d.text((x+14,y+51),label,font=font,fill=INK)
    control=r["control"]
    d.text((x+14,y+73),control,font=small,fill="#667A89")
sheet.save(OUT/"vista_previa.png")
(OUT/"LEEME.md").write_text(f"""# Kit de iconos para frmMain

{len(records)} recursos originales, geométricos, a color y con fondo transparente.

- `png32/`: PNG RGBA de 32 × 32 píxeles.
- `svg/`: fuentes vectoriales de 32 × 32 unidades, escalables.
- `catalogo.html`: catálogo con búsqueda, tamaño real y prueba sobre fondo oscuro.
- `manifest.json`: relación entre control, texto del botón y archivos. `enlace_en_designer` indica si se encontró una referencia de enlace en el diseñador; no garantiza visibilidad en ejecución.
- `vista_previa.png`: lámina de todos los PNG a tamaño real.

Los nombres corresponden a FrmMain.designer.vb. Se incluyen controles auxiliares y antiguos que aún tienen Caption. Controles relacionados pueden compartir símbolo; algunos llevan distintivos de acción. Se omiten etiquetas de estado y controles sin texto.

## Uso en DevExpress

En el diseñador, selecciona el botón y asigna su PNG en `ImageOptions.LargeImage`. Si ya tiene `ImageOptions.SvgImage`, retíralo para que no prevalezca sobre el PNG. Para usar el vector, importa el SVG en `ImageOptions.SvgImage` y configura `SvgImageSize` a 32 × 32.

Puedes importar los PNG mediante el editor de recursos del proyecto. No asignes directamente rutas absolutas del catálogo en la aplicación distribuida.

El proyecto ControlGanadero no se ha modificado. La integración y revisión visual dentro del formulario quedan pendientes.

## Regeneración

Ejecuta `python crear_kit.py` desde la carpeta superior. Requiere Pillow y acceso al diseñador original. Los PNG se rasterizan a 4× y se reducen con antialiasing; las fuentes SVG se generan con las mismas primitivas geométricas.
""",encoding="utf-8")
for r in records:
    im=Image.open(OUT/r["png"])
    assert im.size==(32,32) and im.mode=="RGBA"
    assert im.getpixel((0,0))[3]==0
with zipfile.ZipFile(ROOT/"Kit_frmMain_32.zip","w",zipfile.ZIP_DEFLATED) as z:
    for f in OUT.rglob("*"):
        if f.is_file(): z.write(f,f.relative_to(ROOT))
    z.write(Path(__file__),"crear_kit.py")
print(f"Generados y verificados {len(records)} PNG y SVG. ZIP: {ROOT/'Kit_frmMain_32.zip'}")
