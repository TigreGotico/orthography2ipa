# Chamorro (`ch`)

<!-- atlas:summary begin -->
Chamorro is an Austronesian language, written in the Latin script. Glottolog places it in Guam and Northern Mariana Islands. The `ch` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ch` |
| ISO 639-3 | [cha](https://iso639-3.sil.org/code/cha), Chamorro |
| Glottolog | [cham1312](https://glottolog.org/resource/languoid/id/cham1312), Chamorro |
| Wikidata | [Q33262](https://www.wikidata.org/wiki/Q33262) |
| Wikipedia | [Chamorro language](https://en.wikipedia.org/wiki/Chamorro_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Guam](by-region.md#guam), [Northern Mariana Islands](by-region.md#northern-mariana-islands) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Malayo-Polynesian (family node)](https://tigregotico.github.io/orthography2ipa/#poz) `poz` |
| Explorer | [`ch` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ch) |
| Spec file | [`ch.json`](../../orthography2ipa/data/ch.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Chamorro (Chamoru), Mariana Islands. Official orthography (Guam/CNMI orthography commissions): <å> = /ɑ/ vs <a> = /æ/, <ch> = /ts/, <y> = /dz/, <ñ> = /ɲ/, <ng> = /ŋ/, glottal stop written with an apostrophe.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1973 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 25 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ch.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ch` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-topping1973"></a>Topping, Donald M. (1973). *Chamorro Reference Grammar*. University of Hawaii Press.
2. <a id="src-chamorro_wiki"></a>Wikipedia contributors (2024). *Chamorro language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Chamorro_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 24 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ | ʔ |
| Affricate |  |  | dz ts |  |  |  |
| Nasal | m |  | n | ɲ | ŋ |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative |  | f | s |  |  | h |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Near-open | æ |  |
| Open |  | ɑ |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [æ] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨y⟩ | [dz] |  |
| ⟨å⟩ | [ɑ] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ʼ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ch")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Chadian Arabic](shu-TD.md) · [Home](../index.md) · [Chavacano →](cbk-PH.md)
