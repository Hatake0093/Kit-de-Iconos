"""Copia los SVG del Kit semantico a LectorComedero.Maui/Resources/Images.

En un proyecto .NET MAUI no hace falta registrar nada: los SVG que estan en
Resources/Images se empaquetan solos al compilar (MauiImage). Por eso este
script solo copia archivos.

Uso:
    python mover_kit_a_lectorcomedero.py                # simulacion (no cambia nada)
    python mover_kit_a_lectorcomedero.py --aplicar      # copia los SVG
    python mover_kit_a_lectorcomedero.py --aplicar --limpiar
        # ademas borra de Images los SVG que estaban en el kit en una corrida
        # anterior y ya no estan (manifiesto .kit_manifest.txt)
"""
import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
KIT = AQUI / "simulador de control ganadero" / "Kit_semantico" / "svg"
DESTINO = Path(r"C:\Users\uhw30\Documents\PRODUCCION\LectorComedero"
               r"\src\LectorComedero.Maui\Resources\Images")
MANIFIESTO = DESTINO / ".kit_manifest.txt"
RESPALDO = AQUI / "Respaldos" / "lectorcomedero_images"
NOMBRE_SEGURO = re.compile(r"[A-Za-z0-9_-]+\.svg")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aplicar", action="store_true", help="ejecutar (sin esto solo simula)")
    ap.add_argument("--limpiar", action="store_true",
                    help="borrar los SVG del kit que ya no estan en el kit")
    args = ap.parse_args()

    for p in (KIT, DESTINO):
        if not p.is_dir():
            sys.exit(f"No existe: {p}")

    kit = {f.name: f for f in KIT.glob("*.svg")}
    if not kit:
        sys.exit(f"No hay SVG en {KIT}")

    existentes = {f.name: f for f in DESTINO.glob("*.svg")}
    previos = set()
    if MANIFIESTO.exists():
        previos = {l.strip() for l in MANIFIESTO.read_text(encoding="utf-8").splitlines() if l.strip()}

    nuevos = sorted(n for n in kit if n not in existentes)
    reemplazos = sorted(n for n in kit if n in existentes)
    quitar = sorted(n for n in previos if n not in kit and n in existentes) if args.limpiar else []
    raros = sorted(n for n in kit if not NOMBRE_SEGURO.fullmatch(n))

    print(f"Kit:          {len(kit)} svg en {KIT}")
    print(f"Destino:      {DESTINO}")
    print(f"Nuevos:       {len(nuevos)}")
    print(f"Reemplazos:   {len(reemplazos)}  (mismo nombre; se sobrescriben)")
    print(f"Quitar:       {len(quitar)}  ({'activo con --limpiar' if not args.limpiar else 'del kit anterior'})")
    if raros:
        print("! Nombres con espacios o acentos (revisar; MAUI los puede renombrar):")
        for n in raros:
            print(f"    {n}")
    if nuevos[:15]:
        print("  Nuevos:", ", ".join(nuevos[:15]) + (" ..." if len(nuevos) > 15 else ""))

    if not args.aplicar:
        print("\nSimulacion: no se cambio nada. Usa --aplicar para ejecutar.")
        return

    if reemplazos or quitar:
        dest = RESPALDO / datetime.now().strftime("%Y%m%d_%H%M%S")
        dest.mkdir(parents=True)
        for n in reemplazos + quitar:
            shutil.copy2(existentes[n], dest / n)
        print(f"Respaldo de lo que se sobrescribe o quita: {dest}")

    for n in quitar:
        existentes[n].unlink()
    for n, src in sorted(kit.items()):
        shutil.copy2(src, DESTINO / n)

    MANIFIESTO.write_text("\n".join(sorted(kit)) + "\n", encoding="utf-8")
    print(f"Listo: {len(kit)} svg copiados a {DESTINO}")
    print("Recompila LectorComedero.Maui; los iconos quedan disponibles como 'nombre' (sin extension).")


if __name__ == "__main__":
    main()
