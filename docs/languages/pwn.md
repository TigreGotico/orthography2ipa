# Paiwan (`pwn`)

<!-- atlas:summary begin -->
Paiwan is an Austronesian language, written in the Latin script. Glottolog places it in China. The `pwn` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pwn` |
| ISO 639-3 | [pwn](https://iso639-3.sil.org/code/pwn), Paiwan |
| Glottolog | [paiw1248](https://glottolog.org/resource/languoid/id/paiw1248), Paiwan |
| Wikidata | [Q715755](https://www.wikidata.org/wiki/Q715755) |
| Wikipedia | [Paiwan language](https://en.wikipedia.org/wiki/Paiwan_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [China](by-region.md#china) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Austronesian](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1307) `x-clade-aust1307` |
| Explorer | [`pwn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pwn) |
| Spec file | [`pwn.json`](../../orthography2ipa/data/pwn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Paiwan (pinayuanan), a Formosan language of southern Taiwan and one of the most conservative Austronesian languages.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2003 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 27 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pwn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pwn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-paiwan_language_wiki"></a>Wikipedia contributors (2026). *Paiwan language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Paiwan_language)
2. <a id="src-early_whitehorn2003"></a>Early, Robert, Whitehorn, John (2003). *One Hundred Paiwan Texts (Pacific Linguistics 542)*. Pacific Linguistics, Australian National University (open access, CC BY-SA 4.0, ANU Open Research). Cited: 14-15. [openresearch-repository.anu.edu.au](https://openresearch-repository.anu.edu.au/items/f5456a54-1139-4eb2-9299-1e7de36fceda)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 28 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | ɖ | c ɟ | k ɡ | q | ʔ |
| Affricate |  |  | ts | tʃ |  |  |  |  |  |
| Nasal | m |  | n |  |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative |  | v | s z |  |  |  |  |  |  |
| Approximant |  |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  | ʎ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dj⟩ | [ɟ] |  |
| ⟨dr⟩ | [ɖ] |  |
| ⟨e⟩ | [ə] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lj⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tj⟩ | [c] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pwn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ottoman Turkish](ota.md) · [Home](../index.md) · [Palenquero →](pln.md)
