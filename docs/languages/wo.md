# Wolof (`wo`)

<!-- atlas:summary begin -->
Wolof is an Atlantic-Congo language, written in the Latin script. Glottolog places it in 5 countries. The `wo` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `wo` |
| ISO 639-3 | [wol](https://iso639-3.sil.org/code/wol), Wolof |
| Glottolog | [nucl1347](https://glottolog.org/resource/languoid/id/nucl1347), Wolof |
| Wikidata | [Q34257](https://www.wikidata.org/wiki/Q34257) |
| Wikipedia | [Wolof language](https://en.wikipedia.org/wiki/Wolof_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Gambia](by-region.md#gambia), [Guinea-Bissau](by-region.md#guinea-bissau), [Mali](by-region.md#mali), [Mauritania](by-region.md#mauritania), [Senegal](by-region.md#senegal) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1971, living |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`wo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#wo) |
| Spec file | [`wo.json`](../../orthography2ipa/data/wo.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Wolof, the main language of Senegal (also Gambia, Mauritania). The official Latin orthography (Senegalese decree, latest revision 2005) is close to one-to-one with the phonemes: ⟨c⟩ = palatal /c/, ⟨j⟩ = /ɟ/, ⟨ñ⟩ = /ɲ/, ⟨ŋ⟩ = /ŋ/, ⟨x⟩ = /x/, ⟨q⟩ = uvular /q/ (always geminate-like), ⟨y⟩ = /j/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1994 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 33 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/wo.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `wo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-senegal2005"></a>République du Sénégal (2005). *Décret n° 2005-992 relatif à l'orthographe et la séparation des mots en wolof*. Journal Officiel de la République du Sénégal.
2. <a id="src-ka1994"></a>Ka, Omar (1994). *Wolof Phonology and Morphology*. University Press of America.
3. <a id="src-wolof_wiki"></a>Wikipedia contributors (2024). *Wolof language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Wolof_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 38 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c ɟ | k ɡ | q qː |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f | s |  |  | x | χ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Near-open |  | ɐ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [mb] [nd] [w] [ŋɡ] [ɲɟ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɐ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [c] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ɟ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨nj⟩ | [ɲɟ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨à⟩ | [a] |  |
| ⟨é⟩ | [e] |  |
| ⟨ë⟩ | [ə] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ŋ⟩ | [ŋ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "wo")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Wiyot](wiy.md) · [Home](../index.md) · [Wu Chinese →](wuu-Latn-wugniu.md)
