# GHC Study

Offline Android study app for the German Hunting Course.

Current source version: **v1.4.7** (built from the audited v1.4.5 baseline APK, with modular Schalenwild matrix overlays). Original study-card Details and Other Facts remain based exclusively on GHC class slides.

### Schalenwild comparison matrices

**Study Cards → Schalenwild** contains **one expandable comparison panel immediately above the existing search and study-card grid**, with three switchable views:

1. **Fortpflanzung (Reproduction):** existing horizontally scrollable 12-month rut/birth chart for seven species, with gestation and emphasis on Eiruhe, boar's 3+3+3 gestation and the unresolved Gamswild course discrepancy. Use Both / Rut / Births to filter.
2. **Geweih & Horn (Antlers / Horns):** antlers versus permanent horns versus tusks; course-qualified shedding, velvet-growth and rubbing details. Missing cross-species month data is deliberately marked — rather than invented.
3. **Erkennung (Identification):** trophy type, adult tooth count (32/34/44), ruminant status and Niederwild/Hochwild classification, including memory cues for the exceptions.

All three views are offline and share one panel. Switching views does not clone or overwrite existing study-card facts. German hunting vocabulary is paired with English wording. Tabs support touch and arrow-key operation; tables scroll horizontally with a sticky species column. A live phone-layout check remains necessary.

Implementation: app/src/main/assets/schalenwild-matrix.js, schalenwild-matrix.css, and tools/inject_schalenwild_matrix.py. The GitHub Actions build recovers the existing audited app assets and launcher icon from the checked-in v1.4.5 APK, then injects these modules. tools/test_schalenwild_matrix.js validates original course facts, seven species, the three comparison views, tab state and scoped stylesheet with built-in Node tools.

### Build, source review and limitations

Build on GitHub Actions → **Build Android APK**. The expected artifact name is **GHC-Study-v1.4.7-debug-apk**. Check the latest GitHub Actions run and install the APK on a Galaxy S23 Ultra before considering v1.4.7 device-verified.

The figures come from the connected GHC Section 1 study deck and the seven original species slide PDFs. The **idea** of a comparison layout was inspired by [Waidwissen WaidMatrix](https://youtu.be/bZSqIRW5zTQ), not the copied graphics or an imported transcript. Course disagreements are explicitly flagged instead of silently resolved.

- Source audit: research/waidwissen-schalenwild-intake.md
- Matrix roadmap and acceptance checks: research/waidwissen-comparison-matrix-roadmap.md
