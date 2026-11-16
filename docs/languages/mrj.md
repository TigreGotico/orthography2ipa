# Hill Mari (Western Mari) (`mrj`)

<!-- atlas:summary begin -->
Hill Mari (Western Mari) is a Mari language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `mrj` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mrj` |
| Wikidata | [Q1776032](https://www.wikidata.org/wiki/Q1776032) |
| Wikipedia | [Hill Mari Wikipedia](https://en.wikipedia.org/wiki/Hill_Mari_Wikipedia) |
| Family | [Uralic](by-family.md#uralic) > [Mari](by-family.md#uralic--mari) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Mari](https://tigregotico.github.io/orthography2ipa/#chm) `chm` |
| Explorer | [`mrj` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mrj) |
| Spec file | [`mrj.json`](../../orthography2ipa/data/mrj.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Hill Mari / Western Mari (кырык мары), Mari El, Russia. INPUT CONTRACT: modern Hill Mari 35-letter Cyrillic orthography, NFC (⟨Ӓӓ Ӧӧ Ӱӱ Ӹӹ⟩ are precomposed characters).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1998 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 40 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mrj.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mrj` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kangasmaa-minn1998"></a>Kangasmaa-Minn, Eeva (1998). *Mari*. in Daniel Abondolo (ed.), The Uralic Languages, Routledge. [routledge.com](https://www.routledge.com/The-Uralic-Languages/Abondolo-Valijarvi/p/book/9781138459166)
2. <a id="src-hillmari_wiki"></a>Wikipedia contributors (2024). *Hill Mari language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Hill_Mari_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `mrj` | gold | lexicon-derived | CC BY 4.0 | 1018 | 0.0075 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 38 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | t |  |  | k |
| Affricate |  |  |  | ts | tʃ |  |  |
| Nasal | m |  |  | n |  |  | ŋ |
| Trill |  |  |  | r |  |  |  |
| Fricative |  | f v | ð | s z | ʃ ʒ |  | x ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y |  | u ɯ |
| Close-mid | e ø |  | o |
| Mid |  | ə |  |
| Near-open | æ |  |  |
| Open |  |  | ɑ |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [ŋɡ] [ʃtʃ] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ö⟩ | [ø] |  |
| ⟨а⟩ | [ɑ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɣ] |  |
| ⟨д⟩ | [ð] |  |
| ⟨е⟩ | [e] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нг⟩ | [ŋɡ] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ə] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] [u] |  |
| ⟨я⟩ | [ja] [ɑ] |  |
| ⟨ё⟩ | [jo] [o] |  |
| ⟨ҥ⟩ | [ŋ] |  |
| ⟨ӓ⟩ | [æ] |  |
| ⟨ӧ⟩ | [ø] |  |
| ⟨ӱ⟩ | [y] |  |
| ⟨ӹ⟩ | [ɯ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mrj")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hiligaynon](hil.md) · [Home](../index.md) · [Hindi →](hi.md)
