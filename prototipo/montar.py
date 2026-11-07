"""Monta o protótipo num único arquivo HTML, embutindo fotos e texturas.

Uso: python3 prototipo/montar.py
Lê prototipo/src/index.html e prototipo/assets/, e grava prototipo/index.html.
"""
import base64
import json
from pathlib import Path

raiz = Path(__file__).parent
assets = raiz / "assets"
html = (raiz / "src" / "index.html").read_text(encoding="utf-8")


def data_uri(nome):
    dados = base64.b64encode((assets / f"{nome}.jpg").read_bytes()).decode()
    return f"data:image/jpeg;base64,{dados}"


for tex in ["wood", "leather", "paper", "endpaper"]:
    html = html.replace("{{IMG:%s}}" % tex, data_uri(tex))

fotos = [p.stem for p in assets.glob("*.jpg") if p.stem not in {"wood", "leather", "paper", "endpaper"}]
html = html.replace("{{IMGS_JSON}}", json.dumps({f: data_uri(f) for f in sorted(fotos)}))
html = html.replace("{{CREDITOS_JSON}}", (assets / "creditos.json").read_text(encoding="utf-8"))

saida = raiz / "index.html"
saida.write_text(html, encoding="utf-8")
print(f"{saida} ({saida.stat().st_size // 1024} KB)")
