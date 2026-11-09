# Uyghur (`ug`)

<!-- atlas:summary begin -->
Uyghur is a Turkic language, written in the Arabic script. Glottolog places it in 7 countries. The `ug` spec is at the research tier. It cites 5 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ug` |
| ISO 639-3 | [uig](https://iso639-3.sil.org/code/uig), Uighur |
| Glottolog | [uigh1240](https://glottolog.org/resource/languoid/id/uigh1240), Uighur |
| Wikidata | [Q13263](https://www.wikidata.org/wiki/Q13263) |
| Wikipedia | [Uyghur language](https://en.wikipedia.org/wiki/Uyghur_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [India](by-region.md#india), [Kazakhstan](by-region.md#kazakhstan), [Kyrgyzstan](by-region.md#kyrgyzstan), [Mongolia](by-region.md#mongolia), [Pakistan](by-region.md#pakistan), [Uzbekistan](by-region.md#uzbekistan) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`ug` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ug) |
| Spec file | [`ug.json`](../../orthography2ipa/data/ug.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Uyghur, written in the Uyghur Perso-Arabic alphabet (Uyghur Ereb Yéziqi, UEY), the official script in Xinjiang. RESEARCH: grapheme inventory now specified.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1991 to 2024. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 34 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ug.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ug` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-uyghur_wiki"></a>Wikipedia contributors (2024). *Uyghur language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Uyghur_language)
2. <a id="src-uyghur_alphabets_wiki"></a>Wikipedia contributors (2024). *Uyghur alphabets*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Uyghur_alphabets)
3. <a id="src-hahn1991"></a>Hahn, Reinhard F. (1991). *Spoken Uyghur*. University of Washington Press.
4. <a id="src-phoible"></a>Moran, Steven & McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/)
5. <a id="src-wikipron"></a>Lee, Jackson L. et al. (2020). *WikiPron: A Tool for Extracting Pronunciation Data from Wiktionary*. LREC. [github.com](https://github.com/CUNY-CL/wikipron)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ug` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2644 | 0.0419 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ug` | generated | epitran-derived | CC0 1.0 | 40503 | 0.0864 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e ø | o |
| Open-mid | ɛ |  |
| Open |  | ɑ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ئ⟩ | [ʔ] | default [ʔ] · word initial ∅ |
| ⟨ا⟩ | [ɑ] |  |
| ⟨ب⟩ | [b] |  |
| ⟨ت⟩ | [t] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨خ⟩ | [χ] |  |
| ⟨د⟩ | [d] |  |
| ⟨ر⟩ | [r] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨غ⟩ | [ʁ] |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [q] |  |
| ⟨ك⟩ | [k] |  |
| ⟨ل⟩ | [l] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨و⟩ | [o] |  |
| ⟨ى⟩ | [i] |  |
| ⟨ي⟩ | [j] |  |
| ⟨پ⟩ | [p] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨ژ⟩ | [ʒ] |  |
| ⟨ک⟩ | [k] |  |
| ⟨ڭ⟩ | [ŋ] |  |
| ⟨گ⟩ | [ɡ] |  |
| ⟨ھ⟩ | [h] |  |
| ⟨ۆ⟩ | [ø] |  |
| ⟨ۇ⟩ | [u] |  |
| ⟨ۈ⟩ | [y] |  |
| ⟨ۋ⟩ | [w] [v] |  |
| ⟨ې⟩ | [e] |  |
| ⟨ە⟩ | [ɛ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ug")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Urdu](ur.md) · [Home](../index.md) · [Uzbek →](uz.md)
