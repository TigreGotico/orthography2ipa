# Northern Sami (`se`)

<!-- atlas:summary begin -->
Northern Sami is a Saami language, written in the Latin script. Glottolog places it in Finland, Norway, Russia and Sweden. The `se` spec is at the research tier. It cites 1 source and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `se` |
| ISO 639-3 | [sme](https://iso639-3.sil.org/code/sme), Northern Sami |
| Glottolog | [nort2671](https://glottolog.org/resource/languoid/id/nort2671), North Saami |
| Wikidata | [Q33947](https://www.wikidata.org/wiki/Q33947) |
| Wikipedia | [Northern Sami](https://en.wikipedia.org/wiki/Northern_Sami) |
| Family | [Uralic](by-family.md#uralic) > [Saami](by-family.md#uralic--saami) |
| Region | [Eurasia](by-region.md#eurasia) > [Finland](by-region.md#finland), [Norway](by-region.md#norway), [Russia](by-region.md#russia), [Sweden](by-region.md#sweden) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1600, living |
| Parent | [Saami](https://tigregotico.github.io/orthography2ipa/#x-clade-saam1281) `x-clade-saam1281` |
| Explorer | [`se` in the data explorer](https://tigregotico.github.io/orthography2ipa/#se) |
| Spec file | [`se.json`](../../orthography2ipa/data/se.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Northern Sami, largest Sami language spoken in Norway, Sweden and Finland. Sami alphabets include several extended characters: č /tʃ/, đ /ð/, ŋ /ŋ/, š /ʃ/, ž /ʒ/, ŧ /θ/. Consonant gradation system similar to Finnish. Polysynthetic morphology.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2024. [Sources](#sources) lists them. The spec file writes all 29 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/se.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `se` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 0 of them have a DOI or a URL.

1. <a id="src-wiki-se"></a>Wikipedia contributors (2024). *Northern Sami*.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `se` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4125 | 0.2749 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 29 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dz ts | tʃ |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Fricative |  | f v | ð θ | s | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a aː |  |
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
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [dz] |  |
| ⟨á⟩ | [aː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨đ⟩ | [ð] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ŧ⟩ | [θ] |  |
| ⟨ž⟩ | [ʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "se")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Northern Russian](ru-x-northern.md) · [Home](../index.md) · [Northern Sotho →](nso.md)
