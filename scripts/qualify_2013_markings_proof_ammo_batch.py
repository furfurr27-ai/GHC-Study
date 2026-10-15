#!/usr/bin/env python3
"""Four narrowly source-audited 2013 ammo/marking/proof questions.

Source-first build overlay. Never rewrite printed answer choices, IDs, or key.
An imported firearm's foreign proof marks and proof-law exemptions must not
be mistaken for a blanket statement that a US-manufactured gun is illegal.
"""
import json
from pathlib import Path

INDEX=Path("app/src/main/assets/index.html")
ORIGINAL="https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view"
CLASS="Weapons - Ammo (20260214).pdf; Firearms Markings, Centerfire vs Rimfire, Rimmed vs Rimless, Shotgun Gauge sections"
MARKS="https://www.gesetze-im-internet.de/waffg_2002/__24.html"
PROOF3="https://www.gesetze-im-internet.de/beschg/__3.html"
PROOF4="https://www.gesetze-im-internet.de/beschg/__4.html"
PROOF6="https://www.gesetze-im-internet.de/beschg/__6.html"

CASES={
"P2013-S3-Q07":{
 "fragment":"Which one of the following cartridges is a RIMFIRE?",
 "answer":["b"], "status":"source_compared_explanation_qualified",
 "source":CLASS,
 "other":[],
 "explanation":(
  "The original 2013 test keys B: .22 LR uses rimfire ignition. "
  "The 2026 GHC Weapons - Ammo lesson explains that rimfire priming "
  "compound is around the inside of the case rim, where the firing pin "
  "strikes. In contrast, .222 Remington and 7x57R use CENTERFIRE "
  "primers. The R in 7x57R identifies a RIMMED cartridge case for "
  "extraction; a rimmed case is not necessarily rimfire. Rim shape "
  "and the position of the primer describe different features."
 ),
 "flag":"ghc-2026-rimfire-rimmed-vs-centerfire-confirmed"},
"P2013-S3-Q14":{
 "fragment":"What are the legal markings of a rifle?",
 "answer":["b"], "status":"source_compared_explanation_qualified",
 "source":MARKS,
 "other":[PROOF6],
 "explanation":(
  "The 19 December 2013 paper keys B: serial number, proof-house "
  "information, manufacturer and TYPE OF AMMUNITION. This matches "
  "the core markings taught in the 2026 GHC Weapons - Ammo lesson. "
  "But two distinct legal schemes apply: WaffG §24(1) covers the "
  "manufacturer, country-of-manufacture code, exact ammunition or "
  "barrel caliber designation, serial number and, in certain "
  "third-country imports, import country/year. BeschG §6 separately "
  "describes official proof marks after successful testing. Specific "
  "exceptions and transitional conditions exist; the 2013 four-part "
  "answer is useful for that paper but NOT an exhaustive current "
  "list of mandatory markings for every weapon or component."
 ),
 "classroom":CLASS,"flag":"waffg24-proof-mark-distinction-source-checked"},
"P2013-S3-Q15":{
 "fragment":"US made guns must be inspected by a German Beschussamt",
 "answer":["a"], "status":"source_compared_key_conflict",
 "source":PROOF3,
 "other":[PROOF4,PROOF6],
 "explanation":(
  "HISTORICAL GENERALIZATION: the December 2013 GHC paper keys "
  "TRUE that every U.S.-made gun imported into Germany must be "
  "inspected by a GERMAN Beschussamt. Under BeschG §3, civilian "
  "firearms first introduced to the regulated German market normally "
  "require official proof testing. But BeschG §4(1) specifically "
  "exempts certain categories and temporary purposes and §4(2) "
  "recognizes proof marks from states covered by an agreement "
  "on MUTUAL RECOGNITION of official proof marks. For a U.S.-"
  "manufactured firearm, the country of manufacture alone does "
  "not decide whether prior recognized proof, proof exemption "
  "or a fresh proof test is required. U.S. factory safety tests "
  "are not automatically a recognized foreign government proof "
  "mark. The old TRUE answer is not a universal current rule: "
  "check the exact firearm, provenance and competent proof authority."
 ),
 "warning":(
  "The 2013 blanket proof-house TRUE/FALSE item is overbroad. "
  "Current BeschG §§3–4 include recognized foreign-proof marks "
  "and specific exemptions. The original paper key is preserved "
  "but is not complete legal guidance."
 ),
 "flag":"dated-2013-universal-german-proof-house-assertion"},
"P2013-S3-Q16":{
 "fragment":"Which shotgun barrel has the bigger diameter?",
 "answer":["a"],"status":"source_compared_explanation_qualified",
 "source":CLASS,
 "other":[],
 "explanation":(
  "The original 2013 answer A is correct: a 12-gauge smoothbore "
  "has a larger nominal bore than a 20-gauge. The 2026 GHC Weapons "
  "- Ammo lesson teaches the traditional GAUGE number as the "
  "number of lead spheres of that bore diameter making one pound; "
  "fewer spheres means each sphere is larger, so 12 gauge is "
  "larger than 20 gauge. Shotgun gauge is not the same measurement "
  "as the chamber length: European markings such as 12/70 and "
  "20/70 separately state the nominal chamber length in mm. "
  "The .410 designation is an exception expressed as a bore "
  "measurement in inches rather than a traditional gauge number."
 ),
 "flag":"ghc-2026-shotgun-gauge-vs-chamber-dimensions"}
}

def extract(txt):
 marker="window.GHC_QUESTIONS="; start=txt.index(marker)+len(marker)
 bank,size=json.JSONDecoder().raw_decode(txt[start:]);return start,start+size,bank

def keyfields(bank):
 return {q["id"]:(q["stem"],q["choices"],q["correct"],q["answerType"],q.get("sourceRefs"),q.get("section")) for q in bank}

def main():
 html=INDEX.read_text(encoding="utf-8")
 first,last,bank=extract(html)
 if len(bank)!=867 or len({q["id"] for q in bank})!=867:raise AssertionError("Source question count drifted")
 orig=keyfields(bank)
 found=set()
 for q in bank:
  case=CASES.get(q["id"])
  if not case:continue
  found.add(q["id"])
  if case["fragment"].lower() not in q["stem"].lower() or q["correct"]!=case["answer"]:
   raise AssertionError("Paper wording / answer changed: "+q["id"])
  q["learningWhy"]=q["explanation"]=case["explanation"]
  q["sourceReview"]={
   "status":case["status"],
   "checkedSource":case["source"],
   "additionalCheckedSources":case["other"],
   "classroomSource":CLASS,
   "originalPracticePaperSource":ORIGINAL,
   "originalPaperKeyVerified":True,
   "reviewed":"2026-10-15",
   "keyPreserved":True,
   "sourceBankKeyDisputed":case["status"]=="source_compared_key_conflict"}
  flag=q.setdefault("flags",[])
  if case["flag"] not in flag:flag.append(case["flag"])
  refs=q.setdefault("officialRefs",[])
  for url in [case["source"]]+case["other"]:
   if not url.startswith("https://"):continue
   if not any(r.get("url")==url for r in refs):
    refs.append({"label":"Current German official law — scoped individual source comparison","url":url})
  if case.get("warning"):q["preAnswerWarning"]=case["warning"]
 if found!=set(CASES):raise AssertionError("Missing audited entries: "+repr(set(CASES)-found))
 if keyfields(bank)!=orig:raise AssertionError("Original 867 exam records were rewritten")
 html=html[:first]+json.dumps(bank,ensure_ascii=False,separators=(",",":"))+html[last:]
 if "current.preAnswerWarning?" not in html or "Matched archival answer only" not in html:
  raise AssertionError("Inherited safety/source law warning UX missing")
 INDEX.write_text(html,encoding="utf-8")
 print("PASS: four exact 2013 paper/classroom/current-law audits; 3 qualified, 1 proof-law conflict; 867 answer keys untouched")

if __name__=="__main__":
 main()
