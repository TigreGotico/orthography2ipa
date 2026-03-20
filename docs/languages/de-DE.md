# German (de-DE) — Phonology Reference

**Code**: `de-DE` | **Family**: Germanic | **Script**: Latin (alphabet)
**Quality tier**: research | **Sources**: Wiese (1996), Hall (2003), Mangold (2005)

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

The digraph ⟨ch⟩ has two main realizations conditioned by the preceding vowel:

| Environment | Realization | Examples |
|:---|:---:|:---|
| After a, o, u, au | [x] (ach-Laut, velar fricative) | `Bach` [bax], `noch` [nɔx], `Buch` [buːx] |
| After e, i, ä, ö, ü, consonants, word-initially | [ç] (ich-Laut, palatal fricative) | `ich` [ɪç], `echt` [ɛçt], `Milch` [mɪlç] |
| Classical loanwords (word-initial) | [k] | `Charakter` [kaˈʁaktɐ], `Chor` [koːɐ̯] |

```json
"ch": {
  "after_vowel": ["x"],
  "after_consonant": ["ç"],
  "word_initial": ["k"],
  "default": ["ç"]
}
```

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

## References

- Wiese, R. (1996). *The Phonology of German*. Oxford University Press.
- Hall, T.A. (2003). *Phonologie des Deutschen: eine Einführung*. de Gruyter.
- Mangold, M. (2005). *Duden Aussprachewörterbuch* (6th ed.). Dudenverlag.
- Wikipedia: [German phonology](https://en.wikipedia.org/wiki/German_phonology)
