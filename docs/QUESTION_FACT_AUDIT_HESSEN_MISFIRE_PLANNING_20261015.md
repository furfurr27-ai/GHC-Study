# GHC Study — focused question-fact provenance audit, first 3/867 (15 October 2026)

## Scope and immutable-answer contract

Inspected the actual `window.GHC_QUESTIONS` bank **867 entries** extracted from the GitHub `app/src/main/assets/index.html` blob. This is **not** a completed 867-question factual audit. This pass qualifies three distinct problematic/stale question **explanations**, preserving each original question ID, stem, multiple-choice options, answer letter(s), section, `answerType`, and original question sourceRefs. The historical exam practice key and present-day/on-range procedures are separated rather than rewriting a keyed legacy question to match a classroom handout.

Build-only overlay: `scripts/qualify_question_source_caveats.py`; test `scripts/check_question_source_caveats.py` verifies the source and real APK. The overlay explicitly compares all 867 before/after immutable IDs/answers/choices and refuses to run against a changed question set.

### Audit entry 1 — `P2013-S4-Q05`

**Original 2013 practice-test question:** `What is considered the proper gender ration for cloven hoofed game under an Abschussplan?` Key `a: 1 : 1` unchanged.

**Source actually checked:** [Hessisches Ministerium, 20 February 2025 guideline for the management/hunting of Schalenwild](https://rp-kassel.hessen.de/sites/rp-kassel.hessen.de/files/2025-03/2025_02_20_richtlinie_fuer_die_hege_und_bejagung_des_schalenwildes_in_hessen.pdf), specific **Rehwild** section 3.2 (printed p. 13, web PDF page index 12). It calls for 50:50 planning but permits, on Hegegemeinschaft proposal during population reduction, a temporary shift to 60:40 female-to-male. The same guideline includes species-specific and condition-dependent guidelines for Rotwild, Damwild and Muffelwild.

**Correction:** Preserve 2013 practice key 1:1, but add an explanatory caution that it is *not* an unchangeable universal legal quota for every species/context. Distinguish the default target from a qualified management exception. Do not replace actual 2025 official agency guidance with old classroom generalities.

### Audit entry 2 — `P2013-S4-Q08`

**Question:** `Which cloven-hoofed game maybe hunted without a game harvest plan without exception?` Key `a: Schwarzwild` unchanged.

**Source actually checked:** [Hessen RP Kassel hosted 7 March 2025 decree on Abschussplanung, -festsetzung und -vollzug](https://rp-kassel.hessen.de/sites/rp-kassel.hessen.de/files/2025-03/2025_03_07_erlass_abschussplanung-festsetzung_und-vollzug.pdf), section 3.2, cites **BJagdG § 21(2)**: Schalenwild with the exception of Schwarzwild is subject to Abschussplan requirements. The decree is listed by the state upper hunting authority's current downloads.

**Correction:** Explicitly qualify that the exception is only to a harvest plan—not to hunting seasons, reporting, game welfare, safety rules, or other applicable law. The actual practice key is left untouched.

### Audit entry 3 — `H2023-D04-Q137`

**Question:** `How do you respond to a misfire?` Source Hessen 2023 practice bank option a: keep muzzle downrange and only open the action after 10 seconds. Key `a` unchanged.

**Primary GHC classroom source directly checked:** Connected original [`Range - Saftey (20260211).pdf`](https://drive.google.com/file/d/1tjfFeqn-1lEAy_7FEsn-gL_LOKlLr9Oq/view), `Miss Fire procedures for any range` passage says to keep the firearm pointed downrange for 10 seconds and then **carefully hand it to the instructor**. This teaching differs from the Hessen answer's unsupervised action-opening wording.

**Correction:** Show both verbatim instructional intents clearly: to answer the historical Hessen quiz, choose `a`; on the GHC class range follow the instructor/range safety officer's explicit procedure rather than treating an exam answer as permission to manipulate or open a firearm. The project does **not** resolve the range safety difference by inventing a unified procedure.

## CI and release gates

Workflow overlay runs for source smoke and Android APK builds and for separately installable APK. New checker tests specific explanation strings, citations and **original keyed answers** in both assembled `index.html` and actual built APK's `assets/index.html`, in addition to the existing strict 71/71 image/media gate, glossary checker and Android emulator smoke test.

**Evidence limitations:** Original 2013 bank key and 2023 translated Hessen question representations were inspected from the live GitHub app question bank, not re-fetched from the full original paper question scans in this review. The connected GHC 2026 range-slide text and cited 2025 Hessen directives were read directly; official PDF page screenshots were attempted but not retrieved. The source review corrects **three explanatory entries only**; it does not prove all 867 facts/answers correct nor that regulations remained unchanged after source publication. Physical Galaxy S23 Ultra testing remains outstanding.

**Current status**: Await exact new workflows' outcome before calling the assembled and APK tests successful. See `NEXT_ACTION.md`.
