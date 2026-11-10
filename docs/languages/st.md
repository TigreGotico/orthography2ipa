# Southern Sotho (Sesotho) (`st`)

<!-- atlas:summary begin -->
Southern Sotho (Sesotho) is a Bantu language, written in the Latin script. Glottolog places it in Lesotho and South Africa. The `st` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `st` |
| ISO 639-3 | [sot](https://iso639-3.sil.org/code/sot), Southern Sotho |
| Glottolog | [sout2807](https://glottolog.org/resource/languoid/id/sout2807), Southern Sotho |
| Wikipedia | [Sotho language](https://en.wikipedia.org/wiki/Sotho_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Lesotho](by-region.md#lesotho), [South Africa](by-region.md#south-africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1830, living |
| Parent | [Bantu](https://tigregotico.github.io/orthography2ipa/#x-clade-narr1281) `x-clade-narr1281` |
| Explorer | [`st` in the data explorer](https://tigregotico.github.io/orthography2ipa/#st) |
| Spec file | [`st.json`](../../orthography2ipa/data/st.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Southern Sotho (Sesotho), a Sotho-Tswana (Bantu) language of Lesotho and South Africa. INPUT CONTRACT: this spec implements the SOUTH AFRICAN standard orthography (the one used in South African publications and described as the main system in the Wikipedia 'Sesotho orthography' article), NOT the Lesotho orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1957 to 2025. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/st.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `st` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sesotho_orthography_wiki"></a>Wikipedia contributors (2024). *Sesotho orthography*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Sesotho_orthography)
2. <a id="src-sesotho_phonology_wiki"></a>Wikipedia contributors (2025). *Sesotho phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Sesotho_phonology)
3. <a id="src-doke_mofokeng1957"></a>Doke, C.M. & Mofokeng, S.M. (1957). *Textbook of Southern Sotho Grammar*. Longmans, Green & Co., Cape Town.
4. <a id="src-demuth1995sesotho"></a>Demuth, K. (1995). *Sesotho*. In: Encyclopedia of Language and Linguistics / Bantu descriptive sketches.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b pʰ pʼ |  | d tʰ tʼ |  |  | kʰ kʼ |  |  |
| Affricate |  |  | tsʰ tsʼ tɬʼ t͡ɬʰ | dʒ t͡ʃʰ t͡ʃʼ |  |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |  |
| Fricative |  | f | s | ʃ ʒ |  | x | ʁ | h ɦ |
| Lateral fricative |  |  | ɬ |  |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Near-close | ɪ | ʊ |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open |  | ɑ |

Sequences that the spec writes as one unit: [bʒ] [fʃ] [pʃʰ] [pʃʼ] [w] [ǃ] [ǃʰ] [ᵑǃ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨bj⟩ | [bʒ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] [e] [ɪ] |  |
| ⟨f⟩ | [f] |  |
| ⟨fj⟩ | [fʃ] |  |
| ⟨h⟩ | [ɦ] [h] |  |
| ⟨hl⟩ | [ɬ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] [ʒ] |  |
| ⟨k⟩ | [kʼ] |  |
| ⟨kg⟩ | [x] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nq⟩ | [ᵑǃ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] [o] [ʊ] |  |
| ⟨p⟩ | [pʼ] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨pj⟩ | [pʃʼ] |  |
| ⟨pjh⟩ | [pʃʰ] |  |
| ⟨q⟩ | [ǃ] |  |
| ⟨qh⟩ | [ǃʰ] |  |
| ⟨r⟩ | [ʁ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [tʼ] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨tj⟩ | [t͡ʃʼ] |  |
| ⟨tjh⟩ | [t͡ʃʰ] |  |
| ⟨tl⟩ | [tɬʼ] |  |
| ⟨tlh⟩ | [t͡ɬʰ] |  |
| ⟨ts⟩ | [tsʼ] |  |
| ⟨tsh⟩ | [tsʰ] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "st")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Southern Russian](ru-x-southern.md) · [Home](../index.md) · [Southern Yukaghir →](yux.md)
