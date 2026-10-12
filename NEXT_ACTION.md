# GHC Study — next verified work

Updated: 2026-10-12

## Working branch / review
- Active changes: `feature/slide-audit-glossary-tests-20261012`.
- Comparison/review target: `audit/v145-source-recovery` (not older `main`).
- Draft pull request: https://github.com/furfurr27-ai/GHC-Study/pull/3
- This remains based on v1.4.5, Android applicationId `org.ghcstudy.v141`, versionCode 145.

## Verified implementation
- The application has an offline `glossary.html` and `glossary-data.js` linked in navigation and Reference.
- Exactly 162 glossary entries: 77 existing meaning/etymology entries, 85 source-worksheet terms flagged as definition pending.
- JavaScript/DOM regression covers Quiz Mode question selection, answer/feedback, Study Mode category/card/back, Reference reset modal, glossary search/filters/crosslinks.
- Android Back bridge's existing Python regression cases pass, and a source-driven Android APK build with the glossary packaged has passed in GitHub Actions.
- The emulator job tests Android 35 installation, launch, glossary navigation and Back; consult latest workflow results before calling it passed.

## Class factual source intake
- All 38 listed GHC primary class deck PDFs were directly fetched and readable text retrieved (batch documents under `docs/`).
- Exactly 117 study cards have 819 source-coded fact blocks; the register `audit/study-card-claim-register-20261012.json` explicitly marks 12 blocks checked against slides and **807 requiring semantic/page-level verification**.
- Review each pending claim directly against its original PDF. Do not promote inferred or simply numeric-matched facts to verified.
- The `Murmeltier` and `Seehund/Robbe` cards refer to an additional Other Game guide not present in the primary deck inventory (the separate hunting-law deck is available).
- Source PDFs' simple text extraction did not preserve reliable slide boundaries or all visual facts; inspect original pages and graphics.
- Correct any actual contradictions with a citation to filename/page; preserve original factual intent and separate current legal facts from historic class facts.
- The original 867 practice/Hessen questions and 77 existing vocabulary definitions were **not** comprehensively semantically audited in this pass.

## Next actions
1. Complete the 807 pending fact-block checks using original PDF page/image inspection. For each block record deck, actual page, supporting text/image, and correction if needed.
2. Verify 85 worksheet-only vocabulary definitions and etymologies; never invent provenance. Review the existing 77 etymology notes separately.
3. Check Android emulator CI evidence; then install on Samsung Galaxy S23 Ultra and test login-free offline operation, saved progress backup/restore, images, Android Back, and progress persistence after update.
4. Pay attention to debug APK signing: independent GitHub Actions jobs may generate different debug keys, so users may not be able to update an existing debug installation in place. Back up saved progress before considering uninstall/reinstall; offer a side-by-side applicationId build if appropriate.
5. Only after verified functional parity and factual review should source changes be promoted into older `main`.
