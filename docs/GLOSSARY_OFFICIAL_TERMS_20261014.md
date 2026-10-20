# GHC Study glossary — independently verified German authorities (2026-10-14)

This batch uses three **official government references** for worksheet headwords that did not have an exact English definition in the inspected 2026 GHC slide text. These are indexed separately from class-slide claims, historical guide claims, and Jägersprache etymology.

| Worksheet term | English glossary definition | Official source actually checked | Evidence label |
| --- | --- | --- | --- |
| `Bundesverwaltungsamt (BVA)` | Federal Office of Administration | [Bundesverwaltungsamt official site](https://bva.bund.de/); describes the autonomous federal administrative authority and its central government functions | `official_external_not_class_slide` |
| `Europaeischen Feuerwaffenpass` | European Firearms Pass | [Bundesportal (Hessen) — European firearms pass](https://verwaltung.bund.de/leistungsverzeichnis/EN/leistung/99089010012000/herausgeber/HE-9982158/region/060000000000) and [federal service portal detail (updated 2026-03-04)](https://verwaltung.bund.de/leistungsverzeichnis/DE/leistung/99089010012000/herausgeber/BY-3421/region/09) | `official_external_current_regulatory` |
| `Veterinaeramt` | District veterinary authority / veterinary office | [Bundesportal (Hessen) — notification of suspected animal disease](https://verwaltung.bund.de/leistungsverzeichnis/DE/leistung/99110023000000/herausgeber/HE-8967785/region/060000000000); references notification to the competent `Veterinäramt` | `official_external_hessen` |

The European Firearms Pass is for **temporary cross-border travel with listed firearms**; it is **not a blanket permission** to bring firearms into any country. Destination/transit-state rules and additional documents still matter, and the app should not be treated as a legal clearance decision. We deliberately do not copy the portal's jurisdiction-specific number of weapons, validity period, fees or eligibility rules into the glossary.

The local `Veterinäramt` description does not classify any specific game disease as reportable; reporting obligations require separate current law verification. The BVA is not represented as the issuer of the Jagdschein.

None of these entries claims that the class slides provided an exact translated headword. All three original `etymology` fields remain blank.

**Current status:** 162 indexed / **143 defined / 19 pending**. This batch changes the offline glossary and related functional tests; it does not touch 867 exam keys/questions, 117 study cards, saved progress IDs or Android app version. App assets are still offline: cited URLs are text attribution, not required to load the application.

## Sources actually checked

1. Original `Jägersprache1.xlsx` worksheet, fetched directly from the connected Google Drive file, contains each term without an English definition.
2. The three official-source webpages above, retrieved in this turn.
3. GitHub `app/src/main/assets/glossary-data.js` and `tests/functional-smoke.cjs`, modified on the active unmerged branch.

This is an independent term-definition audit, not a completed review of historical Jägersprache origins or current German hunting/firearms law.
