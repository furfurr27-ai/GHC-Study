#!/usr/bin/env python3
"""Source-review six firearm-safety questions, retaining every legacy exam key.

One archived multi-answer key is materially incomplete (car entry also requires
unloading); mark disputed and show a warning BEFORE the answer is checked.
"""
import json
from pathlib import Path

INDEX = Path("app/src/main/assets/index.html")
GHC_AMMO = "Weapons - Ammo (20260214).pdf; GHC SAFETY / high-seat passage"
GHC_RANGE = "Range - Saftey (20260211).pdf; GHC FIREARMS SAFETY / Ranges, Muzzle Awareness passage"
GHC_TECH = "Hunting Techniques (20260216).pdf; Drive Hunts / Jagdleiter Brief"
OFFICIAL = "https://www.svlfg.de/sichere-jagd"

# Entries are individually verified against directly retrieved originals and
# the SVLFG official German hunting accident-prevention explanation of VSG 4.4.
REVIEW = {
  "P2013-S3-Q02": {
    "expected": ["b", "c"],
    "stem": "When must a hunter unload their weapon",
    "status": "source_compared_key_conflict",
    "source": OFFICIAL,
    "classroom": GHC_AMMO,
    "originalPracticePaperSource": "https://drive.google.com/file/d/1f_bWpni_W7xpReNHPHCWittNiQSBFOwX/view",
    "originalPaperKeyVerified": True,
    "explanation": (
      "IMPORTANT LEGACY KEY CONFLICT: the original 2013 practice-test key only "
      "marks B (climbing the high seat) and C (crossing obstacles) in the " 
      "actual 19 December 2013 paper Answer Key (Section 3, Question 2). D (getting "
      "into a car) ALSO requires unloading under current German hunting "
      "accident-prevention instructions. SVLFG's VSG 4.4 explanation explicitly "
      "requires unloading before entering/exiting vehicles, during travel, "
      "when ascending/descending high seats, and while crossing obstacles. "
      "The February 2026 GHC Weapons/Ammo class also forbids ascending or "
      "descending with a loaded gun. This item's original B/C answer remains "
      "unchanged for archival fidelity, but the key is incomplete for safe "
      "real-world practice: never treat the omitted car option as safe."
    ),
    "flag": "disputed-2013-key-omits-mandatory-vehicle-unloading",
    "warning": (
      "Legacy key under factual dispute: a safety-critical option is omitted "
      "from the archived answer set. Historical scoring is not current range "
      "or hunting-safety guidance; review the explanation and SVLFG rules."
    ),
  },
  "H2023-D08-Q052": {
    "expected": ["a"],
    "stem": "climb into a raised hide",
    "status": "source_compared_explanation_qualified",
    "source": OFFICIAL,
    "classroom": GHC_AMMO,
    "explanation": (
      "Correct: unload the loaded Repetierbüchse (bolt-action rifle) before "
      "climbing the Hochsitz (raised hide). GHC Weapons - Ammo (14 February "
      "2026) explicitly says never ascend or descend with a loaded firearm. "
      "The SVLFG hunting accident-prevention guidance also requires chamber/"
      "barrel unloading before climbing, descending, or crossing obstacles. "
      "Moving the safety alone or merely opening the bolt is not the keyed "
      "alternative to unloading before climbing."
    ),
    "flag": "ghc-and-svlfg-2026-confirm-high-seat-unloading",
  },
  "H2023-D08-Q047": {
    "expected": ["c"],
    "stem": "driving to the hunt in your car",
    "status": "source_compared_explanation_qualified",
    "source": OFFICIAL,
    "classroom": GHC_AMMO,
    "explanation": (
      "Correct: the firearm must be unloaded while travelling in a car to "
      "the hunt. SVLFG's hunting accident-prevention guidance expressly "
      "requires unloading before entering/exiting and during vehicle travel, "
      "including within a hunting district (Revier). Whether the gun can be "
      "immediately accessible is a separate transport/carrying distinction "
      "under WaffG; access rules do not make it permissible to keep it loaded. "
      "The GHC Weapons/Ammo class teaches unloading when not actively hunting."
    ),
    "flag": "svlfg-confirmed-vehicle-unloaded",
  },
  "H2023-D17-Q008": {
    "expected": ["a"],
    "stem": "opening the bolt",
    "status": "source_compared_explanation_qualified",
    "source": OFFICIAL,
    "classroom": GHC_RANGE,
    "explanation": (
      "Correct in the GHC supervised range context: keep the muzzle pointed "
      "toward the target/backstop (downrange) even while operating the bolt. "
      "The February 2026 GHC Range Safety slide directs the rifle horizontally "
      "downrange and says muzzle awareness applies at all times; never turn "
      "or talk while sweeping the weapon across others. SVLFG VSG 4.4 "
      "requires a harmless muzzle direction even when a firearm is unloaded. "
      "This is the range's controlled safe direction, not a universal rule "
      "to aim at any fixed elevation on other terrain."
    ),
    "flag": "ghc-and-svlfg-confirm-safe-range-bolt-direction",
  },
  "H2023-D17-Q018": {
    "expected": ["a"],
    "stem": "held while loading and unloading",
    "status": "source_compared_explanation_qualified",
    "source": OFFICIAL,
    "classroom": GHC_AMMO,
    "explanation": (
      "Correct: keep the muzzle in a direction where no one is endangered "
      "while loading or unloading. The GHC 2026 Weapons/Ammo lesson explicitly "
      "says to point the firearm in a safe direction and to treat every "
      "firearm as loaded. SVLFG's hunting safety guidance requires a harmless "
      "muzzle direction regardless of loaded condition. Blindly pointing "
      "straight up or down is not a replacement for knowing the actual "
      "backstop, environment, and people nearby."
    ),
    "flag": "ghc-and-svlfg-confirm-safe-loading-muzzle",
  },
  "H2023-D08-Q024": {
    "expected": ["b"],
    "stem": "load his weapon at a driven hunt",
    "status": "source_compared_explanation_qualified",
    "source": GHC_TECH,
    "classroom": GHC_AMMO,
    "explanation": (
      "The original Hessen question keys B: after taking the assigned stand. "
      "This is not permission to load as soon as one reaches any stand: "
      "the GHC 2026 Weapons/Ammo lesson says to follow the forester/guide's "
      "instructions and the social/drive hunt's safety briefing for loading "
      "directions. Hunting Techniques (16 February 2026) says the Jagdleiter "
      "briefing states open game, safe positions and start/stop times and "
      "signals. Remain unloaded until the announced authorized point of the "
      "hunt, in the assigned stand and permitted safe sector."
    ),
    "flag": "ghc-driven-hunt-stand-loading-subject-to-jagdleiter",
  },
}

def locate(text):
    marker = "window.GHC_QUESTIONS="
    start = text.index(marker) + len(marker)
    items, span = json.JSONDecoder().raw_decode(text[start:])
    return start, start + span, items

def immutable(questions):
    return {q["id"]: (q["stem"], q["choices"], q["correct"], q["answerType"], q.get("sourceRefs"), q.get("section")) for q in questions}

def main():
    html = INDEX.read_text(encoding="utf-8")
    begin, end, questions = locate(html)
    if len(questions) != 867 or len({q["id"] for q in questions}) != 867:
        raise AssertionError("Original 867 bank records changed")
    before = immutable(questions)
    found = set()
    for q in questions:
        cfg = REVIEW.get(q["id"])
        if cfg is None:
            continue
        found.add(q["id"])
        if q["correct"] != cfg["expected"] or cfg["stem"].lower() not in q["stem"].lower():
            raise AssertionError("Original key/stem requires manual check: " + q["id"])
        q["explanation"] = cfg["explanation"]
        q["learningWhy"] = cfg["explanation"]
        q["sourceReview"] = {
            "status": cfg["status"],
            "checkedSource": cfg["source"],
            "classroomSource": cfg["classroom"],
            "reviewed": "2026-10-15",
            "keyPreserved": True,
            "sourceBankKeyDisputed": cfg["status"] == "source_compared_key_conflict",
            "originalPracticePaperSource": cfg.get("originalPracticePaperSource"),
            "originalPaperKeyVerified": cfg.get("originalPaperKeyVerified", False)
        }
        flags = q.setdefault("flags", [])
        if cfg["flag"] not in flags:
            flags.append(cfg["flag"])
        if cfg["source"].startswith("https://"):
            ref = q.setdefault("officialRefs", [])
            if not any(x.get("url") == cfg["source"] for x in ref):
                ref.append({"label": "SVLFG — VSG 4.4 hunting accident-prevention and firearm handling", "url": cfg["source"]})
        if "warning" in cfg:
            q["preAnswerWarning"] = cfg["warning"]
    if found != set(REVIEW):
        raise AssertionError("Target record(s) missing: " + repr(set(REVIEW)-found))
    if before != immutable(questions):
        raise AssertionError("Immutable exam key/choices/source/IDs changed")
    html = html[:begin] + json.dumps(questions, ensure_ascii=False, separators=(",", ":")) + html[end:]
    # Show a source-dispute warning before the legacy key grades the choice.
    # Warning is neutral and deliberately does not give away omitted option D.
    original = "esc(current.stem)+'</h2><div id=\"choices\">'"
    new = "esc(current.stem)+'</h2>'+(current.preAnswerWarning?'<div class=\"alert\" role=\"note\"><strong>Source review notice:</strong> '+esc(current.preAnswerWarning)+'</div>':'')+'<div id=\"choices\">'"
    if original not in html:
        raise AssertionError("Quiz UI rendering entry point moved: inspect before safety warning change")
    html = html.replace(original, new, 1)
    if html.count("Source review notice:") != 1:
        raise AssertionError("Unexpected duplicate source notice")
    INDEX.write_text(html, encoding="utf-8")
    print("PASS: six source-checked safety items (1 legacy-key dispute, 5 qualified) and pre-answer notice; 867 IDs/answers unchanged")

if __name__ == "__main__":
    main()
