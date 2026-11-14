# Khiamniungan Naga (`kix`)

<!-- atlas:summary begin -->
Khiamniungan Naga is a Sino-Tibetan language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `kix` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kix` |
| ISO 639-3 | [kix](https://iso639-3.sil.org/code/kix), Khiamniungan Naga |
| Wikipedia | [Khiamniungan Naga language](https://en.wikipedia.org/wiki/Khiamniungan_Naga_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Sino-Tibetan (family node)](https://tigregotico.github.io/orthography2ipa/#sit) `sit` |
| Explorer | [`kix` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kix) |
| Spec file | [`kix.json`](../../orthography2ipa/data/kix.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Patsho Khiamniungan in the Latin practical orthography. Tone is written.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2023 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 60 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kix.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kix` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-thaam_kevichusa_ezung_2023"></a>Thaam, Keen, Kevichüsa-Ezung, Mimi (2023). *Phonology of Khiamniungan*. वाक् मंथन (SEL India), Vol. 9, Issue II. Cited: 39-47. [selindia.org](https://selindia.org/wp-content/uploads/2024/08/04_Phonology-of-Khiamniungan.pdf)
2. <a id="src-wiktionary_kix"></a>Wiktionary contributors (2026). *Khiamniungan Naga entries and entry guidelines*. Wiktionary. [en.wikipedia.org](https://en.wikipedia.org/wiki/Khiamniungan_Naga_language)
3. <a id="src-khiamniungan_glottolog"></a>Glottolog (2023). *Khiamniungan Naga (khia1237)*. Max Planck Institute for Evolutionary Anthropology.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kix` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4240 | 0.0788 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | t tʰ |  |  | k kʰ | ʔ |
| Affricate |  |  | ts tsʰ | tʃ tʃʰ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | v | s | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Near-close | ɪ |  | ʊ |
| Close-mid |  |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [a³³] [a³¹] [a⁵²] [a⁵⁵] [i³³] [i³¹] [i⁵²] [i⁵⁵] [o³³] [o³¹] [o⁵²] [o⁵⁵] [u³³] [u³¹] [u⁵²] [u⁵⁵] [w] [ə³³] [ə³¹] [ə⁵⁵] [ɛ³³] [ɛ³¹] [ɛ⁵²] [ɛ⁵⁵].

Tones: [⁵⁵] high level, [³³] mid level, [³¹] low; written 31 in the Patsho transcriptions, described as low level for Thang, [⁵²] falling.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [p] |  |
| ⟨ch⟩ | [tʃʰ] |  |
| ⟨d⟩ | [t] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨g⟩ | [k] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨j⟩ | [tʃ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tsh⟩ | [tsʰ] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨à⟩ | [a³¹] |  |
| ⟨á⟩ | [a⁵⁵] |  |
| ⟨â⟩ | [a⁵²] |  |
| ⟨è⟩ | [ɛ³¹] |  |
| ⟨é⟩ | [ɛ⁵⁵] |  |
| ⟨ê⟩ | [ɛ⁵²] |  |
| ⟨ì⟩ | [i³¹] |  |
| ⟨í⟩ | [i⁵⁵] |  |
| ⟨î⟩ | [i⁵²] |  |
| ⟨ò⟩ | [o³¹] |  |
| ⟨ó⟩ | [o⁵⁵] |  |
| ⟨ô⟩ | [o⁵²] |  |
| ⟨ù⟩ | [u³¹] |  |
| ⟨ú⟩ | [u⁵⁵] |  |
| ⟨û⟩ | [u⁵²] |  |
| ⟨ü⟩ | [ə] |  |
| ⟨ā⟩ | [a³³] |  |
| ⟨ē⟩ | [ɛ³³] |  |
| ⟨ě⟩ | [ɛ] |  |
| ⟨ī⟩ | [i³³] |  |
| ⟨ō⟩ | [o³³] |  |
| ⟨ū⟩ | [u³³] |  |
| ⟨ǎ⟩ | [a] |  |
| ⟨ǐ⟩ | [i] |  |
| ⟨ǒ⟩ | [o] |  |
| ⟨ǔ⟩ | [u] |  |
| ⟨ǖ⟩ | [ə³³] |  |
| ⟨ǘ⟩ | [ə⁵⁵] |  |
| ⟨ǚ⟩ | [ə] |  |
| ⟨ǜ⟩ | [ə³¹] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 1 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `kix_coda_h_glottal` | /h/ → [ʔ], in the coda | ⟨tsah⟩ [ʦʌ̌ʔ] | [Thaam 2023](#src-thaam_kevichusa_ezung_2023) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kix")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Khasi](kha.md) · [Home](../index.md) · [Khmer →](km.md)
