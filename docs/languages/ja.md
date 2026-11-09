# Japanese (`ja`)

<!-- atlas:summary begin -->
Japanese is a Japonic language, written in the Kana script. Glottolog places it in Japan. The `ja` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ja` |
| Aliases | `jpn` |
| ISO 639-3 | [jpn](https://iso639-3.sil.org/code/jpn), Japanese |
| Glottolog | [nucl1643](https://glottolog.org/resource/languoid/id/nucl1643), Japanese |
| Wikidata | [Q5287](https://www.wikidata.org/wiki/Q5287) |
| Wikipedia | [Japanese language](https://en.wikipedia.org/wiki/Japanese_language) |
| Family | [Japonic](by-family.md#japonic) |
| Region | [Eurasia](by-region.md#eurasia) > [Japan](by-region.md#japan) |
| Script | [Kana](by-script.md#kana) (syllabary) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 800, living |
| Parent | [Proto-Japonic (family node)](https://tigregotico.github.io/orthography2ipa/#jpx) `jpx` |
| Explorer | [`ja` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ja) |
| Spec file | [`ja.json`](../../orthography2ipa/data/ja.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Tokyo Japanese. Moraic structure: each kana = one mora. The moraic nasal /N/ and the moraic obstruent /Q/ are placeless archiphonemes realised by allophone_rules from the following segment.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1987 to 2012. [Sources](#sources) lists them. The spec file writes all 305 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ja.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ja` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-vance1987"></a>Vance, T.J. (1987). *An Introduction to Japanese Phonology*. SUNY Press.
2. <a id="src-vance2008"></a>Vance, T.J. (2008). *The Sounds of Japanese*. Cambridge University Press.
3. <a id="src-labrune2012"></a>Labrune, L. (2012). *The Phonology of Japanese*. Oxford University Press.
4. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `ja` | gold | lexicon-derived | MIT, each file its own | 115500 | 0.3276 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ja` | generated | epitran-derived | CC0 1.0 | 42550 | 0.4273 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 179 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d t |  | k kʲ ɡ ɡʲ |  | ʔ |
| Affricate |  |  | dz ts | dʑ tɕ |  |  |  |
| Nasal | m |  | n | ɲ | ŋ | ɴ |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative | ɸ β̞ | v | s z | ç ɕ ʑ |  |  | h ɦ |
| Approximant |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | ɯ ɯ̃ ɯ̥ |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [N] [Q] [ba] [be] [bi] [bo] [bɯ] [bʲa] [bʲo] [bʲɯ] [da] [de] [di] [do] [dzɯ] [dɯ] [dʑa] [dʑe] [dʑi] [dʑo] [dʑɯ] [dʲɯ] [ha] [he] [ho] [ja] [je] [jo] [jɯ] [ka] [ke] [ki] [ko] [kwa] [kwe] [kwi] [kwo] [kɯ] [kʲa] [kʲo], and 99 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ぁ⟩ | [a] |  |
| ⟨あ⟩ | [a] |  |
| ⟨ぃ⟩ | [i] |  |
| ⟨い⟩ | [i] |  |
| ⟨いぇ⟩ | [je] |  |
| ⟨ぅ⟩ | [ɯ] |  |
| ⟨う⟩ | [ɯ] |  |
| ⟨うぃ⟩ | [wi] |  |
| ⟨うぇ⟩ | [we] |  |
| ⟨うぉ⟩ | [wo] |  |
| ⟨ぇ⟩ | [e] |  |
| ⟨え⟩ | [e] |  |
| ⟨ぉ⟩ | [o] |  |
| ⟨お⟩ | [o] |  |
| ⟨か⟩ | [ka] |  |
| ⟨が⟩ | [ɡa] |  |
| ⟨き⟩ | [ki] |  |
| ⟨きゃ⟩ | [kʲa] |  |
| ⟨きゅ⟩ | [kʲɯ] |  |
| ⟨きょ⟩ | [kʲo] |  |
| ⟨ぎ⟩ | [ɡi] |  |
| ⟨ぎゃ⟩ | [ɡʲa] |  |
| ⟨ぎゅ⟩ | [ɡʲɯ] |  |
| ⟨ぎょ⟩ | [ɡʲo] |  |
| ⟨く⟩ | [kɯ] |  |
| ⟨くぁ⟩ | [kwa] |  |
| ⟨くぃ⟩ | [kwi] |  |
| ⟨くぇ⟩ | [kwe] |  |
| ⟨くぉ⟩ | [kwo] |  |
| ⟨ぐ⟩ | [ɡɯ] |  |
| ⟨ぐぁ⟩ | [ɡwa] |  |
| ⟨ぐぃ⟩ | [ɡwi] |  |
| ⟨ぐぇ⟩ | [ɡwe] |  |
| ⟨ぐぉ⟩ | [ɡwo] |  |
| ⟨け⟩ | [ke] |  |
| ⟨げ⟩ | [ɡe] |  |
| ⟨こ⟩ | [ko] |  |
| ⟨ご⟩ | [ɡo] |  |
| ⟨さ⟩ | [sa] |  |
| ⟨ざ⟩ | [za] |  |
| ⟨し⟩ | [ɕi] |  |
| ⟨しぇ⟩ | [ɕe] |  |
| ⟨しゃ⟩ | [ɕa] |  |
| ⟨しゅ⟩ | [ɕɯ] |  |
| ⟨しょ⟩ | [ɕo] |  |
| ⟨じ⟩ | [dʑi] |  |
| ⟨じぇ⟩ | [dʑe] |  |
| ⟨じゃ⟩ | [dʑa] |  |
| ⟨じゅ⟩ | [dʑɯ] |  |
| ⟨じょ⟩ | [dʑo] |  |
| ⟨す⟩ | [sɯ] |  |
| ⟨すぃ⟩ | [si] |  |
| ⟨ず⟩ | [zɯ] |  |
| ⟨ずぃ⟩ | [zi] |  |
| ⟨せ⟩ | [se] |  |
| ⟨ぜ⟩ | [ze] |  |
| ⟨そ⟩ | [so] |  |
| ⟨ぞ⟩ | [zo] |  |
| ⟨た⟩ | [ta] |  |
| ⟨だ⟩ | [da] |  |
| ⟨ち⟩ | [tɕi] |  |
| ⟨ちぇ⟩ | [tɕe] |  |
| ⟨ちゃ⟩ | [tɕa] |  |
| ⟨ちゅ⟩ | [tɕɯ] |  |
| ⟨ちょ⟩ | [tɕo] |  |
| ⟨ぢ⟩ | [dʑi] |  |
| ⟨ぢゃ⟩ | [dʑa] |  |
| ⟨ぢゅ⟩ | [dʑɯ] |  |
| ⟨ぢょ⟩ | [dʑo] |  |
| ⟨っ⟩ | [Q] |  |
| ⟨つ⟩ | [tsɯ] |  |
| ⟨つぁ⟩ | [tsa] |  |
| ⟨つぃ⟩ | [tsi] |  |
| ⟨つぇ⟩ | [tse] |  |
| ⟨つぉ⟩ | [tso] |  |
| ⟨づ⟩ | [dzɯ] |  |
| ⟨て⟩ | [te] |  |
| ⟨てぃ⟩ | [ti] |  |
| ⟨てゅ⟩ | [tʲɯ] |  |
| ⟨で⟩ | [de] |  |
| ⟨でぃ⟩ | [di] |  |
| ⟨でゅ⟩ | [dʲɯ] |  |
| ⟨と⟩ | [to] |  |
| ⟨とぅ⟩ | [tɯ] |  |
| ⟨ど⟩ | [do] |  |
| ⟨どぅ⟩ | [dɯ] |  |
| ⟨な⟩ | [na] |  |
| ⟨に⟩ | [ɲi] |  |
| ⟨にゃ⟩ | [ɲa] |  |
| ⟨にゅ⟩ | [ɲɯ] |  |
| ⟨にょ⟩ | [ɲo] |  |
| ⟨ぬ⟩ | [nɯ] |  |
| ⟨ね⟩ | [ne] |  |
| ⟨の⟩ | [no] |  |
| ⟨は⟩ | [ha] |  |
| ⟨ば⟩ | [ba] |  |
| ⟨ぱ⟩ | [pa] |  |
| ⟨ひ⟩ | [çi] |  |
| ⟨ひゃ⟩ | [ça] |  |
| ⟨ひゅ⟩ | [çɯ] |  |
| ⟨ひょ⟩ | [ço] |  |
| ⟨び⟩ | [bi] |  |
| ⟨びゃ⟩ | [bʲa] |  |
| ⟨びゅ⟩ | [bʲɯ] |  |
| ⟨びょ⟩ | [bʲo] |  |
| ⟨ぴ⟩ | [pi] |  |
| ⟨ぴゃ⟩ | [pʲa] |  |
| ⟨ぴゅ⟩ | [pʲɯ] |  |
| ⟨ぴょ⟩ | [pʲo] |  |
| ⟨ふ⟩ | [ɸɯ] |  |
| ⟨ふぁ⟩ | [ɸa] |  |
| ⟨ふぃ⟩ | [ɸi] |  |
| ⟨ふぇ⟩ | [ɸe] |  |
| ⟨ふぉ⟩ | [ɸo] |  |
| ⟨ふゅ⟩ | [ɸʲɯ] |  |
| ⟨ぶ⟩ | [bɯ] |  |
| ⟨ぷ⟩ | [pɯ] |  |
| ⟨へ⟩ | [he] |  |
| ⟨べ⟩ | [be] |  |
| ⟨ぺ⟩ | [pe] |  |
| ⟨ほ⟩ | [ho] |  |
| ⟨ぼ⟩ | [bo] |  |
| ⟨ぽ⟩ | [po] |  |
| ⟨ま⟩ | [ma] |  |
| ⟨み⟩ | [mi] |  |
| ⟨みゃ⟩ | [mʲa] |  |
| ⟨みゅ⟩ | [mʲɯ] |  |
| ⟨みょ⟩ | [mʲo] |  |
| ⟨む⟩ | [mɯ] |  |
| ⟨め⟩ | [me] |  |
| ⟨も⟩ | [mo] |  |
| ⟨や⟩ | [ja] |  |
| ⟨ゆ⟩ | [jɯ] |  |
| ⟨よ⟩ | [jo] |  |
| ⟨ら⟩ | [ɾa] |  |
| ⟨り⟩ | [ɾi] |  |
| ⟨りゃ⟩ | [ɾʲa] |  |
| ⟨りゅ⟩ | [ɾʲɯ] |  |
| ⟨りょ⟩ | [ɾʲo] |  |
| ⟨る⟩ | [ɾɯ] |  |
| ⟨れ⟩ | [ɾe] |  |
| ⟨ろ⟩ | [ɾo] |  |
| ⟨ゎ⟩ | [wa] |  |
| ⟨わ⟩ | [wa] |  |
| ⟨ゐ⟩ | [i] |  |
| ⟨ゑ⟩ | [e] |  |
| ⟨を⟩ | [o] |  |
| ⟨ん⟩ | [N] |  |
| ⟨ゔ⟩ | [vɯ] |  |
| ⟨ァ⟩ | [a] |  |
| ⟨ア⟩ | [a] |  |
| ⟨ィ⟩ | [i] |  |
| ⟨イ⟩ | [i] |  |
| ⟨イェ⟩ | [je] |  |
| ⟨ゥ⟩ | [ɯ] |  |
| ⟨ウ⟩ | [ɯ] |  |
| ⟨ウィ⟩ | [wi] |  |
| ⟨ウェ⟩ | [we] |  |
| ⟨ウォ⟩ | [wo] |  |
| ⟨ェ⟩ | [e] |  |
| ⟨エ⟩ | [e] |  |
| ⟨ォ⟩ | [o] |  |
| ⟨オ⟩ | [o] |  |
| ⟨カ⟩ | [ka] |  |
| ⟨ガ⟩ | [ɡa] |  |
| ⟨キ⟩ | [ki] |  |
| ⟨キャ⟩ | [kʲa] |  |
| ⟨キュ⟩ | [kʲɯ] |  |
| ⟨キョ⟩ | [kʲo] |  |
| ⟨ギ⟩ | [ɡi] |  |
| ⟨ギャ⟩ | [ɡʲa] |  |
| ⟨ギュ⟩ | [ɡʲɯ] |  |
| ⟨ギョ⟩ | [ɡʲo] |  |
| ⟨ク⟩ | [kɯ] |  |
| ⟨クァ⟩ | [kwa] |  |
| ⟨クィ⟩ | [kwi] |  |
| ⟨クェ⟩ | [kwe] |  |
| ⟨クォ⟩ | [kwo] |  |
| ⟨グ⟩ | [ɡɯ] |  |
| ⟨グァ⟩ | [ɡwa] |  |
| ⟨グィ⟩ | [ɡwi] |  |
| ⟨グェ⟩ | [ɡwe] |  |
| ⟨グォ⟩ | [ɡwo] |  |
| ⟨ケ⟩ | [ke] |  |
| ⟨ゲ⟩ | [ɡe] |  |
| ⟨コ⟩ | [ko] |  |
| ⟨ゴ⟩ | [ɡo] |  |
| ⟨サ⟩ | [sa] |  |
| ⟨ザ⟩ | [za] |  |
| ⟨シ⟩ | [ɕi] |  |
| ⟨シェ⟩ | [ɕe] |  |
| ⟨シャ⟩ | [ɕa] |  |
| ⟨シュ⟩ | [ɕɯ] |  |
| ⟨ショ⟩ | [ɕo] |  |
| ⟨ジ⟩ | [dʑi] |  |
| ⟨ジェ⟩ | [dʑe] |  |
| ⟨ジャ⟩ | [dʑa] |  |
| ⟨ジュ⟩ | [dʑɯ] |  |
| ⟨ジョ⟩ | [dʑo] |  |
| ⟨ス⟩ | [sɯ] |  |
| ⟨スィ⟩ | [si] |  |
| ⟨ズ⟩ | [zɯ] |  |
| ⟨ズィ⟩ | [zi] |  |
| ⟨セ⟩ | [se] |  |
| ⟨ゼ⟩ | [ze] |  |
| ⟨ソ⟩ | [so] |  |
| ⟨ゾ⟩ | [zo] |  |
| ⟨タ⟩ | [ta] |  |
| ⟨ダ⟩ | [da] |  |
| ⟨チ⟩ | [tɕi] |  |
| ⟨チェ⟩ | [tɕe] |  |
| ⟨チャ⟩ | [tɕa] |  |
| ⟨チュ⟩ | [tɕɯ] |  |
| ⟨チョ⟩ | [tɕo] |  |
| ⟨ヂ⟩ | [dʑi] |  |
| ⟨ヂャ⟩ | [dʑa] |  |
| ⟨ヂュ⟩ | [dʑɯ] |  |
| ⟨ヂョ⟩ | [dʑo] |  |
| ⟨ッ⟩ | [Q] |  |
| ⟨ツ⟩ | [tsɯ] |  |
| ⟨ツァ⟩ | [tsa] |  |
| ⟨ツィ⟩ | [tsi] |  |
| ⟨ツェ⟩ | [tse] |  |
| ⟨ツォ⟩ | [tso] |  |
| ⟨ヅ⟩ | [dzɯ] |  |
| ⟨テ⟩ | [te] |  |
| ⟨ティ⟩ | [ti] |  |
| ⟨テュ⟩ | [tʲɯ] |  |
| ⟨デ⟩ | [de] |  |
| ⟨ディ⟩ | [di] |  |
| ⟨デュ⟩ | [dʲɯ] |  |
| ⟨ト⟩ | [to] |  |
| ⟨トゥ⟩ | [tɯ] |  |
| ⟨ド⟩ | [do] |  |
| ⟨ドゥ⟩ | [dɯ] |  |
| ⟨ナ⟩ | [na] |  |
| ⟨ニ⟩ | [ɲi] |  |
| ⟨ニャ⟩ | [ɲa] |  |
| ⟨ニュ⟩ | [ɲɯ] |  |
| ⟨ニョ⟩ | [ɲo] |  |
| ⟨ヌ⟩ | [nɯ] |  |
| ⟨ネ⟩ | [ne] |  |
| ⟨ノ⟩ | [no] |  |
| ⟨ハ⟩ | [ha] |  |
| ⟨バ⟩ | [ba] |  |
| ⟨パ⟩ | [pa] |  |
| ⟨ヒ⟩ | [çi] |  |
| ⟨ヒャ⟩ | [ça] |  |
| ⟨ヒュ⟩ | [çɯ] |  |
| ⟨ヒョ⟩ | [ço] |  |
| ⟨ビ⟩ | [bi] |  |
| ⟨ビャ⟩ | [bʲa] |  |
| ⟨ビュ⟩ | [bʲɯ] |  |
| ⟨ビョ⟩ | [bʲo] |  |
| ⟨ピ⟩ | [pi] |  |
| ⟨ピャ⟩ | [pʲa] |  |
| ⟨ピュ⟩ | [pʲɯ] |  |
| ⟨ピョ⟩ | [pʲo] |  |
| ⟨フ⟩ | [ɸɯ] |  |
| ⟨ファ⟩ | [ɸa] |  |
| ⟨フィ⟩ | [ɸi] |  |
| ⟨フェ⟩ | [ɸe] |  |
| ⟨フォ⟩ | [ɸo] |  |
| ⟨フュ⟩ | [ɸʲɯ] |  |
| ⟨ブ⟩ | [bɯ] |  |
| ⟨プ⟩ | [pɯ] |  |
| ⟨ヘ⟩ | [he] |  |
| ⟨ベ⟩ | [be] |  |
| ⟨ペ⟩ | [pe] |  |
| ⟨ホ⟩ | [ho] |  |
| ⟨ボ⟩ | [bo] |  |
| ⟨ポ⟩ | [po] |  |
| ⟨マ⟩ | [ma] |  |
| ⟨ミ⟩ | [mi] |  |
| ⟨ミャ⟩ | [mʲa] |  |
| ⟨ミュ⟩ | [mʲɯ] |  |
| ⟨ミョ⟩ | [mʲo] |  |
| ⟨ム⟩ | [mɯ] |  |
| ⟨メ⟩ | [me] |  |
| ⟨モ⟩ | [mo] |  |
| ⟨ヤ⟩ | [ja] |  |
| ⟨ユ⟩ | [jɯ] |  |
| ⟨ヨ⟩ | [jo] |  |
| ⟨ラ⟩ | [ɾa] |  |
| ⟨リ⟩ | [ɾi] |  |
| ⟨リャ⟩ | [ɾʲa] |  |
| ⟨リュ⟩ | [ɾʲɯ] |  |
| ⟨リョ⟩ | [ɾʲo] |  |
| ⟨ル⟩ | [ɾɯ] |  |
| ⟨レ⟩ | [ɾe] |  |
| ⟨ロ⟩ | [ɾo] |  |
| ⟨ヮ⟩ | [wa] |  |
| ⟨ワ⟩ | [wa] |  |
| ⟨ヰ⟩ | [i] |  |
| ⟨ヱ⟩ | [e] |  |
| ⟨ヲ⟩ | [o] |  |
| ⟨ン⟩ | [N] |  |
| ⟨ヴ⟩ | [vɯ] |  |
| ⟨ヴァ⟩ | [va] |  |
| ⟨ヴィ⟩ | [vi] |  |
| ⟨ヴェ⟩ | [ve] |  |
| ⟨ヴォ⟩ | [vo] |  |
| ⟨ヴュ⟩ | [vʲɯ] |  |
| ⟨ヷ⟩ | [va] |  |
| ⟨ー⟩ | [ː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 26 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `JA_Q_GEMINATE_K` | /Q/ → [k], before [k] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_KY` | /Q/ → [kʲ], before [kʲ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_G` | /Q/ → [ɡ], before [ɡ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_GY` | /Q/ → [ɡʲ], before [ɡʲ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_P` | /Q/ → [p], before [p] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_PY` | /Q/ → [pʲ], before [pʲ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_B` | /Q/ → [b], before [b] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_BY` | /Q/ → [bʲ], before [bʲ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_T` | /Q/ → [t], before [t] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_D` | /Q/ → [d], before [d] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_S` | /Q/ → [s], before [s] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_Z` | /Q/ → [z], before [z] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_SH` | /Q/ → [ɕ], before [ɕ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_ZH` | /Q/ → [ʑ], before [ʑ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_F` | /Q/ → [ɸ], before [ɸ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_HY` | /Q/ → [ç], before [ç] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_H` | /Q/ → [h], before [h] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_V` | /Q/ → [v], before [v] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_VOICELESS_AFFRICATE` | /Q/ → [t], before [ts] [tɕ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GEMINATE_VOICED_AFFRICATE` | /Q/ → [d], before [dz] [dʑ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_Q_GLOTTAL_DEFAULT` | /Q/ → [ʔ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_N_ASSIMILATE_LABIAL` | /N/ → [m], before [p] [pʲ] [b] [bʲ] [m] [mʲ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_N_ASSIMILATE_CORONAL` | /N/ → [n], before [t] [d] [n] [ts] [dz] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_N_ASSIMILATE_PALATAL` | /N/ → [ɲ], before [tɕ] [dʑ] [ɲ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_N_ASSIMILATE_VELAR` | /N/ → [ŋ], before [k] [kʲ] [ɡ] [ɡʲ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
| `JA_N_UVULAR_DEFAULT` | /N/ → [ɴ] | - | [Vance 2008](#src-vance2008), [Labrune 2012](#src-labrune2012) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ja")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Jamaican Patois](jam.md) · [Home](../index.md) · [Jingpho →](kac.md)
