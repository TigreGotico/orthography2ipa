# Kurukh (`kru`)

<!-- atlas:summary begin -->
Kurukh is a Dravidian language, written in the Devanagari script. Glottolog places it in the Eurasia macroarea. The `kru` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kru` |
| ISO 639-3 | [kru](https://iso639-3.sil.org/code/kru), Kurukh |
| Wikipedia | [Kurukh language](https://en.wikipedia.org/wiki/Kurukh_language) |
| Family | [Dravidian](by-family.md#dravidian) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Devanagari](by-script.md#devanagari) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Dravidian](https://tigregotico.github.io/orthography2ipa/#x-clade-drav1251) `x-clade-drav1251` |
| Explorer | [`kru` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kru) |
| Spec file | [`kru.json`](../../orthography2ipa/data/kru.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Kurukh (Oraon), a North Dravidian language of eastern India written in Devanagari. Consonant letters and vowel signs (matras) are mapped to standard Devanagari IPA values, including the retroflex and breathy-voiced series and nuqta letters ड़ ढ़ ख़.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1928 to 2024. [Sources](#sources) lists them. The spec file writes all 59 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kru.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kru` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kru_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Kurukh (kuru1301)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/kuru1301)
2. <a id="src-winfield1928"></a>Winfield, W. W. (1928). *A Grammar of the Kurux Language*. Asiatic Society of Bengal, Calcutta.
3. <a id="src-kru_wikipedia"></a>Wikipedia contributors (2024). *Kurukh language*. Wikipedia.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kru` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 187 | 0.1947 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 46 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  |  | dʒ tʃ tʃʰ |  |  |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |
| Fricative |  |  | s | ʃ |  |  | x | h |
| Approximant |  | ʋ |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | aː |  |  |

Sequences that the spec writes as one unit: [ai] [au] [bʱ] [dʒʱ] [d̪ʱ] [ɖʱ] [ɡʱ] [ɽʱ] [̃].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ँ⟩ | [̃] |  |
| ⟨ं⟩ | [̃] |  |
| ⟨ः⟩ | [h] |  |
| ⟨अ⟩ | [ə] |  |
| ⟨आ⟩ | [aː] |  |
| ⟨इ⟩ | [i] |  |
| ⟨ई⟩ | [iː] |  |
| ⟨उ⟩ | [u] |  |
| ⟨ऊ⟩ | [uː] |  |
| ⟨ए⟩ | [e] |  |
| ⟨ऐ⟩ | [ai] |  |
| ⟨ओ⟩ | [o] |  |
| ⟨औ⟩ | [au] |  |
| ⟨क⟩ | [k] |  |
| ⟨ख⟩ | [kʰ] |  |
| ⟨ख़⟩ | [x] |  |
| ⟨ग⟩ | [ɡ] |  |
| ⟨घ⟩ | [ɡʱ] |  |
| ⟨ङ⟩ | [ŋ] |  |
| ⟨च⟩ | [tʃ] |  |
| ⟨छ⟩ | [tʃʰ] |  |
| ⟨ज⟩ | [dʒ] |  |
| ⟨झ⟩ | [dʒʱ] |  |
| ⟨ञ⟩ | [ɲ] |  |
| ⟨ट⟩ | [ʈ] |  |
| ⟨ठ⟩ | [ʈʰ] |  |
| ⟨ड⟩ | [ɖ] |  |
| ⟨ड़⟩ | [ɽ] |  |
| ⟨ढ⟩ | [ɖʱ] |  |
| ⟨ढ़⟩ | [ɽʱ] |  |
| ⟨ण⟩ | [ɳ] |  |
| ⟨त⟩ | [t̪] |  |
| ⟨थ⟩ | [t̪ʰ] |  |
| ⟨द⟩ | [d̪] |  |
| ⟨ध⟩ | [d̪ʱ] |  |
| ⟨न⟩ | [n] |  |
| ⟨प⟩ | [p] |  |
| ⟨फ⟩ | [pʰ] |  |
| ⟨ब⟩ | [b] |  |
| ⟨भ⟩ | [bʱ] |  |
| ⟨म⟩ | [m] |  |
| ⟨य⟩ | [j] |  |
| ⟨र⟩ | [r] |  |
| ⟨ल⟩ | [l] |  |
| ⟨व⟩ | [ʋ] |  |
| ⟨श⟩ | [ʃ] |  |
| ⟨ष⟩ | [ʃ] |  |
| ⟨स⟩ | [s] |  |
| ⟨ह⟩ | [h] |  |
| ⟨ा⟩ | [aː] |  |
| ⟨ि⟩ | [i] |  |
| ⟨ी⟩ | [iː] |  |
| ⟨ु⟩ | [u] |  |
| ⟨ू⟩ | [uː] |  |
| ⟨े⟩ | [e] |  |
| ⟨ै⟩ | [ai] |  |
| ⟨ो⟩ | [o] |  |
| ⟨ौ⟩ | [au] |  |
| ⟨्⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kru")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kurdish](ku.md) · [Home](../index.md) · [Kusaal →](kus.md)
