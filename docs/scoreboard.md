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
| ar | wikipron | 14268 | 0.3131 | [0.3109, 0.3153] | 0.0452 | research | crowd-scraped |
| ast | wikipron | 4167 | 0.0654 | [0.0621, 0.0685] | 0.6439 | research | crowd-scraped |
| ca | 4catac | 160 | 0.4026 | [0.3930, 0.4120] | 0.0000 | research | expert-human |
| ca | styletts2_phonemes | 13442 | 0.4061 | [0.4048, 0.4075] | 0.0000 | research | espeak-derived |
| ca-x-balear | 4catac | 160 | 0.3893 | [0.3803, 0.3986] | 0.0000 | research | expert-human |
| ca-x-occidental | 4catac | 160 | 0.4663 | [0.4578, 0.4748] | 0.0000 | research | expert-human |
| ca-x-valencia | 4catac | 160 | 0.2994 | [0.2907, 0.3078] | 0.0000 | research | expert-human |
| cy | wikipron | 14467 | 0.2153 | [0.2123, 0.2185] | 0.3044 | research | crowd-scraped |
| da | wikipron | 4331 | 0.4511 | [0.4450, 0.4574] | 0.0420 | research | crowd-scraped |
| de | styletts2_phonemes | 11351 | 0.4285 | [0.4269, 0.4301] | 0.0000 | research | espeak-derived |
| de | wikipron | 53010 | 0.3265 | [0.3251, 0.3279] | 0.0563 | research | crowd-scraped |
| el | styletts2_phonemes | 10081 | 0.2095 | [0.2074, 0.2117] | 0.0000 | research | espeak-derived |
| el | wikipron | 19108 | 0.1318 | [0.1298, 0.1337] | 0.3310 | research | crowd-scraped |
| en | styletts2_phonemes | 10199 | 0.4570 | [0.4556, 0.4586] | 0.0000 | research | espeak-derived |
| en | wikipron | 78439 | 0.3739 | [0.3722, 0.3754] | 0.1020 | research | crowd-scraped |
| en-GB | wikipron | 78381 | 0.3494 | [0.3479, 0.3510] | 0.1186 | research | crowd-scraped |
| en-US | ipa_childes | 18055 | 0.4296 | [0.4258, 0.4334] | 0.1140 | research | machine-generated |
| eo | wikipron | 41245 | 0.0569 | [0.0559, 0.0579] | 0.7491 | research | crowd-scraped |
| es | styletts2_phonemes | 10367 | 0.1391 | [0.1370, 0.1410] | 0.0001 | research | espeak-derived |
| es | wikipron | 131506 | 0.0845 | [0.0840, 0.0850] | 0.4457 | research | crowd-scraped |
| et | ipa_childes | 11040 | 0.2953 | [0.2922, 0.2985] | 0.1041 | research | machine-generated |
| eu | hitz_basque_ipa | 3113 | 0.2089 | [0.2025, 0.2156] | 0.2310 | research | machine-generated |
| eu | wikipron | 12010 | 0.0391 | [0.0377, 0.0405] | 0.6979 | research | crowd-scraped |
| ext-PT-x-barrancos | barranquenho_dict | 316 | 0.1366 | [0.1169, 0.1568] | 0.5285 | research | machine-generated |
| fa | styletts2_phonemes | 12796 | 0.5770 | [0.5760, 0.5780] | 0.0000 | research | espeak-derived |
| fi | styletts2_phonemes | 10339 | 0.2991 | [0.2964, 0.3016] | 0.0000 | research | espeak-derived |
| fi | wikipron | 168808 | 0.0552 | [0.0549, 0.0555] | 0.4939 | research | crowd-scraped |
| fr | styletts2_phonemes | 10379 | 0.3532 | [0.3517, 0.3545] | 0.0000 | research | espeak-derived |
| fr | wikipron | 85496 | 0.1773 | [0.1762, 0.1785] | 0.3210 | research | crowd-scraped |
| ga | wikipron | 9621 | 0.4731 | [0.4673, 0.4785] | 0.0732 | research | crowd-scraped |
| gd | wikipron | 3720 | 0.6203 | [0.6110, 0.6305] | 0.0401 | research | crowd-scraped |
| gl | wikipron | 8091 | 0.0928 | [0.0902, 0.0955] | 0.5485 | research | crowd-scraped |
| hi | wikipron | 30375 | 0.4365 | [0.4349, 0.4382] | 0.0047 | research | crowd-scraped |
| hr | wikipron | 26469 | 0.2998 | [0.2982, 0.3014] | 0.0050 | research | crowd-scraped |
| hu | ipa_childes | 4776 | 0.1331 | [0.1292, 0.1371] | 0.3961 | research | machine-generated |
| hy | wikipron | 17704 | 0.1027 | [0.1010, 0.1044] | 0.4681 | research | crowd-scraped |
| id | ipa_childes | 9646 | 0.1223 | [0.1197, 0.1250] | 0.4566 | research | machine-generated |
| is | ipadict | 60642 | 0.2694 | [0.2681, 0.2705] | 0.0628 | research | lexicon-derived |
| is | wikipron | 10093 | 0.2514 | [0.2483, 0.2545] | 0.1120 | research | crowd-scraped |
| it | styletts2_phonemes | 10197 | 0.2233 | [0.2211, 0.2253] | 0.0000 | research | espeak-derived |
| it | wikipron | 82276 | 0.1083 | [0.1075, 0.1091] | 0.3840 | research | crowd-scraped |
| ml | wikipron | 9464 | 0.5019 | [0.4990, 0.5047] | 0.0023 | research | crowd-scraped |
| mwl | mirandese_dict | 572 | 0.3033 | [0.2823, 0.3241] | 0.1923 | research | machine-generated |
| mwl | mirandese_g2p | 205 | 0.1851 | [0.1597, 0.2127] | 0.3610 | research | expert-human |
| mwl-x-ifanes | mirandese_dict | 4 | 0.5000 | [0.1667, 0.8333] | 0.2500 | research | machine-generated |
| mwl-x-ifanes | mirandese_g2p | 2 | 0.7500 | [0.5000, 1.0000] | 0.0000 | research | expert-human |
| mwl-x-sendim | mirandese_dict | 79 | 0.2858 | [0.2364, 0.3370] | 0.2025 | research | machine-generated |
| mwl-x-sendim | mirandese_g2p | 11 | 0.3914 | [0.2347, 0.5405] | 0.1818 | research | expert-human |
| nb | wikipron | 2725 | 0.4871 | [0.4798, 0.4944] | 0.0316 | skeleton | crowd-scraped |
| nl | wikipron | 45872 | 0.2663 | [0.2649, 0.2680] | 0.1286 | research | crowd-scraped |
| oc | wikipron | 675 | 0.1608 | [0.1472, 0.1731] | 0.3985 | research | crowd-scraped |
| pl | styletts2_phonemes | 11435 | 0.2098 | [0.2077, 0.2119] | 0.0000 | research | espeak-derived |
| pl | wikipron | 148990 | 0.1213 | [0.1207, 0.1219] | 0.3523 | research | crowd-scraped |
| pt | styletts2_phonemes | 11552 | 0.3865 | [0.3849, 0.3881] | 0.0000 | research | espeak-derived |
| pt | wikipron | 56891 | 0.1076 | [0.1065, 0.1087] | 0.4769 | research | crowd-scraped |
| pt-AO | portuguese_phonetic_lexicon | 53348 | 0.2715 | [0.2702, 0.2727] | 0.0753 | research | crowd-scraped |
| pt-BR | portuguese_phonetic_lexicon | 53346 | 0.2200 | [0.2189, 0.2211] | 0.0729 | research | crowd-scraped |
| pt-BR | wikipron | 57814 | 0.0662 | [0.0652, 0.0671] | 0.6195 | research | crowd-scraped |
| pt-MZ | portuguese_phonetic_lexicon | 53346 | 0.2020 | [0.2006, 0.2033] | 0.1946 | research | crowd-scraped |
| pt-PT | ep_dialects | 30 | 0.1733 | [0.1476, 0.2007] | 0.0000 | research | expert-human |
| pt-PT | infopedia_pt | 102684 | 0.2516 | [0.2505, 0.2526] | 0.1094 | research | lexicon-derived |
| pt-PT | portuguese_phonetic_lexicon | 53349 | 0.1397 | [0.1387, 0.1408] | 0.2946 | research | crowd-scraped |
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
| pt-TL | portuguese_phonetic_lexicon | 53346 | 0.3840 | [0.3828, 0.3853] | 0.0157 | research | crowd-scraped |
| ro | wikipron | 8977 | 0.0348 | [0.0334, 0.0366] | 0.7683 | research | crowd-scraped |
| ru | styletts2_phonemes | 10555 | 0.4041 | [0.4021, 0.4060] | 0.0000 | research | espeak-derived |
| ru | wikipron | 403870 | 0.3115 | [0.3112, 0.3119] | 0.0147 | research | crowd-scraped |
| sk | wikipron | 15893 | 0.1432 | [0.1405, 0.1460] | 0.4404 | research | crowd-scraped |
| sq | wikipron | 4900 | 0.0965 | [0.0928, 0.1003] | 0.5606 | research | crowd-scraped |
| sr | ipa_childes | 9838 | 0.4244 | [0.4213, 0.4275] | 0.0327 | research | machine-generated |
| sv | styletts2_phonemes | 2706 | 0.4019 | [0.3988, 0.4052] | 0.0000 | research | espeak-derived |
| sv | wikipron | 5076 | 0.3424 | [0.3371, 0.3477] | 0.0914 | research | crowd-scraped |
| ta | wikipron | 10093 | 0.7250 | [0.7211, 0.7287] | 0.0054 | research | crowd-scraped |
| tl | wikipron | 25857 | 0.1179 | [0.1162, 0.1195] | 0.4318 | research | crowd-scraped |
| tr | wikipron | 11579 | 0.1236 | [0.1208, 0.1264] | 0.4470 | research | crowd-scraped |
| uk | styletts2_phonemes | 9888 | 0.5507 | [0.5486, 0.5526] | 0.0000 | research | espeak-derived |
| zh | ipa_childes | 4717 | 0.5167 | [0.5125, 0.5209] | 0.0087 | research | machine-generated |
