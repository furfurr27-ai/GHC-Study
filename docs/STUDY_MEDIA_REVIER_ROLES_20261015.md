# GHC Study media batch 10 — model Revier Roles (2026-10-15)

## Primary classroom evidence actually checked

The original connected **Range - Revier (20260922).pdf** (30 pages) was inspected directly, including rendered pages **7 and 30**. Page 7, *Who is in a Revier*, distinguishes officials, Game Rights Owner, Hunters, Land Owners and Land Users, with the hunters including Jagdausübende, Jagdaufseher, Begehungsschein holder, Jagdgast and Berufsjäger. Page 30, *What We’re Working on Locally*, presents a **Model Revier X** relationship using the labels **Pächter** and **Ami-Jäger Team**. It is a teaching **example**, not an official or exhaustive hierarchy.

The previous `revierroles` study card used a lecture-slide image including text and farm equipment. The new image is a 900×500 **standalone two-photo comparison** generated during APK assembly using only the two individual original class photographs from page 30, with the two original classroom labels on a white background. It is **not** a whole-slide screenshot. The existing card Details still provide the complete role explanations.

| Classroom image | PDF embedded image | Source byte SHA-256 | Git file |
| --- | --- | --- | --- |
| *Pächter* example photograph | page 30, xref **191**, JPEG 401×600 | `853cdd232e4143d2e27ced239ad01b652d8e9cace819cbfd5a7d76f0e601415a` | `app/src/main/assets/media/revier-role-paechter-class-photo.jpeg` |
| *Ami-Jäger Team* example photograph | page 30, xref **192**, JPEG 348×466 | `1eff4e7bb204c7cca82cc02007b5e72ddbf09e3b378c42a5384795dce8d8dccf` | `app/src/main/assets/media/revier-role-hunter-class-photo.jpeg` |

The generated app asset is `media/study-revierroles-two-examples.webp`, built by `scripts/crop_study_slide_images.py`. The individual photographs and their provenance are recorded under `audit/study-media-review-20261014.json:assemblyMontages.revierroles`; `scripts/check_study_media.py` validates their exact original hashes, page/XObject list and the assembled mapping. These generic educational model images should **not** be presented as portraits of actual current Revier office-holders, legal authority, or the complete roles list.

## Verification

[Standalone APK build 38668957594](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38668957594) **succeeded**. Downloaded and extracted the actual APK. Direct inspection verified `revierroles` now resolves to the 900×500 offline image with correct source metadata; both original JPEGs are present.

The previous **66-image / 160-definition APK** and this **67-image / 160-definition APK** were extracted side-by-side and programmatically compared:
- **117** study-card IDs and all their **non-image fields byte-equivalent after JSON decoding**; the only card-image remapping is `revierroles`.
- The packaged `glossary-data.js` files are byte-identical (**160 defined / 2 pending**).
- The launcher icon binaries are byte-identical.
- The new APK SHA-256 is **`a0cbd0f3220b8539f5c2d2bb63a309ef82be4cd6994a3b57ba2314649782cc0a`**, file size **13,554,801 bytes**.

The current full Android 35 regression is [run 38668935001](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38668935001): check the final emulator result separately. The standalone artifact build success is **not** a Samsung Galaxy S23 Ultra test.

## Four still-unresolved image cards

`drivebrief`, `misfire`, `abschussplan`, `shotdistance` remain **whole-slide** visual blockers. Don't invent a current official Abschussplan from the classroom `Streckenliste 2014/2015`: it is a **record of game taken**, not the planned harvest. Hessen RP Kassel's [hunting authority download page](https://rp-kassel.hessen.de/forsten-und-landwirtschaft/jagd) provides separate Streckenliste and Abschussplanung forms, and its 2025 [Abschussplanung directive](https://rp-kassel.hessen.de/sites/rp-kassel.hessen.de/files/2025-03/2025_03_07_erlass_abschussplanung-festsetzung_und-vollzug.pdf) confirms that separation. A current form was **not** added because its exact graphic, image reuse permissions and proper crop have not been verified in the app build.

`misfire` and `shotdistance` are safety-sensitive: don't substitute an incorrect demonstration or a simple rule-of-thumb dangerous-distance picture without an authoritative match to the course topic. `drivebrief` is text-heavy in the original February 2026 hunting techniques slide and has no standalone photograph there; obtain a suitable class/official illustration before replacing.

## Limitations

No original question, answer key/explanation, card text, stored progress key, Android navigation logic or app metadata changed. The 867-question factual audit, 77 existing etymology origin accounts and the two ambiguous worksheet words (`Jagdschuetz`, `Tiroler`) remain open. Original classroom photos may have been borrowed from external sources; no independent public redistribution license was certified. Draft PR #3 remains unmerged.
