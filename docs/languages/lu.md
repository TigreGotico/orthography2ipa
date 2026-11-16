# Luba-Katanga (Kiluba) (`lu`)

<!-- atlas:summary begin -->
Luba-Katanga (Kiluba) is a Bantu language, written in the Latin script. Glottolog places it in Congo - Kinshasa. The `lu` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lu` |
| ISO 639-3 | [lub](https://iso639-3.sil.org/code/lub), Luba-Katanga |
| Glottolog | [luba1250](https://glottolog.org/resource/languoid/id/luba1250), Luba-Katanga |
| Wikidata | [Q36157](https://www.wikidata.org/wiki/Q36157) |
| Wikipedia | [Luba-Katanga language](https://en.wikipedia.org/wiki/Luba-Katanga_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Congo - Kinshasa](by-region.md#congo---kinshasa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Bantu](https://tigregotico.github.io/orthography2ipa/#x-clade-narr1281) `x-clade-narr1281` |
| Explorer | [`lu` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lu) |
| Spec file | [`lu.json`](../../orthography2ipa/data/lu.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Luba-Katanga (Kiluba), Guthrie L.33, Bantu language of Haut-Katanga and Haut-Lomami provinces, DR Congo. 22-letter Latin alphabet: five vowels a/e/i/o/u (with a length contrast not marked in standard spelling) and 17 consonants. /p, b/ have the fricative allophones [ɸ, β] intervocalically or before a semivowel (Van Avermaet & Mbuya 1954).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1954 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 34 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lu.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lu` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-vanavermaet_mbuya1954"></a>Van Avermaet, E. & Mbuya, B. (1954). *Dictionnaire kiluba-français*. Institut Royal Colonial Belge.
2. <a id="src-lub_wiki"></a>Wikipedia contributors (2025). *Luba-Katanga language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Luba-Katanga_language)
3. <a id="src-omniglot_lub"></a>Ager, Simon (2025). *Luba-Katanga language and alphabet*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/lubakatanga.htm)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t ⁿt |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ ⁿdʒ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Fricative | ɸ β | f v | s z ⁿs ⁿz |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [mb] [nd] [w] [ŋk] [ŋɡ] [ᵐp] [ᶬf] [ᶬv].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] | default [b] · intervocalic [β] |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨mf⟩ | [ᶬf] |  |
| ⟨mp⟩ | [ᵐp] |  |
| ⟨mv⟩ | [ᶬv] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨nj⟩ | [ⁿdʒ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨ns⟩ | [ⁿs] |  |
| ⟨nt⟩ | [ⁿt] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨nz⟩ | [ⁿz] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] | default [p] · intervocalic [ɸ] |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lu")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Luba-Kasai](lua.md) · [Home](../index.md) · [Luganda →](lg.md)
