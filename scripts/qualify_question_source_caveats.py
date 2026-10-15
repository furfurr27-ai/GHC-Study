#!/usr/bin/env python3
"""Source-qualify three exact GHC study-bank Q explanations without altering exam keys.

The historical Hessen/practice bank correct choices remain untouched; the
annotations distinguish original course range instructions from a different
legacy Hessen answer and 2025 state deer-harvest planning directives.
"""
import json
from pathlib import Path

INDEX = Path("app/src/main/assets/index.html")
BANK = "GHC_QUESTIONS"
DIRECTIVE = "https://rp-kassel.hessen.de/sites/rp-kassel.hessen.de/files/2025-03/2025_03_07_erlass_abschussplanung-festsetzung_und-vollzug.pdf"
GUIDELINE = "https://rp-kassel.hessen.de/sites/rp-kassel.hessen.de/files/2025-03/2025_02_20_richtlinie_fuer_die_hege_und_bejagung_des_schalenwildes_in_hessen.pdf"

def locate(content):
    needle = "window." + BANK + "="
    pos = content.index(needle) + len(needle)
    data, consumed = json.JSONDecoder().raw_decode(content[pos:])
    return pos, pos + consumed, data

def main():
    content = INDEX.read_text(encoding="utf-8")
    start, stop, questions = locate(content)
    if len(questions) != 867:
        raise AssertionError("Question count changed: inspect rather than silently modifying")
    originals = {q["id"]: {
        "stem": q["stem"],
        "choices": q["choices"],
        "correct": q["correct"],
        "answerType": q["answerType"],
        "sourceRefs": q.get("sourceRefs"),
        "section": q.get("section")
    } for q in questions}
    patches = {
        "P2013-S4-Q05": {
            "choice": ["a"],
            "stemPart": "gender ration",
            "explanation": (
                "The original 2013 practice question keys 1:1 (male to female). "
                "Hessen's 20 February 2025 Schalenwild hunting guideline normally sets "
                "a 50:50 sex ratio for harvest planning, but recognizes management "
                "exceptions: for Rehwild a Hegegemeinschaft proposal can temporarily "
                "shift the target to as much as 60:40 female-to-male during necessary "
                "population reduction. Learn 1:1 as this legacy key, not a fixed "
                "universal or unchangeable legal quota for all hoofed game."
            ),
            "source": GUIDELINE,
            "tag": "legacy-practice-plan-ratio-qualified-2025",
        },
        "P2013-S4-Q08": {
            "choice": ["a"],
            "stemPart": "harvest plan",
            "explanation": (
                "The original 2013 practice key identifies Schwarzwild (wild boar). "
                "The Hessian hunting authority's 7 March 2025 Abschussplanung decree "
                "restates the BJagdG section 21(2) rule: Schalenwild other than "
                "Schwarzwild requires an Abschussplan. This exception to the "
                "harvest-plan requirement is not an exemption from hunting seasons, "
                "legal restrictions, game reporting or firearms safety."
            ),
            "source": DIRECTIVE,
            "tag": "hessen-boar-plan-exception-2025-confirmed",
        },
        "H2023-D04-Q137": {
            "choice": ["a"],
            "stemPart": "misfire",
            "explanation": (
                "The Hessen question bank keys option (a): keep the muzzle "
                "downrange and wait about 10 seconds before opening the action "
                "(hangfire risk). IMPORTANT GHC RANGE DIFFERENCE: the actual "
                "February 2026 GHC Range Safety slide says to keep the firearm "
                "pointed downrange for 10 seconds and then carefully pass control "
                "to the instructor; it does NOT tell students to independently "
                "open the action. Preserve the Hessen bank key for exam study, "
                "but on the supervised class range follow the instructor/RSO's "
                "specific procedure rather than generalizing this answer."
            ),
            "source": "Range - Saftey (20260211).pdf, classroom Misfire procedures passage",
            "tag": "ghc-2026-range-sequence-differs-from-hessen-choice",
        },
    }
    seen = set()
    for q in questions:
        patch = patches.get(q["id"])
        if not patch:
            continue
        seen.add(q["id"])
        if q["correct"] != patch["choice"] or patch["stemPart"] not in q["stem"].lower():
            raise AssertionError("Question or key changed since source review: " + q["id"])
        # Only explanatory fields and transparent provenance flags are modified.
        q["explanation"] = patch["explanation"]
        q["learningWhy"] = patch["explanation"]
        q["sourceReview"] = {
            "status": "qualified_after_source_comparison",
            "checkedSource": patch["source"],
            "reviewed": "2026-10-15",
            "keyPreserved": True
        }
        flags = q.setdefault("flags", [])
        if patch["tag"] not in flags:
            flags.append(patch["tag"])
        if patch["source"].startswith("https:"):
            refs = q.setdefault("officialRefs", [])
            if not any(r.get("url") == patch["source"] for r in refs):
                refs.append({"label": "Hessen official 2025 directive — scoped source review", "url": patch["source"]})
    if seen != set(patches):
        raise AssertionError("Target questions absent: " + repr(set(patches) - seen))
    now = {q["id"]: {
        "stem": q["stem"], "choices": q["choices"], "correct": q["correct"],
        "answerType": q["answerType"], "sourceRefs": q.get("sourceRefs"),
        "section": q.get("section")
    } for q in questions}
    if originals != now or len(now) != 867:
        raise AssertionError("Question ID, wording, answer or section modified unexpectedly")
    updated = json.dumps(questions, ensure_ascii=False, separators=(",", ":"))
    content = content[:start] + updated + content[stop:]
    INDEX.write_text(content, encoding="utf-8")
    print("PASS: 3 individually source-qualified question explanations; 867 keys/choices/IDs unchanged")

if __name__ == "__main__":
    main()
