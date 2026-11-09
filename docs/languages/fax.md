# A Fala (Xalimego) (`fax`)

<!-- atlas:summary begin -->
A Fala (Xalimego) is an Ibero-Romance language, written in the Latin script. Glottolog places it in Portugal and Spain. The `fax` spec is at the research tier. It cites 5 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `fax` |
| ISO 639-3 | [fax](https://iso639-3.sil.org/code/fax), Fala |
| Glottolog | [fala1241](https://glottolog.org/resource/languoid/id/fala1241), Fala |
| Wikidata | [Q300402](https://www.wikidata.org/wiki/Q300402) |
| Wikipedia | [Fala language](https://en.wikipedia.org/wiki/Fala_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Portugal](by-region.md#portugal), [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Galician](gl-ES.md) `gl-ES` |
| Explorer | [`fax` in the data explorer](https://tigregotico.github.io/orthography2ipa/#fax) |
| Spec file | [`fax.json`](../../orthography2ipa/data/fax.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> A Fala (Xalimego/Fala de Xálima). Galician-Portuguese linguistic island in Cáceres, Extremadura. Three local varieties: Valverdeiru (Valverde del Fresno), Lagarteiro (Eljas), Mañegu (San Martín de Trevejo). ~5,000, 10,000 speakers.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1994 to 2023. [Sources](#sources) lists them. The spec file writes all 58 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/fax.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `fax` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-grupo_xalima_tesoro"></a>Grupo de Estudo d'A Fala (Grupo Xálima) (2019). *A Fala de Xálima: valverdeiru, lagarteiru, manhegu. Un tesoro luso-extremeño*. Diputación de Cáceres. Cited: 37-56. [archivo.dip-caceres.es](https://archivo.dip-caceres.es/wp-content/uploads/2024/01/05-087-02.pdf)
2. <a id="src-carrasco_fala2023"></a>Carrasco González, J.M. (2023). *A Fala (do Val de Xálima)*. eHumanista/IVITRA 24. [dehesa.unex.es](https://dehesa.unex.es/)
3. <a id="src-penny2002"></a>Penny, R. (2002). *A History of the Spanish Language*. Cambridge University Press.
4. <a id="src-mateus_dandrade2000"></a>Mateus, M.H.M. & d'Andrade, E. (2000). *The Phonology of Portuguese*. Oxford University Press.
5. <a id="src-alarcos_llorach1994"></a>Alarcos Llorach, E. (1994). *Gramática de la Lengua Española*. Espasa.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `fax` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 655 | 0.0977 | yes |
| `spain_romance_tts` | `fax` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0519 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 53 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  |  | tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð θ | s z | ʃ ʒ |  | ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o õ |
| Open-mid | ɛ |  | ɔ |
| Near-open |  | ɐ ɐ̃ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [iw] [ja] [je] [jo] [oj] [ow] [uj] [w] [wa] [we] [wo] [ɐ̃w̃] [ɡw].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [ɐ] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] | default [b] · intervocalic [β] |
| ⟨c⟩ | [k] [θ] | before e [θ] · before i [θ] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | default [d] · intervocalic [ð] |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] | default [f] · word initial [f] [h] |
| ⟨g⟩ | [ɡ] [ʒ] | before e [ʒ] · before i [ʒ] · default [ɡ] · intervocalic [ɣ] |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [je] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [iw] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [ʎ] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nh⟩ | [ɲ] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨ou⟩ | [ow] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] | before consonant [ɾ] · intervocalic [ɾ] · onset [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] | default [s] · intervocalic [s] [z] |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [uj] |  |
| ⟨uo⟩ | [wo] |  |
| ⟨v⟩ | [b] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨z⟩ | [θ] |  |
| ⟨á⟩ | [a] |  |
| ⟨ã⟩ | [ɐ̃] |  |
| ⟨ão⟩ | [ɐ̃w̃] |  |
| ⟨ç⟩ | [s] |  |
| ⟨é⟩ | [ɛ] |  |
| ⟨ê⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [ɔ] |  |
| ⟨ô⟩ | [o] |  |
| ⟨õ⟩ | [õ] |  |
| ⟨ú⟩ | [u] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 12 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `GL_OPEN_O` | /o/ → [ɔ], stressed, in 4 listed words | ⟨corre⟩ [ˈkɔre] | Regueira 1996, Freixeiro Mato 1998 |
| `GL_STOP_AFTER_NASAL` | /β/ → [b], after a coda nasal | ⟨ambos⟩ [ˈambos] | Regueira 2010, Freixeiro Mato 1998, Xove 2002 |
| `GL_STOP_AFTER_NASAL_D` | /ð/ → [d], after a coda nasal | - | Regueira 2010 |
| `GL_STOP_AFTER_NASAL_G` | /ɣ/ → [ɡ], after a coda nasal | ⟨tango⟩ [ˈtaŋɡo] | Regueira 2010, Freixeiro Mato 1998 |
| `GL_NASAL_VELAR` | /n/ → [ŋ], before [k] [ɡ] [ɣ] [x] | ⟨Angumil⟩ [aŋɡuˈmil] | Regueira 2010, Freixeiro Mato 1998, Xove 2002 |
| `GL_NASAL_LABIAL` | /n/ → [m], before [p] [b] [β] [m] | ⟨benvida⟩ [bemˈbiða] | Regueira 2010, Freixeiro Mato 1998 |
| `GL_NASAL_FINAL_NS` | /n/ → [ŋ], before [s], with more context in the spec | ⟨Bertamiráns⟩ [beɾtamiˈɾaŋs] | Regueira 2010, Freixeiro Mato 1998 |
| `GL_RAISE_O_BEFORE_NASAL` | /ɔ/ → [o], before a coda nasal, before [n] [m] [ŋ] [ɲ] | ⟨Antón⟩ [anˈtoŋ] | Regueira 2010, Freixeiro Mato 1998 |
| `GL_TRILL_AFTER_L_N_S` | /ɾ/ → [r], after [l] [n] [s] [ŋ] | ⟨alroto⟩ [alˈroto] | Freixeiro Mato 1998, Xove 2002 |
| `GL_STOP_BEFORE_IDENTICAL_B` | /β/ → [b], before [β] | - | Regueira 2010, Freixeiro Mato 1998 |
| `GL_STOP_BEFORE_IDENTICAL_D` | /ð/ → [d], before [ð] | - | Regueira 2010, Freixeiro Mato 1998 |
| `GL_STOP_BEFORE_IDENTICAL_G` | /ɣ/ → [ɡ], before [ɣ] | - | Regueira 2010, Freixeiro Mato 1998 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "fax")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Languages from A to Z](a-z.md) · [Home](../index.md) · [Abkhaz →](ab.md)
