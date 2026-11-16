# Lao (`lo`)

<!-- atlas:summary begin -->
Lao is a Tai-Kadai language, written in the Lao script. Glottolog places it in Cambodia, Laos and Thailand. The `lo` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lo` |
| ISO 639-3 | [lao](https://iso639-3.sil.org/code/lao), Lao |
| Glottolog | [laoo1244](https://glottolog.org/resource/languoid/id/laoo1244), Lao |
| Wikidata | [Q9211](https://www.wikidata.org/wiki/Q9211) |
| Wikipedia | [Lao language](https://en.wikipedia.org/wiki/Lao_language) |
| Family | [Tai-Kadai](by-family.md#tai-kadai) |
| Region | [Eurasia](by-region.md#eurasia) > [Cambodia](by-region.md#cambodia), [Laos](by-region.md#laos), [Thailand](by-region.md#thailand) |
| Script | [Lao](by-script.md#lao) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [Proto-Tai-Kadai (family node)](https://tigregotico.github.io/orthography2ipa/#tai) `tai` |
| Explorer | [`lo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lo) |
| Spec file | [`lo.json`](../../orthography2ipa/data/lo.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lao, the Southwestern Tai language of Laos, written in its own Indic-derived abugida. The spec describes the Vientiane standard.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2007 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 66 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lo.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-enfield2007"></a>Enfield, N.J. (2007). *A Grammar of Lao*. Mouton de Gruyter.
2. <a id="src-lao_wiki"></a>Wikipedia contributors (2024). *Lao language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lao_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `kaikki` ([kaikki.org](https://kaikki.org/dictionary/)) | `lo` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2315 | 0.3570 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 46 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ p̚ |  | d t tʰ t̚ |  | k kʰ k̚ | ʔ |
| Affricate |  |  |  | tɕ |  |  |
| Nasal | m |  | n | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f | s |  |  | h |
| Approximant |  | ʋ |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː ɯ ɯː |
| Close-mid | eː | o oː |
| Open-mid | ɛː | ɔː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [aj] [am] [aw] [aʔ] [iːə] [uːə] [w] [ɔʔ] [ɯːə].

Tones: [low_class_no_mark] mid, [low_class_mai_ek] falling, [low_class_mai_tho] high, [mid_class_no_mark] low, [mid_class_mai_ek] low, [mid_class_mai_tho] mid, [high_class_no_mark] rising, [high_class_mai_ek] mid, [high_class_mai_tho] high.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ກ⟩ | [k] |  |
| ⟨ຂ⟩ | [kʰ] |  |
| ⟨ຄ⟩ | [kʰ] |  |
| ⟨ງ⟩ | [ŋ] |  |
| ⟨ຈ⟩ | [tɕ] |  |
| ⟨ຊ⟩ | [s] |  |
| ⟨ຍ⟩ | [ɲ] |  |
| ⟨ດ⟩ | [d] |  |
| ⟨ຕ⟩ | [t] |  |
| ⟨ຖ⟩ | [tʰ] |  |
| ⟨ທ⟩ | [tʰ] |  |
| ⟨ນ⟩ | [n] |  |
| ⟨ບ⟩ | [b] |  |
| ⟨ປ⟩ | [p] |  |
| ⟨ຜ⟩ | [pʰ] |  |
| ⟨ຝ⟩ | [f] |  |
| ⟨ພ⟩ | [pʰ] |  |
| ⟨ຟ⟩ | [f] |  |
| ⟨ມ⟩ | [m] |  |
| ⟨ຢ⟩ | [j] |  |
| ⟨ຣ⟩ | [l] |  |
| ⟨ລ⟩ | [l] |  |
| ⟨ວ⟩ | [ʋ] |  |
| ⟨ສ⟩ | [s] |  |
| ⟨ຫ⟩ | [h] |  |
| ⟨ຫງ⟩ | [ŋ] |  |
| ⟨ຫຍ⟩ | [ɲ] |  |
| ⟨ຫນ⟩ | [n] |  |
| ⟨ຫມ⟩ | [m] |  |
| ⟨ຫຣ⟩ | [l] |  |
| ⟨ຫລ⟩ | [l] |  |
| ⟨ຫວ⟩ | [ʋ] |  |
| ⟨ຫຼ⟩ | [l] |  |
| ⟨ອ⟩ | [ɔː] | word initial [ʔ] |
| ⟨ຮ⟩ | [h] |  |
| ⟨ະ⟩ | [aʔ] |  |
| ⟨ັ⟩ | [a] |  |
| ⟨າ⟩ | [aː] |  |
| ⟨າະ⟩ | [ɔʔ] |  |
| ⟨ຳ⟩ | [am] |  |
| ⟨ິ⟩ | [i] |  |
| ⟨ີ⟩ | [iː] |  |
| ⟨ຶ⟩ | [ɯ] |  |
| ⟨ຶອ⟩ | [ɯːə] |  |
| ⟨ື⟩ | [ɯː] |  |
| ⟨ືອ⟩ | [ɯːə] |  |
| ⟨ຸ⟩ | [u] |  |
| ⟨ູ⟩ | [uː] |  |
| ⟨ົ⟩ | [o] |  |
| ⟨ົວ⟩ | [uːə] |  |
| ⟨ົາ⟩ | [aw] |  |
| ⟨ຼ⟩ | [l] |  |
| ⟨ຽ⟩ | [iːə] |  |
| ⟨ເ⟩ | [eː] |  |
| ⟨ແ⟩ | [ɛː] |  |
| ⟨ໂ⟩ | [oː] |  |
| ⟨ໃ⟩ | [aj] |  |
| ⟨ໄ⟩ | [aj] |  |
| ⟨່⟩ | ∅ |  |
| ⟨້⟩ | ∅ |  |
| ⟨໊⟩ | ∅ |  |
| ⟨໋⟩ | ∅ |  |
| ⟨໌⟩ | ∅ |  |
| ⟨ໍ⟩ | [ɔː] |  |
| ⟨ໜ⟩ | [n] |  |
| ⟨ໝ⟩ | [m] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 6 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `LO_CODA_STOP_T` | /d t tʰ s/ → [t̚], in the coda | ⟨ວັດ⟩ [ʋat̚] | [Enfield 2007](#src-enfield2007) |
| `LO_CODA_STOP_P` | /b p pʰ f/ → [p̚], in the coda | - | [Enfield 2007](#src-enfield2007) |
| `LO_CODA_STOP_K` | /k kʰ/ → [k̚], in the coda | - | [Enfield 2007](#src-enfield2007) |
| `LO_CODA_NY_GLIDE` | /ɲ/ → [j], in the coda | - | [Enfield 2007](#src-enfield2007) |
| `LO_V_CODA_W` | /ʋ/ → [w], in the coda | - | [Enfield 2007](#src-enfield2007) |
| `LO_O_CARRIER` | /ɔː/ → [ʔ], before a vowel, spelled ⟨ອ⟩ | ⟨ອິດ⟩ [ʔit̚] | [Enfield 2007](#src-enfield2007) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lo")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lamboya](lmy.md) · [Home](../index.md) · [Lapurdian Basque →](eu-x-lapurdi.md)
