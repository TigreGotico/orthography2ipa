# Estonian (`et`)

<!-- atlas:summary begin -->
Estonian is a Finnic language, written in the Latin script. Glottolog places it in Estonia, Latvia and Russia. The `et` spec is at the research tier. It cites 1 source and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `et` |
| ISO 639-3 | [est](https://iso639-3.sil.org/code/est), Estonian |
| Glottolog | [esto1258](https://glottolog.org/resource/languoid/id/esto1258), Estonian |
| Wikidata | [Q9072](https://www.wikidata.org/wiki/Q9072) |
| Wikipedia | [Estonian language](https://en.wikipedia.org/wiki/Estonian_language) |
| Family | [Uralic](by-family.md#uralic) > [Finnic](by-family.md#uralic--finnic) |
| Region | [Eurasia](by-region.md#eurasia) > [Estonia](by-region.md#estonia), [Latvia](by-region.md#latvia), [Russia](by-region.md#russia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1525, living |
| Parent | [Finnic](https://tigregotico.github.io/orthography2ipa/#x-clade-finn1317) `x-clade-finn1317` |
| Explorer | [`et` in the data explorer](https://tigregotico.github.io/orthography2ipa/#et) |
| Spec file | [`et.json`](../../orthography2ipa/data/et.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Estonian, Finnic language with three phonemic quantity degrees (short, long, overlong). Loanword consonants b, d, g are phonemically lenis (partially voiced). Vowel õ /ɤ/ is typologically unusual. No grammatical gender.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2009. [Sources](#sources) lists them. The spec file writes all 27 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/et.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `et` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-asu_teras2009"></a>Asu, Eva Liina & Teras, Pire (2009). *Estonian*. Journal of the International Phonetic Association 39(3), 367-372. Cited: 367-372. [doi.org](https://doi.org/10.1017/S002510030999017X)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `et` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2763 | 0.1587 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `et` | generated | espeak-derived | CC BY 4.0 | 11040 | 0.2769 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `et` | generated | epitran-derived | CC0 1.0 | 35140 | 0.2121 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e ø | o ɤ |
| Near-open | æ |  |
| Open |  | ɑ |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [p] [b] |  |
| ⟨d⟩ | [t] [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [k] [ɡ] |  |
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
| ⟨z⟩ | [z] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨õ⟩ | [ɤ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "et")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Esperanto](eo.md) · [Home](../index.md) · [Etruscan →](ett.md)
