# Wiyot (`wiy`)

<!-- atlas:summary begin -->
Wiyot is an Algic language, written in the Latin script. Glottolog places it in the North America macroarea. The `wiy` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `wiy` |
| ISO 639-3 | [wiy](https://iso639-3.sil.org/code/wiy), Wiyot |
| Wikipedia | [Wiyot language](https://en.wikipedia.org/wiki/Wiyot_language) |
| Family | [Algic](by-family.md#algic) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Algic](https://tigregotico.github.io/orthography2ipa/#x-clade-algi1248) `x-clade-algi1248` |
| Explorer | [`wiy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#wiy) |
| Spec file | [`wiy.json`](../../orthography2ipa/data/wiy.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Algic language (a divergent isolate within Algic, alongside Yurok) of coastal northern California, written in Teeter's Americanist practical orthography (the WikiPron gold this spec is scored against is transcribed with Teeter's letters, not the Wiyot Tribe's alternate orthography).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1925 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 44 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/wiy.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `wiy` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 5 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wiy_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Wiyot (wiyo1248)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/wiyo1248)
2. <a id="src-wiy_orthography"></a>Wikipedia contributors (2024). *Wiyot language, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Wiyot_language)
3. <a id="src-wiy_teeter_1964"></a>Teeter, Karl V. (1964). *The Wiyot Language*. University of California Press. [archive.org](https://archive.org/details/wiyotlanguage0037teet)
4. <a id="src-wiy_reichard_1925"></a>Reichard, Gladys A. (1925). *Wiyot Grammar and Texts*. University of California Publications in American Archaeology and Ethnology 22(1), University of California Press. Cited: 9, 131-132. [archive.org](https://archive.org/details/WiyotGrammarAndTexts)
5. <a id="src-wiy_teeter_1995"></a>Teeter, Karl V. (1995). *Wiyot Obsolescence*. Papers of the Algonquian Conference 26, Carleton University. Cited: 457-461. [ojs.library.carleton.ca](https://ojs.library.carleton.ca/index.php/ALGQP/article/view/601)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `wiy` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 151 | 0.0164 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ | t tʰ |  |  | k kʰ kʷ kʷʰ ɡʷ | ʔ |
| Affricate |  | ts tsʰ | tʃ tʃʰ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Tap |  | ɾ |  |  |  |  |
| Fricative | β | s | ʃ |  | ɣ | h |
| Lateral fricative |  | ɬ |  |  |  |  |
| Approximant |  | ɹ |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i ì í | u ù ú |
| Close-mid | e è é |  |
| Open | a à á | ɑ ɑ̀ ɑ́ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [β] |  |
| ⟨c⟩ | [ts] |  |
| ⟨ch⟩ | [tsʰ] |  |
| ⟨d⟩ | [ɾ] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨gw⟩ | [ɡʷ] |  |
| ⟨h⟩ | [h] | default [ʔ] · word initial [h] |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨kwh⟩ | [kʷʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [ɬ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ɑ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [ɹ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨à⟩ | [à] |  |
| ⟨á⟩ | [á] |  |
| ⟨è⟩ | [è] |  |
| ⟨é⟩ | [é] |  |
| ⟨ì⟩ | [ì] |  |
| ⟨í⟩ | [í] |  |
| ⟨ò⟩ | [ɑ̀] |  |
| ⟨ó⟩ | [ɑ́] |  |
| ⟨ù⟩ | [ù] |  |
| ⟨ú⟩ | [ú] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨čh⟩ | [tʃʰ] |  |
| ⟨ł⟩ | [ɬ] |  |
| ⟨š⟩ | [ʃ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "wiy")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Western Punjabi](pnb-PK.md) · [Home](../index.md) · [Wolof →](wo.md)
