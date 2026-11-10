# Twi (`tw`)

<!-- atlas:summary begin -->
Twi is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Ghana and Togo. The `tw` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tw` |
| Aliases | `twi` |
| ISO 639-3 | [twi](https://iso639-3.sil.org/code/twi), Twi |
| Glottolog | [akan1250](https://glottolog.org/resource/languoid/id/akan1250), Akan |
| Wikidata | [Q36850](https://www.wikidata.org/wiki/Q36850) |
| Wikipedia | [Twi](https://en.wikipedia.org/wiki/Twi) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Ghana](by-region.md#ghana), [Togo](by-region.md#togo) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Akan (Twi-Fante)](ak.md) `ak` |
| Explorer | [`tw` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tw) |
| Spec file | [`tw.json`](../../orthography2ipa/data/tw.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Twi, the Akan literary standard used in Ashanti, Eastern, and parts of Bono/Bono East/Ahafo regions of Ghana, comprises the Asante and Akuapem sub-varieties.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1988 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes no spelling of its own. It takes all 33 from [Akan (Twi-Fante)](ak.md) `ak`.

The [spec file](../../orthography2ipa/data/tw.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tw` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-twi_language_wiki"></a>Wikipedia contributors (2026). *Twi*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Twi)
2. <a id="src-dolphyne1988"></a>Dolphyne, Florence Abena (1988). *The Akan (Twi-Fante) Language: Its Sound Systems and Tonal Structure*. Ghana Universities Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k kʷ ɡ ɡʷ |  |
| Affricate |  |  |  |  | dʑ dʑʷ tɕ tɕʷ |  |  |
| Nasal | m |  | n |  | ɲ ɲʷ | ŋ ŋʷ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ | ɽ |  |  |  |
| Fricative |  | f | s |  | ɕ ɕʷ |  | h hʷ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Near-close | ɪ |  | ʊ |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Near-open | æ | ɐ |  |
| Open | a |  |  |

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
| ⟨dw⟩ | [ɡʷ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gw⟩ | [ɡʷ] |  |
| ⟨gy⟩ | [dʑ] |  |
| ⟨h⟩ | [h] |  |
| ⟨hw⟩ | [hʷ] |  |
| ⟨hy⟩ | [ɕ] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨ky⟩ | [tɕ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nw⟩ | [ŋʷ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tw⟩ | [kʷ] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɛ⟩ | [ɛ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tw")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tuscan](it-IT-x-toscana.md) · [Home](../index.md) · [Tyap →](kcg.md)
