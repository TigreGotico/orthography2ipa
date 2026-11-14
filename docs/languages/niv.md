# Gilyak (`niv`)

<!-- atlas:summary begin -->
Gilyak is a Nivkh language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `niv` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `niv` |
| ISO 639-3 | [niv](https://iso639-3.sil.org/code/niv), Gilyak |
| Wikipedia | [Nivkh language](https://en.wikipedia.org/wiki/Nivkh_language) |
| Family | [Nivkh](by-family.md#nivkh) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nivkh](https://tigregotico.github.io/orthography2ipa/#x-clade-nivk1234) `x-clade-nivk1234` |
| Explorer | [`niv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#niv) |
| Spec file | [`niv.json`](../../orthography2ipa/data/niv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Nivkh (Gilyak) is a Paleosiberian language isolate, this entry follows the Amur dialect Cyrillic alphabet (Gruzdeva 1998).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1998 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 57 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/niv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `niv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-niv_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Amur Nivkh (gily1242)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/gily1242)
2. <a id="src-gruzdeva1998"></a>Gruzdeva, Ekaterina (1998). *Nivkh (Languages of the World/Materials 111)*. Lincom Europa.
3. <a id="src-niv_orthography"></a>Wikipedia contributors (2024). *Nivkh language, writing system and phonology*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Nivkh_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `niv` | gold | lexicon-derived | CC BY 4.0 | 833 | 0.0695 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `niv` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 624 | 0.2246 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 46 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  | c ɟ | k kʰ ɡ | q qʰ |  |
| Affricate |  |  | ts | tʃ |  |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |  |
| Trill |  |  | r r̥ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ | x ɣ | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Near-open | æ |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [æ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дь⟩ | [ɟ] |  |
| ⟨е⟩ | [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨кʼ⟩ | [kʰ] |  |
| ⟨к’⟩ | [kʰ] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨пʼ⟩ | [pʰ] |  |
| ⟨п’⟩ | [pʰ] |  |
| ⟨р⟩ | [r] |  |
| ⟨р̌⟩ | [r̥] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨тʼ⟩ | [tʰ] |  |
| ⟨ть⟩ | [c] |  |
| ⟨т’⟩ | [tʰ] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ҏ⟩ | [r̥] |  |
| ⟨ғ⟩ | [ɣ] |  |
| ⟨ҕ⟩ | [ʁ] |  |
| ⟨қ⟩ | [q] |  |
| ⟨ҟ⟩ | [qʰ] |  |
| ⟨ҳ⟩ | [χ] |  |
| ⟨ӄ⟩ | [q] |  |
| ⟨ӄʼ⟩ | [qʰ] |  |
| ⟨ӄ’⟩ | [qʰ] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӷ⟩ | [ʁ] |  |
| ⟨ӻ⟩ | [ʁ] |  |
| ⟨ӽ⟩ | [χ] |  |
| ⟨ӿ⟩ | [h] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "niv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← German](de-DE.md) · [Home](../index.md) · [Gipuzkoan Basque →](eu-x-gipuzkoa.md)
