# Veps (`vep`)

<!-- atlas:summary begin -->
Veps is an Uralic language, written in the Latin script. Glottolog places it in Russia. The `vep` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `vep` |
| ISO 639-3 | [vep](https://iso639-3.sil.org/code/vep), Veps |
| Glottolog | [veps1250](https://glottolog.org/resource/languoid/id/veps1250), Veps |
| Wikidata | [Q32747](https://www.wikidata.org/wiki/Q32747) |
| Wikipedia | [Veps language](https://en.wikipedia.org/wiki/Veps_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1989, living |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`vep` in the data explorer](https://tigregotico.github.io/orthography2ipa/#vep) |
| Spec file | [`vep.json`](../../orthography2ipa/data/vep.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Veps (vepsän kel'), Finnic (Uralic), Karelia / Leningrad Oblast. The modern (post-1989) orthography uses a 29-character Latin alphabet: 22 basic Latin letters, six with diacritics (č š ž ü ä ö) and the prime ⟨ʹ⟩. ⟨c⟩ = /t͡s/, ⟨č⟩ = /t͡ʃ/, ⟨š⟩ = /ʃ/, ⟨ž⟩ = /ʒ/, ⟨ü⟩ = /y/, ⟨ä⟩ = /æ/, ⟨ö⟩ = /ø/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1981 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 28 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/vep.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `vep` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-zaitseva1981"></a>Zaitseva, Maria I. (1981). *Грамматика вепсского языка (Grammar of the Veps Language)*. Nauka.
2. <a id="src-veps_language_wiki"></a>Wikipedia contributors (2026). *Veps language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Veps_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `vep` | gold | lexicon-derived | CC BY 4.0 | 1004 | 0.2065 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 30 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | t͡s | t͡ʃ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y | ɨ | u |
| Close-mid | e ø |  | o |
| Near-open | æ |  |  |
| Open |  |  | ɑ |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [t͡s] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [z] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |
| ⟨č⟩ | [t͡ʃ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "vep")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Venezuelan Spanish](es-VE.md) · [Home](../index.md) · [Vietnamese →](vi.md)
