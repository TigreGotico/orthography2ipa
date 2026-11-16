# Waigali (`wbk`)

<!-- atlas:summary begin -->
Waigali is an Indo-Iranian language, written in the Latin script. Glottolog places it in the Eurasia, Papunesia and South America macroareas. The `wbk` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `wbk` |
| ISO 639-3 | [wbk](https://iso639-3.sil.org/code/wbk), Waigali |
| Wikipedia | [Waigali language](https://en.wikipedia.org/wiki/Waigali_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian](by-family.md#indo-european--indo-iranian) |
| Region | [Eurasia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Indo-Iranian](https://tigregotico.github.io/orthography2ipa/#x-clade-indo1320) `x-clade-indo1320` |
| Explorer | [`wbk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#wbk) |
| Spec file | [`wbk.json`](../../orthography2ipa/data/wbk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Waigali (Kalasha-ala), a Nuristani (Indo-European) language of Afghanistan.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1998 to 2024. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/wbk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `wbk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wbk_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Nuristani Kalasha (waig1243)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/waig1243)
2. <a id="src-wbk_wikipedia"></a>Wikipedia contributors (2024). *Waigali language*. Wikipedia.
3. <a id="src-wbk_degener1998"></a>Degener, Almuth (1998). *Die Sprache von Nisheygram im afghanischen Hindukusch*. Harrassowitz Verlag.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `wbk` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 153 | 0.2022 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 40 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d̪ t̪ |  | ɖ ʈ |  | k ɡ | q |  |
| Affricate |  | ts | dʒ tʃ |  |  |  |  |  |
| Nasal | m | n |  | ɳ |  | ŋ |  |  |
| Trill |  | r |  |  |  |  |  |  |
| Tap |  |  |  | ɽ |  |  |  |  |
| Fricative |  | s z | ʃ ʒ | ʂ ʐ |  | x ɣ |  | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d̪] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t̪] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ž⟩ | [ʒ] |  |
| ⟨ǰ⟩ | [dʒ] |  |
| ⟨ɣ⟩ | [ɣ] |  |
| ⟨ḍ⟩ | [ɖ] |  |
| ⟨ṇ⟩ | [ɳ] |  |
| ⟨ṛ⟩ | [ɽ] |  |
| ⟨ṣ⟩ | [ʂ] |  |
| ⟨ṭ⟩ | [ʈ] |  |
| ⟨ẓ⟩ | [ʐ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "wbk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Võro](vro.md) · [Home](../index.md) · [Walloon →](wa.md)
