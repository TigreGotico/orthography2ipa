# Temne (`tem`)

<!-- atlas:summary begin -->
Temne is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Guinea and Sierra Leone. The `tem` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tem` |
| ISO 639-3 | [tem](https://iso639-3.sil.org/code/tem), Timne |
| Glottolog | [timn1235](https://glottolog.org/resource/languoid/id/timn1235), Timne |
| Wikidata | [Q36613](https://www.wikidata.org/wiki/Q36613) |
| Wikipedia | [Temne language](https://en.wikipedia.org/wiki/Temne_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Guinea](by-region.md#guinea), [Sierra Leone](by-region.md#sierra-leone) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`tem` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tem) |
| Spec file | [`tem.json`](../../orthography2ipa/data/tem.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Temne, Mel branch of Atlantic-Congo (not close to Mande, despite sharing Sierra Leone with Mende), spoken by ~2 million people mainly in Northern Sierra Leone and the Western Area.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1961 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 28 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tem.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tem` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wilson1961"></a>Wilson, William André Auquier (1961). *An Outline of the Temne Language*. School of Oriental and African Studies, University of London.
2. <a id="src-temne_wiki"></a>Wikipedia contributors (2026). *Temne language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Temne_language)
3. <a id="src-kanu_tucker_2010"></a>Kanu, Sullay M. and Tucker, Benjamin V. (2010). *Temne*. Journal of the International Phonetic Association 40(2), Illustrations of the IPA. Cited: 247-253. [cambridge.org](https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/temne/BD1773945818578E52AF92431AEE168C)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 28 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t t̪ |  |  | k |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ ʌ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [kp] [w] [ɡb].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨gb⟩ | [ɡb] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨kp⟩ | [kp] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t̪] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ə⟩ | [ə] |  |
| ⟨ɛ⟩ | [ɛ] |  |
| ⟨ʌ⟩ | [ʌ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tem")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Telugu](te.md) · [Home](../index.md) · [Ternate →](tft.md)
