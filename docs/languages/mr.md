# Marathi (`mr`)

<!-- atlas:summary begin -->
Marathi is an Indo-Aryan language, written in the Devanagari script. Glottolog places it in India. The `mr` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mr` |
| ISO 639-3 | [mar](https://iso639-3.sil.org/code/mar), Marathi |
| Glottolog | [mara1378](https://glottolog.org/resource/languoid/id/mara1378), Marathi |
| Wikidata | [Q1571](https://www.wikidata.org/wiki/Q1571) |
| Wikipedia | [Marathi language](https://en.wikipedia.org/wiki/Marathi_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india) |
| Script | [Devanagari](by-script.md#devanagari) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Child lects | 2, see [Related lects](#related-lects) |
| Explorer | [`mr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mr) |
| Spec file | [`mr.json`](../../orthography2ipa/data/mr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Marathi (Maharashtra). No phonemic vowel length -- the script writes the Sanskrit length distinction but the language has lost it, so ⟨आ ई ऊ ए ओ⟩ are transcribed without a length mark and ⟨अ⟩ vs ⟨आ⟩ is a quality contrast [ə] vs [a]. ⟨ळ⟩ is the retroflex lateral flap [ɭ̆], a Marathi hallmark. ⟨र⟩ is a tap.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1991 to 2009. [Sources](#sources) lists them. The spec file writes all 73 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `mr` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Andh](https://tigregotico.github.io/orthography2ipa/#anr) `anr`: India, stub tier
- [Deccan](https://tigregotico.github.io/orthography2ipa/#dcc) `dcc`: India, stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-dhongde_wali2009"></a>Dhongde, R.V. & Wali, K. (2009). *Marathi*. John Benjamins.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mr` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4267 | 0.0535 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `mr` | generated | epitran-derived | CC0 1.0 | 16938 | 0.3063 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 63 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  | dz ts |  | dʑ tɕ tɕʰ |  |  |
| Nasal | m |  | n | ɳ | ɲ | ŋ |  |
| Tap |  |  | ɾ | ɽ |  |  |  |
| Fricative |  |  | s | ʂ | ɕ |  | h ɦ |
| Approximant |  | ʋ |  |  | j |  |  |
| Lateral approximant |  |  | l | ɭ ɭ̆ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid |  |  | ɔ |
| Near-open | æ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [bʱ] [dzʱ] [dʑn] [dʑʱ] [d̪ʱ] [lʱ] [mʱ] [nʱ] [w] [ɖʱ] [əi] [əu] [ɡʱ] [ɭ̆ʱ] [ɳʱ] [ɽʱ] [ɾu] [ɾʱ] [ʋʱ] [ʰ] [̃].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ँ⟩ | [̃] |  |
| ⟨ं⟩ | [̃] |  |
| ⟨ः⟩ | [ʰ] |  |
| ⟨अ⟩ | [ə] |  |
| ⟨आ⟩ | [a] |  |
| ⟨इ⟩ | [i] |  |
| ⟨ई⟩ | [i] |  |
| ⟨उ⟩ | [u] |  |
| ⟨ऊ⟩ | [u] |  |
| ⟨ऋ⟩ | [ɾu] |  |
| ⟨ऍ⟩ | [æ] |  |
| ⟨ए⟩ | [e] |  |
| ⟨ऐ⟩ | [əi] |  |
| ⟨ऑ⟩ | [ɔ] |  |
| ⟨ओ⟩ | [o] |  |
| ⟨औ⟩ | [əu] |  |
| ⟨क⟩ | [k] |  |
| ⟨ख⟩ | [kʰ] |  |
| ⟨ग⟩ | [ɡ] |  |
| ⟨घ⟩ | [ɡʱ] |  |
| ⟨ङ⟩ | [ŋ] |  |
| ⟨च⟩ | [tɕ] [ts] |  |
| ⟨छ⟩ | [tɕʰ] |  |
| ⟨ज⟩ | [dʑ] [dz] |  |
| ⟨ज्ञ⟩ | [dʑn] |  |
| ⟨झ⟩ | [dzʱ] [dʑʱ] |  |
| ⟨ञ⟩ | [ɲ] |  |
| ⟨ट⟩ | [ʈ] |  |
| ⟨ठ⟩ | [ʈʰ] |  |
| ⟨ड⟩ | [ɖ] |  |
| ⟨ड़⟩ | [ɽ] |  |
| ⟨ढ⟩ | [ɖʱ] |  |
| ⟨ढ़⟩ | [ɽʱ] |  |
| ⟨ण⟩ | [ɳ] |  |
| ⟨ण्ह⟩ | [ɳʱ] |  |
| ⟨त⟩ | [t̪] |  |
| ⟨थ⟩ | [t̪ʰ] |  |
| ⟨द⟩ | [d̪] |  |
| ⟨ध⟩ | [d̪ʱ] |  |
| ⟨न⟩ | [n] |  |
| ⟨न्ह⟩ | [nʱ] |  |
| ⟨प⟩ | [p] |  |
| ⟨फ⟩ | [pʰ] |  |
| ⟨ब⟩ | [b] |  |
| ⟨भ⟩ | [bʱ] |  |
| ⟨म⟩ | [m] |  |
| ⟨म्ह⟩ | [mʱ] |  |
| ⟨य⟩ | [j] |  |
| ⟨र⟩ | [ɾ] |  |
| ⟨र्ह⟩ | [ɾʱ] |  |
| ⟨ल⟩ | [l] |  |
| ⟨ल्ह⟩ | [lʱ] |  |
| ⟨ळ⟩ | [ɭ̆] |  |
| ⟨ळ्ह⟩ | [ɭ̆ʱ] |  |
| ⟨व⟩ | [ʋ] |  |
| ⟨व्ह⟩ | [ʋʱ] |  |
| ⟨श⟩ | [ɕ] |  |
| ⟨ष⟩ | [ʂ] |  |
| ⟨स⟩ | [s] |  |
| ⟨ह⟩ | [ɦ] |  |
| ⟨ा⟩ | [a] |  |
| ⟨ि⟩ | [i] |  |
| ⟨ी⟩ | [i] |  |
| ⟨ु⟩ | [u] |  |
| ⟨ू⟩ | [u] |  |
| ⟨ृ⟩ | [ɾu] |  |
| ⟨ॅ⟩ | [æ] |  |
| ⟨े⟩ | [e] |  |
| ⟨ै⟩ | [əi] |  |
| ⟨ॉ⟩ | [ɔ] |  |
| ⟨ो⟩ | [o] |  |
| ⟨ौ⟩ | [əu] |  |
| ⟨्⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 46 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `MR_SCHWA_FINAL_b` | /bə/ → [b], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_bʱ` | /bʱə/ → [bʱ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_dz` | /dzə/ → [dz], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_dzʱ` | /dzʱə/ → [dzʱ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_dʑ` | /dʑə/ → [dʑ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_dʑʱ` | /dʑʱə/ → [dʑʱ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_d̪` | /d̪ə/ → [d̪], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_j` | /jə/ → [j], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_k` | /kə/ → [k], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | ⟨अंकुश⟩ [əŋkuɕ] | [Masica 1991](#src-masica1991), Indo-Aryan Languages 1991 |
| `MR_SCHWA_FINAL_kʰ` | /kʰə/ → [kʰ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_l` | /lə/ → [l], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_m` | /mə/ → [m], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_n` | /nə/ → [n], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_p` | /pə/ → [p], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_pʰ` | /pʰə/ → [pʰ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_s` | /sə/ → [s], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ts` | /tsə/ → [ts], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_tɕ` | /tɕə/ → [tɕ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_tɕʰ` | /tɕʰə/ → [tɕʰ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_t̪` | /t̪ə/ → [t̪], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɕ` | /ɕə/ → [ɕ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɖ` | /ɖə/ → [ɖ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɖʱ` | /ɖʱə/ → [ɖʱ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɡ` | /ɡə/ → [ɡ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɡʱ` | /ɡʱə/ → [ɡʱ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɦ` | /ɦə/ → [ɦ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɭ` | /ɭə/ → [ɭ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɭ̆` | /ɭ̆ə/ → [ɭ̆], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɲ` | /ɲə/ → [ɲ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɳ` | /ɳə/ → [ɳ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɽ` | /ɽə/ → [ɽ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ɾ` | /ɾə/ → [ɾ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ʂ` | /ʂə/ → [ʂ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ʈ` | /ʈə/ → [ʈ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ʈʰ` | /ʈʰə/ → [ʈʰ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_SCHWA_FINAL_ʋ` | /ʋə/ → [ʋ], word-finally, after [a] [ə] [i] [u] [e] [o] [æ] [ɔ] and 38 more | - | - |
| `MR_ANUSVARA_VELAR` | /̃/ → [ŋ], spelled ⟨ं⟩, before ⟨क⟩ ⟨ख⟩ ⟨ग⟩ ⟨घ⟩ | ⟨अंक⟩ [əŋkə] | [Masica 1991](#src-masica1991), Indo-Aryan Languages 1991 |
| `MR_ANUSVARA_PALATAL` | /̃/ → [n], spelled ⟨ं⟩, before ⟨च⟩ ⟨छ⟩ ⟨ज⟩ ⟨झ⟩ | ⟨अंजीर⟩ [ənd͡ʑiɾ] | - |
| `MR_ANUSVARA_RETROFLEX` | /̃/ → [ɳ], spelled ⟨ं⟩, before ⟨ट⟩ ⟨ठ⟩ ⟨ड⟩ ⟨ढ⟩ | - | - |
| `MR_ANUSVARA_DENTAL` | /̃/ → [n], spelled ⟨ं⟩, before ⟨त⟩ ⟨थ⟩ ⟨द⟩ ⟨ध⟩ | - | - |
| `MR_ANUSVARA_LABIAL` | /̃/ → [m], spelled ⟨ं⟩, before ⟨प⟩ ⟨फ⟩ ⟨ब⟩ ⟨भ⟩ | - | - |
| `MR_AFFRICATE_PALATAL_ts` | /ts/ → [tɕ], before [i] [e] [æ] [j] | - | [Dhongde 2009](#src-dhongde_wali2009), John Benjamins 2009 |
| `MR_AFFRICATE_PALATAL_dz` | /dz/ → [dʑ], before [i] [e] [æ] [j] | - | - |
| `MR_AFFRICATE_PALATAL_dzʱ` | /dzʱ/ → [dʑʱ], before [i] [e] [æ] [j] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Maquiritari](mch.md) · [Home](../index.md) · [Marchigiano →](it-IT-x-marche.md)
