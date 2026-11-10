# Rionorese (`ast-PT-x-rionor`)

<!-- atlas:summary begin -->
Rionorese is an Asturleonese variety, written in the Latin script. Its code names Portugal. The `ast-PT-x-rionor` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ast-PT-x-rionor` |
| ISO 639-3 | [ast](https://iso639-3.sil.org/code/ast), Asturian |
| Wikipedia | [Rio de Onor](https://en.wikipedia.org/wiki/Rio_de_Onor) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance > Asturleonese](by-family.md#indo-european--italic--romance--ibero-romance--asturleonese) |
| Region | [Eurasia](by-region.md#eurasia) > [Portugal](by-region.md#portugal) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Ancestor | [Medieval Asturian-Leonese of Portugal](https://tigregotico.github.io/orthography2ipa/#ast-PT-x-medieval) `ast-PT-x-medieval` |
| Explorer | [`ast-PT-x-rionor` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ast-PT-x-rionor) |
| Spec file | [`ast-PT-x-rionor.json`](../../orthography2ipa/data/ast-PT-x-rionor.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Rionorese (Rionorês), the nearly-extinct Asturleonese variety spoken in Rio de Onor (PT) / Rihonor de Castilla (ES), straddling the Portuguese-Spanish border in Trás-os-Montes. Fewer than 100 elderly speakers as of the early 2000s (Macias 2003). Grounded in Macias (2003) and Carvalho & Dias (1955).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1900 to 2005. [Sources](#sources) lists them. The spec file writes 52 of the 78 spellings of its letter table and takes the other 26 from [Medieval Asturian-Leonese of Portugal](https://tigregotico.github.io/orthography2ipa/#ast-PT-x-medieval) `ast-PT-x-medieval`.

The [spec file](../../orthography2ipa/data/ast-PT-x-rionor.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ast-PT-x-rionor` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-macias2003"></a>Macias, Dina Rodrigues (2003). *Dialecto rionorês: Contributo para o seu estudo*. Instituto Politécnico de Bragança, Série Estudos 64.
2. <a id="src-carvalho_dias1955"></a>Carvalho, José Herculano de & Dias, Jorge (1955). *O Falar de Rio de Onor*. I.E.E.D., Faculdade de Letras, Coimbra.
3. <a id="src-frias_conde_sanabria"></a>Frías-Conde, Xavier (2005). *El Habla de Sanabria*. CES Don Bosco (UCM), ISR Romania Minor. Cited: p. 4.
4. <a id="src-vasconcelos1900"></a>Vasconcelos, J. Leite de (1900). *Estudos de Philologia Mirandesa (Vol. II)*. Imprensa Nacional, Lisboa. Cited: 54. [archive.org](https://archive.org/details/estudosdephilolo02vascuoft)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `portuguese_tts` | `ast-PT-x-rionor` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.2429 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 71 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k kʲ ɡ |  |
| Affricate |  |  |  | d͡z ts | d͡ʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð | s s̺ z z̺ | ʃ ʒ | ʝ | x ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i i̯ ĩ |  | u u̯ ũ |
| Close-mid | e ẽ |  | o õ |
| Open-mid | ɛ |  | ɔ |
| Near-open |  | ɐ̃ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [ja] [je] [jo] [ju] [kw] [oj] [ow] [uj] [w] [wa] [we] [wo] [wɐ] [wɔ] [õj̃] [ɐ̃w̃] [ɟ͡ʝ] [ɡw] [ɡwe] [ɡwi].
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
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] |
| ⟨ch⟩ | [ʃ] |  |
| ⟨d⟩ | [d] | intervocalic [ð] |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] | intervocalic [f] · word initial [f] |
| ⟨g⟩ | [ɡ] [x] | before e [x] · before i [x] |
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
| ⟨iê⟩ | [je] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] | onset [l] |
| ⟨lh⟩ | [ʎ] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nh⟩ | [ɲ] |  |
| ⟨o⟩ | [o] | word final [u] |
| ⟨oi⟩ | [oj] |  |
| ⟨ou⟩ | [ow] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] | before e [k] · before i [k] · before vowel [kw] |
| ⟨r⟩ | [ɾ] | intervocalic [ɾ] · onset [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] | intervocalic [z̺] · word initial [s̺] |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tch⟩ | [tʃ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [uj] |  |
| ⟨uo⟩ | [wo] |  |
| ⟨uâ⟩ | [wɐ] |  |
| ⟨uô⟩ | [wɔ] |  |
| ⟨v⟩ | [b] | intervocalic [b] · word initial [b] |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [j] |  |
| ⟨yy⟩ | [kʲ] |  |
| ⟨z⟩ | [s] | intervocalic [d͡z] · word final [d͡z] · word initial [d͡z] |
| ⟨à⟩ | [a] |  |
| ⟨á⟩ | [a] |  |
| ⟨â⟩ | [a] |  |
| ⟨ã⟩ | [ɐ̃] |  |
| ⟨ão⟩ | [ɐ̃w̃] |  |
| ⟨ç⟩ | [s] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [ɛ] |  |
| ⟨ê⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [ɔ] |  |
| ⟨ô⟩ | [o] |  |
| ⟨õ⟩ | [õ] |  |
| ⟨õe⟩ | [õj̃] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ĩ⟩ | [ĩ] |  |
| ⟨ũ⟩ | [ũ] |  |
| ⟨ḥ⟩ | [h] |  |
| ⟨ẽ⟩ | [ẽ] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-l⟩ ⟨-d⟩ ⟨-z⟩ ⟨-x⟩ ⟨-t⟩ ⟨-n⟩ ⟨-m⟩ ⟨-f⟩. These endings take the penult: ⟨-s⟩ ⟨-ns⟩.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 6 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AST_NASAL_a` | /a/ → [ɐ̃], before a coda nasal | - | - |
| `AST_NASAL_e` | /e/ → [ẽ], before a coda nasal | - | - |
| `AST_NASAL_i` | /i/ → [ĩ], before a coda nasal | - | - |
| `AST_NASAL_o` | /o/ → [õ], before a coda nasal | - | - |
| `AST_NASAL_u` | /u/ → [ũ], before a coda nasal | - | - |
| `AST_NASAL_ABSORB` | /n m/ → ∅, in the coda, after a vowel | - | - |

The spec switches off 16 inherited rules: `AST_GLIDE_I_RISING`, `AST_GLIDE_U_RISING`, `AST_GLIDE_I_FALLING`, `AST_GLIDE_U_FALLING`, `AST_SPIRANT_B`, `AST_SPIRANT_D`, `AST_SPIRANT_G`, `AST_SPIRANT_G_INITIAL`, `AST_AFFRICATE_Y_INITIAL`, `AST_TRILL_AFTER_L_N_S`, `AST_NASAL_LABIAL`, `AST_NASAL_VELAR`, `AST_NASAL_FINAL`, `AST_VOICE_S`, `AST_VOICE_THETA`, `AST_VOICE_SH`.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ast-PT-x-rionor")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Rijāl Almaʿ Arabic](ar-SA-x-rijal-alma.md) · [Home](../index.md) · [Rioplatense Spanish →](es-AR.md)
