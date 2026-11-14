# Tewa (USA) (`tew`)

<!-- atlas:summary begin -->
Tewa (USA) is a Kiowa-Tanoan language, written in the Latin script. Glottolog places it in the North America macroarea. The `tew` spec is at the research tier. It cites 7 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tew` |
| ISO 639-3 | [tew](https://iso639-3.sil.org/code/tew), Tewa (USA) |
| Wikipedia | [Tewa language](https://en.wikipedia.org/wiki/Tewa_language) |
| Family | [Kiowa-Tanoan](by-family.md#kiowa-tanoan) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Kiowa-Tanoan](https://tigregotico.github.io/orthography2ipa/#x-clade-kiow1265) `x-clade-kiow1265` |
| Explorer | [`tew` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tew) |
| Spec file | [`tew.json`](../../orthography2ipa/data/tew.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Rio Grande Tewa (Kiowa-Tanoan) in the practical orthography of the San Juan Pueblo Téwa Dictionary (Martinez 1982), the spelling this community's own literacy materials use. IPA correspondences follow Sutton (2014). INPUT CONTRACT: Martinez-orthography Tewa.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 7 works, from 1966 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 115 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tew.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tew` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 7 works. 5 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-tew_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Rio Grande Tewa (tewa1260)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/tewa1260)
2. <a id="src-tew_orthography"></a>Wikipedia contributors (2024). *Tewa language, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Tewa_language)
3. <a id="src-tew_martinez1982"></a>Martinez, Esther (Pʼoe Tsáwä̃) (1982). *San Juan Pueblo Téwa Dictionary*. San Juan Pueblo Bilingual Program, San Juan Pueblo, NM.
4. <a id="src-tew_sutton2014"></a>Sutton, Logan Dean (2014). *Kiowa-Tanoan: A Synchronic and Diachronic Study*. PhD dissertation, University of New Mexico. [digitalrepository.unm.edu](https://digitalrepository.unm.edu/ling_etds/34/)
5. <a id="src-tew_speirs1966"></a>Speirs, Randall Hannaford (1966). *Some aspects of the structure of Rio Grande Tewa*. PhD dissertation, State University of New York at Buffalo. [sil.org](https://www.sil.org/resources/archives/9702)
6. <a id="src-tew_kroskrity1993"></a>Kroskrity, Paul V. (1993). *Language, History, and Identity: Ethnolinguistic Studies of the Arizona Tewa*. University of Arizona Press.
7. <a id="src-tew_wiktionary_module"></a>Wiktionary contributors (2025). *Module:tew-IPA (English Wiktionary)*. Wikimedia Foundation. [en.wiktionary.org](https://en.wiktionary.org/wiki/Module:tew-IPA)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `tew` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 106 | 0.0000 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 185 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  |  | d t tʼ |  |  | k kʷ kʷʼ kʼ ɡ | ʔ |
| Affricate |  |  |  | t͡s t͡sʼ | d͡ʒ t͡ʃ t͡ʃʼ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | θ | s | ʃ |  | x xʷ ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | ì ìː í íː î îː ĩ̀ ĩ̀ː ĩ́ ĩ́ː ĩ̂ ĩ̂ː | ù ùː ú úː û ûː ũ̀ ũ̀ː ũ̂ ũ̂ː ṹ ṹː |
| Close-mid | è èː é éː ê êː ẽ̀ ẽ̀ː ẽ́ ẽ́ː ẽ̂ ẽ̂ː | ò òː ó óː ô ôː õ̀ õ̀ː õ̂ õ̂ː ṍ ṍː |
| Near-open | æ̀ æ̀ː æ̂ æ̂ː æ̃̀ æ̃̀ː æ̃́ æ̃́ː æ̃̂ æ̃̂ː ǽ ǽː |  |
| Open |  | ɑ̀ ɑ̀ː ɑ́ ɑ́ː ɑ̂ ɑ̂ː ɑ̃̀ ɑ̃̀ː ɑ̃́ ɑ̃́ː ɑ̃̂ ɑ̃̂ː |

Sequences that the spec writes as one unit: [w] [ŋɡ] [ɑ̀j] [ɑ́j] [ɑ̂j] [ɑ̃̀j] [ɑ̃́j] [ɑ̃̂j] [ʔæ̀] [ʔæ̀ː] [ʔæ̂] [ʔæ̂ː] [ʔæ̃̀] [ʔæ̃̀ː] [ʔæ̃́] [ʔæ̃́ː] [ʔæ̃̂] [ʔæ̃̂ː] [ʔè] [ʔèː] [ʔé] [ʔéː] [ʔê] [ʔêː] [ʔì] [ʔìː] [ʔí] [ʔíː] [ʔî] [ʔîː] [ʔò] [ʔòː] [ʔó] [ʔóː] [ʔô] [ʔôː] [ʔõ̀] [ʔõ̀ː] [ʔõ̂] [ʔõ̂ː], and 40 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ̀] | word initial [ʔɑ̀] |
| ⟨aa⟩ | [ɑ̀ː] | word initial [ʔɑ̀ː] |
| ⟨ay⟩ | [èː] | before vowel [ɑ̀j] · word initial [ʔèː] |
| ⟨a̧⟩ | [ɑ̃̀] | word initial [ʔɑ̃̀] |
| ⟨a̧a⟩ | [ɑ̃̀ː] | word initial [ʔɑ̃̀ː] |
| ⟨a̧y⟩ | [ẽ̀ː] | before vowel [ɑ̃̀j] · word initial [ʔẽ̀ː] |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [t͡s] |  |
| ⟨ch⟩ | [t͡ʃ] |  |
| ⟨chʼ⟩ | [t͡ʃʼ] |  |
| ⟨cʼ⟩ | [t͡sʼ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [è] | word initial [ʔè] |
| ⟨ee⟩ | [ìː] | word initial [ʔìː] |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ì] | word initial [ʔì] |
| ⟨i̧⟩ | [ĩ̀] | word initial [ʔĩ̀] |
| ⟨j⟩ | [d͡ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [x] |  |
| ⟨khw⟩ | [xʷ] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨kwʼ⟩ | [kʷʼ] |  |
| ⟨kʼ⟩ | [kʼ] |  |
| ⟨kʼw⟩ | [kʷʼ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨o⟩ | [ò] | word initial [ʔò] |
| ⟨oe⟩ | [òː] | word initial [ʔòː] |
| ⟨o̧⟩ | [õ̀] | word initial [ʔõ̀] |
| ⟨o̧e⟩ | [õ̀ː] | word initial [ʔõ̀ː] |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨pʼ⟩ | [pʼ] |  |
| ⟨qw⟩ | [xʷ] |  |
| ⟨r⟩ | [d] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [θ] |  |
| ⟨ts⟩ | [t͡s] |  |
| ⟨tsʼ⟩ | [t͡sʼ] |  |
| ⟨tʼ⟩ | [tʼ] |  |
| ⟨u⟩ | [ù] | word initial [ʔù] |
| ⟨uu⟩ | [ùː] | word initial [ʔùː] |
| ⟨u̧⟩ | [ũ̀] | word initial [ʔũ̀] |
| ⟨u̧u⟩ | [ũ̀ː] | word initial [ʔũ̀ː] |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨wh⟩ | [xʷ] |  |
| ⟨xw⟩ | [xʷ] |  |
| ⟨y⟩ | [j] |  |
| ⟨á⟩ | [ɑ́] | word initial [ʔɑ́] |
| ⟨áa⟩ | [ɑ́ː] | word initial [ʔɑ́ː] |
| ⟨áy⟩ | [éː] | before vowel [ɑ́j] · word initial [ʔéː] |
| ⟨á̧⟩ | [ɑ̃́] | word initial [ʔɑ̃́] |
| ⟨á̧a⟩ | [ɑ̃́ː] | word initial [ʔɑ̃́ː] |
| ⟨á̧y⟩ | [ẽ́ː] | before vowel [ɑ̃́j] · word initial [ʔẽ́ː] |
| ⟨â⟩ | [ɑ̂] | word initial [ʔɑ̂] |
| ⟨âa⟩ | [ɑ̂ː] | word initial [ʔɑ̂ː] |
| ⟨ây⟩ | [êː] | before vowel [ɑ̂j] · word initial [ʔêː] |
| ⟨â̧⟩ | [ɑ̃̂] | word initial [ʔɑ̃̂] |
| ⟨â̧a⟩ | [ɑ̃̂ː] | word initial [ʔɑ̃̂ː] |
| ⟨â̧y⟩ | [ẽ̂ː] | before vowel [ɑ̃̂j] · word initial [ʔẽ̂ː] |
| ⟨ä⟩ | [æ̀] | word initial [ʔæ̀] |
| ⟨ää⟩ | [æ̀ː] | word initial [ʔæ̀ː] |
| ⟨ä́⟩ | [ǽ] | word initial [ʔǽ] |
| ⟨ä́ä⟩ | [ǽː] | word initial [ʔǽː] |
| ⟨ä̂⟩ | [æ̂] | word initial [ʔæ̂] |
| ⟨ä̂ä⟩ | [æ̂ː] | word initial [ʔæ̂ː] |
| ⟨ä̧⟩ | [æ̃̀] | word initial [ʔæ̃̀] |
| ⟨ä̧ä⟩ | [æ̃̀ː] | word initial [ʔæ̃̀ː] |
| ⟨ä̧́⟩ | [æ̃́] | word initial [ʔæ̃́] |
| ⟨ä̧́ä⟩ | [æ̃́ː] | word initial [ʔæ̃́ː] |
| ⟨ä̧̂⟩ | [æ̃̂] | word initial [ʔæ̃̂] |
| ⟨ä̧̂ä⟩ | [æ̃̂ː] | word initial [ʔæ̃̂ː] |
| ⟨é⟩ | [é] | word initial [ʔé] |
| ⟨ée⟩ | [íː] | word initial [ʔíː] |
| ⟨ê⟩ | [ê] | word initial [ʔê] |
| ⟨êe⟩ | [îː] | word initial [ʔîː] |
| ⟨í⟩ | [í] | word initial [ʔí] |
| ⟨í̧⟩ | [ĩ́] | word initial [ʔĩ́] |
| ⟨î⟩ | [î] | word initial [ʔî] |
| ⟨î̧⟩ | [ĩ̂] | word initial [ʔĩ̂] |
| ⟨ñ⟩ | [j] |  |
| ⟨ó⟩ | [ó] | word initial [ʔó] |
| ⟨óe⟩ | [óː] | word initial [ʔóː] |
| ⟨ó̧⟩ | [ṍ] | word initial [ʔṍ] |
| ⟨ó̧e⟩ | [ṍː] | word initial [ʔṍː] |
| ⟨ô⟩ | [ô] | word initial [ʔô] |
| ⟨ôe⟩ | [ôː] | word initial [ʔôː] |
| ⟨ô̧⟩ | [õ̂] | word initial [ʔõ̂] |
| ⟨ô̧e⟩ | [õ̂ː] | word initial [ʔõ̂ː] |
| ⟨ú⟩ | [ú] | word initial [ʔú] |
| ⟨úu⟩ | [úː] | word initial [ʔúː] |
| ⟨ú̧⟩ | [ṹ] | word initial [ʔṹ] |
| ⟨ú̧u⟩ | [ṹː] | word initial [ʔṹː] |
| ⟨û⟩ | [û] | word initial [ʔû] |
| ⟨ûu⟩ | [ûː] | word initial [ʔûː] |
| ⟨û̧⟩ | [ũ̂] | word initial [ʔũ̂] |
| ⟨û̧u⟩ | [ũ̂ː] | word initial [ʔũ̂ː] |
| ⟨č⟩ | [t͡ʃ] |  |
| ⟨čʼ⟩ | [t͡ʃʼ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ȩ⟩ | [ẽ̀] | word initial [ʔẽ̀] |
| ⟨ȩe⟩ | [ĩ̀ː] | word initial [ʔĩ̀ː] |
| ⟨ȩ́⟩ | [ẽ́] | word initial [ʔẽ́] |
| ⟨ȩ́e⟩ | [ĩ́ː] | word initial [ʔĩ́ː] |
| ⟨ȩ̂⟩ | [ẽ̂] | word initial [ʔẽ̂] |
| ⟨ȩ̂e⟩ | [ĩ̂ː] | word initial [ʔĩ̂ː] |
| ⟨ʔ⟩ | [ʔ] |  |
| ⟨ḏ⟩ | [d] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 3 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `TEW_CODA_NASAL_VELAR` | /m n j/ → [ŋ], before a consonant | - | [Martinez 1982](#src-tew_martinez1982), [Sutton 2014](#src-tew_sutton2014) |
| `TEW_CODA_NASAL_VELAR_FINAL` | /m n j/ → [ŋ], word-finally | - | - |
| `TEW_SILENT_FINAL_H` | /h/ → ∅, word-finally, after ⟨e⟩ ⟨é⟩ ⟨ê⟩ ⟨ȩ⟩ ⟨ȩ́⟩ ⟨ȩ̂⟩ | ⟨teh⟩ [tè] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tew")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tetum](tet.md) · [Home](../index.md) · [Thai →](th.md)
