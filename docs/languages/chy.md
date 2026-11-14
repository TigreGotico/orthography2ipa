# Cheyenne (`chy`)

<!-- atlas:summary begin -->
Cheyenne is an Algic language, written in the Latin script. Glottolog places it in United States. The `chy` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `chy` |
| ISO 639-3 | [chy](https://iso639-3.sil.org/code/chy), Cheyenne |
| Glottolog | [chey1247](https://glottolog.org/resource/languoid/id/chey1247), Cheyenne |
| Wikidata | [Q33265](https://www.wikidata.org/wiki/Q33265) |
| Wikipedia | [Cheyenne language](https://en.wikipedia.org/wiki/Cheyenne_language) |
| Family | [Algic](by-family.md#algic) |
| Region | [North America](by-region.md#north-america) > [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Algic](https://tigregotico.github.io/orthography2ipa/#x-clade-algi1248) `x-clade-algi1248` |
| Explorer | [`chy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#chy) |
| Spec file | [`chy.json`](../../orthography2ipa/data/chy.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cheyenne (Tsėhésenėstsestȯtse), Algonquian language of Montana and Oklahoma. Uses the standard practical orthography developed by Wayne Leman and the Cheyenne translation project: three vowel qualities a e o, each of which may carry high tone (á é ó, low tone unmarked) or be voiceless/whispered (ȧ ė ȯ).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2011 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 21 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/chy.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `chy` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-leman2011"></a>Leman, Wayne (2011). *A Reference Grammar of the Cheyenne Language*. Lulu / Cheyenne Language Project.
2. <a id="src-chy_wiki"></a>Wikipedia contributors (2024). *Cheyenne language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Cheyenne_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 20 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t |  | k | ʔ |
| Nasal | m |  | n |  |  |  |
| Fricative |  | v | s | ʃ | x | h |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close-mid | e e̥ é | o o̥ ó |
| Open | a á ḁ |  |

Tones: [á] high, [é] high, [ó] high.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨e⟩ | [e] |  |
| ⟨h⟩ | [h] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨v⟩ | [v] |  |
| ⟨x⟩ | [x] |  |
| ⟨á⟩ | [á] |  |
| ⟨é⟩ | [é] |  |
| ⟨ó⟩ | [ó] |  |
| ⟨ė⟩ | [e̥] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ȧ⟩ | [ḁ] |  |
| ⟨ȯ⟩ | [o̥] |  |
| ⟨’⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "chy")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Cheso Aragonese](an-x-cheso.md) · [Home](../index.md) · [Chibcha →](chb.md)
