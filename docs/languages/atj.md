# Atikamekw (`atj`)

<!-- atlas:summary begin -->
Atikamekw is an Algic language, written in the Latin script. Glottolog places it in Canada. The `atj` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `atj` |
| ISO 639-3 | [atj](https://iso639-3.sil.org/code/atj), Atikamekw |
| Glottolog | [atik1240](https://glottolog.org/resource/languoid/id/atik1240), Atikamekw |
| Wikidata | [Q56590](https://www.wikidata.org/wiki/Q56590) |
| Wikipedia | [Atikamekw language](https://en.wikipedia.org/wiki/Atikamekw_language) |
| Family | [Algic](by-family.md#algic) |
| Region | [North America](by-region.md#north-america) > [Canada](by-region.md#canada) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Algic](https://tigregotico.github.io/orthography2ipa/#x-clade-algi1248) `x-clade-algi1248` |
| Explorer | [`atj` in the data explorer](https://tigregotico.github.io/orthography2ipa/#atj) |
| Spec file | [`atj.json`](../../orthography2ipa/data/atj.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Atikamekw (Atikamekw Nehiromowin), Algonquian (Cree) language of Quebec, written in a Latin orthography (not syllabics, unlike most Cree varieties). ⟨c⟩ = /ʃ/ and ⟨tc⟩ = /tʃ/, ⟨r⟩ is a tap, the reflex of Proto-Algonquian *l which gives Atikamekw its 'r-dialect' character.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1978 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 19 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/atj.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `atj` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-beland1978"></a>Béland, Jean-Pierre (1978). *Atikamekw Morphology and Lexicon*. University of California, Berkeley (PhD thesis).
2. <a id="src-atikamekw_wiki"></a>Wikipedia contributors (2025). *Atikamekw language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Atikamekw_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 19 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  | k |  |
| Affricate |  |  | tʃ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Tap |  | ɾ |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː |  |
| Close-mid | eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨c⟩ | [ʃ] |  |
| ⟨e⟩ | [eː] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tc⟩ | [tʃ] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨â⟩ | [aː] |  |
| ⟨î⟩ | [iː] |  |
| ⟨ô⟩ | [oː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "atj")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Atayal](tay.md) · [Home](../index.md) · [Atong →](aot.md)
