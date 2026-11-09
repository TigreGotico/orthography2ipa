# Gorontalo (`gor`)

<!-- atlas:summary begin -->
Gorontalo is an Austronesian language, written in the Latin script. Glottolog places it in Indonesia. The `gor` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gor` |
| ISO 639-3 | [gor](https://iso639-3.sil.org/code/gor), Gorontalo |
| Glottolog | [goro1259](https://glottolog.org/resource/languoid/id/goro1259), Gorontalo |
| Wikidata | [Q2501174](https://www.wikidata.org/wiki/Q2501174) |
| Wikipedia | [Gorontalo language](https://en.wikipedia.org/wiki/Gorontalo_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Indonesia](by-region.md#indonesia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Austronesian](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1307) `x-clade-aust1307` |
| Explorer | [`gor` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gor) |
| Spec file | [`gor.json`](../../orthography2ipa/data/gor.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Gorontalo (Bahasa Hulontalo), Philippine-type Austronesian language of northern Sulawesi, Indonesia, written today in an Indonesian-based Latin alphabet (historically also in Jawi/Pegon Arabic script, which is out of scope).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1991 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 26 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gor.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gor` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-gorontalo_wiki"></a>Wikipedia contributors (2025). *Gorontalo language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Gorontalo_language)
2. <a id="src-steinhauer1991"></a>Steinhauer, Hein (1991). *Sentence-initial elements in Gorontalo*. Pacific Linguistics.
3. <a id="src-omniglot_gorontalo"></a>Ager, Simon (2026). *Gorontalo language, alphabet and pronunciation*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/gorontalo.htm)
4. <a id="src-little1995"></a>Little, Elizabeth (1995). *Gorontalo phonology (in: Sneddon, J. N. (ed.), Studies in Sulawesi Linguistics IV)*. Universitas Katolik Indonesia Atma Jaya (NUSA 37). Cited: 523.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d d̠ t | c ɟ | k ɡ | ʔ |
| Nasal | m | n | ɲ | ŋ |  |
| Trill |  | r |  |  |  |
| Fricative |  | s |  |  | h |
| Approximant |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w] [ɓ] [ɗ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] [ɓ] |  |
| ⟨c⟩ | [c] |  |
| ⟨d⟩ | [d] [ɗ] [d̠] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ɟ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [ʔ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨’⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gor")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Gipuzkoan Basque](eu-x-gipuzkoa.md) · [Home](../index.md) · [Greenlandic →](kl.md)
