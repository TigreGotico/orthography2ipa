# Turkmen (`tk`)

<!-- atlas:summary begin -->
Turkmen is a Turkic language, written in the Latin script. Glottolog places it in 8 countries. The `tk` spec is at the research tier. It cites 2 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tk` |
| ISO 639-3 | [tuk](https://iso639-3.sil.org/code/tuk), Turkmen |
| Glottolog | [turk1304](https://glottolog.org/resource/languoid/id/turk1304), Turkmen |
| Wikidata | [Q9267](https://www.wikidata.org/wiki/Q9267) |
| Wikipedia | [Turkmen language](https://en.wikipedia.org/wiki/Turkmen_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Afghanistan](by-region.md#afghanistan), [Iran](by-region.md#iran), [Iraq](by-region.md#iraq), [Pakistan](by-region.md#pakistan), [Tajikistan](by-region.md#tajikistan), [Turkmenistan](by-region.md#turkmenistan), [Türkiye](by-region.md#türkiye), [Uzbekistan](by-region.md#uzbekistan) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1993, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`tk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tk) |
| Spec file | [`tk.json`](../../orthography2ipa/data/tk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Turkmen in the Latin alphabet official since 1993.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1998 to 2004. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-gray2004"></a>Gray, David (2004). *A Short Descriptive Grammar of the Turkmen Language*. SIL-NEG, Cheltenham. Cited: 5-7. [archive.org](https://archive.org/details/032-turkmen)
2. <a id="src-johanson_csato1998"></a>Johanson, L. & Csátó, É. Á. (eds.) (1998). *The Turkic Languages*. Routledge. Cited: 261-272.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `tk` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 424 | 0.2316 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `tk` | generated | epitran-derived | CC0 1.0 | 5881 | 0.1629 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative |  | f | ð θ | s z | ʃ ʒ |  | ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Near-open | æ æː |  |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɣ] · word initial [ɡ] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [θ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [ɯ] |  |
| ⟨z⟩ | [ð] |  |
| ⟨ä⟩ | [æː] |  |
| ⟨ç⟩ | [tʃ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |
| ⟨ý⟩ | [j] |  |
| ⟨ň⟩ | [ŋ] |  |
| ⟨ş⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Turkish](tr.md) · [Home](../index.md) · [Turoyo →](tru.md)
