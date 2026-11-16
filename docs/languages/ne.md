# Nepali (`ne`)

<!-- atlas:summary begin -->
Nepali is an Indo-Aryan language, written in the Devanagari script. Glottolog places it in Nepal. The `ne` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ne` |
| ISO 639-3 | [nep](https://iso639-3.sil.org/code/nep), Nepali (macrolanguage) |
| Glottolog | [nepa1254](https://glottolog.org/resource/languoid/id/nepa1254), Nepali |
| Wikidata | [Q33823](https://www.wikidata.org/wiki/Q33823) |
| Wikipedia | [Nepali language](https://en.wikipedia.org/wiki/Nepali_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Nepal](by-region.md#nepal) |
| Script | [Devanagari](by-script.md#devanagari) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1700, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Explorer | [`ne` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ne) |
| Spec file | [`ne.json`](../../orthography2ipa/data/ne.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard (eastern) Nepali, the variety of the national media.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1971 to 2009. [Sources](#sources) lists them. The spec file writes all 62 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ne.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ne` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 1 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-khatiwada2009"></a>Khatiwada, R. (2009). *Nepali (Illustrations of the IPA)*. Journal of the International Phonetic Association 39(3). Cited: 373-380. [doi.org](https://doi.org/10.1017/S0025100309990181)
2. <a id="src-bandhu1971"></a>Bandhu, C., Dahal, B. M., Holzhausen, A. & Hale, A. (1971). *Nepali segmental phonology*. Summer Institute of Linguistics / Tribhuvan University.
3. <a id="src-pokharel1989"></a>Pokharel, M. P. (1989). *Experimental analysis of Nepali sound system*. Ph.D. dissertation, University of Pune.
4. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
5. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
6. <a id="src-matthews1984"></a>Matthews, D.J. (1984). *A Course in Nepali*. SOAS.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `kaikki` ([kaikki.org](https://kaikki.org/dictionary/)) | `ne` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2052 | 0.1191 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 85 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ | d̪ t̪ t̪ʰ | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  | dz ts tsʰ |  |  |  |  |
| Nasal | m | n | ɳ |  | ŋ |  |
| Trill |  | r |  |  |  |  |
| Tap |  | ɾ | ɽ ɽ̃ |  |  |  |
| Fricative | ɸ β | s |  |  | x ɣ | h ɦ |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid |  | ʌ |
| Open | ä |  |

Sequences that the spec writes as one unit: [bʌ] [bʱ] [bʱʌ] [dzʌ] [dzʱ] [dzʱʌ] [d̪ʌ] [d̪ʱ] [d̪ʱʌ] [jʌ] [ktsʰ] [ktsʰʌ] [kʌ] [kʰʌ] [lʌ] [mʌ] [nʌ] [pʌ] [pʰʌ] [ri] [rʌ] [sʌ] [tsʌ] [tsʰʌ] [t̪ʌ] [t̪ʰʌ] [w] [wʌ] [ŋʌ] [ɖʌ] [ɖʱ] [ɖʱʌ] [ɡj] [ɡjʌ] [ɡʌ] [ɡʱ] [ɡʱʌ] [ɦʌ] [ɳʌ] [ɽʌ], and 7 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ँ⟩ | [̃] |  |
| ⟨ं⟩ | [̃] | before consonant [n] · default [̃] · word final [̃] |
| ⟨ः⟩ | ∅ |  |
| ⟨अ⟩ | [ʌ] |  |
| ⟨आ⟩ | [ä] |  |
| ⟨इ⟩ | [i] |  |
| ⟨ई⟩ | [i] |  |
| ⟨उ⟩ | [u] |  |
| ⟨ऊ⟩ | [u] |  |
| ⟨ऋ⟩ | [ri] |  |
| ⟨ए⟩ | [e] |  |
| ⟨ऐ⟩ | [ʌi] |  |
| ⟨ओ⟩ | [o] |  |
| ⟨औ⟩ | [ʌu] |  |
| ⟨क⟩ | [k] |  |
| ⟨क्ष⟩ | [ktsʰ] |  |
| ⟨ख⟩ | [kʰ] |  |
| ⟨ग⟩ | [ɡ] |  |
| ⟨घ⟩ | [ɡʱ] |  |
| ⟨ङ⟩ | [ŋ] |  |
| ⟨च⟩ | [ts] |  |
| ⟨छ⟩ | [tsʰ] |  |
| ⟨ज⟩ | [dz] |  |
| ⟨ज्ञ⟩ | [ɡj] |  |
| ⟨झ⟩ | [dzʱ] |  |
| ⟨ञ⟩ | [n] |  |
| ⟨ट⟩ | [ʈ] |  |
| ⟨ठ⟩ | [ʈʰ] |  |
| ⟨ड⟩ | [ɖ] |  |
| ⟨ड़⟩ | [ɽ] |  |
| ⟨ढ⟩ | [ɖʱ] |  |
| ⟨ढ़⟩ | [ɽʱ] |  |
| ⟨ण⟩ | [ɳ] |  |
| ⟨त⟩ | [t̪] |  |
| ⟨थ⟩ | [t̪ʰ] |  |
| ⟨द⟩ | [d̪] |  |
| ⟨ध⟩ | [d̪ʱ] |  |
| ⟨न⟩ | [n] |  |
| ⟨प⟩ | [p] |  |
| ⟨फ⟩ | [pʰ] |  |
| ⟨ब⟩ | [b] |  |
| ⟨भ⟩ | [bʱ] |  |
| ⟨म⟩ | [m] |  |
| ⟨य⟩ | [j] |  |
| ⟨र⟩ | [r] |  |
| ⟨ल⟩ | [l] |  |
| ⟨व⟩ | [w] |  |
| ⟨श⟩ | [s] |  |
| ⟨ष⟩ | [s] |  |
| ⟨स⟩ | [s] |  |
| ⟨ह⟩ | [ɦ] |  |
| ⟨ा⟩ | [ä] |  |
| ⟨ि⟩ | [i] |  |
| ⟨ी⟩ | [i] |  |
| ⟨ु⟩ | [u] |  |
| ⟨ू⟩ | [u] |  |
| ⟨ृ⟩ | [ri] |  |
| ⟨े⟩ | [e] |  |
| ⟨ै⟩ | [ʌi] |  |
| ⟨ो⟩ | [o] |  |
| ⟨ौ⟩ | [ʌu] |  |
| ⟨्⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 71 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NE_ANUSVARA_VELAR` | /n/ → [ŋ], before [k] [kʰ] [ɡ] [ɡʱ] [ŋ], spelled ⟨ं⟩ | ⟨संगीत⟩ [sʌŋɡit̪] | [Khatiwada 2009](#src-khatiwada2009) |
| `NE_ANUSVARA_LABIAL` | /n/ → [m], before [p] [pʰ] [b] [bʱ] [m] [w], spelled ⟨ं⟩ | - | - |
| `NE_ANUSVARA_RETROFLEX` | /n/ → [ɳ], before [ʈ] [ʈʰ] [ɖ] [ɖʱ] [ɳ], spelled ⟨ं⟩ | - | - |
| `NE_SCHWA_KEEP_b` | /bʌ/ → [bʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_bʱ` | /bʱʌ/ → [bʱʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_dz` | /dzʌ/ → [dzʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_dzʱ` | /dzʱʌ/ → [dzʱʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_d̪` | /d̪ʌ/ → [d̪ʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_d̪ʱ` | /d̪ʱʌ/ → [d̪ʱʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_j` | /jʌ/ → [jʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_k` | /kʌ/ → [kʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ktsʰ` | /ktsʰʌ/ → [ktsʰʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_kʰ` | /kʰʌ/ → [kʰʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_l` | /lʌ/ → [lʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_m` | /mʌ/ → [mʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_n` | /nʌ/ → [nʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_p` | /pʌ/ → [pʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_pʰ` | /pʰʌ/ → [pʰʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_r` | /rʌ/ → [rʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_s` | /sʌ/ → [sʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ts` | /tsʌ/ → [tsʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_tsʰ` | /tsʰʌ/ → [tsʰʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_t̪` | /t̪ʌ/ → [t̪ʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_t̪ʰ` | /t̪ʰʌ/ → [t̪ʰʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_w` | /wʌ/ → [wʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ŋ` | /ŋʌ/ → [ŋʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ɖ` | /ɖʌ/ → [ɖʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ɖʱ` | /ɖʱʌ/ → [ɖʱʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ɡ` | /ɡʌ/ → [ɡʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ɡj` | /ɡjʌ/ → [ɡjʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ɡʱ` | /ɡʱʌ/ → [ɡʱʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ɦ` | /ɦʌ/ → [ɦʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ɳ` | /ɳʌ/ → [ɳʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ɽ` | /ɽʌ/ → [ɽʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ɽʱ` | /ɽʱʌ/ → [ɽʱʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ʈ` | /ʈʌ/ → [ʈʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_KEEP_ʈʰ` | /ʈʰʌ/ → [ʈʰʌ], after [b] [bʱ] [dz] [dzʱ] [d̪] [d̪ʱ] [j] [k] and 26 more | - | - |
| `NE_SCHWA_FINAL_b` | /bʌ/ → [b], not word-initially, word-finally | ⟨stays⟩ [kinʌbʱʌne] | [Khatiwada 2009](#src-khatiwada2009) |
| `NE_SCHWA_FINAL_bʱ` | /bʱʌ/ → [bʱ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_dz` | /dzʌ/ → [dz], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_dzʱ` | /dzʱʌ/ → [dzʱ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_d̪` | /d̪ʌ/ → [d̪], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_d̪ʱ` | /d̪ʱʌ/ → [d̪ʱ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_j` | /jʌ/ → [j], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_k` | /kʌ/ → [k], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ktsʰ` | /ktsʰʌ/ → [ktsʰ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_kʰ` | /kʰʌ/ → [kʰ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_l` | /lʌ/ → [l], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_m` | /mʌ/ → [m], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_n` | /nʌ/ → [n], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_p` | /pʌ/ → [p], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_pʰ` | /pʰʌ/ → [pʰ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_r` | /rʌ/ → [r], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_s` | /sʌ/ → [s], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ts` | /tsʌ/ → [ts], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_tsʰ` | /tsʰʌ/ → [tsʰ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_t̪` | /t̪ʌ/ → [t̪], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_t̪ʰ` | /t̪ʰʌ/ → [t̪ʰ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_w` | /wʌ/ → [w], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ŋ` | /ŋʌ/ → [ŋ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ɖ` | /ɖʌ/ → [ɖ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ɖʱ` | /ɖʱʌ/ → [ɖʱ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ɡ` | /ɡʌ/ → [ɡ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ɡj` | /ɡjʌ/ → [ɡj], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ɡʱ` | /ɡʱʌ/ → [ɡʱ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ɦ` | /ɦʌ/ → [ɦ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ɳ` | /ɳʌ/ → [ɳ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ɽ` | /ɽʌ/ → [ɽ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ɽʱ` | /ɽʱʌ/ → [ɽʱ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ʈ` | /ʈʌ/ → [ʈ], not word-initially, word-finally | - | - |
| `NE_SCHWA_FINAL_ʈʰ` | /ʈʰʌ/ → [ʈʰ], not word-initially, word-finally | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ne")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nenets](yrk.md) · [Home](../index.md) · [Newar →](new.md)
