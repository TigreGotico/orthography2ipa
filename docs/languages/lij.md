# Ligurian / Genoese (lij): Phonology Reference

**Code**: `lij` | **Family**: Indo-European > Romance > Gallo-Italic | **Script**: Latin (alphabet) | **Quality tier**: research | **Reference variety**: Genoese (*Zeneise*)

Ligurian is a Gallo-Italic language of Liguria and was the historical lingua franca of Mediterranean maritime trade. The `lij` spec models Genoese. It inherits its grapheme and allophone base from the Gallo-Italic Vulgar Latin spec `la-x-galloitalic` and overrides it with the Genoese values.

## Input contract

The spec follows the standard *grafia ofiçiâ* of the [Académia Ligùstica do Brénno](https://en.wikipedia.org/wiki/Academia_Ligustica_do_Brenno), the official Genoese orthography. The Ligurian Wikipedia and the dictionaries of Toso both use it. Give the spec text in that orthography, with accents and length marks. Ad-hoc or Italianising spellings are out of scope.

## The main grapheme correspondences

These correspondences are the features that a Genoese spec must get right. Several of them are diagnostic of the language and set it apart from Italian.

| Grapheme | IPA | Note |
|:---:|:---:|:---|
| `x` | /ʒ/ | The diagnostic Genoese letter, the sound of French ⟨j⟩ |
| `o` | /u/ | Genoese ⟨o⟩ is Italian ⟨u⟩. `ó` is /u/ and `ô` is /uː/ |
| `ò` | /ɔ/ | Open back, in contrast with `o` /u/. `ö` is /ɔː/ |
| `u` | /y/ | Front rounded. `û` and `ü` are /yː/ |
| `eu` | /ø/ | Front rounded mid. `êu` and `ëu` are /øː/ |
| `æ` | /ɛː/ | Long open-mid front |
| `ç` | /s/ | The voiceless sibilant with a cedilla |
| `z` | /z/ | Always /z/ and never an affricate, unlike Italian |
| `sc` | /ʃ/ before a front vowel, else /sk/ | positional |
| `scc` | /ʃtʃ/ | trigraph |
| `n-`, `nn-`, `ñ` | /ŋ/ | the velar nasal between vowels |

The table shows the first candidate of each grapheme. Some real output:

```python
>>> import orthography2ipa as o
>>> [o.transcribe(w, "lij") for w in ["gexa", "çittæ", "scciappâ", "lann-a"]]
['ˈdʒeʒa', 'siˈtɛː', 'ʃtʃiaˈpaː', 'ˈlãŋa']
```

`gexa` is 'church', `çittæ` is 'city' and `lann-a` is 'wool'.

### Softening of c and g

| Grapheme | Before a front vowel | Elsewhere |
|:---:|:---:|:---:|
| `c` | [tʃ] | [k] (`ch` is always [k]) |
| `g` | [dʒ] | [ɡ] (`gh` is always [ɡ]) |

### Vowel length and stress

The grafia writes length and stress with accent marks:

| Mark | Letters | Meaning |
|:---|:---|:---|
| Grave | `à è ì ò ù` | the stressed vowel, with the quality /a ɛ i ɔ y/ |
| Acute | `é ó` | stressed close-mid /e/ and /u/ |
| Circumflex | `â ê î ô û` | a long stressed vowel at the end of a word |
| Diaeresis | `ä ë ï ö ü` | a long vowel inside a word |

The default stress is on the penultimate syllable. A written accent, or the ligature `æ`, marks the stressed syllable and always wins. So the spelling gives the stress, and the `stress` block lists every accented letter as a stress mark.

## Allophone rules

The spec models the velar nasal and vowel nasalisation as allophone rules:

| Rule | Effect | Source |
|:---|:---|:---|
| `LIJ_N_VELAR_FINAL` | /n/ becomes [ŋ] at the end of a word (`can` gives `ˈkaŋ`, 'dog') | Toso 1997 |
| `LIJ_N_VELAR_ASSIM` | /n/ becomes [ŋ] before /k ɡ/ | Toso 1997 |
| `LIJ_N_LABIAL_ASSIM` | /n/ becomes [m] before /p b m f/ | Toso 1997 |
| `LIJ_NASAL_*` | a vowel becomes nasal before [ŋ] (`lann-a` gives `ˈlãŋa`) | Forner 1975, Toso 1997 |

Modern Genoese has total degemination. The spec maps each written double consonant to one phoneme, so `xatta` 'cat' gives `ˈʒata`.

## Vowel inventory

The close vowels are /i y u/, the mid vowels are /e ø ɛ ɔ/ and the open vowel is /a/. Each has a long counterpart /iː yː uː eː øː ɛː ɔː aː/, and each has nasal allophones before the velar nasal. The front rounded pair /y ø/ and the length contrast are the main vowel features (Forner 1975).

## Known limitations

After palatal `c` or `g`, a written ⟨i⟩ before a back vowel only marks the palatal. The spec handles it with the digraphs `cia cio ciu gia gio giu` and their accented forms. So `ciù` gives `ˈtʃy` and `giornâ` gives `dʒurˈnaː`, with no [i]. Before a consonant the ⟨i⟩ is a real vowel and stays, so `cina` gives `ˈtʃina`.

The spec reads `gl` as [ɡl], because Genoese does not have the Italian ⟨gli⟩ [ʎ].

## Benchmark

The `wikipron` row is crowd-scraped and can gate a promotion. The `vox_communis` row is epitran-derived, so it measures agreement with epitran and cannot gate. See the [scoreboard](../evaluation/generated/scoreboard.md) for the scores.

## Sources

- Académia Ligùstica do Brénno. *Grafia ofiçiâ: grafia moderna do zeneize.* 2008. <http://www.zeneize.net/>
- Toso, Fiorenzo. *Grammatica del genovese: varietà urbana e di koinè.* Le Mani, 1997.
- Forner, Werner. *Generative Phonologie des Dialekts von Genua.* Buske, 1975.
- Maiden, M. & Parry, M. (eds.) *The Dialects of Italy.* Routledge, 1997.
- Omniglot. *Genoese (Zeneize) language and pronunciation.* <https://www.omniglot.com/writing/genoese.htm> (tertiary cross-check).

---
[← Italian](it-IT.md) · [Home](../index.md) · [Pyrenean-valley Aragonese subdialects →](an-valleys.md)
