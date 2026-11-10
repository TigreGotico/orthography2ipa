# Pnar (`pbv`)

<!-- atlas:summary begin -->
Pnar is an Austroasiatic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `pbv` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pbv` |
| ISO 639-3 | [pbv](https://iso639-3.sil.org/code/pbv), Pnar |
| Wikipedia | [Pnar language](https://en.wikipedia.org/wiki/Pnar_language) |
| Family | [Austroasiatic](by-family.md#austroasiatic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Austroasiatic](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1305) `x-clade-aust1305` |
| Explorer | [`pbv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pbv) |
| Spec file | [`pbv.json`](../../orthography2ipa/data/pbv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Austroasiatic (Khasian) language of Meghalaya, India, written in the missionary-derived Roman orthography shared with Khasi.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2015 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 37 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pbv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pbv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-pbv_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Pnar (pnar1238)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/pnar1238)
2. <a id="src-pbv_omniglot"></a>Ager, S. (2024). *Pnar language and alphabet*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/pnar.htm)
3. <a id="src-pbv_khasi_wikipedia"></a>Wikipedia contributors (2024). *Khasi language (writing system)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Khasi_language)
4. <a id="src-pbv_ring2015"></a>Ring, Hiram (2015). *A Grammar of Pnar*. PhD dissertation, Nanyang Technological University.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `pbv` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 101 | 0.3358 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ | d t̪ t̪ʰ |  |  | k kʰ ɡ |  |
| Affricate |  |  | dʒ tʃ |  |  |  |
| Nasal | m | n |  | ɲ | ŋ |  |
| Trill |  | r |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː | ɨ | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | e eː |  | oː |
| Open-mid | ɛ |  | ɔ |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [bʱ] [dʒʱ] [dʱ] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨bh⟩ | [bʱ] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [dʱ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨ie⟩ | [e] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨jh⟩ | [dʒʱ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t̪] |  |
| ⟨th⟩ | [t̪ʰ] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨á⟩ | [aː] |  |
| ⟨é⟩ | [eː] |  |
| ⟨í⟩ | [iː] |  |
| ⟨ï⟩ | [ɨ] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [oː] |  |
| ⟨ú⟩ | [uː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pbv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Plains Cree](crk.md) · [Home](../index.md) · [Polabian →](pox.md)
