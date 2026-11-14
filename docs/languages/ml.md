# Malayalam (`ml`)

<!-- atlas:summary begin -->
Malayalam is a Dravidian language, written in the Malayalam script. Glottolog places it in India. The `ml` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ml` |
| ISO 639-3 | [mal](https://iso639-3.sil.org/code/mal), Malayalam |
| Glottolog | [mala1464](https://glottolog.org/resource/languoid/id/mala1464), Malayalam |
| Wikidata | [Q36236](https://www.wikidata.org/wiki/Q36236) |
| Wikipedia | [Malayalam](https://en.wikipedia.org/wiki/Malayalam) |
| Family | [Dravidian](by-family.md#dravidian) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india) |
| Script | [Malayalam](by-script.md#malayalam) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1100, living |
| Parent | [Tamil](ta.md) `ta` |
| Explorer | [`ml` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ml) |
| Spec file | [`ml.json`](../../orthography2ipa/data/ml.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Malayalam (Kerala). Descended from Old Tamil, diverged c. 9th, 13th century CE. Unique phoneme: ⟨ഴ⟩ = /z/ (derived from Proto-Dravidian *ḻ, retained as /z/ only in Malayalam). Uses the most complex Brahmic script (~60 base characters). Phonemic gemination. Heavy Sanskrit vocabulary in formal register.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1996 to 2017. [Sources](#sources) lists them. The spec file writes all 72 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ml.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ml` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 1 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-krishnamurti2003"></a>Krishnamurti, B. (2003). *The Dravidian Languages*. Cambridge University Press.
2. <a id="src-asher_kumari1997"></a>Asher, R.E. & Kumari, T.C. (1997). *Malayalam*. Routledge. Cited: 405-406.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
4. <a id="src-namboodiripad_garellek2017"></a>Namboodiripad, S. & Garellek, M. (2017). *Illustrations of the IPA: Malayalam (Namboodiri Dialect)*. Journal of the International Phonetic Association 47(1). Cited: 109-118. [doi.org](https://doi.org/10.1017/S0025100315000407)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ml` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 9464 | 0.2623 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ml` | generated | epitran-derived | CC0 1.0 | 6464 | 0.1468 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 87 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ pː |  | d̪ tː t̪ t̪ʰ t̪ː |  | ɖ ʈ ʈʰ ʈː |  | k kʰ kː ɡ |  |
| Affricate |  |  |  | dʒː |  | dʑ tɕ tɕʰ tɕː |  |  |
| Nasal | m mː ̃m |  | n nː |  | ɳ ɳː | ɲ ɲː | ŋ ŋː |  |
| Trill |  |  | r r̩ r̩ː |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  |  | s sː | ʃ ʃː | ʂ ʂː |  | xː | h hː |
| Approximant |  | ʋ ʋː |  |  | ɻ ɻː | j jː |  |  |
| Lateral approximant |  |  | l lː l̩ |  | ɭ ɭː |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ai] [au] [ba] [bʱ] [dʑa] [dʑʱ] [d̪a] [d̪ʱ] [ka] [kʂː] [pa] [tɕa] [t̪a] [w] [ɖa] [ɖʱ] [ɡa] [ɡʱ] [ʃriːː] [ʈa].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ം⟩ | [̃m] [ŋ] |  |
| ⟨ഃ⟩ | [h] |  |
| ⟨അ⟩ | [a] |  |
| ⟨ആ⟩ | [aː] |  |
| ⟨ഇ⟩ | [i] |  |
| ⟨ഈ⟩ | [iː] |  |
| ⟨ഉ⟩ | [u] |  |
| ⟨ഊ⟩ | [uː] |  |
| ⟨ഋ⟩ | [r̩] |  |
| ⟨ഌ⟩ | [l̩] |  |
| ⟨എ⟩ | [e] |  |
| ⟨ഏ⟩ | [eː] |  |
| ⟨ഐ⟩ | [ai] |  |
| ⟨ഒ⟩ | [o] |  |
| ⟨ഓ⟩ | [oː] |  |
| ⟨ഔ⟩ | [au] |  |
| ⟨ക⟩ | [k] |  |
| ⟨ഖ⟩ | [kʰ] |  |
| ⟨ഗ⟩ | [ɡ] |  |
| ⟨ഘ⟩ | [ɡʱ] |  |
| ⟨ങ⟩ | [ŋ] |  |
| ⟨ച⟩ | [tɕ] |  |
| ⟨ഛ⟩ | [tɕʰ] |  |
| ⟨ജ⟩ | [dʑ] |  |
| ⟨ഝ⟩ | [dʑʱ] |  |
| ⟨ഞ⟩ | [ɲ] |  |
| ⟨ട⟩ | [ʈ] |  |
| ⟨ഠ⟩ | [ʈʰ] |  |
| ⟨ഡ⟩ | [ɖ] |  |
| ⟨ഢ⟩ | [ɖʱ] |  |
| ⟨ണ⟩ | [ɳ] |  |
| ⟨ത⟩ | [t̪] |  |
| ⟨ഥ⟩ | [t̪ʰ] |  |
| ⟨ദ⟩ | [d̪] |  |
| ⟨ധ⟩ | [d̪ʱ] |  |
| ⟨ന⟩ | [n] |  |
| ⟨പ⟩ | [p] |  |
| ⟨ഫ⟩ | [pʰ] |  |
| ⟨ബ⟩ | [b] |  |
| ⟨ഭ⟩ | [bʱ] |  |
| ⟨മ⟩ | [m] |  |
| ⟨യ⟩ | [j] |  |
| ⟨ര⟩ | [ɾ] |  |
| ⟨റ⟩ | [r] |  |
| ⟨ല⟩ | [l] |  |
| ⟨ള⟩ | [ɭ] |  |
| ⟨ഴ⟩ | [ɻ] |  |
| ⟨വ⟩ | [ʋ] |  |
| ⟨ശ⟩ | [ʃ] |  |
| ⟨ഷ⟩ | [ʂ] |  |
| ⟨സ⟩ | [s] |  |
| ⟨ഹ⟩ | [h] |  |
| ⟨ാ⟩ | [aː] |  |
| ⟨ി⟩ | [i] |  |
| ⟨ീ⟩ | [iː] |  |
| ⟨ു⟩ | [u] |  |
| ⟨ൂ⟩ | [uː] |  |
| ⟨ൃ⟩ | [r̩] |  |
| ⟨െ⟩ | [e] |  |
| ⟨േ⟩ | [eː] |  |
| ⟨ൈ⟩ | [ai] |  |
| ⟨ൊ⟩ | [o] |  |
| ⟨ോ⟩ | [oː] |  |
| ⟨ൌ⟩ | [au] |  |
| ⟨്⟩ | ∅ |  |
| ⟨ൠ⟩ | [r̩ː] |  |
| ⟨ൺ⟩ | [ɳ] |  |
| ⟨ൻ⟩ | [n] |  |
| ⟨ർ⟩ | [r] |  |
| ⟨ൽ⟩ | [l] |  |
| ⟨ൾ⟩ | [ɭ] |  |
| ⟨ൿ⟩ | [k] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 103 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `TA_GEM1_dʒ` | /dʒ/ → [dʒː], before [dʒa] [dʒ] | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_GEM1_h` | /h/ → [hː], before [ha] [h] | - | Keane 2004 |
| `TA_GEM1_j` | /j/ → [jː], before [ja] [j] | - | Keane 2004 |
| `TA_GEM1_k` | /k/ → [kː], before [ka] [k] | - | Keane 2004 |
| `TA_GEM1_kʂ` | /kʂ/ → [kʂː], before [kʂa] [kʂ] | - | Keane 2004 |
| `TA_GEM1_l` | /l/ → [lː], before [la] [l] | - | Keane 2004 |
| `TA_GEM1_m` | /m/ → [mː], before [ma] [m] | - | Keane 2004 |
| `TA_GEM1_n` | /n/ → [nː], before [na] [n] | - | Keane 2004 |
| `TA_GEM1_p` | /p/ → [pː], before [pa] [p] | - | Keane 2004 |
| `TA_GEM1_r` | /r/ → [tː], before [ra] [r] | - | [Krishnamurti 2003](#src-krishnamurti2003), [Asher 1997](#src-asher_kumari1997), [Namboodiripad 2017](#src-namboodiripad_garellek2017) |
| `TA_GEM1_s` | /s/ → [sː], before [sa] [s] | - | Keane 2004 |
| `TA_GEM1_tɕ` | /tɕ/ → [tɕː], before [tɕa] [tɕ] | - | Keane 2004 |
| `TA_GEM1_t̪` | /t̪/ → [t̪ː], before [t̪a] [t̪] | - | Keane 2004 |
| `TA_GEM1_x` | /x/ → [xː], before [xa] [x] | - | Keane 2004 |
| `TA_GEM1_ŋ` | /ŋ/ → [ŋː], before [ŋa] [ŋ] | - | Keane 2004 |
| `TA_GEM1_ɭ` | /ɭ/ → [ɭː], before [ɭa] [ɭ] | - | Keane 2004 |
| `TA_GEM1_ɲ` | /ɲ/ → [ɲː], before [ɲa] [ɲ] | - | Keane 2004 |
| `TA_GEM1_ɳ` | /ɳ/ → [ɳː], before [ɳa] [ɳ] | - | Keane 2004 |
| `TA_GEM1_ɻ` | /ɻ/ → [ɻː], before [ɻa] [ɻ] | - | Keane 2004 |
| `TA_GEM1_ʂ` | /ʂ/ → [ʂː], before [ʂa] [ʂ] | - | Keane 2004 |
| `TA_GEM1_ʃ` | /ʃ/ → [ʃː], before [ʃa] [ʃ] | - | Keane 2004 |
| `TA_GEM1_ʃriː` | /ʃriː/ → [ʃriːː], before [ʃriːa] [ʃriː] | - | Keane 2004 |
| `TA_GEM1_ʈ` | /ʈ/ → [ʈː], before [ʈa] [ʈ] | - | Keane 2004 |
| `TA_GEM1_ʋ` | /ʋ/ → [ʋː], before [ʋa] [ʋ] | - | Keane 2004 |
| `TA_GEM2_dʒa` | /dʒa/ → [a], after [dʒ] | ⟨பக்கம்⟩ [pakːam] | Keane 2004 |
| `TA_GEM2_dʒ` | /dʒ/ → ∅, after [dʒ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ha` | /ha/ → [a], after [h] | - | Keane 2004 |
| `TA_GEM2_h` | /h/ → ∅, after [h], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ja` | /ja/ → [a], after [j] | - | Keane 2004 |
| `TA_GEM2_j` | /j/ → ∅, after [j], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ka` | /ka/ → [a], after [k] | - | Keane 2004 |
| `TA_GEM2_k` | /k/ → ∅, after [k], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_kʂa` | /kʂa/ → [a], after [kʂ] | - | Keane 2004 |
| `TA_GEM2_kʂ` | /kʂ/ → ∅, after [kʂ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_la` | /la/ → [a], after [l] | - | Keane 2004 |
| `TA_GEM2_l` | /l/ → ∅, after [l], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ma` | /ma/ → [a], after [m] | - | Keane 2004 |
| `TA_GEM2_m` | /m/ → ∅, after [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_na` | /na/ → [a], after [n] | - | Keane 2004 |
| `TA_GEM2_n` | /n/ → ∅, after [n], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_pa` | /pa/ → [a], after [p] | - | Keane 2004 |
| `TA_GEM2_p` | /p/ → ∅, after [p], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ra` | /ra/ → [a], after [r] | - | Keane 2004 |
| `TA_GEM2_r` | /r/ → ∅, after [r], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Asher 1997](#src-asher_kumari1997), [Namboodiripad 2017](#src-namboodiripad_garellek2017) |
| `TA_GEM2_sa` | /sa/ → [a], after [s] | - | Keane 2004 |
| `TA_GEM2_s` | /s/ → ∅, after [s], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_tɕa` | /tɕa/ → [a], after [tɕ] | - | Keane 2004 |
| `TA_GEM2_tɕ` | /tɕ/ → ∅, after [tɕ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_t̪a` | /t̪a/ → [a], after [t̪] | - | Keane 2004 |
| `TA_GEM2_t̪` | /t̪/ → ∅, after [t̪], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_xa` | /xa/ → [a], after [x] | - | Keane 2004 |
| `TA_GEM2_x` | /x/ → ∅, after [x], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ŋa` | /ŋa/ → [a], after [ŋ] | - | Keane 2004 |
| `TA_GEM2_ŋ` | /ŋ/ → ∅, after [ŋ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ɭa` | /ɭa/ → [a], after [ɭ] | - | Keane 2004 |
| `TA_GEM2_ɭ` | /ɭ/ → ∅, after [ɭ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ɲa` | /ɲa/ → [a], after [ɲ] | - | Keane 2004 |
| `TA_GEM2_ɲ` | /ɲ/ → ∅, after [ɲ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ɳa` | /ɳa/ → [a], after [ɳ] | - | Keane 2004 |
| `TA_GEM2_ɳ` | /ɳ/ → ∅, after [ɳ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ɻa` | /ɻa/ → [a], after [ɻ] | - | Keane 2004 |
| `TA_GEM2_ɻ` | /ɻ/ → ∅, after [ɻ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ʂa` | /ʂa/ → [a], after [ʂ] | - | Keane 2004 |
| `TA_GEM2_ʂ` | /ʂ/ → ∅, after [ʂ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ʃa` | /ʃa/ → [a], after [ʃ] | - | Keane 2004 |
| `TA_GEM2_ʃ` | /ʃ/ → ∅, after [ʃ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ʃriːa` | /ʃriːa/ → [a], after [ʃriː] | - | Keane 2004 |
| `TA_GEM2_ʃriː` | /ʃriː/ → ∅, after [ʃriː], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ʈa` | /ʈa/ → [a], after [ʈ] | - | Keane 2004 |
| `TA_GEM2_ʈ` | /ʈ/ → ∅, after [ʈ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_GEM2_ʋa` | /ʋa/ → [a], after [ʋ] | - | Keane 2004 |
| `TA_GEM2_ʋ` | /ʋ/ → ∅, after [ʋ], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | Keane 2004 |
| `TA_NOVOICE_ka` | /ka/ → [ka], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | ⟨கற்க⟩ [karka] | Keane 2004 |
| `TA_NOVOICE_k` | /k/ → [k], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | Keane 2004 |
| `TA_NOVOICE_pa` | /pa/ → [pa], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | Keane 2004 |
| `TA_NOVOICE_p` | /p/ → [p], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | Keane 2004 |
| `TA_NOVOICE_tɕa` | /tɕa/ → [tɕa], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | Keane 2004 |
| `TA_NOVOICE_tɕ` | /tɕ/ → [tɕ], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | Keane 2004 |
| `TA_NOVOICE_t̪a` | /t̪a/ → [t̪a], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | Keane 2004 |
| `TA_NOVOICE_t̪` | /t̪/ → [t̪], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | Keane 2004 |
| `TA_NOVOICE_ʈa` | /ʈa/ → [ʈa], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | Keane 2004 |
| `TA_NOVOICE_ʈ` | /ʈ/ → [ʈ], after [b] [dʑ] [dʒ] [d̪] [h] [j] [k] [kʂ] and 20 more | - | Keane 2004 |
| `TA_VOICE_N_ka` | /ka/ → [ɡa], after [ŋ] [ɲ] [ɳ] [n] [m] | ⟨புத்தகம்⟩ [put̪ːaɡam] | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004, Schiffman 1999 |
| `TA_VOICE_N_k` | /k/ → [ɡ], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_N_pa` | /pa/ → [ba], after [ŋ] [ɲ] [ɳ] [n] [m] | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_N_p` | /p/ → [b], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_N_tɕa` | /tɕa/ → [dʑa], after [ŋ] [ɲ] [ɳ] [n] [m] | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_N_tɕ` | /tɕ/ → [dʑ], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_N_t̪a` | /t̪a/ → [d̪a], after [ŋ] [ɲ] [ɳ] [n] [m] | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_N_t̪` | /t̪/ → [d̪], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_N_ʈa` | /ʈa/ → [ɖa], after [ŋ] [ɲ] [ɳ] [n] [m] | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_N_ʈ` | /ʈ/ → [ɖ], after [ŋ] [ɲ] [ɳ] [n] [m], before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_ka` | /ka/ → [ɡa], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_k` | /k/ → [ɡ], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_pa` | /pa/ → [ba], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_p` | /p/ → [b], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_tɕa` | /tɕa/ → [dʑa], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), [Asher 1997](#src-asher_kumari1997) |
| `TA_VOICE_tɕ` | /tɕ/ → [dʑ], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), [Asher 1997](#src-asher_kumari1997) |
| `TA_VOICE_t̪a` | /t̪a/ → [d̪a], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_t̪` | /t̪/ → [d̪], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_ʈa` | /ʈa/ → [ɖa], not word-initially | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_VOICE_ʈ` | /ʈ/ → [ɖ], not word-initially, before [a] [aː] [i] [iː] [u] [uː] [e] [eː] and 4 more | - | [Krishnamurti 2003](#src-krishnamurti2003), Keane 2004 |
| `TA_GEM2_r_FINAL` | /r/ → ∅, word-finally, after [r] | - | [Asher 1997](#src-asher_kumari1997), [Namboodiripad 2017](#src-namboodiripad_garellek2017) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ml")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Malay](ms.md) · [Home](../index.md) · [Maldivian →](dv.md)
