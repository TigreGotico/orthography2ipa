# Comparison to other G2P systems

Committed cross-system comparison: orthography2ipa vs **espeak-ng**, **epitran**, **gruut**, **pycotovia** (Galician), and **ahotts-g2p** (Basque & Spanish) on the same gold datasets/loaders as [`docs/scoreboard.md`](scoreboard.md), using the FULL gold set of every mapped language (no cap — the same no-caps policy as the scoreboard; the one explicitly-flagged exception is the 617k-row Portal lexicon, scored on a fixed-seed sample and marked `sampled` in the JSON) — so the `o2i PER` column here matches the scoreboard's rows for the same language/dataset pair. Regenerate with:

```bash
pip install '.[compare]'  # epitran, gruut, pycotovia, ahotts-g2p — dev-only extra
PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard
```

Machine-readable form: [`benchmarks/comparison.json`](../benchmarks/comparison.json).

## Coverage

Not every gold language has a mapping for every competitor system: espeak-ng, epitran, gruut, pycotovia, ahotts-g2p, and africa-g2p each cover a different, smaller subset of languages than orthography2ipa's 493 language codes. A missing mapping, or a system that isn't installed, is reported as `n/a` for that row rather than skipped or faked — this table never crashes and never silently drops a system, it just says when it has nothing to compare. `epitran`/`gruut`/`pycotovia`/`ahotts-g2p` are only installed via the dev-only `[compare]` extra; a committed run generated without them shows `n/a` in those columns for every row — that reflects the generating environment, not a claim those systems don't support the language.

### ahotts-g2p output space (fairness)

`ahotts-g2p` (Aholab / HiTZ AhoTTS G2P port; `eu`, `es`) emits its transcription in the StyleTTS2 single-character training convention, where the library's `MULTI` table folds affricates (`tʃ`→`C`, `ts`→`V`, `tʂ`→`P`), aspirates (`pʰ`→`H`, `kʰ`→`K`, `tʰ`→`T`) and **stress-marked vowels** (`ˈi`→`I` … `ˈu`→`U`) onto single ASCII letters — e.g. `kaixo`→`kajʃO`, `mundua`→`mundUa`, `etxea`→`eCEa`. Scoring that raw against IPA gold would charge a spurious error on every uppercase char, so the harness UNFOLDS it back to standard IPA (the inverse of `ahotts_g2p.phones.MULTI`, stress rendered as `ˈ` so the shared `normalize` strips it like every other system) BEFORE scoring: `kajʃO`→`kajʃˈo`, `mundUa`→`mundˈua`, `eCEa`→`etʃˈea`. All systems are thus compared in one IPA space. The two ahotts-g2p `version`s (`classic`/`modern`) produce near-identical output; the committed rows use `classic` (see the `ahotts_version` field in `benchmarks/comparison.json`). NOTE: the `eu` `hitz_basque_ipa` gold is authored by HiTZ/Aholab (UPV/EHU), the same lab behind AhoTTS, so ahotts-g2p's very low PER there is close to same-source; the independent `eu` `wikipron` (Wiktionary) row is the fairer external comparison point. The audio-only `pyahotts` package is NOT a comparison system here (no phoneme output); `ahotts-g2p` is the G2P port that supersedes it for this table.

### africa-g2p coverage (honest limits)

`africa-g2p` (Ghana NLP; rule-based G2P for ~400 African-language ISO 639-3 codes, derived from Hartell's *Alphabets of Africa*, UNESCO 1993) is not on PyPI, so it is not part of the `[compare]` extra — install it from a locally built wheel of the upstream checkout before regenerating this table (see the script's module docstring). Rows only appear for gold languages BOTH orthography2ipa and africa-g2p's own `registry()` cover; as of this run that intersection is small (10 languages: `arb`, `cop`, `hts`, `kab`, `ktz`, `lad`, `mfe`, `ngh`, `nup`, `tzm`) — most of africa-g2p's ~400 codes have no o2i gold registered yet, and most o2i gold languages are outside africa-g2p's coverage. None of these ten has a matching espeak-ng voice, epitran code, or gruut language on this machine either, so africa-g2p is currently the only comparison point for these rows — that is reported plainly rather than papered over with `n/a` silence.

The `N` column is the number of unique gold words for that language/dataset pair; each system's own scored count can be slightly lower (a word it failed to transcribe is excluded from its PER, not counted as an error) — see the `*_n` fields in `benchmarks/comparison.json` for the exact per-system count.

## Normalization

Every system is scored with the identical normalization and PER metric orthography2ipa's own scoreboard uses (`scripts/benchmark.py:normalize`/`levenshtein`): NFC-normalize, strip stress marks (the length mark is retained), strip narrow-transcription diacritics (broad comparison), drop whitespace (segmentation-free), then score Levenshtein distance against the best-matching gold variant. No system is normalized differently or given a more forgiving metric.

## Honesty

This table includes languages where orthography2ipa **loses** to espeak-ng. Cherry-picking would make the comparison worthless.

| Lang | Dataset | N | o2i PER | espeak PER | epitran PER | gruut PER | pycotovia PER | ahotts-g2p PER | africa-g2p PER |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| arb | arabic_tts | 20 | 0.0000 | n/a | n/a | n/a | n/a | n/a | 0.2680 |
| ca | 4catac | 160 | 0.1069 | 0.0451 | 0.4664 | n/a | n/a | n/a | n/a |
| ca-x-balear | 4catac | 160 | 0.2033 | 0.0817 | 0.5017 | n/a | n/a | n/a | n/a |
| ca-x-occidental | 4catac | 160 | 0.1150 | 0.0588 | 0.4394 | n/a | n/a | n/a | n/a |
| ca-x-valencia | 4catac | 160 | 0.0944 | 0.0515 | 0.3815 | n/a | n/a | n/a | n/a |
| cop | wikipron | 591 | 0.3716 | n/a | n/a | n/a | n/a | n/a | 0.4430 |
| cy | wikipron | 14811 | 0.2148 | 0.3119 | 0.2259 | n/a | n/a | n/a | n/a |
| de | wikipron | 53011 | 0.3265 | 0.2381 | 0.3083 | n/a | n/a | n/a | n/a |
| el | wikipron | 19108 | 0.0343 | 0.0797 | n/a | n/a | n/a | n/a | n/a |
| en | wikipron | 80995 | 0.3592 | 0.2092 | 0.8333 | 0.1788 | n/a | n/a | n/a |
| en-US | cmudict | 126052 | 0.5003 | 0.3048 | n/a | 0.1531 | n/a | n/a | n/a |
| es | wikipron | 132190 | 0.0879 | 0.1071 | 0.0277 | n/a | n/a | 0.1041 | n/a |
| eu | hitz_basque_ipa | 3113 | 0.1848 | 0.1588 | n/a | n/a | n/a | 0.0217 | n/a |
| eu-wikipron | wikipron | 12022 | 0.0100 | 0.1077 | n/a | n/a | n/a | 0.1713 | n/a |
| fi | wikipron | 168814 | 0.0539 | 0.2354 | 0.1324 | n/a | n/a | n/a | n/a |
| fr | wikipron | 85516 | 0.1643 | 0.0740 | 0.2280 | n/a | n/a | n/a | n/a |
| ga | wikipron | 9621 | 0.1837 | 0.5312 | n/a | n/a | n/a | n/a | n/a |
| gl | wikipron | 8091 | 0.0911 | n/a | n/a | n/a | 0.0898 | n/a | n/a |
| hi | wikipron | 30379 | 0.1563 | 0.2816 | 0.3323 | n/a | n/a | n/a | n/a |
| hts | wikipron | 329 | 0.3728 | n/a | n/a | n/a | n/a | n/a | 0.2769 |
| it | wikipron | 82280 | 0.0588 | 0.0722 | 0.0852 | n/a | n/a | n/a | n/a |
| kab | vox_communis | 54546 | 0.2106 | n/a | n/a | n/a | n/a | n/a | 0.4373 |
| ktz | wikipron | 134 | 0.3451 | n/a | n/a | n/a | n/a | n/a | 0.3800 |
| lad | wikipron | 131 | 0.1397 | n/a | n/a | n/a | n/a | n/a | 0.6256 |
| mfe | wikipron | 206 | 0.2665 | n/a | n/a | n/a | n/a | n/a | 0.3001 |
| ngh | wikipron | 263 | 0.3663 | n/a | n/a | n/a | n/a | n/a | 0.3961 |
| nl | wikipron | 45872 | 0.2663 | 0.1265 | 0.2911 | n/a | n/a | n/a | n/a |
| nup | wikipron | 393 | 0.4932 | n/a | n/a | n/a | n/a | n/a | 0.4582 |
| pl | wikipron | 148992 | 0.0480 | 0.1132 | 0.0633 | n/a | n/a | n/a | n/a |
| pt-PT | portuguese_unified | 3000 | 0.2250 | 0.3669 | 0.4146 | n/a | n/a | n/a | n/a |
| ro | wikipron | 8978 | 0.0356 | 0.0893 | 0.0378 | n/a | n/a | n/a | n/a |
| ru | wikipron | 403873 | 0.1451 | 0.3953 | 0.3202 | n/a | n/a | n/a | n/a |
| sv | wikipron | 5082 | 0.2727 | 0.2580 | 0.3864 | n/a | n/a | n/a | n/a |
| tr | wikipron | 11582 | 0.1232 | 0.2740 | 0.1354 | n/a | n/a | n/a | n/a |
| tzm | wikipron | 658 | 0.0160 | n/a | n/a | n/a | n/a | n/a | 1.0005 |

**o2i beats espeak on 13 of 24 comparable languages.**

## Catalan dialects vs espeak (BSC)

The Barcelona Supercomputing Center (BSC) added Catalan dialect voices to espeak-ng (central, balearic, north-western, valencian). This table compares each o2i Catalan dialect spec against the matching espeak-ng dialect voice on the 4catac gold (expert human-annotated regional accents) — the same expert gold used for the `ca` row in the main table above.

All three BSC dialect voices (`ca-ba`, `ca-nw`, `ca-va`) were found on this machine's espeak-ng install; each dialect row below uses its own dialect-specific voice.

| Dialect | o2i spec | espeak voice | N | o2i PER | espeak PER |
|---|---|---|---:|---:|---:|
| central | ca | ca | 160 | 0.1069 | 0.0451 |
| balear | ca-x-balear | ca-ba | 160 | 0.2033 | 0.0817 |
| valencian | ca-x-valencia | ca-va | 160 | 0.0944 | 0.0515 |
| occidental (nord-occidental) | ca-x-occidental | ca-nw | 160 | 0.1150 | 0.0588 |
