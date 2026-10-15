# GHC Study photo-only cards — 2026-10-14 continuation (batch 5)

## Source-based image extraction, not slide reproduction

I inspected the actual slide-image assets packaged in the audited v1.4.6 APK (not merely filenames or previous descriptions), cropped photographic regions from the original classroom material, and previewed each selection. The build-time Python/Pillow overlay updates only the relevant study-card image mappings and generates one picture-only offline `.webp` per card. The source media and class text are retained unchanged for audit reproducibility.

| Classroom study card | Original picture subject | Source-pixel crop `(x1,y1,x2,y2)` | Content caveat |
|---|---|---|---|
| `labrador` | Labrador Retriever in `The Best / a Good all around dog` slide | `(167,113,546,333)` | Class example of an all-round hunting dog |
| `dogcert` | Hunter and tracking dog wearing high-visibility vest during training | `(432,71,686,253)` | Illustrates training, not proof of a certification standard |
| `trichinella` | Photomicrograph of encysted `Trichinella` larva | `(607,264,895,439)` | Class specimen reference; not an independent pathology diagnosis |
| `rabies` | Open-mouthed dog image used on class `Rabies – Tollwut` slide | `(652,42,800,203)` | Illustrative only; aggressive appearance does **not** establish rabies |
| `asf` | Recumbent wild boar on game-disease class slide | `(76,88,700,394)` | Illustrative only; a dead animal's appearance alone is **not** evidence of ASF |
| `footmouth` | Photograph of a diseased cloven hoof from FMD class slide | `(648,388,880,492)` | Classroom lesion example; current disease/reporting conclusions are not inferred from this picture |

Six earlier cards were also corrected this continuation: `capercaillie`, `blackgrouse`, `blackkite`, `brantgoose`, `canadagoose`, `combinationguns`, `rangesafety`, `doggroups`, and `kennel`. A further `firearmactions` card was changed to a no-text photo montage using four original action-type images from its class slide (details in `docs/STUDY_MEDIA_BATCH4_20261014.md`).

## Current media ledger

- Original class image set: **117** cards, **71** displaying full lecture slide/page/collage instead of an isolated photo/diagram, **1** wrong-subject Shot Placement photo.
- Photo-only source remediations now implemented in assembly: **38**.
- Wrong-subject `shotplacement`: already replaced by the February 2026 roe-deer heart/lung diagram, exact SHA-256 verified.
- Original slide/page pictures left to replace: **33**; the image-quality release gate remains open.
- 143 / 162 glossary entries defined; 19 terms pending. No glossary meanings or etymology notes were edited in this image pass.
- The 867-question examination pool and study-card factual content have not been changed. Previous factual audit remains 803 checked classroom text blocks and 11 historical-guide exceptions.

## Evidence and limitations

Directly checked original assets: the bundled class-slide images for all above named cards, not internet image substitutes. Preview contact sheets saved in the working environment prior to source changes. The registered image paths, crop parameters, and SHA-verified original Shot Placement asset are enforced by `scripts/check_study_media.py` during CI. Image-path existence and build compilation cannot establish appropriateness of every remaining picture; the 33 unresolved slides and physical Galaxy S23 Ultra test remain outstanding.

Only mark this 38-image batch **verified for Android** after seeing the exact commit's success for **functional smoke, APK build, and emulator-smoke**, and mark it a TEST build rather than a finished release until the rest of the image and factual audit passes.
