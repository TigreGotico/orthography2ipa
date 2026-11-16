# Sasak (`sas`)

<!-- atlas:summary begin -->
Sasak is an Austronesian language, written in the Latin script. Glottolog places it in Indonesia. The `sas` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sas` |
| ISO 639-3 | [sas](https://iso639-3.sil.org/code/sas), Sasak |
| Glottolog | [sasa1249](https://glottolog.org/resource/languoid/id/sasa1249), Sasak |
| Wikidata | [Q1294047](https://www.wikidata.org/wiki/Q1294047) |
| Wikipedia | [Sasak language](https://en.wikipedia.org/wiki/Sasak_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Indonesia](by-region.md#indonesia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Malayo-Polynesian (family node)](https://tigregotico.github.io/orthography2ipa/#poz) `poz` |
| Explorer | [`sas` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sas) |
| Spec file | [`sas.json`](../../orthography2ipa/data/sas.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Sasak (Bahasa Sasak), spoken by ~2-2.7 million on Lombok, West Nusa Tenggara, Indonesia (Austronesian, Malayo-Polynesian, closely related to Balinese and Sumbawa).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 2020 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sas.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sas` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sas_jipa2020"></a>Archangeli, Diana & Tanashur, Panji & Yip, Jonathan (2020). *Sasak, Meno-Mené dialect*. Journal of the International Phonetic Association 50(1). Cited: 93-106. [cambridge.org](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D426C876E009E03B65C639D31FA78E59/S0025100318000063a.pdf/sasak-meno-mene-dialect.pdf)
2. <a id="src-sas_wiki"></a>Wikipedia contributors (2024). *Sasak language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Sasak_language)
3. <a id="src-labphon_nasal_sub"></a>Various (2021). *Phonological and phonetic properties of nasal substitution in Sasak and Javanese*. Laboratory Phonology. [journal-labphon.org](https://www.journal-labphon.org/article/id/6208/)
4. <a id="src-ldtc_sasak"></a>Language Documentation Training Center (2023). *Sasak (Nisa), Orthography & Phonology*. LDTC. [ldtc.org](https://www.ldtc.org/languages/sasak-nisa/orthography)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  | k ɡ | ʔ |
| Affricate |  |  | dʑ tɕ |  |  |
| Nasal | m | n | ɲ | ŋ |  |
| Trill |  | r |  |  |  |
| Tap |  | ɾ |  |  |  |
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

Sequences that the spec writes as one unit: [ae] [ai] [au] [ia] [oe] [uə] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ae⟩ | [ae] |  |
| ⟨ai⟩ | [ai] |  |
| ⟨au⟩ | [au] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tɕ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ə] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ia] |  |
| ⟨j⟩ | [dʑ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oe⟩ | [oe] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uə⟩ | [uə] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sas")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sarsi](srs.md) · [Home](../index.md) · [Sassarese Sardinian →](sdc.md)
