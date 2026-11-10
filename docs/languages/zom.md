# Zou (`zom`)

<!-- atlas:summary begin -->
Zou is a Sino-Tibetan language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `zom` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `zom` |
| ISO 639-3 | [zom](https://iso639-3.sil.org/code/zom), Zou |
| Wikipedia | [Zou language](https://en.wikipedia.org/wiki/Zou_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Ancestor | [Proto-Kuki-Chin (reconstructed)](https://tigregotico.github.io/orthography2ipa/#mni-x-proto-kuki-chin) `mni-x-proto-kuki-chin` |
| Explorer | [`zom` in the data explorer](https://tigregotico.github.io/orthography2ipa/#zom) |
| Spec file | [`zom.json`](../../orthography2ipa/data/zom.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Zou (Zomi) is a Kuki-Chin (Sino-Tibetan) language of Manipur and Chin State, written in a Latin script developed by J.H. Cope. Base Latin consonants and vowels are mapped, with ng/kh/ph/th the expected digraphs and aspirates.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2012 to 2024. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/zom.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `zom` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-zom_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Zou (zouu1235)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/zouu1235)
2. <a id="src-zom_tungdim2012"></a>Tungdim, Philip Thangliènmâng (2012). *A Descriptive Grammar of the Zo Language*. PhD dissertation, Jawaharlal Nehru University.
3. <a id="src-zom_singh_himmat2013"></a>Singh, Yashawanta and Himmat, Lukram (2013). *Zou Phonology*. Language in India. Cited: 683-701. [languageinindia.com](http://www.languageinindia.com/feb2013/zouphonologyfinal.pdf)
4. <a id="src-zom_mortensen2023"></a>Mortensen, David R. (2023). *Kuki-Chin Phonology: An Overview*. Himalayan Linguistics 22(1): 5-35. Cited: 5-35. [escholarship.org](https://escholarship.org/uc/item/1d326124)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `zom` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 134 | 0.4399 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 39 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ | ʔ |
| Affricate |  |  | ts | dʒ t͡ʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid |  | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [w] [ʔa] [ʔe] [ʔi] [ʔo] [ʔu] [ʔɔ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | word initial [ʔa] |
| ⟨aw⟩ | [ɔ] | word initial [ʔɔ] |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [t͡ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] | word initial [ʔe] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] | before consonant [ʔ] · word final [ʔ] |
| ⟨i⟩ | [i] | word initial [ʔi] |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] | word initial [ʔo] |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [u] | word initial [ʔu] |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "zom")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Zhuang](za.md) · [Home](../index.md) · [Zulu →](zu.md)
