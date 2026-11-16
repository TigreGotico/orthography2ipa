# Tetelcingo Nahuatl (`nhg`)

<!-- atlas:summary begin -->
Tetelcingo Nahuatl is an Uto-Aztecan language, written in the Latin script. Glottolog places it in the North America macroarea. The `nhg` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nhg` |
| ISO 639-3 | [nhg](https://iso639-3.sil.org/code/nhg), Tetelcingo Nahuatl |
| Wikipedia | [Tetelcingo Nahuatl](https://en.wikipedia.org/wiki/Tetelcingo_Nahuatl) |
| Family | [Uto-Aztecan](by-family.md#uto-aztecan) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nahuatl](https://tigregotico.github.io/orthography2ipa/#nah) `nah` |
| Explorer | [`nhg` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nhg) |
| Spec file | [`nhg.json`](../../orthography2ipa/data/nhg.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Uto-Aztecan (Nahuan) variety of central Mexico written in a Classical-style Spanish-based orthography. Digraphs tl=[tɬ], tz=[ts], ch=[tʃ], x=[ʃ], cu/hu for labiovelar/[w] and qu=[k] are mapped.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1979 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 24 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nhg.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nhg` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-nhg_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Tetelcingo Nahuatl (tete1251)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/tete1251)
2. <a id="src-nhg_orthography"></a>Wikipedia contributors (2024). *Tetelcingo Nahuatl, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Tetelcingo_Nahuatl)
3. <a id="src-nhg_tuggy1979"></a>Tuggy, David H. (1979). *Tetelcingo Nahuatl*. in Modern Aztec Grammatical Sketches (Studies in Uto-Aztecan Grammar), SIL. [scholars.sil.org](https://scholars.sil.org/sites/scholars/files/david_h_tuggy/publications/dissertation/dtuggy-dissertation-cg-nhg.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nhg` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 295 | 0.2367 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 21 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  | k kʷ | ʔ |
| Affricate |  | ts tɬ | tʃ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
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
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨cu⟩ | [kʷ] |  |
| ⟨e⟩ | [e] |  |
| ⟨h⟩ | [h] |  |
| ⟨hu⟩ | [w] |  |
| ⟨i⟩ | [i] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [k] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tl⟩ | [tɬ] |  |
| ⟨tz⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [s] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nhg")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ternate](tft.md) · [Home](../index.md) · [Tetum →](tet.md)
