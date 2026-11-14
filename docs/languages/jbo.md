# Lojban (`jbo`)

<!-- atlas:summary begin -->
Lojban is a Constructed language, written in the Latin script. Glottolog places it in United States. The `jbo` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `jbo` |
| ISO 639-3 | [jbo](https://iso639-3.sil.org/code/jbo), Lojban |
| Glottolog | [lojb1234](https://glottolog.org/resource/languoid/id/lojb1234), Lojban |
| Wikidata | [Q36350](https://www.wikidata.org/wiki/Q36350) |
| Wikipedia | [Lojban](https://en.wikipedia.org/wiki/Lojban) |
| Family | [Constructed](by-family.md#constructed) |
| Region | [North America](by-region.md#north-america) > [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1987, living |
| Explorer | [`jbo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#jbo) |
| Spec file | [`jbo.json`](../../orthography2ipa/data/jbo.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lojban (la .lojban.), constructed logical language, published by the Logical Language Group (1997 baseline, from Loglan 1955). Fully phonemic orthography: one letter = one phoneme. The apostrophe ⟨'⟩ is a voiceless glide /h/ occurring only between vowels, ⟨y⟩ is the schwa /ə/ used as a buffer/hesitation vowel.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1997 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 24 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/jbo.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `jbo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-cll1997"></a>Cowan, John Woldemar (1997). *The Complete Lojban Language*. Logical Language Group. Cited: Chapter 3 (Orthography and Phonology). [lojban.org](https://lojban.org/publications/cll/)
2. <a id="src-lojban_wiki"></a>Wikipedia contributors (2025). *Lojban*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lojban)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 24 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ |  |
| Nasal | m |  | n |  |  |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | x | h |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid |  |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Open | a |  |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [h] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] |  |
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
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [ə] |  |
| ⟨z⟩ | [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "jbo")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Logudorese Sardinian](src.md) · [Home](../index.md) · [Lolopo →](ycl.md)
