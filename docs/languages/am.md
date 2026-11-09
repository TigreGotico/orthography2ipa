# Amharic (`am`)

<!-- atlas:summary begin -->
Amharic is a Semitic language, written in the Ethiopic script. Glottolog places it in Djibouti and Ethiopia. The `am` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `am` |
| ISO 639-3 | [amh](https://iso639-3.sil.org/code/amh), Amharic |
| Glottolog | [amha1245](https://glottolog.org/resource/languoid/id/amha1245), Amharic |
| Wikidata | [Q28244](https://www.wikidata.org/wiki/Q28244) |
| Wikipedia | [Amharic](https://en.wikipedia.org/wiki/Amharic) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic](by-family.md#afro-asiatic--semitic) |
| Region | [Africa](by-region.md#africa) > [Djibouti](by-region.md#djibouti), [Ethiopia](by-region.md#ethiopia) |
| Script | [Ethiopic](by-script.md#ethiopic) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [Proto-Ethiopian-Semitic (family node)](https://tigregotico.github.io/orthography2ipa/#sem-x-ethiopic) `sem-x-ethiopic` |
| Explorer | [`am` in the data explorer](https://tigregotico.github.io/orthography2ipa/#am) |
| Spec file | [`am.json`](../../orthography2ipa/data/am.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Amharic Ethiopic (Ge'ez) script. Abugida where each character encodes consonant + vowel, 7 vowel orders per consonant row. Ejectives: Kʼ, Tʼ, Čʼ, Pʼ, Tsʼ are phonemic.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1992 to 2020. [Sources](#sources) lists them. The spec file writes all 286 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/am.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `am` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-leslau1995"></a>Leslau, W. (1995). *Reference Grammar of Amharic*. Harrassowitz.
2. <a id="src-ado2021labialised"></a>Ado, Derib (2020). *Revisiting the status of labialised consonants in contemporary Amharic*. Oslo Studies in Language 11(2), 47-58. Cited: 47-58. [doi.org](https://doi.org/10.5617/osla.8487)
3. <a id="src-hayward1992amharic"></a>Hayward, K. & Hayward, R. J. (1992). *Amharic (Illustrations of the IPA)*. Journal of the International Phonetic Association 22(1-2). Cited: 48-52. [doi.org](https://doi.org/10.1017/S0025100300004606)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `am` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 388 | 0.3296 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `am` | generated | epitran-derived | CC0 1.0 | 5453 | 0.2376 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 239 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  | d t tʼ |  |  | k kʷ kʼ kʼʷ ɡ ɡʷ | ʔ |
| Affricate |  |  | tsʼ | dʒ tʃ tʃʼ |  |  |  |
| Nasal | m |  | n |  | ɲ |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | h hʷ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Central |
|:--|:-:|
| Close | ɨ |

Sequences that the spec writes as one unit: [ba] [be] [bi] [bo] [bu] [bə] [bʷa] [da] [de] [di] [do] [du] [də] [dʒa] [dʒe] [dʒi] [dʒo] [dʒu] [dʒə] [dʒʷa] [dʷa] [fa] [fe] [fi] [fo] [fu] [fə] [fʷa] [ha] [haː] [he] [hi] [ho] [hu] [hə] [hʷa] [hʷe] [hʷi] [hʷə] [ja], and 167 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ሀ⟩ | [hə] |  |
| ⟨ሁ⟩ | [hu] |  |
| ⟨ሂ⟩ | [hi] |  |
| ⟨ሃ⟩ | [haː] |  |
| ⟨ሄ⟩ | [he] |  |
| ⟨ህ⟩ | [h] |  |
| ⟨ሆ⟩ | [ho] |  |
| ⟨ለ⟩ | [lə] |  |
| ⟨ሉ⟩ | [lu] |  |
| ⟨ሊ⟩ | [li] |  |
| ⟨ላ⟩ | [la] |  |
| ⟨ሌ⟩ | [le] |  |
| ⟨ል⟩ | [l] |  |
| ⟨ሎ⟩ | [lo] |  |
| ⟨ሏ⟩ | [lʷa] |  |
| ⟨ሐ⟩ | [hə] |  |
| ⟨ሑ⟩ | [hu] |  |
| ⟨ሒ⟩ | [hi] |  |
| ⟨ሓ⟩ | [ha] |  |
| ⟨ሔ⟩ | [he] |  |
| ⟨ሕ⟩ | [h] |  |
| ⟨ሖ⟩ | [ho] |  |
| ⟨ሗ⟩ | [hʷa] |  |
| ⟨መ⟩ | [mə] |  |
| ⟨ሙ⟩ | [mu] |  |
| ⟨ሚ⟩ | [mi] |  |
| ⟨ማ⟩ | [ma] |  |
| ⟨ሜ⟩ | [me] |  |
| ⟨ም⟩ | [m] |  |
| ⟨ሞ⟩ | [mo] |  |
| ⟨ሟ⟩ | [mʷa] |  |
| ⟨ሠ⟩ | [sə] |  |
| ⟨ሡ⟩ | [su] |  |
| ⟨ሢ⟩ | [si] |  |
| ⟨ሣ⟩ | [sa] |  |
| ⟨ሤ⟩ | [se] |  |
| ⟨ሥ⟩ | [s] |  |
| ⟨ሦ⟩ | [so] |  |
| ⟨ሧ⟩ | [sʷa] |  |
| ⟨ረ⟩ | [ɾə] |  |
| ⟨ሩ⟩ | [ɾu] |  |
| ⟨ሪ⟩ | [ɾi] |  |
| ⟨ራ⟩ | [ɾa] |  |
| ⟨ሬ⟩ | [ɾe] |  |
| ⟨ር⟩ | [ɾ] |  |
| ⟨ሮ⟩ | [ɾo] |  |
| ⟨ሯ⟩ | [ɾʷa] |  |
| ⟨ሰ⟩ | [sə] |  |
| ⟨ሱ⟩ | [su] |  |
| ⟨ሲ⟩ | [si] |  |
| ⟨ሳ⟩ | [sa] |  |
| ⟨ሴ⟩ | [se] |  |
| ⟨ስ⟩ | [s] |  |
| ⟨ሶ⟩ | [so] |  |
| ⟨ሷ⟩ | [sʷa] |  |
| ⟨ሸ⟩ | [ʃə] |  |
| ⟨ሹ⟩ | [ʃu] |  |
| ⟨ሺ⟩ | [ʃi] |  |
| ⟨ሻ⟩ | [ʃa] |  |
| ⟨ሼ⟩ | [ʃe] |  |
| ⟨ሽ⟩ | [ʃ] |  |
| ⟨ሾ⟩ | [ʃo] |  |
| ⟨ሿ⟩ | [ʃʷa] |  |
| ⟨ቀ⟩ | [kʼə] |  |
| ⟨ቁ⟩ | [kʼu] |  |
| ⟨ቂ⟩ | [kʼi] |  |
| ⟨ቃ⟩ | [kʼa] |  |
| ⟨ቄ⟩ | [kʼe] |  |
| ⟨ቅ⟩ | [kʼ] |  |
| ⟨ቆ⟩ | [kʼo] |  |
| ⟨ቈ⟩ | [kʼʷə] |  |
| ⟨ቊ⟩ | [kʼʷi] |  |
| ⟨ቋ⟩ | [kʼʷa] |  |
| ⟨ቌ⟩ | [kʼʷe] |  |
| ⟨ቍ⟩ | [kʼʷ] |  |
| ⟨በ⟩ | [bə] |  |
| ⟨ቡ⟩ | [bu] |  |
| ⟨ቢ⟩ | [bi] |  |
| ⟨ባ⟩ | [ba] |  |
| ⟨ቤ⟩ | [be] |  |
| ⟨ብ⟩ | [b] |  |
| ⟨ቦ⟩ | [bo] |  |
| ⟨ቧ⟩ | [bʷa] |  |
| ⟨ቨ⟩ | [və] |  |
| ⟨ቩ⟩ | [vu] |  |
| ⟨ቪ⟩ | [vi] |  |
| ⟨ቫ⟩ | [va] |  |
| ⟨ቬ⟩ | [ve] |  |
| ⟨ቭ⟩ | [v] |  |
| ⟨ቮ⟩ | [vo] |  |
| ⟨ቯ⟩ | [vʷa] |  |
| ⟨ተ⟩ | [tə] |  |
| ⟨ቱ⟩ | [tu] |  |
| ⟨ቲ⟩ | [ti] |  |
| ⟨ታ⟩ | [ta] |  |
| ⟨ቴ⟩ | [te] |  |
| ⟨ት⟩ | [t] |  |
| ⟨ቶ⟩ | [to] |  |
| ⟨ቷ⟩ | [tʷa] |  |
| ⟨ቸ⟩ | [tʃə] |  |
| ⟨ቹ⟩ | [tʃu] |  |
| ⟨ቺ⟩ | [tʃi] |  |
| ⟨ቻ⟩ | [tʃa] |  |
| ⟨ቼ⟩ | [tʃe] |  |
| ⟨ች⟩ | [tʃ] |  |
| ⟨ቾ⟩ | [tʃo] |  |
| ⟨ቿ⟩ | [tʃʷa] |  |
| ⟨ኀ⟩ | [hə] |  |
| ⟨ኁ⟩ | [hu] |  |
| ⟨ኂ⟩ | [hi] |  |
| ⟨ኃ⟩ | [ha] |  |
| ⟨ኄ⟩ | [he] |  |
| ⟨ኅ⟩ | [h] |  |
| ⟨ኆ⟩ | [ho] |  |
| ⟨ኈ⟩ | [hʷə] |  |
| ⟨ኊ⟩ | [hʷi] |  |
| ⟨ኋ⟩ | [hʷa] |  |
| ⟨ኌ⟩ | [hʷe] |  |
| ⟨ኍ⟩ | [hʷ] |  |
| ⟨ነ⟩ | [nə] |  |
| ⟨ኑ⟩ | [nu] |  |
| ⟨ኒ⟩ | [ni] |  |
| ⟨ና⟩ | [na] |  |
| ⟨ኔ⟩ | [ne] |  |
| ⟨ን⟩ | [n] |  |
| ⟨ኖ⟩ | [no] |  |
| ⟨ኗ⟩ | [nʷa] |  |
| ⟨ኘ⟩ | [ɲə] |  |
| ⟨ኙ⟩ | [ɲu] |  |
| ⟨ኚ⟩ | [ɲi] |  |
| ⟨ኛ⟩ | [ɲa] |  |
| ⟨ኜ⟩ | [ɲe] |  |
| ⟨ኝ⟩ | [ɲ] |  |
| ⟨ኞ⟩ | [ɲo] |  |
| ⟨ኟ⟩ | [ɲʷa] |  |
| ⟨አ⟩ | [ʔə] |  |
| ⟨ኡ⟩ | [ʔu] |  |
| ⟨ኢ⟩ | [ʔi] |  |
| ⟨ኣ⟩ | [ʔa] |  |
| ⟨ኤ⟩ | [ʔe] |  |
| ⟨እ⟩ | [ɨ] |  |
| ⟨ኦ⟩ | [ʔo] |  |
| ⟨ከ⟩ | [kə] |  |
| ⟨ኩ⟩ | [ku] |  |
| ⟨ኪ⟩ | [ki] |  |
| ⟨ካ⟩ | [ka] |  |
| ⟨ኬ⟩ | [ke] |  |
| ⟨ክ⟩ | [k] |  |
| ⟨ኮ⟩ | [ko] |  |
| ⟨ኰ⟩ | [kʷə] |  |
| ⟨ኲ⟩ | [kʷi] |  |
| ⟨ኳ⟩ | [kʷa] |  |
| ⟨ኴ⟩ | [kʷe] |  |
| ⟨ኵ⟩ | [kʷ] |  |
| ⟨ኸ⟩ | [hə] |  |
| ⟨ኹ⟩ | [hu] |  |
| ⟨ኺ⟩ | [hi] |  |
| ⟨ኻ⟩ | [ha] |  |
| ⟨ኼ⟩ | [he] |  |
| ⟨ኽ⟩ | [h] |  |
| ⟨ኾ⟩ | [ho] |  |
| ⟨ዀ⟩ | [hʷə] |  |
| ⟨ዂ⟩ | [hʷi] |  |
| ⟨ዃ⟩ | [hʷa] |  |
| ⟨ዄ⟩ | [hʷe] |  |
| ⟨ዅ⟩ | [hʷ] |  |
| ⟨ወ⟩ | [wə] |  |
| ⟨ዉ⟩ | [wu] |  |
| ⟨ዊ⟩ | [wi] |  |
| ⟨ዋ⟩ | [wa] |  |
| ⟨ዌ⟩ | [we] |  |
| ⟨ው⟩ | [w] |  |
| ⟨ዎ⟩ | [wo] |  |
| ⟨ዐ⟩ | [ʔə] |  |
| ⟨ዑ⟩ | [ʔu] |  |
| ⟨ዒ⟩ | [ʔi] |  |
| ⟨ዓ⟩ | [ʔa] |  |
| ⟨ዔ⟩ | [ʔe] |  |
| ⟨ዕ⟩ | [ɨ] |  |
| ⟨ዖ⟩ | [ʔo] |  |
| ⟨ዘ⟩ | [zə] |  |
| ⟨ዙ⟩ | [zu] |  |
| ⟨ዚ⟩ | [zi] |  |
| ⟨ዛ⟩ | [za] |  |
| ⟨ዜ⟩ | [ze] |  |
| ⟨ዝ⟩ | [z] |  |
| ⟨ዞ⟩ | [zo] |  |
| ⟨ዟ⟩ | [zʷa] |  |
| ⟨ዠ⟩ | [ʒə] |  |
| ⟨ዡ⟩ | [ʒu] |  |
| ⟨ዢ⟩ | [ʒi] |  |
| ⟨ዣ⟩ | [ʒa] |  |
| ⟨ዤ⟩ | [ʒe] |  |
| ⟨ዥ⟩ | [ʒ] |  |
| ⟨ዦ⟩ | [ʒo] |  |
| ⟨ዧ⟩ | [ʒʷa] |  |
| ⟨የ⟩ | [jə] |  |
| ⟨ዩ⟩ | [ju] |  |
| ⟨ዪ⟩ | [ji] |  |
| ⟨ያ⟩ | [ja] |  |
| ⟨ዬ⟩ | [je] |  |
| ⟨ይ⟩ | [j] |  |
| ⟨ዮ⟩ | [jo] |  |
| ⟨ደ⟩ | [də] |  |
| ⟨ዱ⟩ | [du] |  |
| ⟨ዲ⟩ | [di] |  |
| ⟨ዳ⟩ | [da] |  |
| ⟨ዴ⟩ | [de] |  |
| ⟨ድ⟩ | [d] |  |
| ⟨ዶ⟩ | [do] |  |
| ⟨ዷ⟩ | [dʷa] |  |
| ⟨ጀ⟩ | [dʒə] |  |
| ⟨ጁ⟩ | [dʒu] |  |
| ⟨ጂ⟩ | [dʒi] |  |
| ⟨ጃ⟩ | [dʒa] |  |
| ⟨ጄ⟩ | [dʒe] |  |
| ⟨ጅ⟩ | [dʒ] |  |
| ⟨ጆ⟩ | [dʒo] |  |
| ⟨ጇ⟩ | [dʒʷa] |  |
| ⟨ገ⟩ | [ɡə] |  |
| ⟨ጉ⟩ | [ɡu] |  |
| ⟨ጊ⟩ | [ɡi] |  |
| ⟨ጋ⟩ | [ɡa] |  |
| ⟨ጌ⟩ | [ɡe] |  |
| ⟨ግ⟩ | [ɡ] |  |
| ⟨ጎ⟩ | [ɡo] |  |
| ⟨ጐ⟩ | [ɡʷə] |  |
| ⟨ጒ⟩ | [ɡʷi] |  |
| ⟨ጓ⟩ | [ɡʷa] |  |
| ⟨ጔ⟩ | [ɡʷe] |  |
| ⟨ጕ⟩ | [ɡʷ] |  |
| ⟨ጠ⟩ | [tʼə] |  |
| ⟨ጡ⟩ | [tʼu] |  |
| ⟨ጢ⟩ | [tʼi] |  |
| ⟨ጣ⟩ | [tʼa] |  |
| ⟨ጤ⟩ | [tʼe] |  |
| ⟨ጥ⟩ | [tʼ] |  |
| ⟨ጦ⟩ | [tʼo] |  |
| ⟨ጧ⟩ | [tʼʷa] |  |
| ⟨ጨ⟩ | [tʃʼə] |  |
| ⟨ጩ⟩ | [tʃʼu] |  |
| ⟨ጪ⟩ | [tʃʼi] |  |
| ⟨ጫ⟩ | [tʃʼa] |  |
| ⟨ጬ⟩ | [tʃʼe] |  |
| ⟨ጭ⟩ | [tʃʼ] |  |
| ⟨ጮ⟩ | [tʃʼo] |  |
| ⟨ጯ⟩ | [tʃʼʷa] |  |
| ⟨ጰ⟩ | [pʼə] |  |
| ⟨ጱ⟩ | [pʼu] |  |
| ⟨ጲ⟩ | [pʼi] |  |
| ⟨ጳ⟩ | [pʼa] |  |
| ⟨ጴ⟩ | [pʼe] |  |
| ⟨ጵ⟩ | [pʼ] |  |
| ⟨ጶ⟩ | [pʼo] |  |
| ⟨ጷ⟩ | [pʼʷa] |  |
| ⟨ጸ⟩ | [tsʼə] |  |
| ⟨ጹ⟩ | [tsʼu] |  |
| ⟨ጺ⟩ | [tsʼi] |  |
| ⟨ጻ⟩ | [tsʼa] |  |
| ⟨ጼ⟩ | [tsʼe] |  |
| ⟨ጽ⟩ | [tsʼ] |  |
| ⟨ጾ⟩ | [tsʼo] |  |
| ⟨ጿ⟩ | [tsʼʷa] |  |
| ⟨ፀ⟩ | [tsʼə] |  |
| ⟨ፁ⟩ | [tsʼu] |  |
| ⟨ፂ⟩ | [tsʼi] |  |
| ⟨ፃ⟩ | [tsʼa] |  |
| ⟨ፄ⟩ | [tsʼe] |  |
| ⟨ፅ⟩ | [tsʼ] |  |
| ⟨ፆ⟩ | [tsʼo] |  |
| ⟨ፈ⟩ | [fə] |  |
| ⟨ፉ⟩ | [fu] |  |
| ⟨ፊ⟩ | [fi] |  |
| ⟨ፋ⟩ | [fa] |  |
| ⟨ፌ⟩ | [fe] |  |
| ⟨ፍ⟩ | [f] |  |
| ⟨ፎ⟩ | [fo] |  |
| ⟨ፏ⟩ | [fʷa] |  |
| ⟨ፐ⟩ | [pə] |  |
| ⟨ፑ⟩ | [pu] |  |
| ⟨ፒ⟩ | [pi] |  |
| ⟨ፓ⟩ | [pa] |  |
| ⟨ፔ⟩ | [pe] |  |
| ⟨ፕ⟩ | [p] |  |
| ⟨ፖ⟩ | [po] |  |
| ⟨ፗ⟩ | [pʷa] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "am")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← American English](en-US.md) · [Home](../index.md) · [Amis →](ami.md)
