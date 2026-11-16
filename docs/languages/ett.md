# Etruscan (`ett`)

<!-- atlas:summary begin -->
Etruscan is a Tyrsenian language, written in the Old Italic script. The `ett` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ett` |
| ISO 639-3 | [ett](https://iso639-3.sil.org/code/ett), Etruscan |
| Wikipedia | [Etruscan language](https://en.wikipedia.org/wiki/Etruscan_language) |
| Family | [Tyrsenian](by-family.md#tyrsenian) |
| Script | [Old Italic](by-script.md#old-italic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Tyrsenian](https://tigregotico.github.io/orthography2ipa/#x-clade-tyrsen) `x-clade-tyrsen` |
| Explorer | [`ett` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ett) |
| Spec file | [`ett.json`](../../orthography2ipa/data/ett.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Extinct, non-Indo-European (Tyrsenian) language of ancient Italy written in the Old Italic (Etruscan) alphabet.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 26 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ett.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ett` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ett_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Etruscan (etru1241)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/etru1241)
2. <a id="src-ett_wikipedia"></a>Wikipedia contributors (2024). *Etruscan language (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Etruscan_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ett` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 207 | 0.1444 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 24 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  | k kʰ |  |
| Affricate |  |  | ts |  |  |  |
| Nasal | m |  | n |  |  |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f | s | ʃ |  | h |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [ks] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨𐌀⟩ | [a] |  |
| ⟨𐌁⟩ | [b] |  |
| ⟨𐌂⟩ | [k] |  |
| ⟨𐌃⟩ | [d] |  |
| ⟨𐌄⟩ | [e] |  |
| ⟨𐌅⟩ | [w] |  |
| ⟨𐌆⟩ | [ts] |  |
| ⟨𐌇⟩ | [h] |  |
| ⟨𐌈⟩ | [tʰ] |  |
| ⟨𐌉⟩ | [i] |  |
| ⟨𐌊⟩ | [k] |  |
| ⟨𐌋⟩ | [l] |  |
| ⟨𐌌⟩ | [m] |  |
| ⟨𐌍⟩ | [n] |  |
| ⟨𐌏⟩ | [o] |  |
| ⟨𐌐⟩ | [p] |  |
| ⟨𐌑⟩ | [ʃ] |  |
| ⟨𐌒⟩ | [k] |  |
| ⟨𐌓⟩ | [r] |  |
| ⟨𐌔⟩ | [s] |  |
| ⟨𐌕⟩ | [t] |  |
| ⟨𐌖⟩ | [u] |  |
| ⟨𐌗⟩ | [ks] |  |
| ⟨𐌘⟩ | [pʰ] |  |
| ⟨𐌙⟩ | [kʰ] |  |
| ⟨𐌚⟩ | [f] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ett")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Estonian](et.md) · [Home](../index.md) · [Evenki →](evn.md)
