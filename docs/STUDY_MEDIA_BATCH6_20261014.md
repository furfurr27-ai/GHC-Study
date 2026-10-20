# GHC Study media batch 6 — 13 course-derived standalone visuals (2026-10-14)

## Method

The original `GHC-Study-v1.4.6-Standalone-Install.apk` was opened directly and all **33 outstanding** card-media sources extracted from `assets/media/`. These are the actual images being shown by the app, not filenames or previous chat summaries. Three contact sheets and the relevant individual **900×675**, **900×507**, **720×540** course slide images were reviewed.

From those 33, the **13 entries below** contained self-contained subject photographs or *individual technical diagrams* that could be separated from full lecture-slide titles, logos, or surrounding explanatory bullets. An offline image-only overlay in `scripts/crop_study_slide_images.py` uses the rectangle coordinates below; it preserves all quiz IDs, study card prose, user progress and original source images.

| Card ID | Original classroom subject | Cropping rectangle (left, top, right, bottom) | Visual content |
|---|---|---|---|
| `goldeneagle` | Steinadler vs Schreiadler/Schelladler class comparison | (476,289,890,653) | Right-hand **Steinadler** photograph; species name supplied by original slide, label cropped away |
| `hornsignals` | Hunting Traditions, horn signals | (547,142,873,386) | Three hunters sounding `Jagdhorn` indoors |
| `waidgerechtigkeit` | Hunting Traditions, horn signals | (502,402,861,632) | Group respecting game with traditional horn signals at a hunt |
| `branchsigns` | Hunting Traditions, `Schützenbruch` | (518,158,876,580) | Hunter with harvested game and ceremonial branch |
| `lastbite` | Hunting Traditions, `Letzter Bissen` / `Inbesitznahmebruch` | (577,443,871,658) | Standalone original animal-and-branch engraving, without lecture text |
| `methods` | Hunting Techniques, methods | (352,69,894,448) | Original seven-photo class collage depicting stalking, sitting, driving, calling and other methods, without the slide body text |
| `followup` | Hunting Dogs, `Schweißhund` photo comparisons | (315,414,613,593) | Blood-tracking hound following a ground scent |
| `coldweapons` | Hirschfänger/Saufeder | (54,94,653,354) | Standalone original **weapon-anatomy drawing** showing both historic implements; intrinsic figure labels retained |
| `shotgunshell` | Shotguns, barrels and shell-chamber length | (192,72,526,531) | Original **shotgun/barrel and chamber measurement** technical schematic, without enclosing slide |
| `ammotypes` | Ammunition cartridge types | (121,78,319,498) | Original illustrated **cartridge and headstamp** examples; slide's left-side callout removed |
| `stecher` | Set triggers / Doppelzüngelstecher | (319,176,571,515) | Original **German double-trigger mechanism** technical drawing, with source arrows retained |
| `scopebasics` | Scopes, sight picture and eye relief | (111,234,347,510) | Three original **eye-relief/sight alignment** diagrams with intrinsic German labels |
| `trees` | GHC Field & Forest: the Big 5 German Trees | five source-pixel rectangles listed below | Five course photographs extracted separately and assembled in order *Oak / Fir / Alder / Spruce / Pine*, without lecture text |

**Tree montage rectangles:** Oak/Eiche (70,149,221,350); Fir/Tanne (410,166,707,316); Alder/Erle (31,372,219,623); Spruce/Fichte (303,380,536,565); Pine/Kiefer (611,351,873,557). The generated 900×360 WebP contains only course photographs and white spacing; the text Details section remains the reference for their names.

### Scope and content cautions

Some source diagrams contain integral numbering, leader lines and German figure labels. These remain because they identify functional parts and are not copies of the whole presentation slide. The `methods` and `trees` images are **picture montages**, not single photographs; neither includes lesson bullet text. `Waidgerechtigkeit` is represented by a real hunt ceremony image as a *tradition example*, not proof of ethical conduct. The original Golden Eagle class caption labels the subject `Steinadler`; the bird has not been independently species-verified by an ornithological source.

The following cards were **not** given arbitrary or misleading replacements: `dogparts`, `drivebrief`, `misfire`, `transport`, `diseasenames`, `kundigeperson`, `parasites`, `revierrules`, `protectedwildlife`, `abschussplan`, `wildschaden`, `gunmarkings`, `gunstorage`, `handgunquota`, `shotdistance`, `dogdiseases`, `birdanatomy`, `birdchecklist`, `revierroles`, and `sparrowhawk`. These still require primary slide asset extraction, carefully documented artwork, or other properly attributed illustrations. A poor crop of a text-only slide is not an acceptable fix.

### Checkpoint

The media ledger `audit/study-media-review-20261014.json` records **117 cards, 71 originally whole-slide/page images, 51 corrected image references during Android assembly and 20 remaining**, with the independently corrected source-authentic Shot Placement diagram counted separately. No known wrong-subject image remains in the corrected set. The source `index.html` still contains pre-assembly visual references by design; the assembly scripts generate the Android display overlays.

**Latest code commits:** `26c2c6dafcda6a434665307ae02a292e4b643090` image assembly, `3ef3b2f75a6a7bb2c0d780c0a1712d034d3a7bd1` audited status. Standalone and full Android CI are to be checked for these exact commits; **do not imply this 51-image state passed emulator without CI confirmation**.

### Sources actually checked

- Directly extracted images and mapping records from the earlier successfully built 38-image Android APK, including the class-source filenames
- Each listed original course-slide image and a manually inspected picture-only crop preview
- GitHub `scripts/crop_study_slide_images.py` and `audit/study-media-review-20261014.json`

No new hunting-law or disease-reporting claims, fabricated etymologies, or new study-card text were inserted.
