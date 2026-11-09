# Canarian Spanish (`es-ES-x-canarias`)

<!-- atlas:summary begin -->
Canarian Spanish is an Ibero-Romance variety, written in the Latin script. Its code names Spain. The `es-ES-x-canarias` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `es-ES-x-canarias` |
| ISO 639-3 | [spa](https://iso639-3.sil.org/code/spa), Spanish |
| Glottolog | [cana1269](https://glottolog.org/resource/languoid/id/cana1269), Canary Islands Spanish |
| Wikidata | [Q957764](https://www.wikidata.org/wiki/Q957764) |
| Wikipedia | [Canarian Spanish](https://en.wikipedia.org/wiki/Canarian_Spanish) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Castilian Spanish](es-ES.md) `es-ES` |
| Explorer | [`es-ES-x-canarias` in the data explorer](https://tigregotico.github.io/orthography2ipa/#es-ES-x-canarias) |
| Spec file | [`es-ES-x-canarias.json`](../../orthography2ipa/data/es-ES-x-canarias.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Canarian Spanish (Islas Canarias). Systematic seseo (no /θ/), yeísmo, coda /s/ aspiration (less extreme than Andalusian), partial /x/ aspiration. Strong historical connections to Andalusian and Caribbean Spanish. Conservative affricate [tʃ] preservation. -d deletion in participial -ado.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1918 to 2011. [Sources](#sources) lists them. The spec file writes 4 of the 61 spellings of its letter table and takes the other 57 from [Castilian Spanish](es-ES.md) `es-ES`.

The [spec file](../../orthography2ipa/data/es-ES-x-canarias.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `es-ES-x-canarias` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-hualde2005"></a>Hualde, J.I. (2005). *The Sounds of Spanish*. Cambridge University Press.
2. <a id="src-penny2002"></a>Penny, R. (2002). *A History of the Spanish Language*. Cambridge University Press.
3. <a id="src-zamora_vicente1960"></a>Zamora Vicente, A. (1960). *Dialectología española*. Gredos.
4. <a id="src-lipski_overview"></a>Lipski, John M. (2011). *Geographical and Social Varieties of Spanish: An Overview*. In J.I. Hualde, A. Olarrea & E. O'Rourke (eds.), The Handbook of Hispanic Linguistics, Wiley-Blackwell. Cited: pp. 1-26. [johnlipski.github.io](https://johnlipski.github.io/geo.pdf)
5. <a id="src-lipski1986"></a>Lipski, John M. (1986). *Reduction of Spanish Word-Final /s/ and /n/*. Canadian Journal of Linguistics / Revue canadienne de linguistique 31(2). Cited: p. 140, pp. 146-147.
6. <a id="src-navarro1918"></a>Navarro Tomás, Tomás (1918). *Manual de pronunciación española*. Centro de Estudios Históricos, Madrid. Cited: § 87 p. 66. [archive.org](https://archive.org/details/manualdepronunci00navauoft)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `es-ES-x-canarias` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0000 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 65 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |  |
| Affricate |  |  |  |  | tʃ |  |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |  |
| Trill |  |  |  | r |  |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |  |
| Fricative | β | f | ð θ | s |  | ʝ | x ɣ | χ | h |
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
| ⟨b⟩ | [b] | intervocalic [β] |
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | intervocalic [ð] · word final [ð] |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ei̯] | before vowel [ej] · default [ei̯] |
| ⟨eu⟩ | [eu̯] | before vowel [ew] · default [eu̯] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [x] | before e [x] · before i [x] · intervocalic [ɣ] |
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
| ⟨j⟩ | [x] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʝ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] | before consonant [n] [ŋ] · word final [ŋ] |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oi⟩ | [oi̯] | before vowel [oj] · default [oi̯] |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] [h] | before consonant [h] [s] · intervocalic [s] · word final [h] · word initial [s] |
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

The spec applies 7 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `ES_TRILL_AFTER_CORONAL` | /ɾ/ → [r], after [n] [l] [s] | ⟨alrededor⟩ [alreðeˈðoɾ] | [Hualde 2005](#src-hualde2005), Navarro Tomás 1977, Quilis 1993 |
| `ES_NASAL_LABIAL` | /n/ → [m], before [b] [β] [p] [m] | ⟨inmaculada⟩ [immakuˈlaða] | [Hualde 2005](#src-hualde2005), Navarro Tomás 1977, Quilis 1993 |
| `ES_NASAL_VELAR` | /n/ → [ŋ], in the coda, before [k] [ɡ] [ɣ] [w] | - | [Navarro 1918](#src-navarro1918) |
| `ES_SPIRANT_B` | /b/ → [β], after [a] [e] [i] [o] [u] [ɛ] [ɔ] [æ] and 28 more | - | [Navarro 1918](#src-navarro1918) |
| `ES_SPIRANT_D` | /d/ → [ð], after [a] [e] [i] [o] [u] [ɛ] [ɔ] [æ] and 26 more | - | [Navarro 1918](#src-navarro1918) |
| `ES_SPIRANT_G` | /ɡ/ → [ɣ], after [a] [e] [i] [o] [u] [ɛ] [ɔ] [æ] and 28 more | - | [Navarro 1918](#src-navarro1918) |
| `CANARIAS_X_TO_H` | /x/ → [h] | ⟨cojo⟩ [ˈkoho] | [Hualde 2005](#src-hualde2005), [Zamora 1960](#src-zamora_vicente1960) |

The spec applies 6 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `ES_EXT_SPIRANT_B` | `[^mnŋɲ̃]$` | `^([ˈˌ]?)b` | right [β] | - | [Navarro 1918](#src-navarro1918) |
| `ES_EXT_SPIRANT_D` | `[^mnŋɲ̃lʎ]$` | `^([ˈˌ]?)d` | right [ð] | - | [Navarro 1918](#src-navarro1918) |
| `ES_EXT_SPIRANT_G` | `[^mnŋɲ̃]$` | `^([ˈˌ]?)ɡ` | right [ɣ] | - | [Navarro 1918](#src-navarro1918) |
| `ES_EXT_FINAL_N_LABIAL` | `ŋ$` | `^[ˈˌ]?[pbβm]` | left [m] | ⟨un buen baile⟩ [um bwem baile] | [Lipski 1986](#src-lipski1986), [Navarro 1918](#src-navarro1918), Zamora and Guitart 1982 |
| `ES_EXT_FINAL_N_CORONAL` | `ŋ$` | `^[ˈˌ]?[tdðθszlɾrnɲʎʝʃʒf]` | left [n] | - | [Lipski 1986](#src-lipski1986), [Navarro 1918](#src-navarro1918), Zamora and Guitart 1982 |
| `ES_EXT_FINAL_N_VELAR` | `[nŋ]$` | `^[ˈˌ]?[kɡɣxw]` | left [ŋ] | ⟨en casa⟩ [eŋ kása] | [Lipski 2011](#src-lipski_overview), [Lipski 1986](#src-lipski1986), [Navarro 1918](#src-navarro1918) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "es-ES-x-canarias")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Campidanese Sardinian](sro.md) · [Home](../index.md) · [Cantabrian →](ast-x-cantabri.md)
