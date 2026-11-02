# Faroese (`fo`)

**Code**: `fo` | **Family**: Indo-European > Germanic > North Germanic (West Scandinavian) | **Script**: Latin (alphabet) | **Quality tier**: production

Faroese (føroyskt) is the language of the Faroe Islands, and Icelandic is its closest living relative. The orthography is the etymological norm of Hammershaimb from the 19th century. It keeps the spelling close to Old West Norse and to Icelandic, not to the modern spoken sound. So a letter-by-letter reading of a Faroese word is usually wrong. For this reason, the spec depends on positional grapheme rules and allophone rules more than on its flat grapheme table.

## Orthographic depth and production threshold

Faroese has a deep orthography, so the 0.25 PER production threshold applies (see [quality tiers](../quality_tiers.md#the-per-threshold)). The written form does not fully determine quantity. Vowel length and vowel quality both alternate with syllable structure, and only the syllable structure is written. The spelling writes voicing on the stops, but the contrast is aspiration. The letters ⟨g⟩ and ⟨ð⟩ each cover several surface forms, and position selects among them. This is not dialect noise. It is the norm as designed, fixed to a sound system that has since changed.

## Phonology as encoded

### Quantity

Every stressed vowel letter has two values that differ in quality, not only in length. The long value occurs in an open stressed syllable. The short value occurs before a geminate or a consonant cluster. The long values are `nucleus_stressed` entries in `positional_graphemes`. A `FO_SHORTEN_*` allophone rule for each vowel shortens it before a consonant cluster.

| Letter | Long | Short |
|:---:|:---:|:---:|
| ⟨a⟩ | [ɛaː] | [a] |
| ⟨á⟩ | [ɔaː] | [ɔ] |
| ⟨e⟩ | [eː] | [ɛ] |
| ⟨i y⟩ | [iː] | [ɪ] |
| ⟨í ý⟩ | [ʊiː] | [ʊj] |
| ⟨o⟩ | [oː] | [ɔ] |
| ⟨ó⟩ | [ɔuː] | [œ] |
| ⟨u⟩ | [uː] | [ʊ] |
| ⟨ú⟩ | [ʉuː] | [ʏ] |
| ⟨ø⟩ | [øː] | [œ] |

### Stops

Faroese has no voicing contrast in its stops. The spec reads ⟨b d g⟩ as the unaspirated stops [p t k]. It reads ⟨p t k⟩ as aspirated only at the start of a word, and as plain elsewhere. The geminates ⟨pp tt kk⟩ are preaspirated [ʰpp ʰtt ʰkk].

### Palatalisation

Before ⟨e i y⟩, the spec reads ⟨k g sk⟩ as [tʃʰ tʃ ʃ]. The digraphs ⟨kj gj ggj skj sj⟩ give the same palatal values, and ⟨hj⟩ is [j]. The letters ⟨í ý⟩ do not cause palatalisation, because they pattern as the back-onset diphthong [ʊi]. The spec has separate entries for ⟨kí gí skí⟩ and their ⟨ý⟩ forms, which keep the velar.

The inherited diphthong spellings ⟨kei koy gei goy skei skoy⟩ also block palatalisation and keep the velar. The spelling ⟨ey⟩ does not block it:

```python
>>> import orthography2ipa as o
>>> [o.transcribe(w, "fo") for w in ["geykur", "keisari", "kirkja"]]
['ˈtʃɛiːkʊɹ', 'ˈkʰaiːsaɹɪ', 'ˈtʃʰɪɹtʃʰa']
```

### Other segments

The sequences ⟨ógv úgv⟩ are [ɛkv] and [ɪkv]. The vowel changes quality and a stop is inserted, which no letter-by-letter reading gives. So the spec stores them as grapheme units.

The rhotic /r/ is the alveolar approximant [ɹ], not a trill. The spec reads ⟨ll⟩ as [tl] first and ⟨nn⟩ as [nn] first, with [ll] and [tn] as second candidates.

The letter ⟨ð⟩ is silent by default. Between vowels the spec gives the glide [j] first, with [v] and [w] as further candidates. The WikiPron gold prefers [w] after a rounded vowel and [v] or [j] elsewhere. No cited source states that condition, so the spec does not encode it. Between vowels, ⟨g⟩ also gives [j] first and [v] second.

### Stress

Stress falls on the first syllable of every word. The acute-accented letters mark vowel quality, not stress, and the `stress` block puts the stress on the first syllable.

## Benchmark

The `wikipron` row is crowd-scraped and is the row that qualifies `fo` for production. See the [scoreboard](../scoreboard.md) for its score.

## Known limitations

Compound secondary stress is the largest open class of error. The `nucleus_stressed` position fires only on the first syllable of the word. So a second or later stem in a compound never gets its long vowel. Almost all gold rows with two or more length marks come out short for this reason. A fix needs a detector for compound boundaries, and the engine has none.

Two cluster processes are real but vary in the gold. One is retroflex assimilation of ⟨rn rs rt rl rd⟩. The other is the stop insertion that turns ⟨rn⟩ into [tn]. For example, ⟨Arnar⟩ is [aɻɳaɹ], and ⟨Arinbjørn⟩ ends in [pjœtn]. The spec encodes neither, because a categorical rule would state more than the sources support.

Danish loanwords keep plain velars and plain [a] where a native word would palatalise or diphthongise. The spec has no loan lexicon to separate the two layers of vocabulary.

## Sources

- Árnason, K. *The Phonology of Icelandic and Faroese*. Oxford University Press, 2011.
- Þráinsson, H., Petersen, H. P., Jacobsen, J. í L. & Hansen, Z. S. *Faroese: An Overview and Reference Grammar*. Føroya Fróðskaparfelag, 2004.
- Lockwood, W. B. *An Introduction to Modern Faroese*. Munksgaard, 1955.

---
[← German](de-DE.md) · [Home](../index.md) · [Spanish →](es-ES.md)
