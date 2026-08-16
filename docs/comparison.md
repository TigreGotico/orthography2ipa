# Comparison to other G2P systems

This table shows how well orthography2ipa (o2i) predicts IPA pronunciation compared to twelve other G2P systems (including the five o2i-downstream family engines — arbtok, tugaphone, g2p_barranquenho, mwl_phonemizer, udarnik), on the same gold word lists, language by language.

Every number is a **PER (Phoneme Error Rate)**: lower is better, `0.0000` is a perfect match, and it CAN exceed `1.0` when a system's output is much longer or shorter than the gold (more edits than the gold has phonemes).

## Leaderboard

One line per language: the best system on its primary gold, and where o2i lands. **Ranking policy: lexicon-free only** — a system's bundled per-word exception dictionary/lexicon never counts toward "winner", on the fair-comparison principle that o2i, by hard rule, ships no such lexicon of its own (see "How to read this" below for the full rationale and the per-engine disposition).

- **same-source** — the gold IS that system's own output; excluded from ranking, never a "winner".
- **n/a** — the system has no mapping, or isn't installed, for this language.
- **(lexicon)** — a lexicon-backed stock value: shown on the board for information, never ranked. Its rules-only sibling column (or the engine's own audited-lexicon-free stock value) is what actually competes for "winner".
- **tie** — two or more systems within 0.001 PER of the best; named, never a bare "tie".
- **rules-only** — the system with its bundled dictionary/lexicon disabled, scored on rules alone (see "How to read this" below).
- **#N** — N-th place by PER on that row, RANKED OVER THE LEXICON-FREE WORLD; `#1` is the winner.
- **"... with its lexicon scores N — informational"** — a lexicon-backed stock value that would have scored lowest of all systems on this row, named so it is never hidden — just not counted as the winner.

- **ar** — tie (arbtok, o2i) #1
- **arb (Classical Arabic)** — o2i not scored: this gold was drafted by o2i's own lineage — see same-source (africa-g2p #1 among the rest)
- **ca (Catalan)** — o2i #1 (beats espeak rules-only) (espeak with its lexicon scores 0.0403 — informational)
- **ca-x-balear (Balearic Catalan)** — o2i #1 (beats espeak rules-only) (espeak with its lexicon scores 0.0797 — informational)
- **ca-x-occidental (North-Western Catalan)** — o2i #1 (beats espeak rules-only) (espeak with its lexicon scores 0.0497 — informational)
- **ca-x-valencia (Valencian)** — o2i #1 (beats espeak rules-only) (espeak with its lexicon scores 0.0439 — informational)
- **cop (Coptic (Sahidic))** — o2i #1 (beats africa-g2p)
- **cy (Welsh)** — o2i #1 (beats epitran)
- **de (German)** — o2i #1 (beats espeak rules-only)
- **el (Modern Greek)** — o2i #1 (beats espeak rules-only)
- **en (English)** — espeak rules-only #1, o2i #3 (gruut with its lexicon scores 0.1776 — informational)
- **en-GB (British English (RP))** — espeak rules-only #1, o2i #3 (espeak with its lexicon scores 0.1472 — informational)
- **en-US (American English (General American))** — gruut rules-only #1, o2i #3
- **es (Spanish)** — epitran #1, o2i #2
- **eu (Basque (Euskara))** — o2i #1 (beats espeak rules-only)
- **eu-wikipron (Basque (Euskara), wikipron-primary variant)** — o2i #1 (beats espeak rules-only)
- **ext-PT-x-barrancos** — primary gold has no comparable systems (same-source); see the per-language table below for a comparison on a secondary gold
- **fi (Finnish)** — o2i #1 (beats epitran)
- **fr (French)** — o2i #1 (beats espeak rules-only)
- **ga (Irish)** — o2i #1 (beats espeak rules-only)
- **gl (Galician)** — o2i #1 (beats pycotovia)
- **hi (Hindi)** — o2i #1 (beats espeak rules-only)
- **hts (Hadza)** — o2i #1 (beats africa-g2p)
- **it (Italian)** — o2i #1 (beats espeak rules-only)
- **kab (Kabyle)** — o2i #1 (beats africa-g2p)
- **ktz (Juǀʼhoan)** — o2i #1 (beats africa-g2p)
- **lad (Ladino (Judeo-Spanish))** — o2i #1 (beats africa-g2p)
- **mfe (Morisyen)** — o2i #1 (beats africa-g2p)
- **mwl** — tie (mwl_phonemizer, o2i) #1
- **ngh (Nǁng)** — o2i #1 (beats africa-g2p)
- **nl (Dutch)** — o2i #1 (beats espeak rules-only)
- **nup (Nupe)** — o2i #1 (beats africa-g2p)
- **pl (Polish)** — o2i #1 (beats epitran)
- **pt-PT (European Portuguese)** — o2i #1 (beats espeak rules-only) (tugaphone with its lexicon scores 0.1887 — informational)
- **ro (Romanian)** — o2i #1 (beats epitran)
- **ru (Russian)** — o2i #1 (beats epitran)
- **sv (Swedish)** — o2i #1 (beats espeak rules-only)
- **tr (Turkish)** — o2i #1 (beats epitran)
- **tzm (Central Atlas Tamazight)** — o2i #1 (beats africa-g2p)

## The o2i family

orthography2ipa is a shared lattice — a grapheme table plus allophone/sandhi rules per language variety — that several TigreGotico projects build directly on top of, adding what the shared lattice deliberately leaves to the caller (lexicons, diacritization, dialect selection, normalization). These are FIRST-CLASS to this board, not "other G2P systems" being compared against o2i as competitors:

*Versions pinned: the family rows above were produced with arbtok 0.0.0a57, tugaphone 1.2.1a1, g2p_barranquenho 0.1.2a3, mwl_phonemizer 2.1.0a2 — every one of these exact versions is published on PyPI as a pre-release alpha (verified with `pip index versions <pkg> --pre`), so the number is reproducible from a plain `pip install --pre <pkg>==<version>` even on generating environments that installed a local/editable checkout at the same version instead.*

- **[arbtok](https://github.com/TigreGotico/arbtok)** — adds Arabic diacritization, dialect lexicons, nativized loanwords, and code-switch handling on top of the shared `ar`/`arb` lattice (the RANKED `arbtok` column below runs with both bundled lexicons off for a fair lexicon-free comparison — see `arbtok (lexicon)` for the full-featured stock number).
- **[tugaphone](https://github.com/TigreGotico/tugaphone)** — adds the curated `tugalex` pronunciation lexicon, sense-based homograph marking, and cross-dialect contact-language handling on top of the Portuguese-family lattice.
- **[g2p_barranquenho](https://github.com/TigreGotico/g2p_barranquenho)** — adds the Barranquenho (Spanish/Portuguese contact variety) rule layer on top of the `ext-PT-x-barrancos` lattice.
- **[mwl_phonemizer](https://github.com/TigreGotico/mwl_phonemizer)** — adds Mirandese dialect selection, an optional native-speaker lexicon overlay, and CRF correction on top of the `mwl` lattice.
- **[udarnik](https://github.com/TigreGotico/udarnik)** — adds a stressonnx-placed lexical accent on top of the `ru` lattice — Russian stress is free and unwritten, and the spec's own notes name its positional guess as the main source of its error, so supplying the real stress is what conditions akanje and ikanje correctly (no word->IPA lexicon: udarnik defaults to none. Its stressonnx `ruaccent` backend does consult a 110,826-entry accent dictionary and a 19,740-entry omograph dictionary before its models — 11.21% and 4.89% of unique `alphacep_ru_book` words respectively — but those hold STRESS POSITIONS, not pronunciations, so the column is ranked as effectively lexicon-free with the exception documented, the same treatment ahotts-g2p gets).

**Reading a family row: headroom, not a loss.** Where a family system's PER beats bare o2i's on a row that is NOT `same-source` (see below — same-source rows are refused as a comparison point, exactly like every other system on this board), that gap is a concrete demonstration of what the shared `orthography2ipa` specs could still absorb into the base lattice — a diacritizer pass, a closed-class lexicon, a dialect rule — not evidence o2i "lost" to a competitor. Where a family row instead ties o2i exactly, that is equally informative: it means the family member's extra stages are not (yet, or not on this gold) adding anything the base lattice does not already do on its own.

**Headroom is not automatically absorbable: the measured `ar` case.** "Headroom" above says a family gap shows what the base lattice *could* absorb. For the two independent Arabic rows (`ipadict`, raw `wikipron`) that reading has been tested directly and it does NOT hold — the entire arbtok margin is its neural diacritizer, which is a model, not a rule, and therefore not portable into a grapheme lattice at all. The ablation, run over the same word sets and the same scorer as the board rows (`ArbtokG2PPlugin(lang="ar", lexicon=None, dialect_lexicon=False)`, one stage disabled at a time):

| arbtok config | ipadict PER | wikipron PER |
|---|---|---|
| full (the ranked column) | 0.1727 | 0.1543 |
| `diacritize=False` | 0.3073 | 0.2547 |
| `stress=False` | 0.1727 | 0.1543 |
| `nativize=False` | 0.1727 | 0.1543 |
| `fusion=False` | 0.1721 | 0.1540 |
| `arabizi=False` | 0.1727 | 0.1543 |
| bare o2i, for reference | 0.3073 | 0.2514 |

Turning the diacritizer off collapses arbtok onto o2i exactly (ipadict 0.3073, the bare-o2i number to four places) or slightly BEHIND it (wikipron 0.2547 vs o2i's 0.2514); every other stage moves the score by at most 0.0006. Word-for-word, diacritizer-off arbtok and o2i emit byte-identical output on 98.1% (ipadict) and 94.4% (wikipron) of words, and on the remainder arbtok is net even (10 better / 10 worse) and net worse (4 better / 63 worse) respectively — i.e. the shared lattice has no residual rule-shaped deficit for a port to recover. The gap is a vocalization gap and nothing else: neither gold's headwords carry any harakat (0 of 2319 and 0 of 2735), and 71% (ipadict) / 55% (wikipron) of o2i's total edit distance is INSERTION of a short vowel the orthography simply does not write, with most of the consonant insertions being gemination the absent shadda does not write either. This is the honest ceiling for a rule-based lattice on undiacritized Arabic input, and it is why `ar`'s spec documents a fully-diacritized input contract rather than pretending to guess: the `wikipron_ar_diacritized` row, where harakat are restored on the INPUT before scoring, is where the two systems are compared with that ceiling lifted — and there they tie. That row carries its own caveat: the diacritized input is restored by `text2tashkeel`, the same diacritizer arbtok's default pipeline uses internally, so a diacritization error the two systems share is not an independence signal.

**Measurement stays unchanged.** Every family row is scored under the exact same discipline as every other system on this board: the SAME `same-source` refusal when a family engine would be scored against gold drawn from o2i's own lineage (see "How to read this" below — all five family engines are built on o2i's lattice, so they inherit o2i's own same-source exposure 1:1); the SAME lexicon-vs-rules-only discipline — g2p_barranquenho and mwl_phonemizer's lexicon-free DEFAULT configuration are ranked normally; arbtok's DEFAULT is lexicon-backed (a 145,890-entry stem lexicon plus a per-lect dialect lexicon, both on), so the ranked `arbtok` column is a deliberately NON-default configuration (`lexicon=None, dialect_lexicon=False`) leaving only the rule path plus a 22-entry closed demonstrative-pronoun exception table with no independent toggle, while the unmodified stock number is shown separately as the informational `arbtok (lexicon)` column; tugaphone's always-on `tugalex` lexicon has no public disable switch at all, so it is excluded from the lexicon-free Winner/leaderboard ranking the same way — and the SAME honest reporting either way, a family engine beating o2i is reported as loudly as a tie.

## Results by language

### ar

| Dataset | N | o2i | gruut (lexicon) | arbtok | arbtok (lexicon) | tugaphone (lexicon) | g2p_barranquenho | mwl_phonemizer | Winner |
|---|---|---|---|---|---|---|---|---|---|
| arabic_tts | 20 | same-source | n/a | same-source | same-source | same-source | same-source | same-source | n/a |
| gold20_arabic | 20 | same-source | n/a | same-source | same-source | same-source | same-source | same-source | n/a |
| ipadict | 2319 | 0.3073 | same-source | 0.1727 | 0.1693 | n/a | n/a | n/a | arbtok |
| wikipron | 2735 | 0.2514 | n/a | 0.1543 | 0.1472 | n/a | n/a | n/a | arbtok |
| wikipron_ar_diacritized | 2717 | 0.1788 | n/a | 0.1781 | 0.1781 | n/a | n/a | n/a | tie (arbtok, o2i) |

### arb (Classical Arabic)

| Dataset | N | o2i | africa-g2p | arbtok | arbtok (lexicon) | tugaphone (lexicon) | g2p_barranquenho | mwl_phonemizer | Winner |
|---|---|---|---|---|---|---|---|---|---|
| arabic_tts | 20 | same-source | 0.2836 | same-source | same-source | same-source | same-source | same-source | africa-g2p |
| gold20_arabic | 20 | same-source | 0.2666 | same-source | same-source | same-source | same-source | same-source | africa-g2p |

### ca (Catalan)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| 4catac | 160 | 0.0642 | 0.0403 | 0.1206 | 0.4641 | o2i |
| ipa_childes | 3814 | 0.2576 | same-source | same-source | 0.3447 | o2i |
| vox_communis | 218451 | 0.8053 | 0.8195 | 0.8168 | same-source | no system is usable on this gold |
| wikipron | 106 | 0.2565 | 0.2221 | 0.2798 | 0.3518 | o2i |

### ca-x-balear (Balearic Catalan)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| 4catac | 160 | 0.1360 | 0.0797 | 0.1419 | 0.4998 | o2i |

### ca-x-occidental (North-Western Catalan)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| 4catac | 160 | 0.0822 | 0.0497 | 0.0832 | 0.4348 | o2i |

### ca-x-valencia (Valencian)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| 4catac | 160 | 0.0677 | 0.0439 | 0.0762 | 0.3775 | o2i |

### cop (Coptic (Sahidic))

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 591 | 0.3671 | 0.4491 | o2i |

### cy (Welsh)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipa_childes | 4666 | 0.2985 | same-source | same-source | 0.3495 | o2i |
| vox_communis | 18701 | 0.1172 | 0.3005 | 0.3016 | same-source | o2i |
| wikipron | 14811 | 0.1822 | 0.2799 | 0.2709 | 0.2170 | o2i |

### de (German)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| wikipron | 53011 | 0.2103 | 0.2126 | 0.2132 | 0.3064 | o2i |

### el (Modern Greek)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| vox_communis | 5994 | 0.2672 | 0.3347 | 0.3247 | same-source | o2i |
| wikipron | 19108 | 0.0330 | 0.0785 | 0.0765 | n/a | o2i |

### en (English)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | gruut (lexicon) | gruut rules-only | Winner |
|---|---|---|---|---|---|---|---|---|
| wikipron | 80995 | 0.2917 | 0.2081 | 0.2136 | 0.8333 | 0.1776 | 0.2149 | espeak rules-only |

### en-GB (British English (RP))

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | gruut (lexicon) | gruut rules-only | Winner |
|---|---|---|---|---|---|---|---|---|
| ipa_childes | 11447 | 0.3321 | same-source | same-source | n/a | 0.2876 | 0.3313 | tie (gruut rules-only, o2i) |
| ipadict | 65119 | 0.2516 | same-source | same-source | n/a | same-source | 0.2325 | gruut rules-only |
| wikipron | 81545 | 0.2605 | 0.1472 | 0.1540 | 0.8333 | 0.2233 | 0.2528 | espeak rules-only |

### en-US (American English (General American))

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | gruut (lexicon) | gruut rules-only | Winner |
|---|---|---|---|---|---|---|---|---|
| cmudict | 126052 | 0.3736 | 0.3048 | 0.3104 | n/a | same-source | 0.2714 | gruut rules-only |
| ipa_babylm | 20344 | 0.3954 | same-source | same-source | 1.0656 | 0.2788 | 0.3558 | gruut rules-only |
| ipa_childes | 18055 | 0.3123 | same-source | same-source | n/a | 0.1727 | 0.2317 | gruut rules-only |
| ipadict | 125927 | 0.3285 | 0.2954 | 0.3020 | n/a | same-source | 0.2475 | gruut rules-only |

### es (Spanish)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | pycotovia | ahotts-g2p | Winner |
|---|---|---|---|---|---|---|---|---|
| vox_communis | 97715 | 1.2097 | 1.2330 | 1.2247 | same-source | 1.2139 | 1.2117 | no system is usable on this gold |
| wikipron | 132190 | 0.0797 | 0.1071 | 0.1066 | 0.0277 | 0.1108 | 0.1041 | epitran |

### eu (Basque (Euskara))

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | ahotts-g2p | Winner |
|---|---|---|---|---|---|---|---|
| hitz_basque_ipa | 3113 | 0.0984 | 0.1204 | 0.1204 | n/a | same-source | o2i |
| ipa_childes | 3969 | 0.0821 | same-source | same-source | n/a | 0.1396 | o2i |
| vox_communis | 64077 | 0.0644 | 0.1194 | 0.1190 | same-source | 0.1280 | o2i |
| wikipron | 12022 | 0.0546 | 0.1019 | 0.0986 | n/a | 0.1507 | o2i |

### eu-wikipron (Basque (Euskara), wikipron-primary variant)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | ahotts-g2p | Winner |
|---|---|---|---|---|---|---|---|
| hitz_basque_ipa | 3113 | 0.0984 | 0.1204 | 0.1204 | n/a | same-source | o2i |
| ipa_childes | 3969 | 0.0821 | same-source | same-source | n/a | 0.1396 | o2i |
| vox_communis | 64077 | 0.0644 | 0.1194 | 0.1190 | same-source | 0.1280 | o2i |
| wikipron | 12022 | 0.0546 | 0.1019 | 0.0986 | n/a | 0.1507 | o2i |

### ext-PT-x-barrancos

| Dataset | N | o2i | arbtok | arbtok (lexicon) | tugaphone (lexicon) | g2p_barranquenho | mwl_phonemizer | Winner |
|---|---|---|---|---|---|---|---|---|
| barranquenho_dict | 1508 | same-source | same-source | same-source | same-source | same-source | same-source | n/a |
| portuguese_tts | 20 | same-source | same-source | same-source | same-source | same-source | same-source | n/a |
| primary_sources | 10 | 0.2801 | n/a | n/a | n/a | 0.2801 | n/a | tie (g2p_barranquenho, o2i) |

### fi (Finnish)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipadict | 92836 | 0.0609 | 0.1995 | 0.1991 | 0.1111 | o2i |
| vox_communis | 13324 | 0.0037 | 0.1843 | 0.1838 | same-source | o2i |
| wikipron | 168814 | 0.0184 | 0.2062 | 0.2059 | 0.0963 | o2i |

### fr (French)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| wikipron | 85516 | 0.0673 | 0.0740 | 0.0749 | 0.2280 | o2i |

### ga (Irish)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | Winner |
|---|---|---|---|---|---|
| ipa_childes | 1612 | 0.2989 | same-source | same-source | o2i |
| wikipron | 9621 | 0.1834 | 0.5223 | 0.5100 | o2i |

### gl (Galician)

| Dataset | N | o2i | epitran | pycotovia | Winner |
|---|---|---|---|---|---|
| vox_communis | 47515 | 0.0643 | same-source | 0.0883 | o2i |
| wikipron | 8091 | 0.0804 | n/a | 0.0883 | o2i |

### hi (Hindi)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| vox_communis | 13154 | 0.3684 | 0.5184 | 0.5178 | same-source | o2i |
| wikipron | 30379 | 0.1277 | 0.2815 | 0.2819 | 0.3322 | o2i |

### hts (Hadza)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 329 | 0.0224 | 0.2414 | o2i |

### it (Italian)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
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

### mwl

| Dataset | N | o2i | arbtok | arbtok (lexicon) | tugaphone (lexicon) | g2p_barranquenho | mwl_phonemizer | Winner |
|---|---|---|---|---|---|---|---|---|
| mirandese_dict | 990 | 0.0401 | n/a | n/a | n/a | n/a | 0.0401 | tie (mwl_phonemizer, o2i) |
| mirandese_g2p | 205 | 0.1317 | n/a | n/a | n/a | n/a | 0.1317 | tie (mwl_phonemizer, o2i) |
| portuguese_tts | 20 | same-source | same-source | same-source | same-source | same-source | same-source | n/a |

### ngh (Nǁng)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 263 | 0.3655 | 0.3958 | o2i |

### nl (Dutch)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipa_childes | 8108 | 0.2137 | same-source | same-source | 0.4454 | o2i |
| ipadict | 117869 | 0.1767 | 0.1607 | 0.1653 | 0.2948 | espeak rules-only |
| vox_communis | 26137 | 0.2925 | 0.3054 | 0.2986 | same-source | o2i |
| wikipron | 45872 | 0.0902 | 0.1099 | 0.1160 | 0.2843 | o2i |

### nup (Nupe)

| Dataset | N | o2i | africa-g2p | Winner |
|---|---|---|---|---|
| wikipron | 393 | 0.3979 | 0.4582 | o2i |

### pl (Polish)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipa_childes | 15524 | 0.2465 | same-source | same-source | 0.2453 | epitran |
| vox_communis | 47615 | 0.0194 | 0.0793 | 0.0782 | same-source | o2i |
| wikipron | 148992 | 0.0480 | 0.1132 | 0.1136 | 0.0633 | o2i |

### pt-PT (European Portuguese)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | arbtok | arbtok (lexicon) | tugaphone (lexicon) | g2p_barranquenho | mwl_phonemizer | Winner |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ep_dialects | 30 | 0.1185 | 0.3192 | 0.3225 | 0.4095 | n/a | n/a | 0.1185 | n/a | n/a | o2i |
| ipa_childes | 3000 | 0.2498 | same-source | same-source | 0.4027 | n/a | n/a | 0.2496 | n/a | n/a | o2i |
| portuguese_tts | 20 | same-source | 0.3336 | 0.3331 | 0.4042 | same-source | same-source | same-source | same-source | same-source | espeak rules-only |
| portuguese_unified | 3000 | 0.2245 | 0.3669 | 0.3631 | 0.4146 | n/a | n/a | 0.1887 | n/a | n/a | o2i |
| wikipron | 2272 | 0.1346 | 0.2374 | 0.2373 | 0.2903 | n/a | n/a | 0.1341 | n/a | n/a | o2i |

### ro (Romanian)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| vox_communis | 12097 | 0.3332 | 0.4480 | 0.4477 | same-source | o2i |
| wikipron | 8978 | 0.0198 | 0.0825 | 0.0761 | 0.0302 | o2i |

### ru (Russian)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| alphacep_ru_book | 6175 | 0.2395 | 0.3249 | 0.3133 | 0.1008 | epitran |
| coruss_ru | 9527 | 0.3584 | 0.4206 | 0.4311 | 0.2939 | epitran |
| primary_sources | 36 | 0.1867 | 0.3119 | 0.3033 | 0.0744 | epitran |
| vox_communis | 50517 | 0.3481 | 0.3578 | 0.3487 | same-source | tie (espeak rules-only, o2i) |
| wikipron | 403873 | 0.1449 | 0.3953 | 0.3976 | 0.3202 | o2i |

### sv (Swedish)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
|---|---|---|---|---|---|---|
| ipa_childes | 5202 | 0.3449 | same-source | same-source | 0.3576 | o2i |
| ipadict | 21095 | 0.2583 | 0.2611 | 0.2653 | 0.4163 | o2i |
| vox_communis | 19516 | 0.3428 | 0.3214 | 0.3195 | same-source | espeak rules-only |
| wikipron | 5082 | 0.2317 | 0.2337 | 0.2364 | 0.3692 | o2i |

### tr (Turkish)

| Dataset | N | o2i | espeak (lexicon) | espeak rules-only | epitran | Winner |
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

**Ranking policy: lexicon-free only.** Anything with a lexicon does not count as a winner. The Winner column and the leaderboard rank over LEXICON-FREE values only: each engine's rules-only variant where one exists (`espeak_rules`, `gruut_rules`), its stock value where the engine is audited lexicon-free (epitran's rule/mapping tables, pycotovia's closed function-word stress table, africa-g2p's rule-based G2P), and ahotts-g2p's stock value — its HDIC dictionary hits only 1.5%/2.6% of the `eu`/`hitz_basque_ipa` gold, an explicit documented exception, not an oversight (see the per-engine disposition above). A lexicon-BACKED stock value — plain `espeak`, plain `gruut`, and (once it lands) a `transphone`-style tokenizer column — is EXCLUDED from ranking entirely, on the fair-comparison principle that o2i, by hard rule, ships no bundled word-exception lexicon of its own: ranking o2i's rules against another system's rules-plus-dictionary is not a fair fight (see the module docstring's "Fair-comparison 2x2" section, which this policy generalizes from a side table into the primary ranking). This is a deliberate ranking policy, not hidden data — the lexicon-backed columns stay right there on the board, marked `(lexicon)`, for anyone who wants the dictionary-included picture; the leaderboard just also names, as an informational aside, whenever a lexicon-backed value would have scored lowest of all (`espeak with its lexicon scores N — informational`) — visible, never counted.

**Symmetric alternative: the lexicon-backed tier.** The fair-comparison principle cuts both ways, so the board also carries a SECOND ranking where every engine keeps its lexicon on and o2i takes part on the same terms (as `o2i_lex`, o2i plus espeak-ng's own word list) — see "Lexicon-backed tier" below. It is scored on gold FILTERED against the union of every compared engine's lexicon, so it measures generalization beyond those lexicons rather than test-set lookup. It is a separate table with its own winner column and never feeds this leaderboard or the Winner column above.

**Winner column.** The lowest PER on the row IN THE LEXICON-FREE WORLD (see "Ranking policy" above), by name; ties (within 0.001 PER) name every system tied for best rather than a bare `tie`. `same-source` cells never win — they are not real comparisons. When even the best PER on a row exceeds 0.8, the cell says "no system is usable on this gold" instead of naming a misleadingly precise "winner" among systems that are all failing it.

**`same-source` cells.** A cell reads `same-source` (never `n/a`) when the gold dataset IS that system's own output — e.g. scoring `espeak` against `ipa_babylm` (espeak-derived), `ahotts-g2p` against `hitz_basque_ipa` (HiTZ's own phonemizer output, same lab as AhoTTS), or `gruut` (dictionary lookup, not `gruut_rules`) against `cmudict`/`ipadict` (gruut's `en-US` lexicon is CMUdict-derived — see above). Scoring a system against its own generator would score near-zero by construction, not because it is accurate, so that comparison is refused. The same rule applies to o2i itself on `arabic_tts`, `portuguese_tts`, and `gold20_arabic` — gold drafted by the same Claude lineage that wrote orthography2ipa's own Arabic/Portuguese specs.

**epitran's `es`/`gl` gold uses a broad transcription convention.** The wikipron gold rows for `es` and `gl` (and epitran's own output) are scored in the BROAD IPA convention — no allophonic diacritics (`ð β ɣ θ` etc.) and glide notation folded (`j w i̯ u̯` → `i u`) — rather than the narrower transcription o2i and espeak-ng aim for. #867 measured this directly: folding tier symbols out of both sides on `es`/`wikipron` moved o2i's PER from 0.0172 to 0.0090, and folding glide notation too moved it from 0.0099 to 0.0086 — most of a PER change on this row is notation converging, not an audible accuracy change. Read a narrow-vs-broad PER gap here as a convention difference, not a correctness gap.

**Machine-generated gold measures agreement, not accuracy.** Some gold datasets are themselves another phonemizer's or an LLM's output (see each dataset's `provenance_tier` in `benchmarks/comparison.json`). A win on one of those rows shows how much a system agrees with the tool that generated the gold — it is not a correctness claim.

**Normalization.** Every system is scored with the identical normalization and PER metric orthography2ipa's own scoreboard uses (`scripts/benchmark.py:normalize`/`levenshtein`): NFC-normalize, strip stress marks (length marks stay), strip narrow-transcription diacritics, drop whitespace, then score Levenshtein distance against the best-matching gold variant. No system gets a more forgiving metric.

**Honesty.** This table includes languages where o2i **loses** to espeak-ng. Cherry-picking would make the comparison worthless. Every gold dataset a language has gets its own row — not just the flattering one — so a system winning on one gold and losing on another for the SAME language is visible here.

**N** is the number of unique gold words for that language/dataset pair. A system's own scored count can be slightly lower — a word it failed to transcribe is excluded from its PER, not counted as an error — see the `*_n` fields in `benchmarks/comparison.json` for the exact per-system count. `N` can also differ from a PREVIOUS run of this same row for two unrelated reasons: `wikipron` gold is fetched live from its upstream GitHub repository and cached — a re-run against an empty cache picks up whatever Wiktionary-derived content is current upstream at fetch time, which drifts over time independent of any change here — `cy`/`wikipron`'s `N` in this regen (see the table above) differs from the previously committed board for exactly this reason, not an o2i or harness change; and a `sampled` row (below) draws a fixed-seed SUBSET whose exact size can differ slightly from run to run of the loader's own filtering, not from resampling.

## Robustness across golds

A system winning on one gold and losing on another for the SAME language is real signal, not noise to average away. Every language with 2+ espeak-comparable gold datasets is listed below with its exact win/loss split (same-source cells excluded — they are never comparable, see above).

- **`ca`** (MIXED — wins on some golds, loses on others):
  - `4catac` (n=160, tier=expert-human): o2i 0.0642 vs espeak 0.0403 — o2i loses
  - `vox_communis` (n=218451, tier=epitran-derived): o2i 0.8053 vs espeak 0.8195 — o2i wins
  - `wikipron` (n=106, tier=crowd-scraped): o2i 0.2565 vs espeak 0.2221 — o2i loses
- **`cy`** (wins on all golds):
  - `vox_communis` (n=18701, tier=epitran-derived): o2i 0.1172 vs espeak 0.3005 — o2i wins
  - `wikipron` (n=14811, tier=crowd-scraped): o2i 0.1822 vs espeak 0.2799 — o2i wins
- **`el`** (wins on all golds):
  - `vox_communis` (n=5994, tier=epitran-derived): o2i 0.2672 vs espeak 0.3347 — o2i wins
  - `wikipron` (n=19108, tier=crowd-scraped): o2i 0.0330 vs espeak 0.0785 — o2i wins
- **`en-US`** (loses on all golds):
  - `cmudict` (n=126052, tier=lexicon-derived): o2i 0.3736 vs espeak 0.3048 — o2i loses
  - `ipadict` (n=125927, tier=lexicon-derived): o2i 0.3285 vs espeak 0.2954 — o2i loses
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
  - `wikipron` (n=30379, tier=crowd-scraped): o2i 0.1277 vs espeak 0.2815 — o2i wins
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
  - `vox_communis` (n=12097, tier=epitran-derived): o2i 0.3332 vs espeak 0.4480 — o2i wins
  - `wikipron` (n=8978, tier=crowd-scraped): o2i 0.0198 vs espeak 0.0825 — o2i wins
- **`ru`** (wins on all golds):
  - `alphacep_ru_book` (n=6175, tier=machine-generated): o2i 0.2395 vs espeak 0.3249 — o2i wins
  - `coruss_ru` (n=9527, tier=expert-human): o2i 0.3584 vs espeak 0.4206 — o2i wins
  - `primary_sources` (n=36, tier=expert-human): o2i 0.1867 vs espeak 0.3119 — o2i wins
  - `vox_communis` (n=50517, tier=epitran-derived): o2i 0.3481 vs espeak 0.3578 — o2i wins
  - `wikipron` (n=403873, tier=crowd-scraped): o2i 0.1449 vs espeak 0.3953 — o2i wins
- **`sv`** (MIXED — wins on some golds, loses on others):
  - `ipadict` (n=21095, tier=lexicon-derived): o2i 0.2583 vs espeak 0.2611 — o2i wins
  - `vox_communis` (n=19516, tier=epitran-derived): o2i 0.3428 vs espeak 0.3214 — o2i loses
  - `wikipron` (n=5082, tier=crowd-scraped): o2i 0.2317 vs espeak 0.2337 — o2i wins
- **`tr`** (wins on all golds):
  - `vox_communis` (n=49476, tier=epitran-derived): o2i 0.1614 vs espeak 0.3443 — o2i wins
  - `wikipron` (n=11582, tier=crowd-scraped): o2i 0.1230 vs espeak 0.2739 — o2i wins

## Fair-comparison 2x2 (dictionary vs. rules)

The table above conflates espeak-ng's letter-to-sound RULES with its hand-curated word-EXCEPTION list (o2i, by hard rule, ships no such list). This 2x2 isolates the dictionary's contribution on the same gold rows, for the languages where both extra columns are wired up (the `DICTSOURCE_LANG`-mapped subset — see the script's module docstring for how to enable `espeak_rules` via `scripts/build_espeak_rules_only.sh` and `o2i_lex` via `$ESPEAK_DICTSOURCE_PATH`). The dictionary is not a one-way upgrade: across every row with both numbers, espeak-ng's rules-only column actually BEATS stock (dictionary-included) espeak-ng on 29 of 53 rows — the word-exception list sometimes makes espeak-ng WORSE (e.g. letter-spelling acronyms getting a dictionary hit that is wrong for the gold's convention), not always better.

- `o2i` — orthography2ipa, rules only (unchanged from the main table).
- `o2i_lex` — orthography2ipa + a runtime lexicon built from espeak-ng's OWN word-exception list, each word's IPA obtained from espeak-ng itself (o2i rules + espeak's dictionary).
- `espeak` — espeak-ng, rules + its own word-exception dictionary (unchanged from the main table).
- `espeak_rules` — espeak-ng with the word-exception dictionary emptied before compiling (rules only).

| Lang | Dataset | N | o2i | o2i_lex | espeak | espeak_rules |
|---|---|---:|---:|---:|---:|---:|
| ca | 4catac | 160 | 0.0642 | n/a | 0.0403 | 0.1206 |
| ca | vox_communis | 218451 | 0.8053 | n/a | 0.8195 | 0.8168 |
| ca | wikipron | 106 | 0.2565 | n/a | 0.2221 | 0.2798 |
| ca-x-balear | 4catac | 160 | 0.1360 | n/a | 0.0797 | 0.1419 |
| ca-x-occidental | 4catac | 160 | 0.0822 | n/a | 0.0497 | 0.0832 |
| ca-x-valencia | 4catac | 160 | 0.0677 | n/a | 0.0439 | 0.0762 |
| cy | vox_communis | 18701 | 0.1172 | n/a | 0.3005 | 0.3016 |
| cy | wikipron | 14811 | 0.1822 | n/a | 0.2799 | 0.2709 |
| de | wikipron | 53011 | 0.2103 | n/a | 0.2126 | 0.2132 |
| el | vox_communis | 5994 | 0.2672 | n/a | 0.3347 | 0.3247 |
| el | wikipron | 19108 | 0.0330 | n/a | 0.0785 | 0.0765 |
| en | wikipron | 80995 | 0.2917 | 0.2849 | 0.2081 | 0.2136 |
| en-GB | wikipron | 81545 | 0.2605 | n/a | 0.1472 | 0.1540 |
| en-US | cmudict | 126052 | 0.3736 | n/a | 0.3048 | 0.3104 |
| en-US | ipadict | 125927 | 0.3285 | n/a | 0.2954 | 0.3020 |
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
| hi | wikipron | 30379 | 0.1277 | n/a | 0.2815 | 0.2819 |
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
| ro | vox_communis | 12097 | 0.3332 | n/a | 0.4480 | 0.4477 |
| ro | wikipron | 8978 | 0.0198 | n/a | 0.0825 | 0.0761 |
| ru | alphacep_ru_book | 6175 | 0.2395 | n/a | 0.3249 | 0.3133 |
| ru | coruss_ru | 9527 | 0.3584 | n/a | 0.4206 | 0.4311 |
| ru | primary_sources | 36 | 0.1867 | n/a | 0.3119 | 0.3033 |
| ru | vox_communis | 50517 | 0.3481 | n/a | 0.3578 | 0.3487 |
| ru | wikipron | 403873 | 0.1449 | n/a | 0.3953 | 0.3976 |
| sv | ipadict | 21095 | 0.2583 | n/a | 0.2611 | 0.2653 |
| sv | vox_communis | 19516 | 0.3428 | n/a | 0.3214 | 0.3195 |
| sv | wikipron | 5082 | 0.2317 | n/a | 0.2337 | 0.2364 |
| tr | vox_communis | 49476 | 0.1614 | n/a | 0.3443 | 0.3438 |
| tr | wikipron | 11582 | 0.1230 | n/a | 0.2739 | 0.2735 |

Reading the four numbers together: `espeak - espeak_rules` is espeak-ng's dictionary contribution; `o2i_lex - o2i` is what the SAME dictionary is worth bolted onto o2i's rules. `o2i` vs `espeak_rules` is the fairest rules-only comparison; `o2i_lex` vs `espeak` is the fairest dictionary-included comparison.

**Licensing**: espeak-ng's dictsource word lists and the IPA derived from them are GPL. They are used here ONLY at comparison runtime — fetched/built into a local scratch cache (`$ESPEAK_RULES_DATA_PATH`, `.o2i_lex_cache/`), never committed to this repository and never shipped in orthography2ipa's own package or lexicons.

## Lexicon-backed tier — gold filtered against all compared lexicons

This is a SECOND, separate ranking, and it never feeds the leaderboard or the Winner column above. Here every engine runs in its STOCK configuration — lexicons ON, exactly as a caller gets it with no arguments — and o2i takes part on the same terms, as `o2i_lex` (o2i plus espeak-ng's own word list). Ranking stock engines on the raw gold would measure nothing but dictionary size: a gold word that sits in an engine's lexicon is a lookup, not a prediction. So the gold is FILTERED first — every entry present in ANY compared engine's lexicon for that language is removed, the same words removed for every engine — and what remains is scored. The tier therefore measures how well each stock system GENERALIZES beyond the lexicons it ships, not how much of this particular test set it already knows. `N` is the original gold size, `filtered N` what survived the union filter; below 50 residual words a row is reported as insufficient rather than ranked on noise.

| Language | Gold | N | filtered N | o2i + espeak lexicon | espeak-ng (stock) | gruut (stock) | tugaphone (stock) | Winner |
|---|---|---|---|---|---|---|---|---|
| en (English) | `wikipron` | 80995 | 44126 | 0.3078 | 0.2425 | 0.2529 | n/a | espeak-ng (stock) |
| pt-PT (European Portuguese) | `ep_dialects` | 30 | 0 | n/a | n/a | n/a | n/a | insufficient residual gold (< 50) |
| pt-PT (European Portuguese) | `portuguese_unified` | 3000 | 1952 | n/a | 0.3685 | n/a | 0.2202 | tugaphone (stock) |
| pt-PT (European Portuguese) | `wikipron` | 2272 | 1788 | n/a | 0.2352 | n/a | 0.1400 | tugaphone (stock) |

**What the filter removed.** Per row, how many of the gold's words each compared engine's lexicon already contained (the union of these is what was filtered out), and how large that lexicon is:

| Language | Gold | o2i + espeak lexicon | espeak-ng (stock) | gruut (stock) | tugaphone (stock) |
|---|---|---|---|---|---|
| en (English) | `wikipron` | 3527 (of 4716 entries) | 3527 (of 4716 entries) | 36472 (of 124392 entries) | n/a |
| pt-PT (European Portuguese) | `ep_dialects` | n/a | 23 (of 1692 entries) | n/a | 30 (of 53150 entries) |
| pt-PT (European Portuguese) | `portuguese_unified` | n/a | 15 (of 1692 entries) | n/a | 1044 (of 53150 entries) |
| pt-PT (European Portuguese) | `wikipron` | n/a | 57 (of 1692 entries) | n/a | 434 (of 53150 entries) |

**Where each key set came from.** Every lexicon is enumerated from the engine's OWN lookup data, and each gold word is matched against it with the same normalization that engine applies at lookup time (an over-narrow match would silently readmit looked-up words into the residual gold):

- **espeak-ng (stock) — espeak-ng dictsource en_(list|listx|extra)** — version `1.52.0`, matched as NFC + lowercase.
- **espeak-ng (stock) — espeak-ng dictsource pt_(list|listx|extra)** — version `1.52.0`, matched as NFC + lowercase.
- **gruut (stock) — gruut_lang_en/lexicon.db (word_phonemes.word)** — version `2.0.1`, matched as NFC + lowercase.
- **o2i + espeak lexicon — .o2i_lex_cache/en.tsv** — version `7.70.1a2`, matched as o2i lexicon key (NFC + language-aware lower).
- **tugaphone (stock) — tugalex.TugaLexicon().get_ipa_map(region='lbx')** — version `2.0.1a1`, matched as o2i lexicon key (NFC + language-aware lower).

## Catalan dialects vs espeak (BSC)

The Barcelona Supercomputing Center (BSC) added Catalan dialect voices to espeak-ng (central, balearic, north-western, valencian). This table compares each o2i Catalan dialect spec against the matching espeak-ng dialect voice on the 4catac gold (expert human-annotated regional accents) — the same expert gold used for the `ca` row in the main table above.

All three BSC dialect voices (`ca-ba`, `ca-nw`, `ca-va`) were found on this machine's espeak-ng install; each dialect row below uses its own dialect-specific voice.

| Dialect | o2i spec | espeak voice | N | o2i PER | espeak PER |
|---|---|---|---:|---:|---:|
| central | ca | ca | 106 | 0.2565 | 0.2221 |
| balear | ca-x-balear | ca-ba | 160 | 0.1360 | 0.0797 |
| valencian | ca-x-valencia | ca-va | 160 | 0.0677 | 0.0439 |
| occidental (nord-occidental) | ca-x-occidental | ca-nw | 160 | 0.0822 | 0.0497 |

<details>
<summary>Coverage, staleness notes, and how to regenerate this table</summary>

### Coverage

Not every gold language has a mapping for every competitor system: espeak-ng, epitran, gruut, pycotovia, ahotts-g2p, and africa-g2p each cover a different, smaller subset of languages than orthography2ipa's 493 language codes. `epitran`/`gruut`/`pycotovia`/`ahotts-g2p` are only installed via the dev-only `[compare]` extra; a committed run generated without them shows `n/a` in those columns for every row — that reflects the generating environment, not a claim those systems don't support the language.

**`eu-wikipron` is not a 37th language.** It is the SAME Basque spec as `eu`, registered as a separate board entry only so its independent `wikipron` gold can be the language's PRIMARY row for the leaderboard, instead of `eu`'s primary `hitz_basque_ipa` — which comes from HiTZ/Aholab, the same lab behind `ahotts-g2p`, and is close to same-source for that system (see the ahotts-g2p note below). Both entries score the identical set of gold datasets; only which one is PRIMARY differs.

**ahotts-g2p output space.** `ahotts-g2p` (Aholab / HiTZ AhoTTS G2P port; `eu`, `es`) emits its transcription in the StyleTTS2 single-character training convention: the library's `MULTI` table folds affricates (`tʃ`→`C`, `ts`→`V`, `tʂ`→`P`), aspirates (`pʰ`→`H`, `kʰ`→`K`, `tʰ`→`T`) and **stress-marked vowels** (`ˈi`→`I` … `ˈu`→`U`) onto single ASCII letters. Scoring that raw against IPA gold would charge a spurious error on every uppercase char, so the harness UNFOLDS it back to standard IPA (the inverse of `ahotts_g2p.phones.MULTI`) before scoring. The two ahotts-g2p `version`s (`classic`/`modern`) produce near-identical output; the committed rows use `classic` (see the `ahotts_version` field in `benchmarks/comparison.json`). The `eu` `hitz_basque_ipa` gold is authored by HiTZ/Aholab, the same lab behind AhoTTS, so ahotts-g2p's very low PER there is close to same-source — the independent `eu` `wikipron` (Wiktionary) row is the fairer comparison. The audio-only `pyahotts` package is NOT a comparison system here (no phoneme output).

**africa-g2p coverage.** `africa-g2p` (Ghana NLP; rule-based G2P for ~400 African-language ISO 639-3 codes) is not on PyPI, so it is not part of the `[compare]` extra — install it from a locally built wheel of the upstream checkout before regenerating this table (see the script's module docstring). Rows only appear for gold languages BOTH orthography2ipa and africa-g2p's own `registry()` cover — 10 languages as of this run: `arb`, `cop`, `hts`, `kab`, `ktz`, `lad`, `mfe`, `ngh`, `nup`, `tzm`. None of these ten has a matching espeak-ng voice, epitran code, or gruut language on this machine either, so africa-g2p is currently the only comparison point for these rows.

### Staleness

The `o2i PER` column here matches [`benchmarks/results.json`](../benchmarks/results.json)'s `per` for most shared language/dataset pairs, EXCEPT the 7 listed below — those `benchmarks/results.json` rows are stale (a prior PR changed the engine but did not regenerate every affected row there; see e.g. PR #802's `ca`/`4catac`-only regeneration). The numbers in THIS table reflect the current engine via a live run; `benchmarks/results.json` needs a matching regeneration for: `ext-PT-x-barrancos`/`barranquenho_dict` (here 0.0045, results.json 0.1053); `mwl`/`mirandese_dict` (here 0.0401, results.json 0.2665); `mwl`/`mirandese_g2p` (here 0.1317, results.json 0.1404); `sv`/`ipa_childes` (here 0.3449, results.json 0.3476); `sv`/`ipadict` (here 0.2583, results.json 0.2427); `sv`/`vox_communis` (here 0.3428, results.json 0.3735); `sv`/`wikipron` (here 0.2317, results.json 0.2414). 5 more row(s) differ for a DIFFERENT reason — not staleness: this board's `sample_n` config scores a fixed-seed SUBSET of the gold, while `benchmarks/results.json` scores the FULL gold. Same seed, different sample size, so a different PER is expected and regenerating either side will not reconcile them: `ar`/`ipadict` (here 0.3073 on 2319 sampled words, results.json 0.3768 on the full 857160); `ar`/`wikipron` (here 0.2514 on 2735 sampled words, results.json 0.3136 on the full 14268); `ar`/`wikipron_ar_diacritized` (here 0.1788 on 2717 sampled words, results.json 0.1666 on the full 14240); `pt-PT`/`ipa_childes` (here 0.2498 on 3000 sampled words, results.json 0.2477 on the full 3846); `pt-PT`/`wikipron` (here 0.1346 on 2272 sampled words, results.json 0.0903 on the full 56891).

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
