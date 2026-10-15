#!/usr/bin/env python3
"""Map an authored, clearly non-official example of Hessian roe-deer harvest planning.

Based on official 2025 Landkreis-Main-Kinzig Anlage 2b planning PDF wording,
not a copy of the legally operative 2026 XLSX form (not accessed). Exact image
hash/provenance checked. Study data, IDs, keys and storage are immutable.
"""
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("app/src/main/assets")
INDEX = ROOT / "index.html"
REL = "media/abschussplan-hessen-anlage2b-educational.svg"
KEY = "study_source_illustration_abschussplan"
GIT_BLOB_SHA1 = "a333ad9456c5e065a1ed6990e37676210d36a34c"
SOURCE = "Nature and animal protection feb 2019.pdf"
HESSEN_FORM = "https://www.mkk.de/media/resources/pdf/mkk_de_1/buergerservice_1/lebenslagen_1/sicherheit_und_ordnung_1/32_kreisordnungsamt_1/jagdbehoerde/2025_4/Abschussplanung_Rehwild.pdf"
OFFICIAL_LIST = "https://rp-kassel.hessen.de/forsten-und-landwirtschaft/jagd"

def locate(text, name):
    marker = "window." + name + "="
    start = text.index(marker) + len(marker)
    obj, used = json.JSONDecoder().raw_decode(text[start:])
    return start, start + used, obj

def main():
    raw = (ROOT / REL).read_bytes()
    gitblob = b"blob " + str(len(raw)).encode() + b"\x00" + raw
    if hashlib.sha1(gitblob).hexdigest() != GIT_BLOB_SHA1:
        raise AssertionError("Authored Abschussplan picture differs from reviewed source bytes")
    tree = ET.fromstring(raw)
    if tree.tag != "{http://www.w3.org/2000/svg}svg":
        raise AssertionError("Expected standalone vector illustration")
    if tree.attrib.get("viewBox") != "0 0 960 540":
        raise AssertionError("Unexpected plan SVG dimensions")
    text_nodes = []
    for node in tree.iter():
        tag = node.tag.rsplit("}", 1)[-1].lower()
        if tag in {"script", "image", "foreignobject", "iframe", "animate", "set"}:
            raise AssertionError("Embedded resources disallowed")
        if any("href" in k.lower() or k.lower().startswith("on") for k in node.attrib):
            raise AssertionError("No external links or executable attributes allowed")
        if tag == "text":
            text_nodes.append("".join(node.itertext()))
    contents = " ".join(text_nodes)
    if not all(s in contents for s in ["ABSCHUSSPLAN", "Jagdbezirk", "Planungszeitraum", "VORSCHLAG", "NOT AN OFFICIAL FORM"]):
        raise AssertionError("Source qualifiers or planning concepts missing")
    html = INDEX.read_text(encoding="utf-8")
    _, _, cards = locate(html, "GHC_STUDY_CARDS")
    _, _, images = locate(html, "GHC_STUDY_IMAGES")
    if len(cards) != 117:
        raise AssertionError("Unexpected card count")
    original = {c["id"]: {k:v for k,v in c.items() if k not in ("imageKey", "visualId")} for c in cards}
    card = next((c for c in cards if c["id"] == "abschussplan"), None)
    if card is None or "harvest" not in card.get("english", "").lower():
        raise AssertionError("Abschussplan card missing or changed")
    if card.get("imageKey") not in {"abschussplan", KEY}:
        raise AssertionError("Unexpected Abschussplan image; inspect before replacing")
    if card.get("source") != SOURCE:
        raise AssertionError("Classroom card source changed")
    card["imageKey"] = KEY
    card["visualId"] = None
    images[KEY] = {
        "src": REL,
        "source": SOURCE,
        "page": None,
        "classroomPageRange": "20, 32",
        "authoredIllustration": True,
        "notOfficialForm": True,
        "illustrationGitBlobSHA1": GIT_BLOB_SHA1,
        "referenceFormPDF": HESSEN_FORM,
        "referenceFormAuthority": "Main-Kinzig-Kreis Jagdbehoerde (Hessen), PDF published in 2025 path",
        "officialPlanningFormsList": OFFICIAL_LIST,
        "review": (
            "NEW educational planning-process illustration based on the 2025 publicly posted "
            "Hessian Anlage 2b Rehwild PDF and original GHC class concept. NOT an official or "
            "fillable form; exact current RP Kassel 2026 XLSX form fields not inspected. "
            "Differentiates retrospective Jahresstrecke from prospective Abschussvorschlag."
        ),
    }
    now = {c["id"]: {k:v for k,v in c.items() if k not in ("imageKey", "visualId")} for c in cards}
    if now != original:
        raise AssertionError("Image overlay changed card facts")
    for key, data in (("GHC_STUDY_CARDS", cards), ("GHC_STUDY_IMAGES", images)):
        begin, end, _ = locate(html, key)
        html = html[:begin] + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + html[end:]
    INDEX.write_text(html, encoding="utf-8")
    print("PASS: class-based Abschussplan educational SVG installed with facts intact")

if __name__ == "__main__":
    main()
