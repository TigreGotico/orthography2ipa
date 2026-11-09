# Hindi (`hi`)

<!-- atlas:summary begin -->
Hindi is an Indo-Aryan language, written in the Devanagari script. Glottolog places it in Bangladesh, Bhutan, India and Nepal. The `hi` spec is at the research tier. It cites 6 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `hi` |
| Aliases | `hin` |
| ISO 639-3 | [hin](https://iso639-3.sil.org/code/hin), Hindi |
| Glottolog | [hind1269](https://glottolog.org/resource/languoid/id/hind1269), Hindi |
| Wikidata | [Q1568](https://www.wikidata.org/wiki/Q1568) |
| Wikipedia | [Hindi](https://en.wikipedia.org/wiki/Hindi) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [Bhutan](by-region.md#bhutan), [India](by-region.md#india), [Nepal](by-region.md#nepal) |
| Script | [Devanagari](by-script.md#devanagari) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Child lects | 2, see [Related lects](#related-lects) |
| Explorer | [`hi` in the data explorer](https://tigregotico.github.io/orthography2ipa/#hi) |
| Spec file | [`hi.json`](../../orthography2ipa/data/hi.json) |
<!-- atlas:header end -->

## Overview

The `hi` spec describes Standard Hindi (Khaṛī Bolī) in Devanagari. Its parent is Sanskrit (`sa`). The spec states its own letter table and does not inherit one. Its main rules are the inherent vowel and its deletion, the four-way laryngeal contrast, and the nukta letters of Perso-Arabic loans.

## The Devanagari abugida

Devanagari is an abugida. A consonant letter carries an inherent vowel /ə/, and a vowel sign (mātrā) replaces it. The spec declares /ə/ as its `inherent_vowel`. Hindi deletes the inherent vowel in some positions (see [Schwa deletion](#schwa-deletion)).

| Component | What it does | Engine output |
|:---|:---|:---|
| Consonant letter | Carries the inherent /ə/ | क `kə` |
| Vowel sign (mātrā) | Replaces the inherent vowel | का `kaː` |
| Virama (्) | Removes the inherent vowel | क् `k` |
| Independent vowel | Writes a vowel with no consonant before it | आ `aː` |

## Four-way laryngeal contrast

Hindi stops have four laryngeal categories at each place of articulation (Ohala 1983, Masica 1991):

| Category | Bilabial | Dental | Retroflex | Velar |
|:---|:---:|:---:|:---:|:---:|
| Voiceless unaspirated | प [p] | त [t̪] | ट [ʈ] | क [k] |
| Voiceless aspirated | फ [pʰ] | थ [t̪ʰ] | ठ [ʈʰ] | ख [kʰ] |
| Voiced | ब [b] | द [d̪] | ड [ɖ] | ग [ɡ] |
| Voiced aspirated (breathy) | भ [bʱ] | ध [d̪ʱ] | ढ [ɖʱ] | घ [ɡʱ] |

Dentals and retroflexes contrast. The spec keeps them apart: ताल 'rhythm' gives `t̪aːl`, and टाल 'to put off' gives `ʈaːl`. The nasals are ङ [ŋ], ञ [ɲ], ण [ɳ], न [n] and म [m].

## Retroflex flaps

Between vowels, the retroflex stops ड [ɖ] and ढ [ɖʱ] are flaps [ɽ ɽʱ]. The orthography writes the flaps with a nukta, as ड़ and ढ़, and the spec maps those letters to `ɽ` and `ɽʱ`. The spec has no positional rule for the bare letters, so ड and ढ are always `ɖ` and `ɖʱ`.

| Word | Engine output |
|:---|:---|
| पड़ना 'to fall' | `pəɽnaː` |
| बढ़ना 'to grow' | `bəɽʱnaː` |
| बडा (bare ड) | `bəɖaː` |

## Schwa deletion

Hindi does not pronounce the inherent vowel in two positions. The spec states both as `allophone_rules`, one rule per consonant phoneme.

The `HI_SCHWA_FINAL_*` rules delete the inherent vowel of a word-final consonant letter. They apply after a cluster too, as in शब्द `ʃəbd̪`. They do not apply at the start of a word, so a monosyllabic one-letter word keeps its only vowel: न gives `nə`. The source is Ohala (1983, ch. 5) and Ohala (1999: 101). The `अ` grapheme also has a `word_final` entry that writes nothing.

The `HI_SCHWA_MEDIAL_*` rules delete a medial inherent vowel in the context VC_CV, applied from right to left (Narasimhan, Sproat & Kiraz 2004). The `HI_SCHWA_KEEP_*` rules guard that deletion after a consonant (Ohala 1983, ch. 5).

| Word | Engine output |
|:---|:---|
| कमल 'lotus' | `kəməl` |
| करना 'to do' | `kəɾnaː` |
| अपना 'own' | `əpnaː` |
| राम | `ɾaːm` |

Sanskrit (`sa`) keeps the inherent vowel and declares no such rule. That is why the deletion is in the Hindi data and not in the engine.

## Vowels

| Independent | Mātrā | IPA | Example (engine output) |
|:---:|:---:|:---:|:---|
| अ | (inherent) | [ə] | कमल `kəməl` |
| आ | ा | [aː] | काम `kaːm` 'work' |
| इ | ि | [ɪ] | किताब `kɪt̪aːb` 'book' |
| ई | ी | [iː] | दीवार `d̪iːʋaːɾ` 'wall' |
| उ | ु | [ʊ] | उन `ʊn` 'them' |
| ऊ | ू | [uː] | ऊन `uːn` 'wool' |
| ए | े | [eː] | एक `eːk` 'one' |
| ऐ | ै | [ɛː] | ऐसा `ɛːsaː` 'such' |
| ओ | ो | [oː] | ओस `oːs` 'dew' |
| औ | ौ | [ɔː] | औरत `ɔːɾət̪` 'woman' |

## Nasalisation

Two signs write nasality. Chandrabindu ँ nasalises the vowel. Anusvara ं nasalises the vowel too, and before a consonant it is a nasal at the place of that consonant: अंग is [ɐŋɡ] and अंत is [ɐnt]. The spec writes both signs as nasalisation of the vowel in every position. The `before_consonant` entry of ं is the nasal tilde, not a nasal consonant.

| Word | Engine output |
|:---|:---|
| हाँ 'yes' | `ɦãː` |
| अंग 'body part' | `ə̃ɡ` |
| अंत 'end' | `ə̃t̪` |

## Perso-Arabic loans (nukta letters)

Hindi writes consonants from Perso-Arabic loans with a dot below the letter (nukta). The spec maps each of them:

| Letter | IPA | Origin | Example |
|:---:|:---:|:---|:---|
| क़ | [q] | Arabic ق | क़िस्मत 'fate', `qɪsmət̪` |
| ख़ | [x] | Arabic and Persian خ | ख़त 'letter' |
| ग़ | [ɣ] | Arabic and Persian غ | ग़ैर 'other', `ɣɛːɾ` |
| ज़ | [z] | Arabic and Persian ز | ज़मीन 'earth' |
| फ़ | [f] | Arabic and Persian ف | फ़र्क 'difference' |

Many speakers, mostly in colloquial speech, use the native equivalents (q to k, x to kʰ, z to dʒ, f to pʰ). The spec writes the loan value.

## Known limitations

A word-initial nukta letter with no vowel sign loses its inherent vowel. ख़त gives `xt̪`, ज़मीन gives `zmiːn`, and फ़र्क gives `fɾk`, each with no /ə/ after the first consonant. The same letter keeps its vowel inside a word: मज़ा gives `məzaː`. The precomposed and the decomposed nukta spellings give the same output.

Anusvara before a consonant is nasalisation of the vowel in the output, not a homorganic nasal.

## Gold rows

The `wikipron` row is `crowd-scraped` and can gate. The `vox_communis` row is `epitran-derived`, so it can neither qualify nor block a promotion. For the figures, see the [scoreboard](../evaluation/generated/scoreboard.md).

<!-- atlas:lects begin -->
## Related lects

These specs name `hi` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Urdu](ur.md) `ur`: Afghanistan, Bangladesh, India, Pakistan, research tier
- [Bhojpuri](bho.md) `bho`: India, Nepal, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-shapiro1989"></a>Shapiro, M. (1989). *Hindi*. in B. Comrie (ed.), The World's Major Languages.
2. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
3. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
4. <a id="src-ohala1983"></a>Ohala, M. (1983). *Aspects of Hindi Phonology*. Motilal Banarsidass, Delhi.
5. <a id="src-ohala1999"></a>Ohala, M. (1999). *Hindi*. in Handbook of the International Phonetic Association, Cambridge University Press. Cited: 100-103.
6. <a id="src-narasimhan2004"></a>Narasimhan, B., Sproat, R. & Kiraz, G. (2004). *Schwa-Deletion in Hindi Text-to-Speech Synthesis*. International Journal of Speech Technology 7(4). Cited: 319-333.
<!-- atlas:sources end -->

### Notes on the sources

The page also draws on two works that the spec does not cite:

- Pandey, P. (2014). Hindi. In: *Phonologies of Asia and Africa*. Eisenbrauns.
- Wikipedia: [Hindi phonology](https://en.wikipedia.org/wiki/Hindi_phonology)

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `hi` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 30375 | 0.1277 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `hi` | generated | epitran-derived | CC0 1.0 | 12478 | 0.2765 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 109 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ | q |  |
| Affricate |  |  |  | dʒ tʃ tʃʰ |  |  |  |  |  |
| Nasal | m |  | n n̪ |  | ɳ | ɲ | ŋ |  |  |
| Tap |  |  | ɾ |  | ɽ |  |  |  |  |
| Fricative |  | f v | s z | ʃ | ʂ |  | x ɣ |  | h ɦ |
| Approximant |  | ʋ |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː |  | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | eː |  | oː |
| Mid |  | ə |  |
| Open-mid | ɛː |  | ɔː |
| Near-open | æ æː |  |  |
| Open | aː |  |  |

Sequences that the spec writes as one unit: [bə] [bʱ] [bʱə] [dʒə] [dʒɲ] [dʒɲə] [dʒʱ] [dʒʱə] [d̪ə] [d̪ʱ] [d̪ʱə] [fə] [jə] [kə] [kʃ] [kʃə] [kʰə] [lə] [mə] [nə] [pə] [pʰə] [qə] [sə] [tʃə] [tʃʰə] [t̪ə] [t̪ɾ] [t̪ɾə] [t̪ʰə] [w] [xə] [zə] [ŋə] [ɖə] [ɖʱ] [ɖʱə] [ɡj] [ɡjə] [ɡə], and 20 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ँ⟩ | [̃] |  |
| ⟨ं⟩ | [̃] | before consonant [̃] · default [̃] · word final [̃] |
| ⟨ः⟩ | [h] |  |
| ⟨अ⟩ | [ə] | default [ə] · nucleus unstressed [ə] · word final ∅ |
| ⟨आ⟩ | [aː] |  |
| ⟨इ⟩ | [ɪ] |  |
| ⟨ई⟩ | [iː] |  |
| ⟨उ⟩ | [ʊ] |  |
| ⟨ऊ⟩ | [uː] |  |
| ⟨ऋ⟩ | [ɾɪ] |  |
| ⟨ए⟩ | [eː] |  |
| ⟨ऐ⟩ | [ɛː] |  |
| ⟨ओ⟩ | [oː] |  |
| ⟨औ⟩ | [ɔː] |  |
| ⟨क⟩ | [k] |  |
| ⟨क़⟩ | [q] |  |
| ⟨क्ष⟩ | [kʃ] |  |
| ⟨ख⟩ | [kʰ] |  |
| ⟨ख़⟩ | [x] |  |
| ⟨ग⟩ | [ɡ] |  |
| ⟨ग़⟩ | [ɣ] |  |
| ⟨घ⟩ | [ɡʱ] |  |
| ⟨ङ⟩ | [ŋ] |  |
| ⟨च⟩ | [tʃ] |  |
| ⟨छ⟩ | [tʃʰ] |  |
| ⟨ज⟩ | [dʒ] |  |
| ⟨ज़⟩ | [z] |  |
| ⟨ज्ञ⟩ | [ɡj] [dʒɲ] |  |
| ⟨झ⟩ | [dʒʱ] |  |
| ⟨ञ⟩ | [ɲ] |  |
| ⟨ट⟩ | [ʈ] |  |
| ⟨ठ⟩ | [ʈʰ] |  |
| ⟨ड⟩ | [ɖ] |  |
| ⟨ड़⟩ | [ɽ] |  |
| ⟨ढ⟩ | [ɖʱ] |  |
| ⟨ढ़⟩ | [ɽʱ] |  |
| ⟨ण⟩ | [ɳ] |  |
| ⟨त⟩ | [t̪] |  |
| ⟨त्र⟩ | [t̪ɾ] |  |
| ⟨थ⟩ | [t̪ʰ] |  |
| ⟨द⟩ | [d̪] |  |
| ⟨ध⟩ | [d̪ʱ] |  |
| ⟨न⟩ | [n] |  |
| ⟨प⟩ | [p] |  |
| ⟨फ⟩ | [pʰ] |  |
| ⟨फ़⟩ | [f] |  |
| ⟨ब⟩ | [b] |  |
| ⟨भ⟩ | [bʱ] |  |
| ⟨म⟩ | [m] |  |
| ⟨य⟩ | [j] |  |
| ⟨र⟩ | [ɾ] |  |
| ⟨ल⟩ | [l] |  |
| ⟨व⟩ | [ʋ] |  |
| ⟨श⟩ | [ʃ] |  |
| ⟨श्र⟩ | [ʃɾ] |  |
| ⟨ष⟩ | [ʂ] |  |
| ⟨स⟩ | [s] |  |
| ⟨ह⟩ | [ɦ] |  |
| ⟨ा⟩ | [aː] |  |
| ⟨ि⟩ | [ɪ] |  |
| ⟨ी⟩ | [iː] |  |
| ⟨ु⟩ | [ʊ] |  |
| ⟨ू⟩ | [uː] |  |
| ⟨ृ⟩ | [ɾɪ] |  |
| ⟨े⟩ | [eː] |  |
| ⟨ै⟩ | [ɛː] |  |
| ⟨ो⟩ | [oː] |  |
| ⟨ौ⟩ | [ɔː] |  |
| ⟨्⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 138 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `HI_SCHWA_FINAL_b` | /bə/ → [b], not word-initially, word-finally | ⟨शब्द⟩ [ʃəbd̪] | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_bʱ` | /bʱə/ → [bʱ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_dʒ` | /dʒə/ → [dʒ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_dʒɲ` | /dʒɲə/ → [dʒɲ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_dʒʱ` | /dʒʱə/ → [dʒʱ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_d̪` | /d̪ə/ → [d̪], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_f` | /fə/ → [f], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_j` | /jə/ → [j], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_k` | /kə/ → [k], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_kʃ` | /kʃə/ → [kʃ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_kʰ` | /kʰə/ → [kʰ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_l` | /lə/ → [l], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_m` | /mə/ → [m], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_n` | /nə/ → [n], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_p` | /pə/ → [p], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_pʰ` | /pʰə/ → [pʰ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_q` | /qə/ → [q], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_s` | /sə/ → [s], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_tʃ` | /tʃə/ → [tʃ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_tʃʰ` | /tʃʰə/ → [tʃʰ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_t̪` | /t̪ə/ → [t̪], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_t̪ɾ` | /t̪ɾə/ → [t̪ɾ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_x` | /xə/ → [x], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_z` | /zə/ → [z], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ŋ` | /ŋə/ → [ŋ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɖ` | /ɖə/ → [ɖ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɖʱ` | /ɖʱə/ → [ɖʱ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɡ` | /ɡə/ → [ɡ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɡj` | /ɡjə/ → [ɡj], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɡʱ` | /ɡʱə/ → [ɡʱ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɣ` | /ɣə/ → [ɣ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɦ` | /ɦə/ → [ɦ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɲ` | /ɲə/ → [ɲ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɳ` | /ɳə/ → [ɳ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɽ` | /ɽə/ → [ɽ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɽʱ` | /ɽʱə/ → [ɽʱ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɾ` | /ɾə/ → [ɾ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ɾɪ` | /ɾɪə/ → [ɾɪ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ʂ` | /ʂə/ → [ʂ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ʃ` | /ʃə/ → [ʃ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ʃɾ` | /ʃɾə/ → [ʃɾ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ʈ` | /ʈə/ → [ʈ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ʈʰ` | /ʈʰə/ → [ʈʰ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_FINAL_ʋ` | /ʋə/ → [ʋ], not word-initially, word-finally | - | [Ohala 1983](#src-ohala1983), [Ohala 1999](#src-ohala1999) |
| `HI_SCHWA_KEEP_b` | /bə/ → [bə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983), [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_KEEP_bʱ` | /bʱə/ → [bʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_dʒ` | /dʒə/ → [dʒə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_dʒɲ` | /dʒɲə/ → [dʒɲə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_dʒʱ` | /dʒʱə/ → [dʒʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_d̪` | /d̪ə/ → [d̪ə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_d̪ʱ` | /d̪ʱə/ → [d̪ʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_f` | /fə/ → [fə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_j` | /jə/ → [jə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_k` | /kə/ → [kə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_kʃ` | /kʃə/ → [kʃə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_kʰ` | /kʰə/ → [kʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_l` | /lə/ → [lə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_m` | /mə/ → [mə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_n` | /nə/ → [nə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_p` | /pə/ → [pə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_pʰ` | /pʰə/ → [pʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_q` | /qə/ → [qə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_s` | /sə/ → [sə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_tʃ` | /tʃə/ → [tʃə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_tʃʰ` | /tʃʰə/ → [tʃʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_t̪` | /t̪ə/ → [t̪ə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_t̪ɾ` | /t̪ɾə/ → [t̪ɾə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_t̪ʰ` | /t̪ʰə/ → [t̪ʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_x` | /xə/ → [xə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_z` | /zə/ → [zə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ŋ` | /ŋə/ → [ŋə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɖ` | /ɖə/ → [ɖə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɖʱ` | /ɖʱə/ → [ɖʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɡ` | /ɡə/ → [ɡə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɡj` | /ɡjə/ → [ɡjə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɡʱ` | /ɡʱə/ → [ɡʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɣ` | /ɣə/ → [ɣə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɦ` | /ɦə/ → [ɦə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɲ` | /ɲə/ → [ɲə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɳ` | /ɳə/ → [ɳə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɽ` | /ɽə/ → [ɽə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɽʱ` | /ɽʱə/ → [ɽʱə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɾ` | /ɾə/ → [ɾə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ɾɪ` | /ɾɪə/ → [ɾɪə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ʂ` | /ʂə/ → [ʂə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ʃ` | /ʃə/ → [ʃə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ʃɾ` | /ʃɾə/ → [ʃɾə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ʈ` | /ʈə/ → [ʈə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ʈʰ` | /ʈʰə/ → [ʈʰə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_KEEP_ʋ` | /ʋə/ → [ʋə], after [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983) |
| `HI_SCHWA_MEDIAL_b` | /bə/ → [b], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Ohala 1983](#src-ohala1983), [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_bʱ` | /bʱə/ → [bʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_dʒ` | /dʒə/ → [dʒ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_dʒɲ` | /dʒɲə/ → [dʒɲ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_dʒʱ` | /dʒʱə/ → [dʒʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_d̪` | /d̪ə/ → [d̪], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_d̪ʱ` | /d̪ʱə/ → [d̪ʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_f` | /fə/ → [f], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_j` | /jə/ → [j], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_k` | /kə/ → [k], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_kʃ` | /kʃə/ → [kʃ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_kʰ` | /kʰə/ → [kʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_l` | /lə/ → [l], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_m` | /mə/ → [m], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_n` | /nə/ → [n], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_p` | /pə/ → [p], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_pʰ` | /pʰə/ → [pʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_q` | /qə/ → [q], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_s` | /sə/ → [s], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_tʃ` | /tʃə/ → [tʃ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_tʃʰ` | /tʃʰə/ → [tʃʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_t̪` | /t̪ə/ → [t̪], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_t̪ɾ` | /t̪ɾə/ → [t̪ɾ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_t̪ʰ` | /t̪ʰə/ → [t̪ʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_x` | /xə/ → [x], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_z` | /zə/ → [z], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ŋ` | /ŋə/ → [ŋ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɖ` | /ɖə/ → [ɖ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɖʱ` | /ɖʱə/ → [ɖʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɡ` | /ɡə/ → [ɡ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɡj` | /ɡjə/ → [ɡj], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɡʱ` | /ɡʱə/ → [ɡʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɣ` | /ɣə/ → [ɣ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɦ` | /ɦə/ → [ɦ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɲ` | /ɲə/ → [ɲ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɳ` | /ɳə/ → [ɳ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɽ` | /ɽə/ → [ɽ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɽʱ` | /ɽʱə/ → [ɽʱ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɾ` | /ɾə/ → [ɾ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ɾɪ` | /ɾɪə/ → [ɾɪ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʂ` | /ʂə/ → [ʂ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʃ` | /ʃə/ → [ʃ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʃɾ` | /ʃɾə/ → [ʃɾ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʈ` | /ʈə/ → [ʈ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʈʰ` | /ʈʰə/ → [ʈʰ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
| `HI_SCHWA_MEDIAL_ʋ` | /ʋə/ → [ʋ], not word-initially, before [b] [bʱ] [dʒ] [dʒɲ] [dʒʱ] [d̪] [d̪ʱ] [f] and 38 more | - | [Narasimhan 2004](#src-narasimhan2004), Sproat & Kiraz 2004 |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="किताब|कमल|राम|काम|शब्द|करना|अपना|ज़मीन|दीवार|पड़ना|बढ़ना|क़िस्मत|फ़र्क|हाँ" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "hi")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| किताब | [kɪt̪aːb] |
| कमल | [kəməl] |
| राम | [ɾaːm] |
| काम | [kaːm] |
| शब्द | [ʃəbd̪] |
| करना | [kəɾnaː] |
| अपना | [əpnaː] |
| ज़मीन | [zmiːn] |
| दीवार | [d̪iːʋaːɾ] |
| पड़ना | [pəɽnaː] |
| बढ़ना | [bəɽʱnaː] |
| क़िस्मत | [qɪsmət̪] |
| फ़र्क | [fɾk] |
| हाँ | [ɦãː] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hill Mari](mrj.md) · [Home](../index.md) · [Hiri Motu →](ho.md)
