# Nias (`nia`)

<!-- atlas:summary begin -->
Nias is an Austronesian language, written in the Latin script. Glottolog places it in Indonesia. The `nia` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nia` |
| ISO 639-3 | [nia](https://iso639-3.sil.org/code/nia), Nias |
| Glottolog | [nias1242](https://glottolog.org/resource/languoid/id/nias1242), Nias |
| Wikidata | [Q2407831](https://www.wikidata.org/wiki/Q2407831) |
| Wikipedia | [Nias language](https://en.wikipedia.org/wiki/Nias_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Indonesia](by-region.md#indonesia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Malayo-Polynesian (family node)](https://tigregotico.github.io/orthography2ipa/#poz) `poz` |
| Explorer | [`nia` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nia) |
| Spec file | [`nia.json`](../../orthography2ipa/data/nia.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Nias (Li Niha), Barrier Islands off Sumatra, Indonesia. Latin orthography: six vowels including <ö> = /ɤ/, <ŵ> = /w/ while <w>/<v> spell the labiodental /v ~ ʋ/, <mb> and <ndr> are prenasalised/trilled-release units, <kh> = /x/, apostrophe = glottal stop. Every syllable is open (CV).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2001 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 29 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nia.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nia` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-brown2001"></a>Brown, Lea (2001). *A Grammar of Nias Selatan*. PhD thesis, University of Sydney.
2. <a id="src-nias_wiki"></a>Wikipedia contributors (2024). *Nias language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Nias_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 31 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b |  | d t |  |  | k ɡ | ʔ |
| Affricate |  |  |  | tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill | ʙ |  | r |  |  |  |  |
| Fricative |  | f v | s z |  |  | x | h |
| Approximant |  | ʋ |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o ɤ |
| Open | a |  |

Sequences that the spec writes as one unit: [dʳ] [w] [ᵐb] [ⁿdʳ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [x] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] |  |
| ⟨n⟩ | [n] |  |
| ⟨ndr⟩ | [ⁿdʳ] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [v] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ö⟩ | [ɤ] |  |
| ⟨ŵ⟩ | [w] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nia")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nheengatu](yrl.md) · [Home](../index.md) · [Nicaraguan Spanish →](es-NI.md)
