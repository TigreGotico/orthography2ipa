# Kotava (`avk`)

<!-- atlas:summary begin -->
Kotava is a Constructed language, written in the Latin script. Glottolog places it in United States. The `avk` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `avk` |
| ISO 639-3 | [avk](https://iso639-3.sil.org/code/avk), Kotava |
| Glottolog | [kota1280](https://glottolog.org/resource/languoid/id/kota1280), Kotava |
| Wikidata | [Q1377116](https://www.wikidata.org/wiki/Q1377116) |
| Wikipedia | [Kotava](https://en.wikipedia.org/wiki/Kotava) |
| Family | [Constructed](by-family.md#constructed) |
| Region | [North America](by-region.md#north-america) > [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1978, living |
| Explorer | [`avk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#avk) |
| Spec file | [`avk.json`](../../orthography2ipa/data/avk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kotava, constructed international auxiliary language created by Staren Fetcey (1978, published 1993). Fully phonemic Latin orthography: one letter = one phoneme, 24 letters (⟨h⟩ and ⟨q⟩ are not used). ⟨c⟩ = /ʃ/, ⟨j⟩ = /ʒ/, ⟨x⟩ = /x/, ⟨y⟩ = /j/ (also palatalising).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2016 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 24 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/avk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `avk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-fetcey_grammaka"></a>Fetcey, Staren (2016). *Grammaka ke Kotava (official grammar of Kotava)*. Comité linguistique kotava (Kotava.org). [kotava.org](https://www.kotava.org/)
2. <a id="src-kotava_wiki"></a>Wikipedia contributors (2024). *Kotava*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kotava)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 24 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Nasal | m |  | n |  |  |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "avk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Korean](ko.md) · [Home](../index.md) · [Kpelle →](kpe.md)
