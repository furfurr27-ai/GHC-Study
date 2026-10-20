# v1.4.5 source restoration — audit status

Date: 2026-10-08. This document records what was **directly verified** and what is **not yet proven**. Do not describe partial checks as complete functional parity.

## Observed baseline

- Current main commit at start: `9ce4b3037af3b1a9af5f88ef645265bb06d6f245`.
- Repo contains a v1.4.5 standalone APK (`11,262,412` bytes) in `app/src/main/assets/`, and a large standalone `index.html` (`18,650,194` bytes).
- There is no committed `app/src/main/res/drawable/ic_launcher.png` or `assets/media` directory in the main tree as inspected.
- Android Gradle metadata: applicationId `org.ghcstudy.v141`, minSdk 24, targetSdk / compileSdk 35, versionCode 145, versionName 1.4.5.
- The current workflow **deletes the committed HTML during CI**, extracts `assets/*` and a launcher PNG from the embedded APK, removes the source APK from its temporary build workspace, and packages the recovered files. This is a valid recovery strategy but not a maintainable source-of-truth build.
- Latest inspected CI run: [37732188864](https://github.com/furfurr27-ai/GHC-Study/actions/runs/37732188864), successful; its installable artifact is `GHC-Study-v1.4.5-debug-apk`. A successful build does not prove that behavior matches the baseline or that the APK was exercised on a physical phone.
- The Android activity uses heuristics to click visible `.backlink,.study-back` elements, set global `view` and `mode`, or exit. This does **not** guarantee last-screen navigation for a single-page web UI.
- Manifest icon `@drawable/ic_launcher` relies on CI extracting an image from the APK. It should be committed and verified as a source asset.
- README incorrectly claims the repository is private and refers to v1.4.2; the GitHub repository metadata currently reports public.

## Acceptance criteria for parity

- [ ] Independently inspect original APK manifest, icons, index, and media list; record checksums.
- [ ] Extract every `assets/*` file to tracked source assets; use a dedicated `reference/` or release storage for the old APK rather than packing an APK into the application assets.
- [ ] Compare extracted original files against tracked files byte-for-byte; fail CI if assets are missing or altered unexpectedly.
- [ ] Separate application CSS, JavaScript, question banks, study cards, media manifest, and Android bridge into readable modules **without** silently changing behavior. Prefer a generated standalone distribution file if needed for compatibility.
- [ ] Build solely from checked-in source, without needing to unzip a previous APK in CI.
- [ ] Implement explicit history stack or app-to-native back bridge with tests: modal, study card, nested quiz, references, reset dialog, root behavior.
- [ ] Commit launcher resources (including adaptive icon if supported); test icon packaging.
- [ ] Confirm app installation/upgrade and persistence of quiz progress on Samsung Galaxy S23 Ultra; preserve applicationId and save keys.
- [ ] Regression check study card imagery and Details/Other Facts slide provenance.
- [ ] Regression check direct/related GHC question sections, answers, review explanations, reset scopes, navigation, and offline rendering.
- [ ] Include deterministic asset counts, checksums, unit/smoke tests, and APK verification in CI.

## Immediate next action

Recover the original APK binaries to the work environment (or use a trusted CI extraction manifest) and compare original `assets/index.html`, media paths, Android metadata, and icons. Only then change application logic. Do **not** mark functionality audited because compilation succeeded.

Source locator inventory: [SOURCE_INVENTORY.md](SOURCE_INVENTORY.md).
