# GHC Study — source-claim audit status as of 2026-10-13

This is a durable, automatically counted summary from `audit/study-card-claim-register-20261012.json` on the v1.4.6 development branch. The earlier `docs/STUDY_CARD_SOURCE_AUDIT_20261012.md` is a historical *2026-10-12 baseline*, not the current tally.

## Verified work

- **117** source-linked study cards, **816** displayed fact blocks (compound blocks may assert multiple facts).
- **508** blocks checked for direct fidelity to the text of a corresponding original course PDF.
- **308** blocks still require semantic source review, original page/diagram inspection, or a factual correction.
- Exactly **three** unsourced instructor-note Other Facts were deleted (wolf, Waldkauz eye color, Steinadler national-eagle statement), reducing the original 819 fact-block inventory to 816.
- Verified slide-deck text includes predator mammals, birds of prey, 2020 bird hunting/Federwild, hunting dogs, wild boar, deer, historic weaponry, and 2026 hunting techniques.
- Corrected the wrong Spiegel (wing patch) definition, peregrine “may exceed 300 km/h” wording, dog breed/role statements, specific boar descriptions, and historical legal framing.
- A CI parity check now compares every audit fact block against the actual source embedded in `index.html`; source changes must not silently invalidate this register.

## Course fidelity is not independent truth

- Statements tagged `checked_against_deck_text` were compared with **text extracted from a class PDF**, not checked against original slide figures or independently against live law.
- Hunting times, protected species and weapons-law rules on **2019/2020/2025** slides are not reliable as current field regulations.
- Independent official references correcting two problematic topics (wolves and raccoon family classification) are in `docs/CURRENT_LAW_SOURCE_WARNINGS_20261013.md`. Their web evidence is separate from course-slide evidence.
- All 38 listed class PDFs were originally accessible as readable text, but a claim-by-claim check has **not** been performed on all of them. Original scanned charts and images have not received a visual pass.
- The full **867-question exam answer pool** and **77 original vocabulary etymologies** are not yet comprehensively checked.

## Current per-source block status

| Source as recorded in card | Text-checked | Pending |
|---|---:|---:|
| Predatory Birds (Fall 2026).pdf | 110 | 12 |
| Bird Hunting.pdf | 101 | 3 |
| GHC Predators (Fall 2026).pdf | 96 | 1 |
| GHC Hunting Dogs (Fall 2026).pptx.pdf | 50 | 0 |
| Weapons - Overview (2020).pdf | 38 | 9 |
| Rehwild 2026.pdf | 29 | 1 |
| Hunting_Techniques_V3.1_16FEB26.pdf | 24 | 2 |
| Wildkrankheiten2_BacteriaViruses.pdf | 0 | 25 |
| Schwarzwild Updated February 2025.pdf | 22 | 1 |
| HuntingTraditions.pdf | 0 | 23 |
| Trophy Part 1 & 2 (2025); Game - Rotwild, Rehwild, Damwild, Mufflewild | 0 | 21 |
| Rotwildr_4r.pdf | 15 | 3 |
| Feldhasen (hares) & Kaninchen (rabbits) (vSRS APR 2022)edCBT.pdf | 0 | 18 |
| Sikawild 2025.pdf | 0 | 17 |
| Gamswild2c.pdf | 0 | 17 |
| Nature and animal protection feb 2019.pdf | 0 | 17 |
| Wildkrankheiten1_Parasites.pdf | 0 | 16 |
| Damwild2.pptx.pdf | 0 | 15 |
| Mufflewild 2015.pdf | 0 | 15 |
| Firearms_Range_Saftey_Overview_11FEB26_V2.0.pdf | 0 | 14 |
| Hunting Dogs (202609).pdf | 14 | 0 |
| Fuchs (fox)_Fuchs.pdf | 0 | 12 |
| Guide_08n1-5_Other_Game_2013-08.pdf; Emailing federal hunting law revised AUG 2026.pdf | 0 | 11 |
| GHC Field & Forest Class (APP 2025).pdf | 0 | 11 |
| Game - Federwild.pdf | 9 | 2 |
| Hunting Weapons and Ammunition v3.0_14FEB26.pdf | 0 | 10 |
| GHC Revier Class (v. Sep 2026).pdf | 0 | 8 |
| Wildkrankheiten1_Parasites.pdf; Wildkrankheiten2_BacteriaViruses.pdf | 0 | 7 |
| Emailing German Weapons Law vSRS 19AUG2026.pdf | 0 | 6 |
| Wildkrankheiten3_KundigePerson&Practice.pdf | 0 | 6 |
| Range - Revier (20260922).pdf | 0 | 5 |

## Highest value outstanding audits

Focus on the missing disease/parasite material (important food safety), Hunting Law / German Weapons Law (current-law divergences), trophy anatomy's original drawings, rabbits/hares, additional deer species, and the Other Game guide for Murmeltier / Seehund. Use the original deck's page-image where OCR text is insufficient.

## Glossary and Android testing

The searchable offline glossary has **162 entries**: **107** with meanings (77 original quiz meanings plus 30 directly grounded in class PDFs) and **55** intentionally pending. New meanings were not supplied with invented historical etymologies. German diacritics are restored for several terms and specific reciprocal crosslinks added.

The original quiz count remains 100 practice questions + 767 class-focused questions, plus 77 native vocabulary multiple-choice questions. APK build, DOM tests and Android 35 emulator checks have previously passed; verify the CI state of the **latest** source commit before claiming the final artifact tested. A physical Galaxy S23 Ultra upgrade and offline-progress persistence check remains pending.
