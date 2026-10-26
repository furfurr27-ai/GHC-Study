#!/usr/bin/env python3
"""Validate new field guide map/season assets are actually shipped in an APK."""
import re
import sys
from pathlib import Path
from zipfile import ZipFile
apk = Path(sys.argv[1])
required = [
    "assets/field-guide.html", "assets/field-guide.js",
    "assets/field-guide-data.js", "assets/jungjaeger-data.js",
    "assets/germany-map-data.js", "assets/state-season-data.js",
    "assets/season-engine.js", "assets/state-map-controller.js",
    "assets/index.html", "assets/glossary-data.js",
    "assets/trophy-test.html", "assets/trophy-test-data.js"
]
with ZipFile(apk) as z:
    have = set(z.namelist())
    missing = [p for p in required if p not in have]
    assert not missing, "Missing offline assets: " + repr(missing)
    html = z.read("assets/field-guide.html").decode("utf-8")
    engine = z.read("assets/season-engine.js").decode("utf-8")
    controller = z.read("assets/state-map-controller.js").decode("utf-8")
    mapdata = z.read("assets/germany-map-data.js").decode("utf-8")
    states = z.read("assets/state-season-data.js").decode("utf-8")
    expected = ["DE-BW", "DE-BY", "DE-BE", "DE-BB", "DE-HB", "DE-HH",
                "DE-HE", "DE-MV", "DE-NI", "DE-NW", "DE-RP", "DE-SL",
                "DE-SN", "DE-ST", "DE-SH", "DE-TH"]
    for code in expected:
        assert code in mapdata and code in states, "Missing " + code
    assert mapdata.count('"code":"DE-') == 16, "Expected 16 original SVG paths"
    assert states.count('"code": "DE-') == 16, "Expected 16 state metadata entries"
    assert '"id": "wildcat"' not in states, "Unexpected protected-species entry encoding"
    assert '"wildcat": {' in states and '"unverified": true' in states
    assert 'ghc-selected-bundesland-v1' in controller
    assert 'ghc-field-favorites-v1' not in controller, "Controller must not rename favorites key"
    assert 'Europe/Berlin' in engine
    assert 'UNKNOWN_OR_STALE' in engine and 'CONDITIONAL' in engine
    assert 'ghc-selected-bundesland-v1' not in html, "Selection is runtime storage, not hardcoded"
    assert not re.search(r'<script[^>]+src=["\']https?://', html, re.I)
    for script in ["germany-map-data.js", "state-season-data.js", "season-engine.js", "state-map-controller.js"]:
        assert '<script src="'+script+'"></script>' in html, script + " not loaded"
    assert 'src="field-guide.js"' in html
    assert 'org.ghcstudy.v141' not in html, "Avoid default-app ID hardcoded in WebView"
    assert sum(p.startswith("assets/media/") for p in have) >= 18, "Lost bundled offline study media"
    print("PASS: packaged state map, 16 geometric paths and jurisdictions, sourced season evaluator, offline media and original study archive")
