# GHC Study — Second source-comparison batch: six firearm-handling questions (15 October 2026)

## Provenance of evidence inspected

**Original connected GHC course PDFs directly retrieved in this continuation (readable text):**

1. **`Weapons - Ammo (20260214).pdf`** (connected Google Drive file ID `1aO-ftzIXRw6acqMYlpb71ZG7nV8hZ1Mp`): near its final `SAFETY` sections, directly states `Do NOT rely on mechanical safety`, `Always unload when not actively hunting`, `Always point the gun in a safe direction`, `Treat every firearm as if it is loaded`, `DO NOT ASCEND OR DESCEND WITH A LOADED FIREARM`, and `Obey the rules of the hunt … Load and unload when told`. For drive hunts, loading directions come from the forester/guide's briefing.
2. **`Range - Saftey (20260211).pdf`** (connected ID `1tjfFeqn-1lEAy_7FEsn-gL_LOKlLr9Oq`): under `SHOOTING RULES` specifically requires muzzle awareness, keeping rifle pointed horizontally downrange on the supervised range, never turning and sweeping the muzzle over people, and keeping finger off trigger until the shot.
3. **`Hunting Techniques (20260216).pdf`** (connected ID `1vPg5rBBS_0MOmnRgLK_hLtPQ1Y037cRy`): Jagdleiter's drive-hunt brief covers `open` game, hunting safety, assigned groups and stands, start and stop times/signals.
4. **SVLFG (Sozialversicherung für Landwirtschaft, Forsten und Gartenbau)**, official hunting accident-prevention information [`Sicheres Jagdwesen`](https://www.svlfg.de/sichere-jagd), current page retrieved in October 2026. Specifically its VSG 4.4 overview states (i) guns only loaded during actual hunting, (ii) muzzle always pointed safely whether loaded or not, (iii) firearms unloaded before entering/exiting cars and during vehicle travel, even within a hunting district, and (iv) chamber unloaded before climbing high seats or crossing obstacles. Source section `Ausübung der Jagd`, `Sicherheit beim Fahrzeuggebrauch`, `Sicheres Jagen vom Hochsitz`. **SVLFG is an external official current safety reference, not an original GHC classroom slide.**

**Exact original exam-question IDs, stems, choices and answer letters** were read from live GitHub bank `window.GHC_QUESTIONS` (867 unique IDs); the 2013 paper key was **not separately recovered from a paper scan** in this turn.

## Six specific comparison outcomes

| Existing question ID | Original keyed choice(s) | Compared sources and action |
|---|---|---|
| `P2013-S3-Q02` | **b, c** | **UNRESOLVED HISTORICAL KEY CONFLICT**: car option `d: Getting into a car` is not included in the bank key, yet SVLFG explicitly requires unloading before entering/exiting vehicles, as well as before climbing high seats and crossing obstacles. Do **not** claim b/c alone exhaust the safety obligations. Keep the raw source key unchanged; add a neutral visible **pre-answer** warning and prominent post-answer explanation identifying the omitted option. The key is **not certified factually correct**; original source-paper adjudication pending. |
| `H2023-D08-Q052` | a | Confirm unloading before climbing raised hide; a safety lever or opening bolt in lieu of unloading is not the selected answer. Original 2026 GHC Weapons/Ammo lesson + SVLFG high-seat section. |
| `H2023-D08-Q047` | c | Confirm gun must be unloaded during car travel; vehicle accessibility/transport-mode restrictions are legally distinct from loaded status. 2026 GHC ammo lesson + SVLFG vehicle section. |
| `H2023-D17-Q008` | a | Confirm downrange safe muzzle direction while working a rifle bolt on the supervised GHC range; no dangerous universal rule about arbitrary up/down orientation. Original 2026 GHC Range Safety + SVLFG. |
| `H2023-D17-Q018` | a | Confirm muzzle safe direction while loading/unloading; up or down alone is not guaranteed safe. Original GHC Weapons/Ammo + SVLFG. |
| `H2023-D08-Q024` | b | Historic Hessen drive-hunt key is at one's assigned stand; GHC Weapons/Ammo additionally states **load/unload when instructed** by hunt leader after the Jagdleiter briefing. Reaching a stand alone is not permission to ignore the published loading time. Original GHC Weapons/Ammo and Hunting Techniques classroom lessons. |

No new firearms-handling procedure was invented; where the exam-bank wording may mislead someone during a real hunt, the explanation separates archival scoring from source-checked safety guidance.

## Implementation and testing

- `scripts/qualify_safety_question_batch.py`: applies exactly six guarded explanation and provenance updates at **APK assembly**, after the older three-question audit. Original 867 IDs, questions, options, correct keys, answer types, original sourceRefs and sections are compared byte-for-byte in decoded records and remain unchanged. Five additional entries are `source_compared_explanation_qualified`; P2013-S3-Q02 is `source_compared_key_conflict` and carries `sourceBankKeyDisputed=true`.
- **Explicit UI warning**: the quiz-rendering string adds `<div class="alert" role="note">Source review notice: …</div>` for questions containing `preAnswerWarning`, *before* the answer-choice list and before checking/scoring. The warning deliberately does **not** reveal the question's omitted choice. This does not yet fix the legacy scoring basis; final source-key adjudication is required.
- `scripts/check_safety_question_batch.py`: checks each exact answer ID, source tag, key status, required safety language, preserved English explanation, and exactly one visibly rendered pre-answer warning in **assembled source and packaged APK**.
- `scripts/build_question_source_audit_matrix.py`: now records three honest classes of review outcomes, not simply verified/unverified: **8 individually source-qualified explanations**, **1 disputed archival answer key**, **858 not individually fact-audited**. The disputed one is **not counted as verified correct**. Pre-existing class-source tags on other questions remain navigation aids, not factual proof.
- All 71/71 classroom media strict checks and 117/117 source/packaged offline study images, 162 Jägersprache glossary entries (160 meanings; 2 pending), Android app identity and progress storage remain unchanged.
- Both Android workflows were modified to run both review overlays before assertions and APK packaging, re-open the actual built APK ZIP to check both sets of source caveats, then upload the 867-question source matrix.

**First evidence source:** `docs/QUESTION_FACT_AUDIT_HESSEN_MISFIRE_PLANNING_20261015.md` contains the first three reviews. This file records the **second six-question batch** and the key conflict. Count is **9 source-compared cases total, but only 8 qualified and 1 disputed**, never a generic claim that all nine historical keys are correct.

## Known limitations / next actions

Obtain and inspect the actual paper 2013 practice-test answer key for `P2013-S3-Q02` to determine whether its original key truly omitted `d` or the GitHub bank inherited an extraction/transcription mistake. In the meantime, the user-visible app warns of the conflict but original scoring still applies to this archived item. Avoid interpreting an outdated key as real-world safety authority.

The other **858** question records require direct source-by-source checks; 75 original Jägersprache origin notes remain unsourced, 2 meanings ambiguous; current law and copyright review outstanding. A green Android 35 emulator regression is not equivalent to an actual Samsung Galaxy S23 Ultra install and saved-progress upgrade test.

**Build evidence:** Follow the actual `feature/slide-audit-glossary-tests-20261012` CI results after committing this batch; do not assert APK/emulator pass without looking up the specific post-change run. Keep PR #3 draft/unmerged.
