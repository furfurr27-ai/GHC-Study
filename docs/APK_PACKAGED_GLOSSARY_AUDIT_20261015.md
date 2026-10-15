# GHC Study — APK-packaged glossary/provenance verification (2026-10-15)

## Why this test exists

A green source-level JSDOM test does not alone establish that the packaged Android APK contains the same glossary JavaScript, page, cross-reference IDs, original icon or offline media. This new post-assembly test directly opens the compiled APK as a ZIP and checks the shipped bytes.

## Checks performed by `scripts/check_packaged_glossary.py <apk>`

- Reads `assets/glossary-data.js`, `assets/glossary.html`, `assets/index.html`, and `res/drawable/ic_launcher.png` from the actual APK, failing if absent.
- Parses shipped `window.GHC_GLOSSARY` data and checks 162 unique IDs, original `v001`–`v077` retention, 160 defined and 2 pending term meanings (`x118` and `x148`).
- Confirms all 77 original terms still carry their old word-origin notes, while only two `v047` and `v064` carry independently documented `originVerification` / `originSource` metadata including identifiable Duden URLs.
- Checks that 75 origins remain explicitly unverified and that the shipped UI includes both provenance statuses and has no obsolete `55 worksheet-only` label.
- Produces `build/packaged-glossary-audit.json` for machine-readable CI evidence.

Both `.github/workflows/glossary-functional.yml` and `.github/workflows/android-standalone-apk.yml` now run this script **after APK assembly**. They also run `scripts/check_study_media.py --apk` to ensure that all 117 mapped study-card images resolve to actual offline assets and class-image source hashes still match where tracked. The intentionally unresolved 3 slide-style cards remain a warning in non-strict mode, not a silently hidden release pass.

This guards against stale APK source, missing glossary files, regressions in original term IDs or erroneous claims of verified origins. It **does not** establish factual correctness of all 867 exam questions, visually authenticate species/photo content, independently confirm every etymology, prove Google Drive image rights, or replace Android 35 emulator / physical Galaxy S23 Ultra interaction tests.

## Source and provenance scope

Inputs: actual development-branch glossary data, glossary HTML, earlier class-Jägersprache worksheet, media audit register, checked external dictionary sources cited in `docs/GLOSSARY_ETYMOLOGY_UI_AUDIT_20261015.md`. No original classroom imagery was replaced in this code change. Application IDs, version, card facts, answer keys, local storage IDs and Android native Back bridge remain unchanged.

Code commits: `a9be65de95f514f89917b998f41d6a251c9f9183` (new checker), `de8a349320599a93500f6e93a74567d1b8d6d0ba` (full Android workflow), `71f639851d545d140dbaaf3d2a8fc05bf27c5cce` (standalone workflow). CI workflow runs: [38672777636](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38672777636) and [38672781811](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38672781811). Their complete conclusions must be checked before claiming packaged-byte verification passed.
