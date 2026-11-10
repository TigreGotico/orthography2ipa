# Lombard (classical Milanese orthography) (`lmo-x-milanese`)

<!-- atlas:summary begin -->
Lombard (classical Milanese orthography) is an Italo-Romance variety, written in the Latin script. Glottolog places it in Italy and Switzerland. The `lmo-x-milanese` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lmo-x-milanese` |
| ISO 639-3 | [lmo](https://iso639-3.sil.org/code/lmo), Lombard |
| Glottolog | [lomb1257](https://glottolog.org/resource/languoid/id/lomb1257), Lombard |
| Wikidata | [Q33754](https://www.wikidata.org/wiki/Q33754) |
| Wikipedia | [Ortografia milanese classica](https://it.wikipedia.org/wiki/Ortografia_milanese_classica) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Italo-Romance](by-family.md#indo-european--italic--romance--italo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Italy](by-region.md#italy), [Switzerland](by-region.md#switzerland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1600, living |
| Parent | [Lombard](lmo.md) `lmo` |
| Explorer | [`lmo-x-milanese` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lmo-x-milanese) |
| Spec file | [`lmo-x-milanese.json`](../../orthography2ipa/data/lmo-x-milanese.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lombard written in the classical Milanese orthography (the Circolo Filologico Milanese's revision of Porta-era usage) rather than the Ticinese orthography that `lmo` targets.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1982 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes 2 of the 47 spellings of its letter table and takes the other 45 from [Lombard](lmo.md) `lmo`.

The [spec file](../../orthography2ipa/data/lmo-x-milanese.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lmo-x-milanese` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-porta_isella1982"></a>Porta, Carlo (ed. Isella, Dante) (1982). *Poesie*. Mondadori.
2. <a id="src-ortografia_milanese_classica_wp"></a>Wikipedia contributors (2024). *Ortografia milanese classica*. Wikipedia (it). [it.wikipedia.org](https://it.wikipedia.org/wiki/Ortografia_milanese_classica)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 44 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  | dz ts | dʒ tʃ |  |  |
| Nasal | m | ɱ |  | n |  | ɲ | ŋ |
| Trill |  |  |  | r |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative | β | f v | ð | s z | ʃ |  | ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u |
| Close-mid | e eː ø øː | o oː |
| Open-mid | ɛ | ɔ |
| Open | a aː |  |

Sequences that the spec writes as one unit: [kw] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [tʃ] |  |
| ⟨ch⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sc⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [y] |  |
| ⟨uu⟩ | [yː] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [ts] [dz] |  |
| ⟨à⟩ | [a] |  |
| ⟨â⟩ | [aː] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ê⟩ | [eː] |  |
| ⟨ì⟩ | [i] |  |
| ⟨í⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ô⟩ | [oː] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨öö⟩ | [øː] |  |
| ⟨ù⟩ | [u] |  |
| ⟨ü⟩ | [y] |  |
| ⟨üü⟩ | [yː] |  |
| ⟨œ⟩ | [ø] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lmo-x-milanese")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lombard](lmo.md) · [Home](../index.md) · [Louisiana Creole →](lou.md)
