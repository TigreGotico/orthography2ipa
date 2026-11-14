# Plains Cree (`crk`)

<!-- atlas:summary begin -->
Plains Cree is an Algic language, written in the Latin script. Glottolog places it in the North America macroarea. The `crk` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `crk` |
| ISO 639-3 | [crk](https://iso639-3.sil.org/code/crk), Plains Cree |
| Wikipedia | [Plains Cree](https://en.wikipedia.org/wiki/Plains_Cree) |
| Family | [Algic](by-family.md#algic) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Cree](cr.md) `cr` |
| Explorer | [`crk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#crk) |
| Spec file | [`crk.json`](../../orthography2ipa/data/crk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Algonquian (Cree) variety of the Canadian plains written in the Standard Roman Orthography. Long vowels carry a circumflex (â ê î ô), c=[ts] (ranging to [tʃ]).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1934 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 17 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/crk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `crk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-crk_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Plains Cree (plai1258)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/plai1258)
2. <a id="src-wolfart1996"></a>Wolfart, H. Christoph (1996). *Sketch of Cree, an Algonquian Language*. In: Ives Goddard (ed.), Handbook of North American Indians, vol. 17: Languages. Smithsonian Institution. [archive.org](https://archive.org/details/rosettaproject_crk_detail-1)
3. <a id="src-bloomfield1934"></a>Bloomfield, Leonard (1934). *Plains Cree Texts*. American Ethnological Society (repr. 1974, AMS Press, New York). [archive.org](https://archive.org/details/rosettaproject_crk_book-1)
4. <a id="src-crk_orthography"></a>Wikipedia contributors (2024). *Plains Cree (Standard Roman Orthography), Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Plains_Cree)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `crk` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 159 | 0.1871 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 17 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  | k |  |
| Affricate |  | ts |  |  |  |
| Nasal | m | n |  |  |  |
| Fricative |  | s |  |  | h |
| Approximant |  |  | j |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | iː |  |
| Near-close | ɪ | ʊ |
| Close-mid | eː | oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨c⟩ | [ts] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ʊ] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨â⟩ | [aː] |  |
| ⟨ê⟩ | [eː] |  |
| ⟨î⟩ | [iː] |  |
| ⟨ô⟩ | [oː] |  |

Stress falls on the antepenult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "crk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Pitjantjatjara](pjt.md) · [Home](../index.md) · [Pnar →](pbv.md)
