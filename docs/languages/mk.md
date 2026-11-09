# Macedonian (`mk`)

<!-- atlas:summary begin -->
Macedonian is a South Slavic language, written in the Cyrillic script. Glottolog places it in 5 countries. The `mk` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mk` |
| ISO 639-3 | [mkd](https://iso639-3.sil.org/code/mkd), Macedonian |
| Glottolog | [mace1250](https://glottolog.org/resource/languoid/id/mace1250), Macedonian |
| Wikidata | [Q9296](https://www.wikidata.org/wiki/Q9296) |
| Wikipedia | [Macedonian language](https://en.wikipedia.org/wiki/Macedonian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > South Slavic](by-family.md#indo-european--balto-slavic--slavic--south-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Albania](by-region.md#albania), [Bulgaria](by-region.md#bulgaria), [Greece](by-region.md#greece), [North Macedonia](by-region.md#north-macedonia), [Serbia](by-region.md#serbia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [South Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-sout3147) `x-clade-sout3147` |
| Explorer | [`mk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mk) |
| Spec file | [`mk.json`](../../orthography2ipa/data/mk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Macedonian, codified 1945. South Slavic, closely related to Bulgarian. Analytic case system (lost inflection). Fixed antepenultimate stress (third-from-last syllable). Unique letters: ⟨ѕ⟩ = [dz], ⟨ѓ⟩ = [ɟ], ⟨ќ⟩ = [c].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1993 to 2001. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-friedman2001"></a>Friedman, V.A. (2001). *Macedonian*. Lincom Europa.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `mk` | generated | epitran-derived | CC0 1.0 | 10750 | 0.0221 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c ɟ | k ɡ |
| Affricate |  |  | dz ts | dʒ tʃ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |
| Trill |  |  | r r̩ |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Open-mid | ɛ |  | ɔ |
| Near-open |  | ɐ |  |
| Open | a |  |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [ɛ] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [ɔ] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨ѓ⟩ | [ɟ] |  |
| ⟨ѕ⟩ | [dz] |  |
| ⟨ј⟩ | [j] |  |
| ⟨љ⟩ | [ʎ] |  |
| ⟨њ⟩ | [ɲ] |  |
| ⟨ќ⟩ | [c] |  |
| ⟨џ⟩ | [dʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Luxembourgish](lb.md) · [Home](../index.md) · [Madurese →](mad.md)
