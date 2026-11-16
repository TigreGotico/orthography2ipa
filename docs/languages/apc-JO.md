# Jordanian Arabic (Ammani) (`apc-JO`)

<!-- atlas:summary begin -->
Jordanian Arabic (Ammani) is a Central Semitic language, written in the Arabic script. Its code names Jordan. The `apc-JO` spec is at the research tier. It cites 5 sources and has 4 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `apc-JO` |
| Aliases | `ajp`, `ar-JO` |
| ISO 639-3 | [apc](https://iso639-3.sil.org/code/apc), Levantine Arabic |
| Glottolog | [sout3123](https://glottolog.org/resource/languoid/id/sout3123), South Levantine Arabic |
| Wikidata | [Q3444016](https://www.wikidata.org/wiki/Q3444016) |
| Wikipedia | [Levantine Arabic](https://en.wikipedia.org/wiki/Levantine_Arabic) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Eurasia](by-region.md#eurasia) > [Jordan](by-region.md#jordan) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Proto-Levantine Arabic](apc.md) `apc` |
| Explorer | [`apc-JO` in the data explorer](https://tigregotico.github.io/orthography2ipa/#apc-JO) |
| Spec file | [`apc-JO.json`](../../orthography2ipa/data/apc-JO.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Jordanian Arabic, Ammani koine, a new dialect formed from Jordanian + urban Palestinian contact (Al-Wer 2020).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1964 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes 8 of the 260 spellings of its letter table and takes the other 252 from [Proto-Levantine Arabic](apc.md) `apc`.

The [spec file](../../orthography2ipa/data/apc-JO.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `apc-JO` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 5 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-alwer2020"></a>Al-Wer, E. (2020). *New-dialect formation: The Amman dialect*. In: Lucas & Manfredi (eds.), Arabic and contact-induced change, 551-566. Berlin: Language Science Press. Cited: 551-566. [langsci-press.org](https://langsci-press.org/catalog/book/235)
2. <a id="src-fadda2016"></a>Fadda, H. (2016). *Language Variation in Western Amman*. MA thesis, Canada Institute of Linguistics (CanIL). Cited: 27-30. [web.archive.org](https://web.archive.org/web/20250210163657/https://www.canil.ca/wordpress/wp-content/uploads/2019/11/Fadda-Language-Variation-in-Western-Amman.pdf)
3. <a id="src-almbark2015"></a>Almbark, R. & Hellmuth, S. (2015). *Acoustic analysis of the Syrian Arabic vowel system*. Proceedings of ICPhS 2015 (paper 0612), Glasgow. Cited: 1-4. [internationalphoneticassociation.org](https://www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2015/Papers/ICPHS0612.pdf)
4. <a id="src-cowell1964"></a>Cowell, M.W. (1964). *A Reference Grammar of Syrian Arabic (Based on the Dialect of Damascus)*. Georgetown University Press. [archive.org](https://archive.org/details/referencegrammar0000cowe)
5. <a id="src-levantine_arabic_wiki"></a>Wikipedia contributors (2026). *Levantine Arabic*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Levantine_Arabic)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `primary_sources` | `apc-JO` | gold | expert-human | Apache-2.0 (this repository). Each row quotes and cites a published example. | 13 | 0.2179 | no |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `apc-JO` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2513 | 0.3451 | yes |
| `arabic_tts` | `apc-JO` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0968 | no |
| `gold20_arabic` ([TigreGotico/arabic-dialects-gold20](https://huggingface.co/datasets/TigreGotico/arabic-dialects-gold20)) | `apc-JO` | silver | llm-corrected | CC BY 4.0 | 20 | 0.0995 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 249 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d dˤ t tˤ |  |  | k ɡ | q |  | ʔ |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |  |  |
| Trill |  |  |  | r |  |  |  |  |  |  |
| Fricative |  | f v | ð ðˤ θ | s sˤ z zˤ | ʃ ʒ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l ɫ |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Near-close | ɪ ɪː | ʊ ʊː |
| Close-mid | e eː | oː |
| Near-open | æ |  |
| Open | a aː | ɑ ɑː |

Sequences that the spec writes as one unit: [add] [adˤdˤ] [aj] [aja] [ajaː] [aji] [ajij] [ajiː] [ajj] [aju] [al] [all] [allaːh] [an] [ann] [arr] [ass] [asˤsˤ] [at] [att] [atˤtˤ] [aw] [awa] [awaː] [awi] [awij] [awiː] [awu] [aww] [azz] [azˤzˤ] [aðð] [aðˤðˤ] [aʃʃ] [aːj] [aθθ] [bi] [bidd] [bidˤdˤ] [bil], and 158 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ء⟩ | [ʔ] |  |
| ⟨آ⟩ | [ʔaː] |  |
| ⟨أ⟩ | [ʔa] | before vowel [ʔ] · default [ʔa] |
| ⟨أَ⟩ | [ʔa] |  |
| ⟨أُ⟩ | [ʔu] |  |
| ⟨أُو⟩ | [ʔuː] |  |
| ⟨ؤ⟩ | [ʔ] |  |
| ⟨إ⟩ | [ʔi] | before vowel [ʔ] · default [ʔi] |
| ⟨إِ⟩ | [ʔi] |  |
| ⟨إِي⟩ | [ʔiː] |  |
| ⟨ئ⟩ | [ʔ] |  |
| ⟨ا⟩ | [ʔ] [aː] | default [aː] [ʔ] · word initial [ʔ] [aː] |
| ⟨ال⟩ | [al] [a] |  |
| ⟨التت⟩ | [att] |  |
| ⟨الثث⟩ | [att] [ass] [aθθ] |  |
| ⟨الدد⟩ | [add] |  |
| ⟨الذذ⟩ | [add] [azz] [aðð] |  |
| ⟨الرر⟩ | [arr] |  |
| ⟨الزز⟩ | [azz] |  |
| ⟨السس⟩ | [ass] |  |
| ⟨الشش⟩ | [aʃʃ] |  |
| ⟨الصص⟩ | [asˤsˤ] |  |
| ⟨الضض⟩ | [adˤdˤ] |  |
| ⟨الطط⟩ | [atˤtˤ] |  |
| ⟨الظظ⟩ | [adˤdˤ] [azˤzˤ] [aðˤðˤ] |  |
| ⟨اللل⟩ | [all] |  |
| ⟨اللله⟩ | [allaːh] |  |
| ⟨الله⟩ | [allaːh] |  |
| ⟨النن⟩ | [ann] |  |
| ⟨اً⟩ | [an] |  |
| ⟨اَ⟩ | [a] |  |
| ⟨اَل⟩ | [al] |  |
| ⟨اَلتت⟩ | [att] |  |
| ⟨اَلثث⟩ | [att] [ass] [aθθ] |  |
| ⟨اَلدد⟩ | [add] |  |
| ⟨اَلذذ⟩ | [add] [azz] [aðð] |  |
| ⟨اَلرر⟩ | [arr] |  |
| ⟨اَلزز⟩ | [azz] |  |
| ⟨اَلسس⟩ | [ass] |  |
| ⟨اَلشش⟩ | [aʃʃ] |  |
| ⟨اَلصص⟩ | [asˤsˤ] |  |
| ⟨اَلضض⟩ | [adˤdˤ] |  |
| ⟨اَلطط⟩ | [atˤtˤ] |  |
| ⟨اَلظظ⟩ | [adˤdˤ] [azˤzˤ] [aðˤðˤ] |  |
| ⟨اَللل⟩ | [all] |  |
| ⟨اَلنن⟩ | [ann] |  |
| ⟨اِل⟩ | [il] |  |
| ⟨اِلتت⟩ | [itt] |  |
| ⟨اِلثث⟩ | [itt] [iss] [iθθ] |  |
| ⟨اِلدد⟩ | [idd] |  |
| ⟨اِلذذ⟩ | [idd] [izz] [iðð] |  |
| ⟨اِلرر⟩ | [irr] |  |
| ⟨اِلزز⟩ | [izz] |  |
| ⟨اِلسس⟩ | [iss] |  |
| ⟨اِلشش⟩ | [iʃʃ] |  |
| ⟨اِلصص⟩ | [isˤsˤ] |  |
| ⟨اِلضض⟩ | [idˤdˤ] |  |
| ⟨اِلطط⟩ | [itˤtˤ] |  |
| ⟨اِلظظ⟩ | [idˤdˤ] [izˤzˤ] [iðˤðˤ] |  |
| ⟨اِللل⟩ | [ill] |  |
| ⟨اِلنن⟩ | [inn] |  |
| ⟨ب⟩ | [b] |  |
| ⟨بِال⟩ | [bil] |  |
| ⟨بِالتت⟩ | [bitt] |  |
| ⟨بِالثث⟩ | [bitt] [biss] [biθθ] |  |
| ⟨بِالدد⟩ | [bidd] |  |
| ⟨بِالذذ⟩ | [bidd] [bizz] [biðð] |  |
| ⟨بِالرر⟩ | [birr] |  |
| ⟨بِالزز⟩ | [bizz] |  |
| ⟨بِالسس⟩ | [biss] |  |
| ⟨بِالشش⟩ | [biʃʃ] |  |
| ⟨بِالصص⟩ | [bisˤsˤ] |  |
| ⟨بِالضض⟩ | [bidˤdˤ] |  |
| ⟨بِالطط⟩ | [bitˤtˤ] |  |
| ⟨بِالظظ⟩ | [bidˤdˤ] [bizˤzˤ] [biðˤðˤ] |  |
| ⟨بِاللل⟩ | [bill] |  |
| ⟨بِالنن⟩ | [binn] |  |
| ⟨بِٱ⟩ | [bi] |  |
| ⟨ة⟩ | [a] [at] | after vowel ∅ · default [a] [at] |
| ⟨ةً⟩ | [tan] |  |
| ⟨ةٌ⟩ | [tun] |  |
| ⟨ةٍ⟩ | [tin] |  |
| ⟨ةَ⟩ | [ta] |  |
| ⟨ةُ⟩ | [tu] |  |
| ⟨ةِ⟩ | [ti] |  |
| ⟨ت⟩ | [t] |  |
| ⟨ث⟩ | [t] [s] [θ] |  |
| ⟨ج⟩ | [dʒ] [ʒ] |  |
| ⟨ح⟩ | [ħ] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d] |  |
| ⟨ذ⟩ | [d] [z] [ð] |  |
| ⟨ر⟩ | [r] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [sˤ] |  |
| ⟨ض⟩ | [dˤ] |  |
| ⟨ط⟩ | [tˤ] |  |
| ⟨ظ⟩ | [dˤ] [zˤ] [ðˤ] |  |
| ⟨ع⟩ | [ʕ] |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ـ⟩ | ∅ |  |
| ⟨ف⟩ | [f] |  |
| ⟨فَال⟩ | [fal] |  |
| ⟨فَالتت⟩ | [fatt] |  |
| ⟨فَالثث⟩ | [fatt] [fass] [faθθ] |  |
| ⟨فَالدد⟩ | [fadd] |  |
| ⟨فَالذذ⟩ | [fadd] [fazz] [faðð] |  |
| ⟨فَالرر⟩ | [farr] |  |
| ⟨فَالزز⟩ | [fazz] |  |
| ⟨فَالسس⟩ | [fass] |  |
| ⟨فَالشش⟩ | [faʃʃ] |  |
| ⟨فَالصص⟩ | [fasˤsˤ] |  |
| ⟨فَالضض⟩ | [fadˤdˤ] |  |
| ⟨فَالطط⟩ | [fatˤtˤ] |  |
| ⟨فَالظظ⟩ | [fadˤdˤ] [fazˤzˤ] [faðˤðˤ] |  |
| ⟨فَاللل⟩ | [fall] |  |
| ⟨فَالنن⟩ | [fann] |  |
| ⟨فَٱ⟩ | [fa] |  |
| ⟨ق⟩ | [ɡ] [ʔ] [q] |  |
| ⟨ك⟩ | [k] [tʃ] |  |
| ⟨كَال⟩ | [kal] |  |
| ⟨كَالتت⟩ | [katt] |  |
| ⟨كَالثث⟩ | [katt] [kass] [kaθθ] |  |
| ⟨كَالدد⟩ | [kadd] |  |
| ⟨كَالذذ⟩ | [kadd] [kazz] [kaðð] |  |
| ⟨كَالرر⟩ | [karr] |  |
| ⟨كَالزز⟩ | [kazz] |  |
| ⟨كَالسس⟩ | [kass] |  |
| ⟨كَالشش⟩ | [kaʃʃ] |  |
| ⟨كَالصص⟩ | [kasˤsˤ] |  |
| ⟨كَالضض⟩ | [kadˤdˤ] |  |
| ⟨كَالطط⟩ | [katˤtˤ] |  |
| ⟨كَالظظ⟩ | [kadˤdˤ] [kazˤzˤ] [kaðˤðˤ] |  |
| ⟨كَاللل⟩ | [kall] |  |
| ⟨كَالنن⟩ | [kann] |  |
| ⟨كَٱ⟩ | [ka] |  |
| ⟨ل⟩ | [l] |  |
| ⟨لِل⟩ | [lil] |  |
| ⟨لِلتت⟩ | [litt] |  |
| ⟨لِلثث⟩ | [litt] [liss] [liθθ] |  |
| ⟨لِلدد⟩ | [lidd] |  |
| ⟨لِلذذ⟩ | [lidd] [lizz] [liðð] |  |
| ⟨لِلرر⟩ | [lirr] |  |
| ⟨لِلزز⟩ | [lizz] |  |
| ⟨لِلسس⟩ | [liss] |  |
| ⟨لِلشش⟩ | [liʃʃ] |  |
| ⟨لِلصص⟩ | [lisˤsˤ] |  |
| ⟨لِلضض⟩ | [lidˤdˤ] |  |
| ⟨لِلطط⟩ | [litˤtˤ] |  |
| ⟨لِلظظ⟩ | [lidˤdˤ] [lizˤzˤ] [liðˤðˤ] |  |
| ⟨لِللل⟩ | [lill] |  |
| ⟨لِلنن⟩ | [linn] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨ه⟩ | [h] |  |
| ⟨و⟩ | [w] [uː] | after consonant [uː] [oː] [w] · after vowel [w] · default [w] [uː] · word initial [w] |
| ⟨وة⟩ | [wa] [wat] |  |
| ⟨وو⟩ | [ww] |  |
| ⟨وي⟩ | [wiː] [weː] [uːj] |  |
| ⟨وية⟩ | [uːja] [wja] |  |
| ⟨وَ⟩ | [wa] |  |
| ⟨وَا⟩ | [waː] |  |
| ⟨وَال⟩ | [wal] |  |
| ⟨وَالتت⟩ | [watt] |  |
| ⟨وَالثث⟩ | [watt] [wass] [waθθ] |  |
| ⟨وَالدد⟩ | [wadd] |  |
| ⟨وَالذذ⟩ | [wadd] [wazz] [waðð] |  |
| ⟨وَالرر⟩ | [warr] |  |
| ⟨وَالزز⟩ | [wazz] |  |
| ⟨وَالسس⟩ | [wass] |  |
| ⟨وَالشش⟩ | [waʃʃ] |  |
| ⟨وَالصص⟩ | [wasˤsˤ] |  |
| ⟨وَالضض⟩ | [wadˤdˤ] |  |
| ⟨وَالطط⟩ | [watˤtˤ] |  |
| ⟨وَالظظ⟩ | [wadˤdˤ] [wazˤzˤ] [waðˤðˤ] |  |
| ⟨وَاللل⟩ | [wall] |  |
| ⟨وَالنن⟩ | [wann] |  |
| ⟨وَيْ⟩ | [weː] |  |
| ⟨وَٱ⟩ | [wa] |  |
| ⟨وُ⟩ | [wu] |  |
| ⟨وِال⟩ | [wil] |  |
| ⟨وِالتت⟩ | [witt] |  |
| ⟨وِالثث⟩ | [witt] [wiss] [wiθθ] |  |
| ⟨وِالدد⟩ | [widd] |  |
| ⟨وِالذذ⟩ | [widd] [wizz] [wiðð] |  |
| ⟨وِالرر⟩ | [wirr] |  |
| ⟨وِالزز⟩ | [wizz] |  |
| ⟨وِالسس⟩ | [wiss] |  |
| ⟨وِالشش⟩ | [wiʃʃ] |  |
| ⟨وِالصص⟩ | [wisˤsˤ] |  |
| ⟨وِالضض⟩ | [widˤdˤ] |  |
| ⟨وِالطط⟩ | [witˤtˤ] |  |
| ⟨وِالظظ⟩ | [widˤdˤ] [wizˤzˤ] [wiðˤðˤ] |  |
| ⟨وِاللل⟩ | [will] |  |
| ⟨وِالنن⟩ | [winn] |  |
| ⟨وِٱ⟩ | [wi] |  |
| ⟨ى⟩ | [aː] |  |
| ⟨ي⟩ | [j] [iː] | after consonant [iː] [eː] [j] · after vowel [j] · default [j] [iː] · word initial [j] |
| ⟨ية⟩ | [ja] [jat] |  |
| ⟨يو⟩ | [juː] [joː] [iːw] |  |
| ⟨يوة⟩ | [iːwa] [eːwa] [jwa] |  |
| ⟨يي⟩ | [jj] |  |
| ⟨يَ⟩ | [ja] |  |
| ⟨يَا⟩ | [jaː] |  |
| ⟨يَوْ⟩ | [joː] |  |
| ⟨يِ⟩ | [ji] |  |
| ⟨يِة⟩ | [je] |  |
| ⟨ً⟩ | [an] |  |
| ⟨ًا⟩ | [an] |  |
| ⟨ًى⟩ | [an] |  |
| ⟨ٌ⟩ | [un] |  |
| ⟨ٍ⟩ | [in] |  |
| ⟨َ⟩ | [a] |  |
| ⟨َا⟩ | [aː] |  |
| ⟨َاي⟩ | [aːj] |  |
| ⟨َة⟩ | [a] | before vowel [at] · default [a] |
| ⟨َو⟩ | [aw] |  |
| ⟨َوو⟩ | [aww] |  |
| ⟨َوَ⟩ | [awa] |  |
| ⟨َوَا⟩ | [awaː] |  |
| ⟨َوُ⟩ | [awu] |  |
| ⟨َوِ⟩ | [awi] |  |
| ⟨َى⟩ | [aː] |  |
| ⟨َي⟩ | [aj] |  |
| ⟨َيي⟩ | [ajj] |  |
| ⟨َيَ⟩ | [aja] |  |
| ⟨َيَا⟩ | [ajaː] |  |
| ⟨َيُ⟩ | [aju] |  |
| ⟨َيِ⟩ | [aji] |  |
| ⟨َٰ⟩ | [aː] |  |
| ⟨ُ⟩ | [u] |  |
| ⟨ُو⟩ | [uː] |  |
| ⟨ُوا⟩ | [uː] |  |
| ⟨ُوو⟩ | [uww] |  |
| ⟨ُوي⟩ | [uːj] |  |
| ⟨ُوَ⟩ | [uwa] |  |
| ⟨ُوَا⟩ | [uwaː] |  |
| ⟨ِ⟩ | [i] |  |
| ⟨ِة⟩ | [e] |  |
| ⟨ِي⟩ | [iː] |  |
| ⟨ِيي⟩ | [ijj] |  |
| ⟨ِيَ⟩ | [ija] |  |
| ⟨ِيَا⟩ | [ijaː] |  |
| ⟨ّ⟩ | [ː] |  |
| ⟨ْ⟩ | ∅ |  |
| ⟨ْو⟩ | [w] |  |
| ⟨ْي⟩ | [j] |  |
| ⟨ٰ⟩ | [aː] |  |
| ⟨ٱ⟩ | ∅ |  |
| ⟨ٱل⟩ | [al] |  |
| ⟨ٲ⟩ | [ʔa] |  |
| ⟨پ⟩ | [p] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨ڤ⟩ | [v] |  |
| ⟨ک⟩ | [k] |  |
| ⟨ڪ⟩ | [k] |  |
| ⟨ھ⟩ | [h] |  |
| ⟨ی⟩ | [j] [iː] |  |

Stress falls on the antepenult by default. Stress is sensitive to syllable weight.

Whole-word exceptions (1): ⟨إِذَا⟩ [ʔizaː].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 27 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AR_WASL_EPENTHESIS` | /ʔ/ → [ʔi], word-initially, before a consonant | ⟨اسْأَل⟩ [ʔisʔal] | Ryding 2005 |
| `AR_EMPHASIS_SPREAD_A_AFTER` | /a/ → [ɑ], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_A_BEFORE` | /a/ → [ɑ], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_AFTER` | /aː/ → [ɑː], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_BEFORE` | /aː/ → [ɑː], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_AFTER` | /i/ → [ɪ], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_BEFORE` | /i/ → [ɪ], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_AFTER` | /iː/ → [ɪː], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_BEFORE` | /iː/ → [ɪː], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_AFTER` | /u/ → [ʊ], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_BEFORE` | /u/ → [ʊ], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_AFTER` | /uː/ → [ʊː], after an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_BEFORE` | /uː/ → [ʊː], before an emphatic consonant | - | Watson 2002, Davis 1995, Card 1983 |
| `AR_EMPH_BACK_A_AFTER` | /a/ → [ɑ], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_EMPH_BACK_A_BEFORE` | /a/ → [ɑ], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_EMPH_BACK_AA_AFTER` | /aː/ → [ɑː], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_EMPH_BACK_AA_BEFORE` | /aː/ → [ɑː], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_GLIDE_YA_BEFORE_GEMINATE` | /iː/ → [ij], before [iː] | ⟨مِصْرِيّ⟩ [misˤrijj] | Ryding 2005 |
| `AR_GLIDE_YA_GEMINATE_COPY` | /iː/ → [j], after [iː] | ⟨ends⟩ [ijj] | Ryding 2005 |
| `AR_GLIDE_YA_CONSONANTAL` | /iː/ → [ij], before [j] [ja] [ji] [ju] [jaː] [jiː] [juː] | ⟨ـِيّ⟩ [-ijj] | Watson 2002, Ryding 2005 |
| `AR_GLIDE_WAW_CONSONANTAL` | /uː/ → [uw], before [w] [wa] [wi] [wu] [waː] [wiː] [wuː] | ⟨أُبُوَّة⟩ [ʔubuwwa] | - |
| `AR_LEV_MONO_AY` | /aj/ → [eː] | - | [Fadda 2016](#src-fadda2016), [Almbark 2015](#src-almbark2015) |
| `AR_LEV_MONO_AW` | /aw/ → [oː] | - | [Fadda 2016](#src-fadda2016), [Almbark 2015](#src-almbark2015) |
| `AR_LEV_EMPH_BACK_A_AFTER` | /a/ → [ɑ], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Almbark 2015](#src-almbark2015), Watson 2002 |
| `AR_LEV_EMPH_BACK_A_BEFORE` | /a/ → [ɑ], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_LEV_EMPH_BACK_AA_AFTER` | /aː/ → [ɑː], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |
| `AR_LEV_EMPH_BACK_AA_BEFORE` | /aː/ → [ɑː], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | Watson 2002 |

The spec applies 1 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `AR_HAMZAT_WASL_ARTICLE` | `[aiueoɑæə]ː?$` | `^[aɑ](?=[^aeiouɑɐæɪʊəɛɔː])` | right ∅ | - | Ryding 2005 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "apc-JO")`. They are engine output, not reference transcriptions.

The next table sets the engine output against worked examples printed in a cited source, from the [primary-source gold](../evaluation/datasets.md#primary-source-gold-primary_sources). The rows are spread evenly over that set. The last column says whether the two transcriptions are the same string.

| Spelling | Printed in the source | Engine output | Source, page | Same |
|:--|:--|:--|:--|:--|
| بَيت | SA bajt → AA be:t | [ˈbeːt] | Fadda 2016, p. 29 | no |
| صَوت | SA sˤawt → AA sˤo:tˤ | [ˈsˤoːt] | Fadda 2016, p. 29 | no |
| مَيِّل | [majjɪl] | [ˈmajjil] | Fadda 2016, p. 29 | no |
| رُوح | SA [ru:ħ] → AA [rɵ:ħ] | [ˈruːħ] | Fadda 2016, p. 29 | no |
| أُمّ | [ʔumm] | [ˈʔumm] | Fadda 2016, p. 30 | no |
| حُبّ | [ħubb] | [ˈħubb] | Fadda 2016, p. 30 | no |
| حِبّ | [ħɪbb] | [ˈħibb] | Fadda 2016, p. 30 | no |
| حِلْوَة | [ħɪlwɛ] | [ˈħilwa] | Fadda 2016, p. 30 | no |
| بِشْعَة | [bɪʃʕa] | [ˈbiʃʕa] | Fadda 2016, p. 30 | no |
| عَمَّان | [ʕamma:n] ~ [ʕammæ:n] ~ [ʕammɛ:n] ~ [ʕamme:n] | [ʕamˈmaːn] | Fadda 2016, p. 30 | no |
| ذَنْب | [ðənb] → [zəmb] | [ˈdanb] | Fadda 2016, p. 15 | no |
| ثُلْث | [θʊlθ] → [tʊlt] | [ˈtult] | Fadda 2016, p. 15 | no |

Source: Fadda, H. (2016). *Language Variation in Western Amman*. MA thesis, Canada Institute of Linguistics. [web.archive.org](https://web.archive.org/web/20250210163657/https://www.canil.ca/wordpress/wp-content/uploads/2019/11/Fadda-Language-Variation-in-Western-Amman.pdf)
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

| Repository | What it does with this spec |
|:--|:--|
| [arbtok](https://github.com/TigreGotico/arbtok) | Arabic text to IPA, with tashkeel restoration that knows the dialect. |
<!-- atlas:related end -->

---
[← Jingpho](kac.md) · [Home](../index.md) · [Juba Arabic →](pga.md)
