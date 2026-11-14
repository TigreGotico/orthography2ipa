# Cantonese — Jyutping (`yue-Latn-jyutping`)

<!-- atlas:summary begin -->
Cantonese — Jyutping is a Sino-Tibetan language, written in the Latin script. Glottolog places it in China, Hong Kong SAR China and Macao SAR China. The `yue-Latn-jyutping` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `yue-Latn-jyutping` |
| Glottolog | [cant1236](https://glottolog.org/resource/languoid/id/cant1236), Cantonese |
| Wikidata | [Q649913](https://www.wikidata.org/wiki/Q649913) |
| Wikipedia | [Jyutping](https://en.wikipedia.org/wiki/Jyutping) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [Hong Kong SAR China](by-region.md#hong-kong-sar-china), [Macao SAR China](by-region.md#macao-sar-china) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Cantonese](https://tigregotico.github.io/orthography2ipa/#yue) `yue` |
| Explorer | [`yue-Latn-jyutping` in the data explorer](https://tigregotico.github.io/orthography2ipa/#yue-Latn-jyutping) |
| Spec file | [`yue-Latn-jyutping.json`](../../orthography2ipa/data/yue-Latn-jyutping.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Jyutping (the Linguistic Society of Hong Kong Cantonese Romanization Scheme, LSHK 1993), the officially promoted romanization for Standard Cantonese.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1993 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 77 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/yue-Latn-jyutping.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `yue-Latn-jyutping` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-jyutping_wiki"></a>Wikipedia contributors (2026). *Jyutping*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Jyutping)
2. <a id="src-lshk1993"></a>Linguistic Society of Hong Kong (1993). *The Jyutping Scheme (粵語拼音方案)*. Linguistic Society of Hong Kong. [lshk.org](https://lshk.org/jyutping-scheme/)
3. <a id="src-matthews_yip1994"></a>Matthews, Stephen & Yip, Virginia (1994). *Cantonese: A Comprehensive Grammar*. Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 77 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | t tʰ |  | k kʰ kʷ kʷʰ |  |
| Affricate |  |  | ts tsʰ |  |  |  |
| Nasal | m |  | n |  | ŋ ŋ̍ |  |
| Fricative |  | f | s |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː yː |  | uː |
| Open-mid | œː ɛː |  | ɔː |
| Near-open |  | ɐ |  |
| Open | aː |  |  |

Sequences that the spec writes as one unit: [aːi̯] [aːk̚] [aːm] [aːn] [aːp̚] [aːt̚] [aːu̯] [aːŋ] [ei̯] [iːm] [iːn] [iːp̚] [iːt̚] [iːu̯] [ou̯] [uːn] [uːt̚] [uːy̯] [w] [yːn] [yːt̚] [œːk̚] [œːt̚] [œːŋ] [ɐi̯] [ɐk̚] [ɐm] [ɐn] [ɐp̚] [ɐt̚] [ɐu̯] [ɐŋ] [ɔːk̚] [ɔːn] [ɔːt̚] [ɔːy̯] [ɔːŋ] [ɛːk̚] [ɛːm] [ɛːp̚], and 10 more.

Tones: [1] high level / high falling, 55/53, [2] mid rising, 35, [3] mid level, 33, [4] low falling, 21, [5] low rising, 13, [6] low level, 22, [1(7)] entering high level, 5 (obstruent coda only), [3(8)] entering mid level, 3 (obstruent coda only), [6(9)] entering low level, 2 (obstruent coda only).
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɐ] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨aai⟩ | [aːi̯] |  |
| ⟨aak⟩ | [aːk̚] |  |
| ⟨aam⟩ | [aːm] |  |
| ⟨aan⟩ | [aːn] |  |
| ⟨aang⟩ | [aːŋ] |  |
| ⟨aap⟩ | [aːp̚] |  |
| ⟨aat⟩ | [aːt̚] |  |
| ⟨aau⟩ | [aːu̯] |  |
| ⟨ai⟩ | [ɐi̯] |  |
| ⟨ak⟩ | [ɐk̚] |  |
| ⟨am⟩ | [ɐm] |  |
| ⟨an⟩ | [ɐn] |  |
| ⟨ang⟩ | [ɐŋ] |  |
| ⟨ap⟩ | [ɐp̚] |  |
| ⟨at⟩ | [ɐt̚] |  |
| ⟨au⟩ | [ɐu̯] |  |
| ⟨b⟩ | [p] |  |
| ⟨c⟩ | [tsʰ] |  |
| ⟨d⟩ | [t] |  |
| ⟨e⟩ | [ɛː] |  |
| ⟨ei⟩ | [ei̯] |  |
| ⟨ek⟩ | [ɛːk̚] |  |
| ⟨em⟩ | [ɛːm] |  |
| ⟨eng⟩ | [ɛːŋ] |  |
| ⟨eoi⟩ | [ɵy̯] |  |
| ⟨eon⟩ | [ɵn] |  |
| ⟨eot⟩ | [ɵt̚] |  |
| ⟨ep⟩ | [ɛːp̚] |  |
| ⟨et⟩ | [ɛːt̚] |  |
| ⟨eu⟩ | [ɛːu̯] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [k] |  |
| ⟨gw⟩ | [kʷ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [iː] |  |
| ⟨ik⟩ | [ɪk̚] |  |
| ⟨im⟩ | [iːm] |  |
| ⟨in⟩ | [iːn] |  |
| ⟨ing⟩ | [ɪŋ] |  |
| ⟨ip⟩ | [iːp̚] |  |
| ⟨it⟩ | [iːt̚] |  |
| ⟨iu⟩ | [iːu̯] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [kʰ] |  |
| ⟨kw⟩ | [kʷʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ng̍⟩ | [ŋ̍] |  |
| ⟨o⟩ | [ɔː] |  |
| ⟨oe⟩ | [œː] |  |
| ⟨oek⟩ | [œːk̚] |  |
| ⟨oeng⟩ | [œːŋ] |  |
| ⟨oet⟩ | [œːt̚] |  |
| ⟨oi⟩ | [ɔːy̯] |  |
| ⟨ok⟩ | [ɔːk̚] |  |
| ⟨on⟩ | [ɔːn] |  |
| ⟨ong⟩ | [ɔːŋ] |  |
| ⟨ot⟩ | [ɔːt̚] |  |
| ⟨ou⟩ | [ou̯] |  |
| ⟨p⟩ | [pʰ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨u⟩ | [uː] |  |
| ⟨ui⟩ | [uːy̯] |  |
| ⟨uk⟩ | [ʊk̚] |  |
| ⟨un⟩ | [uːn] |  |
| ⟨ung⟩ | [ʊŋ] |  |
| ⟨ut⟩ | [uːt̚] |  |
| ⟨w⟩ | [w] |  |
| ⟨yu⟩ | [yː] |  |
| ⟨yun⟩ | [yːn] |  |
| ⟨yut⟩ | [yːt̚] |  |
| ⟨z⟩ | [ts] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "yue-Latn-jyutping")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Cantabrian Spanish](es-ES-x-cantabri.md) · [Home](../index.md) · [Castilian Spanish →](es-ES.md)
