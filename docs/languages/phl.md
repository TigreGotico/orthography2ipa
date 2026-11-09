# Phalura (`phl`)

<!-- atlas:summary begin -->
Phalura is an Indo-Iranian language, written in the Latin script. Glottolog places it in the Eurasia, Papunesia and South America macroareas. The `phl` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `phl` |
| ISO 639-3 | [phl](https://iso639-3.sil.org/code/phl), Phalura |
| Wikipedia | [Phalura language](https://en.wikipedia.org/wiki/Phalura_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian](by-family.md#indo-european--indo-iranian) |
| Region | [Eurasia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Ancestor | [Proto-Indo-Iranian](https://tigregotico.github.io/orthography2ipa/#iir) `iir` |
| Explorer | [`phl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#phl) |
| Spec file | [`phl.json`](../../orthography2ipa/data/phl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Phalura/Palula (Dardic, Indo-Aryan, Chitral, Pakistan) in Palula common transcription (PCT), the indological-style Latin transcription used by Liljegren and other Shina-variety scholars (Liljegren 2016, ch. 1.8) -- not the community's Arabic-based practical orthography, which this spec does not cover.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2008 to 2016. [Sources](#sources) lists them. The spec file writes all 55 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/phl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `phl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-liljegren2008"></a>Liljegren, Henrik (2008). *Towards a grammatical description of Palula: An Indo-Aryan language of the Hindu Kush*. Stockholm University.
2. <a id="src-liljegren2016"></a>Liljegren, Henrik (2016). *A Grammar of Palula*. Language Science Press. [langsci-press.org](https://langsci-press.org/catalog/book/82)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `phl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2173 | 0.2660 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 50 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʰ p pʰ |  | d dʰ t tʰ |  | ɖ ʈ |  | k kʰ ɡ ɡʰ | q |  |
| Affricate |  |  |  | dʒ dʒʰ tʃ tʃʰ | ʈʂ | tɕ |  |  |  |
| Nasal | m |  | n |  | ɳ |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |  |
| Fricative |  | f | s z |  | ʂ ʐ | ɕ ʑ | x ɣ |  | h |
| Approximant |  |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː ã |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨bh⟩ | [bʰ] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨ch⟩ | [tʃʰ] |  |
| ⟨c̣⟩ | [ʈʂ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [dʰ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡʰ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨jh⟩ | [dʒʰ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨á⟩ | [a] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ú⟩ | [u] |  |
| ⟨č⟩ | [tɕ] |  |
| ⟨š⟩ | [ɕ] |  |
| ⟨ǰ⟩ | [ʑ] |  |
| ⟨ɣ⟩ | [ɣ] |  |
| ⟨ḍ⟩ | [ɖ] |  |
| ⟨ṇ⟩ | [ɳ] |  |
| ⟨ṛ⟩ | [ɽ] |  |
| ⟨ṣ⟩ | [ʂ] |  |
| ⟨ṭ⟩ | [ʈ] |  |
| ⟨ẓ⟩ | [ʐ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "phl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Persian](fa.md) · [Home](../index.md) · [Picard →](pcd.md)
