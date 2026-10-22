# Trophy Test — source inventory and identification limitations (2026-10-22)

Primary-source folder: https://drive.google.com/drive/folders/1PRbQppS10WBEigmrXka_urSrEGh8YY1L
- 33 image files checked by folder listing; 13 pairs of duplicate WhatsApp JPG names (0002–0014) and 7 additional high-resolution camera panoramas (185942–190013). All 20 unique views opened for visual intake.
- 13 unique WhatsApp photos retained as cropped-asset masters in `research/trophy-test/photos/`; originals excluded from packaged `assets/`. Photo masters may include visible classroom surroundings and reflections; the actual APK contains only cropped mounts.
- App manifest: `app/src/main/assets/trophy-test-data.js` with stable ID, German/English display name, source photo code, crop rectangle and short visual-only identification cue per mount.
- Recognized taxa are photo-based provisional identifications for the actual room, not an authoritative list from a lecturer or confirmed full taxonomy. Uncertain specimens are labeled as needing closer ID and excluded from automatic scoring. Review flags cover martens, a chamois-like skull, pigeon, raptor(s), ducks, partridge-like grouse, white gamebird, another dark gamebird and a gull.
- The 29 entries are study targets for visibly different mounted specimens (species may be repeated in the room); this is **not** a claim that the room contains 29 distinct wild species. The records should be corrected if closer photos or instructor labels resolve ambiguities.
- Crops are generated with `scripts/build_trophy_test.py` and stripped of EXIF; no class-slide images were replaced. This feature does not alter the existing study-card Details / Other Facts content, question banks, answer keys, or mastery storage.
- Real device acceptance outstanding. Build jobs must verify `trophy-test.html` and the cropped 29 JPEGs physically inside the final APK.
