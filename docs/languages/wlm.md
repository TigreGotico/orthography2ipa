# Middle Welsh (`wlm`)

<!-- atlas:summary begin -->
Middle Welsh is a Brythonic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `wlm` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `wlm` |
| ISO 639-3 | [wlm](https://iso639-3.sil.org/code/wlm), Middle Welsh |
| Wikipedia | [Middle Welsh](https://en.wikipedia.org/wiki/Middle_Welsh) |
| Family | [Indo-European](by-family.md#indo-european) > [Celtic > Brythonic](by-family.md#indo-european--celtic--brythonic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Brythonic](https://tigregotico.github.io/orthography2ipa/#x-clade-bryt1239) `x-clade-bryt1239` |
| Explorer | [`wlm` in the data explorer](https://tigregotico.github.io/orthography2ipa/#wlm) |
| Spec file | [`wlm.json`](../../orthography2ipa/data/wlm.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Brittonic (Insular Celtic) medieval stage written in the Latin alphabet.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1964 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 30 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/wlm.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `wlm` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wlm_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Middle Welsh (midd1363)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/midd1363)
2. <a id="src-evans1964"></a>Evans, D. Simon (1964). *A Grammar of Middle Welsh*. Dublin Institute for Advanced Studies.
3. <a id="src-wlm_wikipedia"></a>Wikipedia contributors (2024). *Middle Welsh (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Middle_Welsh)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `wlm` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 403 | 0.2498 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t | k ɡ |  |
| Nasal | m |  |  | n | ŋ |  |
| Trill |  |  |  | r r̥ |  |  |
| Fricative |  | f v | ð θ | s | x | h |
| Lateral fricative |  |  |  | ɬ |  |  |
| Lateral approximant |  |  |  | l |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [ð] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [v] |  |
| ⟨ff⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ɬ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨r⟩ | [r] |  |
| ⟨rh⟩ | [r̥] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [θ] |  |
| ⟨u⟩ | [ɨ] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [u] |  |
| ⟨y⟩ | [ə] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "wlm")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Middle Low German](gml.md) · [Home](../index.md) · [Minangkabau →](min.md)
