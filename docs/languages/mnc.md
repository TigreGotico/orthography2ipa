# Manchu (`mnc`)

<!-- atlas:summary begin -->
Manchu is a Tungusic language, written in the Latn script. Glottolog places it in the Eurasia macroarea. The `mnc` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mnc` |
| ISO 639-3 | [mnc](https://iso639-3.sil.org/code/mnc), Manchu |
| Wikipedia | [Manchu language](https://en.wikipedia.org/wiki/Manchu_language) |
| Family | [Tungusic](by-family.md#tungusic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latn](by-script.md#latn) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Tungusic](https://tigregotico.github.io/orthography2ipa/#x-clade-tung1282) `x-clade-tung1282` |
| Explorer | [`mnc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mnc) |
| Spec file | [`mnc.json`](../../orthography2ipa/data/mnc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> The gold used to exercise this spec is NorthEuraLex's `mnc` row: its Value column is written in Latin letters ("yasa", "oforo", "angga", "weihe"), not the vertical Manchu (Mongolian-derived) script -- confirmed by direct inspection of lexibank/northeuralex forms.csv, which never produces script glyphs for this language.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1892 to 2024. [Sources](#sources) lists them. The spec file writes all 29 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mnc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mnc` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL.

1. <a id="src-moellendorff1892"></a>von Moellendorff, Paul Georg (1892). *A Manchu Grammar, with Analysed Texts*. Shanghai: American Presbyterian Mission Press.
2. <a id="src-gorelova2002"></a>Gorelova, Liliya M. (2002). *Manchu Grammar*. Brill (Handbook of Oriental Studies).
3. <a id="src-mnc_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Manchu (manc1252)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/manc1252)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `mnc` | gold | lexicon-derived | CC BY 4.0 | 1205 | 0.1411 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 26 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b pʰ |  | d tʰ |  |  | k kʰ |
| Affricate |  |  | dz | tʃ tʃʰ |  |  |
| Nasal | m |  | n |  |  | ŋ |
| Trill |  |  | r |  |  |  |
| Fricative |  | f | s | ʃ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Near-close |  | ʊ |
| Close-mid |  | ɤ |
| Open-mid |  | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɤ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [k] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [tʃ] |  |
| ⟨jy⟩ | [tʃ] |  |
| ⟨k⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sy⟩ | [ʃ] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [dz] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ū⟩ | [ʊ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mnc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Maltese](mt.md) · [Home](../index.md) · [Mandarin Chinese →](zh.md)
