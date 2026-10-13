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

The v1.4.6 branch includes **162 offline searchable Jägersprache entries**: 109 have meanings (77 from the prior quiz bank, 30 additional definitions directly checked against course-deck text, and 2 historical marmot terms checked against the 2013 U.S. Forces course guide); 53 worksheet terms await source verification. Historical guide senses are explicitly distinguished from 2026 class-slide evidence. The original 77 historical/etymology explanations themselves are not yet independently validated. The searchable glossary has linked terminology, topic/verification filters, and an offline Android entry point.

**Audit status (2026-10-13):** All 38 listed class PDF texts were retrieved. The app currently has **803 class-PDF-text-checked fact blocks of 814**, leaving **11 pending classroom-slide verification**. The remaining 11 are the historical 2013 course-guide Murmeltier and Seehund/Robbe facts, separately checked against that guide but not misrepresented as 2026 slide evidence. Five unsupported/editorial blocks were removed from the original 819. Checked means fidelity to PDF text, **not** independent biological/legal correctness, verified slide illustration/page location or a complete audit of individual exam explanations. See `audit/study-card-claim-register-20261012.json`, `docs/SLIDE_AUDIT_PROGRESS_20261013.md` and `docs/CURRENT_LAW_SOURCE_WARNINGS_20261013.md`.

GitHub Actions regression covers quiz/navigation/glossary, the Android Back bridge, APK packaging, and Android emulator smoke checks. Installation/upgrade retention on the actual Galaxy S23 Ultra remains to be checked.
