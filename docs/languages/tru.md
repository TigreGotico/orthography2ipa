# Turoyo (`tru`)

<!-- atlas:summary begin -->
Turoyo is a Central Semitic language, written in the Syriac script. Glottolog places it in the Africa and Eurasia macroareas. The `tru` spec is at the research tier. It cites 8 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tru` |
| ISO 639-3 | [tru](https://iso639-3.sil.org/code/tru), Turoyo |
| Wikipedia | [Turoyo language](https://en.wikipedia.org/wiki/Turoyo_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Africa](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas) |
| Script | [Syriac](by-script.md#syriac) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Central Semitic](https://tigregotico.github.io/orthography2ipa/#x-clade-cent2236) `x-clade-cent2236` |
| Explorer | [`tru` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tru) |
| Spec file | [`tru.json`](../../orthography2ipa/data/tru.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Turoyo (Ṣurayt), a modern Semitic (Afroasiatic, Central Neo-Aramaic) language written in the Syriac abjad. Consonant letters are mapped to their base IPA values.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 8 works, from 1987 to 2025. [Sources](#sources) lists them. The spec file writes all 24 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tru.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tru` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 8 works. 7 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-tru_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Turoyo (turo1239)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/turo1239)
2. <a id="src-tru_wikipedia"></a>Wikipedia contributors (2024). *Turoyo language*. Wikipedia.
3. <a id="src-tru_jastrow_1987"></a>Jastrow, Otto (1987). *The Turoyo Language Today*. Journal of Assyrian Academic Studies, vol. 1. Cited: 10. [web.archive.org](https://web.archive.org/web/20200715114314/http://www.jaas.org/edocs/v1/jastrow.pdf)
4. <a id="src-tru_unicode_syriac_block"></a>Unicode Consortium (2025). *The Unicode Standard, Version 17.0: Syriac (Range 0700-074F)*. Unicode, Inc. Cited: 64. [unicode.org](https://www.unicode.org/charts/PDF/U0700.pdf)
5. <a id="src-tru_talay_slomo_surayt"></a>Talay, Shabo (ed.) (2017). *Šlomo Surayt: An Introductory Course to Surayt-Aramaic (Turoyo)*. Bar Hebraeus Verlag / Aramaic Online Project (Erasmus+). Cited: Level A, Lesson 4.3 (nouns), Online Course 5.1 (glossary). [textbook.surayt.com](https://textbook.surayt.com/en/Level%20A/4.3)
6. <a id="src-tru_kalin_2020"></a>Kalin, Laura (2020). *Morphology before phonology: A case study of Turoyo (Neo-Aramaic)*. Morphology (Springer), doi:10.1007/s11525-020-09365-3. Cited: example (7). [ling.auf.net](https://ling.auf.net/lingbuzz/004258)
7. <a id="src-tru_unicode_core_syriac"></a>Unicode Consortium (2025). *The Unicode Standard, Version 17.0, Chapter 9: Middle East-I (Modern and Liturgical Scripts)*. Unicode, Inc. Cited: §9.2.3, §9.3.1. [unicode.org](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-9/)
8. <a id="src-tru_surayt_orthography"></a>Aramaic-Online Project (Erasmus+) (2017). *Surayt Orthography*. Erasmus+ Aramaic-Online Project (2014-2017), Freie Universität Berlin. Cited: 7, 23. [userblogs.fu-berlin.de](https://userblogs.fu-berlin.de/saop/files/2017/08/Surayt-Orthography.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `tru` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 168 | 0.3607 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t tˤ |  |  | k ɡ | q |  | ʔ |
| Affricate |  |  | d͡ʒ |  |  |  |  |  |
| Nasal | m | n |  |  |  |  |  |  |
| Trill |  | r |  |  |  |  |  |  |
| Fricative |  | s sˤ z | ʃ |  |  |  | ħ ʕ | h |
| Approximant |  |  |  | j |  |  |  |  |
| Lateral approximant |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ـ⟩ | ∅ |  |
| ⟨ܐ⟩ | [ʔ] | word final [o] [e] [ʔ] |
| ⟨ܒ⟩ | [b] |  |
| ⟨ܓ⟩ | [ɡ] |  |
| ⟨ܔ⟩ | [d͡ʒ] |  |
| ⟨ܕ⟩ | [d] |  |
| ⟨ܗ⟩ | [h] |  |
| ⟨ܘ⟩ | [u] [w] [o] | word initial [w] |
| ⟨ܙ⟩ | [z] |  |
| ⟨ܚ⟩ | [ħ] |  |
| ⟨ܛ⟩ | [tˤ] |  |
| ⟨ܝ⟩ | [i] [j] [e] | word initial [j] |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tru")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Turkmen](tk.md) · [Home](../index.md) · [Tuscan →](it-IT-x-toscana.md)
