# Waurá (`wau`)

<!-- atlas:summary begin -->
Waurá is an Arawakan language, written in the Latin script. Glottolog places it in the North America and South America macroareas. The `wau` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `wau` |
| ISO 639-3 | [wau](https://iso639-3.sil.org/code/wau), Waurá |
| Wikipedia | [Waurá language](https://en.wikipedia.org/wiki/Waur%C3%A1_language) |
| Family | [Arawakan](by-family.md#arawakan) |
| Region | [North America](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Arawakan](https://tigregotico.github.io/orthography2ipa/#x-clade-araw1281) `x-clade-araw1281` |
| Explorer | [`wau` in the data explorer](https://tigregotico.github.io/orthography2ipa/#wau) |
| Spec file | [`wau.json`](../../orthography2ipa/data/wau.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Arawakan language of the Upper Xingu, Brazil. Published sources give the phonology but not a fully settled official spelling, so the grapheme choices (ts, tx/ch, ü for the high central vowel) follow typical Xinguan Arawakan practice and are skeleton tier. Long vowels contrast and are written doubled.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 24 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/wau.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `wau` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wau_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Waurá (waur1244)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/waur1244)
2. <a id="src-wau_wikipedia"></a>Wikipedia contributors (2024). *Waurá language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Waur%C3%A1_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `wau` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 146 | 0.2968 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 23 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  |  | k | ɢ |  |
| Affricate |  | ts | tʃ |  |  |  |  |  |
| Nasal | m | n |  |  |  |  |  |  |
| Tap |  | ɾ |  |  |  |  |  |  |
| Fricative |  | s |  | ʐ |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ | u uː |
| Close-mid | e eː |  |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨g⟩ | [ɢ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [ɾ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ʐ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tx⟩ | [tʃ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ü⟩ | [ɨ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "wau")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Waray](war.md) · [Home](../index.md) · [Wayuu →](guc.md)
