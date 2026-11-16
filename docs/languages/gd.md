# Scottish Gaelic (`gd`)

<!-- atlas:summary begin -->
Scottish Gaelic is a Goidelic language, written in the Latin script. Glottolog places it in United Kingdom. The `gd` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gd` |
| ISO 639-3 | [gla](https://iso639-3.sil.org/code/gla), Scottish Gaelic |
| Glottolog | [scot1245](https://glottolog.org/resource/languoid/id/scot1245), Scottish Gaelic |
| Wikidata | [Q9314](https://www.wikidata.org/wiki/Q9314) |
| Wikipedia | [Scottish Gaelic](https://en.wikipedia.org/wiki/Scottish_Gaelic) |
| Family | [Indo-European](by-family.md#indo-european) > [Celtic > Goidelic](by-family.md#indo-european--celtic--goidelic) |
| Region | [Eurasia](by-region.md#eurasia) > [United Kingdom](by-region.md#united-kingdom) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1600, living |
| Ancestor | [Proto-Goidelic (reconstructed)](https://tigregotico.github.io/orthography2ipa/#cel-x-goidelic) `cel-x-goidelic` |
| Explorer | [`gd` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gd) |
| Spec file | [`gd.json`](../../orthography2ipa/data/gd.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Scottish Gaelic (Gàidhlig). ~57,000 speakers (2011 census). Highlands and Islands of Scotland.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1956 to 2021. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gd.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gd` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 3 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-macaulay1992"></a>MacAulay, D. (ed.) (1992). *The Celtic Languages*. Cambridge University Press.
2. <a id="src-oftedal1956"></a>Oftedal, M. (1956). *The Gaelic of Leurbost, Isle of Lewis*. Norsk Tidsskrift for Sprogvidenskap.
3. <a id="src-iosad2015"></a>Iosad, P. (2015). *A Substance-Free Framework for Phonology: An Analysis of the Brythonic Languages*. Edinburgh University Press.
4. <a id="src-bauer2011"></a>Bauer, M. (2011). *Blas na Gàidhlig: The Practical Guide to Scottish Gaelic Pronunciation*. Akerbeltz. [akerbeltz.org](https://www.akerbeltz.org/)
5. <a id="src-goc2009"></a>Scottish Qualifications Authority (2009). *Gaelic Orthographic Conventions (GOC)*. SQA. [sqa.org.uk](https://www.sqa.org.uk/)
6. <a id="src-nance_omaolalaigh2021"></a>Nance, C. and Ó Maolalaigh, R. (2021). *Scottish Gaelic*. Journal of the International Phonetic Association 51(2), 261-275 (Illustrations of the IPA). [doi.org](https://doi.org/10.1017/S002510031900015X)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `gd` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 3719 | 0.2774 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 61 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | tʲ tʲʰ t̪ t̪ʰ |  |  | k kʰ kʲ kʲʰ |  |
| Nasal | m |  | n n̪ˠ |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ ɾʲ |  |  |  |  |
| Fricative |  | f v | s̪ | ʃ | ç ʝ | x ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l l̪ˠ |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː ɯ ɯː |
| Near-close | ɪ |  | ʊ |
| Close-mid | e eː |  | o oː ɤ |
| Mid |  | ə |  |
| Open-mid | ɛ ɛː |  | ɔ ɔː |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [hp] [htʲ] [ht̪] [ia] [n̪ˠɣ] [xk] [çkʲ] [ŋk] [əɣ] [ɲkʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [ə] | after e [a] [ɛ] [e] · after i [ə] · after u [ə] · before i [a] · nucleus unstressed [ə] · word final [ə] |
| ⟨ao⟩ | [ɯː] |  |
| ⟨b⟩ | [p] |  |
| ⟨bh⟩ | [v] |  |
| ⟨c⟩ | [kʰ] [kʲʰ] | after front vowel [kʲʰ] · before front vowel [kʲʰ] |
| ⟨ch⟩ | [x] [ç] | after front vowel [ç] · before front vowel [ç] |
| ⟨chd⟩ | [xk] |  |
| ⟨d⟩ | [t̪] [tʲ] | after front vowel [tʲ] · before front vowel [tʲ] |
| ⟨dh⟩ | [ɣ] [ʝ] | after front vowel [j] [ʝ] · before front vowel [ʝ] [j] · word final ∅ |
| ⟨e⟩ | [e] [ɛ] | before back vowel ∅ · before u [eː] · nucleus unstressed [ə] · word final [ə] |
| ⟨f⟩ | [f] |  |
| ⟨fh⟩ | ∅ |  |
| ⟨g⟩ | [k] [kʲ] | after front vowel [kʲ] · before front vowel [kʲ] |
| ⟨gh⟩ | [ɣ] [ʝ] | after front vowel [j] [ʝ] · before front vowel [ʝ] [j] · word final [j] ∅ |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] [ɪ] | after vowel ∅ · before a [i] · before u ∅ |
| ⟨l⟩ | [l̪ˠ] [l] [ʎ] | after front vowel [l] [ʎ] · before front vowel [l] [ʎ] · intervocalic [l] |
| ⟨ll⟩ | [l̪ˠ] [ʎ] | after front vowel [ʎ] · before front vowel [ʎ] |
| ⟨m⟩ | [m] |  |
| ⟨mh⟩ | [v] |  |
| ⟨n⟩ | [n̪ˠ] [n] [ɲ] | after front vowel [ɲ] [n] · before front vowel [ɲ] [n] · intervocalic [n] · word final [n] |
| ⟨ng⟩ | [ŋk] | after front vowel [ɲkʲ] · before front vowel [ɲkʲ] |
| ⟨ngh⟩ | [n̪ˠɣ] |  |
| ⟨nn⟩ | [n̪ˠ] [ɲ] | after front vowel [ɲ] · before front vowel [ɲ] |
| ⟨o⟩ | [ɔ] [o] | after e [ɔ] · after front vowel ∅ · nucleus unstressed [ə] |
| ⟨p⟩ | [pʰ] |  |
| ⟨ph⟩ | [f] |  |
| ⟨r⟩ | [ɾ] [r] | after front vowel [ɾʲ] · before front vowel [ɾʲ] |
| ⟨rr⟩ | [ɾ] [r] |  |
| ⟨s⟩ | [s̪] [ʃ] | after front vowel [ʃ] · before front vowel [ʃ] |
| ⟨sh⟩ | [h] |  |
| ⟨t⟩ | [t̪ʰ] [tʲʰ] | after front vowel [tʲʰ] · before front vowel [tʲʰ] |
| ⟨th⟩ | [h] | word final ∅ |
| ⟨u⟩ | [u] [ʊ] | after e ∅ · before a [u] · before front vowel ∅ · before i [ɯ] [u] · nucleus unstressed [ə] |
| ⟨à⟩ | [aː] |  |
| ⟨è⟩ | [ɛː] |  |
| ⟨é⟩ | [eː] |  |
| ⟨ì⟩ | [iː] |  |
| ⟨ò⟩ | [ɔː] |  |
| ⟨ó⟩ | [oː] |  |
| ⟨ù⟩ | [uː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 10 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `GD_PREASP_C_BROAD` | /kʰ/ → [xk], after a vowel | ⟨mac⟩ [maxk] | [Oftedal 1956](#src-oftedal1956), [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
| `GD_PREASP_C_SLENDER` | /kʲʰ/ → [çkʲ], after a vowel | - | [Oftedal 1956](#src-oftedal1956), [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
| `GD_PREASP_T_BROAD` | /t̪ʰ/ → [ht̪], after a vowel | - | [Oftedal 1956](#src-oftedal1956), [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
| `GD_PREASP_T_SLENDER` | /tʲʰ/ → [htʲ], after a vowel | - | [Oftedal 1956](#src-oftedal1956), [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
| `GD_PREASP_P` | /pʰ/ → [hp], after a vowel | - | [Oftedal 1956](#src-oftedal1956), [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
| `GD_UNASPIRATED_AFTER_CONSONANT_P` | /pʰ/ → [p], after a consonant | - | [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
| `GD_UNASPIRATED_AFTER_CONSONANT_T_BROAD` | /t̪ʰ/ → [t̪], after a consonant | - | [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
| `GD_UNASPIRATED_AFTER_CONSONANT_T_SLENDER` | /tʲʰ/ → [tʲ], after a consonant | - | [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
| `GD_UNASPIRATED_AFTER_CONSONANT_C_BROAD` | /kʰ/ → [k], after a consonant | - | [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
| `GD_UNASPIRATED_AFTER_CONSONANT_C_SLENDER` | /kʲʰ/ → [kʲ], after a consonant | - | [Nance 2021](#src-nance_omaolalaigh2021), Maolalaigh 2021 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gd")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Saʿīdi Arabic](aec-EG.md) · [Home](../index.md) · [Sea Island Creole English →](gul.md)
