# Muong (`mtq`)

<!-- atlas:summary begin -->
Muong is an Austroasiatic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `mtq` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mtq` |
| ISO 639-3 | [mtq](https://iso639-3.sil.org/code/mtq), Muong |
| Wikipedia | [Mường language](https://en.wikipedia.org/wiki/M%C6%B0%E1%BB%9Dng_language) |
| Family | [Austroasiatic](by-family.md#austroasiatic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Austroasiatic](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1305) `x-clade-aust1305` |
| Explorer | [`mtq` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mtq) |
| Spec file | [`mtq.json`](../../orthography2ipa/data/mtq.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Austroasiatic (Vietic) language of northern Vietnam, written in a Vietnamese-based Latin orthography, the Hoa Binh provincial standard uses 28 letters plus tone diacritics. Consonant digraphs follow Vietnamese conventions (nh, ng/ngh, ch, ph, th, tr, gh), with d read /z/ and đ as the implosive.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1982 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 95 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mtq.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mtq` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mtq_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Muong (muon1246)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/muon1246)
2. <a id="src-mtq_wikipedia"></a>Wikipedia contributors (2024). *Muong language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/M%C6%B0%E1%BB%9Dng_language)
3. <a id="src-mtq_omniglot"></a>Ager, S. (2024). *Muong language and alphabet*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/muong.htm)
4. <a id="src-mtq_nguyenvantai"></a>Nguyễn Văn Tài (1982). *Ngữ âm tiếng Mường qua các phương ngôn*. Ủy ban Khoa học Xã hội Việt Nam.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mtq` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 194 | 0.3412 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t tʰ | ʈ | c | k |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z |  |  | ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u ɯ |
| Close-mid | e |  | o |
| Mid |  | ə əː |  |
| Open-mid | ɛ |  | ɔ |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w] [ɓ] [ɗ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [aː] |  |
| ⟨b⟩ | [ɓ] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [c] |  |
| ⟨d⟩ | [z] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨gh⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngh⟩ | [ŋ] |  |
| ⟨nh⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨tr⟩ | [ʈ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [s] |  |
| ⟨y⟩ | [j] |  |
| ⟨à⟩ | [aː] |  |
| ⟨á⟩ | [aː] |  |
| ⟨â⟩ | [ə] |  |
| ⟨ã⟩ | [aː] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [ɛ] |  |
| ⟨ê⟩ | [e] |  |
| ⟨ì⟩ | [i] |  |
| ⟨í⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [ɔ] |  |
| ⟨ô⟩ | [o] |  |
| ⟨õ⟩ | [ɔ] |  |
| ⟨ù⟩ | [u] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ý⟩ | [j] |  |
| ⟨ă⟩ | [a] |  |
| ⟨đ⟩ | [ɗ] |  |
| ⟨ĩ⟩ | [i] |  |
| ⟨ũ⟩ | [u] |  |
| ⟨ơ⟩ | [əː] |  |
| ⟨ư⟩ | [ɯ] |  |
| ⟨ạ⟩ | [aː] |  |
| ⟨ả⟩ | [aː] |  |
| ⟨ấ⟩ | [ə] |  |
| ⟨ầ⟩ | [ə] |  |
| ⟨ẩ⟩ | [ə] |  |
| ⟨ẫ⟩ | [ə] |  |
| ⟨ậ⟩ | [ə] |  |
| ⟨ắ⟩ | [a] |  |
| ⟨ằ⟩ | [a] |  |
| ⟨ẳ⟩ | [a] |  |
| ⟨ẵ⟩ | [a] |  |
| ⟨ặ⟩ | [a] |  |
| ⟨ẹ⟩ | [ɛ] |  |
| ⟨ẻ⟩ | [ɛ] |  |
| ⟨ẽ⟩ | [ɛ] |  |
| ⟨ế⟩ | [e] |  |
| ⟨ề⟩ | [e] |  |
| ⟨ể⟩ | [e] |  |
| ⟨ễ⟩ | [e] |  |
| ⟨ệ⟩ | [e] |  |
| ⟨ỉ⟩ | [i] |  |
| ⟨ị⟩ | [i] |  |
| ⟨ọ⟩ | [ɔ] |  |
| ⟨ỏ⟩ | [ɔ] |  |
| ⟨ố⟩ | [o] |  |
| ⟨ồ⟩ | [o] |  |
| ⟨ổ⟩ | [o] |  |
| ⟨ỗ⟩ | [o] |  |
| ⟨ộ⟩ | [o] |  |
| ⟨ớ⟩ | [əː] |  |
| ⟨ờ⟩ | [əː] |  |
| ⟨ở⟩ | [əː] |  |
| ⟨ỡ⟩ | [əː] |  |
| ⟨ợ⟩ | [əː] |  |
| ⟨ụ⟩ | [u] |  |
| ⟨ủ⟩ | [u] |  |
| ⟨ứ⟩ | [ɯ] |  |
| ⟨ừ⟩ | [ɯ] |  |
| ⟨ử⟩ | [ɯ] |  |
| ⟨ữ⟩ | [ɯ] |  |
| ⟨ự⟩ | [ɯ] |  |
| ⟨ỳ⟩ | [j] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mtq")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mundari](unr.md) · [Home](../index.md) · [Murcian Spanish →](es-ES-x-murcia.md)
