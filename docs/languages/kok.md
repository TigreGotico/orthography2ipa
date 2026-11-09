# Konkani (`kok`)

<!-- atlas:summary begin -->
Konkani is an Indo-Aryan language, written in the Devanagari script. Glottolog places it in India. The `kok` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kok` |
| ISO 639-3 | [kok](https://iso639-3.sil.org/code/kok), Konkani (macrolanguage) |
| Glottolog | [goan1235](https://glottolog.org/resource/languoid/id/goan1235), Goan Konkani |
| Wikidata | [Q34239](https://www.wikidata.org/wiki/Q34239) |
| Wikipedia | [Konkani language](https://en.wikipedia.org/wiki/Konkani_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india) |
| Script | [Devanagari](by-script.md#devanagari) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1700, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Explorer | [`kok` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kok) |
| Spec file | [`kok.json`](../../orthography2ipa/data/kok.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Konkani, 22nd scheduled language of India (1992). Spoken in Goa (official), Karnataka, and Kerala. Multiple scripts: Devanagari (official Goa), Kannada, Roman, this spec reads the Devanagari orthography. Strong Dravidian substrate features: retroflex ⟨ळ⟩ = [ɭ].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1983 to 2021. [Sources](#sources) lists them. The spec file writes all 70 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kok.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kok` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-almeida1989"></a>Almeida, T. (1989). *A Description of Konkani*. Goa University.
4. <a id="src-ohala1983"></a>Ohala, M. (1983). *Aspects of Hindi Phonology*. Motilal Banarsidass, Delhi.
5. <a id="src-narasimhan2004"></a>Narasimhan, B., Sproat, R. & Kiraz, G. (2004). *Schwa-Deletion in Hindi Text-to-Speech Synthesis*. International Journal of Speech Technology 7(4). Cited: 319-333.
6. <a id="src-ashok_dutta2021"></a>Ashok, A. & Dutta, I. (2021). *Syllable Structure and Word Stress in Central Kerala Konkani Variety: An OT Approach*. Journal of Universal Language 22(1). [doi.org](https://doi.org/10.22425/jul.2021.22.1.1)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `kaikki` ([kaikki.org](https://kaikki.org/dictionary/)) | `kok` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 830 | 0.2241 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 102 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  | dz ts tsʰ | dʒ tʃ tʃʰ |  |  |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |
| Tap |  |  | ɾ |  | ɽ |  |  |  |
| Fricative |  | f | s | ʃ | ʂ |  |  | h |
| Approximant |  | ʋ |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ɭ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Near-open | æ |  |  |
| Open | aː |  |  |

Sequences that the spec writes as one unit: [bə] [bʱ] [bʱə] [dzə] [dzʱ] [dzʱə] [dʒə] [dʒʱ] [dʒʱə] [d̪ə] [d̪ʱ] [d̪ʱə] [hə] [jə] [kə] [kʰə] [lə] [lʱ] [mə] [mʱ] [nə] [nʱ] [pə] [pʰə] [sə] [tsə] [tsʰə] [tʃə] [tʃʰə] [t̪ə] [t̪ʰə] [ŋə] [ɖə] [ɖʱ] [ɖʱə] [əi] [əu] [ɡə] [ɡʱ] [ɡʱə], and 17 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ँ⟩ | [̃] |  |
| ⟨ं⟩ | [̃] |  |
| ⟨ः⟩ | [h] |  |
| ⟨अ⟩ | [ə] |  |
| ⟨आ⟩ | [aː] |  |
| ⟨इ⟩ | [i] |  |
| ⟨ई⟩ | [iː] |  |
| ⟨उ⟩ | [u] |  |
| ⟨ऊ⟩ | [uː] |  |
| ⟨ऋ⟩ | [ɾɪ] [ɾu] |  |
| ⟨ए⟩ | [e] [ɛ] |  |
| ⟨ऐ⟩ | [əi] |  |
| ⟨ऑ⟩ | [æ] [ɔ] |  |
| ⟨ओ⟩ | [o] [ɔ] |  |
| ⟨औ⟩ | [əu] |  |
| ⟨क⟩ | [k] |  |
| ⟨ख⟩ | [kʰ] |  |
| ⟨ग⟩ | [ɡ] |  |
| ⟨घ⟩ | [ɡʱ] |  |
| ⟨ङ⟩ | [ŋ] |  |
| ⟨च⟩ | [tʃ] [ts] |  |
| ⟨छ⟩ | [tʃʰ] [tsʰ] |  |
| ⟨ज⟩ | [dʒ] [dz] |  |
| ⟨झ⟩ | [dʒʱ] [dzʱ] |  |
| ⟨ञ⟩ | [ɲ] |  |
| ⟨ट⟩ | [ʈ] |  |
| ⟨ठ⟩ | [ʈʰ] |  |
| ⟨ड⟩ | [ɖ] |  |
| ⟨ड़⟩ | [ɽ] |  |
| ⟨ढ⟩ | [ɖʱ] |  |
| ⟨ण⟩ | [ɳ] |  |
| ⟨ण्ह⟩ | [ɳʱ] |  |
| ⟨त⟩ | [t̪] |  |
| ⟨थ⟩ | [t̪ʰ] |  |
| ⟨द⟩ | [d̪] |  |
| ⟨ध⟩ | [d̪ʱ] |  |
| ⟨न⟩ | [n] |  |
| ⟨न्ह⟩ | [nʱ] |  |
| ⟨प⟩ | [p] |  |
| ⟨फ⟩ | [pʰ] [f] |  |
| ⟨ब⟩ | [b] |  |
| ⟨भ⟩ | [bʱ] |  |
| ⟨म⟩ | [m] |  |
| ⟨म्ह⟩ | [mʱ] |  |
| ⟨य⟩ | [j] |  |
| ⟨र⟩ | [ɾ] |  |
| ⟨र्ह⟩ | [ɾʱ] |  |
| ⟨ल⟩ | [l] |  |
| ⟨ल्ह⟩ | [lʱ] |  |
| ⟨ळ⟩ | [ɭ] |  |
| ⟨ळ्ह⟩ | [ɭʱ] |  |
| ⟨व⟩ | [ʋ] |  |
| ⟨व्ह⟩ | [ʋʱ] |  |
| ⟨श⟩ | [ʃ] |  |
| ⟨ष⟩ | [ʂ] |  |
| ⟨स⟩ | [s] |  |
| ⟨ह⟩ | [h] |  |
| ⟨ा⟩ | [aː] |  |
| ⟨ि⟩ | [i] |  |
| ⟨ी⟩ | [iː] |  |
| ⟨ु⟩ | [u] |  |
| ⟨ू⟩ | [uː] |  |
| ⟨ृ⟩ | [ɾɪ] [ɾu] |  |
| ⟨ॅ⟩ | [æ] [ɛ] |  |
| ⟨े⟩ | [e] [ɛ] |  |
| ⟨ै⟩ | [əi] |  |
| ⟨ॉ⟩ | [æ] [ɔ] |  |
| ⟨ो⟩ | [o] [ɔ] |  |
| ⟨ौ⟩ | [əu] |  |
| ⟨्⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 122 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `KOK_ANUSVARA_VELAR` | /̃/ → [ŋ], spelled ⟨ं⟩, before ⟨क⟩ ⟨ख⟩ ⟨ग⟩ ⟨घ⟩ | ⟨रंग⟩ [ɾəŋɡ] | [Masica 1991](#src-masica1991) |
| `KOK_ANUSVARA_PALATAL` | /̃/ → [n], spelled ⟨ं⟩, before ⟨च⟩ ⟨छ⟩ ⟨ज⟩ ⟨झ⟩ | - | - |
| `KOK_ANUSVARA_RETROFLEX` | /̃/ → [ɳ], spelled ⟨ं⟩, before ⟨ट⟩ ⟨ठ⟩ ⟨ड⟩ ⟨ढ⟩ | - | - |
| `KOK_ANUSVARA_DENTAL` | /̃/ → [n], spelled ⟨ं⟩, before ⟨त⟩ ⟨थ⟩ ⟨द⟩ ⟨ध⟩ | - | - |
| `KOK_ANUSVARA_LABIAL` | /̃/ → [m], spelled ⟨ं⟩, before ⟨प⟩ ⟨फ⟩ ⟨ब⟩ ⟨भ⟩ | - | - |
| `KOK_SCHWA_FINAL_b` | /bə/ → [b], not word-initially, word-finally | - | [Masica 1991](#src-masica1991), [Almeida 1989](#src-almeida1989), [Ohala 1983](#src-ohala1983) |
| `KOK_SCHWA_FINAL_bʱ` | /bʱə/ → [bʱ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_dz` | /dzə/ → [dz], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_dzʱ` | /dzʱə/ → [dzʱ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_dʒ` | /dʒə/ → [dʒ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_dʒʱ` | /dʒʱə/ → [dʒʱ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_d̪` | /d̪ə/ → [d̪], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_h` | /hə/ → [h], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_j` | /jə/ → [j], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_k` | /kə/ → [k], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_kʰ` | /kʰə/ → [kʰ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_l` | /lə/ → [l], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_m` | /mə/ → [m], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_n` | /nə/ → [n], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_p` | /pə/ → [p], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_pʰ` | /pʰə/ → [pʰ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_s` | /sə/ → [s], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ts` | /tsə/ → [ts], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_tsʰ` | /tsʰə/ → [tsʰ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_tʃ` | /tʃə/ → [tʃ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_tʃʰ` | /tʃʰə/ → [tʃʰ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_t̪` | /t̪ə/ → [t̪], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ŋ` | /ŋə/ → [ŋ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ɖ` | /ɖə/ → [ɖ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ɖʱ` | /ɖʱə/ → [ɖʱ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ɡ` | /ɡə/ → [ɡ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ɡʱ` | /ɡʱə/ → [ɡʱ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ɭ` | /ɭə/ → [ɭ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ɲ` | /ɲə/ → [ɲ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ɳ` | /ɳə/ → [ɳ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ɽ` | /ɽə/ → [ɽ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ɾ` | /ɾə/ → [ɾ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ʂ` | /ʂə/ → [ʂ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ʃ` | /ʃə/ → [ʃ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ʈ` | /ʈə/ → [ʈ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ʈʰ` | /ʈʰə/ → [ʈʰ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_FINAL_ʋ` | /ʋə/ → [ʋ], not word-initially, word-finally | - | - |
| `KOK_SCHWA_KEEP_b` | /bə/ → [bə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | [Ohala 1983](#src-ohala1983), [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `KOK_SCHWA_KEEP_bʱ` | /bʱə/ → [bʱə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_dz` | /dzə/ → [dzə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_dzʱ` | /dzʱə/ → [dzʱə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_dʒ` | /dʒə/ → [dʒə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_dʒʱ` | /dʒʱə/ → [dʒʱə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_d̪` | /d̪ə/ → [d̪ə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_d̪ʱ` | /d̪ʱə/ → [d̪ʱə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_h` | /hə/ → [hə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_j` | /jə/ → [jə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_k` | /kə/ → [kə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_kʰ` | /kʰə/ → [kʰə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_l` | /lə/ → [lə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_m` | /mə/ → [mə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_n` | /nə/ → [nə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_p` | /pə/ → [pə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_pʰ` | /pʰə/ → [pʰə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_s` | /sə/ → [sə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ts` | /tsə/ → [tsə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_tsʰ` | /tsʰə/ → [tsʰə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_tʃ` | /tʃə/ → [tʃə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_tʃʰ` | /tʃʰə/ → [tʃʰə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_t̪` | /t̪ə/ → [t̪ə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_t̪ʰ` | /t̪ʰə/ → [t̪ʰə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ŋ` | /ŋə/ → [ŋə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ɖ` | /ɖə/ → [ɖə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ɖʱ` | /ɖʱə/ → [ɖʱə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ɡ` | /ɡə/ → [ɡə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ɡʱ` | /ɡʱə/ → [ɡʱə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ɭ` | /ɭə/ → [ɭə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ɲ` | /ɲə/ → [ɲə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ɳ` | /ɳə/ → [ɳə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ɽ` | /ɽə/ → [ɽə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ɾ` | /ɾə/ → [ɾə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ʂ` | /ʂə/ → [ʂə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ʃ` | /ʃə/ → [ʃə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ʈ` | /ʈə/ → [ʈə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ʈʰ` | /ʈʰə/ → [ʈʰə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_KEEP_ʋ` | /ʋə/ → [ʋə], after [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_b` | /bə/ → [b], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | [Masica 1991](#src-masica1991), [Ohala 1983](#src-ohala1983), [Narasimhan 2004](#src-narasimhan2004) |
| `KOK_SCHWA_MEDIAL_bʱ` | /bʱə/ → [bʱ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_dz` | /dzə/ → [dz], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_dzʱ` | /dzʱə/ → [dzʱ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_dʒ` | /dʒə/ → [dʒ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_dʒʱ` | /dʒʱə/ → [dʒʱ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_d̪` | /d̪ə/ → [d̪], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_h` | /hə/ → [h], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_j` | /jə/ → [j], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_k` | /kə/ → [k], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_kʰ` | /kʰə/ → [kʰ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_l` | /lə/ → [l], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_m` | /mə/ → [m], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_n` | /nə/ → [n], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_p` | /pə/ → [p], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_pʰ` | /pʰə/ → [pʰ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_s` | /sə/ → [s], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ts` | /tsə/ → [ts], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_tsʰ` | /tsʰə/ → [tsʰ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_tʃ` | /tʃə/ → [tʃ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_tʃʰ` | /tʃʰə/ → [tʃʰ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_t̪` | /t̪ə/ → [t̪], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ŋ` | /ŋə/ → [ŋ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ɖ` | /ɖə/ → [ɖ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ɖʱ` | /ɖʱə/ → [ɖʱ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ɡ` | /ɡə/ → [ɡ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ɡʱ` | /ɡʱə/ → [ɡʱ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ɭ` | /ɭə/ → [ɭ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ɲ` | /ɲə/ → [ɲ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ɳ` | /ɳə/ → [ɳ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ɽ` | /ɽə/ → [ɽ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ɾ` | /ɾə/ → [ɾ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ʂ` | /ʂə/ → [ʂ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ʃ` | /ʃə/ → [ʃ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ʈ` | /ʈə/ → [ʈ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ʈʰ` | /ʈʰə/ → [ʈʰ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
| `KOK_SCHWA_MEDIAL_ʋ` | /ʋə/ → [ʋ], not word-initially, before [b] [bʱ] [dz] [dzʱ] [dʒ] [dʒʱ] [d̪] [d̪ʱ] and 31 more | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kok")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kongo](kg.md) · [Home](../index.md) · [Korean →](ko.md)
