# Bemba (`bem`)

<!-- atlas:summary begin -->
Bemba is a Bantu language, written in the Latin script. Glottolog places it in Botswana, Congo - Kinshasa, Malawi and Zambia. The `bem` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bem` |
| ISO 639-3 | [bem](https://iso639-3.sil.org/code/bem), Bemba (Zambia) |
| Glottolog | [bemb1257](https://glottolog.org/resource/languoid/id/bemb1257), Bemba (Zambia) |
| Wikidata | [Q33052](https://www.wikidata.org/wiki/Q33052) |
| Wikipedia | [Bemba language](https://en.wikipedia.org/wiki/Bemba_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Botswana](by-region.md#botswana), [Congo - Kinshasa](by-region.md#congo---kinshasa), [Malawi](by-region.md#malawi), [Zambia](by-region.md#zambia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Bantu](https://tigregotico.github.io/orthography2ipa/#x-clade-narr1281) `x-clade-narr1281` |
| Explorer | [`bem` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bem) |
| Spec file | [`bem.json`](../../orthography2ipa/data/bem.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Bemba (Chibemba, Guthrie M.42), Bantu language of the Northern, Luapula and Copperbelt provinces of Zambia. Five vowel qualities a/e/i/o/u with a phonemic length distinction, not marked in the standard orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1972 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 33 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bem.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `bem` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-hamann_kula2015"></a>Hamann, Silke & Kula, Nancy C. (2015). *Bemba (Illustrations of the IPA)*. Journal of the International Phonetic Association 45(1), 61-69. Cited: 61-69. DOI [10.1017/S0025100314000371](https://doi.org/10.1017/S0025100314000371) · [fon.hum.uva.nl](https://www.fon.hum.uva.nl/silke/articles/Hamann&Kula_2015.pdf)
2. <a id="src-givon1972"></a>Givón, T. (1972). *Studies in ChiBemba and Bantu Grammar*. Studies in African Linguistics, Supplement 3.
3. <a id="src-bem_wiki"></a>Wikipedia contributors (2025). *Bemba language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Bemba_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t ⁿd ⁿt |  |  | k ɡ |
| Affricate |  |  |  | tʃ ⁿdʒ ⁿtʃ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |
| Fricative | β | f | s ⁿs | ʃ ⁿʃ |  |  |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w] [ᵐb] [ᵐp] [ᵑk] [ᵑɡ] [ᶬf].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] |  |
| ⟨mf⟩ | [ᶬf] |  |
| ⟨mp⟩ | [ᵐp] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ⁿd] |  |
| ⟨ndj⟩ | [ⁿdʒ] |  |
| ⟨ng⟩ | [ᵑɡ] |  |
| ⟨ng'⟩ | [ŋ] |  |
| ⟨nk⟩ | [ᵑk] |  |
| ⟨ns⟩ | [ⁿs] |  |
| ⟨nsh⟩ | [ⁿʃ] |  |
| ⟨nt⟩ | [ⁿt] |  |
| ⟨ntsh⟩ | [ⁿtʃ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bem")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Belsetán Aragonese](an-x-belsetan.md) · [Home](../index.md) · [Benasquese →](an-x-benasque.md)
