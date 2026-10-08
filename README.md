# GHC Study Android

Version **1.4.5** (versionCode 145), package `org.ghcstudy.v141`. Target: Samsung Galaxy S23 Ultra. Android minSdk 24, compile/target SDK 35.

The project is currently **public on GitHub**. Do not commit private class slides, copyrighted PDFs, credentials, or personal data.

## Build
GitHub Actions: **Build Android APK from tracked source** (`.github/workflows/android-apk.yml`). The build uses `app/src/main/assets/index.html`, tracked `assets/media/`, and `res/drawable/ic_launcher.png`. It must not extract or embed the historical APK.

## Audit and provenance
- `Audit recovered v1.4.5 against historical APK` compares tracked source files with the original v1.4.5 APK stored in commit `9ce4b3037af3b1a9af5f88ef645265bb06d6f245`.
- `Static app and repository audit` scans asset sizes, media references, duplicate files, external dependencies, and inline JavaScript syntax. Its reports are diagnostic; unreferenced assets are not automatically deleted.
- `docs/SOURCE_INVENTORY.md` maps course sources; `docs/AUDIT_V145.md` records original app parity constraints.

## Non-negotiable regression requirements
- Android system Back returns to the previous app screen; root exits only intentionally.
- Quizzes, direct/related pools, study cards, references, and progress/reset scope retain behavior.
- Existing saved progress and offline images remain usable after updates.
- Study card Details and Other Facts are sourced only from class slides. Photos are individual images, not slide screenshots.

## Change policy
Do not bulk-minify or remove assets without measured savings, an explicit source diff, a successful parity/build audit, and behavior regression evidence. A successful build is not proof of runtime correctness.
