# GHC Study v1.4.6 — batch 8 primary-class-image audit (2026-10-14)

## Scope and sources actually inspected

Continued from the last **fully Android 35 verified 51-image checkpoint**. Inspected the literal media assets in that Android APK, then fetched and examined original 2026 German Hunting Course PDFs directly from the linked class Google Drive:

- `Hunting Dogs (202609).pdf` (46 pages; page 5 contains dog-parts terminology but no clear anatomy drawing in extracted content).
- `Law - Weapons (20260819).pdf` (28 pages; page 8 contains the proof-mark chart, page 21 photographs two gun cabinets).
- `Disease - Parasites.pdf` (40 pages; page 3 contains a panel of lice, flea and tick specimens).
- `Range - Revier (20260922).pdf` (30 pages; page 20 contains an Erbenheim hunting-area map).
- `Disease - Kundige Person.pdf` (32 pages; page 5 has a field-game organ cross-section, page 6 has an *abnormal* lung example).
- `Game - Predatory Birds (202609).pdf` (30 pages; page 10 identifies the image of `Sperber` / Sparrowhawk).

These primary-source PDFs were downloaded locally to inspect their individual embedded figures and slide captions, **not committed wholesale** to GitHub or packaged in the APK. JPEG image streams were extracted directly by their PDF XObject IDs, preserving exact original image bytes. The repository's private feature branch stores only the selected JPEGs, annotated source/page/xref and SHA-256 hashes; the build verifies these on every assembly.

## Ten additional image-only corrections

| Card ID | Replacement actually selected | Primary source or image evidence |
|---|---|---|
| `birdanatomy` | Six original beak-shape figures with German anatomy labels, isolated from the classroom's Bird Anatomy composite without full-slide content | Original source PNG 720×540, crop (350,93)–(506,529) |
| `handgunquota` | Standalone revolver photo, **without the old slide's handgun-number text** | Original `Hand Guns` slide, crop (460,333)–(700,498). Image **does not assert a legal quota** |
| `gunstorage` | Open rifle-safe photograph, directly extracted without slide annotations | `Law - Weapons (20260819).pdf`, page 21, embedded image xref 115 |
| `gunmarkings` | Historic course proof-mark examples chart, intrinsic original marks and captions only | `Law - Weapons (20260819).pdf`, page 8, xref 62. **Not independently current-law-validated** |
| `parasites` | Original external-parasite figure: ticks, fleas and lice | `Disease - Parasites.pdf`, page 3, xref 33 |
| `revierrules` | Aerial view of example Erbenheim Revier with the course's original area boundary drawing | `Range - Revier (20260922).pdf`, page 20, xref 126. **Not an authoritative current boundary** |
| `kundigeperson` | Anatomy of field-dressed hoofed game, with visible internal organs | `Disease - Kundige Person.pdf`, page 5, xref 50. It depicts inspection subject matter, **not an individual's legal certification** |
| `diseasenames` | Classroom photograph shown among **abnormal lung examples** | `Disease - Kundige Person.pdf`, page 6, xref 53. This is **not a remote veterinary diagnosis**, nor a complete disease listing |
| `birdchecklist` | An unlabelled example gallery assembled from six *already verified original classroom* bird photographs | Bean Goose, Mute Swan, Curlew, Tawny Owl, Capercaillie, Kestrel. **Examples only, not a complete list of game birds** |
| `sparrowhawk` | The original, unobstructed `Sperber` photograph with visible head/body/tail, replacing the existing classroom screenshot with a yellow label covering the bird | `Game - Predatory Birds (202609).pdf`, page 10, xref 87 |

The underlying source objects are separately registered in `audit/study-media-review-20261014.json:originalFigureRemaps`. `scripts/crop_study_slide_images.py` creates picture-only crops or composites and installs each exact PDF figure into the corresponding card **only during Android APK assembly**. `scripts/check_study_media.py` verifies exact image path, source PDF title/page/XObject number, JPEG SHA-256, and all card paths; the app assembly separately asserts that no non-image field in any of the 117 cards is modified.

## Current counts and boundaries

- **117 total study cards**.
- **71 originally shown with full lecture slides/page layouts**.
- **53 isolated source-image crops** plus **7 original PDF figures** plus **1 class-bird photo montage** = **61 corrected slide-like media cards**.
- **10 remaining** cards still display source slides: `dogparts`, `drivebrief`, `misfire`, `transport`, `protectedwildlife`, `abschussplan`, `wildschaden`, `shotdistance`, `dogdiseases`, `revierroles`.
- The independent **Shot Placement subject mismatch** remains repaired with its original class diagram, exact SHA-256 check.
- **867 examination questions, their keys and explanations, 117 card textual facts, glossary 143 defined / 19 pending, app icon, storage IDs and Android Back implementation are unchanged**.
- 77 existing etymology paragraphs are still separately unverified against historical sources; 803/814 classroom claim text comparisons and 11 flagged historical-guide exceptions remain the previous factual-audit state.

## Verification gates

The early **51-image baseline** passed all three Android CI stages in [run 38521285106](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38521285106). The newer code changes must be judged by the exact *post-batch-8* Actions results, not assumed to pass because earlier APKs did.

Stand-alone APK compilation and binary/file tests verify packaging, not physical Samsung operation or image attribution beyond the source PDF. `--strict` visual-image gate intentionally remains blocking while 10 full-slide replacements are outstanding. The draft PR remains unmerged.

### Evidence integrity

The visually inspected crop previews, source-PDF page renderings and extracted-figure contact sheets were used in this pass; the proof-mark/legal, Revier-map and veterinary pictures are explicitly marked illustrative rather than current regulations or diagnoses. No external unsourced facts, new class card Details statements, weapon operating procedures or inferred word origins were added.

## Source-specific addendum: actual crop-damage photograph

The original `Law - Hunting (202608).pdf` was fetched directly from the linked classroom Drive folder, and its **page 47** was visually rendered. The slide explicitly captions a photograph as **Game damage (Wildschaden)**, showing actual disturbed farm soil/crop damage. The independent embedded JPEG **xref 241**, 450×280 pixels, was extracted directly without the surrounding slide text and committed as `app/src/main/assets/media/wildschaden-class-crop-damage.jpeg` (31,817 bytes, SHA-256 `1fe0bb80deb5b83598a7bdbb858a1792fdd45c3e5a92d1190a85bbfa69ca3220`). The `wildschaden` card now uses this original course photograph, not the earlier misleading generic wildlife collage.

This image supports *what the class illustrated*, not a legal finding regarding who pays, claim deadlines, or actual cause of the specific disturbance. A second original `Law - Nature and Animal (201902).pdf` slide at page 52 was inspected and depicts cornfield damage on satellite photos, but the cleaner photo from the more recent 2026 Hunting Law deck was chosen instead. No legal text or timed obligations were modified. Exact page/xref/hash are enforced by source-inventory tests.

**Revised media status (post-addendum):** 53 class-source picture crops, 8 exact embedded PDF figures, one six-image class bird gallery = **62 corrected slide-style images**, **9 unresolved** full-slide cards. Independent original Shot Placement error remains fixed. Last remaining IDs: `dogparts`, `drivebrief`, `misfire`, `transport`, `protectedwildlife`, `abschussplan`, `shotdistance`, `dogdiseases`, `revierroles`.

Additional primary files actually inspected in this addendum: `Law - Nature and Animal (201902).pdf`, `Law - Hunting (202608).pdf`, `Weapons - Ammo (20260214).pdf` and `Range - Saftey (20260211).pdf`. Their parsed relevant sections do not supply a trustworthy standalone shot-travel-distance or misfire demonstration illustration; none was substituted. Their text is classroom course material, **not independently verified current law**.
