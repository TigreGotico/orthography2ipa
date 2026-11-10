# Kabardian (`kbd`)

<!-- atlas:summary begin -->
Kabardian is an Abkhaz-Adyge language, written in the Cyrillic script. Glottolog places it in Russia and Türkiye. The `kbd` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kbd` |
| ISO 639-3 | [kbd](https://iso639-3.sil.org/code/kbd), Kabardian |
| Glottolog | [kaba1278](https://glottolog.org/resource/languoid/id/kaba1278), Kabardian |
| Wikidata | [Q33522](https://www.wikidata.org/wiki/Q33522) |
| Wikipedia | [Kabardian language](https://en.wikipedia.org/wiki/Kabardian_language) |
| Family | [Abkhaz-Adyge](by-family.md#abkhaz-adyge) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia), [Türkiye](by-region.md#türkiye) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1924, living |
| Parent | [Abkhaz-Adyge](https://tigregotico.github.io/orthography2ipa/#x-clade-abkh1242) `x-clade-abkh1242` |
| Explorer | [`kbd` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kbd) |
| Spec file | [`kbd.json`](../../orthography2ipa/data/kbd.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kabardian (къэбэрдей адыгэбзэ, East Circassian), Northwest Caucasian, written in a Cyrillic alphabet since 1936 (Latin and Arabic orthographies are historical/diaspora and are not modelled).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1992 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 57 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kbd.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kbd` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kabardian_wiki"></a>Wikipedia contributors (2024). *Kabardian language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kabardian_language)
2. <a id="src-colarusso1992"></a>Colarusso, John (1992). *A Grammar of the Kabardian Language*. University of Calgary Press.
3. <a id="src-kabardian_alphabet_wiki_table"></a>Wikipedia contributors (2026). *Kabardian language, Cyrillic alphabet table*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kabardian_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 59 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  | d t tʼ |  |  | k kʲʼ kʷ kʷʼ ɡʷ | q qʷ |  | ʔ ʔʷ |
| Affricate |  |  | d͡z t͡s t͡sʼ | d͡ʒ t͡ʃ t͡ʃʼ |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative |  | f fʼ v | s z | ʃ ʒ | ɕ ɕʼ ʑ | x xʷ ɣ | ʁ ʁʷ χ χʷ | ħ |  |
| Lateral fricative |  |  | ɬ ɬʼ ɮ |  |  |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central |
|:--|:-:|:-:|
| Mid |  | ə |
| Open | a aː |  |

Sequences that the spec writes as one unit: [aw] [ja] [jaː] [jo] [ju] [jə] [q͡χ] [q͡χʷ] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɣ] |  |
| ⟨гу⟩ | [ɡʷ] |  |
| ⟨гъ⟩ | [ʁ] |  |
| ⟨гъу⟩ | [ʁʷ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дж⟩ | [d͡ʒ] |  |
| ⟨дз⟩ | [d͡z] |  |
| ⟨е⟩ | [ja] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨жь⟩ | [ʑ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [jə] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨ку⟩ | [kʷ] |  |
| ⟨кхъ⟩ | [q͡χ] |  |
| ⟨кхъу⟩ | [q͡χʷ] |  |
| ⟨къ⟩ | [q] |  |
| ⟨къу⟩ | [qʷ] |  |
| ⟨кӏ⟩ | [t͡ʃʼ] [kʲʼ] |  |
| ⟨кӏу⟩ | [kʷʼ] |  |
| ⟨л⟩ | [ɮ] [l] |  |
| ⟨лъ⟩ | [ɬ] |  |
| ⟨лӏ⟩ | [ɬʼ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [aw] |  |
| ⟨п⟩ | [p] |  |
| ⟨пӏ⟩ | [pʼ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨тӏ⟩ | [tʼ] |  |
| ⟨у⟩ | [w] |  |
| ⟨ф⟩ | [f] |  |
| ⟨фӏ⟩ | [fʼ] |  |
| ⟨х⟩ | [x] |  |
| ⟨ху⟩ | [xʷ] |  |
| ⟨хъ⟩ | [χ] |  |
| ⟨хъу⟩ | [χʷ] |  |
| ⟨хь⟩ | [ħ] |  |
| ⟨ц⟩ | [t͡s] |  |
| ⟨цӏ⟩ | [t͡sʼ] |  |
| ⟨ч⟩ | [t͡ʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨щӏ⟩ | [ɕʼ] |  |
| ⟨ы⟩ | [ə] |  |
| ⟨э⟩ | [a] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [jaː] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ӏ⟩ | [ʔ] |  |
| ⟨ӏу⟩ | [ʔʷ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kbd")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Juǀʼhoan](ktz.md) · [Home](../index.md) · [Kabiye →](kbp.md)
