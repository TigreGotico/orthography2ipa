# Azerbaijani (`az`)

<!-- atlas:summary begin -->
Azerbaijani is a Turkic language, written in the Latin script. Glottolog places it in 6 countries. The `az` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `az` |
| ISO 639-3 | [aze](https://iso639-3.sil.org/code/aze), Azerbaijani |
| Glottolog | [nort2697](https://glottolog.org/resource/languoid/id/nort2697), North Azerbaijani |
| Wikidata | [Q9292](https://www.wikidata.org/wiki/Q9292) |
| Wikipedia | [Azerbaijani language](https://en.wikipedia.org/wiki/Azerbaijani_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Armenia](by-region.md#armenia), [Azerbaijan](by-region.md#azerbaijan), [Georgia](by-region.md#georgia), [Iran](by-region.md#iran), [Russia](by-region.md#russia), [Türkiye](by-region.md#türkiye) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1991, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`az` in the data explorer](https://tigregotico.github.io/orthography2ipa/#az) |
| Spec file | [`az.json`](../../orthography2ipa/data/az.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> North Azerbaijani (Latin-script official orthography since 1991). 9-vowel system including front unrounded /æ/ (ə) and back unrounded /ɯ/ (ı). Vowel harmony similar to Turkish. Final devoicing: b→p, c→ç, d→t, g→k.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1997 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/az.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `az` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL.

1. <a id="src-azerbaijani_phonology_wiki"></a>Wikipedia contributors (2024). *Azerbaijani phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Azerbaijani_phonology)
2. <a id="src-comrie1997"></a>Comrie, B. (1997). *The World's Major Languages*. Oxford University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `az` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 434 | 0.2440 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l ɫ |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Near-open | æ |  |
| Open | a |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [dʒ] | default [dʒ] · word final [tʃ] |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] · word final [k] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [ɡ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [tʃ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |
| ⟨ğ⟩ | [ɣ] |  |
| ⟨ı⟩ | [ɯ] |  |
| ⟨ş⟩ | [ʃ] |  |
| ⟨ə⟩ | [æ] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "az")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ayacucho Quechua](quy.md) · [Home](../index.md) · [Bahnar →](bdq.md)
