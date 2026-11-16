# Udmurt (`udm`)

<!-- atlas:summary begin -->
Udmurt is an Uralic language, written in the Cyrillic script. Glottolog places it in Kazakhstan and Russia. The `udm` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `udm` |
| ISO 639-3 | [udm](https://iso639-3.sil.org/code/udm), Udmurt |
| Glottolog | [udmu1245](https://glottolog.org/resource/languoid/id/udmu1245), Udmurt |
| Wikidata | [Q13238](https://www.wikidata.org/wiki/Q13238) |
| Wikipedia | [Udmurt language](https://en.wikipedia.org/wiki/Udmurt_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Kazakhstan](by-region.md#kazakhstan), [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1775, living |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`udm` in the data explorer](https://tigregotico.github.io/orthography2ipa/#udm) |
| Spec file | [`udm.json`](../../orthography2ipa/data/udm.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Udmurt (удмурт кыл), a Permic (Uralic) language of the Udmurt Republic, Russia. INPUT CONTRACT: modern Udmurt Cyrillic text, Unicode NFC (⟨ӝ ӟ ӥ ӧ ӵ⟩ are precomposed characters, not base letter + combining diaeresis).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2018 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 72 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/udm.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `udm` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-udmurt_language_wiki"></a>Wikipedia contributors (2024). *Udmurt language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Udmurt_language)
2. <a id="src-udmurt_alphabet_wikipedia"></a>Wikipedia contributors (2026). *Udmurt language, Orthography (Cyrillic alphabet with IPA values) and Phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Udmurt_language)
3. <a id="src-ganeyev_perevozchikov2018"></a>Ganeyev, Igor', Perevozchikov, Yuriy, Pischlöger, Christian, Bradley, Jeremy (2018). *Марым, лэся…, Udmurt for Beginners (Release 3.0, draft of units 0-10)*. University of Vienna / Ludwig Maximilian University Munich, INFUSE Erasmus+ project. Cited: 10-14. [infuse.finnougristik.uni-muenchen.de](https://www.infuse.finnougristik.uni-muenchen.de/e-learning/udmurt/o5_udmurt.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `udm` | gold | lexicon-derived | CC BY 4.0 | 973 | 0.2110 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 77 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d dʲ t tʲ |  | c ɟ | k ɡ |
| Affricate |  |  | ts | dʒ tʃ | dʑ tɕ |  |
| Nasal | m |  | n |  | ɲ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ ɕː ʑ | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l ɫ |  | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u ɯ |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid |  | ɜ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [dʲa] [dʲe] [dʲi] [dʲo] [dʲu] [ja] [je] [jo] [ju] [tʲa] [tʲe] [tʲi] [tʲo] [tʲu] [ɕa] [ɕe] [ɕi] [ɕo] [ɕu] [ɲa] [ɲe] [ɲi] [ɲo] [ɲu] [ʎa] [ʎe] [ʎi] [ʎo] [ʎu] [ʑa] [ʑe] [ʑi] [ʑo] [ʑu] [ʲ].
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
| ⟨де⟩ | [dʲe] |  |
| ⟨ди⟩ | [dʲi] |  |
| ⟨дю⟩ | [dʲu] |  |
| ⟨дя⟩ | [dʲa] |  |
| ⟨дё⟩ | [dʲo] |  |
| ⟨е⟩ | [je] [e] |  |
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
| ⟨те⟩ | [tʲe] |  |
| ⟨ти⟩ | [tʲi] |  |
| ⟨тю⟩ | [tʲu] |  |
| ⟨тя⟩ | [tʲa] |  |
| ⟨тё⟩ | [tʲo] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕː] [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] [u] |  |
| ⟨я⟩ | [ja] [a] |  |
| ⟨ё⟩ | [jo] [o] |  |
| ⟨ӝ⟩ | [dʒ] |  |
| ⟨ӟ⟩ | [dʑ] |  |
| ⟨ӥ⟩ | [i] |  |
| ⟨ӧ⟩ | [ɜ] [ə] |  |
| ⟨ӵ⟩ | [tʃ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "udm")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ubykh](uby.md) · [Home](../index.md) · [Ukrainian →](uk.md)
