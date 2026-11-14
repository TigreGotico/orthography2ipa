# Lithuanian (`lt`)

<!-- atlas:summary begin -->
Lithuanian is an Eastern Baltic language, written in the Latin script. Glottolog places it in 5 countries. The `lt` spec is at the research tier. It cites 2 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lt` |
| ISO 639-3 | [lit](https://iso639-3.sil.org/code/lit), Lithuanian |
| Glottolog | [lith1251](https://glottolog.org/resource/languoid/id/lith1251), Lithuanian |
| Wikidata | [Q9083](https://www.wikidata.org/wiki/Q9083) |
| Wikipedia | [Lithuanian language](https://en.wikipedia.org/wiki/Lithuanian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Eastern Baltic](by-family.md#indo-european--balto-slavic--eastern-baltic) |
| Region | [Eurasia](by-region.md#eurasia) > [Belarus](by-region.md#belarus), [Latvia](by-region.md#latvia), [Lithuania](by-region.md#lithuania), [Poland](by-region.md#poland), [Russia](by-region.md#russia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1547, living |
| Parent | [Eastern Baltic](https://tigregotico.github.io/orthography2ipa/#x-clade-east2280) `x-clade-east2280` |
| Explorer | [`lt` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lt) |
| Spec file | [`lt.json`](../../orthography2ipa/data/lt.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lithuanian, the oldest attested Baltic language. Retains many archaic Indo-European features. Long vowels marked with macron/ogonek.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1997 to 2024. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lt.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lt` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-baksiene_et_al_2024"></a>Bakšienė, R., Čepaitienė, A., Jaroslavienė, J. & Urbanavičienė, J. (2024). *Standard Lithuanian*. Journal of the International Phonetic Association 54(1), 414-444. DOI [10.1017/S0025100323000105](https://doi.org/10.1017/S0025100323000105)
2. <a id="src-ambrazas1997"></a>Ambrazas, V. (ed.) (1997). *Lithuanian Grammar*. Vilnius: Baltos Lankos.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `lt` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 440 | 0.2640 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `lt` | generated | epitran-derived | CC0 1.0 | 28971 | 0.2706 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 53 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d dʲ t tʲ |  |  | k kʲ ɡ ɡʲ |
| Affricate |  |  | dz dzʲ ts tsʲ | dʒ dʒʲ tʃ tʃʲ |  |  |
| Nasal | m mʲ |  | n nʲ |  |  |  |
| Trill |  |  | r rʲ |  |  |  |
| Fricative |  | f fʲ v vʲ | s sʲ z zʲ | ʃ ʃʲ ʒ ʒʲ |  | x ɣ |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l lʲ |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | iː | uː |
| Near-close | ɪ | ʊ |
| Close-mid | eː | oː |
| Open-mid | ɛ ɛː |  |
| Open | a aː |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨dž⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [ɣ] [x] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨ia⟩ | [a] |  |
| ⟨io⟩ | [oː] |  |
| ⟨iu⟩ | [ʊ] |  |
| ⟨ią⟩ | [aː] |  |
| ⟨iū⟩ | [uː] |  |
| ⟨ių⟩ | [uː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨v⟩ | [v] |  |
| ⟨y⟩ | [iː] |  |
| ⟨z⟩ | [z] |  |
| ⟨ą⟩ | [aː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ė⟩ | [eː] |  |
| ⟨ę⟩ | [ɛː] |  |
| ⟨į⟩ | [iː] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ų⟩ | [uː] |  |
| ⟨ž⟩ | [ʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 20 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `LT_PALATAL_B` | /b/ → [bʲ], before a front vowel | - | [Bakšienė 2024](#src-baksiene_et_al_2024) |
| `LT_PALATAL_C` | /ts/ → [tsʲ], before a front vowel | - | - |
| `LT_PALATAL_CH` | /tʃ/ → [tʃʲ], before a front vowel | - | - |
| `LT_PALATAL_D` | /d/ → [dʲ], before a front vowel | - | - |
| `LT_PALATAL_DZ` | /dʒ/ → [dʒʲ], before a front vowel | - | - |
| `LT_PALATAL_DZ2` | /dz/ → [dzʲ], before a front vowel | - | - |
| `LT_PALATAL_F` | /f/ → [fʲ], before a front vowel | - | - |
| `LT_PALATAL_G` | /ɡ/ → [ɡʲ], before a front vowel | - | - |
| `LT_PALATAL_K` | /k/ → [kʲ], before a front vowel | - | - |
| `LT_PALATAL_L` | /l/ → [lʲ], before a front vowel | - | - |
| `LT_PALATAL_M` | /m/ → [mʲ], before a front vowel | - | - |
| `LT_PALATAL_N` | /n/ → [nʲ], before a front vowel | - | - |
| `LT_PALATAL_P` | /p/ → [pʲ], before a front vowel | - | - |
| `LT_PALATAL_R` | /r/ → [rʲ], before a front vowel | - | - |
| `LT_PALATAL_S` | /s/ → [sʲ], before a front vowel | - | - |
| `LT_PALATAL_SH` | /ʃ/ → [ʃʲ], before a front vowel | - | - |
| `LT_PALATAL_T` | /t/ → [tʲ], before a front vowel | - | - |
| `LT_PALATAL_V` | /v/ → [vʲ], before a front vowel | - | - |
| `LT_PALATAL_Z` | /z/ → [zʲ], before a front vowel | - | - |
| `LT_PALATAL_ZH` | /ʒ/ → [ʒʲ], before a front vowel | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lt")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lingua Franca Nova](lfn.md) · [Home](../index.md) · [Livonian →](liv.md)
