# Yucatec Mexican Spanish (`es-MX-x-yucatan`)

<!-- atlas:summary begin -->
Yucatec Mexican Spanish is an Ibero-Romance variety, written in the Latin script. Its code names Mexico. The `es-MX-x-yucatan` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `es-MX-x-yucatan` |
| ISO 639-3 | [spa](https://iso639-3.sil.org/code/spa), Spanish |
| Wikipedia | [Spanish dialects and varieties](https://en.wikipedia.org/wiki/Spanish_dialects_and_varieties) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [North America](by-region.md#north-america) > [Mexico](by-region.md#mexico) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1600, living |
| Parent | [Mexican Spanish (Highland)](es-MX.md) `es-MX` |
| Explorer | [`es-MX-x-yucatan` in the data explorer](https://tigregotico.github.io/orthography2ipa/#es-MX-x-yucatan) |
| Spec file | [`es-MX-x-yucatan.json`](../../orthography2ipa/data/es-MX-x-yucatan.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Yucatan-Peninsula Spanish, Lipski's (1994) 'Guatemala, parts of the Yucatan, and Costa Rica' zone, strong Yucatec Maya substrate.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1987 to 2012. [Sources](#sources) lists them. The spec file writes 4 of the 61 spellings of its letter table and takes the other 57 from [Castilian Spanish](es-ES.md) `es-ES`.

The [spec file](../../orthography2ipa/data/es-MX-x-yucatan.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `es-MX-x-yucatan` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-lipski_overview"></a>Lipski, John M. (2011). *Geographical and Social Varieties of Spanish: An Overview*. In J.I. Hualde, A. Olarrea & E. O'Rourke (eds.), The Handbook of Hispanic Linguistics, Wiley-Blackwell. Cited: pp. 1-26. [johnlipski.github.io](https://johnlipski.github.io/geo.pdf)
2. <a id="src-lipski1994"></a>Lipski, John M. (1994). *Latin American Spanish*. Longman Linguistics Library, Longman. Cited: ch. Mexico, pp. 271-291 (Yucatan pp. 279-282).
3. <a id="src-michnowicz2012"></a>Michnowicz, Jim (2012). *The Standardization of Yucatan Spanish: Family Case Studies in Izamal and Merida*. In K. Geeslin & M. Diaz-Campos (eds.), Selected Proceedings of the 14th Hispanic Linguistics Symposium, Cascadilla Proceedings Project. Cited: pp. 102-115. [lingref.com](http://www.lingref.com/cpp/hls/14/paper2659.pdf)
4. <a id="src-michnowicz2008"></a>Michnowicz, Jim (2008). *Final -m in Yucatan Spanish: A rapid and anonymous survey*. In J. Bruhn de Garavito & E. Valenzuela (eds.), Selected Proceedings of the 10th Hispanic Linguistics Symposium, Cascadilla Proceedings Project. Cited: pp. 155-165.
5. <a id="src-lope_blanch1987"></a>Lope Blanch, Juan M. (1987). *Estudios sobre el espanol de Yucatan*. Universidad Nacional Autonoma de Mexico (UNAM).
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `es-MX-x-yucatan` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0092 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 66 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |  |
| Affricate |  |  |  |  | tʃ |  |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |  |
| Trill |  |  |  | r |  |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |  |
| Fricative | β | f | ð θ | s s̺ |  | ʝ | x ɣ | χ | h |
| Approximant |  |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [ai̯] [aj] [au̯] [aw] [ei̯] [ej] [eu̯] [ew] [ia] [ie] [io] [ja] [je] [jo] [ju] [ks] [oi̯] [oj] [ua] [ue] [uo] [w] [wa] [we] [wi] [wo] [ɟʝ] [ɡw] [ɡwe] [ɡwi] [ʝa] [ʝe] [ʝo].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai̯] | before vowel [aj] · default [ai̯] |
| ⟨au⟩ | [au̯] | before vowel [aw] · default [au̯] |
| ⟨b⟩ | [b] | intervocalic [b] |
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | intervocalic [d] · word final [d] |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ei̯] | before vowel [ej] · default [ei̯] |
| ⟨eu⟩ | [eu̯] | before vowel [ew] · default [eu̯] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [x] | before e [h] · before i [h] · intervocalic [ɡ] |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨güe⟩ | [ɡwe] |  |
| ⟨güi⟩ | [ɡwi] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [je] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [ju] |  |
| ⟨iá⟩ | [ja] | default [ja] · word initial [ia] |
| ⟨ié⟩ | [je] | default [je] · word initial [ie] |
| ⟨ió⟩ | [jo] | default [jo] · word initial [io] |
| ⟨j⟩ | [h] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʝ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] | before consonant [n] [ŋ] · word final [m] |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oi⟩ | [oi̯] | before vowel [oj] · default [oi̯] |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tx⟩ | [tʃ] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [wi] |  |
| ⟨uo⟩ | [wo] |  |
| ⟨uá⟩ | [wa] | default [wa] · word initial [ua] |
| ⟨ué⟩ | [we] | default [we] · word initial [ue] |
| ⟨uó⟩ | [wo] | default [wo] · word initial [uo] |
| ⟨v⟩ | [b] | intervocalic [β] |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] [s] | before consonant [s] |
| ⟨y⟩ | [ʝ] [i] | before vowel [ʝ] · default [i] |
| ⟨z⟩ | [s] |  |
| ⟨á⟩ | [a] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ü⟩ | [w] |  |
| ⟨ý⟩ | [i] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-l⟩ ⟨-d⟩ ⟨-z⟩ ⟨-j⟩ ⟨-x⟩ ⟨-k⟩ ⟨-f⟩ ⟨-t⟩ ⟨-c⟩ ⟨-b⟩ ⟨-p⟩ ⟨-g⟩ ⟨-m⟩ ⟨-ión⟩ ⟨-ad⟩ ⟨-or⟩ ⟨-al⟩ ⟨-ay⟩ ⟨-ey⟩ ⟨-oy⟩ ⟨-uy⟩. These endings take the penult: ⟨-n⟩ ⟨-s⟩ ⟨-ns⟩.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 3 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `ES_TRILL_AFTER_CORONAL` | /ɾ/ → [r], after [n] [l] [s] | ⟨alrededor⟩ [alreðeˈðoɾ] | Navarro Tomás 1977, Hualde 2005, Quilis 1993 |
| `ES_NASAL_LABIAL` | /n/ → [m], before [b] [β] [p] [m] | ⟨inmaculada⟩ [immakuˈlaða] | Navarro Tomás 1977, Hualde 2005, Quilis 1993 |
| `ES_NASAL_VELAR` | /n/ → [ŋ], in the coda, before [k] [ɡ] [ɣ] [x] [w] | ⟨cinco⟩ [θíŋko] | Navarro Tomás 1918 |

The spec applies 6 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `ES_EXT_SPIRANT_B` | `[^mnŋɲ̃]$` | `^([ˈˌ]?)b` | right [b] | - | [Michnowicz 2012](#src-michnowicz2012) |
| `ES_EXT_SPIRANT_D` | `[^mnŋɲ̃lʎ]$` | `^([ˈˌ]?)d` | right [d] | ⟨occlusive⟩ [b d g] | [Michnowicz 2012](#src-michnowicz2012) |
| `ES_EXT_SPIRANT_G` | `[^mnŋɲ̃]$` | `^([ˈˌ]?)ɡ` | right [ɡ] | - | [Michnowicz 2012](#src-michnowicz2012) |
| `ES_EXT_FINAL_N_LABIAL` | `[nŋ]$` | `^[ˈˌ]?[pbβm]` | left [m] | ⟨un buen baile⟩ [um bwem baile] | [Lipski 2011](#src-lipski_overview), Navarro Tomás 1918, Lipski 1986 |
| `ES_EXT_FINAL_N_CORONAL` | `[nŋ]$` | `^[ˈˌ]?[tdðθszlɾrnɲʎʝʃʒf]` | left [n] | - | [Lipski 2011](#src-lipski_overview), Navarro Tomás 1918, Lipski 1986 |
| `ES_EXT_FINAL_N_VELAR` | `[nŋ]$` | `^[ˈˌ]?[kɡɣxw]` | left [ŋ] | ⟨en casa⟩ [eŋ kása] | [Lipski 2011](#src-lipski_overview), Navarro Tomás 1918, Lipski 1986 |

The spec switches off 3 inherited rules: `ES_SPIRANT_B`, `ES_SPIRANT_D`, `ES_SPIRANT_G`.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "es-MX-x-yucatan")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Yoruba](yo.md) · [Home](../index.md) · [Zaza →](zza.md)
