# Maldivian (Dhivehi) (`dv`)

<!-- atlas:summary begin -->
Maldivian (Dhivehi) is an Indo-Aryan language, written in the Thaana script. Glottolog places it in India and Maldives. The `dv` spec is at the research tier. It cites 1 source and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `dv` |
| ISO 639-3 | [div](https://iso639-3.sil.org/code/div), Dhivehi |
| Glottolog | [dhiv1236](https://glottolog.org/resource/languoid/id/dhiv1236), Dhivehi |
| Wikidata | [Q32656](https://www.wikidata.org/wiki/Q32656) |
| Wikipedia | [Maldivian language](https://en.wikipedia.org/wiki/Maldivian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india), [Maldives](by-region.md#maldives) |
| Script | [Thaana](by-script.md#thaana) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [Indo-Aryan](https://tigregotico.github.io/orthography2ipa/#x-clade-indo1321) `x-clade-indo1321` |
| Explorer | [`dv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#dv) |
| Spec file | [`dv.json`](../../orthography2ipa/data/dv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Maldivian (Dhivehi, ދިވެހި), Indo-Aryan, written in the Thaana script. INPUT CONTRACT: native Thaana text (Unicode block U+0780..U+07B1, NFC), written RIGHT-TO-LEFT, the older Dhives Akuru script and the Malé Latin transliteration are out of scope.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2000. [Sources](#sources) lists them. The spec file writes all 51 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/dv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `dv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-cain2000"></a>Cain, Bruce D. (2000). *Dhivehi (Maldivian): A Synchronic and Diachronic Study*. Cornell University (PhD thesis).
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `dv` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1539 | 0.0891 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `dv` | generated | epitran-derived | CC0 1.0 | 16770 | 0.0801 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 49 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | dˤ d̪ tˤ t̪ |  | ɖ ʈ |  | k ɡ | q |  | ʔ |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |  |  |  |
| Nasal | m |  |  | n |  | ɳ | ɲ |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |  |  |  |
| Fricative |  | f | ð ðˤ θ | s sˤ z | ʃ ʒ | ʂ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  | ʋ |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l |  | ɭ |  |  |  |  |  |

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
| ⟨ހ⟩ | [h] |  |
| ⟨ށ⟩ | [ʂ] |  |
| ⟨ނ⟩ | [n] |  |
| ⟨ރ⟩ | [ɾ] |  |
| ⟨ބ⟩ | [b] |  |
| ⟨ޅ⟩ | [ɭ] |  |
| ⟨ކ⟩ | [k] |  |
| ⟨އ⟩ | ∅ [ʔ] |  |
| ⟨އް⟩ | [ʔ] |  |
| ⟨ވ⟩ | [ʋ] |  |
| ⟨މ⟩ | [m] |  |
| ⟨ފ⟩ | [f] |  |
| ⟨ދ⟩ | [d̪] |  |
| ⟨ތ⟩ | [t̪] |  |
| ⟨ލ⟩ | [l] |  |
| ⟨ގ⟩ | [ɡ] |  |
| ⟨ޏ⟩ | [ɲ] |  |
| ⟨ސ⟩ | [s] |  |
| ⟨ޑ⟩ | [ɖ] |  |
| ⟨ޒ⟩ | [z] |  |
| ⟨ޓ⟩ | [ʈ] |  |
| ⟨ޔ⟩ | [j] |  |
| ⟨ޕ⟩ | [p] |  |
| ⟨ޖ⟩ | [dʒ] |  |
| ⟨ޗ⟩ | [tʃ] |  |
| ⟨ޘ⟩ | [θ] |  |
| ⟨ޙ⟩ | [ħ] |  |
| ⟨ޚ⟩ | [x] |  |
| ⟨ޛ⟩ | [ð] |  |
| ⟨ޜ⟩ | [ʒ] |  |
| ⟨ޝ⟩ | [ʃ] |  |
| ⟨ޞ⟩ | [sˤ] |  |
| ⟨ޟ⟩ | [dˤ] |  |
| ⟨ޠ⟩ | [tˤ] |  |
| ⟨ޡ⟩ | [ðˤ] |  |
| ⟨ޢ⟩ | [ʕ] |  |
| ⟨ޣ⟩ | [ɣ] |  |
| ⟨ޤ⟩ | [q] |  |
| ⟨ޥ⟩ | [w] |  |
| ⟨ަ⟩ | [a] |  |
| ⟨ާ⟩ | [aː] |  |
| ⟨ި⟩ | [i] |  |
| ⟨ީ⟩ | [iː] |  |
| ⟨ު⟩ | [u] |  |
| ⟨ޫ⟩ | [uː] |  |
| ⟨ެ⟩ | [e] |  |
| ⟨ޭ⟩ | [eː] |  |
| ⟨ޮ⟩ | [o] |  |
| ⟨ޯ⟩ | [oː] |  |
| ⟨ް⟩ | ∅ |  |
| ⟨ޱ⟩ | [ɳ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "dv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Malayalam](ml.md) · [Home](../index.md) · [Malecite-Passamaquoddy →](pqm.md)
