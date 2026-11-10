# Bahnar (`bdq`)

<!-- atlas:summary begin -->
Bahnar is an Austroasiatic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `bdq` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bdq` |
| ISO 639-3 | [bdq](https://iso639-3.sil.org/code/bdq), Bahnar |
| Wikipedia | [Bahnar language](https://en.wikipedia.org/wiki/Bahnar_language) |
| Family | [Austroasiatic](by-family.md#austroasiatic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Austroasiatic](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1305) `x-clade-aust1305` |
| Explorer | [`bdq` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bdq) |
| Spec file | [`bdq.json`](../../orthography2ipa/data/bdq.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Austroasiatic (Bahnaric) language of the Vietnamese Central Highlands, written in a Vietnamese-modeled Latin missionary orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1979 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 44 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bdq.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `bdq` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-bdq_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Bahnar (bahn1262)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/bahn1262)
2. <a id="src-bdq_wikipedia"></a>Wikipedia contributors (2024). *Bahnar language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Bahnar_language)
3. <a id="src-banker_banker1979"></a>Banker, John E., Banker, Elizabeth M. (1979). *Bahnar Dictionary (Bahnar-Vietnamese-English)*. Summer Institute of Linguistics, Vietnam Data Microfiche Series.
4. <a id="src-bdq_omniglot"></a>Ager, S. (2024). *Bahnar language and alphabet*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/bahnar.htm)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `bdq` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 198 | 0.3355 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 32 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ | d t tʰ |  | k kʰ ɡ | ʔ |
| Affricate |  |  | dʑ tɕ |  |  |
| Nasal | m | n | ɲ | ŋ |  |
| Trill |  | r |  |  |  |
| Fricative |  | s |  |  | h |
| Approximant |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w] [ɓ] [ɗ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [ɓ] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [tɕ] |  |
| ⟨d⟩ | [ɗ] |  |
| ⟨dj⟩ | [dʑ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʑ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngh⟩ | [ŋ] |  |
| ⟨nh⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [w] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [s] |  |
| ⟨y⟩ | [j] |  |
| ⟨â⟩ | [ə] |  |
| ⟨ê⟩ | [e] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ô⟩ | [o] |  |
| ⟨ă⟩ | [a] |  |
| ⟨đ⟩ | [d] |  |
| ⟨ơ⟩ | [ə] |  |
| ⟨ư⟩ | [ɨ] |  |
| ⟨ʼ⟩ | [ʔ] |  |
| ⟨’⟩ | [ʔ] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bdq")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Azerbaijani](az.md) · [Home](../index.md) · [Bahraini Arabic →](afb-BH.md)
