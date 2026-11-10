# Seychellois Creole (`crs`)

<!-- atlas:summary begin -->
Seychellois Creole is a Gallo-Romance language, written in the Latin script. Glottolog places it in Seychelles. The `crs` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `crs` |
| ISO 639-3 | [crs](https://iso639-3.sil.org/code/crs), Seselwa Creole French |
| Glottolog | [sese1246](https://glottolog.org/resource/languoid/id/sese1246), Seselwa Creole French |
| Wikidata | [Q34015](https://www.wikidata.org/wiki/Q34015) |
| Wikipedia | [Seychellois Creole](https://en.wikipedia.org/wiki/Seychellois_Creole) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Gallo-Romance](by-family.md#indo-european--italic--romance--gallo-romance) |
| Region | [Africa](by-region.md#africa) > [Seychelles](by-region.md#seychelles) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1770, living |
| Parent | [French](fr-FR.md) `fr-FR` |
| Explorer | [`crs` in the data explorer](https://tigregotico.github.io/orthography2ipa/#crs) |
| Spec file | [`crs.json`](../../orthography2ipa/data/crs.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Seychellois Creole (Kreol Seselwa), French-lexifier creole of the Seychelles, official alongside English and French since 1981 when the government's national orthography commission (following Bollée's proposals) standardised the current strictly phonemic spelling, later promoted by Lenstiti Kreol (Michaelis & Rosalie, APiCS ch. 56).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1977 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 28 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/crs.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `crs` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-michaelis_rosalie_apics56"></a>Michaelis, Susanne Maria & Rosalie, Marcel (2013). *Seychelles Creole structure dataset (survey chapter 56)*. In: Michaelis, S.M. et al. (eds.), The Atlas of Pidgin and Creole Language Structures (APiCS), Oxford University Press. [apics-online.info](https://apics-online.info/surveys/56)
2. <a id="src-bollee1977"></a>Bollée, Annegret (1977). *Le créole français des Seychelles: Esquisse d'une grammaire, textes, vocabulaire*. Niemeyer.
3. <a id="src-seychellois_creole_wiki"></a>Wikipedia contributors (2026). *Seychellois Creole*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Seychellois_Creole)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wold` ([lexibank/wold](https://github.com/lexibank/wold)) | `crs` | gold | lexicon-derived | CC BY 4.0 | 1874 | 0.2114 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | ɣ | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e ø | o |
| Open-mid | œ̃ ɛ ɛ̃ | ɔ ɔ̃ |
| Open | a ã | ɑ̃ |

Sequences that the spec writes as one unit: [jɛ] [jɛn] [w] [wɛ] [wɛn] [ɛm] [ɛn] [‿].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨ou⟩ | [u] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɣ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɛ⟩ | [ɛ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 28 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `FR_NASAL_BLOCK_PREVOCALIC_AIN` | /ɛ̃/ → [ɛn], before a vowel, spelled ⟨ain⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_BLOCK_GEMINATE_AIN` | /ɛ̃/ → [ɛ], spelled ⟨ain⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_BLOCK_PREVOCALIC_AIM` | /ɛ̃/ → [ɛm], before a vowel, spelled ⟨aim⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_BLOCK_GEMINATE_AIM` | /ɛ̃/ → [ɛ], spelled ⟨aim⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_BLOCK_PREVOCALIC_EIN` | /ɛ̃/ → [ɛn], before a vowel, spelled ⟨ein⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_BLOCK_GEMINATE_EIN` | /ɛ̃/ → [ɛ], spelled ⟨ein⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_BLOCK_PREVOCALIC_IEN` | /jɛ̃/ → [jɛn], before a vowel, spelled ⟨ien⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_BLOCK_GEMINATE_IEN` | /jɛ̃/ → [jɛ], spelled ⟨ien⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_BLOCK_PREVOCALIC_OIN` | /wɛ̃/ → [wɛn], before a vowel, spelled ⟨oin⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_BLOCK_GEMINATE_OIN` | /wɛ̃/ → [wɛ], spelled ⟨oin⟩, before ⟨n⟩ ⟨m⟩ ⟨nn⟩ ⟨mm⟩ | - | Tranel 1987, Walker 2001, Fouché 1959 |
| `FR_NASAL_a` | /a/ → [ɑ̃], before a coda nasal | - | - |
| `FR_NASAL_ə` | /ə/ → [ɑ̃], before a coda nasal | - | - |
| `FR_NASAL_i` | /i/ → [ɛ̃], before a coda nasal | - | - |
| `FR_NASAL_ɔ` | /ɔ/ → [ɔ̃], before a coda nasal | - | - |
| `FR_NASAL_y` | /y/ → [œ̃], before a coda nasal | - | - |
| `FR_NASAL_ABSORB` | /n m/ → ∅, in the coda, after a vowel | - | - |
| `FR_E_CLOSED_MULTIGRAPH` | /ə/ → [ɛ], before a consonant cluster, spelled ⟨e⟩ | ⟨Abel⟩ [abɛl] | Tranel 1987, Walker 2001 |
| `FR_O_FINAL_OPEN` | /ɔ/ → [o], word-finally, spelled ⟨o⟩ | ⟨mot⟩ [mo] | Tranel 1987 |
| `FR_O_BEFORE_Z` | /ɔ/ → [o], before [z], spelled ⟨o⟩ | ⟨mot⟩ [mo] | Tranel 1987 |
| `FR_AU_BEFORE_R` | /o/ → [ɔ], before [ʁ], spelled ⟨au⟩ | ⟨Laure⟩ [lɔʁ] | Fouché 1959, Tranel 1987, Walker 2001 |
| `FR_EU_BEFORE_Z` | /œ/ → [ø], before [z], spelled ⟨eu⟩ | ⟨Deleuze⟩ [dəløz] | Fouché 1959, Tranel 1987, Walker 2001 |
| `FR_C_HARD_BEFORE_OEU` | /s/ → [k], spelled ⟨c⟩, before ⟨œu⟩ | ⟨cœur⟩ [kœʁ] | - |
| `FR_AI_FINAL_CLOSE_MID` | /ɛ/ → [e], before a word boundary, spelled ⟨ai⟩ | ⟨j'ai⟩ [ʒe] | Walker 2001, Fouché 1959 |
| `FR_E_BEFORE_DOUBLED_CONSONANT` | /ə/ → [ɛ], spelled ⟨e⟩, before ⟨ll⟩ ⟨tt⟩ ⟨rr⟩ | ⟨elle⟩ [ɛl] | Féry 2001, Tranel 1987, New et al. 2004 |
| `CRS_NASAL_a` | /a/ → [ã], before a coda nasal | - | - |
| `CRS_NASAL_e` | /e/ → [ɛ̃], before a coda nasal | - | - |
| `CRS_NASAL_o` | /o/ → [ɔ̃], before a coda nasal | - | - |
| `CRS_NASAL_ABSORB` | /n m/ → ∅, in the coda, after a vowel | - | - |

The spec applies 6 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `FR_LIAISON_Z` | `z$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [z‿] | - | - |
| `FR_LIAISON_T` | `t$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [t‿] | - | - |
| `FR_LIAISON_N` | `n$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [n‿] | - | - |
| `FR_LIAISON_R` | `ʁ$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [ʁ‿] | - | - |
| `FR_LIAISON_P` | `p$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [p‿] | - | - |
| `FR_ENCHAÎNEMENT` | `([bdɡvzʒ])$` | `^[aeiouɛɔɑãɛ̃ɔ̃œ̃]` | left [‿] | - | - |

The spec switches off 2 inherited rules: `FR_E_CLOSED_CLUSTER`, `FR_E_CLOSED_FINAL`.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "crs")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Serer](srr.md) · [Home](../index.md) · [Shan →](shn.md)
