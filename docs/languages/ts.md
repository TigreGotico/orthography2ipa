# Tsonga (Xitsonga) (`ts`)

<!-- atlas:summary begin -->
Tsonga (Xitsonga) is a Bantu language, written in the Latin script. Glottolog places it in Eswatini, Mozambique, South Africa and Zimbabwe. The `ts` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ts` |
| ISO 639-3 | [tso](https://iso639-3.sil.org/code/tso), Tsonga |
| Glottolog | [tson1249](https://glottolog.org/resource/languoid/id/tson1249), Tsonga |
| Wikidata | [Q34327](https://www.wikidata.org/wiki/Q34327) |
| Wikipedia | [Tsonga language](https://en.wikipedia.org/wiki/Tsonga_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Eswatini](by-region.md#eswatini), [Mozambique](by-region.md#mozambique), [South Africa](by-region.md#south-africa), [Zimbabwe](by-region.md#zimbabwe) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Bantu](https://tigregotico.github.io/orthography2ipa/#x-clade-narr1281) `x-clade-narr1281` |
| Explorer | [`ts` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ts) |
| Spec file | [`ts.json`](../../orthography2ipa/data/ts.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Tsonga (Xitsonga). Bantu language spoken in southern Mozambique, Limpopo and Mpumalanga (South Africa), Zimbabwe, and Eswatini. ~7 million speakers, official language of South Africa. KEY FEATURES: (1) FIVE-VOWEL SYSTEM: a/e/i/o/u, e=[ɛ], o=[ɔ]. (2) PRENASALIZED STOPS: mb/nd, phonemic word-initial sequences.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1967 to 1994. [Sources](#sources) lists them. The spec file writes all 44 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ts.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ts` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-cuenod1967"></a>Cuenod, R. (1967). *Tsonga-English Dictionary*. Swiss Mission.
2. <a id="src-baumbach1987"></a>Baumbach, E.J.M. (1987). *Analytical Tsonga Grammar*. University of South Africa.
3. <a id="src-louwrens1994"></a>Louwrens, L.J. (1994). *Dictionary of Northern Sotho Grammatical Terms*. Via Afrika.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ |  |
| Affricate |  |  | dz ts tɬ | dʒ |  |  |  |
| Nasal | m m̩ |  | n nʷ n̩ |  | ɲ | ŋ |  |
| Trill |  |  | r r̤ |  |  |  |  |
| Fricative |  | f v | s | ʃ |  |  | h |
| Lateral fricative |  |  | ɬ |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [bv] [dl] [mb] [nd] [ndz] [nts] [ps] [sw] [w] [ŋk] [ŋw] [ŋɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | word final [a] |
| ⟨b⟩ | [b] |  |
| ⟨bv⟩ | [bv] |  |
| ⟨d⟩ | [d] |  |
| ⟨dl⟩ | [dl] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨hl⟩ | [ɬ] |  |
| ⟨i⟩ | [i] | word final [i] |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] | word final [k] |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] | word initial [m] [m̩] |
| ⟨mb⟩ | [mb] | word initial [mb] |
| ⟨n⟩ | [n] | word initial [n] [n̩] |
| ⟨n'w⟩ | [ŋw] |  |
| ⟨nd⟩ | [nd] | word initial [nd] |
| ⟨ndz⟩ | [ndz] |  |
| ⟨ng⟩ | [ŋ] | word final [ŋ] · word initial [ŋɡ] |
| ⟨nk⟩ | [ŋk] | word initial [ŋk] |
| ⟨nts⟩ | [nts] |  |
| ⟨nw⟩ | [nʷ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] | word final [p] |
| ⟨ph⟩ | [pʰ] |  |
| ⟨ps⟩ | [ps] |  |
| ⟨r⟩ | [r] |  |
| ⟨rh⟩ | [r̤] |  |
| ⟨s⟩ | [s] |  |
| ⟨sw⟩ | [sw] |  |
| ⟨t⟩ | [t] | word final [t] |
| ⟨th⟩ | [tʰ] |  |
| ⟨tl⟩ | [tɬ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [u] | word final [u] |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [j] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ts")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tosk Albanian](als.md) · [Home](../index.md) · [Tswana →](tn.md)
