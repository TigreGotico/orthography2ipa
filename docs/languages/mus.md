# Muscogee (`mus`)

<!-- atlas:summary begin -->
Muscogee is a Muskogean language, written in the Latin script. Glottolog places it in United States. The `mus` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mus` |
| ISO 639-3 | [mus](https://iso639-3.sil.org/code/mus), Creek |
| Glottolog | [cree1270](https://glottolog.org/resource/languoid/id/cree1270), Creek |
| Wikidata | [Q523014](https://www.wikidata.org/wiki/Q523014) |
| Wikipedia | [Muscogee language](https://en.wikipedia.org/wiki/Muscogee_language) |
| Family | [Muskogean](by-family.md#muskogean) |
| Region | [North America](by-region.md#north-america) > [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1835, living |
| Parent | [Muskogean](https://tigregotico.github.io/orthography2ipa/#x-clade-musk1252) `x-clade-musk1252` |
| Explorer | [`mus` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mus) |
| Spec file | [`mus.json`](../../orthography2ipa/data/mus.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Muscogee / Creek (Mvskoke), Muskogean language of Oklahoma, written in the Latin script with the traditional Creek alphabet. Two orthographic conventions deserve note: ⟨c⟩ = /tʃ/ and ⟨r⟩ = the voiceless lateral fricative /ɬ/ (not a rhotic). ⟨v⟩ is the short central vowel /ə ~ a/ and ⟨ē⟩ the long /iː/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2011 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 20 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mus.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mus` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-martin2011"></a>Martin, Jack B. (2011). *A Grammar of Creek (Muskogee)*. University of Nebraska Press.
2. <a id="src-muscogee_wiki"></a>Wikipedia contributors (2025). *Muscogee language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Muscogee_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 21 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t |  |  | k |  |
| Affricate |  |  |  | tʃ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Fricative |  | f | s |  |  |  | h |
| Lateral fricative |  |  | ɬ |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː |  |  |
| Near-close | ɪ |  | ʊ |
| Close-mid |  |  | o |
| Mid |  | ə |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w] [ɛj].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [aː] [a] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨e⟩ | [ɪ] |  |
| ⟨f⟩ | [f] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɛj] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɬ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨v⟩ | [ə] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ē⟩ | [iː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mus")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Murui Huitoto](huu.md) · [Home](../index.md) · [Māori →](mi.md)
