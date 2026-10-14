# Study-media batch 4 — nine picture-only crops (2026-10-14)

## Source review

The original, currently shipped study-card media were opened and visually inspected at source resolution. This pass targets full-slide screenshots for which the underlying teaching photograph can be isolated cleanly. No web image replacements, generated illustrations, captions, or outside factual claims were introduced.

The crop coordinates in `scripts/crop_study_slide_images.py` are **absolute pixel rectangles in the original shipped classroom slide image** (left, top, right, bottom). The build-time overlay updates only image references in the card objects; card text, answer IDs and keys, class source text, glossary data, saved progress keys and app version remain unchanged.

| Card ID | Original classroom material | Chosen photo and precise crop |
| --- | --- | --- |
| `capercaillie` | `Capital Game Birds` comparison | Auerwild male, display fan/head visible; (37,56)–(270,211). Bottom legs removed to avoid numbered slide badge. |
| `blackgrouse` | Same `Capital Game Birds` comparison | Birkwild male courtship/fighting image, (302,107)–(612,252); top numbered badge excluded. |
| `blackkite` | `Milane (Kites)` species-comparison slide | Perched dark kite, (592,75)–(886,426), excluding photo overlap/caption below. |
| `brantgoose` | `Gänse (Geese)` numbered species plate | Ringelgans/Brent Goose photograph, (625,262)–(834,465), excluding species badge. |
| `canadagoose` | Same geese species plate | Kanadagans photograph in flight, (409,476)–(792,661), excluding red number 3. Tip of right wing outside crop. |
| `combinationguns` | `Firearms Terminology: Drilling` class slide | Three-barrel Drilling muzzle end, (650,79)–(879,231), excluding text and other firearms. |
| `rangesafety` | `SHOOTING RULES` GHC range safety slide | Standalone side-on photograph of firearm handling, (436,33)–(885,185); this is an illustrative course photo, not a claim of safe technique. |
| `doggroups` | `Know the Dogs and their Uses` classroom slide | Original group photo of four dogs, (527,491)–(869,654). Shows examples, **not** all six types. |
| `kennel` | Class photograph of outdoor dog kennel | Cropped kennel enclosure, (76,73)–(688,464), removing peripheral framing. |

The nine selected pictures were independently previewed in crop-only contact sheets before commit and inspected to ensure they contain no slide titles, classroom tables, numbered badges or text. Some image borders omit feet or peripheral wings; the animal's identifying head/body remained.

## Evidence status

- Original register: **117** study cards and **71** slide/page-like images.
- Previously corrected from original slides: **22**.
- Additional nine selected in this batch: **9**.
- Total study-card photograph fixes implemented at assembly: **31**.
- Known incorrect subject `shotplacement`: **1 previously corrected** with the exact February 2026 classroom heart–lung image, integrity-hash enforced.
- Remaining slide/page-like images: **40**. Strict image-content release gate still fails intentionally until all are repaired and manually checked.
- Glossary remains 143 defined / 19 pending; question-bank and class-fact audit totals unchanged.

The assembly pipeline validates all 31 cropped card paths and the exact Shot Placement diagram. A successful Android build alone does not prove image subject authenticity or physical Galaxy S23 Ultra functionality. The latest full CI and standalone build must be checked independently against their precise commits. No release merge has been authorized.

## Sources actually checked

The existing v1.4.6 standalone APK image files, the crop QA sheets made from those originals, the feature branch's `scripts/crop_study_slide_images.py` and `audit/study-media-review-20261014.json`. No primary source was assumed checked merely because its filename was recorded in older notes. The exact original source deck/page for each image still requires systematic cross-reference where the APK image metadata does not identify it.

## Fourth-class image overlay: Firearm Action Names

The existing `firearmactions` card previously displayed its entire `Firearms Terminology` lesson slide, with paragraphs describing four actions. The original source image was inspected directly. Four photographs depicting a lever-action rifle, a pump-action long gun, a semiautomatic shotgun and a break-open combination gun were extracted **from that same source image**. The assembly script lays them out in four unlabelled rows on a plain white background, preserving the photograph pixels but not the slide typography.

Source pixel rectangles: lever `(510,90,830,174)`, pump `(508,196,837,260)`, semiauto `(508,284,863,331)`, and combination `(668,333,853,475)`. The assembled montage is `media/study-photo-firearmactions.webp` at 660×580 pixels. It does not add any invented schematic or explanatory text. All firearm-action names continue to be taught through the card's existing Details text.

This one photo-only montage makes the count **32 corrected visual cards and 39 remaining original slide/page images**. The original `firearmactions` slide file remains in the APK for provenance until source-media packaging is cleaned up; this does not imply the user sees it on the revised card. No question-bank content, saved progress IDs or study-card facts were edited.

**Validation:** Android build CI and physical device testing must be checked at the exact post-montage commit `9108b473131f8a4a5ab70cf549f84e715123942e` or later. The earlier 31-crop APK and its test success do not validate this additional montage.
