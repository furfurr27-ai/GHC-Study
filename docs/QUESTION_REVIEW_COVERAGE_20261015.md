# GHC Study — 867-question source-audit coverage and triage (2026-10-15)

**Primary input:** The exact current GHC Study `window.GHC_QUESTIONS` JSON as assembled by the new source review overlay, not memory of prior question pools. The CI `smoke` job in [workflow 38686840738](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38686840738) read these 867 questions and generated `build/question-source-audit-matrix.json`.

## Updated CI-confirmed baseline

| Measure | Count | Meaning |
|---|---:|---|
| Examination questions | **867** | Distinct existing immutable question IDs in this app |
| Source-qualified exam explanations | **8** | Three first-batch reviews, plus five new safety-handling reviews; original source keys and texts are preserved |
| Archival answer keys now explicitly disputed after primary-source review | **1** | `P2013-S3-Q02` original 19 December 2013 practice-test PDF answer key (two independently checked Drive copies) explicitly prints B/C, omitting car unloading option D; verified original-paper error versus present SVLFG safety guidance, flagged before grading while preserving the archival answer |
| Question explanations NOT yet individually fact audited | **858** | No direct source review yet; must not be described as checked or correct because they exist in the app |
| Higher-priority law, firearm, ammunition, safety, disease/parasite subjects | **401** | Automated topic-keyword triage only, **not** a substantive defect finding or evidence of correct/incorrect answer |
| Other question subjects | **466** | General factual review triage |
| Have pre-existing `learningSourceRefs` labels | **100** | A text cross-reference from an earlier version; **NOT** proof that classroom slides and exact page facts were reviewed in this build |
| No pre-existing classroom `learningSourceRefs` label | **767** | More difficult to source and cross-check; not necessarily irrelevant to class |

The revised 8 / 1 / 858 counts were **read back from the source assembly smoke job** in [workflow 38691013165](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38691013165), and must also be verified from the final packaged APK run before calling that release complete. The earlier 3 / 864 counts were confirmed from job 38686840738.

## Repeatable index and guardrails

`scripts/build_question_source_audit_matrix.py` reads every exam-question record from the built app, uniquely inventories original pool and `sourceRefs`, stored pre-existing classroom-source tags, originally provided `classroomSupport` labels, reviewed original evidence if present, and risk-category triage. For each question it now records one of three labels: `source_compared_explanation_qualified` (8), `source_compared_key_conflict` (1), or `not_individually_factual_audited` (858). Unresolved original bank keys are never treated as certified correct.

Both Android workflows produce this matrix from source **and from the actual APK ZIP** and upload it as a JSON artifact. The matrix is a navigation and audit ledger. It **does not certify** course/source material that has not been opened, original translations, keyed Hessen answers, up-to-date regulations, or image accuracy/permissions. A user reading the matrix can identify exactly which questions were audited and prioritize the 858 unaudited remainder.

## Next review phases

1. **401 higher-priority law, firearm and safety-related candidates**: break down by classroom deck, verify exact question IDs and keyed answers against accessible originals, and check current German/Hessen authority for changed legal requirements. Preserve historic source-bank keys, but qualify changed real-world legal rules conspicuously. Avoid wholesale rewriting.
2. **Remaining 466 general biology, nature and field topics**: use direct original classroom PDF page ranges and exact species illustrations when possible, not guessed glossary names or general internet hearsay.
3. Within both groups, prioritize **767 records without any pre-existing classroom slide cross-reference** for source-discovery work, but do not assume all are actually covered in this American GHC class. A question's current `classroomSupport` flag is metadata from a prior version, not newly verified evidence.

The first three independently qualified entries are documented in `docs/QUESTION_FACT_AUDIT_HESSEN_MISFIRE_PLANNING_20261015.md`. Five additional source-qualified safety items and **one unresolved archival key conflict** are documented in `docs/QUESTION_FACT_AUDIT_FIREARM_SAFETY_BATCH_20261015.md`. The disputed question displays a pre-answer warning that does not reveal the omitted option; its original key remains unchanged, and two copies of the **actual December 2013 practice-test PDF** confirm the B/C-only answer is a source-paper error, not an app transcription problem. Historical scoring is still in force for this item; a safe dual-key or unscored review workflow needs explicit engineering before treating that quiz item as an authoritative assessment. This creates an auditable, incremental path to the full original-slide comparison without claiming the existing question pool has been factually authenticated.

## Release status

Media-style replacement/remapping is **71/71**; both Android workflows now enforce strict media coverage and source hashes. The original source figure/photograph versus *newly authored educational schematic* distinction is preserved. Main CI workflow verification for the current question matrix and native emulator must be read from the latest Actions run; physical Samsung Galaxy S23 Ultra tests cannot be substituted by emulator results. Draft PR #3 remains unmerged.
