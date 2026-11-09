# Farefare (Frafra) (`gur`)

<!-- atlas:summary begin -->
Farefare (Frafra) is an Atlantic-Congo language, written in the Latin script. Glottolog places it in the Africa and North America macroareas. The `gur` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gur` |
| Wikipedia | [Frafra language](https://en.wikipedia.org/wiki/Frafra_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#several-macroareas), [North America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`gur` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gur) |
| Spec file | [`gur.json`](../../orthography2ipa/data/gur.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Farefare (Frafra, Gurenɛ/Gurene), a Gur / Mabia (Atlantic-Congo) language of the Upper East Region of Ghana and southern Burkina Faso. INPUT CONTRACT: text is assumed to be in the Latin Farefare orthography, the Latin alphabet WITHOUT ⟨c j q x⟩ and WITH ⟨ɛ ɩ ŋ ɔ ʋ⟩.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2005 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 43 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gur.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gur` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-farefare_wiki"></a>Wikipedia contributors (2026). *Farefare language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Farefare_language)
2. <a id="src-dakubu2005"></a>Dakubu, M. E. Kropp (ed.) (2005). *Collected Language Notes on Gurenɛ Grammar*. Institute of African Studies, University of Ghana, Legon.
3. <a id="src-atintono2013"></a>Atintono, Samuel Awinkene (2013). *The Semantics and Grammar of Positional Verbs in Gurenɛ: A Typological Perspective*. PhD thesis, University of Manchester. [escholar.manchester.ac.uk](https://www.escholar.manchester.ac.uk/uk-ac-man-scw:189249)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `gur` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 111 | 0.2968 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 43 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ | ʔ |
| Nasal | m |  | n |  | ŋ |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative |  | f v | s z |  | ɣ | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː ĩ | u uː ũ |
| Near-close | ɪ ɪː | ʊ ʊː |
| Close-mid | e eː | o oː |
| Open-mid | ɛ ɛː ɛ̃ | ɔ ɔː ɔ̃ |
| Open | a aː ã |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨õ⟩ | [ɔ̃] |  |
| ⟨ĩ⟩ | [ĩ] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ũ⟩ | [ũ] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɔɔ⟩ | [ɔː] |  |
| ⟨ɛ⟩ | [ɛ] |  |
| ⟨ɛɛ⟩ | [ɛː] |  |
| ⟨ɣ⟩ | [ɣ] |  |
| ⟨ɩ⟩ | [ɪ] |  |
| ⟨ɩɩ⟩ | [ɪː] |  |
| ⟨ʋ⟩ | [ʊ] |  |
| ⟨ʋʋ⟩ | [ʊː] |  |
| ⟨ẽ⟩ | [ɛ̃] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gur")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Fante](fat.md) · [Home](../index.md) · [Fernando Po Creole English →](fpe.md)
