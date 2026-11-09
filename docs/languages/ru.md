# Russian (`ru`)

<!-- atlas:summary begin -->
Russian is an East Slavic language, written in the Cyrillic script. Glottolog places it in 20 countries. The `ru` spec is at the research tier. It cites 6 sources and has 5 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ru` |
| Aliases | `rus` |
| ISO 639-3 | [rus](https://iso639-3.sil.org/code/rus), Russian |
| Glottolog | [russ1263](https://glottolog.org/resource/languoid/id/russ1263), Russian |
| Wikidata | [Q7737](https://www.wikidata.org/wiki/Q7737) |
| Wikipedia | [Russian language](https://en.wikipedia.org/wiki/Russian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > East Slavic](by-family.md#indo-european--balto-slavic--slavic--east-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Belarus](by-region.md#belarus), [China](by-region.md#china), [Estonia](by-region.md#estonia), [Finland](by-region.md#finland), [Georgia](by-region.md#georgia), [Kazakhstan](by-region.md#kazakhstan), [Kyrgyzstan](by-region.md#kyrgyzstan), [Latvia](by-region.md#latvia) and 12 more |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [East Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-east1426) `x-clade-east1426` |
| Child lects | 6, see [Related lects](#related-lects) |
| Explorer | [`ru` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ru) |
| Spec file | [`ru.json`](../../orthography2ipa/data/ru.json) |
<!-- atlas:header end -->

## Overview

Russian spelling is regular for consonants and hides most of what happens to vowels. The spec reads the consonants through positional graphemes and allophone rules. Its vowel reduction depends on where the stress falls, and standard Russian text does not write the stress. That gap is the main limit of the spec.

## Stress

Russian word stress is lexical and free (Timberlake 2004). The spelling does not predict it, and standard orthography does not mark it. The spec has a `stress` block with two parts.

The first part reads the stress where the text marks it. The letter ⟨ё⟩ always carries the stress. Dictionaries, textbooks and texts for children mark stress with a combining acute (U+0301) on the stressed vowel. The spec lists both as stress marks, and the acute itself transcribes to nothing.

The second part guesses where the text gives no mark. The default is the penultimate syllable, a statistical choice tuned on the WikiPron gold. It exists only to place the reduction contexts, which the spec defines relative to the stress. A wrong guess changes which vowel stays unreduced:

```python
>>> import orthography2ipa as o
>>> [o.transcribe(w, "ru") for w in ["молоко", "молоко́"]]
['mɐˈɫokə', 'məɫɐˈko']
```

The block also lists the closed class of prosodic clitics in `cliticless_words`: the simple prepositions, the proclitic particles не and ни, and the enclitics же, ли/ль and бы/б. These words carry no stress of their own. Alone, with no stress in the word, a clitic falls through to the weakest degree of reduction, so на gives `nə`.

A stress dictionary, or input with the stress marked, would close this gap. More grapheme rules would not.

## Consonants

### Final devoicing

Russian obstruents are voiceless at the end of a word and before a voiceless obstruent. Positional `word_final` entries devoice б в г д з ж. The `RU_REGR_DEVOICE_*` rules devoice an obstruent before a voiceless one, and the `RU_REGR_VOICE_*` rules voice a voiceless obstruent before a voiced one. The `RU_DEVOICE_SOFT_FIN_*` rules devoice a palatalised б в д з г before a final soft sign.

| Voiced | Voiceless | Example |
|:---:|:---:|:---|
| б [b] | п [p] | `хлеб` [xlʲep] 'bread' |
| в [v] | ф [f] | `кровь` [krofʲ] 'blood' |
| г [ɡ] | к [k] | `враг` [vrak] 'enemy' |
| д [d] | т [t] | `год` [ɡot] 'year' |
| з [z] | с [s] | `раз` [ras] 'time' |
| ж [ʐ] | ш [ʂ] | `нож` [noʂ] 'knife' |

```python
>>> [o.transcribe(w, "ru") for w in ["хлеб", "год", "нож", "сделать"]]
['ˈxlʲep', 'ˈɡot', 'ˈnoʂ', 'ˈzdʲeɫətʲ']
```

One cluster stays wrong. In `гвоздь` 'nail' the final дь devoices to [tʲ], but the з before it keeps its voice, so the output is `ˈɡvozʲtʲ` and not [ɡvosʲtʲ].

### Palatalisation

Most Russian consonants come in a plain and a palatalised pair. The soft sign ⟨ь⟩ and the vowels е, и, ё, ю, я palatalise the consonant before them. The spec reads each consonant letter as its plain value. A `RU_PALAT_*` allophone rule for each of б в г д з к л м н п р с т ф х then palatalises it before a front or iotated vowel, or before ⟨ь⟩. The rule `RU_SOFT_SIGN_SILENT` deletes the soft sign after it has done its work. The `RU_REGR_PALAT_*` rules spread palatalisation backwards in clusters such as ст and нт before a soft consonant.

The letter л is the velarised [ɫ] by default and [lʲ] when palatalised. Three consonants are always soft: ч [tɕ], щ [ɕː] and й [j]. Three are always hard: ж [ʐ], ш [ʂ] and ц [ts]. After a hard ж ш ц, the `RU_HARD_BACK_*` rules turn и into [ɨ] and е into [ɛ].

```python
>>> [o.transcribe(w, "ru") for w in ["пять", "мёд", "жир", "цех"]]
['ˈpʲatʲ', 'ˈmʲɵt', 'ˈʐɨr', 'ˈtsɛx']
```

After a soft consonant, ё is [ɵ], from the rule `RU_DEIOTA_jo`.

### The г of the endings -ого and -его

In the endings -ого and -его, the letter г is [v]. The spec states this in `grammatical_endings` for the ending forms, and in `word_exceptions` for frequent whole words such as его, кого, того and ничего. Words such as много and дорого, where the г is a real [ɡ], are whole-word exceptions too.

```python
>>> [o.transcribe(w, "ru") for w in ["его", "кого", "си́него"]]
['jɪˈvo', 'kɐˈvo', 'ˈsʲinʲɪvə']
```

## Vowel reduction (akanye and ikanye)

Unstressed vowels in Russian reduce in a fixed pattern (Avanesov 1956, Padgett & Tabain 2005). The spec states the pattern with the positions `first_pretonic`, `pretonic` and `posttonic` in `positional_graphemes`.

| Letter | Stressed | First pretonic | Other unstressed |
|:---:|:---:|:---:|:---:|
| о | [o] | [ɐ] | [ə] |
| а | [a] | [ɐ] | [ə] |
| е | [e] | [ɪ] | [ɪ] |
| я | [a] | [ɪ] | [ɪ] before the stress, [ə] after it |
| и | [i] | [ɪ] | [ɪ] |
| у | [u] | [ʊ] | [ʊ] |

With the stress marked, the spec gives the reduced forms:

```python
>>> [o.transcribe(w, "ru") for w in ["носы́", "носово́й", "сады́"]]
['nɐˈsɨ', 'nəsɐˈvoj', 'sɐˈdɨ']
```

## Iotated vowels

The vowels е, ё, ю, я stand for [j] plus a vowel at the start of a word, after another vowel and after ъ or ь. After a consonant they only palatalise the consonant, with no [j]. The spec maps each of the four letters to its iotated value, and the `RU_DEIOTA_*` rules drop the [j] after a consonant.

```python
>>> [o.transcribe(w, "ru") for w in ["яма", "ель", "объе́кт", "няня"]]
['ˈjamə', 'ˈjelʲ', 'ɐˈbjekt', 'ˈnʲanʲə']
```

## Sibilants

| Grapheme | IPA | Description |
|:---:|:---:|:---|
| с | [s] | Alveolar, hard |
| з | [z] | Alveolar, hard |
| ш | [ʂ] | Retroflex, always hard |
| ж | [ʐ] | Retroflex, always hard |
| щ | [ɕː] | Palatal, always soft (long) |
| ч | [tɕ] | Palatal affricate, always soft |
| ц | [ts] | Alveolar affricate, always hard |

## Benchmark

The `wikipron` row is crowd-scraped and comes from WikiPron's `rus_cyrl_narrow.tsv`, because WikiPron scraped Russian only in narrow transcription. The `coruss_ru` and `primary_sources` rows are expert-human. The `alphacep_ru_book` row is machine-generated. The `vox_communis` row is epitran-derived and cannot gate. The WikiPron gold writes no stress mark, so it cannot judge stress placement. See the [scoreboard](../evaluation/generated/scoreboard.md) for the scores, and [the Slavic section of the comparative page](comparative.md#slavic-languages) for Russian among its relatives.

<!-- atlas:lects begin -->
## Related lects

These specs name `ru` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Moscow Russian](https://tigregotico.github.io/orthography2ipa/#ru-x-moscow) `ru-x-moscow`: stub tier
- [Northern Russian](ru-x-northern.md) `ru-x-northern`: research tier
- [Pskov Russian](https://tigregotico.github.io/orthography2ipa/#ru-x-pskov) `ru-x-pskov`: skeleton tier
- [Siberian Russian](https://tigregotico.github.io/orthography2ipa/#ru-x-siberian) `ru-x-siberian`: skeleton tier
- [Southern Russian](ru-x-southern.md) `ru-x-southern`: research tier
- [Ural Russian](https://tigregotico.github.io/orthography2ipa/#ru-x-ural) `ru-x-ural`: stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-jones_ward1969"></a>Jones, D. & Ward, D. (1969). *The Phonetics of Russian*. Cambridge University Press.
2. <a id="src-timberlake2004"></a>Timberlake, A. (2004). *A Reference Grammar of Russian*. Cambridge University Press.
3. <a id="src-padgett_tabain2005"></a>Padgett, J. & Tabain, M. (2005). *Adaptive Dispersion Theory and Phonological Vowel Reduction in Russian*. Phonetica.
4. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
5. <a id="src-wikipron_lee2020"></a>Lee, J. L., Ashby, L. F. E., Garza, M. E., Lee-Sikka, Y., Miller, S., Wong, A., McCarthy, A. D. & Gorman, K. (2020). *WikiPron: Mining Wiktionary for Massively Multilingual Pronunciation Data*. LREC. [github.com](https://github.com/CUNY-CL/wikipron)
6. <a id="src-avanesov1956"></a>Avanesov, R. I. (1956). *Russkoe literaturnoe proiznoshenie*. Prosveshchenie.
<!-- atlas:sources end -->

### Notes on the sources

The page also draws on works that the spec does not cite:

- Padgett, J. (2002). *Russian vowel reduction and dialectology*. UC Santa Cruz.
- Wikipedia: [Russian phonology](https://en.wikipedia.org/wiki/Russian_phonology). It confirms the akanye and ikanye mergers, the pretonic and further-unstressed reduction targets, the merger to [ɪ] after a soft consonant and regressive voicing assimilation, citing Jones & Ward 1969 and Timberlake 2004.
- Wikipedia: [Vowel reduction in Russian](https://en.wikipedia.org/wiki/Vowel_reduction_in_Russian), with worked IPA examples for the reduction of е and и after hard and soft consonants.
- Wikipedia: [Akanye](https://en.wikipedia.org/wiki/Akanye). It confirms pretonic [ɐ] or [ʌ] against further-unstressed [ə], and treats ikanye as a process distinct from akanye, citing Padgett & Tabain 2005.
- The [CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron) README confirms that WikiPron scraped Russian only in narrow transcription.

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `coruss_ru` ([CoRuSS](https://russpeech.spbu.ru/)) | `ru` | gold | expert-human | Not stated upstream | 9527 | 0.3572 | yes |
| `primary_sources` | `ru` | gold | expert-human | Apache-2.0 (this repository). Each row quotes and cites a published example. | 36 | 0.1867 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ru` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 403870 | 0.1443 | yes |
| `alphacep_ru_book` ([alphacep/biggest-ru-book-cleanup](https://huggingface.co/datasets/alphacep/biggest-ru-book-cleanup)) | `ru` | generated | machine-generated | Not stated upstream | 6175 | 0.2391 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ru` | generated | epitran-derived | CC0 1.0 | 50517 | 0.3481 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 82 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d dʲ t tʲ |  |  | k kʲ ɡ ɡʲ |
| Affricate |  |  | ts |  | tɕ |  |
| Nasal | m mʲ |  | n nʲ |  |  | ŋ |
| Trill |  |  | r rʲ |  |  |  |
| Fricative |  | f fʲ v vʲ | s sʲ z zʲ | ʂ ʐ | ɕː | x xʲ |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | lʲ ɫ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Near-close | ɪ |  | ʊ |
| Close-mid | e | ɵ | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Near-open |  | ɐ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [bʲjɪvə] [dʲjɪvə] [ja] [je] [jo] [ju] [jə] [jɪ] [jɵ] [jʊ] [lʲjɪvə] [mʲjɪvə] [nʲjɪvə] [nʲɪvə] [pʲjɪvə] [rʲjɪvə] [sʲjɪvə] [sʲɪvə] [tsɨvə] [tɕj] [tɕjɪvə] [tɕɪvə] [tʲjɪvə] [vʲjɪvə] [zʲjɪvə] [ɕːɪvə] [əvə] [ʂj] [ʂɨvə] [ʐj] [ʐjɪvə] [ʐɨvə] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨́⟩ | ∅ |  |
| ⟨а⟩ | [a] | first pretonic [ɐ] · posttonic [ə] · pretonic [ə] |
| ⟨б⟩ | [b] | default [b] · word final [p] |
| ⟨в⟩ | [v] | default [v] · word final [f] |
| ⟨г⟩ | [ɡ] | default [ɡ] · word final [k] |
| ⟨д⟩ | [d] | default [d] · word final [t] |
| ⟨е⟩ | [je] [e] | posttonic [jɪ] [ɪ] · pretonic [jɪ] [ɪ] |
| ⟨ж⟩ | [ʐ] | default [ʐ] · word final [ʂ] |
| ⟨з⟩ | [z] | default [z] · word final [s] |
| ⟨и⟩ | [i] | posttonic [ɪ] · pretonic [ɪ] |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [ɫ] |  |
| ⟨ль⟩ | [lʲ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] | first pretonic [ɐ] · posttonic [ə] · pretonic [ə] |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] | posttonic [ʊ] · pretonic [ʊ] |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ш⟩ | [ʂ] |  |
| ⟨щ⟩ | [ɕː] |  |
| ⟨щь⟩ | [ɕː] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [ɛ] | posttonic [ɪ] · pretonic [ɪ] |
| ⟨ю⟩ | [ju] | posttonic [jʊ] · pretonic [jʊ] |
| ⟨я⟩ | [ja] | posttonic [jə] · pretonic [jɪ] |
| ⟨ё⟩ | [jo] | default [jo] |

Stress falls on the penult by default. A written ⟨ё⟩ ⟨́⟩ marks the stressed vowel.

Whole-word exceptions (25): ⟨всего⟩ [fsʲɪˈvo], ⟨дорого⟩ [ˈdorəɡə], ⟨его⟩ [jɪˈvo], ⟨кого⟩ [kɐˈvo], ⟨лого⟩ [ˈɫoɡə], ⟨много⟩ [ˈmnoɡə], ⟨моего⟩ [məjɪˈvo], ⟨намного⟩ [nɐˈmnoɡə], ⟨него⟩ [nʲɪˈvo], ⟨недорого⟩ [nʲɪˈdorəɡə], ⟨немного⟩ [nʲɪˈmnoɡə], ⟨никого⟩ [nʲɪkɐˈvo], ⟨ничего⟩ [nʲɪtɕɪˈvo], ⟨ничьего⟩ [nʲɪtɕjɪˈvo], ⟨ого⟩ [ˈoɡo], ⟨одного⟩ [ɐdnɐˈvo], ⟨своего⟩ [svəjɪˈvo], ⟨сего⟩ [sʲɪˈvo], ⟨строго⟩ [ˈstroɡə], ⟨твоего⟩ [tvəjɪˈvo], ⟨того⟩ [tɐˈvo], ⟨убого⟩ [ʊˈboɡə], ⟨чего⟩ [tɕɪˈvo], ⟨чьего⟩ [tɕjɪˈvo], ⟨этого⟩ [ˈɛtəvə].

Grammatical endings: ⟨-бьего⟩ [bʲjɪvə], ⟨-вьего⟩ [vʲjɪvə], ⟨-дьего⟩ [dʲjɪvə], ⟨-жего⟩ [ʐɨvə], ⟨-жьего⟩ [ʐjɪvə], ⟨-зьего⟩ [zʲjɪvə], ⟨-льего⟩ [lʲjɪvə], ⟨-мьего⟩ [mʲjɪvə], ⟨-него⟩ [nʲɪvə], ⟨-ньего⟩ [nʲjɪvə], ⟨-ого⟩ [əvə], ⟨-пьего⟩ [pʲjɪvə], ⟨-рьего⟩ [rʲjɪvə], ⟨-сего⟩ [sʲɪvə], ⟨-сьего⟩ [sʲjɪvə], ⟨-тьего⟩ [tʲjɪvə], ⟨-цего⟩ [tsɨvə], ⟨-чего⟩ [tɕɪvə], ⟨-чьего⟩ [tɕjɪvə], ⟨-шего⟩ [ʂɨvə], ⟨-щего⟩ [ɕːɪvə].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 62 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `RU_HARD_BACK_jɪ` | /jɪ/ → [ɨ], after [ʐ] [ʂ] [ts] | - | - |
| `RU_HARD_BACK_je` | /je/ → [ɛ], after [ʐ] [ʂ] [ts] | ⟨жест⟩ [ʐɛst] | [Jones 1969](#src-jones_ward1969), [Timberlake 2004](#src-timberlake2004), [Avanesov 1956](#src-avanesov1956) |
| `RU_HARD_BACK_ɪ` | /ɪ/ → [ɨ], after [ʐ] [ʂ] [ts] | - | - |
| `RU_HARD_BACK_i` | /i/ → [ɨ], after [ʐ] [ʂ] [ts] | - | - |
| `RU_HARD_BACK_e` | /e/ → [ɛ], after [ʐ] [ʂ] [ts] | ⟨жест⟩ [ʐɛst] | [Jones 1969](#src-jones_ward1969), [Timberlake 2004](#src-timberlake2004), [Avanesov 1956](#src-avanesov1956) |
| `RU_DEVOICE_SOFT_FIN_b` | /b/ → [pʲ], before [ʲ], with more context in the spec | - | - |
| `RU_DEVOICE_SOFT_FIN_v` | /v/ → [fʲ], before [ʲ], with more context in the spec | - | - |
| `RU_DEVOICE_SOFT_FIN_d` | /d/ → [tʲ], before [ʲ], with more context in the spec | - | - |
| `RU_DEVOICE_SOFT_FIN_z` | /z/ → [sʲ], before [ʲ], with more context in the spec | - | - |
| `RU_DEVOICE_SOFT_FIN_ɡ` | /ɡ/ → [kʲ], before [ʲ], with more context in the spec | - | - |
| `RU_PALAT_b` | /b/ → [bʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_v` | /v/ → [vʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_ɡ` | /ɡ/ → [ɡʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_d` | /d/ → [dʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_z` | /z/ → [zʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_k` | /k/ → [kʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_ɫ` | /ɫ/ → [lʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_m` | /m/ → [mʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_n` | /n/ → [nʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_p` | /p/ → [pʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_r` | /r/ → [rʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_s` | /s/ → [sʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_t` | /t/ → [tʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_f` | /f/ → [fʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_PALAT_x` | /x/ → [xʲ], before [jɪ] [jə] [jʊ] [je] [ja] [ju] [jo] [j] and 3 more | - | - |
| `RU_SOFT_SIGN_SILENT` | /ʲ/ → ∅, after [b] [d] [f] [j] [k] [m] [n] [p] and 13 more | - | - |
| `RU_DEIOTA_jɪ` | /jɪ/ → [ɪ], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_jə` | /jə/ → [ə], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_jʊ` | /jʊ/ → [ʊ], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_je` | /je/ → [e], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_ja` | /ja/ → [a], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_DEIOTA_ju` | /ju/ → [u], after [b] [d] [f] [j] [k] [m] [n] [p] and 15 more | - | - |
| `RU_HARD_BACK_jo` | /jo/ → [o], after [ʐ] [ʂ] [ts] | ⟨шёл⟩ [ʂoɫ] | [Jones 1969](#src-jones_ward1969), [Timberlake 2004](#src-timberlake2004) |
| `RU_DEIOTA_jo` | /jo/ → [ɵ], after [b] [d] [f] [j] [k] [m] [n] [p] and 12 more | - | - |
| `RU_DEIOTA_jo_separative` | /jo/ → [jɵ], after [ʲ] [lʲ] | ⟨бельё⟩ [bʲɪlʲjɵ] | - |
| `RU_REGR_DEVOICE_b` | /b/ → [p], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨абсолют⟩ [ɐpsɐlʲut] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_bʲ` | /bʲ/ → [pʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_v` | /v/ → [f], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨всё⟩ [fsʲɵ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_vʲ` | /vʲ/ → [fʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_d` | /d/ → [t], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨водка⟩ [votkə] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_dʲ` | /dʲ/ → [tʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_ɡ` | /ɡ/ → [k], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨водка⟩ [votkə] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_ɡʲ` | /ɡʲ/ → [kʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_z` | /z/ → [s], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨всё⟩ [fsʲɵ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_zʲ` | /zʲ/ → [sʲ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | ⟨всё⟩ [fsʲɵ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_DEVOICE_ʐ` | /ʐ/ → [ʂ], before [p] [t] [k] [f] [s] [ʂ] [x] [ts] and 8 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_p` | /p/ → [b], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_pʲ` | /pʲ/ → [bʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_t` | /t/ → [d], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨сделать⟩ [zʲdʲelətʲ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_tʲ` | /tʲ/ → [dʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨сделать⟩ [zʲdʲelətʲ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_k` | /k/ → [ɡ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨вокзал⟩ [vɐɡzaɫ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_kʲ` | /kʲ/ → [ɡʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_s` | /s/ → [z], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨сделать⟩ [zʲdʲelətʲ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_sʲ` | /sʲ/ → [zʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨сделать⟩ [zʲdʲelətʲ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_f` | /f/ → [v], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | ⟨вокзал⟩ [vɐɡzaɫ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_fʲ` | /fʲ/ → [vʲ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_VOICE_ʂ` | /ʂ/ → [ʐ], before [b] [d] [ɡ] [z] [ʐ] [bʲ] [dʲ] [ɡʲ] and 1 more | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_s` | /s/ → [sʲ], before [t] [d] [n], with more context in the spec | ⟨гости⟩ [ɡosʲtʲɪ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_z` | /z/ → [zʲ], before [t] [d] [n], with more context in the spec | - | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_n` | /n/ → [nʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tɕ] [ɕː] | ⟨снег⟩ [sʲnʲek] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_t` | /t/ → [tʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tɕ] [ɕː] | ⟨гости⟩ [ɡosʲtʲɪ] | [Timberlake 2004](#src-timberlake2004) |
| `RU_REGR_PALAT_d` | /d/ → [dʲ], before [tʲ] [dʲ] [nʲ] [sʲ] [zʲ] [lʲ] [tɕ] [ɕː] | - | [Timberlake 2004](#src-timberlake2004) |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="хлеб|кровь|враг|год|раз|нож|гвоздь" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ru")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| хлеб | [ˈxlʲep] |
| кровь | [ˈkrofʲ] |
| враг | [ˈvrak] |
| год | [ˈɡot] |
| раз | [ˈras] |
| нож | [ˈnoʂ] |
| гвоздь | [ˈɡvozʲtʲ] |

The next table sets the engine output against worked examples printed in a cited source, from the [primary-source gold](../evaluation/datasets.md#primary-source-gold-primary_sources). The rows are spread evenly over that set. The last column says whether the two transcriptions are the same string.

| Spelling | Printed in the source | Engine output | Source, page | Same |
|:--|:--|:--|:--|:--|
| пальцы | /ˈpalʲt͡sɨ/ | [ˈpalʲtsɨ] | Yanushevskaya 2015, p. 222 | no |
| бязь | /ˈbʲasʲ/ | [ˈbʲasʲ] | Yanushevskaya 2015, p. 222 | yes |
| фото | /ˈfota/ | [ˈfotə] | Yanushevskaya 2015, p. 222 | no |
| вялит | /ˈvʲalʲit/ | [ˈvʲalʲɪt] | Yanushevskaya 2015, p. 222 | no |
| дом | /ˈdom/ | [ˈdom] | Yanushevskaya 2015, p. 222 | yes |
| нёс | /ˈnʲos/ | [ˈnʲɵs] | Yanushevskaya 2015, p. 222 | no |
| рад | /ˈrat/ | [ˈrat] | Yanushevskaya 2015, p. 222 | yes |
| сядь | /ˈsʲatʲ/ | [ˈsʲatʲ] | Yanushevskaya 2015, p. 222 | yes |
| царь | /ˈt͡sarʲ/ | [ˈtsarʲ] | Yanushevskaya 2015, p. 222 | no |
| шар | /ˈʃar/ | [ˈʂar] | Yanushevskaya 2015, p. 222 | no |
| кот | /ˈkot/ | [ˈkot] | Yanushevskaya 2015, p. 222 | yes |
| Гёте | /ˈɡʲote/ | [ˈɡʲɵtʲɪ] | Yanushevskaya 2015, p. 222 | no |

Source: Yanushevskaya, I. & Bunčić, D. (2015). *Russian (Illustrations of the IPA)*. Journal of the International Phonetic Association 45(2):221-228. [cambridge.org](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/55589EC639ADEF1764B5ECD0B76970FA/S0025100314000395a.pdf/russian.pdf)
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Romansh](rm.md) · [Home](../index.md) · [Rusyn →](rue.md)
