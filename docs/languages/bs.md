# Bosnian (`bs`)

<!-- atlas:summary begin -->
Bosnian is a Slavic language, written in the Latin script. Glottolog places it in Bosnia & Herzegovina, Croatia, Montenegro and Serbia. The `bs` spec is at the research tier. It cites 5 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bs` |
| Aliases | `bs-Cyrl`, `bs-Cyrl-BA` |
| ISO 639-3 | [bos](https://iso639-3.sil.org/code/bos), Bosnian |
| Glottolog | [bosn1245](https://glottolog.org/resource/languoid/id/bosn1245), Bosnian Standard |
| Wikidata | [Q9303](https://www.wikidata.org/wiki/Q9303) |
| Wikipedia | [Bosnian language](https://en.wikipedia.org/wiki/Bosnian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic](by-family.md#indo-european--balto-slavic--slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Bosnia & Herzegovina](by-region.md#bosnia--herzegovina), [Croatia](by-region.md#croatia), [Montenegro](by-region.md#montenegro), [Serbia](by-region.md#serbia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1850, living |
| Parent | [Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-slav1255) `x-clade-slav1255` |
| Explorer | [`bs` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bs) |
| Spec file | [`bs.json`](../../orthography2ipa/data/bs.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Bosnian (bosanski), Shtokavian standard of the Serbo-Croatian pluricentric language, written in Gaj's Latin alphabet (30 letters, including the digraphs dž, lj, nj which are single letters). Highly phonemic: one letter = one phoneme. ⟨r⟩ may be syllabic between consonants.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 5 works, from 1996 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 60 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bs.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `bs` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 4 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-halilovic1996"></a>Halilović, Senahid (1996). *Pravopis bosanskoga jezika*. Preporod, Sarajevo.
2. <a id="src-scr_phon_wiki"></a>Wikipedia contributors (2025). *Serbo-Croatian phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Serbo-Croatian_phonology)
3. <a id="src-bosnian_wiki"></a>Wikipedia contributors (2025). *Bosnian language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Bosnian_language)
4. <a id="src-icann_lgr_bs_cyrl2026"></a>ICANN (2026). *Reference LGR for language: Bosnian (bs-Cyrl), Version 3*. ICANN. [icann.org](https://www.icann.org/sites/default/files/packages/lgr/lgr-second-level-bosnian-cyrillic-language-13aug26-en.html)
5. <a id="src-cldr_bs_cyrl"></a>Unicode Consortium (2026). *Common Locale Data Repository, locale bs_Cyrl, exemplarCharacters*. Unicode CLDR. [github.com](https://github.com/unicode-org/cldr/blob/main/common/main/bs_Cyrl.xml)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 30 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | ts | dʒ tʃ | dʑ tɕ |  |
| Nasal | m |  | n |  | ɲ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f | s z | ʃ ʒ |  | x |
| Approximant |  | ʋ |  |  | j |  |
| Lateral approximant |  |  | l |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨dž⟩ | [dʒ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lj⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nj⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [ʋ] |  |
| ⟨z⟩ | [z] |  |
| ⟨ć⟩ | [tɕ] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨đ⟩ | [dʑ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [ʋ] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [e] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨ђ⟩ | [dʑ] |  |
| ⟨ј⟩ | [j] |  |
| ⟨љ⟩ | [ʎ] |  |
| ⟨њ⟩ | [ɲ] |  |
| ⟨ћ⟩ | [tɕ] |  |
| ⟨џ⟩ | [dʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bs")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Bodo](brx.md) · [Home](../index.md) · [Bouyei →](pcc.md)
