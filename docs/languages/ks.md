# Kashmiri (`ks`)

<!-- atlas:summary begin -->
Kashmiri is an Indo-Aryan language, written in the Latin script. Glottolog places it in India and Pakistan. The `ks` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ks` |
| ISO 639-3 | [kas](https://iso639-3.sil.org/code/kas), Kashmiri |
| Glottolog | [kash1277](https://glottolog.org/resource/languoid/id/kash1277), Kashmiri |
| Wikidata | [Q33552](https://www.wikidata.org/wiki/Q33552) |
| Wikipedia | [Kashmiri language](https://en.wikipedia.org/wiki/Kashmiri_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india), [Pakistan](by-region.md#pakistan) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Explorer | [`ks` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ks) |
| Spec file | [`ks.json`](../../orthography2ipa/data/ks.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kashmiri (Kāśmīrī), a Dardic language of Jammu & Kashmir. Rich vowel inventory including front rounded and central vowels. Tonal/pitch-accent distinctions reported in some analyses. Three scripts: Sharada (ancient), Nastaliq (modern official), Devanagari (India official).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1991 to 2003. [Sources](#sources) lists them. The spec file writes all 56 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ks.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ks` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-wali_koul1997"></a>Wali, K. & Koul, O.N. (1997). *Kashmiri: A Cognitive-Descriptive Grammar*. Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 49 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  | ts tsʰ | dʒ tʃ tʃʰ |  |  |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |
| Fricative |  |  | s z |  | ʂ | ɕ | x ɣ | h |
| Approximant |  | ʋ |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː ĩ |  | u uː ũ |
| Close-mid | eː ø |  | oː |
| Mid |  | ə əː |  |
| Near-open | æ |  |  |
| Open | a aː ã |  |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨bh⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨ch⟩ | [tʃʰ] |  |
| ⟨d⟩ | [d̪] |  |
| ⟨dh⟩ | [d̪] |  |
| ⟨e⟩ | [eː] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨jh⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t̪] |  |
| ⟨th⟩ | [t̪ʰ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tsh⟩ | [tsʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [ʋ] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ġ⟩ | [ɣ] |  |
| ⟨ĩ⟩ | [ĩ] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨ś⟩ | [ɕ] |  |
| ⟨ũ⟩ | [ũ] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ə⟩ | [ə] |  |
| ⟨ə̄⟩ | [əː] |  |
| ⟨ḍ⟩ | [ɖ] |  |
| ⟨ḍh⟩ | [ɖ] |  |
| ⟨ṅ⟩ | [ŋ] |  |
| ⟨ṇ⟩ | [ɳ] |  |
| ⟨ṛ⟩ | [ɽ] |  |
| ⟨ṣ⟩ | [ʂ] |  |
| ⟨ṭ⟩ | [ʈ] |  |
| ⟨ṭh⟩ | [ʈʰ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ks")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kashmiri](kas.md) · [Home](../index.md) · [Kashubian →](csb.md)
