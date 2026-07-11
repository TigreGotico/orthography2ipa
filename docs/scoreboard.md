# Scoreboard

Committed PER/exact-match results for every gold dataset/language combination registered in `scripts/benchmark.py`. Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard
```

Machine-readable form: [`benchmarks/results.json`](../benchmarks/results.json). Methodology and dataset provenance: [`docs/benchmarks.md`](benchmarks.md).

The `95% CI` column is a bootstrap confidence interval on the mean PER (per-word PERs resampled with replacement, 1000 reps, fixed seed 20260710) — see [`docs/benchmarks.md`](benchmarks.md).

| Lang | Dataset | N | PER | 95% CI | Exact match | Quality tier |
|---|---|---:|---:|---:|---:|---|
| ar | wikipron | 259 | 0.2551 | [0.2377, 0.2725] | 0.1120 | research |
| ast | wikipron | 300 | 0.0876 | [0.0731, 0.1014] | 0.5900 | research |
| ca | 4catac | 160 | 0.4120 | [0.4017, 0.4219] | 0.0000 | research |
| ca | styletts2_phonemes | 300 | 0.4083 | [0.3998, 0.4170] | 0.0000 | research |
| ca-x-balear | 4catac | 160 | 0.3884 | [0.3797, 0.3975] | 0.0000 | research |
| ca-x-occidental | 4catac | 160 | 0.5633 | [0.5549, 0.5720] | 0.0000 | research |
| ca-x-valencia | 4catac | 160 | 0.3005 | [0.2920, 0.3089] | 0.0000 | research |
| cy | wikipron | 276 | 0.2187 | [0.1968, 0.2433] | 0.2899 | research |
| da | wikipron | 273 | 0.4415 | [0.4128, 0.4693] | 0.0476 | research |
| de | styletts2_phonemes | 300 | 0.3964 | [0.3879, 0.4049] | 0.0000 | research |
| de | wikipron | 269 | 0.3613 | [0.3402, 0.3796] | 0.0297 | research |
| el | styletts2_phonemes | 298 | 0.2178 | [0.2023, 0.2326] | 0.0000 | research |
| el | wikipron | 298 | 0.1513 | [0.1341, 0.1678] | 0.3154 | research |
| en | styletts2_phonemes | 300 | 0.4379 | [0.4305, 0.4459] | 0.0000 | research |
| en | wikipron | 220 | 0.4661 | [0.4334, 0.4998] | 0.1000 | research |
| en-GB | wikipron | 245 | 0.4721 | [0.4420, 0.5058] | 0.0816 | research |
| en-US | ipa_childes | 300 | 0.4166 | [0.3809, 0.4528] | 0.2167 | research |
| eo | wikipron | 300 | 0.0303 | [0.0221, 0.0392] | 0.8700 | research |
| es | styletts2_phonemes | 300 | 0.1713 | [0.1584, 0.1851] | 0.0000 | research |
| es | wikipron | 298 | 0.1000 | [0.0870, 0.1134] | 0.4765 | research |
| et | ipa_childes | 300 | 0.3094 | [0.2876, 0.3304] | 0.1533 | research |
| eu | hitz_basque_ipa | 300 | 0.2796 | [0.2579, 0.3011] | 0.1567 | research |
| eu | wikipron | 239 | 0.0768 | [0.0614, 0.0939] | 0.5900 | research |
| fa | styletts2_phonemes | 294 | 0.5787 | [0.5724, 0.5858] | 0.0000 | research |
| fi | styletts2_phonemes | 298 | 0.2919 | [0.2783, 0.3060] | 0.0000 | research |
| fi | wikipron | 294 | 0.0386 | [0.0304, 0.0476] | 0.7483 | research |
| fr | styletts2_phonemes | 300 | 0.3557 | [0.3481, 0.3639] | 0.0000 | research |
| fr | wikipron | 279 | 0.1559 | [0.1332, 0.1781] | 0.4624 | research |
| ga | wikipron | 134 | 0.4330 | [0.3952, 0.4655] | 0.0373 | research |
| gd | wikipron | 210 | 0.6867 | [0.6496, 0.7220] | 0.0286 | research |
| gl | wikipron | 264 | 0.0728 | [0.0604, 0.0868] | 0.6326 | research |
| hi | wikipron | 261 | 0.4424 | [0.4254, 0.4583] | 0.0115 | research |
| hr | wikipron | 292 | 0.2763 | [0.2623, 0.2916] | 0.0171 | research |
| hu | ipa_childes | 297 | 0.1407 | [0.1220, 0.1592] | 0.4444 | research |
| hy | wikipron | 297 | 0.0701 | [0.0580, 0.0824] | 0.6229 | research |
| id | ipa_childes | 300 | 0.1103 | [0.0925, 0.1288] | 0.5633 | research |
| is | ipadict | 300 | 0.2300 | [0.2163, 0.2456] | 0.0900 | research |
| is | wikipron | 258 | 0.2232 | [0.2035, 0.2410] | 0.1395 | research |
| it | styletts2_phonemes | 300 | 0.2100 | [0.2000, 0.2214] | 0.0000 | research |
| it | wikipron | 276 | 0.1004 | [0.0844, 0.1146] | 0.4855 | research |
| ml | wikipron | 280 | 0.6099 | [0.5920, 0.6273] | 0.0000 | research |
| mwl | mirandese | 205 | 0.2244 | [0.1961, 0.2532] | 0.2732 | research |
| mwl-x-sendim | mirandese | 11 | 0.4899 | [0.2727, 0.6844] | 0.1818 | skeleton |
| nb | wikipron | 226 | 0.5133 | [0.4920, 0.5354] | 0.0177 | skeleton |
| nl | wikipron | 260 | 0.3135 | [0.2854, 0.3411] | 0.1692 | research |
| oc | wikipron | 266 | 0.1604 | [0.1421, 0.1793] | 0.3722 | research |
| pl | styletts2_phonemes | 299 | 0.1867 | [0.1764, 0.1978] | 0.0000 | research |
| pl | wikipron | 287 | 0.1195 | [0.1060, 0.1346] | 0.3624 | research |
| pt | styletts2_phonemes | 300 | 0.3999 | [0.3899, 0.4095] | 0.0000 | research |
| pt | wikipron | 242 | 0.1817 | [0.1607, 0.2031] | 0.3058 | research |
| pt-BR | wikipron | 124 | 0.1901 | [0.1572, 0.2236] | 0.3952 | research |
| pt-PT | ep_dialects | 30 | 0.2599 | [0.2226, 0.3020] | 0.0000 | research |
| pt-PT | infopedia_pt | 295 | 0.3160 | [0.2918, 0.3389] | 0.1390 | research |
| pt-PT-x-acores | clup_dialect | 2 | 0.4889 | [0.4860, 0.4918] | 0.0000 | research |
| pt-PT-x-acores | ep_dialects | 29 | 0.3521 | [0.3142, 0.3955] | 0.0000 | research |
| pt-PT-x-alentejo | clup_dialect | 1 | 0.3915 | [0.3915, 0.3915] | 0.0000 | research |
| pt-PT-x-alentejo | ep_dialects | 30 | 0.3216 | [0.2805, 0.3628] | 0.0333 | research |
| pt-PT-x-alfena | clup_dialect | 1 | 0.4836 | [0.4836, 0.4836] | 0.0000 | skeleton |
| pt-PT-x-algarve | clup_dialect | 3 | 0.5456 | [0.4970, 0.6070] | 0.0000 | research |
| pt-PT-x-algarve | ep_dialects | 30 | 0.3549 | [0.3101, 0.3972] | 0.0000 | research |
| pt-PT-x-aveiro | clup_dialect | 6 | 0.4518 | [0.4124, 0.4931] | 0.0000 | skeleton |
| pt-PT-x-beira | clup_dialect | 8 | 0.4590 | [0.4325, 0.4979] | 0.0000 | research |
| pt-PT-x-lisbon | clup_dialect | 5 | 0.4711 | [0.4326, 0.5078] | 0.0000 | research |
| pt-PT-x-lisbon | ep_dialects | 45 | 0.2851 | [0.2545, 0.3167] | 0.0000 | research |
| pt-PT-x-madeira | clup_dialect | 4 | 0.4630 | [0.4285, 0.5162] | 0.0000 | research |
| pt-PT-x-madeira | ep_dialects | 30 | 0.2662 | [0.2302, 0.3060] | 0.0000 | research |
| pt-PT-x-minho | clup_dialect | 9 | 0.4588 | [0.4319, 0.4858] | 0.0000 | research |
| pt-PT-x-porto | clup_dialect | 17 | 0.5134 | [0.4862, 0.5401] | 0.0000 | research |
| pt-PT-x-porto | ep_dialects | 40 | 0.2550 | [0.2202, 0.2864] | 0.0500 | research |
| pt-PT-x-trasosmontes | clup_dialect | 6 | 0.4819 | [0.4630, 0.5031] | 0.0000 | research |
| pt-PT-x-viana | clup_dialect | 4 | 0.4880 | [0.4473, 0.5358] | 0.0000 | skeleton |
| ro | wikipron | 281 | 0.0597 | [0.0486, 0.0710] | 0.6370 | research |
| ru | styletts2_phonemes | 299 | 0.3934 | [0.3827, 0.4046] | 0.0000 | research |
| ru | wikipron | 268 | 0.3635 | [0.3475, 0.3795] | 0.0112 | research |
| sk | wikipron | 300 | 0.1206 | [0.1029, 0.1370] | 0.4700 | research |
| sq | wikipron | 249 | 0.0915 | [0.0719, 0.1113] | 0.6867 | research |
| sr | ipa_childes | 300 | 0.4764 | [0.4545, 0.4984] | 0.0467 | research |
| sv | styletts2_phonemes | 300 | 0.3835 | [0.3752, 0.3924] | 0.0000 | research |
| sv | wikipron | 279 | 0.3508 | [0.3305, 0.3721] | 0.0609 | research |
| ta | wikipron | 293 | 0.8949 | [0.8631, 0.9324] | 0.0000 | research |
| tl | wikipron | 269 | 0.2309 | [0.2150, 0.2464] | 0.0446 | research |
| tr | wikipron | 296 | 0.1409 | [0.1236, 0.1592] | 0.3953 | research |
| uk | styletts2_phonemes | 299 | 0.4960 | [0.4842, 0.5074] | 0.0000 | research |
| zh | ipa_childes | 300 | 0.5183 | [0.4973, 0.5381] | 0.0200 | research |
