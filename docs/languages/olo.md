# Livvi-Karelian (`olo`)

<!-- atlas:summary begin -->
Livvi-Karelian is an Uralic language, written in the Latin script. Glottolog places it in Finland and Russia. The `olo` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `olo` |
| ISO 639-3 | [olo](https://iso639-3.sil.org/code/olo), Livvi |
| Glottolog | [livv1243](https://glottolog.org/resource/languoid/id/livv1243), Livvi |
| Wikidata | [Q36584](https://www.wikidata.org/wiki/Q36584) |
| Wikipedia | [Livvi-Karelian language](https://en.wikipedia.org/wiki/Livvi-Karelian_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Finland](by-region.md#finland), [Russia](by-region.md#russia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Uralic (family node)](https://tigregotico.github.io/orthography2ipa/#urj) `urj` |
| Explorer | [`olo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#olo) |
| Spec file | [`olo.json`](../../orthography2ipa/data/olo.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Livvi-Karelian (livvinkarjala / Olonets Karelian), Republic of Karelia (Russia). Written in the Latin-based Karelian alphabet (2007 unified norm, <ü> was replaced by <y>). Values follow the Finnic convention: <a>=/ɑ/, <ä>=/æ/, <ö>=/ø/, <y>=/y/, <c>=/ts/, <č>=/tʃ/, <š>=/ʃ/, <ž>=/ʒ/, <v>=/ʋ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2002 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 28 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/olo.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `olo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-markianova2002"></a>Markianova, Ljudmila (2002). *Livvin karjalan kielioppi (Karelian grammar)*. Periodika, Petrozavodsk.
2. <a id="src-livvi_wiki"></a>Wikipedia contributors (2024). *Livvi-Karelian language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Livvi-Karelian_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `olo` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 278 | 0.0801 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d dʲ t tʲ |  |  | k ɡ |  |  |
| Affricate |  |  | ts | tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ |  | x | χ | h |
| Approximant |  | ʋ |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e ø | o |
| Near-open | æ |  |
| Open |  | ɑ |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
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
| ⟨v⟩ | [ʋ] |  |
| ⟨y⟩ | [y] |  |
| ⟨z⟩ | [z] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "olo")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Livonian](liv.md) · [Home](../index.md) · [Logudorese Sardinian →](src.md)
