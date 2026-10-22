#!/usr/bin/env python3
"""Release gate: trophy room inventory, image crops, source-tagged notes, and isolated progress."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "app/src/main/assets"

def js_object(filename, name):
    text = (ASSETS / filename).read_text(encoding="utf-8")
    match = re.search(r"window\." + name + r"=(.*);\s*$", text, flags=re.S)
    assert match, "Missing or invalid " + name
    return json.loads(match.group(1))

cards = js_object("trophy-test-data.js", "GHC_TROPHY_CARDS")
facts = js_object("trophy-test-info-data.js", "GHC_TROPHY_INFO")
assert len(cards) == 29
assert len({c["id"] for c in cards}) == 29
assert sum(c["certainty"] == "identified" for c in cards) == 19
assert sum(c["certainty"] == "review" for c in cards) == 10
assert set(facts) == {c["id"] for c in cards}
assert {k: sum(x["sourceType"] == k for x in facts.values()) for k in ("study", "slides", "web")} == {"study": 13, "slides": 11, "web": 5}

for card in cards:
    ident = card["id"]
    assert card["group"] in ("Mammals", "Birds"), ident
    assert card["de"] and card["en"] and card["cue"] and card["contrast"], ident
    assert (ASSETS / "trophy-test-media" / (ident + ".jpg")).stat().st_size > 2000, ident
    source = facts[ident]
    assert source["title"] and source["rows"], ident
    assert all(len(pair) == 2 and pair[0] and pair[1] for pair in source["rows"]), ident
    if source["sourceType"] == "web":
        assert source["sourceUrl"].startswith("https://"), ident
        assert source.get("notes") and "External" in source["notes"], ident
    if card["certainty"] == "review":
        assert source.get("notes"), "Uncertain ID needs source qualifier: " + ident

html = (ASSETS / "index.html").read_text(encoding="utf-8")
assert html.count('id="ghc-trophy-test-launcher"') == 1
assert 'data-ghc-matrix="1"' in html, "Schalenwild matrix missing from assembled UI"
page = (ASSETS / "trophy-test.html").read_text(encoding="utf-8")
assert 'src="trophy-test-info-data.js"' in page
assert all('data-mode="' + m + '"' in page for m in ("cards", "flash", "quiz"))
app = (ASSETS / "trophy-test-app.js").read_text(encoding="utf-8")
assert "ghc-trophy-test-progress-v1" in app
assert "ghc-study-progress-v1" not in app
assert "c.certainty==='identified'" in app
assert "informationMarkup(current)" in app
print("PASS: 29 photo cards, 29 source-qualified fact sheets, 19 scoreable, 10 review-only; Quiz Mode and Schalenwild intact")
