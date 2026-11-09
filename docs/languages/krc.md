# Karachay-Balkar (`krc`)

<!-- atlas:summary begin -->
Karachay-Balkar is a Turkic language, written in the Cyrillic script. Glottolog places it in Azerbaijan, Georgia, Kazakhstan and Russia. The `krc` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `krc` |
| ISO 639-3 | [krc](https://iso639-3.sil.org/code/krc), Karachay-Balkar |
| Glottolog | [kara1465](https://glottolog.org/resource/languoid/id/kara1465), Karachay-Balkar |
| Wikidata | [Q33714](https://www.wikidata.org/wiki/Q33714) |
| Wikipedia | [Karachay-Balkar](https://en.wikipedia.org/wiki/Karachay-Balkar) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Azerbaijan](by-region.md#azerbaijan), [Georgia](by-region.md#georgia), [Kazakhstan](by-region.md#kazakhstan), [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`krc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#krc) |
| Spec file | [`krc.json`](../../orthography2ipa/data/krc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Karachay-Balkar (къарачай-малкъар), Kipchak Turkic of the North Caucasus, written in Cyrillic since 1937. Digraphs: <гъ> = /ʁ/, <къ> = /q/, <нг> = /ŋ/, <дж> = /dʒ/ (Karachay, the Balkar varieties have /ʒ/ or /z/ here).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1996 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 35 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/krc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `krc` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-seegmiller1996"></a>Seegmiller, Steve (1996). *Karachay (Languages of the World/Materials 109)*. Lincom Europa.
2. <a id="src-krc_wiki"></a>Wikipedia contributors (2024). *Karachay-Balkar*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Karachay-Balkar)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q ɢ |  |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ | x | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Near-open | æ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [w].
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
| ⟨гъ⟩ | [ʁ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дж⟩ | [dʒ] |  |
| ⟨е⟩ | [je] [e] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨къ⟩ | [q] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нг⟩ | [ŋ] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] [w] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ы⟩ | [ɯ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [y] [ju] |  |
| ⟨я⟩ | [æ] [ja] |  |
| ⟨ё⟩ | [ø] [jo] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "krc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kapampangan](pam.md) · [Home](../index.md) · [Karakalpak →](kaa.md)
