# GHC Study Android

Version **1.4.6** (versionCode 146), package `org.ghcstudy.v141`. Target: Samsung Galaxy S23 Ultra. Android minSdk 24, compile/target SDK 35.

The project is currently **public on GitHub**. Do not commit private class slides, copyrighted PDFs, credentials, or personal data.

## Build
GitHub Actions: **Build Android APK from tracked source** (`.github/workflows/android-apk.yml`). The build uses `app/src/main/assets/index.html`, tracked `assets/media/`, and `res/drawable/ic_launcher.png`. It must not extract or embed the historical APK.

## Audit and provenance
- `Audit recovered v1.4.5 against historical APK` compares tracked source files with the original v1.4.5 APK stored in commit `9ce4b3037af3b1a9af5f88ef645265bb06d6f245`.
- `Static app and repository audit` scans asset sizes, media references, duplicate files, external dependencies, and inline JavaScript syntax. Its reports are diagnostic; unreferenced assets are not automatically deleted.
- `docs/SOURCE_INVENTORY.md` maps course sources; `docs/AUDIT_V145.md` records original app parity constraints.

## Quiz and Study Mode additions
- **Jägersprache1** is the third native Quiz Mode bank with 77 German-to-English vocabulary questions in five topic groups. It shares the existing mastery-progress, backup, and reset machinery.
- **Trophy Anatomy** is the English-only Study Mode title. The card retains the class-based deer and horn facts, and uses the original labeled Rotwild antler image from *Game - Rotwild.pdf*, page 14.

## Non-negotiable regression requirements
- Android system Back returns to the previous app screen; root exits only intentionally.
- Quizzes, direct/related pools, study cards, references, and progress/reset scope retain behavior.
- Existing saved progress and offline images remain usable after updates.
- Study card Details and Other Facts are sourced only from class slides. Photos are individual images, not slide screenshots.

## Change policy
Do not bulk-minify or remove assets without measured savings, an explicit source diff, a successful parity/build audit, and behavior regression evidence. A successful build is not proof of runtime correctness.

## October 2026 glossary and verification work

The v1.4.6 development branch includes **162 offline searchable Jägersprache entries: 160 meanings available and 2 pending** (`Jagdschuetz`, `Tiroler`). Entries distinguish class-PDF text, worksheet-to-class contextual matches, historical course guides, and explicitly labeled external authorities. Of the original 77 word-origin/breakdown notes, **2 now have individually cited historical or word-formation support** (`Schweiß`, `Schweißhund`) and **75 remain unverified**; each status is labeled individually and the summary counts are dynamically derived. Do not interpret a compositional mnemonic as verified historical word origin or poacher camouflage. See `docs/GLOSSARY_ETYMOLOGY_UI_AUDIT_20261015.md`. The glossary remains searchable and cross-referenced, with its offline Android link and all original IDs preserved.

**Audit status (2026-10-13):** All 38 listed class PDF texts were retrieved. The app currently has **803 class-PDF-text-checked fact blocks of 814**, leaving **11 pending classroom-slide verification**. The remaining 11 are the historical 2013 course-guide Murmeltier and Seehund/Robbe facts, separately checked against that guide but not misrepresented as 2026 slide evidence. Five unsupported/editorial blocks were removed from the original 819. Checked means fidelity to PDF text, **not** independent biological/legal correctness, verified slide illustration/page location or a complete audit of individual exam explanations. See `audit/study-card-claim-register-20261012.json`, `docs/SLIDE_AUDIT_PROGRESS_20261013.md` and `docs/CURRENT_LAW_SOURCE_WARNINGS_20261013.md`.

GitHub Actions regression covers quiz/navigation/glossary, the Android Back bridge, APK packaging, and Android emulator smoke checks. Installation/upgrade retention on the actual Galaxy S23 Ultra remains to be checked.

## Exam-question integrity audit (2026-10-13)

`scripts/check_question_bank_integrity.py` now verifies all 867 shipped exam records (100 Practice Test + 767 GHC Focused), answer IDs, options, explanations, and mechanical parenthetical answer giveaways. The source question `H2023-D19-Q042` was corrected to remove a direct parenthetical answer clue without changing the original answer key, and four duplicated malformed question stems were smoothed. The scanner flags 18 same-stem pairs and 491 questions without explicit visual-ref fields for further human review, but does not remove questions or claim those 491 are missing animal pictures. See `docs/QUESTION_BANK_INTEGRITY_20261013.md` and `docs/QUESTION_DUPLICATE_REVIEW_20261013.md`. A green mechanical scan is not a factual or current-law audit.

## Current media release gate (2026-10-15)

The tracked assembly overlay repairs **70 of 71** original whole-slide study thumbnails and separately fixes the unrelated Shot Placement image. **One slide-style visual remains unresolved:** `abschussplan`. Two newly authored, source-limited, self-contained SVG schematics illustrate the original GHC `misfire` and `shotdistance` lessons, clearly labeled as *new illustrations*, not instructor-supplied images. The shotgun visual explicitly warns that its 3 mm × 100 m danger-range rule of thumb is **not a safe boundary**. Media CI verifies SVG hashes, source provenance and 117/117 offline image paths. The strict visual release gate deliberately remains failing until `abschussplan` is accurately depicted as a prospective harvest plan, not a historical Streckenliste. Sources and limitations: `audit/study-media-review-20261014.json`, `docs/STUDY_MEDIA_MISFIRE_SOURCE_SCHEMATIC_20261015.md`, `docs/STUDY_MEDIA_SHOT_DISTANCE_SCHEMATIC_20261015.md`.
