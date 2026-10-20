# Restoration of full GHC Study progress — 2026-10-20

## Incident
Source release v1.4.7 on main was built from v1.4.5 binary extraction and silently omitted newer October 12–15 work. A green CI build did not catch the loss because it checked only the old APK assets and new matrix. User reported Practice Test 2 missing.

## Actually checked
- Github branch `feature/slide-audit-glossary-tests-20261012`, tip `7b31eeca499b4b275949e1550f9f9239963b573d`.
- Separate optional timed-exam branch `feature/practice-test-2-20261015`, tip `8d85669356e39222f1f2c7c57775de1a593eb402`.
- Old main tip before recovery `ebfeb60cb2f169662057ef5f1f86e5b00e3a9506`.
- Original native Quiz Mode practice test scripts and source intake `docs/PRACTICE_TEST_2_INTAKE_20261015.md`.

## New release design
Git tree starts with the audited **latest native development** tree, not v1.4.5 APK. Full media and source files remain tracked; 125 Practice Test 2 questions are added by `scripts/integrate_practice_test_2.py` after the original safety/course overlays. The main-only Schalenwild JS/CSS and injector are copied in and loaded afterward. Full Android workflow is restored with separate smoke, APK and emulator jobs, new matrix regression, and a gate that inspects the actual finished APK for all 125 native questions and glossary/matrix/icon files.

Original package ID `org.ghcstudy.v141` retained. Android code 148/name 1.4.8. Optional standalone ID `org.ghcstudy.v146.standalone` retained for continuity of prior standalone progress. The separate timed 150-minute exam was not forced into the native Quiz Mode because the source branches intentionally used different UI/storage architecture.

## Acceptance gates
1. Workflow source-syntax and full existing UI tests; all five paper parts exactly 25 each, matching one scored item, 867 legacy questions unchanged, 77 vocabulary retained.
2. Study media audit, factual warning text, Android system Back, glossary layout, and navigation verified.
3. Matrix JS/CSS loaded and three tabs working; original app media and icon preserved.
4. APK packaged test directly inspects 125 native-question JSON records and glossary/matrix assets.
5. Emulator workflow passes and user tests original package on Galaxy S23 Ultra, including export/import of prior progress before any uninstall.

Historical photographed keys and dated legal/safety/animal-product practices remain explicitly marked as historical source evidence, not modern professional guidance. The 2013 safety-question contested answer remains flagged.

**CI verdict**: consult actual recovery workflow run and artifact for this commit. This note does not claim tests passed before results are returned.
