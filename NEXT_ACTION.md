# GHC Study — verified continuation handoff

Updated: 2026-10-13. Live source of truth: `feature/slide-audit-glossary-tests-20261012` (draft PR #3 to `audit/v145-source-recovery`). Do **not** restart or overwrite the older `main` branch.

## Build and app invariants

- v1.4.6, versionCode 146; SDK 35 target/compile, minSdk 24; primary app ID `org.ghcstudy.v141`; side-by-side test app ID `org.ghcstudy.v146.standalone`.
- Maintain 100 practice questions, 767 GHC-focused (Direct/Related) questions, 77 vocabulary quiz questions, 117 study cards, and the 162-term Jägersprache glossary (118 with meanings / 44 pending; two meanings from a historical 2013 course guide, not 2026 class slides).
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
