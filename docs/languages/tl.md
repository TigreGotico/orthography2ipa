# Tagalog (`tl`)

<!-- atlas:summary begin -->
Tagalog is an Austronesian language, written in the Latin script. Glottolog places it in Philippines. The `tl` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tl` |
| ISO 639-3 | [tgl](https://iso639-3.sil.org/code/tgl), Tagalog |
| Glottolog | [taga1270](https://glottolog.org/resource/languoid/id/taga1270), Tagalog |
| Wikidata | [Q34057](https://www.wikidata.org/wiki/Q34057) |
| Wikipedia | [Tagalog language](https://en.wikipedia.org/wiki/Tagalog_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Philippines](by-region.md#philippines) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1593, living |
| Parent | [Proto-Malayo-Polynesian (family node)](https://tigregotico.github.io/orthography2ipa/#poz) `poz` |
| Explorer | [`tl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tl) |
| Spec file | [`tl.json`](../../orthography2ipa/data/tl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Filipino/Tagalog standard orthography (Abakada + expanded 28-letter alphabet). Glottal stop /ʔ/ is phonemic but unwritten (word-initial vowels, mid-word, and some finals). Word-final K → [ʔ]. Intervocalic D → [ɾ]. NG = /ŋ/ (single phoneme, alphabetized as unit). Stress marked with tilde (˜) in formal texts.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1972 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 27 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL.

1. <a id="src-schachter_otanes1972"></a>Schachter, P. & Otanes, F.T. (1972). *Tagalog Reference Grammar*. University of California Press.
2. <a id="src-tagalog_phonology_wiki"></a>Wikipedia contributors (2024). *Tagalog phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Tagalog_phonology)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `tl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 25857 | 0.1179 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 29 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | ʔ |
| Affricate |  |  |  | dʒ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative | β | f v | s z |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Near-close |  | ʊ |
| Close-mid | e | o |
| Open-mid | ɛ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [ks] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [s] |  |
| ⟨d⟩ | [d] | default [d] · intervocalic [ɾ] |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] | default [k] · word final [ʔ] |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [s] [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ta'izzi-Adeni Arabic](acq.md) · [Home](../index.md) · [Tahitian →](ty.md)
