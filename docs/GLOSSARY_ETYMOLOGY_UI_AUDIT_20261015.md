# Glossary etymology display and provenance audit — 2026-10-15

## Source evidence actually checked

1. Original classroom `Jaegersprache1.xlsx` (connected Google Drive, file `1wUL9LN8zys5QSPbwTUUCKli8V--qz_Kx`): 127 worksheet headwords, including `Schweiss`, `Jagdschuetz`, `Tiroler`. The `Definition/notes` column is blank for these entries. The worksheet **does not attest any proposed historical etymology**. It cannot be cited as proof of a poacher code.
2. Live development-branch `app/src/main/assets/glossary-data.js`: 162 entries; 160 with English meanings and 2 pending. Exactly 77 records `v001`–`v077` carry non-empty inherited `etymology` fields. Their common source label is the previous GHC 77-term vocabulary dataset, **not an independently reviewed historical dictionary**. All 85 `x...` entries have empty `etymology`.
3. Original classroom `Hunting Techniques (20260216).pdf`, `Range - Saftey (20260211).pdf`, and `Weapons - Ammo (20260214).pdf` (connected Drive; readable text inspected this session). No historical proof of these 77 word-origin narratives was found in the checked extracts. This is **not** a full visual/PDF-page etymology review.
4. Live `app/src/main/assets/glossary.html` and `tests/functional-smoke.cjs` directly inspected to trace how the original notes were displayed and how search/filter tests worked.

## Problem, actual correction, and limits

Previously, the glossary labeled all 77 inherited notes `Word origin / breakdown` without a per-record warning. Some entries contain plausible compositional mnemonics, some contain historical claims, and some already disclaim speculative poacher explanations. Presenting the whole field as verified historical etymology overstates available evidence.

- Retain every original word-origin string, term, meaning, cross-reference, ID, question/progress key and German/English vocabulary pair.
- Each of the 77 records now renders **Unverified inherited word-origin note**. A future independently researched record may render **Verified word origin** only if explicit `originVerification: "verified"` and nonblank `originSource` metadata are recorded. Currently **0 / 77** meet that gate.
- The live glossary summary displays the derived count of meanings available/pending and unverified origin notes; filters now say **Meaning available (source-labeled)** rather than implying all 160 are from the GHC bank.
- Removed an obsolete HTML footer claiming 30 newer definitions and 55 worksheet-only entries. That statement was inconsistent with the current 160/2 data.
- Added executable DOM regressions for all 77 warning labels, 160/2 status counts, no silent verification, and the `Schweiß` qualified note. Do not describe these tests as independently verifying etymological truth.

## Highest-value follow-up: historical origin review

Research each of `v001`–`v077` against credible etymological references (e.g., DWDS historical evidence, Duden etymological citations, Grimm/DWB when relevant) and hunting language sources. Distinguish literal modern decomposition, historical lexical derivation, hunting-specific semantic shift, and *unproven* poacher-code narratives. Record exact citations and relevant edition/page or dated URL for each verified entry, then and only then set the verification fields. Prioritize `v047 Schweiß` / `v064 Schweißhund`, `v033 Geweih`, and `v052 Bruch` by thematic relevance, not by presumed etymological truth.

Two glossary meanings **remain pending**, `x118 Jagdschuetz` and `x148 Tiroler`, because their intended course sense is ambiguous. The worksheet alone does not resolve whether those refer to a role, a dog breed, or some other contextual term. Do not guess.

## Release/test boundary

This patch changes only offline glossary presentation and browser regression expectations. No hunting facts, Android Java bridge, card media, versionCode, application ID, or persistent storage key was modified. GitHub CI must pass on the *final* test commit before treating the change as regression-validated. It still requires physical S23 Ultra acceptance testing, complete question review, 3 pending source-faithful visual replacements, and legal-source freshness review. Keep PR #3 draft and unmerged.
