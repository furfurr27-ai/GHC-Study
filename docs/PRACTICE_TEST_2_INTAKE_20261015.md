# Practice Test 2 — photographed 2021/22 U.S. Forces exam intake (2026-10-15)

## Final checkpoint: five of five parts received

**Status:** The original 125-question photographed practice paper is fully transcribed (25 questions in each of five sections). The user supplied 24 total images: the cover plus 23 question pages, across three uploads. The final four photographs complete Part V Q6–25. All choices remain keyed solely from yellow highlights. The historical document's exact year remains unverified.

Part III — Weapons Law, Firearms and Handling: `app/src/main/assets/practice-test-2-part3.json`, Q1–25; source photos `1000069487.jpg` through `1000069491.jpg`.

Part IV — Nature and Animal Protection, Jagdschutz, Ethics, U.S. Forces Procedures: `practice-test-2-part4.json`, Q1–25; sources `1000069492.jpg` through `1000069495.jpg`.

Part V — Diseases, Handling of Meat, Hygiene: `practice-test-2-part5.json`, Q1–25; source photos `1000069496.jpg` (Q1–5), `1000069497.jpg` (Q6–11), `1000069499.jpg` (Q12–17), `1000069500.jpg` (Q18–22), `1000069501.jpg` (Q23–25).

**Part III answers Q1–25**: B, D, ABD, AB, B, A, ACDE, C, B, A, A, B, C, A, C, ACE, A, C, AB, B, C, B, A, BD, ABDEF.

**Part IV answers Q1–25**: C, CD, B, B, B, A, B, A, AC, A, A, C, B, C, B, A, B, B, C, ABC, B, B, A, A, B.

**Part V answers Q1–25**: B, ABC, CDE, ABE, ACE, B, A, AB, B, ABD, A, D, ABE, BD, A, A, B, ABD, A, C, A, ABC, E, CD, BCD.

**Important highlighted/pen disagreements:** Part V Q6 **B** (not circled C), Q9 **B** (not circled C), Q16 **A** (not circled B), Q18 **ABD** (not E), Q19 **A** (not circled C), Q20 **C** (not circled B), Q24 **CD**, Q25 **BCD**. The highlighted historical keys for Part III Q4 and Part IV Q16 are retained as source evidence, **not current German legal instruction**. Part V Q20's printed key about washing digestive contamination from a carcass is a source transcription, **not independently validated food-safety guidance**.

The active development branch `feature/slide-audit-glossary-tests-20261012` now stores five per-part JSON files, and `scripts/integrate_practice_test_2.py` assembles **125 unique Practice Test 2 records** in the native Quiz Mode source without rewriting the original 867-question exam pool. `tests/practice-test-2-smoke.cjs` checks all five-part availability, multi-select, matching and progress preservation. The native quiz has instant feedback and no 150-minute countdown yet. An isolated full-exam controller with countdown, score by part, timeout and persistence was separately developed and tested on `feature/practice-test-2-20261015`; that branch was **not merged** because concurrent development created a different native Quiz Mode architecture. Do not blindly merge branches or duplicate the Practice Test 2 selector.

This appendix supersedes the initial partial-intake counts and instructions below.

## Source fidelity and paper rules

- User provided ten images: one U.S. Forces Hunting Examination cover and nine subsequent question pages.
- Paper year reported by user as approximately 2021 or 2022, but year was not printed on these pages and is not independently verified.
- Original cover: closed-book examination; use an ink pen; circle answer **letter or letters**; **5 parts**, **25 questions each** (125 total); **1 point per question**; **minimum 13 correct in each part**; total **150 minutes**.
- **Authoritative transcription key for this bank = YELLOW HIGHLIGHTS ONLY.** Blue circles, handwritten ticks/crosses, answer choices that sound factually plausible, and current scientific/legal research are NOT substituted for the highlighted key.
- Original photographs are **not** checked into the public repository. The transcriptions include source photo names for auditing.
- Historical exam responses must not be represented as independent current German hunting-law, firearm-safety, animal-welfare, or biological facts.
- The app is currently an **untimed drill**, not a 150-minute locked exam simulator. For this batch, Parts III–V remain unavailable until supplied.

## Committed data

- `app/src/main/assets/practice-test-2-part1.json`: **25** Game Biology items; `P2022-S1-Q01` to `P2022-S1-Q25`.
- `app/src/main/assets/practice-test-2-part2.json`: **25** Hunting Dogs / Hunting Procedures items; `P2022-S2-Q01` to `P2022-S2-Q25`.
- `scripts/integrate_practice_test_2.py`: guarded, build-time assembly; new `practice2022` source, independent mastery/progress, available-part scopes, info popup, matching-answer UI, and selective reset.
- `tests/practice-test-2-smoke.cjs`: checks 50 imported records, multi-select fidelity, existing 867 question records intact, new bank selector/info/part scope, answer feedback, six-pair matching, and reset menu.
- The full legacy `window.GHC_QUESTIONS` still contains **867** question records; `window.GHC_VOCAB_QUESTIONS` still contains **77**. The new `window.GHC_PRACTICE2_QUESTIONS` is an independent array. Source IDs and saved progress of existing banks are unchanged.
- Source `app/src/main/assets/index.html` remains the 2.8 MB historical base. CI applies `scripts/integrate_practice_test_2.py` **after existing source-audit overlays** and **before tests/APK packaging**. Do not mistake base HTML for final assembled APK.

## Yellow-highlighted answer key

Part I (Game Biology):
`1 AC; 2 C; 3 A; 4 A; 5 B; 6 B; 7 AD; 8 CD; 9 AC; 10 C; 11 C; 12 B; 13 C; 14 E; 15 B; 16 A; 17 C; 18 BCD; 19 B; 20 C; 21 B; 22 D; 23 AC; 24 E; 25 A.`

Part II (Hunting Dogs / Procedures):
`1 ABDE; 2 B; 3 AB; 4 C; 5 C; 6 B; 7 ACD; 8 D; 9 C; 10 B; 11 B; 12 B; 13 B; 14 A; 15 B; 16 ACD; 17 BD; 18 CD; 19 D; 20 A; 21 B; 22 BC; 23 C; 24 C; 25 MATCHING (a→5, b→4, c→6, d→2, e→1, f→3).`

**Matching Q25** remains one scored question; all six of the original pairs must be selected correctly. Do not split it into six separately scored questions or reveal the pairs in the prompt.

## Verification and state

- Existing development branch: `feature/slide-audit-glossary-tests-20261012` (draft PR #3); default `main` is **not** edited or merged.
- Standalone GitHub Actions run [#38800047487](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38800047487) succeeded with integration and APK build.
- GitHub Actions functional **smoke job** in run [#38800047286](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38800047286) succeeded with new Practice Test 2 DOM test. Whole workflow includes Android build/emulator and must be assessed separately before claiming full-device verification.
- Physical Samsung Galaxy S23 Ultra installation/upgrade is not yet tested.

## Archived next-batch instructions (superseded)

1. Inspect new uploads one photographed page at a time; preserve every question, all options and all *yellow* correct selections. Validate multiple correct selections, all-of-the-above choices, and any novel response formats.
2. Add Part III as `app/src/main/assets/practice-test-2-part3.json` with stable IDs `P2022-S3-Q01..Q25` and matching metadata and `answerBasis="yellow-highlight-only"`; subsequent batches use `part4.json` and `part5.json`.
3. Advance the intake guard in `scripts/integrate_practice_test_2.py` (currently explicitly asserts 50 for Parts I and II); support complete 25-question additional sections without accepting incomplete/duplicate ones. Update partial-progress source/information copy and smoke test counts.
4. Re-run both functional and Android standalone workflows on the development branch. Verify new matched answers and no changes to 867 legacy GHC question IDs, explanations, keys, 77 vocabulary entries, 117 study cards, Android Back support, or offline visual media.
5. Do not upload the original scans into the public repository unless user explicitly wants them made public. Keep printed historical answers separate from verified modern law.
