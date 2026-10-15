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
            if review.get("originalPaperKeyVerified") is not True:
                raise AssertionError("Original 2013 source PDF printed key must be directly checked")
            if review.get("originalPracticePaperSource") != "https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view":
                raise AssertionError("Checked 2013 practice-test original PDF citation missing")
            if "actual 19 December 2013 paper Answer Key" not in q["explanation"]:
                raise AssertionError("Original archived answer key finding absent from learner explanation")
            if q.get("safetyAcceptedCorrect") != ["b", "c", "d"]:
                raise AssertionError("Incomplete 2013 key requires B/C/D alternative accepted score while keeping historical B/C")
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
    if html.count("safetyAnswer={},extra=current.safetyAcceptedCorrect||[];") != 1:
        raise AssertionError("Quiz must allow safety-complete response without mutating stored historical key")
    if html.count("acceptedSafety&&!!safetyAnswer[id]") != 1:
        raise AssertionError("Alternative safe answer choices must be displayed correctly")
    if "Correct — safety-complete answer" not in html or "Matched archived 2013 key" not in html:
        raise AssertionError("Must distinguish safety and historical key in learner feedback")
    print("PASS: 6 additional class+official safety reviews, 1 archived key dispute, source warning before grading" + (" (APK)" if a.apk else " (source)"))

if __name__ == "__main__":
    main()
