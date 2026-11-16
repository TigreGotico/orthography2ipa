# Khakas (`kjh`)

<!-- atlas:summary begin -->
Khakas is a Turkic language, written in the Cyrillic script. Glottolog places it in China and Russia. The `kjh` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kjh` |
| ISO 639-3 | [kjh](https://iso639-3.sil.org/code/kjh), Khakas |
| Glottolog | [khak1248](https://glottolog.org/resource/languoid/id/khak1248), Khakas |
| Wikidata | [Q33575](https://www.wikidata.org/wiki/Q33575) |
| Wikipedia | [Khakas language](https://en.wikipedia.org/wiki/Khakas_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1939, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`kjh` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kjh) |
| Spec file | [`kjh.json`](../../orthography2ipa/data/kjh.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Khakas (хакас тілі), a South Siberian Turkic language of the Republic of Khakassia, Russia, written in a Cyrillic alphabet reformed in 1939: the Russian letters plus ⟨ғ⟩ /ɣ/, ⟨і⟩ /ɘ/, ⟨ң⟩ /ŋ/, ⟨ӧ⟩ /ø/, ⟨ӱ⟩ /y/ and the affricate letter ⟨ӌ⟩ /dʒ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1998 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 45 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kjh.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kjh` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-khakas_wiki"></a>Wikipedia contributors (2026). *Khakas language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Khakas_language)
2. <a id="src-anderson1998"></a>Anderson, G. D. S. (1998). *Xakas*. Lincom Europa.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 45 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | ts | dʒ tʃ |  |  |
| Nasal | m |  | n |  |  | ŋ |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː |  | u uː ɯ ɯː |
| Close-mid | e eː ø øː | ɘ | o oː |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [ʃtʃ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨аа⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] [e] |  |
| ⟨ее⟩ | [eː] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨ии⟩ | [iː] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨оо⟩ | [oː] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨уу⟩ | [uː] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] |  |
| ⟨ы⟩ | [ɯ] |  |
| ⟨ыы⟩ | [ɯː] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨і⟩ | [ɘ] |  |
| ⟨ғ⟩ | [ɣ] |  |
| ⟨ң⟩ | [ŋ] |  |
| ⟨ӌ⟩ | [dʒ] |  |
| ⟨ӧ⟩ | [ø] |  |
| ⟨ӧӧ⟩ | [øː] |  |
| ⟨ӱ⟩ | [y] |  |
| ⟨ӱӱ⟩ | [yː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kjh")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ket](ket.md) · [Home](../index.md) · [Khalaj →](klj.md)
