# Burmese (`my`)

<!-- atlas:summary begin -->
Burmese is a Sino-Tibetan language, written in the Myanmar script. Glottolog places it in Bangladesh, Myanmar (Burma) and Thailand. The `my` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `my` |
| ISO 639-3 | [mya](https://iso639-3.sil.org/code/mya), Burmese |
| Glottolog | [nucl1310](https://glottolog.org/resource/languoid/id/nucl1310), Burmese |
| Wikidata | [Q9228](https://www.wikidata.org/wiki/Q9228) |
| Wikipedia | [Burmese language](https://en.wikipedia.org/wiki/Burmese_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [Myanmar (Burma)](by-region.md#myanmar-burma), [Thailand](by-region.md#thailand) |
| Script | [Myanmar](by-script.md#myanmar) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1050, living |
| Parent | [Proto-Sino-Tibetan (family node)](https://tigregotico.github.io/orthography2ipa/#sit) `sit` |
| Explorer | [`my` in the data explorer](https://tigregotico.github.io/orthography2ipa/#my) |
| Spec file | [`my.json`](../../orthography2ipa/data/my.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Burmese in the Myanmar script, standard (Yangon) pronunciation. The spec models the syllable as ONSET + RHYME.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1969 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 231 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/my.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `my` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-watkins2001"></a>Watkins, J. W. (2001). *Burmese (Illustrations of the IPA)*. Journal of the International Phonetic Association 31(2), 291-295. Cited: 291-295. [doi.org](https://doi.org/10.1017/S0025100301002122)
2. <a id="src-okell1969"></a>Okell, J. (1969). *A Reference Grammar of Colloquial Burmese*. Oxford University Press.
3. <a id="src-wheatley1990"></a>Wheatley, J. K. (1990). *Burmese, in B. Comrie (ed.), The World's Major Languages*. Oxford University Press.
4. <a id="src-burmese_wiki"></a>Wikipedia contributors (2024). *Burmese alphabet, Burmese phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Burmese_alphabet)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `my` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 7941 | 0.1926 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 127 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ |  | ʔ |
| Affricate |  |  |  |  | dʑ tɕ tɕʰ |  |  |  |
| Nasal | m m̥ |  | n n̥ |  | ɲ ɲ̊ | ŋ ŋ̊ | ɴ |  |
| Fricative |  | ð θ | s sʰ z | ʃ |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l l̥ |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i ì í ḭ |  | u ù ú ṵ |
| Near-close | ɪ |  | ʊ |
| Close-mid | e è é ḛ |  | o o̰ ò ó |
| Mid |  | ə |  |
| Open-mid | ɛ ɛ̀ ɛ́ ɛ̰ |  | ɔ ɔ̀ ɔ́ ɔ̰ |
| Open | a a̰ à á |  |  |

Sequences that the spec writes as one unit: [aɪʔ] [aʊʔ] [aʔ] [a̰ɪɴ] [a̰ɴ] [a̰ʊɴ] [bj] [eɪʔ] [hj] [lj] [mj] [m̥j] [oʊʔ] [o̰ʊɴ] [pj] [pʰj] [w] [wa̰] [wo̰] [wà] [wá] [wè] [wé] [wì] [wò] [wó] [wɛʔ] [wɛ̀] [wɛ́] [wɪʔ] [wɪ̀ɴ] [wɪ́ɴ] [wɪ̰ɴ] [wḛ] [wḭ] [àɪɴ] [àɴ] [àʊɴ] [áɪɴ] [áɴ], and 24 more.

Tones: [creaky] high, slightly falling, creaky/tense phonation — written ⟨့⟩, or by the vowel sign ⟨ိ ု⟩, [low] low, slightly rising, modal phonation — written by the bare rhyme, or ⟨ာ ီ ူ ေ⟩, [high] high falling, breathy phonation — written ⟨း⟩, or by the vowel sign ⟨ဲ ော⟩, [checked] short, closed by [ʔ]; no tone contrast — written with a final stop letter + asat ⟨်⟩.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨က⟩ | [k] |  |
| ⟨က်⟩ | [ɛʔ] |  |
| ⟨ကျ⟩ | [tɕ] |  |
| ⟨ကြ⟩ | [tɕ] |  |
| ⟨ခ⟩ | [kʰ] |  |
| ⟨ခ်⟩ | [ɛʔ] |  |
| ⟨ချ⟩ | [tɕʰ] |  |
| ⟨ခြ⟩ | [tɕʰ] |  |
| ⟨ဂ⟩ | [ɡ] |  |
| ⟨ဂ်⟩ | [ɛʔ] |  |
| ⟨ဂျ⟩ | [dʑ] |  |
| ⟨ဂြ⟩ | [dʑ] |  |
| ⟨ဃ⟩ | [ɡ] |  |
| ⟨ဃျ⟩ | [dʑ] |  |
| ⟨ဃြ⟩ | [dʑ] |  |
| ⟨င⟩ | [ŋ] |  |
| ⟨င့်⟩ | [ɪ̰ɴ] |  |
| ⟨င်⟩ | [ɪ̀ɴ] |  |
| ⟨င်း⟩ | [ɪ́ɴ] |  |
| ⟨ငျ⟩ | [ɲ] |  |
| ⟨ငြ⟩ | [ɲ] |  |
| ⟨ငှ⟩ | [ŋ̊] |  |
| ⟨စ⟩ | [s] |  |
| ⟨စ်⟩ | [ɪʔ] |  |
| ⟨ဆ⟩ | [sʰ] |  |
| ⟨ဆ်⟩ | [ɪʔ] |  |
| ⟨ဇ⟩ | [z] |  |
| ⟨ဇ်⟩ | [ɪʔ] |  |
| ⟨ဈ⟩ | [z] |  |
| ⟨ဈ်⟩ | [ɪʔ] |  |
| ⟨ဉ⟩ | [ɲ] |  |
| ⟨ဉ့်⟩ | [ɪ̰ɴ] |  |
| ⟨ဉ်⟩ | [ɪ̀ɴ] |  |
| ⟨ဉ်း⟩ | [ɪ́ɴ] |  |
| ⟨ဉှ⟩ | [ɲ̊] |  |
| ⟨ည⟩ | [ɲ] |  |
| ⟨ည့်⟩ | [ḭ] [ḛ] |  |
| ⟨ည်⟩ | [ì] [è] [ɛ̀] |  |
| ⟨ည်း⟩ | [í] [ɛ́] [é] |  |
| ⟨ညှ⟩ | [ɲ̊] |  |
| ⟨ဋ⟩ | [t] |  |
| ⟨ဋ်⟩ | [aʔ] |  |
| ⟨ဌ⟩ | [tʰ] |  |
| ⟨ဌ်⟩ | [aʔ] |  |
| ⟨ဍ⟩ | [d] |  |
| ⟨ဍ်⟩ | [aʔ] |  |
| ⟨ဎ⟩ | [d] |  |
| ⟨ဎ်⟩ | [aʔ] |  |
| ⟨ဏ⟩ | [n] |  |
| ⟨ဏ့်⟩ | [a̰ɴ] |  |
| ⟨ဏ်⟩ | [àɴ] |  |
| ⟨ဏ်း⟩ | [áɴ] |  |
| ⟨ဏှ⟩ | [n̥] |  |
| ⟨တ⟩ | [t] |  |
| ⟨တ်⟩ | [aʔ] |  |
| ⟨ထ⟩ | [tʰ] |  |
| ⟨ထ်⟩ | [aʔ] |  |
| ⟨ဒ⟩ | [d] |  |
| ⟨ဒ်⟩ | [aʔ] |  |
| ⟨ဓ⟩ | [d] |  |
| ⟨ဓ်⟩ | [aʔ] |  |
| ⟨န⟩ | [n] |  |
| ⟨န့်⟩ | [a̰ɴ] |  |
| ⟨န်⟩ | [àɴ] |  |
| ⟨န်း⟩ | [áɴ] |  |
| ⟨နှ⟩ | [n̥] |  |
| ⟨ပ⟩ | [p] |  |
| ⟨ပ်⟩ | [aʔ] |  |
| ⟨ပျ⟩ | [pj] |  |
| ⟨ပျှ⟩ | [pʰj] |  |
| ⟨ပြ⟩ | [pj] |  |
| ⟨ဖ⟩ | [pʰ] |  |
| ⟨ဖ်⟩ | [aʔ] |  |
| ⟨ဖျ⟩ | [pʰj] |  |
| ⟨ဖြ⟩ | [pʰj] |  |
| ⟨ဗ⟩ | [b] |  |
| ⟨ဗ်⟩ | [aʔ] |  |
| ⟨ဗျ⟩ | [bj] |  |
| ⟨ဗျှ⟩ | [pʰj] |  |
| ⟨ဗြ⟩ | [bj] |  |
| ⟨ဘ⟩ | [b] |  |
| ⟨ဘ်⟩ | [aʔ] |  |
| ⟨ဘျ⟩ | [bj] |  |
| ⟨ဘျှ⟩ | [pʰj] |  |
| ⟨ဘြ⟩ | [bj] |  |
| ⟨မ⟩ | [m] |  |
| ⟨မ့်⟩ | [a̰ɴ] |  |
| ⟨မ်⟩ | [àɴ] |  |
| ⟨မ်း⟩ | [áɴ] |  |
| ⟨မျ⟩ | [mj] |  |
| ⟨မျှ⟩ | [m̥j] |  |
| ⟨မြ⟩ | [mj] |  |
| ⟨မှ⟩ | [m̥] |  |
| ⟨ယ⟩ | [j] |  |
| ⟨ယ်⟩ | [ɛ̀] |  |
| ⟨ယှ⟩ | [ʃ] |  |
| ⟨ရ⟩ | [j] |  |
| ⟨ရှ⟩ | [ʃ] |  |
| ⟨လ⟩ | [l] |  |
| ⟨လ်⟩ | [l] |  |
| ⟨လျ⟩ | [lj] |  |
| ⟨လျှ⟩ | [ʃ] |  |
| ⟨လြ⟩ | [lj] |  |
| ⟨လှ⟩ | [l̥] |  |
| ⟨ဝ⟩ | [w] |  |
| ⟨ဝှ⟩ | [ʍ] |  |
| ⟨သ⟩ | [θ] |  |
| ⟨သ်⟩ | [aʔ] |  |
| ⟨သျ⟩ | [θj] |  |
| ⟨သြ⟩ | [θj] |  |
| ⟨ဟ⟩ | [h] |  |
| ⟨ဟျ⟩ | [hj] |  |
| ⟨ဟြ⟩ | [hj] |  |
| ⟨ဟှ⟩ | [h] |  |
| ⟨ဠ⟩ | [l] |  |
| ⟨ဠျ⟩ | [lj] |  |
| ⟨ဠျှ⟩ | [ʃ] |  |
| ⟨ဠြ⟩ | [lj] |  |
| ⟨ဠှ⟩ | [l̥] |  |
| ⟨အ⟩ | [ʔ] |  |
| ⟨ဣ⟩ | [ʔḭ] |  |
| ⟨ဤ⟩ | [ʔì] |  |
| ⟨ဥ⟩ | [ʔṵ] |  |
| ⟨ဦ⟩ | [ʔù] |  |
| ⟨ဧ⟩ | [ʔè] |  |
| ⟨ဩ⟩ | [ʔɔ́] |  |
| ⟨ဪ⟩ | [ʔɔ̀] |  |
| ⟨ါ⟩ | [à] |  |
| ⟨ါ့⟩ | [a̰] |  |
| ⟨ါး⟩ | [á] |  |
| ⟨ာ⟩ | [à] |  |
| ⟨ာ့⟩ | [a̰] |  |
| ⟨ား⟩ | [á] |  |
| ⟨ိ⟩ | [ḭ] |  |
| ⟨ိက်⟩ | [eɪʔ] |  |
| ⟨ိတ်⟩ | [eɪʔ] |  |
| ⟨ိန့်⟩ | [ḛɪɴ] |  |
| ⟨ိန်⟩ | [èɪɴ] |  |
| ⟨ိန်း⟩ | [éɪɴ] |  |
| ⟨ိပ်⟩ | [eɪʔ] |  |
| ⟨ိမ့်⟩ | [ḛɪɴ] |  |
| ⟨ိမ်⟩ | [èɪɴ] |  |
| ⟨ိမ်း⟩ | [éɪɴ] |  |
| ⟨ို⟩ | [ò] |  |
| ⟨ိုက်⟩ | [aɪʔ] |  |
| ⟨ိုင့်⟩ | [a̰ɪɴ] |  |
| ⟨ိုင်⟩ | [àɪɴ] |  |
| ⟨ိုင်း⟩ | [áɪɴ] |  |
| ⟨ိုယ့်⟩ | [o̰] |  |
| ⟨ိုယ်⟩ | [ò] |  |
| ⟨ိုယ်း⟩ | [ó] |  |
| ⟨ိုလ့်⟩ | [o̰] |  |
| ⟨ိုလ်⟩ | [ò] |  |
| ⟨ိုလ်း⟩ | [ó] |  |
| ⟨ို့⟩ | [o̰] |  |
| ⟨ိုး⟩ | [ó] |  |
| ⟨ိံ⟩ | [èɪɴ] |  |
| ⟨ိံ့⟩ | [ḛɪɴ] |  |
| ⟨ိံး⟩ | [éɪɴ] |  |
| ⟨ီ⟩ | [ì] |  |
| ⟨ီး⟩ | [í] |  |
| ⟨ု⟩ | [ṵ] |  |
| ⟨ုတ်⟩ | [oʊʔ] |  |
| ⟨ုန့်⟩ | [o̰ʊɴ] |  |
| ⟨ုန်⟩ | [òʊɴ] |  |
| ⟨ုန်း⟩ | [óʊɴ] |  |
| ⟨ုပ်⟩ | [oʊʔ] |  |
| ⟨ုမ့်⟩ | [o̰ʊɴ] |  |
| ⟨ုမ်⟩ | [òʊɴ] |  |
| ⟨ုမ်း⟩ | [óʊɴ] |  |
| ⟨ုံ⟩ | [òʊɴ] |  |
| ⟨ုံ့⟩ | [o̰ʊɴ] |  |
| ⟨ုံး⟩ | [óʊɴ] |  |
| ⟨ူ⟩ | [ù] |  |
| ⟨ူး⟩ | [ú] |  |
| ⟨ေ⟩ | [è] |  |
| ⟨ေါ⟩ | [ɔ́] |  |
| ⟨ေါင့်⟩ | [a̰ʊɴ] |  |
| ⟨ေါင်⟩ | [àʊɴ] |  |
| ⟨ေါင်း⟩ | [áʊɴ] |  |
| ⟨ေါ့⟩ | [ɔ̰] |  |
| ⟨ေါ့်⟩ | [ɔ̰] |  |
| ⟨ေါ်⟩ | [ɔ̀] |  |
| ⟨ေါ်း⟩ | [ɔ̀] |  |
| ⟨ော⟩ | [ɔ́] |  |
| ⟨ောက်⟩ | [aʊʔ] |  |
| ⟨ောင့်⟩ | [a̰ʊɴ] |  |
| ⟨ောင်⟩ | [àʊɴ] |  |
| ⟨ောင်း⟩ | [áʊɴ] |  |
| ⟨ော့⟩ | [ɔ̰] |  |
| ⟨ော့်⟩ | [ɔ̰] |  |
| ⟨ော်⟩ | [ɔ̀] |  |
| ⟨ော်း⟩ | [ɔ̀] |  |
| ⟨ေ့⟩ | [ḛ] |  |
| ⟨ေး⟩ | [é] |  |
| ⟨ဲ⟩ | [ɛ́] |  |
| ⟨ဲ့⟩ | [ɛ̰] |  |
| ⟨ံ⟩ | [àɴ] |  |
| ⟨ံ့⟩ | [a̰ɴ] |  |
| ⟨ံး⟩ | [áɴ] |  |
| ⟨ွ⟩ | [wa̰] |  |
| ⟨ွက်⟩ | [wɛʔ] |  |
| ⟨ွင့်⟩ | [wɪ̰ɴ] |  |
| ⟨ွင်⟩ | [wɪ̀ɴ] |  |
| ⟨ွင်း⟩ | [wɪ́ɴ] |  |
| ⟨ွစ်⟩ | [wɪʔ] |  |
| ⟨ွတ်⟩ | [ʊʔ] |  |
| ⟨ွန့်⟩ | [ʊ̰ɴ] |  |
| ⟨ွန်⟩ | [ʊ̀ɴ] |  |
| ⟨ွန်း⟩ | [ʊ́ɴ] |  |
| ⟨ွပ်⟩ | [ʊʔ] |  |
| ⟨ွမ့်⟩ | [ʊ̰ɴ] |  |
| ⟨ွမ်⟩ | [ʊ̀ɴ] |  |
| ⟨ွမ်း⟩ | [ʊ́ɴ] |  |
| ⟨ွယ်⟩ | [wɛ̀] |  |
| ⟨ွါ⟩ | [wà] |  |
| ⟨ွါး⟩ | [wá] |  |
| ⟨ွာ⟩ | [wà] |  |
| ⟨ွား⟩ | [wá] |  |
| ⟨ွိ⟩ | [wḭ] |  |
| ⟨ွို⟩ | [wò] |  |
| ⟨ွို့⟩ | [wo̰] |  |
| ⟨ွိုး⟩ | [wó] |  |
| ⟨ွီ⟩ | [wì] |  |
| ⟨ွေ⟩ | [wè] |  |
| ⟨ွေ့⟩ | [wḛ] |  |
| ⟨ွေး⟩ | [wé] |  |
| ⟨ွဲ⟩ | [wɛ́] |  |
| ⟨ဿ⟩ | [θ] |  |
| ⟨ဿျ⟩ | [θj] |  |
| ⟨ဿြ⟩ | [θj] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 6 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `MY_SANDHI_VOICE_K` | /k kʰ/ → [ɡ], not word-initially, in the onset, after a vowel | - | [Watkins 2001](#src-watkins2001), [Wheatley 1990](#src-wheatley1990) |
| `MY_SANDHI_VOICE_TC` | /tɕ tɕʰ/ → [dʑ], not word-initially, in the onset, after a vowel | - | [Watkins 2001](#src-watkins2001), [Wheatley 1990](#src-wheatley1990) |
| `MY_SANDHI_VOICE_S` | /s sʰ/ → [z], not word-initially, in the onset, after a vowel | - | [Watkins 2001](#src-watkins2001), [Wheatley 1990](#src-wheatley1990) |
| `MY_SANDHI_VOICE_T` | /t tʰ/ → [d], not word-initially, in the onset, after a vowel | - | [Watkins 2001](#src-watkins2001), [Wheatley 1990](#src-wheatley1990) |
| `MY_SANDHI_VOICE_P` | /p pʰ/ → [b], not word-initially, in the onset, after a vowel | ⟨ပွန်း⟩ [kɪ̀ɴbʊ́ɴ] | [Watkins 2001](#src-watkins2001), [Wheatley 1990](#src-wheatley1990) |
| `MY_SANDHI_VOICE_TH` | /θ/ → [ð], not word-initially, in the onset, after a vowel | - | [Watkins 2001](#src-watkins2001), [Wheatley 1990](#src-wheatley1990) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "my")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Buriat](bua.md) · [Home](../index.md) · [Buryat →](bxr.md)
