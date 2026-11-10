# Lushootseed (`lut`)

<!-- atlas:summary begin -->
Lushootseed is a Salishan language, written in the Latin script. Glottolog places it in the North America macroarea. The `lut` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lut` |
| ISO 639-3 | [lut](https://iso639-3.sil.org/code/lut), Lushootseed |
| Wikipedia | [Lushootseed](https://en.wikipedia.org/wiki/Lushootseed) |
| Family | [Salishan](by-family.md#salishan) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Salishan](https://tigregotico.github.io/orthography2ipa/#x-clade-sali1255) `x-clade-sali1255` |
| Explorer | [`lut` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lut) |
| Spec file | [`lut.json`](../../orthography2ipa/data/lut.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Salishan language of Puget Sound, Washington, written in a near-phonemic Americanist orthography. Symbols are close to IPA: č=[tʃ], c=[ts], š=[ʃ], ƛ=[tɬ], ɬ, x̌=[χ], and labialized kʷ/xʷ/gʷ/qʷ are mapped, with ʔ for glottal stop.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1994 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 30 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lut.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lut` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-lut_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Northern Lushootseed (lush1252)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/lush1252)
2. <a id="src-bates_hess_hilbert1994"></a>Bates, Dawn, Hess, Thom, Hilbert, Vi (1994). *Lushootseed Dictionary*. University of Washington Press.
3. <a id="src-lut_orthography"></a>Wikipedia contributors (2024). *Lushootseed, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lushootseed)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `lut` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 135 | 0.2259 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 30 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  |  | k kʷ ɡ ɡʷ | q qʷ | ʔ |
| Affricate |  | ts tɬ | tʃ |  |  |  |  |
| Nasal | m | n |  |  |  |  |  |
| Fricative |  | s | ʃ |  | xʷ | χ | h |
| Lateral fricative |  | ɬ |  |  |  |  |  |
| Approximant |  |  |  | j |  |  |  |
| Lateral approximant |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w] [ʼ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gʷ⟩ | [ɡʷ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨kʷ⟩ | [kʷ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨qʷ⟩ | [qʷ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨xʷ⟩ | [xʷ] |  |
| ⟨x̌⟩ | [χ] |  |
| ⟨y⟩ | [j] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ƛ⟩ | [tɬ] |  |
| ⟨ə⟩ | [ə] |  |
| ⟨ɬ⟩ | [ɬ] |  |
| ⟨ʔ⟩ | [ʔ] |  |
| ⟨ʼ⟩ | [ʼ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lut")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Luganda](lg.md) · [Home](../index.md) · [Luxembourgish →](lb.md)
