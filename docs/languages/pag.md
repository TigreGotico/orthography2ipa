# Pangasinan (`pag`)

<!-- atlas:summary begin -->
Pangasinan is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in Philippines. The `pag` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pag` |
| ISO 639-3 | [pag](https://iso639-3.sil.org/code/pag), Pangasinan |
| Glottolog | [pang1290](https://glottolog.org/resource/languoid/id/pang1290), Pangasinan |
| Wikipedia | [Pangasinan language](https://en.wikipedia.org/wiki/Pangasinan_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Philippines](by-region.md#philippines) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`pag` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pag) |
| Spec file | [`pag.json`](../../orthography2ipa/data/pag.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Pangasinan (Salitan Pangasinan), Northern Luzon (Malayo-Polynesian) language of the Philippines. Latin orthography: the 26 basic Latin letters plus the digraph ⟨ng⟩ /ŋ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1971 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 25 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pag.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pag` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-pangasinan_language_wiki"></a>Wikipedia contributors (2026). *Pangasinan language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Pangasinan_language)
2. <a id="src-benton1971"></a>Benton, Richard A. (1971). *Pangasinan Reference Grammar (PALI Language Texts: Philippines)*. University of Hawaii Press (open access edition, CC BY-NC-SA, ScholarSpace). Cited: 3, 14-15, 35-37. [scholarspace.manoa.hawaii.edu](https://scholarspace.manoa.hawaii.edu/bitstreams/e912e166-fdcc-47af-a8c2-165dbabf89d8/download)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `pag` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 227 | 0.1277 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 26 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  |  | k ɡ | ʔ |
| Affricate |  |  | dʒ tʃ |  |  |  |
| Nasal | m | n |  |  | ŋ |  |
| Tap |  | ɾ |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid |  |  | o |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] [ɨ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ë⟩ | [ɨ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pag")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Panamanian Spanish](es-PA.md) · [Home](../index.md) · [Pannonian Rusyn →](rsk.md)
