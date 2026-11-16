# Classical Syriac (`syc`)

<!-- atlas:summary begin -->
Classical Syriac is a Central Semitic language, written in the Syriac script. Glottolog places it in the Africa and Eurasia macroareas. The `syc` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `syc` |
| ISO 639-3 | [syc](https://iso639-3.sil.org/code/syc), Classical Syriac |
| Wikipedia | [Syriac language](https://en.wikipedia.org/wiki/Syriac_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Africa](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas) |
| Script | [Syriac](by-script.md#syriac) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Central Semitic](https://tigregotico.github.io/orthography2ipa/#x-clade-cent2236) `x-clade-cent2236` |
| Explorer | [`syc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#syc) |
| Spec file | [`syc.json`](../../orthography2ipa/data/syc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Classical Syriac, a Semitic (Afroasiatic, Central Semitic/Aramaic) language written in the Syriac abjad. The 22 consonant letters are mapped to their plosive (non-spirantized) IPA values.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1904 to 2024. [Sources](#sources) lists them. The spec file writes all 22 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/syc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `syc` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-syc_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Classical Syriac (clas1252)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/clas1252)
2. <a id="src-syc_noldeke_1904"></a>Nöldeke, Theodor (trans. James A. Crichton) (1904). *Compendious Syriac Grammar*. Williams & Norgate, London. Cited: §2 (pronunciation of the consonants), §4 (vowel expression by the vowel letters ܐ ܘ ܝ), §5 (apparent use of ܐ), §15, §23 (rukkakha and quššaya), Introduction pp. XXXII-XXXIII (Eastern and Western traditions). [archive.org](https://archive.org/stream/CompendiousSyriacGrammar/Compendious_Syriac_Grammar_djvu.txt)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `syc` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 96 | 0.3707 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 26 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t tˤ |  |  | k ɡ | q |  | ʔ |
| Nasal | m | n |  |  |  |  |  |  |
| Trill |  | r |  |  |  |  |  |  |
| Fricative |  | s sˤ z | ʃ |  |  |  | ħ ʕ | h |
| Approximant |  |  |  | j |  |  |  |  |
| Lateral approximant |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close |  | u |
| Close-mid | e | o |
| Open |  | ɑ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ܐ⟩ | [ʔ] | word final [ɑ] [e] [ʔ] |
| ⟨ܒ⟩ | [b] |  |
| ⟨ܓ⟩ | [ɡ] |  |
| ⟨ܕ⟩ | [d] |  |
| ⟨ܗ⟩ | [h] |  |
| ⟨ܘ⟩ | [u] [o] [w] | word initial [w] |
| ⟨ܙ⟩ | [z] |  |
| ⟨ܚ⟩ | [ħ] |  |
| ⟨ܛ⟩ | [tˤ] |  |
| ⟨ܝ⟩ | [j] |  |
| ⟨ܟ⟩ | [k] |  |
| ⟨ܠ⟩ | [l] |  |
| ⟨ܡ⟩ | [m] |  |
| ⟨ܢ⟩ | [n] |  |
| ⟨ܣ⟩ | [s] |  |
| ⟨ܥ⟩ | [ʕ] |  |
| ⟨ܦ⟩ | [p] |  |
| ⟨ܨ⟩ | [sˤ] |  |
| ⟨ܩ⟩ | [q] |  |
| ⟨ܪ⟩ | [r] |  |
| ⟨ܫ⟩ | [ʃ] |  |
| ⟨ܬ⟩ | [t] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "syc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Classical Nahuatl](nci.md) · [Home](../index.md) · [Coastal Dhofari Arabic →](adf-OM.md)
