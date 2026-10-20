# GHC Study — misfire classroom schematic provenance (2026-10-15)

## Exact source and limits

The original connected `Range - Saftey (20260211).pdf` (classroom file also cited in app as `Firearms_Range_Saftey_Overview_11FEB26_V2.0.pdf`) was fetched as readable text during this continuation. Under the heading **“Miss Fire procedures for any range”**, the slide says to keep the firearm pointed downrange for **10 seconds**, then carefully involve/hand it to the **instructor**. A separate passage warns against waving a firearm while turning or talking and bringing the barrel near one's face.

The existing `misfire` card has ID `misfire`, cited page `13`, and preserves the classroom details and 10-second value. The original media is a complete classroom slide thumbnail `media/ad8e3cca305d73e16a2c.webp` (not a stand-alone procedure photo).

**Evidence boundary:** Only extracted classroom PDF text and the existing GitHub card facts were directly checked this continuation. The slide's *image pixels* were not independently inspected, and this newly drawn artwork was not provided by the instructor. A fixed ten-second interval is a **course teaching point**, not a new current-law or universally applicable malfunction-clearing instruction. Follow the supervising range officer and current range procedures in practice.

## Change

A new standalone, self-contained vector **illustration** `media/misfire-classroom-original-schematic.svg` depicts (i) rifle maintained toward the downrange backstop, (ii) the 10-second class interval, and (iii) an instructor standing behind the firing line. The image is deliberately simple and does not depict opening an action, manipulating ammunition, or handing a potentially misfired firearm without supervision. It is NOT a recovered class photograph, extracted original diagram, or legal/safety certification.

- Original author-produced SVG Git blob SHA-1: `088dce056fdde3c4eba03793a7f1d95333e9722d`
- Asset: `app/src/main/assets/media/misfire-classroom-original-schematic.svg`
- Build overlay: `scripts/overlay_misfire_course_schematic.py`; only changes the `misfire` imageKey/visualId and registers the image's explicit authored provenance
- Manifest: `audit/study-media-review-20261014.json` now has a separate `authoredCourseIllustrations` type rather than mislabeling it an original PDF figure/crop
- `scripts/check_study_media.py` checks the actual Git blob content identifier, exact page/source, explicit authored status, and packaged file presence. SVG external scripts, embeds, and executable/link attributes are prohibited in the assembly overlay

All 117 study-card non-image facts, 867 question IDs/keys, glossary meanings, Android Java Back handler, app package IDs and saved progress keys remain unchanged.

## Build/release boundary

Both active workflows run the misfire overlay after the original classroom photo crops and owl mapping. The live media counts are now **69 corrected of 71 originally slide-like cards**, **2 still unresolved**: `abschussplan` (must depict a prospective harvest plan, not a historical Streckenliste) and `shotdistance` (danger-distance heuristic must not be depicted as a universal safe range). The earlier Shot Placement subject mismatch remains separately corrected.

The default media checker should pass all 117 *offline file mappings* after the overlay; the release `--strict` mode must continue to fail until the last 2 originals are corrected and source-verified. A successful build does not verify actual image rendering on a physical Samsung Galaxy S23 Ultra.

## Sources checked

1. Original connected classroom `Range - Saftey (20260211).pdf`, text extraction and full surrounding “Miss Fire procedures” and muzzle-direction sections.
2. Live GitHub `app/src/main/assets/index.html` `window.GHC_STUDY_CARDS`, original image mapping and page citation; live crop/overlay scripts and visual review register.
3. Existing course photo notes in `docs/STUDY_MEDIA_DRIVEBRIEF_AND_LAST3_20261015.md`, which previously documented why a generic firearm photo was rejected.

No external legal/safety source was used to modify classroom facts. The original class PDFs were not copied into the repository.
