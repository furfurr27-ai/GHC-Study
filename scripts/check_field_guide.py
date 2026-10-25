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
assert len(cards)>=19
assert len({c["id"] for c in cards})==len(cards)
assert sum(bool(c.get("photo")) for c in cards)>=11
for item in cards:
  for key in ("id","de","en","latin","group","quick","idmarks","lookalike","habitat","cycle","social","sign","terms","caution","source","course"):
    assert isinstance(item.get(key),str) and item[key].strip(),(item["id"],key)
  src=item.get("photo","")
  if src:
    assert re.fullmatch(r"(?:trophy-test-media|media)/[\w.-]+",src),(item["id"],src)
    assert (ASSETS/src).is_file(),f"Missing offline media for {item['id']}: {src}"
for filename in ("field-guide.html","field-guide.js","field-guide-data.js"):
  assert (ASSETS/filename).stat().st_size>200,filename
if "--apk" in sys.argv:
  path=Path(sys.argv[sys.argv.index("--apk")+1])
  assert path.is_file(),path
  with zipfile.ZipFile(path) as f:
    names=set(f.namelist())
    expected={"assets/field-guide.html","assets/field-guide.js","assets/field-guide-data.js"}
    expected|={"assets/"+c["photo"] for c in cards if c.get("photo")}
    missing=expected-names
    assert not missing, f"APK is missing field-guide assets: {sorted(missing)}"
    html=f.read("assets/field-guide.html")
    assert b'src="https://' not in html,"Remote script or image added"
    print("PASS APK:",len(cards),"cards, all",sum(bool(x.get("photo")) for x in cards),"referenced local pictures packaged")
else:
  print("PASS source:",len(cards),"cards, all",sum(bool(x.get("photo")) for x in cards),"pictured species local")
