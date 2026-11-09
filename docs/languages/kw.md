# Cornish (`kw`)

<!-- atlas:summary begin -->
Cornish is a Brythonic language, written in the Latin script. Glottolog places it in United Kingdom. The `kw` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kw` |
| ISO 639-3 | [cor](https://iso639-3.sil.org/code/cor), Cornish |
| Glottolog | [corn1251](https://glottolog.org/resource/languoid/id/corn1251), Cornish |
| Wikidata | [Q25289](https://www.wikidata.org/wiki/Q25289) |
| Wikipedia | [Cornish language](https://en.wikipedia.org/wiki/Cornish_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Celtic > Brythonic](by-family.md#indo-european--celtic--brythonic) |
| Region | [Eurasia](by-region.md#eurasia) > [United Kingdom](by-region.md#united-kingdom) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 400, living |
| Ancestor | [Common Brythonic](https://tigregotico.github.io/orthography2ipa/#xbr) `xbr` |
| Explorer | [`kw` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kw) |
| Spec file | [`kw.json`](../../orthography2ipa/data/kw.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cornish (Kernewek). Revived language, last native speaker died 1777. Revival since early 20th c., ~3,000 speakers (est. 2020). Three main revival orthographies: Kernewek Standard, Kernewek Unys, Spellyans. This spec follows revived Kernewek Standard pronunciation. Refs: George (1993), Brown (2001).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1992 to 1996. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kw.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kw` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-macaulay1992"></a>MacAulay, D. (ed.) (1992). *The Celtic Languages*. Cambridge University Press.
2. <a id="src-george1993"></a>George, K. (1993). *The Cornish Language and its Literature*. Routledge & Kegan Paul.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kw` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 602 | 0.2521 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Fricative |  | f v | ð θ | s z |  |  | x | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close |  |  | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | øː |  | oː |
| Mid |  | ə |  |
| Open-mid | œː ɛ |  | ɔ |
| Near-open | æ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w] [ʍ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [æ] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ð] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨eu⟩ | [œː] [øː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [x] [h] |  |
| ⟨h⟩ | [h] |  |
| ⟨hw⟩ | [ʍ] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [uː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [θ] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [ɪ] [ə] |  |
| ⟨z⟩ | [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kw")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Colombian Spanish](es-CO-x-costa.md) · [Home](../index.md) · [Corsican →](co.md)
