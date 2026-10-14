# GHC Study — fourth source-backed glossary continuation (2026-10-14)

## Class PDFs directly checked

- `Trophy Part 1 (2025).pdf`, accessible through the connected 2026 GHC class-source inventory, specifically the trophy-type listing `Balg/Pelz - furbearers`. This supports **Pelz — fur/pelt** as an explicitly paired classroom term. No etymology or independent harvest/season law is inferred.
- `Trapping (202607).pdf`, predator bait table explicitly saying `Pine/Stone Marten (Baum - Stein Marder)`. This supports the **compound words** `Baummarder` (pine marten) and `Steinmarder` (stone marten). The worksheet indexes `Baum` and `Stein` separately; **the deck does not establish either bare word as a standalone Jägersprache animal term**. Their entries explicitly explain that Baum alone means tree, Stein alone means stone, and place the hunting-specific use in their compound forms.

## Recorded source classifications

| Worksheet index | Current English value | Evidence type | Caution |
| --- | --- | --- | --- |
| x134 Pelz | Fur or pelt | Direct class PDF paired term | Trophy terminology, not an etymology |
| x083 Baum | Tree (as in Baummarder, pine marten) | Class PDF **compound only** | Don't identify `Baum` by itself as a marten |
| x145 Stein | Stone (as in Steinmarder, stone marten) | Class PDF **compound only** | Don't identify `Stein` by itself as a marten |

**Current glossary totals:** 162 entries, **140 defined / 22 pending**. No question, answer key, study card, imported quiz-progress ID or physical Android app metadata was changed.

## Parallel Android test evidence

- Original Android 35 `google_apis` emulator success run `38464879108` verified Glossary → Quiz Mode with system Back.
- Extended run `38492587017` also verified **Reference → Quiz Mode** system Back. Its expanded test then stopped because the Study Mode UIAutomator node presented `Schalenwild 7 cards · ...` as one combined label, while the harness expected the label to equal exactly `Schalenwild`.
- Fixed the Android emulator UI label matcher at commit `b178fe6dab19c2037c3e8e03c7234feffb4aee3d` to match the same term plus its appended description, without removing page-transition assertions. Check CI at that commit or newer for nested Rehwild card behavior.
- Physical Galaxy S23 Ultra validation and preservation-of-progress upgrade tests are not verified by CI.

## Still pending

Twenty-two worksheet terms remain pending primary-source matching. Original 77 vocabulary etymologies need separate historical corroboration. The claim register still represents 803 directly checked class-slide-text blocks and 11 historical-guide exceptions; figure-only images, current legal currency, and 867 question explanations remain separately unaudited for factual accuracy.

Sources actually inspected in this continuation: the live GitHub regression run and its UIAutomator XML artifact, shipped Android HTML navigation, and the two original class PDFs named above, via their connected Drive readable text. The short PDF quotations do not certify slide graphics or page-number alignment.
