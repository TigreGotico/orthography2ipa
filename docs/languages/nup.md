# Nupe (`nup`)

<!-- atlas:summary begin -->
Nupe is an Atlantic-Congo language, written in the Latin script. Glottolog places it in the Africa and North America macroareas. The `nup` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nup` |
| Wikipedia | [Nupe language](https://en.wikipedia.org/wiki/Nupe_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#several-macroareas), [North America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`nup` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nup) |
| Spec file | [`nup.json`](../../orthography2ipa/data/nup.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Nupe (Nupe-Nupe-Tako), a Nupoid (Volta-Niger, Atlantic-Congo) language of Niger and Kwara States, central Nigeria. ORTHOGRAPHY: Latin-based, 24 base letters (a b c d e f g h i j k l m n o p r s t u v w y z) plus the digraphs dz, gb, kp, sh, ts and zh.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1915 to 2013. [Sources](#sources) lists them. The spec file writes all 30 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nup.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nup` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-banfield1915"></a>Banfield, Alexander W. and Macintyre, John Lester (1915). *A Grammar of the Nupe Language, Together with a Vocabulary*. London: Society for Promoting Christian Knowledge. Cited: 14-17. [archive.org](https://archive.org/details/grammarofnupelan00banfrich)
2. <a id="src-blench_nupoid"></a>Blench, Roger M. (2013). *Oral literature genres of the Nupe of Central Nigeria*. Kay Williamson Educational Foundation. Cited: 5-6. [web.archive.org](https://web.archive.org/web/20150421033828/http://www.rogerblench.info/Language/Niger-Congo/VN/Nupoid/Nupe%20oral%20literature%20genres.pdf)
3. <a id="src-kawu_2002_dissertation"></a>Kawu, Ahmadu Ndanusa (2002). *Variation in Nupe Phonology and Morphology*. Rutgers, The State University of New Jersey (PhD dissertation). [rucore.libraries.rutgers.edu](https://rucore.libraries.rutgers.edu/rutgers-lib/26097/)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nup` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 393 | 0.3979 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 82 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ bʷ p pʲ pʷ |  | d dʲ dʷ t tʲ tʷ |  |  | k kʲ kʷ ɡ ɡʲ ɡʷ |  |
| Affricate |  |  | d͡z d͡zʲ d͡zʷ t͡s t͡sʲ t͡sʷ | d͡ʒ d͡ʒʲ d͡ʒʷ t͡ʃ t͡ʃʲ t͡ʃʷ |  |  |  |
| Nasal | m mʲ mʷ |  | n nʲ nʷ |  |  | ŋ |  |
| Tap |  |  | ɾ ɾʲ ɾʷ |  |  |  |  |
| Fricative |  | f fʲ fʷ v vʲ vʷ | s sʲ sʷ z zʲ zʷ | ʃ ʃʲ ʃʷ ʒ ʒʲ ʒʷ |  |  | h hʲ hʷ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l lʲ lʷ |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i ĩ | u ũ |
| Close-mid | e ẽ | o õ |
| Open | a ã |  |

Sequences that the spec writes as one unit: [k͡p] [k͡pʲ] [k͡pʷ] [w] [ɡ͡b] [ɡ͡bʲ] [ɡ͡bʷ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [t͡ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dz⟩ | [d͡z] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [d͡ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kp⟩ | [k͡p] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [t͡s] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 69 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NUP_LABIAL_b` | /b/ → [bʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_t͡ʃ` | /t͡ʃ/ → [t͡ʃʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_d` | /d/ → [dʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_d͡z` | /d͡z/ → [d͡zʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_f` | /f/ → [fʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_ɡ` | /ɡ/ → [ɡʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_ɡ͡b` | /ɡ͡b/ → [ɡ͡bʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_h` | /h/ → [hʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_d͡ʒ` | /d͡ʒ/ → [d͡ʒʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_k` | /k/ → [kʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_k͡p` | /k͡p/ → [k͡pʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_l` | /l/ → [lʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_m` | /m/ → [mʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_n` | /n/ → [nʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_p` | /p/ → [pʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_ɾ` | /ɾ/ → [ɾʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_s` | /s/ → [sʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_ʃ` | /ʃ/ → [ʃʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_t` | /t/ → [tʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_t͡s` | /t͡s/ → [t͡sʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_v` | /v/ → [vʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_z` | /z/ → [zʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_LABIAL_ʒ` | /ʒ/ → [ʒʷ], before [w] | - | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_b` | /b/ → [bʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_t͡ʃ` | /t͡ʃ/ → [t͡ʃʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_d` | /d/ → [dʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_d͡z` | /d͡z/ → [d͡zʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_f` | /f/ → [fʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_ɡ` | /ɡ/ → [ɡʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_ɡ͡b` | /ɡ͡b/ → [ɡ͡bʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_h` | /h/ → [hʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_d͡ʒ` | /d͡ʒ/ → [d͡ʒʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_k` | /k/ → [kʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_k͡p` | /k͡p/ → [k͡pʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_l` | /l/ → [lʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_m` | /m/ → [mʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_n` | /n/ → [nʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_p` | /p/ → [pʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_ɾ` | /ɾ/ → [ɾʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_s` | /s/ → [sʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_ʃ` | /ʃ/ → [ʃʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_t` | /t/ → [tʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_t͡s` | /t͡s/ → [t͡sʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_v` | /v/ → [vʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_z` | /z/ → [zʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_PALATAL_ʒ` | /ʒ/ → [ʒʲ], before [j] | - | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_W_ABSORB` | /w/ → ∅, after a consonant | - | - |
| `NUP_Y_ABSORB` | /j/ → ∅, after a consonant | - | - |
| `NUP_N_DELETE_FINAL` | /n/ → ∅, word-finally, after a vowel | ⟨dazan⟩ [dāzã̀] | [Banfield 1915](#src-banfield1915), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_N_DELETE_PRENASAL` | /n/ → ∅, after a vowel, before [n] [m] | ⟨tanmako⟩ [tã̀mã̄kō] | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_M_DELETE_FINAL` | /m/ → ∅, word-finally, after a vowel | ⟨dazan⟩ [dāzã̀] | [Banfield 1915](#src-banfield1915), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_M_DELETE_PRENASAL` | /m/ → ∅, after a vowel, before [n] [m] | ⟨tanmako⟩ [tã̀mã̄kō] | [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_N_SYLLABIC` | /n/ → [ŋ], before [b] [t͡ʃ] [d] [d͡z] [f] [ɡ] [ɡ͡b] [h] and 15 more | ⟨dangi⟩ [dàŋ̀ɡī] | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_M_SYLLABIC` | /m/ → [ŋ], before [b] [t͡ʃ] [d] [d͡z] [f] [ɡ] [ɡ͡b] [h] and 15 more | ⟨dangi⟩ [dàŋ̀ɡī] | [Blench 2013](#src-blench_nupoid), [Kawu 2002](#src-kawu_2002_dissertation) |
| `NUP_NASAL_SPREAD_A` | /a/ → [ã], after [n] [m] | ⟨namba⟩ [nã̀ŋ̀bà] | [Kawu 2002](#src-kawu_2002_dissertation), Ladefoged & Maddieson 1996 |
| `NUP_NASAL_FINAL_A` | /a/ → [ã], before [n] [m], with more context in the spec | - | - |
| `NUP_NASAL_PRENASAL_A` | /a/ → [ã], before [n] [m], with more context in the spec | ⟨tanmako⟩ [tã̀mã̄kō] | - |
| `NUP_NASAL_SPREAD_E` | /e/ → [ẽ], after [n] [m] | - | [Kawu 2002](#src-kawu_2002_dissertation), Ladefoged & Maddieson 1996 |
| `NUP_NASAL_FINAL_E` | /e/ → [ẽ], before [n] [m], with more context in the spec | - | - |
| `NUP_NASAL_PRENASAL_E` | /e/ → [ẽ], before [n] [m], with more context in the spec | - | - |
| `NUP_NASAL_SPREAD_I` | /i/ → [ĩ], after [n] [m] | ⟨ani⟩ [ānĩ́] | [Kawu 2002](#src-kawu_2002_dissertation), Ladefoged & Maddieson 1996 |
| `NUP_NASAL_FINAL_I` | /i/ → [ĩ], before [n] [m], with more context in the spec | - | - |
| `NUP_NASAL_PRENASAL_I` | /i/ → [ĩ], before [n] [m], with more context in the spec | - | - |
| `NUP_NASAL_SPREAD_O` | /o/ → [õ], after [n] [m] | - | [Kawu 2002](#src-kawu_2002_dissertation), Ladefoged & Maddieson 1996 |
| `NUP_NASAL_FINAL_O` | /o/ → [õ], before [n] [m], with more context in the spec | - | - |
| `NUP_NASAL_PRENASAL_O` | /o/ → [õ], before [n] [m], with more context in the spec | - | - |
| `NUP_NASAL_SPREAD_U` | /u/ → [ũ], after [n] [m] | - | [Kawu 2002](#src-kawu_2002_dissertation), Ladefoged & Maddieson 1996 |
| `NUP_NASAL_FINAL_U` | /u/ → [ũ], before [n] [m], with more context in the spec | - | - |
| `NUP_NASAL_PRENASAL_U` | /u/ → [ũ], before [n] [m], with more context in the spec | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nup")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nuosu](ii.md) · [Home](../index.md) · [Occitan →](oc.md)
