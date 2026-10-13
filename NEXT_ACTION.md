# GHC Study — verified continuation handoff

Updated: 2026-10-13. Live source of truth: `feature/slide-audit-glossary-tests-20261012` (draft PR #3 to `audit/v145-source-recovery`). Do **not** restart or overwrite the older `main` branch.

## Build and app invariants

- v1.4.6, versionCode 146; SDK 35 target/compile, minSdk 24; primary app ID `org.ghcstudy.v141`; side-by-side test app ID `org.ghcstudy.v146.standalone`.
- Maintain 100 practice questions, 767 GHC-focused (Direct/Related) questions, 77 vocabulary quiz questions, 117 study cards, and the 162-term Jägersprache glossary (135 with meanings / 27 pending; two meanings from a historical 2013 course guide, not 2026 class slides).
- Preserve existing quiz progress storage, selective reset and backup/restore, offline images, system Back and launcher icon. Debug APK signatures from independent builds may differ; the standalone app is safer for initial installation.

## Source research completed and remaining

- Readable text for all 38 inventoried class PDFs was fetched in preceding audits; additional `Guide_08n1-5_Other_Game_2013-08.pdf` was directly located and re-read in Drive today.
- Study-card audit register: **803 text-checked / 11 pending class-slide verification / 814 displayed blocks**. Five unsupported/editorial blocks removed from the original 819. Counts derived from `audit/study-card-claim-register-20261012.json`, not stale chat summaries.
- The 11 pending fact blocks all belong to the Murmeltier (6) and Seehund/Robbe (5) cards. Their historical guide text is now separately traced in each claim's `supplementalSource` field; do **not** mark these as checked against 2026 class slides or as current legal facts. Two individual blocks have only partial support from the guide.
- New 2026-10-13 audit updates verified source wording for wolf, wildcat, bear, Rehwild, Rotwild and Schwarzwild; removed editorial/unattributed material from wolf/trophy cards. See `docs/SLIDE_AUDIT_PROGRESS_20261013.md`.
- Text-checked does **not** certify embedded photo diagrams, genuine page numbering, legal currency, historical etymology or all assertions within compound fact blocks. The 867 examination explanations and original 77 vocabulary etymologies are separate unfinished audits.

## Immediate engineering next steps

1. Verify CI after the latest source/claim-register synchronization. `scripts/check_claim_register_parity.py` compares all fact text, labels and counts against shipped HTML. The prior failed workflow against commit `be6ec881...` failed due to a **stale Collared Dove claim string**, but live 2026-10-13 source/claim comparison is now synchronized.
2. Trigger the glossary/functional CI on changes to both `app/src/main/assets/index.html` and `audit/study-card-claim-register-20261012.json`; do not treat a workflow from an intermediate, not-yet-synchronized commit as final build evidence.
3. Test the latest APK including emulator system Back, glossary and app icon, then use the standalone APK on a Galaxy S23 Ultra for physical validation and offline progress tests.
4. Decide whether historical 2013 course-guide cards should be explicitly segregated from *class-slide-only* Study Mode material. Do not silently remove source-backed content or promote guide evidence to a 2026 slide citation.
5. Finish photo/diagram identification review, question-by-question audit, and glossary/etymology verification before merging PR #3.

## Preserve source discipline

Study-card Details/Other Facts contain class-slide material only unless an exception is explicitly labeled as historical course-guide material; never insert speculative instructor commentary or unsupported internet facts. Maintain separate references to current German hunting law where relevant. No claim that an APK compiled means the installed behavior was tested on the owner's handset.

## 2026-10-13 continuation — glossary batch

- Nine additional worksheet terms now have source-attributed meanings: Brucellose, Schweinepest, Fuchsbandwurm, Kleiner Münsterländer, Hahn in Ruh, Untere Jagdbehörde, Jagdschein, Wiederkäuer, Frettieren. Glossary is 127 defined / 35 pending, 162 total.
- For Frettieren, Jagdschein and Wiederkäuer, the class deck supports the context but does not explicitly translate the worksheet headword. This limited provenance is reflected in per-entry audit metadata. Etymologies remain blank where not directly verified.
- See `docs/GLOSSARY_DEFINITIONS_BATCH_20261013.md` for evidence and open issues. Recheck latest runtime/Android CI before using the updated APK.

## 2026-10-13 — question-integrity continuation

- Added `scripts/check_question_bank_integrity.py` to CI. It verifies all 867 exam items and their answers/learning explanations structurally; a passing report proves no mechanical giveaways under the current heuristic, **not** legal/biological factual truth.
- Fixed the exact answer giveaway in `H2023-D19-Q042` (Jagdschein translated in stem, repeated as choice B), preserving the correct answer ID. Smoothed the duplicated range-supervisor questions `H2023-D04-Q151`/`H2023-D15-Q010` and live-capture questions `H2023-D09-Q083`/`H2023-D15-Q003` without altering scoring.
- Screened 18 identical-stem pairs (11 pairs with identical normalized choice sets); no records deleted because separate sources and progress IDs matter. Full pair list: `docs/QUESTION_DUPLICATE_REVIEW_20261013.md`.
- The static scanner flagged **491 questions without explicit visual-ref fields**. This is a triage statistic, **not** proof that 491 animal questions lack images. Audit animal references separately.
- Emulator CI has been affected by a **Pixel Launcher ANR modal** in one run and by captures of **an unrendered white WebView startup frame** in another. The latest script waits for rendered screens, dismisses only the external launcher dialog, and checks foreground app state. Verify the latest complete CI run before claiming hardware Back passed.
- Latest physical Galaxy S23 Ultra install/backup/restore/upgrade behavior remains untested in this turn.

## 2026-10-13 — second glossary audit and emulator observability

- Six additional class-linked worksheet terms defined: **Absehen, Kugelfang, Objektiv, Okular, Streckeplatz, Visier**. Glossary current tally: **133 defined / 29 pending / 162 total**. Kugelfang has direct bilingual wording in the range slide. The other five are worksheet-term plus English slide context, *not* exact class-slide translation statements. Etymology remains blank. Evidence: `docs/GLOSSARY_DEFINITIONS_BATCH2_20261013.md`.
- Updated glossary JS DOM regression to assert all six definitions and the current filters. Earlier CI runs at the intermediate glossary-only commit expected 127/35 and therefore failed; evaluate the **latest tested commit** instead.
- Added Android emulator failure artifact collection (logcat, WebView provider, activity/window focus state) and WebView page/JavaScript console diagnostics. Existing CI showed a truly blank WebView surface and unresolved system Back, *not* a verified app navigation pass. Check the latest CI run and inspect diagnostics if emulator remains blank.
- Do **not** merge draft PR #3 into the old `main`, or claim a physical Galaxy S23 Ultra test has occurred.

### Emulator follow-up — corrected target selection

- Evidence from CI run `38413027220` demonstrated the previous gesture script tapped **Reference**, not **Glossary**, because its y-coordinate fell below the Glossary anchor. The resulting system Back exited to the launcher; this is still an unisolated Back failure, **not** evidence about glossary page history.
- Corrected the test at commit `38e6e1b07b217bbdfde7cf61e0e1bf8d0a94b6b7` to tap the actual UIAutomator-located Glossary anchor and require the glossary heading, then exercise Android Back. Workflow `38414557677` is queued as of this handoff; verify its eventual conclusion and artifacts before interpreting the result. See `docs/ANDROID_EMULATOR_TEST_DIAGNOSIS_20261013.md`.
- Still test Back from Reference -> prior tab and Study card -> category separately, then perform physical Samsung Galaxy S23 Ultra validation.

### 2026-10-13 — third vocabulary and emulator reliability continuation

- **135 glossary defined / 27 pending / 162 total.** Directly class-PDF-confirmed translations: `Leberegel` → liver flukes (`Disease - Parasites.pdf`) and `jagende Hunde` → hounds (`Hunting Dogs (202609).pdf`). Source evidence: `docs/GLOSSARY_DEFINITIONS_BATCH3_20261013.md`. No etymology inferred, no question-bank changes.
- Android emulator screenshot/accessibility evidence from run `38414557677`: **Pixel Launcher isn't responding** dialog appeared over an otherwise rendered GHC Quiz Mode page and obscured the `Glossary` link. JS smoke + APK build passed; emulator still failed. Robust post-render and post-accessibility ANR retry added in commit `4fe87f69f0b5b6c74b31dc4b5b2481a6465f1fa3`; check its workflow conclusion and the latest after glossary edits.
- Do not treat the prior launcher dialog as a GHC app crash, but do not certify system Back or glossary page navigation until their actual emulator evidence passes. Continue preserving old `main` and unmerged draft PR #3.
