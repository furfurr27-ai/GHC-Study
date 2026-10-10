#!/usr/bin/env python3
"""Regression checks for grouped trophy facts and visible vocabulary label."""
import json
from pathlib import Path
root=Path("app/src/main/assets")
html=(root/"index.html").read_text(encoding="utf-8")
source=json.loads((root/"trophy-antler-horn-card.json").read_text(encoding="utf-8"))
marker="window.GHC_STUDY_CARDS="
cards,_=json.JSONDecoder().raw_decode(html[html.index(marker)+len(marker):])
card=next(c for c in cards if c.get("id")==source["id"])
rows=card["detailsRows"]
assert len(rows)==len(source["details"]), "Each trophy section needs exactly one shared panel"
for row,section in zip(rows,source["details"]):
    assert row[0]==section["heading"]
    assert row[1].count("trophy-fact")==len(section["facts"])
    assert all(fact.replace("&","&amp;") in row[1] for fact in section["facts"])
assert "Jägersprache1" not in html
assert "Jägersprache" in html
assert "row(" + chr(39) + "vocabulary" + chr(39) + "," + chr(39) + "Jägersprache" + chr(39) in html
print("PASS: grouped trophy sections and vocabulary label")
