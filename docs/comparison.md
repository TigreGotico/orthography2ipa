# Comparison to other G2P systems

Committed cross-system comparison: orthography2ipa vs **espeak-ng**, **epitran**, and **gruut** on the same gold datasets/loaders as [`docs/scoreboard.md`](scoreboard.md), using the same default `--limit` — so the `o2i PER` column here matches the scoreboard's rows for the same language/dataset pair. Regenerate with:

```bash
pip install '.[compare]'  # epitran, gruut — dev-only extra
PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard
```

Machine-readable form: [`benchmarks/comparison.json`](../benchmarks/comparison.json).

## Coverage

Not every gold language has a mapping for every competitor system: espeak-ng, epitran, and gruut each cover a different, smaller subset of languages than orthography2ipa's 350+ codes. A missing mapping, or a system that isn't installed, is reported as `n/a` for that row rather than skipped or faked — this table never crashes and never silently drops a system, it just says when it has nothing to compare. `epitran`/`gruut` are only installed via the dev-only `[compare]` extra; a committed run generated without them shows `n/a` in those columns for every row — that reflects the generating environment, not a claim those systems don't support the language.

The `N` column is the number of unique gold words for that language/dataset pair; each system's own scored count can be slightly lower (a word it failed to transcribe is excluded from its PER, not counted as an error) — see the `*_n` fields in `benchmarks/comparison.json` for the exact per-system count.

## Normalization

Every system is scored with the identical normalization and PER metric orthography2ipa's own scoreboard uses (`scripts/benchmark.py:normalize`/`levenshtein`): NFC-normalize, strip stress marks (the length mark is retained), strip narrow-transcription diacritics (broad comparison), drop whitespace (segmentation-free), then score Levenshtein distance against the best-matching gold variant. No system is normalized differently or given a more forgiving metric.

## Honesty

This table includes languages where orthography2ipa **loses** to espeak-ng. Cherry-picking would make the comparison worthless.

| Lang | Dataset | N | o2i PER | espeak PER | epitran PER | gruut PER |
|---|---|---:|---:|---:|---:|---:|
| ca | 4catac | 160 | 0.4170 | 0.1872 | n/a | n/a |
| cy | wikipron | 276 | 0.2187 | 0.3137 | n/a | n/a |
| de | wikipron | 269 | 0.3613 | 0.2587 | n/a | n/a |
| el | wikipron | 298 | 0.1513 | 0.1218 | n/a | n/a |
| en | wikipron | 220 | 0.4799 | 0.4312 | n/a | n/a |
| es | wikipron | 298 | 0.1000 | 0.1534 | n/a | n/a |
| eu | hitz_basque_ipa | 300 | 0.2796 | 0.2253 | n/a | n/a |
| fi | wikipron | 294 | 0.0386 | 0.3915 | n/a | n/a |
| fr | wikipron | 279 | 0.1559 | 0.1200 | n/a | n/a |
| ga | wikipron | 134 | 0.4330 | 0.5792 | n/a | n/a |
| hi | wikipron | 262 | 0.4424 | 0.3661 | n/a | n/a |
| it | wikipron | 276 | 0.1004 | 0.1111 | n/a | n/a |
| nl | wikipron | 260 | 0.3135 | 0.1631 | n/a | n/a |
| pl | wikipron | 287 | 0.1195 | 0.1085 | n/a | n/a |
| ro | wikipron | 281 | 0.0597 | 0.1382 | n/a | n/a |
| ru | wikipron | 268 | 0.3635 | 0.4790 | n/a | n/a |
| sv | wikipron | 279 | 0.3508 | 0.3249 | n/a | n/a |
| tr | wikipron | 296 | 0.1409 | 0.2353 | n/a | n/a |

**o2i beats espeak on 8 of 18 comparable languages.**
