# Scoreboard

Committed PER/exact-match results for every gold dataset/language combination registered in `scripts/benchmark.py`. Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard
```

Machine-readable form: [`benchmarks/results.json`](../benchmarks/results.json). Methodology and dataset provenance: [`docs/benchmarks.md`](benchmarks.md).

| Lang | Dataset | N | PER | Exact match | Quality tier |
|---|---|---:|---:|---:|---|
| ar | wikipron | 259 | 0.2551 | 0.1120 | research |
| ast | wikipron | 300 | 0.0876 | 0.5900 | research |
| ca | 4catac | 160 | 0.4170 | 0.0000 | research |
| ca | styletts2_phonemes | 300 | 0.4043 | 0.0000 | research |
| ca-x-balear | 4catac | 160 | 0.3924 | 0.0000 | research |
| ca-x-occidental | 4catac | 160 | 0.5680 | 0.0000 | research |
| ca-x-valencia | 4catac | 160 | 0.3046 | 0.0000 | research |
| cy | wikipron | 276 | 0.2187 | 0.2899 | research |
| da | wikipron | 273 | 0.4415 | 0.0476 | research |
| de | styletts2_phonemes | 300 | 0.3964 | 0.0000 | research |
| de | wikipron | 269 | 0.3613 | 0.0297 | research |
| el | styletts2_phonemes | 298 | 0.2179 | 0.0000 | research |
| el | wikipron | 298 | 0.1517 | 0.3121 | research |
| en | styletts2_phonemes | 300 | 0.4464 | 0.0000 | research |
| en | wikipron | 220 | 0.4799 | 0.1000 | research |
| en-GB | wikipron | 245 | 0.4876 | 0.0816 | research |
| en-US | ipa_childes | 300 | 0.4166 | 0.2167 | research |
| eo | wikipron | 300 | 0.0303 | 0.8700 | research |
| es | styletts2_phonemes | 300 | 0.1713 | 0.0000 | research |
| es | wikipron | 298 | 0.1000 | 0.4765 | research |
| et | ipa_childes | 300 | 0.3094 | 0.1533 | research |
| eu | hitz_basque_ipa | 300 | 0.2796 | 0.1567 | research |
| eu | wikipron | 239 | 0.0768 | 0.5900 | research |
| fa | styletts2_phonemes | 294 | 0.5787 | 0.0000 | research |
| fi | styletts2_phonemes | 298 | 0.2919 | 0.0000 | research |
| fi | wikipron | 294 | 0.0386 | 0.7483 | research |
| fr | styletts2_phonemes | 300 | 0.3557 | 0.0000 | research |
| fr | wikipron | 279 | 0.1559 | 0.4624 | research |
| ga | wikipron | 134 | 0.4330 | 0.0373 | research |
| gd | wikipron | 210 | 0.6867 | 0.0286 | research |
| gl | wikipron | 264 | 0.0728 | 0.6326 | research |
| hi | wikipron | 261 | 0.4573 | 0.0077 | research |
| hr | wikipron | 292 | 0.2763 | 0.0171 | research |
| hu | ipa_childes | 297 | 0.1407 | 0.4444 | research |
| hy | wikipron | 297 | 0.0701 | 0.6229 | research |
| id | ipa_childes | 300 | 0.1103 | 0.5633 | research |
| is | ipadict | 300 | 0.2300 | 0.0900 | research |
| is | wikipron | 258 | 0.2232 | 0.1395 | research |
| it | styletts2_phonemes | 300 | 0.2100 | 0.0000 | research |
| it | wikipron | 276 | 0.1004 | 0.4855 | research |
| ml | wikipron | 280 | 0.6718 | 0.0000 | research |
| mwl | mirandese | 205 | 0.2244 | 0.2732 | research |
| mwl-x-sendim | mirandese | 11 | 0.4899 | 0.1818 | skeleton |
| nb | wikipron | 226 | 0.5133 | 0.0177 | skeleton |
| nl | wikipron | 260 | 0.3135 | 0.1692 | research |
| oc | wikipron | 266 | 0.1604 | 0.3722 | research |
| pl | styletts2_phonemes | 299 | 0.1867 | 0.0000 | research |
| pl | wikipron | 287 | 0.1195 | 0.3624 | research |
| pt | styletts2_phonemes | 300 | 0.3999 | 0.0000 | research |
| pt | wikipron | 242 | 0.1817 | 0.3058 | research |
| pt-BR | wikipron | 124 | 0.1901 | 0.3952 | research |
| pt-PT | ep_dialects | 30 | 0.2599 | 0.0000 | research |
| pt-PT | infopedia_pt | 295 | 0.3160 | 0.1390 | research |
| pt-PT-x-acores | clup_dialect | 2 | 0.4889 | 0.0000 | research |
| pt-PT-x-acores | ep_dialects | 29 | 0.3521 | 0.0000 | research |
| pt-PT-x-alentejo | clup_dialect | 1 | 0.3915 | 0.0000 | research |
| pt-PT-x-alentejo | ep_dialects | 30 | 0.3216 | 0.0333 | research |
| pt-PT-x-alfena | clup_dialect | 1 | 0.4836 | 0.0000 | skeleton |
| pt-PT-x-algarve | clup_dialect | 3 | 0.5456 | 0.0000 | research |
| pt-PT-x-algarve | ep_dialects | 30 | 0.3549 | 0.0000 | research |
| pt-PT-x-aveiro | clup_dialect | 6 | 0.4518 | 0.0000 | skeleton |
| pt-PT-x-beira | clup_dialect | 8 | 0.4590 | 0.0000 | research |
| pt-PT-x-lisbon | clup_dialect | 5 | 0.4711 | 0.0000 | research |
| pt-PT-x-lisbon | ep_dialects | 45 | 0.2851 | 0.0000 | research |
| pt-PT-x-madeira | clup_dialect | 4 | 0.4630 | 0.0000 | research |
| pt-PT-x-madeira | ep_dialects | 30 | 0.2662 | 0.0000 | research |
| pt-PT-x-minho | clup_dialect | 9 | 0.4588 | 0.0000 | research |
| pt-PT-x-porto | clup_dialect | 17 | 0.5134 | 0.0000 | research |
| pt-PT-x-porto | ep_dialects | 40 | 0.2550 | 0.0500 | research |
| pt-PT-x-trasosmontes | clup_dialect | 6 | 0.4819 | 0.0000 | research |
| pt-PT-x-viana | clup_dialect | 4 | 0.4880 | 0.0000 | skeleton |
| ro | wikipron | 281 | 0.0597 | 0.6370 | research |
| ru | styletts2_phonemes | 299 | 0.3934 | 0.0000 | research |
| ru | wikipron | 268 | 0.3635 | 0.0112 | research |
| sk | wikipron | 300 | 0.1206 | 0.4700 | research |
| sq | wikipron | 249 | 0.0915 | 0.6867 | research |
| sr | ipa_childes | 300 | 0.4764 | 0.0467 | research |
| sv | styletts2_phonemes | 300 | 0.3835 | 0.0000 | research |
| sv | wikipron | 279 | 0.3508 | 0.0609 | research |
| ta | wikipron | 293 | 0.8949 | 0.0000 | research |
| tl | wikipron | 269 | 0.2309 | 0.0446 | research |
| tr | wikipron | 296 | 0.1397 | 0.3986 | research |
| uk | styletts2_phonemes | 299 | 0.4960 | 0.0000 | research |
| zh | ipa_childes | 300 | 0.5183 | 0.0200 | research |
