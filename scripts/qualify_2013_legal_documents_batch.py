#!/usr/bin/env python3
"""Four individually audited 2013 GHC legal/documentation questions.

The original 2013 printed answer keys, IDs, choices, and storage keys are
immutable. The active federal law is a separate, explicitly dated annotation.
"""
import json
from pathlib import Path

INDEX = Path("app/src/main/assets/index.html")
PAPER = "Practice Hunting Test  2013-12-19.pdf, Part III original printed Question and Answer Key"
PAPER_URL = "https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view"
W10 = "https://www.gesetze-im-internet.de/waffg_2002/__10.html"
W12 = "https://www.gesetze-im-internet.de/waffg_2002/__12.html"
W13 = "https://www.gesetze-im-internet.de/waffg_2002/__13.html"
W38 = "https://www.gesetze-im-internet.de/waffg_2002/__38.html"
STGB32 = "https://www.gesetze-im-internet.de/stgb/__32.html"

CASES = {
    "P2013-S3-Q05": {
        "stem": "Which documents must a hunter carry with them",
        "answers": ["a", "c", "d"],
        "status": "source_compared_explanation_qualified",
        "primary": W38,
        "others": [W12, W13],
        "detail": (
            "Original 2013 Section 3 Question 5 keys A/C/D: Jagdschein, "
            "personal ID/passport, and loan-document information. Current "
            "WaffG §38(1) requires identification and, for a temporary "
            "loan under §12(1)(1), evidence naming the transferring person, "
            "the person temporarily entitled to possess the gun, and the "
            "transfer date. A lawfully hunting person also carries their "
            "Jagdschein under §38(1)(2). WaffG §13(4) treats the valid "
            "hunting license as equivalent to a WBK for temporary acquisition "
            "of qualifying hunting long guns under §12(1)(1). The loan must "
            "still be lawful, temporary and purpose-limited; this does not "
            "authorize anyone to borrow arbitrary weapons or evade local "
            "hunting-range requirements."
        ),
        "flag": "2013-borrowed-rifle-documents-confirmed-2026-waffg",
    },
    "P2013-S3-Q09": {
        "stem": "Which documents do you need to purchase a .308W rifle",
        "answers": ["b"],
        "status": "source_compared_key_conflict",
        "primary": W13,
        "others": [W10],
        "detail": (
            "DATED PAPER QUESTION: the original December 2013 Section 3 "
            "Question 9 keys B (WBK + Jagdschein + ID). Under current "
            "WaffG §13(3), a holder of a VALID ANNUAL Jagdschein may acquire "
            "a qualifying lawful hunting LONG GUN without a separate prior "
            "acquisition permit or pre-existing WBK for that purchase, but "
            "must apply to the competent authority for its WBK entry/issue "
            "within TWO WEEKS after acquiring it. This exception does not "
            "apply to everyone holding any type of Jagdschein, nor to all "
            "firearms, nor to people without German acquisition rights. "
            "Bring proof of identity and the hunting license and comply "
            "with actual retailer, registration and U.S. Forces-specific "
            "procedures. B is this 2013 PAPER key, NOT a universal current "
            "statement that a WBK must already exist before all rifle buys."
        ),
        "warning": (
            "Dated 2013 rifle-purchase paperwork: current WaffG §13(3) "
            "has a specific annual-Jagdschein exception and a later "
            "registration deadline. The historical paper key is not "
            "a complete description of today's requirements."
        ),
        "flag": "legacy-2013-rifle-purchase-wbk-prepermit-mismatch",
    },
    "P2013-S3-Q10": {
        "stem": "Which documents do you need to purchase a 9mm Luger pistol",
        "answers": ["c"],
        "status": "source_compared_explanation_qualified",
        "primary": W10,
        "others": [W13],
        "detail": (
            "The 2013 Section 3 Question 10 keys C: identity, hunting "
            "license, and a WBK with a specific acquisition authorization "
            "for the 9 mm Luger handgun. Current WaffG §10(1) requires "
            "firearm-acquisition authority to be recorded in a WBK or by "
            "entry in an existing WBK, and identifies gun type/number/"
            "caliber. Unlike qualifying hunting long guns under §13(3), "
            "hunters do not have the same general permit-free handgun "
            "acquisition exception. WaffG §13(2) recognizes a hunting "
            "need for up to two qualifying handguns but does not dispense "
            "with pre-acquisition permission. Verify authorization with "
            "the competent German weapons authority for the specific "
            "handgun and transfer; a Jagdschein alone is not a permit "
            "to buy any pistol."
        ),
        "flag": "2013-handgun-prior-acquisition-authorization-qualified-2026",
    },
    "P2013-S3-Q13": {
        "stem": "Before using your pistol in a self defense situation",
        "answers": ["c"],
        "status": "source_compared_key_conflict",
        "primary": STGB32,
        "others": [],
        "detail": (
            "IMPORTANT HISTORICAL PAPER ERROR / LEGAL SAFETY ISSUE: "
            "the December 2013 Section 3 Question 13 keys C (both a "
            "verbal warning AND a warning shot before defensive pistol "
            "use). Current German StGB §32 defines Notwehr by what "
            "defense is NECESSARY to stop a present unlawful attack; "
            "it imposes NO universal requirement to fire a warning "
            "shot and no unconditional fixed verbal-warning-then-shot "
            "sequence. Firing a warning shot itself can endanger "
            "bystanders and creates separate legal and safety risks. "
            "Whether any particular defensive act is justified "
            "depends on actual necessity and circumstances. The "
            "original C letter is archived source material and "
            "must NEVER be treated as tactical or legal instructions "
            "to fire a warning shot. Seek emergency help and use "
            "lawful nonviolent options where safe."
        ),
        "warning": (
            "Safety-critical outdated 2013 self-defense key: current "
            "StGB §32 does NOT require a warning shot before every "
            "defensive act. Do not treat the archived answer as an "
            "instruction to fire a gun; see the legal distinction "
            "in the explanation."
        ),
        "flag": "unsafe-legacy-2013-self-defense-warning-shot-mandate",
    },
}


def parsed(text):
    token = "window.GHC_QUESTIONS="
    pos = text.index(token) + len(token)
    questions, size = json.JSONDecoder().raw_decode(text[pos:])
    return pos, pos + size, questions


def immutable(questions):
    return {
        q["id"]: (q["stem"], q["choices"], q["correct"], q["answerType"],
                  q.get("sourceRefs"), q.get("section"))
        for q in questions
    }


def main():
    html = INDEX.read_text(encoding="utf-8")
    first, last, bank = parsed(html)
    if len(bank) != 867 or len({x["id"] for x in bank}) != 867:
        raise AssertionError("The original 867 exam question IDs changed")
    original = immutable(bank)
    seen = set()
    for q in bank:
        info = CASES.get(q["id"])
        if info is None:
            continue
        seen.add(q["id"])
        if q["correct"] != info["answers"] or info["stem"].lower() not in q["stem"].lower():
            raise AssertionError("Original printed question differs; inspect paper: " + q["id"])
        q["explanation"] = info["detail"]
        q["learningWhy"] = info["detail"]
        q["sourceReview"] = {
            "status": info["status"],
            "checkedSource": info["primary"],
            "additionalCheckedSources": info["others"],
            "originalPracticePaperSource": PAPER_URL,
            "originalPracticePaperLocator": PAPER + " (question " + q["id"].split("-Q")[-1] + ")",
            "originalPaperKeyVerified": True,
            "keyPreserved": True,
            "sourceBankKeyDisputed": info["status"] == "source_compared_key_conflict",
            "reviewed": "2026-10-15",
        }
        for ref in [info["primary"]] + info["others"]:
            q.setdefault("officialRefs", [])
            if not any(z.get("url") == ref for z in q["officialRefs"]):
                q["officialRefs"].append({"label": "German federal law (current official text)", "url": ref})
        flags = q.setdefault("flags", [])
        if info["flag"] not in flags:
            flags.append(info["flag"])
        if "warning" in info:
            q["preAnswerWarning"] = info["warning"]
    if seen != set(CASES):
        raise AssertionError("Missing targeted original paper questions: " + str(set(CASES) - seen))
    if immutable(bank) != original:
        raise AssertionError("Question answer keys, options, IDs, sections or source IDs drifted")
    html = html[:first] + json.dumps(bank, ensure_ascii=False, separators=(",", ":")) + html[last:]
    if "current.preAnswerWarning?" not in html:
        raise AssertionError("The UI must render warnings before answers")
    INDEX.write_text(html, encoding="utf-8")
    print("PASS: 4 original-paper/current-law comparisons; 2 qualified, 2 flagged historical-law errors, all 867 keys unchanged")


if __name__ == "__main__":
    main()
