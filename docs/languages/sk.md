# Slovak (`sk`)

<!-- atlas:summary begin -->
Slovak is a West Slavic language, written in the Latin script. Glottolog places it in 7 countries. The `sk` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sk` |
| ISO 639-3 | [slk](https://iso639-3.sil.org/code/slk), Slovak |
| Glottolog | [slov1269](https://glottolog.org/resource/languoid/id/slov1269), Slovak |
| Wikidata | [Q9058](https://www.wikidata.org/wiki/Q9058) |
| Wikipedia | [Slovak language](https://en.wikipedia.org/wiki/Slovak_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > West Slavic](by-family.md#indo-european--balto-slavic--slavic--west-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Austria](by-region.md#austria), [Czechia](by-region.md#czechia), [Hungary](by-region.md#hungary), [Poland](by-region.md#poland), [Serbia](by-region.md#serbia), [Slovakia](by-region.md#slovakia), [Ukraine](by-region.md#ukraine) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [West Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2792) `x-clade-west2792` |
| Explorer | [`sk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sk) |
| Spec file | [`sk.json`](../../orthography2ipa/data/sk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Slovak. Close to Czech but distinct in several ways: ⟨h⟩ = [ɦ] (like Czech, not [h]), diphthongs ⟨ia ie iu ô⟩, syllabic liquids ⟨r l⟩ and their long counterparts ⟨ŕ ĺ⟩, rhythmic law: two consecutive long syllables not permitted (second long vowel shortens). Palatal consonant pair: ⟨ď ť⟩ = [ɟ c].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1993 to 1996. [Sources](#sources) lists them. The spec file writes all 61 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-short1993b"></a>Short, D. (1993). *Slovak*. in B. Comrie & G. Corbett (eds.), The Slavonic Languages.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sk` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 15893 | 0.1346 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `sk` | generated | epitran-derived | CC0 1.0 | 15944 | 0.0902 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 73 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c ɟ | k ɡ |  |
| Affricate |  |  | dz ts | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r r̩ r̩ː |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | ɦ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l lʲ l̩ l̩ː |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Open-mid | ɛ ɛː | ɔ ɔː |
| Near-open | æ |  |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ci] [ciː] [cɛ] [di] [diː] [dɛ] [iu] [iɐ] [iɛ] [ks] [kv] [li] [liː] [lɛ] [lʲi] [lʲiː] [lʲɛ] [ni] [niː] [nɛ] [ti] [tiː] [tɛ] [uɔ] [ɟi] [ɟiː] [ɟɛ] [ɲi] [ɲiː] [ɲɛ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] |  |
| ⟨de⟩ | [ɟɛ] [dɛ] |  |
| ⟨di⟩ | [ɟi] [di] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨dí⟩ | [ɟiː] [diː] |  |
| ⟨dž⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [ɦ] |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [iɐ] |  |
| ⟨ie⟩ | [iɛ] |  |
| ⟨iu⟩ | [iu] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨le⟩ | [lʲɛ] [lɛ] |  |
| ⟨li⟩ | [lʲi] [li] |  |
| ⟨lí⟩ | [lʲiː] [liː] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ne⟩ | [ɲɛ] [nɛ] |  |
| ⟨ni⟩ | [ɲi] [ni] |  |
| ⟨ní⟩ | [ɲiː] [niː] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [kv] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨te⟩ | [cɛ] [tɛ] |  |
| ⟨ti⟩ | [ci] [ti] |  |
| ⟨tí⟩ | [ciː] [tiː] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [i] |  |
| ⟨z⟩ | [z] |  |
| ⟨á⟩ | [aː] |  |
| ⟨ä⟩ | [ɛ] [æ] |  |
| ⟨é⟩ | [ɛː] |  |
| ⟨í⟩ | [iː] |  |
| ⟨ó⟩ | [ɔː] |  |
| ⟨ô⟩ | [uɔ] |  |
| ⟨ú⟩ | [uː] |  |
| ⟨ý⟩ | [iː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ď⟩ | [ɟ] |  |
| ⟨ĺ⟩ | [l̩ː] |  |
| ⟨ľ⟩ | [lʲ] |  |
| ⟨ň⟩ | [ɲ] |  |
| ⟨ŕ⟩ | [r̩ː] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ť⟩ | [c] |  |
| ⟨ž⟩ | [ʒ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Skolt Sami](sms.md) · [Home](../index.md) · [Slovenian →](sl.md)
