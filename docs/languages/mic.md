# Mi'kmaq (`mic`)

<!-- atlas:summary begin -->
Mi'kmaq is an Algic language, written in the Latin script. Glottolog places it in the North America macroarea. The `mic` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mic` |
| ISO 639-3 | [mic](https://iso639-3.sil.org/code/mic), Mi'kmaq |
| Wikipedia | [Mi'kmaq language](https://en.wikipedia.org/wiki/Mi%27kmaq_language) |
| Family | [Algic](by-family.md#algic) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Algic](https://tigregotico.github.io/orthography2ipa/#x-clade-algi1248) `x-clade-algi1248` |
| Explorer | [`mic` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mic) |
| Spec file | [`mic.json`](../../orthography2ipa/data/mic.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Algic (Algonquian) language of Atlantic Canada. The grapheme map reads the Listuguj orthography, which the shipped wikipron gold uses, the Francis-Smith letters k and á é í ó ú are carried as well, but Francis-Smith is not modelled in full here, since its schwa letter ɨ is absent.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1968 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 30 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mic.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mic` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mic_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Mi'kmaq (mikm1235)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/mikm1235)
2. <a id="src-mic_fidelholtz1968"></a>Fidelholtz, James Lawrence (1968). *Micmac Morphophonemics*. PhD dissertation, Massachusetts Institute of Technology. Cited: 12. [hdl.handle.net](https://hdl.handle.net/1721.1/13001)
3. <a id="src-mic_mikmaqonline"></a>Mi'gmaq-Mi'kmaq Online (Listuguj Mi'gmaq Government) (2024). *Mi'gmaq-Mi'kmaq Online Talking Dictionary*. Listuguj Mi'gmaq Government. [mikmaqonline.org](https://mikmaqonline.org/)
4. <a id="src-mic_orthography"></a>Wikipedia contributors (2024). *Mi'kmaq language (Francis-Smith orthography), Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Mi%27kmaq_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mic` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 203 | 0.1114 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 24 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  | k kʷ |  |
| Affricate |  |  | tʃ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Fricative |  | s |  |  | x | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | eː |  | oː |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ə] |  |
| ⟨a⟩ | [a] |  |
| ⟨a'⟩ | [aː] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨e'⟩ | [eː] |  |
| ⟨g⟩ | [k] |  |
| ⟨gw⟩ | [kʷ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨i'⟩ | [iː] |  |
| ⟨j⟩ | [tʃ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨o'⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [x] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨u'⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨á⟩ | [aː] |  |
| ⟨é⟩ | [eː] |  |
| ⟨í⟩ | [iː] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mic")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mexican Spanish](es-MX.md) · [Home](../index.md) · [Middle Dutch →](dum.md)
