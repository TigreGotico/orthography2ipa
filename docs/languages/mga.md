# Middle Irish (900-1200) (`mga`)

<!-- atlas:summary begin -->
Middle Irish (900-1200) is a Goidelic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `mga` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mga` |
| ISO 639-3 | [mga](https://iso639-3.sil.org/code/mga), Middle Irish (900-1200) |
| Wikipedia | [Middle Irish](https://en.wikipedia.org/wiki/Middle_Irish) |
| Family | [Indo-European](by-family.md#indo-european) > [Celtic > Goidelic](by-family.md#indo-european--celtic--goidelic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Goidelic](https://tigregotico.github.io/orthography2ipa/#x-clade-goid1240) `x-clade-goid1240` |
| Explorer | [`mga` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mga) |
| Spec file | [`mga.json`](../../orthography2ipa/data/mga.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Middle Irish (c. 900-1200), the Goidelic stage between Old Irish and Early Modern Irish, written in the Latin alphabet. The spec models the four things Middle Irish spelling actually encodes.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1946 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 52 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mga.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mga` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mga_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Middle Irish (10-12th century) (midd1360)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/midd1360)
2. <a id="src-thurneysen1946"></a>Thurneysen, Rudolf (trans. D. A. Binchy & Osborn Bergin) (1946). *A Grammar of Old Irish*. Dublin Institute for Advanced Studies.
3. <a id="src-breatnach1994"></a>Breatnach, Liam (1994). *An Mheán-Ghaeilge, in Stair na Gaeilge*. Roinn na Sean-Ghaeilge, Coláiste Phádraig, Maigh Nuad.
4. <a id="src-mccone2005"></a>McCone, Kim (2005). *A First Old Irish Grammar and Reader*. Department of Old Irish, National University of Ireland, Maynooth.
5. <a id="src-mga_wikipedia"></a>Wikipedia contributors (2024). *Middle Irish (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Middle_Irish)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mga` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 328 | 0.0594 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 61 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Dental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d d̠ʲ t t̠ʲ |  | k kʲ ɡ ɡʲ |  |
| Nasal | m mʲ |  | n nʲ n̠ʲ |  | ŋ |  |
| Trill |  |  | r rʲ |  |  |  |
| Tap |  |  | ɾ ɾʲ |  |  |  |
| Fricative | ɸ ɸʲ β βʲ β̃ β̃ʲ | ð ðʲ θ θʲ | s | ɕ | x xʲ ɣ ɣʲ | h |
| Lateral approximant |  |  | l lʲ l̠ʲ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e eː |  | o oː ɤː |
| Mid |  | ə |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [eo̯] [e̯oː] [iə̯] [iːə] [uːə] [ŋɡ] [ŋɡʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | nucleus unstressed [ə] |
| ⟨ae⟩ | [ɤː] |  |
| ⟨ao⟩ | [ɤː] |  |
| ⟨aí⟩ | [ɤː] |  |
| ⟨b⟩ | [b] | after i [bʲ] · before back vowel [b] · before front vowel [bʲ] |
| ⟨bb⟩ | [b] | after i [bʲ] · before back vowel [b] · before front vowel [bʲ] |
| ⟨c⟩ | [k] | after i [kʲ] · before back vowel [k] · before front vowel [kʲ] |
| ⟨cc⟩ | [k] | after i [kʲ] · before back vowel [k] · before front vowel [kʲ] |
| ⟨ch⟩ | [x] | after i [xʲ] · before back vowel [x] · before front vowel [xʲ] |
| ⟨d⟩ | [d] | after i [d̠ʲ] · before back vowel [d] · before front vowel [d̠ʲ] |
| ⟨dd⟩ | [d] | after i [d̠ʲ] · before back vowel [d] · before front vowel [d̠ʲ] |
| ⟨e⟩ | [e] | nucleus unstressed [ə] |
| ⟨eo⟩ | [eo̯] |  |
| ⟨eó⟩ | [e̯oː] |  |
| ⟨f⟩ | [ɸ] | after i [ɸʲ] · before back vowel [ɸ] · before front vowel [ɸʲ] |
| ⟨fh⟩ | ∅ |  |
| ⟨g⟩ | [ɡ] | after i [ɡʲ] · before back vowel [ɡ] · before front vowel [ɡʲ] |
| ⟨gg⟩ | [ɡ] | after i [ɡʲ] · before back vowel [ɡ] · before front vowel [ɡʲ] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] | nucleus unstressed [ə] |
| ⟨ia⟩ | [iə̯] |  |
| ⟨l⟩ | [l] | after i [lʲ] · before back vowel [l] · before front vowel [lʲ] |
| ⟨ll⟩ | [l] | after i [l̠ʲ] · before back vowel [l] · before front vowel [l̠ʲ] |
| ⟨m⟩ | [m] | after i [mʲ] · before back vowel [m] · before front vowel [mʲ] |
| ⟨mb⟩ | [m] | after i [mʲ] · before back vowel [m] · before front vowel [mʲ] |
| ⟨mm⟩ | [m] | after i [mʲ] · before back vowel [m] · before front vowel [mʲ] |
| ⟨n⟩ | [n] | after i [nʲ] · before back vowel [n] · before front vowel [nʲ] |
| ⟨ng⟩ | [ŋɡ] | after i [ŋɡʲ] · before back vowel [ŋɡ] · before front vowel [ŋɡʲ] · word final [ŋ] |
| ⟨nn⟩ | [n] | after i [n̠ʲ] · before back vowel [n] · before front vowel [n̠ʲ] |
| ⟨o⟩ | [o] | nucleus unstressed [ə] |
| ⟨oí⟩ | [ɤː] |  |
| ⟨p⟩ | [p] | after i [pʲ] · before back vowel [p] · before front vowel [pʲ] |
| ⟨ph⟩ | [ɸ] | after i [ɸʲ] · before back vowel [ɸ] · before front vowel [ɸʲ] |
| ⟨pp⟩ | [p] | after i [pʲ] · before back vowel [p] · before front vowel [pʲ] |
| ⟨r⟩ | [ɾ] | after i [ɾʲ] · before back vowel [ɾ] · before front vowel [ɾʲ] |
| ⟨rr⟩ | [r] | after i [rʲ] · before back vowel [r] · before front vowel [rʲ] |
| ⟨s⟩ | [s] | after i [ɕ] · before back vowel [s] · before front vowel [ɕ] |
| ⟨sh⟩ | [h] |  |
| ⟨t⟩ | [t] | after i [t̠ʲ] · before back vowel [t] · before front vowel [t̠ʲ] |
| ⟨th⟩ | [θ] | after i [θʲ] · before back vowel [θ] · before front vowel [θʲ] |
| ⟨tt⟩ | [t] | after i [t̠ʲ] · before back vowel [t] · before front vowel [t̠ʲ] |
| ⟨u⟩ | [u] | nucleus unstressed [ə] |
| ⟨á⟩ | [aː] |  |
| ⟨áe⟩ | [ɤː] |  |
| ⟨é⟩ | [eː] |  |
| ⟨éo⟩ | [e̯oː] |  |
| ⟨í⟩ | [iː] |  |
| ⟨ía⟩ | [iːə] |  |
| ⟨ó⟩ | [oː] |  |
| ⟨óe⟩ | [ɤː] |  |
| ⟨ú⟩ | [uː] |  |
| ⟨úa⟩ | [uːə] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 46 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `MGA_LENITION_b` | /b/ → [β], after a vowel, spelled ⟨b⟩ | ⟨abacc⟩ [aβək] | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_d` | /d/ → [ð], after a vowel, spelled ⟨d⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_ɡ` | /ɡ/ → [ɣ], after a vowel, spelled ⟨g⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_bʲ` | /bʲ/ → [βʲ], after a vowel, spelled ⟨b⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_d̠ʲ` | /d̠ʲ/ → [ðʲ], after a vowel, spelled ⟨d⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_ɡʲ` | /ɡʲ/ → [ɣʲ], after a vowel, spelled ⟨g⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_m_BEFORE_VOWEL` | /m/ → [β̃], after a vowel, before a vowel, spelled ⟨m⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_m_BEFORE_LIQUID` | /m/ → [β̃], after a vowel, spelled ⟨m⟩, before ⟨l⟩ ⟨r⟩ ⟨ll⟩ ⟨rr⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_m_WORD_FINAL` | /m/ → [β̃], after a vowel, before a word boundary, spelled ⟨m⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_mʲ_BEFORE_VOWEL` | /mʲ/ → [β̃ʲ], after a vowel, before a vowel, spelled ⟨m⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_mʲ_BEFORE_LIQUID` | /mʲ/ → [β̃ʲ], after a vowel, spelled ⟨m⟩, before ⟨l⟩ ⟨r⟩ ⟨ll⟩ ⟨rr⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_LENITION_mʲ_WORD_FINAL` | /mʲ/ → [β̃ʲ], after a vowel, before a word boundary, spelled ⟨m⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_MEDIAL_VOICING_k` | /k/ → [ɡ], after a vowel, spelled ⟨c⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_MEDIAL_VOICING_kʲ` | /kʲ/ → [ɡʲ], after a vowel, spelled ⟨c⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_MEDIAL_VOICING_t` | /t/ → [d], after a vowel, spelled ⟨t⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_MEDIAL_VOICING_t̠ʲ` | /t̠ʲ/ → [d̠ʲ], after a vowel, spelled ⟨t⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_MEDIAL_VOICING_p` | /p/ → [b], after a vowel, spelled ⟨p⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_MEDIAL_VOICING_pʲ` | /pʲ/ → [bʲ], after a vowel, spelled ⟨p⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_CLUSTER_QUALITY_t_REGRESSIVE` | /t/ → [t̠ʲ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | ⟨tre⟩ [t̠ʲɾʲe] | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_d_REGRESSIVE` | /d/ → [d̠ʲ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_k_REGRESSIVE` | /k/ → [kʲ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_ɡ_REGRESSIVE` | /ɡ/ → [ɡʲ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_p_REGRESSIVE` | /p/ → [pʲ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_b_REGRESSIVE` | /b/ → [bʲ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_s_REGRESSIVE` | /s/ → [ɕ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | ⟨slis⟩ [ɕlʲiɕ] | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_ɸ_REGRESSIVE` | /ɸ/ → [ɸʲ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_x_REGRESSIVE` | /x/ → [xʲ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | ⟨icht⟩ [ixʲt̠ʲ] | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_θ_REGRESSIVE` | /θ/ → [θʲ], before [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_t_PROGRESSIVE` | /t/ → [t̠ʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | ⟨tre⟩ [t̠ʲɾʲe] | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_d_PROGRESSIVE` | /d/ → [d̠ʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_k_PROGRESSIVE` | /k/ → [kʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_ɡ_PROGRESSIVE` | /ɡ/ → [ɡʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_p_PROGRESSIVE` | /p/ → [pʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_b_PROGRESSIVE` | /b/ → [bʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_s_PROGRESSIVE` | /s/ → [ɕ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | ⟨slis⟩ [ɕlʲiɕ] | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_ɸ_PROGRESSIVE` | /ɸ/ → [ɸʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_x_PROGRESSIVE` | /x/ → [xʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | ⟨icht⟩ [ixʲt̠ʲ] | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_θ_PROGRESSIVE` | /θ/ → [θʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_FORTIS_R_ɾ` | /ɾ/ → [r], word-initially, spelled ⟨r⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_FORTIS_R_ɾʲ` | /ɾʲ/ → [rʲ], word-initially, spelled ⟨r⟩ | - | [Thurneysen 1946](#src-thurneysen1946), [Breatnach 1994](#src-breatnach1994) |
| `MGA_GLIDE_I_AFTER_VOWEL` | /i ə/ → ∅, after a vowel, spelled ⟨i⟩ | ⟨aile⟩ [alʲə] | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_GLIDE_BEFORE_BACK_VOWEL` | /e i ə/ → ∅, after a consonant, before a back vowel, spelled ⟨e⟩ ⟨i⟩ | ⟨aile⟩ [alʲə] | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_m_PROGRESSIVE` | /m/ → [mʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_n_PROGRESSIVE` | /n/ → [nʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | - | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_l_PROGRESSIVE` | /l/ → [lʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | ⟨slis⟩ [ɕlʲiɕ] | [Thurneysen 1946](#src-thurneysen1946) |
| `MGA_CLUSTER_QUALITY_ɾ_PROGRESSIVE` | /ɾ/ → [ɾʲ], word-finally, after [ɾʲ] [rʲ] [lʲ] [l̠ʲ] [nʲ] [n̠ʲ] [mʲ] [β̃ʲ] and 13 more | ⟨tre⟩ [t̠ʲɾʲe] | [Thurneysen 1946](#src-thurneysen1946) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mga")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Middle Dutch](dum.md) · [Home](../index.md) · [Middle Low German →](gml.md)
