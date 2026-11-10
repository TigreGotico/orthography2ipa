# Southern Yukaghir (`yux`)

<!-- atlas:summary begin -->
Southern Yukaghir is a Yukaghir language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `yux` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `yux` |
| ISO 639-3 | [yux](https://iso639-3.sil.org/code/yux), Southern Yukaghir |
| Wikipedia | [Southern Yukaghir language](https://en.wikipedia.org/wiki/Southern_Yukaghir_language) |
| Family | [Yukaghir](by-family.md#yukaghir) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Yukaghir](https://tigregotico.github.io/orthography2ipa/#x-clade-yuka1259) `x-clade-yuka1259` |
| Explorer | [`yux` in the data explorer](https://tigregotico.github.io/orthography2ipa/#yux) |
| Spec file | [`yux.json`](../../orthography2ipa/data/yux.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Southern (Kolyma) Yukaghir is a Yukaghir language of northeastern Siberia written in a Cyrillic alphabet extended for its palatal and back vowels.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2003 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 35 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/yux.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `yux` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-yux_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Southern Yukaghir (sout2750)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/sout2750)
2. <a id="src-yux_orthography"></a>Wikipedia contributors (2024). *Southern Yukaghir language, writing system and phonology*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Southern_Yukaghir_language)
3. <a id="src-yux_maslova2003"></a>Maslova, Elena (2003). *A Grammar of Kolyma Yukaghir*. Mouton de Gruyter (Mouton Grammar Library 27).
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `yux` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 242 | 0.2711 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  |  | k ɡ |
| Affricate |  |  | tʃ | d͡ʑ |  |
| Nasal | m | n |  | ɲ | ŋ |
| Trill |  | r |  |  |  |
| Fricative |  | s z | ʃ ʒ |  | x |
| Approximant |  |  |  | j |  |
| Lateral approximant |  | l |  | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e ø |  | o |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [w] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дь⟩ | [d͡ʑ] |  |
| ⟨е⟩ | [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨х⟩ | [x] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ө⟩ | [ø] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "yux")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Southern Sotho](st.md) · [Home](../index.md) · [Sranan Tongo →](srn.md)
