# Standard Moroccan Tamazight (`zgh`)

<!-- atlas:summary begin -->
Standard Moroccan Tamazight is a Berber language, written in the Tifinagh script. Glottolog places it in Morocco. The `zgh` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `zgh` |
| ISO 639-3 | [zgh](https://iso639-3.sil.org/code/zgh), Standard Moroccan Tamazight |
| Glottolog | [stan1324](https://glottolog.org/resource/languoid/id/stan1324), Standard Moroccan Tamazight |
| Wikidata | [Q7598268](https://www.wikidata.org/wiki/Q7598268) |
| Wikipedia | [Standard Moroccan Amazigh](https://en.wikipedia.org/wiki/Standard_Moroccan_Amazigh) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Berber](by-family.md#afro-asiatic--berber) |
| Region | [Africa](by-region.md#africa) > [Morocco](by-region.md#morocco) |
| Script | [Tifinagh](by-script.md#tifinagh) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 2001, living |
| Ancestor | [Berber (Proto-Berber / Common Tamazight)](https://tigregotico.github.io/orthography2ipa/#ber) `ber` |
| Explorer | [`zgh` in the data explorer](https://tigregotico.github.io/orthography2ipa/#zgh) |
| Spec file | [`zgh.json`](../../orthography2ipa/data/zgh.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Moroccan Amazigh / Tamazight (ⵜⴰⵎⴰⵣⵉⵖⵜ ⵜⴰⵏⴰⵡⴰⵢⵜ), the standardised Amazigh variety codified by IRCAM (Institut Royal de la Culture Amazighe) and an official language of Morocco since 2011.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 2006 to 2024. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 33 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/zgh.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `zgh` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-ircam2006"></a>Ameur, M., Bouhjar, A., Boukhris, F., et al. (IRCAM) (2006). *Graphie et orthographe de l'amazighe*. Institut Royal de la Culture Amazighe, Rabat. [ircam.ma](https://www.ircam.ma/)
2. <a id="src-tifinagh_wiki"></a>Wikipedia contributors (2024). *Tifinagh*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Tifinagh)
3. <a id="src-zgh_wiki"></a>Wikipedia contributors (2024). *Standard Moroccan Amazigh*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Standard_Moroccan_Amazigh)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b |  | d dˤ t tˤ |  |  | k kʷ ɡ ɡʷ | q |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r rˤ |  |  |  |  |  |  |
| Fricative |  | f | s sˤ z zˤ | ʃ ʒ |  | ɣ | χ | ħ ʕ | h |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ⴰ⟩ | [a] |  |
| ⟨ⴱ⟩ | [b] |  |
| ⟨ⴳ⟩ | [ɡ] |  |
| ⟨ⴳⵯ⟩ | [ɡʷ] |  |
| ⟨ⴷ⟩ | [d] |  |
| ⟨ⴹ⟩ | [dˤ] |  |
| ⟨ⴻ⟩ | [ə] |  |
| ⟨ⴼ⟩ | [f] |  |
| ⟨ⴽ⟩ | [k] |  |
| ⟨ⴽⵯ⟩ | [kʷ] |  |
| ⟨ⵀ⟩ | [h] |  |
| ⟨ⵃ⟩ | [ħ] |  |
| ⟨ⵄ⟩ | [ʕ] |  |
| ⟨ⵅ⟩ | [χ] |  |
| ⟨ⵇ⟩ | [q] |  |
| ⟨ⵉ⟩ | [i] |  |
| ⟨ⵊ⟩ | [ʒ] |  |
| ⟨ⵍ⟩ | [l] |  |
| ⟨ⵎ⟩ | [m] |  |
| ⟨ⵏ⟩ | [n] |  |
| ⟨ⵓ⟩ | [u] [w] |  |
| ⟨ⵔ⟩ | [r] |  |
| ⟨ⵕ⟩ | [rˤ] |  |
| ⟨ⵖ⟩ | [ɣ] |  |
| ⟨ⵙ⟩ | [s] |  |
| ⟨ⵚ⟩ | [sˤ] |  |
| ⟨ⵛ⟩ | [ʃ] |  |
| ⟨ⵜ⟩ | [t] |  |
| ⟨ⵟ⟩ | [tˤ] |  |
| ⟨ⵡ⟩ | [w] |  |
| ⟨ⵢ⟩ | [j] |  |
| ⟨ⵣ⟩ | [z] |  |
| ⟨ⵥ⟩ | [zˤ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "zgh")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sranan Tongo](srn.md) · [Home](../index.md) · [Sudanese Arabic →](apd-SD.md)
