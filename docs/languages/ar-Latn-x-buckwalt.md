# Arabic (Buckwalter transliteration) (`ar-Latn-x-buckwalt`)

<!-- atlas:summary begin -->
Arabic (Buckwalter transliteration) is a Central Semitic variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `ar-Latn-x-buckwalt` spec is at the research tier. It cites 1 source and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ar-Latn-x-buckwalt` |
| Aliases | `ar-Latn-buckwalter` |
| Wikipedia | [Buckwalter transliteration](https://en.wikipedia.org/wiki/Buckwalter_transliteration) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Arabic](ar.md) `ar` |
| Explorer | [`ar-Latn-x-buckwalt` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ar-Latn-x-buckwalt) |
| Spec file | [`ar-Latn-x-buckwalt.json`](../../orthography2ipa/data/ar-Latn-x-buckwalt.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Buckwalter is NOT an orthography, it is a lossless 1:1 ASCII re-encoding of Arabic letters, devised so Arabic could be handled by ASCII-only tooling. Nobody reads Buckwalter as a language, it is a machine convenience, and it is recorded here as `orthography_kind: transliteration` to say so.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 1 work, from 2002. [Sources](#sources) lists them. The spec file writes all 60 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ar-Latn-x-buckwalt.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ar-Latn-x-buckwalt` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-buckwalter2002"></a>Buckwalter, Tim (2002). *Buckwalter Arabic Morphological Analyzer (LDC2002L49)*. Linguistic Data Consortium. [catalog.ldc.upenn.edu](https://catalog.ldc.upenn.edu/LDC2002L49)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 63 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b |  |  | d dˤ t tˤ |  |  | k | q |  | ʔ |
| Affricate |  |  |  |  | dʒ |  |  |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |  |  |
| Trill |  |  |  | r |  |  |  |  |  |  |
| Fricative |  | f | ð ðˤ θ | s sˤ z | ʃ |  | x ɣ |  | ħ ʕ | h |
| Lateral fricative |  |  |  | ɮˤ |  |  |  |  |  |  |
| Approximant |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l ɫ |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Near-close | ɪ ɪː | ʊ ʊː |
| Near-open | æ |  |
| Open | a aː | ɑ ɑː |

Sequences that the spec writes as one unit: [aj] [al] [an] [at] [aw] [ij] [in] [ja] [jaː] [ji] [un] [uw] [w] [wa] [waː] [wu] [ʔa] [ʔaː] [ʔi] [ː].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨$⟩ | [ʃ] |  |
| ⟨&⟩ | [ʔ] |  |
| ⟨'⟩ | [ʔ] |  |
| ⟨*⟩ | [ð] |  |
| ⟨<⟩ | [ʔi] | before vowel [ʔ] · default [ʔi] |
| ⟨>⟩ | [ʔa] | before vowel [ʔ] · default [ʔa] |
| ⟨A⟩ | [ʔ] [aː] | default [aː] [ʔ] · word initial [ʔ] [aː] |
| ⟨a⟩ | [a] |  |
| ⟨Aa⟩ | [aː] |  |
| ⟨aA⟩ | [aː] |  |
| ⟨Al⟩ | [al] [a] |  |
| ⟨aw⟩ | [aw] |  |
| ⟨aY⟩ | [aː] |  |
| ⟨ay⟩ | [aj] |  |
| ⟨b⟩ | [b] |  |
| ⟨D⟩ | [dˤ] |  |
| ⟨d⟩ | [d] |  |
| ⟨E⟩ | [ʕ] |  |
| ⟨F⟩ | [an] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨H⟩ | [ħ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨iy⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨K⟩ | [in] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨N⟩ | [un] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | ∅ |  |
| ⟨ow⟩ | [w] |  |
| ⟨oy⟩ | [j] |  |
| ⟨p⟩ | [a] [at] | after vowel ∅ · default [a] [at] |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨S⟩ | [sˤ] |  |
| ⟨s⟩ | [s] |  |
| ⟨T⟩ | [tˤ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uw⟩ | [uː] |  |
| ⟨v⟩ | [θ] |  |
| ⟨w⟩ | [w] [uː] | default [w] [uː] · word final [uː] [w] |
| ⟨wa⟩ | [wa] |  |
| ⟨waA⟩ | [waː] |  |
| ⟨wu⟩ | [wu] |  |
| ⟨x⟩ | [x] |  |
| ⟨Y⟩ | [aː] |  |
| ⟨y⟩ | [j] [iː] | default [j] [iː] · word final [iː] [j] |
| ⟨ya⟩ | [ja] |  |
| ⟨yaA⟩ | [jaː] |  |
| ⟨yi⟩ | [ji] |  |
| ⟨Z⟩ | [ðˤ] |  |
| ⟨z⟩ | [z] |  |
| ⟨|⟩ | [ʔaː] |  |
| ⟨}⟩ | [ʔ] |  |
| ⟨~⟩ | [ː] |  |

Stress falls on the antepenult by default. Stress is sensitive to syllable weight.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 21 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AR_WASL_EPENTHESIS` | /ʔ/ → [ʔi], word-initially, before a consonant | ⟨اسْأَل⟩ [ʔisʔal] | Ryding 2005 |
| `AR_EMPHASIS_SPREAD_A_AFTER` | /a/ → [ɑ], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_A_BEFORE` | /a/ → [ɑ], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_AFTER` | /aː/ → [ɑː], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_BEFORE` | /aː/ → [ɑː], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_AFTER` | /i/ → [ɪ], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_BEFORE` | /i/ → [ɪ], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_AFTER` | /iː/ → [ɪː], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_BEFORE` | /iː/ → [ɪː], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_AFTER` | /u/ → [ʊ], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_BEFORE` | /u/ → [ʊ], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_AFTER` | /uː/ → [ʊː], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_BEFORE` | /uː/ → [ʊː], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPH_BACK_A_AFTER` | /a/ → [ɑ], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_EMPH_BACK_A_BEFORE` | /a/ → [ɑ], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_EMPH_BACK_AA_AFTER` | /aː/ → [ɑː], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_EMPH_BACK_AA_BEFORE` | /aː/ → [ɑː], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_GLIDE_YA_BEFORE_GEMINATE` | /iː/ → [ij], before [iː] | ⟨مِصْرِيّ⟩ [misˤrijj] | Ryding 2005 |
| `AR_GLIDE_YA_GEMINATE_COPY` | /iː/ → [j], after [iː] | ⟨ends⟩ [ijj] | Ryding 2005 |
| `AR_GLIDE_YA_CONSONANTAL` | /iː/ → [ij], before [j] [ja] [ji] [ju] [jaː] [jiː] [juː] | ⟨ـِيّ⟩ [-ijj] | Watson 2002, Ryding 2005 |
| `AR_GLIDE_WAW_CONSONANTAL` | /uː/ → [uw], before [w] [wa] [wi] [wu] [waː] [wiː] [wuː] | ⟨أُبُوَّة⟩ [ʔubuwwa] | - |

The spec applies 1 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `AR_HAMZAT_WASL_ARTICLE` | `[aiueoɑæə]ː?$` | `^[aɑ](?=[^aeiouɑɐæɪʊəɛɔː])` | right ∅ | - | Ryding 2005 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ar-Latn-x-buckwalt")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

| Repository | What it does with this spec |
|:--|:--|
| [arbtok](https://github.com/TigreGotico/arbtok) | Arabic text to IPA, with tashkeel restoration that knows the dialect. |
<!-- atlas:related end -->

---
[← Arabic](ar.md) · [Home](../index.md) · [Aragonese →](an.md)
