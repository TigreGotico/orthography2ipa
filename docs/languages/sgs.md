# Samogitian (`sgs`)

<!-- atlas:summary begin -->
Samogitian is a Balto-Slavic language, written in the Latin script. Glottolog places it in Lithuania. The `sgs` spec is at the research tier. It cites 1 source and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sgs` |
| ISO 639-3 | [sgs](https://iso639-3.sil.org/code/sgs), Samogitian |
| Glottolog | [samo1265](https://glottolog.org/resource/languoid/id/samo1265), Samogitian |
| Wikidata | [Q213434](https://www.wikidata.org/wiki/Q213434) |
| Wikipedia | [Samogitian dialect](https://en.wikipedia.org/wiki/Samogitian_dialect) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic](by-family.md#indo-european--balto-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Lithuania](by-region.md#lithuania) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Balto-Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-balt1263) `x-clade-balt1263` |
| Explorer | [`sgs` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sgs) |
| Spec file | [`sgs.json`](../../orthography2ipa/data/sgs.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Samogitian (žemaitėška / žemaitiu kalba), an East Baltic variety of north-western Lithuania, treated by some as a dialect of Lithuanian and by others as a separate language.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 1 work, from 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sgs.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sgs` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-samogitian_dialect_wiki"></a>Wikipedia contributors (2026). *Samogitian dialect*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Samogitian_dialect)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 30 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | ts | tʃ |  |  |
| Nasal | m |  | n |  |  |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [z] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ė⟩ | [eː] |  |
| ⟨ė̄⟩ | [eː] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ž⟩ | [ʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sgs")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Samoan](sm.md) · [Home](../index.md) · [Sanabrese →](ast-x-sanabria.md)
