# Livonian (`liv`)

<!-- atlas:summary begin -->
Livonian is an Uralic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `liv` spec is at the research tier. It cites 2 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `liv` |
| ISO 639-3 | [liv](https://iso639-3.sil.org/code/liv), Liv |
| Wikipedia | [Livonian language](https://en.wikipedia.org/wiki/Livonian_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Uralic (family node)](https://tigregotico.github.io/orthography2ipa/#urj) `urj` |
| Explorer | [`liv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#liv) |
| Spec file | [`liv.json`](../../orthography2ipa/data/liv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Livonian (Finnic, Uralic, last L1 speaker died 2013, now revitalised).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2002 to 2012. [Sources](#sources) lists them. The spec file writes all 40 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/liv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `liv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-viitso_ernstreits2012"></a>Viitso, Tiit-Rein & Ernštreits, Valts (2012). *Līvõkīel-ēstikīel-lețkīel sõnārōntõz (Livonian-Estonian-Latvian Dictionary)*. University of Tartu / Latviešu valodas aģentūra.
2. <a id="src-moseley2002"></a>Moseley, Christopher (2002). *Livonian (Languages of the World/Materials 349)*. Lincom Europa.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `liv` | gold | lexicon-derived | CC BY 4.0 | 1042 | 0.0752 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `liv` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2480 | 0.1173 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 40 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d dʲ t tʲ |  |  | k ɡ | ʔ |
| Affricate |  |  |  | tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ |  |  |
| Trill |  |  | r rʲ |  |  |  |  |
| Fricative |  | f v | s | ʃ ʒ |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ | u uː |
| Near-close |  |  | ʊ ʊː |
| Close-mid | e eː |  | o oː |
| Mid |  | ə |  |
| Open-mid |  |  | ɔː |
| Near-open | æ æː |  |  |
| Open |  |  | ɑ ɑː |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨õ⟩ | [ɨ] [ə] | word final [ə] |
| ⟨ā⟩ | [ɑː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ļ⟩ | [ʎ] |  |
| ⟨ņ⟩ | [ɲ] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨ŗ⟩ | [rʲ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ž⟩ | [ʒ] |  |
| ⟨ǟ⟩ | [æː] |  |
| ⟨ǭ⟩ | [ɔː] |  |
| ⟨ț⟩ | [tʲ] |  |
| ⟨ȯ⟩ | [ʊ] |  |
| ⟨ȱ⟩ | [ʊː] |  |
| ⟨ḑ⟩ | [dʲ] |  |
| ⟨’⟩ | [ʔ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "liv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lithuanian](lt.md) · [Home](../index.md) · [Livvi-Karelian →](olo.md)
