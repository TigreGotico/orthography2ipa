# Danish (`da`)

<!-- atlas:summary begin -->
Danish is a North Germanic language, written in the Latin script. Glottolog places it in Denmark, Faroe Islands, Germany and Greenland. The `da` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `da` |
| Aliases | `dan` |
| ISO 639-3 | [dan](https://iso639-3.sil.org/code/dan), Danish |
| Glottolog | [dani1285](https://glottolog.org/resource/languoid/id/dani1285), Danish |
| Wikidata | [Q9035](https://www.wikidata.org/wiki/Q9035) |
| Wikipedia | [Danish language](https://en.wikipedia.org/wiki/Danish_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > North Germanic](by-family.md#indo-european--germanic--northwest-germanic--north-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Denmark](by-region.md#denmark), [Faroe Islands](by-region.md#faroe-islands), [Germany](by-region.md#germany), [Greenland](by-region.md#greenland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Ancestor | [Old Norse](https://tigregotico.github.io/orthography2ipa/#non) `non` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`da` in the data explorer](https://tigregotico.github.io/orthography2ipa/#da) |
| Spec file | [`da.json`](../../orthography2ipa/data/da.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Danish (rigsdansk). QUANTITY: a stressed vowel is long in an open syllable / before a single consonant and short before a consonant cluster or a doubled consonant letter, Danish itself has NO long consonants, so doubled letters are read as a single consonant (they only signal the preceding short vowel).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1998 to 2023. [Sources](#sources) lists them. The spec file writes all 63 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/da.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `da` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Danish (Copenhagen / Rigsdansk)](https://tigregotico.github.io/orthography2ipa/#da-x-copenhag) `da-x-copenhag`: skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-basboll2005"></a>Basbøll, H. (2005). *The Phonology of Danish*. Oxford University Press.
2. <a id="src-gronnum1998"></a>Grønnum, N. (1998). *Danish (Illustrations of the IPA)*. Journal of the International Phonetic Association 28(1-2): 99-105. Cited: 99-105. [doi.org](https://doi.org/10.1017/S0025100300006290)
3. <a id="src-gronnum2005"></a>Grønnum, N. (2005). *Fonetik og fonologi: Almen og dansk*. Akademisk Forlag. Cited: 308.
4. <a id="src-puggaardrode2023"></a>Puggaard-Rode, R. (2023). *Stop! Hey, what's that sound? The representation and realization of Danish stops*. LOT dissertation series, LOT, Amsterdam (Leiden University). Cited: 39-41, 45, 46, 58, 64, 111. [hdl.handle.net](https://hdl.handle.net/1887/3505668)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `da` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4331 | 0.3455 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `da` | generated | espeak-derived | CC BY 4.0 | 2233 | 0.4476 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 76 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː b̥ p pʰ pː |  |  | d dː d̥ t tʰ tː |  | k kʰ kː ɡ ɡː ɡ̊ |  |  |
| Nasal | m mː |  |  | n nː |  | ŋ |  |  |
| Fricative |  | f fː v vː | ð | s sː | ɕ |  | ʁ ʁː | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  |  | l lː |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː |  | u uː |
| Near-close | ɪ ʏ |  | ʊ |
| Close-mid | e eː ø øː |  | o oː |
| Mid |  | ə |  |
| Open-mid | œ ɛ ɛː |  | ɔ ɔː |
| Near-open | æ | ɐ ɐ̯ |  |
| Open | a aː |  | ɑ ɑː |

Sequences that the spec writes as one unit: [aj] [ew] [iɡ] [ks] [sb] [sd] [sɡ] [w] [ŋk] [ɑw] [ɔj].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [æ] [ɑː] | default [a] · nucleus stressed [aː] |
| ⟨aa⟩ | [ɔː] |  |
| ⟨au⟩ | [ɑw] |  |
| ⟨av⟩ | [ɑw] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [bː] |  |
| ⟨c⟩ | [k] [s] | before front vowel [s] · default [k] |
| ⟨ch⟩ | [ɕ] [k] |  |
| ⟨ck⟩ | [kː] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [dː] |  |
| ⟨e⟩ | [e] [ɛ] [ə] | default [ɛ] · nucleus stressed [eː] · nucleus unstressed [ə] |
| ⟨eg⟩ | [aj] |  |
| ⟨ej⟩ | [aj] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gg⟩ | [ɡː] |  |
| ⟨h⟩ | [h] |  |
| ⟨hj⟩ | [j] |  |
| ⟨hv⟩ | [v] |  |
| ⟨i⟩ | [i] [ɪ] | default [i] · nucleus stressed [iː] |
| ⟨ig⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨kj⟩ | [ɕ] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [o] [ɔ] | default [ɔ] · nucleus stressed [oː] |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [ʁ] |  |
| ⟨rr⟩ | [ʁː] |  |
| ⟨s⟩ | [s] |  |
| ⟨sj⟩ | [ɕ] |  |
| ⟨sk⟩ | [sɡ] | before front vowel [sɡ] · default [sɡ] |
| ⟨sp⟩ | [sb] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨st⟩ | [sd] |  |
| ⟨t⟩ | [t] |  |
| ⟨tj⟩ | [ɕ] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] [ʊ] | default [u] · nucleus stressed [uː] |
| ⟨v⟩ | [v] |  |
| ⟨vv⟩ | [vː] |  |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [y] [ʏ] | default [y] · nucleus stressed [yː] |
| ⟨z⟩ | [s] |  |
| ⟨å⟩ | [ɔ] [ɔː] | default [ɔ] · nucleus stressed [ɔː] |
| ⟨æ⟩ | [ɛ] [ɛː] | default [ɛ] · nucleus stressed [ɛː] |
| ⟨ø⟩ | [ø] [œ] | default [ø] · nucleus stressed [øː] |
| ⟨øg⟩ | [ɔj] |  |
| ⟨øj⟩ | [ɔj] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 49 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `DA_SCHWA_TO_A_BEFORE_R` | /ə/ → [ɐ], before [ʁ] | ⟨sanger⟩ [ˈsɑ.ŋɐ] | [Basbøll 2005](#src-basboll2005), [Puggaard-Rode 2023](#src-puggaardrode2023), Brink & Lund 1975 |
| `DA_R_ABSORBED_AFTER_SCHWA` | /ʁ/ → ∅, after [ə] | - | - |
| `DA_SCHWA_TO_A_AFTER_R` | /ə/ → [ɐ], after [ʁ] | ⟨store⟩ [ˈsdoːɐ] | - |
| `DA_R_ABSORBED_BEFORE_SCHWA` | /ʁ/ → ∅, after a vowel, before [ə] | ⟨rhotic-less⟩ [ˈkʰlætɐ] | [Puggaard-Rode 2023](#src-puggaardrode2023) |
| `DA_LOWER_I_BEFORE_NG` | /i iː/ → [e], before [ŋ] | ⟨ting⟩ [teŋ] | [Puggaard-Rode 2023](#src-puggaardrode2023) |
| `DA_LOWER_Y_BEFORE_NG` | /y yː/ → [ø], before [ŋ] | ⟨synge⟩ [ˈsøŋə] | - |
| `DA_LOWER_U_BEFORE_NG` | /u uː/ → [o], before [ŋ] | ⟨tung⟩ [toŋ] | - |
| `DA_LOWER_I_BEFORE_NASAL_CLUSTER` | /i iː/ → [e], before [n] [m], with more context in the spec | ⟨vinder⟩ [ˈvenɐ] | [Puggaard-Rode 2023](#src-puggaardrode2023) |
| `DA_LOWER_Y_BEFORE_NASAL_CLUSTER` | /y yː/ → [ø], before [n] [m], with more context in the spec | ⟨pynt⟩ [pønt] | - |
| `DA_LOWER_U_BEFORE_NASAL_CLUSTER` | /u uː/ → [o], before [n] [m], with more context in the spec | ⟨bunde⟩ [ˈbonə] | - |
| `DA_IG_FINAL_SHORT` | /iː/ → [i], word-finally, spelled ⟨ig⟩ | ⟨syndig⟩ [ˈsønti] | [Puggaard-Rode 2023](#src-puggaardrode2023) |
| `DA_IG_BEFORE_G_NOT_A_DIGRAPH` | /iː/ → [iɡ], spelled ⟨ig⟩, before ⟨g⟩ | ⟨ligge⟩ [ˈliɡə] | - |
| `DA_G_AFTER_IG_DELETE` | /ɡ/ → ∅, spelled ⟨g⟩, after ⟨ig⟩ | - | - |
| `DA_SHORTEN_A` | /aː/ → [a], before a consonant cluster | - | - |
| `DA_SHORTEN_E` | /eː/ → [ɛ], before a consonant cluster | - | - |
| `DA_SHORTEN_I` | /iː/ → [i], before a consonant cluster | - | - |
| `DA_SHORTEN_O` | /oː/ → [ɔ], before a consonant cluster | - | - |
| `DA_SHORTEN_U` | /uː/ → [u], before a consonant cluster | - | - |
| `DA_SHORTEN_Y` | /yː/ → [y], before a consonant cluster | - | - |
| `DA_SHORTEN_Æ` | /ɛː/ → [ɛ], before a consonant cluster | - | - |
| `DA_SHORTEN_Ø` | /øː/ → [ø], before a consonant cluster | - | - |
| `DA_SHORTEN_Å` | /ɔː/ → [ɔ], before a consonant cluster | - | - |
| `DA_A_RETRACT_AFTER_R_SHORT` | /a/ → [ɑ], after [ʁ] | ⟨fra⟩ [fʁɑ] | [Basbøll 2005](#src-basboll2005), [Grønnum 2005](#src-gronnum2005) |
| `DA_A_RETRACT_AFTER_R_LONG` | /aː/ → [ɑː], after [ʁ] | - | [Basbøll 2005](#src-basboll2005), [Grønnum 2005](#src-gronnum2005) |
| `DA_A_RETRACT_BEFORE_R_SHORT` | /a/ → [ɑ], before [ʁ] | ⟨har⟩ [hɑː] | [Basbøll 2005](#src-basboll2005), [Grønnum 2005](#src-gronnum2005) |
| `DA_A_RETRACT_BEFORE_R_LONG` | /aː/ → [ɑː], before [ʁ] | - | [Basbøll 2005](#src-basboll2005), [Grønnum 2005](#src-gronnum2005) |
| `DA_H_CODA_DELETE` | /h/ → ∅, not word-initially, in the coda | - | [Basbøll 2005](#src-basboll2005) |
| `DA_G_ELIDE` | /ɡ/ → ∅, not word-initially, before a vowel, after [iː] [eː] [ɛː] [aː] [ɑː] [yː] [øː] [uː] and 2 more, spelled ⟨g⟩ | ⟨tage⟩ [tæːə] | [Grønnum 2005](#src-gronnum2005) |
| `DA_SOFT_D_GEMINATE` | /dː/ → [ð], not word-initially, after a vowel | ⟨sidde⟩ [siðə] | [Basbøll 2005](#src-basboll2005), [Grønnum 2005](#src-gronnum2005) |
| `DA_DEGEM_B` | /bː/ → [b] | - | - |
| `DA_DEGEM_D` | /dː/ → [d] | - | - |
| `DA_DEGEM_F` | /fː/ → [f] | - | - |
| `DA_DEGEM_G` | /ɡː/ → [ɡ] | - | - |
| `DA_DEGEM_K` | /kː/ → [k] | - | - |
| `DA_DEGEM_L` | /lː/ → [l] | - | - |
| `DA_DEGEM_M` | /mː/ → [m] | - | - |
| `DA_DEGEM_N` | /nː/ → [n] | - | - |
| `DA_DEGEM_P` | /pː/ → [p] | - | - |
| `DA_DEGEM_R` | /ʁː/ → [ʁ] | - | - |
| `DA_DEGEM_S` | /sː/ → [s] | - | - |
| `DA_DEGEM_T` | /tː/ → [t] | - | - |
| `DA_DEGEM_V` | /vː/ → [v] | - | - |
| `DA_DEGEM_CK` | /kː/ → [k] | - | - |
| `DA_SOFT_D` | /d/ → [ð], not word-initially, after a vowel | - | - |
| `DA_SILENT_D` | /d/ → ∅, after [n] [l] [ʁ] | - | - |
| `DA_LEXICAL_LOWER_TIL` | /iː i/ → [e], stressed, in 1 listed words | ⟨til⟩ [ˈtel] | [Basbøll 2005](#src-basboll2005), [Grønnum 2005](#src-gronnum2005) |
| `DA_LEXICAL_LOWER_NUL` | /uː u/ → [o], stressed, in 1 listed words | ⟨nul⟩ [ˈnol] | [Basbøll 2005](#src-basboll2005), [Grønnum 2005](#src-gronnum2005) |
| `DA_LEXICAL_LOWER_KYS` | /yː y/ → [ø], stressed, in 1 listed words | ⟨kys⟩ [ˈkøs] | [Basbøll 2005](#src-basboll2005), [Grønnum 2005](#src-gronnum2005) |
| `DA_LEXICAL_LOWER_SOEN` | /øː ø/ → [œ], stressed, in 1 listed words | ⟨søn⟩ [ˈsœn] | [Basbøll 2005](#src-basboll2005), [Grønnum 2005](#src-gronnum2005) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "da")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Dangme](ada.md) · [Home](../index.md) · [Dargwa →](dar.md)
