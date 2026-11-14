# South Slavey (`xsl`)

<!-- atlas:summary begin -->
South Slavey is an Athabaskan-Eyak-Tlingit language, written in the Latin script. Glottolog places it in the North America macroarea. The `xsl` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `xsl` |
| ISO 639-3 | [xsl](https://iso639-3.sil.org/code/xsl), South Slavey |
| Wikipedia | [Slavey language](https://en.wikipedia.org/wiki/Slavey_language) |
| Family | [Athabaskan-Eyak-Tlingit](by-family.md#athabaskan-eyak-tlingit) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Athabaskan-Eyak-Tlingit](https://tigregotico.github.io/orthography2ipa/#x-clade-atha1245) `x-clade-atha1245` |
| Explorer | [`xsl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#xsl) |
| Spec file | [`xsl.json`](../../orthography2ipa/data/xsl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Northern Athabaskan (Dene) language of the Dehcho region of the Northwest Territories, in its practical Roman orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1989 to 2024. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 87 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/xsl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `xsl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-xsl_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: South Slavey (sout2959)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/sout2959)
2. <a id="src-xsl_wikipedia"></a>Wikipedia contributors (2024). *Slavey language, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Slavey_language)
3. <a id="src-xsl_dene_speech_atlas"></a>McDonough, Joyce (ed.) (2020). *Dene Speech Atlas: Orthography for South Slavey*. University of Rochester. [sas.rochester.edu](https://www.sas.rochester.edu/lin/DeneSpeechAtlas/dene-language-groups/south-slavey/orthography-for-south-slave/)
4. <a id="src-xsl_preaspiration"></a>Wikipedia contributors (2024). *Preaspiration, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Preaspiration)
5. <a id="src-xsl_rice1989"></a>Rice, Keren (1989). *A Grammar of Slave*. Mouton de Gruyter.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `xsl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 146 | 0.0273 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 90 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  | d t tʰ tʼ ⁿd ⁿt |  | c cʰ | k kʰ kʷ kʷʰ kʼ ɡ | ʔ |
| Affricate |  | dð tθʰ tθʼ | dz ts tsʰ tsʼ tɬ tɬʰ tɬʼ | dʒ tʃ tʃʰ tʃʼ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | ð θ | s z | ʃ ʒ | ç ʝ | x xʷ ɣ ɣʷ | h |
| Lateral fricative |  |  | ɬ ɮ |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | ì ìː í íː ĩ̀ ĩ́ | ù ùː ú úː ũ̀ ṹ |
| Near-close | ɪ̀ ɪ́ |  |
| Close-mid |  | ò òː ó óː õ̀ ṍ |
| Open-mid | ɛ̀ ɛ̀ː ɛ́ ɛ́ː ɛ̃̀ ɛ̃́ |  |
| Open | à àː á áː ã̀ ã́ |  |

Sequences that the spec writes as one unit: [dl] [tð] [w] [ʰ] [ᵐb] [ᵐp].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [à] |  |
| ⟨aa⟩ | [àː] |  |
| ⟨aá⟩ | [áː] |  |
| ⟨b⟩ | [p] [b] |  |
| ⟨ch⟩ | [tʃʰ] |  |
| ⟨ch'⟩ | [tʃʼ] |  |
| ⟨chʼ⟩ | [tʃʼ] |  |
| ⟨d⟩ | [t] [d] |  |
| ⟨ddh⟩ | [tð] [dð] |  |
| ⟨dh⟩ | [ð] |  |
| ⟨dl⟩ | [tɬ] [dl] |  |
| ⟨dz⟩ | [ts] [dz] |  |
| ⟨e⟩ | [ɛ̀] |  |
| ⟨ee⟩ | [ɛ̀ː] |  |
| ⟨eé⟩ | [ɛ́ː] |  |
| ⟨g⟩ | [k] [ɡ] |  |
| ⟨gh⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ì] |  |
| ⟨ii⟩ | [ìː] |  |
| ⟨ií⟩ | [íː] |  |
| ⟨j⟩ | [tʃ] [dʒ] |  |
| ⟨k⟩ | [kʰ] |  |
| ⟨k'⟩ | [kʼ] |  |
| ⟨kʼ⟩ | [kʼ] |  |
| ⟨l⟩ | [ɮ] [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] [ᵐp] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ⁿd] [ⁿt] |  |
| ⟨o⟩ | [ò] |  |
| ⟨oo⟩ | [òː] |  |
| ⟨oó⟩ | [óː] |  |
| ⟨p⟩ | [p] |  |
| ⟨p'⟩ | [pʼ] |  |
| ⟨pʼ⟩ | [pʼ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨t'⟩ | [tʼ] |  |
| ⟨th⟩ | [θ] |  |
| ⟨tl⟩ | [tɬʰ] |  |
| ⟨tl'⟩ | [tɬʼ] |  |
| ⟨tlʼ⟩ | [tɬʼ] |  |
| ⟨ts⟩ | [tsʰ] |  |
| ⟨ts'⟩ | [tsʼ] |  |
| ⟨tsʼ⟩ | [tsʼ] |  |
| ⟨tth⟩ | [tθʰ] |  |
| ⟨tth'⟩ | [tθʼ] |  |
| ⟨tthʼ⟩ | [tθʼ] |  |
| ⟨tł⟩ | [tɬʰ] |  |
| ⟨tł'⟩ | [tɬʼ] |  |
| ⟨tłʼ⟩ | [tɬʼ] |  |
| ⟨tʼ⟩ | [tʼ] |  |
| ⟨u⟩ | [ù] |  |
| ⟨uu⟩ | [ùː] |  |
| ⟨uú⟩ | [úː] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] [ʒ] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |
| ⟨á⟩ | [á] |  |
| ⟨áa⟩ | [áː] |  |
| ⟨é⟩ | [ɛ́] |  |
| ⟨ée⟩ | [ɛ́ː] |  |
| ⟨í⟩ | [í] |  |
| ⟨íi⟩ | [íː] |  |
| ⟨ó⟩ | [ó] |  |
| ⟨óo⟩ | [óː] |  |
| ⟨ú⟩ | [ú] |  |
| ⟨úu⟩ | [úː] |  |
| ⟨ą⟩ | [ã̀] |  |
| ⟨ą́⟩ | [ã́] |  |
| ⟨ę⟩ | [ɛ̃̀] |  |
| ⟨ę́⟩ | [ɛ̃́] |  |
| ⟨į⟩ | [ĩ̀] |  |
| ⟨į́⟩ | [ĩ́] |  |
| ⟨ł⟩ | [ɬ] |  |
| ⟨ų⟩ | [ũ̀] |  |
| ⟨ų́⟩ | [ṹ] |  |
| ⟨ǫ⟩ | [õ̀] |  |
| ⟨ǫ́⟩ | [ṍ] |  |
| ⟨ɂ⟩ | [ʔ] |  |
| ⟨ʼ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 11 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `xsl_k_front` | /kʰ/ → [cʰ], spelled ⟨k⟩, before ⟨e⟩ ⟨é⟩ ⟨ę⟩ ⟨ę́⟩ ⟨i⟩ ⟨í⟩ ⟨į⟩ ⟨į́⟩ and 6 more | - | - |
| `xsl_k_round` | /kʰ/ → [kʷʰ], spelled ⟨k⟩, before ⟨o⟩ ⟨ó⟩ ⟨ǫ⟩ ⟨ǫ́⟩ ⟨u⟩ ⟨ú⟩ ⟨ų⟩ ⟨ų́⟩ and 6 more | - | - |
| `xsl_g_front` | /k/ → [c], spelled ⟨g⟩, before ⟨e⟩ ⟨é⟩ ⟨ę⟩ ⟨ę́⟩ ⟨i⟩ ⟨í⟩ ⟨į⟩ ⟨į́⟩ and 6 more | - | - |
| `xsl_g_round` | /k/ → [kʷ], spelled ⟨g⟩, before ⟨o⟩ ⟨ó⟩ ⟨ǫ⟩ ⟨ǫ́⟩ ⟨u⟩ ⟨ú⟩ ⟨ų⟩ ⟨ų́⟩ and 6 more | - | - |
| `xsl_x_front` | /x/ → [ç], spelled ⟨x⟩, before ⟨e⟩ ⟨é⟩ ⟨ę⟩ ⟨ę́⟩ ⟨i⟩ ⟨í⟩ ⟨į⟩ ⟨į́⟩ and 6 more | - | - |
| `xsl_x_round` | /x/ → [xʷ], spelled ⟨x⟩, before ⟨o⟩ ⟨ó⟩ ⟨ǫ⟩ ⟨ǫ́⟩ ⟨u⟩ ⟨ú⟩ ⟨ų⟩ ⟨ų́⟩ and 6 more | - | - |
| `xsl_gh_front` | /ɣ/ → [ʝ], spelled ⟨gh⟩, before ⟨e⟩ ⟨é⟩ ⟨ę⟩ ⟨ę́⟩ ⟨i⟩ ⟨í⟩ ⟨į⟩ ⟨į́⟩ and 6 more | - | - |
| `xsl_gh_round` | /ɣ/ → [ɣʷ], spelled ⟨gh⟩, before ⟨o⟩ ⟨ó⟩ ⟨ǫ⟩ ⟨ǫ́⟩ ⟨u⟩ ⟨ú⟩ ⟨ų⟩ ⟨ų́⟩ and 6 more | - | - |
| `xsl_coda_h_preaspiration` | /h/ → [ʰ], before a consonant, spelled ⟨h⟩ | - | - |
| `xsl_i_lax_non_final` | /ì/ → [ɪ̀], spelled ⟨i⟩, with more context in the spec | ⟨lidí⟩ [ɮɪ̀tí] | - |
| `xsl_i_lax_non_final_high` | /í/ → [ɪ́], spelled ⟨í⟩, with more context in the spec | ⟨ɂamíi⟩ [ʔàmɪ́ì] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "xsl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Souletin Basque](eu-x-zuberera.md) · [Home](../index.md) · [Southern Altai →](alt.md)
