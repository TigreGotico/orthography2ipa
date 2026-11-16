# Central Kurdish (Sorani) (`ckb`)

<!-- atlas:summary begin -->
Central Kurdish (Sorani) is an Iranian language, written in the Arabic script. Glottolog places it in Iran and Iraq. The `ckb` spec is at the research tier. It cites 1 source and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ckb` |
| ISO 639-3 | [ckb](https://iso639-3.sil.org/code/ckb), Central Kurdish |
| Glottolog | [cent1972](https://glottolog.org/resource/languoid/id/cent1972), Central Kurdish |
| Wikidata | [Q36811](https://www.wikidata.org/wiki/Q36811) |
| Wikipedia | [Central Kurdish](https://en.wikipedia.org/wiki/Central_Kurdish) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Iranian](by-family.md#indo-european--indo-iranian--iranian) |
| Region | [Eurasia](by-region.md#eurasia) > [Iran](by-region.md#iran), [Iraq](by-region.md#iraq) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1920, living |
| Parent | [Iranian](https://tigregotico.github.io/orthography2ipa/#x-clade-iran1269) `x-clade-iran1269` |
| Explorer | [`ckb` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ckb) |
| Spec file | [`ckb.json`](../../orthography2ipa/data/ckb.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Central Kurdish / Sorani (کوردیی ناوەندی), the main Kurdish variety of Iraq and western Iran.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2016. [Sources](#sources) lists them. The spec file writes all 35 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ckb.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ckb` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-opengin2016"></a>Öpengin, Ergin (2016). *The Mukri Variety of Central Kurdish: Grammar, Texts, and Lexicon*. Semitica et Semitohamitica Berolinensia 19, Reichert Verlag. [doi.org](https://doi.org/10.29091/9783954906314)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ckb` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 972 | 0.2107 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ckb` | generated | epitran-derived | CC0 1.0 | 26140 | 0.2607 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q |  | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l ɫ |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | iː | uː |
| Near-close |  | ʊ |
| Close-mid | eː | oː |
| Open-mid | ɛ |  |
| Open | aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ئ⟩ | [ʔ] ∅ |  |
| ⟨ا⟩ | [aː] |  |
| ⟨ب⟩ | [b] |  |
| ⟨ت⟩ | [t] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨ح⟩ | [ħ] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d] |  |
| ⟨ر⟩ | [ɾ] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ع⟩ | [ʕ] |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [q] |  |
| ⟨ل⟩ | [l] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨ه⟩ | [h] |  |
| ⟨و⟩ | [ʊ] [w] |  |
| ⟨وو⟩ | [uː] |  |
| ⟨پ⟩ | [p] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨ڕ⟩ | [r] |  |
| ⟨ژ⟩ | [ʒ] |  |
| ⟨ڤ⟩ | [v] |  |
| ⟨ک⟩ | [k] |  |
| ⟨گ⟩ | [ɡ] |  |
| ⟨ڵ⟩ | [ɫ] |  |
| ⟨ھ⟩ | [h] |  |
| ⟨ۆ⟩ | [oː] |  |
| ⟨ی⟩ | [iː] [j] |  |
| ⟨ێ⟩ | [eː] |  |
| ⟨ە⟩ | [ɛ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ckb")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Central Galician](gl-ES-x-central.md) · [Home](../index.md) · [Central Nahuatl →](nhn.md)
