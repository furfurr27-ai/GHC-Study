# Waidwissen / WaidMatrix — external research intake

Reviewed: 2026-10-18
Status: Supplementary source review incorporated as an **original Schalenwild comparison matrix in Android v1.4.6**. This does not overwrite the GHC study-card Details, Other Facts, or any course answer.

## Sources actually checked
- User-provided public video: https://youtu.be/bZSqIRW5zTQ — *WaidMatrix zum Schalenwild – Verstehe die Zeiten!*. Video title was accessible; a verified full video transcript was **not** available.
- Creator channel: https://www.youtube.com/@waidwissen
- Creator's accessible written companion: https://waidwissen.com/einfuehrung-zum-schalenwild (section "WaidMatrix zum Schalenwild" and antler-cycle tables).
- GHC course study source: *GHC Section 1 - Game Biology Conservation Study.pptx*, connected Drive ID `1uHb06B0OlUcacqmZFNjw42-1LtOM9C0i`, Question Board 1, especially Question 4; this is a **consolidated course study deck**, not a complete independent recheck of original animal PDFs.
- Current repository: `README.md`, recovered baseline `app/src/main/assets/index.html`, `schalenwild-matrix.js`, `.css`, and `tools/inject_schalenwild_matrix.py`. The large HTML is reconstructed by the APK workflow; matrix files are injected separately.

## Original, paraphrased teaching takeaways
1. Teach reproductive chronology as **Brunftzeit (rut) → Tragzeit (gestation) → Setzzeit (birth season)**. Put the English meaning immediately after each German term.
2. For deer, teach the separate antler sequence **Abwerfen (shed) → Schieben (grow in velvet) → Fegen (rub off velvet)**. Do not confuse antlers, which are shed, with permanently retained horns.
3. **Rehwild** is a special breeding-calendar case because **Eiruhe (delayed implantation)** separates mating from subsequent embryonic development; the course expects Jul–Aug breeding and May–Jun fawning.
4. Most animals in the Waidwissen comparison give birth in spring or early summer, but an approximate mnemonic must never replace the course-specific range for an individual species.
5. Treat Waidwissen's five-month antler-growth rule as an **approximate memory aid**, not an exact biological constant for every animal.
6. Do not automatically import Waidwissen's entire month/gestation table into GHC question answers, because the figures and scopes differ from the course study deck.

## Discrepancy register — preserve course answers pending original slide verification

| Species | GHC Section 1 condensed course answer | Waidwissen written companion | Handling |
|---|---|---|---|
| Rehwild (roe deer) | Rut Jul–Aug; gestation 40–42 weeks incl. Eiruhe; births May–Jun | Rut Jul–Aug; approx. 9.5 months incl. Eiruhe; births May–Jun | Broadly compatible; explain delayed implantation in supplementary Understanding |
| Rotwild (red deer) | Rut Sep–Oct; gestation 33–34 weeks; births May–Jun | Rut Sep–Oct; gestation shown as 8.5 months; births May–Jun | **Conflict in gestation figure**; keep GHC figure until original class slides checked |
| Damwild (fallow deer) | Rut late Oct–mid Nov; gestation 30–34 weeks; births Jun | Rut Oct–Nov; approx. 7.5–8 months; births May–Jun | Course-specific wording retained |
| Sikawild (sika deer) | Rut Oct–Nov; gestation 30–34 weeks; births Jun | Rut Oct–Nov; approx. 7.5 months; births May–Jun | Course-specific wording retained |
| Gamswild (chamois) | Rut Nov; gestation 20–21 weeks; births May | Rut Nov–Dec; approx. 6 months; births May–Jun | **Conflict in gestation figure**; keep GHC answer pending original slides |
| Muffelwild (mouflon) | Rut Oct–Dec; gestation approx. 22 weeks; births Mar–Jun | Rut Oct–Nov; approx. 5.5 months; births Apr–May | Different seasonal bounds; do not overwrite course answer |

## Completed app integration (v1.4.6)
- Study Cards → **Schalenwild** gains a collapsible **Jahresmatrix** above the existing study-card search and grid.
- The matrix compares 7 species across all 12 months, using a rut/birth filter and gestation figures, with sourced standouts and memory aids.
- Each figure was reviewed against the original class slide PDF for that species (listed below). Course-source statements are not replaced by outside figures.
- The design is original; attribution links to the Waidwissen video, but no proprietary video, transcript, image or graphic is copied into the APK.
- Integration assets: `app/src/main/assets/schalenwild-matrix.js`, `schalenwild-matrix.css` and `tools/inject_schalenwild_matrix.py`.
- GitHub Actions build for initial v1.4.6 completed successfully, including the HTML injection and JavaScript syntax checks. Real-device layout/navigation testing is still outstanding.

## Original class-slide PDFs checked directly (2026-10-18)
- [Game - Rehwild (2026).pdf](https://drive.google.com/file/d/1WRy1ScZPtRgKdsZ6xXosrBZjUU3ghpOR/view) — mid-July–mid-August rut; 40–42 weeks including Eiruhe; May–June fawning.
- [Game - Rotwild.pdf](https://drive.google.com/file/d/18jWSwS3sN51I7b6xgAeo_kxCAeO72xrz/view) — September–October rut; 33–34 weeks; May–June births.
- [Game - Schwarzwild (202502).pdf](https://drive.google.com/file/d/1ZOjyFAHaCoWyuxfHm5ux1WI76VIfF6H6/view) — mainly Dec–Jan rut (irregular Nov–Jan), 3 months + 3 weeks + 3 days, March–April births with possible year-round births.
- [Game - Damwild.pdf](https://drive.google.com/file/d/1HYGuwUjiX-m4QQcJuZ-GLRd3lufW0fEs/view) — late October–mid November rut; 30–34 weeks; June births.
- [Game - Sikawild (2025).pdf](https://drive.google.com/file/d/1HLO4PeaqfMHJOB9pZDwprt2AObTNRtIK/view) — October–November rut; 30–34 weeks; June births.
- [Game - Gamswild.pdf](https://drive.google.com/file/d/1shF50XQ8LEwJwfGmLdJBgXNfA3AA9QIq/view) — November rut; 20–21 weeks; May births as written; **the three values appear chronologically inconsistent**. Flagged in the matrix, not silently corrected.
- [Game - Mufflewild (2015).pdf](https://drive.google.com/file/d/1tXW1RQSNDj11XyL5BL_bBAx2xHpnPY5m/view) — October–December rut; 22 weeks; March–June births.

## Limitations
This remains a review of one public Waidwissen video and a companion article, **not a review of every video on the channel**; a verified full-video transcript was unavailable. All seven course animal PDFs listed above were retrieved and checked for the matrix figures, but no visual Android-device test has yet been reported. A green GitHub Actions build confirms packaging, not on-device usability.
