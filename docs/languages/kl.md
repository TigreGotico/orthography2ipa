# Greenlandic (Kalaallisut) (`kl`)

<!-- atlas:summary begin -->
Greenlandic (Kalaallisut) is an Eskimo-Aleut language, written in the Latin script. Glottolog places it in Denmark and Greenland. The `kl` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kl` |
| ISO 639-3 | [kal](https://iso639-3.sil.org/code/kal), Kalaallisut |
| Glottolog | [kala1399](https://glottolog.org/resource/languoid/id/kala1399), Kalaallisut |
| Wikidata | [Q25355](https://www.wikidata.org/wiki/Q25355) |
| Wikipedia | [Greenlandic language](https://en.wikipedia.org/wiki/Greenlandic_language) |
| Family | [Eskimo-Aleut](by-family.md#eskimo-aleut) |
| Region | [North America](by-region.md#north-america) > [Denmark](by-region.md#denmark), [Greenland](by-region.md#greenland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1721, living |
| Parent | [Eskimo-Aleut](https://tigregotico.github.io/orthography2ipa/#x-clade-eski1264) `x-clade-eski1264` |
| Explorer | [`kl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kl) |
| Spec file | [`kl.json`](../../orthography2ipa/data/kl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kalaallisut (West Greenlandic), the official language of Greenland. The 1973 orthography is essentially phonemic.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1974 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 25 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-fortescue1984"></a>Fortescue, Michael (1984). *West Greenlandic (Croom Helm Descriptive Grammars)*. Croom Helm.
2. <a id="src-rischel1974"></a>Rischel, Jørgen (1974). *Topics in West Greenlandic Phonology*. Akademisk Forlag.
3. <a id="src-greenlandic_wiki"></a>Wikipedia contributors (2024). *Greenlandic language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Greenlandic_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1580 | 0.1765 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 28 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k | q |  |
| Affricate |  |  | tsː |  |  |  |  |
| Nasal | m |  | n |  | ŋ | ɴ |  |
| Fricative |  | f v | s |  | ɣ | ʁ | h |
| Lateral fricative |  |  | ɬː |  |  |  |  |
| Approximant |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Open-mid |  | ɜ | ɔ |
| Open | a |  | ɑ |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ɬː] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [ʁ] |  |
| ⟨rn⟩ | [ɴ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [tsː] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Gorontalo](gor.md) · [Home](../index.md) · [Guadramilese →](ast-PT-x-guadrami.md)
