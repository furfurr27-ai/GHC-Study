#!/usr/bin/env python3
"""Verify the *packaged APK* contains the audited, searchable offline glossary.

This audits packaged bytes, not merely source files before Android assembly.
It verifies source/provenance metadata but does not certify historical accuracy.
"""
import argparse
import json
import zipfile
from pathlib import Path


def parse_glossary(js):
    tag = "window.GHC_GLOSSARY="
    pos = js.find(tag)
    if pos == -1:
        raise AssertionError("APK glossary data declaration missing")
    values, _ = json.JSONDecoder().raw_decode(js[pos + len(tag):])
    return values


def audit(apk):
    with zipfile.ZipFile(apk) as archive:
        js = archive.read("assets/glossary-data.js").decode("utf-8")
        html = archive.read("assets/glossary.html").decode("utf-8")
        archive.read("assets/index.html")
        archive.read("res/drawable/ic_launcher.png")
    terms = parse_glossary(js)
    assert len(terms) == 162, "Unexpected glossary population"
    ids = [item["id"] for item in terms]
    assert len(set(ids)) == 162, "Duplicate glossary IDs"
    by_id = {item["id"]: item for item in terms}
    assert sum(t["status"] == "defined" for t in terms) == 160, "Defined meaning regression"
    pending = {t["id"] for t in terms if t["status"] == "pending"}
    assert pending == {"x118", "x148"}, f"Unexpected undefined terms: {pending}"
    original = [t for t in terms if t["id"].startswith("v")]
    assert {t["id"] for t in original} == {f"v{i:03d}" for i in range(1, 78)}, "Original 77 term IDs drifted"
    origin_notes = [t for t in terms if t.get("etymology", "").strip()]
    assert len(origin_notes) == 77 and all(t["id"].startswith("v") for t in origin_notes), "Inherited etymology text loss"
    verified = [t for t in origin_notes if t.get("originVerification") == "verified"]
    assert {t["id"] for t in verified} == {"v047", "v064"}, "Verified origin list drifted"
    assert all("duden.de" in t.get("originSource", "") for t in verified), "Origin lacks verifiable source"
    assert len(origin_notes) - len(verified) == 75
    assert all(t.get("originVerification") != "verified" for t in origin_notes if t["id"] not in {"v047", "v064"})
    assert "origin-unverified" in html and "origin-verified" in html, "Glossary UI lacks provenance labels"
    assert "originVerified(x)" in html and "originSource" in html, "Verified origin display guard missing"
    assert "55 worksheet-only" not in html, "Old status count leaked into APK"
    assert "secret code" in by_id["v047"]["etymology"], "Schweiß historical caveat was removed"
    report = {
        "apk": Path(apk).name,
        "glossaryTerms": len(terms),
        "definedMeanings": 160,
        "pendingTermIds": sorted(pending),
        "inheritedWordOriginNotes": len(origin_notes),
        "verifiedWordOriginIds": sorted(t["id"] for t in verified),
        "unverifiedWordOriginNotes": len(origin_notes) - len(verified),
        "uiProvenanceLabelsPresent": True,
        "scope": "APK packaged-byte structural and provenance verification, not etymology or physical Android correctness",
    }
    output = Path("build/packaged-glossary-audit.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print("PASS: APK glossary", report["glossaryTerms"], "terms;",
          len(verified), "verified origins;",
          report["unverifiedWordOriginNotes"], "unverified origins")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("apk")
    args = parser.parse_args()
    audit(args.apk)
