# Tokelau (`tkl`)

<!-- atlas:summary begin -->
Tokelau is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in the Africa, Eurasia, Papunesia and South America macroareas. The `tkl` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tkl` |
| ISO 639-3 | [tkl](https://iso639-3.sil.org/code/tkl), Tokelau |
| Wikipedia | [Tokelauan language](https://en.wikipedia.org/wiki/Tokelauan_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Africa](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`tkl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tkl) |
| Spec file | [`tkl.json`](../../orthography2ipa/data/tkl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Tokelauan is a Polynesian (Nuclear Polynesian, Samoic-Ellicean) Austronesian language of Tokelau, written in a Latin alphabet on the Samoan pattern.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 20 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tkl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tkl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-tkl_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Tokelau (toke1240)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/toke1240)
2. <a id="src-tkl_wikipedia"></a>Wikipedia contributors (2024). *Tokelauan language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Tokelauan_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `tkl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 340 | 0.0497 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 20 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t | k |  |
| Nasal | m |  | n | ŋ |  |
| Fricative |  | f v |  |  | h |
| Lateral approximant |  |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ŋ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨ū⟩ | [uː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tkl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tok Pisin](tpi.md) · [Home](../index.md) · [Toki Pona →](tok.md)
