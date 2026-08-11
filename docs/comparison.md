# Comparison to other G2P systems

Committed cross-system comparison: orthography2ipa vs **espeak-ng**, **epitran**, **gruut**, **pycotovia** (Galician), and **ahotts-g2p** (Basque & Spanish) on the same gold datasets/loaders as [`docs/scoreboard.md`](scoreboard.md), using the FULL gold set of every mapped language (no cap — the same no-caps policy as the scoreboard; the one explicitly-flagged exception is `pt-PT`, whose 598k-row `portuguese_unified` ('Portal lexicon') made a per-word-external-system full pass impractical, so its config sets a `sample_n` — and because `sample_n` is a per-LANGUAGE cap, not a per-dataset one, it now applies to every dataset registered for `pt-PT`, not just `portuguese_unified`; all of them are marked `sampled` in the JSON). The `o2i PER` column here matches [`benchmarks/results.json`](../benchmarks/results.json)'s `per` for most shared language/dataset pairs, EXCEPT the 20 listed below — those `benchmarks/results.json` rows are stale (a prior PR changed the engine but did not regenerate every affected row there; see e.g. PR #802's `ca`/`4catac`-only regeneration). The numbers in THIS table reflect the current engine via a live run; `benchmarks/results.json` needs a matching regeneration for: `ca`/`4catac` (here 0.0986, results.json 0.0798); `ca-x-balear`/`4catac` (here 0.1997, results.json 0.1792); `ca-x-occidental`/`4catac` (here 0.1026, results.json 0.0960); `ca-x-valencia`/`4catac` (here 0.0851, results.json 0.0783); `cop`/`wikipron` (here 0.3671, results.json 0.3716); `cy`/`wikipron` (here 0.1822, results.json 0.2134); `en`/`wikipron` (here 0.3585, results.json 0.3215); `en-US`/`cmudict` (here 0.5003, results.json 0.4656); `en-US`/`ipa_babylm` (here 0.4766, results.json 0.4510); `en-US`/`ipa_childes` (here 0.3805, results.json 0.3507); `en-US`/`ipadict` (here 0.5332, results.json 0.4962); `fr`/`wikipron` (here 0.1189, results.json 0.0882); `kab`/`vox_communis` (here 0.2071, results.json 0.2304); `mfe`/`wikipron` (here 0.1238, results.json 0.2665); `nl`/`ipadict` (here 0.1616, results.json 0.1767); `nup`/`wikipron` (here 0.3979, results.json 0.4932); `pl`/`ipa_childes` (here 0.2465, results.json 0.2715); `pt-PT`/`ipa_childes` (here 0.2498, results.json 0.2477); `pt-PT`/`wikipron` (here 0.1346, results.json 0.0903); `ro`/`vox_communis` (here 0.3282, results.json 0.3411). Regenerate with:

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

**Every gold dataset a language has, not one.** Earlier versions of this table picked a single 'battleground' gold per language. Multiple rows per language are now committed — one per registered gold dataset for that language — so a system winning on one gold and losing on another for the SAME language is visible here, not hidden by picking the flattering row.

**`same-source` cells**: a cell reads `same-source` (never `n/a`) when the gold dataset IS that system's own output — e.g. scoring `espeak` against `ipa_babylm` (espeak-derived) or `ahotts-g2p` against `hitz_basque_ipa` (HiTZ's own ahoNT phonemizer output, same lab as AhoTTS). Scoring a system against its own generator is tautological — it would score near-zero by construction, not because it is accurate — so that comparison is refused rather than reported. The same rule applies to **o2i itself**: `arabic_tts`, `portuguese_tts` and `gold20_arabic` were drafted by the same Claude lineage that authored orthography2ipa's own Arabic/Portuguese dialect specs (near-circular per the datasets' provenance notes in `scripts/benchmark.py`) — a spec author's own generated gold measures self-agreement with the spec, not correctness, so the `o2i PER` cell on those rows also reads `same-source`.

**Machine-generated-reference rows are agreement, not accuracy.** Rows whose gold is itself another phonemizer's or an LLM's output (see each dataset's `provenance_tier` in `benchmarks/comparison.json`, and `docs/scoreboard.md`'s provenance legend) measure how much a system agrees with the tool that generated the gold — not whether either is correct. A win on such a row is not a claim of accuracy.

| Lang | Dataset | N | o2i PER | espeak PER | epitran PER | gruut PER | pycotovia PER | ahotts-g2p PER | africa-g2p PER |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| arb | arabic_tts | 20 | same-source | n/a | n/a | n/a | n/a | n/a | 0.2836 |
| arb | gold20_arabic | 20 | same-source | n/a | n/a | n/a | n/a | n/a | 0.2666 |
| ca | 4catac | 160 | 0.0986 | 0.0403 | 0.4641 | n/a | n/a | n/a | n/a |
| ca | ipa_childes | 3814 | 0.2595 | same-source | 0.3447 | n/a | n/a | n/a | n/a |
| ca | vox_communis | 218451 | 0.8088 | 0.8195 | same-source | n/a | n/a | n/a | n/a |
| ca | wikipron | 106 | 0.2596 | 0.2221 | 0.3518 | n/a | n/a | n/a | n/a |
| ca-x-balear | 4catac | 160 | 0.1997 | 0.0797 | 0.4998 | n/a | n/a | n/a | n/a |
| ca-x-occidental | 4catac | 160 | 0.1026 | 0.0497 | 0.4348 | n/a | n/a | n/a | n/a |
| ca-x-valencia | 4catac | 160 | 0.0851 | 0.0439 | 0.3775 | n/a | n/a | n/a | n/a |
| cop | wikipron | 591 | 0.3671 | n/a | n/a | n/a | n/a | n/a | 0.4491 |
| cy | ipa_childes | 4666 | 0.2985 | same-source | 0.3495 | n/a | n/a | n/a | n/a |
| cy | vox_communis | 18701 | 0.1172 | 0.3005 | same-source | n/a | n/a | n/a | n/a |
| cy | wikipron | 14811 | 0.1822 | 0.2799 | 0.2170 | n/a | n/a | n/a | n/a |
| de | wikipron | 53011 | 0.2103 | 0.2126 | 0.3064 | n/a | n/a | n/a | n/a |
| el | vox_communis | 5994 | 0.2672 | 0.3347 | same-source | n/a | n/a | n/a | n/a |
| el | wikipron | 19108 | 0.0330 | 0.0785 | n/a | n/a | n/a | n/a | n/a |
| en | wikipron | 80995 | 0.3585 | 0.2081 | 0.8333 | 0.1776 | n/a | n/a | n/a |
| en-US | cmudict | 126052 | 0.5003 | 0.3048 | n/a | 0.1531 | n/a | n/a | n/a |
| en-US | ipa_babylm | 20344 | 0.4766 | same-source | 1.0656 | 0.2788 | n/a | n/a | n/a |
| en-US | ipa_childes | 18055 | 0.3805 | same-source | n/a | 0.1727 | n/a | n/a | n/a |
| en-US | ipadict | 125927 | 0.5332 | 0.2954 | n/a | 0.1132 | n/a | n/a | n/a |
| es | vox_communis | 97715 | 1.2133 | 1.2330 | same-source | n/a | n/a | 1.2117 | n/a |
| es | wikipron | 132190 | 0.0879 | 0.1071 | 0.0277 | n/a | n/a | 0.1041 | n/a |
| eu | hitz_basque_ipa | 3113 | 0.0984 | 0.1204 | n/a | n/a | n/a | same-source | n/a |
| eu | ipa_childes | 3969 | 0.0821 | same-source | n/a | n/a | n/a | 0.1396 | n/a |
| eu | vox_communis | 64077 | 0.0644 | 0.1194 | same-source | n/a | n/a | 0.1280 | n/a |
| eu | wikipron | 12022 | 0.0546 | 0.1019 | n/a | n/a | n/a | 0.1507 | n/a |
| eu-wikipron | hitz_basque_ipa | 3113 | 0.0984 | 0.1204 | n/a | n/a | n/a | same-source | n/a |
| eu-wikipron | ipa_childes | 3969 | 0.0821 | same-source | n/a | n/a | n/a | 0.1396 | n/a |
| eu-wikipron | vox_communis | 64077 | 0.0644 | 0.1194 | same-source | n/a | n/a | 0.1280 | n/a |
| eu-wikipron | wikipron | 12022 | 0.0546 | 0.1019 | n/a | n/a | n/a | 0.1507 | n/a |
| fi | ipadict | 92836 | 0.0609 | 0.1995 | 0.1111 | n/a | n/a | n/a | n/a |
| fi | vox_communis | 13324 | 0.0037 | 0.1843 | same-source | n/a | n/a | n/a | n/a |
| fi | wikipron | 168814 | 0.0184 | 0.2062 | 0.0963 | n/a | n/a | n/a | n/a |
| fr | wikipron | 85516 | 0.1189 | 0.0740 | 0.2280 | n/a | n/a | n/a | n/a |
| ga | ipa_childes | 1612 | 0.2989 | same-source | n/a | n/a | n/a | n/a | n/a |
| ga | wikipron | 9621 | 0.1834 | 0.5223 | n/a | n/a | n/a | n/a | n/a |
| gl | vox_communis | 47515 | 0.0771 | n/a | same-source | n/a | 0.0883 | n/a | n/a |
| gl | wikipron | 8091 | 0.0906 | n/a | n/a | n/a | 0.0883 | n/a | n/a |
| hi | vox_communis | 13154 | 0.3684 | 0.5184 | same-source | n/a | n/a | n/a | n/a |
| hi | wikipron | 30379 | 0.1562 | 0.2815 | 0.3322 | n/a | n/a | n/a | n/a |
| hts | wikipron | 329 | 0.3728 | n/a | n/a | n/a | n/a | n/a | 0.2769 |
| it | vox_communis | 90366 | 1.1402 | 1.1830 | same-source | n/a | n/a | n/a | n/a |
| it | wikipron | 82280 | 0.0588 | 0.0722 | 0.0852 | n/a | n/a | n/a | n/a |
| kab | vox_communis | 54546 | 0.2071 | n/a | same-source | n/a | n/a | n/a | 0.4339 |
| ktz | wikipron | 134 | 0.3464 | n/a | n/a | n/a | n/a | n/a | 0.3806 |
| lad | wikipron | 131 | 0.1397 | n/a | n/a | n/a | n/a | n/a | 0.6256 |
| mfe | wikipron | 206 | 0.1238 | n/a | n/a | n/a | n/a | n/a | 0.3001 |
| ngh | wikipron | 263 | 0.3655 | n/a | n/a | n/a | n/a | n/a | 0.3958 |
| nl | ipa_childes | 8108 | 0.2137 | same-source | 0.4454 | n/a | n/a | n/a | n/a |
| nl | ipadict | 117869 | 0.1616 | 0.1607 | 0.2948 | n/a | n/a | n/a | n/a |
| nl | vox_communis | 26137 | 0.2925 | 0.3054 | same-source | n/a | n/a | n/a | n/a |
| nl | wikipron | 45872 | 0.0902 | 0.1099 | 0.2843 | n/a | n/a | n/a | n/a |
| nup | wikipron | 393 | 0.3979 | n/a | n/a | n/a | n/a | n/a | 0.4582 |
| pl | ipa_childes | 15524 | 0.2465 | same-source | 0.2453 | n/a | n/a | n/a | n/a |
| pl | vox_communis | 47615 | 0.0194 | 0.0793 | same-source | n/a | n/a | n/a | n/a |
| pl | wikipron | 148992 | 0.0480 | 0.1132 | 0.0633 | n/a | n/a | n/a | n/a |
| pt-PT | ep_dialects | 30 | 0.1185 | 0.3192 | 0.4095 | n/a | n/a | n/a | n/a |
| pt-PT | ipa_childes | 3000 | 0.2498 | same-source | 0.4027 | n/a | n/a | n/a | n/a |
| pt-PT | portuguese_tts | 20 | same-source | 0.3336 | 0.4042 | n/a | n/a | n/a | n/a |
| pt-PT | portuguese_unified | 3000 | 0.2250 | 0.3669 | 0.4146 | n/a | n/a | n/a | n/a |
| pt-PT | wikipron | 2272 | 0.1346 | 0.2374 | 0.2903 | n/a | n/a | n/a | n/a |
| ro | vox_communis | 12097 | 0.3282 | 0.4480 | same-source | n/a | n/a | n/a | n/a |
| ro | wikipron | 8978 | 0.0342 | 0.0825 | 0.0302 | n/a | n/a | n/a | n/a |
| ru | primary_sources | 36 | 0.1867 | 0.3119 | 0.0744 | n/a | n/a | n/a | n/a |
| ru | vox_communis | 50547 | 0.3447 | 0.3594 | same-source | n/a | n/a | n/a | n/a |
| ru | wikipron | 403873 | 0.1451 | 0.3953 | 0.3202 | n/a | n/a | n/a | n/a |
| sv | ipa_childes | 5202 | 0.3449 | same-source | 0.3576 | n/a | n/a | n/a | n/a |
| sv | ipadict | 21095 | 0.2583 | 0.2611 | 0.4163 | n/a | n/a | n/a | n/a |
| sv | vox_communis | 19516 | 0.3428 | 0.3214 | same-source | n/a | n/a | n/a | n/a |
| sv | wikipron | 5082 | 0.2317 | 0.2337 | 0.3692 | n/a | n/a | n/a | n/a |
| tr | ipa_childes | 2748 | 0.1372 | same-source | 0.1194 | n/a | n/a | n/a | n/a |
| tr | vox_communis | 49476 | 0.1614 | 0.3443 | same-source | n/a | n/a | n/a | n/a |
| tr | wikipron | 11582 | 0.1230 | 0.2739 | 0.1352 | n/a | n/a | n/a | n/a |
| tzm | wikipron | 658 | 0.0160 | n/a | n/a | n/a | n/a | n/a | 1.0005 |

Counted over distinct LANGUAGES (one row per language: its configured primary gold dataset — see `_primary_rows`), never over table rows, and split by whether that primary gold is an independent reference or another tool's/LLM's output:

- **Gold-tier** (expert-human / lexicon-derived / crowd-scraped primary gold): o2i beats espeak on 16 of 23 comparable languages.
- **Agreement-tier** (machine-generated / espeak-derived / epitran-derived / llm-generated primary gold — measures agreement with the generating tool, not accuracy; see "Honesty" above): o2i beats espeak on 1 of 1 comparable languages.

## Robustness across golds

A system winning on one gold and losing on another for the SAME language is real signal, not noise to average away. Every language with 2+ espeak-comparable gold datasets is listed below with its exact win/loss split (same-source cells excluded — they are never comparable, see above).

- **`ca`** (MIXED — wins on some golds, loses on others):
  - `4catac` (n=160, tier=expert-human): o2i 0.0986 vs espeak 0.0403 — o2i loses
  - `vox_communis` (n=218451, tier=epitran-derived): o2i 0.8088 vs espeak 0.8195 — o2i wins
  - `wikipron` (n=106, tier=crowd-scraped): o2i 0.2596 vs espeak 0.2221 — o2i loses
- **`cy`** (wins on all golds):
  - `vox_communis` (n=18701, tier=epitran-derived): o2i 0.1172 vs espeak 0.3005 — o2i wins
  - `wikipron` (n=14811, tier=crowd-scraped): o2i 0.1822 vs espeak 0.2799 — o2i wins
- **`el`** (wins on all golds):
  - `vox_communis` (n=5994, tier=epitran-derived): o2i 0.2672 vs espeak 0.3347 — o2i wins
  - `wikipron` (n=19108, tier=crowd-scraped): o2i 0.0330 vs espeak 0.0785 — o2i wins
- **`en-US`** (loses on all golds):
  - `cmudict` (n=126052, tier=lexicon-derived): o2i 0.5003 vs espeak 0.3048 — o2i loses
  - `ipadict` (n=125927, tier=lexicon-derived): o2i 0.5332 vs espeak 0.2954 — o2i loses
- **`es`** (wins on all golds):
  - `vox_communis` (n=97715, tier=epitran-derived): o2i 1.2133 vs espeak 1.2330 — o2i wins
  - `wikipron` (n=132190, tier=crowd-scraped): o2i 0.0879 vs espeak 0.1071 — o2i wins
- **`eu`** (wins on all golds):
  - `hitz_basque_ipa` (n=3113, tier=machine-generated): o2i 0.0984 vs espeak 0.1204 — o2i wins
  - `vox_communis` (n=64077, tier=epitran-derived): o2i 0.0644 vs espeak 0.1194 — o2i wins
  - `wikipron` (n=12022, tier=crowd-scraped): o2i 0.0546 vs espeak 0.1019 — o2i wins
- **`eu-wikipron`** (wins on all golds):
  - `hitz_basque_ipa` (n=3113, tier=machine-generated): o2i 0.0984 vs espeak 0.1204 — o2i wins
  - `vox_communis` (n=64077, tier=epitran-derived): o2i 0.0644 vs espeak 0.1194 — o2i wins
  - `wikipron` (n=12022, tier=crowd-scraped): o2i 0.0546 vs espeak 0.1019 — o2i wins
- **`fi`** (wins on all golds):
  - `ipadict` (n=92836, tier=machine-generated): o2i 0.0609 vs espeak 0.1995 — o2i wins
  - `vox_communis` (n=13324, tier=epitran-derived): o2i 0.0037 vs espeak 0.1843 — o2i wins
  - `wikipron` (n=168814, tier=crowd-scraped): o2i 0.0184 vs espeak 0.2062 — o2i wins
- **`hi`** (wins on all golds):
  - `vox_communis` (n=13154, tier=epitran-derived): o2i 0.3684 vs espeak 0.5184 — o2i wins
  - `wikipron` (n=30379, tier=crowd-scraped): o2i 0.1562 vs espeak 0.2815 — o2i wins
- **`it`** (wins on all golds):
  - `vox_communis` (n=90366, tier=epitran-derived): o2i 1.1402 vs espeak 1.1830 — o2i wins
  - `wikipron` (n=82280, tier=crowd-scraped): o2i 0.0588 vs espeak 0.0722 — o2i wins
- **`nl`** (MIXED — wins on some golds, loses on others):
  - `ipadict` (n=117869, tier=machine-generated): o2i 0.1616 vs espeak 0.1607 — o2i loses
  - `vox_communis` (n=26137, tier=epitran-derived): o2i 0.2925 vs espeak 0.3054 — o2i wins
  - `wikipron` (n=45872, tier=crowd-scraped): o2i 0.0902 vs espeak 0.1099 — o2i wins
- **`pl`** (wins on all golds):
  - `vox_communis` (n=47615, tier=epitran-derived): o2i 0.0194 vs espeak 0.0793 — o2i wins
  - `wikipron` (n=148992, tier=crowd-scraped): o2i 0.0480 vs espeak 0.1132 — o2i wins
- **`pt-PT`** (wins on all golds):
  - `ep_dialects` (n=30, tier=expert-human): o2i 0.1185 vs espeak 0.3192 — o2i wins
  - `portuguese_unified` (n=3000, tier=lexicon-derived): o2i 0.2250 vs espeak 0.3669 — o2i wins
  - `wikipron` (n=2272, tier=crowd-scraped): o2i 0.1346 vs espeak 0.2374 — o2i wins
- **`ro`** (wins on all golds):
  - `vox_communis` (n=12097, tier=epitran-derived): o2i 0.3282 vs espeak 0.4480 — o2i wins
  - `wikipron` (n=8978, tier=crowd-scraped): o2i 0.0342 vs espeak 0.0825 — o2i wins
- **`ru`** (wins on all golds):
  - `primary_sources` (n=36, tier=expert-human): o2i 0.1867 vs espeak 0.3119 — o2i wins
  - `vox_communis` (n=50547, tier=epitran-derived): o2i 0.3447 vs espeak 0.3594 — o2i wins
  - `wikipron` (n=403873, tier=crowd-scraped): o2i 0.1451 vs espeak 0.3953 — o2i wins
- **`sv`** (MIXED — wins on some golds, loses on others):
  - `ipadict` (n=21095, tier=lexicon-derived): o2i 0.2583 vs espeak 0.2611 — o2i wins
  - `vox_communis` (n=19516, tier=epitran-derived): o2i 0.3428 vs espeak 0.3214 — o2i loses
  - `wikipron` (n=5082, tier=crowd-scraped): o2i 0.2317 vs espeak 0.2337 — o2i wins
- **`tr`** (wins on all golds):
  - `vox_communis` (n=49476, tier=epitran-derived): o2i 0.1614 vs espeak 0.3443 — o2i wins
  - `wikipron` (n=11582, tier=crowd-scraped): o2i 0.1230 vs espeak 0.2739 — o2i wins

## Fair-comparison 2x2 (dictionary vs. rules)

The table above conflates espeak-ng's letter-to-sound RULES with its hand-curated word-EXCEPTION list (o2i, by hard rule, ships no such list). This 2x2 isolates the dictionary's contribution on the same gold rows, for the languages where both extra columns are wired up (the `DICTSOURCE_LANG`-mapped subset — see the script's module docstring for how to enable `espeak_rules` via `scripts/build_espeak_rules_only.sh` and `o2i_lex` via `$ESPEAK_DICTSOURCE_PATH`):

- `o2i` — orthography2ipa, rules only (unchanged from the main table).
- `o2i_lex` — orthography2ipa + a runtime lexicon built from espeak-ng's OWN word-exception list, each word's IPA obtained from espeak-ng itself (o2i rules + espeak's dictionary).
- `espeak` — espeak-ng, rules + its own word-exception dictionary (unchanged from the main table).
- `espeak_rules` — espeak-ng with the word-exception dictionary emptied before compiling (rules only).

| Lang | Dataset | N | o2i | o2i_lex | espeak | espeak_rules |
|---|---|---:|---:|---:|---:|---:|
| _(none)_ | | | | | | |

Reading the four numbers together: `espeak - espeak_rules` is espeak-ng's dictionary contribution; `o2i_lex - o2i` is what the SAME dictionary is worth bolted onto o2i's rules. `o2i` vs `espeak_rules` is the fairest rules-only comparison; `o2i_lex` vs `espeak` is the fairest dictionary-included comparison.

**Licensing**: espeak-ng's dictsource word lists and the IPA derived from them are GPL. They are used here ONLY at comparison runtime — fetched/built into a local scratch cache (`$ESPEAK_RULES_DATA_PATH`, `.o2i_lex_cache/`), never committed to this repository and never shipped in orthography2ipa's own package or lexicons.

## Catalan dialects vs espeak (BSC)

The Barcelona Supercomputing Center (BSC) added Catalan dialect voices to espeak-ng (central, balearic, north-western, valencian). This table compares each o2i Catalan dialect spec against the matching espeak-ng dialect voice on the 4catac gold (expert human-annotated regional accents) — the same expert gold used for the `ca` row in the main table above.

All three BSC dialect voices (`ca-ba`, `ca-nw`, `ca-va`) were found on this machine's espeak-ng install; each dialect row below uses its own dialect-specific voice.

| Dialect | o2i spec | espeak voice | N | o2i PER | espeak PER |
|---|---|---|---:|---:|---:|
| central | ca | ca | 106 | 0.2596 | 0.2221 |
| balear | ca-x-balear | ca-ba | 160 | 0.1997 | 0.0797 |
| valencian | ca-x-valencia | ca-va | 160 | 0.0851 | 0.0439 |
| occidental (nord-occidental) | ca-x-occidental | ca-nw | 160 | 0.1026 | 0.0497 |
