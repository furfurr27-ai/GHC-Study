# GHC Study — original-source Transport illustration correction (2026-10-14)

## Direct class PDF inspection

The original `Law - Weapons (20260819).pdf`, fetched from the connected GHC classroom Google Drive, was inspected as a 28-page PDF. Page **23** is titled **Cases** and shows several gun carrying cases. Its original embedded photograph **xref 120** displays three closed long-gun cases. This is a photograph from the *actual classroom material*, not a screenshot of the complete lecture slide, a stock substitute, or a generated weapon illustration.

The photo is suitable for the `transport` study card as an **illustration of firearm cases**, but it **does not prove** that the photographed cases, locks, firearms or their contents meet current German transport regulations. The original classroom text on page 22 is historical course teaching, not a verified current legal clearance decision; it was not repeated in the image.

## Implementation and provenance

- Original PDF: `Law - Weapons (20260819).pdf`
- PDF page: **23** (one-based)
- Original PDF image XObject: **120**; exact `/DCTDecode` JPEG
- Original figure bytes: **47,766**
- Git blob SHA-1: `a57381acb774719e76f7c7715184cd3199ba3968`
- Original image SHA-256: `434832c3a8490570733b563bfce5aa7b0c4b4bdd0ffe230f01f7490745803e20`
- Private repository asset: `app/src/main/assets/media/transport-original-hunting-cases.jpeg`

`scripts/crop_study_slide_images.py` now points the `transport` card to this local original JPEG **at Android APK assembly**, using the existing provenance fields `source`, `page`, `originalPdfEmbeddedImageXref`, `originalFigureSHA256`. `scripts/check_study_media.py` verifies all these source identifiers and the exact file hash. Only the card's image-key / visual-key mapping is permitted to change; the assembly-time guard rejects any change to non-image study-card facts, titles, notes, or IDs.

`audit/study-media-review-20261014.json` records the remap. Updated counts: **117 study cards, 71 originally slide/page-like pictures, 53 individual picture crops + 9 original embedded PDF figures + 1 original six-photo gallery + 1 original classroom-photo reuse = 64 corrected slide/page images; 7 unresolved full slides**. The independent Shot Placement wrong-subject error remains fixed and source-hash-verified.

The seven remaining are `dogparts`, `drivebrief`, `misfire`, `abschussplan`, `shotdistance`, `dogdiseases`, and `revierroles`. These still require appropriate visuals; do not use the old `Streckenliste` harvest-record form as an `Abschussplan`.

## Evidence and release limits

**Actually checked:** original connected classroom `Law - Weapons (20260819).pdf`, its page 23 rendered as an image, individual embedded image xref 120 viewed alone, extracted JPEG byte length and SHA-256, live GitHub asset and assembly scripts. No new firearm-handling procedure or present-day weapons law has been added.

A GitHub Actions standalone APK build at the new source commit is evidence of packaging, not a physical Samsung Galaxy S23 Ultra test. The full Android 35 emulator job, 7 remaining slide images, 867 factual exam-answer review, and independently sourced Jägersprache histories remain separate release gates.
