# GHC Study — verified continuation handoff

Updated: 2026-10-13. Live source of truth: `feature/slide-audit-glossary-tests-20261012` (draft PR #3 to `audit/v145-source-recovery`). Do **not** restart or overwrite the older `main` branch.

## Build and app invariants

- v1.4.6, versionCode 146; SDK 35 target/compile, minSdk 24; primary app ID `org.ghcstudy.v141`; side-by-side test app ID `org.ghcstudy.v146.standalone`.
- Maintain 100 practice questions, 767 GHC-focused (Direct/Related) questions, 77 vocabulary quiz questions, 117 study cards, and the 162-term Jägersprache glossary (143 with meanings / 19 pending; two meanings from a historical 2013 course guide, not 2026 class slides).
- Preserve existing quiz progress storage, selective reset and backup/restore, offline images, system Back and launcher icon. Debug APK signatures from independent builds may differ; the standalone app is safer for initial installation.

## Source research completed and remaining

- Readable text for all 38 inventoried class PDFs was fetched in preceding audits; additional `Guide_08n1-5_Other_Game_2013-08.pdf` was directly located and re-read in Drive today.
- Study-card audit register: **803 text-checked / 11 pending class-slide verification / 814 displayed blocks**. Five unsupported/editorial blocks removed from the original 819. Counts derived from `audit/study-card-claim-register-20261012.json`, not stale chat summaries.
- The 11 pending fact blocks all belong to the Murmeltier (6) and Seehund/Robbe (5) cards. Their historical guide text is now separately traced in each claim's `supplementalSource` field; do **not** mark these as checked against 2026 class slides or as current legal facts. Two individual blocks have only partial support from the guide.
- New 2026-10-13 audit updates verified source wording for wolf, wildcat, bear, Rehwild, Rotwild and Schwarzwild; removed editorial/unattributed material from wolf/trophy cards. See `docs/SLIDE_AUDIT_PROGRESS_20261013.md`.
- Text-checked does **not** certify embedded photo diagrams, genuine page numbering, legal currency, historical etymology or all assertions within compound fact blocks. The 867 examination explanations and original 77 vocabulary etymologies are separate unfinished audits.

## Immediate engineering next steps

1. Verify CI after the latest source/claim-register synchronization. `scripts/check_claim_register_parity.py` compares all fact text, labels and counts against shipped HTML. The prior failed workflow against commit `be6ec881...` failed due to a **stale Collared Dove claim string**, but live 2026-10-13 source/claim comparison is now synchronized.
2. Trigger the glossary/functional CI on changes to both `app/src/main/assets/index.html` and `audit/study-card-claim-register-20261012.json`; do not treat a workflow from an intermediate, not-yet-synchronized commit as final build evidence.
3. Test the latest APK including emulator system Back, glossary and app icon, then use the standalone APK on a Galaxy S23 Ultra for physical validation and offline progress tests.
4. Decide whether historical 2013 course-guide cards should be explicitly segregated from *class-slide-only* Study Mode material. Do not silently remove source-backed content or promote guide evidence to a 2026 slide citation.
5. Finish photo/diagram identification review, question-by-question audit, and glossary/etymology verification before merging PR #3.

## Preserve source discipline

Study-card Details/Other Facts contain class-slide material only unless an exception is explicitly labeled as historical course-guide material; never insert speculative instructor commentary or unsupported internet facts. Maintain separate references to current German hunting law where relevant. No claim that an APK compiled means the installed behavior was tested on the owner's handset.

## 2026-10-13 continuation — glossary batch

- Nine additional worksheet terms now have source-attributed meanings: Brucellose, Schweinepest, Fuchsbandwurm, Kleiner Münsterländer, Hahn in Ruh, Untere Jagdbehörde, Jagdschein, Wiederkäuer, Frettieren. Glossary is 127 defined / 35 pending, 162 total.
- For Frettieren, Jagdschein and Wiederkäuer, the class deck supports the context but does not explicitly translate the worksheet headword. This limited provenance is reflected in per-entry audit metadata. Etymologies remain blank where not directly verified.
- See `docs/GLOSSARY_DEFINITIONS_BATCH_20261013.md` for evidence and open issues. Recheck latest runtime/Android CI before using the updated APK.

## 2026-10-13 — question-integrity continuation

- Added `scripts/check_question_bank_integrity.py` to CI. It verifies all 867 exam items and their answers/learning explanations structurally; a passing report proves no mechanical giveaways under the current heuristic, **not** legal/biological factual truth.
- Fixed the exact answer giveaway in `H2023-D19-Q042` (Jagdschein translated in stem, repeated as choice B), preserving the correct answer ID. Smoothed the duplicated range-supervisor questions `H2023-D04-Q151`/`H2023-D15-Q010` and live-capture questions `H2023-D09-Q083`/`H2023-D15-Q003` without altering scoring.
- Screened 18 identical-stem pairs (11 pairs with identical normalized choice sets); no records deleted because separate sources and progress IDs matter. Full pair list: `docs/QUESTION_DUPLICATE_REVIEW_20261013.md`.
- The static scanner flagged **491 questions without explicit visual-ref fields**. This is a triage statistic, **not** proof that 491 animal questions lack images. Audit animal references separately.
- Emulator CI has been affected by a **Pixel Launcher ANR modal** in one run and by captures of **an unrendered white WebView startup frame** in another. The latest script waits for rendered screens, dismisses only the external launcher dialog, and checks foreground app state. Verify the latest complete CI run before claiming hardware Back passed.
- Latest physical Galaxy S23 Ultra install/backup/restore/upgrade behavior remains untested in this turn.

## 2026-10-13 — second glossary audit and emulator observability

- Six additional class-linked worksheet terms defined: **Absehen, Kugelfang, Objektiv, Okular, Streckeplatz, Visier**. Glossary current tally: **133 defined / 29 pending / 162 total**. Kugelfang has direct bilingual wording in the range slide. The other five are worksheet-term plus English slide context, *not* exact class-slide translation statements. Etymology remains blank. Evidence: `docs/GLOSSARY_DEFINITIONS_BATCH2_20261013.md`.
- Updated glossary JS DOM regression to assert all six definitions and the current filters. Earlier CI runs at the intermediate glossary-only commit expected 127/35 and therefore failed; evaluate the **latest tested commit** instead.
- Added Android emulator failure artifact collection (logcat, WebView provider, activity/window focus state) and WebView page/JavaScript console diagnostics. Existing CI showed a truly blank WebView surface and unresolved system Back, *not* a verified app navigation pass. Check the latest CI run and inspect diagnostics if emulator remains blank.
- Do **not** merge draft PR #3 into the old `main`, or claim a physical Galaxy S23 Ultra test has occurred.

### Emulator follow-up — corrected target selection

- Evidence from CI run `38413027220` demonstrated the previous gesture script tapped **Reference**, not **Glossary**, because its y-coordinate fell below the Glossary anchor. The resulting system Back exited to the launcher; this is still an unisolated Back failure, **not** evidence about glossary page history.
- Corrected the test at commit `38e6e1b07b217bbdfde7cf61e0e1bf8d0a94b6b7` to tap the actual UIAutomator-located Glossary anchor and require the glossary heading, then exercise Android Back. Workflow `38414557677` is queued as of this handoff; verify its eventual conclusion and artifacts before interpreting the result. See `docs/ANDROID_EMULATOR_TEST_DIAGNOSIS_20261013.md`.
- Still test Back from Reference -> prior tab and Study card -> category separately, then perform physical Samsung Galaxy S23 Ultra validation.

### 2026-10-13 — third vocabulary and emulator reliability continuation

- **135 glossary defined / 27 pending / 162 total.** Directly class-PDF-confirmed translations: `Leberegel` → liver flukes (`Disease - Parasites.pdf`) and `jagende Hunde` → hounds (`Hunting Dogs (202609).pdf`). Source evidence: `docs/GLOSSARY_DEFINITIONS_BATCH3_20261013.md`. No etymology inferred, no question-bank changes.
- Android emulator screenshot/accessibility evidence from run `38414557677`: **Pixel Launcher isn't responding** dialog appeared over an otherwise rendered GHC Quiz Mode page and obscured the `Glossary` link. JS smoke + APK build passed; emulator still failed. Robust post-render and post-accessibility ANR retry added in commit `4fe87f69f0b5b6c74b31dc4b5b2481a6465f1fa3`; check its workflow conclusion and the latest after glossary edits.
- Do not treat the prior launcher dialog as a GHC app crash, but do not certify system Back or glossary page navigation until their actual emulator evidence passes. Continue preserving old `main` and unmerged draft PR #3.

### Android 35 AOSP CI isolation (2026-10-13)

- The previous Pixel 6/google_apis emulator screenshot directly showed a **Pixel Launcher ANR overlay** on top of an otherwise visible GHC Quiz Mode page, causing false "Glossary missing" errors.
- CI test now recovers from this external dialog and uses the Android 35 `default` (AOSP) emulator image instead of `google_apis` to avoid Pixel Launcher as an unrelated dependency. This still tests Android 35 WebView but does not reproduce Samsung One UI; the physical device test is independent and still necessary.
- Updated glossary filter regression to compute expected Defined/Pending counts from shipped glossary data while requiring exactly 162 classified terms and checking new bilingual meanings. The exact documented snapshot remains **135 defined / 27 pending**.
- **Validation gate:** check latest `GHC glossary and functional regression` run on commit `bd3c479634a92c2a2b00ee70d8034ff4cad0aa08` and confirm both APK and emulator jobs. If AOSP image setup fails, inspect the SDK image availability and revert that CI configuration without changing app content. Do **not** claim Android Back passes solely because static Java/JS tests pass.

### 2026-10-14 — verified Android Back and source-attributed glossary additions

- **Verified** Android 35 `google_apis` emulator run [38464879108](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38464879108): actual Glossary page launched, native system Back returned to main Quiz screen, app survived and the screenshots changed as expected. Physical Samsung/One UI operation is still **not** verified.
- The proposed AOSP `default` emulator image in runs `38465059326` and `38465259390` failed with a persistent blank WebView before any Back assertion. Reverted workflow to previously working `google_apis` image.
- Added **Reference → Quiz Mode** and **Rehwild card → Schalenwild category** native Back tests in the emulator harness, with visual transition check. These remain pending separate successful CI evidence.
- New context-supported glossary entries: `Bestaetigter Jagdaufseher` and `Erleger bruch`. Both cite directly checked class text and explicitly distinguish exact German worksheet wording from related class terminology; no current-law or historical word-origin claim is made. **137 defined / 25 pending / 162 total**.
- Evidence: `docs/CONTINUATION_20261014_ANDROID_GLOSSARY.md`. Continue the 25 pending terms only when class-file evidence is sufficient. Preserve all 867 question IDs, 77 legacy etymologies and 117 study cards and refrain from merging PR #3 before final gates.

### 2026-10-14 — CI startup and external launcher-ANR hardening

- Successful `google_apis` emulator run `38464879108` remains the latest **confirmed full pass** of Glossary page navigation + Android Back.
- Intermediate Android CI for expanded Reference / study-card Back checks sometimes failed **before navigation** due to a persistent white WebView frame or an external Pixel Launcher ANR overlay. Neither failure independently proves a problem in those Back transitions.
- CI harness now makes **one app-data-preserving cold Activity restart** after eight consecutive blank home screenshots, and retains all blank-frame failures if restart does not paint.
- Evidence artifact `11862067973` shows the external launcher ANR dialog provided both **Close app** and **Wait**. Selecting **Wait** made the popup recur immediately eight times. Harness now selects **Close app** for Pixel Launcher first (and only for that external process), then rechecks the real GHC screen. This never dismisses a GHC app ANR.
- Next validation: inspect run `38492308855` (commit `4dd54a1b23e26d9f4c8e5967fe8de0151d634a20`) and confirm original Glossary + added Reference/study-card Back paths. Do **not** conflate JS/API structural test passes with this final Android emulator gate.

### 2026-10-14 — confirmed Reference Back bug and targeted repair

- **New confirmed defect:** Android 35 run `38492014050` successfully navigated Glossary→Quiz with native Back, but Android Back from **Reference** returned to Pixel Launcher. The previous JavaScript bridge called private `view/mode` variables inside the app IIFE as though they were globals. In an `evaluateJavascript` call those globals are undefined, causing `finish()` on the root HTML page.
- **Repair:** `MainActivity.java` now programmatically clicks existing live DOM navigation controls instead of reading closure-private state; see commit `b1006b54f79fa0279988a9e7e8ae330a96f2693c`. It handles modal, card→category, category→hub, quiz-question→quiz-home, Reference/Study Hub→Quiz Mode, and preserves WebView history fallback for the separate Glossary page. App banks and saved-progress keys are unchanged.
- **Regression correction:** `scripts/test_android_back.py` now tests this JavaScript in a VM **without injecting false global view/mode bindings** (commit `950cd4aac78a941ec900451538c26fda8dfa6b63`). Static smoke checks passed; check latest full APK/emulator result, not just this unit test.
- CI emulator startup may independently fail due blank WebView and a recurring Pixel Launcher ANR; the harness retries a single cold app launch and now selects **Close app** on the external launcher's dialog instead of recurring `Wait`. Do not label a cloud-emulator startup failure a return-navigation failure.
- Follow-up: verify **native Reference→Quiz** and **Rehwild card→Schalenwild** on a full successful Android 35 run. Then do physical Galaxy S23 Ultra tests: install, offline images, progress backup/restore and updates. Comprehensive source fact checks and 25 glossary pending definitions remain separate.
- See `docs/CONTINUATION_20261014_ANDROID_GLOSSARY.md` for source-based defect reproduction and scope.

### 2026-10-14 — Reference Back verified, nested Study Mode selection and glossary batch 5

- Android 35 emulator run [38492587017](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38492587017) directly **passed** Glossary→Quiz system Back and **Reference→Quiz system Back**, with foreground and accessibility assertions. It then failed due to a **test accessibility label assumption**: the real Study Mode label is `Schalenwild 7 cards · Cloven-hoofed game ...`, not exactly `Schalenwild`. The test selector was updated to allow a label followed by descriptive text at commit `b178fe6dab19c2037c3e8e03c7234feffb4aee3d`. Check its updated CI for **Schalenwild→Rehwild→Back** before claiming that path passed.
- Direct class slides `Trophy Part 1 (2025).pdf` and `Trapping (202607).pdf` support **Pelz** (fur/pelt) and **Baum/Stein** *within* Baummarder/Steinmarder compounds; the bare words are not certified as independent hunters' animal slang. All three entries label evidence limits, and no etymology is asserted. **140 defined / 22 pending / 162 total**. Source register: `docs/GLOSSARY_DEFINITIONS_BATCH5_20261014.md`.
- The standalone APK build from the new glossary data passed [run 38494935225](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38494935225). JS/test Android regression was also updated with three more term checks and is being validated separately. No new quiz/progress IDs or data migrations introduced.

### 2026-10-14 — all three Android system Back scenarios verified

- **Complete Android 35 `google_apis` CI passed**: [run 38494758022](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38494758022) reports success for JS smoke, APK build, and emulator. Emulator logs show true native Back with rendered screenshots for **Glossary→Quiz**, **Reference→Quiz**, and **Rehwild study card→Schalenwild category**. The earlier failure at Schalenwild was due only to the test expecting an exact accessibility label instead of the combined label including description; fixed by `b178fe6dab19c2037c3e8e03c7234feffb4aee3d`.
- The subsequent three-word **official-source glossary batch** defines BVA, European Firearms Pass and Veterinäramt, explicitly marked independent authority references, not class-slide text. Details and links: `docs/GLOSSARY_OFFICIAL_TERMS_20261014.md`. **143 defined / 19 pending / 162 total**. Avoid claiming the Firearms Pass itself authorizes every border crossing.
- Standalone APK including the three new definitions **built successfully** at [run 38495167108](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38495167108). The glossary UI regression has source-specific assertions committed at `61d513a53c1732529d685b78c7553b81dc5f4703`; check that commit's full CI for latest combined validation, as it postdates the last proven Android run.
- Still no physical Galaxy S23 Ultra test (including first-run/offline media/progress restoration). Keep draft PR #3 unmerged. Question-by-question factual verification and historical etymology sources remain open.
