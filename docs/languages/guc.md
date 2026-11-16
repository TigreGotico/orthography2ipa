# Wayuu (`guc`)

<!-- atlas:summary begin -->
Wayuu is an Arawakan language, written in the Latin script. Glottolog places it in Colombia and Venezuela. The `guc` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `guc` |
| ISO 639-3 | [guc](https://iso639-3.sil.org/code/guc), Wayuu |
| Glottolog | [wayu1243](https://glottolog.org/resource/languoid/id/wayu1243), Wayuu |
| Wikidata | [Q891085](https://www.wikidata.org/wiki/Q891085) |
| Wikipedia | [Wayuu language](https://en.wikipedia.org/wiki/Wayuu_language) |
| Family | [Arawakan](by-family.md#arawakan) |
| Region | [South America](by-region.md#south-america) > [Colombia](by-region.md#colombia), [Venezuela](by-region.md#venezuela) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Arawakan](https://tigregotico.github.io/orthography2ipa/#x-clade-araw1281) `x-clade-araw1281` |
| Explorer | [`guc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#guc) |
| Spec file | [`guc.json`](../../orthography2ipa/data/guc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Wayuu (wayuunaiki), Arawakan language of the Guajira Peninsula (Colombia and Venezuela). Latin orthography standardised for bilingual education. Six vowel qualities /i ɛ ɨ a u ɔ/ (⟨i e ü a u o⟩), each with a long counterpart written by doubling. Plosives and nasals lengthen (geminate), written double: pp tt kk mm nn.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1994 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/guc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `guc` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-alvarez1994"></a>Álvarez, José (1994). *Estudios de lingüística guajira*. Secretaría de Cultura del Estado Zulia, Maracaibo.
2. <a id="src-guc_wiki"></a>Wikipedia contributors (2024). *Wayuu language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Wayuu_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 30 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pː | t tː |  |  | k kː | ʔ |
| Nasal | m mː | n nː |  |  |  |  |
| Trill |  | r |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ ɨː | u uː |
| Open-mid | ɛ ɛː |  | ɔ ɔː |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨ee⟩ | [ɛː] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [h] |  |
| ⟨k⟩ | [k] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨oo⟩ | [ɔː] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ü⟩ | [ɨ] |  |
| ⟨üü⟩ | [ɨː] |  |
| ⟨ꞌ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "guc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Waurá](wau.md) · [Home](../index.md) · [Welsh →](cy.md)
