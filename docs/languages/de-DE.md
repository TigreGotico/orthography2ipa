# German (de-DE) — Phonology Reference

**Code**: `de-DE` | **Family**: Indo-European > Germanic | **Script**: Latin (alphabet)
**Quality tier**: research (deep orthography; production threshold ≤ 0.25 PER at ≥ 500 gold entries) | **Sources**: Wiese (1996), Hall (2003), Mangold (2005), Kohler (1990), Wikipedia German phonology, Wikipedia German orthography

**Benchmark**: wikipron, n=269, PER 0.3613 (improved from a 0.3656 baseline after
fixing the ich-Laut/ach-Laut front/back vowel split described below). Still
above the 0.25 deep-orthography production ceiling and below the 500-entry
minimum, so the spec remains at `research` tier.

---

## Consonant System

### Obstruent Inventory

| Manner | Bilabial | Labiodental | Alveolar | Palato-alv. | Palatal | Velar | Uvular/Glottal |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Plosive | p b | | t d | | | k ɡ | |
| Affricate | pf | | ts | tʃ | | | |
| Fricative | | f v | s z | ʃ | ç | x | ʁ h |
| Nasal | m | | n | | | ŋ | |
| Lateral | | | l | | | | |

### Auslautverhärtung (Final Devoicing)

One of the most important rules in German: **obstruents in coda position (including word-finally) are always voiceless**.

| Voiced (onset) | Voiceless (coda/word-final) | Example |
|:---:|:---:|:---|
| b | p | `Grab` [ɡʁaːp] vs. `graben` [ɡʁaːbən] |
| d | t | `Hund` [hʊnt] vs. `Hunde` [hʊndə] |
| ɡ | k | `Tag` [taːk] vs. `Tage` [taːɡə] |
| v | f | `brav` [bʁaːf] vs. `brave` [bʁaːvə] |

`positional_graphemes` encodes this for `b`, `d`, `g`, `v`:
```json
"b": {"word_final": ["p"], "coda": ["p"], "default": ["b"]}
```

**Note**: `s` at word onset before vowels is voiced [z] (`sagen` [zaːɡən]), voiceless elsewhere.

### Ch — Ach-Laut vs. Ich-Laut

The digraph ⟨ch⟩ has two main realizations conditioned by the preceding
vowel (Kohler 1990; Wiese 1996):

| Environment | Realization | Examples |
|:---|:---:|:---|
| After a, o, u (back vowels) | [x] (ach-Laut, velar fricative) | `Bach` [bax], `noch` [nɔx], `Buch` [buːx] |
| After e, i (front vowels), consonants, word-initially | [ç] (ich-Laut, palatal fricative) | `ich` [ɪç], `echt` [ɛçt], `Milch` [mɪlç] |
| Classical loanwords (word-initial) | [k] | `Charakter` [kaˈʁaktɐ], `Chor` [koːɐ̯] |

```json
"ch": {
  "after_a": ["x", "ç"],
  "after_o": ["x", "ç"],
  "after_u": ["x", "ç"],
  "after_e": ["ç", "x"],
  "after_i": ["ç", "x"],
  "after_vowel": ["ç", "x"],
  "word_initial": ["k", "ç"],
  "default": ["ç"]
}
```

**Known engine-limit exception**: `GraphemePosition` only distinguishes
`after_a/e/i/o/u` for single-letter vowel graphemes. ⟨ch⟩ following the
umlauts ä/ö/ü (`Bücher`, `Löcher`) or the diphthong graphemes eu/äu falls
back to the generic `after_vowel` bucket, which defaults to [ç] — correct
for the umlauts (front vowels) but not encodable as a distinct rule
without extending the position enum further.

**Known engine-limit exception**: only `word_final` position is computed
by the tokenizer (no medial-coda syllabification), so Auslautverhärtung
before a following consonant inside a word (e.g. `Abschied`) is not
applied; only absolute word-final devoicing is.

### Sp / St — Positional Assimilation

In **word-initial position**, ⟨sp⟩ → [ʃp] and ⟨st⟩ → [ʃt]. In other positions: [sp], [st].

| Position | ⟨sp⟩ | ⟨st⟩ | Examples |
|:---|:---:|:---:|:---|
| Word-initial | [ʃp] | [ʃt] | `spielen` [ʃpiːlən], `stark` [ʃtaʁk] |
| Non-initial | [sp] | [st] | `Wespe` [vɛspə], `Fenster` [fɛnstɐ] |

---

## Vowel System

German has a length contrast (short vs. long) for all vowels, plus front rounded vowels (ü, ö):

| Grapheme | IPA | Length | Example |
|:---:|:---:|:---:|:---|
| a | [a] / [aː] | short/long | `Mann` [man] / `Bahn` [baːn] |
| e | [ɛ] / [eː] / [ə] | short/long/schwa | `Bett` [bɛt] / `See` [zeː] / `bitte` [bɪtə] |
| i | [ɪ] / [iː] | short/long | `mit` [mɪt] / `Lied` [liːt] |
| o | [ɔ] / [oː] | short/long | `voll` [fɔl] / `Boot` [boːt] |
| u | [ʊ] / [uː] | short/long | `Hund` [hʊnt] / `gut` [ɡuːt] |
| ä | [ɛ] / [ɛː] | short/long | `Männer` [mɛnɐ] / `Mädchen` [mɛːtçən] |
| ö | [œ] / [øː] | short/long | `können` [kœnən] / `hören` [høːʁən] |
| ü | [ʏ] / [yː] | short/long | `dünn` [dʏn] / `kühn` [kyːn] |

### Diphthongs

| Grapheme | IPA | Example |
|:---:|:---:|:---|
| ei, ai | [aɪ̯] | `Eis` [aɪ̯s], `Mai` [maɪ̯] |
| au | [aʊ̯] | `Haus` [haʊ̯s] |
| eu, äu | [ɔʏ̯] | `neu` [nɔʏ̯], `Häuser` [hɔʏ̯zɐ] |

---

## Key Positional Rules Summary

| Grapheme | Environment | Realization | Phenomenon |
|:---:|:---|:---:|:---|
| b, d, g, v | coda / word-final | p, t, k, f | Auslautverhärtung |
| s | word-initial + vowel | z | Voiced onset |
| ch | after a/o/u | x | Ach-Laut |
| ch | after e/i/front vowels | ç | Ich-Laut |
| sp, st | word-initial | ʃp, ʃt | Affrication |
| ig | word-final | ɪç | Suffix reduction |

---

## Glottal Stop (Not Encoded)

Word-initial and stressed word-internal vowel onsets are frequently preceded
by a glottal stop [ʔ] in careful Standard German, e.g. `Oase` [ʔoˈʔaːzə]
(Kohler 1990). It is not phonemic, is far more frequent in northern
varieties than in the south, and is commonly absent in colloquial speech
(Wikipedia German phonology). wikipron-style gold transcriptions used for
this repository's benchmark do not include it, so it is deliberately not
inserted — doing so would inflate PER against the gold rather than improve
accuracy.

## References

- Wiese, R. (1996). *The Phonology of German*. Oxford University Press.
- Hall, T.A. (2003). *Phonologie des Deutschen: eine Einführung*. de Gruyter.
- Mangold, M. (2005). *Duden Aussprachewörterbuch* (6th ed.). Dudenverlag.
- Kohler, K.J. (1990). *Illustrations of the IPA: German*. Journal of the International Phonetic Association 20(1).
- Wikipedia: [German phonology](https://en.wikipedia.org/wiki/German_phonology)
- Wikipedia: [German orthography](https://en.wikipedia.org/wiki/German_orthography)

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [germanic](germanic.md), [en-GB](en-GB.md)*
