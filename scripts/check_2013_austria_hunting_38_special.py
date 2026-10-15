#!/usr/bin/env python3
"""Guard one manufacturer-confirmed revolver fact and one dated Austrian travel key.

Validate assembled questions OR actual APK assets, preserving original answer
letters and nonspoiling notice before historical Austria question is graded.
"""
import argparse,json
from pathlib import Path
from zipfile import ZipFile

ORIGINAL="https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view"
RUGER="https://ruger-docs.s3.amazonaws.com/_manuals/securitySix.pdf"
AUSTRIA="https://www.oesterreich.gv.at/de/lexicon/J/Seite.991741"
RULES={
 "P2013-S3-Q06":(["a"],"source_compared_explanation_qualified",
                 ["AMMUNITION","printed p.4","marked .357 Magnum","restricted to .38 Special"]),
 "P2013-S3-Q20":(["b"],"source_compared_key_conflict",
                 ["Jagdgastkarte","Bundesland","April 2026","European Firearms Pass","NOT itself hunting permission"]),
}
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--apk")
 args=p.parse_args()
 if args.apk:
  with ZipFile(args.apk) as apk:html=apk.read("assets/index.html").decode("utf-8")
 else:
  html=Path("app/src/main/assets/index.html").read_text("utf-8")
 mark="window.GHC_QUESTIONS=";a=html.index(mark)+len(mark)
 questions,_=json.JSONDecoder().raw_decode(html[a:])
 assert len(questions)==867 and len({q["id"] for q in questions})==867,"867 original keys required"
 byid={q["id"]:q for q in questions}
 for id,(correct,status,phrases) in RULES.items():
  q=byid[id];review=q.get("sourceReview") or {}
  assert q["correct"]==correct,(id,"archive key changed")
  assert review.get("status")==status and review.get("keyPreserved") is True,id
  assert review.get("originalPracticePaperSource")==ORIGINAL and review.get("originalPaperKeyVerified") is True,id
  assert review.get("sourceBankKeyDisputed") is (status=="source_compared_key_conflict"),id
  assert q.get("explanation")==q.get("learningWhy"),id
  assert all(t in q["explanation"] for t in phrases),(id,"missing critical source-backed context")
  assert any(x.get("url")==review.get("checkedSource") for x in q.get("officialRefs",[])),id
  assert not q.get("safetyAcceptedCorrect"),(id,"No additional automatic legal answer choices invented")
  if id=="P2013-S3-Q06":
   assert review["checkedSource"]==RUGER,id
   assert not q.get("preAnswerWarning"),id
   assert "screenshot inspected" in review.get("sourceNotes",""),id
  else:
   assert review["checkedSource"]==AUSTRIA,id
   assert "ARCHIVED checklist" in q.get("preAnswerWarning",""),id
   assert "province" in q["preAnswerWarning"].lower(),id
   assert "Matched archival answer only" in html,id
   assert "current.preAnswerWarning?" in html,id
 print("PASS: original 2013 .38 Special/.357 and provincial Austrian hunting-card source audits; 867 question answers preserved"+(" (APK)" if args.apk else " (source)"))

if __name__=="__main__":main()
