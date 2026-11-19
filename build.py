"""src/page.html に地図データとクレジットを埋め込み、2つのファイルを書き出す。
- index.html    : GitHub Pages 用の完全なHTML
- artifact.html : claude.ai Artifact 用（<head>/<body>なしの断片）
使い方: python3 build.py
"""
import json, pathlib

root = pathlib.Path(__file__).parent
page = (root / "src" / "page.html").read_text(encoding="utf-8")
geo = (root / "geo.js").read_text(encoding="utf-8").strip()
world = (root / "world.js").read_text(encoding="utf-8").strip()
terrain = (root / "terrain.js").read_text(encoding="utf-8").strip()
neighbors = (root / "neighbors.js").read_text(encoding="utf-8").strip()
credits = json.loads((root / "images" / "credits.json").read_text(encoding="utf-8"))
page = page.replace("/*GEO*/", geo).replace("/*WORLD*/", world).replace("/*TERRAIN*/", terrain).replace("/*NEIGHBORS*/", neighbors).replace(
    "/*CREDITS*/", "window.CREDITS=" + json.dumps(credits, ensure_ascii=False) + ";")

(root / "artifact.html").write_text(page, encoding="utf-8")
(root / "index.html").write_text(
    '<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + page.replace("<header", "</head>\n<body>\n<header", 1) + "\n</body>\n</html>\n",
    encoding="utf-8")
print("built index.html and artifact.html")
