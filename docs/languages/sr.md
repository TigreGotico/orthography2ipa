# Serbian (`sr`)

<!-- atlas:summary begin -->
Serbian is a South Slavic language, written in the Cyrillic script. Glottolog places it in 9 countries. The `sr` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sr` |
| ISO 639-3 | [srp](https://iso639-3.sil.org/code/srp), Serbian |
| Glottolog | [serb1264](https://glottolog.org/resource/languoid/id/serb1264), Serbian Standard |
| Wikidata | [Q9299](https://www.wikidata.org/wiki/Q9299) |
| Wikipedia | [Serbian language](https://en.wikipedia.org/wiki/Serbian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > South Slavic](by-family.md#indo-european--balto-slavic--slavic--south-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Albania](by-region.md#albania), [Bosnia & Herzegovina](by-region.md#bosnia--herzegovina), [Bulgaria](by-region.md#bulgaria), [Croatia](by-region.md#croatia), [Hungary](by-region.md#hungary), [Montenegro](by-region.md#montenegro), [North Macedonia](by-region.md#north-macedonia), [Romania](by-region.md#romania) and 1 more |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [South Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-sout3147) `x-clade-sout3147` |
| Explorer | [`sr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sr) |
| Spec file | [`sr.json`](../../orthography2ipa/data/sr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Serbian (Štokavian dialect, Ekavian variant in Serbia). Written in Cyrillic (primary) and Latin (Gaj) scripts. Four-accent system: short/long × falling/rising pitch accent. Two palatal affricate pairs: ⟨ћ/ć⟩ = [tɕ], ⟨ч/č⟩ = [tʃ], ⟨ђ/đ⟩ = [dʑ], ⟨џ/dž⟩ = [dʒ]. No vowel reduction (unlike Russian). Syllabic /r̩/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1993 to 1996. [Sources](#sources) lists them. The spec file writes all 60 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sr` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-browne_1993"></a>Browne, W. (1993). *Serbo-Croat*. in B. Comrie & G. Corbett (eds.), The Slavonic Languages.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `sr` | generated | epitran-derived | CC BY 4.0 | 9838 | 0.3232 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `sr` | generated | epitran-derived | CC0 1.0 | 3624 | 0.3298 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 32 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | ts | dʒ tʃ | dʑ tɕ |  |
| Nasal | m |  | n |  | ɲ | ŋ |
| Trill |  |  | r r̩ |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Open-mid | ɛ | ɔ |
| Open | a |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨dž⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lj⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nj⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [z] |  |
| ⟨ć⟩ | [tɕ] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨đ⟩ | [dʑ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |
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
| ⟨ђ⟩ | [dʑ] |  |
| ⟨ј⟩ | [j] |  |
| ⟨љ⟩ | [ʎ] |  |
| ⟨њ⟩ | [ɲ] |  |
| ⟨ћ⟩ | [tɕ] |  |
| ⟨џ⟩ | [dʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Senhaja de Srair](sjs.md) · [Home](../index.md) · [Serer →](srr.md)
