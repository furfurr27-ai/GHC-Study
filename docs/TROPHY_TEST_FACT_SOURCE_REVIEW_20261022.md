# Trophy Test fact-sheet source verification — 2026-10-22

## Scope
GitHub source release: **v1.4.10**, merged PR #5; the previous v1.4.9 photo-only baseline remains in Git history.

App contains 29 separately cropped original exam-room mount photographs sourced from connected Google Drive folder [German Hunting / Trophy Test](https://drive.google.com/drive/folders/1PRbQppS10WBEigmrXka_urSrEGh8YY1L) (33 photo entries, including duplicates). Each specimen has photo-based recognition notes, a source-labelled compact card, and explicit confidence flag. 19 named specimens can appear in scored Identify mode. The other ten are review-only and carry species/group comparisons, not verified IDs.

## Evidence actually checked in this work period

- **Original GHC class PDF**: *Game - Mufflewild (2015).pdf*, Drive ID `1tXW1RQSNDj11XyL5BL_bBAx2xHpnPY5m`. Reviewed extracted contents directly: Widder/Schaf/Lamm, October–December rut, 22 weeks gestation, March–June birth period, 32 teeth, Hochwild, Schnecken horns. The file itself calls this a 'Baseball Card Data' layout.
- **Original GHC class PDF**: *Game - Rotwild.pdf*, Drive ID `18jWSwS3sN51I7b6xgAeo_kxCAeO72xrz`. Reviewed extracted text directly: September–October rut, 33–34 weeks, May–June births, 34 adult teeth, Grandeln, Leittier/Kahlwildrudel terminology.
- **Original GHC class PDF**: *Game - Federwild.pdf*, Drive ID `1n7PYc8WDv72owQUeYNaRx4UvW1RT7RBD`. Reviewed content for bird group coverage (including Fasan, Rebhuhn, Schnepfe, Möwen, Tauben, Enten). Used group comparisons only for specimens with uncertain identity.
- **Original GHC class PDF**: *Game - Predatory Birds (202609).pdf*, Drive ID `1Tew6IB7SZ1QFrBxgxUwf61lZb3Bn_IQg`. Reviewed content identifying corvids (Rabenkrähe, Elster, Häher), the phrase 'forest police' for jays, and raptor categories. Not adequate to identify unknown mounted raptors from the room photographs alone.
- **External pages located/reviewed**: NABU Vogeltrainer Star at `https://vogeltrainer.nabu.de/vogel/star/`, NABU Vogeltrainer Buntspecht at `https://vogeltrainer.nabu.de/vogel/buntspecht/`, and Bundesinformationszentrum Landwirtschaft (BZL) domestic chicken `https://www.landwirtschaft.de/garten/selbst-anbauen/tiere-halten/huehner-halten-im-eigenen-garten`. Also located relevant NABU regional squirrel feature and coastal avocet publication. These are distinctly marked external supplemental notes, not slide-only content.
- **Repo files**: `app/src/main/assets/trophy-test-info-data.js`, `trophy-test-data.js`, `trophy-test-app.js`; `scripts/check_trophy_test.py` and `scripts/check_packaged_trophy_test.py`. All 29 entries parse with expected source labels: 13 based on existing Study Mode summaries, 11 slide-comparison summaries, 5 externally sourced. These counts are source-label categories, **not** a claim every line of all 29 summaries was checked directly against its original PDF in this session.

## Important distinctions
- For `sourceType=study`: facts reuse the earlier slide-based Study Mode consolidation; only representative original class decks were directly rechecked in this work period.
- For `sourceType=slides`: class-deck comparisons are framed as group knowledge, not confirmation of an ambiguous mount.
- For `sourceType=web`: external reference facts are visually/verbally labelled *Supplemental animal facts* in the app.
- **Do not claim the ten uncertain specimen identities are established** by associated group facts. They stay excluded from scored photo recognition.
- Source files may be historical; current hunting seasons, legal restrictions, animal diseases and wildlife-protection obligations require updated authoritative verification elsewhere.

## Reproducibility / release acceptance
- All source photo masters are in `research/trophy-test/photos/`. An offline build crops exactly 29 isolated images and strips metadata.
- Both primary and alternate Android pipelines build from tracked current application source, not from an obsolete APK. All 125 Practice Test 2 questions in 5 sections, the glossary, Schalenwild matrix and launcher icon are required by the packaged-APK validator.
- Release source PR #5 merge commit `4cc626ad819454d97186c4852aca0ed90c6bb788`. Primary build run `39839330448`; alternate glossary workflow run `39839330484`, Android APK and emulator steps verified successful.
- **Outstanding:** physical Galaxy S23 Ultra installation, source photo identification review with instructor, and saved-progress backup/export validation. Preserve existing app data before uninstalling if Android signing certificates conflict.
