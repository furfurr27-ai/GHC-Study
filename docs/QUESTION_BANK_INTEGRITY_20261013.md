# GHC Study question-bank structural and answer-clue audit (2026-10-13)

## Scope and limitations

Checked the **867 questions actually embedded** in the v1.4.6 offline Android app source, not the abandoned 2,000-plus-question pool. The checked set consists of 100 Practice Test questions and 767 GHC Focused Hessen questions (747 single-answer and 120 multiple-answer items). Also checked that the separate 77-question Jägersprache quiz bank is present.

This is a **structural/wording audit**, not a review of whether any keyed answer, biological explanation, German law statement, or animal photo is true. Text and source metadata remain subject to the separate question-by-question course-slide audit.

## Concrete correction made

- **H2023-D19-Q042 (Weapons Law: Self-Defense)** previously stated `Jagdschein (hunting license)` in the question stem and offered **the hunting license** as correct option B. That was an answer giveaway. The stem now reads: *As a newly qualified hunter, you intend to purchase a Drilling (three-barreled combination gun), an over-under combination gun, and a double-barreled shotgun. Which document must you present to the dealer?*
- The original source answer ID remains `b`; **all choices, answer keys, explanation text, and scoring behavior are preserved**.
- An explicit JS DOM regression test prevents reintroducing the parenthetical translation.

## Automated evidence

The new `scripts/check_question_bank_integrity.py` reads shipped `window.GHC_QUESTIONS` and `window.GHC_VOCAB_QUESTIONS` directly from `app/src/main/assets/index.html`, verifies the 867/77 counts, valid answer IDs, unique choices and question IDs, single/multiple-answer consistency, nonempty stems, explanations and learning-why text, and searches for literal correct-option text repeated in stems and parenthetical hints.

At the 2026-10-13 CI check after the correction:
- **0** invalid answer references, duplicate choice texts, missing explanations, or blank stems detected.
- **0** possible parenthetical/direct answer giveaways detected by the current heuristic.
- **18** duplicate stem groups, flagged for human comparison; the question catalog was **not** silently deduplicated because the answer contexts or selection may differ.
- **491** questions have no explicit `visualRefs` or `animalVisualRefs`. This is not a count of missing photos: many questions are non-animal, and other image paths may exist. A separate animal-question visual coverage audit is required.

A successful run with the scanner and app smoke checks: https://github.com/furfurr27-ai/GHC-Study/actions/runs/38355462397

## Open work

1. Match all 867 answer keys and explanations to their actual class-deck/question-pool source records.
2. Compare the 18 same-stem groups for genuine redundant copies versus legitimate differently keyed questions; do not change pool count without explicit source comparison.
3. Determine which animal identification questions are among the 491 without explicit image refs and address true gaps with correctly sourced photos.
4. Preserve the original Jägersprache words and German/English meanings while avoiding question-stem parentheticals that directly supply a choice.
5. Check current German weapons/hunting law independently of the historical class-question explanations.

No release or physical Galaxy S23 Ultra regression has been declared complete by this structural audit.
