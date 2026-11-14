# Kikuyu (`ki`)

<!-- atlas:summary begin -->
Kikuyu is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Kenya. The `ki` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ki` |
| ISO 639-3 | [kik](https://iso639-3.sil.org/code/kik), Kikuyu |
| Glottolog | [kiku1240](https://glottolog.org/resource/languoid/id/kiku1240), Kikuyu |
| Wikidata | [Q33587](https://www.wikidata.org/wiki/Q33587) |
| Wikipedia | [Kikuyu language](https://en.wikipedia.org/wiki/Kikuyu_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Kenya](by-region.md#kenya) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`ki` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ki) |
| Spec file | [`ki.json`](../../orthography2ipa/data/ki.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kikuyu (Gĩkũyũ), Bantu language of central Kenya. Seven vowels written with five letters plus the tilde pair ⟨ĩ ũ⟩ for the close-mid /e o/, while plain ⟨e o⟩ are the open-mid /ɛ ɔ/ and ⟨a⟩ is the low CENTRAL /a/ (Englebretson 2015, Figures 2 and 4).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1967 to 2015. [Sources](#sources) lists them. The spec file writes all 34 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ki.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ki` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-englebretson_2015_gikuyu_sketch"></a>Englebretson, Robert (ed.) (2015). *A Basic Sketch Grammar of Gĩkũyũ*. Rice University Field Methods Class. [ruf.rice.edu](https://www.ruf.rice.edu/~reng/kik/sketch.pdf)
2. <a id="src-armstrong1967"></a>Armstrong, Lilias E. (1967). *The Phonetic and Tonal Structure of Kikuyu*. London: Published for the International African Institute by Dawsons of Pall Mall.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ki` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1025 | 0.3914 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 32 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive |  |  | t ⁿd |  |  | k |  |
| Affricate |  |  |  | ⁿdʒ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative | β | ð |  | ʃ |  | ɣ | h |
| Approximant |  |  |  |  | j |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open-mid | ɛ ɛː | ɔ ɔː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w] [ᵐb] [ᵑɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [β] |  |
| ⟨c⟩ | [ʃ] |  |
| ⟨d⟩ | [ð] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨ee⟩ | [ɛː] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ⁿd] |  |
| ⟨ng⟩ | [ᵑɡ] |  |
| ⟨ng'⟩ | [ŋ] |  |
| ⟨nj⟩ | [ⁿdʒ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨oo⟩ | [ɔː] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [ð] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] | after consonant [o] · default [w] |
| ⟨y⟩ | [j] |  |
| ⟨ĩ⟩ | [e] |  |
| ⟨ĩĩ⟩ | [eː] |  |
| ⟨ũ⟩ | [o] |  |
| ⟨ũũ⟩ | [oː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ki")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ki-Nubi](kcn.md) · [Home](../index.md) · [Kildin Sami →](sjd.md)
