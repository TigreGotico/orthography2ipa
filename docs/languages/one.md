# Oneida (`one`)

<!-- atlas:summary begin -->
Oneida is an Iroquoian language, written in the Latin script. Glottolog places it in Canada and United States. The `one` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `one` |
| ISO 639-3 | [one](https://iso639-3.sil.org/code/one), Oneida |
| Glottolog | [onei1249](https://glottolog.org/resource/languoid/id/onei1249), Oneida |
| Wikidata | [Q857858](https://www.wikidata.org/wiki/Q857858) |
| Wikipedia | [Oneida language](https://en.wikipedia.org/wiki/Oneida_language) |
| Family | [Iroquoian](by-family.md#iroquoian) |
| Region | [North America](by-region.md#north-america) > [Canada](by-region.md#canada), [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Iroquoian](https://tigregotico.github.io/orthography2ipa/#x-clade-iroq1247) `x-clade-iroq1247` |
| Explorer | [`one` in the data explorer](https://tigregotico.github.io/orthography2ipa/#one) |
| Spec file | [`one.json`](../../orthography2ipa/data/one.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Oneida (Onʌyoteʔa·ka), a Northern Iroquoian language of Wisconsin, Ontario and New York.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2006 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 17 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/one.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `one` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-oneida_wiki"></a>Wikipedia contributors (2025). *Oneida language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Oneida_language)
2. <a id="src-abbott2006"></a>Abbott, Clifford (2006). *Oneida Teaching Grammar, Part I: Sounds and the alphabet*. University of Wisconsin-Green Bay, Oneida Language program. Cited: 6-8. [uwgb.edu](https://www.uwgb.edu/UWGBCMS/media/Oneida-Language/files/PartI.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 17 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|
| Plosive | t |  | k kʷ | ʔ |
| Affricate | ts |  |  |  |
| Nasal | n |  |  |  |
| Fricative | s |  |  | h |
| Approximant |  | j |  |  |
| Lateral approximant | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | ũ |
| Close-mid | e |  | o |
| Mid |  | ə̃ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨e⟩ | [e] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨l⟩ | [l] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [ũ] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ʌ⟩ | [ə̃] |  |
| ⟨ʔ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "one")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Omani Arabic](acx-OM.md) · [Home](../index.md) · [Oromo →](om.md)
