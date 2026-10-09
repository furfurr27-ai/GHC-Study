#!/usr/bin/env python3
"""Preserve individual trophy facts as distinct visible rows in the legacy study card."""
import json
from pathlib import Path
p=Path("app/src/main/assets/index.html")
s=p.read_text(encoding="utf-8")
marker="window.GHC_STUDY_CARDS="
start=s.index(marker)+len(marker)
cards,n=json.JSONDecoder().raw_decode(s[start:])
source=json.loads(Path("app/src/main/assets/trophy-antler-horn-card.json").read_text(encoding="utf-8"))
matching=[c for c in cards if c.get("id")==source["id"]]
assert len(matching)==1
card=matching[0]
rows=[]
for section in source["details"]:
    for i,fact in enumerate(section["facts"]):
        rows.append([section["heading"] if i==0 else "•",fact])
assert len(rows)>10
card["detailsRows"]=rows
replacement=json.dumps(cards,ensure_ascii=False,separators=(",",":"))
p.write_text(s[:start]+replacement+s[start+n:],encoding="utf-8")
print("Trophy details formatted as",len(rows),"individual bullet rows")
