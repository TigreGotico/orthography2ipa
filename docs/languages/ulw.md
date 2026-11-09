# Ulwa (`ulw`)

<!-- atlas:summary begin -->
Ulwa is a Misumalpan language, written in the Latin script. Glottolog places it in the North America macroarea. The `ulw` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ulw` |
| ISO 639-3 | [ulw](https://iso639-3.sil.org/code/ulw), Ulwa (Nicaragua) |
| Wikipedia | [Ulwa language](https://en.wikipedia.org/wiki/Ulwa_language) |
| Family | [Misumalpan](by-family.md#misumalpan) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Misumalpan](https://tigregotico.github.io/orthography2ipa/#x-clade-misu1242) `x-clade-misu1242` |
| Explorer | [`ulw` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ulw) |
| Spec file | [`ulw.json`](../../orthography2ipa/data/ulw.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Misumalpan (Southern Sumu) language of Karawala, Nicaragua, in the practical orthography of the Ulwa dictionary. Three vowel qualities a/i/u each contrast for length (written doubled), ng is the velar nasal. Stress is predictable (first syllable if heavy, otherwise second) and so is not written.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1999 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 20 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ulw.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ulw` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ulw_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Ulwa (ulwa1239)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/ulwa1239)
2. <a id="src-ulw_wikipedia"></a>Wikipedia contributors (2024). *Ulwa language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ulwa_language)
3. <a id="src-ulw_green1999"></a>Green, Thomas Michael (1999). *A Lexicographic Study of Ulwa*. PhD dissertation, MIT. [tmgreen.github.io](https://tmgreen.github.io/papers/thesis.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ulw` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 102 | 0.0888 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 20 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  | k |  |
| Nasal | m | n |  | ŋ |  |
| Trill |  | r |  |  |  |
| Fricative |  | s |  |  | h |
| Approximant |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ulw")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ukrainian](uk.md) · [Home](../index.md) · [Umbrian dialect →](it-IT-x-umbria.md)
