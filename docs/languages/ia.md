# Interlingua (`ia`)

<!-- atlas:summary begin -->
Interlingua is a Constructed language, written in the Latin script. Glottolog places it in France. The `ia` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ia` |
| ISO 639-3 | [ina](https://iso639-3.sil.org/code/ina), Interlingua (IALA) |
| Glottolog | [inte1239](https://glottolog.org/resource/languoid/id/inte1239), Interlingua (International Auxiliary Language Association) |
| Wikidata | [Q35934](https://www.wikidata.org/wiki/Q35934) |
| Wikipedia | [Interlingua](https://en.wikipedia.org/wiki/Interlingua) |
| Family | [Constructed](by-family.md#constructed) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1951, living |
| Explorer | [`ia` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ia) |
| Spec file | [`ia.json`](../../orthography2ipa/data/ia.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Interlingua (IALA, Gode & Blair 1951). Near-phonemic Latin orthography with 'continental' values. ⟨c⟩ = /k/, but /ts/ before e, i, y, ⟨ch⟩ = /ʃ/ in French-derived words, /k/ in Greek/Italian-derived ones, ⟨s⟩ is often voiced [z] between vowels, ⟨qu⟩ = /kw/ (but /k/ in que, qui).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1951 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 30 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ia.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ia` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-gode_blair1951"></a>Gode, Alexander & Blair, Hugh E. (1951). *Interlingua: A Grammar of the International Language*. Storm Publishers (IALA).
2. <a id="src-gode1951_dict"></a>Gode, Alexander (1951). *Interlingua-English: A Dictionary of the International Language*. Storm Publishers (IALA).
3. <a id="src-interlingua_wiki"></a>Wikipedia contributors (2024). *Interlingua*. Wikipedia. Cited: Letter-to-sound table and stress rule. [en.wikipedia.org](https://en.wikipedia.org/wiki/Interlingua)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ia` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 443 | 0.0646 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [ks] [kw] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [ts] | before front vowel [ts] · default [k] |
| ⟨ch⟩ | [ʃ] [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] [s] |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [j] [i] |  |
| ⟨z⟩ | [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ia")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ingush](inh.md) · [Home](../index.md) · [Interlingue →](ie.md)
