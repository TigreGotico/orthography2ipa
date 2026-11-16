# Galibi Carib (`car`)

<!-- atlas:summary begin -->
Galibi Carib is a Cariban language, written in the Latin script. Glottolog places it in the South America macroarea. The `car` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `car` |
| ISO 639-3 | [car](https://iso639-3.sil.org/code/car), Galibi Carib |
| Wikipedia | [Carib language](https://en.wikipedia.org/wiki/Carib_language) |
| Family | [Cariban](by-family.md#cariban) |
| Region | [South America](by-region.md#south-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Cariban](https://tigregotico.github.io/orthography2ipa/#x-clade-cari1283) `x-clade-cari1283` |
| Explorer | [`car` in the data explorer](https://tigregotico.github.io/orthography2ipa/#car) |
| Spec file | [`car.json`](../../orthography2ipa/data/car.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Cariban language (Kariña/Kali'na, a.k.a. Galibi Carib) of Venezuela and the Guianas, Latin orthography (Hoff 1968). The grapheme ï (also seen written ɨ in some sources/dictionaries, mapped equivalently) denotes the high central vowel /ɨ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1968 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 30 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/car.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `car` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-car_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Galibi Carib (gali1262)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/gali1262)
2. <a id="src-hoff1968"></a>Hoff, Berend J. (1968). *The Carib Language*. Martinus Nijhoff.
3. <a id="src-courtz2008"></a>Courtz, Henk (2008). *A Carib Grammar and Dictionary*. Magoria Books. Cited: pp. 1, 22, 43-45. [archive.org](https://archive.org/download/caribdictionary/carib%20dictionary.pdf)
4. <a id="src-car_wikipedia"></a>Wikipedia contributors (2024). *Carib language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Carib_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wold` ([lexibank/wold](https://github.com/lexibank/wold)) | `car` | gold | lexicon-derived | CC BY 4.0 | 1191 | 0.1400 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `car` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 232 | 0.3116 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 26 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ | ʔ |
| Nasal | m |  | n |  |  |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative |  | f | s |  |  |  |
| Approximant |  |  |  | j |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Open | a |  |  |

Sequences that the spec writes as one unit: [aʔ] [eʔ] [iʔ] [oʔ] [uʔ] [w] [ɨʔ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨à⟩ | [aʔ] |  |
| ⟨è⟩ | [eʔ] |  |
| ⟨ì⟩ | [iʔ] |  |
| ⟨ï⟩ | [ɨ] |  |
| ⟨ò⟩ | [oʔ] |  |
| ⟨ù⟩ | [uʔ] |  |
| ⟨ɨ⟩ | [ɨ] |  |
| ⟨ʼ⟩ | [ʔ] |  |
| ⟨ỳ⟩ | [ɨʔ] |  |
| ⟨’⟩ | [ʔ] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "car")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Gagauz](gag.md) · [Home](../index.md) · [Galician →](gl-ES.md)
