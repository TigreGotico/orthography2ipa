# Dongxiang (`sce`)

<!-- atlas:summary begin -->
Dongxiang is a Mongolic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `sce` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sce` |
| ISO 639-3 | [sce](https://iso639-3.sil.org/code/sce), Dongxiang |
| Wikipedia | [Dongxiang language](https://en.wikipedia.org/wiki/Dongxiang_language) |
| Family | [Mongolic](by-family.md#mongolic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Mongolic (family node)](https://tigregotico.github.io/orthography2ipa/#xgn) `xgn` |
| Explorer | [`sce` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sce) |
| Spec file | [`sce.json`](../../orthography2ipa/data/sce.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Dongxiang (autonym Santa) is a Mongolic language of Gansu, written here in the experimental Pinyin-based romanization of A Yibulaheimai and A Shelefu (2001), which is the orthography Kim's description transcribes and the one the shipped gold uses.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2003 to 2024. [Sources](#sources) lists them. The spec file writes all 45 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sce.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sce` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sce_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Dongxiang (dong1285)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/dong1285)
2. <a id="src-sce_kim2003"></a>Kim, Stephen S. (2003). *Santa*. in Janhunen, J. (ed.), The Mongolic Languages, Routledge. Cited: 346-363. DOI [10.4324/9780203987919](https://doi.org/10.4324/9780203987919)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sce` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 168 | 0.0640 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | t tʰ |  |  | k kʰ | q qʰ |  |
| Affricate |  |  | ts tsʰ |  | tɕ tɕʰ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f | s | ʂ | ɕ | x | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u ɯ |
| Close-mid |  |  | o |
| Mid |  | ə |  |
| Open |  |  | ɑ |

Sequences that the spec writes as one unit: [jo] [ju] [jɑ] [jɑw] [jə] [nk] [tʂ] [tʂʰ] [w] [wɑ] [wɑj] [wəj] [ɑj] [ɑw] [əj] [əw].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨ai⟩ | [ɑj] |  |
| ⟨ao⟩ | [ɑw] |  |
| ⟨b⟩ | [p] |  |
| ⟨c⟩ | [tsʰ] |  |
| ⟨ch⟩ | [tʂʰ] |  |
| ⟨d⟩ | [t] |  |
| ⟨e⟩ | [ə] |  |
| ⟨ei⟩ | [əj] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [k] |  |
| ⟨gh⟩ | [q] |  |
| ⟨gv⟩ | [ʁ] |  |
| ⟨h⟩ | [x] |  |
| ⟨hh⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [jɑ] |  |
| ⟨iao⟩ | [jɑw] |  |
| ⟨ie⟩ | [jə] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [ju] |  |
| ⟨j⟩ | [tɕ] |  |
| ⟨k⟩ | [kʰ] |  |
| ⟨kh⟩ | [qʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] | before vowel [nk] · default [ŋ] |
| ⟨o⟩ | [o] |  |
| ⟨ou⟩ | [əw] |  |
| ⟨p⟩ | [pʰ] |  |
| ⟨q⟩ | [tɕʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʂ] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wɑ] |  |
| ⟨uai⟩ | [wɑj] |  |
| ⟨ui⟩ | [wəj] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ɕ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [ts] |  |
| ⟨zh⟩ | [tʂ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 1 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `SCE_UVULAR_BACKING_I` | /i/ → [ɯ], after [q] [qʰ] [ʁ] | - | Kim 2003 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sce")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Dominican Spanish](es-DO.md) · [Home](../index.md) · [Duala →](dua.md)
