# Western Apache (`apw`)

<!-- atlas:summary begin -->
Western Apache is an Athabaskan-Eyak-Tlingit language, written in the Latin script. Glottolog places it in the North America macroarea. The `apw` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `apw` |
| ISO 639-3 | [apw](https://iso639-3.sil.org/code/apw), Western Apache |
| Wikipedia | [Western Apache language](https://en.wikipedia.org/wiki/Western_Apache_language) |
| Family | [Athabaskan-Eyak-Tlingit](by-family.md#athabaskan-eyak-tlingit) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Athabaskan-Eyak-Tlingit](https://tigregotico.github.io/orthography2ipa/#x-clade-atha1245) `x-clade-atha1245` |
| Explorer | [`apw` in the data explorer](https://tigregotico.github.io/orthography2ipa/#apw) |
| Spec file | [`apw.json`](../../orthography2ipa/data/apw.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Southern Athabaskan (Apachean) language of east-central Arizona, written in the practical orthography used for San Carlos and White Mountain Apache.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1998 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 123 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/apw.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `apw` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-apw_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Western Apache (west2615)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/west2615)
2. <a id="src-apw_wikipedia"></a>Wikipedia contributors (2026). *Western Apache language, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Western_Apache_language)
3. <a id="src-apw_gordon2001"></a>Gordon, Matthew, Potter, Brian, Dawson, John, de Reuse, Willem, Ladefoged, Peter (2001). *Phonetic Structures of Western Apache*. International Journal of American Linguistics 67(4), 415-448. Cited: 415-448. [doi.org](https://doi.org/10.1086/466470)
4. <a id="src-apw_dereuse2006"></a>de Reuse, Willem J., Goode, Phillip (2006). *A Practical Grammar of the San Carlos Apache Language*. LINCOM Europa.
5. <a id="src-apw_bray1998"></a>Bray, Dorothy (ed.) (1998). *Western Apache-English Dictionary: A Community-Generated Bilingual Dictionary*. Bilingual Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `apw` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 147 | 0.3076 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 67 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ | t tʰ tʼ |  |  | k kʰ kʼ | ʔ |
| Affricate |  | ts tsʰ tsʼ tɬ tɬʰ tɬʼ | dʒ tʃʰ tʃʼ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Fricative |  | s z | ʃ ʒ |  | x ɣ | h |
| Lateral fricative |  | ɬ |  |  |  |  |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close |  | u uː ú úː |
| Near-close | ɪ ɪː ɪ́ ɪ́ː ɪ̃ ɪ̃ː ɪ̃́ ɪ̃́ː |  |
| Close-mid |  | o oː ó óː õ õː ṍ ṍː |
| Open-mid | ɛ ɛː ɛ́ ɛ́ː ɛ̃ ɛ̃ː ɛ̃́ ɛ̃́ː |  |
| Open | a aː á áː ã ãː ã́ ã́ː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨aá⟩ | [áː] |  |
| ⟨a̜⟩ | [ã] |  |
| ⟨a̜a̜⟩ | [ãː] |  |
| ⟨a̜á̜⟩ | [ã́ː] |  |
| ⟨b⟩ | [p] |  |
| ⟨ch⟩ | [tʃʰ] |  |
| ⟨ch'⟩ | [tʃʼ] |  |
| ⟨chʼ⟩ | [tʃʼ] |  |
| ⟨ch’⟩ | [tʃʼ] |  |
| ⟨d⟩ | [t] |  |
| ⟨dl⟩ | [tɬ] |  |
| ⟨dz⟩ | [ts] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨ee⟩ | [ɛː] |  |
| ⟨eé⟩ | [ɛ́ː] |  |
| ⟨e̜⟩ | [ɛ̃] |  |
| ⟨e̜e̜⟩ | [ɛ̃ː] |  |
| ⟨e̜é̜⟩ | [ɛ̃́ː] |  |
| ⟨g⟩ | [k] |  |
| ⟨gh⟩ | [ɣ] |  |
| ⟨h⟩ | [x] [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨ii⟩ | [ɪː] |  |
| ⟨ií⟩ | [ɪ́ː] |  |
| ⟨i̜⟩ | [ɪ̃] |  |
| ⟨i̜i̜⟩ | [ɪ̃ː] |  |
| ⟨i̜í̜⟩ | [ɪ̃́ː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [kʰ] |  |
| ⟨k'⟩ | [kʼ] |  |
| ⟨kʼ⟩ | [kʼ] |  |
| ⟨k’⟩ | [kʼ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨oó⟩ | [óː] |  |
| ⟨o̜⟩ | [õ] |  |
| ⟨o̜o̜⟩ | [õː] |  |
| ⟨o̜ó̜⟩ | [ṍː] |  |
| ⟨p⟩ | [pʰ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨t'⟩ | [tʼ] |  |
| ⟨tl'⟩ | [tɬʼ] |  |
| ⟨tlʼ⟩ | [tɬʼ] |  |
| ⟨tl’⟩ | [tɬʼ] |  |
| ⟨ts⟩ | [tsʰ] |  |
| ⟨ts'⟩ | [tsʼ] |  |
| ⟨tsʼ⟩ | [tsʼ] |  |
| ⟨ts’⟩ | [tsʼ] |  |
| ⟨tł⟩ | [tɬʰ] |  |
| ⟨tł'⟩ | [tɬʼ] |  |
| ⟨tłʼ⟩ | [tɬʼ] |  |
| ⟨tł’⟩ | [tɬʼ] |  |
| ⟨tʼ⟩ | [tʼ] |  |
| ⟨t’⟩ | [tʼ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨uú⟩ | [úː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |
| ⟨á⟩ | [á] |  |
| ⟨áa⟩ | [áː] |  |
| ⟨áá⟩ | [áː] |  |
| ⟨á̜⟩ | [ã́] |  |
| ⟨á̜a̜⟩ | [ã́ː] |  |
| ⟨á̜á̜⟩ | [ã́ː] |  |
| ⟨é⟩ | [ɛ́] |  |
| ⟨ée⟩ | [ɛ́ː] |  |
| ⟨éé⟩ | [ɛ́ː] |  |
| ⟨é̜⟩ | [ɛ̃́] |  |
| ⟨é̜e̜⟩ | [ɛ̃́ː] |  |
| ⟨é̜é̜⟩ | [ɛ̃́ː] |  |
| ⟨í⟩ | [ɪ́] |  |
| ⟨íi⟩ | [ɪ́ː] |  |
| ⟨íí⟩ | [ɪ́ː] |  |
| ⟨í̜⟩ | [ɪ̃́] |  |
| ⟨í̜i̜⟩ | [ɪ̃́ː] |  |
| ⟨í̜í̜⟩ | [ɪ̃́ː] |  |
| ⟨ó⟩ | [ó] |  |
| ⟨óo⟩ | [óː] |  |
| ⟨óó⟩ | [óː] |  |
| ⟨ó̜⟩ | [ṍ] |  |
| ⟨ó̜o̜⟩ | [ṍː] |  |
| ⟨ó̜ó̜⟩ | [ṍː] |  |
| ⟨ú⟩ | [ú] |  |
| ⟨úu⟩ | [úː] |  |
| ⟨úú⟩ | [úː] |  |
| ⟨ą⟩ | [ã] |  |
| ⟨ąą⟩ | [ãː] |  |
| ⟨ąą́⟩ | [ã́ː] |  |
| ⟨ą́⟩ | [ã́] |  |
| ⟨ą́ą⟩ | [ã́ː] |  |
| ⟨ą́ą́⟩ | [ã́ː] |  |
| ⟨ę⟩ | [ɛ̃] |  |
| ⟨ęę⟩ | [ɛ̃ː] |  |
| ⟨ęę́⟩ | [ɛ̃́ː] |  |
| ⟨ę́⟩ | [ɛ̃́] |  |
| ⟨ę́ę⟩ | [ɛ̃́ː] |  |
| ⟨ę́ę́⟩ | [ɛ̃́ː] |  |
| ⟨į⟩ | [ɪ̃] |  |
| ⟨įį⟩ | [ɪ̃ː] |  |
| ⟨įį́⟩ | [ɪ̃́ː] |  |
| ⟨į́⟩ | [ɪ̃́] |  |
| ⟨į́į⟩ | [ɪ̃́ː] |  |
| ⟨į́į́⟩ | [ɪ̃́ː] |  |
| ⟨ł⟩ | [ɬ] |  |
| ⟨ǫ⟩ | [õ] |  |
| ⟨ǫǫ⟩ | [õː] |  |
| ⟨ǫǫ́⟩ | [ṍː] |  |
| ⟨ǫ́⟩ | [ṍ] |  |
| ⟨ǫ́ǫ⟩ | [ṍː] |  |
| ⟨ǫ́ǫ́⟩ | [ṍː] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "apw")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Western Andalusian Spanish](es-ES-x-andalusi-w.md) · [Home](../index.md) · [Western Aragonese →](an-x-occident.md)
