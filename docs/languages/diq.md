# Zazaki (`diq`)

<!-- atlas:summary begin -->
Zazaki is an Iranian language, written in the Latin script. Glottolog places it in Türkiye. The `diq` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `diq` |
| ISO 639-3 | [diq](https://iso639-3.sil.org/code/diq), Dimli (individual language) |
| Glottolog | [diml1238](https://glottolog.org/resource/languoid/id/diml1238), Dimli |
| Wikidata | [Q10199](https://www.wikidata.org/wiki/Q10199) |
| Wikipedia | [Zaza language](https://en.wikipedia.org/wiki/Zaza_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Iranian](by-family.md#indo-european--indo-iranian--iranian) |
| Region | [Eurasia](by-region.md#eurasia) > [Türkiye](by-region.md#türkiye) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Iranian](https://tigregotico.github.io/orthography2ipa/#x-clade-iran1269) `x-clade-iran1269` |
| Explorer | [`diq` in the data explorer](https://tigregotico.github.io/orthography2ipa/#diq) |
| Spec file | [`diq.json`](../../orthography2ipa/data/diq.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Zazaki (Dimli / Kirmanjki), a Northwestern Iranian language of eastern Anatolia. COMMITMENT: this map implements the 32-letter ZAZA LATIN ALPHABET derived from the Kurdish Hawar (Bedirxan) alphabet, the alphabet used by the Zazaki Wikipedia and by modern Zazaki publishing.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1998 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 34 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/diq.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `diq` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-zaza_language_wiki"></a>Wikipedia contributors (2026). *Zaza language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Zaza_language)
2. <a id="src-paul1998_zazaki"></a>Paul, Ludwig (1998). *Zazaki: Grammatik und Versuch einer Dialektologie*. Reichert, Wiesbaden.
3. <a id="src-todd2008_dimili"></a>Todd, Terry Lynn (2008). *A Grammar of Dimili (also known as Zaza)*. Iremet Förlag, Stockholm.
4. <a id="src-kurdish_alphabets_wiki"></a>Wikipedia contributors (2026). *Kurdish alphabets*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kurdish_alphabets)
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
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ |  | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l ɫ |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Near-close | ɪ |  | ʊ |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Open | a |  | ɑ ɑ̃ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [d͡ʒ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [ɾ] [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [t͡ʃ] |  |
| ⟨ê⟩ | [e] |  |
| ⟨î⟩ | [i] |  |
| ⟨û⟩ | [u] |  |
| ⟨ğ⟩ | [ɣ] |  |
| ⟨ı⟩ | [ɪ] |  |
| ⟨ş⟩ | [ʃ] |  |
| ⟨ẍ⟩ | [ɣ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "diq")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Zaza](zza.md) · [Home](../index.md) · [Zhuang →](za.md)
