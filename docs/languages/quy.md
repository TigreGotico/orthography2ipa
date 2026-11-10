# Ayacucho Quechua (`quy`)

<!-- atlas:summary begin -->
Ayacucho Quechua is a Quechuan language, written in the Latin script. Glottolog places it in Peru. The `quy` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `quy` |
| ISO 639-3 | [quy](https://iso639-3.sil.org/code/quy), Ayacucho Quechua |
| Glottolog | [ayac1239](https://glottolog.org/resource/languoid/id/ayac1239), Ayacucho Quechua |
| Wikidata | [Q35145](https://www.wikidata.org/wiki/Q35145) |
| Wikipedia | [Ayacucho Quechua](https://en.wikipedia.org/wiki/Ayacucho_Quechua) |
| Family | [Quechuan](by-family.md#quechuan) |
| Region | [South America](by-region.md#south-america) > [Peru](by-region.md#peru) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Quechua](https://tigregotico.github.io/orthography2ipa/#qu) `qu` |
| Explorer | [`quy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#quy) |
| Spec file | [`quy.json`](../../orthography2ipa/data/quy.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ayacucho (Chanka) Quechua, the Southern Quechua variety of Ayacucho, Peru.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2025. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 18 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/quy.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `quy` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ayacucho_quechua_wiki"></a>Wikipedia contributors (2025). *Ayacucho Quechua*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ayacucho_Quechua)
2. <a id="src-southern_quechua_wiki"></a>Wikipedia contributors (2025). *Southern Quechua*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Southern_Quechua)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 21 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  | k |  |  |
| Affricate |  |  | tʃ |  |  |  |  |
| Nasal | m | n |  | ɲ |  |  |  |
| Trill |  | r |  |  |  |  |  |
| Fricative |  | s |  |  |  | χ | h |
| Approximant |  |  |  | j |  |  |  |
| Lateral approximant |  | l |  | ʎ |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Open-mid | ɛ | ɔ |
| Open | a | ɑ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [χ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ñ⟩ | [ɲ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 6 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `QUY_UVULAR_LOWER_A` | /a/ → [ɑ], before [χ] | - | - |
| `QUY_UVULAR_LOWER_A_AFTER` | /a/ → [ɑ], after [χ] | - | - |
| `QUY_UVULAR_LOWER_I` | /i/ → [ɛ], before [χ] | - | - |
| `QUY_UVULAR_LOWER_I_AFTER` | /i/ → [ɛ], after [χ] | - | - |
| `QUY_UVULAR_LOWER_U` | /u/ → [ɔ], before [χ] | - | - |
| `QUY_UVULAR_LOWER_U_AFTER` | /u/ → [ɔ], after [χ] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "quy")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Avar](av.md) · [Home](../index.md) · [Azerbaijani →](az.md)
