# Scoreboard

**Grain of salt — read this first.** Reliable G2P "gold" barely exists. Most datasets below are semi-automated, dictionary-extracted, community-scraped, or a phonemizer's OWN output reused as a reference. A low PER against a `machine-generated` gold means "agrees with that tool", NOT "correct". Absolute PER is noisy — read every number as **directional/relative**, and cross-reference the `95% CI` (a wide or degenerate interval, common on small-`N` rows, means the row cannot support a conclusion). Full per-dataset classification and the honest caveats: [`docs/benchmarks.md`](benchmarks.md) ("Provenance and reliability").

`Provenance` legend (most → least trustworthy, all still subject to notation conventions and small-`N` noise): **expert-human** (phonetician / native-speaker / expert-annotator) > **lexicon-derived** (dictionary, human lexicographers) > **crowd-scraped** (Wiktionary) > **machine-generated** (a phonemizer's own output — biggest grain of salt; agreement-with-tool, not correctness).

Committed PER/exact-match results for every gold dataset/language combination registered in `scripts/benchmark.py`. Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard
```

Machine-readable form: [`benchmarks/results.json`](../benchmarks/results.json). Methodology and dataset provenance: [`docs/benchmarks.md`](benchmarks.md).

The `95% CI` column is a bootstrap confidence interval on the mean PER (per-word PERs resampled with replacement, 1000 reps, fixed seed 20260710) — see [`docs/benchmarks.md`](benchmarks.md).

| Lang | Dataset | N | PER | 95% CI | Exact match | Quality tier | Provenance |
|---|---|---:|---:|---:|---:|---|---|
| ar | wikipron | 259 | 0.2566 | [0.2391, 0.2737] | 0.1081 | research | crowd-scraped |
| ast | wikipron | 300 | 0.0876 | [0.0731, 0.1014] | 0.5900 | research | crowd-scraped |
| ca | 4catac | 160 | 0.4120 | [0.4017, 0.4219] | 0.0000 | research | expert-human |
| ca | styletts2_phonemes | 300 | 0.4083 | [0.3998, 0.4170] | 0.0000 | research | machine-generated |
| ca-x-balear | 4catac | 160 | 0.3884 | [0.3797, 0.3975] | 0.0000 | research | expert-human |
| ca-x-occidental | 4catac | 160 | 0.5633 | [0.5549, 0.5720] | 0.0000 | research | expert-human |
| ca-x-valencia | 4catac | 160 | 0.3005 | [0.2920, 0.3089] | 0.0000 | research | expert-human |
| cy | wikipron | 276 | 0.2187 | [0.1968, 0.2433] | 0.2899 | research | crowd-scraped |
| da | wikipron | 273 | 0.4415 | [0.4128, 0.4693] | 0.0476 | research | crowd-scraped |
| de | styletts2_phonemes | 300 | 0.3964 | [0.3879, 0.4049] | 0.0000 | research | machine-generated |
| de | wikipron | 269 | 0.3613 | [0.3402, 0.3796] | 0.0297 | research | crowd-scraped |
| el | styletts2_phonemes | 298 | 0.2178 | [0.2023, 0.2326] | 0.0000 | research | machine-generated |
| el | wikipron | 298 | 0.1513 | [0.1341, 0.1678] | 0.3154 | research | crowd-scraped |
| en | styletts2_phonemes | 300 | 0.4379 | [0.4305, 0.4459] | 0.0000 | research | machine-generated |
| en | wikipron | 220 | 0.4661 | [0.4334, 0.4998] | 0.1000 | research | crowd-scraped |
| en-GB | wikipron | 245 | 0.4721 | [0.4420, 0.5058] | 0.0816 | research | crowd-scraped |
| en-US | ipa_childes | 300 | 0.4166 | [0.3809, 0.4528] | 0.2167 | research | machine-generated |
| eo | wikipron | 300 | 0.0303 | [0.0221, 0.0392] | 0.8700 | research | crowd-scraped |
| es | styletts2_phonemes | 300 | 0.1713 | [0.1584, 0.1851] | 0.0000 | research | machine-generated |
| es | wikipron | 298 | 0.1000 | [0.0870, 0.1134] | 0.4765 | research | crowd-scraped |
| et | ipa_childes | 300 | 0.3094 | [0.2876, 0.3304] | 0.1533 | research | machine-generated |
| eu | hitz_basque_ipa | 300 | 0.2796 | [0.2579, 0.3011] | 0.1567 | research | machine-generated |
| eu | wikipron | 239 | 0.0768 | [0.0614, 0.0939] | 0.5900 | research | crowd-scraped |
| fa | styletts2_phonemes | 294 | 0.5787 | [0.5724, 0.5858] | 0.0000 | research | machine-generated |
| fi | styletts2_phonemes | 298 | 0.2919 | [0.2783, 0.3060] | 0.0000 | research | machine-generated |
| fi | wikipron | 294 | 0.0386 | [0.0304, 0.0476] | 0.7483 | research | crowd-scraped |
| fr | styletts2_phonemes | 300 | 0.3557 | [0.3481, 0.3639] | 0.0000 | research | machine-generated |
| fr | wikipron | 279 | 0.1559 | [0.1332, 0.1781] | 0.4624 | research | crowd-scraped |
| ga | wikipron | 134 | 0.4330 | [0.3952, 0.4655] | 0.0373 | research | crowd-scraped |
| gd | wikipron | 210 | 0.6867 | [0.6496, 0.7220] | 0.0286 | research | crowd-scraped |
| gl | wikipron | 264 | 0.0728 | [0.0604, 0.0868] | 0.6326 | research | crowd-scraped |
| hi | wikipron | 261 | 0.4424 | [0.4254, 0.4583] | 0.0115 | research | crowd-scraped |
| hr | wikipron | 292 | 0.2763 | [0.2623, 0.2916] | 0.0171 | research | crowd-scraped |
| hu | ipa_childes | 297 | 0.1407 | [0.1220, 0.1592] | 0.4444 | research | machine-generated |
| hy | wikipron | 297 | 0.0701 | [0.0580, 0.0824] | 0.6229 | research | crowd-scraped |
| id | ipa_childes | 300 | 0.1103 | [0.0925, 0.1288] | 0.5633 | research | machine-generated |
| is | ipadict | 300 | 0.2300 | [0.2163, 0.2456] | 0.0900 | research | lexicon-derived |
| is | wikipron | 258 | 0.2232 | [0.2035, 0.2410] | 0.1395 | research | crowd-scraped |
| it | styletts2_phonemes | 300 | 0.2100 | [0.2000, 0.2214] | 0.0000 | research | machine-generated |
| it | wikipron | 276 | 0.1004 | [0.0844, 0.1146] | 0.4855 | research | crowd-scraped |
| ml | wikipron | 280 | 0.6099 | [0.5920, 0.6273] | 0.0000 | research | crowd-scraped |
| mwl | mirandese | 205 | 0.2020 | [0.1772, 0.2288] | 0.2976 | research | expert-human |
| mwl-x-sendim | mirandese | 11 | 0.3687 | [0.2197, 0.5203] | 0.1818 | research | expert-human |
| nb | wikipron | 226 | 0.5133 | [0.4920, 0.5354] | 0.0177 | skeleton | crowd-scraped |
| nl | wikipron | 260 | 0.3135 | [0.2854, 0.3411] | 0.1692 | research | crowd-scraped |
| oc | wikipron | 266 | 0.1604 | [0.1421, 0.1793] | 0.3722 | research | crowd-scraped |
| pl | styletts2_phonemes | 299 | 0.1867 | [0.1764, 0.1978] | 0.0000 | research | machine-generated |
| pl | wikipron | 287 | 0.1195 | [0.1060, 0.1346] | 0.3624 | research | crowd-scraped |
| pt | styletts2_phonemes | 300 | 0.3871 | [0.3765, 0.3972] | 0.0000 | research | machine-generated |
| pt | wikipron | 242 | 0.2090 | [0.1858, 0.2315] | 0.3058 | research | crowd-scraped |
| pt-BR | wikipron | 124 | 0.1578 | [0.1258, 0.1904] | 0.5000 | research | crowd-scraped |
| pt-PT | ep_dialects | 30 | 0.2218 | [0.1836, 0.2634] | 0.0000 | research | expert-human |
| pt-PT | infopedia_pt | 295 | 0.2942 | [0.2698, 0.3175] | 0.1627 | research | lexicon-derived |
| pt-PT-x-acores | clup_dialect | 2 | 0.4464 | [0.4413, 0.4515] | 0.0000 | research | expert-human |
| pt-PT-x-acores | ep_dialects | 29 | 0.3058 | [0.2746, 0.3415] | 0.0000 | research | expert-human |
| pt-PT-x-alentejo | clup_dialect | 1 | 0.3716 | [0.3716, 0.3716] | 0.0000 | research | expert-human |
| pt-PT-x-alentejo | ep_dialects | 30 | 0.3174 | [0.2775, 0.3622] | 0.0000 | research | expert-human |
| pt-PT-x-alfena | clup_dialect | 1 | 0.4573 | [0.4573, 0.4573] | 0.0000 | skeleton | expert-human |
| pt-PT-x-algarve | clup_dialect | 3 | 0.5024 | [0.4497, 0.5547] | 0.0000 | research | expert-human |
| pt-PT-x-algarve | ep_dialects | 30 | 0.3152 | [0.2703, 0.3590] | 0.0000 | research | expert-human |
| pt-PT-x-aveiro | clup_dialect | 6 | 0.4140 | [0.3777, 0.4526] | 0.0000 | skeleton | expert-human |
| pt-PT-x-beira | clup_dialect | 8 | 0.4315 | [0.4051, 0.4734] | 0.0000 | research | expert-human |
| pt-PT-x-lisbon | clup_dialect | 5 | 0.4428 | [0.4154, 0.4701] | 0.0000 | research | expert-human |
| pt-PT-x-lisbon | ep_dialects | 45 | 0.2505 | [0.2211, 0.2804] | 0.0000 | research | expert-human |
| pt-PT-x-madeira | clup_dialect | 4 | 0.4329 | [0.3968, 0.4843] | 0.0000 | research | expert-human |
| pt-PT-x-madeira | ep_dialects | 30 | 0.2235 | [0.1897, 0.2590] | 0.0000 | research | expert-human |
| pt-PT-x-minho | clup_dialect | 9 | 0.4349 | [0.4091, 0.4618] | 0.0000 | research | expert-human |
| pt-PT-x-porto | clup_dialect | 17 | 0.4895 | [0.4607, 0.5180] | 0.0000 | research | expert-human |
| pt-PT-x-porto | ep_dialects | 40 | 0.2342 | [0.2002, 0.2658] | 0.0500 | research | expert-human |
| pt-PT-x-trasosmontes | clup_dialect | 6 | 0.4446 | [0.4251, 0.4689] | 0.0000 | research | expert-human |
| pt-PT-x-viana | clup_dialect | 4 | 0.4666 | [0.4304, 0.5121] | 0.0000 | skeleton | expert-human |
| ro | wikipron | 281 | 0.0597 | [0.0486, 0.0710] | 0.6370 | research | crowd-scraped |
| ru | styletts2_phonemes | 299 | 0.3934 | [0.3827, 0.4046] | 0.0000 | research | machine-generated |
| ru | wikipron | 268 | 0.3635 | [0.3475, 0.3795] | 0.0112 | research | crowd-scraped |
| sk | wikipron | 300 | 0.1206 | [0.1029, 0.1370] | 0.4700 | research | crowd-scraped |
| sq | wikipron | 249 | 0.0915 | [0.0719, 0.1113] | 0.6867 | research | crowd-scraped |
| sr | ipa_childes | 300 | 0.4764 | [0.4545, 0.4984] | 0.0467 | research | machine-generated |
| sv | styletts2_phonemes | 300 | 0.3835 | [0.3752, 0.3924] | 0.0000 | research | machine-generated |
| sv | wikipron | 279 | 0.3508 | [0.3305, 0.3721] | 0.0609 | research | crowd-scraped |
| ta | wikipron | 293 | 0.8949 | [0.8631, 0.9324] | 0.0000 | research | crowd-scraped |
| tl | wikipron | 269 | 0.2309 | [0.2150, 0.2464] | 0.0446 | research | crowd-scraped |
| tr | wikipron | 296 | 0.1409 | [0.1236, 0.1592] | 0.3953 | research | crowd-scraped |
| uk | styletts2_phonemes | 299 | 0.4960 | [0.4842, 0.5074] | 0.0000 | research | machine-generated |
| zh | ipa_childes | 300 | 0.5183 | [0.4973, 0.5381] | 0.0200 | research | machine-generated |
