# Tongan (`to`)

<!-- atlas:summary begin -->
Tongan is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in Tonga. The `to` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `to` |
| ISO 639-3 | [ton](https://iso639-3.sil.org/code/ton), Tonga (Tonga Islands) |
| Glottolog | [tong1325](https://glottolog.org/resource/languoid/id/tong1325), Tonga (Tonga Islands) |
| Wikipedia | [Tongan language](https://en.wikipedia.org/wiki/Tongan_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Tonga](by-region.md#tonga) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`to` in the data explorer](https://tigregotico.github.io/orthography2ipa/#to) |
| Spec file | [`to.json`](../../orthography2ipa/data/to.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Tongan (lea faka-Tonga), Polynesian, Kingdom of Tonga.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1953 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 22 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/to.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `to` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-churchward1953"></a>Churchward, C. Maxwell (1953). *Tongan Grammar*. Oxford University Press.
2. <a id="src-tongan_language_wiki"></a>Wikipedia contributors (2024). *Tongan language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Tongan_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 22 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t | k | ʔ |
| Nasal | m |  | n | ŋ |  |
| Fricative |  | f v | s |  | h |
| Lateral approximant |  |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ʻ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "to")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Toki Pona](tok.md) · [Home](../index.md) · [Tosk Albanian →](als.md)
