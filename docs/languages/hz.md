# Herero (`hz`)

<!-- atlas:summary begin -->
Herero is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Angola, Botswana and Namibia. The `hz` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `hz` |
| ISO 639-3 | [her](https://iso639-3.sil.org/code/her), Herero |
| Glottolog | [here1253](https://glottolog.org/resource/languoid/id/here1253), Herero |
| Wikidata | [Q33315](https://www.wikidata.org/wiki/Q33315) |
| Wikipedia | [Herero language](https://en.wikipedia.org/wiki/Herero_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Angola](by-region.md#angola), [Botswana](by-region.md#botswana), [Namibia](by-region.md#namibia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1880, living |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`hz` in the data explorer](https://tigregotico.github.io/orthography2ipa/#hz) |
| Spec file | [`hz.json`](../../orthography2ipa/data/hz.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Herero (Otjiherero), a Bantu language of Namibia and Botswana. INPUT CONTRACT: the standard Latin Otjiherero orthography (the practical missionary-derived spelling used in Namibian publications and schools) is assumed, text is expected to be already normalised.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 2002 to 2025. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/hz.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `hz` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-herero_language_wiki"></a>Wikipedia contributors (2024). *Herero language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Herero_language)
2. <a id="src-omniglot_herero"></a>Ager, S. (2024). *Herero language, alphabet and pronunciation*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/herero.php)
3. <a id="src-mohlig_marten_kavari2002"></a>Möhlig, W.J.G., Marten, L. & Kavari, J.U. (2002). *A Grammatical Sketch of Herero (Otjiherero)*. Rüdiger Köppe Verlag, Köln.
4. <a id="src-herero_phonology_wiki_tables"></a>Wikipedia contributors (2025). *Herero language, Phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Herero_language#Phonology)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t ⁿd |  |  | k ɡ |  |
| Affricate |  |  |  |  | tʃ ⁿdʒ |  |  |  |
| Nasal | m |  |  | n |  | ɲ |  |  |
| Trill |  |  |  | r |  |  |  |  |
| Fricative |  | f v | ð | s |  |  |  | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Open-mid | ɛ ɛː | ɔ ɔː |
| Open |  | ɑ ɑː |

Sequences that the spec writes as one unit: [w] [ᵐb] [ᵐw] [ᵑɡ] [ᵑɡʷ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨aa⟩ | [ɑː] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨ee⟩ | [ɛː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] |  |
| ⟨mw⟩ | [ᵐw] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ⁿd] |  |
| ⟨ndj⟩ | [ⁿdʒ] |  |
| ⟨ng⟩ | [ᵑɡ] |  |
| ⟨ngw⟩ | [ᵑɡʷ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨oo⟩ | [ɔː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tj⟩ | [tʃ] |  |
| ⟨u⟩ | [u] [w] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [ð] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "hz")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hejazi Arabic](acw-SA.md) · [Home](../index.md) · [Hiligaynon →](hil.md)
