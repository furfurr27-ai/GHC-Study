# GHC v1.4.6 Android 35 emulator investigation — 2026-10-13

## Evidence from the completed failed run

Workflow: https://github.com/furfurr27-ai/GHC-Study/actions/runs/38413027220 (the Android app build and JS smoke tests passed; the emulator step failed).

- The emulator installed and launched `org.ghcstudy.v141`.
- The Java WebView client logged `Page finished: file:///android_asset/index.html`.
- Evidence screenshots showed **Quiz Mode**, then **Reference**, not the separate glossary page. Therefore the previous test's “Glossary” screenshot comparison was not actually checking the glossary.
- UIAutomator on the home screen reported the **Reference** button at `[616,2239][929,2400]` and the **Glossary** link at `[926,2239][1080,2289]`. The former script tapped `W*7/8, H-95`, which is at `945,2305` for a 1080×2400 screen: too low for the link and it activated Reference.
- From that Reference screen, system Back caused the launcher to gain focus. Whether the defect is native Back dispatch, JS evaluation, or an emulator-specific transition is still **undetermined**; the earlier test does not establish glossary-history navigation.
- The screenshot was no longer blank in this run, though a still-earlier run showed a white WebView. Rendering failures and Back navigation failures are separate observations.

## Corrective instrumentation and test change

- `MainActivity.java` now logs WebView page start/finish, resource errors and JS console messages.
- `tests/android-emulator-smoke.sh` collects logcat, WebView provider, activity and window state when a test fails (CI uploads these in `GHC-emulator-functional-evidence`).
- The test now locates the Glossary link from UIAutomator bounds instead of tapping a hardcoded region, confirms glossary page content, then presses system Back and requires the app to remain foreground.
- Latest test commit: `38e6e1b07b217bbdfde7cf61e0e1bf8d0a94b6b7`. **Do not claim pass until its own workflow completes.**

## Still required

1. Verify the corrected real-glossary page-navigation/Back run to completion.
2. Independently test system Back from **Reference to previous tab** and from **Study card to category**, rather than assuming success from the glossary test alone.
3. Install the standalone APK on a Galaxy S23 Ultra for offline images, progress persistence/backup/restore and Back.
4. No code or CI result here verifies physical device behavior.
