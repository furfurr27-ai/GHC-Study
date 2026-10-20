# Study-media batch 3 — thirteen verified bird and raptor photo crops (2026-10-14)

## Purpose and method

This follows the first nine picture-only crops in `docs/STUDY_MEDIA_VISUAL_AUDIT_20261014.md`. The study-card images in the original **v1.4.6 Android package** were extracted and visually inspected one by one. For each selected original GHC class image, an exact source-pixel rectangle was reviewed in a contact-sheet preview and confirmed to contain the target bird or raptor, with no presentation title, bullet text, colored caption or numerical badge in the selected pixels. Source slide layout and text are left in the original files for audit traceability, but only the cropped photograph is displayed in the assembled APK.

## Source-specific crop plan

| Card ID | German / English subject | Original slide illustration | Exact crop (left, top, right, bottom) |
| --- | --- | --- | --- |
| `curlew` | Großer Brachvogel / Eurasian Curlew | Brachvogel & Bekassine; right Curlew photograph | 438,243,639,398 |
| `whitefrontedgoose` | Bläßgans / White-fronted Goose | Gänse comparison; photo #1, excluding badge | 633,70,833,243 |
| `tawnyowl` | Waldkauz / Tawny Owl | Käuze; left photograph | 25,217,259,595 |
| `osprey` | Fischadler / Osprey | Adler; upper-left raptor photo | 12,118,429,492 |
| `seaeagle` | Seeadler / White-tailed Eagle | Adler; lower-right flying sea eagle; excludes green/yellow page labels | 498,253,889,574 |
| `eagleowl` | Uhu / Eagle Owl | Uhu; right perched owl photo | 366,105,642,435 |
| `kestrel` | Turmfalke / Common Kestrel | Falken; top-right kestrel photo; excludes caption | 460,76,866,343 |
| `harriers` | Weihen / Harriers | Weihen; upper-right perched harrier photo | 592,75,881,287 |
| `carrioncrow` | Rabenkrähe / Carrion Crow | Rabenkrähe; upper-left isolated crow photograph | 13,16,251,175 |
| `rook` | Saatkrähe / Rook | Rook vs Crow; lower-left photo (beak and bare facial base visible) | 18,278,407,570 |
| `raven` | Kolkrabe / Common Raven | Kolkrabe; lower-right flying raven photograph | 371,345,846,646 |
| `magpie` | Elster / Eurasian Magpie | Elster; lower-right perched magpie photograph | 493,356,860,600 |
| `jays` | Eichelhäher / Eurasian Jay | Häher; lower-right Eurasian Jay photograph | 398,331,860,658 |

All dimensions here are source-image pixels. Outputs are `media/study-photo-<cardId>.webp` generated during both Android build workflows from `scripts/crop_study_slide_images.py`. The cropped image selection is applied by card ID only; the facts, source notes, quiz bank, study progress, and answer/explanation content are untouched.

### Deliberately deferred

Other full-slide candidates were inspected but **not** cropped when a text overlay or numbered badge could not be removed without clipping the bird's head, body or diagnostic feathers: `capercaillie`, `blackgrouse`, `goldeneagle`, `sparrowhawk`, and `canadagoose`. `blackkite` likewise needs a cleaner source or careful graphic evaluation. This is more reliable than replacing the original slide screenshot with a poor species-identification image.

## Quality gates

- Visual-review register: `audit/study-media-review-20261014.json` now records **22** original slide/page-like cards repaired at assembly, leaving **49** slide/page-like cards and **1** `shotplacement` subject mismatch for later review.
- `scripts/check_study_media.py` verifies every one of 117 cards has an existing local image, that each repaired card points to its exact new `study-photo-ID.webp`, and that flagged/repaired/mismatched counts remain internally consistent.
- `--strict` remains a **release-blocking** option: full image-content audit is not complete even after 22 successful crops.
- Latest GitHub Actions standalone and full Android CI runs at this batch must be inspected before claiming that this exact 22-crop version is APK/emulator verified. The Android 35 three-route Back regression previously passed at [run 38497590290](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38497590290), before these 13 new crops.
- A Samsung Galaxy S23 Ultra installation, offline media scan and progress-backup/restore test are still required for physical acceptance.

**Sources actually checked:** the packaged GHC v1.4.6 offline image files (from a verified Actions APK), original course slide images embedded in those files, the active GitHub crop script, the audited card IDs/media mapping, and visually inspected photo-crop previews. No external unsourced species photographs or new legal statements were inserted.
