#!/usr/bin/env python3
"""Deterministic inventory of study-card image links and visual-review flags.

This is NOT an automated image classifier: the 2026-10-14 human-thumbnail
review is recorded separately in audit/study-media-review-20261014.json.
Default mode verifies asset integrity and records known visual defects; use
--strict when the release gate should reject any unresolved visual defects.
"""
import argparse
import json
import hashlib
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
        corrected_subjects = review.get("correctedSemanticMismatch", {})
        exact_figures = review.get("originalFigureRemaps", {})
        montages = review.get("assemblyMontages", {})
        reused = review.get("classPhotoReuse", {})
        authored = review.get("authoredCourseIllustrations", {})
        resolved = repaired | set(exact_figures) | set(montages) | set(reused) | set(authored)
        assert repaired <= flagged and len(repaired) == review["counts"].get("assemblyCrops", 0)
        ids = {c["id"] for c in cards}
        assert len(cards) == len(ids) == review["counts"]["reviewed"], "Study-card inventory changed; refresh media audit"
        assert flagged.isdisjoint(mismatches), "Conflicting media-review flags"
        assert (flagged | mismatches) <= ids, "Media review references missing cards"
        assert len(flagged) == review["counts"]["slideOrPageLike"]
        assert len(mismatches) == review["counts"]["semanticMismatch"]
        assert len(ids - flagged - mismatches - set(corrected_subjects)) == review["counts"]["standaloneLikely"]
        assert len(corrected_subjects) == review["counts"].get("correctedSemanticMismatch", 0)
        assert set(corrected_subjects).isdisjoint(flagged | mismatches)
        assert set(exact_figures) <= flagged and set(exact_figures).isdisjoint(repaired)
        assert len(exact_figures) == review["counts"].get("originalFigureRemaps", 0)
        assert len(montages) == review["counts"].get("assemblyMontages", 0)
        assert set(montages) <= flagged and set(montages).isdisjoint(repaired | set(exact_figures))
        assert set(reused) <= flagged and set(reused).isdisjoint(repaired | set(exact_figures) | set(montages))
        assert len(reused) == review["counts"].get("classPhotoReuse", 0)
        assert set(authored) <= flagged and set(authored).isdisjoint(repaired | set(exact_figures) | set(montages) | set(reused))
        assert len(authored) == review["counts"].get("authoredCourseIllustrations", 0)
        assert len(flagged - resolved) == review["counts"].get("remainingSlideOrPageLike")
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
            if card["id"] in corrected_subjects:
                expected = corrected_subjects[card["id"]]["image"]
                if rel != expected:
                    failures.append(card["id"] + ": original class diagram not installed (" + str(rel) + ")")
                else:
                    import hashlib
                    if hashlib.sha256(b).hexdigest() != corrected_subjects[card["id"]]["integritySha256"]:
                        failures.append(card["id"] + ": diagram binary differs from original verified course extraction")
                kind = "corrected_subject_mismatch"
            elif card["id"] in reused:
                source = reused[card["id"]]
                if rel != source["path"] or info.get("photoReusedFromCardId") != source["sourceCardId"]:
                    failures.append(card["id"] + ": audited classroom species photo reuse did not match expected source")
                kind = "reused_original_class_photo"
            elif card["id"] in montages:
                example = montages[card["id"]]
                if rel != example["path"]:
                    failures.append(card["id"] + ": expected original-image montage "+example["path"]+" but got "+str(rel))
                if "exampleCardIds" in example and info.get("pictureExampleCardIds") != example["exampleCardIds"]:
                    failures.append(card["id"] + ": gallery example/source IDs drifted")
                if "pictureSourcePageXrefs" in example and info.get("pictureSourcePageXrefs") != example["pictureSourcePageXrefs"]:
                    failures.append(card["id"] + ": original PDF page and image IDs drifted")
                if "imageSources" in example:
                    import hashlib
                    for source in example["imageSources"]:
                        try:
                            raw=read(source["path"])
                        except (FileNotFoundError,KeyError):
                            failures.append(card["id"] + ": source picture missing: " + source["path"])
                            continue
                        if hashlib.sha256(raw).hexdigest()!=source["sha256"]:
                            failures.append(card["id"] + ": source picture hash mismatch: " + source["path"])
                kind = "verified_class_source_picture_montage"
            elif card["id"] in exact_figures:
                figure = exact_figures[card["id"]]
                if rel != figure["path"]:
                    failures.append(card["id"] + ": expected the exact class PDF figure " + figure["path"] + ", got " + str(rel))
                else:
                    import hashlib
                    if hashlib.sha256(b).hexdigest() != figure["sha256"]:
                        failures.append(card["id"] + ": original class PDF image hash mismatch")
                    if info.get("originalPdfEmbeddedImageXref") != figure["xref"] or info.get("page") != figure["page"] or info.get("source") != figure["source"]:
                        failures.append(card["id"] + ": original figure source page/xref provenance drifted")
                kind = "direct_original_pdf_figure"
            elif card["id"] in authored:
                drawing = authored[card["id"]]
                if rel != drawing["path"]:
                    failures.append(card["id"] + ": authored classroom illustration mismatch: " + str(rel))
                if info.get("authoredIllustration") is not True:
                    failures.append(card["id"] + ": illustration incorrectly presented as original classroom photography")
                if info.get("source") != drawing["source"] or info.get("page") != drawing["page"]:
                    failures.append(card["id"] + ": original classroom lesson/page provenance drifted")
                if "originalClassroomPageRange" in drawing and info.get("originalClassroomPageRange") != drawing["originalClassroomPageRange"]:
                    failures.append(card["id"] + ": classroom slide-range source attribution drifted")
                expected_sha = drawing["gitBlobSha1"]
                actual_sha = hashlib.sha1(b"blob " + str(len(b)).encode() + b"\x00" + b).hexdigest()
                if actual_sha != expected_sha or info.get("illustrationGitBlobSHA1") != expected_sha:
                    failures.append(card["id"] + ": authored vector schematic checksum drifted")
                if not rel.endswith(".svg") or b"<script" in b.lower() or b"<foreignObject" in b:
                    failures.append(card["id"] + ": unsafe or invalid standalone vector asset")
                kind = "authored_course_text_schematic_not_original_pdf_figure"
            elif card["id"] in repaired:
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
        print("Visual review:", len(flagged), "original slide/page-like;", len(repaired), "picture crops;", len(exact_figures), "direct PDF figures;", len(montages), "source montages;", len(reused), "class-photo reuses;", len(authored), "author-drawn course diagrams;", len(flagged-resolved), "remaining;", len(mismatches), "subject mismatches;", len(corrected_subjects), "corrected wrong-subject illustration")
        if failures:
            for failure in failures:
                print("ERROR:", failure, file=sys.stderr)
            return 1
        if flagged - resolved or mismatches:
            print("WARNING: Full-slide images and/or subject mismatch remain. See build/study-media-inventory.json")
            if a.strict:
                return 2
        return 0
    finally:
        if pkg:
            pkg.close()

if __name__ == "__main__":
    raise SystemExit(main())
