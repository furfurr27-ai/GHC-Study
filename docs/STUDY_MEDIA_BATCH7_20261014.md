# Study-media batch 7 — two original-course figure crops (2026-10-14)

The two remaining pictured lesson assets below were opened at the native **720 × 540** resolution from the actual prior GHC v1.4.6 Android package. Each card still displayed a full lecture slide. Unlike text-only slides, these had meaningful, individually separable illustrations. We previewed the exact rectangles before changing the image-only assembly script.

| Study card ID | Original lesson image | New crop (source pixels) | Content and evidence limit |
|---|---|---|---|
| `birdanatomy` | GHC `Bird Anatomy` classroom slide, containing internal organs, bones and a six-form German beak diagram | `(350,93)–(506,529)` | **Six original beak-shape drawings** and German figure labels; isolated from the composite slide. This illustrates beak morphology, **not** all skeletal/organ anatomy. |
| `handgunquota` | GHC historic `Hand Guns` class slide with text about handgun limits and multiple firearm pictures | `(460,333)–(700,498)` | **One standalone revolver photograph** from the original slide. This illustrates a handgun type, **not** the current legal quota, storage, transport or purchase authorization. All old classroom statutory text is outside the crop. |

The two rectangles are registered in `scripts/crop_study_slide_images.py`; their exact paths are generated as `media/study-photo-birdanatomy.webp` and `media/study-photo-handgunquota.webp` at APK assembly. Original slide graphics remain as provenance. These two edits change only `imageKey` and `visualId` for their study cards, with a build guard that verifies **all 117 non-image card objects** have exactly the original facts, IDs and names after assembly.

**Media audit after batch 7:** 117 cards total, 71 originally full-slide style, **53 isolated original-source figures**, **18 unresolved slide pictures**, one separately corrected exact-source Shot Placement diagram, and zero currently known wrong-subject images after the correction. The count does not certify that the other unmodified pictures are all semantically correct.

The attached course PDF `Hunting Dogs (202609).pdf` was also fetched and its text reviewed directly, including page 5 `Know the Parts of the Dog` listing *Rute, Fahne, Behang, Pfote, Decke*. It does **not** provide an obvious standalone annotated anatomy figure in its readable text. The `dogparts` picture remains pending; the existing group-photo image would be misleading as a diagram of those body parts.

**Sources actually checked:** the v1.4.6 APK's classroom slide image assets for the two cards, manually rendered crop previews, live GitHub source, and the original connected `Hunting Dogs (202609).pdf` for the dog-parts source limitation. No new law or exam answer claims are inferred from these pictures.

The exact post-batch-7 Android emulator CI must be verified separately from the standalone compilation result before this version is called emulator-validated.
