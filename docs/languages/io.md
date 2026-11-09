# Ido (`io`)

<!-- atlas:summary begin -->
Ido is a Constructed language, written in the Latin script. Glottolog places it in France. The `io` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `io` |
| ISO 639-3 | [ido](https://iso639-3.sil.org/code/ido), Ido |
| Glottolog | [idoo1234](https://glottolog.org/resource/languoid/id/idoo1234), Ido |
| Wikidata | [Q35224](https://www.wikidata.org/wiki/Q35224) |
| Wikipedia | [Ido](https://en.wikipedia.org/wiki/Ido) |
| Family | [Constructed](by-family.md#constructed) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1907, living |
| Explorer | [`io` in the data explorer](https://tigregotico.github.io/orthography2ipa/#io) |
| Spec file | [`io.json`](../../orthography2ipa/data/io.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ido (1907, reformed Esperanto). Uses the plain 26-letter Latin alphabet with no diacritics: ⟨c⟩ = /ts/, ⟨ch⟩ = /tʃ/, ⟨sh⟩ = /ʃ/, ⟨j⟩ = /ʒ/ (~/dʒ/), ⟨qu⟩ = /kw/ (~/kv/), ⟨x⟩ = /ks/ (~/ɡz/), ⟨y⟩ = /j/, ⟨w⟩ = /w/. Stress is on the penultimate syllable, except verb infinitives, which are stressed on the final syllable.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1925 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 29 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/io.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `io` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-beaufront1925"></a>de Beaufront, Louis (1925). *Kompleta Gramatiko Detaloza di la Linguo Internaciona Ido*. Uniono por la Linguo Internaciona.
2. <a id="src-ido_wiki"></a>Wikipedia contributors (2024). *Ido*. Wikipedia. Cited: Alphabet/IPA table and stress rule. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ido)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `io` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 6815 | 0.0974 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [ks] [kv] [kw] [w] [ɡz].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
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
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

Stress falls on the penult by default. These endings take final stress: ⟨-ar⟩ ⟨-ir⟩ ⟨-or⟩.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "io")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Icelandic](is.md) · [Home](../index.md) · [Ifanês →](mwl-x-ifanes.md)
