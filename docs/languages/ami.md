# Amis (`ami`)

<!-- atlas:summary begin -->
Amis is an Austronesian language, written in the Latin script. Glottolog places it in China. The `ami` spec is at the research tier. It cites 1 source and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ami` |
| ISO 639-3 | [ami](https://iso639-3.sil.org/code/ami), Amis |
| Glottolog | [amis1246](https://glottolog.org/resource/languoid/id/amis1246), Amis |
| Wikidata | [Q35132](https://www.wikidata.org/wiki/Q35132) |
| Wikipedia | [Amis language](https://en.wikipedia.org/wiki/Amis_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [China](by-region.md#china) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Austronesian](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1307) `x-clade-aust1307` |
| Explorer | [`ami` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ami) |
| Spec file | [`ami.json`](../../orthography2ipa/data/ami.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Amis (Pangcah), the largest Formosan (Austronesian) language of Taiwan, written in the official romanised orthography promulgated by Taiwan's Council of Indigenous Peoples. Practical orthography: /ts/ = ⟨c⟩, /j/ = ⟨y⟩, /ʡ/ = ⟨ʼ⟩, /ʔ/ = ⟨^⟩, /ɮ/ = ⟨d⟩, /ŋ/ = ⟨ng⟩, /ʜ/ = ⟨x⟩, /v/ = ⟨f⟩, /ɺ/ = ⟨l⟩.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 1 work, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 24 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ami.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ami` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ami_wiki"></a>Wikipedia contributors (2024). *Amis language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Amis_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  |  | t t̪ |  | k | ʔ |
| Affricate |  |  |  | ts |  |  |  |
| Nasal | m |  |  | n n̪ |  | ŋ |  |
| Trill |  |  |  | r |  |  |  |
| Fricative |  | v | ð | s |  | ɣ | h |
| Lateral fricative |  |  |  | ɮ |  |  |  |
| Approximant |  |  |  |  | j |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w] [ɺ] [ʜ] [ʡ] [ʢ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨^⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [ɮ] |  |
| ⟨e⟩ | [ə] |  |
| ⟨f⟩ | [v] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [ɺ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [u] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʜ] |  |
| ⟨y⟩ | [j] |  |
| ⟨ʼ⟩ | [ʡ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ami")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Amharic](am.md) · [Home](../index.md) · [Ancient Egyptian →](egy.md)
