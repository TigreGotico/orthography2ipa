# Russian (ru) — Phonology Reference

**Code**: `ru` | **Family**: Slavic | **Script**: Cyrillic (alphabet)
**Quality tier**: research | **Sources**: Avanesov (1956), Jones & Ward (1969), Padgett (2002), Timberlake (2004), Padgett & Tabain (2005)

---

## Known limitation: stress is not orthographically marked

Russian word stress is **lexical and free** — it is not predictable from
spelling and standard orthography does not mark it. The spec therefore
carries no `stress` block (the research-tier exemption for languages
whose stress is not orthography-predictable applies here). Consequently
the pretonic/posttonic/nucleus-unstressed vowel-reduction rules below are
only reachable when the caller supplies pre-stressed input; on ordinary
unmarked spelling the engine cannot locate the stressed syllable, so
every vowel falls through to its unstressed-agnostic default form. This
is the dominant source of PER against unmarked gold sets (WikiPron's
`rus_cyrl_narrow.tsv`) and is why this spec is capped at `research`, not
`production` — closing this gap requires either a stress dictionary or
accepting pre-accented input, not further grapheme-rule tuning.

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

The spec models palatalization-before-iotated-vowel as explicit
two-grapheme tokens (`бе`→`bʲe`, `би`→`bʲi`, `дя`→`dʲa`, …) for the
**fifteen** consonants that contrast plain/palatalized (б в г д з к л
м н п р с т ф х), since the generic `before_e`/`before_i` positional
mechanism in the engine only matches Latin-script vowel letters and
does not fire on Cyrillic. That gives 12 bare soft-sign digraphs (бь
вь дь зь ль мь нь пь рь сь ть фь, representing the consonant alone,
e.g. word-finally) plus 75 iotated-vowel CV digraphs (each of the 15
consonants × е/и/я/ё/ю). Coda devoicing is extended to the palatalized
voiced obstruents, but only for the bare soft-sign digraphs (бь→пʲ,
вь→фʲ, дь→тʲ, зь→сʲ) so a word like `гвоздь` "nail" devoices its final
дь to [tʲ] — it is **not** applied to the iotated-vowel CV digraphs
(e.g. дя, зе), since those always resolve to a consonant immediately
followed by a vowel and are therefore never in coda position.

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
- Timberlake, A. (2004). *A Reference Grammar of Russian*. Cambridge University Press.
- Padgett, J. & Tabain, M. (2005). *Adaptive Dispersion Theory and Phonological Vowel Reduction in Russian*. Phonetica.
- Wikipedia: [Russian phonology](https://en.wikipedia.org/wiki/Russian_phonology) — confirms akanye/ikanye mergers, pretonic vs. further-unstressed reduction targets, post-soft-consonant merger to [ɪ], and regressive voicing assimilation (cites Jones & Ward 1969, Timberlake 2004).
- Wikipedia: [Vowel reduction in Russian](https://en.wikipedia.org/wiki/Vowel_reduction_in_Russian) — worked examples with IPA for е/и reduction after hard vs. soft consonants.
- Wikipedia: [Akanye](https://en.wikipedia.org/wiki/Akanye) — confirms pretonic [ɐ]/[ʌ] vs. further-unstressed [ə], and that ikanye is treated as a phonologically distinct process from akanye (cites Padgett & Tabain 2005).
- [CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron) README — confirms Russian was scraped only in narrow transcription, which is why the `ru` gold benchmark row uses `rus_cyrl_narrow.tsv`.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [slavic](slavic.md)*
