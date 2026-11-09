# Mandarin Chinese (`zh`)

<!-- atlas:summary begin -->
Mandarin Chinese is a Sinitic language, written in the Latin script. Glottolog places it in 8 countries. The `zh` spec is at the research tier. It cites 7 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `zh` |
| Aliases | `zho` |
| ISO 639-3 | [zho](https://iso639-3.sil.org/code/zho), Chinese |
| Glottolog | [mand1415](https://glottolog.org/resource/languoid/id/mand1415), Mandarin Chinese |
| Wikidata | [Q7850](https://www.wikidata.org/wiki/Q7850) |
| Wikipedia | [Chinese language](https://en.wikipedia.org/wiki/Chinese_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) > [Sinitic](by-family.md#sino-tibetan--sinitic) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [Laos](by-region.md#laos), [Mongolia](by-region.md#mongolia), [Myanmar (Burma)](by-region.md#myanmar-burma), [North Korea](by-region.md#north-korea), [Russia](by-region.md#russia), [Taiwan](by-region.md#taiwan), [Vietnam](by-region.md#vietnam) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [Middle Chinese](https://tigregotico.github.io/orthography2ipa/#ltc) `ltc` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`zh` in the data explorer](https://tigregotico.github.io/orthography2ipa/#zh) |
| Spec file | [`zh.json`](../../orthography2ipa/data/zh.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Mandarin (Pǔtōnghuà), Beijing-based. THIS SPEC READS PINYIN, NOT HANZI, its graphemes are Pinyin units and the input contract is Pinyin. Nothing here reads a Han character, and nothing could: a Han character does not encode sound, so no rule engine can pronounce one. That limit is stated by `zh-Hani`.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 7 works, from 1958 to 2023. [Sources](#sources) lists them. The spec file writes all 360 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/zh.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `zh` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Chinese (Han script)](https://tigregotico.github.io/orthography2ipa/#zh-Hani) `zh-Hani`: stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 7 works. 3 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-duanmu2007"></a>Duanmu, S. (2007). *The Phonology of Standard Chinese (2nd ed.)*. Oxford University Press.
2. <a id="src-chao1968"></a>Chao, Y.R. (1968). *A Grammar of Spoken Chinese*. University of California Press.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
4. <a id="src-lin2007"></a>Lin, Y.-H. (2007). *The Sounds of Chinese*. Cambridge University Press.
5. <a id="src-pinyin_scheme1958"></a>中国文字改革委员会 (Committee for Reform of the Chinese Written Language) (1958). *汉语拼音方案 [Scheme for the Chinese Phonetic Alphabet]*. First National People's Congress, text published by the Ministry of Education of the PRC. [moe.gov.cn](http://www.moe.gov.cn/jyb_sjzl/ziliao/A19/195802/t19580201_186000.html)
6. <a id="src-lee2023"></a>이미경 (Lee, Mi-kyoung) (2023). *중국어 감탄사의 유형과 특징 고찰, 《现代汉语词典》중심으로 [Types and characteristics of Chinese interjections, based on the Xiandai Hanyu Cidian]*. 中國語文學 (Journal of Chinese Language and Literature) 94. Cited: 287-315. [journal.kci.go.kr](https://journal.kci.go.kr/clsyn/archive/articlePdf?artiId=ART003036565)
7. <a id="src-duanmu2005"></a>Duanmu, S. (2005). *Chinese (Mandarin), Phonology of*. Author's preprint (February 2005) for the Encyclopedia of Language and Linguistics, 2nd ed. (Elsevier). Cited: 1-2. [public.websites.umich.edu](https://public.websites.umich.edu/~duanmu/ELL05.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `zh` | generated | machine-generated | CC BY 4.0 | 4718 | 0.2879 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 329 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | t tʰ |  |  | k kʰ |
| Affricate |  |  | ts tsʰ | ʈʂ ʈʂʰ | tɕ tɕʰ |  |
| Nasal | m |  | n |  |  | ŋ |
| Fricative |  | f | s | ʂ ʐ | ɕ | x |
| Approximant |  |  | ɹ̩ | ɻ ɻ̩ | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y | ɨ | u |
| Close-mid |  |  | o ɤ |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a |  | ɑ |

Sequences that the spec writes as one unit: [ai] [ai˥] [ai˥˩] [ai˧˥] [ai˨˩˦] [an] [an˥] [an˥˩] [an˧˥] [an˨˩˦] [au] [au˥] [au˥˩] [au˧˥] [au˨˩˦] [a˥] [a˥˩] [a˧˥] [a˨˩˦] [ei] [ei˥] [ei˥˩] [ei˧˥] [ei˨˩˦] [fou] [fou˥] [fou˥˩] [fou˧˥] [fou˨˩˦] [fwo] [fwo˥] [fwo˥˩] [fwo˧˥] [fwo˨˩˦] [in] [in˥] [in˥˩] [in˧˥] [in˨˩˦] [iŋ], and 252 more.

Tones: [˥] high level (1st), [˧˥] rising (2nd), [˨˩˦] dipping (3rd), [˥˩] falling (4th), [] neutral (5th).
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨0⟩ | ∅ |  |
| ⟨1⟩ | [˥] |  |
| ⟨2⟩ | [˧˥] |  |
| ⟨3⟩ | [˨˩˦] |  |
| ⟨4⟩ | [˥˩] |  |
| ⟨5⟩ | ∅ |  |
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai] |  |
| ⟨an⟩ | [an] |  |
| ⟨ang⟩ | [ɑŋ] |  |
| ⟨ao⟩ | [au] |  |
| ⟨b⟩ | [p] |  |
| ⟨bo⟩ | [pwo] |  |
| ⟨bò⟩ | [pwo˥˩] |  |
| ⟨bó⟩ | [pwo˧˥] |  |
| ⟨bō⟩ | [pwo˥] |  |
| ⟨bǒ⟩ | [pwo˨˩˦] |  |
| ⟨c⟩ | [tsʰ] |  |
| ⟨ch⟩ | [ʈʂʰ] |  |
| ⟨chi⟩ | [ʈʂʰɨ] [ʈʂʰɻ̩] |  |
| ⟨chì⟩ | [ʈʂʰɨ˥˩] [ʈʂʰɻ̩˥˩] |  |
| ⟨chí⟩ | [ʈʂʰɨ˧˥] [ʈʂʰɻ̩˧˥] |  |
| ⟨chī⟩ | [ʈʂʰɨ˥] [ʈʂʰɻ̩˥] |  |
| ⟨chǐ⟩ | [ʈʂʰɨ˨˩˦] [ʈʂʰɻ̩˨˩˦] |  |
| ⟨ci⟩ | [tsʰɨ] [tsʰɹ̩] |  |
| ⟨cì⟩ | [tsʰɨ˥˩] [tsʰɹ̩˥˩] |  |
| ⟨cí⟩ | [tsʰɨ˧˥] [tsʰɹ̩˧˥] |  |
| ⟨cī⟩ | [tsʰɨ˥] [tsʰɹ̩˥] |  |
| ⟨cǐ⟩ | [tsʰɨ˨˩˦] [tsʰɹ̩˨˩˦] |  |
| ⟨d⟩ | [t] |  |
| ⟨e⟩ | [ɤ] |  |
| ⟨ei⟩ | [ei] |  |
| ⟨en⟩ | [ən] |  |
| ⟨eng⟩ | [əŋ] |  |
| ⟨er⟩ | [ɚ] |  |
| ⟨f⟩ | [f] |  |
| ⟨fo⟩ | [fwo] |  |
| ⟨fou⟩ | [fou] |  |
| ⟨fò⟩ | [fwo˥˩] |  |
| ⟨fòu⟩ | [fou˥˩] |  |
| ⟨fó⟩ | [fwo˧˥] |  |
| ⟨fóu⟩ | [fou˧˥] |  |
| ⟨fō⟩ | [fwo˥] |  |
| ⟨fōu⟩ | [fou˥] |  |
| ⟨fǒ⟩ | [fwo˨˩˦] |  |
| ⟨fǒu⟩ | [fou˨˩˦] |  |
| ⟨g⟩ | [k] |  |
| ⟨h⟩ | [x] |  |
| ⟨hm⟩ | [xm] |  |
| ⟨hng⟩ | [xŋ] |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ian⟩ | [jɛn] |  |
| ⟨iang⟩ | [jɑŋ] |  |
| ⟨iao⟩ | [jau] |  |
| ⟨ie⟩ | [je] |  |
| ⟨in⟩ | [in] |  |
| ⟨ing⟩ | [iŋ] |  |
| ⟨iong⟩ | [jʊŋ] |  |
| ⟨iu⟩ | [jou] |  |
| ⟨ià⟩ | [ja˥˩] |  |
| ⟨iàn⟩ | [jɛn˥˩] |  |
| ⟨iàng⟩ | [jɑŋ˥˩] |  |
| ⟨iào⟩ | [jau˥˩] |  |
| ⟨iá⟩ | [ja˧˥] |  |
| ⟨ián⟩ | [jɛn˧˥] |  |
| ⟨iáng⟩ | [jɑŋ˧˥] |  |
| ⟨iáo⟩ | [jau˧˥] |  |
| ⟨iè⟩ | [je˥˩] |  |
| ⟨ié⟩ | [je˧˥] |  |
| ⟨iòng⟩ | [jʊŋ˥˩] |  |
| ⟨ióng⟩ | [jʊŋ˧˥] |  |
| ⟨iù⟩ | [jou˥˩] |  |
| ⟨iú⟩ | [jou˧˥] |  |
| ⟨iā⟩ | [ja˥] |  |
| ⟨iān⟩ | [jɛn˥] |  |
| ⟨iāng⟩ | [jɑŋ˥] |  |
| ⟨iāo⟩ | [jau˥] |  |
| ⟨iē⟩ | [je˥] |  |
| ⟨iě⟩ | [je˨˩˦] |  |
| ⟨iōng⟩ | [jʊŋ˥] |  |
| ⟨iū⟩ | [jou˥] |  |
| ⟨iǎ⟩ | [ja˨˩˦] |  |
| ⟨iǎn⟩ | [jɛn˨˩˦] |  |
| ⟨iǎng⟩ | [jɑŋ˨˩˦] |  |
| ⟨iǎo⟩ | [jau˨˩˦] |  |
| ⟨iǒng⟩ | [jʊŋ˨˩˦] |  |
| ⟨iǔ⟩ | [jou˨˩˦] |  |
| ⟨j⟩ | [tɕ] |  |
| ⟨k⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mo⟩ | [mwo] |  |
| ⟨mou⟩ | [mou] |  |
| ⟨mò⟩ | [mwo˥˩] |  |
| ⟨mòu⟩ | [mou˥˩] |  |
| ⟨mó⟩ | [mwo˧˥] |  |
| ⟨móu⟩ | [mou˧˥] |  |
| ⟨mō⟩ | [mwo˥] |  |
| ⟨mōu⟩ | [mou˥] |  |
| ⟨mǒ⟩ | [mwo˨˩˦] |  |
| ⟨mǒu⟩ | [mou˨˩˦] |  |
| ⟨m̀⟩ | [m˥˩] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [ɔ] [o] |  |
| ⟨ong⟩ | [ʊŋ] |  |
| ⟨ou⟩ | [ou] |  |
| ⟨p⟩ | [pʰ] |  |
| ⟨po⟩ | [pʰwo] |  |
| ⟨pou⟩ | [pʰou] |  |
| ⟨pò⟩ | [pʰwo˥˩] |  |
| ⟨pòu⟩ | [pʰou˥˩] |  |
| ⟨pó⟩ | [pʰwo˧˥] |  |
| ⟨póu⟩ | [pʰou˧˥] |  |
| ⟨pō⟩ | [pʰwo˥] |  |
| ⟨pōu⟩ | [pʰou˥] |  |
| ⟨pǒ⟩ | [pʰwo˨˩˦] |  |
| ⟨pǒu⟩ | [pʰou˨˩˦] |  |
| ⟨q⟩ | [tɕʰ] |  |
| ⟨r⟩ | [ɻ] |  |
| ⟨ri⟩ | [ɻɨ] [ɻɻ̩] |  |
| ⟨rì⟩ | [ɻɨ˥˩] [ɻɻ̩˥˩] |  |
| ⟨rí⟩ | [ɻɨ˧˥] [ɻɻ̩˧˥] |  |
| ⟨rī⟩ | [ɻɨ˥] [ɻɻ̩˥] |  |
| ⟨rǐ⟩ | [ɻɨ˨˩˦] [ɻɻ̩˨˩˦] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʂ] |  |
| ⟨shi⟩ | [ʂɨ] [ʂɻ̩] |  |
| ⟨shì⟩ | [ʂɨ˥˩] [ʂɻ̩˥˩] |  |
| ⟨shí⟩ | [ʂɨ˧˥] [ʂɻ̩˧˥] |  |
| ⟨shī⟩ | [ʂɨ˥] [ʂɻ̩˥] |  |
| ⟨shǐ⟩ | [ʂɨ˨˩˦] [ʂɻ̩˨˩˦] |  |
| ⟨si⟩ | [sɨ] [sɹ̩] |  |
| ⟨sì⟩ | [sɨ˥˩] [sɹ̩˥˩] |  |
| ⟨sí⟩ | [sɨ˧˥] [sɹ̩˧˥] |  |
| ⟨sī⟩ | [sɨ˥] [sɹ̩˥] |  |
| ⟨sǐ⟩ | [sɨ˨˩˦] [sɹ̩˨˩˦] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨u⟩ | [u] | after palatal [y] |
| ⟨ua⟩ | [wa] |  |
| ⟨uai⟩ | [wai] |  |
| ⟨uan⟩ | [wan] | after palatal [ɥɛn] |
| ⟨uang⟩ | [wɑŋ] |  |
| ⟨ue⟩ | [ɥe] |  |
| ⟨ueng⟩ | [wəŋ] |  |
| ⟨ui⟩ | [wei] |  |
| ⟨un⟩ | [wən] | after palatal [yn] |
| ⟨uo⟩ | [wo] |  |
| ⟨uà⟩ | [wa˥˩] |  |
| ⟨uài⟩ | [wai˥˩] |  |
| ⟨uàn⟩ | [wan˥˩] | after palatal [ɥɛn˥˩] |
| ⟨uàng⟩ | [wɑŋ˥˩] |  |
| ⟨uá⟩ | [wa˧˥] |  |
| ⟨uái⟩ | [wai˧˥] |  |
| ⟨uán⟩ | [wan˧˥] | after palatal [ɥɛn˧˥] |
| ⟨uáng⟩ | [wɑŋ˧˥] |  |
| ⟨uè⟩ | [ɥe˥˩] |  |
| ⟨uèng⟩ | [wəŋ˥˩] |  |
| ⟨ué⟩ | [ɥe˧˥] |  |
| ⟨uéng⟩ | [wəŋ˧˥] |  |
| ⟨uì⟩ | [wei˥˩] |  |
| ⟨uí⟩ | [wei˧˥] |  |
| ⟨uò⟩ | [wo˥˩] |  |
| ⟨uó⟩ | [wo˧˥] |  |
| ⟨uā⟩ | [wa˥] |  |
| ⟨uāi⟩ | [wai˥] |  |
| ⟨uān⟩ | [wan˥] | after palatal [ɥɛn˥] |
| ⟨uāng⟩ | [wɑŋ˥] |  |
| ⟨uē⟩ | [ɥe˥] |  |
| ⟨uēng⟩ | [wəŋ˥] |  |
| ⟨uě⟩ | [ɥe˨˩˦] |  |
| ⟨uěng⟩ | [wəŋ˨˩˦] |  |
| ⟨uī⟩ | [wei˥] |  |
| ⟨uō⟩ | [wo˥] |  |
| ⟨uǎ⟩ | [wa˨˩˦] |  |
| ⟨uǎi⟩ | [wai˨˩˦] |  |
| ⟨uǎn⟩ | [wan˨˩˦] | after palatal [ɥɛn˨˩˦] |
| ⟨uǎng⟩ | [wɑŋ˨˩˦] |  |
| ⟨uǐ⟩ | [wei˨˩˦] |  |
| ⟨uǒ⟩ | [wo˨˩˦] |  |
| ⟨v⟩ | [y] |  |
| ⟨ve⟩ | [ɥe] |  |
| ⟨vn⟩ | [yn] |  |
| ⟨w⟩ | [w] |  |
| ⟨wo⟩ | [wo] |  |
| ⟨wu⟩ | [u] |  |
| ⟨wò⟩ | [wo˥˩] |  |
| ⟨wó⟩ | [wo˧˥] |  |
| ⟨wù⟩ | [u˥˩] |  |
| ⟨wú⟩ | [u˧˥] |  |
| ⟨wō⟩ | [wo˥] |  |
| ⟨wū⟩ | [u˥] |  |
| ⟨wǒ⟩ | [wo˨˩˦] |  |
| ⟨wǔ⟩ | [u˨˩˦] |  |
| ⟨x⟩ | [ɕ] |  |
| ⟨y⟩ | [j] |  |
| ⟨yan⟩ | [jɛn] |  |
| ⟨yang⟩ | [jɑŋ] |  |
| ⟨ye⟩ | [je] |  |
| ⟨yi⟩ | [i] |  |
| ⟨yin⟩ | [in] |  |
| ⟨ying⟩ | [iŋ] |  |
| ⟨yu⟩ | [y] |  |
| ⟨yuan⟩ | [ɥɛn] |  |
| ⟨yue⟩ | [ɥe] |  |
| ⟨yun⟩ | [yn] |  |
| ⟨yuàn⟩ | [ɥɛn˥˩] |  |
| ⟨yuán⟩ | [ɥɛn˧˥] |  |
| ⟨yuè⟩ | [ɥe˥˩] |  |
| ⟨yué⟩ | [ɥe˧˥] |  |
| ⟨yuān⟩ | [ɥɛn˥] |  |
| ⟨yuē⟩ | [ɥe˥] |  |
| ⟨yuě⟩ | [ɥe˨˩˦] |  |
| ⟨yuǎn⟩ | [ɥɛn˨˩˦] |  |
| ⟨yàn⟩ | [jɛn˥˩] |  |
| ⟨yàng⟩ | [jɑŋ˥˩] |  |
| ⟨yán⟩ | [jɛn˧˥] |  |
| ⟨yáng⟩ | [jɑŋ˧˥] |  |
| ⟨yè⟩ | [je˥˩] |  |
| ⟨yé⟩ | [je˧˥] |  |
| ⟨yì⟩ | [i˥˩] |  |
| ⟨yìn⟩ | [in˥˩] |  |
| ⟨yìng⟩ | [iŋ˥˩] |  |
| ⟨yí⟩ | [i˧˥] |  |
| ⟨yín⟩ | [in˧˥] |  |
| ⟨yíng⟩ | [iŋ˧˥] |  |
| ⟨yù⟩ | [y˥˩] |  |
| ⟨yùn⟩ | [yn˥˩] |  |
| ⟨yú⟩ | [y˧˥] |  |
| ⟨yún⟩ | [yn˧˥] |  |
| ⟨yān⟩ | [jɛn˥] |  |
| ⟨yāng⟩ | [jɑŋ˥] |  |
| ⟨yē⟩ | [je˥] |  |
| ⟨yě⟩ | [je˨˩˦] |  |
| ⟨yī⟩ | [i˥] |  |
| ⟨yīn⟩ | [in˥] |  |
| ⟨yīng⟩ | [iŋ˥] |  |
| ⟨yū⟩ | [y˥] |  |
| ⟨yūn⟩ | [yn˥] |  |
| ⟨yǎn⟩ | [jɛn˨˩˦] |  |
| ⟨yǎng⟩ | [jɑŋ˨˩˦] |  |
| ⟨yǐ⟩ | [i˨˩˦] |  |
| ⟨yǐn⟩ | [in˨˩˦] |  |
| ⟨yǐng⟩ | [iŋ˨˩˦] |  |
| ⟨yǔ⟩ | [y˨˩˦] |  |
| ⟨yǔn⟩ | [yn˨˩˦] |  |
| ⟨z⟩ | [ts] |  |
| ⟨zh⟩ | [ʈʂ] |  |
| ⟨zhi⟩ | [ʈʂɨ] [ʈʂɻ̩] |  |
| ⟨zhì⟩ | [ʈʂɨ˥˩] [ʈʂɻ̩˥˩] |  |
| ⟨zhí⟩ | [ʈʂɨ˧˥] [ʈʂɻ̩˧˥] |  |
| ⟨zhī⟩ | [ʈʂɨ˥] [ʈʂɻ̩˥] |  |
| ⟨zhǐ⟩ | [ʈʂɨ˨˩˦] [ʈʂɻ̩˨˩˦] |  |
| ⟨zi⟩ | [tsɨ] [tsɹ̩] |  |
| ⟨zì⟩ | [tsɨ˥˩] [tsɹ̩˥˩] |  |
| ⟨zí⟩ | [tsɨ˧˥] [tsɹ̩˧˥] |  |
| ⟨zī⟩ | [tsɨ˥] [tsɹ̩˥] |  |
| ⟨zǐ⟩ | [tsɨ˨˩˦] [tsɹ̩˨˩˦] |  |
| ⟨à⟩ | [a˥˩] |  |
| ⟨ài⟩ | [ai˥˩] |  |
| ⟨àn⟩ | [an˥˩] |  |
| ⟨àng⟩ | [ɑŋ˥˩] |  |
| ⟨ào⟩ | [au˥˩] |  |
| ⟨á⟩ | [a˧˥] |  |
| ⟨ái⟩ | [ai˧˥] |  |
| ⟨án⟩ | [an˧˥] |  |
| ⟨áng⟩ | [ɑŋ˧˥] |  |
| ⟨áo⟩ | [au˧˥] |  |
| ⟨è⟩ | [ɤ˥˩] |  |
| ⟨èi⟩ | [ei˥˩] |  |
| ⟨èn⟩ | [ən˥˩] |  |
| ⟨èng⟩ | [əŋ˥˩] |  |
| ⟨èr⟩ | [ɚ˥˩] |  |
| ⟨é⟩ | [ɤ˧˥] |  |
| ⟨éi⟩ | [ei˧˥] |  |
| ⟨én⟩ | [ən˧˥] |  |
| ⟨éng⟩ | [əŋ˧˥] |  |
| ⟨ér⟩ | [ɚ˧˥] |  |
| ⟨ê⟩ | [ɛ] |  |
| ⟨ê̄⟩ | [ɛ˥] |  |
| ⟨ê̌⟩ | [ɛ˨˩˦] |  |
| ⟨ì⟩ | [i˥˩] |  |
| ⟨ìn⟩ | [in˥˩] |  |
| ⟨ìng⟩ | [iŋ˥˩] |  |
| ⟨í⟩ | [i˧˥] |  |
| ⟨ín⟩ | [in˧˥] |  |
| ⟨íng⟩ | [iŋ˧˥] |  |
| ⟨ò⟩ | [wo˥˩] |  |
| ⟨òng⟩ | [ʊŋ˥˩] |  |
| ⟨òu⟩ | [ou˥˩] |  |
| ⟨ó⟩ | [wo˧˥] |  |
| ⟨óng⟩ | [ʊŋ˧˥] |  |
| ⟨óu⟩ | [ou˧˥] |  |
| ⟨ù⟩ | [u˥˩] | after palatal [y˥˩] |
| ⟨ùn⟩ | [wən˥˩] | after palatal [yn˥˩] |
| ⟨ú⟩ | [u˧˥] | after palatal [y˧˥] |
| ⟨ún⟩ | [wən˧˥] | after palatal [yn˧˥] |
| ⟨ü⟩ | [y] |  |
| ⟨üan⟩ | [ɥɛn] |  |
| ⟨üe⟩ | [ɥe] |  |
| ⟨ün⟩ | [yn] |  |
| ⟨üàn⟩ | [ɥɛn˥˩] |  |
| ⟨üán⟩ | [ɥɛn˧˥] |  |
| ⟨üè⟩ | [ɥe˥˩] |  |
| ⟨üé⟩ | [ɥe˧˥] |  |
| ⟨üān⟩ | [ɥɛn˥] |  |
| ⟨üē⟩ | [ɥe˥] |  |
| ⟨üě⟩ | [ɥe˨˩˦] |  |
| ⟨üǎn⟩ | [ɥɛn˨˩˦] |  |
| ⟨ā⟩ | [a˥] |  |
| ⟨āi⟩ | [ai˥] |  |
| ⟨ān⟩ | [an˥] |  |
| ⟨āng⟩ | [ɑŋ˥] |  |
| ⟨āo⟩ | [au˥] |  |
| ⟨ē⟩ | [ɤ˥] |  |
| ⟨ēi⟩ | [ei˥] |  |
| ⟨ēn⟩ | [ən˥] |  |
| ⟨ēng⟩ | [əŋ˥] |  |
| ⟨ēr⟩ | [ɚ˥] |  |
| ⟨ě⟩ | [ɤ˨˩˦] |  |
| ⟨ěi⟩ | [ei˨˩˦] |  |
| ⟨ěn⟩ | [ən˨˩˦] |  |
| ⟨ěng⟩ | [əŋ˨˩˦] |  |
| ⟨ěr⟩ | [ɚ˨˩˦] |  |
| ⟨ī⟩ | [i˥] |  |
| ⟨īn⟩ | [in˥] |  |
| ⟨īng⟩ | [iŋ˥] |  |
| ⟨ńg⟩ | [ŋ˧˥] |  |
| ⟨ňg⟩ | [ŋ˨˩˦] |  |
| ⟨ō⟩ | [wo˥] |  |
| ⟨ōng⟩ | [ʊŋ˥] |  |
| ⟨ōu⟩ | [ou˥] |  |
| ⟨ū⟩ | [u˥] | after palatal [y˥] |
| ⟨ūn⟩ | [wən˥] | after palatal [yn˥] |
| ⟨ǎ⟩ | [a˨˩˦] |  |
| ⟨ǎi⟩ | [ai˨˩˦] |  |
| ⟨ǎn⟩ | [an˨˩˦] |  |
| ⟨ǎng⟩ | [ɑŋ˨˩˦] |  |
| ⟨ǎo⟩ | [au˨˩˦] |  |
| ⟨ǐ⟩ | [i˨˩˦] |  |
| ⟨ǐn⟩ | [in˨˩˦] |  |
| ⟨ǐng⟩ | [iŋ˨˩˦] |  |
| ⟨ǒ⟩ | [wo˨˩˦] |  |
| ⟨ǒng⟩ | [ʊŋ˨˩˦] |  |
| ⟨ǒu⟩ | [ou˨˩˦] |  |
| ⟨ǔ⟩ | [u˨˩˦] | after palatal [y˨˩˦] |
| ⟨ǔn⟩ | [wən˨˩˦] | after palatal [yn˨˩˦] |
| ⟨ǖ⟩ | [y˥] |  |
| ⟨ǖn⟩ | [yn˥] |  |
| ⟨ǘ⟩ | [y˧˥] |  |
| ⟨ǘn⟩ | [yn˧˥] |  |
| ⟨ǚ⟩ | [y˨˩˦] |  |
| ⟨ǚn⟩ | [yn˨˩˦] |  |
| ⟨ǜ⟩ | [y˥˩] |  |
| ⟨ǜn⟩ | [yn˥˩] |  |
| ⟨ǹg⟩ | [ŋ˥˩] |  |
| ⟨ḿ⟩ | [m˧˥] |  |
| ⟨ế⟩ | [ɛ˧˥] |  |
| ⟨ề⟩ | [ɛ˥˩] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "zh")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Manchu](mnc.md) · [Home](../index.md) · [Mandinka →](mnk.md)
