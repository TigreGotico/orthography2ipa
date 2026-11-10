# Kusaal (`kus`)

<!-- atlas:summary begin -->
Kusaal is an Atlantic-Congo language, written in the Latin script. Glottolog places it in the Africa and North America macroareas. The `kus` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kus` |
| Wikipedia | [Kusaal language](https://en.wikipedia.org/wiki/Kusaal_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#several-macroareas), [North America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`kus` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kus) |
| Spec file | [`kus.json`](../../orthography2ipa/data/kus.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kusaal (Kʋsaal), a Gur / Mabia (Atlantic-Congo) language of north-eastern Ghana. INPUT CONTRACT: text is assumed to be in the UNIFIED KUSAAL ORTHOGRAPHY in use since 2013 (the orthography of the 2015+ Bible revision, 'B3' in Eddyshaw's grammar), for the AGOLLE dialect, the literary standard.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 2018 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kus.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kus` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-eddyshaw2025_grammar"></a>Eddyshaw, David (2025). *A Grammar of Kusaal*. Zenodo (CC-BY-4.0). Cited: 18-24. [zenodo.org](https://zenodo.org/records/16656892)
2. <a id="src-musah2018"></a>Musah, Anthony Agoswin (2018). *A Grammar of Kusaal: A Mabia (Gur) Language of Northern Ghana*. Peter Lang. [peterlang.com](https://www.peterlang.com/document/1056754)
3. <a id="src-kusaal_wiki"></a>Wikipedia contributors (2026). *Kusaal language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kusaal_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  | k kʰ ɡ | ʔ |
| Nasal | m |  | n | ɲ | ŋ |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative |  | f v | s z |  |  | h |
| Approximant |  |  |  | j j̃ |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Near-close | ɪ | ʊ |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [k͡p] [w] [w̃] [ŋ͡m] [ɡ͡b].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɪ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] [ɪ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kp⟩ | [k͡p] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nw⟩ | [w̃] |  |
| ⟨ny⟩ | [j̃] |  |
| ⟨o⟩ | [ʊ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɛ⟩ | [ɛ] |  |
| ⟨ɩ⟩ | [ɪ] |  |
| ⟨ʋ⟩ | [ʊ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kus")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kurukh](kru.md) · [Home](../index.md) · [Kuwaiti Arabic →](afb-KW.md)
