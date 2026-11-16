# Eastern Egyptian Bedawi Arabic (`avl-EG`)

<!-- atlas:summary begin -->
Eastern Egyptian Bedawi Arabic is a Central Semitic language, written in the Arabic script. Its code names Egypt. The `avl-EG` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `avl-EG` |
| Aliases | `ar-EG-x-bedawi`, `avl` |
| ISO 639-3 | [avl](https://iso639-3.sil.org/code/avl), Eastern Egyptian Bedawi Arabic |
| Glottolog | [east2690](https://glottolog.org/resource/languoid/id/east2690), Eastern Egyptian Bedawi Arabic |
| Wikipedia | [Eastern Egyptian Bedawi Arabic](https://en.wikipedia.org/wiki/Eastern_Egyptian_Bedawi_Arabic) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Africa](by-region.md#africa) > [Egypt](by-region.md#egypt) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Egyptian Arabic (Cairene)](arz-EG.md) `arz-EG` |
| Explorer | [`avl-EG` in the data explorer](https://tigregotico.github.io/orthography2ipa/#avl-EG) |
| Spec file | [`avl-EG.json`](../../orthography2ipa/data/avl-EG.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Eastern Egyptian Bedawi Arabic, the Bedouin dialects of Sinai and the eastern desert. INPUT CONTRACT: transcribes orthography+harakat. It hangs off arz-EG and differs from Cairene in three places, one of them structural.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2002 to 2004. [Sources](#sources) lists them. The spec file writes 6 of the 258 spellings of its letter table and takes the other 252 from [Egyptian Arabic (Cairene)](arz-EG.md) `arz-EG`.

The [spec file](../../orthography2ipa/data/avl-EG.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `avl-EG` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-dejong2004"></a>de Jong, R. (2004). *Characteristics of Bedouin Dialects in Southern Sinai: Preliminary Observations*. Brill, in Haak, de Jong & Versteegh (eds.), Approaches to Arabic Dialects. Cited: 151-164, esp. 154-156. [archive.org](https://archive.org/details/book1_10527)
2. <a id="src-watson2002"></a>Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press. Cited: 9.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 222 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d dˤ t tˤ |  |  | k ɡ | q |  | ʔ |
| Affricate |  |  |  |  | dʒ |  |  |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |  |  |
| Trill |  |  |  | r |  |  |  |  |  |  |
| Fricative |  | f v | ð ðˤ θ | s sˤ z zˤ | ʃ ʒ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l ɫ |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Near-close | ɪ ɪː | ʊ ʊː |
| Close-mid | eː | oː |
| Near-open | æ |  |
| Open | a aː | ɑ ɑː |

Sequences that the spec writes as one unit: [add] [adˤdˤ] [aj] [aja] [ajaː] [aji] [ajijj] [ajiː] [ajj] [aju] [al] [all] [allaːh] [an] [ann] [arr] [ass] [asˤsˤ] [at] [att] [atˤtˤ] [aw] [awa] [awaː] [awi] [awijj] [awiː] [awu] [aww] [azz] [azˤzˤ] [aʃʃ] [aːj] [bi] [bidd] [bidˤdˤ] [bil] [bill] [binn] [birr], and 133 more.
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
| ⟨الثث⟩ | [att] [ass] |  |
| ⟨الدد⟩ | [add] |  |
| ⟨الذذ⟩ | [add] [azz] |  |
| ⟨الرر⟩ | [arr] |  |
| ⟨الزز⟩ | [azz] |  |
| ⟨السس⟩ | [ass] |  |
| ⟨الشش⟩ | [aʃʃ] |  |
| ⟨الصص⟩ | [asˤsˤ] |  |
| ⟨الضض⟩ | [adˤdˤ] |  |
| ⟨الطط⟩ | [atˤtˤ] |  |
| ⟨الظظ⟩ | [adˤdˤ] [azˤzˤ] |  |
| ⟨اللل⟩ | [all] |  |
| ⟨اللله⟩ | [allaːh] |  |
| ⟨الله⟩ | [allaːh] |  |
| ⟨النن⟩ | [ann] |  |
| ⟨اً⟩ | [an] |  |
| ⟨اَ⟩ | [a] |  |
| ⟨اَل⟩ | [al] |  |
| ⟨اَلتت⟩ | [att] |  |
| ⟨اَلثث⟩ | [att] [ass] |  |
| ⟨اَلدد⟩ | [add] |  |
| ⟨اَلذذ⟩ | [add] [azz] |  |
| ⟨اَلرر⟩ | [arr] |  |
| ⟨اَلزز⟩ | [azz] |  |
| ⟨اَلسس⟩ | [ass] |  |
| ⟨اَلشش⟩ | [aʃʃ] |  |
| ⟨اَلصص⟩ | [asˤsˤ] |  |
| ⟨اَلضض⟩ | [adˤdˤ] |  |
| ⟨اَلطط⟩ | [atˤtˤ] |  |
| ⟨اَلظظ⟩ | [adˤdˤ] [azˤzˤ] |  |
| ⟨اَللل⟩ | [all] |  |
| ⟨اَلنن⟩ | [ann] |  |
| ⟨اِل⟩ | [il] |  |
| ⟨اِلتت⟩ | [itt] |  |
| ⟨اِلثث⟩ | [itt] [iss] |  |
| ⟨اِلدد⟩ | [idd] |  |
| ⟨اِلذذ⟩ | [idd] [izz] |  |
| ⟨اِلرر⟩ | [irr] |  |
| ⟨اِلزز⟩ | [izz] |  |
| ⟨اِلسس⟩ | [iss] |  |
| ⟨اِلشش⟩ | [iʃʃ] |  |
| ⟨اِلصص⟩ | [isˤsˤ] |  |
| ⟨اِلضض⟩ | [idˤdˤ] |  |
| ⟨اِلطط⟩ | [itˤtˤ] |  |
| ⟨اِلظظ⟩ | [idˤdˤ] [izˤzˤ] |  |
| ⟨اِللل⟩ | [ill] |  |
| ⟨اِلنن⟩ | [inn] |  |
| ⟨ب⟩ | [b] |  |
| ⟨بِال⟩ | [bil] |  |
| ⟨بِالتت⟩ | [bitt] |  |
| ⟨بِالثث⟩ | [bitt] [biss] |  |
| ⟨بِالدد⟩ | [bidd] |  |
| ⟨بِالذذ⟩ | [bidd] [bizz] |  |
| ⟨بِالرر⟩ | [birr] |  |
| ⟨بِالزز⟩ | [bizz] |  |
| ⟨بِالسس⟩ | [biss] |  |
| ⟨بِالشش⟩ | [biʃʃ] |  |
| ⟨بِالصص⟩ | [bisˤsˤ] |  |
| ⟨بِالضض⟩ | [bidˤdˤ] |  |
| ⟨بِالطط⟩ | [bitˤtˤ] |  |
| ⟨بِالظظ⟩ | [bidˤdˤ] [bizˤzˤ] |  |
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
| ⟨ث⟩ | [θ] |  |
| ⟨ج⟩ | [dʒ] [ʒ] |  |
| ⟨ح⟩ | [ħ] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d] |  |
| ⟨ذ⟩ | [ð] |  |
| ⟨ر⟩ | [r] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [sˤ] |  |
| ⟨ض⟩ | [ðˤ] |  |
| ⟨ط⟩ | [tˤ] |  |
| ⟨ظ⟩ | [ðˤ] |  |
| ⟨ع⟩ | [ʕ] |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ـ⟩ | ∅ |  |
| ⟨ف⟩ | [f] |  |
| ⟨فَال⟩ | [fal] |  |
| ⟨فَالتت⟩ | [fatt] |  |
| ⟨فَالثث⟩ | [fatt] [fass] |  |
| ⟨فَالدد⟩ | [fadd] |  |
| ⟨فَالذذ⟩ | [fadd] [fazz] |  |
| ⟨فَالرر⟩ | [farr] |  |
| ⟨فَالزز⟩ | [fazz] |  |
| ⟨فَالسس⟩ | [fass] |  |
| ⟨فَالشش⟩ | [faʃʃ] |  |
| ⟨فَالصص⟩ | [fasˤsˤ] |  |
| ⟨فَالضض⟩ | [fadˤdˤ] |  |
| ⟨فَالطط⟩ | [fatˤtˤ] |  |
| ⟨فَالظظ⟩ | [fadˤdˤ] [fazˤzˤ] |  |
| ⟨فَاللل⟩ | [fall] |  |
| ⟨فَالنن⟩ | [fann] |  |
| ⟨فَٱ⟩ | [fa] |  |
| ⟨ق⟩ | [ɡ] |  |
| ⟨ك⟩ | [k] |  |
| ⟨كَال⟩ | [kal] |  |
| ⟨كَالتت⟩ | [katt] |  |
| ⟨كَالثث⟩ | [katt] [kass] |  |
| ⟨كَالدد⟩ | [kadd] |  |
| ⟨كَالذذ⟩ | [kadd] [kazz] |  |
| ⟨كَالرر⟩ | [karr] |  |
| ⟨كَالزز⟩ | [kazz] |  |
| ⟨كَالسس⟩ | [kass] |  |
| ⟨كَالشش⟩ | [kaʃʃ] |  |
| ⟨كَالصص⟩ | [kasˤsˤ] |  |
| ⟨كَالضض⟩ | [kadˤdˤ] |  |
| ⟨كَالطط⟩ | [katˤtˤ] |  |
| ⟨كَالظظ⟩ | [kadˤdˤ] [kazˤzˤ] |  |
| ⟨كَاللل⟩ | [kall] |  |
| ⟨كَالنن⟩ | [kann] |  |
| ⟨كَٱ⟩ | [ka] |  |
| ⟨ل⟩ | [l] |  |
| ⟨لِل⟩ | [lil] |  |
| ⟨لِلتت⟩ | [litt] |  |
| ⟨لِلثث⟩ | [litt] [liss] |  |
| ⟨لِلدد⟩ | [lidd] |  |
| ⟨لِلذذ⟩ | [lidd] [lizz] |  |
| ⟨لِلرر⟩ | [lirr] |  |
| ⟨لِلزز⟩ | [lizz] |  |
| ⟨لِلسس⟩ | [liss] |  |
| ⟨لِلشش⟩ | [liʃʃ] |  |
| ⟨لِلصص⟩ | [lisˤsˤ] |  |
| ⟨لِلضض⟩ | [lidˤdˤ] |  |
| ⟨لِلطط⟩ | [litˤtˤ] |  |
| ⟨لِلظظ⟩ | [lidˤdˤ] [lizˤzˤ] |  |
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
| ⟨وَالثث⟩ | [watt] [wass] |  |
| ⟨وَالدد⟩ | [wadd] |  |
| ⟨وَالذذ⟩ | [wadd] [wazz] |  |
| ⟨وَالرر⟩ | [warr] |  |
| ⟨وَالزز⟩ | [wazz] |  |
| ⟨وَالسس⟩ | [wass] |  |
| ⟨وَالشش⟩ | [waʃʃ] |  |
| ⟨وَالصص⟩ | [wasˤsˤ] |  |
| ⟨وَالضض⟩ | [wadˤdˤ] |  |
| ⟨وَالطط⟩ | [watˤtˤ] |  |
| ⟨وَالظظ⟩ | [wadˤdˤ] [wazˤzˤ] |  |
| ⟨وَاللل⟩ | [wall] |  |
| ⟨وَالنن⟩ | [wann] |  |
| ⟨وَٱ⟩ | [wa] |  |
| ⟨وُ⟩ | [wu] |  |
| ⟨وِال⟩ | [wil] |  |
| ⟨وِالتت⟩ | [witt] |  |
| ⟨وِالثث⟩ | [witt] [wiss] |  |
| ⟨وِالدد⟩ | [widd] |  |
| ⟨وِالذذ⟩ | [widd] [wizz] |  |
| ⟨وِالرر⟩ | [wirr] |  |
| ⟨وِالزز⟩ | [wizz] |  |
| ⟨وِالسس⟩ | [wiss] |  |
| ⟨وِالشش⟩ | [wiʃʃ] |  |
| ⟨وِالصص⟩ | [wisˤsˤ] |  |
| ⟨وِالضض⟩ | [widˤdˤ] |  |
| ⟨وِالطط⟩ | [witˤtˤ] |  |
| ⟨وِالظظ⟩ | [widˤdˤ] [wizˤzˤ] |  |
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
| ⟨يِ⟩ | [ji] |  |
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
| ⟨َوِيي⟩ | [awijj] |  |
| ⟨َى⟩ | [aː] |  |
| ⟨َي⟩ | [aj] |  |
| ⟨َيي⟩ | [ajj] |  |
| ⟨َيَ⟩ | [aja] |  |
| ⟨َيَا⟩ | [ajaː] |  |
| ⟨َيُ⟩ | [aju] |  |
| ⟨َيِ⟩ | [aji] |  |
| ⟨َيِيي⟩ | [ajijj] |  |
| ⟨َٰ⟩ | [aː] |  |
| ⟨ُ⟩ | [u] |  |
| ⟨ُو⟩ | [uː] |  |
| ⟨ُوا⟩ | [uː] |  |
| ⟨ُوو⟩ | [uww] |  |
| ⟨ُوي⟩ | [uːj] |  |
| ⟨ُوَ⟩ | [uwa] |  |
| ⟨ُوَا⟩ | [uwaː] |  |
| ⟨ِ⟩ | [i] |  |
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
| ⟨چ⟩ | [ʒ] |  |
| ⟨ڤ⟩ | [v] |  |
| ⟨ک⟩ | [k] |  |
| ⟨ڪ⟩ | [k] |  |
| ⟨ھ⟩ | [h] |  |
| ⟨ی⟩ | [j] [iː] |  |

Stress falls on the antepenult by default. Stress is sensitive to syllable weight.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 27 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AR_WASL_EPENTHESIS` | /ʔ/ → [ʔi], word-initially, before a consonant | ⟨اسْأَل⟩ [ʔisʔal] | Ryding 2005 |
| `AR_EMPHASIS_SPREAD_A_AFTER` | /a/ → [ɑ], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_A_BEFORE` | /a/ → [ɑ], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_AFTER` | /aː/ → [ɑː], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_BEFORE` | /aː/ → [ɑː], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_AFTER` | /i/ → [ɪ], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_BEFORE` | /i/ → [ɪ], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_AFTER` | /iː/ → [ɪː], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_BEFORE` | /iː/ → [ɪː], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_AFTER` | /u/ → [ʊ], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_BEFORE` | /u/ → [ʊ], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_AFTER` | /uː/ → [ʊː], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_BEFORE` | /uː/ → [ʊː], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPH_BACK_A_AFTER` | /a/ → [ɑ], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_EMPH_BACK_A_BEFORE` | /a/ → [ɑ], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_EMPH_BACK_AA_AFTER` | /aː/ → [ɑː], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_EMPH_BACK_AA_BEFORE` | /aː/ → [ɑː], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_GLIDE_YA_BEFORE_GEMINATE` | /iː/ → [ij], before [iː] | ⟨مِصْرِيّ⟩ [misˤrijj] | Ryding 2005 |
| `AR_GLIDE_YA_GEMINATE_COPY` | /iː/ → [j], after [iː] | ⟨ends⟩ [ijj] | Ryding 2005 |
| `AR_GLIDE_YA_CONSONANTAL` | /iː/ → [ij], before [j] [ja] [ji] [ju] [jaː] [jiː] [juː] | ⟨ـِيّ⟩ [-ijj] | [Watson 2002](#src-watson2002), Ryding 2005 |
| `AR_GLIDE_WAW_CONSONANTAL` | /uː/ → [uw], before [w] [wa] [wi] [wu] [waː] [wiː] [wuː] | ⟨أُبُوَّة⟩ [ʔubuwwa] | - |
| `AR_EG_EMPH_BACK_A_AFTER` | /a/ → [ɑ], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_EG_EMPH_BACK_A_BEFORE` | /a/ → [ɑ], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_EG_EMPH_BACK_AA_AFTER` | /aː/ → [ɑː], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_EG_EMPH_BACK_AA_BEFORE` | /aː/ → [ɑː], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `EG_MONO_AY` | /aj/ → [eː] | - | [Watson 2002](#src-watson2002), Mitchell 1956, Badawi & Hinds 1986 |
| `EG_MONO_AW` | /aw/ → [oː] | - | [Watson 2002](#src-watson2002), Mitchell 1956 |

The spec applies 1 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `AR_HAMZAT_WASL_ARTICLE` | `[aiueoɑæə]ː?$` | `^[aɑ](?=[^aeiouɑɐæɪʊəɛɔː])` | right ∅ | - | Ryding 2005 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "avl-EG")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

| Repository | What it does with this spec |
|:--|:--|
| [arbtok](https://github.com/TigreGotico/arbtok) | Arabic text to IPA, with tashkeel restoration that knows the dialect. |
<!-- atlas:related end -->

---
[← Eastern Asturian-Leonese](ast-x-oriental.md) · [Home](../index.md) · [Eastern Galician →](gl-ES-x-oriental.md)
