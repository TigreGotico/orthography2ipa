# Indonesian (Bahasa Indonesia) (`id`)

<!-- atlas:summary begin -->
Indonesian (Bahasa Indonesia) is an Austronesian language, written in the Latin script. Glottolog places it in 6 countries. The `id` spec is at the research tier. It cites 3 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `id` |
| ISO 639-3 | [ind](https://iso639-3.sil.org/code/ind), Indonesian |
| Glottolog | [indo1316](https://glottolog.org/resource/languoid/id/indo1316), Standard Indonesian |
| Wikidata | [Q9240](https://www.wikidata.org/wiki/Q9240) |
| Wikipedia | [Indonesian language](https://en.wikipedia.org/wiki/Indonesian_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Indonesia](by-region.md#indonesia), [Netherlands](by-region.md#netherlands), [Philippines](by-region.md#philippines), [Saudi Arabia](by-region.md#saudi-arabia), [Singapore](by-region.md#singapore), [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Proto-Malayo-Polynesian (family node)](https://tigregotico.github.io/orthography2ipa/#poz) `poz` |
| Explorer | [`id` in the data explorer](https://tigregotico.github.io/orthography2ipa/#id) |
| Spec file | [`id.json`](../../orthography2ipa/data/id.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Indonesian (Bahasa Indonesia). Austronesian language (Malayo-Polynesian), official language of Indonesia. Based on Riau Malay, standardized from the 1920s. ~45 million L1 speakers, ~200 million L2. KEY FEATURES: (1) WORD-FINAL K: <k> in word-final position = [ʔ] (glottal stop), not [k].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1981 to 2003. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/id.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `id` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-sneddon2003"></a>Sneddon, J.N. (2003). *The Indonesian Language: Its History and Role in Modern Society*. University of New South Wales Press.
2. <a id="src-lapoliwa1981"></a>Lapoliwa, H. (1981). *A Generative Approach to the Phonology of Bahasa Indonesia*. Pacific Linguistics, ANU.
3. <a id="src-roosman2000"></a>Roosman, L. (2000). *Indonesian Phonology*. In: Facts about the World's Languages, H.W. Wilson.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `id` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 17965 | 0.1114 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `id` | generated | epitran-derived | CC BY 4.0 | 9646 | 0.1223 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `id` | generated | epitran-derived | CC0 1.0 | 13518 | 0.1312 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [aj] [aw] [ks] [oj] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ə] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] | intervocalic [h] ∅ · word final [h] ∅ · word initial [h] |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] [ʔ] | word final [ʔ] · word initial [k] |
| ⟨kh⟩ | [x] |  |
| ⟨l⟩ | [l] | word final [l] |
| ⟨m⟩ | [m] | word final [m] |
| ⟨n⟩ | [n] | word final [n] |
| ⟨ng⟩ | [ŋ] | word final [ŋ] · word initial [ŋ] |
| ⟨ny⟩ | [ɲ] | word initial [ɲ] |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] | intervocalic [r] · word final [r] |
| ⟨s⟩ | [s] | word final [s] |
| ⟨sy⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "id")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Inari Sami](smn.md) · [Home](../index.md) · [Ingrian →](izh.md)
