#!/usr/bin/env python3
"""Replace one full-slide misfire image with a source-limited SVG illustration.

The image is *newly drawn* from classroom Range Safety p.13 text, never an
extracted figure, third-party photograph, or assertion of current range rules.
Only this card's imageKey / visualId and the image index may change.
"""
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("app/src/main/assets")
INDEX = ROOT / "index.html"
REL = "media/misfire-classroom-original-schematic.svg"
KEY = "study_course_illustration_misfire"
SOURCE = "Firearms_Range_Saftey_Overview_11FEB26_V2.0.pdf"
PAGE = 13
GIT_BLOB_SHA1 = "088dce056fdde3c4eba03793a7f1d95333e9722d"


def locate(text, name):
    key = "window." + name + "="
    offset = text.index(key) + len(key)
    obj, used = json.JSONDecoder().raw_decode(text[offset:])
    return offset, offset + used, obj


def main():
    raw = (ROOT / REL).read_bytes()
    git_blob = b"blob " + str(len(raw)).encode() + b"\\x00" + raw
    if hashlib.sha1(git_blob).hexdigest() != GIT_BLOB_SHA1:
        raise AssertionError("Misfire schematic differs from exact audited Git blob")
    image = ET.fromstring(raw)
    if image.tag != "{http://www.w3.org/2000/svg}svg":
        raise AssertionError("Expected a self-contained SVG illustration")
    if image.attrib.get("viewBox") != "0 0 960 540":
        raise AssertionError("Schematic viewBox changed")
    for node in image.iter():
        name = node.tag.rsplit("}", 1)[-1].lower()
        if name in {"script", "image", "foreignobject", "iframe", "animate", "set"}:
            raise AssertionError("Misfire illustration contains forbidden embedded resource")
        if any("href" in k.lower() or k.lower().startswith("on") for k in node.attrib):
            raise AssertionError("Misfire illustration includes link or executable attribute")
    text = INDEX.read_text(encoding="utf-8")
    _, _, cards = locate(text, "GHC_STUDY_CARDS")
    _, _, images = locate(text, "GHC_STUDY_IMAGES")
    if len(cards) != 117:
        raise AssertionError("Study-card population changed unexpectedly")
    facts = {
        x["id"]: {k:v for k,v in x.items() if k not in ("visualId", "imageKey")}
        for x in cards
    }
    target = next((x for x in cards if x["id"] == "misfire"), None)
    if target is None:
        raise AssertionError("Misfire card is absent")
    if target.get("pages") != "13" or "10 seconds" not in json.dumps(target):
        raise AssertionError("Misfire card no longer matches cited 2026 range lesson")
    if target.get("imageKey") not in {"misfire", KEY}:
        raise AssertionError("Unexpected source image mapping; inspect before remapping")
    target["visualId"] = None
    target["imageKey"] = KEY
    images[KEY] = {
        "src": REL,
        "source": SOURCE,
        "page": PAGE,
        "authoredIllustration": True,
        "illustrationGitBlobSHA1": GIT_BLOB_SHA1,
        "illustrationOriginalCoursePage": 13,
        "review": (
            "NEW source-based pictorial schematic, not an embedded class photograph. "
            "Depicts muzzle downrange, the class's 10-second wait and instructor "
            "involvement; not a universal range procedure or authorization to handle a misfire."
        ),
    }
    if facts != {
        x["id"]: {k:v for k,v in x.items() if k not in ("visualId", "imageKey")}
        for x in cards
    }:
        raise AssertionError("Misfire image overlay changed facts, notes or IDs")
    for name, data in (("GHC_STUDY_CARDS", cards), ("GHC_STUDY_IMAGES", images)):
        start, end, _ = locate(text, name)
        text = text[:start] + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + text[end:]
    INDEX.write_text(text, encoding="utf-8")
    print("PASS: source-bound misfire SVG mapped; all 117 non-image card fields unchanged")


if __name__ == "__main__":
    main()
