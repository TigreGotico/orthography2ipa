# Gun (Gungbe) (`guw`)

<!-- atlas:summary begin -->
Gun (Gungbe) is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Benin and Nigeria. The `guw` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `guw` |
| ISO 639-3 | [guw](https://iso639-3.sil.org/code/guw), Gun |
| Glottolog | [gunn1250](https://glottolog.org/resource/languoid/id/gunn1250), Gun |
| Wikidata | [Q3111668](https://www.wikidata.org/wiki/Q3111668) |
| Wikipedia | [Gun language](https://en.wikipedia.org/wiki/Gun_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Benin](by-region.md#benin), [Nigeria](by-region.md#nigeria) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1923, living |
| Parent | [Niger-Congo (family node)](https://tigregotico.github.io/orthography2ipa/#nic) `nic` |
| Explorer | [`guw` in the data explorer](https://tigregotico.github.io/orthography2ipa/#guw) |
| Spec file | [`guw.json`](../../orthography2ipa/data/guw.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Gun / Gungbe (Gbe, Benin and south-western Nigeria). Two Latin orthographies are in use for the same language and this spec describes both.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1975 to 2024. [Sources](#sources) lists them. The spec file writes all 57 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/guw.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `guw` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-capo1990"></a>Capo, Hounkpati B. C. (1990). *Towards a Viable Orthography for Egungbe*. African Languages and Cultures 3(2): 109-125. doi:10.1080/09544169008717715. [jstor.org](https://www.jstor.org/stable/1771717)
2. <a id="src-capo1991"></a>Capo, Hounkpati B. C. (1991). *A Comparative Phonology of Gbe*. Foris Publications / Labo Gbe (Int.).
3. <a id="src-aboh2004"></a>Aboh, Enoch O. (2004). *The Morphosyntax of Complement-Head Sequences: Clause Structure and Word Order Patterns in Kwa*. Oxford University Press.
4. <a id="src-benin_alphabet"></a>Commission Nationale de Linguistique (Benin) (1975). *Alphabet des langues nationales du Bénin*. République du Bénin.
5. <a id="src-wikipron_guw"></a>CUNY Computational Linguistics Lab (2024). *WikiPron: Gun (guw) Latin broad transcriptions*. CUNY-CL. [github.com](https://github.com/CUNY-CL/wikipron/blob/master/data/scrape/tsv/guw_latn_broad.tsv)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `guw` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 595 | 0.4311 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | ɖ |  | k kʷ ɡ |  |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |  |
| Nasal | m |  | n |  |  | ɲ ɲʷ |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  |  | x xʷ ɣ ɣʷ | ʁ χ χʷ | h hʷ |
| Approximant |  |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i ĩ | u ũ |
| Close-mid | e | o |
| Open-mid | ɛ ɛ̃ | ɔ ɔ̃ |
| Open | a ã |  |

Sequences that the spec writes as one unit: [k͡p] [w] [ɡ͡b] [ʷ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨d⟩ | [d] [ɖ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨h⟩ | [h] [x] [ɣ] |  |
| ⟨hw⟩ | [ɣʷ] [xʷ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kp⟩ | [k͡p] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨nyw⟩ | [ɲʷ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [k͡p] [p] |  |
| ⟨r⟩ | [ɾ] [l] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] | before vowel [ʷ] [u] · default [u] |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨wh⟩ | [ɣʷ] [xʷ] |  |
| ⟨x⟩ | [x] [χ] |  |
| ⟨xw⟩ | [xʷ] [χʷ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨à⟩ | [a] |  |
| ⟨á⟩ | [a] |  |
| ⟨è⟩ | [e] |  |
| ⟨é⟩ | [e] |  |
| ⟨ì⟩ | [i] |  |
| ⟨í⟩ | [i] |  |
| ⟨ò⟩ | [o] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ù⟩ | [u] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɔ̀⟩ | [ɔ] |  |
| ⟨ɔ́⟩ | [ɔ] |  |
| ⟨ɖ⟩ | [ɖ] |  |
| ⟨ɛ⟩ | [ɛ] |  |
| ⟨ɛ̀⟩ | [ɛ] |  |
| ⟨ɛ́⟩ | [ɛ] |  |
| ⟨ṣ⟩ | [ʃ] [tʃ] |  |
| ⟨ẹ⟩ | [ɛ] |  |
| ⟨ẹ̀⟩ | [ɛ] |  |
| ⟨ẹ́⟩ | [ɛ] |  |
| ⟨ọ⟩ | [ɔ] |  |
| ⟨ọ̀⟩ | [ɔ] |  |
| ⟨ọ́⟩ | [ɔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 12 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `GUW_NASAL_i` | /i/ → [ĩ], before a coda nasal | - | - |
| `GUW_NASAL_u` | /u/ → [ũ], before a coda nasal | - | - |
| `GUW_NASAL_a` | /a/ → [ã], before a coda nasal | - | - |
| `GUW_NASAL_ɛ` | /ɛ/ → [ɛ̃], before a coda nasal | - | - |
| `GUW_NASAL_ɔ` | /ɔ/ → [ɔ̃], before a coda nasal | - | - |
| `GUW_POSTNASAL_a` | /a/ → [ã], after [m] [n] [ɲ] | - | - |
| `GUW_POSTNASAL_ɛ` | /ɛ/ → [ɛ̃], after [m] [n] [ɲ] | - | - |
| `GUW_POSTNASAL_ɔ` | /ɔ/ → [ɔ̃], after [m] [n] [ɲ] | - | - |
| `GUW_POSTNASAL_i` | /i/ → [ĩ], after [m] [n] [ɲ] | - | - |
| `GUW_POSTNASAL_u` | /u/ → [ũ], after [m] [n] [ɲ] | - | - |
| `GUW_NASAL_j` | /j/ → [ɲ], before [i] [u] [a] [ɛ] [ɔ], with more context in the spec | - | [Capo 1991](#src-capo1991) |
| `GUW_NASAL_ABSORB` | /n m/ → ∅, in the coda, after [a] [ɛ] [ɔ] [i] [u] | ⟨ogongo⟩ [oɡonɡo] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "guw")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Gujarati](gu.md) · [Home](../index.md) · [Hadza →](hts.md)
