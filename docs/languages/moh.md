# Mohawk (`moh`)

<!-- atlas:summary begin -->
Mohawk is an Iroquoian language, written in the Latin script. Glottolog places it in Canada and United States. The `moh` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `moh` |
| ISO 639-3 | [moh](https://iso639-3.sil.org/code/moh), Mohawk |
| Glottolog | [moha1258](https://glottolog.org/resource/languoid/id/moha1258), Mohawk |
| Wikidata | [Q13339](https://www.wikidata.org/wiki/Q13339) |
| Wikipedia | [Mohawk language](https://en.wikipedia.org/wiki/Mohawk_language) |
| Family | [Iroquoian](by-family.md#iroquoian) |
| Region | [North America](by-region.md#north-america) > [Canada](by-region.md#canada), [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Iroquoian](https://tigregotico.github.io/orthography2ipa/#x-clade-iroq1247) `x-clade-iroq1247` |
| Explorer | [`moh` in the data explorer](https://tigregotico.github.io/orthography2ipa/#moh) |
| Spec file | [`moh.json`](../../orthography2ipa/data/moh.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Mohawk (Kanien'kéha), Northern Iroquoian.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1973 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 22 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/moh.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `moh` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mohawk_wiki"></a>Wikipedia contributors (2026). *Mohawk language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Mohawk_language)
2. <a id="src-bonvillain1973"></a>Bonvillain, Nancy (1973). *A Grammar of Akwesasne Mohawk*. National Museum of Man Mercury Series, Ethnology Division Paper No. 8 (Canadian Museum of History).
3. <a id="src-michelson1988"></a>Michelson, Karin (1988). *A Comparative Study of Lake-Iroquoian Accent*. Kluwer Academic Publishers.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 24 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | d t |  |  | k ɡ | ʔ |
| Affricate |  | dʒ |  |  |  |
| Nasal | n |  |  |  |  |
| Trill | r |  |  |  |  |
| Fricative | s z |  |  |  | h |
| Approximant |  |  | j |  |  |
| Lateral approximant | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | ũ |
| Close-mid | e eː | o oː |
| Open-mid |  | ʌ̃ |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨en⟩ | [ʌ̃] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨on⟩ | [ũ] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [dʒ] |  |
| ⟨tsy⟩ | [dʒ] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "moh")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Modern Greek](el.md) · [Home](../index.md) · [Moksha →](mdf.md)
