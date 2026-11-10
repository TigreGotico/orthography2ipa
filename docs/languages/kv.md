# Komi (`kv`)

<!-- atlas:summary begin -->
Komi is an Uralic language, written in the Cyrillic script. Glottolog places it in Russia. The `kv` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kv` |
| ISO 639-3 | [kom](https://iso639-3.sil.org/code/kom), Komi |
| Glottolog | [komi1267](https://glottolog.org/resource/languoid/id/komi1267), Komi |
| Wikidata | [Q36126](https://www.wikidata.org/wiki/Q36126) |
| Wikipedia | [Komi language](https://en.wikipedia.org/wiki/Komi_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1918, living |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`kv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kv) |
| Spec file | [`kv.json`](../../orthography2ipa/data/kv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Komi (коми кыв), a Permic (Uralic) language of the Komi Republic, Russia, the Komi-Zyrian literary standard. INPUT CONTRACT: modern Komi Cyrillic text, Unicode NFC, lower-cased by the caller if case-folding is desired. Orthography: the Russian alphabet plus ⟨І і⟩ ('hard i') and ⟨Ӧ ӧ⟩ /ɘ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 74 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-komi_language_wiki"></a>Wikipedia contributors (2024). *Komi language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Komi_language)
2. <a id="src-komi_alphabet_wikipedia"></a>Wikipedia contributors (2026). *Komi language, Writing system (Cyrillic alphabet with IPA values) and Phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Komi_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kv` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 906 | 0.1570 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 75 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c ɟ | k ɡ |
| Affricate |  |  | ts | dʒ tʃ | dʑ tɕ |  |
| Nasal | m |  | n |  | ɲ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʃː ʒ | ɕ ʑ | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l ɫ |  | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e | ɘ | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ca] [ce] [ci] [co] [cu] [ja] [je] [jo] [ju] [ɕa] [ɕe] [ɕi] [ɕo] [ɕu] [ɟa] [ɟe] [ɟi] [ɟo] [ɟu] [ɲa] [ɲe] [ɲi] [ɲo] [ɲu] [ʃtʃ] [ʎa] [ʎe] [ʎi] [ʎo] [ʎu] [ʑa] [ʑe] [ʑi] [ʑo] [ʑu] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨де⟩ | [ɟe] |  |
| ⟨дж⟩ | [dʒ] |  |
| ⟨дз⟩ | [dʑ] |  |
| ⟨ди⟩ | [ɟi] |  |
| ⟨дь⟩ | [ɟ] |  |
| ⟨дю⟩ | [ɟu] |  |
| ⟨дя⟩ | [ɟa] |  |
| ⟨дё⟩ | [ɟo] |  |
| ⟨е⟩ | [e] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨зе⟩ | [ʑe] |  |
| ⟨зи⟩ | [ʑi] |  |
| ⟨зь⟩ | [ʑ] |  |
| ⟨зю⟩ | [ʑu] |  |
| ⟨зя⟩ | [ʑa] |  |
| ⟨зё⟩ | [ʑo] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [ɫ] |  |
| ⟨ле⟩ | [ʎe] |  |
| ⟨ли⟩ | [ʎi] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨лю⟩ | [ʎu] |  |
| ⟨ля⟩ | [ʎa] |  |
| ⟨лё⟩ | [ʎo] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨не⟩ | [ɲe] |  |
| ⟨ни⟩ | [ɲi] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨ню⟩ | [ɲu] |  |
| ⟨ня⟩ | [ɲa] |  |
| ⟨нё⟩ | [ɲo] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨се⟩ | [ɕe] |  |
| ⟨си⟩ | [ɕi] |  |
| ⟨сь⟩ | [ɕ] |  |
| ⟨сю⟩ | [ɕu] |  |
| ⟨ся⟩ | [ɕa] |  |
| ⟨сё⟩ | [ɕo] |  |
| ⟨т⟩ | [t] |  |
| ⟨те⟩ | [ce] |  |
| ⟨ти⟩ | [ci] |  |
| ⟨тш⟩ | [tʃ] |  |
| ⟨ть⟩ | [c] |  |
| ⟨тю⟩ | [cu] |  |
| ⟨тя⟩ | [ca] |  |
| ⟨тё⟩ | [co] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] [ʃː] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [u] [ju] |  |
| ⟨я⟩ | [a] [ja] |  |
| ⟨ё⟩ | [o] [jo] |  |
| ⟨і⟩ | [i] |  |
| ⟨ӧ⟩ | [ɘ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Komering](kge.md) · [Home](../index.md) · [Komi-Permyak →](koi.md)
