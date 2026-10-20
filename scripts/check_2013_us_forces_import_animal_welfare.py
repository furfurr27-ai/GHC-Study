#!/usr/bin/env python3
"""Check original-paper Q18 veterinarian and Q19 US Forces import caveat in APK."""
import argparse,json
from pathlib import Path
from zipfile import ZipFile

Q={
"P2013-S3-Q18":(["d"],"source_compared_explanation_qualified",["VETERINARIAN","TierSchG §4","TierSchG §17"]),
"P2013-S3-Q19":(["b"],"source_compared_key_conflict",["ARCHIVED 2013 TEST ANSWER","Verbringungserlaubnis","AEA Form 550-175A","BOTH U.S. Forces and German","WaffG §29"]),
}
ORIGINAL="https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view"
ARMY2026="https://home.army.mil/ansbach/1717/7260/6577/Infosheet_for_AE_Form_550-175A_-_March_2026.pdf"

def main():
 p=argparse.ArgumentParser();p.add_argument("--apk");opt=p.parse_args()
 if opt.apk:
  with ZipFile(opt.apk) as f:html=f.read("assets/index.html").decode("utf-8")
 else:html=Path("app/src/main/assets/index.html").read_text(encoding="utf-8")
 x=html.index("window.GHC_QUESTIONS=")+len("window.GHC_QUESTIONS=")
 qs,_=json.JSONDecoder().raw_decode(html[x:])
 assert len(qs)==867 and len({q["id"] for q in qs})==867
 index={q["id"]:q for q in qs}
 for id,(correct,status,tags) in Q.items():
  q=index[id];rv=q.get("sourceReview",{})
  assert q["correct"]==correct,(id,"historical key changed")
  assert rv.get("originalPracticePaperSource")==ORIGINAL and rv.get("originalPaperKeyVerified") is True,id
  assert rv.get("keyPreserved") is True and rv.get("status")==status,id
  assert rv.get("sourceBankKeyDisputed") is (status=="source_compared_key_conflict"),id
  assert q.get("learningWhy")==q.get("explanation") and all(t in q["explanation"] for t in tags),id
  assert rv.get("checkedSource") and len(q.get("officialRefs",[]))>=1,id
  assert "safetyAcceptedCorrect" not in q,"No made-up current AR import answer"
  if id=="P2013-S3-Q19":
   assert rv.get("checkedSource")==ARMY2026,id
   assert "not establish current import legality" in q.get("preAnswerWarning",""),id
   assert any(x.get("url")==ARMY2026 for x in q["officialRefs"]),id
  else:assert not q.get("preAnswerWarning"),id
 assert "current.preAnswerWarning?" in html and "Matched archival answer only" in html
 print("PASS: 2 precise source-backed Q18/Q19 records, current U.S. Forces import caveat and stable 867 exam keys"+(" (APK)" if opt.apk else " (source)"))

if __name__=="__main__":main()
