#!/usr/bin/env python3
"""Inject the offline Schalenwild matrix into the recovered APK HTML.

The checked-in APK is our audited v1.4.5 baseline; the GitHub Actions build
recovers its index.html, then this script adds our independent module.
Idempotent, verifies the DOM anchors used by the UI, fails build on mismatch.
"""
from pathlib import Path
import sys

file = Path(sys.argv[1] if len(sys.argv)>1 else "app/src/main/assets/index.html")
html = file.read_text(encoding="utf-8")
head_tag = '<link rel="stylesheet" href="schalenwild-matrix.css" data-ghc-matrix="1">'
script_tag = '<script src="schalenwild-matrix.js" data-ghc-matrix="1"></script>'
assert html.count("</head>")==1 and html.count("</body>")==1, "Unexpected HTML structure"
for marker in ("function renderStudyCategory(catId)", "study-category-head", "studyHubBack", "studySearch"):
    assert marker in html, "Study category contract changed: " + marker
for path in ("schalenwild-matrix.css","schalenwild-matrix.js"):
    assert (file.parent/path).is_file(), "Missing offline asset: "+path
if head_tag not in html:
    html = html.replace("</head>", "  "+head_tag+"\n</head>", 1)
if script_tag not in html:
    html = html.replace("</body>", "  "+script_tag+"\n</body>", 1)
assert html.count(head_tag)==1 and html.count(script_tag)==1
file.write_text(html, encoding="utf-8")
print("Inserted Schalenwild matrix assets into", file, "| bytes:", file.stat().st_size)
