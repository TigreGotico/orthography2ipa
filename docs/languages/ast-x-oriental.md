# Eastern Asturian-Leonese (`ast-x-oriental`)

<!-- atlas:summary begin -->
Eastern Asturian-Leonese is an Asturleonese variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `ast-x-oriental` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ast-x-oriental` |
| ISO 639-3 | [ast](https://iso639-3.sil.org/code/ast), Asturian |
| Glottolog | [east2272](https://glottolog.org/resource/languoid/id/east2272), Eastern Asturian |
| Wikipedia | [Asturian language](https://en.wikipedia.org/wiki/Asturian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance > Asturleonese](by-family.md#indo-european--italic--romance--ibero-romance--asturleonese) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 900, living |
| Parent | [Asturian](ast.md) `ast` |
| Explorer | [`ast-x-oriental` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ast-x-oriental) |
| Spec file | [`ast-x-oriental.json`](../../orthography2ipa/data/ast-x-oriental.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Eastern Asturian-Leonese. Grounded in Morala & Egido (2009) and the Propuesta de Norma Ortográfica.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2003 to 2010. [Sources](#sources) lists them. The spec file writes no spelling of its own. It takes all 64 from [Asturian](ast.md) `ast`.

The [spec file](../../orthography2ipa/data/ast-x-oriental.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ast-x-oriental` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-morala_egido2009"></a>Morala Rodríguez, J.R. & Egido Fernández, M.C. (2009). *A vueltas con una norma para el leonés*. Instituto Castellano y Leonés de la Lengua, Colección Beltenebros 23. Cited: 209-241.
2. <a id="src-propuesta_norma_ortografica"></a>Anonymous (2010). *Propuesta de Norma Ortográfica para el Leonés*. Unpublished markdown document.
3. <a id="src-garcia_arias2003"></a>García Arias, X.Ll. (2003). *Gramática histórica de la lengua asturiana*. Academia de la Llingua Asturiana.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `ast-x-oriental` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0612 | no |
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
| `AST_GLIDE_I_RISING` | /i/ → [j], before [a] [e] [o], spelled ⟨i⟩ | - | ALLA 2001, ALLA 2021 |
| `AST_GLIDE_U_RISING` | /u/ → [w], before [a] [e] [o], spelled ⟨u⟩ | - | ALLA 2001, ALLA 2021 |
| `AST_GLIDE_I_FALLING` | /i/ → [i̯], after [a] [e] [o], spelled ⟨i⟩ | - | ALLA 2001, ALLA 2021 |
| `AST_GLIDE_U_FALLING` | /u/ → [u̯], after [a] [e] [o], spelled ⟨u⟩ | - | ALLA 2001, ALLA 2021 |
| `AST_SPIRANT_B` | /b/ → [β], after [a] [e] [i] [o] [u] [j] [w] [i̯] and 25 more | - | ALLA 2001 |
| `AST_SPIRANT_D` | /d/ → [ð], after [a] [e] [i] [o] [u] [j] [w] [i̯] and 23 more | - | ALLA 2001 |
| `AST_SPIRANT_G` | /ɡ/ → [ɣ], after [a] [e] [i] [o] [u] [j] [w] [i̯] and 15 more | - | ALLA 2001 |
| `AST_SPIRANT_G_INITIAL` | /ɡ/ → [ɣ], word-initially | - | ALLA 2001 |
| `AST_AFFRICATE_Y_INITIAL` | /ʝ/ → [ɟ͡ʝ], word-initially | - | ALLA 2001 |
| `AST_TRILL_AFTER_L_N_S` | /ɾ/ → [r], after [l] [n] [s] [z] | - | ALLA 2021, ALLA 2001 |
| `AST_NASAL_LABIAL` | /n/ → [m], before [p] [b] [β] [m] | - | ALLA 2001 |
| `AST_NASAL_VELAR` | /n/ → [ŋ], before [k] [ɡ] [ɣ] | - | ALLA 2001 |
| `AST_NASAL_FINAL` | /n m/ → [ŋ], word-finally | - | ALLA 2001 |
| `AST_VOICE_S` | /s/ → [z], before [b] [β] [d] [ð] [ɡ] [ɣ] [m] [n] and 8 more | - | ALLA 2001 |
| `AST_VOICE_THETA` | /θ/ → [ð], before [b] [β] [d] [ð] [ɡ] [ɣ] [m] [n] and 8 more | - | ALLA 2001 |
| `AST_VOICE_SH` | /ʃ/ → [ʒ], before [b] [β] [d] [ð] [ɡ] [ɣ] [m] [n] and 8 more | - | ALLA 2001 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ast-x-oriental")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Eastern Andalusian Spanish](es-ES-x-andalusi-e.md) · [Home](../index.md) · [Eastern Egyptian Bedawi Arabic →](avl-EG.md)
