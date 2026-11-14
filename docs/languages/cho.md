# Choctaw (`cho`)

<!-- atlas:summary begin -->
Choctaw is a Muskogean language, written in the Latin script. Glottolog places it in United States. The `cho` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `cho` |
| ISO 639-3 | [cho](https://iso639-3.sil.org/code/cho), Choctaw |
| Glottolog | [choc1276](https://glottolog.org/resource/languoid/id/choc1276), Choctaw |
| Wikidata | [Q32979](https://www.wikidata.org/wiki/Q32979) |
| Wikipedia | [Choctaw language](https://en.wikipedia.org/wiki/Choctaw_language) |
| Family | [Muskogean](by-family.md#muskogean) |
| Region | [North America](by-region.md#north-america) > [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Muskogean](https://tigregotico.github.io/orthography2ipa/#x-clade-musk1252) `x-clade-musk1252` |
| Explorer | [`cho` in the data explorer](https://tigregotico.github.io/orthography2ipa/#cho) |
| Spec file | [`cho.json`](../../orthography2ipa/data/cho.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Choctaw (Chahta anumpa), Muskogean language of Oklahoma and Mississippi, written in the Latin script, with three vowel qualities /i o a/, each contrasting short/long and oral/nasal (Broadwell 2006, A Choctaw Reference Grammar).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2006 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 28 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/cho.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `cho` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-broadwell2006"></a>Broadwell, George Aaron (2006). *A Choctaw Reference Grammar*. University of Nebraska Press.
2. <a id="src-choctaw_wiki"></a>Wikipedia contributors (2025). *Choctaw language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Choctaw_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `cho` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 140 | 0.3381 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | t |  |  | k |  |
| Affricate |  |  |  | tʃ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Fricative |  | f | s | ʃ |  |  | h |
| Lateral fricative |  |  | ɬ |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː ĩː |  |  |
| Near-close | ɪ |  | ʊ |
| Close-mid |  |  | o oː õː |
| Mid |  | ə |  |
| Open | a aː ãː |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨a̱⟩ | [ãː] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨e⟩ | [ɪ] |  |
| ⟨f⟩ | [f] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨i̱⟩ | [ĩː] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [ɬ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] [ʊ] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨o̱⟩ | [õː] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨v⟩ | [ə] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ʋ⟩ | [ə] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 5 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `CHO_NASAL_a_PRECONSONANTAL` | /a/ → [ãː], before ⟨n⟩ ⟨m⟩, with more context in the spec | - | [Broadwell 2006](#src-broadwell2006) |
| `CHO_NASAL_i_PRECONSONANTAL` | /i ɪ/ → [ĩː], before ⟨n⟩ ⟨m⟩, with more context in the spec | - | - |
| `CHO_NASAL_o_PRECONSONANTAL` | /o ʊ/ → [õː], before ⟨n⟩ ⟨m⟩, with more context in the spec | - | - |
| `CHO_NASAL_n_ABSORBED` | /n/ → ∅, after a vowel, before [b] [tʃ] [f] [h] [k] [l] [ɬ] [p] and 5 more | - | [Broadwell 2006](#src-broadwell2006) |
| `CHO_NASAL_m_ABSORBED` | /m/ → ∅, after a vowel, before [b] [tʃ] [f] [h] [k] [l] [ɬ] [p] and 5 more | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "cho")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Chistabín Aragonese](an-x-chistau.md) · [Home](../index.md) · [Chukot →](ckt.md)
