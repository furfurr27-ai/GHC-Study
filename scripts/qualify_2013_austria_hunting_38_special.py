#!/usr/bin/env python3
"""Source-qualify exact 2013 Austria visiting-hunter and .38 Special cartridge Qs.

Preserve old printed answers, original test questions, choices and progress IDs.
Modern EU firearm TRAVEL papers do not independently authorize Austrian HUNTING.
"""
import json
from pathlib import Path

HTML=Path("app/src/main/assets/index.html")
PAPER="https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view"
RUGER="https://ruger-docs.s3.amazonaws.com/_manuals/securitySix.pdf"
AT_JAGDKARTE="https://www.oesterreich.gv.at/de/lexicon/J/Seite.991741"
AT_TRAVEL="https://www.oesterreich.gv.at/en/themen/gesetze_und_recht/waffenrecht/1/Seite.2450210"
AT_CUSTOMS="https://www.bmf.gv.at/en/topics/customs/travellers/prohibitions-and-restrictions-on-imports/carrying-weapons.html"
AT_NO="https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=LrNO&Anlage=&Artikel=&Gesetzesnummer=20000559&Paragraf=59"
AT_OO="https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=LrOO&Anlage=&Artikel=&Gesetzesnummer=20001285&Paragraf=30"

CASES={
"P2013-S3-Q06":{
  "stem":"Can .38 Special cartridges be shot from a .357 Magnum revolver?",
  "correct":["a"],
  "status":"source_compared_explanation_qualified",
  "source":RUGER,
  "additional":[],
  "explanation":(
    "The 19 December 2013 GHC paper keys A (YES). Ruger's original "
    "Security-Six/Speed-Six/Police Service-Six double-action revolver "
    "instruction manual, AMMUNITION section (printed p.4; PDF page "
    "index 3, visually inspected), expressly confirms that a revolver "
    "marked .357 Magnum can also chamber .38 Special, but a revolver "
    "marked .38 Special is restricted to .38 Special ammunition. "
    "This is not a universal interchangeability rule for similar-"
    "looking cartridges or unverified revolver models. Verify "
    "the exact barrel/chamber designation, the model's own manual, "
    "and safe factory-specification ammunition before use; never "
    "assume the reverse (.357 Magnum in a .38 Special revolver) is safe."
  ),
  "flag":"manufacturer-manual-357-magnum-accepts-38-special-not-reverse"},
"P2013-S3-Q20":{
  "stem":"What documents do you need to hunt in Austria?",
  "correct":["b"],
  "status":"source_compared_key_conflict",
  "source":AT_JAGDKARTE,
  "additional":[AT_TRAVEL,AT_CUSTOMS,AT_OO,AT_NO],
  "explanation":(
    "The ORIGINAL 19 December 2013 GHC paper keys B: Jagdschein, "
    "WBK, European Firearms Pass (Europäischer Feuerwaffenpass), "
    "passport, and Austrian Jagdschein. That historical set is "
    "NOT a universal or complete present-day checklist. Austrian "
    "hunting authority is governed by the destination Bundesland: "
    "a valid Austrian Jagdkarte OR qualifying Jagdgastkarte "
    "(provincial guest-hunting card), applicable hunting permission/"
    "invitation and often hunting-liability insurance are relevant. "
    "The Austrian government's January 2026 Jagdkarte explanation "
    "confirms both annual and guest cards, with province-specific "
    "issuers and conditions. For a person residing in an EU "
    "member state who travels WITH a qualifying category-C hunting "
    "firearm, Austria's April 2026 firearm travel instructions "
    "generally require a European Firearms Pass listing the firearm "
    "and evidence of the specific hunting purpose; qualifying "
    "hunters may use the exemption from separate Austrian travel "
    "approval, but not for every firearm category. The European "
    "Firearms Pass is NOT itself hunting permission or a general "
    "carrying/ownership authorization. A WBK, valid German "
    "Jagdschein, passport, guest Jagdkarte, liability coverage "
    "and actual entry permits must be assessed for the hunter's "
    "residency, nationality, gun category, destination province "
    "and purpose. Austrian province examples: Lower Austria's "
    "NÖ Jagdgesetz §59 governs Jagdgastkarten; Upper Austria's "
    "Oö Jagdgesetz 2024 §30 requires a valid Jagdkarte or "
    "Jagdgastkarte to exercise hunting. A German Jagdschein and "
    "European firearms pass by themselves never make a visitor "
    "universally eligible to hunt across all Austrian provinces. "
    "Check the intended Bundesland's Jagdbehörde and Austrian "
    "weapons authority before travel."
  ),
  "warning":(
    "The 2013 Austria travel key is an ARCHIVED checklist, not "
    "a current universal requirement. Provincial Jagdkarte or "
    "Jagdgastkarte, a specific hunting invitation, and firearm-"
    "travel permissions vary by destination and weapon category."
  ),
  "flag":"historical-2013-austria-checklist-varies-province-and-firearm"}
}

def parsed(html):
  marker="window.GHC_QUESTIONS="
  at=html.index(marker)+len(marker)
  arr, used=json.JSONDecoder().raw_decode(html[at:])
  return at,at+used,arr

def stable(bank):
  return {q["id"]:(q["stem"],q["choices"],q["correct"],q["answerType"],q.get("sourceRefs"),q.get("section")) for q in bank}

def main():
  html=HTML.read_text("utf-8")
  a,z,bank=parsed(html)
  if len(bank)!=867 or len({q["id"] for q in bank})!=867:
    raise AssertionError("867 source exam entries missing or duplicated")
  orig=stable(bank)
  done=set()
  for q in bank:
    x=CASES.get(q["id"])
    if x is None:continue
    done.add(q["id"])
    if q["correct"]!=x["correct"] or q["stem"]!=x["stem"]:
      raise AssertionError("Question or original 2013 answer drifted: "+q["id"])
    q["learningWhy"]=q["explanation"]=x["explanation"]
    q["sourceReview"]={
      "status":x["status"],"checkedSource":x["source"],
      "additionalCheckedSources":x["additional"],
      "originalPracticePaperSource":PAPER,
      "originalPaperKeyVerified":True,
      "sourceBankKeyDisputed":x["status"]=="source_compared_key_conflict",
      "keyPreserved":True,
      "reviewed":"2026-10-15",
      "sourceNotes":("Manufacturer printed ammunition instruction page 4 screenshot inspected"
                     if q["id"]=="P2013-S3-Q06" else
                     "Austrian official federal Jan/Apr 2026 pages; provincial statutes by individual Bundesland; old paper answer not legal permission")
    }
    flags=q.setdefault("flags",[])
    if x["flag"] not in flags:flags.append(x["flag"])
    refs=q.setdefault("officialRefs",[])
    for url in [x["source"]]+x["additional"]:
      if not any(z.get("url")==url for z in refs):
        refs.append({"label":"Checked manufacturer primary manual / current Austrian official rules","url":url})
    if "warning" in x:q["preAnswerWarning"]=x["warning"]
  if done!=set(CASES):raise AssertionError("One of the original paper questions is unavailable")
  if stable(bank)!=orig:raise AssertionError("Historical question IDs, answers, choices or progress source fields mutated")
  if "current.preAnswerWarning?" not in html or "Matched archival answer only" not in html:
    raise AssertionError("Guarded source-qualified quiz warning UI missing")
  html=html[:a]+json.dumps(bank,ensure_ascii=False,separators=(",",":"))+html[z:]
  HTML.write_text(html,"utf-8")
  print("PASS: source-compared original .38/.357 and Austrian-hunting travel 2013 Qs; 867 historical answer keys retained")

if __name__=="__main__":
 main()
