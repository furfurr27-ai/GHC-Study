#!/usr/bin/env python3
"""Verify field-guide species/media are offline and (optionally) inside a built APK."""
import json
import re
import sys
import zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/"app/src/main/assets"
data=(ASSETS/"field-guide-data.js").read_text(encoding="utf8")
m=re.fullmatch(r"(?s).*?window\.GHC_FIELD_SPECIES=(\[.*\]);\s*",data)
assert m,"Field cards must be a literal JSON array embedded in the JS data file"
cards=json.loads(m.group(1))
handbook_text=(ASSETS/"jungjaeger-data.js").read_text(encoding="utf8")
hm=re.fullmatch(r"(?s).*?window\\.GHC_JUNGJAEGER_CARDS=(\\[.*\\]);\\s*",handbook_text)
assert hm,"Jungjäger cards must be a literal JSON array embedded in local JS"
handbook=json.loads(hm.group(1))
assert len(handbook)>=40,"Missing offline customs and rule cards"
assert len({c["id"] for c in handbook})==len(handbook)
for entry in handbook:
  for key in ("id","de","en","group","kind","summary","note","source","course"):
    assert isinstance(entry.get(key),str) and entry[key].strip(),(entry["id"],key)
  assert isinstance(entry["steps"],list) and len(entry["steps"])>=2,entry["id"]
assert len({c["group"] for c in handbook})==6,"Missing Jungjäger chapter"
assert len(cards)>=19
assert len({c["id"] for c in cards})==len(cards)
assert sum(bool(c.get("photo")) for c in cards)==len(cards),"All field cards must have bundled animal pictures"
for item in cards:
  for key in ("id","de","en","latin","group","quick","idmarks","lookalike","habitat","cycle","social","sign","terms","caution","source","course"):
    assert isinstance(item.get(key),str) and item[key].strip(),(item["id"],key)
  src=item.get("photo","")
  if src:
    assert re.fullmatch(r"(?:trophy-test-media|media)/[\w.-]+",src),(item["id"],src)
    assert (ASSETS/src).is_file(),f"Missing offline media for {item['id']}: {src}"
for filename in ("field-guide.html","field-guide.js","field-guide-data.js","jungjaeger-data.js"):
  assert (ASSETS/filename).stat().st_size>200,filename
if "--apk" in sys.argv:
  path=Path(sys.argv[sys.argv.index("--apk")+1])
  assert path.is_file(),path
  with zipfile.ZipFile(path) as f:
    names=set(f.namelist())
    expected={"assets/field-guide.html","assets/field-guide.js","assets/field-guide-data.js","assets/jungjaeger-data.js"}
    expected|={"assets/"+c["photo"] for c in cards if c.get("photo")}
    missing=expected-names
    assert not missing, f"APK is missing field-guide assets: {sorted(missing)}"
    html=f.read("assets/field-guide.html")
    assert b'src="https://' not in html,"Remote script or image added"
    print("PASS APK:",len(cards),"animal cards and",len(handbook),"Jungjäger cards, all pictures and offline chapters packaged")
else:
  print("PASS source:",len(cards),"animal cards,",len(handbook),"Jungjäger cards, all pictured species local")
