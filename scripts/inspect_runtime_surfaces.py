#!/usr/bin/env python3
"""Inspect runtime surfaces without exposing the large embedded question pool."""
import re
from pathlib import Path
s=Path("app/src/main/assets/index.html").read_text()
print("HTML bytes",len(s.encode()))
for term in ("function render(", "function goBack(", "function show", "let view=", "let mode=", "const view=", "const mode=", "localStorage", "history.pushState", "popstate", "study-back", "backlink", "addEventListener(", "function save", "function load"):
    print("PATTERN",repr(term),"count",s.count(term))
    hits=list(re.finditer(re.escape(term),s))
    for hit in hits[:3]:
        lo=max(0,hit.start()-180);hi=min(len(s),hit.end()+350)
        print("SNIPPET",re.sub(r"\s+"," ",s[lo:hi])[:550])
for pattern in (r"function\s+([A-Za-z_$][\w$]*)\s*\(",r"(?:let|const|var)\s+(view|mode|screen|page|section|selected\w+)\s*="):
    vals=re.findall(pattern,s)
    print("SYMBOLS",pattern,vals[:160],"total",len(vals))
