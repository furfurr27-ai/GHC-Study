#!/usr/bin/env python3
"""Check six individually audited safety answers and visible legacy-key warning.

Checks fully assembled HTML or actual APK, including the unaltered historical
exam correct keys and pre-answer warning in the quiz renderer.
"""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

EXPECTED = {
  "P2013-S3-Q02": (["b", "c"], "source_compared_key_conflict", ["B (climbing", "C (crossing", "D (getting", "SVLFG"]),
  "H2023-D08-Q052": (["a"], "source_compared_explanation_qualified", ["Hochsitz", "SVLFG"]),
  "H2023-D08-Q047": (["c"], "source_compared_explanation_qualified", ["vehicle", "Revier"]),
  "H2023-D17-Q008": (["a"], "source_compared_explanation_qualified", ["downrange", "bolt", "SVLFG"]),
  "H2023-D17-Q018": (["a"], "source_compared_explanation_qualified", ["safe direction", "SVLFG"]),
  "H2023-D08-Q024": (["b"], "source_compared_explanation_qualified", ["Jagdleiter", "stand", "briefing"]),
}
SVLFG = "https://www.svlfg.de/sichere-jagd"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apk")
    a = parser.parse_args()
    if a.apk:
        with ZipFile(a.apk) as apk:
            html = apk.read("assets/index.html").decode("utf-8")
    else:
        html = Path("app/src/main/assets/index.html").read_text(encoding="utf-8")
    begin = html.index("window.GHC_QUESTIONS=") + len("window.GHC_QUESTIONS=")
    bank, _ = json.JSONDecoder().raw_decode(html[begin:])
    if len(bank) != 867 or len({q["id"] for q in bank}) != 867:
        raise AssertionError("867 immutable source question IDs required")
    by_id = {q["id"]: q for q in bank}
    for id, (correct, status, keywords) in EXPECTED.items():
        q = by_id[id]
        review = q.get("sourceReview") or {}
        if q["correct"] != correct:
            raise AssertionError("Historical answer key changed: " + id)
        if review.get("status") != status or review.get("keyPreserved") is not True:
            raise AssertionError("Question's individual source review missing: " + id)
        if not review.get("checkedSource") or not review.get("classroomSource"):
            raise AssertionError("Classroom or official source citation missing: " + id)
        if q.get("explanation") != q.get("learningWhy"):
            raise AssertionError("Question explanation does not match Understand: " + id)
        if not all(word in q["learningWhy"] for word in keywords):
            raise AssertionError("Critical source-backed detail missing: " + id)
        if id == "P2013-S3-Q02":
            if review.get("sourceBankKeyDisputed") is not True:
                raise AssertionError("Incomplete archival answer key not flagged as disputed")
            if "Legacy key under factual dispute" not in q.get("preAnswerWarning", ""):
                raise AssertionError("Missing user-facing pre-answer warning")
            if "getting into a car" not in q["stem"].lower() and not any(
                "Getting into a car." in opt["text"] for opt in q["choices"]
            ):
                raise AssertionError("Vehicle option disappeared from disputed legacy item")
        elif review.get("sourceBankKeyDisputed"):
            raise AssertionError("Verified questions incorrectly marked disputed")
        if review.get("checkedSource") == SVLFG:
            if not any(ref.get("url") == SVLFG for ref in q.get("officialRefs", [])):
                raise AssertionError("Official source missing from record: " + id)
    warning_ui = "'+(current.preAnswerWarning?'<div class=\"alert\" role=\"note\"><strong>Source review notice:</strong> '+esc(current.preAnswerWarning)+'</div>':'')+"
    if html.count(warning_ui) != 1:
        raise AssertionError("Pre-answer quiz warning not rendered exactly once")
    print("PASS: 6 additional class+official safety reviews, 1 archived key dispute, source warning before grading" + (" (APK)" if a.apk else " (source)"))

if __name__ == "__main__":
    main()
