# Sango (`sg`)

<!-- atlas:summary begin -->
Sango is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Central African Republic, Chad, Congo - Brazzaville and Congo - Kinshasa. The `sg` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sg` |
| ISO 639-3 | [sag](https://iso639-3.sil.org/code/sag), Sango |
| Glottolog | [sang1328](https://glottolog.org/resource/languoid/id/sang1328), Sango |
| Wikidata | [Q33954](https://www.wikidata.org/wiki/Q33954) |
| Wikipedia | [Sango language](https://en.wikipedia.org/wiki/Sango_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Central African Republic](by-region.md#central-african-republic), [Chad](by-region.md#chad), [Congo - Brazzaville](by-region.md#congo---brazzaville), [Congo - Kinshasa](by-region.md#congo---kinshasa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`sg` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sg) |
| Spec file | [`sg.json`](../../orthography2ipa/data/sg.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Sango (Sängö), Ngbandi-based creole and national language of the Central African Republic.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1967 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 40 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sg.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sg` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-samarin1967"></a>Samarin, William J. (1967). *A Grammar of Sango*. Mouton.
2. <a id="src-sango_orth_1984"></a>République Centrafricaine (1984). *Décret fixant l'orthographe officielle du sango*. Government of the Central African Republic.
3. <a id="src-sango_wiki"></a>Wikipedia contributors (2025). *Sango language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Sango_language)
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
| Plosive | b p |  | d t ⁿd |  | k ɡ |  |
| Nasal | m |  | n |  |  |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z ⁿz |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [k͡p] [w] [ɡ͡b] [ᵐb] [ᵑɡ] [ᵑɡ͡b] [ᶬv].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨kp⟩ | [k͡p] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] |  |
| ⟨mv⟩ | [ᶬv] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ⁿd] |  |
| ⟨ng⟩ | [ᵑɡ] |  |
| ⟨ngb⟩ | [ᵑɡ͡b] |  |
| ⟨nz⟩ | [ⁿz] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨â⟩ | [a] |  |
| ⟨ä⟩ | [a] |  |
| ⟨ê⟩ | [e] |  |
| ⟨ë⟩ | [e] |  |
| ⟨î⟩ | [i] |  |
| ⟨ï⟩ | [i] |  |
| ⟨ô⟩ | [o] |  |
| ⟨ö⟩ | [o] |  |
| ⟨û⟩ | [u] |  |
| ⟨ü⟩ | [u] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sg")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sanabrese](ast-x-sanabria.md) · [Home](../index.md) · [Sanskrit →](sa.md)
