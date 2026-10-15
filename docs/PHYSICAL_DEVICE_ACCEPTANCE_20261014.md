# GHC Study v1.4.6 — Galaxy S23 Ultra physical acceptance plan (2026-10-14)

**Status:** Test plan only. No physical handset tests have been performed by the repository CI.

## Fast acceptance check for the completed Practice Test 2 (2026-10-15)

Use the **newest successful v1.4.6 build whose APK job finished on the latest code SHA**. For a low-risk first test, install the standalone APK side-by-side. **It has a different application ID and will not show progress from an existing GHC Study install.** Do not uninstall or clear data from the original app to test a new build.

1. With the phone offline (Airplane Mode) open GHC Study → **Quiz Mode → Practice Test 2**. Confirm all **five parts** and **125 questions** are available; press the ⓘ button to confirm the paper's 150-minute/13-per-part instructions. The native quiz itself is deliberately untimed.
2. Select Part I; answer a normal and a multi-select question. Exit/reopen the same app package and verify progress persisted. Then try **Part II, Question 25** six-pair matching; it must score as **one** question.
3. Navigate to Part III **Question 4** (self-defense), Part IV **Question 16** (injured deer near road), and Part V **Question 20** (gut-contamination). When these come up naturally in the randomized drill, they must show a **historical, not real-world guidance** notice before the answer is checked. The paper's correct choices remain preserved. The app may not present a 2021/22 highlighted key as authority to dispatch animals or handle contaminated meat.
4. Test system Android Back from a nested study card, glossary, modal and active question. Test Search, original dog-anatomy picture, and icon visibility.
5. Use the test package to export a backup, verify a file exists, and only then test reimport, selective progress reset and restoration. NEVER experiment with Reset on the original package without backing it up. Do not claim original-package upgrades preserve data until a real same-application-ID/same-signature update is tested.

**If this passes:** report Android version, whether the package is the standalone or original, and any broken screen/Back/image or progress behavior. Otherwise no further large research tasks are needed to start studying with this historical-paper app.

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
