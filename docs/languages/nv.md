# Navajo (`nv`)

<!-- atlas:summary begin -->
Navajo is an Athabaskan-Eyak-Tlingit language, written in the Latin script. Glottolog places it in United States. The `nv` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nv` |
| ISO 639-3 | [nav](https://iso639-3.sil.org/code/nav), Navajo |
| Glottolog | [nava1243](https://glottolog.org/resource/languoid/id/nava1243), Navajo |
| Wikidata | [Q13310](https://www.wikidata.org/wiki/Q13310) |
| Wikipedia | [Navajo language](https://en.wikipedia.org/wiki/Navajo_language) |
| Family | [Athabaskan-Eyak-Tlingit](by-family.md#athabaskan-eyak-tlingit) |
| Region | [North America](by-region.md#north-america) > [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1930, living |
| Parent | [Athabaskan-Eyak-Tlingit](https://tigregotico.github.io/orthography2ipa/#x-clade-atha1245) `x-clade-atha1245` |
| Explorer | [`nv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nv) |
| Spec file | [`nv.json`](../../orthography2ipa/data/nv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Navajo (Diné bizaad), Southern Athabaskan (Na-Dene), written in a Latin alphabet standardised in the 1930s (Young & Morgan).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1987 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 64 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-young_morgan1987"></a>Young, Robert W. & Morgan, William (1987). *The Navajo Language: A Grammar and Colloquial Dictionary (rev. ed.)*. University of New Mexico Press.
2. <a id="src-mcdonough2003"></a>McDonough, Joyce (2003). *The Navajo Sound System*. Kluwer Academic Publishers.
3. <a id="src-navajo_language_wiki"></a>Wikipedia contributors (2026). *Navajo language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Navajo_language)
4. <a id="src-navajo_phonology_wiki"></a>Wikipedia contributors (2026). *Navajo phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Navajo_phonology)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nv` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 989 | 0.2514 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 68 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t tʰ tʼ |  |  | k kʰ kʷʰ kʼ |  | ʔ |
| Affricate |  | ts tsʰ tsʼ tɬ tɬʰ tɬʼ | tʃ tʃʰ tʃʼ |  |  |  |  |
| Nasal | m | n |  |  |  |  |  |
| Fricative |  | s z | ʃ ʒ | ʝ | x ɣ ɣʷ | ʁ | h hʷ |
| Lateral fricative |  | ɬ |  |  |  |  |  |
| Approximant |  |  |  | j | ɰ |  |  |
| Lateral approximant |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Near-close | ɪ ɪː ɪ́ ɪ́ː ɪ̃ ɪ̃ː ɪ̃́ ɪ̃́ː |  |
| Close-mid | e eː é éː ẽ ẽː ẽ́ ẽ́ː | o oː ó óː õ õː ṍ ṍː |
| Open |  | ɑ ɑː ɑ́ ɑ́ː ɑ̃ ɑ̃ː ɑ̃́ ɑ̃́ː |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨aa⟩ | [ɑː] |  |
| ⟨b⟩ | [p] |  |
| ⟨ch⟩ | [tʃʰ] |  |
| ⟨chʼ⟩ | [tʃʼ] |  |
| ⟨d⟩ | [t] |  |
| ⟨dl⟩ | [tɬ] |  |
| ⟨dz⟩ | [ts] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨g⟩ | [k] |  |
| ⟨gh⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨hw⟩ | [hʷ] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨ii⟩ | [ɪː] |  |
| ⟨j⟩ | [tʃ] |  |
| ⟨k⟩ | [kʰ] |  |
| ⟨kw⟩ | [kʷʰ] |  |
| ⟨kʼ⟩ | [kʼ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨ts⟩ | [tsʰ] |  |
| ⟨tsʼ⟩ | [tsʼ] |  |
| ⟨tł⟩ | [tɬʰ] |  |
| ⟨tłʼ⟩ | [tɬʼ] |  |
| ⟨tʼ⟩ | [tʼ] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |
| ⟨á⟩ | [ɑ́] |  |
| ⟨áá⟩ | [ɑ́ː] |  |
| ⟨é⟩ | [é] |  |
| ⟨éé⟩ | [éː] |  |
| ⟨í⟩ | [ɪ́] |  |
| ⟨íí⟩ | [ɪ́ː] |  |
| ⟨ó⟩ | [ó] |  |
| ⟨óó⟩ | [óː] |  |
| ⟨ą⟩ | [ɑ̃] |  |
| ⟨ąą⟩ | [ɑ̃ː] |  |
| ⟨ą́⟩ | [ɑ̃́] |  |
| ⟨ą́ą́⟩ | [ɑ̃́ː] |  |
| ⟨ę⟩ | [ẽ] |  |
| ⟨ęę⟩ | [ẽː] |  |
| ⟨ę́⟩ | [ẽ́] |  |
| ⟨ę́ę́⟩ | [ẽ́ː] |  |
| ⟨į⟩ | [ɪ̃] |  |
| ⟨įį⟩ | [ɪ̃ː] |  |
| ⟨į́⟩ | [ɪ̃́] |  |
| ⟨į́į́⟩ | [ɪ̃́ː] |  |
| ⟨ł⟩ | [ɬ] |  |
| ⟨ǫ⟩ | [õ] |  |
| ⟨ǫǫ⟩ | [õː] |  |
| ⟨ǫ́⟩ | [ṍ] |  |
| ⟨ǫ́ǫ́⟩ | [ṍː] |  |
| ⟨ʼ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nanai](gld.md) · [Home](../index.md) · [Nawat →](ppl.md)
