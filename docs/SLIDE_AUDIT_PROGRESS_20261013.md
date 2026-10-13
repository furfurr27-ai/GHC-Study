# GHC Study — live course-source audit checkpoint (2026-10-13)

This document replaces outdated numeric handoffs. Values are derived from `audit/study-card-claim-register-20261012.json` on the v1.4.6 feature branch.

## Exact current source-audit tally

- **117 study cards**, **814 displayed fact blocks** (original inventory 819; 5 unsupported/editorial blocks removed).
- **803** blocks checked against text from the original GHC course PDFs, with source/provenance notes recorded in the claim register.
- **11** blocks not verified against original class slides: 6 Murmeltier and 5 Seehund / Robbe blocks. All 11 have now been compared with the **2013 U.S. Forces Other Game course guide**, separately identified as historical source evidence; 2 are only partially supported by its text.
- The remaining 11 are **not** reclassified as verified class-slide evidence simply because the historical course guide contains similar information.

## Corrections made on this checkpoint

- Rehwild / Rotwild: removed the unsupported word *ruminant* from the class-fact rows because the assigned species decks state native, Niederwild/Hochwild, and cloven-hoofed but do not explicitly state ruminant.
- Rotwild: replaced the broad food summary with the course's season-by-season foods and replaced the generic management claim with the directly stated Treibjagd / Abschussplan relationship.
- Schwarzwild: clarified that night-hunting optics and Kirrung feeding limits are course subjects while contemporary restrictions must be separately checked.
- Wolf: removed a repeated editorial/legal disclaimer from Details. The remaining status statement is framed as what the **Fall 2026 slide** says, not a standing legal authorization.
- Trophy Anatomy: removed an editorial statement about missing CIC scoring thresholds that was not itself a class-slide fact.
- Earlier work removed three unsupported instructor-note blocks (wolf, Waldkauz eye color, Steinadler national-eagle statement).

## Audit categories are intentionally different

**Class-slide text checked** is a source-fidelity claim, not confirmation of current German law, biological accuracy, or inspection of graphics. Multiple underlying assertions can occur in a single fact block. An OCR/text match to a deck never proves that the cited page number or picture was verified.

**Historical guide reviewed** means direct textual comparison with `Guide_08n1-5_Other_Game_2013-08.pdf`, section `08m(1)-1` (Murmeltier) or `08m(1)-2` (Robben). The original historical guide is accessible in the connected Drive library. Its 2013 no-season statements are explicitly historical and must not be used for modern hunting decisions.

**Pending class-slide verification** applies to the 11 historical-guide-only fact blocks. These cards may require a clear separate *historical course-guide reference* classification if the project continues to require class slides exclusively for Details and Other Facts.

## By source as recorded in study cards

| Study-card source | Class-PDF text checked | Pending class-slide verification |
|---|---:|---:|
| Guide_08n1-5_Other_Game_2013-08.pdf; Emailing federal hunting law revised AUG 2026.pdf | 0 | 11 |
| Predatory Birds (Fall 2026).pdf | 122 | 0 |
| Bird Hunting.pdf | 104 | 0 |
| GHC Predators (Fall 2026).pdf | 96 | 0 |
| GHC Hunting Dogs (Fall 2026).pptx.pdf | 50 | 0 |
| Weapons - Overview (2020).pdf | 47 | 0 |
| Rehwild 2026.pdf | 30 | 0 |
| Hunting_Techniques_V3.1_16FEB26.pdf | 26 | 0 |
| Wildkrankheiten2_BacteriaViruses.pdf | 25 | 0 |
| Schwarzwild Updated February 2025.pdf | 23 | 0 |
| HuntingTraditions.pdf | 23 | 0 |
| Trophy Part 1 & 2 (2025); Game - Rotwild, Rehwild, Damwild, Mufflewild | 20 | 0 |
| Rotwildr_4r.pdf | 18 | 0 |
| Feldhasen (hares) & Kaninchen (rabbits) (vSRS APR 2022)edCBT.pdf | 18 | 0 |
| Sikawild 2025.pdf | 17 | 0 |
| Gamswild2c.pdf | 17 | 0 |
| Nature and animal protection feb 2019.pdf | 17 | 0 |
| Wildkrankheiten1_Parasites.pdf | 16 | 0 |
| Damwild2.pptx.pdf | 15 | 0 |
| Mufflewild 2015.pdf | 15 | 0 |
| Firearms_Range_Saftey_Overview_11FEB26_V2.0.pdf | 14 | 0 |
| Hunting Dogs (202609).pdf | 14 | 0 |
| Fuchs (fox)_Fuchs.pdf | 12 | 0 |
| GHC Field & Forest Class (APP 2025).pdf | 11 | 0 |
| Game - Federwild.pdf | 11 | 0 |
| Hunting Weapons and Ammunition v3.0_14FEB26.pdf | 10 | 0 |
| GHC Revier Class (v. Sep 2026).pdf | 8 | 0 |
| Wildkrankheiten1_Parasites.pdf; Wildkrankheiten2_BacteriaViruses.pdf | 7 | 0 |
| Emailing German Weapons Law vSRS 19AUG2026.pdf | 6 | 0 |
| Wildkrankheiten3_KundigePerson&Practice.pdf | 6 | 0 |
| Range - Revier (20260922).pdf | 5 | 0 |

## Jägersprache glossary source status

The searchable offline glossary contains **162 terms**, with **133 defined and 29 pending**. Definitions comprise 77 original question-bank glosses (legacy etymologies not independently reverified), 48 additional source-context-supported terms, and two historical guide terms: **Affe** (young marmot; plural *Affen* in the old guide) and **Katz** (female marmot; *Katze* in the guide). The **Bär** entry retains its ordinary 'bear' meaning and adds the separate older-course 'male marmot' sense, all linked to Murmeltier. These historical senses do not claim a verified 2026 class-slide origin.

## Remaining engineering and factual gates

1. Build and regression on the **latest commit**, including source/claim-register parity, quiz and glossary, Android Back, launcher icon and media.
2. Visual inspection of original PDF diagrams and slide pages where image-only facts determine identification.
3. Independent audit of all 867 question explanations and 77 legacy vocabulary etymology notes. These are **not** covered by study-card block counts.
4. Physical Samsung Galaxy S23 Ultra installation/upgrade, offline study images, progress backup/restore and Back/navigation testing.
5. Verify current hunting and weapons law separately from the class slide statements.

**Important:** Three legacy issue categories must not be conflated: source-text fidelity; source illustration fidelity; current legal accuracy.

### Glossary continuation (2026-10-13)

Nine further terms mapped from the worksheet to class-deck evidence (Brucellose, Schweinepest, Fuchsbandwurm, Kleiner Münsterländer, Hahn in Ruh, Untere Jagdbehörde, Jagdschein, Wiederkäuer, Frettieren). Now **127 defined / 35 pending**. Contextual rather than verbatim slide-word confirmations are specifically identified in `glossary-data.js` and `docs/GLOSSARY_DEFINITIONS_BATCH_20261013.md`. The original 77 word origins were not independently reviewed.

### Second glossary batch (2026-10-13)

Six further worksheet terms now have source-attributed definitions (Absehen, Kugelfang, Objektiv, Okular, Streckeplatz and Visier). **133 defined / 29 pending**. The one direct bilingual match is Kugelfang; five others are distinguished as worksheet-to-English-slide contextual equivalents. The separate historical origins have not been validated. See `docs/GLOSSARY_DEFINITIONS_BATCH2_20261013.md`.
