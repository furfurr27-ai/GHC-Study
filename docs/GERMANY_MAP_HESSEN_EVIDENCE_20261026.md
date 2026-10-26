# Germany state-map / Hessen season evidence and release checkpoint — 2026-10-26

**Status: implemented on existing draft PR #7 / `feature/offline-jaeger-field-guide-20261025`, CI and physical-device acceptance must be checked independently before merge.** Target: Jäger Field Guide v1.6.0 / 160. Original app ID `org.ghcstudy.v141`; standalone ID `org.ghcstudy.v146.standalone`. Original 19 illustrated species, 41 practical cards, study archive, glossary, Trophy Test, favorites, notes, scores and native system-Back bridge were not deleted or renamed. Retained storage keys `ghc-field-favorites-v1`, `ghc-field-notes-v1`; new independent key `ghc-selected-bundesland-v1`.

## Primary source inventory: actually checked in this change

| Source | Document / date | Relevant scope and sections | Limitations |
| --- | --- | --- | --- |
| `docs/GERMANY_STATE_MAP_SEASON_SPEC_20261025.md` (in this repository) | Development specification, 2026-10-25 | 16 Länder, states before animals, classification-sensitive indicators, offline & acceptance conditions | Specification, not legal authority |
| `app/src/main/assets/field-guide-data.js`, `field-guide.js`, `field-guide.html` | Existing application source, 2026-10-25 v1.5.1 | 19 IDs, photos, favorite/note persistence, page states, native Back bridge | Source inspection does not constitute runtime test |
| `app/src/main/assets/jungjaeger-data.js`, `docs/JUNGJAEGER_V151_20261025.md` | Existing 41-card reference and evidence notes | Six shared knowledge groups, official/context separation | Historical course context is not current state law |
| `app/src/main/java/org/ghcstudy/offline/MainActivity.java` and CI YAML | Existing Android/WebView source, SDK 35 | Package IDs and JS Back entry | Actual handset untested |
| [LJV Hessen corrected Jagd-/Schonzeiten](https://ljv-hessen.de/download/jagd-und-schonzeiten-bund-land-hessen/) | 2-page PDF, version effective **2026-04-01**, corrected **2026-05-18** per LJV site | **Page 1** deer class matrix; boar, fox, badger, hares, pheasant, pigeon, raccoon; **page 2** duck, rabbit, crow, magpie, numbered footnotes | Association consolidation, not a standalone legal authorization; cross-checked with ministry changes |
| [Official Hessian Gazette 2026 No. 14](https://rp-kassel.hessen.de/sites/rp-kassel.hessen.de/files/2026-03/gvbl_2026_nr_14_aendvo_hjagdvo_regelungstext.pdf) | Binding March 3 HJagdV amendment; effective 1 April 2026 | §1–§2, pp.1–3, revised species/classes/seasons | Amendment, not complete consolidation; checked against LJV table |
| [Later Hessen 2026 No. 32 amendment (secondary transcript)](https://www.umwelt-online.de/regelwerk/natursch/laender/he/z26_0032.htm) | May 20 act, effective 28 May 2026 | Article 3 changes wolf-specific provisions only; no change to the 19 mapped species periods | Official Gazette original preferred; secondary text reviewed |
| [Hessian ministry synopse, JagdV changes](https://landwirtschaft.hessen.de/sites/landwirtschaft.hessen.de/files/2026-03/synopse_hjagdvo_maerz_2026.pdf) | Government 10-page PDF, **2026-04-01** effective comparison | Page 1 §1/§2 addition & invasive species, pp.2–3 revised seasons, §2(4) population rules | Comparison of amendments only, **not full reprint** of all binding provisions |
| [Hessen official Jagd portal](https://landwirtschaft.hessen.de/wald/jagd) | Official landing page, checked 2026-10-26 | Current legal source hub | Online page can change after offline bundle |
| [BJagdG §22](https://www.gesetze-im-internet.de/bjagdg/__22.html) | Federal statute, checked 2026-10-26 | Parent/dependent-young, hunting- and closed-season protections | State and local exceptions/orders still apply |
| [@svg-maps/germany](https://github.com/VictorCazanave/svg-maps/tree/master/packages/germany) | SVG source by Victor Cazanave, based on MapSVG | Exactly 16 Länder polygonal paths, SVG viewBox `0 0 586 793` | **Licensed CC BY 4.0**, credited in app/docs. Alternative to preferred official BKG/geoBoundaries. Boundary geometry should be re-audited against official BKG before a public cartographic release. The bundled map is offline. |

The map source's own README attributes the original map to [MapSVG](https://mapsvg.com/maps/germany) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); the code transforms the original per-state IDs to ISO 3166-2, normalizes the labels and adds pointer/keyboard/list access. Map feature contains no external tile fetch, location API or geolocation permission. State border accuracy is not the same as cadastral/Revier accuracy.

## Coverage matrix (19 original field-guide species per state)

| ISO | State | Regulatory source / species coverage | Classified interval rows | Reviewed UTC |
| --- | --- | --- | ---: | --- |
| DE-BW | Baden-Württemberg | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-BY | Bayern | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-BE | Berlin | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-BB | Brandenburg | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-HB | Bremen | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-HH | Hamburg | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-HE | Hessen | Amendment synopsis + 18 May 2026 corrected calendar; 16 species verified, 3 marked unknown | 26 | 2026-10-26 |
| DE-MV | Mecklenburg-Vorpommern | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-NI | Niedersachsen | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-NW | Nordrhein-Westfalen | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-RP | Rheinland-Pfalz | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-SL | Saarland | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-SN | Sachsen | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-ST | Sachsen-Anhalt | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-SH | Schleswig-Holstein | No legal data reviewed; all 19 species unknown | 0 | — |
| DE-TH | Thüringen | No legal data reviewed; all 19 species unknown | 0 | — |

**Hessen 16 individually calendar-described species:** Rehwild; Schwarzwild; Rotwild; Damwild; Sikawild; Muffelwild; Fuchs; Waschbär; Dachs; Feldhase; Wildkaninchen; Fasan; Stockente; Ringeltaube; Rabenkrähe; Elster. **Three intentionally unresolved** field-card species: Graureiher, Auerwild, Wildkatze. Their status is UNKNOWN, not "closed" or assumed protected, pending cross-check of federal and state species-protection provisions.

At the species level, separate sex/age classes produce **AMBER** until the individual class is chosen and positively identified. HJagdV §2(4) requires special population-based caution for Feldhase/Stockente: data mark their windows AMBER even during calendar dates. Pheasant hens are marked a distinct NO GENERAL SEASON only if explicitly selected. Juvenile/adult Ringeltaube are distinct. Annual green status indicates only *general calendar window*, not a legal hunt. All green statuses require individual verification of license, hunting rights/Revier permission, hunt leader's Freigabe, dependent-young safeguards, hunting method, management plan, reserve/ASP orders and local restrictions.

## Deterministic, conservative offline rule engine

- Calendar dates interpreted using `Europe/Berlin`; bounded source review date and effective-date check, inclusive month-day intervals, crossing New Year.
- `GENERAL_WINDOW_OPEN` green when verified class general season overlaps, no specific unresolved class/condition in cached calendar.
- `GENERAL_WINDOW_CLOSED` gray when specifically verified class outside any season.
- `CONDITIONAL` amber for unresolved classes, population/management conditional caveat.
- `UNKNOWN_OR_STALE` amber for missing state, missing species, stale evidence or source conflict.
- `PROTECTED_OR_NO_GENERAL_SEASON` distinct red for specific independently verified no-general window (female pheasant).
- Separate source URL, review date, exceptions and "Not authorization" disclaimer on detailed card; same strip background as tile.
- No external requests to compute status. Optional source URL links require connectivity.

## Validation and acceptance

Automated regression addition: `tests/state-season-smoke.cjs` with all 16 map/List ISO IDs, Berlin/Bremen/Hamburg accessibility list selection, state switching, user notes/favorites, 19 species and 41 shared cards, conditional selection, seasonal boundary dates, source expiry, category navigation and Android Back handler. A specifically labelled SYNTHETIC fixture tests cross-year and leap-date logic without claiming it as hunting law. New `scripts/check_state_map_apk.py` checks packaged standard/standalone offline map, regulation engine, existing archive and reference assets. Both original CI build workflows retain their existing old study regression tasks. Emulator test script must additionally prove state map→Hessen→animal→Back; physical handset testing remains outstanding.

**Do not merge while CI, emulator, package audit or Samsung Galaxy S23 Ultra airplane-mode tests are unfinished.** CI success is separate from physical-device acceptance. Do not claim that any other Bundesland has been legally audited.
