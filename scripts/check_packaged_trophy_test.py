#!/usr/bin/env python3
"""Inspect built APK bytes—not merely source tree—to prevent another silent feature regression."""
import json
import re
import sys
from zipfile import ZipFile

assert len(sys.argv) == 2, "Usage: check_packaged_trophy_test.py path/to/app.apk"
with ZipFile(sys.argv[1]) as apk:
    names = set(apk.namelist())
    required = [
        "assets/index.html", "assets/glossary-data.js",
        "assets/schalenwild-matrix.js", "assets/schalenwild-matrix.css",
        "assets/trophy-test.html", "assets/trophy-test-app.js",
        "assets/trophy-test-data.js", "assets/trophy-test-info-data.js",
        "assets/trophy-test-launcher.js",
    ]
    for asset in required:
        assert asset in names, "Missing APK asset: " + asset

    def read_js(name, filename):
        text = apk.read("assets/" + filename).decode("utf-8")
        match = re.search(r"window\." + name + r"=(.*);\s*$", text, flags=re.S)
        assert match, "Missing inventory " + name
        return json.loads(match.group(1))

    cards = read_js("GHC_TROPHY_CARDS", "trophy-test-data.js")
    facts = read_js("GHC_TROPHY_INFO", "trophy-test-info-data.js")
    assert len(cards) == 29 and len({c["id"] for c in cards}) == 29
    assert sum(c["certainty"] == "identified" for c in cards) == 19
    assert set(facts) == {c["id"] for c in cards}
    assert {k: sum(x["sourceType"] == k for x in facts.values()) for k in ("study", "slides", "web")} == {"study": 13, "slides": 11, "web": 5}
    for c in cards:
        image = "assets/trophy-test-media/" + c["id"] + ".jpg"
        assert image in names and apk.getinfo(image).file_size > 2000, image
    assert not any("/trophy-test/photos/" in n for n in names), "Original room photos must not be bundled"

    home = apk.read("assets/index.html").decode("utf-8")
    assert 'id="ghc-trophy-test-launcher"' in home, "Trophy Test Quiz Mode tile missing"
    assert 'data-ghc-matrix="1"' in home, "Schalenwild UI not installed"
    match = re.search(r"window\.GHC_PRACTICE2_QUESTIONS=(.*?);\s*window\.GHC_SOURCES", home, flags=re.S)
    assert match, "Practice Test 2 native question bank missing"
    practice2 = json.loads(match.group(1))
    assert len(practice2) == 125 and len({x["id"] for x in practice2}) == 125, "Practice Test 2 loss"
    assert [sum(q["section"] == n for q in practice2) for n in range(1, 6)] == [25]*5, "Practice Test 2 parts missing"
    assert "studyHubBack" in home and "studySearch" in home, "Navigation regression"
    assert b'src="trophy-test-info-data.js"' in apk.read("assets/trophy-test.html")
    assert b"informationMarkup(current)" in apk.read("assets/trophy-test-app.js")
    assert any(n.startswith("res/mipmap") or n.endswith("ic_launcher.png") for n in names), "Launcher icon missing"
print("PASS: actual APK has all 29 photo+fact cards, 125 Practice Test 2 questions, glossary, Schalenwild, and icon")
