# Silesian (`szl`)

<!-- atlas:summary begin -->
Silesian is a West Slavic language, written in the Latin script. Glottolog places it in Poland. The `szl` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `szl` |
| ISO 639-3 | [szl](https://iso639-3.sil.org/code/szl), Silesian |
| Glottolog | [sile1253](https://glottolog.org/resource/languoid/id/sile1253), Silesian |
| Wikidata | [Q30319](https://www.wikidata.org/wiki/Q30319) |
| Wikipedia | [Silesian language](https://en.wikipedia.org/wiki/Silesian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > West Slavic](by-family.md#indo-european--balto-slavic--slavic--west-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Poland](by-region.md#poland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [West Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2792) `x-clade-west2792` |
| Explorer | [`szl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#szl) |
| Spec file | [`szl.json`](../../orthography2ipa/data/szl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Silesian (Ślůnski), West Slavic variety spoken in Silesia (Poland/Czech Republic). Classification as language vs. Polish dialect debated. Distinctive vowels ô /o/ and the palatal sibilants ś, ź. German loanword influence significant. No single standard orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2023 to 2024. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/szl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `szl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-wiki-szl"></a>Wikipedia contributors (2024). *Silesian language*.
2. <a id="src-jaroszewicz2023"></a>Jaroszewicz, Henryk (2023). *Standardization of the Silesian Language: The Current Status and Prospects for Development*. Poznańskie Studia Polonistyczne. Seria Językoznawcza 30(1), 57-72 (open access). Cited: 61, 65. [doi.org](https://doi.org/10.14746/pspsj.2023.30.1.4)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `szl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2377 | 0.2148 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 38 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | dz ts | dʒ tʃ | dʑ tɕ |  |
| Nasal | m |  | n |  | ɲ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ ʑ | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid |  |  | o oː õ |
| Open-mid | ɛ |  | ɔ |
| Open | a ã |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨ch⟩ | [x] |  |
| ⟨cz⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨dź⟩ | [dʑ] |  |
| ⟨dż⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨rz⟩ | [ʒ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sz⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [v] |  |
| ⟨y⟩ | [ɨ] |  |
| ⟨z⟩ | [z] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨ô⟩ | [o] |  |
| ⟨õ⟩ | [õ] |  |
| ⟨ć⟩ | [tɕ] |  |
| ⟨ł⟩ | [w] |  |
| ⟨ń⟩ | [ɲ] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨ŏ⟩ | [ɔ] |  |
| ⟨ś⟩ | [ɕ] |  |
| ⟨ź⟩ | [ʑ] |  |
| ⟨ż⟩ | [ʒ] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "szl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sidamo](sid.md) · [Home](../index.md) · [Sindhi →](sd.md)
