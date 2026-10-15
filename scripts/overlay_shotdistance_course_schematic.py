#!/usr/bin/env python3
"""Map a newly drawn shot-pellet danger-range schematic without altering facts.

Source is the GHC 2020 Weapons Overview slide text, independently corroborated
for the *rule of thumb* by RWS. Neither source establishes a safe boundary.
"""
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path("app/src/main/assets")
INDEX = ROOT / "index.html"
REL = "media/shotdistance-course-danger-illustration.svg"
KEY = "study_course_illustration_shotdistance"
SOURCE = "Weapons - Overview (2020).pdf"
GIT_BLOB_SHA1 = "85314e425b7152ba428e9be0a85cc6859ae5bc03"


def locate(text, name):
    token = "window." + name + "="
    start = text.index(token) + len(token)
    result, used = json.JSONDecoder().raw_decode(text[start:])
    return start, start + used, result


def main():
    raw = (ROOT / REL).read_bytes()
    git_blob = b"blob " + str(len(raw)).encode() + b"\x00" + raw
    if hashlib.sha1(git_blob).hexdigest() != GIT_BLOB_SHA1:
        raise AssertionError("Shot-distance illustration differs from verified Git blob")
    vector = ET.fromstring(raw)
    if vector.tag != "{http://www.w3.org/2000/svg}svg":
        raise AssertionError("Expected standalone SVG schematic")
    if vector.attrib.get("viewBox") != "0 0 960 540":
        raise AssertionError("Shot-distance diagram dimensions changed")
    for node in vector.iter():
        tag = node.tag.rsplit("}", 1)[-1].lower()
        if tag in {"script", "image", "foreignobject", "iframe", "animate", "set"}:
            raise AssertionError("Shot-distance illustration contains an embedded resource")
        if any("href" in k.lower() or k.lower().startswith("on") for k in node.attrib):
            raise AssertionError("Shot-distance illustration has link or executable attribute")
    text = INDEX.read_text(encoding="utf-8")
    _, _, cards = locate(text, "GHC_STUDY_CARDS")
    _, _, images = locate(text, "GHC_STUDY_IMAGES")
    if len(cards) != 117:
        raise AssertionError("Unexpected card count")
    facts = {c["id"]: {k:v for k,v in c.items() if k not in ("visualId", "imageKey")} for c in cards}
    card = next((c for c in cards if c["id"] == "shotdistance"), None)
    if card is None or card.get("pages") != "50-51" or "100" not in json.dumps(card):
        raise AssertionError("Class shot-danger rule/card provenance drifted")
    if card.get("imageKey") not in {"audit_wep_distance", KEY}:
        raise AssertionError("Shot-distance media mapping changed unexpectedly")
    card["imageKey"] = KEY
    card["visualId"] = None
    images[KEY] = {
        "src": REL,
        "source": SOURCE,
        "page": None,
        "originalClassroomPageRange": "50-51",
        "authoredIllustration": True,
        "illustrationGitBlobSHA1": GIT_BLOB_SHA1,
        "review": (
            "NEW source-grounded vector, not a PDF embedded photo. "
            "Shot diameter in mm x 100m is a course danger-distance heuristic, "
            "not an effective shooting range or safe boundary; drawing not to scale."
        ),
    }
    after = {c["id"]: {k:v for k,v in c.items() if k not in ("visualId", "imageKey")} for c in cards}
    if after != facts:
        raise AssertionError("Shot-distance overlay modified immutable card facts")
    for key, data in (("GHC_STUDY_CARDS", cards), ("GHC_STUDY_IMAGES", images)):
        start, stop, _ = locate(text, key)
        text = text[:start] + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + text[stop:]
    INDEX.write_text(text, encoding="utf-8")
    print("PASS: source-bound shot-distance SVG mapped with all card facts intact")


if __name__ == "__main__":
    main()
