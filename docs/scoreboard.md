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
| ar | wikipron | 259 | 0.1868 | [0.1700, 0.2035] | 0.2394 | research | crowd-scraped |
| ast | wikipron | 300 | 0.0876 | [0.0731, 0.1014] | 0.5900 | research | crowd-scraped |
| ca | 4catac | 160 | 0.4026 | [0.3930, 0.4120] | 0.0000 | research | expert-human |
| ca | styletts2_phonemes | 300 | 0.4012 | [0.3928, 0.4099] | 0.0000 | research | machine-generated |
| ca-x-balear | 4catac | 160 | 0.3893 | [0.3803, 0.3986] | 0.0000 | research | expert-human |
| ca-x-occidental | 4catac | 160 | 0.4663 | [0.4578, 0.4748] | 0.0000 | research | expert-human |
| ca-x-valencia | 4catac | 160 | 0.2994 | [0.2907, 0.3078] | 0.0000 | research | expert-human |
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
| eu | hitz_basque_ipa | 300 | 0.2523 | [0.2300, 0.2745] | 0.1967 | research | machine-generated |
| eu | wikipron | 239 | 0.0777 | [0.0623, 0.0953] | 0.5900 | research | crowd-scraped |
| ext-PT-x-barrancos | barranquenho_dict | 297 | 0.1373 | [0.1166, 0.1588] | 0.5320 | research | machine-generated |
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
| mwl | mirandese_dict | 291 | 0.3045 | [0.2786, 0.3298] | 0.1856 | research | machine-generated |
| mwl | mirandese_g2p | 205 | 0.1851 | [0.1597, 0.2127] | 0.3610 | research | expert-human |
| mwl-x-ifanes | mirandese_dict | 4 | 0.5000 | [0.1667, 0.8333] | 0.2500 | research | machine-generated |
| mwl-x-ifanes | mirandese_g2p | 2 | 0.7500 | [0.5000, 1.0000] | 0.0000 | research | expert-human |
| mwl-x-sendim | mirandese_dict | 79 | 0.2858 | [0.2364, 0.3370] | 0.2025 | research | machine-generated |
| mwl-x-sendim | mirandese_g2p | 11 | 0.3914 | [0.2347, 0.5405] | 0.1818 | research | expert-human |
| nb | wikipron | 226 | 0.5133 | [0.4920, 0.5354] | 0.0177 | skeleton | crowd-scraped |
| nl | wikipron | 260 | 0.3135 | [0.2854, 0.3411] | 0.1692 | research | crowd-scraped |
| oc | wikipron | 266 | 0.1604 | [0.1421, 0.1793] | 0.3722 | research | crowd-scraped |
| pl | styletts2_phonemes | 299 | 0.1867 | [0.1764, 0.1978] | 0.0000 | research | machine-generated |
| pl | wikipron | 287 | 0.1195 | [0.1060, 0.1346] | 0.3624 | research | crowd-scraped |
| pt | styletts2_phonemes | 300 | 0.3890 | [0.3785, 0.3992] | 0.0000 | research | machine-generated |
| pt | wikipron | 242 | 0.1795 | [0.1547, 0.2045] | 0.4050 | research | crowd-scraped |
| pt-AO | portuguese_phonetic_lexicon | 300 | 0.2757 | [0.2586, 0.2924] | 0.0767 | research | crowd-scraped |
| pt-BR | portuguese_phonetic_lexicon | 300 | 0.2226 | [0.2091, 0.2362] | 0.0433 | research | crowd-scraped |
| pt-BR | wikipron | 124 | 0.1083 | [0.0770, 0.1403] | 0.5968 | research | crowd-scraped |
| pt-MZ | portuguese_phonetic_lexicon | 300 | 0.1923 | [0.1757, 0.2089] | 0.1933 | research | crowd-scraped |
| pt-PT | ep_dialects | 30 | 0.1733 | [0.1476, 0.2007] | 0.0000 | research | expert-human |
| pt-PT | infopedia_pt | 300 | 0.2649 | [0.2469, 0.2837] | 0.1000 | research | lexicon-derived |
| pt-PT | portuguese_phonetic_lexicon | 300 | 0.1449 | [0.1308, 0.1588] | 0.2933 | research | crowd-scraped |
| pt-PT-x-acores | clup_dialect | 2 | 0.3890 | [0.3833, 0.3948] | 0.0000 | research | expert-human |
| pt-PT-x-acores | ep_dialects | 29 | 0.2115 | [0.1809, 0.2481] | 0.0000 | research | expert-human |
| pt-PT-x-alentejo | clup_dialect | 1 | 0.3416 | [0.3416, 0.3416] | 0.0000 | research | expert-human |
| pt-PT-x-alentejo | ep_dialects | 30 | 0.2788 | [0.2366, 0.3225] | 0.0000 | research | expert-human |
| pt-PT-x-alfena | clup_dialect | 1 | 0.4070 | [0.4070, 0.4070] | 0.0000 | research | expert-human |
| pt-PT-x-algarve | clup_dialect | 3 | 0.4541 | [0.3964, 0.5075] | 0.0000 | research | expert-human |
| pt-PT-x-algarve | ep_dialects | 30 | 0.2748 | [0.2353, 0.3178] | 0.0000 | research | expert-human |
| pt-PT-x-aveiro | clup_dialect | 6 | 0.3747 | [0.3482, 0.4022] | 0.0000 | research | expert-human |
| pt-PT-x-beira | clup_dialect | 8 | 0.3869 | [0.3629, 0.4253] | 0.0000 | research | expert-human |
| pt-PT-x-lisbon | clup_dialect | 5 | 0.3959 | [0.3665, 0.4238] | 0.0000 | research | expert-human |
| pt-PT-x-lisbon | ep_dialects | 45 | 0.1987 | [0.1720, 0.2266] | 0.0222 | research | expert-human |
| pt-PT-x-madeira | clup_dialect | 4 | 0.3905 | [0.3523, 0.4392] | 0.0000 | research | expert-human |
| pt-PT-x-madeira | ep_dialects | 30 | 0.1757 | [0.1424, 0.2098] | 0.0333 | research | expert-human |
| pt-PT-x-minho | clup_dialect | 9 | 0.3844 | [0.3558, 0.4143] | 0.0000 | research | expert-human |
| pt-PT-x-porto | clup_dialect | 17 | 0.4495 | [0.4204, 0.4768] | 0.0000 | research | expert-human |
| pt-PT-x-porto | ep_dialects | 40 | 0.1997 | [0.1724, 0.2259] | 0.0500 | research | expert-human |
| pt-PT-x-trasosmontes | clup_dialect | 6 | 0.3995 | [0.3746, 0.4260] | 0.0000 | research | expert-human |
| pt-PT-x-viana | clup_dialect | 4 | 0.4295 | [0.3982, 0.4707] | 0.0000 | research | expert-human |
| pt-TL | portuguese_phonetic_lexicon | 300 | 0.3808 | [0.3649, 0.3967] | 0.0100 | research | crowd-scraped |
| ro | wikipron | 281 | 0.0597 | [0.0486, 0.0710] | 0.6370 | research | crowd-scraped |
| ru | styletts2_phonemes | 299 | 0.3934 | [0.3827, 0.4046] | 0.0000 | research | machine-generated |
| ru | wikipron | 268 | 0.3635 | [0.3475, 0.3795] | 0.0112 | research | crowd-scraped |
| sk | wikipron | 300 | 0.1206 | [0.1029, 0.1370] | 0.4700 | research | crowd-scraped |
| sq | wikipron | 249 | 0.0915 | [0.0719, 0.1113] | 0.6867 | research | crowd-scraped |
| sr | ipa_childes | 300 | 0.4611 | [0.4391, 0.4828] | 0.0567 | research | machine-generated |
| sv | styletts2_phonemes | 300 | 0.3835 | [0.3752, 0.3924] | 0.0000 | research | machine-generated |
| sv | wikipron | 279 | 0.3508 | [0.3305, 0.3721] | 0.0609 | research | crowd-scraped |
| ta | wikipron | 293 | 0.8949 | [0.8631, 0.9324] | 0.0000 | research | crowd-scraped |
| tl | wikipron | 269 | 0.2309 | [0.2150, 0.2464] | 0.0446 | research | crowd-scraped |
| tr | wikipron | 296 | 0.1409 | [0.1236, 0.1592] | 0.3953 | research | crowd-scraped |
| uk | styletts2_phonemes | 299 | 0.4960 | [0.4842, 0.5074] | 0.0000 | research | machine-generated |
| zh | ipa_childes | 300 | 0.5108 | [0.4910, 0.5300] | 0.0200 | research | machine-generated |
