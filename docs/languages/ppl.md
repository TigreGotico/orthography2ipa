# Nawat (`ppl`)

<!-- atlas:summary begin -->
Nawat is an Uto-Aztecan language, written in the Latin script. Glottolog places it in El Salvador. The `ppl` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ppl` |
| ISO 639-3 | [ppl](https://iso639-3.sil.org/code/ppl), Central American Nawat |
| Glottolog | [pipi1250](https://glottolog.org/resource/languoid/id/pipi1250), Pipil |
| Wikidata | [Q1186896](https://www.wikidata.org/wiki/Q1186896) |
| Wikipedia | [Nawat language](https://en.wikipedia.org/wiki/Nawat_language) |
| Family | [Uto-Aztecan](by-family.md#uto-aztecan) |
| Region | [North America](by-region.md#north-america) > [El Salvador](by-region.md#el-salvador) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Uto-Aztecan](https://tigregotico.github.io/orthography2ipa/#x-clade-utoa1244) `x-clade-utoa1244` |
| Explorer | [`ppl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ppl) |
| Spec file | [`ppl.json`](../../orthography2ipa/data/ppl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Nawat (Pipil), Uto-Aztecan (Nahuan) language of El Salvador. This spec uses the IRIN / Alan King orthography (Iniciativa de Recuperación del Idioma Nawat), the practical standard for revitalisation materials: ⟨kw⟩ = /kʷ/, ⟨tz⟩ = /ts/, ⟨ch⟩ = /tʃ/, ⟨sh⟩ = /ʃ/, ⟨j⟩ = /h/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1985 to 2025. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 18 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ppl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ppl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-campbell1985"></a>Campbell, Lyle (1985). *The Pipil Language of El Salvador*. Mouton de Gruyter.
2. <a id="src-king2004"></a>King, Alan R. (2004). *Gramática elemental del náhuat*. IRIN, El Salvador.
3. <a id="src-nawat_grammar_wiki"></a>Wikipedia contributors (2025). *Nawat grammar*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Nawat_grammar)
4. <a id="src-nawat_wiki"></a>Wikipedia contributors (2025). *Nawat language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Nawat_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ppl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 185 | 0.1322 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 18 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  | k kʷ |  |
| Affricate |  | ts | tʃ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e |  |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨e⟩ | [e] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [h] |  |
| ⟨k⟩ | [k] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tz⟩ | [ts] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ppl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Navajo](nv.md) · [Home](../index.md) · [Ndonga →](ng.md)
