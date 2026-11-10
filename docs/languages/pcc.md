# Bouyei (`pcc`)

<!-- atlas:summary begin -->
Bouyei is a Tai-Kadai language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `pcc` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pcc` |
| ISO 639-3 | [pcc](https://iso639-3.sil.org/code/pcc), Bouyei |
| Wikipedia | [Bouyei language](https://en.wikipedia.org/wiki/Bouyei_language) |
| Family | [Tai-Kadai](by-family.md#tai-kadai) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Tai-Kadai](https://tigregotico.github.io/orthography2ipa/#x-clade-taik1256) `x-clade-taik1256` |
| Explorer | [`pcc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pcc) |
| Spec file | [`pcc.json`](../../orthography2ipa/data/pcc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Bouyei (Haausqyaix), a Northern Tai language of Guizhou, in the official Latin orthography adopted in 1985 and based on the speech of Fuxing, Wangmo County. TONE LETTERS: as in the cognate Zhuang scheme, a syllable-final consonant letter spells the TONE, not a segment.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 2007 to 2024. [Sources](#sources) lists them. The spec file writes all 114 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pcc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pcc` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-pcc_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Bouyei (bouy1240)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/bouy1240)
2. <a id="src-pcc_omniglot"></a>Siegel, W. (compiler), Ager, S. (ed.) (2024). *Bouyei language and alphabet*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/bouyei.htm)
3. <a id="src-pcc_snyder2008"></a>Snyder, Wil (2008). *Bouyei Phonology*. in The Tai-Kadai Languages (Diller, Edmondson & Luo, eds.), Routledge.
4. <a id="src-pcc_wu2007"></a>Snyder, Wil, Wu Wenyi, Liang Yongshu (2007). *Survey of the Guizhou Bouyei Language*. SIL International (SIL Language and Culture Documentation and Description 2007-001). Cited: 326-329. [sil.org](https://www.sil.org/system/files/reapdata/15/19/67/151967442069318851440064774330425756098/49147_Wu_Survey_of_Bouyei.pdf)
5. <a id="src-pcc_unicode_l2_19201"></a>Wang, Yifan (2019). *Proposal to correct LATIN SMALL LETTER TONE SIX (U+0185) (L2/19-201)*. Unicode Technical Committee document register. Cited: 1. [unicode.org](https://www.unicode.org/L2/L2019/19201-correct-tone-six.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `pcc` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 153 | 0.0038 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 224 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ pʲ |  | t tʰ |  | k kʰ kʷ |
| Affricate |  |  | ts tsʰ | tɕ tɕʰ |  |
| Nasal | m mʲ |  | n | ɲ | ŋ ŋʷ |
| Fricative |  | f v | s z | ɕ | x ɣ |
| Lateral fricative |  |  | ɬ |  |  |
| Approximant |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u ɯ |
| Close-mid | e | o |
| Open | a aː |  |

Sequences that the spec writes as one unit: [aːi] [aːm] [aːn] [aːp̚] [aːp̚˧] [aːt̚] [aːt̚˧] [aːu] [aːŋ] [eːk̚] [eːk̚˧] [eːm] [eːn] [eːp̚] [eːp̚˧] [eːt̚] [eːt̚˧] [eːu] [eːŋ] [ik̚] [ik̚˧] [im] [in] [ip̚] [ip̚˧] [it̚] [it̚˧] [iu] [iŋ] [iə] [iəm] [iən] [iəp̚] [iəp̚˧] [iət̚] [iət̚˧] [iəŋ] [oːi] [oːm] [oːn], and 149 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | default [a] · word initial [ʔa] |
| ⟨aa⟩ | [aː] | default [aː] · word initial [ʔaː] |
| ⟨aab⟩ | [aːp̚] | default [aːp̚] · word final [aːp̚˧] · word initial [ʔaːp̚] |
| ⟨aad⟩ | [aːt̚] | default [aːt̚] · word final [aːt̚˧] · word initial [ʔaːt̚] |
| ⟨aai⟩ | [aːi] | default [aːi] · word initial [ʔaːi] |
| ⟨aam⟩ | [aːm] | default [aːm] · word initial [ʔaːm] |
| ⟨aan⟩ | [aːn] | default [aːn] · word initial [ʔaːn] |
| ⟨aang⟩ | [aːŋ] | default [aːŋ] · word initial [ʔaːŋ] |
| ⟨aau⟩ | [aːu] | default [aːu] · word initial [ʔaːu] |
| ⟨ab⟩ | [ɐp̚] | default [ɐp̚] · word final [ɐp̚˧] · word initial [ʔɐp̚] |
| ⟨ad⟩ | [ɐt̚] | default [ɐt̚] · word final [ɐt̚˧] · word initial [ʔɐt̚] |
| ⟨ae⟩ | [ɐɯ] | default [ɐɯ] · word initial [ʔɐɯ] |
| ⟨ag⟩ | [ɐk̚] | default [ɐk̚] · word final [ɐk̚˧] · word initial [ʔɐk̚] |
| ⟨ai⟩ | [ɐi] | default [ɐi] · word initial [ʔɐi] |
| ⟨am⟩ | [ɐm] | default [ɐm] · word initial [ʔɐm] |
| ⟨an⟩ | [ɐn] | default [ɐn] · word initial [ʔɐn] |
| ⟨ang⟩ | [ɐŋ] | default [ɐŋ] · word initial [ʔɐŋ] |
| ⟨ao⟩ | [aːu] | default [aːu] · word initial [ʔaːu] |
| ⟨au⟩ | [ɐu] | default [ɐu] · word initial [ʔɐu] |
| ⟨b⟩ | [p] |  |
| ⟨by⟩ | [pʲ] |  |
| ⟨c⟩ | [tsʰ] | before consonant [˥˧] · default [tsʰ] · word final [˥˧] |
| ⟨d⟩ | [t] |  |
| ⟨e⟩ | [ɯ] | default [ɯ] · word initial [ʔɯ] |
| ⟨ea⟩ | [ɯə] | default [ɯə] · word initial [ʔɯə] |
| ⟨eab⟩ | [ɯəp̚] | default [ɯəp̚] · word final [ɯəp̚˧] · word initial [ʔɯəp̚] |
| ⟨ead⟩ | [ɯət̚] | default [ɯət̚] · word final [ɯət̚˧] · word initial [ʔɯət̚] |
| ⟨eam⟩ | [ɯəm] | default [ɯəm] · word initial [ʔɯəm] |
| ⟨eang⟩ | [ɯəŋ] | default [ɯəŋ] · word initial [ʔɯəŋ] |
| ⟨ed⟩ | [ɯt̚] | default [ɯt̚] · word final [ɯt̚˧] · word initial [ʔɯt̚] |
| ⟨ee⟩ | [e] | default [e] · word initial [ʔe] |
| ⟨eeb⟩ | [eːp̚] | default [eːp̚] · word final [eːp̚˧] · word initial [ʔeːp̚] |
| ⟨eed⟩ | [eːt̚] | default [eːt̚] · word final [eːt̚˧] · word initial [ʔeːt̚] |
| ⟨eeg⟩ | [eːk̚] | default [eːk̚] · word final [eːk̚˧] · word initial [ʔeːk̚] |
| ⟨eem⟩ | [eːm] | default [eːm] · word initial [ʔeːm] |
| ⟨een⟩ | [eːn] | default [eːn] · word initial [ʔeːn] |
| ⟨eeng⟩ | [eːŋ] | default [eːŋ] · word initial [ʔeːŋ] |
| ⟨eeu⟩ | [eːu] | default [eːu] · word initial [ʔeːu] |
| ⟨eg⟩ | [ɯk̚] | default [ɯk̚] · word final [ɯk̚˧] · word initial [ʔɯk̚] |
| ⟨ei⟩ | [ɯi] | default [ɯi] · word initial [ʔɯi] |
| ⟨en⟩ | [ɯn] | default [ɯn] · word initial [ʔɯn] |
| ⟨eng⟩ | [ɯŋ] | default [ɯŋ] · word initial [ʔɯŋ] |
| ⟨f⟩ | [f] | before consonant [˧˩] · default [f] · word final [˧˩] |
| ⟨g⟩ | [k] |  |
| ⟨gv⟩ | [kʷ] |  |
| ⟨h⟩ | [x] | before consonant [˧] · default [x] · word final [˧] |
| ⟨hr⟩ | [ɣ] |  |
| ⟨i⟩ | [i] | default [i] · word initial [ʔi] |
| ⟨iab⟩ | [iəp̚] | default [iəp̚] · word final [iəp̚˧] · word initial [ʔiəp̚] |
| ⟨iad⟩ | [iət̚] | default [iət̚] · word final [iət̚˧] · word initial [ʔiət̚] |
| ⟨iam⟩ | [iəm] | default [iəm] · word initial [ʔiəm] |
| ⟨ian⟩ | [iən] | default [iən] · word initial [ʔiən] |
| ⟨iang⟩ | [iəŋ] | default [iəŋ] · word initial [ʔiəŋ] |
| ⟨ib⟩ | [ip̚] | default [ip̚] · word final [ip̚˧] · word initial [ʔip̚] |
| ⟨id⟩ | [it̚] | default [it̚] · word final [it̚˧] · word initial [ʔit̚] |
| ⟨ie⟩ | [iə] | default [iə] · word initial [ʔiə] |
| ⟨ig⟩ | [ik̚] | default [ik̚] · word final [ik̚˧] · word initial [ʔik̚] |
| ⟨im⟩ | [im] | default [im] · word initial [ʔim] |
| ⟨in⟩ | [in] | default [in] · word initial [ʔin] |
| ⟨ing⟩ | [iŋ] | default [iŋ] · word initial [ʔiŋ] |
| ⟨iu⟩ | [iu] | default [iu] · word initial [ʔiu] |
| ⟨j⟩ | [tɕ] | before consonant [˥˧] · default [tɕ] · word final [˥˧] |
| ⟨k⟩ | [kʰ] |  |
| ⟨l⟩ | [l] | before consonant [˨˦] · default [l] · word final [˨˦] |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ɓ] |  |
| ⟨my⟩ | [mʲ] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ɗ] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngv⟩ | [ŋʷ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] | default [o] · word initial [ʔo] |
| ⟨ob⟩ | [ɔp̚] | default [ɔp̚] · word final [ɔp̚˧] · word initial [ʔɔp̚] |
| ⟨od⟩ | [ɔt̚] | default [ɔt̚] · word final [ɔt̚˧] · word initial [ʔɔt̚] |
| ⟨og⟩ | [ɔk̚] | default [ɔk̚] · word final [ɔk̚˧] · word initial [ʔɔk̚] |
| ⟨oi⟩ | [oːi] | default [oːi] · word initial [ʔoːi] |
| ⟨om⟩ | [ɔm] | default [ɔm] · word initial [ʔɔm] |
| ⟨on⟩ | [ɔn] | default [ɔn] · word initial [ʔɔn] |
| ⟨ong⟩ | [ɔŋ] | default [ɔŋ] · word initial [ʔɔŋ] |
| ⟨oo⟩ | [o] | default [o] · word initial [ʔo] |
| ⟨oob⟩ | [oːp̚] | default [oːp̚] · word final [oːp̚˧] · word initial [ʔoːp̚] |
| ⟨ood⟩ | [oːt̚] | default [oːt̚] · word final [oːt̚˧] · word initial [ʔoːt̚] |
| ⟨oom⟩ | [oːm] | default [oːm] · word initial [ʔoːm] |
| ⟨oon⟩ | [oːn] | default [oːn] · word initial [ʔoːn] |
| ⟨oong⟩ | [oːŋ] | default [oːŋ] · word initial [ʔoːŋ] |
| ⟨ou⟩ | [əu] | default [əu] · word initial [ʔəu] |
| ⟨p⟩ | [pʰ] |  |
| ⟨q⟩ | [tɕʰ] | before consonant [˨˦] · default [tɕʰ] · word final [˨˦] |
| ⟨qv⟩ | [ʔv] |  |
| ⟨qy⟩ | [ʔj] |  |
| ⟨r⟩ | [z] |  |
| ⟨s⟩ | [s] | before consonant [˧˥] · default [s] · word final [˧˥] |
| ⟨sl⟩ | [ɬ] |  |
| ⟨t⟩ | [tʰ] | before consonant [˧˥] · default [tʰ] · word final [˧˥] |
| ⟨u⟩ | [u] | default [u] · word initial [ʔu] |
| ⟨uab⟩ | [uəp̚] | default [uəp̚] · word final [uəp̚˧] · word initial [ʔuəp̚] |
| ⟨uad⟩ | [uət̚] | default [uət̚] · word final [uət̚˧] · word initial [ʔuət̚] |
| ⟨uam⟩ | [uəm] | default [uəm] · word initial [ʔuəm] |
| ⟨uan⟩ | [uən] | default [uən] · word initial [ʔuən] |
| ⟨uang⟩ | [uəŋ] | default [uəŋ] · word initial [ʔuəŋ] |
| ⟨ub⟩ | [up̚] | default [up̚] · word final [up̚˧] · word initial [ʔup̚] |
| ⟨ud⟩ | [ut̚] | default [ut̚] · word final [ut̚˧] · word initial [ʔut̚] |
| ⟨ue⟩ | [uə] | default [uə] · word initial [ʔuə] |
| ⟨ug⟩ | [uk̚] | default [uk̚] · word final [uk̚˧] · word initial [ʔuk̚] |
| ⟨ui⟩ | [ui] | default [ui] · word initial [ʔui] |
| ⟨um⟩ | [um] | default [um] · word initial [ʔum] |
| ⟨un⟩ | [un] | default [un] · word initial [ʔun] |
| ⟨ung⟩ | [uŋ] | default [uŋ] · word initial [ʔuŋ] |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ɕ] | before consonant [˧˩] · default [ɕ] · word final [˧˩] |
| ⟨y⟩ | [j] | before consonant [˧] · default [j] · word final [˧] |
| ⟨z⟩ | [ts] | before consonant [˩] · default [ts] · word final [˩] |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pcc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Bosnian](bs.md) · [Home](../index.md) · [Breton →](br.md)
