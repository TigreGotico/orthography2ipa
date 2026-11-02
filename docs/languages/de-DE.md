# German (de-DE): Phonology Reference

**Code**: `de-DE` | **Family**: Indo-European > Germanic > West Germanic | **Script**: Latin (alphabet) | **Quality tier**: research

The `de-DE` spec describes Standard German after Wiese (1996), Hall (2003), the Duden pronouncing dictionary (Mangold 2005) and the IPA Illustration by Kohler (1990). German has a deep orthography, so the deep threshold of 0.25 PER applies to a promotion (see [quality tiers](../quality_tiers.md#the-per-threshold)). The spec is at `research` tier. For its scores on the WikiPron gold, see the [scoreboard](../scoreboard.md).

## Consonants

The spec maps the consonant letters to this inventory:

| Manner | Bilabial | Labiodental | Alveolar | Palato-alveolar | Palatal | Velar | Uvular or glottal |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Plosive | p b | | t d | | | k ɡ | |
| Affricate | pf | | ts | tʃ | | | |
| Fricative | | f v | s z | ʃ | ç | x | ʁ h |
| Nasal | m | | n | | | ŋ | |
| Lateral | | | l | | | | |
| Approximant | | | | | j | | |

### Final devoicing

German obstruents are voiceless at the end of a word (Auslautverhärtung). The examples are from Wiese (1996):

| Voiced (onset) | Voiceless (word-final) | Example |
|:---:|:---:|:---|
| b | p | `Grab` [ɡʁaːp] against `graben` [ɡʁaːbən] |
| d | t | `Hund` [hʊnt] against `Hunde` [hʊndə] |
| ɡ | k | `Tag` [taːk] against `Tage` [taːɡə] |
| v | f | `brav` [bʁaːf] against `brave` [bʁaːvə] |

The spec states the rule as a `word_final` entry on ⟨b d g v⟩ in `positional_graphemes`:

```json
"b": {"word_final": ["p"], "default": ["b"]}
```

The rule covers only the absolute end of the word. The engine has a `coda` position, but the spec does not use it for these letters. So a coda inside a word keeps its voiced value. The spec gives `ˈabʃiːt` for `Abschied` and `ˈjaɡt` for `Jagd`, where the grammars have [p] and [k].

The spec gives ⟨s⟩ the value [z] at the start of a word and between vowels, as in `sagen` [zaːɡən] and `lesen`. The `word_initial` entry does not check the next letter, so it also voices ⟨s⟩ before a consonant. The spec gives `ˈzkat` for `Skat`.

### Ach-Laut and ich-Laut

The digraph ⟨ch⟩ has two main values. The preceding vowel selects the value (Kohler 1990, Wiese 1996):

| Environment | Value | Examples |
|:---|:---:|:---|
| After a, o, u (back vowels) | [x] (ach-Laut, velar fricative) | `Bach` [bax], `noch` [nɔx], `Buch` [buːx] |
| After e, i (front vowels), after consonants, word-initially | [ç] (ich-Laut, palatal fricative) | `ich` [ɪç], `echt` [ɛçt], `Milch` [mɪlç] |
| Classical loanwords (word-initial) | [k] | `Charakter` [kaˈʁaktɐ], `Chor` [koːɐ̯] |

The spec states this in `positional_graphemes`:

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

The `after_a` to `after_u` positions exist only for the five plain vowel letters. After ⟨ä ö ü⟩, ⟨ch⟩ takes the generic `after_vowel` entry, which ranks [ç] first. That is correct, because the umlaut vowels are front vowels (`Bücher`, `Löcher`). A diphthong grapheme counts by its first letter. So ⟨au⟩ selects `after_a` and gives [x] in `Bauch`, and ⟨eu⟩ selects `after_e` and gives [ç] in `euch`.

### Initial sp and st

At the start of a word, ⟨sp⟩ is [ʃp] and ⟨st⟩ is [ʃt]. In other positions they are [sp] and [st]. The spec has a `word_initial` entry for each digraph.

| Position | ⟨sp⟩ | ⟨st⟩ | Examples |
|:---|:---:|:---:|:---|
| Word-initial | [ʃp] | [ʃt] | `spielen` [ʃpiːlən], `stark` [ʃtaʁk] |
| Not initial | [sp] | [st] | `Wespe` [vɛspə], `Fenster` [fɛnstɐ] |

### Final -ig

Word-final ⟨-ig⟩ is [ɪç], as in `König` and `ewig`. The spec does not treat ⟨ig⟩ as a grapheme. The allophone rule `DE_FINAL_IG_SPIRANT` changes the [k] of a word-final ⟨g⟩ after [ɪ] to [ç]. The spec gives `ˈkøːnɪç` for `König`.

## Vowels

Each German vowel letter has a short and a long value, and ⟨e⟩ also has schwa. The examples are from the cited grammars:

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

The spec lists the short value first. The `DE_OPEN_SYLLABLE_*` allophone rules give the long value to a vowel in an open syllable, before one consonant and a vowel. The `DE_UNSTRESSED_TENSE_*` rules give the tense short value [i o u y] to an unstressed vowel before the stress and at the end of a word (Wiese 1996, ch. 2).

Unstressed ⟨e⟩ is [ə] through the `nucleus_unstressed` position, and word-final ⟨er⟩ is [ɐ], as in `Mutter`. A vowel letter followed by the lengthening ⟨h⟩ is one long-vowel grapheme, such as ⟨ah⟩ [aː] in `Bahn`. Before a vowel, the spec keeps the [h] of these graphemes and gives `ˈɡeːhən` for `gehen`.

### Diphthongs

| Grapheme | IPA | Example |
|:---:|:---:|:---|
| ei, ai | [aɪ̯] | `Eis` [aɪ̯s], `Mai` [maɪ̯] |
| au | [aʊ̯] | `Haus` [haʊ̯s] |
| eu, äu | [ɔʏ̯] | `neu` [nɔʏ̯], `Häuser` [hɔʏ̯zɐ] |

The spec writes the diphthongs as `aɪ`, `aʊ` and `ɔʏ`, without the non-syllabic mark.

## Stress

The `stress` block puts stress on the first syllable, which is the Germanic default (Wiese 1996, ch. 8). A closed set of suffixes attracts final stress: -ion, -tät, -ei, -eur, -ent, -ant, -enz, -anz, -ös, -iv, -ur and -al. The suffixes -ieren and -ismus take stress on the penult. The spec gives `naˈtsi̯oːn` for `Nation` and `ʃtuˈdiːʁən` for `studieren`.

The unstressed prefixes be-, ge-, ver-, ent-, er-, zer- and emp- move stress in ways that no suffix rule captures. The spec notes record this gap. Loanword stress is also outside the block, so the spec gives `ˈkaːʁaktɐ` for `Charakter`.

## Word exceptions

The `word_exceptions` table holds two closed sets. The first is the -sal nouns, such as `Schicksal`, `Trübsal` and `Labsal`, where ⟨s⟩ begins a suffix after a consonant and is voiced. The second is the grammatical terms in -tiv, such as `Genitiv` and `Dativ`.

## Positional rules

| Grapheme | Environment | Value | Mechanism |
|:---:|:---|:---:|:---|
| b, d, g, v | word-final | p, t, k, f | `positional_graphemes`, `word_final` |
| s | word-initial, intervocalic | z | `positional_graphemes` |
| ch | after a, o, u | x | `positional_graphemes`, `after_a` to `after_u` |
| ch | after e, i and other vowels | ç | `positional_graphemes`, `after_e`, `after_i`, `after_vowel` |
| sp, st | word-initial | ʃp, ʃt | `positional_graphemes`, `word_initial` |
| e | unstressed nucleus | ə | `positional_graphemes`, `nucleus_unstressed` |
| er | word-final | ɐ | `positional_graphemes`, `word_final` |
| g | word-final after [ɪ] | ç | allophone rule `DE_FINAL_IG_SPIRANT` |

## Glottal stop

Careful Standard German often puts a glottal stop [ʔ] before a vowel at the start of a word or a stressed syllable, as in `Oase` [ʔoˈʔaːzə] (Kohler 1990). It is not phonemic. It is much more frequent in northern varieties than in the south, and colloquial speech often leaves it out ([German phonology](https://en.wikipedia.org/wiki/German_phonology)). The WikiPron gold does not write it. The spec does not insert it, because the gold would count each inserted [ʔ] as an error.

## References

- Wiese, R. (1996). *The Phonology of German*. Oxford University Press.
- Hall, T.A. (2003). *Phonologie des Deutschen: eine Einführung*. de Gruyter.
- Mangold, M. (2005). *Duden Aussprachewörterbuch* (6th ed.). Dudenverlag.
- Kohler, K.J. (1990). *Illustrations of the IPA: German*. Journal of the International Phonetic Association 20(1).
- Wikipedia: [German phonology](https://en.wikipedia.org/wiki/German_phonology)
- Wikipedia: [German orthography](https://en.wikipedia.org/wiki/German_orthography)

---
[← English](en-GB.md) · [Home](../index.md) · [Faroese →](fo.md)
