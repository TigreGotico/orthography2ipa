# Tamil (`ta`)

<!-- atlas:summary begin -->
Tamil is a Dravidian language, written in the Tamil script. Glottolog places it in India and Sri Lanka. The `ta` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ta` |
| ISO 639-3 | [tam](https://iso639-3.sil.org/code/tam), Tamil |
| Glottolog | [tami1289](https://glottolog.org/resource/languoid/id/tami1289), Tamil |
| Wikidata | [Q5885](https://www.wikidata.org/wiki/Q5885) |
| Wikipedia | [Tamil language](https://en.wikipedia.org/wiki/Tamil_language) |
| Family | [Dravidian](by-family.md#dravidian) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india), [Sri Lanka](by-region.md#sri-lanka) |
| Script | [Tamil](by-script.md#tamil) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from -300, living |
| Ancestor | [Proto-Dravidian](https://tigregotico.github.io/orthography2ipa/#ta-x-proto-dravidia) `ta-x-proto-dravidia` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`ta` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ta) |
| Spec file | [`ta.json`](../../orthography2ipa/data/ta.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Tamil (Tamil Nadu, India + Sri Lanka). Dravidian language, not related to Indo-Aryan.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1996 to 2004. [Sources](#sources) lists them. The spec file writes all 50 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ta.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `ta` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Malayalam](ml.md) `ml`: India, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 0 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-krishnamurti2003"></a>Krishnamurti, B. (2003). *The Dravidian Languages*. Cambridge University Press.
2. <a id="src-schiffman1999"></a>Schiffman, H.F. (1999). *A Reference Grammar of Spoken Tamil*. Cambridge University Press. Cited: 7.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
4. <a id="src-keane2004"></a>Keane, E. (2004). *Tamil*. Illustrations of the IPA, Journal of the International Phonetic Association 34(1). Cited: 111-116.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ta` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 10093 | 0.3757 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ta` | generated | epitran-derived | CC0 1.0 | 135937 | 0.1214 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 86 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pː |  |  | d̪ t̪ t̪ː |  | ɖ ʈ ʈː |  | k kː ɡ |  |
| Affricate |  |  |  |  | dʒ dʒː |  | dʑ tɕ tɕː |  |  |
| Nasal | m mː |  |  | n nː n̪ |  | ɳ ɳː | ɲ ɲː | ŋ ŋː |  |
| Trill |  |  |  | r rː |  |  |  |  |  |
| Tap |  |  |  | ɾ |  | ɽ |  |  |  |
| Fricative | β | v | ð | s sː | ʃ ʃː | ʂ ʂː | ɕ | x xː | h hː |
| Approximant |  | ʋ ʋː |  |  |  | ɻ ɻː | j jː |  |  |
| Lateral approximant |  |  |  | l lː |  | ɭ ɭː |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː ɯ |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ai] [au] [ba] [dʑa] [d̪a] [ka] [kʂ] [kʂː] [pa] [sa] [tɕa] [tɾ] [t̪a] [w] [ɖa] [ɡa] [ʃriː] [ʃriːː] [ʈa].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ஃ⟩ | [x] [h] ∅ |  |
| ⟨அ⟩ | [a] |  |
| ⟨ஆ⟩ | [aː] |  |
| ⟨இ⟩ | [i] |  |
| ⟨ஈ⟩ | [iː] |  |
| ⟨உ⟩ | [u] |  |
| ⟨ஊ⟩ | [uː] |  |
| ⟨எ⟩ | [e] |  |
| ⟨ஏ⟩ | [eː] |  |
| ⟨ஐ⟩ | [ai] |  |
| ⟨ஒ⟩ | [o] |  |
| ⟨ஓ⟩ | [oː] |  |
| ⟨ஔ⟩ | [au] |  |
| ⟨க⟩ | [k] [ɡ] [x] |  |
| ⟨க்ஷ⟩ | [kʂ] |  |
| ⟨ங⟩ | [ŋ] |  |
| ⟨ச⟩ | [tɕ] [s] [dʑ] |  |
| ⟨ஜ⟩ | [dʒ] |  |
| ⟨ஞ⟩ | [ɲ] |  |
| ⟨ட⟩ | [ʈ] [ɖ] |  |
| ⟨ண⟩ | [ɳ] |  |
| ⟨த⟩ | [t̪] [d̪] [ð] |  |
| ⟨ந⟩ | [n] |  |
| ⟨ன⟩ | [n] |  |
| ⟨ப⟩ | [p] [b] |  |
| ⟨ம⟩ | [m] |  |
| ⟨ய⟩ | [j] |  |
| ⟨ர⟩ | [ɾ] |  |
| ⟨ற⟩ | [r] [tɾ] |  |
| ⟨ல⟩ | [l] |  |
| ⟨ள⟩ | [ɭ] |  |
| ⟨ழ⟩ | [ɻ] |  |
| ⟨வ⟩ | [ʋ] [v] |  |
| ⟨ஶ⟩ | [ʃ] |  |
| ⟨ஷ⟩ | [ʂ] |  |
| ⟨ஸ⟩ | [s] |  |
| ⟨ஸ்ரீ⟩ | [ʃriː] |  |
| ⟨ஹ⟩ | [h] |  |
| ⟨ா⟩ | [aː] |  |
| ⟨ி⟩ | [i] |  |
| ⟨ீ⟩ | [iː] |  |
| ⟨ு⟩ | [u] |  |
| ⟨ூ⟩ | [uː] |  |
| ⟨ெ⟩ | [e] |  |
| ⟨ே⟩ | [eː] |  |
| ⟨ை⟩ | [ai] |  |
| ⟨ொ⟩ | [o] |  |
| ⟨ோ⟩ | [oː] |  |
| ⟨ௌ⟩ | [au] |  |
| ⟨்⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 102 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `TA_GEM1_dʒ` | /dʒ/ → [dʒː], before [dʒa] [dʒ] | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_GEM1_h` | /h/ → [hː], before [ha] [h] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_j` | /j/ → [jː], before [ja] [j] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_k` | /k/ → [kː], before [ka] [k] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_kʂ` | /kʂ/ → [kʂː], before [kʂa] [kʂ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_l` | /l/ → [lː], before [la] [l] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_m` | /m/ → [mː], before [ma] [m] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_n` | /n/ → [nː], before [na] [n] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_p` | /p/ → [pː], before [pa] [p] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_r` | /r/ → [rː], before [ra] [r] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_s` | /s/ → [sː], before [sa] [s] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_tɕ` | /tɕ/ → [tɕː], before [tɕa] [tɕ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_t̪` | /t̪/ → [t̪ː], before [t̪a] [t̪] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_x` | /x/ → [xː], before [xa] [x] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ŋ` | /ŋ/ → [ŋː], before [ŋa] [ŋ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ɭ` | /ɭ/ → [ɭː], before [ɭa] [ɭ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ɲ` | /ɲ/ → [ɲː], before [ɲa] [ɲ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ɳ` | /ɳ/ → [ɳː], before [ɳa] [ɳ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ɻ` | /ɻ/ → [ɻː], before [ɻa] [ɻ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ʂ` | /ʂ/ → [ʂː], before [ʂa] [ʂ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ʃ` | /ʃ/ → [ʃː], before [ʃa] [ʃ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ʃriː` | /ʃriː/ → [ʃriːː], before [ʃriːa] [ʃriː] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ʈ` | /ʈ/ → [ʈː], before [ʈa] [ʈ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM1_ʋ` | /ʋ/ → [ʋː], before [ʋa] [ʋ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_dʒa` | /dʒa/ → [a], after [dʒ] | ⟨பக்கம்⟩ [pakːam] | [Keane 2004](#src-keane2004) |
| `TA_GEM2_dʒ` | /dʒ/ → ∅, after [dʒ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ha` | /ha/ → [a], after [h] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_h` | /h/ → ∅, after [h], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ja` | /ja/ → [a], after [j] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_j` | /j/ → ∅, after [j], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ka` | /ka/ → [a], after [k] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_k` | /k/ → ∅, after [k], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_kʂa` | /kʂa/ → [a], after [kʂ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_kʂ` | /kʂ/ → ∅, after [kʂ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_la` | /la/ → [a], after [l] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_l` | /l/ → ∅, after [l], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ma` | /ma/ → [a], after [m] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_m` | /m/ → ∅, after [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_na` | /na/ → [a], after [n] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_n` | /n/ → ∅, after [n], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_pa` | /pa/ → [a], after [p] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_p` | /p/ → ∅, after [p], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ra` | /ra/ → [a], after [r] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_r` | /r/ → ∅, after [r], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_sa` | /sa/ → [a], after [s] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_s` | /s/ → ∅, after [s], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_tɕa` | /tɕa/ → [a], after [tɕ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_tɕ` | /tɕ/ → ∅, after [tɕ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_t̪a` | /t̪a/ → [a], after [t̪] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_t̪` | /t̪/ → ∅, after [t̪], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_xa` | /xa/ → [a], after [x] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_x` | /x/ → ∅, after [x], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ŋa` | /ŋa/ → [a], after [ŋ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ŋ` | /ŋ/ → ∅, after [ŋ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ɭa` | /ɭa/ → [a], after [ɭ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ɭ` | /ɭ/ → ∅, after [ɭ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ɲa` | /ɲa/ → [a], after [ɲ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ɲ` | /ɲ/ → ∅, after [ɲ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ɳa` | /ɳa/ → [a], after [ɳ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ɳ` | /ɳ/ → ∅, after [ɳ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ɻa` | /ɻa/ → [a], after [ɻ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ɻ` | /ɻ/ → ∅, after [ɻ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʂa` | /ʂa/ → [a], after [ʂ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʂ` | /ʂ/ → ∅, after [ʂ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʃa` | /ʃa/ → [a], after [ʃ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʃ` | /ʃ/ → ∅, after [ʃ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʃriːa` | /ʃriːa/ → [a], after [ʃriː] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʃriː` | /ʃriː/ → ∅, after [ʃriː], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʈa` | /ʈa/ → [a], after [ʈ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʈ` | /ʈ/ → ∅, after [ʈ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʋa` | /ʋa/ → [a], after [ʋ] | - | [Keane 2004](#src-keane2004) |
| `TA_GEM2_ʋ` | /ʋ/ → ∅, after [ʋ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_ka` | /ka/ → [ka], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | ⟨கற்க⟩ [karka] | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_k` | /k/ → [k], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_pa` | /pa/ → [pa], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_p` | /p/ → [p], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_tɕa` | /tɕa/ → [tɕa], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_tɕ` | /tɕ/ → [tɕ], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_t̪a` | /t̪a/ → [t̪a], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_t̪` | /t̪/ → [t̪], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_ʈa` | /ʈa/ → [ʈa], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | [Keane 2004](#src-keane2004) |
| `TA_NOVOICE_ʈ` | /ʈ/ → [ʈ], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_ka` | /ka/ → [ɡa], after [ŋ] [ɲ] [ɳ] [n] [m] | ⟨புத்தகம்⟩ [put̪ːaɡam] | [Krishnamurti 2003](#src-krishnamurti2003), [Schiffman 1999](#src-schiffman1999), [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_k` | /k/ → [ɡ], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_pa` | /pa/ → [ba], after [ŋ] [ɲ] [ɳ] [n] [m] | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_p` | /p/ → [b], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_tɕa` | /tɕa/ → [dʑa], after [ŋ] [ɲ] [ɳ] [n] [m] | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_tɕ` | /tɕ/ → [dʑ], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_t̪a` | /t̪a/ → [d̪a], after [ŋ] [ɲ] [ɳ] [n] [m] | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_t̪` | /t̪/ → [d̪], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_ʈa` | /ʈa/ → [ɖa], after [ŋ] [ɲ] [ɳ] [n] [m] | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_N_ʈ` | /ʈ/ → [ɖ], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_ka` | /ka/ → [ɡa], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_k` | /k/ → [ɡ], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_pa` | /pa/ → [ba], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_p` | /p/ → [b], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_tɕa` | /tɕa/ → [sa], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_tɕ` | /tɕ/ → [s], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_t̪a` | /t̪a/ → [d̪a], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_t̪` | /t̪/ → [d̪], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_ʈa` | /ʈa/ → [ɖa], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
| `TA_VOICE_ʈ` | /ʈ/ → [ɖ], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Keane 2004](#src-keane2004) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ta")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Talysh](tly.md) · [Home](../index.md) · [Tarifit →](rif.md)
