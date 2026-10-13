# GHC Study — next verified work

Updated: 2026-10-13

## Working branch / review
- Active changes: `feature/slide-audit-glossary-tests-20261012`.
- Comparison/review target: `audit/v145-source-recovery` (not older `main`).
- Draft pull request: https://github.com/furfurr27-ai/GHC-Study/pull/3
- Baseline source: v1.4.5. Candidate build: **v1.4.6, versionCode 146**. The main upgrade package remains `org.ghcstudy.v141`; side-by-side tester is `org.ghcstudy.v146.standalone`.

## Verified implementation
- The application has an offline `glossary.html` and `glossary-data.js` linked in navigation and Reference.
- Exactly 162 glossary entries: 107 now have meanings (77 original bank meanings plus 30 verified against original class PDF text), while 55 worksheet terms remain definition-pending. Legacy 77 etymologies are still not independently checked.
- JavaScript/DOM regression covers Quiz Mode question selection, answer/feedback, Study Mode category/card/back, Reference reset modal, glossary search/filters/crosslinks.
- Android Back bridge's existing Python regression cases pass, and a source-driven Android APK build with the glossary packaged has passed in GitHub Actions.
- The emulator job tests Android 35 installation, launch, glossary navigation and Back; consult latest workflow results before calling it passed.

## Class factual source intake
- All 38 listed GHC primary class deck PDFs were directly fetched and readable text retrieved (batch documents under `docs/`).
- Exactly 117 study cards now have 816 source-coded fact blocks after 3 unsupported non-slide notes were deleted. Claim register `audit/study-card-claim-register-20261012.json` marks **508 checked against actual class PDF text** and **308 requiring source-semantic or image/page review**. Class/text agreement is not independent current-law correctness.
- Review each of the remaining 308 pending claims directly against its original PDF. Do not promote inferred or simply numeric-matched facts to verified.
- The `Murmeltier` and `Seehund/Robbe` cards refer to an additional Other Game guide not present in the primary deck inventory (the separate hunting-law deck is available).
- Source PDFs' simple text extraction did not preserve reliable slide boundaries or all visual facts; inspect original pages and graphics.
- Correct any actual contradictions with a citation to filename/page; preserve original factual intent and separate current legal facts from historic class facts.
- The original 867 practice/Hessen questions and 77 existing vocabulary definitions were **not** comprehensively semantically audited in this pass.

## Next actions
1. Complete the 807 pending fact-block checks using original PDF page/image inspection. For each block record deck, actual page, supporting text/image, and correction if needed.
2. Verify 55 remaining worksheet-only vocabulary definitions and etymologies; never invent provenance. Review the existing 77 etymology notes separately.
3. Check Android emulator CI evidence; then install on Samsung Galaxy S23 Ultra and test login-free offline operation, saved progress backup/restore, images, Android Back, and progress persistence after update.
4. Pay attention to debug APK signing: independent GitHub Actions jobs may generate different debug keys, so users may not be able to update an existing debug installation in place. Back up saved progress before considering uninstall/reinstall; offer a side-by-side applicationId build if appropriate.
5. Only after verified functional parity and factual review should source changes be promoted into older `main`.

## New verified corrections
- Rechecked Fall 2026 predator class cards and 2026 bird-of-prey cards, dog deck, 2020 Federwild and 2025 wild boar. Corrected peregrine diving speed (up to ~300 km/h), Stockente wing Spiegel, unclear dog group names, and wild boar signs. Three unsupported instructor notes were deleted.
- Current German wolf law may permit **conditional**, strictly managed hunting although the class slide says 'no season'; this is not a general hunt authorization. The class 'small bear' raccoon description is not literal taxonomy. Primary independent references and exact limitations: `docs/CURRENT_LAW_SOURCE_WARNINGS_20261013.md`.
- Glossary now also uses restored German diacritics for source-backed terms, with reciprocal cross-references; the original 77 question-bank terms are preserved.
- Verify the most recent GitHub Actions run AFTER source changes, as successful earlier runs refer to older commits.
