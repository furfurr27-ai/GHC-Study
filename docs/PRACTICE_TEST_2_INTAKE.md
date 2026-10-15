# Practice Test 2 — photo intake checkpoint

Last updated: 2026-10-15. This checkpoint is intentionally independent of the primary GHC Study slide audit.

## Authoritative source and staging location

- Staging branch: `feature/practice-test-2-20261015`, branched from `feature/slide-audit-glossary-tests-20261012` at its 2026-10-15 checkpoint.
- Exam intake: `app/src/main/assets/practice-test-2.json`. Modify this file, not the generated page.
- Browser page source: `scripts/practice-test2-template.html`, with the special `<!-- PRACTICE_TEST_2_DATA -->` placeholder.
- Build assembler: `scripts/build_practice_test2.py` generates the offline `assets/practice-test-2.html` page and inserts the Practice Test 2 entry into the packaged Quiz Mode homepage. Does not rewrite `window.GHC_QUESTIONS` or the 867 historical source questions.
- Regression: `scripts/check_practice_test2.py`; wired to `.github/workflows/android-standalone-apk.yml`.
- Separate saved answers: `GHC_PT2_PARTIAL_PROGRESS_V1` in localStorage. Do not reset historical quiz progress.

## Captured pages in first batch

The user uploaded 10 photographs into the conversation: cover `20261015_213803.jpg`; Part I Q1–6 `1000069478.jpg`; Part I Q7–12 `1000069479.jpg`; Part I Q13–19 `1000069480.jpg`; Part I Q20–25 `1000069481.jpg`; Part II Q1–5 `1000069482.jpg`; Part II Q6–11 `1000069483.jpg`; Part II Q12–18 `1000069484.jpg`; Part II Q19–24 `1000069485.jpg`; Part II Q25 `1000069486.jpg`. These are local conversation source filenames, not GitHub image assets; no scans or private personal details were committed.

- Part I Game Biology, questions 1–25, complete (batch 1).
- Part II Hunting Dogs / Hunting Procedures, questions 1–25, complete (batch 1).
- Part III Weapons Law, Firearms and Handling, questions 1–25, complete (batch 2).
- Part IV Nature and Animal Protection, Jagdschutz, Ethics and U.S. Forces Procedures, questions 1–25, complete (batch 2).
- Part V Diseases, Handling of Meat, Hygiene, questions 1–5 captured and staged under `pendingSections`. Questions 6–25 remain to be uploaded.
- **105 of 125 questions transcribed: 100 immediately playable across four complete sections, 5 retained pending Part V completion. Test intake remains incomplete.**
- Source year (2021 or 2022) was described by the user and is not printed/verified on the available cover.
- Cover rules: closed book; ink pen; circle one or more letter(s); 5 × 25 questions; one point per question; at least 13 correct **per part**; **150 minutes total**.
- **Correct answer method: use ONLY YELLOW HIGHLIGHTED text on photographed paper.** Blue handwritten circles, black ticks, crossings-out or other pen marks must NEVER override the highlighted key. Preserve questionable historical answers literally, with separate legal/factual caveats rather than silently correcting the primary key.
- Matching Part II question 25 is one question with six submatches, not six scored questions. Correct mapping is a→5, b→4, c→6, d→2, e→1, f→3.
- Check multi-select against highlights carefully (examples: P1 Q1 A+C; P1 Q18 B+C+D; P2 Q1 A+B+D+E; P2 Q16 A+C+D). Do not convert an "All of the above" highlight to multiple selected options; the selected answer is the highlighted single letter only.

## Next-batch procedure

1. Inspect the newly uploaded photo pages in order; identify part, question range, prompt, all answer options and yellow highlights.
2. Add only the new records to the existing `sections` array in `practice-test-2.json`. Maintain unique IDs `PT2-P{part}-Q{two-digit number}`.
3. For a partially photographed part, retain records in a separate intake note, or complete it before adding to the array: the assembler currently requires **25 questions per published part**. Do not fabricate missing questions.
4. Update `receivedQuestionCount`; retain `isComplete:false` until all five sections are present and reviewed.
5. Add the new `sourceImage` filename for traceability, validate original spelling and highlighted-only answer keys; don't add source photographs to the public repo.
6. Run assembler then `scripts/check_practice_test2.py`; check standalone APK packaging and actual device navigation separately. Do not call an APK build a Galaxy S23 Ultra device test.
7. Once all 125 questions are transcribed, implement/verify the complete **150-minute** exam mode and per-part 13/25 scoring; remove intake-preview messaging only after completing functionality and regression checks.
8. Keep the changes separate from the existing 100 Practice Test, 767 GHC Focused, 77 vocabulary, glossary, slide audit and current-law warnings. Merge this dedicated staging branch only after verifying no regressions with newer live development branch commits.

## Exact first-batch answer letters

Part I Q1–25: AC, C, A, A, B, B, AD, CD, AC, C, C, B, C, E, B, A, C, BCD, B, C, B, D, AC, E, A.

Part II Q1–24: ABDE, B, AB, C, C, B, ACD, D, C, B, B, B, B, A, B, ACD, BD, CD, D, A, B, BC, C, C. Q25 is matching a5 b4 c6 d2 e1 f3.

This is an historical-answer transcription checkpoint, **not** confirmation that the test reflects current hunting laws or species taxonomy.


## Second photo batch (10 additional images, 2026-10-15)

- `1000069487.jpg`: Part III Q1–6
- `1000069488.jpg`: Part III Q7–12
- `1000069489.jpg`: Part III Q13–18
- `1000069490.jpg`: Part III Q19–24
- `1000069491.jpg`: Part III Q25
- `1000069492.jpg`: Part IV Q1–6
- `1000069493.jpg`: Part IV Q7–13
- `1000069494.jpg`: Part IV Q14–19
- `1000069495.jpg`: Part IV Q20–25
- `1000069496.jpg`: Part V Q1–5

Exact answer letters read only from **yellow highlighting**, with blue circles and black checks ignored:

- Part III Q1–25: B, D, ABD, AB, B, A, ACDE, C, B, A, A, B, C, A, C, ACE, A, C, AB, B, C, B, A, BD, ABDEF.
- Part IV Q1–25: C, CD, B, B, B, A, B, A, AC, A, A, C, B, C, B, A, B, B, C, ABC, B, B, A, A, B.
- Part V Q1–5 (pending): B, ABC, CDE, ABE, ACE.

Key exceptions to protect from future "corrections" during transcription: Part III Q4 highlights **A+B** for universal self-defense warnings, Part III Q25 highlights **A+B+D+E+F** but not C/G, Part IV Q9 highlights **A+C** (one or three years), and Part IV Q16 highlights **A** for the injured deer outside the hunter's own hunting area. These are *historical answer-key records, not independently verified current legal advice*. The page preserves a general historical-source disclaimer. Current German law and official U.S. Forces procedures require a separate substantive audit before anyone relies on these claims.

### Resume instructions for final batch

1. Inspect the user's remaining photographs. The expected continuation starts **Part V Q6**. Do not assume that all photos start at the expected numbering—confirm printed question numbers.
2. Keep existing Part V Q1–5 verbatim unless photo-level correction is warranted.
3. Append Part V Q6–25, move the completed 25-item Part V object from `pendingSections` into `sections`, and set `pendingSections: []`.
4. Set `receivedQuestionCount=125`, `availableQuestionCount=125`, `pendingQuestionCount=0`, `isComplete=true`, and update the intake `status`.
5. Update `scripts/check_practice_test2.py` and `tests/practice-test2-smoke.cjs` to assert 125 captured and all five parts visible; replace the 105-item checkpoint assumptions. Run the available Android+browser regression workflows.
6. Implement the **full five-part timed 150-minute simulation**, with 13/25 passing **per individual part**, only after the source collection is complete. The existing partial preview intentionally has no exam timer.

