# Votic (`vot`)

<!-- atlas:summary begin -->
Votic is a Finnic language, written in the Latin script. Glottolog places it in Russia. The `vot` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `vot` |
| ISO 639-3 | [vot](https://iso639-3.sil.org/code/vot), Votic |
| Glottolog | [voti1245](https://glottolog.org/resource/languoid/id/voti1245), Votic |
| Wikidata | [Q32858](https://www.wikidata.org/wiki/Q32858) |
| Wikipedia | [Votic language](https://en.wikipedia.org/wiki/Votic_language) |
| Family | [Uralic](by-family.md#uralic) > [Finnic](by-family.md#uralic--finnic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Finnic](https://tigregotico.github.io/orthography2ipa/#x-clade-finn1317) `x-clade-finn1317` |
| Explorer | [`vot` in the data explorer](https://tigregotico.github.io/orthography2ipa/#vot) |
| Spec file | [`vot.json`](../../orthography2ipa/data/vot.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Votic (vaďďa tšeeli), a Finnic (Uralic) language of Ingria, closely related to Estonian and Ingrian.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1998 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes 13 of the 72 spellings of its letter table and takes the other 59 from [Finnish](fi.md) `fi`.

The [spec file](../../orthography2ipa/data/vot.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `vot` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-votic_language_wikipedia"></a>Wikipedia contributors (2026). *Votic language, Phonology and Orthography*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Votic_language)
2. <a id="src-abondolo1998"></a>Abondolo, D. (ed.) (1998). *The Uralic Languages*. Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `vot` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2832 | 0.0898 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 75 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pː |  | d t tː |  |  | k kː ɡ |  |
| Affricate |  |  |  | t͡ʃ t͡ʃː |  |  |  |
| Nasal | m mː |  | n nː |  |  | ŋ ŋː |  |
| Trill |  |  | r rː |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s sː z | ʃ ʃː ʒ ʒː | ç | x | h ɦ |
| Approximant |  | ʋ |  |  | j |  |  |
| Lateral approximant |  |  | l lː |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u uː |
| Close-mid | e eː ø øː | o oː ɤ ɤː |
| Near-open | æ æː |  |
| Open |  | ɑ ɑː |

Sequences that the spec writes as one unit: [ei] [eu] [ey] [ie] [iu] [iy] [oi] [ou] [ui] [uo] [w] [yi] [yø] [æi] [æy] [øi] [øy] [ŋk] [ɑi] [ɑu].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨aa⟩ | [ɑː] |  |
| ⟨ai⟩ | [ɑi] |  |
| ⟨au⟩ | [ɑu] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [s] |  |
| ⟨d⟩ | [d] | default [d] |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨ei⟩ | [ei] |  |
| ⟨eu⟩ | [eu] |  |
| ⟨ey⟩ | [ey] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ie⟩ | [ie] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨iu⟩ | [iu] |  |
| ⟨iy⟩ | [iy] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] | default [k] |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋː] | default [ŋː] |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oi] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [ou] |  |
| ⟨p⟩ | [p] | default [p] |
| ⟨pp⟩ | [pː] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] | default [t] |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨ui⟩ | [ui] |  |
| ⟨uo⟩ | [uo] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [v] |  |
| ⟨y⟩ | [y] |  |
| ⟨yi⟩ | [yi] |  |
| ⟨yy⟩ | [yː] |  |
| ⟨yö⟩ | [yø] |  |
| ⟨z⟩ | [z] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨äi⟩ | [æi] |  |
| ⟨äy⟩ | [æy] |  |
| ⟨ää⟩ | [æː] |  |
| ⟨õ⟩ | [ɤ] |  |
| ⟨õõ⟩ | [ɤː] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨öi⟩ | [øi] |  |
| ⟨öy⟩ | [øy] |  |
| ⟨öö⟩ | [øː] |  |
| ⟨ü⟩ | [y] |  |
| ⟨üü⟩ | [yː] |  |
| ⟨č⟩ | [t͡ʃ] |  |
| ⟨čč⟩ | [t͡ʃː] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨šš⟩ | [ʃː] |  |
| ⟨ž⟩ | [ʒ] |  |
| ⟨žž⟩ | [ʒː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "vot")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Volapük](vo.md) · [Home](../index.md) · [Võro →](vro.md)
