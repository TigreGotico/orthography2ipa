# Lashi (`lsi`)

<!-- atlas:summary begin -->
Lashi is a Sino-Tibetan language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `lsi` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lsi` |
| ISO 639-3 | [lsi](https://iso639-3.sil.org/code/lsi), Lashi |
| Wikipedia | [Lashi language](https://en.wikipedia.org/wiki/Lashi_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Sino-Tibetan](https://tigregotico.github.io/orthography2ipa/#x-clade-sino1245) `x-clade-sino1245` |
| Explorer | [`lsi` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lsi) |
| Spec file | [`lsi.json`](../../orthography2ipa/data/lsi.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lashi (Lacid, Leqi) is a Burmish (Sino-Tibetan) language of Myanmar and Yunnan written in a Latin orthography devised in the 1970s.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 2011 to 2024. [Sources](#sources) lists them. The spec file writes all 54 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lsi.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lsi` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-lsi_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Lashi (lash1243)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/lash1243)
2. <a id="src-lsi_omniglot_chart"></a>Ager, Simon (Omniglot) (2024). *Lashi (Lacid) language and alphabet*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/lashi.htm)
3. <a id="src-lsi_luk2017"></a>Hkaw Luk (2017). *A grammatical sketch of Lacid*. MA thesis, Payap University, Chiang Mai. Cited: 3-4, 13-18, 183. [drive.google.com](https://drive.google.com/file/d/1ySgqYFe3Lwk2JNY5-EsV7ArywPXCrIG5/view)
4. <a id="src-lsi_wannemacher2011"></a>Wannemacher, Mark (2011). *A phonological overview of the Lacid language*. Linguistics Institute, Payap University, Chiang Mai.
5. <a id="src-lsi_noftz2017"></a>Noftz, Robert (2017). *A literature review on segments in Lacid (Lashi)*. Payap University.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `lsi` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 96 | 0.4222 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 75 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ p̚ |  | d t tʰ t̚ |  |  | k kʰ k̚ ɡ | ʔ |
| Affricate |  |  | d͡z t͡s t͡sʰ | t͡ʃ t͡ʃʰ | d͡ʑ t͡ɕ t͡ɕʰ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s | ʃ | ɕ | ɣ | h |
| Approximant |  |  | ɹ |  | j | ɰ |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e ø |  | o |
| Mid |  | ə |  |
| Open-mid |  |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [aj] [aw] [a̰j] [a̰w] [kʰj] [oj] [ow] [o̰j] [o̰w] [w] [wa] [wa̰] [we] [wi] [wḛ] [wḭ] [ʔa] [ʔaj] [ʔaw] [ʔe] [ʔi] [ʔo] [ʔoj] [ʔow] [ʔu] [ʔø] [ʔɔ] [ʔɨ] [̰].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | word initial [ʔa] |
| ⟨ai⟩ | [aj] | word initial [ʔaj] |
| ⟨au⟩ | [aw] | word initial [ʔaw] |
| ⟨b⟩ | [b] [p] |  |
| ⟨c⟩ | [t͡ɕʰ] [t͡ʃʰ] |  |
| ⟨d⟩ | [d] [t] |  |
| ⟨e⟩ | [e] | word initial [ʔe] |
| ⟨ei⟩ | [ɨ] [ə] | word initial [ʔɨ] |
| ⟨eu⟩ | [ɨ] [ə] | word initial [ʔɨ] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [k] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] | word initial [ʔi] |
| ⟨j⟩ | [d͡ʑ] [t͡ʃ] |  |
| ⟨jh⟩ | [t͡ɕ] [t͡ʃ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨kyh⟩ | [kʰj] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mh⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngh⟩ | [ŋ] |  |
| ⟨nh⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨nyh⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] [o] | word initial [ʔɔ] |
| ⟨oe⟩ | [ø] [o] | word initial [ʔø] |
| ⟨oi⟩ | [oj] | word initial [ʔoj] |
| ⟨oo⟩ | [o] | word initial [ʔo] |
| ⟨ou⟩ | [ow] | word initial [ʔow] |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨q⟩ | [ɣ] [ɰ] |  |
| ⟨r⟩ | [ɹ] [r] |  |
| ⟨rh⟩ | [ɹ] [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ɕ] [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨u⟩ | [u] | word initial [ʔu] |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [wi] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [t͡sʰ] |  |
| ⟨y⟩ | [j] |  |
| ⟨yh⟩ | [j] |  |
| ⟨z⟩ | [d͡z] [t͡s] |  |
| ⟨zh⟩ | [t͡s] |  |
| ⟨ʼ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 23 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `lsi-checked-coda-b` | /b/ → [p̚], before a consonant, with more context in the spec | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-checked-final-b` | /b/ → [p̚], word-finally | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-checked-coda-d` | /d/ → [t̚], before a consonant, with more context in the spec | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-checked-final-d` | /d/ → [t̚], word-finally | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-checked-coda-g` | /ɡ/ → [k̚], before a consonant, with more context in the spec | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-checked-final-g` | /ɡ/ → [k̚], word-finally | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-zero-initial-glottal` | insert [ʔ] after /a e i o ɔ u ɨ ø ʔa ʔe ʔi ʔo ʔɔ ʔu ʔɨ ʔø ʔaj ʔoj ʔaw ʔow/, before a vowel | ⟨Noa⟩ [nɔʔa] | - |
| `lsi-o-closed-syllable` | /ɔ/ → [o], before a coda, with more context in the spec | ⟨loo⟩ [lo] | - |
| `lsi-o-closed-syllable-zero-initial` | /ʔɔ/ → [ʔo], before a coda, with more context in the spec | ⟨og⟩ [ʔok] | - |
| `lsi-unreleased-coda-p` | /p/ → [p̚], before a consonant, with more context in the spec | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-unreleased-final-p` | /p/ → [p̚], word-finally | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-unreleased-coda-t` | /t/ → [t̚], before a consonant, with more context in the spec | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-unreleased-final-t` | /t/ → [t̚], word-finally | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-unreleased-coda-k` | /k/ → [k̚], before a consonant, with more context in the spec | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-unreleased-final-k` | /k/ → [k̚], word-finally | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-creaky-after-glottalised-sonorant` | insert [̰] after /a e i o ɔ u ø ɨ ə/, after ⟨mh⟩ ⟨nh⟩ ⟨nyh⟩ ⟨ngh⟩ ⟨lh⟩ ⟨rh⟩ ⟨yh⟩ | - | [Hkaw 2017](#src-lsi_luk2017) |
| `lsi-creaky-after-glottalised-sonorant-aj` | /aj/ → [a̰j], after ⟨mh⟩ ⟨nh⟩ ⟨nyh⟩ ⟨ngh⟩ ⟨lh⟩ ⟨rh⟩ ⟨yh⟩ | - | - |
| `lsi-creaky-after-glottalised-sonorant-oj` | /oj/ → [o̰j], after ⟨mh⟩ ⟨nh⟩ ⟨nyh⟩ ⟨ngh⟩ ⟨lh⟩ ⟨rh⟩ ⟨yh⟩ | - | - |
| `lsi-creaky-after-glottalised-sonorant-aw` | /aw/ → [a̰w], after ⟨mh⟩ ⟨nh⟩ ⟨nyh⟩ ⟨ngh⟩ ⟨lh⟩ ⟨rh⟩ ⟨yh⟩ | - | - |
| `lsi-creaky-after-glottalised-sonorant-ow` | /ow/ → [o̰w], after ⟨mh⟩ ⟨nh⟩ ⟨nyh⟩ ⟨ngh⟩ ⟨lh⟩ ⟨rh⟩ ⟨yh⟩ | - | - |
| `lsi-creaky-after-glottalised-sonorant-wi` | /wi/ → [wḭ], after ⟨mh⟩ ⟨nh⟩ ⟨nyh⟩ ⟨ngh⟩ ⟨lh⟩ ⟨rh⟩ ⟨yh⟩ | - | - |
| `lsi-creaky-after-glottalised-sonorant-we` | /we/ → [wḛ], after ⟨mh⟩ ⟨nh⟩ ⟨nyh⟩ ⟨ngh⟩ ⟨lh⟩ ⟨rh⟩ ⟨yh⟩ | - | - |
| `lsi-creaky-after-glottalised-sonorant-wa` | /wa/ → [wa̰], after ⟨mh⟩ ⟨nh⟩ ⟨nyh⟩ ⟨ngh⟩ ⟨lh⟩ ⟨rh⟩ ⟨yh⟩ | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lsi")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lapurdian Basque](eu-x-lapurdi.md) · [Home](../index.md) · [Latgalian →](ltg.md)
