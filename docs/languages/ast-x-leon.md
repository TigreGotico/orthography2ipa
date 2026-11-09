# Leonese (`ast-x-leon`)

<!-- atlas:summary begin -->
Leonese is an Asturleonese variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `ast-x-leon` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ast-x-leon` |
| ISO 639-3 | [ast](https://iso639-3.sil.org/code/ast), Asturian |
| Glottolog | [leon1250](https://glottolog.org/resource/languoid/id/leon1250), Leonese |
| Wikidata | [Q34108](https://www.wikidata.org/wiki/Q34108) |
| Wikipedia | [Leonese dialect](https://en.wikipedia.org/wiki/Leonese_dialect) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance > Asturleonese](by-family.md#indo-european--italic--romance--ibero-romance--asturleonese) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Parent | [Asturian](ast.md) `ast` |
| Child lects | 3, see [Related lects](#related-lects) |
| Explorer | [`ast-x-leon` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ast-x-leon) |
| Spec file | [`ast-x-leon.json`](../../orthography2ipa/data/ast-x-leon.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Medieval and modern Leonese (llingua llionesa / leonés). KEY GRAPHEME→PHONEME CORRESPONDENCES grounded in Morala & Egido (2009) and the Propuesta de Norma Ortográfica (anonymous, undated): (1) ⟨x⟩ = /ʃ/ (dorsopalatal fricative sorda, unanimous across all text models, Source B §2.3, Source A pp. 10, 15).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2003 to 2010. [Sources](#sources) lists them. The spec file writes 34 of the 61 spellings of its letter table and takes the other 27 from [Asturian](ast.md) `ast`.

The [spec file](../../orthography2ipa/data/ast-x-leon.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `ast-x-leon` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Medieval Asturian-Leonese of Portugal](https://tigregotico.github.io/orthography2ipa/#ast-PT-x-medieval) `ast-PT-x-medieval`: Portugal, research tier
- [Leonese](ast-ES-x-leon.md) `ast-ES-x-leon`: Spain, research tier
- [Sanabrese](ast-x-sanabria.md) `ast-x-sanabria`: research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-morala_egido2009"></a>Morala Rodríguez, J.R. & Egido Fernández, M.C. (2009). *A vueltas con una norma para el leonés*. Instituto Castellano y Leonés de la Lengua, Colección Beltenebros 23, in El Leonés en el siglo XXI. Cited: 209-241.
2. <a id="src-propuesta_norma_ortografica"></a>Anonymous (2010). *Propuesta de Norma Ortográfica para el Leonés: Hacia una codificación coherente, patrimonial y dialectalmente inclusiva*. Unpublished markdown document.
3. <a id="src-garcia_arias2003"></a>García Arias, X.Ll. (2003). *Gramática histórica de la lengua asturiana*. Academia de la Llingua Asturiana.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `ast-x-leon` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0856 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 62 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k kʲ ɡ |  |
| Affricate |  |  |  | d͡z ts t͡s | d͡ʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð | s̺ s̻ z z̺ z̻ | ʃ ʒ | ʝ | ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i i̯ | u u̯ |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [ja] [je] [jo] [ju] [oj] [ow] [w] [wa] [we] [wi] [wo] [ɟ͡ʝ] [ɡw] [ɡwe] [ɡwi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] | intervocalic [β] |
| ⟨c⟩ | [k] [t͡s] | before e [t͡s] · before i [t͡s] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | intervocalic [ð] |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | before e [ʒ] · before i [ʒ] · intervocalic [ɣ] |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨güe⟩ | [ɡwe] |  |
| ⟨güi⟩ | [ɡwi] |  |
| ⟨h⟩ | ∅ |  |
| ⟨h.⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [je] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [ju] |  |
| ⟨j⟩ | [ʒ] [d͡ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [ʎ] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] | before consonant [n] [ŋ] · word final [n] [ŋ] |
| ⟨nh⟩ | [ɲ] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨ou⟩ | [ow] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s̺] [z̺] | intervocalic [z̺] · word initial [s̺] |
| ⟨ss⟩ | [s̺] |  |
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
| ⟨z⟩ | [d͡z] [z̻] | intervocalic [d͡z] · word final [z̻] · word initial [d͡z] |
| ⟨á⟩ | [a] |  |
| ⟨ç⟩ | [t͡s] |  |
| ⟨é⟩ | [ɛ] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [ɔ] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ḥ⟩ | [h] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-l⟩ ⟨-d⟩ ⟨-z⟩ ⟨-x⟩ ⟨-t⟩ ⟨-n⟩ ⟨-m⟩ ⟨-f⟩. These endings take the penult: ⟨-s⟩ ⟨-ns⟩.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.

The spec switches off 16 inherited rules: `AST_GLIDE_I_RISING`, `AST_GLIDE_U_RISING`, `AST_GLIDE_I_FALLING`, `AST_GLIDE_U_FALLING`, `AST_SPIRANT_B`, `AST_SPIRANT_D`, `AST_SPIRANT_G`, `AST_SPIRANT_G_INITIAL`, `AST_AFFRICATE_Y_INITIAL`, `AST_TRILL_AFTER_L_N_S`, `AST_NASAL_LABIAL`, `AST_NASAL_VELAR`, `AST_NASAL_FINAL`, `AST_VOICE_S`, `AST_VOICE_THETA`, `AST_VOICE_SH`.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ast-x-leon")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Leonese](ast-ES-x-leon.md) · [Home](../index.md) · [Lezgian →](lez.md)
