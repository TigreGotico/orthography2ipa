# Pannonian Rusyn (`rsk`)

<!-- atlas:summary begin -->
Pannonian Rusyn is a Slavic language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `rsk` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `rsk` |
| Wikidata | [Q35660](https://www.wikidata.org/wiki/Q35660) |
| Wikipedia | [Pannonian Rusyn Wikipedia](https://en.wikipedia.org/wiki/Pannonian_Rusyn_Wikipedia) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic](by-family.md#indo-european--balto-slavic--slavic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-slav1255) `x-clade-slav1255` |
| Explorer | [`rsk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#rsk) |
| Spec file | [`rsk.json`](../../orthography2ipa/data/rsk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Pannonian Rusyn (руски язик) of Vojvodina (Serbia) and Slavonia (Croatia), ISO 639-3 rsk since 2022, codified on the Ruski Krstur dialect and phonologically much closer to the Eastern Slovak dialects than to Carpathian Rusyn or Ukrainian. INPUT CONTRACT: Pannonian Rusyn Cyrillic text, Unicode NFC.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 2004 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 53 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/rsk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `rsk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-rsk_wiki"></a>Wikipedia contributors (2024). *Pannonian Rusyn Wikipedia*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Pannonian_Rusyn_Wikipedia)
2. <a id="src-pannonian_rusyn_wikipedia"></a>Wikipedia contributors (2026). *Pannonian Rusyn, Alphabet, Phonology (consonants, vowels), Prosody and Voicing*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Pannonian_Rusyn)
3. <a id="src-ramac_2004_rusynskyj_jazyk"></a>Юлиян Рамач (2004). *Русиньскый язык, ІІ. Літературный язык. Войводина*. Uniwersytet Opolski, Instytut filologii Polskiej. Cited: 277-304. [archive.org](https://archive.org/details/rusynskyiiazyk0000unse/page/277)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 56 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c ɟ | k ɡ |  |
| Affricate |  |  | dz dzː ts tsː | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | ɦ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [ca] [ci] [cu] [cɛ] [ja] [ji] [ju] [jɛ] [w] [ɟa] [ɟi] [ɟu] [ɟɛ] [ɲa] [ɲi] [ɲu] [ɲɛ] [ʎa] [ʎi] [ʎu] [ʎɛ] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] [w] |  |
| ⟨г⟩ | [ɦ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дж⟩ | [dʒ] |  |
| ⟨дз⟩ | [dz] |  |
| ⟨дь⟩ | [ɟ] |  |
| ⟨дю⟩ | [ɟu] |  |
| ⟨дя⟩ | [ɟa] |  |
| ⟨дє⟩ | [ɟɛ] |  |
| ⟨дї⟩ | [ɟi] |  |
| ⟨е⟩ | [ɛ] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨лю⟩ | [ʎu] |  |
| ⟨ля⟩ | [ʎa] |  |
| ⟨лє⟩ | [ʎɛ] |  |
| ⟨лї⟩ | [ʎi] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨ню⟩ | [ɲu] |  |
| ⟨ня⟩ | [ɲa] |  |
| ⟨нє⟩ | [ɲɛ] |  |
| ⟨нї⟩ | [ɲi] |  |
| ⟨о⟩ | [ɔ] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨ть⟩ | [c] |  |
| ⟨тю⟩ | [cu] |  |
| ⟨тя⟩ | [ca] |  |
| ⟨тє⟩ | [cɛ] |  |
| ⟨тї⟩ | [ci] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨є⟩ | [jɛ] |  |
| ⟨ї⟩ | [ji] |  |
| ⟨ґ⟩ | [ɡ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "rsk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Pangasinan](pag.md) · [Home](../index.md) · [Pashto →](ps.md)
