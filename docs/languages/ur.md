# Urdu (`ur`)

<!-- atlas:summary begin -->
Urdu is an Indo-Aryan language, written in the Arabic script. Glottolog places it in Afghanistan, Bangladesh, India and Pakistan. The `ur` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ur` |
| ISO 639-3 | [urd](https://iso639-3.sil.org/code/urd), Urdu |
| Glottolog | [urdu1245](https://glottolog.org/resource/languoid/id/urdu1245), Urdu |
| Wikidata | [Q1617](https://www.wikidata.org/wiki/Q1617) |
| Wikipedia | [Urdu](https://en.wikipedia.org/wiki/Urdu) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Afghanistan](by-region.md#afghanistan), [Bangladesh](by-region.md#bangladesh), [India](by-region.md#india), [Pakistan](by-region.md#pakistan) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Hindi](hi.md) `hi` |
| Explorer | [`ur` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ur) |
| Spec file | [`ur.json`](../../orthography2ipa/data/ur.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Urdu (Pakistan national language, Indian Muslim register). Phonologically near-identical to Hindi but with additional phonemes from Persian/Arabic loans: /q x ɣ f z/. Written right-to-left in Nastaliq (a form of Perso-Arabic script). Four-way laryngeal contrast: plain/aspirated × voiced/voiceless.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1884 to 2003. [Sources](#sources) lists them. The spec file writes all 62 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ur.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ur` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 0 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-platts1884"></a>Platts, J.T. (1884). *A Grammar of the Hindustani or Urdu Language*. W.H. Allen.
4. <a id="src-ohala1999"></a>Ohala, M. (1999). *Hindi (Illustrations of the IPA)*. Handbook of the International Phonetic Association, Cambridge University Press.
5. <a id="src-shapiro2003"></a>Shapiro, M. (2003). *Hindi*. In Cardona & Jain (eds.), The Indo-Aryan Languages, Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ur` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 6296 | 0.3077 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 116 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ | q | ʔ |
| Affricate |  |  |  | dʒ tʃ tʃʰ |  |  |  |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Tap |  |  | ɾ |  | ɽ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ʂ |  | x ɣ |  | h ɦ |
| Approximant |  | ʋ |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː |  | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | eː |  | o oː |
| Mid |  | ə |  |
| Open-mid | ɛː |  | ɔː |
| Open | aː |  |  |

Sequences that the spec writes as one unit: [bə] [bʱ] [bʱə] [dʒə] [dʒɲ] [dʒɲə] [dʒʱ] [dʒʱə] [d̪ə] [d̪ʱ] [d̪ʱə] [fə] [jə] [kə] [kʃ] [kʃə] [kʰə] [lə] [lʱ] [mə] [mʱ] [nə] [nʱ] [pə] [pʰə] [qə] [sə] [tʃə] [tʃʰə] [t̪ə] [t̪ɾ] [t̪ɾə] [t̪ʰə] [w] [xə] [zə] [ŋə] [ɖə] [ɖʱ] [ɖʱə], and 26 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ء⟩ | [ʔ] ∅ |  |
| ⟨آ⟩ | [aː] |  |
| ⟨ؤ⟩ | [ʔ] [o] ∅ |  |
| ⟨ئ⟩ | [ʔ] [j] ∅ |  |
| ⟨ا⟩ | [aː] [ə] | default [aː] · word initial [ə] [ɪ] [ʊ] |
| ⟨ب⟩ | [b] |  |
| ⟨بھ⟩ | [bʱ] |  |
| ⟨ت⟩ | [t̪] |  |
| ⟨تھ⟩ | [t̪ʰ] |  |
| ⟨ث⟩ | [s] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨جھ⟩ | [dʒʱ] |  |
| ⟨ح⟩ | [ɦ] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d̪] |  |
| ⟨دھ⟩ | [d̪ʱ] |  |
| ⟨ذ⟩ | [z] |  |
| ⟨ر⟩ | [ɾ] [r] |  |
| ⟨رھ⟩ | [ɾʱ] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [s] |  |
| ⟨ض⟩ | [z] |  |
| ⟨ط⟩ | [t̪] |  |
| ⟨ظ⟩ | [z] |  |
| ⟨ع⟩ | ∅ [ʔ] | default ∅ [ʔ] · word initial [ə] [ɪ] [ʊ] |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [q] |  |
| ⟨ل⟩ | [l] |  |
| ⟨لھ⟩ | [lʱ] |  |
| ⟨م⟩ | [m] |  |
| ⟨مھ⟩ | [mʱ] |  |
| ⟨ن⟩ | [n] |  |
| ⟨نھ⟩ | [nʱ] |  |
| ⟨و⟩ | [ʋ] [oː] [uː] [ɔː] | after vowel [ʋ] · before vowel [ʋ] · default [uː] [oː] [ɔː] [ʋ] · word initial [ʋ] |
| ⟨ً⟩ | [ən] |  |
| ⟨َ⟩ | [ə] |  |
| ⟨ُ⟩ | [ʊ] |  |
| ⟨ِ⟩ | [ɪ] |  |
| ⟨ٹ⟩ | [ʈ] |  |
| ⟨ٹھ⟩ | [ʈʰ] |  |
| ⟨پ⟩ | [p] |  |
| ⟨پھ⟩ | [pʰ] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨چھ⟩ | [tʃʰ] |  |
| ⟨ڈ⟩ | [ɖ] |  |
| ⟨ڈھ⟩ | [ɖʱ] |  |
| ⟨ڑ⟩ | [ɽ] |  |
| ⟨ڑھ⟩ | [ɽʱ] |  |
| ⟨ژ⟩ | [ʒ] |  |
| ⟨ک⟩ | [k] |  |
| ⟨کھ⟩ | [kʰ] |  |
| ⟨گ⟩ | [ɡ] |  |
| ⟨گھ⟩ | [ɡʱ] |  |
| ⟨ں⟩ | [̃] |  |
| ⟨ھ⟩ | [ʰ] |  |
| ⟨ہ⟩ | [ɦ] | default [ɦ] · word final [aː] [eː] [ɦ] |
| ⟨ۂ⟩ | [eː] |  |
| ⟨ی⟩ | [j] [iː] [eː] | after vowel [j] · before vowel [j] · default [iː] [eː] [j] · word initial [j] |
| ⟨ے⟩ | [eː] [ɛː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 143 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `HI_SCHWA_FINAL_b` | /bə/ → [b], not word-initially, word-finally | ⟨शब्द⟩ [ʃəbd̪] | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_bʱ` | /bʱə/ → [bʱ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_dʒ` | /dʒə/ → [dʒ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_dʒɲ` | /dʒɲə/ → [dʒɲ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_dʒʱ` | /dʒʱə/ → [dʒʱ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_d̪` | /d̪ə/ → [d̪], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_f` | /fə/ → [f], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_j` | /jə/ → [j], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_k` | /kə/ → [k], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_kʃ` | /kʃə/ → [kʃ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_kʰ` | /kʰə/ → [kʰ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_l` | /lə/ → [l], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_m` | /mə/ → [m], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_n` | /nə/ → [n], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_p` | /pə/ → [p], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_pʰ` | /pʰə/ → [pʰ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_q` | /qə/ → [q], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_s` | /sə/ → [s], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_tʃ` | /tʃə/ → [tʃ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_tʃʰ` | /tʃʰə/ → [tʃʰ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_t̪` | /t̪ə/ → [t̪], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_t̪ɾ` | /t̪ɾə/ → [t̪ɾ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_x` | /xə/ → [x], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_z` | /zə/ → [z], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ŋ` | /ŋə/ → [ŋ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɖ` | /ɖə/ → [ɖ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɖʱ` | /ɖʱə/ → [ɖʱ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɡ` | /ɡə/ → [ɡ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɡj` | /ɡjə/ → [ɡj], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɡʱ` | /ɡʱə/ → [ɡʱ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɣ` | /ɣə/ → [ɣ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɦ` | /ɦə/ → [ɦ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɲ` | /ɲə/ → [ɲ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɳ` | /ɳə/ → [ɳ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɽ` | /ɽə/ → [ɽ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɽʱ` | /ɽʱə/ → [ɽʱ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɾ` | /ɾə/ → [ɾ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ɾɪ` | /ɾɪə/ → [ɾɪ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ʂ` | /ʂə/ → [ʂ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ʃ` | /ʃə/ → [ʃ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ʃɾ` | /ʃɾə/ → [ʃɾ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ʈ` | /ʈə/ → [ʈ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ʈʰ` | /ʈʰə/ → [ʈʰ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_FINAL_ʋ` | /ʋə/ → [ʋ], not word-initially, word-finally | - | [Ohala 1999](#src-ohala1999), Ohala 1983 |
| `HI_SCHWA_KEEP_b` | /bə/ → [bə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983, Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_bʱ` | /bʱə/ → [bʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_dʒ` | /dʒə/ → [dʒə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_dʒɲ` | /dʒɲə/ → [dʒɲə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_dʒʱ` | /dʒʱə/ → [dʒʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_d̪` | /d̪ə/ → [d̪ə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_d̪ʱ` | /d̪ʱə/ → [d̪ʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_f` | /fə/ → [fə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_j` | /jə/ → [jə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_k` | /kə/ → [kə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_kʃ` | /kʃə/ → [kʃə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_kʰ` | /kʰə/ → [kʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_l` | /lə/ → [lə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_m` | /mə/ → [mə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_n` | /nə/ → [nə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_p` | /pə/ → [pə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_pʰ` | /pʰə/ → [pʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_q` | /qə/ → [qə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_s` | /sə/ → [sə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_tʃ` | /tʃə/ → [tʃə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_tʃʰ` | /tʃʰə/ → [tʃʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_t̪` | /t̪ə/ → [t̪ə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_t̪ɾ` | /t̪ɾə/ → [t̪ɾə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_t̪ʰ` | /t̪ʰə/ → [t̪ʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_x` | /xə/ → [xə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_z` | /zə/ → [zə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ŋ` | /ŋə/ → [ŋə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɖ` | /ɖə/ → [ɖə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɖʱ` | /ɖʱə/ → [ɖʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɡ` | /ɡə/ → [ɡə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɡj` | /ɡjə/ → [ɡjə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɡʱ` | /ɡʱə/ → [ɡʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɣ` | /ɣə/ → [ɣə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɦ` | /ɦə/ → [ɦə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɲ` | /ɲə/ → [ɲə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɳ` | /ɳə/ → [ɳə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɽ` | /ɽə/ → [ɽə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɽʱ` | /ɽʱə/ → [ɽʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɾ` | /ɾə/ → [ɾə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ɾɪ` | /ɾɪə/ → [ɾɪə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ʂ` | /ʂə/ → [ʂə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ʃ` | /ʃə/ → [ʃə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ʃɾ` | /ʃɾə/ → [ʃɾə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ʈ` | /ʈə/ → [ʈə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ʈʰ` | /ʈʰə/ → [ʈʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_KEEP_ʋ` | /ʋə/ → [ʋə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983 |
| `HI_SCHWA_MEDIAL_b` | /bə/ → [b], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Ohala 1983, Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_bʱ` | /bʱə/ → [bʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_dʒ` | /dʒə/ → [dʒ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_dʒɲ` | /dʒɲə/ → [dʒɲ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_dʒʱ` | /dʒʱə/ → [dʒʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_d̪` | /d̪ə/ → [d̪], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_f` | /fə/ → [f], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_j` | /jə/ → [j], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_k` | /kə/ → [k], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_kʃ` | /kʃə/ → [kʃ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_kʰ` | /kʰə/ → [kʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_l` | /lə/ → [l], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_m` | /mə/ → [m], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_n` | /nə/ → [n], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_p` | /pə/ → [p], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_pʰ` | /pʰə/ → [pʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_q` | /qə/ → [q], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_s` | /sə/ → [s], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_tʃ` | /tʃə/ → [tʃ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_tʃʰ` | /tʃʰə/ → [tʃʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_t̪` | /t̪ə/ → [t̪], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_t̪ɾ` | /t̪ɾə/ → [t̪ɾ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_x` | /xə/ → [x], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_z` | /zə/ → [z], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ŋ` | /ŋə/ → [ŋ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɖ` | /ɖə/ → [ɖ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɖʱ` | /ɖʱə/ → [ɖʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɡ` | /ɡə/ → [ɡ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɡj` | /ɡjə/ → [ɡj], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɡʱ` | /ɡʱə/ → [ɡʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɣ` | /ɣə/ → [ɣ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɦ` | /ɦə/ → [ɦ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɲ` | /ɲə/ → [ɲ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɳ` | /ɳə/ → [ɳ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɽ` | /ɽə/ → [ɽ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɽʱ` | /ɽʱə/ → [ɽʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɾ` | /ɾə/ → [ɾ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɾɪ` | /ɾɪə/ → [ɾɪ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʂ` | /ʂə/ → [ʂ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʃ` | /ʃə/ → [ʃ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʃɾ` | /ʃɾə/ → [ʃɾ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʈ` | /ʈə/ → [ʈ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʈʰ` | /ʈʰə/ → [ʈʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʋ` | /ʋə/ → [ʋ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | Sproat & Kiraz 2004 |
| `UR_CARRIER_DROP_BEFORE_MATER` | /ə/ → ∅, word-initially, spelled ⟨ا⟩ ⟨ع⟩, before ⟨ا⟩ ⟨آ⟩ ⟨ی⟩ ⟨و⟩ | ⟨ایک›⟩ [eːk] | - |
| `UR_MATER_NUCLEUS_AFTER_DROPPED_CARRIER` | /j/ → [eː], spelled ⟨ی⟩, after ⟨ا⟩, with more context in the spec | - | - |
| `UR_WAW_NUCLEUS_AFTER_DROPPED_CARRIER` | /ʋ/ → [ɔː], spelled ⟨و⟩, after ⟨ا⟩, with more context in the spec | - | - |
| `UR_HA_E_MALFUZ` | /aː/ → [ɦ], word-finally, spelled ⟨ہ⟩, after ⟨ا⟩ ⟨آ⟩ | - | [Platts 1884](#src-platts1884), [Ohala 1999](#src-ohala1999) |
| `UR_NASAL_VELAR` | /n/ → [ŋ], before [k] [ɡ] [kʰ] [ɡʱ] | - | [Ohala 1999](#src-ohala1999), [Shapiro 2003](#src-shapiro2003) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ur")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Upper Sorbian](hsb.md) · [Home](../index.md) · [Uyghur →](ug.md)
