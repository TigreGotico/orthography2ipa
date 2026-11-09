# Toki Pona (`tok`)

<!-- atlas:summary begin -->
Toki Pona is a Constructed language, written in the Latin script. Glottolog places it in Canada. The `tok` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tok` |
| ISO 639-3 | [tok](https://iso639-3.sil.org/code/tok), Toki Pona |
| Glottolog | [toki1239](https://glottolog.org/resource/languoid/id/toki1239), Toki Pona |
| Wikidata | [Q36846](https://www.wikidata.org/wiki/Q36846) |
| Wikipedia | [Toki Pona](https://en.wikipedia.org/wiki/Toki_Pona) |
| Family | [Constructed](by-family.md#constructed) |
| Region | [North America](by-region.md#north-america) > [Canada](by-region.md#canada) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 2001, living |
| Explorer | [`tok` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tok) |
| Spec file | [`tok.json`](../../orthography2ipa/data/tok.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Toki Pona (Sonja Lang, 2001, book 2014). Minimal, fully phonemic orthography: 14 letters = 14 phonemes, 9 consonants /p t k s m n l j w/ and 5 vowels /a e i o u/. Syllables are (C)V(n), the sequences ji, ti, wu, wo, nn, nm are disallowed. Stress is always on the first syllable of a word.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2014 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 14 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tok.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tok` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-lang2014"></a>Lang, Sonja (2014). *Toki Pona: The Language of Good*. Sonja Lang.
2. <a id="src-tokipona_wiki"></a>Wikipedia contributors (2024). *Toki Pona*. Wikipedia. Cited: Phoneme inventory and stress. [en.wikipedia.org](https://en.wikipedia.org/wiki/Toki_Pona)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 14 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|
| Plosive | p | t |  | k |
| Nasal | m | n |  |  |
| Fricative |  | s |  |  |
| Approximant |  |  | j |  |
| Lateral approximant |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨e⟩ | [e] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tok")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tokelau](tkl.md) · [Home](../index.md) · [Tongan →](to.md)
