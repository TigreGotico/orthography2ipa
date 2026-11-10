# Asturian (`ast`)

<!-- atlas:summary begin -->
Asturian is an Asturleonese language, written in the Latin script. Glottolog places it in Portugal and Spain. The `ast` spec is at the research tier. It cites 5 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ast` |
| ISO 639-3 | [ast](https://iso639-3.sil.org/code/ast), Asturian |
| Glottolog | [astu1245](https://glottolog.org/resource/languoid/id/astu1245), Asturian-Leonese-Cantabrian |
| Wikidata | [Q29507](https://www.wikidata.org/wiki/Q29507) |
| Wikipedia | [Asturian language](https://en.wikipedia.org/wiki/Asturian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance > Asturleonese](by-family.md#indo-european--italic--romance--ibero-romance--asturleonese) |
| Region | [Eurasia](by-region.md#eurasia) > [Portugal](by-region.md#portugal), [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 900, living |
| Parent | [Asturleonese](https://tigregotico.github.io/orthography2ipa/#x-clade-astu1244) `x-clade-astu1244` |
| Child lects | 4, see [Related lects](#related-lects) |
| Explorer | [`ast` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ast) |
| Spec file | [`ast.json`](../../orthography2ipa/data/ast.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Asturian, spoken in the Principality of Asturias (Spain), as the Academia de la Llingua Asturiana (ALLA) writes it.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1994 to 2021. [Sources](#sources) lists them. The spec file writes all 64 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ast.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `ast` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Cantabrian](ast-x-cantabri.md) `ast-x-cantabri`: research tier
- [Leonese](ast-x-leon.md) `ast-x-leon`: research tier
- [Western Asturian-Leonese](ast-x-occident.md) `ast-x-occident`: research tier
- [Eastern Asturian-Leonese](ast-x-oriental.md) `ast-x-oriental`: research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 0 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-garcia_arias2003"></a>García Arias, X.Ll. (2003). *Gramática histórica de la lengua asturiana*. Academia de la Llingua Asturiana.
2. <a id="src-alarcos_llorach1994"></a>Alarcos Llorach, E. (1994). *Gramática de la Lengua Española*. Espasa.
3. <a id="src-penny2002"></a>Penny, R. (2002). *A History of the Spanish Language*. Cambridge University Press.
4. <a id="src-alla2021_normes"></a>Academia de la Llingua Asturiana (2021). *Normes Ortográfiques (8a edición revisada)*. Academia de la Llingua Asturiana, Uviéu. Cited: 13-47.
5. <a id="src-alla2001_gramatica"></a>Academia de la Llingua Asturiana (2001). *Gramática de la Llingua Asturiana (3a edición)*. Academia de la Llingua Asturiana, Uviéu. Cited: 16-68.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ast` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4169 | 0.0696 | yes |
| `spain_romance_tts` | `ast` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0334 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 57 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k kʲ ɡ |  |
| Affricate |  |  |  | ts | tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð θ | s s̺ z z̺ | ʃ ʒ | ʝ | ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i i̯ | u u̯ |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [ai̯] [au̯] [ei̯] [eu̯] [ja] [je] [jo] [ju] [oi̯] [ou̯] [w] [wa] [we] [wi] [wo] [ɟ͡ʝ] [ɡw].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai̯] |  |
| ⟨au⟩ | [au̯] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [θ] | before e [θ] · before i [θ] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ei̯] |  |
| ⟨eu⟩ | [eu̯] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨h⟩ | ∅ |  |
| ⟨h.⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [je] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [ju] |  |
| ⟨j⟩ | [ʝ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨l.l⟩ | [ʎ] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oi̯] |  |
| ⟨ou⟩ | [ou̯] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨qu'⟩ | [k] |  |
| ⟨quʼ⟩ | [k] |  |
| ⟨qu’⟩ | [k] |  |
| ⟨r⟩ | [ɾ] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [wi] |  |
| ⟨uo⟩ | [wo] |  |
| ⟨v⟩ | [b] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [ʝ] |  |
| ⟨yy⟩ | [kʲ] |  |
| ⟨z⟩ | [θ] |  |
| ⟨á⟩ | [a] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ü⟩ | [w] |  |
| ⟨ʼ⟩ | ∅ |  |
| ⟨ḥ⟩ | [h] |  |
| ⟨ḷḷ⟩ | [ʎ] |  |
| ⟨’⟩ | ∅ |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-al⟩ ⟨-el⟩ ⟨-il⟩ ⟨-ol⟩ ⟨-ul⟩ ⟨-d⟩ ⟨-z⟩ ⟨-x⟩ ⟨-t⟩ ⟨-m⟩ ⟨-f⟩ ⟨-b⟩ ⟨-c⟩ ⟨-g⟩ ⟨-j⟩ ⟨-k⟩ ⟨-p⟩ ⟨-v⟩ ⟨-w⟩. These endings take the penult: ⟨-s⟩ ⟨-ns⟩.

Whole-word exceptions (7): ⟨y⟩ [i], ⟨yla⟩ [ila], ⟨yles⟩ [iles], ⟨ylo⟩ [ilo], ⟨ylos⟩ [ilos], ⟨ylu⟩ [ilu], ⟨yos⟩ [ʝos].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 16 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AST_GLIDE_I_RISING` | /i/ → [j], before [a] [e] [o], spelled ⟨i⟩ | - | [Normes Ortográfiques 2021](#src-alla2021_normes), [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_GLIDE_U_RISING` | /u/ → [w], before [a] [e] [o], spelled ⟨u⟩ | - | [Normes Ortográfiques 2021](#src-alla2021_normes), [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_GLIDE_I_FALLING` | /i/ → [i̯], after [a] [e] [o], spelled ⟨i⟩ | - | [Normes Ortográfiques 2021](#src-alla2021_normes), [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_GLIDE_U_FALLING` | /u/ → [u̯], after [a] [e] [o], spelled ⟨u⟩ | - | [Normes Ortográfiques 2021](#src-alla2021_normes), [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_SPIRANT_B` | /b/ → [β], after [a] [e] [i] [o] [u] [j] [w] [i̯] and 25 more | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_SPIRANT_D` | /d/ → [ð], after [a] [e] [i] [o] [u] [j] [w] [i̯] and 23 more | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_SPIRANT_G` | /ɡ/ → [ɣ], after [a] [e] [i] [o] [u] [j] [w] [i̯] and 15 more | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_SPIRANT_G_INITIAL` | /ɡ/ → [ɣ], word-initially | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_AFFRICATE_Y_INITIAL` | /ʝ/ → [ɟ͡ʝ], word-initially | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_TRILL_AFTER_L_N_S` | /ɾ/ → [r], after [l] [n] [s] [z] | - | [Normes Ortográfiques 2021](#src-alla2021_normes), [Gramática de 2001](#src-alla2001_gramatica), ALLA 2021 |
| `AST_NASAL_LABIAL` | /n/ → [m], before [p] [b] [β] [m] | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_NASAL_VELAR` | /n/ → [ŋ], before [k] [ɡ] [ɣ] | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_NASAL_FINAL` | /n m/ → [ŋ], word-finally | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_VOICE_S` | /s/ → [z], before [b] [β] [d] [ð] [ɡ] [ɣ] [m] [n] and 8 more | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_VOICE_THETA` | /θ/ → [ð], before [b] [β] [d] [ð] [ɡ] [ɣ] [m] [n] and 8 more | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
| `AST_VOICE_SH` | /ʃ/ → [ʒ], before [b] [β] [d] [ð] [ɡ] [ɣ] [m] [n] and 8 more | - | [Gramática de 2001](#src-alla2001_gramatica), ALLA 2001 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ast")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Assyrian Neo-Aramaic](aii.md) · [Home](../index.md) · [Atayal →](tay.md)
