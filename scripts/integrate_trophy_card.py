#!/usr/bin/env python3
"""Insert source-reviewed trophy terminology into the existing offline Study Mode data."""
import json
from pathlib import Path

root = Path("app/src/main/assets")
html_path = root / "index.html"
source = json.loads((root / "trophy-antler-horn-card.json").read_text())
html = html_path.read_text(encoding="utf-8")
marker = "window.GHC_STUDY_CARDS="
start = html.index(marker) + len(marker)
cards, consumed = json.JSONDecoder().raw_decode(html[start:])
assert isinstance(cards, list) and len(cards) > 10
if any(c.get("id") == source["id"] for c in cards):
    raise SystemExit("Trophy card already exists; refusing duplicate")
card = {
    "id": source["id"],
    "category": "traditions",
    "title": source["title"],
    "english": "Trophies – Antlers and Horns",
    "priority": "!",
    "source": "Trophy Part 1 & 2 (2025); Game – Rotwild, Rehwild, Damwild, Mufflewild",
    "pages": "Class decks (see source list)",
    "detailsRows": [[section["heading"], " · ".join(section["facts"])] for section in source["details"]],
    "otherFacts": source["otherFacts"],
    "visualId": "roe_buck_summer"
}
cards.append(card)
replacement = json.dumps(cards, ensure_ascii=False, separators=(",", ":"))
html = html[:start] + replacement + html[start + consumed:]
html_path.write_text(html, encoding="utf-8")
assert source["id"] in html
print("Inserted trophy study card in Traditions; total cards:", len(cards))
