# Mundari (`unr`)

<!-- atlas:summary begin -->
Mundari is an Austroasiatic language, written in the Latin script. Glottolog places it in Bangladesh, India and Nepal. The `unr` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `unr` |
| ISO 639-3 | [unr](https://iso639-3.sil.org/code/unr), Mundari |
| Glottolog | [mund1320](https://glottolog.org/resource/languoid/id/mund1320), Mundari |
| Wikidata | [Q3327828](https://www.wikidata.org/wiki/Q3327828) |
| Wikipedia | [Mundari language](https://en.wikipedia.org/wiki/Mundari_language) |
| Family | [Austroasiatic](by-family.md#austroasiatic) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [India](by-region.md#india), [Nepal](by-region.md#nepal) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Ancestor | [Proto-Munda (reconstructed)](https://tigregotico.github.io/orthography2ipa/#sat-x-proto-munda) `sat-x-proto-munda` |
| Explorer | [`unr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#unr) |
| Spec file | [`unr.json`](../../orthography2ipa/data/unr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Mundari (Jharkhand). Closely related to Santali. Written in Latin (linguistic convention) or Devanagari. Has some retroflex consonants from IA contact.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1974 to 2001. [Sources](#sources) lists them. The spec file writes all 38 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/unr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `unr` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-evans2001"></a>Evans, N. (2001). *Mundari*. in J. Garry & C. Rubino (eds.), Facts About the World's Languages.
2. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
3. <a id="src-diffloth1974"></a>Diffloth, G. (1974). *Austro-Asiatic Languages*. Encyclopaedia Britannica.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 38 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ | d t tʰ |  | ɖ |  | k kʰ ɡ | ʔ |
| Affricate |  |  | dʒ tʃ tʃʰ |  |  |  |  |
| Nasal | m | n |  | ɳ |  | ŋ |  |
| Trill |  | r |  |  |  |  |  |
| Fricative |  | s |  |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open-mid |  | ɔ |
| Open | a aː |  |

Sequences that the spec writes as one unit: [aˀ] [iˀ] [uˀ] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aʔ⟩ | [aˀ] |  |
| ⟨aː⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨ch⟩ | [tʃʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨eː⟩ | [eː] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨iʔ⟩ | [iˀ] |  |
| ⟨iː⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
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
| ⟨tʰ⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uʔ⟩ | [uˀ] |  |
| ⟨uː⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɖ⟩ | [ɖ] |  |
| ⟨ɳ⟩ | [ɳ] |  |
| ⟨ʔ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "unr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Moroccan Arabic](ary-MA.md) · [Home](../index.md) · [Muong →](mtq.md)
