# Mooré (`mos`)

<!-- atlas:summary begin -->
Mooré is an Atlantic-Congo language, written in the Latin script. Glottolog places it in 5 countries. The `mos` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mos` |
| ISO 639-3 | [mos](https://iso639-3.sil.org/code/mos), Mossi |
| Glottolog | [moss1236](https://glottolog.org/resource/languoid/id/moss1236), Mossi |
| Wikidata | [Q36096](https://www.wikidata.org/wiki/Q36096) |
| Wikipedia | [Mooré](https://en.wikipedia.org/wiki/Moor%C3%A9) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Burkina Faso](by-region.md#burkina-faso), [Côte d’Ivoire](by-region.md#côte-divoire), [Ghana](by-region.md#ghana), [Mali](by-region.md#mali), [Togo](by-region.md#togo) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`mos` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mos) |
| Spec file | [`mos.json`](../../orthography2ipa/data/mos.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Mooré (Moore, Mossi), the principal Gur / Oti-Volta language of Burkina Faso. INPUT CONTRACT: text is assumed to be in the official Burkinabè national-alphabet Mooré orthography: a ʼ b d e ɛ f g h i ɩ k l m n o p r s t u ʋ v w y z, with nasal vowels written with a TILDE (ã ẽ ĩ õ ũ).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1982 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mos.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mos` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-moore_language_wiki"></a>Wikipedia contributors (2026). *Moore language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Moor%C3%A9)
2. <a id="src-moore_fr_wiki"></a>Wikipédia contributors (2026). *Mooré (Écriture / alphabet national burkinabè)*. Wikipédia (French). [fr.wikipedia.org](https://fr.wikipedia.org/wiki/Moor%C3%A9)
3. <a id="src-nikiema1982"></a>Nikiema, Norbert (1982). *Sɛbtaare: méthode pratique de transcription du mooré*. Presses Africaines, Ouagadougou.
4. <a id="src-kabore1985"></a>Kaboré, Raphaël (1985). *Essai d'analyse de la langue mòoré (parler de Waogodgo, Ouagadougou)*. Thèse d'État, Université Paris 7.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 32 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ | ʔ |
| Nasal | m |  | n | ɲ |  |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i ĩ | u ũ |
| Near-close | ɪ | ʊ |
| Close-mid | e ẽ | o õ |
| Open-mid | ɛ |  |
| Open | a ã |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨õ⟩ | [õ] |  |
| ⟨ĩ⟩ | [ĩ] |  |
| ⟨ũ⟩ | [ũ] |  |
| ⟨ɛ⟩ | [ɛ] |  |
| ⟨ɩ⟩ | [ɪ] |  |
| ⟨ʋ⟩ | [ʊ] |  |
| ⟨ʼ⟩ | [ʔ] |  |
| ⟨ẽ⟩ | [ẽ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mos")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mongolian](mn.md) · [Home](../index.md) · [Morisyen →](mfe.md)
