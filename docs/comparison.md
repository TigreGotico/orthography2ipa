# Comparison to other G2P systems

Committed cross-system comparison: orthography2ipa vs **espeak-ng**, **epitran**, **gruut**, **pycotovia** (Galician), and **ahotts-g2p** (Basque & Spanish) on the same gold datasets/loaders as [`docs/scoreboard.md`](scoreboard.md), using the FULL gold set of every mapped language (no cap — the same no-caps policy as the scoreboard; the one explicitly-flagged exception is the 617k-row Portal lexicon, scored on a fixed-seed sample and marked `sampled` in the JSON) — so the `o2i PER` column here matches the scoreboard's rows for the same language/dataset pair. Regenerate with:

```bash
pip install '.[compare]'  # epitran, gruut, pycotovia, ahotts-g2p — dev-only extra
PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard
```

Machine-readable form: [`benchmarks/comparison.json`](../benchmarks/comparison.json).

## Coverage

Not every gold language has a mapping for every competitor system: espeak-ng, epitran, gruut, pycotovia, and ahotts-g2p each cover a different, smaller subset of languages than orthography2ipa's 493 language codes. A missing mapping, or a system that isn't installed, is reported as `n/a` for that row rather than skipped or faked — this table never crashes and never silently drops a system, it just says when it has nothing to compare. `epitran`/`gruut`/`pycotovia`/`ahotts-g2p` are only installed via the dev-only `[compare]` extra; a committed run generated without them shows `n/a` in those columns for every row — that reflects the generating environment, not a claim those systems don't support the language.

### ahotts-g2p output space (fairness)

`ahotts-g2p` (Aholab / HiTZ AhoTTS G2P port; `eu`, `es`) emits its transcription in the StyleTTS2 single-character training convention, where the library's `MULTI` table folds affricates (`tʃ`→`C`, `ts`→`V`, `tʂ`→`P`), aspirates (`pʰ`→`H`, `kʰ`→`K`, `tʰ`→`T`) and **stress-marked vowels** (`ˈi`→`I` … `ˈu`→`U`) onto single ASCII letters — e.g. `kaixo`→`kajʃO`, `mundua`→`mundUa`, `etxea`→`eCEa`. Scoring that raw against IPA gold would charge a spurious error on every uppercase char, so the harness UNFOLDS it back to standard IPA (the inverse of `ahotts_g2p.phones.MULTI`, stress rendered as `ˈ` so the shared `normalize` strips it like every other system) BEFORE scoring: `kajʃO`→`kajʃˈo`, `mundUa`→`mundˈua`, `eCEa`→`etʃˈea`. All systems are thus compared in one IPA space. The two ahotts-g2p `version`s (`classic`/`modern`) produce near-identical output; the committed rows use `classic` (see the `ahotts_version` field in `benchmarks/comparison.json`). NOTE: the `eu` `hitz_basque_ipa` gold is authored by HiTZ/Aholab (UPV/EHU), the same lab behind AhoTTS, so ahotts-g2p's very low PER there is close to same-source; the independent `eu` `wikipron` (Wiktionary) row is the fairer external comparison point. The audio-only `pyahotts` package is NOT a comparison system here (no phoneme output); `ahotts-g2p` is the G2P port that supersedes it for this table.

The `N` column is the number of unique gold words for that language/dataset pair; each system's own scored count can be slightly lower (a word it failed to transcribe is excluded from its PER, not counted as an error) — see the `*_n` fields in `benchmarks/comparison.json` for the exact per-system count.

## Normalization

Every system is scored with the identical normalization and PER metric orthography2ipa's own scoreboard uses (`scripts/benchmark.py:normalize`/`levenshtein`): NFC-normalize, strip stress marks (the length mark is retained), strip narrow-transcription diacritics (broad comparison), drop whitespace (segmentation-free), then score Levenshtein distance against the best-matching gold variant. No system is normalized differently or given a more forgiving metric.

## Honesty

This table includes languages where orthography2ipa **loses** to espeak-ng. Cherry-picking would make the comparison worthless.

| Lang | Dataset | N | o2i PER | espeak PER | epitran PER | gruut PER | pycotovia PER | ahotts-g2p PER |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| ca | 4catac | 160 | 0.1054 | 0.0451 | 0.4673 | n/a | n/a | n/a |
| ca-x-balear | 4catac | 160 | 0.1927 | 0.0817 | 0.5025 | n/a | n/a | n/a |
| ca-x-occidental | 4catac | 160 | 0.1204 | 0.0588 | 0.4403 | n/a | n/a | n/a |
| ca-x-valencia | 4catac | 160 | 0.0946 | 0.0515 | 0.3820 | n/a | n/a | n/a |
| cy | wikipron | 14486 | 0.2153 | 0.2976 | 0.2228 | n/a | n/a | n/a |
| de | wikipron | 53011 | 0.3265 | 0.2381 | 0.3083 | n/a | n/a | n/a |
| el | wikipron | 19108 | 0.1318 | 0.0797 | n/a | n/a | n/a | n/a |
| en | wikipron | 78445 | 0.3739 | 0.2126 | 0.8333 | 0.1800 | n/a | n/a |
| es | wikipron | 131507 | 0.0845 | 0.1072 | 0.0277 | n/a | n/a | 0.1042 |
| eu | hitz_basque_ipa | 3113 | 0.2089 | 0.1588 | n/a | n/a | n/a | 0.0217 |
| eu-wikipron | wikipron | 12022 | 0.0391 | 0.1077 | n/a | n/a | n/a | 0.1713 |
| fi | wikipron | 168814 | 0.0552 | 0.2498 | 0.1327 | n/a | n/a | n/a |
| fr | wikipron | 85516 | 0.1773 | 0.0740 | 0.2280 | n/a | n/a | n/a |
| ga | wikipron | 9621 | 0.1821 | 0.5312 | n/a | n/a | n/a | n/a |
| gl | wikipron | 8091 | 0.0928 | n/a | n/a | n/a | 0.0898 | n/a |
| hi | wikipron | 30379 | 0.1563 | 0.2832 | 0.3323 | n/a | n/a | n/a |
| it | wikipron | 82280 | 0.1083 | 0.1002 | 0.1245 | n/a | n/a | n/a |
| nl | wikipron | 45872 | 0.2663 | 0.1265 | 0.2911 | n/a | n/a | n/a |
| pl | wikipron | 148992 | 0.1213 | 0.1132 | 0.0633 | n/a | n/a | n/a |
| pt-PT | portuguese_phonetic_lexicon | 3000 | 0.1403 | 0.3313 | 0.3792 | n/a | n/a | n/a |
| ro | wikipron | 8978 | 0.0348 | 0.0893 | 0.0378 | n/a | n/a | n/a |
| ru | wikipron | 403873 | 0.3073 | 0.3989 | 0.3212 | n/a | n/a | n/a |
| sv | wikipron | 5082 | 0.2747 | 0.2582 | 0.3862 | n/a | n/a | n/a |
| tr | wikipron | 11582 | 0.1236 | 0.2755 | 0.1358 | n/a | n/a | n/a |

**o2i beats espeak on 10 of 23 comparable languages.**

## Catalan dialects vs espeak (BSC)

The Barcelona Supercomputing Center (BSC) added Catalan dialect voices to espeak-ng (central, balearic, north-western, valencian). This table compares each o2i Catalan dialect spec against the matching espeak-ng dialect voice on the 4catac gold (expert human-annotated regional accents) — the same expert gold used for the `ca` row in the main table above.

All three BSC dialect voices (`ca-ba`, `ca-nw`, `ca-va`) were found on this machine's espeak-ng install; each dialect row below uses its own dialect-specific voice.

| Dialect | o2i spec | espeak voice | N | o2i PER | espeak PER |
|---|---|---|---:|---:|---:|
| central | ca | ca | 160 | 0.1054 | 0.0451 |
| balear | ca-x-balear | ca-ba | 160 | 0.1927 | 0.0817 |
| valencian | ca-x-valencia | ca-va | 160 | 0.0946 | 0.0515 |
| occidental (nord-occidental) | ca-x-occidental | ca-nw | 160 | 0.1204 | 0.0588 |
