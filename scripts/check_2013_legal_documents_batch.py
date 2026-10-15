#!/usr/bin/env python3
"""Check four separately source-verified 2013 printed GHC answers.

The historical questions remain immutable even when modern law conflicts.
Inspect the assembled HTML or the actual packaged APK.
"""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

CASE = {
    "P2013-S3-Q05": (["a", "c", "d"], "source_compared_explanation_qualified", ["§38(1)", "§13(4)", "Jagdschein"]),
    "P2013-S3-Q09": (["b"], "source_compared_key_conflict", ["§13(3)", "TWO WEEKS", "LONG GUN"]),
    "P2013-S3-Q10": (["c"], "source_compared_explanation_qualified", ["§10(1)", "handgun", "Jagdschein alone"]),
    "P2013-S3-Q13": (["c"], "source_compared_key_conflict", ["§32", "warning shot", "NEVER"]),
}
ORIGINAL = "https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view"

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--apk")
    opts=p.parse_args()
    if opts.apk:
        with ZipFile(opts.apk) as apk:
            html=apk.read("assets/index.html").decode("utf-8")
    else:
        html=Path("app/src/main/assets/index.html").read_text(encoding="utf-8")
    begin=html.index("window.GHC_QUESTIONS=")+len("window.GHC_QUESTIONS=")
    bank,_=json.JSONDecoder().raw_decode(html[begin:])
    assert len(bank)==867 and len({q["id"] for q in bank})==867, "867 stable question IDs expected"
    lookup={q["id"]:q for q in bank}
    for qid,(correct,status,phrases) in CASE.items():
        q=lookup[qid]
        ref=q.get("sourceReview") or {}
        assert q["correct"]==correct,(qid,"Historical original paper answer changed")
        assert ref.get("status")==status and ref.get("keyPreserved") is True,qid
        assert ref.get("originalPracticePaperSource")==ORIGINAL and ref.get("originalPaperKeyVerified") is True,qid
        assert ref.get("sourceBankKeyDisputed") is (status=="source_compared_key_conflict"),qid
        assert ref.get("checkedSource","").startswith("https://www.gesetze-im-internet.de/"),qid
        assert q.get("explanation")==q.get("learningWhy") and all(t in q["explanation"] for t in phrases),qid
        assert any(x.get("url")==ref["checkedSource"] for x in q.get("officialRefs",[])),qid
        assert "safetyAcceptedCorrect" not in q,"Do not invent multiple correct choices for legally nuanced 2013 wording"
        if status=="source_compared_key_conflict":
            assert q.get("preAnswerWarning") and "2013" in q["preAnswerWarning"],qid
        assert "current.preAnswerWarning?" in html,"Quiz must show a legal source warning BEFORE checking"
    assert "Matched archival answer only" in html, "Disputed keyed answers must not get an unqualified correct label"
    print("PASS: four original-paper document/self-defense law records (2 qualified/2 flagged), original keys and rendered law warning retained"+(" (actual APK)" if opts.apk else " (source)"))

if __name__=="__main__":
    main()
