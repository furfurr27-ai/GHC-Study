#!/usr/bin/env python3
"""Audit enforcement for exact original 2013 paper markings/ammunition questions."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

EXPECTED={
"P2013-S3-Q07":(["b"],"source_compared_explanation_qualified",[".22 LR","CENTERFIRE","7x57R"]),
"P2013-S3-Q14":(["b"],"source_compared_explanation_qualified",["WaffG §24(1)","BeschG §6","TYPE OF AMMUNITION"]),
"P2013-S3-Q15":(["a"],"source_compared_key_conflict",["BeschG §3","§4(2)","MUTUAL RECOGNITION"]),
"P2013-S3-Q16":(["a"],"source_compared_explanation_qualified",["12-gauge","20-gauge","12/70"]),
}
ORIGINAL="https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view"

def main():
 p=argparse.ArgumentParser();p.add_argument("--apk");args=p.parse_args()
 if args.apk:
  with ZipFile(args.apk) as z:html=z.read("assets/index.html").decode("utf-8")
 else:html=Path("app/src/main/assets/index.html").read_text(encoding="utf-8")
 start=html.index("window.GHC_QUESTIONS=")+len("window.GHC_QUESTIONS=")
 qs,_=json.JSONDecoder().raw_decode(html[start:])
 assert len(qs)==867 and len({q["id"] for q in qs})==867
 byid={q["id"]:q for q in qs}
 for id,(original,status,phrases) in EXPECTED.items():
  q=byid[id];info=q.get("sourceReview") or {}
  assert q["correct"]==original,id
  assert info.get("status")==status and info.get("keyPreserved") is True,id
  assert info.get("originalPaperKeyVerified") is True,id
  assert info.get("originalPracticePaperSource")==ORIGINAL,id
  assert info.get("checkedSource") and info.get("classroomSource"),id
  assert q.get("learningWhy")==q.get("explanation") and all(s in q["explanation"] for s in phrases),id
  assert info.get("sourceBankKeyDisputed") is (status=="source_compared_key_conflict"),id
  if status=="source_compared_key_conflict":
   assert "2013" in q.get("preAnswerWarning","") and "BeschG" in q["preAnswerWarning"],id
   assert "safetyAcceptedCorrect" not in q, "No invented score-alternative allowed for proof-law nuance"
  else:
   assert "preAnswerWarning" not in q,id
 assert "Matched archival answer only" in html and "current.preAnswerWarning?" in html
 print("PASS: four sourced 2013 cartridge/marks/proof/gauge facts: 3 qualified, 1 overbroad archived law; 867 answer keys retained"+(" (APK)" if args.apk else " (source)"))

if __name__=="__main__":
 main()
