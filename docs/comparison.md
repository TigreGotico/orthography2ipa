# Comparison to other G2P systems

This table shows how well orthography2ipa (o2i) predicts IPA pronunciation compared to seven other G2P systems, on the same gold word lists, language by language.

Every number is a **PER (Phoneme Error Rate)**: lower is better, `0.0000` is a perfect match, and it CAN exceed `1.0` when a system's output is much longer or shorter than the gold (more edits than the gold has phonemes).

## Leaderboard

One line per language: the best system on its primary gold, and where o2i lands.

- **same-source** — the gold IS that system's own output; excluded from ranking, never a "winner".
- **n/a** — the system has no mapping, or isn't installed, for this language.
- **tie** — two or more systems within 0.001 PER of the best; named, never a bare "tie".
- **rules-only** — the system with its bundled dictionary/lexicon disabled, scored on rules alone (see "How to read this" below).
- **#N** — N-th place by PER on that row; `#1` is the winner.

- **arb (Classical Arabic)** — o2i not scored: this gold was drafted by o2i's own lineage — see same-source (africa-g2p #1 among the rest)
- **ca (Catalan)** — espeak #1, o2i #2, o2i #1 on rules-only
- **ca-x-balear (Balearic Catalan)** — espeak #1, o2i #3
- **ca-x-occidental (North-Western Catalan)** — espeak #1, o2i #3
- **ca-x-valencia (Valencian)** — espeak #1, o2i #2, tied #1 on rules-only
- **cop (Coptic (Sahidic))** — o2i #1 (beats africa-g2p)
- **cy (Welsh)** — o2i #1 (beats epitran)
- **de (German)** — o2i #1 (beats espeak)
- **el (Modern Greek)** — o2i #1 (beats espeak rules-only)
- **en (English)** — gruut #1, o2i #5
- **en-GB (British English (RP))** — espeak #1, o2i #5
- **en-US (American English (General American))** — gruut rules-only #1, o2i #4
- **es (Spanish)** — epitran #1, o2i #2
- **eu (Basque (Euskara))** — o2i #1 (beats espeak)
- **eu-wikipron (Basque (Euskara), wikipron-primary variant)** — o2i #1 (beats espeak rules-only)
- **fi (Finnish)** — o2i #1 (beats epitran)
- **fr (French)** — o2i #1 (beats espeak)
- **ga (Irish)** — o2i #1 (beats espeak rules-only)
- **gl (Galician)** — o2i #1 (beats pycotovia)
- **hi (Hindi)** — o2i #1 (beats espeak)
- **hts (Hadza)** — o2i #1 (beats africa-g2p)
- **it (Italian)** — o2i #1 (beats espeak)
- **kab (Kabyle)** — o2i #1 (beats africa-g2p)
- **ktz (Juǀʼhoan)** — o2i #1 (beats africa-g2p)
- **lad (Ladino (Judeo-Spanish))** — o2i #1 (beats africa-g2p)
- **mfe (Morisyen)** — o2i #1 (beats africa-g2p)
- **ngh (Nǁng)** — o2i #1 (beats africa-g2p)
- **nl (Dutch)** — o2i #1 (beats espeak)
- **nup (Nupe)** — o2i #1 (beats africa-g2p)
- **pl (Polish)** — o2i #1 (beats epitran)
- **pt-PT (European Portuguese)** — o2i #1 (beats espeak rules-only)
- **ro (Romanian)** — epitran #1, o2i #2
- **ru (Russian)** — o2i #1 (beats epitran)
- **sv (Swedish)** — o2i #1 (beats espeak)
- **tr (Turkish)** — o2i #1 (beats epitran)
- **tzm (Central Atlas Tamazight)** — o2i #1 (beats africa-g2p)

## Results by language

### arb (Classical Arabic)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| arabic_tts | 20 | same-source | 0.2836 | africa-g2p |
| gold20_arabic | 20 | same-source | 0.2666 | africa-g2p |

### ca (Catalan)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| 4catac | 160 | 0.0643 | 0.0403 | 0.1206 | 0.4641 | espeak |
| ipa_childes | 3814 | 0.2579 | same-source | same-source | 0.3447 | o2i |
| vox_communis | 218451 | 0.8055 | 0.8195 | 0.8168 | same-source | no system is usable on this gold |
| wikipron | 106 | 0.2565 | 0.2221 | 0.2798 | 0.3518 | espeak |

### ca-x-balear (Balearic Catalan)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| 4catac | 160 | 0.1471 | 0.0797 | 0.1419 | 0.4998 | espeak |

### ca-x-occidental (North-Western Catalan)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| 4catac | 160 | 0.0944 | 0.0497 | 0.0832 | 0.4348 | espeak |

### ca-x-valencia (Valencian)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| 4catac | 160 | 0.0759 | 0.0439 | 0.0762 | 0.3775 | espeak |

### cop (Coptic (Sahidic))

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 591 | 0.3671 | 0.4491 | o2i |

### cy (Welsh)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipa_childes | 4666 | 0.2985 | same-source | same-source | 0.3495 | o2i |
| vox_communis | 18701 | 0.1172 | 0.3005 | 0.3016 | same-source | o2i |
| wikipron | 14811 | 0.1822 | 0.2799 | 0.2709 | 0.2170 | o2i |

### de (German)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| wikipron | 53011 | 0.2103 | 0.2126 | 0.2132 | 0.3064 | o2i |

### el (Modern Greek)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| vox_communis | 5994 | 0.2672 | 0.3347 | 0.3247 | same-source | o2i |
| wikipron | 19108 | 0.0330 | 0.0785 | 0.0765 | n/a | o2i |

### en (English)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | gruut | gruut rules-only | Winner |
|---|---|---|---|---|---|---|---|---|
| wikipron | 80995 | 0.2927 | 0.2081 | 0.2136 | 0.8333 | 0.1776 | 0.2149 | gruut |

### en-GB (British English (RP))

| Dataset | N | o2i | espeak | espeak rules-only | epitran | gruut | gruut rules-only | Winner |
|---|---|---|---|---|---|---|---|---|
| ipa_childes | 11447 | 0.3321 | same-source | same-source | n/a | 0.2876 | 0.3313 | gruut |
| ipadict | 65119 | 0.2516 | same-source | same-source | n/a | same-source | 0.2325 | gruut rules-only |
| wikipron | 81545 | 0.2605 | 0.1472 | 0.1540 | 0.8333 | 0.2233 | 0.2528 | espeak |

### en-US (American English (General American))

| Dataset | N | o2i | espeak | espeak rules-only | epitran | gruut | gruut rules-only | Winner |
|---|---|---|---|---|---|---|---|---|
| cmudict | 126052 | 0.4268 | 0.3048 | 0.3104 | n/a | same-source | 0.2714 | gruut rules-only |
| ipa_babylm | 20344 | 0.4180 | same-source | same-source | 1.0656 | 0.2788 | 0.3558 | gruut |
| ipa_childes | 18055 | 0.3220 | same-source | same-source | n/a | 0.1727 | 0.2317 | gruut |
| ipadict | 125927 | 0.4576 | 0.2954 | 0.3020 | n/a | same-source | 0.2475 | gruut rules-only |

### es (Spanish)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | pycotovia | ahotts-g2p | Winner |
|---|---|---|---|---|---|---|---|---|
| vox_communis | 97715 | 1.2097 | 1.2330 | 1.2247 | same-source | 1.2139 | 1.2117 | no system is usable on this gold |
| wikipron | 132190 | 0.0797 | 0.1071 | 0.1066 | 0.0277 | 0.1108 | 0.1041 | epitran |

### eu (Basque (Euskara))

| Dataset | N | o2i | espeak | espeak rules-only | epitran | ahotts-g2p | Winner |
|---|---|---|---|---|---|---|---|
| hitz_basque_ipa | 3113 | 0.0984 | 0.1204 | 0.1204 | n/a | same-source | o2i |
| ipa_childes | 3969 | 0.0821 | same-source | same-source | n/a | 0.1396 | o2i |
| vox_communis | 64077 | 0.0644 | 0.1194 | 0.1190 | same-source | 0.1280 | o2i |
| wikipron | 12022 | 0.0546 | 0.1019 | 0.0986 | n/a | 0.1507 | o2i |

### eu-wikipron (Basque (Euskara), wikipron-primary variant)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | ahotts-g2p | Winner |
|---|---|---|---|---|---|---|---|
| hitz_basque_ipa | 3113 | 0.0984 | 0.1204 | 0.1204 | n/a | same-source | o2i |
| ipa_childes | 3969 | 0.0821 | same-source | same-source | n/a | 0.1396 | o2i |
| vox_communis | 64077 | 0.0644 | 0.1194 | 0.1190 | same-source | 0.1280 | o2i |
| wikipron | 12022 | 0.0546 | 0.1019 | 0.0986 | n/a | 0.1507 | o2i |

### fi (Finnish)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipadict | 92836 | 0.0609 | 0.1995 | 0.1991 | 0.1111 | o2i |
| vox_communis | 13324 | 0.0037 | 0.1843 | 0.1838 | same-source | o2i |
| wikipron | 168814 | 0.0184 | 0.2062 | 0.2059 | 0.0963 | o2i |

### fr (French)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| wikipron | 85516 | 0.0673 | 0.0740 | 0.0749 | 0.2280 | o2i |

### ga (Irish)

| Dataset | N | o2i | espeak | espeak rules-only | Winner |
|---|---|---|---|---|---|
| ipa_childes | 1612 | 0.2989 | same-source | same-source | o2i |
| wikipron | 9621 | 0.1834 | 0.5223 | 0.5100 | o2i |

### gl (Galician)

| Dataset | N | o2i | epitran | pycotovia | Winner |
|---|---|---|---|---|---|
| vox_communis | 47515 | 0.0643 | same-source | 0.0883 | o2i |
| wikipron | 8091 | 0.0804 | n/a | 0.0883 | o2i |

### hi (Hindi)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| vox_communis | 13154 | 0.3684 | 0.5184 | 0.5178 | same-source | o2i |
| wikipron | 30379 | 0.1562 | 0.2815 | 0.2819 | 0.3322 | o2i |

### hts (Hadza)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 329 | 0.0650 | 0.2769 | o2i |

### it (Italian)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| vox_communis | 90366 | 1.1378 | 1.1830 | 1.1739 | same-source | no system is usable on this gold |
| wikipron | 82280 | 0.0441 | 0.0722 | 0.0767 | 0.0852 | o2i |

### kab (Kabyle)

| Dataset | N | o2i | epitran | africa-g2p | Winner |
|---|---|---|---|---|---|
| vox_communis | 54546 | 0.2071 | same-source | 0.4339 | o2i |

### ktz (Juǀʼhoan)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 134 | 0.3464 | 0.3806 | o2i |

### lad (Ladino (Judeo-Spanish))

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 131 | 0.1397 | 0.6256 | o2i |

### mfe (Morisyen)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 206 | 0.1238 | 0.3001 | o2i |

### ngh (Nǁng)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 263 | 0.3655 | 0.3958 | o2i |

### nl (Dutch)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipa_childes | 8108 | 0.2137 | same-source | same-source | 0.4454 | o2i |
| ipadict | 117869 | 0.1767 | 0.1607 | 0.1653 | 0.2948 | espeak |
| vox_communis | 26137 | 0.2925 | 0.3054 | 0.2986 | same-source | o2i |
| wikipron | 45872 | 0.0902 | 0.1099 | 0.1160 | 0.2843 | o2i |

### nup (Nupe)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 393 | 0.3979 | 0.4582 | o2i |

### pl (Polish)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipa_childes | 15524 | 0.2465 | same-source | same-source | 0.2453 | epitran |
| vox_communis | 47615 | 0.0194 | 0.0793 | 0.0782 | same-source | o2i |
| wikipron | 148992 | 0.0480 | 0.1132 | 0.1136 | 0.0633 | o2i |

### pt-PT (European Portuguese)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ep_dialects | 30 | 0.1185 | 0.3192 | 0.3225 | 0.4095 | o2i |
| ipa_childes | 3000 | 0.2498 | same-source | same-source | 0.4027 | o2i |
| portuguese_tts | 20 | same-source | 0.3336 | 0.3331 | 0.4042 | tie (espeak, espeak rules-only) |
| portuguese_unified | 3000 | 0.2245 | 0.3669 | 0.3631 | 0.4146 | o2i |
| wikipron | 2272 | 0.1346 | 0.2374 | 0.2373 | 0.2903 | o2i |

### ro (Romanian)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| vox_communis | 12097 | 0.3282 | 0.4480 | 0.4477 | same-source | o2i |
| wikipron | 8978 | 0.0342 | 0.0825 | 0.0761 | 0.0302 | epitran |

### ru (Russian)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| primary_sources | 36 | 0.1867 | 0.3119 | 0.3033 | 0.0744 | epitran |
| vox_communis | 50547 | 0.3447 | 0.3594 | 0.3501 | same-source | o2i |
| wikipron | 403873 | 0.1451 | 0.3953 | 0.3975 | 0.3202 | o2i |

### sv (Swedish)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipa_childes | 5202 | 0.3449 | same-source | same-source | 0.3576 | o2i |
| ipadict | 21095 | 0.2583 | 0.2611 | 0.2653 | 0.4163 | o2i |
| vox_communis | 19516 | 0.3428 | 0.3214 | 0.3195 | same-source | espeak rules-only |
| wikipron | 5082 | 0.2317 | 0.2337 | 0.2364 | 0.3692 | o2i |

### tr (Turkish)

| Dataset | N | o2i | espeak | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipa_childes | 2748 | 0.1372 | same-source | same-source | 0.1194 | epitran |
| vox_communis | 49476 | 0.1614 | 0.3443 | 0.3438 | same-source | o2i |
| wikipron | 11582 | 0.1230 | 0.2739 | 0.2735 | 0.1352 | o2i |

### tzm (Central Atlas Tamazight)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 658 | 0.0160 | 1.0005 | o2i |

## How to read this

**Systems compared.** o2i vs **espeak-ng**, **espeak-ng rules-only**, **epitran**, **gruut**, **gruut rules-only**, **pycotovia** (Galician & Spanish), **ahotts-g2p** (Basque & Spanish), and **africa-g2p** (10 African-language rows) — seven systems, two of which (espeak-ng, gruut) also get a rules-only column. Each system covers a different subset of languages. A missing mapping, or a system not installed in the generating environment, shows as `n/a` — never skipped, never faked.

**Rules-only columns, and why only two engines have one.** A "rules-only" column runs the SAME engine with its bundled dictionary/lexicon disabled, so it can only fall back on its own letter-to-sound rules or g2p model — the fair comparison against o2i, which by hard rule ships no word-exception list of its own. Disposition per engine:

- **espeak-ng** — `espeak_rules`: its dictsource `_list`/`_listx`/`_extra` word-exception files emptied before compiling (`scripts/build_espeak_rules_only.sh`, espeak-ng 1.52.0 pinned). Every number is verified before publishing: the build's manifest must list the language AND the compiled dictionary must differ from the stock one by md5 (`assert_espeak_rules_built_for`) — an earlier version of this board published a stock-vs-stock "comparison" for `es` because that check did not exist yet.
- **gruut** — `gruut_rules`: its bundled lexicon lookup (`TextProcessorSettings.lookup_phonemes`) disabled at runtime so every word falls through to gruut's own g2p fallback model instead of a dictionary hit. This exists because gruut's `en-US` lexicon (124,392 words) turned out to be CMUdict-derived and covers 98.2% of both the `cmudict` and `ipadict` gold sets — see the same-source note below for those two rows.
- **epitran** is a rule/mapping-based transliterator for the languages this board scores, not a lexicon lookup, so there is no dictionary to strip; the `es`/`gl` gold it is scored against uses a BROAD transcription convention (no ð/β/ɣ/θ allophone diacritics, glide notation folded) rather than the narrow one o2i and espeak-ng target — see the note on that below.
- **pycotovia** — audited: its lexicon is closed to function-word stress tables (a small, fixed, rule-grade set, not a general word dictionary), so there is no general-purpose lexicon to disable and no rules-only column is needed.
- **ahotts-g2p** — audited: it ships an HDIC dictionary (1,990 expansion entries; 103 TF_MRK words whose phonetic transcription is supplied directly by the dictionary; 1,065 per-word allophone-exception and 293 stress-marked entries), but those entries hit only 1.5% of the `eu` wikipron gold and 2.6% of `hitz_basque_ipa`, so a rules-only column would move the number by a fraction of a percent — recorded here rather than given a column.

**Winner column.** The lowest PER on the row, by name; ties (within 0.001 PER) name every system tied for best rather than a bare `tie`. `same-source` cells never win — they are not real comparisons. When even the best PER on a row exceeds 0.8, the cell says "no system is usable on this gold" instead of naming a misleadingly precise "winner" among systems that are all failing it.

**`same-source` cells.** A cell reads `same-source` (never `n/a`) when the gold dataset IS that system's own output — e.g. scoring `espeak` against `ipa_babylm` (espeak-derived), `ahotts-g2p` against `hitz_basque_ipa` (HiTZ's own phonemizer output, same lab as AhoTTS), or `gruut` (dictionary lookup, not `gruut_rules`) against `cmudict`/`ipadict` (gruut's `en-US` lexicon is CMUdict-derived — see above). Scoring a system against its own generator would score near-zero by construction, not because it is accurate, so that comparison is refused. The same rule applies to o2i itself on `arabic_tts`, `portuguese_tts`, and `gold20_arabic` — gold drafted by the same Claude lineage that wrote orthography2ipa's own Arabic/Portuguese specs.

**epitran's `es`/`gl` gold uses a broad transcription convention.** The wikipron gold rows for `es` and `gl` (and epitran's own output) are scored in the BROAD IPA convention — no allophonic diacritics (`ð β ɣ θ` etc.) and glide notation folded (`j w i̯ u̯` → `i u`) — rather than the narrower transcription o2i and espeak-ng aim for. #867 measured this directly: folding tier symbols out of both sides on `es`/`wikipron` moved o2i's PER from 0.0172 to 0.0090, and folding glide notation too moved it from 0.0099 to 0.0086 — most of a PER change on this row is notation converging, not an audible accuracy change. Read a narrow-vs-broad PER gap here as a convention difference, not a correctness gap.

**Machine-generated gold measures agreement, not accuracy.** Some gold datasets are themselves another phonemizer's or an LLM's output (see each dataset's `provenance_tier` in `benchmarks/comparison.json`). A win on one of those rows shows how much a system agrees with the tool that generated the gold — it is not a correctness claim.

**Normalization.** Every system is scored with the identical normalization and PER metric orthography2ipa's own scoreboard uses (`scripts/benchmark.py:normalize`/`levenshtein`): NFC-normalize, strip stress marks (length marks stay), strip narrow-transcription diacritics, drop whitespace, then score Levenshtein distance against the best-matching gold variant. No system gets a more forgiving metric.

**Honesty.** This table includes languages where o2i **loses** to espeak-ng. Cherry-picking would make the comparison worthless. Every gold dataset a language has gets its own row — not just the flattering one — so a system winning on one gold and losing on another for the SAME language is visible here.

**N** is the number of unique gold words for that language/dataset pair. A system's own scored count can be slightly lower — a word it failed to transcribe is excluded from its PER, not counted as an error — see the `*_n` fields in `benchmarks/comparison.json` for the exact per-system count. `N` can also differ from a PREVIOUS run of this same row for two unrelated reasons: `wikipron` gold is fetched live from its upstream GitHub repository and cached — a re-run against an empty cache picks up whatever Wiktionary-derived content is current upstream at fetch time, which drifts over time independent of any change here — `cy`/`wikipron`'s `N` in this regen (see the table above) differs from the previously committed board for exactly this reason, not an o2i or harness change; and a `sampled` row (below) draws a fixed-seed SUBSET whose exact size can differ slightly from run to run of the loader's own filtering, not from resampling.

## Robustness across golds

A system winning on one gold and losing on another for the SAME language is real signal, not noise to average away. Every language with 2+ espeak-comparable gold datasets is listed below with its exact win/loss split (same-source cells excluded — they are never comparable, see above).

- **`ca`** (MIXED — wins on some golds, loses on others):
  - `4catac` (n=160, tier=expert-human): o2i 0.0643 vs espeak 0.0403 — o2i loses
  - `vox_communis` (n=218451, tier=epitran-derived): o2i 0.8055 vs espeak 0.8195 — o2i wins
  - `wikipron` (n=106, tier=crowd-scraped): o2i 0.2565 vs espeak 0.2221 — o2i loses
- **`cy`** (wins on all golds):
  - `vox_communis` (n=18701, tier=epitran-derived): o2i 0.1172 vs espeak 0.3005 — o2i wins
  - `wikipron` (n=14811, tier=crowd-scraped): o2i 0.1822 vs espeak 0.2799 — o2i wins
- **`el`** (wins on all golds):
  - `vox_communis` (n=5994, tier=epitran-derived): o2i 0.2672 vs espeak 0.3347 — o2i wins
  - `wikipron` (n=19108, tier=crowd-scraped): o2i 0.0330 vs espeak 0.0785 — o2i wins
- **`en-US`** (loses on all golds):
  - `cmudict` (n=126052, tier=lexicon-derived): o2i 0.4268 vs espeak 0.3048 — o2i loses
  - `ipadict` (n=125927, tier=lexicon-derived): o2i 0.4576 vs espeak 0.2954 — o2i loses
- **`es`** (wins on all golds):
  - `vox_communis` (n=97715, tier=epitran-derived): o2i 1.2097 vs espeak 1.2330 — o2i wins
  - `wikipron` (n=132190, tier=crowd-scraped): o2i 0.0797 vs espeak 0.1071 — o2i wins
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
  - `vox_communis` (n=90366, tier=epitran-derived): o2i 1.1378 vs espeak 1.1830 — o2i wins
  - `wikipron` (n=82280, tier=crowd-scraped): o2i 0.0441 vs espeak 0.0722 — o2i wins
- **`nl`** (MIXED — wins on some golds, loses on others):
  - `ipadict` (n=117869, tier=machine-generated): o2i 0.1767 vs espeak 0.1607 — o2i loses
  - `vox_communis` (n=26137, tier=epitran-derived): o2i 0.2925 vs espeak 0.3054 — o2i wins
  - `wikipron` (n=45872, tier=crowd-scraped): o2i 0.0902 vs espeak 0.1099 — o2i wins
- **`pl`** (wins on all golds):
  - `vox_communis` (n=47615, tier=epitran-derived): o2i 0.0194 vs espeak 0.0793 — o2i wins
  - `wikipron` (n=148992, tier=crowd-scraped): o2i 0.0480 vs espeak 0.1132 — o2i wins
- **`pt-PT`** (wins on all golds):
  - `ep_dialects` (n=30, tier=expert-human): o2i 0.1185 vs espeak 0.3192 — o2i wins
  - `portuguese_unified` (n=3000, tier=lexicon-derived): o2i 0.2245 vs espeak 0.3669 — o2i wins
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

The table above conflates espeak-ng's letter-to-sound RULES with its hand-curated word-EXCEPTION list (o2i, by hard rule, ships no such list). This 2x2 isolates the dictionary's contribution on the same gold rows, for the languages where both extra columns are wired up (the `DICTSOURCE_LANG`-mapped subset — see the script's module docstring for how to enable `espeak_rules` via `scripts/build_espeak_rules_only.sh` and `o2i_lex` via `$ESPEAK_DICTSOURCE_PATH`). The dictionary is not a one-way upgrade: across every row with both numbers, espeak-ng's rules-only column actually BEATS stock (dictionary-included) espeak-ng on 28 of 51 rows — the word-exception list sometimes makes espeak-ng WORSE (e.g. letter-spelling acronyms getting a dictionary hit that is wrong for the gold's convention), not always better.

- `o2i` — orthography2ipa, rules only (unchanged from the main table).
- `o2i_lex` — orthography2ipa + a runtime lexicon built from espeak-ng's OWN word-exception list, each word's IPA obtained from espeak-ng itself (o2i rules + espeak's dictionary).
- `espeak` — espeak-ng, rules + its own word-exception dictionary (unchanged from the main table).
- `espeak_rules` — espeak-ng with the word-exception dictionary emptied before compiling (rules only).

| Lang | Dataset | N | o2i | o2i_lex | espeak | espeak_rules |
|---|---|---:|---:|---:|---:|---:|
| ca | 4catac | 160 | 0.0643 | n/a | 0.0403 | 0.1206 |
| ca | vox_communis | 218451 | 0.8055 | n/a | 0.8195 | 0.8168 |
| ca | wikipron | 106 | 0.2565 | n/a | 0.2221 | 0.2798 |
| ca-x-balear | 4catac | 160 | 0.1471 | n/a | 0.0797 | 0.1419 |
| ca-x-occidental | 4catac | 160 | 0.0944 | n/a | 0.0497 | 0.0832 |
| ca-x-valencia | 4catac | 160 | 0.0759 | n/a | 0.0439 | 0.0762 |
| cy | vox_communis | 18701 | 0.1172 | n/a | 0.3005 | 0.3016 |
| cy | wikipron | 14811 | 0.1822 | n/a | 0.2799 | 0.2709 |
| de | wikipron | 53011 | 0.2103 | n/a | 0.2126 | 0.2132 |
| el | vox_communis | 5994 | 0.2672 | n/a | 0.3347 | 0.3247 |
| el | wikipron | 19108 | 0.0330 | n/a | 0.0785 | 0.0765 |
| en | wikipron | 80995 | 0.2927 | n/a | 0.2081 | 0.2136 |
| en-GB | wikipron | 81545 | 0.2605 | n/a | 0.1472 | 0.1540 |
| en-US | cmudict | 126052 | 0.4268 | n/a | 0.3048 | 0.3104 |
| en-US | ipadict | 125927 | 0.4576 | n/a | 0.2954 | 0.3020 |
| es | vox_communis | 97715 | 1.2097 | n/a | 1.2330 | 1.2247 |
| es | wikipron | 132190 | 0.0797 | n/a | 0.1071 | 0.1066 |
| eu | hitz_basque_ipa | 3113 | 0.0984 | n/a | 0.1204 | 0.1204 |
| eu | vox_communis | 64077 | 0.0644 | n/a | 0.1194 | 0.1190 |
| eu | wikipron | 12022 | 0.0546 | n/a | 0.1019 | 0.0986 |
| eu-wikipron | hitz_basque_ipa | 3113 | 0.0984 | n/a | 0.1204 | 0.1204 |
| eu-wikipron | vox_communis | 64077 | 0.0644 | n/a | 0.1194 | 0.1190 |
| eu-wikipron | wikipron | 12022 | 0.0546 | n/a | 0.1019 | 0.0986 |
| fi | ipadict | 92836 | 0.0609 | n/a | 0.1995 | 0.1991 |
| fi | vox_communis | 13324 | 0.0037 | n/a | 0.1843 | 0.1838 |
| fi | wikipron | 168814 | 0.0184 | n/a | 0.2062 | 0.2059 |
| fr | wikipron | 85516 | 0.0673 | n/a | 0.0740 | 0.0749 |
| ga | wikipron | 9621 | 0.1834 | n/a | 0.5223 | 0.5100 |
| hi | vox_communis | 13154 | 0.3684 | n/a | 0.5184 | 0.5178 |
| hi | wikipron | 30379 | 0.1562 | n/a | 0.2815 | 0.2819 |
| it | vox_communis | 90366 | 1.1378 | n/a | 1.1830 | 1.1739 |
| it | wikipron | 82280 | 0.0441 | n/a | 0.0722 | 0.0767 |
| nl | ipadict | 117869 | 0.1767 | n/a | 0.1607 | 0.1653 |
| nl | vox_communis | 26137 | 0.2925 | n/a | 0.3054 | 0.2986 |
| nl | wikipron | 45872 | 0.0902 | n/a | 0.1099 | 0.1160 |
| pl | vox_communis | 47615 | 0.0194 | n/a | 0.0793 | 0.0782 |
| pl | wikipron | 148992 | 0.0480 | n/a | 0.1132 | 0.1136 |
| pt-PT | ep_dialects | 30 | 0.1185 | n/a | 0.3192 | 0.3225 |
| pt-PT | portuguese_tts | 20 | same-source | n/a | 0.3336 | 0.3331 |
| pt-PT | portuguese_unified | 3000 | 0.2245 | n/a | 0.3669 | 0.3631 |
| pt-PT | wikipron | 2272 | 0.1346 | n/a | 0.2374 | 0.2373 |
| ro | vox_communis | 12097 | 0.3282 | n/a | 0.4480 | 0.4477 |
| ro | wikipron | 8978 | 0.0342 | n/a | 0.0825 | 0.0761 |
| ru | primary_sources | 36 | 0.1867 | n/a | 0.3119 | 0.3033 |
| ru | vox_communis | 50547 | 0.3447 | n/a | 0.3594 | 0.3501 |
| ru | wikipron | 403873 | 0.1451 | n/a | 0.3953 | 0.3975 |
| sv | ipadict | 21095 | 0.2583 | n/a | 0.2611 | 0.2653 |
| sv | vox_communis | 19516 | 0.3428 | n/a | 0.3214 | 0.3195 |
| sv | wikipron | 5082 | 0.2317 | n/a | 0.2337 | 0.2364 |
| tr | vox_communis | 49476 | 0.1614 | n/a | 0.3443 | 0.3438 |
| tr | wikipron | 11582 | 0.1230 | n/a | 0.2739 | 0.2735 |

Reading the four numbers together: `espeak - espeak_rules` is espeak-ng's dictionary contribution; `o2i_lex - o2i` is what the SAME dictionary is worth bolted onto o2i's rules. `o2i` vs `espeak_rules` is the fairest rules-only comparison; `o2i_lex` vs `espeak` is the fairest dictionary-included comparison.

**Licensing**: espeak-ng's dictsource word lists and the IPA derived from them are GPL. They are used here ONLY at comparison runtime — fetched/built into a local scratch cache (`$ESPEAK_RULES_DATA_PATH`, `.o2i_lex_cache/`), never committed to this repository and never shipped in orthography2ipa's own package or lexicons.

## Catalan dialects vs espeak (BSC)

The Barcelona Supercomputing Center (BSC) added Catalan dialect voices to espeak-ng (central, balearic, north-western, valencian). This table compares each o2i Catalan dialect spec against the matching espeak-ng dialect voice on the 4catac gold (expert human-annotated regional accents) — the same expert gold used for the `ca` row in the main table above.

All three BSC dialect voices (`ca-ba`, `ca-nw`, `ca-va`) were found on this machine's espeak-ng install; each dialect row below uses its own dialect-specific voice.

| Dialect | o2i spec | espeak voice | N | o2i PER | espeak PER |
|---|---|---|---:|---:|---:|
| central | ca | ca | 106 | 0.2565 | 0.2221 |
| balear | ca-x-balear | ca-ba | 160 | 0.1471 | 0.0797 |
| valencian | ca-x-valencia | ca-va | 160 | 0.0759 | 0.0439 |
| occidental (nord-occidental) | ca-x-occidental | ca-nw | 160 | 0.0944 | 0.0497 |

<details>
<summary>Coverage, staleness notes, and how to regenerate this table</summary>

### Coverage

Not every gold language has a mapping for every competitor system: espeak-ng, epitran, gruut, pycotovia, ahotts-g2p, and africa-g2p each cover a different, smaller subset of languages than orthography2ipa's 493 language codes. `epitran`/`gruut`/`pycotovia`/`ahotts-g2p` are only installed via the dev-only `[compare]` extra; a committed run generated without them shows `n/a` in those columns for every row — that reflects the generating environment, not a claim those systems don't support the language.

**`eu-wikipron` is not a 37th language.** It is the SAME Basque spec as `eu`, registered as a separate board entry only so its independent `wikipron` gold can be the language's PRIMARY row for the leaderboard, instead of `eu`'s primary `hitz_basque_ipa` — which comes from HiTZ/Aholab, the same lab behind `ahotts-g2p`, and is close to same-source for that system (see the ahotts-g2p note below). Both entries score the identical set of gold datasets; only which one is PRIMARY differs.

**ahotts-g2p output space.** `ahotts-g2p` (Aholab / HiTZ AhoTTS G2P port; `eu`, `es`) emits its transcription in the StyleTTS2 single-character training convention: the library's `MULTI` table folds affricates (`tʃ`→`C`, `ts`→`V`, `tʂ`→`P`), aspirates (`pʰ`→`H`, `kʰ`→`K`, `tʰ`→`T`) and **stress-marked vowels** (`ˈi`→`I` … `ˈu`→`U`) onto single ASCII letters. Scoring that raw against IPA gold would charge a spurious error on every uppercase char, so the harness UNFOLDS it back to standard IPA (the inverse of `ahotts_g2p.phones.MULTI`) before scoring. The two ahotts-g2p `version`s (`classic`/`modern`) produce near-identical output; the committed rows use `classic` (see the `ahotts_version` field in `benchmarks/comparison.json`). The `eu` `hitz_basque_ipa` gold is authored by HiTZ/Aholab, the same lab behind AhoTTS, so ahotts-g2p's very low PER there is close to same-source — the independent `eu` `wikipron` (Wiktionary) row is the fairer comparison. The audio-only `pyahotts` package is NOT a comparison system here (no phoneme output).

**africa-g2p coverage.** `africa-g2p` (Ghana NLP; rule-based G2P for ~400 African-language ISO 639-3 codes) is not on PyPI, so it is not part of the `[compare]` extra — install it from a locally built wheel of the upstream checkout before regenerating this table (see the script's module docstring). Rows only appear for gold languages BOTH orthography2ipa and africa-g2p's own `registry()` cover — 10 languages as of this run: `arb`, `cop`, `hts`, `kab`, `ktz`, `lad`, `mfe`, `ngh`, `nup`, `tzm`. None of these ten has a matching espeak-ng voice, epitran code, or gruut language on this machine either, so africa-g2p is currently the only comparison point for these rows.

### Staleness

The `o2i PER` column here matches [`benchmarks/results.json`](../benchmarks/results.json)'s `per` for every shared language/dataset pair that used the same word count. 2 more row(s) differ for a DIFFERENT reason — not staleness: this board's `sample_n` config scores a fixed-seed SUBSET of the gold, while `benchmarks/results.json` scores the FULL gold. Same seed, different sample size, so a different PER is expected and regenerating either side will not reconcile them: `pt-PT`/`ipa_childes` (here 0.2498 on 3000 sampled words, results.json 0.2477 on the full 3846); `pt-PT`/`wikipron` (here 0.1346 on 2272 sampled words, results.json 0.0903 on the full 56891).

**espeak-rules-only coverage.** `espeak-rules-only` (the `espeak_rules_per` field) is a permanent column on this board: espeak-ng compiled from its own letter-to-sound rules with every per-language word-exception list (`_list`/`_listx`/`_extra`) emptied first — see `scripts/build_espeak_rules_only.sh`. Every row with a stock `espeak` number also carries an `espeak-rules-only` one in this run.

### Win tallies

Counted over distinct LANGUAGES (one row per language: its configured primary gold dataset — see `_primary_rows`), never over table rows, split by whether the primary gold is an independent reference or another tool's/LLM's output:

- **Gold-tier** (expert-human / lexicon-derived / crowd-scraped primary gold): o2i beats espeak on 17 of 24 comparable languages.
- **Agreement-tier** (machine-generated / espeak-derived / epitran-derived / llm-generated primary gold — measures agreement with the generating tool, not accuracy): o2i beats espeak on 1 of 1 comparable languages.

### Regenerate

```bash
pip install '.[compare]'  # epitran, gruut, pycotovia, ahotts-g2p — dev-only extra
PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard
```

Machine-readable form: [`benchmarks/comparison.json`](../benchmarks/comparison.json).

</details>
