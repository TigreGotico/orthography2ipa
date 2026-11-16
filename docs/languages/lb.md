# Luxembourgish (`lb`)

<!-- atlas:summary begin -->
Luxembourgish is a West Germanic language, written in the Latin script. Glottolog places it in Belgium, France, Germany and Luxembourg. The `lb` spec is at the research tier. It cites 1 source and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lb` |
| ISO 639-3 | [ltz](https://iso639-3.sil.org/code/ltz), Luxembourgish |
| Glottolog | [luxe1241](https://glottolog.org/resource/languoid/id/luxe1241), Moselle Franconian |
| Wikidata | [Q9051](https://www.wikidata.org/wiki/Q9051) |
| Wikipedia | [Luxembourgish language](https://en.wikipedia.org/wiki/Luxembourgish_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Belgium](by-region.md#belgium), [France](by-region.md#france), [Germany](by-region.md#germany), [Luxembourg](by-region.md#luxembourg) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1340, living |
| Parent | [West Germanic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2793) `x-clade-west2793` |
| Explorer | [`lb` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lb) |
| Spec file | [`lb.json`](../../orthography2ipa/data/lb.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Luxembourgish (Lëtzebuergesch), the Moselle Franconian national language of Luxembourg, described here from Gilles & Trouvain's Illustration of the IPA.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2013. [Sources](#sources) lists them. The spec file writes all 50 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lb.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lb` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-gilles_trouvain2013"></a>Gilles, Peter & Trouvain, Jürgen (2013). *Luxembourgish (Illustrations of the IPA)*. Journal of the International Phonetic Association 43(1). Cited: 67-74. [doi.org](https://doi.org/10.1017/S0025100312000278)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `lb` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 3893 | 0.2412 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Affricate |  |  | ts |  |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  |  |  |  |  | ʀ |  |
| Fricative |  | f v | s z | ʃ | ɕ |  | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y |  | u uː |
| Close-mid | e eː øː |  | o oː |
| Mid |  | ə |  |
| Near-open | æ |  |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [iə] [ks] [kw] [uə] [æːɪ] [æːʊ] [œɪ] [ɑɪ] [ɑʊ] [əʊ] [ɜɪ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨ai⟩ | [ɑɪ] |  |
| ⟨au⟩ | [ɑʊ] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [χ] | after a [χ] · after o [χ] · after u [χ] · default [ɕ] |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨ei⟩ | [ɑɪ] |  |
| ⟨eu⟩ | [œɪ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] · intervocalic [ʁ] · word final [χ] · word initial [ɡ] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ie⟩ | [iə] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [əʊ] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [ʀ] |  |
| ⟨s⟩ | [z] | default [s] · intervocalic [z] · word final [s] · word initial [z] |
| ⟨sch⟩ | [ʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨ue⟩ | [uə] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [f] |  |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨z⟩ | [ts] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨äi⟩ | [æːɪ] |  |
| ⟨äu⟩ | [æːʊ] |  |
| ⟨é⟩ | [eː] |  |
| ⟨éi⟩ | [ɜɪ] |  |
| ⟨ë⟩ | [ə] |  |
| ⟨ö⟩ | [øː] |  |
| ⟨ü⟩ | [y] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lb")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lushootseed](lut.md) · [Home](../index.md) · [Macedonian →](mk.md)
