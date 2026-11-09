# Punjabi (`pa`)

<!-- atlas:summary begin -->
Punjabi is an Indo-Aryan language, written in the Gurmukhi script. Glottolog places it in Bangladesh, India and Pakistan. The `pa` spec is at the research tier. It cites 7 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pa` |
| ISO 639-3 | [pan](https://iso639-3.sil.org/code/pan), Panjabi |
| Glottolog | [panj1256](https://glottolog.org/resource/languoid/id/panj1256), Eastern Panjabi |
| Wikidata | [Q58635](https://www.wikidata.org/wiki/Q58635) |
| Wikipedia | [Punjabi language](https://en.wikipedia.org/wiki/Punjabi_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [India](by-region.md#india), [Pakistan](by-region.md#pakistan) |
| Script | [Gurmukhi](by-script.md#gurmukhi) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`pa` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pa) |
| Spec file | [`pa.json`](../../orthography2ipa/data/pa.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Eastern Punjabi (Gurmukhi script, India). Typologically remarkable: lexical tone developed from the loss of the Old Indo-Aryan voiced-aspirate (murmured) series.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 7 works, from 1972 to 2019. [Sources](#sources) lists them. The spec file writes all 61 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pa.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `pa` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Western Punjabi (Shahmukhi)](pnb-PK.md) `pnb-PK`: Pakistan, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 7 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-shackle1972"></a>Shackle, C. (1972). *Punjabi*. University of London Press.
4. <a id="src-hussain2019"></a>Hussain, Q., Proctor, M., Harvey, M. & Demuth, K. (2019). *Punjabi (Lyallpuri variety)*. Journal of the International Phonetic Association 50(2): 282-297. [doi.org](https://doi.org/10.1017/S0025100319000021)
5. <a id="src-kanwal_ritchart2015"></a>Kanwal, J. & Ritchart, A. (2015). *An experimental investigation of tonogenesis in Punjabi*. Proceedings of the 18th International Congress of Phonetic Sciences. [internationalphoneticassociation.org](https://www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2015/Papers/ICPHS0929.pdf)
6. <a id="src-evans2018"></a>Evans, J., Yeh, W.-C. & Kulkarni, R. (2018). *Acoustics of tone in Indian Punjabi*. Transactions of the Philological Society 116(3): 509-528. [doi.org](https://doi.org/10.1111/1467-968X.12135)
7. <a id="src-singh_lehal_schwa"></a>Singh, P. & Lehal, G. S. (2010). *A Rule Based Schwa Deletion Algorithm for Punjabi TTS System*. [learnpunjabi.org](https://www.learnpunjabi.org/pdf/_paper_id_60__a_rule_based_schwa_deletion_algorithm_for_punjabi_tts_system__final_.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `pa` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1360 | 0.2541 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `pa` | generated | epitran-derived | CC0 1.0 | 4003 | 0.4432 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 64 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ | q |  |
| Affricate |  |  |  | dʒ tʃ tʃʰ |  |  |  |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Tap |  |  | ɾ |  | ɽ |  |  |  |  |
| Fricative |  | f | s z | ʃ |  |  | x ɣ |  | h ɦ |
| Approximant |  | ʋ |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  | ɭ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː |  | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | eː |  | oː |
| Mid |  | ə |  |
| Open-mid | ɛː |  | ɔː |
| Open | aː |  |  |

Sequences that the spec writes as one unit: [b˩] [dʒ˩] [d̪˩] [k˩] [k˩ə] [p˩] [p˩ə] [tʃ˩] [tʃ˩ə] [t̪˩] [t̪˩ə] [w] [ɖ˩] [ɡ˩] [ʈ˩] [ʈ˩ə] [ː] [̃].

Tones: [˥] high, [˧] mid (neutral), [˩] low.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ਂ⟩ | [̃] |  |
| ⟨ਅ⟩ | [ə] |  |
| ⟨ਆ⟩ | [aː] |  |
| ⟨ਇ⟩ | [ɪ] |  |
| ⟨ਈ⟩ | [iː] |  |
| ⟨ਉ⟩ | [ʊ] |  |
| ⟨ਊ⟩ | [uː] |  |
| ⟨ਏ⟩ | [eː] |  |
| ⟨ਐ⟩ | [ɛː] |  |
| ⟨ਓ⟩ | [oː] |  |
| ⟨ਔ⟩ | [ɔː] |  |
| ⟨ਕ⟩ | [k] |  |
| ⟨ਕ਼⟩ | [q] |  |
| ⟨ਖ⟩ | [kʰ] |  |
| ⟨ਖ਼⟩ | [x] |  |
| ⟨ਗ⟩ | [ɡ] |  |
| ⟨ਗ਼⟩ | [ɣ] |  |
| ⟨ਘ⟩ | [ɡ˩] |  |
| ⟨ਙ⟩ | [ŋ] |  |
| ⟨ਚ⟩ | [tʃ] |  |
| ⟨ਛ⟩ | [tʃʰ] |  |
| ⟨ਜ⟩ | [dʒ] |  |
| ⟨ਜ਼⟩ | [z] |  |
| ⟨ਝ⟩ | [dʒ˩] |  |
| ⟨ਞ⟩ | [ɲ] |  |
| ⟨ਟ⟩ | [ʈ] |  |
| ⟨ਠ⟩ | [ʈʰ] |  |
| ⟨ਡ⟩ | [ɖ] |  |
| ⟨ਢ⟩ | [ɖ˩] |  |
| ⟨ਣ⟩ | [ɳ] |  |
| ⟨ਤ⟩ | [t̪] |  |
| ⟨ਥ⟩ | [t̪ʰ] |  |
| ⟨ਦ⟩ | [d̪] |  |
| ⟨ਧ⟩ | [d̪˩] |  |
| ⟨ਨ⟩ | [n] |  |
| ⟨ਪ⟩ | [p] |  |
| ⟨ਫ⟩ | [pʰ] |  |
| ⟨ਫ਼⟩ | [f] |  |
| ⟨ਬ⟩ | [b] |  |
| ⟨ਭ⟩ | [b˩] |  |
| ⟨ਮ⟩ | [m] |  |
| ⟨ਯ⟩ | [j] |  |
| ⟨ਰ⟩ | [ɾ] |  |
| ⟨ਲ⟩ | [l] |  |
| ⟨ਲ਼⟩ | [ɭ] |  |
| ⟨ਵ⟩ | [ʋ] |  |
| ⟨ਸ⟩ | [s] |  |
| ⟨ਸ਼⟩ | [ʃ] |  |
| ⟨ਹ⟩ | [ɦ] |  |
| ⟨ਾ⟩ | [aː] |  |
| ⟨ਿ⟩ | [ɪ] |  |
| ⟨ੀ⟩ | [iː] |  |
| ⟨ੁ⟩ | [ʊ] |  |
| ⟨ੂ⟩ | [uː] |  |
| ⟨ੇ⟩ | [eː] |  |
| ⟨ੈ⟩ | [ɛː] |  |
| ⟨ੋ⟩ | [oː] |  |
| ⟨ੌ⟩ | [ɔː] |  |
| ⟨ੜ⟩ | [ɽ] |  |
| ⟨ੰ⟩ | [̃] |  |
| ⟨ੱ⟩ | [ː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 54 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `PA_DH_INITIAL_ɡ˩_0` | /ɡ˩ə/ → [k˩ə], word-initially | - | [Kanwal 2015](#src-kanwal_ritchart2015), [Evans 2018](#src-evans2018), Yeh & Kulkarni 2018 |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pa")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Pular](fuf.md) · [Home](../index.md) · [Qassimi Arabic →](ars-SA-x-qassim.md)
