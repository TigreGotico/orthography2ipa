# Khalaj (`klj`)

<!-- atlas:summary begin -->
Khalaj is a Turkic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `klj` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `klj` |
| ISO 639-3 | [klj](https://iso639-3.sil.org/code/klj), Khalaj |
| Wikipedia | [Khalaj language](https://en.wikipedia.org/wiki/Khalaj_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Turkic](https://tigregotico.github.io/orthography2ipa/#x-clade-turk1311) `x-clade-turk1311` |
| Explorer | [`klj` in the data explorer](https://tigregotico.github.io/orthography2ipa/#klj) |
| Spec file | [`klj.json`](../../orthography2ipa/data/klj.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Khalaj is a divergent Turkic language of central Iran, here written in a Latin orthography of the Azerbaijani/Turkish type.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1988 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 33 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/klj.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `klj` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-klj_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Khalaj Turkic (turk1303)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/turk1303)
2. <a id="src-doerfer1988"></a>Doerfer, Gerhard (1988). *Grammatik des Chaladsch (Khalaj Grammar)*. Turcologica 4. Harrassowitz, Wiesbaden.
3. <a id="src-doerfer_iranica"></a>Doerfer, Gerhard (2011). *ḴALAJ ii. Ḵalaji Language*. Encyclopaedia Iranica. [iranicaonline.org](https://www.iranicaonline.org/articles/khalaj-ii-language/)
4. <a id="src-klj_orthography"></a>Wikipedia contributors (2024). *Khalaj language, writing system and phonology*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Khalaj_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `klj` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 155 | 0.2995 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x ɣ |  | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Near-open | æ |  |
| Open |  | ɑ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [dʒ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [tʃ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |
| ⟨ğ⟩ | [ɣ] |  |
| ⟨ı⟩ | [ɯ] |  |
| ⟨ş⟩ | [ʃ] |  |
| ⟨ə⟩ | [æ] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "klj")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Khakas](kjh.md) · [Home](../index.md) · [Khanty →](kca.md)
