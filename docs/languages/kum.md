# Kumyk (`kum`)

<!-- atlas:summary begin -->
Kumyk is a Turkic language, written in the Cyrillic script. Glottolog places it in Kazakhstan and Russia. The `kum` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kum` |
| ISO 639-3 | [kum](https://iso639-3.sil.org/code/kum), Kumyk |
| Glottolog | [kumy1244](https://glottolog.org/resource/languoid/id/kumy1244), Kumyk |
| Wikidata | [Q36209](https://www.wikidata.org/wiki/Q36209) |
| Wikipedia | [Kumyk language](https://en.wikipedia.org/wiki/Kumyk_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Kazakhstan](by-region.md#kazakhstan), [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1938, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`kum` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kum) |
| Spec file | [`kum.json`](../../orthography2ipa/data/kum.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kumyk (къумукъ тил), a Kipchak Turkic language of Dagestan, Russia, written in a Cyrillic alphabet reformed in 1938: the Russian letters plus the digraphs ⟨гъ⟩ /ʁ/, ⟨гь⟩ /h/, ⟨къ⟩ /q/, ⟨нг⟩ /ŋ/ (borrowed from the Caucasian-contact convention shared with Karachay-Balkar/Nogai) and the umlaut letters ⟨оь⟩ /ø/, ⟨уь⟩ /y/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1998 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 39 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kum.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kum` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kumyk_wiki"></a>Wikipedia contributors (2026). *Kumyk language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kumyk_language)
2. <a id="src-johanson_csato1998"></a>Johanson, L. & Csató, É. Á. (eds.) (1998). *The Turkic Languages*. Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 41 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q ɢ | ʔ |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Open | a |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [ʃtʃ].
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
| ⟨гь⟩ | [h] |  |
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
| ⟨оь⟩ | [ø] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨уь⟩ | [y] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] |  |
| ⟨ъ⟩ | [ʔ] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kum")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Krio](kri.md) · [Home](../index.md) · [Kurdish →](ku.md)
