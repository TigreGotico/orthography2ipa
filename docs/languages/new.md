# Newar (`new`)

<!-- atlas:summary begin -->
Newar is a Sino-Tibetan language, written in the Devanagari script. Glottolog places it in India and Nepal. The `new` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `new` |
| ISO 639-3 | [new](https://iso639-3.sil.org/code/new), Nepal Bhasa |
| Glottolog | [newa1246](https://glottolog.org/resource/languoid/id/newa1246), Kathmandu Valley Newari |
| Wikidata | [Q33979](https://www.wikidata.org/wiki/Q33979) |
| Wikipedia | [Newar language](https://en.wikipedia.org/wiki/Newar_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india), [Nepal](by-region.md#nepal) |
| Script | [Devanagari](by-script.md#devanagari) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Sino-Tibetan](https://tigregotico.github.io/orthography2ipa/#x-clade-sino1245) `x-clade-sino1245` |
| Explorer | [`new` in the data explorer](https://tigregotico.github.io/orthography2ipa/#new) |
| Spec file | [`new.json`](../../orthography2ipa/data/new.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Newar (Nepal Bhasa) of the Kathmandu Valley, a Sino-Tibetan language written today in Devanagari and historically in the Newar, Ranjana and other Nepalese scripts.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 2003 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes 42 of the 80 spellings of its letter table and takes the other 38 from [Hindi](hi.md) `hi`.

The [spec file](../../orthography2ipa/data/new.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `new` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-genetti2007"></a>Genetti, Carol (2007). *A Grammar of Dolakha Newar*. Mouton de Gruyter.
2. <a id="src-hale2006"></a>Hale, Austin & Shrestha, Kedar P. (2006). *Newar (Nepal Bhasa)*. LINCOM Europa.
3. <a id="src-new_wiki"></a>Wikipedia contributors (2024). *Newar language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Newar_language)
4. <a id="src-phoible"></a>Moran, Steven & McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/)
5. <a id="src-hargreaves2003"></a>Hargreaves, David (2003). *Kathmandu Newar (Nepal Bhasa)*. Routledge. Cited: 371-384.
6. <a id="src-ishida_newa"></a>Ishida, Richard (2024). *Newa (Newar) orthography notes*. r12a.github.io. [r12a.github.io](https://r12a.github.io/scripts/newa/new.html)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `new` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 416 | 0.0282 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 122 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ | ɖ ʈ ʈʰ |  | k kʰ ɡ | q |  |
| Affricate |  |  | d̠z̠ t̠s̠ |  | d͡ʑ t͡ɕ t͡ɕʰ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |  |
| Tap |  |  | ɾ | ɽ |  |  |  |  |
| Fricative |  | f | s z |  | ɕ | x ɣ |  | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Near-close |  |  | ʊ |
| Close-mid | e eː |  | o oː |
| Mid |  | ə əː |  |
| Open-mid | ɛː ɛ̃ː |  | ɔ ɔː |
| Near-open | æː æ̃ː |  |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [bə] [bʱ] [bʱə] [dʒə] [dʒɲ] [dʒɲə] [dʒʱə] [dʱ] [d̪ə] [d̪ʱə] [d͡ʑʱ] [fə] [jə] [jʱ] [kə] [kʃ] [kʃə] [kʰə] [lə] [lʱ] [mə] [mʱ] [nə] [nʱ] [pə] [pʰə] [qə] [sə] [tɾ] [tʃə] [tʃʰə] [t̪ə] [t̪ɾə] [t̪ʰə] [w] [wʱ] [xə] [zə] [ŋə] [ɖə], and 30 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ँ⟩ | [̃] |  |
| ⟨ँय्⟩ | [ɛ̃ː] |  |
| ⟨ं⟩ | [̃ː] | before consonant [̃ː] · default [̃ː] · word final [̃ː] |
| ⟨ः⟩ | [ː] |  |
| ⟨अ⟩ | [ə] | default [ə] · nucleus unstressed [ə] · word final ∅ |
| ⟨अय्⟩ | [ɛː] |  |
| ⟨आ⟩ | [a] |  |
| ⟨आय्⟩ | [æː] |  |
| ⟨इ⟩ | [i] |  |
| ⟨ई⟩ | [iː] |  |
| ⟨उ⟩ | [u] |  |
| ⟨ऊ⟩ | [uː] |  |
| ⟨ऋ⟩ | [ɾɪ] |  |
| ⟨ए⟩ | [e] |  |
| ⟨ऐ⟩ | [əi] |  |
| ⟨ओ⟩ | [o] |  |
| ⟨औ⟩ | [əu] |  |
| ⟨क⟩ | [k] |  |
| ⟨क़⟩ | [q] |  |
| ⟨क्ष⟩ | [kʃ] |  |
| ⟨ख⟩ | [kʰ] |  |
| ⟨ख़⟩ | [x] |  |
| ⟨ग⟩ | [ɡ] |  |
| ⟨ग़⟩ | [ɣ] |  |
| ⟨घ⟩ | [ɡʱ] |  |
| ⟨ङ⟩ | [ŋ] |  |
| ⟨च⟩ | [t͡ɕ] |  |
| ⟨छ⟩ | [t͡ɕʰ] |  |
| ⟨ज⟩ | [d͡ʑ] |  |
| ⟨ज़⟩ | [z] |  |
| ⟨ज्ञ⟩ | [ɡj] [dʒɲ] |  |
| ⟨झ⟩ | [d͡ʑʱ] |  |
| ⟨ञ⟩ | [ɲ] |  |
| ⟨ट⟩ | [ʈ] |  |
| ⟨ठ⟩ | [ʈʰ] |  |
| ⟨ड⟩ | [ɖ] |  |
| ⟨ड़⟩ | [ɽ] |  |
| ⟨ढ⟩ | [ɖʱ] |  |
| ⟨ढ़⟩ | [ɽʱ] |  |
| ⟨ण⟩ | [n] |  |
| ⟨त⟩ | [t] |  |
| ⟨त्र⟩ | [tɾ] |  |
| ⟨थ⟩ | [tʰ] |  |
| ⟨द⟩ | [d] |  |
| ⟨ध⟩ | [dʱ] |  |
| ⟨न⟩ | [n] |  |
| ⟨न्ह⟩ | [nʱ] |  |
| ⟨प⟩ | [p] |  |
| ⟨फ⟩ | [pʰ] |  |
| ⟨फ़⟩ | [f] |  |
| ⟨ब⟩ | [b] |  |
| ⟨भ⟩ | [bʱ] |  |
| ⟨म⟩ | [m] |  |
| ⟨म्ह⟩ | [mʱ] |  |
| ⟨य⟩ | [j] |  |
| ⟨य्⟩ | [ɛː] |  |
| ⟨र⟩ | [ɾ] |  |
| ⟨र्ह⟩ | [ɾʱ] |  |
| ⟨ल⟩ | [l] |  |
| ⟨ल्ह⟩ | [lʱ] |  |
| ⟨व⟩ | [w] |  |
| ⟨श⟩ | [s] |  |
| ⟨श्र⟩ | [ʃɾ] |  |
| ⟨ष⟩ | [s] |  |
| ⟨स⟩ | [s] |  |
| ⟨ह⟩ | [h] |  |
| ⟨ा⟩ | [a] |  |
| ⟨ाँय्⟩ | [æ̃ː] |  |
| ⟨ाय्⟩ | [æː] |  |
| ⟨ि⟩ | [i] |  |
| ⟨ी⟩ | [iː] |  |
| ⟨ु⟩ | [u] |  |
| ⟨ू⟩ | [uː] |  |
| ⟨ृ⟩ | [ɾɪ] |  |
| ⟨े⟩ | [e] |  |
| ⟨ै⟩ | [əi] |  |
| ⟨ो⟩ | [o] |  |
| ⟨ौ⟩ | [əu] |  |
| ⟨्⟩ | ∅ |  |
| ⟨‌⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 138 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `HI_SCHWA_FINAL_b` | /bə/ → [bə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_bʱ` | /bʱə/ → [bʱə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_dʒ` | /dʒə/ → [dʒə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_dʒɲ` | /dʒɲə/ → [dʒɲə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_dʒʱ` | /dʒʱə/ → [dʒʱə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_d̪` | /d̪ə/ → [d̪ə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_f` | /fə/ → [fə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_j` | /jə/ → [jə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_k` | /kə/ → [kə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_kʃ` | /kʃə/ → [kʃə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_kʰ` | /kʰə/ → [kʰə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_l` | /lə/ → [lə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_m` | /mə/ → [mə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_n` | /nə/ → [nə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_p` | /pə/ → [pə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_pʰ` | /pʰə/ → [pʰə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_q` | /qə/ → [qə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_s` | /sə/ → [sə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_tʃ` | /tʃə/ → [tʃə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_tʃʰ` | /tʃʰə/ → [tʃʰə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_t̪` | /t̪ə/ → [t̪ə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_t̪ɾ` | /t̪ɾə/ → [t̪ɾə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_x` | /xə/ → [xə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_z` | /zə/ → [zə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ŋ` | /ŋə/ → [ŋə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɖ` | /ɖə/ → [ɖə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɖʱ` | /ɖʱə/ → [ɖʱə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɡ` | /ɡə/ → [ɡə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɡj` | /ɡjə/ → [ɡjə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɡʱ` | /ɡʱə/ → [ɡʱə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɣ` | /ɣə/ → [ɣə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɦ` | /ɦə/ → [ɦə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɲ` | /ɲə/ → [ɲə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɳ` | /ɳə/ → [ɳə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɽ` | /ɽə/ → [ɽə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɽʱ` | /ɽʱə/ → [ɽʱə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɾ` | /ɾə/ → [ɾə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ɾɪ` | /ɾɪə/ → [ɾɪə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ʂ` | /ʂə/ → [ʂə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ʃ` | /ʃə/ → [ʃə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ʃɾ` | /ʃɾə/ → [ʃɾə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ʈ` | /ʈə/ → [ʈə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ʈʰ` | /ʈʰə/ → [ʈʰə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_FINAL_ʋ` | /ʋə/ → [ʋə], not word-initially, word-finally | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006) |
| `HI_SCHWA_KEEP_b` | /bə/ → [bə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_bʱ` | /bʱə/ → [bʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_dʒ` | /dʒə/ → [dʒə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_dʒɲ` | /dʒɲə/ → [dʒɲə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_dʒʱ` | /dʒʱə/ → [dʒʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_d̪` | /d̪ə/ → [d̪ə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_d̪ʱ` | /d̪ʱə/ → [d̪ʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_f` | /fə/ → [fə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_j` | /jə/ → [jə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_k` | /kə/ → [kə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_kʃ` | /kʃə/ → [kʃə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_kʰ` | /kʰə/ → [kʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_l` | /lə/ → [lə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_m` | /mə/ → [mə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_n` | /nə/ → [nə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_p` | /pə/ → [pə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_pʰ` | /pʰə/ → [pʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_q` | /qə/ → [qə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_s` | /sə/ → [sə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_tʃ` | /tʃə/ → [tʃə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_tʃʰ` | /tʃʰə/ → [tʃʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_t̪` | /t̪ə/ → [t̪ə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_t̪ɾ` | /t̪ɾə/ → [t̪ɾə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_t̪ʰ` | /t̪ʰə/ → [t̪ʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_x` | /xə/ → [xə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_z` | /zə/ → [zə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ŋ` | /ŋə/ → [ŋə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɖ` | /ɖə/ → [ɖə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɖʱ` | /ɖʱə/ → [ɖʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɡ` | /ɡə/ → [ɡə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɡj` | /ɡjə/ → [ɡjə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɡʱ` | /ɡʱə/ → [ɡʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɣ` | /ɣə/ → [ɣə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɦ` | /ɦə/ → [ɦə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɲ` | /ɲə/ → [ɲə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɳ` | /ɳə/ → [ɳə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɽ` | /ɽə/ → [ɽə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɽʱ` | /ɽʱə/ → [ɽʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɾ` | /ɾə/ → [ɾə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ɾɪ` | /ɾɪə/ → [ɾɪə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ʂ` | /ʂə/ → [ʂə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ʃ` | /ʃə/ → [ʃə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ʃɾ` | /ʃɾə/ → [ʃɾə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ʈ` | /ʈə/ → [ʈə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ʈʰ` | /ʈʰə/ → [ʈʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_ʋ` | /ʋə/ → [ʋə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_b` | /bə/ → [bə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_bʱ` | /bʱə/ → [bʱə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_dʒ` | /dʒə/ → [dʒə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_dʒɲ` | /dʒɲə/ → [dʒɲə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_dʒʱ` | /dʒʱə/ → [dʒʱə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_d̪` | /d̪ə/ → [d̪ə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_f` | /fə/ → [fə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_j` | /jə/ → [jə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_k` | /kə/ → [kə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_kʃ` | /kʃə/ → [kʃə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_kʰ` | /kʰə/ → [kʰə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_l` | /lə/ → [lə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_m` | /mə/ → [mə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_n` | /nə/ → [nə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_p` | /pə/ → [pə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_pʰ` | /pʰə/ → [pʰə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_q` | /qə/ → [qə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_s` | /sə/ → [sə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_tʃ` | /tʃə/ → [tʃə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_tʃʰ` | /tʃʰə/ → [tʃʰə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_t̪` | /t̪ə/ → [t̪ə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_t̪ɾ` | /t̪ɾə/ → [t̪ɾə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_x` | /xə/ → [xə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_z` | /zə/ → [zə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ŋ` | /ŋə/ → [ŋə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɖ` | /ɖə/ → [ɖə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɖʱ` | /ɖʱə/ → [ɖʱə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɡ` | /ɡə/ → [ɡə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɡj` | /ɡjə/ → [ɡjə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɡʱ` | /ɡʱə/ → [ɡʱə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɣ` | /ɣə/ → [ɣə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɦ` | /ɦə/ → [ɦə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɲ` | /ɲə/ → [ɲə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɳ` | /ɳə/ → [ɳə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɽ` | /ɽə/ → [ɽə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɽʱ` | /ɽʱə/ → [ɽʱə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɾ` | /ɾə/ → [ɾə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɾɪ` | /ɾɪə/ → [ɾɪə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʂ` | /ʂə/ → [ʂə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʃ` | /ʃə/ → [ʃə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʃɾ` | /ʃɾə/ → [ʃɾə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʈ` | /ʈə/ → [ʈə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʈʰ` | /ʈʰə/ → [ʈʰə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʋ` | /ʋə/ → [ʋə], before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Genetti 2007](#src-genetti2007), [Hale 2006](#src-hale2006), Sproat & Kiraz 2004 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "new")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nepali](ne.md) · [Home](../index.md) · [Nganasan →](nio.md)
