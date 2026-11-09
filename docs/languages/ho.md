# Hiri Motu (`ho`)

<!-- atlas:summary begin -->
Hiri Motu is an Austronesian language, written in the Latin script. Glottolog places it in Papua New Guinea. The `ho` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ho` |
| ISO 639-3 | [hmo](https://iso639-3.sil.org/code/hmo), Hiri Motu |
| Glottolog | [hiri1237](https://glottolog.org/resource/languoid/id/hiri1237), Hiri Motu |
| Wikidata | [Q33617](https://www.wikidata.org/wiki/Q33617) |
| Wikipedia | [Hiri Motu](https://en.wikipedia.org/wiki/Hiri_Motu) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Papua New Guinea](by-region.md#papua-new-guinea) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1880, living |
| Parent | [Austronesian](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1307) `x-clade-aust1307` |
| Explorer | [`ho` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ho) |
| Spec file | [`ho.json`](../../orthography2ipa/data/ho.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Hiri Motu (Police Motu), a simplified, pidginised variety of Motu and one of the three official languages of Papua New Guinea. Latin script, phonemic spelling with a five-vowel system /i ɛ a ɔ u/. ⟨v⟩ is the voiced bilabial fricative /β/, ⟨r⟩ is a tap /ɾ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1985 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 19 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ho.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ho` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-dutton1985"></a>Dutton, Tom E. (1985). *Police Motu: iena sivarai (its story)*. University of Papua New Guinea Press.
2. <a id="src-hirimotu_wiki"></a>Wikipedia contributors (2025). *Hiri Motu*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Hiri_Motu)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 19 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|
| Plosive | b p | d t | k ɡ |  |
| Nasal | m | n |  |  |
| Tap |  | ɾ |  |  |
| Fricative | β | s |  | h |
| Lateral approximant |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Open-mid | ɛ | ɔ |
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
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [β] |  |
| ⟨w⟩ | [w] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ho")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hindi](hi.md) · [Home](../index.md) · [Hmong Daw →](mww.md)
