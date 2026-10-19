# GHC Study — comparison matrices: placement and source-review plan

Reviewed/planned: 2026-10-19. Scope: **UI/content roadmap, not APK implementation**.
Repository baseline checked: v1.4.6 in `README.md`, `app/build.gradle`, `app/src/main/assets/schalenwild-matrix.js`, `.css`, `tools/inject_schalenwild_matrix.py`, and `.github/workflows/android-apk.yml`.

## Existing integration — preserve it
- Entry: **Study Cards → Schalenwild**.
- Existing matrix is inserted by `tryMount()` in `schalenwild-matrix.js` immediately **before `#studySearch`** in the rendered `#app`, if the heading inside `.study-category-head h1` is `Schalenwild` and `#studyHubBack` exists.
- Existing collapsed/expanded structure: `<details>`; currently `isOpen=true`. Do not duplicate this panel in Quiz Mode or add another home-ribbon button.
- Existing content: 7 species, 12-month calendar, Rut/Births/Both filter, gestation, standouts, source and unresolved Gamswild course contradiction.
- Existing release: **v1.4.6**; code packaged by GitHub Actions after recovery of v1.4.5 source APK. Need real S23 Ultra device testing. Verify workflow run/artifact afresh before distributing.
- Existing study-card **Details** and **Other Facts** remain slide-only. Outside-provider ideas and comparisons are extra interpretation, not replacements for class slides.

## Specific UI evolution
Keep one collapsible panel above search and the card grid, rename heading to **Schalenwild · Vergleichsmatrizen** (Schalenwild · Comparison Matrices). Keep one line of descriptive subtext: **7 species · see patterns and exceptions**.
Within it, replace `Both / Rut / Births` as the primary top-level control with three horizontal, horizontally scrollable views:
1. **Fortpflanzung** (Reproduction) — defaults to current 12-month view; the existing `Both | Brunft | Geburt` toggles become a SECONDARY control shown only in this view. Retain exact class values and discrepancy footnote.
2. **Geweih & Horn** (Antlers & Horns) — compare *Abwerfen → Schieben → Fegen* for antler-bearing deer and **permanent horns** for Gams/Muffel; show Schwarzwild separately as **tusks**, with N/A rather than invented months. Exact month cells should be added only after original GHC species slide checks for antler cycles.
3. **Erkennungsmerkmale** (Identification) — a compact comparison of 7 species on traits already checked in class sources, e.g. horns/antlers/tusks, ruminant vs omnivore, Niederwild vs Hochwild, adult tooth count (32/34/44). Never infer an unverified point.

Phone constraints: keep species label sticky when panning sideways if compatible with the Android WebView; 36 px minimum tap targets; table scrolled horizontally but no entire-page horizontal overflow; first view auto-selected when the panel opens. Color AND letters/icons for key states, accessible month names, source footnote. Allow collapsing notes instead of large uninterrupted explanatory paragraphs. Preserve native Android Back and prior study-card navigation. Preserve tab/filter selection and panel openness on category re-render if possible.

Suggested word-for-word headings:
- **Schalenwild · Vergleichsmatrizen**
- **Compare seven species. Look for patterns, then remember the exceptions.**
- **Brunft (rut) · Geburt (birth) · Tragzeit (gestation)**
- **Prüfungsmerker · Exam standouts**
- **Rehwild: Eiruhe delays development after mating.**
- **Schwarzwild: 3 months + 3 weeks + 3 days; births can occur outside the main season.**
- **Gamswild: class-slide timing needs confirmation** (keep short warning, detailed explanation in an expandable note).
- **Source: GHC course slides. Layout inspired by Waidwissen.**

Quiz-mode connection (future): question 4 (reproduction), question 1 (horns vs antlers), question 6 (teeth), and question 8/12 (antlers) can include an explicit **See Schalenwild matrix** navigation link **only when tested**; avoid embedding multiple clones of the chart.

## Other verified Waidwissen video-lesson topics, with matrix opportunities
The public Waidwissen article **Einführung zum Schalenwild** enumerates video-labelled sections `🎬 Trughirsche vs. Echte Hirsche`, `🎬 Wiederkäuergebiss`, `🎬 Wiederkäuermagen`, `🎬 Äsungstypen`, `🎬 Laufskelett und Fährte`, `🎬 Vergleich: Geweihträger und Hornträger`, `🎬 WaidMatrix zum Schalenwild`, `🎬 Geweihträger`, `🎬 Hornträger` and `🎬 Wiederkäuer...` topics. `Einführung zum Haarwild` lists `🎬 Decke, Schwarte und Balg`, `🎬 Gebiss (Beispiel: Fuchs)`, and `🎬 Hochwild oder Niederwild`. A separate Waidwissen page publicly identifies a weapons-handling YouTube series. **These are labelled lesson topics, NOT an independently verified full public YouTube channel upload catalog or full transcripts.**

Prioritized research to matrix:
- **High:** Antler/horn cycles (Schalenwild) — directly adds to current matrix, use original GHC species decks.
- **High:** Species dentition (Schalenwild) — 32 vs 34 vs 44 teeth; compare with checked GHC Section 1 Question 6.
- **High:** Wildfowl identifiers (Federwild) — swimming vs diving ducks and look-alikes; check GHC slides, esp. class Section 1 Questions 30–35.
- **High:** Predator identification (Raubwild) — martens/weasels and canine/feline groups; check Q22–28 and class animal decks.
- **Medium:** Antler vs horn, true vs false deer, rumination/feeding groups (Schalenwild) — classifications with contrasting features.
- **Medium:** Trees and cereal crops (Field/Forest) — useful visual identification matrix by leaves/needles, cones, awns; check Field & Forest sources.
- **Medium:** Game tracks (Schalenwild) — hoof/track clues; verify original class slides and avoid oversimplified identification.
- **Lower:** Hunting-dog types and uses (Hunting Dogs) — useful group comparison but verify directly against the class PDF first.
- **Not for automatic imports:** Jagdzeiten/legal rules, firearm-handling procedures and disease reporting obligations require current jurisdiction-specific official/class review.

## Source policy
Directly reviewed in this planning turn:
- GitHub v1.4.6 readback listed above.
- Google Drive: *GHC Section 1 - Game Biology Conservation Study.pptx* (connected slide text, particularly Schalenwild Q1–Q12, Federwild Q29–Q35, Raubwild Q22–Q28).
- Provider pages: https://waidwissen.com/einfuehrung-zum-schalenwild , https://waidwissen.com/einfuehrung-zum-haarwild , https://waidwissen.com/haarwild , https://waidwissen.com/merksprueche , and https://waidwissen.com/jagdschein .
- Existing repo audit: `research/waidwissen-schalenwild-intake.md` lists **seven original species PDFs checked in an earlier work phase**. Those PDFs were not all independently reread in this planning turn.

Access limits: Channel's public YouTube /videos listing did not expose a useful video catalog through available web access; this review is **not a comprehensive list of channel videos**. Full individual video transcripts were not accessed. Do not claim every suggested feature was taught in a specific YouTube upload. Text tables and mnemonic constructions must be original, linked to source, not copied from Waidwissen proprietary diagrams.

## Acceptance gates
- No duplicate matrix panel or regressions to study cards, quiz, back button, launcher icon, offline operation.
- Each displayed exam number traceable to specific instructor slide/page and named source; mismatches flagged rather than silently corrected.
- Selected matrix and active month/filter work on S23 Ultra Android WebView in portrait; landscape usable; no cut-off species names.
- Buttons and expanded state survive category navigation as intended; accessible voice labels.
- APK and GitHub Actions validation pass AND on-device manual smoke test performed before claiming fully verified.
