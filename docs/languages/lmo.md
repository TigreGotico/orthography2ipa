# Lombard (`lmo`)

<!-- atlas:summary begin -->
Lombard is an Italo-Romance language, written in the Latin script. Glottolog places it in Italy and Switzerland. The `lmo` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lmo` |
| ISO 639-3 | [lmo](https://iso639-3.sil.org/code/lmo), Lombard |
| Glottolog | [lomb1257](https://glottolog.org/resource/languoid/id/lomb1257), Lombard |
| Wikidata | [Q33754](https://www.wikidata.org/wiki/Q33754) |
| Wikipedia | [Lombard language](https://en.wikipedia.org/wiki/Lombard_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Italo-Romance](by-family.md#indo-european--italic--romance--italo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Italy](by-region.md#italy), [Switzerland](by-region.md#switzerland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Ancestor | [Gallo-Italic Vulgar Latin](https://tigregotico.github.io/orthography2ipa/#la-x-gallo-italic) `la-x-gallo-italic` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`lmo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lmo) |
| Spec file | [`lmo.json`](../../orthography2ipa/data/lmo.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lombard. Gallo-Italic language of Lombardy, parts of Piedmont, and Swiss Ticino. ~3.5 million speakers. Reference variety: Western Lombard (Milanese). Key features: (1) Front rounded vowels /y, ø/. (2) Phonemic vowel length. (3) Degemination. (4) Extreme final vowel loss. (5) Intervocalic lenition (Sanga 1984).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1996 to 2024. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes 29 of the 47 spellings of its letter table and takes the other 18 from [Gallo-Italic Vulgar Latin](https://tigregotico.github.io/orthography2ipa/#la-x-gallo-italic) `la-x-gallo-italic`.

The [spec file](../../orthography2ipa/data/lmo.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `lmo` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Lombard (classical Milanese orthography)](lmo-x-milanese.md) `lmo-x-milanese`: Italy, Switzerland, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
2. <a id="src-loporcaro2009"></a>Loporcaro, M. (2009). *Profilo linguistico dei dialetti italiani*. Laterza.
3. <a id="src-ortografia_ticinese_wp"></a>Wikipedia contributors (2024). *Ortografia ticinese*. Wikipedia (it). [it.wikipedia.org](https://it.wikipedia.org/wiki/Ortografia_ticinese)
4. <a id="src-ortografia_milanese_classica_wp"></a>Wikipedia contributors (2024). *Ortografia milanese classica*. Wikipedia (it). [it.wikipedia.org](https://it.wikipedia.org/wiki/Ortografia_milanese_classica)
5. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `lmo` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 406 | 0.2892 | yes |
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
| ⟨â⟩ | [a] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ê⟩ | [eː] |  |
| ⟨ì⟩ | [i] |  |
| ⟨í⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ô⟩ | [u] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lmo")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lolopo](ycl.md) · [Home](../index.md) · [Lombard →](lmo-x-milanese.md)
