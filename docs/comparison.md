# Comparison to other G2P systems

Committed cross-system comparison: orthography2ipa vs **espeak-ng**, **epitran**, **gruut**, **pycotovia** (Galician), and **pyahotts** (Basque) on the same gold datasets/loaders as [`docs/scoreboard.md`](scoreboard.md), using the same default `--limit` — so the `o2i PER` column here matches the scoreboard's rows for the same language/dataset pair. Regenerate with:

```bash
pip install '.[compare]'  # epitran, gruut, pycotovia, pyahotts — dev-only extra
PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard
```

Machine-readable form: [`benchmarks/comparison.json`](../benchmarks/comparison.json).

## Coverage

Not every gold language has a mapping for every competitor system: espeak-ng, epitran, gruut, pycotovia, and pyahotts each cover a different, smaller subset of languages than orthography2ipa's 350+ codes. A missing mapping, or a system that isn't installed, is reported as `n/a` for that row rather than skipped or faked — this table never crashes and never silently drops a system, it just says when it has nothing to compare. `epitran`/`gruut`/`pycotovia`/`pyahotts` are only installed via the dev-only `[compare]` extra; a committed run generated without them shows `n/a` in those columns for every row — that reflects the generating environment, not a claim those systems don't support the language. `pyahotts` is `n/a` for every row regardless of installation: its only public API synthesizes audio and exposes no text-level phoneme output, so there is nothing to compare against gold IPA (see the harness module docstring).

The `N` column is the number of unique gold words for that language/dataset pair; each system's own scored count can be slightly lower (a word it failed to transcribe is excluded from its PER, not counted as an error) — see the `*_n` fields in `benchmarks/comparison.json` for the exact per-system count.

## Normalization

Every system is scored with the identical normalization and PER metric orthography2ipa's own scoreboard uses (`scripts/benchmark.py:normalize`/`levenshtein`): NFC-normalize, strip stress marks (the length mark is retained), strip narrow-transcription diacritics (broad comparison), drop whitespace (segmentation-free), then score Levenshtein distance against the best-matching gold variant. No system is normalized differently or given a more forgiving metric.

## Honesty

This table includes languages where orthography2ipa **loses** to espeak-ng. Cherry-picking would make the comparison worthless.

| Lang | Dataset | N | o2i PER | espeak PER | epitran PER | gruut PER | pycotovia PER | pyahotts PER |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| ca | 4catac | 160 | 0.4120 | 0.1872 | n/a | n/a | n/a | n/a |
| ca-x-balear | 4catac | 160 | 0.3884 | 0.2174 | n/a | n/a | n/a | n/a |
| ca-x-occidental | 4catac | 160 | 0.5633 | 0.1939 | n/a | n/a | n/a | n/a |
| ca-x-valencia | 4catac | 160 | 0.3005 | 0.1878 | n/a | n/a | n/a | n/a |
| cy | wikipron | 276 | 0.2187 | 0.3137 | n/a | n/a | n/a | n/a |
| de | wikipron | 269 | 0.3613 | 0.2587 | n/a | n/a | n/a | n/a |
| el | wikipron | 298 | 0.1513 | 0.1218 | n/a | n/a | n/a | n/a |
| en | wikipron | 220 | 0.4661 | 0.4312 | n/a | n/a | n/a | n/a |
| es | wikipron | 298 | 0.1000 | 0.1534 | n/a | n/a | n/a | n/a |
| eu | hitz_basque_ipa | 300 | 0.2796 | 0.2253 | n/a | n/a | n/a | n/a |
| fi | wikipron | 294 | 0.0386 | 0.3915 | n/a | n/a | n/a | n/a |
| fr | wikipron | 279 | 0.1559 | 0.1200 | n/a | n/a | n/a | n/a |
| ga | wikipron | 134 | 0.4330 | 0.5792 | n/a | n/a | n/a | n/a |
| gl | wikipron | 264 | 0.0728 | n/a | n/a | n/a | 0.0773 | n/a |
| hi | wikipron | 262 | 0.4424 | 0.3661 | n/a | n/a | n/a | n/a |
| it | wikipron | 276 | 0.1004 | 0.1111 | n/a | n/a | n/a | n/a |
| nl | wikipron | 260 | 0.3135 | 0.1631 | n/a | n/a | n/a | n/a |
| pl | wikipron | 287 | 0.1195 | 0.1085 | n/a | n/a | n/a | n/a |
| ro | wikipron | 281 | 0.0597 | 0.1382 | n/a | n/a | n/a | n/a |
| ru | wikipron | 268 | 0.3635 | 0.4790 | n/a | n/a | n/a | n/a |
| sv | wikipron | 279 | 0.3508 | 0.3249 | n/a | n/a | n/a | n/a |
| tr | wikipron | 296 | 0.1409 | 0.2353 | n/a | n/a | n/a | n/a |

**o2i beats espeak on 8 of 21 comparable languages.**

## Catalan dialects vs espeak (BSC)

The Barcelona Supercomputing Center (BSC) added Catalan dialect voices to espeak-ng (central, balearic, north-western, valencian). This table compares each o2i Catalan dialect spec against the matching espeak-ng dialect voice on the 4catac gold (expert human-annotated regional accents) — the same expert gold used for the `ca` row in the main table above.

All three BSC dialect voices (`ca-ba`, `ca-nw`, `ca-va`) were found on this machine's espeak-ng install; each dialect row below uses its own dialect-specific voice.

| Dialect | o2i spec | espeak voice | N | o2i PER | espeak PER |
|---|---|---|---:|---:|---:|
| central | ca | ca | 160 | 0.4120 | 0.1872 |
| balear | ca-x-balear | ca-ba | 160 | 0.3884 | 0.2174 |
| valencian | ca-x-valencia | ca-va | 160 | 0.3005 | 0.1878 |
| occidental (nord-occidental) | ca-x-occidental | ca-nw | 160 | 0.5633 | 0.1939 |
