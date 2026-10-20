# GHC Study v1.4.6 — original Hunting Dogs image recovery (2026-10-14)

## Original classroom files actually inspected

The full 46-page primary class file **Hunting Dogs (202609).pdf** was opened and its embedded image assets directly inspected, rather than relying on the previous OCR-derived inventory. That revealed an image the earlier source audit missed:

1. **Page 4 — `Jäger Latein - Dog Parts`**. The class includes a large standalone black-and-white **dog anatomy diagram** with arrows labeling `Behang`, `Fahne`, `Rute`, `Decke`, `Pfoten`, `Widerrist`, `Kruppe` and other named body parts. This is directly appropriate for the `dogparts` study card. Image XObject **98**, **1183×719 JPEG, 131411 bytes**, SHA-256 `cf12124d1f9d64ad7508379af8782374e479e114ebea3bd73cd275949e2a694d`. Page 5 independently lists the English meanings for five parts. This corrects the earlier incomplete claim that the deck contained only a dog group photograph for this topic.
2. **Page 26 — `Dog Diseases`**: original warning-sign photograph mentioning `Tollwut` (rabies). Source image xref **457**, 511×388, SHA-256 `04b2030e8e4b02b5d043d0a660a96b7af507b3001cec3d69876ed0595dbfa9c7`. The picture is a **warning sign**, not a picture of a rabid animal or evidence of a current outbreak.
3. **Page 27 — `Why Worry?`**: two standalone examples, an original parasite/intestinal worm illustration xref **464** (456×541; SHA-256 `b98b1105633d60bb4759f9756f1deca35738d23525dc9e48774b1f97a0d9c744`) and an annotated tick life-stage image xref **465** (450×312; SHA-256 `c8d67c9732912d21ac4da7a506416c5706d8f9e83158fb44af2bbebd98cf2931`). The tick image contains the original intrinsic species labels; it is a visual example, **not proof every depicted tick occurs in Hessen**.

The original PDF credits pictures generally to Google image searches; **third-party reuse rights have not been independently established**. Repository remains private; this audit is not a license assessment.

## Implementation

- `dogparts` now points at the original image `media/dogparts-original-course-anatomy.jpeg` in the assembled APK with exact source filename, page, embedded-image xref and SHA-256 checks. It displays the drawing only, **not the full lecture slide**.
- `dogdiseases` now points at `media/study-dogdiseases-examples.webp`, assembled offline at 1050×380 from the three exact source JPEGs. It is a **picture-only gallery of examples** (rabies warning, worms, ticks), not a complete diagram of every bacterial/viral/parasitic dog illness, a veterinary diagnostic algorithm, or up-to-date medical advice.
- The gallery source JPEGs are individually hash-checked during assembly; `scripts/check_study_media.py` validates their exact original bytes, source page/xref sequence, and the output image mapping.
- Both changes are *image-only overlays*: all 117 source study-card nonimage fields and question/answer IDs remain unchanged and protected by the assembly invariant.
- `audit/study-media-review-20261014.json` now records **66 corrected full-slide/page displays out of 71**, with **five remaining**: `drivebrief`, `misfire`, `abschussplan`, `shotdistance`, `revierroles`. The prior unrelated Shot Placement error was fixed with its exact source diagram and remains hash-verified.

## Testing and open gates

An initial separate Android build for the new gallery failed in the *media test only* with `KeyError: exampleCardIds`. The manifest's new source-image gallery has `pictureSourcePageXrefs` and `imageSources` rather than the older six-bird-card `exampleCardIds`. The checker was corrected at commit `23a1f4994b59d6a1f277f61ea9f887141e529136` to distinguish gallery types and SHA-verify each underlying source. Do **not** call the combined two-image remediation Android-verified until the latest standalone APK and full Android 35 CI at that commit or later both pass.

Other outstanding release gates: five unresolved visual cards, precise source rights, two ambiguous `Jagdschuetz` and `Tiroler` worksheet terms, the original 77 historical etymology statements, 867 examination-answer/explanation factual truth checks, and a physical Samsung Galaxy S23 Ultra progress/offline/navigation acceptance run.

**Sources actually checked:** local original September 2026 Hunting Dogs classroom PDF, its page renderings and four directly extracted image XObjects; live private GitHub image mapping, registry and CI scripts; actual build logs, with failures distinguished from app content defects.
