# GHC Study — Shotgun danger-distance illustration (2026-10-15)

## Original GHC evidence actually checked

The connected original `Weapons - Overview (2020).pdf` was retrieved and inspected in readable-text form. In its **Ammo Travel Distance** teaching section it explicitly presents:

> Rule of Thumb: Shot size (in mm) x 100m = distance where shotgun ammo is still dangerous

The existing `shotdistance` study card (ID, version and facts unchanged) cites pages **50–51** of that lesson and states the same *approximate danger-distance* equation. The original card image was classified as a full-slide/large-layout screenshot, not an isolated standalone instructional figure. The exact visual page layout and original course photo/diagram XObject were **not** independently inspected in this continuation; a new illustration must not be misrepresented as recovered instructor artwork.

A separate independently checked external manufacturing glossary corroborates the same scope: [RWS, Gesamtschussweite](https://rws-ammunition.com/de/infotainment/glossar/G/gesamtschussweite) says `Schrotdurchmesser in mm x 100` is a **Richtwert** for total shot travel / area of danger, not effective hunting range (`Weitschussgrenze`). This corroboration is external, not additional class-slide text. The original classroom card's unrelated separate muzzle-brake statement remains unchanged.

## New illustration and evidence labeling

A self-contained, NEW SVG technical illustration depicts scattered pellets downrange, shows **3 mm × 100 m ≈ 300 m** as a *worked example of the classroom rule*, and displays the explicit warning **“CLASSROOM ESTIMATE · NOT A SAFE BOUNDARY.”** No graphical line is drawn between a danger zone and a supposedly safe zone, and the image is not to scale. The example derives arithmetically from the class/RWS heuristic; it is not an independent ballistics measurement, modern safety standard or safe firing-distance recommendation.

- Asset: `app/src/main/assets/media/shotdistance-course-danger-illustration.svg`
- Git blob SHA-1: `85314e425b7152ba428e9be0a85cc6859ae5bc03`
- Build overlay: `scripts/overlay_shotdistance_course_schematic.py`
- Original classroom title: `Weapons - Overview (2020).pdf`
- Course card cited span: 50–51 (the image metadata records this as a **span**, with exact one-based original image page deliberately unset)
- `authoredCourseIllustrations.shotdistance` in the visual register explicitly marks this as newly drawn, not an embedded original course JPEG
- Media CI checks its exact blob hash, source title/span and self-contained SVG mapping, alongside 117/117 offline images

The overlay changes only the target card's `imageKey` / `visualId` and the image registry. All underlying card details, exam questions/keys, saved progress identifiers and Android package settings are unchanged.

## Remaining gate

After the earlier source-grounded Misfire schematic and this new shot-distance drawing, **70 of 71** original full-slide study pictures are corrected, separately from the already repaired wrong-subject Shot Placement card. The only outstanding full-slide image is `abschussplan`. The `--strict` visual-media release gate must continue failing until that image is replaced with an accurate illustration of a **prospective harvest plan**, rather than the historical `Streckenliste` tally of harvested game.

This report documents source text and new authoring provenance; it does not assert verified original PDF graphics, complete German ballistics law compliance, or Samsung One UI hardware testing.
