# Dzongkha (`dz`)

<!-- atlas:summary begin -->
Dzongkha is a Sino-Tibetan language, written in the Tibetan script. Glottolog places it in Bhutan, China, India and Nepal. The `dz` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `dz` |
| ISO 639-3 | [dzo](https://iso639-3.sil.org/code/dzo), Dzongkha |
| Glottolog | [dzon1239](https://glottolog.org/resource/languoid/id/dzon1239), Dzongkha |
| Wikidata | [Q33081](https://www.wikidata.org/wiki/Q33081) |
| Wikipedia | [Dzongkha](https://en.wikipedia.org/wiki/Dzongkha) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bhutan](by-region.md#bhutan), [China](by-region.md#china), [India](by-region.md#india), [Nepal](by-region.md#nepal) |
| Script | [Tibetan](by-script.md#tibetan) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Sino-Tibetan](https://tigregotico.github.io/orthography2ipa/#x-clade-sino1245) `x-clade-sino1245` |
| Explorer | [`dz` in the data explorer](https://tigregotico.github.io/orthography2ipa/#dz) |
| Spec file | [`dz.json`](../../orthography2ipa/data/dz.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Dzongkha (རྫོང་ཁ), national language of Bhutan, written in the Tibetan script (Uchen/Joyi).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1988 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 132 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/dz.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `dz` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-dz_wiki"></a>Wikipedia contributors (2024). *Dzongkha language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Dzongkha)
2. <a id="src-vandriem1998"></a>van Driem, George (1998). *Dzongkha*. Research School CNWS, Leiden University.
3. <a id="src-phoible"></a>Moran, Steven & McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/)
4. <a id="src-wikipron"></a>Lee, Jackson L. et al. (2020). *WikiPron: A Tool for Extracting Pronunciation Data from Wiktionary*. LREC. [github.com](https://github.com/CUNY-CL/wikipron)
5. <a id="src-mazaudon_michailovsky1988"></a>Mazaudon, Martine & Michailovsky, Boyd (1988). *Lost syllables and tone contour in Dzongkha (Bhutan)*. In: Bradley, D. et al. (eds.), Prosodic Analysis and Asian Linguistics, Pacific Linguistics C-104, pp. 115-136. Cited: 115-136.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `dz` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 230 | 0.3392 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 70 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ | t tʰ | ʈ ʈʰ |  | k kʰ |  |
| Affricate |  | t͡s t͡sʰ |  | t͡ɕ t͡ɕʰ |  |  |
| Nasal | m | n |  | ɲ | ŋ |  |
| Trill |  | r |  |  |  |  |
| Fricative |  | s z | ʂ | ɕ ʑ |  | h |
| Lateral fricative |  | ɬ |  |  |  |  |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u uː |
| Close-mid | e eː ø øː | o oː |
| Open-mid | ɛ ɛː |  |
| Open |  | ɑ ɑː |

Sequences that the spec writes as one unit: [eː˥] [eː˩] [e˥] [e˩] [iː˥] [iː˩] [i˥] [i˩] [oː˥] [oː˩] [o˥] [o˩] [uː˥] [uː˩] [u˥] [u˩] [w] [yː˥] [yː˩] [øː˥] [øː˩] [ɑː˥] [ɑː˩] [ɑ˥] [ɑ˩] [ɛː˥] [ɛː˩] [ː].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨་⟩ | ∅ |  |
| ⟨ཀ⟩ | [k] |  |
| ⟨ཀྭ⟩ | [k] |  |
| ⟨ཀྱ⟩ | [t͡ɕ] |  |
| ⟨ཀྲ⟩ | [ʈ] |  |
| ⟨ཀླ⟩ | [l] |  |
| ⟨ཁ⟩ | [kʰ] |  |
| ⟨ཁྭ⟩ | [kʰ] |  |
| ⟨ཁྱ⟩ | [t͡ɕʰ] |  |
| ⟨ཁྲ⟩ | [ʈʰ] |  |
| ⟨ག⟩ | [k] | after vowel [k] · before consonant ∅ |
| ⟨གཡ⟩ | [j] |  |
| ⟨གྭ⟩ | [k] |  |
| ⟨གྱ⟩ | [t͡ɕ] |  |
| ⟨གྲ⟩ | [ʈ] |  |
| ⟨གླ⟩ | [l] |  |
| ⟨ང⟩ | [ŋ] | after vowel [ŋ] |
| ⟨ཅ⟩ | [t͡ɕ] |  |
| ⟨ཅྭ⟩ | [t͡ɕ] |  |
| ⟨ཆ⟩ | [t͡ɕʰ] |  |
| ⟨ཇ⟩ | [t͡ɕ] |  |
| ⟨ཉ⟩ | [ɲ] |  |
| ⟨ཉྭ⟩ | [ɲ] |  |
| ⟨ཏ⟩ | [t] |  |
| ⟨ཏྭ⟩ | [t] |  |
| ⟨ཏྲ⟩ | [ʈ] |  |
| ⟨ཐ⟩ | [tʰ] |  |
| ⟨ཐྲ⟩ | [ʈʰ] |  |
| ⟨ད⟩ | [t] | after vowel [t] · before consonant ∅ |
| ⟨དབ⟩ | [w] |  |
| ⟨དྭ⟩ | [t] |  |
| ⟨དྲ⟩ | [ʈ] |  |
| ⟨ན⟩ | [n] | after vowel [n] |
| ⟨པ⟩ | [p] |  |
| ⟨པྱ⟩ | [t͡ɕ] |  |
| ⟨པྲ⟩ | [ʈ] |  |
| ⟨ཕ⟩ | [pʰ] |  |
| ⟨ཕྱ⟩ | [t͡ɕʰ] |  |
| ⟨ཕྲ⟩ | [ʈʰ] |  |
| ⟨བ⟩ | [p] | after vowel [p] · before consonant ∅ |
| ⟨བྱ⟩ | [t͡ɕ] |  |
| ⟨བྲ⟩ | [ʈ] |  |
| ⟨བླ⟩ | [l] |  |
| ⟨མ⟩ | [m] | after vowel [m] · before consonant ∅ |
| ⟨མྱ⟩ | [ɲ] |  |
| ⟨མྲ⟩ | [m] |  |
| ⟨ཙ⟩ | [t͡s] |  |
| ⟨ཙྭ⟩ | [t͡s] |  |
| ⟨ཚ⟩ | [t͡sʰ] |  |
| ⟨ཚྭ⟩ | [t͡sʰ] |  |
| ⟨ཛ⟩ | [t͡s] |  |
| ⟨ཛླ⟩ | [l] |  |
| ⟨ཝ⟩ | [w] |  |
| ⟨ཞ⟩ | [ʑ] |  |
| ⟨ཞྭ⟩ | [ʑ] |  |
| ⟨ཟ⟩ | [z] |  |
| ⟨ཟྭ⟩ | [z] |  |
| ⟨ཟླ⟩ | [l] |  |
| ⟨འ⟩ | ∅ | after vowel ∅ · before consonant ∅ |
| ⟨འཁྱ⟩ | [t͡ɕʰ] |  |
| ⟨འགྱ⟩ | [t͡ɕ] |  |
| ⟨ཡ⟩ | [j] |  |
| ⟨ར⟩ | [r] |  |
| ⟨རྐ⟩ | [k] |  |
| ⟨རྐྱ⟩ | [t͡ɕ] |  |
| ⟨རྒ⟩ | [k] |  |
| ⟨རྒྱ⟩ | [t͡ɕ] |  |
| ⟨རྔ⟩ | [ŋ] |  |
| ⟨རྗ⟩ | [t͡ɕ] |  |
| ⟨རྙ⟩ | [ɲ] |  |
| ⟨རྟ⟩ | [t] |  |
| ⟨རྡ⟩ | [t] |  |
| ⟨རྣ⟩ | [n] |  |
| ⟨རྦ⟩ | [p] |  |
| ⟨རྨ⟩ | [m] |  |
| ⟨རྨྱ⟩ | [ɲ] |  |
| ⟨རྩ⟩ | [t͡s] |  |
| ⟨རྫ⟩ | [t͡s] |  |
| ⟨རྭ⟩ | [r] |  |
| ⟨རླ⟩ | [l] |  |
| ⟨ལ⟩ | [l] |  |
| ⟨ལྐ⟩ | [k] |  |
| ⟨ལྒ⟩ | [k] |  |
| ⟨ལྔ⟩ | [ŋ] |  |
| ⟨ལྕ⟩ | [t͡ɕ] |  |
| ⟨ལྗ⟩ | [t͡ɕ] |  |
| ⟨ལྟ⟩ | [t] |  |
| ⟨ལྡ⟩ | [t] |  |
| ⟨ལྤ⟩ | [p] |  |
| ⟨ལྦ⟩ | [w] |  |
| ⟨ལྭ⟩ | [l] |  |
| ⟨ལྷ⟩ | [ɬ] |  |
| ⟨ཤ⟩ | [ɕ] |  |
| ⟨ཤྭ⟩ | [ɕ] |  |
| ⟨ཤྲ⟩ | [ʂ] |  |
| ⟨ས⟩ | [s] |  |
| ⟨སྐ⟩ | [k] |  |
| ⟨སྐྱ⟩ | [t͡ɕ] |  |
| ⟨སྐྲ⟩ | [ʈ] |  |
| ⟨སྒ⟩ | [k] |  |
| ⟨སྒྱ⟩ | [t͡ɕ] |  |
| ⟨སྒྲ⟩ | [ʈ] |  |
| ⟨སྔ⟩ | [ŋ] |  |
| ⟨སྙ⟩ | [ɲ] |  |
| ⟨སྟ⟩ | [t] |  |
| ⟨སྡ⟩ | [t] |  |
| ⟨སྣ⟩ | [n] |  |
| ⟨སྤ⟩ | [p] |  |
| ⟨སྤྱ⟩ | [t͡ɕ] |  |
| ⟨སྤྲ⟩ | [ʈ] |  |
| ⟨སྦ⟩ | [p] |  |
| ⟨སྦྱ⟩ | [t͡ɕ] |  |
| ⟨སྦྲ⟩ | [ʈ] |  |
| ⟨སྨ⟩ | [m] |  |
| ⟨སྨྱ⟩ | [ɲ] |  |
| ⟨སྨྲ⟩ | [m] |  |
| ⟨སྩ⟩ | [t͡s] |  |
| ⟨སྭ⟩ | [s] |  |
| ⟨སྲ⟩ | [s] |  |
| ⟨སླ⟩ | [l] |  |
| ⟨ཧ⟩ | [h] |  |
| ⟨ཧྭ⟩ | [h] |  |
| ⟨ཧྱ⟩ | [ɕ] |  |
| ⟨ཧྲ⟩ | [r] |  |
| ⟨ཨ⟩ | [ɑ] | before vowel ∅ |
| ⟨ཱ⟩ | [ː] |  |
| ⟨ི⟩ | [i] |  |
| ⟨ུ⟩ | [u] |  |
| ⟨ེ⟩ | [e] |  |
| ⟨ཻ⟩ | [e] |  |
| ⟨ོ⟩ | [o] |  |
| ⟨ཽ⟩ | [o] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 83 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `DZ_UMLAUT_ད_ɑ_HIGH` | /ɑ/ → [eː˥], before [t], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ད_HIGH` | /ɑ/ → [eː˥], before [t], spelled ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ད_ɑ_LOW` | /ɑ/ → [eː˩], before [t], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ད_LOW` | /ɑ/ → [eː˩], before [t], spelled ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ད_o_HIGH` | /o/ → [øː˥], before [t], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ད_o_LOW` | /o/ → [øː˩], before [t], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ད_u_HIGH` | /u/ → [yː˥], before [t], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ད_u_LOW` | /u/ → [yː˩], before [t], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ད_i_HIGH` | /i/ → [iː˥], before [t], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ད_i_LOW` | /i/ → [iː˩], before [t], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ད_e_HIGH` | /e/ → [eː˥], before [t], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ད_e_LOW` | /e/ → [eː˩], before [t], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ད⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_ɑ_HIGH` | /ɑ/ → [eː˥], before [n], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ན_HIGH` | /ɑ/ → [eː˥], before [n], spelled ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_ɑ_LOW` | /ɑ/ → [eː˩], before [n], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ན_LOW` | /ɑ/ → [eː˩], before [n], spelled ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_o_HIGH` | /o/ → [øː˥], before [n], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_o_LOW` | /o/ → [øː˩], before [n], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_u_HIGH` | /u/ → [yː˥], before [n], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_u_LOW` | /u/ → [yː˩], before [n], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_i_HIGH` | /i/ → [iː˥], before [n], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_i_LOW` | /i/ → [iː˩], before [n], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_e_HIGH` | /e/ → [eː˥], before [n], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ན_e_LOW` | /e/ → [eː˩], before [n], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ན⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_ɑ_HIGH` | /ɑ/ → [ɛː˥], before [l], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ལ_HIGH` | /ɑ/ → [ɛː˥], before [l], spelled ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_ɑ_LOW` | /ɑ/ → [ɛː˩], before [l], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ལ_LOW` | /ɑ/ → [ɛː˩], before [l], spelled ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_o_HIGH` | /o/ → [øː˥], before [l], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_o_LOW` | /o/ → [øː˩], before [l], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_u_HIGH` | /u/ → [yː˥], before [l], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_u_LOW` | /u/ → [yː˩], before [l], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_i_HIGH` | /i/ → [iː˥], before [l], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_i_LOW` | /i/ → [iː˩], before [l], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_e_HIGH` | /e/ → [ɛː˥], before [l], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ལ_e_LOW` | /e/ → [ɛː˩], before [l], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ལ⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_ɑ_HIGH` | /ɑ/ → [ɛː˥], before [s], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ས_HIGH` | /ɑ/ → [ɛː˥], before [s], spelled ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_ɑ_LOW` | /ɑ/ → [ɛː˩], before [s], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ས_LOW` | /ɑ/ → [ɛː˩], before [s], spelled ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_o_HIGH` | /o/ → [øː˥], before [s], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_o_LOW` | /o/ → [øː˩], before [s], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_u_HIGH` | /u/ → [yː˥], before [s], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_u_LOW` | /u/ → [yː˩], before [s], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_i_HIGH` | /i/ → [iː˥], before [s], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_i_LOW` | /i/ → [iː˩], before [s], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_e_HIGH` | /e/ → [ɛː˥], before [s], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ས_e_LOW` | /e/ → [ɛː˩], before [s], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ས⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_ɑ_HIGH` | /ɑ/ → [ɑː˥], before [r], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ར_HIGH` | /ɑ/ → [ɑː˥], before [r], spelled ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_ɑ_LOW` | /ɑ/ → [ɑː˩], before [r], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_INH_ར_LOW` | /ɑ/ → [ɑː˩], before [r], spelled ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_o_HIGH` | /o/ → [oː˥], before [r], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_o_LOW` | /o/ → [oː˩], before [r], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_u_HIGH` | /u/ → [uː˥], before [r], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_u_LOW` | /u/ → [uː˩], before [r], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_i_HIGH` | /i/ → [iː˥], before [r], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_i_LOW` | /i/ → [iː˩], before [r], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_e_HIGH` | /e/ → [eː˥], before [r], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_UMLAUT_ར_e_LOW` | /e/ → [eː˩], before [r], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more, before ⟨ར⟩ | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988), Driem 1998 |
| `DZ_TONE_PREFIXED_SONORANT_ɑ` | /ɑ/ → [ɑ˥], after ⟨གཡ⟩ ⟨ང⟩ ⟨ཉ⟩ ⟨ཉྭ⟩ ⟨ན⟩ ⟨མ⟩ ⟨མྱ⟩ ⟨མྲ⟩ and 4 more, with more context in the spec | - | Driem 1998 |
| `DZ_TONE_PREFIXED_SONORANT_INH` | /ɑ/ → [ɑ˥], after [h] [j] [k] [kʰ] [l] [m] [n] [p] and 21 more, spelled ⟨གཡ⟩ ⟨ང⟩ ⟨ཉ⟩ ⟨ཉྭ⟩ ⟨ན⟩ ⟨མ⟩ ⟨མྱ⟩ ⟨མྲ⟩ and 4 more, after ⟨ག⟩ ⟨ད⟩ ⟨བ⟩ ⟨མ⟩ ⟨འ⟩ | - | Driem 1998 |
| `DZ_TONE_PREFIXED_SONORANT_i` | /i/ → [i˥], after ⟨གཡ⟩ ⟨ང⟩ ⟨ཉ⟩ ⟨ཉྭ⟩ ⟨ན⟩ ⟨མ⟩ ⟨མྱ⟩ ⟨མྲ⟩ and 4 more, with more context in the spec | - | Driem 1998 |
| `DZ_TONE_PREFIXED_SONORANT_u` | /u/ → [u˥], after ⟨གཡ⟩ ⟨ང⟩ ⟨ཉ⟩ ⟨ཉྭ⟩ ⟨ན⟩ ⟨མ⟩ ⟨མྱ⟩ ⟨མྲ⟩ and 4 more, with more context in the spec | - | Driem 1998 |
| `DZ_TONE_PREFIXED_SONORANT_e` | /e/ → [e˥], after ⟨གཡ⟩ ⟨ང⟩ ⟨ཉ⟩ ⟨ཉྭ⟩ ⟨ན⟩ ⟨མ⟩ ⟨མྱ⟩ ⟨མྲ⟩ and 4 more, with more context in the spec | - | Driem 1998 |
| `DZ_TONE_PREFIXED_SONORANT_o` | /o/ → [o˥], after ⟨གཡ⟩ ⟨ང⟩ ⟨ཉ⟩ ⟨ཉྭ⟩ ⟨ན⟩ ⟨མ⟩ ⟨མྱ⟩ ⟨མྲ⟩ and 4 more, with more context in the spec | - | Driem 1998 |
| `DZ_TONE_HIGH_ɑ` | /ɑ/ → [ɑ˥], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_INH_HIGH` | /ɑ/ → [ɑ˥], after [h] [j] [k] [kʰ] [l] [m] [n] [p] and 21 more, spelled ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_HIGH_i` | /i/ → [i˥], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_HIGH_u` | /u/ → [u˥], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_HIGH_e` | /e/ → [e˥], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_HIGH_o` | /o/ → [o˥], after ⟨ཀ⟩ ⟨ཀྭ⟩ ⟨ཀྱ⟩ ⟨ཀྲ⟩ ⟨ཀླ⟩ ⟨ཁ⟩ ⟨ཁྭ⟩ ⟨ཁྱ⟩ and 69 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_LOW_ɑ` | /ɑ/ → [ɑ˩], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_INH_LOW` | /ɑ/ → [ɑ˩], after [h] [j] [k] [kʰ] [l] [m] [n] [p] and 21 more, spelled ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_LOW_i` | /i/ → [i˩], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_LOW_u` | /u/ → [u˩], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_LOW_e` | /e/ → [e˩], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_TONE_LOW_o` | /o/ → [o˩], after ⟨ག⟩ ⟨གཡ⟩ ⟨གྭ⟩ ⟨གྱ⟩ ⟨གྲ⟩ ⟨གླ⟩ ⟨ང⟩ ⟨ཇ⟩ and 39 more | - | [Mazaudon 1988](#src-mazaudon_michailovsky1988) |
| `DZ_SUFFIX_DROP_ས` | /s sɑ/ → ∅, after [ɑ] [i] [u] [e] [o] [ɛ] [ø] [y] and 9 more, spelled ⟨ས⟩ | - | Driem 1998 |
| `DZ_SUFFIX_DROP_ད` | /t tɑ/ → ∅, after [ɑ] [i] [u] [e] [o] [ɛ] [ø] [y] and 9 more, spelled ⟨ད⟩ | - | Driem 1998 |
| `DZ_SUFFIX_DROP_ལ` | /l lɑ/ → ∅, after [ɑ] [i] [u] [e] [o] [ɛ] [ø] [y] and 9 more, spelled ⟨ལ⟩ | - | Driem 1998 |
| `DZ_SUFFIX_DROP_ར` | /r rɑ/ → ∅, after [ɑ] [i] [u] [e] [o] [ɛ] [ø] [y] and 9 more, spelled ⟨ར⟩ | - | Driem 1998 |
| `DZ_POST_SUFFIX_S` | /s sɑ/ → ∅, after [k] [ŋ] [n] [m] [p] [t] [l] [r] and 4 more, spelled ⟨ས⟩ | - | Driem 1998 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "dz")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Dutch](nl-NL.md) · [Home](../index.md) · [Eastern Andalusian Spanish →](es-ES-x-andalusi-e.md)
