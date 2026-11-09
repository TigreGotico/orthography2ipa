# Western Punjabi (Shahmukhi) (`pnb-PK`)

<!-- atlas:summary begin -->
Western Punjabi (Shahmukhi) is an Indo-Aryan language, written in the Arabic script. Its code names Pakistan. The `pnb-PK` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pnb-PK` |
| Aliases | `pa-PK`, `pnb` |
| ISO 639-3 | [pnb](https://iso639-3.sil.org/code/pnb), Western Panjabi |
| Glottolog | [west2386](https://glottolog.org/resource/languoid/id/west2386), Western Panjabi |
| Wikipedia | [Punjabi language](https://en.wikipedia.org/wiki/Punjabi_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Pakistan](by-region.md#pakistan) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Punjabi](pa.md) `pa` |
| Explorer | [`pnb-PK` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pnb-PK) |
| Spec file | [`pnb-PK.json`](../../orthography2ipa/data/pnb-PK.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Western Punjabi written in Shahmukhi (Perso-Arabic/Nastaliq) script. Phonological system closely parallels Eastern Punjabi (Gurmukhi) but with stronger Persian/Arabic lexical stratum introducing /f q x ɣ z ʒ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1972 to 2003. [Sources](#sources) lists them. The spec file writes all 57 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pnb-PK.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pnb-PK` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-shackle2003"></a>Shackle, C. (2003). *Panjabi*. Routledge (in Cardona & Jain, The Indo-Aryan Languages). Cited: 581, 621.
2. <a id="src-bhatia1993"></a>Bhatia, T.K. (1993). *Punjabi: A Cognitive-Descriptive Grammar*. Routledge.
3. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
4. <a id="src-shackle1972"></a>Shackle, C. (1972). *Punjabi*. University of London Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 68 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ | q | ʔ |
| Affricate |  |  |  | dʒ tʃ tʃʰ |  |  |  |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Tap |  |  | ɾ |  | ɽ |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ |  |  | x ɣ |  | h ɦ |
| Approximant |  | ʋ |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  | ɭ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | eː |  | oː |
| Mid |  | ə |  |
| Open-mid | ɛː |  | ɔː |
| Open | aː |  |  |

Sequences that the spec writes as one unit: [b˩] [dʒ˩] [d̪˩] [k˩] [k˩ə] [p˩] [p˩ə] [tʃ˩] [tʃ˩ə] [t̪˩] [t̪˩ə] [w] [ɖ˩] [ən] [ɡ˩] [ʈ˩] [ʈ˩ə] [̃].

Tones: [H] high-rising tone (historically from voiceless aspirate onset), [L] low-falling tone (historically from voiced aspirate onset), [M] level/mid tone (default; no special onset).
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨آ⟩ | [aː] |  |
| ⟨ا⟩ | [ə] [aː] |  |
| ⟨ب⟩ | [b] |  |
| ⟨بھ⟩ | [b] |  |
| ⟨ت⟩ | [t̪] |  |
| ⟨تھ⟩ | [t̪ʰ] |  |
| ⟨ث⟩ | [s] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨جھ⟩ | [dʒ] |  |
| ⟨ح⟩ | [h] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d̪] |  |
| ⟨دھ⟩ | [d̪] |  |
| ⟨ذ⟩ | [z] |  |
| ⟨ر⟩ | [r] |  |
| ⟨رھ⟩ | [r] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [s] |  |
| ⟨ض⟩ | [z] |  |
| ⟨ط⟩ | [t̪] |  |
| ⟨ظ⟩ | [z] |  |
| ⟨ع⟩ | [ʔ] ∅ |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [q] [k] |  |
| ⟨ل⟩ | [l] |  |
| ⟨لھ⟩ | [l] |  |
| ⟨م⟩ | [m] |  |
| ⟨مھ⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨نھ⟩ | [n] |  |
| ⟨و⟩ | [ʋ] [oː] [uː] [ɔː] |  |
| ⟨ً⟩ | [ən] |  |
| ⟨َ⟩ | [ə] |  |
| ⟨ُ⟩ | [u] |  |
| ⟨ِ⟩ | [i] |  |
| ⟨ٹ⟩ | [ʈ] |  |
| ⟨ٹھ⟩ | [ʈʰ] |  |
| ⟨پ⟩ | [p] |  |
| ⟨پھ⟩ | [pʰ] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨چھ⟩ | [tʃʰ] |  |
| ⟨ڈ⟩ | [ɖ] |  |
| ⟨ڈھ⟩ | [ɖ] |  |
| ⟨ڑ⟩ | [ɖ] |  |
| ⟨ڑھ⟩ | [ɽ] |  |
| ⟨ژ⟩ | [ʒ] |  |
| ⟨ک⟩ | [k] |  |
| ⟨کھ⟩ | [kʰ] |  |
| ⟨گ⟩ | [ɡ] |  |
| ⟨گھ⟩ | [ɡ] |  |
| ⟨ں⟩ | [̃] |  |
| ⟨ھ⟩ | [ɦ] |  |
| ⟨ی⟩ | [j] [iː] [eː] |  |
| ⟨ے⟩ | [eː] [ɛː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 54 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `PA_DH_INITIAL_ɡ˩_0` | /ɡ˩ə/ → [k˩ə], word-initially | - | [Shackle 2003](#src-shackle2003), [Bhatia 1993](#src-bhatia1993), Kanwal & Ritchart 2015 |
| `PA_DH_INITIAL_ɡ˩_1` | /ɡ˩/ → [k˩], word-initially | - | - |
| `PA_DH_INITIAL_dʒ˩_0` | /dʒ˩ə/ → [tʃ˩ə], word-initially | - | - |
| `PA_DH_INITIAL_dʒ˩_1` | /dʒ˩/ → [tʃ˩], word-initially | - | - |
| `PA_DH_INITIAL_ɖ˩_0` | /ɖ˩ə/ → [ʈ˩ə], word-initially | - | - |
| `PA_DH_INITIAL_ɖ˩_1` | /ɖ˩/ → [ʈ˩], word-initially | - | - |
| `PA_DH_INITIAL_d̪˩_0` | /d̪˩ə/ → [t̪˩ə], word-initially | - | - |
| `PA_DH_INITIAL_d̪˩_1` | /d̪˩/ → [t̪˩], word-initially | - | - |
| `PA_DH_INITIAL_b˩_0` | /b˩ə/ → [p˩ə], word-initially | - | - |
| `PA_DH_INITIAL_b˩_1` | /b˩/ → [p˩], word-initially | - | - |
| `PA_SCHWA_FINAL_b` | /bə/ → [b], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_b˩` | /b˩ə/ → [b˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_dʒ` | /dʒə/ → [dʒ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_dʒ˩` | /dʒ˩ə/ → [dʒ˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_d̪` | /d̪ə/ → [d̪], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_d̪˩` | /d̪˩ə/ → [d̪˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_f` | /fə/ → [f], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_j` | /jə/ → [j], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_k` | /kə/ → [k], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_kʰ` | /kʰə/ → [kʰ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_k˩` | /k˩ə/ → [k˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_l` | /lə/ → [l], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_m` | /mə/ → [m], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_n` | /nə/ → [n], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_p` | /pə/ → [p], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_pʰ` | /pʰə/ → [pʰ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_p˩` | /p˩ə/ → [p˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_q` | /qə/ → [q], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_s` | /sə/ → [s], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_tʃ` | /tʃə/ → [tʃ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_tʃʰ` | /tʃʰə/ → [tʃʰ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_tʃ˩` | /tʃ˩ə/ → [tʃ˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_t̪` | /t̪ə/ → [t̪], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_t̪˩` | /t̪˩ə/ → [t̪˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_x` | /xə/ → [x], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_z` | /zə/ → [z], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ŋ` | /ŋə/ → [ŋ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɖ` | /ɖə/ → [ɖ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɖ˩` | /ɖ˩ə/ → [ɖ˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɡ` | /ɡə/ → [ɡ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɡ˩` | /ɡ˩ə/ → [ɡ˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɣ` | /ɣə/ → [ɣ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɦ` | /ɦə/ → [ɦ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɭ` | /ɭə/ → [ɭ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɲ` | /ɲə/ → [ɲ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɳ` | /ɳə/ → [ɳ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɽ` | /ɽə/ → [ɽ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ɾ` | /ɾə/ → [ɾ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ʃ` | /ʃə/ → [ʃ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ʈ` | /ʈə/ → [ʈ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ʈʰ` | /ʈʰə/ → [ʈʰ], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ʈ˩` | /ʈ˩ə/ → [ʈ˩], not word-initially, word-finally | - | - |
| `PA_SCHWA_FINAL_ʋ` | /ʋə/ → [ʋ], not word-initially, word-finally | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pnb-PK")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Western Galician](gl-ES-x-occident.md) · [Home](../index.md) · [Wiyot →](wiy.md)
