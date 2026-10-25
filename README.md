# Jäger Field Guide v1.5.0 — offline field reference (2026-10-25)

The hunting course is completed. **The Android app now opens directly to the Jäger Field Guide**, a searchable offline animal reference with 19 bilingual baseball-style cards, locally saved favorites and Revier notes, identification traits, seasonal biology, signs and disease cautions. The original Quiz/Study application, old progress storage keys, Trophy Test, source-audited glossary, and its Android package identity are preserved at **Study archive**.

**Legal caution:** Animal pages are not current hunting authorization; the app deliberately does not display static "legal to hunt now" badges. Hessen revised its hunting ordinance effective April 1, 2026. Always verify local current seasons/orders, dependent-young protections, game management plans and ASP controls with the responsible authorities.

**Picture status:** 11/19 cards use already packaged course or exam-trophy images; eight explicitly show no-photo placeholders. Mounted photographs are labelled as such, not mistaken for live-animal field photographs.

Source review, provenance, test instructions, limitations and finite next steps: [Field Guide v1.5.0 checkpoint](docs/FIELD_GUIDE_V150_20261025.md). Test the field guide via \`node tests/field-guide-smoke.cjs\` and \`node tests/field-guide-functional.cjs\` (with jsdom); source/APK image audits via \`python3 scripts/check_field_guide.py\`. Real Galaxy S23 Ultra APK upgrade acceptance is still outstanding.

---

# GHC Study v1.4.10 — completed Trophy Test animal fact cards (2026-10-22)

The v1.4.9 release introduced **29 individual room-photo cards**, using source-cropped photographs of actual mounts in the exam room. This v1.4.10 enhancement adds a **source-labelled compact animal fact sheet to each card**, including German/English hunting terms, key biology, identification, comparison notes and memory cues where supported. Facts are revealed **only after a flashcard answer or graded identification response** and are visible during normal Cards browsing. An external fact is labelled as *Supplemental animal facts*, never mixed into the GHC-course-labelled *Details · Other Facts*. Uncertain mounts remain excluded from scored recognition.

Of the 29 summaries, 13 reuse the existing slide-based Study Mode material, 11 describe class-slide comparison groups, and 5 use separately identified German nature/animal reference material (NABU or Bundesinformationszentrum Landwirtschaft). The 10 visually uncertain mounts are **not** upgraded to definite species answers without a better specimen photograph or instructor confirmation.

**Release source and app identity:** Android `versionName=1.4.10`, `versionCode=150`, original application ID `org.ghcstudy.v141`, preserving the existing app's on-device progress namespace. No exam questions or older card datasets were replaced. Practice Test 2 still contains all 125 items across five 25-question parts. Glossary, source audits, historical-source warning text, Schalenwild comparison views, offline media, and Android Back are preserved.

**Build assurance:** Primary GitHub Actions run [39839330448](https://github.com/furfurr27-ai/GHC-Study/actions/runs/39839330448) and alternate glossary build [39839330484](https://github.com/furfurr27-ai/GHC-Study/actions/runs/39839330484) each passed Android APK packaging and emulator checks for the v1.4.10 source. Primary source smoke individual steps all completed successfully; consult its workflow job's final conclusion if necessary. Primary APK artifact: `GHC-Study-v1.4.10-TROPHY-TEST-full-debug-apk`. Final Samsung Galaxy S23 Ultra installation and progress-backup verification must still be done on device.

**Sources/limits:** [Trophy Test source audit](docs/TROPHY_TEST_SOURCE_AUDIT_20261022.md) and [reviewed source notes](docs/TROPHY_TEST_FACT_SOURCE_REVIEW_20261022.md). Do not treat an external nature reference as a hunting-course answer or an uncertain photograph as an identified animal.

---

# GHC Study v1.4.9 — Trophy Test (2026-10-22)

The user supplied 33 Drive files under `German Hunting/Trophy Test`: 13 repeated WhatsApp phone-photo pairs (26 files total) plus seven original phone panoramas. The new Quiz Mode Trophy Test uses 13 unique WhatsApp room views (cropped to individual specimens, with originals kept outside Android assets) to provide **29 specimen baseball cards**. Nineteen have enough photo evidence for scored name identification; ten are explicitly `review` because exact species cannot be established confidently, and are excluded from graded questions.

Modes: Cards (Mammals/Birds filters, individual English/German label, exact room crop, photo-observed ID cues), Flashcards (photo before revealing name; self-assessment), Identify (four-choice photo questions with feedback). Progress stored in `ghc-trophy-test-progress-v1`, independent of the existing exam-question bank. Build automatically crops 29 offline JPEGs with EXIF stripped. Existing 867 exams + 125 Practice Test 2 + 77 vocabulary, glossary, study media, Schalenwild matrices and package ID are unchanged.

**Source:** `https://drive.google.com/drive/folders/1PRbQppS10WBEigmrXka_urSrEGh8YY1L` (33 images examined as room overview, including duplicates), tracked images `research/trophy-test/photos/` and photo/crop manifest `app/src/main/assets/trophy-test-data.js`. Species labels are practical visual study identifications, not externally taxonomically verified; review-only entries must be checked with close-ups.

**Build checks:** `scripts/check_trophy_test.py`, `tests/trophy-test-smoke.cjs`, and `scripts/check_packaged_trophy_test.py` assert all 29 crops and preserve Practice Test 2, glossary, and matrices in packaged APK. Follow current CI results before claiming the release validated. Device acceptance on the Samsung S23 Ultra remains outstanding.

---

# GHC Study — restored full release v1.4.8 (2026-10-20)

**Important recovery:** v1.4.7 incorrectly built from an obsolete v1.4.5 APK, omitting completed development. This release uses the **latest 2026-10-15 tracked source** (branch `feature/slide-audit-glossary-tests-20261012`) as its base and layers the three Schalenwild matrices on top.

- **Practice Test 2:** 125 photographed paper questions in native Quiz Mode (five groups of 25), yellow-highlight answers preserved, matching question, source-selection, warning labels, progress/reset.
- Other preserved work: 867 legacy exam questions + 77 vocabulary questions, 117 study cards, all 71 reviewed thumbnail replacements, 162 searchable glossary entries, etymology notes, historical-source cautions, stable icons, Android Back behavior.
- **Schalenwild:** reproduction calendar + antler/horn comparison + identification matrix, separately packaged.
- Application ID unchanged: `org.ghcstudy.v141`; versionCode 148. If the Android signing key differs between previous installs, **export progress before making any uninstall decision**.
- **Source-driven build:** no legacy APK extraction. Required release checks: `tests/practice-test-2-smoke.cjs`, glossary/quiz/Back/media audits, `tools/test_schalenwild_matrix.js`, APK inspection of all 125 records and offline assets, emulator smoke.
- **Separate timed exam prototype:** preserved on `feature/practice-test-2-20261015`, **not** merged; native quiz remains the agreed untimed study drill. No duplication of Practice Test 2 entry.
- This is a software restoration, not certification of historical 2021/22 paper answers or current law.

See `docs/RESTORE_FULL_PROGRESS_20261020.md` for source history, tests and acceptance.

---

## Archived development notes (2026-10-15; prior to v1.4.8)

## Practice Test 2 — complete five-part photographed paper (2026-10-15)

**125/125 questions transcribed, five parts of 25.** The original Quiz Mode integration is used with native progress, selective reset, study scope, and ⓘ cover instructions. Only **yellow highlighted** paper answers are keyed; pen circles and ticks are ignored. Final sections added: Part III Weapons Law/Firearms, Part IV Nature/Animal Protection and U.S. Forces Procedures, and Part V Diseases/Meat Handling/Hygiene. Part II Q25 is a single one-point six-pair matching question.

Tracked data: `app/src/main/assets/practice-test-2-part1.json` through `practice-test-2-part5.json`. Assembler: `scripts/integrate_practice_test_2.py`; regression: `tests/practice-test-2-smoke.cjs`; source/provenance checkpoint: `docs/PRACTICE_TEST_2_INTAKE_20261015.md`. The native Quiz Mode is an **untimed drill** (the printed paper's 150-minute limit is displayed in info). The separately tested `feature/practice-test-2-20261015` branch contains a complete standalone timed simulator but is not merged into this branch, to avoid duplicate entry points.

The 2021/22 date is user-reported and unverified. These are historical test-answer transcriptions, **not** verified current law, firearm-safety or game-meat inspection instructions. The existing 867 GHC exam items and 77 Jägersprache questions remain unchanged. Current development stays off `main`; physical Samsung Galaxy S23 Ultra acceptance is still outstanding.

### Archived initial 50-question intake (superseded by completed status above)

Added a **separate Quiz Mode bank** for the user's more recent U.S. Forces Hunting Examination practice example. Initial intake: **50 of 125 questions**, all 25 questions in Part I (Game Biology) and all 25 in Part II (Hunting Dogs / Hunting Procedures). **Only yellow highlighted answers** are keyed; pen circles are not. Part II Q25 uses an actual six-way matching interface and counts as **one** question. A new ⓘ info modal displays cover instructions: closed book, ink pen, circle letter(s), five 25-question parts, 13 needed **in each part**, one point per question, 150-minute written exam limit. The current app drill is **not timed**.

Data: `app/src/main/assets/practice-test-2-part1.json`, `practice-test-2-part2.json`. Integration: `scripts/integrate_practice_test_2.py`, applied after source-audit overlays in full feature-branch CI; separate source selector, part drill scopes, mastery, progress/backup/reset, no edit to the historical 867-question source bank or 77 vocabulary records. Tests: `tests/practice-test-2-smoke.cjs`. Checkpoint and continuation: `docs/PRACTICE_TEST_2_INTAKE_20261015.md`. **More photo batches expected for Parts III–V.** Exam source date 2021/22 is user-estimated, not verified on paper. The original photos have **not** been committed to this public repo. Standalone APK build [#38800047487](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38800047487) and functional smoke job [#38800047286](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38800047286) succeeded. Do not merge draft PR #3 or edit main without user direction.

# GHC Study Android

Version **1.4.6** (versionCode 146), package `org.ghcstudy.v141`. Target: Samsung Galaxy S23 Ultra. Android minSdk 24, compile/target SDK 35.

The project is currently **public on GitHub**. Do not commit private class slides, copyrighted PDFs, credentials, or personal data.

## Build
GitHub Actions: **Build Android APK from tracked source** (`.github/workflows/android-apk.yml`). The build uses `app/src/main/assets/index.html`, tracked `assets/media/`, and `res/drawable/ic_launcher.png`. It must not extract or embed the historical APK.

## Audit and provenance
- `Audit recovered v1.4.5 against historical APK` compares tracked source files with the original v1.4.5 APK stored in commit `9ce4b3037af3b1a9af5f88ef645265bb06d6f245`.
- `Static app and repository audit` scans asset sizes, media references, duplicate files, external dependencies, and inline JavaScript syntax. Its reports are diagnostic; unreferenced assets are not automatically deleted.
- `docs/SOURCE_INVENTORY.md` maps course sources; `docs/AUDIT_V145.md` records original app parity constraints.

## Quiz and Study Mode additions
- **Jägersprache1** is the third native Quiz Mode bank with 77 German-to-English vocabulary questions in five topic groups. It shares the existing mastery-progress, backup, and reset machinery.
- **Trophy Anatomy** is the English-only Study Mode title. The card retains the class-based deer and horn facts, and uses the original labeled Rotwild antler image from *Game - Rotwild.pdf*, page 14.

## Non-negotiable regression requirements
- Android system Back returns to the previous app screen; root exits only intentionally.
- Quizzes, direct/related pools, study cards, references, and progress/reset scope retain behavior.
- Existing saved progress and offline images remain usable after updates.
- Study card Details and Other Facts are sourced only from class slides. Photos are individual images, not slide screenshots.

## Change policy
Do not bulk-minify or remove assets without measured savings, an explicit source diff, a successful parity/build audit, and behavior regression evidence. A successful build is not proof of runtime correctness.

## October 2026 glossary and verification work

The v1.4.6 development branch includes **162 offline searchable Jägersprache entries: 160 meanings available and 2 pending** (`Jagdschuetz`, `Tiroler`). Entries distinguish class-PDF text, worksheet-to-class contextual matches, historical course guides, and explicitly labeled external authorities. Of the original 77 word-origin/breakdown notes, **2 now have individually cited historical or word-formation support** (`Schweiß`, `Schweißhund`) and **75 remain unverified**; each status is labeled individually and the summary counts are dynamically derived. Do not interpret a compositional mnemonic as verified historical word origin or poacher camouflage. See `docs/GLOSSARY_ETYMOLOGY_UI_AUDIT_20261015.md`. The glossary remains searchable and cross-referenced, with its offline Android link and all original IDs preserved.

**Audit status (2026-10-13):** All 38 listed class PDF texts were retrieved. The app currently has **803 class-PDF-text-checked fact blocks of 814**, leaving **11 pending classroom-slide verification**. The remaining 11 are the historical 2013 course-guide Murmeltier and Seehund/Robbe facts, separately checked against that guide but not misrepresented as 2026 slide evidence. Five unsupported/editorial blocks were removed from the original 819. Checked means fidelity to PDF text, **not** independent biological/legal correctness, verified slide illustration/page location or a complete audit of individual exam explanations. See `audit/study-card-claim-register-20261012.json`, `docs/SLIDE_AUDIT_PROGRESS_20261013.md` and `docs/CURRENT_LAW_SOURCE_WARNINGS_20261013.md`.

GitHub Actions regression covers quiz/navigation/glossary, the Android Back bridge, APK packaging, and Android emulator smoke checks. Installation/upgrade retention on the actual Galaxy S23 Ultra remains to be checked.

## Exam-question integrity audit (2026-10-13)

`scripts/check_question_bank_integrity.py` now verifies all 867 shipped exam records (100 Practice Test + 767 GHC Focused), answer IDs, options, explanations, and mechanical parenthetical answer giveaways. The source question `H2023-D19-Q042` was corrected to remove a direct parenthetical answer clue without changing the original answer key, and four duplicated malformed question stems were smoothed. The scanner flags 18 same-stem pairs and 491 questions without explicit visual-ref fields for further human review, but does not remove questions or claim those 491 are missing animal pictures. See `docs/QUESTION_BANK_INTEGRITY_20261013.md` and `docs/QUESTION_DUPLICATE_REVIEW_20261013.md`. A green mechanical scan is not a factual or current-law audit.

## Current media release gate (2026-10-15)

The tracked assembly overlay now repairs **71 of 71** originally slide-style study thumbnails into standalone class-photo crops, direct original embedded PDF figures, photo montages, a verified classroom image reuse or **three explicitly NEW course/official-text-grounded educational SVG illustrations** (`misfire`, `shotdistance`, `abschussplan`). The two safety-topic drawings do not claim universal operating procedures or guaranteed safe distances. The Abschussplan illustration differentiates prospective planned culls from historical Streckenliste and visibly says **NOT AN OFFICIAL FORM**; it was drawn using text from the publicly posted 2025 Hessian Anlage 2b Rehwild PDF, not an inaccessible current 2026 XLSX workbook. Both build workflows now require strict 71/71 media source and **APK-packaged** integrity checks. The unrelated wrong-subject Shot Placement picture was corrected previously. These checks do not replace the 867-question factual audit, glossary historical source verification, legal review, independent photo rights checks, or physical Samsung device validation. See `audit/study-media-review-20261014.json`, `docs/STUDY_MEDIA_ABSCHUSSPLAN_SOURCE_20261015.md`, `docs/STUDY_MEDIA_MISFIRE_SOURCE_SCHEMATIC_20261015.md`, and `docs/STUDY_MEDIA_SHOT_DISTANCE_SCHEMATIC_20261015.md`.

The **867-question source audit** now distinguishes **18 individually source-qualified explanations**, **8 historical 2013 answer-key limitations or legal-scope warnings** (Q02 vehicle unloading, Q03 transport checklist, Q09 prior WBK, Q11 semiautomatic capacity, Q13 warning shots, Q15 proof-house claim, Q19 military firearm import, Q20 Austria hunting/travel checklist), and **841 not yet individually fact-audited** questions. The disputed `P2013-S3-Q02` question **really does omit car entry/unloading from B/C in both inspected copies of the original 19 December 2013 paper answer key** (not an app transcription mistake), despite SVLFG's current VSG 4.4 safety rule. The quiz displays a neutral warning **before grading** and its explanation describes the missing option; the historical `correct=[b,c]` key remains preserved but is **not certified complete** for safety. The quiz now also accepts **B/C/D** as a safety-complete response without marking vehicle unloading wrong, clearly distinguishing the archived and safety-complete responses after grading; a runtime JSDOM regression checks both. Five additional GHC classroom and SVLFG firearm-safety comparisons cover safe muzzle direction, climbing, vehicle unloading and driven-hunt leader loading instructions. Five more 2013 practice questions about firearms storage, transport, minimum caliber/energy and semiautomatic hunting have been individually compared with the **original December 2013 PDF**, the connected 2026 GHC Weapons/Ammo lesson, and current **WaffG §12, AWaffV §13, BJagdG §19**. Two new pre-answer notices explain current legal differences while original exam keys are kept; `docs/QUESTION_FACT_AUDIT_WEAPONS_LAW_20261015.md` records each source and caveat. **Four further original 2013 paperwork/self-defense questions** were checked against WaffG §§10, 12, 13 and 38 and StGB §32: borrowed long-gun paperwork and handgun authorization (qualified), and two flagged historical errors regarding long-gun prior WBK and universal self-defense warning-shot sequence. The latter warnings appear before grading, with the printed historical answers marked archival-only after checking rather than simply 'Correct'. See `docs/QUESTION_FACT_AUDIT_2013_DOCUMENTS_SELF_DEFENSE_20261015.md`. Four further 2013 questions (`P2013-S3-Q07/Q14/Q15/Q16`) were checked directly against the 2026 GHC ammunition/markings class deck and German WaffG §24/BeschG §§3–6; rimfire vs rimmed, shotgun gauge and proof/marking distinctions are source-qualified, while the paper's unconditional German proof-house test claim gets a pre-answer warning and archival-only grading. Sources: `docs/QUESTION_FACT_AUDIT_2013_MARKINGS_PROOF_AMMO_20261015.md`. Source-check of original 2013 `P2013-S3-Q18/Q19`: the sick-domestic-dog answer refers to a veterinarian (TierSchG §§4,17); the categorical 2013 `NO` answer for U.S. Forces AR-15 import is specifically flagged as historical, **not** a current permit ruling. USAREUR-AF's March 2026 customs pamphlet requires German import permission and U.S. Forces registration; WaffG §29 and technical classification also apply. See `docs/QUESTION_FACT_AUDIT_US_FORCES_IMPORT_ANIMAL_20261015.md`. No blanket import permission or ban is asserted. Another two 2013 original-paper questions were checked: `P2013-S3-Q06` .38 Special ammunition in a properly marked .357 Magnum revolver was verified by a directly viewed **Ruger manufacturer manual**; `P2013-S3-Q20` Austrian hunting-travel documents are marked **historical only** because Austrian provincial `Jagdkarte/Jagdgastkarte`, actual hunting permission, European Firearms Pass and firearm-category requirements vary. Its archive key is not unconditional permission to hunt or carry. See `docs/QUESTION_FACT_AUDIT_2013_AUSTRIA_38_SPECIAL_20261015.md`. Both workflows test these caveats, verify stable 867 original IDs/answers and emit `build/question-source-audit-matrix.json` from assembled source and actual APK; pre-existing classroom links are not proof of audited sources. Original evidence and unresolved conflict: `docs/QUESTION_FACT_AUDIT_HESSEN_MISFIRE_PLANNING_20261015.md`, `docs/QUESTION_FACT_AUDIT_FIREARM_SAFETY_BATCH_20261015.md`, `docs/QUESTION_REVIEW_COVERAGE_20261015.md`. Physical Samsung S23 Ultra acceptance, physical acceptance of the narrowly scoped dual-accepted scoring for the faulty 2013 paper answer, remaining etymologies and current-law reviews are outstanding.
