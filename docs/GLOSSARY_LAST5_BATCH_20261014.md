# GHC Study — two final contextual glossary definitions (2026-10-14)

## Sources actually checked, with explicit evidence tiers

The source headwords `Einwachser-Mufflon` and `Stangensulze` appear in the connected `Jaegersprache1.xlsx` worksheet, which supplies German terms but **no definitions**. I checked readable text from the original class `Game - Mufflewild (2015).pdf`, `Range - Revier (20260922).pdf`, and `Hunting Dogs (202609).pdf` instead of relying on a prior conversation summary.

- The Muffelwild class lesson explicitly says `Schnecken – horns`, horns are **not shed**, and grow continuously. It does **not** explicitly supply the longer word `Einwachser` in its extractable slide text.
- The accessible Revier lesson text does **not** explicitly define `Stangensulze`; the worksheet includes it as its own bare headword. Do not claim it appears in the Revier PDF based solely on familiarity with salt licks.

Two independent and attributable external-source checks were used to fill these exact English meanings.

| Worksheet ID / German | English meaning added | Checked source, evidence type and limit |
|---|---|---|
| `x100 Einwachser-Mufflon` | **Mouflon ram with inward-growing horns** | [Deutscher Jagdverband — Mufflon species factsheet](https://www.jagdverband.de/zahlen-fakten/tiersteckbriefe/mufflon-ovis-ammon-musimon), explicitly names `Einwachser/Scheuerer` for a ram whose horn tips grow into its neck or jaw; [Bavarian State Wildlife Portal — Muffelwild](https://www.wildtierportal.bayern.de/wildtiere_bayern/096779/index.php), independently corroborates. **External national hunting association + state agency**, with class *horn-growth context only*. |
| `x144 Stangensulze` | **Post-mounted salt lick for game animals** | [JÄGER magazine — Stangensulze](https://www.jaegermagazin.de/jaeger-praxis/salzlecke-bauen-fuer-rehwild-rotwild-und-co-anleitung-fuer-jaeger/) describes salt on a post/trunk with rainwater runoff; [Jagdschule AJN — Jagdbetrieb education](https://jaegerpruefung-ajn.de/wp-content/uploads/2022/04/Fragen-Jagdbetrieb-Kurzfassung-22.ppt.pdf) distinguishes indirect Stangensulze from a direct stump lick. **Hunting press + independent training material**, not a class-slide quotation or a statement on local legal permission. |

Both original `etymology` fields remain deliberately blank; no historical or poacher-code story is invented. No handling instructions, required dimensions, hunting regulation or veterinary conclusions are imported.

## Vocabulary release gate

After committing these entries, glossary dataset: **162 indexed, 159 source-defined, 3 pending**. The remaining worksheet headwords are `Abschussgebuehr`, `Jagdschuetz`, and `Tiroler`, all still blank in `english` with `status=pending`. These deserve **exact contextual** confirmation:

- `Abschussgebuehr`: often an animal-specific harvest/shooting fee, but a published legal or contractual source is needed before giving a universal classroom definition or implying an amount.
- `Jagdschuetz`: don't silently equate it with `Jagdschutz` (game protection), `bestätigter Jagdaufseher` (confirmed game warden), or `Wildschütz` (a historically ambiguous hunter/poacher word); identify precisely what worksheet author intended.
- `Tiroler`: may be shorthand for `Tiroler Bracke` in a dog lesson, but the directly fetched `Hunting Dogs (202609).pdf` extract **did not include that headword**. It could also mean a person from Tyrol. Do not make the dog-breed sense an unqualified fact.

`tests/functional-smoke.cjs` now tests both exact meanings, blank word origins, total **159/3**, and the three exact pending names. It also retains existing browser/UI, question-bank and Android-native Back checks. Neither card text nor the 867 questions/answers nor app data keys changed.

**Other unchanged gates:** Android media audit currently 63 corrected full-slide image cards / 8 unresolved; old Shot Placement mismatch fixed. Android 35 emulator pass before this batch at [run 38541009317](https://github.com/furfurr27-ai/GHC-Study/actions/runs/38541009317). This new glossary batch requires its **own CI result** before calling the assembled APK validated, and a Samsung Galaxy S23 Ultra physical test is not available.

Reviewed source types: original Google Drive classroom PDF extracts and Jägersprache worksheet; two external hunting/wildlife authority pages and two external hunting education/press sources; live GitHub glossary and regression scripts. Not all original slide graphics were inspected for these two specific terms; the source-evidence label reflects that limitation.
