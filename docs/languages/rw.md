# Kinyarwanda (`rw`)

<!-- atlas:summary begin -->
Kinyarwanda is a Bantu language, written in the Latin script. Glottolog places it in 5 countries. The `rw` spec is at the research tier. It cites 1 source and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `rw` |
| ISO 639-3 | [kin](https://iso639-3.sil.org/code/kin), Kinyarwanda |
| Glottolog | [kiny1244](https://glottolog.org/resource/languoid/id/kiny1244), Kinyarwanda |
| Wikidata | [Q33573](https://www.wikidata.org/wiki/Q33573) |
| Wikipedia | [Kinyarwanda](https://en.wikipedia.org/wiki/Kinyarwanda) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Burundi](by-region.md#burundi), [Congo - Kinshasa](by-region.md#congo---kinshasa), [Rwanda](by-region.md#rwanda), [Tanzania](by-region.md#tanzania), [Uganda](by-region.md#uganda) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Bantu](https://tigregotico.github.io/orthography2ipa/#x-clade-narr1281) `x-clade-narr1281` |
| Explorer | [`rw` in the data explorer](https://tigregotico.github.io/orthography2ipa/#rw) |
| Spec file | [`rw.json`](../../orthography2ipa/data/rw.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kinyarwanda (Rwanda national language). Bantu language. Prenasalized consonants are single phonemes. High tone vs. low tone, not marked in standard orthography. C/CY = /tʃ/, SH = /ʃ/, NY = /ɲ/. Grapheme table checked against Kimenyi (1980): no discrepancy found.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 1980. [Sources](#sources) lists them. The spec file writes all 35 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/rw.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `rw` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kimenyi1980"></a>Kimenyi, Alexandre (1980). *A Relational Grammar of Kinyarwanda*. University of California Publications in Linguistics, vol. 91. University of California Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `rw` | generated | epitran-derived | CC0 1.0 | 381086 | 0.1388 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [mb] [mp] [nd] [ndʒ] [nt] [w] [ŋk] [ŋɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨cy⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨jy⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨mp⟩ | [mp] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨nj⟩ | [ndʒ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nt⟩ | [nt] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "rw")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kildin Sami](sjd.md) · [Home](../index.md) · [Kirundi →](rn.md)
