# Developer-ready implementation spec — Germany state map, localized Jungjäger guide & hunting-season indicators
Version: 2026-10-25. Scope: NEXT planned feature (v1.6.x); specification only, no feature code yet.

## Live project starting point
Repository: furfurr27-ai/GHC-Study; existing development PR #7, branch feature/offline-jaeger-field-guide-20261025. Current verified development version v1.5.1, code 152, package org.ghcstudy.v141; separate install variant org.ghcstudy.v146.standalone. Android app uses WebView with bundled assets/field-guide.html, field-guide.js, field-guide-data.js (19 species), jungjaeger-data.js (41 practical cards) and original archive index.html. Do not recreate, destroy or overwrite existing animal pictures, source data, quiz progress, notes, glossary or trophy tests. Before making changes, re-read current main, PR head, README.md, NEXT_ACTION.md and CI state. Resolve any newer commits first.

## Target user experience
On app launch, the first page is an offline, interactive map of the 16 German Bundesländer. Distinct, tappable SVG state outlines, high contrast, keyboard/assistive labels, and a synchronized alphabetical accessible state list (critical for Hamburg, Bremen, Berlin). No auto-location or permission request. Previously used state is highlighted but user can change it; provide one-tap Continue to last state. After tap, open a chosen-state home with large state name, review status/date, Change state, and grouped links:
- Wildarten / Animal cards
- Jagd- und Schonzeiten / Seasons
- Jungjäger-Wissen / Customs, horn and etiquette
- Jagdarten / Methods
- Sicherheit / Safety
- Jagdrecht / State & federal law
- Nach dem Schuss / Wounding, tracking and meat handling
- State specifics / Landesbesonderheiten and official current sources
Use German terms with concise English equivalents. Show common content in every state; add overlays only when supported by an actual relevant state source. Save state locally under a NEW storage key; never rename prior favorite, Revier-note or quiz-progress keys.

### All 16 states (ISO 3166-2)
DE-BW Baden-Württemberg; DE-BY Bayern; DE-BE Berlin; DE-BB Brandenburg;
DE-HB Bremen; DE-HH Hamburg; DE-HE Hessen; DE-MV Mecklenburg-Vorpommern;
DE-NI Niedersachsen; DE-NW Nordrhein-Westfalen; DE-RP Rheinland-Pfalz;
DE-SL Saarland; DE-SN Sachsen; DE-ST Sachsen-Anhalt; DE-SH Schleswig-Holstein;
DE-TH Thüringen.

## Map assets
Bundle a small, accurate, simplified 16-polygon interactive SVG generated from a provenance-checked and correctly licensed official BKG VG250 Länder boundary layer (https://www.bkg.bund.de/SharedDocs/Produktinformationen/BKG/DE/P-2025/250911_VG250.html) or a credited CC BY geoBoundaries Germany ADM1 layer (https://www.geoboundaries.org/countryDownloads.html). Preserve named attribution/license in docs and in the app; verify license before publishing asset. SVG paths must carry the stable ISO code, accessible name and hit region; city states need an accessible list or enlarged selection targets. Bundle offline, no runtime external map libraries/tiles or geolocation.

## Data model: base + jurisdiction overlay
Keep shared animal biology and most Brauchtum cards global. Add reviewed state datasets as independent assets (suggested assets/states/DE-HE.json, etc.), an official-source registry, and a pure deterministic season evaluator. Every state includes:
- state code/name, jurisdiction schema version, lastReviewedUTC, currentSource/effective dates, official source URLs and notes
- species ID mapped to existing exact 19 IDs, and separate sex/age/management classes where necessary
- intervals with start/end calendar dates (inclusive), crossing-year semantics, legal basis/sections, effectiveFrom/effectiveTo, exception notes, and specific place restrictions
- distinction between law, binding state order, official administrative guidance, association summary, custom, and inference
- reviewNeeded/unknown markers rather than blank records implying Closed
- local restriction warnings for ASF/ASP, wildlife diseases, reserves, protected dependents, management plans and host Freigabe

DATA MUST NOT be created from memory or copied unsourced across states. A public state overview is NOT sufficient to claim every species/class interval was verified. Source URLs and as-of dates must be traceable per entry. Preserve an evidence table listing the exact regulations/sections reviewed and gaps.

## Season engine and card appearance
Inputs: selected state + existing animal ID + optional verified sex/age class + date in Europe/Berlin + state rule metadata. Derive status dynamically; do not store a manually chosen Open field. Evaluate calendar ranges including New Year boundaries, leap years, inclusive start/end, pending amendments and conflicting sources. Return:
- GENERAL_WINDOW_OPEN (subtle GREEN background on both list tile and opened baseball card) only where a current verified state rule confirms a general window applicable to the displayed class with no unresolved class ambiguity
- GENERAL_WINDOW_CLOSED (slate/GRAY background) only when verified regulations confirm no general open interval for the class on that date
- CONDITIONAL (AMBER) when the season depends on age/sex, management conditions, territory, special orders, or where class is not selected; **never** make a species-level green card when only certain classes are open
- UNKNOWN_OR_STALE (neutral/AMBER) when source is missing, contradictory, outdated or not yet individually audited; **never** infer Closed just because there is no entry
- PROTECTED_OR_NO_GENERAL_SEASON (distinct muted/RED outline and explicit text), based only on verified status, not assumptions.

Badge words MUST say "Allgemeine Jagdzeit" or "General season window", never "Schuss frei", "Legal to shoot" or "Huntable now." Badge always includes season start/end or "conditions vary", source title, as-of/review date, and a visible "Not authorization" note. Provide text/icons as well as color, and check WCAG AA contrast. Opening an animal card MUST show its selected-state strip and classification summary; changing state recolors cards immediately. NEVER let user-entered notes or device date override source requirements. If review freshness cannot be established, downgrade to UNKNOWN_OR_STALE even if numerical range mathematically matches today's date.

Legal caution always visible: even when a general window is open, hunting still depends on valid Jagdschein and Revier permission, Bundes-/Landesrecht, management plans, species/class ID, dependent-young protection, local orders, restricted areas, disease zones and hunt-leader instructions. Refuse to imply statewide status can adjudicate location-specific permission. Reference BJagdG §22: https://www.gesetze-im-internet.de/bjagdg/__22.html.

## State-specific cards beyond seasons
Within each category surface federal/common cards plus additions/cautions from the selected state's law, while labelling legal scope. "Strecke legen", Jagdhorn and most customs stay shared; do not invent differences. Display a Landesbesonderheiten section with actual cited state provisions only. Distinguish statutory rules, VSG 4.4 safety, local host protocols and nonbinding customs. Allow "Official state rules (online)" links but do not pretend an offline device has synchronized.

## Implement Hessen first; do not fake the other 15
Hessen source hierarchy: check official Hessen law hub (https://landwirtschaft.hessen.de/wald/jagd), official current HJagdV and revisions effective 2026-04-01, and the LJV Hessen corrected Jagd-/Schonzeiten PDF dated 2026-05-18 (https://ljv-hessen.de/jagd-in-hessen/jagd-schonzeiten/). Read actual regulation/table, not merely summary. Populate all 19 species' records only where independently supported and distinguish missing classes. Other 15 states must be selectable, show all shared content, official source landing links when verified, and honest "season data not yet verified for this state" warnings; NO green on those unpopulated states. Use a state coverage matrix (16 rows: source verified, wildlife coverage count, classes reviewed, exceptions, last reviewed).

## Tests and acceptance
1. All 16 SVG paths and list controls map to same ISO state IDs; tapping Berlin/Bremen/Hamburg works via list.
2. State selection saved/reloaded; new-state home, proper title and category overlays, Change state and Android system Back work.
3. Animal search, all 19 photographs, glossary, 41 Jungjäger cards, favorites, notes and full old study archive still work offline with airplane mode.
4. Automated fixtures (clearly marked SYNTHETIC, not hunting facts) cover ordinary open/closed, conditional age/sex, unknown, expired evidence, source conflict, protected/no-general-season, Nov→Feb crossing, leap date and exact start/end dates.
5. Both animal TILE and inside BASEBALL CARD visibly recolor; badges and review citations match selected state after switching twice.
6. No missing-state or generic federal fallback silently turns green. Missing dates never count as a closed season.
7. Accessibility test: each state can be selected without map precision; status is readable without color; responsive on Galaxy S23 Ultra and landscape.
8. CI builds ordinary and separately installable APK, confirms SVG/state data packed and no external network requirement; Node/jsdom source+functional tests and Android 35 emulator home→state→animal→Back→Study archive regression pass.
9. Phone acceptance (explicitly not yet done): install side-by-side debug APK, airplane-mode map, Hessen card/status, other state unknown states, original GHC app unaffected. No merge before actual CI + phone check.

## Finite deliverables and stop condition
Commit map assets/source license, state registry and Hessen data with source table, deterministic evaluator, new navigation, tests, README, checkpoint and release APK workflow. Do not expand species database, overhaul the study app, or build a live data service as a side task. Do not claim all 16 states fully sourced until they really are. Bump Android version monotonically after inspecting live HEAD (candidate v1.6.0/versionCode 160, not an instruction to overwrite a newer build). Open/update a PR; preserve original PR #7 until its merge/release policy is resolved. Stop at the tested map + honest Hessen-first prototype; only then plan remaining-state research as separate bounded batches.
