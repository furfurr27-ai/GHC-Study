# GHC Study — Abschussplan image, exact sources and limitations (2026-10-15)

## Problem

The `abschussplan` study card previously displayed a classroom whole-slide thumbnail. The historical `Streckenliste` image initially considered from the original Revier PDF is **not** a prospective Abschussplan and was correctly rejected. The original Nature/Animal Protection 2019 GHC slides teach the term `Abschussplan` and population regulation, not the exact current form layout.

## Primary and current official evidence actually checked this turn

1. **Hessisches Ministerium / Regierungspräsidium Kassel** (Hessen upper hunting authority), [official Jagd downloads](https://rp-kassel.hessen.de/forsten-und-landwirtschaft/jagd). The current listing as checked October 15, 2026 separately offers `Anlage 1 Streckenliste`, `Anlage 2a Abschussplanung Rot-, Dam-, Muffelwild` and `Anlage 2b Rehwild` (XLSX). **The 2026 XLSX was linked and download attempted, but could not be retrieved into our container. It was NOT visually inspected or parsed.**
2. **Hessisches Ministerium**, [7 March 2025 decree `Abschussplanung, -festsetzung und -vollzug`](https://rp-kassel.hessen.de/sites/rp-kassel.hessen.de/files/2025-03/2025_03_07_erlass_abschussplanung-festsetzung_und-vollzug.pdf), especially section 4 and Rehwild planning discussions. It identifies Anlage 2a/2b as model forms, strongly recommends the official `Jagdstatistik Hessen` digital portal, and describes a multi-year (three-year) roe-deer plan. This was read from web-extracted official PDF text; screenshot of that PDF not used to authenticate a form illustration.
3. **Main-Kinzig-Kreis Jagdbehörde**, publicly posted **2025** [`Anlage 2b Seite 1 — Abschussplan für Rehwild — Abschussplanung`](https://www.mkk.de/media/resources/pdf/mkk_de_1/buergerservice_1/lebenslagen_1/sicherheit_und_ordnung_1/32_kreisordnungsamt_1/jagdbehoerde/2025_4/Abschussplanung_Rehwild.pdf). The one-page official administrative PDF was directly opened in the research browser and its extractable text inspected. Its identifiable fields: `Untere Jagdbehörde`, `Hegegemeinschaft`, `Jagdbezirk`, `Fläche/davon bejagbar`, `Jagdausübungsberechtigte(r)`, `Jagdrechtsinhaber`, `Planungszeitraum`, historical `Jahresstrecke der letzten drei Jagdjahre`, and prospective `Abschussvorschlag` by the hunting-right holder, the `Hegegemeinschaft`, and `Sachkundige`; sex/age categories for Rehwild. The web-PDF screenshot operation returned **cache miss**; its exact page geometry and graphics were *not visually authenticated*. It is **not proven identical to the inaccessible 2026 XLSX**.
4. Existing live GitHub `app/src/main/assets/index.html` study card `abschussplan` and card facts were previously parsed; 117 cards. Original 2019 classroom source `Law - Nature and Animal (201902).pdf` was fetched as readable text and directly confirms the term and conservation purpose.

## What changed and what did not

Instead of copying a full government form as a reduced, illegible slide image or inventing an enforceable form, I authored one **self-contained, educational SVG** that explains the distinction in large legible blocks. It has unfilled `Jagdbezirk`/`Hegegemeinschaft`/`Planungszeitraum` fields and separates:
- **Rückblick:** `Jahresstrecke der letzten 3 Jagdjahre` (retrospective actual harvest figures, purposely blank)
- **Vorschlag:** proposed male/female Rehwild cull (purposely blank, no invented quotas)
- **Hegegemeinschaft / Jagdbehörde:** proposal and formal setting

The bottom of the SVG conspicuously reads `EDUCATIONAL SCHEMATIC · BASED ON HESSIAN ANLAGE 2b · NOT AN OFFICIAL FORM`. It is a **newly drawn source-grounded instructional diagram**, **not** an extracted PDF image, downloaded current Excel form, enforceable 2026 plan, recommendation, authorization, or signed official document.

- Asset: `app/src/main/assets/media/abschussplan-hessen-anlage2b-educational.svg`
- Exact source Git blob SHA1: `a333ad9456c5e065a1ed6990e37676210d36a34c`
- Build-only mapping: `scripts/overlay_abschussplan_course_schematic.py` (changes ONLY visualId/imageKey for one `abschussplan` card and its new media index; 117 card's non-image facts intact)
- Audit: `audit/study-media-review-20261014.json` classifies the newly drawn image as `authoredCourseIllustrations`, **not** as an original sourced photograph/embedded PDF image
- Tests: `scripts/check_study_media.py` checks exact Git blob content, source references, explicit `notOfficialForm` metadata and visible on-image warning; both workflows now assemble all three course-topic illustrations and run **`--strict`** media checks against both assembled source and *actual packaged APK*.

## Coverage and remaining limitations

All **71 originally slide-like study-card images** now have separate standalone images/illustrations in the assembled app: 53 original class photo crops, 11 exact source PDF figure extractions, 3 picture montages, 1 source-photo reuse and 3 clearly marked newly authored source-text-based educational vectors (`misfire`, `shotdistance`, `abschussplan`). All 117 offline study images are independently checked by CI. The unrelated `shotplacement` wrong-subject visual had previously been corrected. The visual-style gate is no longer the outstanding release issue *once CI actually passes at this code*.

This is **not** independent verification of all 117 image subjects, image copyright redistribution permission, 867 questions, 160 glossary definitions, 75 word histories, German weapons/hunting law currency, or physical Samsung Galaxy S23 Ultra operation. The class course prose/card meanings have not changed. The app still requires physical install and saved-progress upgrade/back tests. Do not claim current 2026 Hessen official spreadsheet inspection.

**Latest CI and Git SHA:** read live workflows and checkpoint after this change. Record results precisely before claiming that `--strict` release validation passed.
