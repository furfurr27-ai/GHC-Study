# Duplicate-stem review of shipped GHC exam bank (2026-10-13)

## Evidence
Read the actual v1.4.6 offline `GHC_QUESTIONS` array (100 GHC Practice Test and 767 Hessen/GHC Focused records), grouped by normalized stem and compared correct-option wording. The structural check identified **18 two-question stem groups** involving 36 records:

- **11 pairs** have the same normalized answer-choice set and the same correct-option text.
- **7 pairs** have differing choices or wording. Four of the 18 pairs had correct options worded differently but still expressed the same apparent answer on direct text comparison; these four are **not proof of legally correct answer keys**.
- Duplicate IDs were **not** detected; these are different question IDs, often deliberately preserved from different Hessen source categories. Do not remove without checking the original section and progress implications.

## Duplicate pair inventory

| Pairs | Subject | Notes |
|---|---|---|
| `P2013-S2-Q07` / `H2023-D20-Q097` | Parasites | Two different banks, different explanatory phrasing of the correct answer |
| `H2023-D04-Q075` / `H2023-D04-Q087` | Firearms proof marks | Slight correct-choice wording differences |
| `H2023-D04-Q151` / `H2023-D15-Q010` | Range supervisor | Identical choice set; awkward duplicate stem revised in both |
| `H2023-D04-Q154` / `H2023-D15-Q013` | Permission to begin shooting | Identical choices |
| `H2023-D04-Q158` / `H2023-D15-Q017` | Alcohol and shooting | Identical choices |
| `H2023-D18-Q044` / `H2023-D18-Q045` | Sport shooter documents | Identical choices |
| `H2023-D18-Q062` / `H2023-D18-Q082` | Hunter acquisition documents | Identical choices |
| `H2023-D18-Q063` / `H2023-D18-Q083` | Combination gun and WBK | Identical choices |
| `H2023-D19-Q043` / `H2023-D19-Q088` | Reporting lost firearm | Choice counts differ; correct wording agrees |
| `H2023-D19-Q046` / `H2023-D19-Q092` | Long gun quantity | Choice wording differs; correct wording agrees |
| `H2023-D19-Q055` / `H2023-D19-Q086` | Hunting documents | Multiple-answer choice lists differ but both keyed texts agree |
| `H2023-D10-Q103` / `H2023-D05-Q002` | Scaring game from land | Identical choices |
| `H2023-D10-Q107` / `H2023-D05-Q006` | Maize field damage | Same apparent answer with a longer explanatory choice |
| `H2023-D10-Q118` / `H2023-D05-Q017` | Hunting cooperative damage liability | Same apparent answer with a longer explanatory choice |
| `H2023-D10-Q121` / `H2023-D05-Q020` | Liability for hunting action | Identical choices |
| `H2023-D09-Q083` / `H2023-D15-Q003` | Live-capture traps | Identical choices; awkward duplicate stem revised in both |
| `H2023-D09-Q084` / `H2023-D15-Q004` | Permitted traps | Identical choices |
| `H2023-D09-Q089` / `H2023-D15-Q009` | Fox traps | Identical choices |

## Corrections made
- `H2023-D19-Q042`: removed the parenthetical that literally repeated its correct option, *hunting license*; **answer key remains B**.
- `H2023-D04-Q151` and `H2023-D15-Q010`: corrected *responsible person responsible for supervising ...* to *Must shooters follow the instructions of the person supervising the shooting range?*
- `H2023-D09-Q083` and `H2023-D15-Q003`: corrected *live capture, catching an animal unharmed of game* to *Which of these traps is designed to capture game alive and unharmed?*
- Other stems, choice IDs and scoring keys are unchanged. Browser regressions now check all five revised IDs.

## Unverified / next work
This is a linguistic and structural review. Confirm source answer keys and current law from the original German Hessen question catalog and relevant 2026 course slides. The 18 repeated pairs may be shown in different scopes and deliberately carry separate saved-progress IDs; silently deduplicating them would change quizzes and progress accounting.

For the automated scan, see `scripts/check_question_bank_integrity.py` and `docs/QUESTION_BANK_INTEGRITY_20261013.md`.
