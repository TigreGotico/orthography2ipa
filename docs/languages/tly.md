# Talysh (`tly`)

<!-- atlas:summary begin -->
Talysh is an Iranian language, written in the Latin script. Glottolog places it in Azerbaijan, Iran and Russia. The `tly` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tly` |
| ISO 639-3 | [tly](https://iso639-3.sil.org/code/tly), Talysh |
| Glottolog | [taly1247](https://glottolog.org/resource/languoid/id/taly1247), North-Central Talysh |
| Wikidata | [Q34318](https://www.wikidata.org/wiki/Q34318) |
| Wikipedia | [Talysh language](https://en.wikipedia.org/wiki/Talysh_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Iranian](by-family.md#indo-european--indo-iranian--iranian) |
| Region | [Eurasia](by-region.md#eurasia) > [Azerbaijan](by-region.md#azerbaijan), [Iran](by-region.md#iran), [Russia](by-region.md#russia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Iranian](https://tigregotico.github.io/orthography2ipa/#x-clade-iran1269) `x-clade-iran1269` |
| Explorer | [`tly` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tly) |
| Spec file | [`tly.json`](../../orthography2ipa/data/tly.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Talysh (tolışi), a Northwestern Iranian language of the Caspian littoral in Azerbaijan and Iran. COMMITMENT: this map implements the AZERBAIJANI-BASED TALYSH LATIN ALPHABET (the 'Azerbaijan variant'), the script of the Talysh Wikipedia.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tly.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tly` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-talysh_language_wiki"></a>Wikipedia contributors (2026). *Talysh language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Talysh_language)
2. <a id="src-talysh_alphabet_wiki"></a>Wikipedia contributors (2026). *Talysh alphabet*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Talysh_alphabet)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 39 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q |  |
| Affricate |  |  |  | d͡ʒ t͡ʃ |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ |  | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ | u |
| Near-close | ɪ ʏ |  |  |
| Close-mid | e eː |  | o |
| Mid |  | ə |  |
| Open-mid |  |  | ɔ |
| Near-open | æ |  |  |
| Open | a |  | ɑ ɑː |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [d͡ʒ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] [ɪ] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [ɡ] |  |
| ⟨r⟩ | [r] [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [t͡ʃ] |  |
| ⟨ü⟩ | [ʏ] |  |
| ⟨ğ⟩ | [ɣ] |  |
| ⟨ı⟩ | [ə] [ɨ] |  |
| ⟨ş⟩ | [ʃ] |  |
| ⟨ə⟩ | [a] [æ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tly")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tajik](tg.md) · [Home](../index.md) · [Tamil →](ta.md)
