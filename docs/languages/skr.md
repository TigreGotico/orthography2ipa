# Saraiki (`skr`)

<!-- atlas:summary begin -->
Saraiki is an Indo-Aryan language, written in the Arabic script. Glottolog places it in India and Pakistan. The `skr` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `skr` |
| ISO 639-3 | [skr](https://iso639-3.sil.org/code/skr), Saraiki |
| Glottolog | [sera1259](https://glottolog.org/resource/languoid/id/sera1259), Saraiki |
| Wikidata | [Q33902](https://www.wikidata.org/wiki/Q33902) |
| Wikipedia | [Saraiki language](https://en.wikipedia.org/wiki/Saraiki_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india), [Pakistan](by-region.md#pakistan) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Indo-Aryan](https://tigregotico.github.io/orthography2ipa/#x-clade-indo1321) `x-clade-indo1321` |
| Explorer | [`skr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#skr) |
| Spec file | [`skr.json`](../../orthography2ipa/data/skr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Saraiki (سرائیکی) written in the Saraiki Shahmukhi alphabet standardised by the Anjuman Taraqqi-e-Saraiki, an extension of the Urdu Perso-Arabic abjad.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1976 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 51 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/skr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `skr` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-skr_wiki"></a>Wikipedia contributors (2024). *Saraiki language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Saraiki_language)
2. <a id="src-phoible"></a>Moran, Steven & McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/)
3. <a id="src-shackle1976"></a>Shackle, Christopher (1976). *The Siraiki Language of Central Pakistan: A Reference Grammar*. School of Oriental and African Studies.
4. <a id="src-bashir_conners2019"></a>Bashir, Elena & Conners, Thomas J. (2019). *A Descriptive Grammar of Hindko, Panjabi, and Saraiki*. De Gruyter Mouton. DOI [10.1515/9781614512257](https://doi.org/10.1515/9781614512257)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `skr` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 309 | 0.2869 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 49 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | ɖ ʈ |  | k ɡ | q | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |  |
| Nasal | m |  | n |  | ɳ |  | ŋ |  |  |
| Tap |  |  | ɾ |  | ɽ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | x ɣ |  | h |
| Approximant |  |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː |  | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | eː |  | oː |
| Mid |  | ə |  |
| Open | aː |  | ɑː |

Sequences that the spec writes as one unit: [eːv] [iːv] [oːv] [uːv] [ŋɡ] [ɓ] [ɗ] [ɠ] [ʄ] [ʰ] [̃].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ء⟩ | [ʔ] |  |
| ⟨آ⟩ | [aː] [ɑː] |  |
| ⟨ؤ⟩ | ∅ [v] |  |
| ⟨ئ⟩ | ∅ [j] |  |
| ⟨ا⟩ | [aː] [ɑː] | default [aː] [ɑː] · word initial [ə] [ʊ] [ɪ] |
| ⟨ب⟩ | [b] |  |
| ⟨ت⟩ | [t] |  |
| ⟨ث⟩ | [s] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨ح⟩ | [h] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d] |  |
| ⟨ذ⟩ | [z] |  |
| ⟨ر⟩ | [ɾ] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [s] |  |
| ⟨ض⟩ | [z] |  |
| ⟨ط⟩ | [t] |  |
| ⟨ظ⟩ | [z] |  |
| ⟨ع⟩ | [ʔ] |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [q] |  |
| ⟨ل⟩ | [l] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨نگ⟩ | [ŋɡ] |  |
| ⟨و⟩ | [v] [uː] [oː] | after consonant [oː] [uː] · default [v] [uː] [oː] · word final [uː] [oː] · word initial [v] |
| ⟨وو⟩ | [oːv] [uːv] |  |
| ⟨ٹ⟩ | [ʈ] |  |
| ⟨ٻ⟩ | [ɓ] |  |
| ⟨پ⟩ | [p] |  |
| ⟨ڄ⟩ | [ʄ] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨ڈ⟩ | [ɖ] |  |
| ⟨ڑ⟩ | [ɽ] |  |
| ⟨ژ⟩ | [ʒ] |  |
| ⟨ک⟩ | [k] |  |
| ⟨گ⟩ | [ɡ] |  |
| ⟨ڳ⟩ | [ɠ] |  |
| ⟨ں⟩ | [̃] |  |
| ⟨ھ⟩ | [ʰ] |  |
| ⟨ہ⟩ | [h] |  |
| ⟨ہہ⟩ | [h] |  |
| ⟨ی⟩ | [j] [iː] [eː] | after consonant [eː] [iː] · default [j] [iː] [eː] · word final [iː] [eː] · word initial [j] |
| ⟨یو⟩ | [iːv] [eːv] |  |
| ⟨ے⟩ | [eː] |  |
| ⟨ݙ⟩ | [ɗ] |  |
| ⟨ݨ⟩ | [ɳ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "skr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Santali](sat.md) · [Home](../index.md) · [Sardinian →](sc.md)
