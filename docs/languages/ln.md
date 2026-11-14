# Lingala (`ln`)

<!-- atlas:summary begin -->
Lingala is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Central African Republic, Congo - Brazzaville and Congo - Kinshasa. The `ln` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ln` |
| ISO 639-3 | [lin](https://iso639-3.sil.org/code/lin), Lingala |
| Glottolog | [ling1263](https://glottolog.org/resource/languoid/id/ling1263), Kinshasa Lingala |
| Wikidata | [Q36217](https://www.wikidata.org/wiki/Q36217) |
| Wikipedia | [Lingala](https://en.wikipedia.org/wiki/Lingala) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Central African Republic](by-region.md#central-african-republic), [Congo - Brazzaville](by-region.md#congo---brazzaville), [Congo - Kinshasa](by-region.md#congo---kinshasa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`ln` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ln) |
| Spec file | [`ln.json`](../../orthography2ipa/data/ln.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lingala (lingála), Bantu lingua franca of the Congo river basin. Literary Lingala has a seven-vowel system /a e ɛ i o ɔ u/ written with the IPA letters ⟨ɛ ɔ⟩, spoken Lingala reduces this to five. Prenasalised sequences are written ⟨mb mp nd ng nk ns nt nz⟩ and ⟨gb⟩ is the labial-velar /ɡ͡b/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1963 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 53 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ln.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ln` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-lingala_wiki"></a>Wikipedia contributors (2026). *Lingala*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lingala)
2. <a id="src-redden1963"></a>Redden, James E., Bongo, F. (1963). *Lingala Basic Course (Foreign Service Institute Basic Course Series)*. Foreign Service Institute, U.S. Department of State (public domain, livelingua.com mirror). Cited: xi-xiv. [livelingua.com](https://www.livelingua.com/fsi/FSI%20-%20Lingala%20Basic%20Course%20-%20Student%20Text.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Nasal | m |  | n |  | ɲ |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [mb] [mp] [nd] [ns] [nt] [nz] [w] [ŋk] [ŋɡ] [ɡ͡b].
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
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨mp⟩ | [mp] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨ns⟩ | [ns] |  |
| ⟨nt⟩ | [nt] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨nz⟩ | [nz] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨á⟩ | [a] |  |
| ⟨â⟩ | [a] |  |
| ⟨é⟩ | [e] |  |
| ⟨ê⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨î⟩ | [i] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ô⟩ | [o] |  |
| ⟨ú⟩ | [u] |  |
| ⟨û⟩ | [u] |  |
| ⟨ě⟩ | [e] |  |
| ⟨ǎ⟩ | [a] |  |
| ⟨ǐ⟩ | [i] |  |
| ⟨ǒ⟩ | [o] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɔ́⟩ | [ɔ] |  |
| ⟨ɔ̂⟩ | [ɔ] |  |
| ⟨ɛ⟩ | [ɛ] |  |
| ⟨ɛ́⟩ | [ɛ] |  |
| ⟨ɛ̂⟩ | [ɛ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ln")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Limburgish](li-x-rheindok.md) · [Home](../index.md) · [Lingua Franca Nova →](lfn.md)
