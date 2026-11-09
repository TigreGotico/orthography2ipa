# Northern Tiwa (`twf`)

<!-- atlas:summary begin -->
Northern Tiwa is a Kiowa-Tanoan language, written in the Latin script. Glottolog places it in the North America macroarea. The `twf` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `twf` |
| ISO 639-3 | [twf](https://iso639-3.sil.org/code/twf), Northern Tiwa |
| Wikipedia | [Taos language](https://en.wikipedia.org/wiki/Taos_language) |
| Family | [Kiowa-Tanoan](by-family.md#kiowa-tanoan) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Kiowa-Tanoan](https://tigregotico.github.io/orthography2ipa/#x-clade-kiow1265) `x-clade-kiow1265` |
| Explorer | [`twf` in the data explorer](https://tigregotico.github.io/orthography2ipa/#twf) |
| Spec file | [`twf.json`](../../orthography2ipa/data/twf.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kiowa-Tanoan (Northern Tiwa) language of Taos Pueblo, New Mexico, written in the practical orthography of Trager (1948).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1946 to 2024. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 118 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/twf.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `twf` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-twf_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Taos Northern Tiwa (nort1550)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/nort1550)
2. <a id="src-twf_wikipedia_language"></a>Wikipedia contributors (2024). *Taos language, section 'Transcription'*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Taos_language)
3. <a id="src-twf_wikipedia_phonology"></a>Wikipedia contributors (2024). *Taos phonology*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Taos_phonology)
4. <a id="src-twf_trager1946"></a>Trager, George L. (1946). *An outline of Taos grammar*. In C. Osgood (Ed.), Linguistic structures of native America, pp. 184-221. New York: Wenner-Gren Foundation for Anthropological Research. Cited: 184-221.
5. <a id="src-twf_trager1948"></a>Trager, George L. (1948). *Taos I: A language revisited*. International Journal of American Linguistics, 14 (3). Cited: 155-160.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `twf` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 135 | 0.0240 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 123 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  |  | k ɡ | ʔ |
| Affricate |  |  | tʃ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Tap |  | ɾ |  |  |  |  |
| Fricative |  | s |  |  | x | h |
| Lateral fricative |  | ɬ |  |  |  |  |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i ì í ĩ ĩ̀ ĩ́ ĩ̄ ī | u ù ú ũ ũ̀ ũ̄ ū ṹ |
| Close-mid | e è é ē ẽ ẽ̀ ẽ́ ẽ̄ | ɤ ɤ̀ ɤ́ ɤ̄ |
| Near-open | æ æ̀ æ̃ æ̃̀ æ̃́ æ̃̄ ǣ ǽ |  |
| Open |  | ɑ ɑ̀ ɑ́ ɑ̃ ɑ̃̀ ɑ̃́ ɑ̃̄ ɑ̄ |

Sequences that the spec writes as one unit: [fɾ] [kʔ] [ph] [pʔ] [th] [tʃʔ] [tʔ] [w] [ĩ̄ẽ̄] [īē] [īǣ] [ūɑ̄] [ɤ̄ɑ̄] [ʔe] [ʔi] [ʔu] [ʔæ] [ʔæ̀] [ʔæ̃] [ʔæ̃̀] [ʔæ̃́] [ʔæ̃̄] [ʔè] [ʔé] [ʔì] [ʔí] [ʔù] [ʔú] [ʔē] [ʔĩ] [ʔĩ̀] [ʔĩ́] [ʔĩ̄] [ʔĩ̄ẽ̄] [ʔī] [ʔīē] [ʔīǣ] [ʔũ] [ʔũ̀] [ʔũ̄], and 22 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [æ] | word initial [ʔæ] |
| ⟨a̋⟩ | [ǽ] | word initial [ʔǽ] |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨c'⟩ | [tʃʔ] |  |
| ⟨cʼ⟩ | [tʃʔ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] | word initial [ʔe] |
| ⟨e̋⟩ | [é] | word initial [ʔé] |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] | word initial [ʔi] |
| ⟨i̋⟩ | [í] | word initial [ʔí] |
| ⟨k⟩ | [k] |  |
| ⟨k'⟩ | [kʔ] |  |
| ⟨kʼ⟩ | [kʔ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ɑ] | word initial [ʔɑ] |
| ⟨p⟩ | [p] |  |
| ⟨p'⟩ | [pʔ] |  |
| ⟨ph⟩ | [ph] |  |
| ⟨phr⟩ | [fɾ] |  |
| ⟨pʼ⟩ | [pʔ] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨t'⟩ | [tʔ] |  |
| ⟨th⟩ | [th] |  |
| ⟨tʼ⟩ | [tʔ] |  |
| ⟨u⟩ | [u] | word initial [ʔu] |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨à⟩ | [ǣ] | word initial [ʔǣ] |
| ⟨á⟩ | [ǣ] | word initial [ʔǣ] |
| ⟨â⟩ | [æ̀] | word initial [ʔæ̀] |
| ⟨è⟩ | [ē] | word initial [ʔē] |
| ⟨é⟩ | [ē] | word initial [ʔē] |
| ⟨ê⟩ | [è] | word initial [ʔè] |
| ⟨ì⟩ | [ī] | word initial [ʔī] |
| ⟨ìa⟩ | [īǣ] | word initial [ʔīǣ] |
| ⟨ìe⟩ | [īē] | word initial [ʔīē] |
| ⟨í⟩ | [ī] | word initial [ʔī] |
| ⟨ía⟩ | [īǣ] | word initial [ʔīǣ] |
| ⟨íe⟩ | [īē] | word initial [ʔīē] |
| ⟨î⟩ | [ì] | word initial [ʔì] |
| ⟨ò⟩ | [ɑ̄] | word initial [ʔɑ̄] |
| ⟨ó⟩ | [ɑ̄] | word initial [ʔɑ̄] |
| ⟨ô⟩ | [ɑ̀] | word initial [ʔɑ̀] |
| ⟨ù⟩ | [ū] | word initial [ʔū] |
| ⟨ùo⟩ | [ūɑ̄] | word initial [ʔūɑ̄] |
| ⟨ú⟩ | [ū] | word initial [ʔū] |
| ⟨úo⟩ | [ūɑ̄] | word initial [ʔūɑ̄] |
| ⟨û⟩ | [ù] | word initial [ʔù] |
| ⟨ą⟩ | [æ̃] | word initial [ʔæ̃] |
| ⟨ą̀⟩ | [æ̃̄] | word initial [ʔæ̃̄] |
| ⟨ą́⟩ | [æ̃̄] | word initial [ʔæ̃̄] |
| ⟨ą̂⟩ | [æ̃̀] | word initial [ʔæ̃̀] |
| ⟨ą̋⟩ | [æ̃́] | word initial [ʔæ̃́] |
| ⟨ą̌⟩ | [æ̃́] | word initial [ʔæ̃́] |
| ⟨ą̏⟩ | [æ̃̀] | word initial [ʔæ̃̀] |
| ⟨ę⟩ | [ẽ] | word initial [ʔẽ] |
| ⟨ę̀⟩ | [ẽ̄] | word initial [ʔẽ̄] |
| ⟨ę́⟩ | [ẽ̄] | word initial [ʔẽ̄] |
| ⟨ę̂⟩ | [ẽ̀] | word initial [ʔẽ̀] |
| ⟨ę̋⟩ | [ẽ́] | word initial [ʔẽ́] |
| ⟨ę̌⟩ | [ẽ́] | word initial [ʔẽ́] |
| ⟨ę̏⟩ | [ẽ̀] | word initial [ʔẽ̀] |
| ⟨ě⟩ | [é] | word initial [ʔé] |
| ⟨į⟩ | [ĩ] | word initial [ʔĩ] |
| ⟨į̀⟩ | [ĩ̄] | word initial [ʔĩ̄] |
| ⟨į̀ę⟩ | [ĩ̄ẽ̄] | word initial [ʔĩ̄ẽ̄] |
| ⟨į́⟩ | [ĩ̄] | word initial [ʔĩ̄] |
| ⟨į́ę⟩ | [ĩ̄ẽ̄] | word initial [ʔĩ̄ẽ̄] |
| ⟨į̂⟩ | [ĩ̀] | word initial [ʔĩ̀] |
| ⟨į̋⟩ | [ĩ́] | word initial [ʔĩ́] |
| ⟨į̌⟩ | [ĩ́] | word initial [ʔĩ́] |
| ⟨į̏⟩ | [ĩ̀] | word initial [ʔĩ̀] |
| ⟨ł⟩ | [ɬ] |  |
| ⟨ő⟩ | [ɑ́] | word initial [ʔɑ́] |
| ⟨ű⟩ | [ú] | word initial [ʔú] |
| ⟨ų⟩ | [ũ] | word initial [ʔũ] |
| ⟨ų̀⟩ | [ũ̄] | word initial [ʔũ̄] |
| ⟨ų́⟩ | [ũ̄] | word initial [ʔũ̄] |
| ⟨ų̂⟩ | [ũ̀] | word initial [ʔũ̀] |
| ⟨ų̋⟩ | [ṹ] | word initial [ʔṹ] |
| ⟨ų̌⟩ | [ṹ] | word initial [ʔṹ] |
| ⟨ų̏⟩ | [ũ̀] | word initial [ʔũ̀] |
| ⟨ǎ⟩ | [ǽ] | word initial [ʔǽ] |
| ⟨ǐ⟩ | [í] | word initial [ʔí] |
| ⟨ǒ⟩ | [ɑ́] | word initial [ʔɑ́] |
| ⟨ǔ⟩ | [ú] | word initial [ʔú] |
| ⟨ǫ⟩ | [ɑ̃] | word initial [ʔɑ̃] |
| ⟨ǫ̀⟩ | [ɑ̃̄] | word initial [ʔɑ̃̄] |
| ⟨ǫ́⟩ | [ɑ̃̄] | word initial [ʔɑ̃̄] |
| ⟨ǫ̂⟩ | [ɑ̃̀] | word initial [ʔɑ̃̀] |
| ⟨ǫ̋⟩ | [ɑ̃́] | word initial [ʔɑ̃́] |
| ⟨ǫ̌⟩ | [ɑ̃́] | word initial [ʔɑ̃́] |
| ⟨ǫ̏⟩ | [ɑ̃̀] | word initial [ʔɑ̃̀] |
| ⟨ȁ⟩ | [æ̀] | word initial [ʔæ̀] |
| ⟨ȅ⟩ | [è] | word initial [ʔè] |
| ⟨ȉ⟩ | [ì] | word initial [ʔì] |
| ⟨ȍ⟩ | [ɑ̀] | word initial [ʔɑ̀] |
| ⟨ȕ⟩ | [ù] | word initial [ʔù] |
| ⟨ə⟩ | [ɤ] | word initial [ʔɤ] |
| ⟨ə̀⟩ | [ɤ̄] | word initial [ʔɤ̄] |
| ⟨ə̀o⟩ | [ɤ̄ɑ̄] | word initial [ʔɤ̄ɑ̄] |
| ⟨ə́⟩ | [ɤ̄] | word initial [ʔɤ̄] |
| ⟨ə́o⟩ | [ɤ̄ɑ̄] | word initial [ʔɤ̄ɑ̄] |
| ⟨ə̂⟩ | [ɤ̀] | word initial [ʔɤ̀] |
| ⟨ə̋⟩ | [ɤ́] | word initial [ʔɤ́] |
| ⟨ə̌⟩ | [ɤ́] | word initial [ʔɤ́] |
| ⟨ə̏⟩ | [ɤ̀] | word initial [ʔɤ̀] |
| ⟨ʼ⟩ | [ʔ] |  |
| ⟨’⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "twf")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Northern Sotho](nso.md) · [Home](../index.md) · [Northern Yukaghir →](ykg.md)
