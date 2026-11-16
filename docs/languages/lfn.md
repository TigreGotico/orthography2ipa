# Lingua Franca Nova (`lfn`)

<!-- atlas:summary begin -->
Lingua Franca Nova is a Constructed language, written in the Latin script. Glottolog places it in United States. The `lfn` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lfn` |
| ISO 639-3 | [lfn](https://iso639-3.sil.org/code/lfn), Lingua Franca Nova |
| Glottolog | [ling1267](https://glottolog.org/resource/languoid/id/ling1267), Lingua Franca Nova |
| Wikidata | [Q146803](https://www.wikidata.org/wiki/Q146803) |
| Wikipedia | [Lingua Franca Nova](https://en.wikipedia.org/wiki/Lingua_Franca_Nova) |
| Family | [Constructed](by-family.md#constructed) |
| Region | [North America](by-region.md#north-america) > [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1998, living |
| Explorer | [`lfn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lfn) |
| Spec file | [`lfn.json`](../../orthography2ipa/data/lfn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lingua Franca Nova (elefen), constructed auxiliary language created by C. George Boeree (1998), Romance lexicon with a creole-like grammar. Fully regular phonemic orthography: 22 Latin letters (k, q, w, y are used only in proper names). ⟨c⟩ is always [k], ⟨x⟩ is [ʃ], ⟨j⟩ is [ʒ].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1998 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 22 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lfn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lfn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-boeree1998"></a>Boeree, C. George (1998). *Lingua Franca Nova*. Shippensburg University. [elefen.org](https://elefen.org/)
2. <a id="src-lingua_franca_nova_wiki"></a>Wikipedia contributors (2026). *Lingua Franca Nova*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lingua_Franca_Nova)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 26 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

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
| ⟨c⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
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
| ⟨x⟩ | [ʃ] |  |
| ⟨z⟩ | [z] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lfn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lingala](ln.md) · [Home](../index.md) · [Lithuanian →](lt.md)
