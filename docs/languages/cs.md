# Czech (`cs`)

<!-- atlas:summary begin -->
Czech is a West Slavic language, written in the Latin script. Glottolog places it in Austria, Czechia, Poland and Slovakia. The `cs` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `cs` |
| Aliases | `ces` |
| ISO 639-3 | [ces](https://iso639-3.sil.org/code/ces), Czech |
| Glottolog | [czec1258](https://glottolog.org/resource/languoid/id/czec1258), Czech |
| Wikidata | [Q9056](https://www.wikidata.org/wiki/Q9056) |
| Wikipedia | [Czech language](https://en.wikipedia.org/wiki/Czech_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > West Slavic](by-family.md#indo-european--balto-slavic--slavic--west-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Austria](by-region.md#austria), [Czechia](by-region.md#czechia), [Poland](by-region.md#poland), [Slovakia](by-region.md#slovakia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [West Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2792) `x-clade-west2792` |
| Explorer | [`cs` in the data explorer](https://tigregotico.github.io/orthography2ipa/#cs) |
| Spec file | [`cs.json`](../../orthography2ipa/data/cs.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Czech. Notable for the unique phoneme /r̝/ (⟨ř⟩) and systematic vowel length contrast. ⟨ch⟩ is the only official digraph and sorts as a separate letter. FINAL DEVOICING: obstruents devoice in coda/word-finally (b→p, d→t, ď→ť, g→k, v→f, z→s, ž→š, h→ch).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1993 to 1996. [Sources](#sources) lists them. The spec file writes all 56 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/cs.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `cs` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-short1993"></a>Short, D. (1993). *Czech*. in B. Comrie & G. Corbett (eds.), The Slavonic Languages.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `cs` | generated | epitran-derived | CC0 1.0 | 44148 | 0.0680 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 60 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c ɟ | k ɡ |  |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r r̝ r̝̊ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | ɦ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | iː | u uː |
| Near-close | ɪ |  |
| Close-mid |  | o oː |
| Open-mid | ɛ ɛː |  |
| Open | a aː |  |

Sequences that the spec writes as one unit: [au] [ciː] [cɛ] [cɪ] [diː] [dɪ] [eu] [jɛ] [ks] [kv] [mɲɛ] [niː] [nɪ] [ou] [tiː] [tɪ] [ɟiː] [ɟɛ] [ɟɪ] [ɲiː] [ɲɛ] [ɲɪ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨au⟩ | [au] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [ts] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨di⟩ | [ɟɪ] [dɪ] |  |
| ⟨dí⟩ | [ɟiː] [diː] |  |
| ⟨dě⟩ | [ɟɛ] |  |
| ⟨dž⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨eu⟩ | [eu] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] · word final [k] |
| ⟨h⟩ | [ɦ] | default [ɦ] · word final [x] |
| ⟨i⟩ | [ɪ] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mě⟩ | [mɲɛ] |  |
| ⟨n⟩ | [n] |  |
| ⟨ni⟩ | [ɲɪ] [nɪ] |  |
| ⟨ní⟩ | [ɲiː] [niː] |  |
| ⟨ně⟩ | [ɲɛ] |  |
| ⟨o⟩ | [o] |  |
| ⟨ou⟩ | [ou] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [kv] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ti⟩ | [cɪ] [tɪ] |  |
| ⟨tí⟩ | [ciː] [tiː] |  |
| ⟨tě⟩ | [cɛ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] | default [v] · word final [f] |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [ɪ] |  |
| ⟨z⟩ | [z] | default [z] · word final [s] |
| ⟨á⟩ | [aː] |  |
| ⟨é⟩ | [ɛː] |  |
| ⟨í⟩ | [iː] |  |
| ⟨ó⟩ | [oː] |  |
| ⟨ú⟩ | [uː] |  |
| ⟨ý⟩ | [iː] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ď⟩ | [ɟ] | default [ɟ] · word final [c] |
| ⟨ě⟩ | [jɛ] | after consonant [jɛ] · default [jɛ] |
| ⟨ň⟩ | [ɲ] |  |
| ⟨ř⟩ | [r̝] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ť⟩ | [c] |  |
| ⟨ů⟩ | [uː] |  |
| ⟨ž⟩ | [ʒ] | default [ʒ] · word final [ʃ] |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "cs")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Cypriot Maronite Arabic](acy.md) · [Home](../index.md) · [Dagbani →](dag.md)
