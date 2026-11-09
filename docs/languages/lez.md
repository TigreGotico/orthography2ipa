# Lezgian (`lez`)

<!-- atlas:summary begin -->
Lezgian is a Nakh-Daghestanian language, written in the Cyrillic script. Glottolog places it in 5 countries. The `lez` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lez` |
| ISO 639-3 | [lez](https://iso639-3.sil.org/code/lez), Lezghian |
| Glottolog | [lezg1247](https://glottolog.org/resource/languoid/id/lezg1247), Lezgian |
| Wikidata | [Q31746](https://www.wikidata.org/wiki/Q31746) |
| Wikipedia | [Lezgian language](https://en.wikipedia.org/wiki/Lezgian_language) |
| Family | [Nakh-Daghestanian](by-family.md#nakh-daghestanian) |
| Region | [Eurasia](by-region.md#eurasia) > [Azerbaijan](by-region.md#azerbaijan), [Georgia](by-region.md#georgia), [Kazakhstan](by-region.md#kazakhstan), [Russia](by-region.md#russia), [Ukraine](by-region.md#ukraine) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nakh-Daghestanian](https://tigregotico.github.io/orthography2ipa/#x-clade-nakh1245) `x-clade-nakh1245` |
| Explorer | [`lez` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lez) |
| Spec file | [`lez.json`](../../orthography2ipa/data/lez.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lezgian (лезги чӏал) of Dagestan and Azerbaijan, written in a Cyrillic alphabet since 1938 (41 letters).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1993 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 43 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lez.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lez` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-lez_wiki"></a>Wikipedia contributors (2024). *Lezgian language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lezgian_language)
2. <a id="src-lezgin_alphabets_wiki"></a>Wikipedia contributors (2026). *Lezgin alphabets, comparative table of Arabic / Latin / Cyrillic / IPA*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lezgin_alphabets)
3. <a id="src-haspelmath1993"></a>Haspelmath, Martin (1993). *A Grammar of Lezgian*. Mouton de Gruyter (Mouton Grammar Library 9).
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `lez` | gold | lexicon-derived | CC BY 4.0 | 969 | 0.1329 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 50 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ pʼ |  | d t tʰ tʼ |  |  | k kʰ kʼ ɡ | q qʰ qʼ | ʔ |
| Affricate |  |  | t͡s t͡sʰ t͡sʼ | t͡ʃ t͡ʃʰ t͡ʃʼ |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Near-open | æ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨гъ⟩ | [ʁ] |  |
| ⟨гь⟩ | [h] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [e] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [kʰ] [k] |  |
| ⟨къ⟩ | [q] |  |
| ⟨кь⟩ | [qʼ] |  |
| ⟨кӏ⟩ | [kʼ] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [pʰ] [p] |  |
| ⟨пӏ⟩ | [pʼ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [tʰ] [t] |  |
| ⟨тӏ⟩ | [tʼ] |  |
| ⟨у⟩ | [u] |  |
| ⟨уь⟩ | [y] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨хъ⟩ | [qʰ] |  |
| ⟨хь⟩ | [x] |  |
| ⟨ц⟩ | [t͡sʰ] [t͡s] |  |
| ⟨цӏ⟩ | [t͡sʼ] |  |
| ⟨ч⟩ | [t͡ʃʰ] [t͡ʃ] |  |
| ⟨чӏ⟩ | [t͡ʃʼ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨ъ⟩ | [ʔ] |  |
| ⟨ы⟩ | [ə] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] [y] |  |
| ⟨я⟩ | [ja] [æ] |  |
| ⟨ё⟩ | [jo] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lez")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Leonese](ast-x-leon.md) · [Home](../index.md) · [Libyan Arabic →](ar-LY.md)
