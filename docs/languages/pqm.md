# Malecite-Passamaquoddy (`pqm`)

<!-- atlas:summary begin -->
Malecite-Passamaquoddy is an Algic language, written in the Latin script. Glottolog places it in the North America macroarea. The `pqm` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pqm` |
| ISO 639-3 | [pqm](https://iso639-3.sil.org/code/pqm), Malecite-Passamaquoddy |
| Wikipedia | [Malecite–Passamaquoddy language](https://en.wikipedia.org/wiki/Malecite%E2%80%93Passamaquoddy_language) |
| Family | [Algic](by-family.md#algic) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Algic](https://tigregotico.github.io/orthography2ipa/#x-clade-algi1248) `x-clade-algi1248` |
| Explorer | [`pqm` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pqm) |
| Spec file | [`pqm.json`](../../orthography2ipa/data/pqm.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Algic (Eastern Algonquian) language of Maine and New Brunswick in the standard Passamaquoddy-Maliseet orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 18 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pqm.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pqm` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-pqm_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Malecite-Passamaquoddy (male1292)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/male1292)
2. <a id="src-pqm_orthography"></a>Wikipedia contributors (2024). *Malecite-Passamaquoddy language, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Malecite%E2%80%93Passamaquoddy_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `pqm` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 151 | 0.1759 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 18 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  | k kʷ | ʔ |
| Affricate |  |  | tʃ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Fricative |  | s |  |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid |  | o |
| Open-mid | ɛ |  |
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
| ⟨c⟩ | [tʃ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [kʷ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pqm")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Maldivian](dv.md) · [Home](../index.md) · [Maltese →](mt.md)
