# GHC Study v1.4.6 — visual inspection of every study-card image (2026-10-14)

## Evidence and verified counts

I extracted the **actual v1.4.6 standalone Android APK**, read the 117 study-card records and their `GHC_VISUALS` / `GHC_STUDY_IMAGES` mappings, and verified that each chosen `media/*` image physically existed in the ZIP. Then I created **five contact sheets**, inspecting all 117 rendered thumbnails visually.

- **117/117** cards had a resolvable offline media path, corresponding to **110 distinct** images in the original app.
- **71/117** study-card images visibly contained full classroom-slide/page layouts, multi-photo slide panels, presentation text, or slide chrome instead of standalone photos/illustrations. Some slides were reused between related cards.
- **1/117** has a specifically mismatched subject: `shotplacement` (Shot Placement) shows a raised hunting stand / `Hochsitz`, rather than a shot-placement image.
- The remaining **45** appeared to be standalone photography or diagrams at contact-sheet resolution. That does **not** certify exact species, license/copyright permissions, authenticity of source/page claims or historical/current-law accuracy.

Machine-readable review: `audit/study-media-review-20261014.json`. Run `python3 scripts/check_study_media.py` after assembling overlays to compare all card records, image files and visual-review labels. Default mode exits successfully if links are intact while loudly reporting the unresolved slide-layout/subject issues. `--strict` additionally blocks releases while visual defects remain. A generated `build/study-media-inventory.json` is available as a GitHub Actions artifact. This is **not** an image classifier and cannot independently determine that a photo is the right animal.

## Picture-only crop remediation — first assembled APK batch

The original 2013 guide images for four wildlife study cards contained an entire scanned/printed page. The embedded **animal photographs themselves** were usable and recognizable, so we retain the familiar source photo but remove the guide header, body text and page decoration:

| Card | Source picture | New standalone photo | Crop on original source pixels |
| --- | --- | --- | --- |
| Muffelwild (`mouflon`) | `Guide_08f_Mouflon_2013-08.pdf` full page | `media/study-photo-mouflon.webp` (450×463) | (160,180)–(610,643) |
| Murmeltier (`marmot`) | `Guide_08n1-5_Other_Game_2013-08.pdf` full page | `media/study-photo-marmot.webp` (568×257) | (104,245)–(672,502) |
| Seehund (`seal`) | Same guide's seal page | `media/study-photo-seal.webp` (537×356) | (114,184)–(651,540) |
| Bär (`bear`) | Class slide with photo plus notes | `media/study-photo-bear.webp` (580×381) | (138,85)–(718,466) |

The four crops were visually checked from the original APK pixels before implementation. `scripts/crop_study_slide_images.py` uses Pillow at APK assembly time to make the four WebP files and updates only the `STUDY_CARDS` image pointers and `GHC_STUDY_IMAGES` mapping inside the *assembled* HTML. **Text facts, notes, source labels, IDs, scoring and saved progress keys remain unchanged.** The original images stay in the repository for audit traceability.

The resulting standalone APK was successfully built in [GitHub Actions run 38496380116](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38496380116). A direct inspection of its APK verified **four new WebP assets with exact dimensions**, 117 study cards, **143 defined terms of 162**, and 242 total bundled media files.

**Open backlog after first assembled batch: 67 slide/page-like images plus the Shot Placement mismatch.** These are actively known visual defects, not newly missing files. Subsequent passes should prioritize animal-specific cropped illustrations from the student's existing slides and only use trusted external images when no suitable class photo exists. Do not copy whole-slide screenshots or text-only material back onto cards.

## Source and execution limits

- These four fixes are applied in both **Android APK assembly workflows**. The unassembled source file `app/src/main/assets/index.html` still retains the original source visual mapping until the assembly overlay runs; do not claim the raw HTML file itself has been updated.
- The pipeline installs Pillow and tests image paths; independent screenshot checks of the new Android build and actual Galaxy S23 Ultra physical installation must still be completed.
- The 2013 Murmeltier and Seehund content remains explicitly *historical*, not certified as current class-slide content; the visual crop does not change those source-status warnings.
- The app's separate factual-audit register remains **803/814** text-checked claim blocks with 11 historical course-guide exceptions. Etymology, 867 answer/explanation truth checks, source-page accuracy and current law are separate unfinished tasks.

Sources actually inspected: the downloaded standalone Android APK and decoded asset metadata; a full image-by-image visual contact sheet of all 117 current selections; connected course-source identification recorded in embedded asset provenance; GitHub branch files, pipeline scripts, and Actions build artifact evidence.

### 2026-10-14 seal crop QA correction

The first build’s seal crop included the original guide-page caption and part of its descriptive paragraph below the photograph. Manual inspection of the original source image identified the photograph bounding box at x=114–651, y=184–540; the crop script was corrected at commit `7d3ebfa1b73da1ebef1b4ec530edf22c441cf38b`. Prior batch-one APK artifact `38496380116` should **not** be distributed as picture-only-correct because it contains the older oversize seal crop. A fresh build is required for a properly caption-free seal image. No card prose, source claims or progress data changed.
