# GHC Study — 2026-10-15 drive-hunt photograph recovery and final three media blockers

## Primary classroom images actually checked

The connected **Hunting Techniques (20260216).pdf** (33 slides, original file also appearing as `Hunting_Techniques_V3.1_16FEB26.pdf`) was inspected directly, including slides **9–16**. Slide 13 is a **text-only** `Drive Hunts` discussion of the Jagdleiter briefing. Adjacent slide **15**, `Drive Hunts / General Equipment`, includes a genuine classroom-photo example of an outdoor group wearing high-visibility hunting clothing, with one hunter gesturing toward a direction while others stand nearby. The photograph does **not prove a formal Jagdleiter briefing took place** or demonstrate every briefing element.

Rather than copying slide 13 or displaying an unrelated photograph, the `drivebrief` card is mapped to this standalone original classroom image. No procedural instructions were added or inferred.

- Source classroom PDF: `Hunting Techniques (20260216).pdf`
- Source page: **15** (one-based)
- Embedded JPEG XObject: **83**
- Source image size: **423 × 318**
- Source file: `app/src/main/assets/media/drivebrief-class-hunters-discussing.jpeg`
- Exact Git blob SHA-1: `a314fec028ffa4fc54ecd70af17c63dc1fa49baa`
- Exact source-image SHA-256: `3e0ea5c5f46a851135b57519dc514d7eb3926c25d02d7e7c32432ab9935b368d`

`scripts/crop_study_slide_images.py` now maps `drivebrief` to this original JPEG during APK assembly; `scripts/check_study_media.py` verifies the source document title, page, XObject ID, SHA-256 and actual image path. The previous full slide remains available for provenance, but is no longer the card's displayed image.

## Source integrity and test gates

The preceding Revier Roles fix was separately [Android 35 emulator verified in run 38668935001](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38668935001), including functional smoke, APK build and three system Back-navigation paths. Its standalone APK passed as run 38668957594, and direct inspection confirmed 117 original card non-image fields, glossary data and app icon identical to the preceding 66-image APK.

The new **68-image** code is at commit `7acf5e9253f1d523a651b0eef002f8736ae0e826`, with manifest count update `b9c55a3cf7f83465224ba2f37dacbd6fd7dcba25`. **Check final Android CI and standalone APK conclusions at that code or newer** before asserting 68-image verification. Source GIF/JPEGs and source PDFs were checked directly, but final One UI hardware compatibility has not been tested.

## Corrected-media ledger after the new change

- **117** study cards.
- **71** originally lecture-slide-like image displays.
- **53** separate photo crops, **11** exact embedded PDF JPEG figures, **3** source-photo montages, **1** classroom photo reuse = **68 corrected**.
- **3** full-slide cards remain unresolved: `misfire`, `abschussplan`, `shotdistance`.
- The separate historical `shotplacement` image mismatch remains corrected and exact original source hash checked.

## Why these three are intentionally pending

1. **Misfire.** The 2026 Range Safety PDF slide gives its instructor's range procedure in text; the appended photograph of firearm components does not depict the required actions. No safe, accurate, standalone instructor-approved procedure illustration was found in the exact source pages inspected. A generic gun photograph would be misleading. Do not present present-day safety guidance derived from an image alone.
2. **Abschussplan.** The 2014/2015 form in the Revier lecture is a **Streckenliste** (actual harvest record), not an **Abschussplan** (planned harvest). The [Hessen RP Kassel hunting downloads](https://rp-kassel.hessen.de/forsten-und-landwirtschaft/jagd) list separate blank examples for `Streckenliste`, `Anlage 2a Abschussplanung Rot-, Dam- und Muffelwild`, and `Anlage 2b Rehwild`. Its [2025 harvest planning directive](https://rp-kassel.hessen.de/sites/rp-kassel.hessen.de/files/2025-03/2025_03_07_erlass_abschussplanung-festsetzung_und-vollzug.pdf) identifies the appropriate current forms and online portal. An exact, suitably sized graphic of that **planning** form is still needed; no old harvest table was substituted.
3. **Shot Distance.** The existing lesson tables and arithmetic rules describe shot/pellet travel hazard heuristics, not a universal safe maximum. The original teaching material has no isolated, verified distance/dispersion diagram supporting every context; don't invent one or present a crude thumb-rule as guaranteed safety.

All **867** question IDs, answer/explanation records, **117** study-card facts, glossary **160/162** definitions, app icon, system Back and progress storage keys remain outside this media edit. Historical origins of **77** terms, the two ambiguous worksheet words `Jagdschuetz` and `Tiroler`, full question-fact audit and physical Samsung S23 Ultra testing remain pending.

## Copyright/provenance caveat

Individual image bytes were copied from the user-supplied course PDF. The class deck itself may have borrowed third-party web photography. This establishes classroom provenance, **not independent public redistribution permission**. The private draft GitHub PR remains unmerged.

**Actually inspected:** the 2026 Hunting Techniques original PDF slides 9–16 and JPEG xref83, the source Revier role figures and Revier PDF page30, original Hunting Dogs Dog Parts PDF page4 and its verified image, GitHub Actions run/job results, two standalone APK files compared at the 66/67 stage, and the independent Hessen RP Kassel official hunting-form source. This does not constitute a current German law audit.
