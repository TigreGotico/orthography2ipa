# Senhaja de Srair (Berber) (`sjs`)

<!-- atlas:summary begin -->
Senhaja de Srair (Berber) is a Berber language, written in the Latin script. Glottolog places it in the Africa macroarea. The `sjs` spec is at the research tier. It cites 1 source and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sjs` |
| ISO 639-3 | [sjs](https://iso639-3.sil.org/code/sjs), Senhaja De Srair |
| Wikipedia | [Senhaja de Srair Berber](https://en.wikipedia.org/wiki/Senhaja_de_Srair_Berber) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Berber](by-family.md#afro-asiatic--berber) |
| Region | [Africa](by-region.md#africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Ancestor | [Berber (Proto-Berber / Common Tamazight)](https://tigregotico.github.io/orthography2ipa/#ber) `ber` |
| Explorer | [`sjs` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sjs) |
| Spec file | [`sjs.json`](../../orthography2ipa/data/sjs.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Senhaja de Srair (a Northern/Rif Berber variety of Morocco), in Berber-Latin notation with pharyngeals ⟨ḥ ɛ⟩, emphatics ⟨ḍ ṣ ṭ ẓ ṛ⟩ and ⟨ǧ⟩=/dʒ/. Strong Moroccan Arabic adstrate.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2013. [Sources](#sources) lists them. The spec file writes all 34 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sjs.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sjs` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kossmann2013"></a>Kossmann, Maarten (2013). *The Arabic Influence on Northern Berber*. Brill.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sjs` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 845 | 0.0467 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b |  | d dˤ t tˤ |  |  | k ɡ | q |  |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r rˤ |  |  |  |  |  |  |
| Fricative |  | f | s sˤ z zˤ | ʃ ʒ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid |  |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ə] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ǧ⟩ | [dʒ] |  |
| ⟨ɛ⟩ | [ʕ] |  |
| ⟨ɣ⟩ | [ɣ] |  |
| ⟨ḍ⟩ | [dˤ] |  |
| ⟨ḥ⟩ | [ħ] |  |
| ⟨ṛ⟩ | [rˤ] |  |
| ⟨ṣ⟩ | [sˤ] |  |
| ⟨ṭ⟩ | [tˤ] |  |
| ⟨ẓ⟩ | [zˤ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sjs")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Seneca](see.md) · [Home](../index.md) · [Serbian →](sr.md)
