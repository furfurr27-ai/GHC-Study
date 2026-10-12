#!/usr/bin/env python3
"""Safely split legacy inline CSS/JS into ordered offline files in a staging build.

Run after content integration; preserves script order and leaves tracked legacy HTML unchanged.
"""
import re
from pathlib import Path

root=Path("app/src/main/assets")
html=root/"index.html"
s=html.read_text(encoding="utf-8")
out=root/"modules"/"legacy"
out.mkdir(parents=True,exist_ok=True)
css=re.compile(r"<style(?P<attrs>[^>]*)>(?P<body>[\s\S]*?)</style>",re.I)
scripts=re.compile(r"<script(?P<attrs>[^>]*)>(?P<body>[\s\S]*?)</script>",re.I)
counts={"css":0,"js":0}
def extract_css(m):
    counts["css"]+=1
    name="style-%02d.css"%counts["css"]
    (out/name).write_text(m.group("body"),encoding="utf-8")
    return '<link rel="stylesheet" href="modules/legacy/'+name+'">'
s=css.sub(extract_css,s)
def extract_js(m):
    attrs=m.group("attrs")
    if re.search(r"\bsrc\s*=",attrs,re.I): return m.group(0)
    if re.search(r"\btype\s*=\s*['\"](?:application/json|importmap)",attrs,re.I): return m.group(0)
    counts["js"]+=1
    name="script-%02d.js"%counts["js"]
    (out/name).write_text(m.group("body"),encoding="utf-8")
    return '<script'+attrs+' src="modules/legacy/'+name+'"></script>'
s=scripts.sub(extract_js,s)
html.write_text(s,encoding="utf-8")
assert counts["js"]>=1
print("Split legacy assets:",counts)
