#!/usr/bin/env python3
"""Validate the source-reviewed trophy card stays integrated with its labeled class figure."""
import json
from pathlib import Path

root = Path("app/src/main/assets")
source = json.loads((root / "trophy-antler-horn-card.json").read_text(encoding="utf-8"))
html = (root / "index.html").read_text(encoding="utf-8")
prefix = "window.GHC_STUDY_CARDS="
pos = html.index(prefix) + len(prefix)
cards, _ = json.JSONDecoder().raw_decode(html[pos:])
matching = [card for card in cards if card.get("id") == source["id"]]
assert len(matching) == 1, "Trophy card must appear exactly once in Study Mode"
card = matching[0]
assert card["title"] == source["title"] == "Trophy Anatomy"
assert card["imageKey"] == "rotwild_antler_parts"
assert card["category"] == "traditions"
assert all(t in str(card["detailsRows"]) for t in ("Krone", "Rosenstock", "Eissprosse"))
images_start = html.index("window.GHC_STUDY_IMAGES=") + len("window.GHC_STUDY_IMAGES=")
images, _ = json.JSONDecoder().raw_decode(html[images_start:])
asset = images["rotwild_antler_parts"]["src"]
assert asset == source["imageFile"]
assert (root / asset).is_file(), "Course antler diagram missing from tracked media"
print("PASS: integrated English trophy title, complete class content, and labeled Rotwild image")
