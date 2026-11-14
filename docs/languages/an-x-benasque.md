# Benasquese (patués, Benasque valley) (`an-x-benasque`)

<!-- atlas:summary begin -->
Benasquese (patués, Benasque valley) is an Ibero-Romance variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `an-x-benasque` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `an-x-benasque` |
| Aliases | `an-x-benasques` |
| ISO 639-3 | [arg](https://iso639-3.sil.org/code/arg), Aragonese |
| Wikipedia | [Benasquese dialect](https://en.wikipedia.org/wiki/Benasquese_dialect) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1100, living |
| Parent | [Aragonese](an.md) `an` |
| Explorer | [`an-x-benasque` in the data explorer](https://tigregotico.github.io/orthography2ipa/#an-x-benasque) |
| Spec file | [`an-x-benasque.json`](../../orthography2ipa/data/an-x-benasque.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Benasquese (benasqués, patués, ribagorzano de Benasque), the Aragonese-Catalan TRANSITIONAL variety of the upper Ésera valley (Vall de Benás/Benasque, Alta Ribagorza, Huesca).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2001 to 2022. [Sources](#sources) lists them. The spec file writes 7 of the 58 spellings of its letter table and takes the other 51 from [Aragonese](an.md) `an`.

The [spec file](../../orthography2ipa/data/an-x-benasque.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `an-x-benasque` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-saura_rami2003"></a>Saura Rami, J.A. (2003). *Elementos de fonética y morfosintaxis benasquesas*. Institución Fernando el Católico / Gara d'Edizions, Zaragoza. Cited: 43-106 (fonética).
2. <a id="src-giralt_latorre_afa_review"></a>Giralt Latorre, J. (2006). *Reseña de J.A. Saura Rami, Elementos de fonética y morfosintaxis benasquesas*. Archivo de Filología Aragonesa LXI-LXII, pp. 419-424. Cited: 419-424. [ifc.dpz.es](https://ifc.dpz.es/recursos/publicaciones/25/19/_ebook.pdf)
3. <a id="src-aragones_fonetica_diacronica"></a>Academia Aragonesa de la Lengua (eds.) (2022). *Para una fonética diacrónica del aragonés*. Revista de la Academia Aragonesa de la Lengua. [revistas.academiaaragonesadelalengua.org](https://revistas.academiaaragonesadelalengua.org/raal/es/article/download/8/17/44)
4. <a id="src-nagore_lain2001"></a>Nagore Laín, F. (2001). *Gramática de la Lengua Aragonesa*. Librería General.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `an-x-benasque` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0510 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 49 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  | ts | tʃ |  |  |
| Nasal | m |  |  | n |  | ɲ |  |
| Trill |  |  |  | r |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative | β | f | ð θ | s | ʃ | ʝ | x ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [ja] [je] [jo] [ju] [oj] [w] [wa] [we] [wi] [wo] [ɡw] [ɡwe] [ɡwi].
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
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | intervocalic [ð] · word final [ð] ∅ |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [tʃ] [x] | before e [tʃ] · before i [tʃ] |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨güe⟩ | [ɡwe] |  |
| ⟨güi⟩ | [ɡwi] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [je] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [ju] |  |
| ⟨ix⟩ | [ʃ] |  |
| ⟨j⟩ | [tʃ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] [ʎ] | onset [l] [ʎ] |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] [r] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tz⟩ | [θ] [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [wi] |  |
| ⟨uo⟩ | [wo] |  |
| ⟨v⟩ | [b] | intervocalic [β] |
| ⟨w⟩ | [w] [b] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [ʝ] [j] [i] |  |
| ⟨z⟩ | [s] |  |
| ⟨á⟩ | [a] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ü⟩ | [u] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨è⟩ ⟨í⟩ ⟨ó⟩ ⟨ò⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-l⟩ ⟨-d⟩ ⟨-z⟩ ⟨-x⟩ ⟨-t⟩ ⟨-c⟩ ⟨-k⟩ ⟨-f⟩ ⟨-n⟩ ⟨-m⟩. These endings take the penult: ⟨-s⟩ ⟨-ns⟩.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "an-x-benasque")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Bemba](bem.md) · [Home](../index.md) · [Bengali →](bn.md)
