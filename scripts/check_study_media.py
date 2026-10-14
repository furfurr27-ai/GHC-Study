#!/usr/bin/env python3
"""Deterministic inventory of study-card image links and visual-review flags.

This is NOT an automated image classifier: the 2026-10-14 human-thumbnail
review is recorded separately in audit/study-media-review-20261014.json.
Default mode verifies asset integrity and records known visual defects; use
--strict when the release gate should reject any unresolved visual defects.
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path

def embedded_json(html, label):
    token = "window." + label + "="
    at = html.find(token)
    if at < 0:
        raise ValueError("Missing embedded " + token)
    return json.JSONDecoder().raw_decode(html[at + len(token):])[0]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apk", help="Inspect packaged APK assets rather than source directory")
    parser.add_argument("--strict", action="store_true", help="Fail if any visually flagged card remains")
    a = parser.parse_args()
    root = Path("app/src/main/assets")
    pkg = zipfile.ZipFile(a.apk) if a.apk else None
    try:
        def read(rel):
            if pkg:
                return pkg.read("assets/" + rel)
            return (root / rel).read_bytes()
        html = read("index.html").decode("utf-8")
        cards = embedded_json(html, "GHC_STUDY_CARDS")
        visuals = {v["id"]: v for v in embedded_json(html, "GHC_VISUALS")}
        extra = embedded_json(html, "GHC_STUDY_IMAGES")
        review = json.loads(Path("audit/study-media-review-20261014.json").read_text())
        flagged = set(review["slideOrPageLike"])
        mismatches = set(review["semanticMismatch"])
        repaired = set(review.get("assemblyCrops", []))
        assert repaired <= flagged and len(repaired) == review["counts"].get("assemblyCrops", 0)
        ids = {c["id"] for c in cards}
        assert len(cards) == len(ids) == review["counts"]["reviewed"], "Study-card inventory changed; refresh media audit"
        assert flagged.isdisjoint(mismatches), "Conflicting media-review flags"
        assert (flagged | mismatches) <= ids, "Media review references missing cards"
        assert len(flagged) == review["counts"]["slideOrPageLike"]
        assert len(mismatches) == review["counts"]["semanticMismatch"]
        assert len(ids - flagged - mismatches) == review["counts"]["standaloneLikely"]
        results = []
        failures = []
        for card in cards:
            vid, ikey = card.get("visualId"), card.get("imageKey")
            info = visuals.get(vid) if vid else None
            if not info and ikey:
                info = extra.get(ikey)
            rel = info.get("src") if info else None
            if not rel or not rel.startswith("media/") or ".." in rel:
                failures.append(card["id"] + ": no safe local image mapping")
                continue
            try:
                b = read(rel)
            except (FileNotFoundError, KeyError):
                failures.append(card["id"] + ": missing file " + rel)
                continue
            if len(b) < 256:
                failures.append(card["id"] + ": suspiciously small image " + rel)
            if card["id"] in repaired:
                expected = "media/study-photo-" + card["id"] + ".webp"
                if rel != expected:
                    failures.append(card["id"] + ": expected generated crop " + expected + ", got " + rel)
                kind = "cropped_standalone_photo"
            else:
                kind = "slide_or_page_like" if card["id"] in flagged else ("subject_mismatch" if card["id"] in mismatches else "likely_standalone_image")
            results.append({"id": card["id"], "title": card.get("title"), "image": rel, "bytes": len(b), "classification": kind})
        summary = {"checkedCardCount": len(cards), "resolvedImageCount": len(results), "uniqueImageCount": len({x["image"] for x in results}), "visualReview": review["counts"], "missingOrInvalid": failures, "cards": results}
        Path("build").mkdir(exist_ok=True)
        Path("build/study-media-inventory.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
        print("Study media:", len(results), "/", len(cards), "resolved;", summary["uniqueImageCount"], "unique images")
        print("Visual review:", len(flagged), "original slide/page-like;", len(repaired), "corrected in assembly;", len(flagged)-len(repaired), "remaining;", len(mismatches), "subject mismatches")
        if failures:
            for failure in failures:
                print("ERROR:", failure, file=sys.stderr)
            return 1
        if flagged - repaired or mismatches:
            print("WARNING: Full-slide images and/or subject mismatch remain. See build/study-media-inventory.json")
            if a.strict:
                return 2
        return 0
    finally:
        if pkg:
            pkg.close()

if __name__ == "__main__":
    raise SystemExit(main())
