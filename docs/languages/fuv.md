# Nigerian Fulfulde (`fuv`)

<!-- atlas:summary begin -->
Nigerian Fulfulde is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Cameroon, Chad and Nigeria. The `fuv` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `fuv` |
| ISO 639-3 | [fuv](https://iso639-3.sil.org/code/fuv), Nigerian Fulfulde |
| Glottolog | [nige1253](https://glottolog.org/resource/languoid/id/nige1253), Hausa States Fulfulde |
| Wikipedia | [Nigerian Fulfulde](https://en.wikipedia.org/wiki/Nigerian_Fulfulde) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Cameroon](by-region.md#cameroon), [Chad](by-region.md#chad), [Nigeria](by-region.md#nigeria) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Fula (Fulah / Fulfulde / Pular)](ff.md) `ff` |
| Explorer | [`fuv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#fuv) |
| Spec file | [`fuv.json`](../../orthography2ipa/data/fuv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Nigerian Fulfulde, the Fula (ff) variety of Northern Nigeria, spoken by ~17 million people (2020 estimate) and following the Pan-Nigerian Latin alphabet standard for its Latin orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1970 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes no spelling of its own. It takes all 42 from [Fula (Fulah / Fulfulde / Pular)](ff.md) `ff`.

The [spec file](../../orthography2ipa/data/fuv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `fuv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-fuv_wiki"></a>Wikipedia contributors (2026). *Nigerian Fulfulde*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Nigerian_Fulfulde)
2. <a id="src-arnott1970"></a>Arnott, D.W. (1970). *The Nominal and Verbal System of Fula*. Oxford University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 39 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  |  | k kː ɡ | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |
| Fricative |  | f | s |  |  |  |  | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [mb] [nd] [ndʒ] [w] [ŋɡ] [ɓ] [ɗ] [ʄ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨bh⟩ | [ɓ] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ɗ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] | word final [l] [ɽ] |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] | word initial [mb] |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] | word initial [nd] |
| ⟨ng⟩ | [ŋɡ] | word initial [ŋɡ] |
| ⟨nj⟩ | [ndʒ] | word initial [ndʒ] |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] | word final [o] |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] | word final [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] | word final [u] |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ƴ⟩ | [ʄ] |  |
| ⟨ɓ⟩ | [ɓ] |  |
| ⟨ɗ⟩ | [ɗ] |  |
| ⟨ɲ⟩ | [ɲ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "fuv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nigerian Arabic](shu-NG.md) · [Home](../index.md) · [Nigerian Pidgin →](pcm.md)
