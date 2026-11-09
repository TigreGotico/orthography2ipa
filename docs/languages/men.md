# Mende (`men`)

<!-- atlas:summary begin -->
Mende is a Mande language, written in the Latin script. Glottolog places it in Guinea, Liberia and Sierra Leone. The `men` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `men` |
| ISO 639-3 | [men](https://iso639-3.sil.org/code/men), Mende (Sierra Leone) |
| Glottolog | [mend1266](https://glottolog.org/resource/languoid/id/mend1266), Mende (Sierra Leone) |
| Wikidata | [Q1478672](https://www.wikidata.org/wiki/Q1478672) |
| Wikipedia | [Mende language](https://en.wikipedia.org/wiki/Mende_language) |
| Family | [Mande](by-family.md#mande) |
| Region | [Africa](by-region.md#africa) > [Guinea](by-region.md#guinea), [Liberia](by-region.md#liberia), [Sierra Leone](by-region.md#sierra-leone) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Mande](https://tigregotico.github.io/orthography2ipa/#x-clade-mand1469) `x-clade-mand1469` |
| Explorer | [`men` in the data explorer](https://tigregotico.github.io/orthography2ipa/#men) |
| Spec file | [`men.json`](../../orthography2ipa/data/men.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Mende, Southwestern Mande, spoken by ~2.5 million people as a major lingua franca of southern Sierra Leone (also Liberia, Guinea).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1969 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 26 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/men.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `men` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-innes1969"></a>Innes, Gordon (1969). *A Mende Grammar*. School of Oriental and African Studies, University of London.
2. <a id="src-mende_wiki"></a>Wikipedia contributors (2026). *Mende language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Mende_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 31 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ |  |  |  |
| Nasal | m |  | n |  | ɲ |  |  |
| Fricative |  | f v | s |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [kp] [mb] [nd] [w] [ŋɡ] [ŋɡb] [ɡb] [ɲdʒ].
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
| ⟨gb⟩ | [ɡb] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kp⟩ | [kp] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɛ⟩ | [ɛ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "men")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Meitei](mni.md) · [Home](../index.md) · [Mexican Spanish →](es-MX-x-costa.md)
