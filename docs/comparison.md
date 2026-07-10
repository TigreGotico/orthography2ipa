# Comparison to other G2P systems

Committed cross-system comparison: orthography2ipa vs **espeak-ng**, **epitran**, and **gruut** on the SAME gold rows used by [`docs/scoreboard.md`](scoreboard.md). Regenerate with:

```bash
pip install '.[compare]'  # epitran, gruut — dev-only extra
PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard
```

Machine-readable form: [`benchmarks/comparison.json`](../benchmarks/comparison.json).

## Coverage

Not every gold language has a mapping for every competitor system: espeak-ng, epitran, and gruut each cover a different, smaller subset of languages than orthography2ipa's 350+ codes. A missing mapping, or a system that isn't installed, is reported as `n/a` for that row rather than skipped or faked — this table never crashes and never silently drops a system, it just says when it has nothing to compare.

## Normalization

Every system is scored with the identical normalization and PER metric orthography2ipa's own scoreboard uses (`scripts/benchmark.py:normalize`/`levenshtein`): NFC-normalize, strip stress/length marks, strip narrow-transcription diacritics (broad comparison), drop whitespace (segmentation-free), then score Levenshtein distance against the best-matching gold variant. No system is normalized differently or given a more forgiving metric.

## Honesty

This table includes languages where orthography2ipa **loses** to espeak-ng. Cherry-picking would make the comparison worthless.

| Lang | Dataset | N | o2i PER | espeak PER | epitran PER | gruut PER |
|---|---|---:|---:|---:|---:|---:|
| ca | 4catac | 100 | 0.4272 | 0.1856 | n/a | n/a |
| cy | wikipron | 90 | 0.2660 | 0.4988 | n/a | n/a |
| de | wikipron | 89 | 0.3434 | 0.3530 | n/a | n/a |
| el | wikipron | 99 | 0.1544 | 0.1515 | n/a | n/a |
| en | wikipron | 86 | 0.4318 | 0.4563 | n/a | n/a |
| es | wikipron | 100 | 0.1361 | 0.1721 | n/a | n/a |
| eu | hitz_basque_ipa | 100 | 0.2650 | 0.2180 | n/a | n/a |
| fi | wikipron | 98 | 0.0298 | 0.3367 | n/a | n/a |
| fr | wikipron | 92 | 0.1938 | 0.1933 | n/a | n/a |
| ga | wikipron | 52 | 0.4435 | 0.5304 | n/a | n/a |
| hi | wikipron | 90 | 0.4687 | 0.3603 | n/a | n/a |
| it | wikipron | 91 | 0.1017 | 0.1503 | n/a | n/a |
| nl | wikipron | 85 | 0.2865 | 0.2342 | n/a | n/a |
| pl | wikipron | 94 | 0.1405 | 0.1070 | n/a | n/a |
| ro | wikipron | 96 | 0.0467 | 0.0979 | n/a | n/a |
| ru | wikipron | 90 | 0.3789 | 0.4664 | n/a | n/a |
| sv | wikipron | 97 | 0.3766 | 0.3501 | n/a | n/a |
| tr | wikipron | 98 | 0.1588 | 0.2124 | n/a | n/a |

**o2i beats espeak on 10 of 18 comparable languages.**
