# Tyap (`kcg`)

<!-- atlas:summary begin -->
Tyap is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Nigeria. The `kcg` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kcg` |
| ISO 639-3 | [kcg](https://iso639-3.sil.org/code/kcg), Tyap |
| Glottolog | [tyap1238](https://glottolog.org/resource/languoid/id/tyap1238), Tyap |
| Wikidata | [Q3912765](https://www.wikidata.org/wiki/Q3912765) |
| Wikipedia | [Tyap](https://en.wikipedia.org/wiki/Tyap) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Nigeria](by-region.md#nigeria) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`kcg` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kcg) |
| Spec file | [`kcg.json`](../../orthography2ipa/data/kcg.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Tyap (a̱lyem Tyap), a Plateau (Atlantic-Congo) language cluster of southern Kaduna State, Nigeria. ORTHOGRAPHY: Latin script.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1992 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 43 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kcg.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kcg` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-tyap_wiki"></a>Wikipedia contributors (2026). *Tyap*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Tyap)
2. <a id="src-follingstad1992"></a>Follingstad, Carl (1992). *Zhwunzhwuo A̱lyem A̱ Tyap*. Tyap Literacy Committee & Nigeria Bible Translation Trust. Cited: 4-43.
3. <a id="src-akau2014"></a>Akau, Kambai T. L. (2014). *A̱lyem Tyap: Tyap dictionary*. Tyap Literacy Committee. Cited: xxiv-xxix.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 41 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | d͡z t͡s | d͡ʒ t͡ʃ t͡ʃʲ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s | ʃ ʃʲ ʒʲ | ç | x ɣ ɣʲ ɣʷ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Near-close | ɪ |  |  |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [k͡p] [w] [ɡ͡b] [ʍ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨a̱⟩ | [ə] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [t͡ʃ] |  |
| ⟨ch⟩ | [t͡ʃ] |  |
| ⟨chy⟩ | [t͡ʃʲ] |  |
| ⟨cy⟩ | [t͡ʃʲ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨gh⟩ | [ɣ] |  |
| ⟨ghw⟩ | [ɣʷ] |  |
| ⟨ghy⟩ | [ɣʲ] |  |
| ⟨h⟩ | [h] |  |
| ⟨hw⟩ | [ʍ] |  |
| ⟨hy⟩ | [ç] |  |
| ⟨i⟩ | [i] |  |
| ⟨i̱⟩ | [ɪ] |  |
| ⟨j⟩ | [d͡ʒ] |  |
| ⟨jhy⟩ | [ʒʲ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [x] |  |
| ⟨kp⟩ | [k͡p] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨shy⟩ | [ʃʲ] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [t͡s] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [d͡z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kcg")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Twi](tw.md) · [Home](../index.md) · [Ubykh →](uby.md)
