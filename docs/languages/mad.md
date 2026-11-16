# Madurese (`mad`)

<!-- atlas:summary begin -->
Madurese is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in Indonesia. The `mad` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mad` |
| ISO 639-3 | [mad](https://iso639-3.sil.org/code/mad), Madurese |
| Glottolog | [nucl1460](https://glottolog.org/resource/languoid/id/nucl1460), Madurese |
| Wikipedia | [Madurese language](https://en.wikipedia.org/wiki/Madurese_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Indonesia](by-region.md#indonesia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`mad` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mad) |
| Spec file | [`mad.json`](../../orthography2ipa/data/mad.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Madurese (Bhâsa Madhurâ) in the Latin orthography (Alfabet Latèn), a Javanese-script orthography also exists and is not covered here. Distinctive three-way laryngeal contrast in stops, voiceless unaspirated, voiced, and a breathy/aspirated series written with ⟨h⟩ digraphs (bh, dh, jh, gh).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2020 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 30 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mad.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mad` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mad_wiki"></a>Wikipedia contributors (2024). *Madurese language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Madurese_language)
2. <a id="src-misnadin2020"></a>Misnadin (2020). *Madurese. Illustrations of the IPA*. Journal of the International Phonetic Association 50(1), 109-126 (open access). Cited: 109-111. [doi.org](https://doi.org/10.1017/S0025100318000257)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 32 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid |  |  | ɤ |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [bʱ] [dʒʱ] [dʱ] [w] [ɡʱ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨bh⟩ | [bʱ] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [dʱ] |  |
| ⟨e⟩ | [ə] [ɨ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡʱ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨jh⟩ | [dʒʱ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨â⟩ | [ɤ] |  |
| ⟨è⟩ | [ɛ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mad")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Macedonian](mk.md) · [Home](../index.md) · [Maguindanaon →](mdh.md)
