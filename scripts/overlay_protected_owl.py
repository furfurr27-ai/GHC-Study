#!/usr/bin/env python3
"""Remap a protected-wildlife study card to an existing class owl photograph.

Run after crop_study_slide_images.py. This changes only visualId/imageKey;
the classroom card's prose, IDs, questions and saved state remain untouched.
"""
import json
from pathlib import Path

ASSETS = Path("app/src/main/assets")
INDEX = ASSETS / "index.html"
SOURCE_ID = "tawnyowl"
TARGET_ID = "protectedwildlife"
IMAGE_KEY = "study_reused_protected_owl"

def locate(text, name):
    prefix = "window." + name + "="
    start = text.index(prefix) + len(prefix)
    data, offset = json.JSONDecoder().raw_decode(text[start:])
    return start, start + offset, data

def main():
    text = INDEX.read_text(encoding="utf-8")
    _, _, cards = locate(text, "GHC_STUDY_CARDS")
    _, _, images = locate(text, "GHC_STUDY_IMAGES")
    source = next((x for x in cards if x["id"] == SOURCE_ID), None)
    target = next((x for x in cards if x["id"] == TARGET_ID), None)
    if source is None or target is None:
        raise ValueError("Study-card ID not found")
    existing = images.get(source.get("imageKey"))
    if not existing or existing.get("src") != "media/study-photo-tawnyowl.webp":
        raise ValueError("Source is not the previously audited original-class owl photo")
    if not (ASSETS / existing["src"]).is_file():
        raise ValueError("Original class owl photo absent")
    facts = {x["id"]: {k: v for k, v in x.items() if k not in ("imageKey", "visualId")} for x in cards}
    images[IMAGE_KEY] = {
        "src": existing["src"],
        "source": existing.get("source") or "Game - Predatory Birds (202609).pdf",
        "page": existing.get("page"),
        "photoReusedFromCardId": SOURCE_ID,
        "review": "Original classroom Waldkauz owl photo: protected-species example only, not current legal authorization"
    }
    target["visualId"] = None
    target["imageKey"] = IMAGE_KEY
    assert facts == {x["id"]: {k: v for k, v in x.items() if k not in ("imageKey", "visualId")} for x in cards}
    for name, value in [("GHC_STUDY_CARDS", cards), ("GHC_STUDY_IMAGES", images)]:
        left, right, _ = locate(text, name)
        text = text[:left] + json.dumps(value, ensure_ascii=False, separators=(",", ":")) + text[right:]
    INDEX.write_text(text, encoding="utf-8")
    print("PASS: original-class owl photo reused; Protected Wildlife card prose untouched")

if __name__ == "__main__":
    main()
