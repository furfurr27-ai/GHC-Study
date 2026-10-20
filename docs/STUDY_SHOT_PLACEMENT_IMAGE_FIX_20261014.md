# GHC Shot Placement image repair — exact course-source extraction (2026-10-14)

## Confirmed defect and corrected image

The v1.4.6 study card `shotplacement` had been mapped to `GHC_VISUALS['high_seat']`, a photograph of a raised hunting stand (`Hochsitz`). That image is unrelated to the card's stated purpose: broadside `Blattschuss`, aiming for the heart–lung region.

The connected *original course deck* `Hunting_Techniques_V3.1_16FEB26.pdf`, class slide **23 of 33**, has the correct heart–lung shot-placement illustration for a broadside roe deer. The PDF page text says:

- `Shot Placement`
- `Shoot only broadside animals`
- `Shoot only in the heart-lung area (Blattschuss)`
- `Above the front leg, One-third to halfway up the body`

The page was visually rendered directly and inspected. Its isolated **embedded figure** (PDF xref **149**, source image 331×279 pixels) was independently extracted without the slide header, page body text, surrounding postmortem photographs or instructor logo.

For visual legibility and a compact offline package, a grayscale-threshold conversion was made, preserving the original anatomy and the circle/crosshair placement. Resulting source diagram:

- Repository path: `app/src/main/assets/media/shotplacement-class-diagram.png`
- Format: 331×279 monochrome PNG, 3,250 bytes
- Verified SHA-256: `c00ab76a236fc161b4594dbcd93182a4ed2b4324d5ae7ee52f0916cf6d60cb0f`
- Verified Git blob object: `4c909a898c48c4db257cb22b4f938d328e99a6a7`
- Source: original course PDF slide 23; **not** externally generated anatomy or a full-page screenshot

Build-time assembly (`scripts/crop_study_slide_images.py`) maps only `shotplacement` to `study_extracted_shotplacement`, sets the illustration's source attribution/page and removes the wrong `high_seat` card visual reference. All card text, course notes, factual checks, glossary terms, quiz IDs/keys, progress state and other cards remain unchanged.

## Audit handling and release gates

The original mismatch remains visible for traceability in `audit/study-media-review-20261014.json:originalSemanticMismatch`; the new `correctedSemanticMismatch` entry records the source and hash. Thus the visual-status counts after this batch are **117 cards**, **22 slide/photo crops**, **49 remaining slide/page-like card pictures**, **0 unresolved known subject mismatches**, and **1 corrected known subject mismatch**.

`scripts/check_study_media.py` verifies both the file hash and the card-to-diagram mapping in the fully assembled APK. The absolute result remains a **test build** until GitHub Actions smoke, APK, Android 35 emulator and physical Samsung Galaxy S23 Ultra checks are reviewed.

### Sources actually checked

- The original connected class PDF file (not just prior chat or saved memory), verified 33-page metadata, page-23 extracted text and rendered page-23 image, plus its embedded 331×279 source graphic
- Existing app's `shotplacement` card data and the incorrect `high_seat` visual mapping in the actual Android APK
- GitHub live feature branch and the uploaded Git source object SHA

No new hunting guidance, ballistic values, season laws or nonclass factual statements were introduced.
