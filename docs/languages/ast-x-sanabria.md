# Sanabrese (`ast-x-sanabria`)

<!-- atlas:summary begin -->
Sanabrese is an Asturleonese variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `ast-x-sanabria` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ast-x-sanabria` |
| ISO 639-3 | [ast](https://iso639-3.sil.org/code/ast), Asturian |
| Wikipedia | [Asturian language](https://en.wikipedia.org/wiki/Asturian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance > Asturleonese](by-family.md#indo-european--italic--romance--ibero-romance--asturleonese) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Parent | [Leonese](ast-x-leon.md) `ast-x-leon` |
| Explorer | [`ast-x-sanabria` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ast-x-sanabria) |
| Spec file | [`ast-x-sanabria.json`](../../orthography2ipa/data/ast-x-sanabria.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Sanabrese (Sanabrés), Asturleonese occidental spoken in the Sanabria comarca (Zamora, Spain) and Portuguese-side sub-zones (Guadramil, Rio de Onor). Classified as hablas de Sanabria within Asturleonese occidental (Frías-Conde, El Habla de Sanabria, p. 2).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2003 to 2005. [Sources](#sources) lists them. The spec file writes 16 of the 61 spellings of its letter table and takes the other 45 from [Leonese](ast-x-leon.md) `ast-x-leon`.

The [spec file](../../orthography2ipa/data/ast-x-sanabria.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ast-x-sanabria` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 0 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-frias_conde_sanabria"></a>Frías-Conde, Xavier (2005). *El Habla de Sanabria*. CES Don Bosco (UCM), ISR Romania Minor (conference/seminar handout, 7 pp.). Cited: 1-7.
2. <a id="src-garcia_arias2003"></a>García Arias, X.Ll. (2003). *Gramática histórica de la lengua asturiana*. Academia de la Llingua Asturiana.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `ast-x-sanabria` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.1236 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 64 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k kʲ ɡ |  |
| Affricate |  |  |  | d͡z ts t͡s | d͡ʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð θ | s s̺ s̻ z z̺ z̻ | ʃ ʒ | ʝ | ɣ | h |
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
| ⟨c⟩ | [k] [θ] | before e [θ] · before i [θ] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | intervocalic [ð] |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] | word initial [f] |
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
| ⟨ll⟩ | [ʎ] | word initial [ʎ] |
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
| ⟨s⟩ | [s] |  |
| ⟨ss⟩ | [s] |  |
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
| ⟨ç⟩ | [θ] |  |
| ⟨é⟩ | [ɛ] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] | word initial [ɲ] |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ast-x-sanabria")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Samogitian](sgs.md) · [Home](../index.md) · [Sango →](sg.md)
