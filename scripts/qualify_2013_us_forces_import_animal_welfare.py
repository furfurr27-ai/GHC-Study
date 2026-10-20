#!/usr/bin/env python3
"""Original-paper/2026 military-customs verification for two exact 2013 questions.

Q19 is flagged as a dated blanket answer, NOT converted into permission to
import any firearm. Q18 is the qualified veterinary referral scenario.
Never alter original paper keyed answers, IDs, options or progress identifiers.
"""
import json
from pathlib import Path
INDEX=Path("app/src/main/assets/index.html")
PAPER="https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view"
ARMY_REG="https://www.aepubs.eur.army.mil/AE-Regulations/smdsearch8659/190-6/"
CUSTOMS_2026="https://home.army.mil/ansbach/1717/7260/6577/Infosheet_for_AE_Form_550-175A_-_March_2026.pdf"
JAG_2025="https://www.21tsc.army.mil/Portals/21/JAG/KLI-2025-4%20Fall%20Newsletter.pdf?ver=bcojSWE7IGO2aQwTeE_LdA%3D%3D"
WAFFG29="https://www.gesetze-im-internet.de/waffg_2002/__29.html"
WAFFG_LIST="https://www.gesetze-im-internet.de/waffg_2002/anlage_2.html"
TIER4="https://www.gesetze-im-internet.de/tierschg/__4.html"
TIER17="https://www.gesetze-im-internet.de/tierschg/__17.html"

CASE={
"P2013-S3-Q18":{
 "fragment":"An old Farmer who lives in your hunting area asks",
 "correct":["d"],
 "status":"source_compared_explanation_qualified",
 "source":TIER4,"other":[TIER17],
 "explanation":(
  "The 19 December 2013 practice paper keys D: refer the farmer "
  "to a VETERINARIAN. A privately owned sick dog is not huntable "
  "wild game, and the hunter's Jagdschein does not itself authorize "
  "killing another person's pet as a hunting act. Under German "
  "TierSchG §4, a vertebrate may be killed only under rules intended "
  "to avoid suffering and by a person with the necessary knowledge "
  "and ability; TierSchG §17 penalizes killing a vertebrate without "
  "a reasonable cause. A veterinarian can examine the animal and "
  "advise on necessary treatment or medically justified euthanasia. "
  "The owner's request, offensive smell or the dog's age alone "
  "must not be construed as permission for an improvised killing."
 ),
 "flag":"source-verified-veterinary-referral-not-huntable-pet"},
"P2013-S3-Q19":{
 "fragment":"Can a U.S. Forces hunter import their AR15 into Germany?",
 "correct":["b"],
 "status":"source_compared_key_conflict",
 "source":CUSTOMS_2026,
 "other":[ARMY_REG,JAG_2025,WAFFG29,WAFFG_LIST],
 "explanation":(
  "ARCHIVED 2013 TEST ANSWER: B / NO. That is what the printed "
  "GHC practice test keys; it is NOT an independent determination "
  "about today's import eligibility of every rifle marketed as "
  "AR-15. U.S. Forces personnel remain subject to German "
  "weapons law AND military registration/import requirements. "
  "USAREUR-AF's March 2026 customs instructions explicitly say "
  "firearms may not be brought into Germany before registration "
  "with BOTH U.S. Forces and German authorities. The described "
  "customs process calls for USAREUR-AF firearms registration, "
  "a German Jagdschein or WBK, and German Verbringungserlaubnis "
  "(import authorization) before using AEA Form 550-175A. "
  "Army in Europe Regulation 190-6 remains listed CURRENT "
  "by the Army publications service; a 2025 U.S. Army Europe "
  "legal bulletin likewise warns that U.S. Forces and host "
  "nation permission are BOTH required. German WaffG §29 "
  "regulates cross-border firearm transfer permissions; "
  "Anlage 2 classifies prohibited/permission-controlled "
  "firearms by technical characteristics, not merely a "
  "commercial AR-15 nickname. No actual AR-15 model, "
  "configuration, magazine or applicant was evaluated; "
  "do NOT interpret this explanation as import approval "
  "or as a universal legal ban. Consult the U.S. Forces "
  "Firearms Section and German weapons authority BEFORE "
  "shipping, ordering or travelling with a firearm."
 ),
 "warning":(
  "Dated 2013 U.S. Forces AR-15 question: its printed yes/no key "
  "does not establish current import legality for any specific "
  "weapon. Both German approval and U.S. Forces registration "
  "are required; see the original-paper vs 2026 authority comparison."
 ),
 "flag":"historical-ar15-import-blanket-answer-requires-specific-authorizations"}
}

def locate(txt):
 token="window.GHC_QUESTIONS=";a=txt.index(token)+len(token)
 arr,span=json.JSONDecoder().raw_decode(txt[a:]);return a,a+span,arr

def immutable(qs):
 return {q["id"]:(q["stem"],q["choices"],q["correct"],q["answerType"],q.get("sourceRefs"),q.get("section")) for q in qs}

def main():
 html=INDEX.read_text(encoding="utf-8")
 begin,end,qs=locate(html)
 if len(qs)!=867 or len({q["id"] for q in qs})!=867:raise AssertionError("867 original exam IDs expected")
 original=immutable(qs);found=set()
 for q in qs:
  info=CASE.get(q["id"])
  if not info:continue
  found.add(q["id"])
  if info["fragment"].lower() not in q["stem"].lower() or q["correct"]!=info["correct"]:
   raise AssertionError("Original question wording/key drifted: "+q["id"])
  q["learningWhy"]=q["explanation"]=info["explanation"]
  q["sourceReview"]={
    "status":info["status"],
    "checkedSource":info["source"],
    "additionalCheckedSources":info["other"],
    "originalPracticePaperSource":PAPER,
    "originalPaperKeyVerified":True,
    "keyPreserved":True,
    "reviewed":"2026-10-15",
    "sourceBankKeyDisputed":info["status"]=="source_compared_key_conflict"}
  flags=q.setdefault("flags",[])
  if info["flag"] not in flags:flags.append(info["flag"])
  for ref in [info["source"]]+info["other"]:
   refs=q.setdefault("officialRefs",[])
   if not any(x.get("url")==ref for x in refs):
    refs.append({"label":"Individually checked original authority / current official rules","url":ref})
  if info.get("warning"):q["preAnswerWarning"]=info["warning"]
 if found!=set(CASE):raise AssertionError("Expected exact two old-paper questions")
 if immutable(qs)!=original:raise AssertionError("Original answers/IDs/progress immutable")
 if "current.preAnswerWarning?" not in html or "Matched archival answer only" not in html:
  raise AssertionError("Pre-answer legal warnings and historical feedback must be present")
 html=html[:begin]+json.dumps(qs,ensure_ascii=False,separators=(",",":"))+html[end:]
 INDEX.write_text(html,encoding="utf-8")
 print("PASS: 2 original 2013 questions sourced (veterinary referral qualified; U.S. Forces AR-15 blanket answer flagged); 867 keys intact")

if __name__=="__main__":
 main()
