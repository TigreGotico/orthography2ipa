# Crimean Tatar (`crh`)

<!-- atlas:summary begin -->
Crimean Tatar is a Turkic language, written in the Latin script. Glottolog places it in 9 countries. The `crh` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `crh` |
| ISO 639-3 | [crh](https://iso639-3.sil.org/code/crh), Crimean Tatar |
| Glottolog | [crim1257](https://glottolog.org/resource/languoid/id/crim1257), Crimean Tatar |
| Wikidata | [Q33357](https://www.wikidata.org/wiki/Q33357) |
| Wikipedia | [Crimean Tatar language](https://en.wikipedia.org/wiki/Crimean_Tatar_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Bulgaria](by-region.md#bulgaria), [Kyrgyzstan](by-region.md#kyrgyzstan), [Lithuania](by-region.md#lithuania), [Moldova](by-region.md#moldova), [Romania](by-region.md#romania), [Russia](by-region.md#russia), [Türkiye](by-region.md#türkiye), [Ukraine](by-region.md#ukraine) and 1 more |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Turkic](https://tigregotico.github.io/orthography2ipa/#x-clade-turk1311) `x-clade-turk1311` |
| Explorer | [`crh` in the data explorer](https://tigregotico.github.io/orthography2ipa/#crh) |
| Spec file | [`crh.json`](../../orthography2ipa/data/crh.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Crimean Tatar in the standard Latin alphabet (Turkish-style, official since 1997). Largely one-to-one letter→phoneme orthography. ⟨c⟩=/dʒ/, ⟨ç⟩=/tʃ/, ⟨ş⟩=/ʃ/, ⟨j⟩=/ʒ/, ⟨ğ⟩=/ɣ/, ⟨h⟩=/x/, ⟨ñ⟩=/ŋ/, ⟨q⟩=/q/, ⟨ı⟩=/ɯ/, ⟨ü⟩=/y/, ⟨ö⟩=/ø/. Vowel harmony operates but is fully reflected in spelling.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2024. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/crh.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `crh` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-crh_wiki"></a>Wikipedia contributors (2024). *Crimean Tatar language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Crimean_Tatar_language)
2. <a id="src-crh_alpha_wiki"></a>Wikipedia contributors (2024). *Crimean Tatar alphabets*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Crimean_Tatar_alphabets)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Near-close | ɪ |  |
| Close-mid | e ø | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [dʒ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [tʃ] |  |
| ⟨ñ⟩ | [ŋ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |
| ⟨ğ⟩ | [ɣ] |  |
| ⟨ı⟩ | [ɯ] |  |
| ⟨ş⟩ | [ʃ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "crh")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Cree](cr.md) · [Home](../index.md) · [Croatian →](hr.md)
