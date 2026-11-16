# Ottoman Turkish (1500-1928) (`ota`)

<!-- atlas:summary begin -->
Ottoman Turkish (1500-1928) is a Turkic language, written in the Arabic script. Glottolog places it in the Eurasia macroarea. The `ota` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ota` |
| ISO 639-3 | [ota](https://iso639-3.sil.org/code/ota), Ottoman Turkish (1500-1928) |
| Wikipedia | [Ottoman Turkish](https://en.wikipedia.org/wiki/Ottoman_Turkish) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Turkish](tr.md) `tr` |
| Explorer | [`ota` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ota) |
| Spec file | [`ota.json`](../../orthography2ipa/data/ota.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ottoman Turkish, the Perso-Arabic-script form of Turkish written until the 1928 alphabet reform.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1992 to 2025. [Sources](#sources) lists them. The spec file writes all 49 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ota.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ota` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ota_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Ottoman Turkish (otto1234)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/otto1234)
2. <a id="src-ota_wikipedia"></a>Wikipedia contributors (2024). *Ottoman Turkish alphabet*. Wikipedia.
3. <a id="src-ota_zimmer_orgun"></a>Zimmer, K. & Orgun, O. (1992). *Turkish (Illustrations of the IPA)*. Journal of the International Phonetic Association.
4. <a id="src-ota_goksel_kerslake"></a>Göksel, A. & Kerslake, C. (2005). *Turkish: A Comprehensive Grammar*. Routledge.
5. <a id="src-ota_unicode_arabic_chart"></a>The Unicode Consortium (2025). *The Unicode Standard 17.0, code chart: Arabic (Range 0600-06FF)*. Unicode, Inc. [unicode.org](https://www.unicode.org/charts/PDF/U0600.pdf)
6. <a id="src-ota_jaf_kayhan2021"></a>Jaf, A. A. & Koc Kayhan, S. (2021). *Machine-Based Transliterate of Ottoman to Latin-Based Script*. Scientific Programming 2021: 7152935. [doi.org](https://doi.org/10.1155/2021/7152935)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ota` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 161 | 0.3536 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c ɟ | k ɡ | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l ɫ |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e | o |
| Open-mid | œ |  |
| Open | a aː |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ء⟩ | [ʔ] |  |
| ⟨آ⟩ | [a] [aː] |  |
| ⟨أ⟩ | [ʔ] |  |
| ⟨ؤ⟩ | [ʔ] |  |
| ⟨إ⟩ | [ʔ] |  |
| ⟨ئ⟩ | [ʔ] |  |
| ⟨ا⟩ | [a] | default [a] · word initial [e] [a] [i] [ɯ] |
| ⟨ب⟩ | [b] |  |
| ⟨ة⟩ | [a] |  |
| ⟨ت⟩ | [t] |  |
| ⟨ث⟩ | [s] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨ح⟩ | [h] |  |
| ⟨خ⟩ | [h] [x] |  |
| ⟨د⟩ | [d] |  |
| ⟨ذ⟩ | [z] |  |
| ⟨ر⟩ | [ɾ] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [s] |  |
| ⟨ض⟩ | [d] |  |
| ⟨ط⟩ | [t] |  |
| ⟨ظ⟩ | [z] |  |
| ⟨ع⟩ | [ʔ] | default ∅ [ʔ] · word final ∅ |
| ⟨غ⟩ | [ɡ] [ɣ] ∅ |  |
| ⟨ـ⟩ | ∅ |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [k] |  |
| ⟨ك⟩ | [k] [c] [ɡ] [ɟ] [ŋ] |  |
| ⟨ل⟩ | [l] [ɫ] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨ه⟩ | [h] | default [h] · word final [e] [a] [h] |
| ⟨و⟩ | [v] [u] [o] | after vowel [v] · before vowel [v] · default [u] [o] [y] [œ] [v] · word initial [v] |
| ⟨ى⟩ | [j] [i] | after vowel [j] · before vowel [j] · default [i] [ɯ] [j] · word initial [j] |
| ⟨ي⟩ | [j] [i] | after vowel [j] · before vowel [j] · default [i] [ɯ] [j] · word initial [j] |
| ⟨َ⟩ | [e] |  |
| ⟨ُ⟩ | [u] |  |
| ⟨ِ⟩ | [i] |  |
| ⟨ْ⟩ | ∅ |  |
| ⟨پ⟩ | [p] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨ژ⟩ | [ʒ] |  |
| ⟨ک⟩ | [k] [c] [ɡ] [ɟ] [ŋ] |  |
| ⟨ڭ⟩ | [ŋ] |  |
| ⟨گ⟩ | [ɡ] [ɟ] |  |
| ⟨ی⟩ | [j] [i] | after vowel [j] · before vowel [j] · default [i] [ɯ] [j] · word initial [j] |
| ⟨‌⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 11 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `OTA_CARRIER_DROP_BEFORE_MATER` | /e a/ → ∅, word-initially, spelled ⟨ا⟩, before ⟨و⟩ ⟨ی⟩ ⟨ي⟩ ⟨ى⟩ | ⟨ایكیشر›⟩ [iciʃeɾ] | - |
| `OTA_YE_NUCLEUS_AFTER_DROPPED_CARRIER` | /j/ → [i], spelled ⟨ی⟩ ⟨ي⟩ ⟨ى⟩, after ⟨ا⟩, with more context in the spec | - | - |
| `OTA_VAV_NUCLEUS_AFTER_DROPPED_CARRIER` | /v/ → [o], spelled ⟨و⟩, after ⟨ا⟩, with more context in the spec | - | - |
| `OTA_YE_NUCLEUS_BACK_MEDIAL` | /i/ → [ɯ], spelled ⟨ی⟩ ⟨ي⟩ ⟨ى⟩, with more context in the spec | ⟨قیشله›⟩ [kɯʃɫa] | - |
| `OTA_ELIF_BACK` | /e/ → [a], spelled ⟨ا⟩, with more context in the spec | - | - |
| `OTA_HE_FINAL_BACK` | /e/ → [a], word-finally, spelled ⟨ه⟩, with more context in the spec | ⟨بالطه›⟩ [baɫta] | - |
| `OTA_VAV_FRONT` | /u/ → [y], spelled ⟨و⟩, with more context in the spec | ⟨یورك›⟩ [jyɾec] | - |
| `OTA_L_VELARIZED` | /l/ → [ɫ], after [a] [o] [u] [ɯ] | ⟨same l⟩ [l, ɫ] | - |
| `OTA_KEF_VELAR_NASAL` | /k/ → [ŋ], word-finally, spelled ⟨ك⟩ ⟨ک⟩, after ⟨و⟩ ⟨ا⟩, with more context in the spec | ⟨طوك›⟩ [doŋ] | - |
| `OTA_KEF_PALATAL_HARMONY` | /k/ → [c], spelled ⟨ك⟩ ⟨ک⟩, with more context in the spec | ⟨اكمك›⟩ [ecmec] | - |
| `OTA_GAF_PALATAL_HARMONY` | /ɡ/ → [ɟ], spelled ⟨گ⟩, with more context in the spec | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ota")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ossetian](os.md) · [Home](../index.md) · [Paiwan →](pwn.md)
