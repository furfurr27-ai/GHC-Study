# GHC Study — 867-question source-audit coverage and triage (2026-10-15)

**Primary input:** The exact current GHC Study `window.GHC_QUESTIONS` JSON as assembled by the new source review overlay, not memory of prior question pools. The CI `smoke` job in [workflow 38686840738](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38686840738) read these 867 questions and generated `build/question-source-audit-matrix.json`.

## Updated CI-confirmed baseline

| Measure | Count | Meaning |
|---|---:|---|
| Examination questions | **867** | Distinct existing immutable question IDs in this app |
| Source-qualified exam explanations | **11** | Three original planning/misfire reviews, five GHC/SVLFG handling reviews, three new dated-paper storage/ballistics/transport confirmations; original paper keys untouched |
| Archival answer keys or dated-law wording now flagged | **3** | `P2013-S3-Q02` original 2013 B/C paper key omits unloading when entering a vehicle (confirmed in two paper copies, dual-scored B/C or B/C/D); `P2013-S3-Q03` 2013 car-transport checklist overstates universally mandatory modern wording; `P2013-S3-Q11` two-round-magazine restriction differs from current total-loaded-cartridge rule. The latter two have warnings before answering. No original keys rewritten |
| Question explanations NOT yet individually fact audited | **853** | No direct source review yet; must not be described as checked or correct because they exist in the app |
| Higher-priority law, firearm, ammunition, safety, disease/parasite subjects | **401** | Automated topic-keyword triage only, **not** a substantive defect finding or evidence of correct/incorrect answer |
| Other question subjects | **466** | General factual review triage |
| Have pre-existing `learningSourceRefs` labels | **100** | A text cross-reference from an earlier version; **NOT** proof that classroom slides and exact page facts were reviewed in this build |
| No pre-existing classroom `learningSourceRefs` label | **767** | More difficult to source and cross-check; not necessarily irrelevant to class |

The earlier 8 / 1 / 858 counts were confirmed in [CI run 38691013165](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38691013165). The new 11 / 3 / 853 source matrix is validated in the APK assembly workflow and requires the exact 14 reviewed question IDs; check the latest CI job logs before asserting completion of the emulator run. The automated tally does **not** certify the 853 other answers.

## Repeatable index and guardrails

`scripts/build_question_source_audit_matrix.py` reads every exam-question record from the built app, uniquely inventories original pool and `sourceRefs`, stored pre-existing classroom-source tags, originally provided `classroomSupport` labels, reviewed original evidence if present, and risk-category triage. For each question it now records one of three labels: `source_compared_explanation_qualified` (11), `source_compared_key_conflict` (3), or `not_individually_factual_audited` (853). Unresolved original bank keys are never treated as certified correct.

Both Android workflows produce this matrix from source **and from the actual APK ZIP** and upload it as a JSON artifact. The matrix is a navigation and audit ledger. It **does not certify** course/source material that has not been opened, original translations, keyed Hessen answers, up-to-date regulations, or image accuracy/permissions. A user reading the matrix can identify exactly which questions were audited and prioritize the 853 unaudited remainder.

## Next review phases

1. **401 higher-priority law, firearm and safety-related candidates**: break down by classroom deck, verify exact question IDs and keyed answers against accessible originals, and check current German/Hessen authority for changed legal requirements. Preserve historic source-bank keys, but qualify changed real-world legal rules conspicuously. Avoid wholesale rewriting.
2. **Remaining 466 general biology, nature and field topics**: use direct original classroom PDF page ranges and exact species illustrations when possible, not guessed glossary names or general internet hearsay.
3. Within both groups, prioritize **767 records without any pre-existing classroom slide cross-reference** for source-discovery work, but do not assume all are actually covered in this American GHC class. A question's current `classroomSupport` flag is metadata from a prior version, not newly verified evidence.

The first three independently qualified entries are documented in `docs/QUESTION_FACT_AUDIT_HESSEN_MISFIRE_PLANNING_20261015.md`. Five further safe-handling explanations and a confirmed original-paper mistake are in `docs/QUESTION_FACT_AUDIT_FIREARM_SAFETY_BATCH_20261015.md`. Five 2013 original-paper firearms-law questions were additionally compared with current official federal law in `docs/QUESTION_FACT_AUDIT_WEAPONS_LAW_20261015.md` (three qualified and two dated legal-wording conflicts). The disputed question displays a pre-answer warning that does not reveal the omitted option; its original key remains unchanged, and two copies of the **actual December 2013 practice-test PDF** confirm the B/C-only answer is a source-paper error, not an app transcription problem. The quiz now accepts **both** the historical B/C paper answer and the safety-complete B/C/D response, without changing the stored archival key; feedback clearly distinguishes them and a JSDOM UI test checks the alternative scoring. This is a source-grounded accommodation for one defective exam item, not authority to use the old key in the field. This creates an auditable, incremental path to the full original-slide comparison without claiming the existing question pool has been factually authenticated.

## Release status

Media-style replacement/remapping is **71/71**; both Android workflows now enforce strict media coverage and source hashes. The original source figure/photograph versus *newly authored educational schematic* distinction is preserved. Main CI workflow verification for the current question matrix and native emulator must be read from the latest Actions run; physical Samsung Galaxy S23 Ultra tests cannot be substituted by emulator results. Draft PR #3 remains unmerged.
