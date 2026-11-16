# Southern Dagaare (`dga`)

<!-- atlas:summary begin -->
Southern Dagaare is an Atlantic-Congo language, written in the Latin script. Glottolog places it in the Africa and North America macroareas. The `dga` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `dga` |
| Wikipedia | [Dagaare language](https://en.wikipedia.org/wiki/Dagaare_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#several-macroareas), [North America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Niger-Congo (family node)](https://tigregotico.github.io/orthography2ipa/#nic) `nic` |
| Explorer | [`dga` in the data explorer](https://tigregotico.github.io/orthography2ipa/#dga) |
| Spec file | [`dga.json`](../../orthography2ipa/data/dga.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Central Dagaare (Dàgáárè), a Gur / Mabia (Atlantic-Congo) language of northwestern Ghana and southern Burkina Faso. Glottolog sout2789 'Central Dagaare' carries ISO 639-3 dga, Ethnologue names the same code Southern Dagaare.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2022 to 2026. [Sources](#sources) lists them. The spec file writes all 94 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/dga.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `dga` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wikidata_Q123351833"></a>Wikidata contributors (2026). *Wikidata item Q123351833*. Wikimedia Foundation. [wikidata.org](https://www.wikidata.org/wiki/Q123351833)
2. <a id="src-angsongna2020"></a>Angsongna, Alexander & Akinbo, Samuel (2022). *Dàgáárè (Central)*. Journal of the International Phonetic Association 52(2), 341-367 (Illustrations of the IPA). [doi.org](https://doi.org/10.1017/S0025100320000225)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `primary_sources` | `dga` | gold | expert-human | Apache-2.0 (this repository). Each row quotes and cites a published example. | 35 | 0.1143 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 108 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ |  |
| Affricate |  |  |  | d͡ʒ t͡ʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Fricative |  | f v | s z |  |  |  | h |
| Approximant |  |  | ɹ |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː ì ìː í íː î îː |  | u uː ù ùː ú úː û ûː |
| Near-close | ɪ ɪː ɪ̀ ɪ̀ː ɪ́ ɪ́ː ɪ̂ ɪ̂ː |  | ʊ ʊː ʊ̀ ʊ̀ː ʊ́ ʊ́ː ʊ̂ ʊ̂ː |
| Close-mid | e eː è èː é éː ê êː |  | o oː ò òː ó óː ô ôː |
| Mid |  | ə əː ə̀ ə̀ː ə́ ə́ː ə̂ ə̂ː |  |
| Open-mid | ɛ ɛː ɛ̀ ɛ̀ː ɛ́ ɛ́ː ɛ̂ ɛ̂ː |  | ɔ ɔː ɔ̀ ɔ̀ː ɔ́ ɔ́ː ɔ̂ ɔ̂ː |
| Open | a aː à àː á áː â âː |  |  |

Sequences that the spec writes as one unit: [k͡p] [w] [ŋ͡m] [ɡɾ] [ɡ͡b].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [i] [e] [ɪ] |  |
| ⟨ee⟩ | [iː] [eː] [ɪː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨gr⟩ | [ɡɾ] |  |
| ⟨gy⟩ | [d͡ʒ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨kp⟩ | [k͡p] |  |
| ⟨ky⟩ | [t͡ʃ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] [ʊ] |  |
| ⟨oo⟩ | [oː] [ʊː] |  |
| ⟨r⟩ | [ɹ] |  |
| ⟨s⟩ | [s] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨à⟩ | [à] |  |
| ⟨àà⟩ | [àː] |  |
| ⟨àá⟩ | [áː] |  |
| ⟨á⟩ | [á] |  |
| ⟨áà⟩ | [âː] |  |
| ⟨áá⟩ | [áː] |  |
| ⟨â⟩ | [â] |  |
| ⟨è⟩ | [ì] [è] [ɪ̀] |  |
| ⟨èè⟩ | [ìː] [èː] [ɪ̀ː] |  |
| ⟨èé⟩ | [íː] [éː] [ɪ́ː] |  |
| ⟨é⟩ | [í] [é] [ɪ́] |  |
| ⟨éè⟩ | [îː] [êː] [ɪ̂ː] |  |
| ⟨éé⟩ | [íː] [éː] [ɪ́ː] |  |
| ⟨ê⟩ | [î] [ê] [ɪ̂] |  |
| ⟨ì⟩ | [ì] |  |
| ⟨ìì⟩ | [ìː] |  |
| ⟨ìí⟩ | [íː] |  |
| ⟨í⟩ | [í] |  |
| ⟨íì⟩ | [îː] |  |
| ⟨íí⟩ | [íː] |  |
| ⟨î⟩ | [î] |  |
| ⟨ò⟩ | [ò] [ʊ̀] |  |
| ⟨òò⟩ | [òː] [ʊ̀ː] |  |
| ⟨òó⟩ | [óː] [ʊ́ː] |  |
| ⟨ó⟩ | [ó] [ʊ́] |  |
| ⟨óò⟩ | [ôː] [ʊ̂ː] |  |
| ⟨óó⟩ | [óː] [ʊ́ː] |  |
| ⟨ô⟩ | [ô] [ʊ̂] |  |
| ⟨ù⟩ | [ù] |  |
| ⟨ùù⟩ | [ùː] |  |
| ⟨ùú⟩ | [úː] |  |
| ⟨ú⟩ | [ú] |  |
| ⟨úù⟩ | [ûː] |  |
| ⟨úú⟩ | [úː] |  |
| ⟨û⟩ | [û] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ŋm⟩ | [ŋ͡m] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɔɔ⟩ | [ɔː] |  |
| ⟨ɔ̀⟩ | [ɔ̀] |  |
| ⟨ɔ̀ɔ̀⟩ | [ɔ̀ː] |  |
| ⟨ɔ̀ɔ́⟩ | [ɔ́ː] |  |
| ⟨ɔ́⟩ | [ɔ́] |  |
| ⟨ɔ́ɔ̀⟩ | [ɔ̂ː] |  |
| ⟨ɔ́ɔ́⟩ | [ɔ́ː] |  |
| ⟨ɔ̂⟩ | [ɔ̂] |  |
| ⟨ɛ⟩ | [ɛ] |  |
| ⟨ɛɛ⟩ | [ɛː] |  |
| ⟨ɛ̀⟩ | [ɛ̀] |  |
| ⟨ɛ̀ɛ̀⟩ | [ɛ̀ː] |  |
| ⟨ɛ̀ɛ́⟩ | [ɛ́ː] |  |
| ⟨ɛ́⟩ | [ɛ́] |  |
| ⟨ɛ́ɛ̀⟩ | [ɛ̂ː] |  |
| ⟨ɛ́ɛ́⟩ | [ɛ́ː] |  |
| ⟨ɛ̂⟩ | [ɛ̂] |  |
| ⟨ạ⟩ | [ə] |  |
| ⟨ạ̀⟩ | [ə̀] |  |
| ⟨ạ̀ạ̀⟩ | [ə̀ː] |  |
| ⟨ạ̀ạ́⟩ | [ə́ː] |  |
| ⟨ạ́⟩ | [ə́] |  |
| ⟨ạ́ạ̀⟩ | [ə̂ː] |  |
| ⟨ạ́ạ́⟩ | [ə́ː] |  |
| ⟨ạạ⟩ | [əː] |  |
| ⟨ậ⟩ | [ə̂] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "dga")`. They are engine output, not reference transcriptions.

The next table sets the engine output against worked examples printed in a cited source, from the [primary-source gold](../evaluation/datasets.md#primary-source-gold-primary_sources). The rows are spread evenly over that set. The last column says whether the two transcriptions are the same string.

| Spelling | Printed in the source | Engine output | Source, page | Same |
|:--|:--|:--|:--|:--|
| pɛ́gé | /pʰɛ́gí/ | [pʰɛ́ɡí] | Angsongna 2022, p. 343 | no |
| tègè | /tʰìgì/ | [tʰìɡì] | Angsongna 2022, p. 343 | no |
| gàà | /gàː/ | [ɡàː] | Angsongna 2022, p. 343 | no |
| è | /ʔì/ | [ì] | Angsongna 2022, p. 343 | no |
| ségé | /sígí/ | [síɡí] | Angsongna 2022, p. 343 | no |
| kyɛ́ | /t͡ʃɛ́/ | [t͡ʃɛ́] | Angsongna 2022, p. 343 | yes |
| nɛ́nè | /nɛ́nì/ | [nɛ́nì] | Angsongna 2022, p. 343 | yes |
| ŋmáné | /ŋ͡mání/ | [ŋ͡mání] | Angsongna 2022, p. 343 | yes |
| pɛ́gré | /pʰɛ́gɾí/ | [pʰɛ́ɡɾí] | Angsongna 2022, p. 343 | no |
| dê | /dɪ̂/ | [dî] | Angsongna 2022, p. 345 | no |
| vạ | /və́/ | [və] | Angsongna 2022, p. 345 | no |
| dó | /dó/ | [dó] | Angsongna 2022, p. 345 | yes |

Source: Angsongna, Alexander & Akinbo, Samuel (2022). *Dàgáárè (Central)*. Journal of the International Phonetic Association 52(2), 341-367 (Illustrations of the IPA, first published online 14 December 2020). [doi.org](https://doi.org/10.1017/S0025100320000225)
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Southern Altai](alt.md) · [Home](../index.md) · [Southern Min →](nan-Latn-pehoeji.md)
