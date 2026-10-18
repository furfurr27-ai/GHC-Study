# GHC Study

Offline Android study app for the German Hunting Course.

Current build: **v1.4.6** (from audited v1.4.5 baseline APK). Source material on the original study cards remains based on GHC class slides; their Details and Other Facts are not overwritten.

### Schalenwild comparison matrix

Study Cards → Schalenwild includes an offline, horizontally scrollable **Jahresmatrix**, highlighting rut and birth periods across the seven principal hoofed-game groups, with gestation figures and quick distinctions. The matrix derives its numbers from the class animal PDF slides; the comparison visualization was inspired by [Waidwissen](https://youtu.be/bZSqIRW5zTQ).

Implementation: `app/src/main/assets/schalenwild-matrix.js`, `.css`, and `tools/inject_schalenwild_matrix.py`.

Build: GitHub Actions → **Build Android APK**. Workflow recovers the baseline HTML, assets, and launcher icon from the checked-in v1.4.5 APK, injects the matrix assets, and assembles a debug APK. Check the workflow run and install on device before declaring the new release fully verified.

Research and source discrepancy register: `research/waidwissen-schalenwild-intake.md`.
