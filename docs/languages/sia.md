# Akkala Sami (`sia`)

<!-- atlas:summary begin -->
Akkala Sami is a Saami language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `sia` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sia` |
| ISO 639-3 | [sia](https://iso639-3.sil.org/code/sia), Akkala Sami |
| Wikipedia | [Akkala Sami language](https://en.wikipedia.org/wiki/Akkala_Sami_language) |
| Family | [Uralic](by-family.md#uralic) > [Saami](by-family.md#uralic--saami) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Saami](https://tigregotico.github.io/orthography2ipa/#x-clade-saam1281) `x-clade-saam1281` |
| Explorer | [`sia` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sia) |
| Spec file | [`sia.json`](../../orthography2ipa/data/sia.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Akkala Sami is a Kola (Eastern) Saami language of the Uralic family, spoken in the Babino (Akkala) area of the Kola Peninsula, the last fluent speaker died in 2003, so every record of it is elicited fieldwork rather than living speech.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1987 to 2024. [Sources](#sources) lists them. The spec file writes all 53 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sia.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sia` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sia_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Akkala Saami (akka1237)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/akka1237)
2. <a id="src-sia_zajkov1987"></a>Zajkov, Petr M. (1987). *Babinskij dialekt saamskogo jazyka (fonologo-morfologicheskoe issledovanie)*. Karelian Branch of the USSR Academy of Sciences, Petrozavodsk. Cited: 28-56. [theswissbay.ch](https://theswissbay.ch/pdf/Books/Linguistics/Mega%20linguistics%20pack/Uralic/Saami%20(Akkala);%20%D0%91%D0%B0%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B4%D0%B8%D0%B0%D0%BB%D0%B5%D0%BA%D1%82%20%D1%81%D0%B0%D0%B0%D0%BC%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0%20(Zajkov).pdf)
3. <a id="src-sia_ksdp"></a>Rießler, M. et al. (Kola Saami Documentation Project) (2010). *Kola Saami: the language*. DoBeS / MPI Nijmegen. [dobes.mpi.nl](https://dobes.mpi.nl/projects/sami/language/)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sia` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 179 | 0.0948 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 66 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d dʲ t tʲ |  | c | k kʲ ɡ ɡʲ |  |
| Affricate |  |  | ts tsʲ | tʃ |  |  |  |
| Nasal | m mʲ |  | n |  | ɲ | ŋ ŋʲ |  |
| Trill |  |  | r rʲ |  |  |  |  |
| Fricative |  | f fʲ v vʲ | s sʲ z zʲ | ʃ ʒ | ɕ | x xʲ | h hʲ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l̥ ɫ |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ ɨː | u uː |
| Near-close | ɪ |  |  |
| Close-mid |  |  | o oː |
| Open-mid | ɛ ɛː |  | ɔ |
| Open | a |  | ɑ ɑː |

Sequences that the spec writes as one unit: [jo] [ju] [juː] [jɑ] [jɑː] [jɛ] [jɛː] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [ɑ] |  |
| ⟨а̄⟩ | [ɑː] |  |
| ⟨а̊⟩ | [ɔ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [jɛ] |  |
| ⟨е̄⟩ | [jɛː] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨к̌⟩ | [c] |  |
| ⟨л⟩ | [ɫ] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨о⟩ | [o] |  |
| ⟨о̄⟩ | [oː] |  |
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
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ы̄⟩ | [ɨː] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [ɛ] |  |
| ⟨э̄⟩ | [ɛː] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨ю̄⟩ | [juː] |  |
| ⟨я⟩ | [jɑ] |  |
| ⟨я̄⟩ | [jɑː] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ҍ⟩ | [ʲ] |  |
| ⟨һ⟩ | [h] |  |
| ⟨ӆ⟩ | [l̥] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӓ⟩ | [a] |  |
| ⟨ӣ⟩ | [iː] |  |
| ⟨ӭ⟩ | [ɛ] |  |
| ⟨ӯ⟩ | [uː] |  |
| ⟨ӹ⟩ | [ɪ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 26 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `SIA_PALAT_pʲ` | /p/ → [pʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_bʲ` | /b/ → [bʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_tʲ` | /t/ → [tʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_dʲ` | /d/ → [dʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_kʲ` | /k/ → [kʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_ɡʲ` | /ɡ/ → [ɡʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_fʲ` | /f/ → [fʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_vʲ` | /v/ → [vʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_sʲ` | /s/ → [sʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_zʲ` | /z/ → [zʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_xʲ` | /x/ → [xʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_hʲ` | /h/ → [hʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_mʲ` | /m/ → [mʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_ɲ` | /n/ → [ɲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_rʲ` | /r/ → [rʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_ʎ` | /ɫ/ → [ʎ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_tsʲ` | /ts/ → [tsʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_ŋʲ` | /ŋ/ → [ŋʲ], before [jɛ] [jɑ] [ju] [jo] [jɛː] [jɑː] [juː] [i] and 2 more | - | [Zajkov 1987](#src-sia_zajkov1987) |
| `SIA_PALAT_GEM_LATERAL` | /ɫ/ → [ʎ], before [ʎ] | - | - |
| `SIA_IOT_ABSORB_ɛ` | /jɛ/ → [ɛ], after a consonant | - | - |
| `SIA_IOT_ABSORB_ɑ` | /jɑ/ → [ɑ], after a consonant | - | - |
| `SIA_IOT_ABSORB_u` | /ju/ → [u], after a consonant | - | - |
| `SIA_IOT_ABSORB_o` | /jo/ → [o], after a consonant | - | - |
| `SIA_IOT_ABSORB_ɛː` | /jɛː/ → [ɛː], after a consonant | - | - |
| `SIA_IOT_ABSORB_ɑː` | /jɑː/ → [ɑː], after a consonant | - | - |
| `SIA_IOT_ABSORB_uː` | /juː/ → [uː], after a consonant | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sia")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Akan](ak.md) · [Home](../index.md) · [Akoose →](bss.md)
