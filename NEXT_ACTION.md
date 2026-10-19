# NEXT_ACTION — GHC Study

Verified state: **2026-10-19**, main branch, Android **v1.4.7**, versionCode **147**.

## This development task is complete on GitHub

Study Cards → Schalenwild now has one collapsible **Schalenwild · Vergleichsmatrizen** panel above the search field, with three tabs: **Fortpflanzung (Reproduction)**, **Geweih & Horn (Antlers/Horns)** and **Erkennung (Identification)**. It is implemented in external JS/CSS over the original audited v1.4.5 APK HTML, preserving existing study-card Details and Other Facts.

Main implementation:
- app/src/main/assets/schalenwild-matrix.js
- app/src/main/assets/schalenwild-matrix.css
- tools/inject_schalenwild_matrix.py
- tools/test_schalenwild_matrix.js

Course sources rechecked: all seven original Game species PDFs in connected Google Drive and consolidated GHC Section 1 study deck. Known unresolved source discrepancy: Gamswild slide gives November rut, 20–21 weeks gestation and May births; the matrix preserves the slide values with a warning rather than inventing a correction. The Waidwissen video inspired the visualization only.

## Build VERIFIED

GitHub Actions run #194 succeeded and uploaded `GHC-Study-v1.4.7-debug-apk`:

https://github.com/furfurr27-ai/GHC-Study/actions/runs/39292481477

Successful run steps: recover audited baseline, inject assets, JavaScript syntax, matrix regression tests, Android Gradle assembleDebug, packaged asset checks, artifact upload. Artifact was confirmed present and not expired on 2026-10-19.

## ONLY remaining acceptance item: physical Android check

On Samsung Galaxy S23 Ultra, install the **v1.4.7** APK from the successful run. Check:
1. Study Cards → Schalenwild: ONE comparison panel above the existing search and grid.
2. Open all three views; long tables scroll sideways, species names stay visible, all seven rows appear.
3. Reproduction Both/Rut/Births controls work. Switch views and return; collapse/reopen; exit/re-enter Schalenwild.
4. No clipped controls in portrait, Android system Back still navigates inside app, launcher icon preserved, and the app works offline.
5. Study-card details and Quiz Mode still show existing course content.

Do **not** claim the phone test passed without an actual report. If failed, fix only the observed defect, rerun workflow and update version/checkpoint. If passed, this Schalenwild matrix task can be closed. Do not add speculative next features as blockers.

## Later enhancements — optional, not blockers

Further comparison matrices (Federwild lookalikes, Raubwild, Field/Forest) are proposed in research/waidwissen-comparison-matrix-roadmap.md. They require separate source checks and explicit implementation decisions; the creator's full YouTube catalog/transcripts have not been comprehensively accessed.

Research/source inventory:
- research/waidwissen-schalenwild-intake.md
- research/waidwissen-comparison-matrix-roadmap.md
