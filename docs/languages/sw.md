# Swahili (`sw`)

<!-- atlas:summary begin -->
Swahili is a Bantu language, written in the Latin script. Glottolog places it in 7 countries. The `sw` spec is at the research tier. It cites 6 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sw` |
| ISO 639-3 | [swh](https://iso639-3.sil.org/code/swh), Swahili (individual language) |
| Glottolog | [swah1253](https://glottolog.org/resource/languoid/id/swah1253), Swahili |
| Wikidata | [Q7838](https://www.wikidata.org/wiki/Q7838) |
| Wikipedia | [Swahili language](https://en.wikipedia.org/wiki/Swahili_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Burundi](by-region.md#burundi), [Kenya](by-region.md#kenya), [Mozambique](by-region.md#mozambique), [Rwanda](by-region.md#rwanda), [Somalia](by-region.md#somalia), [Tanzania](by-region.md#tanzania), [Uganda](by-region.md#uganda) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Proto-Bantu (family node)](https://tigregotico.github.io/orthography2ipa/#bnt) `bnt` |
| Explorer | [`sw` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sw) |
| Spec file | [`sw.json`](../../orthography2ipa/data/sw.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Swahili (Kiswahili). Bantu lingua franca of East Africa, official in Tanzania, Kenya, Uganda and the DRC.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1944 to 2023. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sw.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sw` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-nurse_hinnebusch1993"></a>Nurse, D. & Hinnebusch, T.J. (1993). *Swahili and Sabaki: A Linguistic History*. University of California Press.
2. <a id="src-ashton1944"></a>Ashton, E.O. (1944). *Swahili Grammar*. Longmans.
3. <a id="src-mkude2004"></a>Mkude, D., Mvungi, M. & Msanjila, Y. (2004). *Sarufi ya Kiswahili*. Oxford University Press Eastern Africa.
4. <a id="src-alsamaani2023"></a>Alsamaani, M. (2023). *The Voice-Onset Time of Arabic Loanwords in Swahili*. Migration Letters 20(8): 1225-1238. Cited: 1225-1238. [migrationletters.com](https://migrationletters.com/index.php/ml/article/download/5957/4047/16356)
5. <a id="src-awino2022"></a>Awino, E., Wanzare, L., Muchemi, L., Wanjawa, B., Ombui, E., Indede, F., McOnyango, O. & Okal, B. (2022). *Phonemic Representation and Transcription for Speech to Text Applications for Under-resourced Indigenous African Languages: The Case of Kiswahili*. arXiv:2210.16537. [arxiv.org](https://arxiv.org/pdf/2210.16537)
6. <a id="src-maddieson2003"></a>Maddieson, I. (2003). *The sounds of the Bantu languages (Chapter 2 of The Bantu Languages)*. Routledge. [escholarship.org](https://escholarship.org/content/qt7j1054t9/qt7j1054t9_noSplash_90db4831887d3125030fcfa443d2027e.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sw` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 307 | 0.2539 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `sw` | generated | machine-generated | MIT, each file its own | 48308 | 0.1608 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `sw` | generated | epitran-derived | CC0 1.0 | 48334 | 0.1286 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 43 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m m̩ |  |  | n n̩ |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | ð θ | s z | ʃ |  | x ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [mb] [mv] [nd] [ndʒ] [w] [ŋɡ] [ɓ] [ɗ] [ɠ] [ʄ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [ɓ] [b] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [ɗ] [d] |  |
| ⟨dh⟩ | [ð] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɠ] [ɡ] |  |
| ⟨gh⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʄ] [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [x] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] | before consonant [m̩] |
| ⟨mb⟩ | [mb] |  |
| ⟨mv⟩ | [mv] |  |
| ⟨n⟩ | [n] | before consonant [n̩] |
| ⟨nd⟩ | [nd] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨ng'⟩ | [ŋ] |  |
| ⟨nj⟩ | [ndʒ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [θ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sw")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Susu](sus.md) · [Home](../index.md) · [Swedish →](sv.md)
