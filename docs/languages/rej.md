# Rejang (`rej`)

<!-- atlas:summary begin -->
Rejang is an Austronesian language, written in the Latin script. Glottolog places it in Indonesia. The `rej` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `rej` |
| ISO 639-3 | [rej](https://iso639-3.sil.org/code/rej), Rejang |
| Glottolog | [reja1240](https://glottolog.org/resource/languoid/id/reja1240), Rejang |
| Wikidata | [Q3056339](https://www.wikidata.org/wiki/Q3056339) |
| Wikipedia | [Rejang language](https://en.wikipedia.org/wiki/Rejang_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Indonesia](by-region.md#indonesia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Malayo-Polynesian (family node)](https://tigregotico.github.io/orthography2ipa/#poz) `poz` |
| Explorer | [`rej` in the data explorer](https://tigregotico.github.io/orthography2ipa/#rej) |
| Spec file | [`rej.json`](../../orthography2ipa/data/rej.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Rejang, spoken by ~350,000 people in Bengkulu and South Sumatra provinces, southwestern Sumatra, Indonesia (Austronesian, Malayo-Polynesian).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1961 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 33 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/rej.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `rej` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-rej_omniglot"></a>Ager, Simon (2024). *Rejang script and language*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/redjang.htm)
2. <a id="src-rej_wiki"></a>Wikipedia contributors (2024). *Rejang language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Rejang_language)
3. <a id="src-r12a_rjng"></a>Richard Ishida (r12a) (2022). *Rejang orthography notes*. r12a.github.io. [r12a.github.io](https://r12a.github.io/scripts/rjng/rej.html)
4. <a id="src-jaspan1961"></a>Jaspan, M.A. (1961). *Fieldwork on Rejang language and culture, Bengkulu (1961-1963)*. Unpublished field notes, cited in Wikipedia 'Rejang language'.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t ⁿd | c ɟ | k ɡ | ʔ |
| Nasal | m | n | ɲ | ŋ |  |
| Trill |  | r |  |  |  |
| Fricative |  | s |  |  | h |
| Approximant |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ai] [au] [w] [əu] [ɛa] [ᵐb] [ᵑɡ] [ᶮɟ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai] |  |
| ⟨au⟩ | [au] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [c] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ə] |  |
| ⟨ea⟩ | [ɛa] |  |
| ⟨eu⟩ | [əu] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ɟ] |  |
| ⟨k⟩ | [k] | default [k] · word final [ʔ] |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ⁿd] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngg⟩ | [ᵑɡ] |  |
| ⟨nj⟩ | [ᶮɟ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "rej")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Qatari Arabic](afb-QA.md) · [Home](../index.md) · [Rijāl Almaʿ Arabic →](ar-SA-x-rijal-alma.md)
