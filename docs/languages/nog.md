# Nogai (`nog`)

<!-- atlas:summary begin -->
Nogai is a Turkic language, written in the Cyrillic script. Glottolog places it in Kazakhstan and Russia. The `nog` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nog` |
| ISO 639-3 | [nog](https://iso639-3.sil.org/code/nog), Nogai |
| Glottolog | [noga1249](https://glottolog.org/resource/languoid/id/noga1249), Nogai |
| Wikidata | [Q33871](https://www.wikidata.org/wiki/Q33871) |
| Wikipedia | [Nogai language](https://en.wikipedia.org/wiki/Nogai_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Kazakhstan](by-region.md#kazakhstan), [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1960, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`nog` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nog) |
| Spec file | [`nog.json`](../../orthography2ipa/data/nog.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Nogai (ногай тили), a Kipchak Turkic language spoken in the North Caucasus and lower Volga, Russia, written in a Cyrillic alphabet reformed in 1960: the Russian letters plus the umlaut letters ⟨аь⟩ /æ/, ⟨оь⟩ /œ/, ⟨уь⟩ /y/ and the digraphs ⟨гъ⟩ /ʁ/, ⟨къ⟩ /q/, ⟨нъ⟩ /ŋ/, ⟨дж⟩ /dʒ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1998 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 38 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nog.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nog` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-nogai_alphabets_wiki"></a>Wikipedia contributors (2026). *Nogai alphabets*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Nogai_alphabets)
2. <a id="src-nogai_wiki"></a>Wikipedia contributors (2026). *Nogai language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Nogai_language)
3. <a id="src-johanson_csato1998"></a>Johanson, L. & Csató, É. Á. (eds.) (1998). *The Turkic Languages*. Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 39 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | ʁ χ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e | o |
| Open-mid | œ |  |
| Near-open | æ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [w] [ʃtʃ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨аь⟩ | [æ] |  |
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
| ⟨нъ⟩ | [ŋ] |  |
| ⟨о⟩ | [o] |  |
| ⟨оь⟩ | [œ] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨уь⟩ | [y] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] |  |
| ⟨ы⟩ | [ɯ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nog")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nigerian Pidgin](pcm.md) · [Home](../index.md) · [Norman →](nrf.md)
