# Sassarese Sardinian (`sdc`)

<!-- atlas:summary begin -->
Sassarese Sardinian is a Romance language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `sdc` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sdc` |
| ISO 639-3 | [sdc](https://iso639-3.sil.org/code/sdc), Sassarese Sardinian |
| Wikipedia | [Sassarese language](https://en.wikipedia.org/wiki/Sassarese_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance](by-family.md#indo-european--italic--romance) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Ancestor | [Italo-Romance Vulgar Latin](https://tigregotico.github.io/orthography2ipa/#la-x-italia) `la-x-italia` |
| Explorer | [`sdc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sdc) |
| Spec file | [`sdc.json`](../../orthography2ipa/data/sdc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Romance variety of northern Sardinia (transitional Sardo-Corsican) written in the Latin alphabet. Grapheme map follows Italian-based conventions with Sassarese specifics: the retroflex ddh/dd [ɖ], ch/gh for plain velars, gn [ɲ], sc [ʃ] and the affricate readings of c/g before front vowels.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1999 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sdc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sdc` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sdc_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Sassarese Sardinian (sass1235)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/sass1235)
2. <a id="src-sdc_wikipedia"></a>Wikipedia contributors (2024). *Sassarese language (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Sassarese_language)
3. <a id="src-sdc_bazzoni1999"></a>Bazzoni, Gian Paolo (1999). *Elementi di grammatica sassarese*. Self-published/regional imprint.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sdc` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 321 | 0.1865 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 25 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | ɖ |  | k ɡ |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  | ɲ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s | ʃ |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [tʃe].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] |  |
| ⟨ce⟩ | [tʃe] |  |
| ⟨ch⟩ | [k] |  |
| ⟨ci⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [ɖ] |  |
| ⟨ddh⟩ | [ɖ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gi⟩ | [dʒ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sc⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [ts] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sdc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sasak](sas.md) · [Home](../index.md) · [Saterland Frisian →](stq.md)
