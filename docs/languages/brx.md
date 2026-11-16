# Bodo (`brx`)

<!-- atlas:summary begin -->
Bodo is a Sino-Tibetan language, written in the Latin script. Glottolog places it in India and Nepal. The `brx` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `brx` |
| ISO 639-3 | [brx](https://iso639-3.sil.org/code/brx), Bodo (India) |
| Glottolog | [bodo1269](https://glottolog.org/resource/languoid/id/bodo1269), Bodo-Mech |
| Wikidata | [Q33223](https://www.wikidata.org/wiki/Q33223) |
| Wikipedia | [Bodo language](https://en.wikipedia.org/wiki/Bodo_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india), [Nepal](by-region.md#nepal) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Ancestor | [Proto-Boro-Garo (reconstructed)](https://tigregotico.github.io/orthography2ipa/#brx-x-proto-boro-garo) `brx-x-proto-boro-garo` |
| Explorer | [`brx` in the data explorer](https://tigregotico.github.io/orthography2ipa/#brx) |
| Spec file | [`brx.json`](../../orthography2ipa/data/brx.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Bodo (Assam, India). Tibeto-Burman, Boro-Garo branch. Phonemic tonal distinction (falling vs. level). Written in Devanagari (official since 2003). Aspirated and plain stops both phonemic.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1996 to 2006. [Sources](#sources) lists them. The spec file writes all 38 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/brx.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `brx` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-joseph_burling2006"></a>Joseph, U.V. & Burling, R. (2006). *Comparative Grammar of the Boro-Garo Languages*. CIIL.
2. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
3. <a id="src-gordon2005"></a>Gordon, R.G. (ed.) (2005). *Ethnologue: Languages of the World (15th ed.)*. SIL International.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 39 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ | d t tʰ |  |  | k kʰ ɡ | ʔ |
| Affricate |  | ts | dʒ tʃ tʃʰ |  |  |  |
| Nasal | m | n |  |  | ŋ |  |
| Trill |  | r |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː ɯ |
| Close-mid | e eː |  | o oː |
| Mid |  | ə |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [bʱ] [dʱ] [w] [ɡʱ].

Tones: [level] level tone, [falling] falling tone.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aː⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨bʱ⟩ | [bʱ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dʒ⟩ | [dʒ] |  |
| ⟨dʱ⟩ | [dʱ] |  |
| ⟨e⟩ | [e] |  |
| ⟨eː⟩ | [eː] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨iː⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨kʰ⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oː⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨pʰ⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tʃ⟩ | [tʃ] |  |
| ⟨tʃʰ⟩ | [tʃʰ] |  |
| ⟨tʰ⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uː⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ə⟩ | [ə] |  |
| ⟨ɡ⟩ | [ɡ] |  |
| ⟨ɡʱ⟩ | [ɡʱ] |  |
| ⟨ʃ⟩ | [ʃ] |  |
| ⟨ʔ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "brx")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Bislama](bi.md) · [Home](../index.md) · [Bosnian →](bs.md)
