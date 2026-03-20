# Russian (ru) — Phonology Reference

**Code**: `ru` | **Family**: Slavic | **Script**: Cyrillic (alphabet)
**Quality tier**: research | **Sources**: Avanesov (1956), Jones & Ward (1969), Padgett (2002)

---

## Consonant System

### Final Devoicing (Neutralization)

Russian obstruents are **always voiceless in coda position** (word-finally and before another obstruent):

| Voiced | Voiceless | Example |
|:---:|:---:|:---|
| б [b] | п [p] | `хлеб` [xlʲep] "bread" |
| в [v] | ф [f] | `кровь` [krof] "blood" |
| г [ɡ] | к [k] | `враг` [vrak] "enemy" |
| д [d] | т [t] | `год` [ɡot] "year" |
| з [z] | с [s] | `раз` [ras] "time" |
| ж [ʐ] | ш [ʂ] | `нож` [noʂ] "knife" |

Applies across morpheme boundaries in fast speech: `сделать` [zdʲelatʲ].

### Palatalization (Softening)

Russian has a pervasive **consonant palatalization** system. The soft sign ⟨ь⟩ and front vowels (е/и/ё/ю/я) palatalize the preceding consonant:

| Hard | Soft | Notation |
|:---:|:---:|:---|
| б [b] | бь [bʲ] | before е/и/ё/ю/я |
| д [d] | дь [dʲ] | |
| н [n] | нь [nʲ] | `конь` [konʲ] "horse" |
| т [t] | ть [tʲ] | `пять` [pʲatʲ] "five" |
| л [l] | ль [lʲ] | `ноль` [nolʲ] "zero" |

**Always soft** (unpaired): ч [tɕ], щ [ɕː], й [j]
**Always hard** (unpaired): ж [ʐ], ш [ʂ], ц [ts]

### Г in Genitive Endings

In grammatical endings `-ого`/`-его`, the letter г is pronounced [v]:
- `синего` → [sʲinʲɪvə] "blue (gen.)"
- `его` → [jɪvo] "his/him"

```json
"г": {"before_e": ["v"], "before_i": ["v"], "word_final": ["k"], "default": ["ɡ"]}
```

---

## Vowel Reduction (Akan'ye)

Unstressed vowels in Russian undergo **systematic reduction** — one of the most important phonological features.

### О Reduction

| Syllable position | Realization | Examples |
|:---|:---:|:---|
| Stressed | [o] | `нос` [nos] "nose" |
| 1st pretonic (directly before stressed) | [ɐ] | `носы` [nɐˈsɨ] "noses" |
| Other unstressed | [ə] | `носовой` [nəsɐˈvoj] |

### А Reduction

| Syllable position | Realization | Examples |
|:---|:---:|:---|
| Stressed | [a] | `сад` [sat] "garden" |
| 1st pretonic | [ɐ] | `сады` [sɐˈdɨ] |
| Other unstressed | [ə] | `садовник` [sɐˈdovnʲɪk] |

### И/Е After Hard Consonants (Akan'ye variant — Ikan'ye)

| Vowel | After hard consonant (unstressed) | Example |
|:---:|:---:|:---|
| е [e] | [ɪ] | `место` → unstressed е → [ɪ] |
| я [a]/[ja] | [ɪ] | `мяч` → unstressed я → [ɪ] |

---

## Iotated Vowels

The vowels е, ё, ю, я are **iotated** (preceded by [j]) when:
1. **Word-initial**: `яма` [ˈjamə] "pit", `ель` [jelʲ] "fir"
2. **After another vowel**: `моя` [mɐˈja] "my"
3. **After ъ or ь** (hard/soft sign): `объект` [ɐbˈjekt]

After a consonant, they signal palatalization of that consonant only (no [j] prefix):
- `няня` [ˈnʲanʲə] — н is palatalized, no [j]

---

## Sibilants

Russian has two sets of sibilants:

| Grapheme | IPA | Description |
|:---:|:---:|:---|
| с | [s] | Alveolar, hard |
| з | [z] | Alveolar, hard |
| ш | [ʂ] | Retroflex, always hard |
| ж | [ʐ] | Retroflex, always hard |
| щ | [ɕː] | Palatal, always soft (long) |
| ч | [tɕ] | Palatal affricate, always soft |
| ц | [ts] | Alveolar affricate, always hard |

---

## References

- Avanesov, R.I. (1956). *Russian Literary Pronunciation*. Moscow: Uchpedgiz.
- Jones, D. & Ward, D. (1969). *The Phonetics of Russian*. Cambridge University Press.
- Padgett, J. (2002). *Russian vowel reduction and dialectology*. UC Santa Cruz.
- Wikipedia: [Russian phonology](https://en.wikipedia.org/wiki/Russian_phonology)
