#!/usr/bin/env python3
"""Audit five exact 2013 weapons-law questions with primary dated exam + current law.

This is a BUILD overlay, not a source-bank rewrite. Preserve all original
keys/choices/IDs. Visibly flag obsolete or over-narrow law wording pre-answer.
"""
import json
from pathlib import Path

INDEX = Path("app/src/main/assets/index.html")
PAPER = "Practice Hunting Test  2013-12-19.pdf, PART III and original printed Answer Key, Google Drive 1f_bWpni_W7xpReNHPHCWittNiQSBFOwX"
CLASS_AMMO = "Weapons - Ammo (20260214).pdf, Ammunition and SAFETY sections"
W12 = "https://www.gesetze-im-internet.de/waffg_2002/__12.html"
A13 = "https://www.gesetze-im-internet.de/awaffv/__13.html"
B19 = "https://www.gesetze-im-internet.de/bjagdg/__19.html"
SV = "https://www.svlfg.de/sichere-jagd"

REVIEW = {
    "P2013-S3-Q01": {
        "stem": "How do you have to store guns?",
        "correct": ["c"],
        "status": "source_compared_explanation_qualified",
        "source": A13,
        "explanation": (
            "2013 practice key C: store firearms in a secured Waffenschrank, "
            "with access only for authorized people. This is a general principle, "
            "not a complete present-day safe specification. Current AWaffV § 13 "
            "requires permit-controlled firearms to be UNLOADED and normally "
            "secured in a certified DIN/EN 1143-1 container meeting the relevant "
            "resistance grade (often grade 0 or I), with special rules for "
            "weapon types, number, weight, location, approved alternatives and "
            "applicable transitional cases. A hiding place or ordinary unlocked "
            "room is not an adequate substitute. Confirm the actual safe with "
            "the local weapons authority; the 2013 wording alone is insufficient."
        ),
        "flag": "official-2026-storage-requirements-qualify-old-bank",
    },
    "P2013-S3-Q03": {
        "stem": "To legally transport their rifle in their car, a hunter must",
        "correct": ["e"],
        "status": "source_compared_key_conflict",
        "source": W12,
        "explanation": (
            "DATED-EXAM VS CURRENT-LAW SCOPE: the 19 December 2013 paper keys E "
            "(all of the above): unloaded, locked case, trunk and boxed "
            "ammunition in the case. Those are the paper's expected answers, "
            "not a universal list of what § 12(3)(2) WaffG independently "
            "REQUIRES in every transport situation. For the statutory "
            "transport exception the firearm must be not ready to fire "
            "(nicht schussbereit) AND not readily accessible (nicht "
            "zugriffsbereit) while moving it for an authorized purpose. "
            "A locked container is a strong way to secure it; a trunk is "
            "not named as a universal statutory requirement by §12(3)(2). "
            "SVLFG separately instructs unloading in vehicles and safe "
            "separation of gun and ammunition, with different rules when "
            "moving within a hunting district. Do not rely on the 2013 "
            "all-of-the-above checklist to describe every current legal case."
        ),
        "warning": (
            "Historical legal-language notice: this 2013 transport question "
            "uses a stricter, dated checklist. The archived key is preserved; "
            "its 'must' wording is not a complete statement of today's WaffG."
        ),
        "flag": "dated-2013-transport-checklist-not-universal-statutory-rule",
    },
    "P2013-S3-Q04": {
        "stem": "State the minimum caliber and minimum energy",
        "correct": ["a"],
        "status": "source_compared_explanation_qualified",
        "source": B19,
        "explanation": (
            "Correct for the general federal rule on Schalenwild OTHER than "
            "Rehwild: BJagdG § 19(1)(2)(b) prohibits rifle cartridges below "
            "6.5 mm, and cartridges of 6.5 mm or larger normally need at "
            "least 2,000 J impact energy at 100 m (E100). The 2026 GHC "
            "Weapons/Ammo slide confirms 2,000 J for non-roe cloven-hoofed "
            "game and 1,000 J E100 for roe deer. Do not apply the 6.5 mm "
            "threshold to the distinct roe-deer rule in §19(1)(2)(a); "
            "§19(3) also provides for officially examined use-specific "
            "ammunition exceptions. These are legal thresholds, not a "
            "recommendation for shot placement or ammunition choice."
        ),
        "classroom": CLASS_AMMO,
        "flag": "ghc-and-current-bjagdg-confirm-e100-and-roe-distinction",
    },
    "P2013-S3-Q08": {
        "stem": "To transport your rifle in a car home from the shooting range",
        "correct": ["c"],
        "status": "source_compared_explanation_qualified",
        "source": W12,
        "explanation": (
            "The original 2013 answer C emphasizes the essential statutory "
            "transport concept: the rifle must be unloaded (nicht schussbereit) "
            "and not readily accessible (nicht zugriffsbereit) when transported "
            "home from the shooting range under WaffG §12(3)(2). An open bolt "
            "alone does not address accessibility, and merely taking "
            "cartridges out of the chamber while keeping an accessible gun "
            "does not satisfy this ordinary transport exception. "
            "SVLFG additionally requires unloading before entering vehicles "
            "and throughout travel. Check that the gun is secured and "
            "follow all applicable storage, carrying and transport rules."
        ),
        "flag": "current-waffg-transport-no-ready-fire-or-access",
    },
    "P2013-S3-Q11": {
        "stem": "Is it legal to hunt with a semiautomatic rifle in Germany?",
        "correct": ["c"],
        "status": "source_compared_key_conflict",
        "source": B19,
        "explanation": (
            "DATED LAW / LEGACY EXAM KEY: the original 19 December 2013 paper "
            "keys C, limiting a semiautomatic hunting rifle's magazine to "
            "two rounds. Today's federal BJagdG §19(1)(2)(c) instead "
            "prohibits firing at game with a semiautomatic LONG GUN loaded "
            "with MORE THAN THREE cartridges in TOTAL (including the "
            "chamber), as well as using automatic firearms. A two-round "
            "magazine with a chamber round remains compatible, but the old "
            "wording is NOT the current universal law: legal compliance "
            "depends on how many cartridges are actually loaded in total, "
            "not solely on a magazine's nominal two-round capacity. "
            "Other federal/state weapons and hunting restrictions still apply."
        ),
        "warning": (
            "Law changed since this 2013 paper. The keyed two-round-magazine "
            "wording is archival; current BJagdG §19 uses a three-cartridge "
            "TOTAL-LOADED limit for semiautomatic long guns when hunting."
        ),
        "flag": "dated-2013-semi-auto-magazine-rule-replaced-by-3-total-loaded",
    },
}

def extract(html):
    token="window.GHC_QUESTIONS="
    a=html.index(token)+len(token)
    questions,n=json.JSONDecoder().raw_decode(html[a:])
    return a,a+n,questions

def immutable(questions):
    return {q["id"]: (q["stem"],q["choices"],q["correct"],q["answerType"],
                      q.get("sourceRefs"),q.get("section")) for q in questions}

def main():
    html=INDEX.read_text(encoding="utf-8")
    start,end,questions=extract(html)
    assert len(questions)==867 and len({q["id"] for q in questions})==867, "Bank changed"
    before=immutable(questions)
    done=set()
    for q in questions:
        cfg=REVIEW.get(q["id"])
        if cfg is None: continue
        if q["correct"]!=cfg["correct"] or cfg["stem"].lower() not in q["stem"].lower():
            raise AssertionError("Original question or paper key differs: "+q["id"])
        done.add(q["id"])
        q["explanation"]=cfg["explanation"]
        q["learningWhy"]=cfg["explanation"]
        q["sourceReview"]={
            "status":cfg["status"],
            "checkedSource":cfg["source"],
            "classroomSource":cfg.get("classroom"),
            "originalPracticePaperSource":PAPER,
            "originalPaperKeyVerified":True,
            "keyPreserved":True,
            "sourceBankKeyDisputed":cfg["status"]=="source_compared_key_conflict",
            "reviewed":"2026-10-15"
        }
        q.setdefault("flags",[])
        if cfg["flag"] not in q["flags"]:q["flags"].append(cfg["flag"])
        q.setdefault("officialRefs",[])
        if not any(x.get("url")==cfg["source"] for x in q["officialRefs"]):
            q["officialRefs"].append({"label":"Current German federal law — precise section","url":cfg["source"]})
        if "warning" in cfg:q["preAnswerWarning"]=cfg["warning"]
    if done!=set(REVIEW):raise AssertionError("Target question absent: "+repr(set(REVIEW)-done))
    if immutable(questions)!=before:raise AssertionError("Original 867 quiz IDs/keys/choices/source or sections changed")
    html=html[:start]+json.dumps(questions,ensure_ascii=False,separators=(",",":"))+html[end:]
    INDEX.write_text(html,encoding="utf-8")
    print("PASS: 5 exact current-law source reviews (3 qualified, 2 dated/overbroad legacy keys) with 867 historical answers preserved")

if __name__=="__main__":
    main()
