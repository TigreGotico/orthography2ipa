# Kildin Sami (`sjd`)

<!-- atlas:summary begin -->
Kildin Sami is a Saami language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `sjd` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sjd` |
| ISO 639-3 | [sjd](https://iso639-3.sil.org/code/sjd), Kildin Sami |
| Wikipedia | [Kildin Sami language](https://en.wikipedia.org/wiki/Kildin_Sami_language) |
| Family | [Uralic](by-family.md#uralic) > [Saami](by-family.md#uralic--saami) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Saami](https://tigregotico.github.io/orthography2ipa/#x-clade-saam1281) `x-clade-saam1281` |
| Explorer | [`sjd` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sjd) |
| Spec file | [`sjd.json`](../../orthography2ipa/data/sjd.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Kildin Sami is a Kola (Eastern) Saami language of the Uralic family, written in an extended Cyrillic alphabet (Kert 1971 orthography, revised 1980s).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1971 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 56 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sjd.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sjd` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sjd_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Kildin Saami (kild1236)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/kild1236)
2. <a id="src-kert1971"></a>Kert, Georgij M. (1971). *Саамский язык (Кильдинский диалект): Фонетика, морфология, синтаксис (The Sami Language, Kildin Dialect: Phonetics, Morphology, Syntax)*. Nauka.
3. <a id="src-sjd_orthography"></a>Wikipedia contributors (2024). *Kildin Sami language, writing system and phonology*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kildin_Sami_language)
4. <a id="src-sjd_dobes"></a>Kola Saami Documentation Project (DoBeS) (2012). *Kola Sámi, Language: phonology*. Max Planck Institute for Psycholinguistics, Nijmegen. [dobes.mpi.nl](https://dobes.mpi.nl/projects/sami/language/)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `sjd` | gold | lexicon-derived | CC BY 4.0 | 1011 | 0.1368 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sjd` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 756 | 0.2298 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 50 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts | tʃ |  |  |  |
| Nasal | m m̥ |  | n n̥ |  | ɲ | ŋ |  |
| Trill |  |  | r r̥ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ç ɕ | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l l̥ |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ ɨː | u uː |
| Close-mid | e eː |  | o oː |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [ja] [jaː] [je] [jeː] [jo] [ju] [juː] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨а̄⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] |  |
| ⟨е̄⟩ | [jeː] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨о⟩ | [o] |  |
| ⟨о̄⟩ | [oː] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨сь⟩ | [ɕ] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨хь⟩ | [ç] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ы̄⟩ | [ɨː] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨э̄⟩ | [eː] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨ю̄⟩ | [juː] |  |
| ⟨я⟩ | [ja] |  |
| ⟨я̄⟩ | [jaː] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ҋ⟩ | [j] |  |
| ⟨ҍ⟩ | [ʲ] |  |
| ⟨ҏ⟩ | [r̥] |  |
| ⟨һ⟩ | [h] |  |
| ⟨ӆ⟩ | [l̥] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӊ⟩ | [n̥] |  |
| ⟨ӎ⟩ | [m̥] |  |
| ⟨ӓ⟩ | [a] |  |
| ⟨ӣ⟩ | [iː] |  |
| ⟨ӭ⟩ | [e] |  |
| ⟨ӯ⟩ | [uː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sjd")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kikuyu](ki.md) · [Home](../index.md) · [Kinyarwanda →](rw.md)
