# Scoreboard

**Grain of salt — read this first.** Reliable G2P "gold" barely exists. Most datasets below are semi-automated, dictionary-extracted, community-scraped, or a phonemizer's OWN output reused as a reference. A low PER against a `machine-generated` gold means "agrees with that tool", NOT "correct". Absolute PER is noisy — read every number as **directional/relative**, and cross-reference the `95% CI` (a wide or degenerate interval, common on small-`N` rows, means the row cannot support a conclusion). Full per-dataset classification and the honest caveats: [`docs/benchmarks.md`](benchmarks.md) ("Provenance and reliability").

`Provenance` legend (most → least trustworthy, all still subject to notation conventions and small-`N` noise): **expert-human** (phonetician / native-speaker / expert-annotator) > **lexicon-derived** (dictionary, human lexicographers) > **crowd-scraped** (Wiktionary) > **machine-generated** (some other tool's output; agreement-with-tool, not correctness) > **espeak-derived** / **epitran-derived** (a COMPETITOR's output: measures agreement with a system we benchmark ourselves against, so it can neither qualify a language for `production` nor block one) > **llm-generated** (an LLM's output: no lexicon, no rules, therefore no error model — a disagreement is not even diagnostic; never gate on it).

Committed PER/exact-match results for every gold dataset/language combination registered in `scripts/benchmark.py`. Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard
```

Machine-readable form: [`benchmarks/results.json`](../benchmarks/results.json). Methodology and dataset provenance: [`docs/benchmarks.md`](benchmarks.md).

The `95% CI` column is a bootstrap confidence interval on the mean PER (per-word PERs resampled with replacement, 1000 reps, fixed seed 20260710) — see [`docs/benchmarks.md`](benchmarks.md).

| Lang | Dataset | N | PER | 95% CI | Exact match | Quality tier | Provenance |
|---|---|---:|---:|---:|---:|---|---|
| an | wikipron | 902 | 0.0653 | [0.0588, 0.0720] | 0.6530 | research | crowd-scraped |
| ar | ipadict | 857160 | 0.3762 | [0.3760, 0.3764] | 0.0028 | research | machine-generated |
| ar | wikipron | 14268 | 0.3128 | [0.3106, 0.3151] | 0.0453 | research | crowd-scraped |
| ast | wikipron | 4167 | 0.0654 | [0.0621, 0.0685] | 0.6439 | research | crowd-scraped |
| ca | 4catac | 160 | 0.1054 | [0.0995, 0.1111] | 0.0062 | research | expert-human |
| ca | ipa_childes | 3813 | 0.2886 | [0.2824, 0.2948] | 0.1618 | research | espeak-derived |
| ca | styletts2_phonemes | 13442 | 0.3119 | [0.3105, 0.3134] | 0.0000 | research | espeak-derived |
| ca | wikipron | 106 | 0.2678 | [0.2210, 0.3107] | 0.3113 | research | crowd-scraped |
| ca-x-balear | 4catac | 160 | 0.1927 | [0.1855, 0.2003] | 0.0000 | research | expert-human |
| ca-x-occidental | 4catac | 160 | 0.1204 | [0.1141, 0.1276] | 0.0000 | research | expert-human |
| ca-x-valencia | 4catac | 160 | 0.0946 | [0.0884, 0.1007] | 0.0062 | research | expert-human |
| cy | ipa_childes | 4662 | 0.3009 | [0.2933, 0.3084] | 0.2711 | research | espeak-derived |
| cy | wikipron | 14467 | 0.2153 | [0.2123, 0.2185] | 0.3044 | research | crowd-scraped |
| da | ipa_childes | 2233 | 0.4704 | [0.4582, 0.4829] | 0.0506 | research | espeak-derived |
| da | wikipron | 4331 | 0.3427 | [0.3361, 0.3493] | 0.1152 | research | crowd-scraped |
| de | styletts2_phonemes | 11351 | 0.4079 | [0.4062, 0.4095] | 0.0000 | research | espeak-derived |
| de | wikipron | 53010 | 0.3265 | [0.3251, 0.3279] | 0.0563 | research | crowd-scraped |
| de-DE | ipa_childes | 24857 | 0.3881 | [0.3860, 0.3904] | 0.0356 | research | epitran-derived |
| de-DE | ipadict | 777785 | 0.3526 | [0.3522, 0.3529] | 0.0166 | research | crowd-scraped |
| el | styletts2_phonemes | 10081 | 0.2015 | [0.1994, 0.2038] | 0.0001 | research | espeak-derived |
| el | wikipron | 19108 | 0.1318 | [0.1298, 0.1337] | 0.3310 | research | crowd-scraped |
| en | styletts2_phonemes | 10199 | 0.2853 | [0.2834, 0.2871] | 0.0000 | research | espeak-derived |
| en | wikipron | 78439 | 0.3739 | [0.3722, 0.3754] | 0.1020 | research | crowd-scraped |
| en-GB | ipa_childes | 11447 | 0.3864 | [0.3823, 0.3905] | 0.0974 | research | espeak-derived |
| en-GB | ipadict | 65119 | 0.3427 | [0.3410, 0.3442] | 0.1187 | research | espeak-derived |
| en-GB | wikipron | 78381 | 0.3494 | [0.3479, 0.3510] | 0.1186 | research | crowd-scraped |
| en-US | ipa_babylm | 20111 | 0.5257 | [0.5178, 0.5329] | 0.1159 | research | espeak-derived |
| en-US | ipa_childes | 18055 | 0.4296 | [0.4258, 0.4334] | 0.1140 | research | espeak-derived |
| en-US | ipadict | 125927 | 0.5758 | [0.5742, 0.5773] | 0.0267 | research | lexicon-derived |
| eo | ipadict | 23245 | 0.0338 | [0.0330, 0.0346] | 0.7502 | research | machine-generated |
| eo | wikipron | 41245 | 0.0569 | [0.0559, 0.0579] | 0.7491 | research | crowd-scraped |
| es | styletts2_phonemes | 10367 | 0.1332 | [0.1312, 0.1351] | 0.0002 | research | espeak-derived |
| es | wikipron | 131506 | 0.0845 | [0.0840, 0.0850] | 0.4457 | research | crowd-scraped |
| es-ES | ipa_childes | 13155 | 0.0945 | [0.0922, 0.0966] | 0.5391 | research | epitran-derived |
| es-ES | ipadict | 595896 | 0.0537 | [0.0535, 0.0538] | 0.5734 | research | machine-generated |
| es-MX | ipadict | 595885 | 0.0633 | [0.0631, 0.0635] | 0.5111 | skeleton | machine-generated |
| et | ipa_childes | 11040 | 0.2953 | [0.2922, 0.2985] | 0.1041 | research | espeak-derived |
| eu | hitz_basque_ipa | 3113 | 0.2089 | [0.2025, 0.2156] | 0.2310 | research | machine-generated |
| eu | ipa_childes | 3969 | 0.1297 | [0.1254, 0.1343] | 0.3938 | research | espeak-derived |
| eu | wikipron | 12010 | 0.0391 | [0.0377, 0.0405] | 0.6979 | research | crowd-scraped |
| ext-PT-x-barrancos | barranquenho_dict | 316 | 0.1366 | [0.1169, 0.1568] | 0.5285 | research | llm-generated |
| fa | ipadict | 7695 | 0.4816 | [0.4791, 0.4842] | 0.0003 | research | machine-generated |
| fa | styletts2_phonemes | 12796 | 0.5760 | [0.5751, 0.5771] | 0.0000 | research | espeak-derived |
| fi | ipadict | 92836 | 0.1002 | [0.0996, 0.1008] | 0.3089 | research | machine-generated |
| fi | styletts2_phonemes | 10339 | 0.2920 | [0.2894, 0.2945] | 0.0000 | research | espeak-derived |
| fi | wikipron | 168808 | 0.0552 | [0.0549, 0.0555] | 0.4939 | research | crowd-scraped |
| fr | styletts2_phonemes | 10379 | 0.2395 | [0.2378, 0.2411] | 0.0000 | research | espeak-derived |
| fr | wikipron | 85496 | 0.1773 | [0.1762, 0.1785] | 0.3210 | research | crowd-scraped |
| fr-FR | ipa_childes | 9443 | 0.1966 | [0.1921, 0.2011] | 0.4064 | research | espeak-derived |
| fr-FR | ipadict | 245715 | 0.2033 | [0.2026, 0.2041] | 0.2614 | research | machine-generated |
| ga | ipa_childes | 1611 | 0.2976 | [0.2873, 0.3075] | 0.1651 | research | espeak-derived |
| ga | wikipron | 9616 | 0.1821 | [0.1787, 0.1857] | 0.3144 | research | crowd-scraped |
| gd | wikipron | 3719 | 0.3213 | [0.3145, 0.3285] | 0.1492 | research | crowd-scraped |
| gl | wikipron | 8091 | 0.0928 | [0.0902, 0.0955] | 0.5485 | research | crowd-scraped |
| hi | wikipron | 30375 | 0.1563 | [0.1549, 0.1577] | 0.2319 | research | crowd-scraped |
| hr | ipa_childes | 4769 | 0.2066 | [0.2016, 0.2117] | 0.2772 | research | epitran-derived |
| hr | wikipron | 26469 | 0.2998 | [0.2982, 0.3014] | 0.0050 | research | crowd-scraped |
| hu | ipa_childes | 4776 | 0.1331 | [0.1292, 0.1371] | 0.3961 | research | epitran-derived |
| hy | wikipron | 17704 | 0.1027 | [0.1010, 0.1044] | 0.4681 | research | crowd-scraped |
| id | ipa_childes | 9646 | 0.1223 | [0.1197, 0.1250] | 0.4566 | research | epitran-derived |
| is | ipa_childes | 4106 | 0.3935 | [0.3878, 0.3990] | 0.0356 | research | espeak-derived |
| is | ipadict | 60642 | 0.2694 | [0.2681, 0.2705] | 0.0628 | research | lexicon-derived |
| is | wikipron | 10093 | 0.2514 | [0.2483, 0.2545] | 0.1120 | research | crowd-scraped |
| it | styletts2_phonemes | 10197 | 0.2042 | [0.2021, 0.2062] | 0.0000 | research | espeak-derived |
| it | wikipron | 82276 | 0.1083 | [0.1075, 0.1091] | 0.3840 | research | crowd-scraped |
| it-IT | ipa_childes | 4583 | 0.2599 | [0.2543, 0.2655] | 0.1767 | research | espeak-derived |
| ja | ipadict | 115495 | 0.3771 | [0.3755, 0.3786] | 0.1418 | research | lexicon-derived |
| jam | ipadict | 1869 | 0.1769 | [0.1665, 0.1861] | 0.3863 | research | lexicon-derived |
| km | ipadict | 3257 | 0.6351 | [0.6299, 0.6410] | 0.0000 | skeleton | lexicon-derived |
| lad | wikipron | 131 | 0.1408 | [0.1136, 0.1691] | 0.4427 | research | crowd-scraped |
| ml | wikipron | 9464 | 0.3321 | [0.3288, 0.3355] | 0.0450 | research | crowd-scraped |
| ms | ipadict | 27894 | 0.6924 | [0.6911, 0.6937] | 0.0001 | stub | machine-generated |
| mwl | mirandese_dict | 572 | 0.3033 | [0.2823, 0.3241] | 0.1923 | research | llm-generated |
| mwl | mirandese_g2p | 205 | 0.1862 | [0.1610, 0.2141] | 0.3610 | research | expert-human |
| mwl-x-ifanes | mirandese_dict | 4 | 0.5000 | [0.1667, 0.8333] | 0.2500 | research | llm-generated |
| mwl-x-ifanes | mirandese_g2p | 2 | 0.7500 | [0.5000, 1.0000] | 0.0000 | research | expert-human |
| mwl-x-sendim | mirandese_dict | 79 | 0.2858 | [0.2364, 0.3370] | 0.2025 | research | llm-generated |
| mwl-x-sendim | mirandese_g2p | 11 | 0.3914 | [0.2347, 0.5405] | 0.1818 | research | expert-human |
| nb | ipa_childes | 3176 | 0.4044 | [0.3959, 0.4123] | 0.1020 | research | espeak-derived |
| nb | ipadict | 10169 | 0.3503 | [0.3461, 0.3544] | 0.1065 | research | machine-generated |
| nb | wikipron | 2725 | 0.3553 | [0.3455, 0.3643] | 0.1468 | research | crowd-scraped |
| nl | ipa_childes | 8108 | 0.3459 | [0.3413, 0.3503] | 0.1238 | research | espeak-derived |
| nl | ipadict | 117869 | 0.2925 | [0.2915, 0.2937] | 0.1092 | research | machine-generated |
| nl | wikipron | 45872 | 0.2663 | [0.2649, 0.2680] | 0.1286 | research | crowd-scraped |
| oc | wikipron | 675 | 0.1608 | [0.1472, 0.1731] | 0.3985 | research | crowd-scraped |
| or | ipadict | 6216 | 0.1176 | [0.1146, 0.1205] | 0.3867 | research | machine-generated |
| pl | ipa_childes | 15523 | 0.3063 | [0.3032, 0.3095] | 0.1487 | research | espeak-derived |
| pl | styletts2_phonemes | 11435 | 0.1951 | [0.1929, 0.1972] | 0.0000 | research | espeak-derived |
| pl | wikipron | 148990 | 0.1213 | [0.1207, 0.1219] | 0.3523 | research | crowd-scraped |
| pt | styletts2_phonemes | 11552 | 0.3443 | [0.3427, 0.3460] | 0.0000 | research | espeak-derived |
| pt | wikipron | 56891 | 0.1076 | [0.1065, 0.1087] | 0.4769 | research | crowd-scraped |
| pt-AO | portuguese_phonetic_lexicon | 53348 | 0.2714 | [0.2701, 0.2727] | 0.0753 | research | crowd-scraped |
| pt-BR | ipa_childes | 2116 | 0.2536 | [0.2451, 0.2627] | 0.2595 | research | espeak-derived |
| pt-BR | ipadict | 95933 | 0.2436 | [0.2426, 0.2445] | 0.0434 | research | machine-generated |
| pt-BR | portuguese_phonetic_lexicon | 53346 | 0.2199 | [0.2188, 0.2210] | 0.0729 | research | crowd-scraped |
| pt-BR | wikipron | 57814 | 0.0662 | [0.0652, 0.0671] | 0.6195 | research | crowd-scraped |
| pt-MZ | portuguese_phonetic_lexicon | 53346 | 0.2018 | [0.2005, 0.2031] | 0.1947 | research | crowd-scraped |
| pt-PT | ep_dialects | 30 | 0.1339 | [0.1066, 0.1614] | 0.1000 | research | expert-human |
| pt-PT | infopedia_pt | 102684 | 0.2511 | [0.2501, 0.2521] | 0.1094 | research | lexicon-derived |
| pt-PT | ipa_childes | 3846 | 0.2449 | [0.2388, 0.2508] | 0.2470 | research | espeak-derived |
| pt-PT | portuguese_phonetic_lexicon | 53349 | 0.1397 | [0.1386, 0.1407] | 0.2948 | research | crowd-scraped |
| pt-PT-x-acores | clup_dialect | 2 | 0.3441 | [0.3401, 0.3482] | 0.0000 | research | expert-human |
| pt-PT-x-acores | ep_dialects | 29 | 0.1427 | [0.1140, 0.1720] | 0.0345 | research | expert-human |
| pt-PT-x-alentejo | clup_dialect | 1 | 0.2943 | [0.2943, 0.2943] | 0.0000 | research | expert-human |
| pt-PT-x-alentejo | ep_dialects | 30 | 0.2338 | [0.1813, 0.2946] | 0.0667 | research | expert-human |
| pt-PT-x-alfena | clup_dialect | 1 | 0.3348 | [0.3348, 0.3348] | 0.0000 | research | expert-human |
| pt-PT-x-algarve | clup_dialect | 3 | 0.3898 | [0.3166, 0.4652] | 0.0000 | research | expert-human |
| pt-PT-x-algarve | ep_dialects | 30 | 0.1759 | [0.1346, 0.2162] | 0.1333 | research | expert-human |
| pt-PT-x-aveiro | clup_dialect | 6 | 0.3250 | [0.3058, 0.3472] | 0.0000 | research | expert-human |
| pt-PT-x-beira | clup_dialect | 8 | 0.3524 | [0.3207, 0.3935] | 0.0000 | research | expert-human |
| pt-PT-x-lisbon | clup_dialect | 5 | 0.3237 | [0.2836, 0.3724] | 0.0000 | research | expert-human |
| pt-PT-x-lisbon | ep_dialects | 45 | 0.1438 | [0.1188, 0.1688] | 0.0889 | research | expert-human |
| pt-PT-x-madeira | clup_dialect | 4 | 0.3460 | [0.3082, 0.3839] | 0.0000 | research | expert-human |
| pt-PT-x-madeira | ep_dialects | 30 | 0.1241 | [0.0888, 0.1606] | 0.2000 | research | expert-human |
| pt-PT-x-minho | clup_dialect | 9 | 0.3322 | [0.3073, 0.3570] | 0.0000 | research | expert-human |
| pt-PT-x-porto | clup_dialect | 17 | 0.4150 | [0.3907, 0.4378] | 0.0000 | research | expert-human |
| pt-PT-x-porto | ep_dialects | 40 | 0.1603 | [0.1317, 0.1947] | 0.1250 | research | expert-human |
| pt-PT-x-trasosmontes | clup_dialect | 6 | 0.3537 | [0.3313, 0.3807] | 0.0000 | research | expert-human |
| pt-PT-x-viana | clup_dialect | 4 | 0.3851 | [0.3519, 0.4206] | 0.0000 | research | expert-human |
| pt-TL | portuguese_phonetic_lexicon | 53346 | 0.3840 | [0.3828, 0.3853] | 0.0157 | research | crowd-scraped |
| qu | ipa_childes | 1850 | 0.4421 | [0.4322, 0.4519] | 0.0676 | stub | espeak-derived |
| ro | wikipron | 8977 | 0.0348 | [0.0334, 0.0366] | 0.7683 | research | crowd-scraped |
| ro-RO | ipa_childes | 2311 | 0.2647 | [0.2565, 0.2723] | 0.1839 | research | espeak-derived |
| ro-RO | ipadict | 72375 | 0.0479 | [0.0473, 0.0486] | 0.6976 | research | lexicon-derived |
| ru | styletts2_phonemes | 10555 | 0.3809 | [0.3789, 0.3830] | 0.0000 | research | espeak-derived |
| ru | wikipron | 403870 | 0.3073 | [0.3070, 0.3077] | 0.0149 | research | crowd-scraped |
| sk | wikipron | 15893 | 0.1432 | [0.1405, 0.1460] | 0.4404 | research | crowd-scraped |
| sq | wikipron | 4900 | 0.0965 | [0.0928, 0.1003] | 0.5606 | research | crowd-scraped |
| sr | ipa_childes | 9838 | 0.4244 | [0.4213, 0.4275] | 0.0327 | research | epitran-derived |
| sv | ipa_childes | 5202 | 0.3472 | [0.3411, 0.3536] | 0.1690 | research | espeak-derived |
| sv | ipadict | 21094 | 0.3183 | [0.3156, 0.3208] | 0.0704 | research | lexicon-derived |
| sv | styletts2_phonemes | 2706 | 0.3505 | [0.3473, 0.3538] | 0.0000 | research | espeak-derived |
| sv | wikipron | 5076 | 0.2747 | [0.2689, 0.2817] | 0.2394 | research | crowd-scraped |
| sw | ipadict | 48308 | 0.2206 | [0.2190, 0.2222] | 0.2044 | research | machine-generated |
| ta | wikipron | 10093 | 0.4235 | [0.4202, 0.4270] | 0.0183 | research | crowd-scraped |
| tl | wikipron | 25857 | 0.1179 | [0.1162, 0.1195] | 0.4318 | research | crowd-scraped |
| tr | ipa_childes | 2748 | 0.1374 | [0.1329, 0.1420] | 0.3646 | research | espeak-derived |
| tr | wikipron | 11579 | 0.1236 | [0.1208, 0.1264] | 0.4470 | research | crowd-scraped |
| uk | styletts2_phonemes | 9888 | 0.5413 | [0.5391, 0.5431] | 0.0000 | research | espeak-derived |
| vi | ipadict | 70902 | 0.6384 | [0.6375, 0.6392] | 0.0000 | research | machine-generated |
| zh | ipa_childes | 4717 | 0.5167 | [0.5125, 0.5209] | 0.0087 | research | machine-generated |
