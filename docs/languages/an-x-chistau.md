# Chistabín Aragonese (Gistaín/Chistau valley) (`an-x-chistau`)

<!-- atlas:summary begin -->
Chistabín Aragonese (Gistaín/Chistau valley) is an Ibero-Romance variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `an-x-chistau` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `an-x-chistau` |
| Aliases | `an-x-chistabin` |
| ISO 639-3 | [arg](https://iso639-3.sil.org/code/arg), Aragonese |
| Wikidata | [Q11023714](https://www.wikidata.org/wiki/Q11023714) |
| Wikipedia | [Aragonés chistabino](https://es.wikipedia.org/wiki/Aragon%C3%A9s_chistabino) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1100, living |
| Parent | [Aragonese](an.md) `an` |
| Explorer | [`an-x-chistau` in the data explorer](https://tigregotico.github.io/orthography2ipa/#an-x-chistau) |
| Spec file | [`an-x-chistau.json`](../../orthography2ipa/data/an-x-chistau.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Chistabín, the Aragonese of the Gistaín/Chistau valley (Valle de Chistau, Sobrarbe, Huesca), a Central/Eastern High-Aragonese variety, comparatively well preserved (references: Blas Gabarda & Romanos Hernando 2008 'Diccionario aragonés chistabín', Mott 1989).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1989 to 2008. [Sources](#sources) lists them. The spec file writes 2 of the 60 spellings of its letter table and takes the other 58 from [Aragonese](an.md) `an`.

The [spec file](../../orthography2ipa/data/an-x-chistau.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `an-x-chistau` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-blas_romanos2008"></a>Blas Gabarda, F. & Romanos Hernando, F. (2008). *Diccionario aragonés chistabín (Bal de Chistau)*. Gara d'Edizions / Institución Fernando el Católico.
2. <a id="src-mott1989"></a>Mott, B. (1989). *El habla de Gistaín*. Instituto de Estudios Altoaragoneses.
3. <a id="src-varvaro_afa"></a>Várvaro, A. (1991). *De la escritura al habla: la diptongación de O breve tónica en el Alto Aragón*. Archivo de Filología Aragonesa XLVI-XLVII. Cited: 245-268. [ifc.dpz.es](https://ifc.dpz.es/recursos/publicaciones/15/72/12varvaro.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `an-x-chistau` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0555 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 54 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  | ts | tʃ |  |  |
| Nasal | m |  |  | n nː |  | ɲ |  |
| Trill |  |  |  | r |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative | β | f | ð θ | s | ʃ | ʝ | x ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l lː |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [iʃ] [ja] [je] [jo] [ju] [jʃ] [ks] [oj] [w] [wa] [we] [wi] [wo] [ɡw] [ɡwe] [ɡwi].
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
| ⟨c⟩ | [k] [θ] [s] | before e [θ] [s] · before i [θ] [s] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | intervocalic [ð] · word final [ð] ∅ |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [tʃ] [x] | before e [x] [tʃ] · before i [x] [tʃ] · intervocalic [ɣ] |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨güe⟩ | [ɡwe] |  |
| ⟨güi⟩ | [ɡwi] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [je] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [ju] |  |
| ⟨ix⟩ | [ʃ] [iʃ] [jʃ] |  |
| ⟨j⟩ | [x] [tʃ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] [ʎ] | onset [l] [ʎ] |
| ⟨ll⟩ | [ʎ] |  |
| ⟨l·l⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨n·n⟩ | [nː] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] [r] | before consonant [ɾ] · intervocalic [ɾ] · word final ∅ · word initial [r] |
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
| ⟨x⟩ | [ʃ] [ks] |  |
| ⟨y⟩ | [ʝ] [j] [i] |  |
| ⟨z⟩ | [θ] [s] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "an-x-chistau")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Chilean Spanish](es-CL.md) · [Home](../index.md) · [Choctaw →](cho.md)
