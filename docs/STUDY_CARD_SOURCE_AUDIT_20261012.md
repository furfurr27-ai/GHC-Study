> **Historical snapshot (2026-10-12).** This document describes the initial 819-block inventory and should not be used as the current pass/fail tally. The current 2026-10-13 audited state is **508 text-checked / 308 pending / 816 total** (three unsupported notes removed). See [live audit progress](SLIDE_AUDIT_PROGRESS_20261013.md) and the JSON claim register.

# GHC Study v1.4.5 — study-card source map and factual audit register

**Date:** 2026-10-12. **Source baseline:** recoverable v1.4.5 index.html on `audit/v145-source-recovery`, as used by the feature branch.

## Actual scope examined

- **117 study cards** examined structurally; **819 displayed fact blocks** enumerated. A block can contain several separate propositions, so this understates the number of individual factual claims.
- **38 class PDFs** were fetched directly from the linked primary Google Drive folder; each yielded readable text. The records are in batches 1–6 in this directory. These are text extractions only; image-only facts and original page layouts are not yet checked.
- **117/117 cards** have at least one identifiable PDF source among the course decks in the fetched inventory; **0 cards** have sources that do not map to those inventory titles and need the original additional guide.
- Card-level source attribution, claimed page ranges, visual references and fact-block counts are mapped below. This is an **audit register**, not a claim of completed fact-by-fact certification.

## Confirmed against directly inspected class-deck text

- **Rehwild:** the slide explicitly gives `Blattzeit`, 40–42 weeks' total gestation with delayed egg development until December, the third premolar's 3-cusp to 2-cusp change at 13–15 months, and the course's 1,000 J / 100 m (.222 example) point. These specifics agree with the Rehwild card. This confirms fidelity to the class slide; it does **not** independently validate present-day legality of any firearm use.
- **Rotwild:** the slide directly gives September–October `Brunftzeit`, 33–34 weeks' gestation, 34 adult teeth around 32 months, and `Grandeln` as the upper eyeteeth. These specifics agree with the card.
- **Türkentaube:** the source's `<1/4 kg` and `5-7x breedings` wording aligns with the app's `under about 0.25 kg` and `5–7 breeding attempts`. The automated numeric-string flag was a formatting false positive, not a source contradiction.
- **German hunting law deck (August 2026):** the text says 1,000 J at 100 m for roe deer/seal and 2,000 J at 100 m and at least 6.5 mm caliber for other cloven-hoofed game as class guidance. **Current law must be independently checked before field use.**

## Outstanding critical verification

1. The 38 PDF responses did not preserve reliable **individual slide/page boundaries** or extract all text from illustrations; page-specific attribution cannot yet be certified.
2. **819 fact blocks were inventoried, not independently semantically verified one by one.** Rehwild was directly reviewed across 29 of its 30 fact blocks, Rotwild across 15 of 18, and Türkentaube across 2 of 3, for **46 blocks checked against complete corresponding slide-deck text**. The remaining 773 blocks were inventoried and screened but not fully checked. The excluded blocks include compound statements not wholly traceable to the source text. Numerical source-term screening is merely a queue for manual investigation.
3. **Murmeltier and Seehund/Robbe** use an `Other Game` guide not in the 38-deck primary-source inventory. Verify that guide before treating these two cards as class-sourced.
4. Nine firearm-reference cards trace to a 2020 overview; even accurate old slides must not be treated as current weapons-law advice without checking updated law.
5. Full animal-photo identification, image labeling and Android screen-reader accessibility are not proven by text extraction.
6. This exercise checks **study-card text**. A separate 867-question-answer and 77-vocabulary-translation fact audit would still be required to certify every assessment item.

## Card-by-card source registration

| Card ID | Card | Deck identified | Claimed pages | Fact blocks | Media reference | Fact-level status |
|---|---|---|---|---:|---|---|
| `roe` | Rehwild | Game - Rehwild (2026) | 2–3, 5, 7–8, 13–14, 19, 35 | 30 | Referenced | Needs claim-level semantic verification |
| `boar` | Schwarzwild | Game - Schwarzwild (202502) | 2, 4–5, 9–10, 22, 28, 40 | 23 | Referenced | Needs claim-level semantic verification |
| `reddeer` | Rotwild | Game - Rotwild | 2–4, 7–8, 40–41 | 18 | Referenced | Needs claim-level semantic verification |
| `fallow` | Damwild | Game - Damwild | 2–3, 5–7, 10 | 15 | Referenced | Needs claim-level semantic verification |
| `sika` | Sikawild | Game - Sikawild | 2–4, 6–9, 13 | 17 | Referenced | Needs claim-level semantic verification |
| `chamois` | Gamswild | Game - Gamswild | 2–8, 15 | 17 | Referenced | Needs claim-level semantic verification |
| `mouflon` | Muffelwild | Game - Mufflewild | 1–10, 16–18 | 15 | Referenced | Needs claim-level semantic verification |
| `hare` | Feldhase | Game - Hares & Rabbits | 5–6 | 9 | Referenced | Needs claim-level semantic verification |
| `rabbit` | Wildkaninchen | Game - Hares & Rabbits | 16–17 | 9 | Referenced | Needs claim-level semantic verification |
| `marmot` | Murmeltier | Law - Hunting | Other Game p.1; Federal law p.11 | 6 | Referenced | Needs claim-level semantic verification |
| `seal` | Seehund / Robbe | Law - Hunting | Other Game p.2; Federal law p.11, 20, 32 | 5 | Referenced | Needs claim-level semantic verification |
| `fox` | Fuchs | Game - Fox | 2–3, 5, 8–12 | 12 | Referenced | Needs claim-level semantic verification |
| `wolf` | Wolf (wolf) | Game - Predators | 4 | 7 | Referenced | Needs claim-level semantic verification |
| `lynx` | Luchs | Game - Predators | 5 | 7 | Referenced | Needs claim-level semantic verification |
| `wildcat` | Wildkatze | Game - Predators | 6 | 8 | Referenced | Needs claim-level semantic verification |
| `bear` | Bär | Game - Predators | 8 | 5 | Referenced | Needs claim-level semantic verification |
| `badger` | Dachs | Game - Predators | 9 | 9 | Referenced | Needs claim-level semantic verification |
| `raccoon` | Waschbär | Game - Predators | 10 | 6 | Referenced | Needs claim-level semantic verification |
| `raccoondog` | Marderhund | Game - Predators | 11 | 10 | Referenced | Needs claim-level semantic verification |
| `pinemarten` | Baummarder | Game - Predators | 12 | 8 | Referenced | Needs claim-level semantic verification |
| `stonemarten` | Steinmarder | Game - Predators | 13 | 8 | Referenced | Needs claim-level semantic verification |
| `stoat` | Hermelin | Game - Predators | 14 | 7 | Referenced | Needs claim-level semantic verification |
| `leastweasel` | Mauswiesel | Game - Predators | 15 | 7 | Referenced | Needs claim-level semantic verification |
| `polecat` | Iltis | Game - Predators | 16 | 8 | Referenced | Needs claim-level semantic verification |
| `mink` | Nerz | Game - Predators | 17 | 8 | Referenced | Needs claim-level semantic verification |
| `pheasant` | Fasan | Game - Federwild | 9–11 | 11 | Referenced | Needs claim-level semantic verification |
| `partridge` | Rebhuhn | Game - Federwild | 12–13 | 9 | Referenced | Needs claim-level semantic verification |
| `snipe` | Bekassine | Game - Federwild | 14, 17 | 5 | Referenced | Needs claim-level semantic verification |
| `woodcock` | Waldschnepfe | Game - Federwild | 15–16 | 7 | Referenced | Needs claim-level semantic verification |
| `woodpigeon` | Ringeltaube | Game - Federwild | 19–20 | 6 | Referenced | Needs claim-level semantic verification |
| `stockdove` | Hohltaube / Stocktaube | Game - Federwild | 21 | 4 | Referenced | Needs claim-level semantic verification |
| `turtledove` | Turteltaube | Game - Federwild | 22 | 4 | Referenced | Needs claim-level semantic verification |
| `collareddove` | Türkentaube | Game - Federwild | 19, 23 | 4 | Referenced | Needs claim-level semantic verification |
| `mallard` | Stockente | Game - Federwild | 26–28 | 6 | Referenced | Needs claim-level semantic verification |
| `greylag` | Graugans | Game - Federwild | 32–33 | 4 | Referenced | Needs claim-level semantic verification |
| `curlew` | Großer Brachvogel | Game - Federwild | 14, 17 | 5 | Referenced | Needs claim-level semantic verification |
| `beangoose` | Saatgans | Game - Federwild | 32–33 | 4 | Referenced | Needs claim-level semantic verification |
| `whitefrontedgoose` | Bläßgans | Game - Federwild | 34 | 4 | Referenced | Needs claim-level semantic verification |
| `brantgoose` | Ringelgans | Game - Federwild | 34 | 4 | Referenced | Needs claim-level semantic verification |
| `canadagoose` | Kanadagans | Game - Federwild | 34 | 4 | Referenced | Needs claim-level semantic verification |
| `merganser` | Gänsesäger | Game - Federwild | 37 | 4 | Referenced | Needs claim-level semantic verification |
| `muteswan` | Höckerschwan | Game - Federwild | 38 | 4 | Referenced | Needs claim-level semantic verification |
| `greatcrestedgrebe` | Haubentaucher | Game - Federwild | 39 | 4 | Referenced | Needs claim-level semantic verification |
| `coot` | Blässhuhn | Game - Federwild | 40 | 3 | Referenced | Needs claim-level semantic verification |
| `capercaillie` | Auerwild | Game - Federwild | 44 | 4 | Referenced | Needs claim-level semantic verification |
| `blackgrouse` | Birkwild | Game - Federwild | 44 | 4 | Referenced | Needs claim-level semantic verification |
| `buzzard` | Mäusebussard | Game - Predatory Birds | 6–7 | 7 | Referenced | Needs claim-level semantic verification |
| `goshawk` | Habicht | Game - Predatory Birds | 10 | 4 | Referenced | Needs claim-level semantic verification |
| `redkite` | Rotmilan | Game - Predatory Birds | 11 | 7 | Referenced | Needs claim-level semantic verification |
| `peregrine` | Wanderfalke | Game - Predatory Birds | 14 | 7 | Referenced | Needs claim-level semantic verification |
| `owls` | Eulen | Game - Predatory Birds | 17–19 | 6 | Referenced | Needs claim-level semantic verification |
| `smallowls` | Käuze | Game - Predatory Birds | 19 | 5 | Referenced | Needs claim-level semantic verification |
| `tawnyowl` | Waldkauz | Game - Predatory Birds | 19 | 6 | Referenced | Needs claim-level semantic verification |
| `goldeneagle` | Steinadler | Game - Predatory Birds | 8 | 7 | Referenced | Needs claim-level semantic verification |
| `osprey` | Fischadler | Game - Predatory Birds | 9 | 7 | Referenced | Needs claim-level semantic verification |
| `seaeagle` | Seeadler | Game - Predatory Birds | 9 | 7 | Referenced | Needs claim-level semantic verification |
| `sparrowhawk` | Sperber | Game - Predatory Birds | 10 | 7 | Referenced | Needs claim-level semantic verification |
| `blackkite` | Schwarzer Milan | Game - Predatory Birds | 11 | 7 | Referenced | Needs claim-level semantic verification |
| `harriers` | Weihen | Game - Predatory Birds | 12–13 | 7 | Referenced | Needs claim-level semantic verification |
| `kestrel` | Turmfalke | Game - Predatory Birds | 15 | 8 | Referenced | Needs claim-level semantic verification |
| `eagleowl` | Uhu | Game - Predatory Birds | 17–18, 21 | 7 | Referenced | Needs claim-level semantic verification |
| `carrioncrow` | Rabenkrähe | Game - Predatory Birds | 24 | 5 | Referenced | Needs claim-level semantic verification |
| `rook` | Saatkrähe | Game - Predatory Birds | 25 | 5 | Referenced | Needs claim-level semantic verification |
| `raven` | Kolkrabe | Game - Predatory Birds | 26 | 5 | Referenced | Needs claim-level semantic verification |
| `magpie` | Elster | Game - Predatory Birds | 28 | 5 | Referenced | Needs claim-level semantic verification |
| `jays` | Häher | Game - Predatory Birds | 29 | 5 | Referenced | Needs claim-level semantic verification |
| `doggroups` | Six Hunting-Dog Groups | Hunting Dogs | 7–8 | 11 | Referenced | Needs claim-level semantic verification |
| `dogparts` | Dog Parts | Hunting Dogs | 4–5 | 6 | Referenced | Needs claim-level semantic verification |
| `kennel` | Hundezwinger | Hunting Dogs | 24 | 6 | Referenced | Needs claim-level semantic verification |
| `dk` | Deutsch Kurzhaar | Hunting Dogs | 7–12 | 4 | Referenced | Needs claim-level semantic verification |
| `dl` | Deutsch Langhaar | Hunting Dogs | 7, 11 | 4 | Referenced | Needs claim-level semantic verification |
| `dackel` | Dackel | Hunting Dogs | 7, 15 | 5 | Referenced | Needs claim-level semantic verification |
| `jagdterrier` | Deutscher Jagdterrier | Hunting Dogs | 7, 15 | 5 | Referenced | Needs claim-level semantic verification |
| `hannover` | Hannoverscher Schweißhund | Hunting Dogs | 7, 21 | 5 | Referenced | Needs claim-level semantic verification |
| `bavarian` | Bayerischer Gebirgsschweißhund | Hunting Dogs | 7, 21 | 4 | Referenced | Needs claim-level semantic verification |
| `waidgerechtigkeit` | Waidgerechtigkeit | History - Traditions | 8–9 | 5 | Referenced | Needs claim-level semantic verification |
| `hornsignals` | Jagdhornsignale | History - Traditions | 10 | 5 | Referenced | Needs claim-level semantic verification |
| `branchsigns` | Schützenbruch & Branch Signs | History - Traditions | 11–14 | 7 | Referenced | Needs claim-level semantic verification |
| `lastbite` | Letzter Bissen & Inbesitznahmebruch | History - Traditions | 15 | 6 | Referenced | Needs claim-level semantic verification |
| `methods` | Pirsch, Ansitz, Lockjagd, Fallenjagd | Hunting Techniques (20260216) | 2–4 | 7 | Referenced | Needs claim-level semantic verification |
| `drivebrief` | Drive-Hunt Brief | Hunting Techniques (20260216) | 12–13 | 7 | Referenced | Needs claim-level semantic verification |
| `shotplacement` | Shot Placement | Hunting Techniques (20260216) | 23 | 6 | Referenced | Needs claim-level semantic verification |
| `followup` | After the Shot | Hunting Techniques (20260216) | 24, 26 | 6 | Referenced | Needs claim-level semantic verification |
| `firearmactions` | Firearm Action Names | Weapons - Ammo | 14–15 | 5 | Referenced | Needs claim-level semantic verification |
| `combinationguns` | Combination Guns | Weapons - Ammo | 12, 18–19 | 5 | Referenced | Needs claim-level semantic verification |
| `rangesafety` | Range Handling | Range - Saftey | 9, 11–12 | 8 | Referenced | Needs claim-level semantic verification |
| `misfire` | Misfire Procedure | Range - Saftey | 13 | 6 | Referenced | Needs claim-level semantic verification |
| `transport` | Transport to / from a Hunt | Law - Weapons | 22 | 6 | Referenced | Needs claim-level semantic verification |
| `diseasenames` | Disease Names | Disease - Parasites; Disease - Bacteria Viruses | Parasites p.24–26; Bacteria/Viruses disease list and ASF p.27 | 7 | Referenced | Needs claim-level semantic verification |
| `kundigeperson` | Kundige Person | Disease - Kundige Person | 2–3 | 6 | Referenced | Needs claim-level semantic verification |
| `trichinella` | Trichinose | Disease - Parasites | 24, 26 | 9 | Referenced | Needs claim-level semantic verification |
| `asf` | Afrikanische Schweinepest (ASP) | Disease - Bacteria Viruses | 27 | 8 | Referenced | Needs claim-level semantic verification |
| `rabies` | Tollwut | Disease - Bacteria Viruses | 21 | 9 | Referenced | Needs claim-level semantic verification |
| `footmouth` | Maul- und Klauenseuche | Disease - Bacteria Viruses | 20 | 8 | Referenced | Needs claim-level semantic verification |
| `parasites` | Parasite Prevention | Disease - Parasites | 16, 40 | 7 | Referenced | Needs claim-level semantic verification |
| `revierrules` | Revier Rules | Range - Revier | 4–5 | 8 | Referenced | Needs claim-level semantic verification |
| `protectedwildlife` | Wounded vs Protected Wildlife | Law - Nature and Animal | 8, 10 | 5 | Referenced | Needs claim-level semantic verification |
| `abschussplan` | Abschussplan | Law - Nature and Animal | 20, 32 | 6 | Referenced | Needs claim-level semantic verification |
| `wildschaden` | Wildschaden | Law - Nature and Animal | 44, 47 | 6 | Referenced | Needs claim-level semantic verification |
| `crops` | Primary German Crops | Field & Forest | 9–18 | 5 | Referenced | Needs claim-level semantic verification |
| `trees` | The “Big 5” German Trees | Field & Forest | 31 | 6 | Referenced | Needs claim-level semantic verification |
| `coldweapons` | Hirschfänger & Saufeder | Weapons - Overview | 12 | 5 | Referenced | Needs claim-level semantic verification |
| `shotgunshell` | Shotgun Shell Length & Gauge | Weapons - Overview | 19, 45-46 | 5 | Referenced | Needs claim-level semantic verification |
| `gunmarkings` | German Gun Markings | Weapons - Overview | 28 | 6 | Referenced | Needs claim-level semantic verification |
| `stecher` | Stecher Trigger | Weapons - Overview | 31 | 5 | Referenced | Needs claim-level semantic verification |
| `gunstorage` | German Firearm Storage | Weapons - Overview | 34 | 5 | Referenced | Needs claim-level semantic verification |
| `handgunquota` | Hunter Handguns | Weapons - Overview | 37 | 5 | Referenced | Needs claim-level semantic verification |
| `ammotypes` | Cartridge Types & Markings | Weapons - Overview | 41-42 | 5 | Referenced | Needs claim-level semantic verification |
| `shotdistance` | Shotgun Danger Distance | Weapons - Overview | 50-51 | 5 | Referenced | Needs claim-level semantic verification |
| `scopebasics` | Scopes & Parallax | Weapons - Overview | 58, 60-61 | 6 | Referenced | Needs claim-level semantic verification |
| `labrador` | Labrador Retriever | Hunting Dogs | 22 | 4 | Referenced | Needs claim-level semantic verification |
| `dogdiseases` | Dog Diseases | Hunting Dogs | 26 | 5 | Referenced | Needs claim-level semantic verification |
| `dogcert` | Dog Training & Certification | Hunting Dogs | 32 | 5 | Referenced | Needs claim-level semantic verification |
| `birdanatomy` | Bird Anatomy | Game - Federwild | 7 | 4 | Referenced | Needs claim-level semantic verification |
| `birdchecklist` | Federwild Review Checklist | Game - Federwild | 46-49 | 7 | Referenced | Needs claim-level semantic verification |
| `revierroles` | Who Is in a Revier? | Range - Revier | 6-7 | 5 | Referenced | Needs claim-level semantic verification |
| `trophy-antler-horn-terminology` | Trophy Anatomy | Game - Rehwild (2026); Game - Rotwild; Game - Damwild; Game - Mufflewild; Trophy Parts 1–2 | Game - Rotwild.pdf pp. 14–16; other class decks | 21 | Referenced | Needs claim-level semantic verification |
