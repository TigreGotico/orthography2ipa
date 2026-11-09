# Khasi (`kha`)

<!-- atlas:summary begin -->
Khasi is an Austroasiatic language, written in the Latin script. Glottolog places it in Bangladesh and India. The `kha` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kha` |
| ISO 639-3 | [kha](https://iso639-3.sil.org/code/kha), Khasi |
| Glottolog | [khas1269](https://glottolog.org/resource/languoid/id/khas1269), Khasi |
| Wikidata | [Q33584](https://www.wikidata.org/wiki/Q33584) |
| Wikipedia | [Khasi language](https://en.wikipedia.org/wiki/Khasi_language) |
| Family | [Austroasiatic](by-family.md#austroasiatic) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [India](by-region.md#india) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Ancestor | [Proto-Mon-Khmer (reconstructed)](https://tigregotico.github.io/orthography2ipa/#kha-x-proto-mon-khmer) `kha-x-proto-mon-khmer` |
| Explorer | [`kha` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kha) |
| Spec file | [`kha.json`](../../orthography2ipa/data/kha.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Khasi (Meghalaya, India). Austroasiatic, Mon-Khmer branch, unrelated to IA, Dravidian, or Munda. One of only two scheduled languages not from IA or Dravidian families. Written in Latin script since Welsh/British missionary period (1840s). Matrilineal society, shares phonological typology with Southeast Asian Mon-Khmer.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1961 to 1985. [Sources](#sources) lists them. The spec file writes all 34 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kha.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kha` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-rabel1961"></a>Rabel, L. (1961). *Khasi: A Language of Assam*. Louisiana State University Press.
2. <a id="src-nagaraja1985"></a>Nagaraja, K.S. (1985). *Khasi: A Descriptive Analysis*. Deccan College.
3. <a id="src-diffloth1974"></a>Diffloth, G. (1974). *Austro-Asiatic Languages*. Encyclopaedia Britannica.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ | d t tʰ |  |  | k kʰ ɡ | ʔ |
| Affricate |  |  | dʒ |  |  |  |
| Nasal | m | n |  | ɲ | ŋ |  |
| Trill |  | r |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ai] [au] [dʒŋ] [ia] [oi] [ui] [w] [ŋk].
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
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ia] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨jng⟩ | [dʒŋ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oi] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨ui⟩ | [ui] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [ə] [ʔ] |  |
| ⟨ï⟩ | [j] |  |
| ⟨ñ⟩ | [ɲ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kha")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Khanty](kca.md) · [Home](../index.md) · [Khiamniungan Naga →](kix.md)
