# Cayuga (`cay`)

<!-- atlas:summary begin -->
Cayuga is an Iroquoian language, written in the Latin script. Glottolog places it in Canada and United States. The `cay` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `cay` |
| ISO 639-3 | [cay](https://iso639-3.sil.org/code/cay), Cayuga |
| Glottolog | [cayu1261](https://glottolog.org/resource/languoid/id/cayu1261), Cayuga |
| Wikidata | [Q32967](https://www.wikidata.org/wiki/Q32967) |
| Wikipedia | [Cayuga language](https://en.wikipedia.org/wiki/Cayuga_language) |
| Family | [Iroquoian](by-family.md#iroquoian) |
| Region | [North America](by-region.md#north-america) > [Canada](by-region.md#canada), [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Iroquoian](https://tigregotico.github.io/orthography2ipa/#x-clade-iroq1247) `x-clade-iroq1247` |
| Explorer | [`cay` in the data explorer](https://tigregotico.github.io/orthography2ipa/#cay) |
| Spec file | [`cay.json`](../../orthography2ipa/data/cay.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cayuga (Gayogo̱hó꞉nǫʼ), a Northern Iroquoian language of Six Nations of the Grand River, Ontario.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2024 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 19 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/cay.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `cay` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-cayuga_wiki"></a>Wikipedia contributors (2025). *Cayuga language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Cayuga_language)
2. <a id="src-dyck_etal2024"></a>Dyck, Carrie, Froman, Frances, Keye, Alfred and Keye, Lottie (2024). *A grammar and dictionary of Gayogo̱hó:nǫˀ (Cayuga)*. Language Science Press. Cited: 13-17, 29-30. [zenodo.org](https://zenodo.org/records/10473483/files/398-dyck-2024.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 18 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | t |  |  | k | ʔ |
| Affricate | ts | tʃ |  |  |  |
| Nasal | n |  |  |  |  |
| Fricative | s | ʃ |  |  | h |
| Approximant | ɹ |  | j |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i |  |
| Close-mid | e | o õ |
| Open-mid | ɛ̃ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨d⟩ | [t] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [k] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ts] |  |
| ⟨k⟩ | [k] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨r⟩ | [ɹ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ę⟩ | [ɛ̃] |  |
| ⟨ǫ⟩ | [õ] |  |
| ⟨ˀ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 2 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `CAY_TS_PALATALIZE` | /ts/ → [tʃ], before a front vowel | - | - |
| `CAY_S_PALATALIZE` | /s/ → [ʃ], before [i] [j] [ɹ] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "cay")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Catalan](ca.md) · [Home](../index.md) · [Cebuano →](ceb.md)
