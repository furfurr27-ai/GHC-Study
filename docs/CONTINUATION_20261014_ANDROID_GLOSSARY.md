# GHC Study — glossary batch 4 and Android Back checkpoint (2026-10-14)

## Glossary: two context-supported worksheet terms

Two entries from `Jägersprache1.xlsx` were matched against readable class-PDF passages **without silently representing the exact worksheet words as quoted slide definitions**.

| Worksheet headword | Meaning recorded | Directly inspected class deck | Provenance limit |
|---|---|---|---|
| `Bestaetigter Jagdaufseher` | Appointed/confirmed hunting supervisor (warden) | `Range - Revier (20260922).pdf` identifies *Jagdaufseher* as an “appointed or designated supervisor” | The deck does **not** establish statutory requirements, privileges, or the formal legal meaning of *bestätigt*. The worksheet supplies this longer phrase. |
| `Erleger bruch` | Shooter's branch — an honor sprig associated with harvested game | `History - Traditions.pdf` describes *Schützenbruch (Shooter’s Branch)* for cloven-hoofed game, customary presentation and placement on right side of hat | The class deck explicitly names *Schützenbruch*, **not** the worksheet-spaced headword *Erleger bruch*. It is contextual correspondence, not direct class translation. |

Both entries retain blank etymologies; no unverified story about poachers or deliberate linguistic concealment has been introduced.

**Glossary count:** 162 indexed, **137 defined and 25 pending**.

## Android 35 verification evidence

- Successful [GitHub Actions run 38464879108](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38464879108) completed JS smoke tests, Android APK build, true offline Glossary navigation, and system Back to the Quiz Mode home screen on the **Android 35 `google_apis` emulator**. Its log states both the foreground/process and screenshot-change checks passed. This is verified emulator behavior, **not** a physical Galaxy S23 Ultra installation.
- Later `default`/AOSP system-image runs [38465059326](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38465059326) and [38465259390](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38465259390) installed and started the app, but the WebView stayed white throughout their startup checks; they never reached navigation. This is an emulator image/runtime regression, not proof Android system Back failed.
- Restored the `google_apis` image in workflow at commit `a96ddad89731ccb07b26e38f666c343c56c7e1c6`.
- Added separate emulator checks to tap **Reference**, invoke native Back and verify Quiz Mode; then tap **Study Mode → Schalenwild → Rehwild**, invoke native Back and check the category screen and screenshot transition. Current test code at `951e951230d0dc255c66718406f0d406b314c74f`. Those expanded scenarios remain pending their latest CI result; do not conflate them with already proven Glossary Back.

## Other unchanged source-audit gates

117 study cards; 814 display blocks, 803 text-compared against assigned class PDFs, 11 historical-guide-only exceptions; 867 question items structurally inspected, factual explanations and legacy word origins still require independent checking. Current German hunting/weapon law and figure-only slide evidence remain separate checks.

### Sources actually checked this turn

- Live GitHub PR #3, `NEXT_ACTION.md`, CI run logs 38464879108, 38465059326, 38465259390 and their job statuses.
- Connected class `Range - Revier (20260922).pdf` and `History - Traditions.pdf` extracted text for new glossary entries.
- Locally inspected original app HTML inside a previously compiled Android APK for the actual Study Mode category/card navigation code, without modifying the authoritative source HTML.

No field device, figure-only slide, or current legal corpus was independently validated.

## Confirmed Android Back defect and code correction

In full Android 35 emulator run [38492014050](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38492014050), opening Reference succeeded, but pressing Android system Back exited to Pixel Launcher. This is a **confirmed within-app navigation defect** and is separate from occasional launch-blank or launcher-ANR CI failures.

Cause directly confirmed by comparing source: `index.html` defines `var view, mode` inside its startup IIFE, not on `window`. Earlier `MainActivity.navigateBack()` called `evaluateJavascript` and attempted to access these variables and functions as globals, received `error`, and fell through to `finish()` when WebView had no page history.

Fix committed at `b1006b54f79fa0279988a9e7e8ae330a96f2693c`: instead of accessing private state, JavaScript uses the existing app DOM controls with bound handlers: `#studyCatBack` (card → category), `#studyHubBack` (category → hub), `[data-action=home]` (quiz question → quiz home), active navigation tab + `[data-tab=study]` (Study Mode hub/Reference → Quiz Mode), and `#closeModal` (modal dismissal). A separately loaded glossary continues to use WebView history. No question bank, progress keys, or study-card data were changed.

Regression `scripts/test_android_back.py` was rewritten at `950cd4aac78a941ec900451538c26fda8dfa6b63` to **not expose app IIFE variables as globals** in its mock and instead simulate the actual DOM controls. Prior mock passed a broken implementation because it incorrectly injected global `view/mode` into the testing environment.

The new native code must still pass CI and the expanded Android emulator run. This note does **not** claim the current build has passed Reference or card Back on Android hardware or the user's Samsung handset.
