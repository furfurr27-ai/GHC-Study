# GHC Study source architecture

## Current Android application

- `app/src/main/assets/index.html` — recovered legacy offline application; kept intact to preserve the audited question pools and existing behavior.
- `app/src/main/assets/media/` — bundled offline photographs and illustrations.
- `app/src/main/assets/german-vocabulary-quiz.json` — vocabulary question data, grouped by subject.
- `app/src/main/assets/trophy-antler-horn-card.json` — source-reviewed trophy terminology card.
- `scripts/german_vocab_runtime.js` — vocabulary quiz controller, choices, answer feedback and persistence.
- `scripts/integrate_trophy_card.py` — deterministic APK build assembler for supplemental content.

## Editing rules

Edit vocabulary content in its JSON file, not the generated APK or the embedded question pool. Edit vocabulary UI in the dedicated JavaScript file. Edit trophy facts in the trophy JSON file. Build workflows run the assembler against the tracked HTML before Gradle packages the APK.

## Planned incremental extraction

The original HTML contains a large historical question pool and tightly coupled global JavaScript. Do not split it mechanically without browser regression tests: script execution order, global names, local storage and offline asset paths must remain stable. Extract CSS, immutable data, and navigation logic into separate tracked files in stages, verifying quiz parity, study cards, Android Back and offline images after each stage.

## Release gate

A green Gradle build proves APK packaging only. Before calling a feature working, require a browser/runtime test for its visible entry point, category selection, question display, feedback, and Back navigation. On-device validation is separate.
