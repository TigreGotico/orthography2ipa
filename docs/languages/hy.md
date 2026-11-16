# Armenian (`hy`)

<!-- atlas:summary begin -->
Armenian is an Armenic language, written in the Armenian script. Glottolog places it in 6 countries. The `hy` spec is at the research tier. It cites 1 source and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `hy` |
| ISO 639-3 | [hye](https://iso639-3.sil.org/code/hye), Armenian |
| Glottolog | [nucl1235](https://glottolog.org/resource/languoid/id/nucl1235), Eastern Armenian |
| Wikidata | [Q8785](https://www.wikidata.org/wiki/Q8785) |
| Wikipedia | [Armenian language](https://en.wikipedia.org/wiki/Armenian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Armenic](by-family.md#indo-european--armenic) |
| Region | [Eurasia](by-region.md#eurasia) > [Armenia](by-region.md#armenia), [Azerbaijan](by-region.md#azerbaijan), [Georgia](by-region.md#georgia), [Iran](by-region.md#iran), [Syria](by-region.md#syria), [Türkiye](by-region.md#türkiye) |
| Script | [Armenian](by-script.md#armenian) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 405, living |
| Parent | [Armenic](https://tigregotico.github.io/orthography2ipa/#x-clade-arme1241) `x-clade-arme1241` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`hy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#hy) |
| Spec file | [`hy.json`](../../orthography2ipa/data/hy.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Eastern Armenian (standard). Armenian alphabet (Aybuben) has 38 letters. Digraph ու = /u/. Letters ե and ո have positional allophones: word-initial ե = /jɛ/, medial = /ɛ/, word-initial ո = /vo/, medial = /o/. Aspirated stops (թ, չ, փ, ք, ց) vs plain voiced (բ, գ, դ) vs plain voiceless (կ, պ, տ).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2009. [Sources](#sources) lists them. The spec file writes all 39 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/hy.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `hy` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Western Armenian](hyw.md) `hyw`: Türkiye, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-dumtragut2009"></a>Dum-Tragut, Jasmine (2009). *Armenian: Modern Eastern Armenian*. London Oriental and African Language Library 14, John Benjamins. [doi.org](https://doi.org/10.1075/loall.14)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `hy` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 17734 | 0.1027 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `hy` | generated | epitran-derived | CC0 1.0 | 26671 | 0.0465 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 39 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ |  |  |
| Affricate |  |  | dz ts tsʰ | dʒ tʃ tʃʰ |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid |  |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Open |  |  | ɑ |

Sequences that the spec writes as one unit: [jɛ] [jɛv] [vo].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ա⟩ | [ɑ] |  |
| ⟨բ⟩ | [b] |  |
| ⟨գ⟩ | [ɡ] |  |
| ⟨դ⟩ | [d] |  |
| ⟨ե⟩ | [jɛ] | default [ɛ] · word initial [jɛ] |
| ⟨զ⟩ | [z] |  |
| ⟨է⟩ | [ɛ] |  |
| ⟨ը⟩ | [ə] |  |
| ⟨թ⟩ | [tʰ] |  |
| ⟨ժ⟩ | [ʒ] |  |
| ⟨ի⟩ | [i] |  |
| ⟨լ⟩ | [l] |  |
| ⟨խ⟩ | [χ] |  |
| ⟨ծ⟩ | [ts] |  |
| ⟨կ⟩ | [k] |  |
| ⟨հ⟩ | [h] |  |
| ⟨ձ⟩ | [dz] |  |
| ⟨ղ⟩ | [ʁ] |  |
| ⟨ճ⟩ | [tʃ] |  |
| ⟨մ⟩ | [m] |  |
| ⟨յ⟩ | [j] |  |
| ⟨ն⟩ | [n] |  |
| ⟨շ⟩ | [ʃ] |  |
| ⟨ո⟩ | [o] [vo] | default [o] · word initial [vo] |
| ⟨ու⟩ | [u] |  |
| ⟨չ⟩ | [tʃʰ] |  |
| ⟨պ⟩ | [p] |  |
| ⟨ջ⟩ | [dʒ] |  |
| ⟨ռ⟩ | [r] |  |
| ⟨ս⟩ | [s] |  |
| ⟨վ⟩ | [v] |  |
| ⟨տ⟩ | [t] |  |
| ⟨ր⟩ | [ɾ] |  |
| ⟨ց⟩ | [tsʰ] |  |
| ⟨փ⟩ | [pʰ] |  |
| ⟨ք⟩ | [kʰ] |  |
| ⟨օ⟩ | [o] |  |
| ⟨ֆ⟩ | [f] |  |
| ⟨և⟩ | [jɛv] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "hy")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Aranese](oc-x-aranes.md) · [Home](../index.md) · [Aromanian →](rup.md)
