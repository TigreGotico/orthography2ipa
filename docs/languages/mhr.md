# Eastern Mari (`mhr`)

<!-- atlas:summary begin -->
Eastern Mari is a Mari language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `mhr` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mhr` |
| Wikidata | [Q3906614](https://www.wikidata.org/wiki/Q3906614) |
| Wikipedia | [Meadow Mari Wikipedia](https://en.wikipedia.org/wiki/Meadow_Mari_Wikipedia) |
| Family | [Uralic](by-family.md#uralic) > [Mari](by-family.md#uralic--mari) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Mari](https://tigregotico.github.io/orthography2ipa/#chm) `chm` |
| Explorer | [`mhr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mhr) |
| Spec file | [`mhr.json`](../../orthography2ipa/data/mhr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Meadow Mari / Eastern Mari (олык марий), Uralic (Mari) language of the Mari El Republic, Russia. INPUT CONTRACT: modern Meadow Mari Cyrillic orthography, NFC. Orthography: the Russian alphabet plus ⟨Ҥҥ⟩ /ŋ/, ⟨Ӧӧ⟩ /ø/ and ⟨Ӱӱ⟩ /y/ (Alhoniemi 1985, Sec. 1).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1985 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 72 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mhr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mhr` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-alhoniemi1985"></a>Alhoniemi, Alho (1985). *Marin kielioppi*. Suomalais-Ugrilainen Seura. [sgr.fi](https://www.sgr.fi/apuneuvot.html)
2. <a id="src-mhr_wiki"></a>Wikipedia contributors (2024). *Meadow Mari Wikipedia*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Meadow_Mari_Wikipedia)
3. <a id="src-meadow_mari_language_wiki"></a>Wikipedia contributors (2026). *Meadow Mari language, Alphabet and Phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Meadow_Mari_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `mhr` | gold | lexicon-derived | CC BY 4.0 | 992 | 0.1736 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 71 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d dʲ t tʲ |  |  | k ɡ |
| Affricate |  |  | ts | tʃ |  |  |
| Nasal | m |  | n nʲ |  |  | ŋ |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s sʲ z zʲ | ʃ ʒ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e ø | o ɤ |
| Open |  | ɑ |

Sequences that the spec writes as one unit: [dʲa] [dʲe] [dʲi] [dʲo] [dʲu] [ja] [je] [jo] [ju] [nʲa] [nʲe] [nʲi] [nʲo] [nʲu] [sʲa] [sʲe] [sʲi] [sʲo] [sʲu] [tʲa] [tʲe] [tʲi] [tʲo] [tʲu] [zʲa] [zʲe] [zʲi] [zʲo] [zʲu] [ʃtʃ] [ʎa] [ʎe] [ʎi] [ʎo] [ʎu] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [ɑ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨де⟩ | [dʲe] |  |
| ⟨ди⟩ | [dʲi] |  |
| ⟨дь⟩ | [dʲ] |  |
| ⟨дю⟩ | [dʲu] |  |
| ⟨дя⟩ | [dʲa] |  |
| ⟨дё⟩ | [dʲo] |  |
| ⟨е⟩ | [je] [e] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨зе⟩ | [zʲe] |  |
| ⟨зи⟩ | [zʲi] |  |
| ⟨зь⟩ | [zʲ] |  |
| ⟨зю⟩ | [zʲu] |  |
| ⟨зя⟩ | [zʲa] |  |
| ⟨зё⟩ | [zʲo] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨ле⟩ | [ʎe] |  |
| ⟨ли⟩ | [ʎi] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨лю⟩ | [ʎu] |  |
| ⟨ля⟩ | [ʎa] |  |
| ⟨лё⟩ | [ʎo] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨не⟩ | [nʲe] |  |
| ⟨ни⟩ | [nʲi] |  |
| ⟨нь⟩ | [nʲ] |  |
| ⟨ню⟩ | [nʲu] |  |
| ⟨ня⟩ | [nʲa] |  |
| ⟨нё⟩ | [nʲo] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨се⟩ | [sʲe] |  |
| ⟨си⟩ | [sʲi] |  |
| ⟨сь⟩ | [sʲ] |  |
| ⟨сю⟩ | [sʲu] |  |
| ⟨ся⟩ | [sʲa] |  |
| ⟨сё⟩ | [sʲo] |  |
| ⟨т⟩ | [t] |  |
| ⟨те⟩ | [tʲe] |  |
| ⟨ти⟩ | [tʲi] |  |
| ⟨ть⟩ | [tʲ] |  |
| ⟨тю⟩ | [tʲu] |  |
| ⟨тя⟩ | [tʲa] |  |
| ⟨тё⟩ | [tʲo] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɤ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] [u] |  |
| ⟨я⟩ | [ja] [ɑ] |  |
| ⟨ё⟩ | [jo] [o] |  |
| ⟨ҥ⟩ | [ŋ] |  |
| ⟨ӧ⟩ | [ø] |  |
| ⟨ӱ⟩ | [y] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mhr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Eastern Galician](gl-ES-x-oriental.md) · [Home](../index.md) · [Eastern Min →](cdo-Latn-x-buc.md)
