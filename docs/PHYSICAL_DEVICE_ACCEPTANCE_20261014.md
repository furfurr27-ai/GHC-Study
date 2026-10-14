# GHC Study v1.4.6 — Galaxy S23 Ultra physical acceptance plan (2026-10-14)

**Status:** Test plan only. No physical handset tests have been performed by the repository CI.

## Install and compatibility

1. Download the newest **successful** `Build standalone GHC Study APK` Actions artifact (package `org.ghcstudy.v146.standalone`, versionCode 146). This is intentionally separate from the older `org.ghcstudy.v141` installation and reduces debug-signature conflicts.
2. Confirm launcher icon, correct GHC Study name, local page rendering and that Study Mode and Reference can be opened without network.
3. Record Android/One UI version, WebView version and whether navigation uses three buttons or gesture bar. Target device is Samsung Galaxy S23 Ultra. Do not assume Android emulator results reproduce One UI.

## Navigation checkpoints

| Starting screen | Action | Required result |
|---|---|---|
| Quiz Mode home | Open Glossary; press Android system Back | Returns to Quiz Mode without closing the app |
| Quiz Mode home | Open Reference; press Android system Back | Returns to Quiz Mode without closing the app |
| Study Mode hub | Open Schalenwild → Rehwild; press system Back | Returns to Schalenwild list with Rehwild tile |
| Schalenwild list | Press system Back | Returns to Study Mode hub |
| Study Mode hub | Press system Back | Returns to Quiz Mode |
| An active quiz question | Press system Back | Returns to Quiz Mode home without clearing existing progress |
| An open modal | Press system Back | Dismisses modal without exiting |
| Quiz Mode root | Press system Back | Android may return to launcher; no nested app screen remains |

## Data and offline checkpoints

- Verify 100 Practice Test, 767 GHC Focused (Direct/Related) and 77 Jägersprache quiz items remain selectable; never reset existing app data merely for testing.
- Answer a previously untouched question, close/reopen **the same package** and verify state persists. Do not use an uninstall/reinstall cycle for this check.
- From Reference, export a backup, inspect that a file was produced, then test import/restore **only on the side-by-side standalone test package**. Preserve the original data and backup first.
- Test selective progress reset only on the test package, including by category and subcategory.
- Enable Airplane Mode after the app is installed and launch it offline; inspect a sample from Rehwild, bird, dog, raptor, trophy, and other-game cards. Verify images are standalone illustrations/photos rather than whole-slide screenshots; inspect legibility and missing-image placeholders.
- Confirm search for `Schweiß` / `Schweiss`, `Kugelfang` and `Leberegel`, visible provenance flags and cross-links in the offline Jägersprache glossary.
- Verify the 2013 Murmeltier / Seehund historical-source warning is visible and no obsolete legal statement appears as current hunting permission.

## Release criteria

Do not claim a physically tested release until these checks are recorded with actual device evidence. An APK build success is not a handset usability or data-migration check. Also keep the 803/814 source-text block count separate from legal currency, image accuracy, examination factual review and etymology validation.
