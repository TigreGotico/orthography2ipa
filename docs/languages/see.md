# Seneca (`see`)

<!-- atlas:summary begin -->
Seneca is an Iroquoian language, written in the Latin script. Glottolog places it in Canada and United States. The `see` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `see` |
| ISO 639-3 | [see](https://iso639-3.sil.org/code/see), Seneca |
| Glottolog | [sene1264](https://glottolog.org/resource/languoid/id/sene1264), Seneca |
| Wikidata | [Q1185133](https://www.wikidata.org/wiki/Q1185133) |
| Wikipedia | [Seneca language](https://en.wikipedia.org/wiki/Seneca_language) |
| Family | [Iroquoian](by-family.md#iroquoian) |
| Region | [North America](by-region.md#north-america) > [Canada](by-region.md#canada), [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Iroquoian](https://tigregotico.github.io/orthography2ipa/#x-clade-iroq1247) `x-clade-iroq1247` |
| Explorer | [`see` in the data explorer](https://tigregotico.github.io/orthography2ipa/#see) |
| Spec file | [`see.json`](../../orthography2ipa/data/see.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Seneca (Onödowáʼga:), Northern Iroquoian, the westernmost of the Five Nations Iroquoian languages. Eight vowels: six oral /i e æ a o u/ (written a ä e i o u, with ⟨ä⟩ for the near-open front vowel) and two nasal /ɛ̃ ɔ̃/ (written with trema, ë ö).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1967 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 23 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/see.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `see` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-seneca_wiki"></a>Wikipedia contributors (2026). *Seneca language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Seneca_language)
2. <a id="src-chafe1967"></a>Chafe, Wallace L. (1967). *Seneca Morphology and Dictionary*. Smithsonian Contributions to Anthropology No. 4.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 23 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | d t |  |  | k ɡ | ʔ |
| Affricate | dz ts | dʒ tʃ |  |  |  |
| Nasal | n |  |  |  |  |
| Fricative | s | ʃ |  |  | h |
| Approximant |  |  | j |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ̃ | ɔ̃ |
| Near-open | æ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨d⟩ | [d] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨ë⟩ | [ɛ̃] |  |
| ⟨ö⟩ | [ɔ̃] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨š⟩ | [ʃ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "see")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sendinês](mwl-x-sendim.md) · [Home](../index.md) · [Senhaja de Srair →](sjs.md)
