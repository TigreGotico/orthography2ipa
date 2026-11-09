# Slovenian (`sl`)

<!-- atlas:summary begin -->
Slovenian is a South Slavic language, written in the Latin script. Glottolog places it in 5 countries. The `sl` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sl` |
| ISO 639-3 | [slv](https://iso639-3.sil.org/code/slv), Slovenian |
| Glottolog | [slov1268](https://glottolog.org/resource/languoid/id/slov1268), Slovenian |
| Wikidata | [Q9063](https://www.wikidata.org/wiki/Q9063) |
| Wikipedia | [Slovenian language](https://en.wikipedia.org/wiki/Slovenian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > South Slavic](by-family.md#indo-european--balto-slavic--slavic--south-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Austria](by-region.md#austria), [Croatia](by-region.md#croatia), [Hungary](by-region.md#hungary), [Italy](by-region.md#italy), [Slovenia](by-region.md#slovenia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [South Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-sout3147) `x-clade-sout3147` |
| Explorer | [`sl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sl) |
| Spec file | [`sl.json`](../../orthography2ipa/data/sl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Slovenian. Unique among Slavic languages: retains a dual number in grammar. ⟨l⟩ → [w] in syllable coda (e.g. *delal* [dɛˈlaw]). ⟨v⟩ is variable [v ~ ʋ ~ w ~ f] depending on context. Standard language has phonemic pitch accent (tone), many dialects are toneless.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1993 to 1996. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-priestly1993"></a>Priestly, T.M.S. (1993). *Slovenian*. in B. Comrie & G. Corbett (eds.), The Slavonic Languages.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
4. <a id="src-sustarsic_komar_petek1995"></a>Šuštaršič, R., Komar, S. & Petek, B. (1995). *Slovene*. Journal of the International Phonetic Association 25(2), 86-90. [doi.org](https://doi.org/10.1017/S0025100300005211)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 5139 | 0.3166 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `sl` | generated | epitran-derived | CC0 1.0 | 6603 | 0.3451 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | ts | dʒ tʃ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x |
| Approximant |  | ʋ |  |  | j |  |
| Lateral approximant |  |  | l |  | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e eː |  | o oː |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w] [ər].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨dž⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] [e] [ə] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] [w] |  |
| ⟨lj⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nj⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] [ʋ] [w] |  |
| ⟨z⟩ | [z] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [eː] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [oː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 13 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `SL_SYLLABIC_R_BETWEEN_CONSONANTS` | /r/ → [ər], after a consonant, before a consonant, spelled ⟨r⟩ | ⟨rdeč⟩ [ərdéːtʃ] | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_SYLLABIC_R_INITIAL` | /r/ → [ər], after a word boundary, before a consonant, spelled ⟨r⟩ | ⟨rdeč⟩ [ərdéːtʃ] | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_SYLLABIC_R_FINAL` | /r/ → [ər], after a consonant, before a word boundary, spelled ⟨r⟩ | ⟨rdeč⟩ [ərdéːtʃ] | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_FINAL_DEVOICE_S` | /z/ → [s], word-finally | ⟨brez⟩ [bréːs] | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_FINAL_DEVOICE_T` | /d/ → [t], word-finally | - | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_FINAL_DEVOICE_P` | /b/ → [p], word-finally | - | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_FINAL_DEVOICE_Ʃ` | /ʒ/ → [ʃ], word-finally | - | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_FINAL_DEVOICE_K` | /ɡ/ → [k], word-finally | - | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_DEVOICE_BEFORE_VOICELESS_S` | /z/ → [s], before [p] [t] [k] [s] [ʃ] [x] [f] [ts] and 1 more | ⟨sladko⟩ [sláːtkɔ] | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_DEVOICE_BEFORE_VOICELESS_T` | /d/ → [t], before [p] [t] [k] [s] [ʃ] [x] [f] [ts] and 1 more | - | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_DEVOICE_BEFORE_VOICELESS_P` | /b/ → [p], before [p] [t] [k] [s] [ʃ] [x] [f] [ts] and 1 more | - | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_DEVOICE_BEFORE_VOICELESS_Ʃ` | /ʒ/ → [ʃ], before [p] [t] [k] [s] [ʃ] [x] [f] [ts] and 1 more | - | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
| `SL_DEVOICE_BEFORE_VOICELESS_K` | /ɡ/ → [k], before [p] [t] [k] [s] [ʃ] [x] [f] [ts] and 1 more | - | [Šuštaršič 1995](#src-sustarsic_komar_petek1995), Komar & Petek 1995 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Slovak](sk.md) · [Home](../index.md) · [Somali →](so.md)
