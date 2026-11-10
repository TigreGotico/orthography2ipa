# Dungan (`dng`)

<!-- atlas:summary begin -->
Dungan is a Sinitic language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `dng` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `dng` |
| ISO 639-3 | [dng](https://iso639-3.sil.org/code/dng), Dungan |
| Wikipedia | [Dungan language](https://en.wikipedia.org/wiki/Dungan_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) > [Sinitic](by-family.md#sino-tibetan--sinitic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Sinitic](https://tigregotico.github.io/orthography2ipa/#x-clade-sini1245) `x-clade-sini1245` |
| Explorer | [`dng` in the data explorer](https://tigregotico.github.io/orthography2ipa/#dng) |
| Spec file | [`dng.json`](../../orthography2ipa/data/dng.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Dungan is a Sinitic (Sino-Tibetan) language, a Central Asian Mandarin variety of Gansu-Shaanxi type, written in a Cyrillic alphabet with the extra letters ә, ў, ү, ң and җ. The spec is built on the syllable model the orthography itself encodes: an initial, then a final spelled as a fixed letter sequence.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1979 to 2024. [Sources](#sources) lists them. The spec file writes all 56 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/dng.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `dng` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-dng_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Dungan (dung1253)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/dung1253)
2. <a id="src-dng_mair1990"></a>Mair, Victor H. (1990). *Implications of the Soviet Dungan Script for Chinese Language Reform (Two Non-Tetragraphic Northern Sinitic Languages)*. Sino-Platonic Papers 18, Department of East Asian Languages and Civilizations, University of Pennsylvania. Cited: A-10. [sino-platonic.org](https://sino-platonic.org/complete/spp018_dungan_gyami.pdf)
3. <a id="src-dng_salmi2007"></a>Salmi, Olli (2007). *Central Asian Dungan as a Chinese Dialect*. www.tsalo.fi. [tsalo.fi](https://www.tsalo.fi/dungan/Dungan%20as%20Chinese%20Dialect.html)
4. <a id="src-dng_zavjalova1979"></a>Zav'jalova, Olga I. (1979). *Dungan phonology*. Cited throughout Salmi 2007 (pp. 41, 43, 56, 57).
5. <a id="src-dng_lintao2012"></a>Lin, Tao (林涛) (2012). *东干语调查研究 [A survey study of the Dungan language]*. Beijing: 中国社会科学出版社. ISBN 978-7-5161-1418-6. Cited: 77-89 (ch. 3, 东干语的语音系统).
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `dng` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 269 | 0.4087 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | t tʰ |  |  | k kʰ |
| Affricate |  |  | ts tsʰ | ʈʂ ʈʂʰ | tɕ tɕʰ |  |
| Nasal | m |  | n |  |  | ŋ |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z̩ | ʂ ʐ ʐ̩ | ɕ | x |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y |  | u |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Near-open | æ̃ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ei] [ia] [iou] [iæ̃] [iŋ] [iɑŋ] [iɔ] [iə] [ou] [ua] [uei] [uæ̃] [uŋ] [uɑŋ] [uə] [uɛ] [yæ̃] [yŋ] [yə] [ɑŋ] [əŋ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨ан⟩ | [æ̃] |  |
| ⟨б⟩ | [p] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [k] |  |
| ⟨д⟩ | [t] |  |
| ⟨е⟩ | [iə] |  |
| ⟨ж⟩ | [ʐ] |  |
| ⟨з⟩ | [ts] |  |
| ⟨и⟩ | [i] |  |
| ⟨ин⟩ | [iŋ] |  |
| ⟨й⟩ | ∅ |  |
| ⟨к⟩ | [kʰ] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [ɔ] |  |
| ⟨он⟩ | [ɑŋ] |  |
| ⟨п⟩ | [pʰ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [tʰ] |  |
| ⟨у⟩ | [ou] |  |
| ⟨уа⟩ | [ua] |  |
| ⟨уан⟩ | [uæ̃] |  |
| ⟨уй⟩ | [uei] |  |
| ⟨ун⟩ | [uŋ] |  |
| ⟨уон⟩ | [uɑŋ] |  |
| ⟨уэ⟩ | [uɛ] |  |
| ⟨уэй⟩ | [uei] |  |
| ⟨уә⟩ | [uə] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [tsʰ] |  |
| ⟨ч⟩ | [ʈʂʰ] |  |
| ⟨ш⟩ | [ʂ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ʐ̩] |  |
| ⟨ый⟩ | [ei] |  |
| ⟨ын⟩ | [əŋ] |  |
| ⟨ь⟩ | ∅ |  |
| ⟨э⟩ | [ɛ] |  |
| ⟨ю⟩ | [iou] |  |
| ⟨я⟩ | [ia] |  |
| ⟨ян⟩ | [iæ̃] |  |
| ⟨ё⟩ | [iɔ] |  |
| ⟨ён⟩ | [iɑŋ] |  |
| ⟨ў⟩ | [u] |  |
| ⟨җ⟩ | [ʈʂ] |  |
| ⟨ң⟩ | [ŋ] |  |
| ⟨ү⟩ | [y] |  |
| ⟨үан⟩ | [yæ̃] |  |
| ⟨үн⟩ | [yŋ] |  |
| ⟨үә⟩ | [yə] |  |
| ⟨ә⟩ | [ə] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 4 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `dng_dzh_palatalisation` | /ʈʂ/ → [tɕ], before ⟨и⟩ ⟨ин⟩ ⟨е⟩ ⟨ё⟩ ⟨ён⟩ ⟨ю⟩ ⟨я⟩ ⟨ян⟩ and 4 more | - | [Salmi 2007](#src-dng_salmi2007) |
| `dng_ch_palatalisation` | /ʈʂʰ/ → [tɕʰ], before ⟨и⟩ ⟨ин⟩ ⟨е⟩ ⟨ё⟩ ⟨ён⟩ ⟨ю⟩ ⟨я⟩ ⟨ян⟩ and 4 more | - | [Salmi 2007](#src-dng_salmi2007) |
| `dng_apical_vowel_dental` | /ʐ̩/ → [z̩], after [ts] [tsʰ] [s] | - | [Salmi 2007](#src-dng_salmi2007) |
| `dng_zhy_syllabic` | /ʐ/ → ∅, before ⟨ы⟩ | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "dng")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Duala](dua.md) · [Home](../index.md) · [Dutch →](nl-NL.md)
