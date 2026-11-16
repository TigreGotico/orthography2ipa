# Tulu (`tcy`)

<!-- atlas:summary begin -->
Tulu is a Dravidian language, written in the Latin script. Glottolog places it in India. The `tcy` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tcy` |
| ISO 639-3 | [tcy](https://iso639-3.sil.org/code/tcy), Tulu |
| Glottolog | [tulu1258](https://glottolog.org/resource/languoid/id/tulu1258), Tulu |
| Wikidata | [Q34251](https://www.wikidata.org/wiki/Q34251) |
| Wikipedia | [Tulu language](https://en.wikipedia.org/wiki/Tulu_language) |
| Family | [Dravidian](by-family.md#dravidian) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Dravidian](https://tigregotico.github.io/orthography2ipa/#x-clade-drav1251) `x-clade-drav1251` |
| Explorer | [`tcy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tcy) |
| Spec file | [`tcy.json`](../../orthography2ipa/data/tcy.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Tulu (coastal Karnataka / Udupi / Mangaluru district). South Dravidian language, unwritten in daily practice but has traditional Tigaḷari script (Buddhist manuscripts). Usually written in Kannada script. Distinct from Kannada despite geographic closeness. Full aspirate series from Sanskrit contact.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1967 to 2003. [Sources](#sources) lists them. The spec file writes all 49 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tcy.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tcy` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-krishnamurti2003"></a>Krishnamurti, B. (2003). *The Dravidian Languages*. Cambridge University Press.
2. <a id="src-bhat1967"></a>Bhat, D.N.S. (1967). *Tulu Verb Morphology*. Deccan College Postgraduate and Research Institute.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 50 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  |  |  |  | dʑ tɕ tɕʰ |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  |  | s | ʃ | ʂ |  |  | h |
| Approximant |  | ʋ |  |  | ɻ | j |  |  |
| Lateral approximant |  |  | l |  | ɭ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ | u uː ɯ |
| Close-mid | e eː |  | o oː |
| Open-mid | ɛ |  |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [ai] [au] [bʱ] [dʑʱ] [d̪ʱ] [ɖʱ] [ɡʱ].
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
| ⟨bh⟩ | [bʱ] |  |
| ⟨c⟩ | [tɕ] |  |
| ⟨ch⟩ | [tɕʰ] |  |
| ⟨d⟩ | [d̪] |  |
| ⟨dh⟩ | [d̪ʱ] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡʱ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʑ] |  |
| ⟨jh⟩ | [dʑʱ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t̪] |  |
| ⟨th⟩ | [t̪ʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [ʋ] |  |
| ⟨y⟩ | [j] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ĕ⟩ | [ɛ] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨ś⟩ | [ʃ] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ŭ⟩ | [ɨ] |  |
| ⟨ḍ⟩ | [ɖ] |  |
| ⟨ḍh⟩ | [ɖʱ] |  |
| ⟨ḷ⟩ | [ɭ] |  |
| ⟨ḻ⟩ | [ɻ] |  |
| ⟨ṅ⟩ | [ŋ] |  |
| ⟨ṇ⟩ | [ɳ] |  |
| ⟨ṣ⟩ | [ʂ] |  |
| ⟨ṭ⟩ | [ʈ] |  |
| ⟨ṭh⟩ | [ʈʰ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tcy")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tswana](tn.md) · [Home](../index.md) · [Tumbuka →](tum.md)
