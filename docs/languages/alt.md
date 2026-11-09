# Southern Altai (`alt`)

<!-- atlas:summary begin -->
Southern Altai is a Turkic language, written in the Cyrillic script. Glottolog places it in China, Kazakhstan, Mongolia and Russia. The `alt` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `alt` |
| ISO 639-3 | [alt](https://iso639-3.sil.org/code/alt), Southern Altai |
| Glottolog | [sout2694](https://glottolog.org/resource/languoid/id/sout2694), Southern Altai |
| Wikidata | [Q1991779](https://www.wikidata.org/wiki/Q1991779) |
| Wikipedia | [Southern Altai language](https://en.wikipedia.org/wiki/Southern_Altai_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [Kazakhstan](by-region.md#kazakhstan), [Mongolia](by-region.md#mongolia), [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1922, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`alt` in the data explorer](https://tigregotico.github.io/orthography2ipa/#alt) |
| Spec file | [`alt.json`](../../orthography2ipa/data/alt.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Southern Altai (Turkic, Altai Republic), written in a Cyrillic alphabet = the Russian alphabet plus ⟨ј⟩ /dʒ~ɟ/, ⟨ҥ⟩ /ŋ/, ⟨ӧ⟩ /ø/, ⟨ӱ⟩ /y/. Vowel harmony (front/back, rounding) operates throughout, vowel length is phonemic and written by doubling.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1947 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 35 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/alt.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `alt` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-altai_wiki"></a>Wikipedia contributors (2024). *Southern Altai language*. Wikipedia. Cited: Cyrillic alphabet (with the extra letters ј, ҥ, ӧ, ӱ), 8-vowel system /i y e ø ɯ u a o/ with phonemic length, and the 20-consonant inventory (x, ts marginal, in Russian loans only). [en.wikipedia.org](https://en.wikipedia.org/wiki/Southern_Altai_language)
2. <a id="src-baskakov1947"></a>Baskakov, N. A. (1947). *Ойротско-русский словарь (Oirot-Russian Dictionary)*. OGIZ.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | ɟ | k ɡ |
| Affricate |  |  | ts | dʒ tʃ |  |  |
| Nasal | m |  | n |  |  | ŋ |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ | x ɣ |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Open | a |  |

Sequences that the spec writes as one unit: [ja] [jo] [ju].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [e] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ы⟩ | [ɯ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ј⟩ | [dʒ] |  |
| ⟨ҥ⟩ | [ŋ] |  |
| ⟨ӧ⟩ | [ø] |  |
| ⟨ӱ⟩ | [y] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "alt")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← South Slavey](xsl.md) · [Home](../index.md) · [Southern Dagaare →](dga.md)
