# Cypriot Maronite Arabic (`acy`)

<!-- atlas:summary begin -->
Cypriot Maronite Arabic is a Central Semitic language, written in the Latin script. Glottolog places it in Cyprus. The `acy` spec is at the research tier. It cites 5 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `acy` |
| ISO 639-3 | [acy](https://iso639-3.sil.org/code/acy), Cypriot Arabic |
| Glottolog | [cypr1248](https://glottolog.org/resource/languoid/id/cypr1248), Cypriot Arabic |
| Wikidata | [Q56416](https://www.wikidata.org/wiki/Q56416) |
| Wikipedia | [Cypriot Arabic](https://en.wikipedia.org/wiki/Cypriot_Arabic) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Eurasia](by-region.md#eurasia) > [Cyprus](by-region.md#cyprus) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Ancestor | [Classical Arabic](https://tigregotico.github.io/orthography2ipa/#arb) `arb` |
| Explorer | [`acy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#acy) |
| Spec file | [`acy.json`](../../orthography2ipa/data/acy.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cypriot Maronite Arabic (CMA), ISO 639-3: acy. Locally called 'Sanna' (our language) or 'Arabiya'. Critically endangered (UNESCO): ~1,000, 2,000 speakers (2020), mostly elderly. Maronite Christians migrated to Cyprus ~8th, 12th c. CE.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 5 works, from 1964 to 2004. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/acy.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `acy` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 0 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-borg1985"></a>Borg, A. (1985). *Cypriot Arabic: A Historical and Comparative Investigation into the Phonology and Morphology of the Arabic Vernacular Spoken by the Maronites of Kormakiti Village in the Kyrenia District of North-Western Cyprus*. Deutsche Morgenländische Gesellschaft / Franz Steiner, Stuttgart.
2. <a id="src-borg2004"></a>Borg, A. (2004). *A Comparative Glossary of Cypriot Maronite Arabic (Arabic-English)*. Brill (Handbook of Oriental Studies), Leiden.
3. <a id="src-watson2002"></a>Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press.
4. <a id="src-holes2004"></a>Holes, C. (2004). *Modern Arabic: Structures, Functions, and Varieties*. Georgetown University Press.
5. <a id="src-newton1964"></a>Newton, B.E. (1964). *Cypriot Greek: Its Phonology and Inflections*. Linguistics.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d dˤ t tˤ |  |  | k ɡ |  |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | ð θ | s sˤ z | ʃ |  | x ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Near-close | ɪ ɪː | ʊ ʊː |
| Close-mid | e eː | o oː |
| Open-mid | ɛː |  |
| Open | a aː | ɑ ɑː |

Sequences that the spec writes as one unit: [w] [ʔi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aː⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨dʒ⟩ | [dʒ] [tʃ] |  |
| ⟨dˤ⟩ | [dˤ] [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨iː⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oː⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sˤ⟩ | [sˤ] [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tˤ⟩ | [tˤ] [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uː⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨z⟩ | [z] |  |
| ⟨ð⟩ | [ð] |  |
| ⟨ɛː⟩ | [ɛː] |  |
| ⟨ɡ⟩ | [ɡ] |  |
| ⟨ɣ⟩ | [ɣ] |  |
| ⟨ʃ⟩ | [ʃ] |  |
| ⟨θ⟩ | [θ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 13 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AR_WASL_EPENTHESIS` | /ʔ/ → [ʔi], word-initially, before a consonant | ⟨اسْأَل⟩ [ʔisʔal] | Ryding 2005 |
| `AR_EMPHASIS_SPREAD_A_AFTER` | /a/ → [ɑ], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_A_BEFORE` | /a/ → [ɑ], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_AFTER` | /aː/ → [ɑː], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_BEFORE` | /aː/ → [ɑː], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_AFTER` | /i/ → [ɪ], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_BEFORE` | /i/ → [ɪ], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_AFTER` | /iː/ → [ɪː], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_BEFORE` | /iː/ → [ɪː], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_AFTER` | /u/ → [ʊ], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_BEFORE` | /u/ → [ʊ], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_AFTER` | /uː/ → [ʊː], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_BEFORE` | /uː/ → [ʊː], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |

The spec applies 1 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `AR_HAMZAT_WASL_ARTICLE` | `[aiueoɑæə]ː?$` | `^[aɑ](?=[^aeiouɑɐæɪʊəɛɔː])` | right ∅ | - | Ryding 2005 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "acy")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

| Repository | What it does with this spec |
|:--|:--|
| [arbtok](https://github.com/TigreGotico/arbtok) | Arabic text to IPA, with tashkeel restoration that knows the dialect. |
<!-- atlas:related end -->

---
[← Cypriot Greek](el-CY.md) · [Home](../index.md) · [Czech →](cs.md)
