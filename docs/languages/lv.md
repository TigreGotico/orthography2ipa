# Latvian (`lv`)

<!-- atlas:summary begin -->
Latvian is an Eastern Baltic language, written in the Latin script. Glottolog places it in 5 countries. The `lv` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lv` |
| ISO 639-3 | [lav](https://iso639-3.sil.org/code/lav), Latvian |
| Glottolog | [latv1249](https://glottolog.org/resource/languoid/id/latv1249), Latvian |
| Wikidata | [Q9078](https://www.wikidata.org/wiki/Q9078) |
| Wikipedia | [Latvian language](https://en.wikipedia.org/wiki/Latvian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Eastern Baltic](by-family.md#indo-european--balto-slavic--eastern-baltic) |
| Region | [Eurasia](by-region.md#eurasia) > [Belarus](by-region.md#belarus), [Estonia](by-region.md#estonia), [Latvia](by-region.md#latvia), [Lithuania](by-region.md#lithuania), [Russia](by-region.md#russia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1585, living |
| Parent | [Eastern Baltic](https://tigregotico.github.io/orthography2ipa/#x-clade-east2280) `x-clade-east2280` |
| Explorer | [`lv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lv) |
| Spec file | [`lv.json`](../../orthography2ipa/data/lv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Latvian (Lettish), Baltic language spoken in Latvia. Palatalised consonants marked with cedilla. Long vowels marked with macron. Three tone system (level, falling, broken).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2021 to 2024. [Sources](#sources) lists them. The spec file writes all 33 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wiki-lv"></a>Wikipedia contributors (2024). *Latvian language*.
2. <a id="src-wiki-lv-phon"></a>Wikipedia contributors (2024). *Latvian phonology*.
3. <a id="src-kalnaca_lokmane2021"></a>Kalnača, Andra, Lokmane, Ilze (2021). *Latvian Grammar*. University of Latvia Press (open access). Cited: 20-21. [dspace.lu.lv](https://dspace.lu.lv/dspace/handle/7/54312)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `lv` | gold | lexicon-derived | CC BY 4.0 | 1213 | 0.1901 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c ɟ | k ɡ |
| Affricate |  |  | ts | tʃ |  |  |
| Nasal | m |  | n |  | ɲ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Open-mid | ɛ ɛː |  |
| Open | a aː |  |

Sequences that the spec writes as one unit: [uo].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [uo] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [z] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ē⟩ | [ɛː] |  |
| ⟨ģ⟩ | [ɟ] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ķ⟩ | [c] |  |
| ⟨ļ⟩ | [ʎ] |  |
| ⟨ņ⟩ | [ɲ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ž⟩ | [ʒ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Latgalian](ltg.md) · [Home](../index.md) · [Laz →](lzz.md)
