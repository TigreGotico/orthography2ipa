# Mapudungun (`arn`)

<!-- atlas:summary begin -->
Mapudungun is an Araucanian language, written in the Latin script. Glottolog places it in Argentina and Chile. The `arn` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `arn` |
| ISO 639-3 | [arn](https://iso639-3.sil.org/code/arn), Mapudungun |
| Glottolog | [mapu1245](https://glottolog.org/resource/languoid/id/mapu1245), Mapudungun |
| Wikidata | [Q33730](https://www.wikidata.org/wiki/Q33730) |
| Wikipedia | [Mapudungun language](https://en.wikipedia.org/wiki/Mapudungun_language) |
| Family | [Araucanian](by-family.md#araucanian) |
| Region | [South America](by-region.md#south-america) > [Argentina](by-region.md#argentina), [Chile](by-region.md#chile) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Araucanian](https://tigregotico.github.io/orthography2ipa/#x-clade-arau1255) `x-clade-arau1255` |
| Explorer | [`arn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#arn) |
| Spec file | [`arn.json`](../../orthography2ipa/data/arn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Mapudungun (Mapuche/Araucanian), an isolate of central-southern Chile and Argentine Patagonia.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1997 to 2008. [Sources](#sources) lists them. The spec file writes all 27 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/arn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `arn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-campbell1997"></a>Campbell, Lyle (1997). *American Indian Languages: The Historical Linguistics of Native America*. Oxford University Press.
2. <a id="src-smeets2008"></a>Smeets, Ineke (2008). *A Grammar of Mapuche*. Mouton de Gruyter.
3. <a id="src-salas2006"></a>Salas, Adalberto (2006). *El mapuche o araucano: fonología, gramática y antología de cuentos*. Centro de Estudios Públicos.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wold` ([lexibank/wold](https://github.com/lexibank/wold)) | `arn` | gold | lexicon-derived | CC BY 4.0 | 1269 | 0.0112 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t |  |  |  | k ɡ |  |
| Affricate |  |  |  | tʃ | ʈʂ |  |  |  |
| Nasal | m |  | n n̪ |  |  | ɲ | ŋ |  |
| Fricative |  | f | s z |  |  |  |  | h |
| Approximant |  |  |  |  | ɻ | j |  |  |
| Lateral approximant |  |  | l l̪ |  |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɻ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tr⟩ | [ʈʂ] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ü⟩ | [ɨ] |  |
| ⟨ḻ⟩ | [l̪] |  |
| ⟨ṉ⟩ | [n̪] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "arn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Manx](gv.md) · [Home](../index.md) · [Maquiritari →](mch.md)
