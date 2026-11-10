# Kalmyk (`xal`)

<!-- atlas:summary begin -->
Kalmyk is a Mongolic language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `xal` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `xal` |
| ISO 639-3 | [xal](https://iso639-3.sil.org/code/xal), Kalmyk |
| Glottolog | [kalm1244](https://glottolog.org/resource/languoid/id/kalm1244), Kalmyk |
| Wikidata | [Q33634](https://www.wikidata.org/wiki/Q33634) |
| Wikipedia | [Kalmyk Oirat](https://en.wikipedia.org/wiki/Kalmyk_Oirat) |
| Family | [Mongolic](by-family.md#mongolic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Mongolic](https://tigregotico.github.io/orthography2ipa/#x-clade-mong1349) `x-clade-mong1349` |
| Explorer | [`xal` in the data explorer](https://tigregotico.github.io/orthography2ipa/#xal) |
| Spec file | [`xal.json`](../../orthography2ipa/data/xal.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kalmyk Oirat (хальмг келн), the Mongolic language of Kalmykia, written since 1938 in a Cyrillic alphabet: the Russian letters plus Әә /æ/, Өө /ø/, Үү /y/, Җҗ /d͡ʒ/, Ңң /ŋ/ and Һһ /ɣ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2024 to 2026. 3 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 45 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/xal.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `xal` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-xal_wiki"></a>Wikipedia contributors (2024). *Kalmyk language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kalmyk_Oirat)
2. <a id="src-kalmyk_alphabet_ipa_wiki"></a>Wikipedia contributors (2026). *Kalmyk Oirat, Alphabet matching table and Phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kalmyk_Oirat)
3. <a id="src-cyrillic_alphabets_wiki"></a>Wikipedia contributors (2026). *Cyrillic alphabets, Kalmyk and Buryat sections*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Cyrillic_alphabets)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `xal` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 318 | 0.2813 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 45 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | ɢ |
| Affricate |  |  | t͡s | d͡ʒ t͡ʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕː | x ɣ |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u uː |
| Close-mid | e eː ø øː | o oː |
| Near-open | æ æː |  |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [jʊ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨аа⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] [ɢ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [e] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨ии⟩ | [iː] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨оо⟩ | [oː] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨уу⟩ | [uː] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [t͡s] |  |
| ⟨ч⟩ | [t͡ʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕː] |  |
| ⟨ы⟩ | [i] |  |
| ⟨э⟩ | [e] |  |
| ⟨ээ⟩ | [eː] |  |
| ⟨ю⟩ | [jʊ] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨җ⟩ | [d͡ʒ] |  |
| ⟨ң⟩ | [ŋ] |  |
| ⟨ү⟩ | [y] |  |
| ⟨үү⟩ | [yː] |  |
| ⟨һ⟩ | [ɣ] |  |
| ⟨ә⟩ | [æ] |  |
| ⟨әә⟩ | [æː] |  |
| ⟨ө⟩ | [ø] |  |
| ⟨өө⟩ | [øː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "xal")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kaingang](kgp.md) · [Home](../index.md) · [Kannada →](kn.md)
