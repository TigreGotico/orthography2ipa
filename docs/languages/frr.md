# North Frisian (`frr`)

<!-- atlas:summary begin -->
North Frisian is a West Germanic language, written in the Latin script. Glottolog places it in Denmark and Germany. The `frr` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `frr` |
| ISO 639-3 | [frr](https://iso639-3.sil.org/code/frr), Northern Frisian |
| Glottolog | [nort2626](https://glottolog.org/resource/languoid/id/nort2626), Northern Frisian |
| Wikidata | [Q28224](https://www.wikidata.org/wiki/Q28224) |
| Wikipedia | [North Frisian language](https://en.wikipedia.org/wiki/North_Frisian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Denmark](by-region.md#denmark), [Germany](by-region.md#germany) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Ancestor | [Old Frisian](https://tigregotico.github.io/orthography2ipa/#ofs) `ofs` |
| Explorer | [`frr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#frr) |
| Spec file | [`frr.json`](../../orthography2ipa/data/frr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> North Frisian (Nordfriisk / Frasch / Freesk), spoken by ~8,000, 10,000 speakers in Nordfriesland (Schleswig-Holstein, Germany). Severely endangered. Comprises ~10 distinct dialect groups divided into insular (Söl'ring, Fering, Öömrang, Halunder) and mainland (Mooring, Goesharde, Wiedingharde, Karrharde, etc.) varieties.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 2001. [Sources](#sources) lists them. The spec file writes all 53 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/frr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `frr` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-walker_wilts2001"></a>Walker, A. & Wilts, O. (2001). *The North Frisian Language*. Fryske Akademy / Nordfriesisches Institut.
2. <a id="src-arhammar2001"></a>Århammar, N. (2001). *The North Frisian Dialects*. Fryske Akademy / Nordfriesisches Institut.
3. <a id="src-fort_munske2001"></a>Fort, M.C. & Munske, H.H. (eds.) (2001). *Handbuch des Friesischen / Handbook of Frisian Studies*. Max Niemeyer Verlag.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 50 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s | ʃ |  | x | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː yː |  | uː |
| Near-close | ɪ ʏ |  | ʊ |
| Close-mid | eː øː |  | oː |
| Mid |  | ə |  |
| Open-mid | œ ɛ |  | ɔ |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [ai] [au] [iə] [ks] [uə] [w] [yə] [ŋk] [œi] [ɔi] [ɔu] [ɛi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨ai⟩ | [ai] |  |
| ⟨au⟩ | [au] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨dj⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] [ə] | default [ɛ] [ə] · nucleus stressed [ɛ] · nucleus unstressed [ə] |
| ⟨ee⟩ | [eː] |  |
| ⟨ei⟩ | [ɛi] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] · word final [k] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨ia⟩ | [iə] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨oi⟩ | [ɔi] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [ɔu] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] [ʁ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sch⟩ | [ʃ] |  |
| ⟨sj⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨tj⟩ | [tʃ] |  |
| ⟨tsch⟩ | [tʃ] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨ua⟩ | [uə] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] [f] | default [v] · word final [f] |
| ⟨w⟩ | [v] [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨z⟩ | [ts] |  |
| ⟨ä⟩ | [ɛ] |  |
| ⟨äi⟩ | [ɛi] |  |
| ⟨ö⟩ | [œ] |  |
| ⟨öi⟩ | [œi] |  |
| ⟨öö⟩ | [øː] |  |
| ⟨ü⟩ | [ʏ] |  |
| ⟨üa⟩ | [yə] |  |
| ⟨üü⟩ | [yː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "frr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Norman](nrm.md) · [Home](../index.md) · [North-Western Catalan →](ca-x-occident.md)
