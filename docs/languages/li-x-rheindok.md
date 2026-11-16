# Limburgish (Rheinische Dokumenta notation) (`li-x-rheindok`)

<!-- atlas:summary begin -->
Limburgish (Rheinische Dokumenta notation) is a Germanic variety, written in the Latin script. Glottolog places it in Belgium, Germany and Netherlands. The `li-x-rheindok` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `li-x-rheindok` |
| ISO 639-3 | [lim](https://iso639-3.sil.org/code/lim), Limburgan |
| Glottolog | [limb1263](https://glottolog.org/resource/languoid/id/limb1263), Limburgan |
| Wikidata | [Q102172](https://www.wikidata.org/wiki/Q102172) |
| Wikipedia | [Rheinische Dokumenta](https://en.wikipedia.org/wiki/Rheinische_Dokumenta) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic](by-family.md#indo-european--germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Belgium](by-region.md#belgium), [Germany](by-region.md#germany), [Netherlands](by-region.md#netherlands) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Limburgish](li.md) `li` |
| Explorer | [`li-x-rheindok` in the data explorer](https://tigregotico.github.io/orthography2ipa/#li-x-rheindok) |
| Spec file | [`li-x-rheindok.json`](../../orthography2ipa/data/li-x-rheindok.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Rheinische Dokumenta is the Landschaftsverband Rheinland's transcription standard for the dialects of the Rhineland, and part of the Limburgish gold this library is benchmarked against is written in it rather than in the Veldeke Spelling 2003 that `li` models.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1987 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 51 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/li-x-rheindok.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `li-x-rheindok` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-honnen1987_rheinische_dokumenta"></a>Honnen, Peter (after preparatory work by Fritz Langensiepen) (1987). *Rheinische Dokumenta. Lautschrift fuer rheinische Mundarten. Mundartdokumentation im Rheinland*. Rheinland-Verlag, Koeln (2nd edition, issued by the Landschaftsverband Rheinland), 39 pp. [rheinische-landeskunde.lvr.de](https://rheinische-landeskunde.lvr.de/de/sprache/sprache_publikationen/sprache_publikationen_buecher_1/rheinische_dokumenta_publikation_1.html)
2. <a id="src-rheinische_dokumenta_wiki"></a>Wikipedia contributors (2026). *Rheinische Dokumenta*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Rheinische_Dokumenta)
3. <a id="src-cornelissen1989_rheinisches_platt"></a>Cornelissen, Georg, Honnen, Peter, Langensiepen, Fritz (eds.) (1989). *Das rheinische Platt. Eine Bestandsaufnahme*. Rheinland-Verlag, Koeln.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 65 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative | β | f v | s z | ʃ ʒ | ç ʝ | x ɣ | ʁ χ | h ɦ |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  | ʎ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː |  | u uː |
| Near-close | ɪ ɪː ʏ ʏː |  | ʊ ʊː |
| Close-mid | e eː ø øː |  | o oː |
| Mid |  | ə əː |  |
| Open-mid | œ œː ɛ ɛː |  | ɔ ɔː |
| Near-open | æ æː | ɐ ɐː |  |
| Open | a aː |  | ɑ ɑː ɒː |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [ɐ] |  |
| ⟨aa⟩ | [aː] [ɐː] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [x] |  |
| ⟨c̭h⟩ | [χ] |  |
| ⟨c̲h̲⟩ | [ç] |  |
| ⟨c͜h⟩ | [ɣ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨e̩⟩ | [ə] |  |
| ⟨e̩e̩⟩ | [əː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] [ɪ] |  |
| ⟨ii⟩ | [iː] [ɪː] |  |
| ⟨j⟩ | [ʝ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] [ʊ] |  |
| ⟨oo⟩ | [oː] [ʊː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ʁ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sch⟩ | [ʃ] |  |
| ⟨s͜ch⟩ | [ʒ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [ʊ] [u] |  |
| ⟨uu⟩ | [ʊː] [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] [β] |  |
| ⟨ä⟩ | [ɛ] |  |
| ⟨ää⟩ | [ɛː] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨öö⟩ | [øː] |  |
| ⟨ü⟩ | [y] [ʏ] |  |
| ⟨üü⟩ | [yː] [ʏː] |  |
| ⟨ą̈⟩ | [æ] |  |
| ⟨ą̈ą̈⟩ | [æː] |  |
| ⟨ǫ⟩ | [ɔ] |  |
| ⟨ǫǫ⟩ | [ɔː] |  |
| ⟨ǫ̈⟩ | [œ] |  |
| ⟨ǫ̈ǫ̈⟩ | [œː] |  |
| ⟨ṛ⟩ | [ʁ] |  |
| ⟨ṣ⟩ | [z] |  |
| ⟨ạ⟩ | [ɑ] |  |
| ⟨ạạ⟩ | [ɑː] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 2 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `LI_OPEN_SYLLABLE_E` | /æ/ → [eː], stressed, before a consonant, spelled ⟨e⟩, with more context in the spec | - | Spelling 2003, Peters 2006 |
| `LI_OPEN_SYLLABLE_E_TONE_SIGN` | /æ/ → [eː], stressed, spelled ⟨e⟩, before ⟨~⟩ ⟨\⟩, with more context in the spec | - | - |

The spec switches off 1 inherited rules: `LI_FINAL_H_LENGTH_SIGN`.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "li-x-rheindok")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Limburgish](li.md) · [Home](../index.md) · [Lingala →](ln.md)
