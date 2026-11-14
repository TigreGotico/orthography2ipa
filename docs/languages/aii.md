# Assyrian Neo-Aramaic (`aii`)

<!-- atlas:summary begin -->
Assyrian Neo-Aramaic is a Central Semitic language, written in the Syriac script. Glottolog places it in the Africa and Eurasia macroareas. The `aii` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `aii` |
| ISO 639-3 | [aii](https://iso639-3.sil.org/code/aii), Assyrian Neo-Aramaic |
| Wikipedia | [Assyrian Neo-Aramaic](https://en.wikipedia.org/wiki/Assyrian_Neo-Aramaic) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Africa](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas) |
| Script | [Syriac](by-script.md#syriac) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Central Semitic](https://tigregotico.github.io/orthography2ipa/#x-clade-cent2236) `x-clade-cent2236` |
| Explorer | [`aii` in the data explorer](https://tigregotico.github.io/orthography2ipa/#aii) |
| Spec file | [`aii.json`](../../orthography2ipa/data/aii.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Assyrian Neo-Aramaic (Suret), a modern Semitic (Afroasiatic, Northeastern Neo-Aramaic) language written in the East Syriac abjad.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1904 to 2024. [Sources](#sources) lists them. The spec file writes all 23 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/aii.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `aii` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-aii_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Assyrian Neo-Aramaic (assy1241)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/assy1241)
2. <a id="src-aii_khan_urmi"></a>Khan, Geoffrey (2016). *The Neo-Aramaic Dialect of the Assyrian Christians of Urmi*. Brill. [brill.com](https://brill.com/display/title/32908)
3. <a id="src-aii_odisho"></a>Odisho, Edward Y. (1988). *The Sound System of Modern Assyrian (Neo-Aramaic)*. Otto Harrassowitz.
4. <a id="src-aii_noldeke_syriac_grammar"></a>Nöldeke, Theodor (trans. Crichton, James A.) (1904). *Compendious Syriac Grammar*. Williams & Norgate. [archive.org](https://archive.org/details/CompendiousSyriacGrammar)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `aii` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4836 | 0.3758 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 44 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t tˤ |  |  | k ɡ | q |  | ʔ |
| Affricate |  |  |  |  | d͡ʒ t͡ʃ |  |  |  |  |  |
| Nasal | m |  |  | n |  |  |  |  |  |  |
| Trill |  |  |  | r |  |  |  |  |  |  |
| Fricative |  | f v | ð θ | s sˤ z | ʃ ʒ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | eː | o oː |
| Open | aː | ɑː |

Sequences that the spec writes as one unit: [uw] [uww] [w] [woː] [wuː].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ܐ⟩ | [ʔ] [ɑː] [aː] [eː] | word final [ɑː] [aː] [eː] · word initial [ʔ] |
| ⟨ܒ⟩ | [b] [w] [v] | word final [w] [v] [b] |
| ⟨ܓ⟩ | [ɡ] [d͡ʒ] [ɣ] | word final [ɣ] [ɡ] |
| ⟨ܕ⟩ | [d] [ð] | word final [ð] [d] |
| ⟨ܗ⟩ | [h] |  |
| ⟨ܘ⟩ | [uː] [u] [oː] [o] [w] | word final [oː] [uː] · word initial [w] |
| ⟨ܘܘ⟩ | [uw] [uww] | word initial [wuː] [woː] |
| ⟨ܙ⟩ | [z] [ʒ] |  |
| ⟨ܚ⟩ | [x] [ħ] |  |
| ⟨ܛ⟩ | [tˤ] |  |
| ⟨ܝ⟩ | [iː] [j] [eː] [i] | word final [iː] [j] · word initial [j] |
| ⟨ܟ⟩ | [k] [x] [t͡ʃ] | word final [x] [k] |
| ⟨ܠ⟩ | [l] |  |
| ⟨ܡ⟩ | [m] |  |
| ⟨ܢ⟩ | [n] |  |
| ⟨ܣ⟩ | [s] |  |
| ⟨ܥ⟩ | [ʕ] |  |
| ⟨ܦ⟩ | [p] [f] |  |
| ⟨ܨ⟩ | [sˤ] |  |
| ⟨ܩ⟩ | [q] |  |
| ⟨ܪ⟩ | [r] |  |
| ⟨ܫ⟩ | [ʃ] [ʒ] |  |
| ⟨ܬ⟩ | [t] [θ] | word final [θ] [t] |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "aii")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Assamese](as.md) · [Home](../index.md) · [Asturian →](ast.md)
