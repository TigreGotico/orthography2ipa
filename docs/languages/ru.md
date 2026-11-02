# Russian (ru): Phonology Reference

**Code**: `ru` | **Family**: Indo-European > Slavic > East Slavic | **Script**: Cyrillic (alphabet) | **Quality tier**: research

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

The `wikipron` row is crowd-scraped and comes from WikiPron's `rus_cyrl_narrow.tsv`, because WikiPron scraped Russian only in narrow transcription. The `coruss_ru` and `primary_sources` rows are expert-human. The `alphacep_ru_book` row is machine-generated. The `vox_communis` row is epitran-derived and cannot gate. The WikiPron gold writes no stress mark, so it cannot judge stress placement. See the [scoreboard](../scoreboard.md) for the scores, and [the Slavic section of the comparative page](comparative.md#slavic-languages) for Russian among its relatives.

## References

- Avanesov, R.I. (1956). *Russian Literary Pronunciation*. Moscow: Uchpedgiz.
- Jones, D. & Ward, D. (1969). *The Phonetics of Russian*. Cambridge University Press.
- Padgett, J. (2002). *Russian vowel reduction and dialectology*. UC Santa Cruz.
- Timberlake, A. (2004). *A Reference Grammar of Russian*. Cambridge University Press.
- Padgett, J. & Tabain, M. (2005). *Adaptive Dispersion Theory and Phonological Vowel Reduction in Russian*. Phonetica.
- Wikipedia: [Russian phonology](https://en.wikipedia.org/wiki/Russian_phonology). It confirms the akanye and ikanye mergers, the pretonic and further-unstressed reduction targets, the merger to [ɪ] after a soft consonant and regressive voicing assimilation, citing Jones & Ward 1969 and Timberlake 2004.
- Wikipedia: [Vowel reduction in Russian](https://en.wikipedia.org/wiki/Vowel_reduction_in_Russian), with worked IPA examples for the reduction of е and и after hard and soft consonants.
- Wikipedia: [Akanye](https://en.wikipedia.org/wiki/Akanye). It confirms pretonic [ɐ] or [ʌ] against further-unstressed [ə], and treats ikanye as a process distinct from akanye, citing Padgett & Tabain 2005.
- [CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron) README. It confirms that WikiPron scraped Russian only in narrow transcription.

---
[← Mirandese](mwl.md) · [Home](../index.md) · [Modern Standard Arabic →](ar.md)
