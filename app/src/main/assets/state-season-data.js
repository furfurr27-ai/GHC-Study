/* Locally bundled, source-labelled Hessen season calendar. NOT authorization. Updated 2026-10-26. */
window.GHC_SEASON_DATA={
 "schemaVersion": 1,
 "selectedDateBasis": "Europe/Berlin",
 "states": [
  {
   "code": "DE-BW",
   "name": "Baden-Württemberg",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-BY",
   "name": "Bayern",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-BE",
   "name": "Berlin",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-BB",
   "name": "Brandenburg",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-HB",
   "name": "Bremen",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-HH",
   "name": "Hamburg",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-HE",
   "name": "Hessen",
   "seasonStatus": "reviewed subset",
   "reviewed": "2026-10-26"
  },
  {
   "code": "DE-MV",
   "name": "Mecklenburg-Vorpommern",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-NI",
   "name": "Niedersachsen",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-NW",
   "name": "Nordrhein-Westfalen",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-RP",
   "name": "Rheinland-Pfalz",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-SL",
   "name": "Saarland",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-SN",
   "name": "Sachsen",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-ST",
   "name": "Sachsen-Anhalt",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-SH",
   "name": "Schleswig-Holstein",
   "seasonStatus": "unverified",
   "reviewed": null
  },
  {
   "code": "DE-TH",
   "name": "Thüringen",
   "seasonStatus": "unverified",
   "reviewed": null
  }
 ],
 "hessen": {
  "code": "DE-HE",
  "effectiveFrom": "2026-04-01",
  "sourceReviewed": "2026-10-26",
  "reviewExpires": "2027-04-26",
  "sources": [
   {
    "id": "HJagdV-2",
    "title": "Official Hessian Gazette 2026 No. 14: March 3 amendment to HJagdV §2 (effective April 1)",
    "kind": "binding official amendment; not a full consolidation",
    "url": "https://rp-kassel.hessen.de/sites/rp-kassel.hessen.de/files/2026-03/gvbl_2026_nr_14_aendvo_hjagdvo_regelungstext.pdf"
   },
   {
    "id": "HMLU-202604",
    "title": "Hessisches Landwirtschaftsministerium: official HJagdV amendment synopsis",
    "kind": "official government amendment comparison",
    "url": "https://landwirtschaft.hessen.de/sites/landwirtschaft.hessen.de/files/2026-03/synopse_hjagdvo_maerz_2026.pdf"
   },
   {
    "id": "LJV-20260518",
    "title": "LJV Hessen Jagd- und Schonzeiten, corrected 18 May 2026",
    "kind": "association consolidated calendar, cross-checked to official amendments",
    "url": "https://ljv-hessen.de/download/jagd-und-schonzeiten-bund-land-hessen/"
   },
   {
    "id": "HESSEN-20260528",
    "title": "Hessian Gazette 2026 No. 32: May 20 changes effective May 28 (wolves/wolf hybrids; no changes to these 19 classes)",
    "kind": "later binding amendment checked for supersession",
    "url": "https://www.umwelt-online.de/regelwerk/natursch/laender/he/z26_0032.htm"
   },
   {
    "id": "BJagdG-22",
    "title": "Bundesjagdgesetz § 22 (dependent-young protections)",
    "kind": "binding federal law",
    "url": "https://www.gesetze-im-internet.de/bjagdg/__22.html"
   }
  ],
  "species": {
   "roe": {
    "classes": [
     {
      "id": "buck",
      "label": "Böcke",
      "intervals": [
       [
        "04-01",
        "01-31"
       ]
      ]
     },
     {
      "id": "doe-kid",
      "label": "Ricken und Kitze",
      "intervals": [
       [
        "09-01",
        "01-31"
       ]
      ]
     },
     {
      "id": "yearling-doe",
      "label": "Schmalrehe",
      "intervals": [
       [
        "04-01",
        "01-31"
       ]
      ]
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "boar": {
    "classes": [
     {
      "id": "all",
      "label": "Schwarzwild (allgemeine Jagdzeit)",
      "intervals": [
       [
        "01-01",
        "12-31"
       ]
      ],
      "conditional": true,
      "reason": "Year-round calendar, but positive sex/age identification and protection of dependent young must be checked; ASP district orders can change access."
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission. ASP restrictions by district.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "red": {
    "classes": [
     {
      "id": "calf",
      "label": "Kälber",
      "intervals": [
       [
        "08-01",
        "01-31"
       ]
      ]
     },
     {
      "id": "yearling",
      "label": "Schmalspießer / Schmaltiere",
      "intervals": [
       [
        "04-01",
        "05-31"
       ],
       [
        "08-01",
        "01-31"
       ]
      ]
     },
     {
      "id": "adult",
      "label": "Hirsche / Alttiere",
      "intervals": [
       [
        "08-01",
        "01-31"
       ]
      ]
     }
    ],
    "exceptions": "Abschussplan and locally applicable management restrictions; General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "fallow": {
    "classes": [
     {
      "id": "adult-calf",
      "label": "Hirsche, Alttiere und Kälber",
      "intervals": [
       [
        "09-01",
        "01-31"
       ]
      ]
     },
     {
      "id": "yearling",
      "label": "Schmalspießer / Schmaltiere",
      "intervals": [
       [
        "04-01",
        "05-31"
       ],
       [
        "08-01",
        "01-31"
       ]
      ]
     }
    ],
    "exceptions": "Abschussplan; General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "sika": {
    "classes": [
     {
      "id": "adult-calf",
      "label": "Hirsche, Alttiere und Kälber",
      "intervals": [
       [
        "09-01",
        "01-31"
       ]
      ]
     },
     {
      "id": "yearling",
      "label": "Schmalspießer / Schmaltiere",
      "intervals": [
       [
        "04-01",
        "05-31"
       ],
       [
        "08-01",
        "01-31"
       ]
      ]
     }
    ],
    "exceptions": "Abschussplan; General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "mouflon": {
    "classes": [
     {
      "id": "adult",
      "label": "Widder und Schafe",
      "intervals": [
       [
        "08-01",
        "01-31"
       ]
      ]
     },
     {
      "id": "yearling",
      "label": "Jährlingswidder / Schmalschafe",
      "intervals": [
       [
        "04-01",
        "05-31"
       ],
       [
        "08-01",
        "01-31"
       ]
      ]
     }
    ],
    "exceptions": "Abschussplan; General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "fox": {
    "classes": [
     {
      "id": "general",
      "label": "Fuchs",
      "intervals": [
       [
        "01-01",
        "12-31"
       ]
      ]
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "raccoon": {
    "classes": [
     {
      "id": "general",
      "label": "Waschbären",
      "intervals": [
       [
        "01-01",
        "12-31"
       ]
      ]
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission. Invasive-species and local orders remain relevant.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "badger": {
    "classes": [
     {
      "id": "adult",
      "label": "Dachse",
      "intervals": [
       [
        "08-01",
        "12-31"
       ]
      ]
     },
     {
      "id": "young",
      "label": "Jungdachs",
      "intervals": [
       [
        "06-01",
        "12-31"
       ]
      ]
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "hare": {
    "classes": [
     {
      "id": "general",
      "label": "Feldhasen",
      "intervals": [
       [
        "10-01",
        "12-31"
       ]
      ],
      "conditional": true,
      "reason": "HJagdV §2(4): sufficient population density and sustainable annual increase must be established."
     }
    ],
    "exceptions": "Conservation/population condition in HJagdV §2(4).",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "rabbit": {
    "classes": [
     {
      "id": "general",
      "label": "Wildkaninchen",
      "intervals": [
       [
        "01-01",
        "12-31"
       ]
      ]
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "pheasant": {
    "classes": [
     {
      "id": "cock",
      "label": "Fasanenhähne",
      "intervals": [
       [
        "10-01",
        "01-15"
       ]
      ]
     },
     {
      "id": "hen",
      "label": "Fasanenhennen",
      "intervals": [],
      "noGeneral": true,
      "reason": "Corrected 18 May 2026 table expressly states no pheasant hens."
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "mallard": {
    "classes": [
     {
      "id": "general",
      "label": "Stockenten",
      "intervals": [
       [
        "09-01",
        "01-15"
       ]
      ],
      "conditional": true,
      "reason": "HJagdV §2(4): harvest only consistent with sufficient population density and sustainable annual increase."
     }
    ],
    "exceptions": "HJagdV §2(4) Niederwild monitoring condition.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "pigeon": {
    "classes": [
     {
      "id": "adult",
      "label": "Adulte Ringeltauben",
      "intervals": [
       [
        "11-01",
        "02-10"
       ]
      ]
     },
     {
      "id": "juvenile",
      "label": "Juvenile Ringeltauben",
      "intervals": [
       [
        "07-01",
        "02-10"
       ]
      ]
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission. Identify adult versus juvenile positively.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "crow": {
    "classes": [
     {
      "id": "general",
      "label": "Rabenkrähen",
      "intervals": [
       [
        "08-01",
        "02-15"
       ]
      ]
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission. Additional species under HJagdV §1(1).",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "magpie": {
    "classes": [
     {
      "id": "general",
      "label": "Elstern",
      "intervals": [
       [
        "08-01",
        "01-31"
       ]
      ]
     }
    ],
    "exceptions": "General hunting window does not override BJagdG §22(4) protection of adults needed for dependent young or individual permission. Additional species under HJagdV §1(1).",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "heron": {
    "unverified": true,
    "reason": "Graureiher status not individually established from the May 2026 HJagdV season summary; do not infer no season or protection.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "auer": {
    "unverified": true,
    "reason": "Auerwild status not individually audited under full federal/state/protection provisions.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   },
   "wildcat": {
    "unverified": true,
    "reason": "Wildkatze protected status is not independently reconciled with all current applicable legal provisions for this season engine.",
    "sourceIds": [
     "HJagdV-2",
     "HMLU-202604",
     "LJV-20260518",
     "BJagdG-22"
    ],
    "evidence": "HJagdV § 2, effective 2026-04-01; corrected LJV Hessen hunting-time table of 2026-05-18."
   }
  }
 }
};
