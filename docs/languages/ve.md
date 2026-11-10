# Venda (`ve`)

<!-- atlas:summary begin -->
Venda is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Botswana, South Africa and Zimbabwe. The `ve` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ve` |
| ISO 639-3 | [ven](https://iso639-3.sil.org/code/ven), Venda |
| Glottolog | [vend1245](https://glottolog.org/resource/languoid/id/vend1245), Venda |
| Wikidata | [Q32704](https://www.wikidata.org/wiki/Q32704) |
| Wikipedia | [Venda language](https://en.wikipedia.org/wiki/Venda_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Botswana](by-region.md#botswana), [South Africa](by-region.md#south-africa), [Zimbabwe](by-region.md#zimbabwe) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`ve` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ve) |
| Spec file | [`ve.json`](../../orthography2ipa/data/ve.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Venda (Tshivenḓa), Bantu language of South Africa and Zimbabwe, one of South Africa's official languages. The Latin orthography adds five under-dot/circumflex-below letters (ḓ ḽ ṋ ṱ) for the dental series contrasting with the alveolar d l n t, and ṅ for /ŋ/ (⟨ng⟩ being prenasalised /ŋɡ/).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1996 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 58 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ve.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ve` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ve_wiki"></a>Wikipedia contributors (2024). *Venda language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Venda_language)
2. <a id="src-mulaudzi1996"></a>Mulaudzi, Phalandwa Abraham (1996). *A descriptive analysis of the morphology of the Tshiguvhu dialect of Venda*. University of South Africa MA dissertation (UNISA Institutional Repository). Cited: 14-17. [uir.unisa.ac.za](https://uir.unisa.ac.za/handle/10500/17535)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 63 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b pʰ pʼ |  | d d̪ tʰ tʼ t̪ʰ t̪ʼ |  |  | c | kʰ kʷʰ kʼ ɡ |  |
| Affricate |  | p̪fʰ p̪fʼ | d͡z d͡zʷ t͡sʰ t͡sʷ t͡sʼ | d͡ʒ t͡ʃʰ t͡ʃʼ |  |  |  |  |
| Nasal | m |  | n n̪ |  |  | ɲ | ŋ ŋʷ |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative | ɸ β | f v | s z | ʃ ʒ | ʂ ʐ |  | x xʷ ɣʷ | h hʷ |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l l̪ |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [bj] [bɣʷ] [b̪v] [nd͡z] [w] [ŋɡ] [ɺ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨bv⟩ | [b̪v] |  |
| ⟨bw⟩ | [bɣʷ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dz⟩ | [d͡z] |  |
| ⟨dzh⟩ | [d͡ʒ] |  |
| ⟨dzw⟩ | [d͡zʷ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨fh⟩ | [ɸ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨hw⟩ | [ɣʷ] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [kʼ] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨khw⟩ | [kʷʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨nz⟩ | [nd͡z] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [pʼ] |  |
| ⟨pf⟩ | [p̪fʼ] |  |
| ⟨pfh⟩ | [p̪fʰ] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨sw⟩ | [ʂ] |  |
| ⟨t⟩ | [tʼ] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨ths⟩ | [t͡sʰ] |  |
| ⟨thsh⟩ | [t͡ʃʰ] |  |
| ⟨ts⟩ | [t͡sʼ] |  |
| ⟨tsh⟩ | [t͡ʃʼ] |  |
| ⟨tsw⟩ | [t͡sʷ] |  |
| ⟨ty⟩ | [c] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨vh⟩ | [β] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨xw⟩ | [xʷ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |
| ⟨zw⟩ | [ʐ] |  |
| ⟨ḓ⟩ | [d̪] |  |
| ⟨ḽ⟩ | [l̪] |  |
| ⟨ṅ⟩ | [ŋ] |  |
| ⟨ṅw⟩ | [ŋʷ] |  |
| ⟨ṋ⟩ | [n̪] |  |
| ⟨ṱ⟩ | [t̪ʼ] |  |
| ⟨ṱh⟩ | [t̪ʰ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ve")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Valencian](ca-x-valencia.md) · [Home](../index.md) · [Venetian →](vec.md)
