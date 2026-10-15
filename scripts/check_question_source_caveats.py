#!/usr/bin/env python3
"""Verify individually sourced exam-question caveats in source HTML or built APK.

This checker is intentionally narrow: three questions verified against directly
checked course and Hessian authority evidence, not all 867 question explanations.
"""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

IDS = {
    "P2013-S4-Q05": (["a"], "50:50", "60:40", "2025"),
    "P2013-S4-Q08": (["a"], "Schwarzwild", "Schalenwild", "2025"),
    "H2023-D04-Q137": (["a"], "GHC RANGE DIFFERENCE", "instructor", "2026"),
}

def parse_bank(html):
    marker = "window.GHC_QUESTIONS="
    pos = html.index(marker) + len(marker)
    bank, _ = json.JSONDecoder().raw_decode(html[pos:])
    return bank

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apk", help="APK to inspect instead of source")
    args = parser.parse_args()
    if args.apk:
        with ZipFile(args.apk) as apk:
            html = apk.read("assets/index.html").decode("utf-8")
    else:
        html = Path("app/src/main/assets/index.html").read_text(encoding="utf-8")
    bank = parse_bank(html)
    assert len(bank) == 867, "Source question count drifted"
    by_id = {q["id"]: q for q in bank}
    assert len(by_id) == 867, "Duplicate question ID"
    for id, (answer, *signals) in IDS.items():
        q = by_id[id]
        assert q["correct"] == answer, f"{id}: answer key unexpectedly changed"
        assert q.get("sourceReview", {}).get("status") == "qualified_after_source_comparison", f"{id}: review missing"
        assert q["sourceReview"]["keyPreserved"] is True, f"{id}: source key drifted"
        assert q["explanation"] == q["learningWhy"], f"{id}: ambiguous explanation UIs"
        assert all(word in q["explanation"] for word in signals), f"{id}: critical safety/legal caveat lost"
        assert any("2025" in flag or "2026" in flag for flag in q.get("flags", [])), f"{id}: review flag missing"
    print("PASS: exact 3 source-reviewed questions qualified within 867 immutable answer keys" + (" (APK)" if args.apk else " (source)"))

if __name__ == "__main__":
    run()
