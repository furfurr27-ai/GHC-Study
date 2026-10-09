#!/usr/bin/env python3
"""Keep trophy facts as bullets inside their shared section panel."""
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
card["detailsRows"]=[
    [section["heading"],"".join("<div class='trophy-fact'>• "+fact.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")+"</div>" for fact in section["facts"])]
    for section in source["details"]
]
replacement=json.dumps(cards,ensure_ascii=False,separators=(",",":"))
result=s[:start]+replacement+s[start+n:]
result=result.replace("Jägersprache1","Jägersprache")
p.write_text(result,encoding="utf-8")
print("Trophy details grouped in",len(card["detailsRows"]),"section panels")
