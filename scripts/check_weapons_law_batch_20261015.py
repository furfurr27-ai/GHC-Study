#!/usr/bin/env python3
"""Verify five narrowly source-audited 2013 firearms-law cases in real APK.

Archival printed keys are immutable. Current-law mismatch warnings precede
grading; this is NOT permission to use the dated rule in current hunting.
"""
import argparse, json
from pathlib import Path
from zipfile import ZipFile

LAW = {
    "P2013-S3-Q01": (["c"], "source_compared_explanation_qualified", ["AWaffV", "DIN/EN 1143-1"]),
    "P2013-S3-Q03": (["e"], "source_compared_key_conflict", ["§ 12(3)(2)", "nicht zugriffsbereit"]),
    "P2013-S3-Q04": (["a"], "source_compared_explanation_qualified", ["6.5 mm", "2,000 J", "Rehwild"]),
    "P2013-S3-Q08": (["c"], "source_compared_explanation_qualified", ["nicht schussbereit", "nicht zugriffsbereit"]),
    "P2013-S3-Q11": (["c"], "source_compared_key_conflict", ["§19(1)(2)(c)", "MORE THAN THREE", "TOTAL"]),
}

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--apk")
    opts=a.parse_args()
    if opts.apk:
        with ZipFile(opts.apk) as z: html=z.read("assets/index.html").decode("utf-8")
    else:
        html=Path("app/src/main/assets/index.html").read_text(encoding="utf-8")
    begin=html.index("window.GHC_QUESTIONS=")+len("window.GHC_QUESTIONS=")
    questions,_=json.JSONDecoder().raw_decode(html[begin:])
    assert len(questions)==867 and len({q["id"] for q in questions})==867
    ids={q["id"]:q for q in questions}
    count=0
    for key,(answer,status,signals) in LAW.items():
        q=ids[key]
        meta=q.get("sourceReview") or {}
        assert q["correct"]==answer, "2013 original answer key drift: "+key
        assert meta.get("status")==status and meta.get("keyPreserved") is True, key
        assert meta.get("originalPaperKeyVerified") is True, key
        assert "Practice Hunting Test" in meta.get("originalPracticePaperSource",""), key
        assert meta.get("checkedSource","").startswith("https://www.gesetze-im-internet.de/"),key
        assert any(x.get("url")==meta["checkedSource"] for x in q.get("officialRefs",[])),key
        assert q["learningWhy"]==q["explanation"] and all(s in q["explanation"] for s in signals),key
        assert meta.get("sourceBankKeyDisputed") is (status=="source_compared_key_conflict"),key
        if status=="source_compared_key_conflict":
            assert q.get("preAnswerWarning") and "2013" in q["preAnswerWarning"],key
            assert "safetyAcceptedCorrect" not in q, "Do not invent alternative answer keys for ambiguous legal wording"
            count+=1
    assert count==2
    assert "current.preAnswerWarning?" in html, "Legacy law notices must actually render before answer"
    print("PASS: 5 original-paper and current-federal-law comparisons, 2 pre-answer law-change warnings, 867 source keys preserved"+(" (APK)" if opts.apk else " (source)"))

if __name__=="__main__":
    main()
