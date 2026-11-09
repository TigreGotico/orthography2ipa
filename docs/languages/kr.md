# Kanuri (`kr`)

<!-- atlas:summary begin -->
Kanuri is a Nilotic language, written in the Latin script. Glottolog places it in the Africa macroarea. The `kr` spec is at the research tier. It cites 5 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kr` |
| ISO 639-3 | [kau](https://iso639-3.sil.org/code/kau), Kanuri |
| Glottolog | [kanu1279](https://glottolog.org/resource/languoid/id/kanu1279), Kanuri-Kanembu |
| Wikidata | [Q36094](https://www.wikidata.org/wiki/Q36094) |
| Wikipedia | [Kanuri language](https://en.wikipedia.org/wiki/Kanuri_language) |
| Family | [Nilotic](by-family.md#nilotic) |
| Region | [Africa](by-region.md#africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nilotic](https://tigregotico.github.io/orthography2ipa/#x-clade-nilo1247) `x-clade-nilo1247` |
| Explorer | [`kr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kr) |
| Spec file | [`kr.json`](../../orthography2ipa/data/kr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kanuri (Kanuri: Kanuri), Saharan (Nilo-Saharan) language of Borno (Nigeria), Niger, Chad and Cameroon.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 5 works, from 1981 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kr` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kanuri_language_wiki"></a>Wikipedia contributors (2026). *Kanuri language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kanuri_language)
2. <a id="src-hutchison_intro"></a>Hutchison, John P. (1981). *Introduction to the Kanuri Language*. African Studies Center, Boston University. Cited: 5-8. [alma.matrix.msu.edu](https://alma.matrix.msu.edu/assets/uploads/2023/02/ALMA_IntroductionToTheKanuriLanguageEdited2.pdf)
3. <a id="src-cyffer_hutchison1990"></a>Cyffer, Norbert & Hutchison, John P. (1990). *Dictionary of the Kanuri Language*. Foris Publications / University of Maiduguri.
4. <a id="src-cyffer1998"></a>Cyffer, Norbert (1998). *A Sketch of Kanuri*. Rüdiger Köppe Verlag, Köln.
5. <a id="src-retroflex_lateral_flap_wiki"></a>Wikipedia contributors (2026). *Voiced retroflex lateral flap*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Voiced_retroflex_lateral_flap)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  |  | k ɡ | ʔ |
| Affricate |  |  |  | d͡ʒ t͡ʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative | ɸ β | f | s z | ʃ |  |  | ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ɭ ɭ̆ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [mb] [nd] [w] [ŋɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [t͡ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [d͡ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ng⟩ | [ŋɡ] [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ǝ⟩ | [ə] [ɨ] |  |
| ⟨ɍ⟩ | [ɭ̆] [r] |  |
| ⟨ə⟩ | [ə] [ɨ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kannada](kn.md) · [Home](../index.md) · [Kapampangan →](pam.md)
