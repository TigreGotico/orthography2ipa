# Faroese (`fo`)

Føroyskt, ~50,000 speakers in the Faroe Islands. West Scandinavian, closest
living relative Icelandic. The orthography is Hammershaimb's 19th-century
etymological norm: it was designed to keep the spelling close to Old West
Norse and to Icelandic, not to the modern spoken sound, so a compositional
letter-by-letter reading of a Faroese word is usually wrong. The spec leans
on positional grapheme rules and allophone rules rather than a flat
grapheme table for that reason.

## Orthographic depth and production threshold

**Deep orthography, the ≤ 0.25 PER production threshold applies** (see
[quality tiers](../quality_tiers.md)). The written form under-determines
quantity (vowel length and quality both alternate with syllable structure
but only the syllable structure is written), the stop series (voicing is
written where the contrast is aspiration), and the two segments spelled
⟨g⟩ and ⟨ð⟩ each cover several distinct surface realisations chosen by
position. None of this is dialectal noise; it is the norm working as
designed, three centuries after the sound system it was fixed to moved on.

## Phonology (as encoded)

- **Quantity.** Every stressed vowel letter has two realisations that
  differ in quality, not only in length: the long value in an open
  stressed syllable, the short value before a geminate or a consonant
  cluster (⟨a⟩ [ɛaː]/[a], ⟨á⟩ [ɔaː]/[ɔ], ⟨e⟩ [eː]/[ɛ], ⟨i y⟩ [iː]/[ɪ],
  ⟨í ý⟩ [ʊiː]/[ʊj], ⟨o⟩ [oː]/[ɔ], ⟨ó⟩ [ɔuː]/[œ], ⟨u⟩ [uː]/[ʊ], ⟨ú⟩
  [ʉuː]/[ʏ], ⟨ø⟩ [øː]/[œ]). The long values sit in `nucleus_stressed`;
  shortening before a cluster is an `allophone_rules` entry per vowel.
- **Stops.** No voicing contrast: ⟨b d g⟩ are the unaspirated stops
  [p t k]. ⟨p t k⟩ are aspirated only in the word-initial onset — medial
  or post-⟨s⟩ they are plain. ⟨pp tt kk⟩ are preaspirated [ʰpp ʰtt ʰkk].
- **Palatalisation.** ⟨k g sk⟩ become [tʃʰ tʃ ʃ] before ⟨e i y⟩ and in the
  digraphs ⟨kj gj ggj skj sj⟩. ⟨í ý⟩ do not trigger it — they pattern as
  the back-onset diphthong [ʊi], not a front vowel. The inherited
  diphthong spellings ⟨kei koy gei goy skei skoy⟩ block it and keep the
  velar; ⟨ey⟩ does not block it (⟨geykur⟩ [tʃɛiːkʊɹ], not [kɛiːkʊɹ]).
  ⟨hj⟩ is [j].
- **Skerping.** ⟨ógv úgv⟩ are [ɛkv]/[ɪkv] — the vowel changes quality and
  a stop is inserted, which no compositional reading gives, so they are
  encoded as grapheme units rather than derived.
- **Rhotic.** /r/ is the alveolar approximant [ɹ], not a trill.
- **⟨ð⟩.** Silent by default; the glide [j] between vowels, with [v] and
  [w] as further allophones. [j] is the 1-best output. WikiPron gold
  favours [w] specifically after a rounded vowel and [v]/[j] elsewhere,
  but no cited source states that conditioning and the spec does not
  encode it.
- **Stress.** Categorically word-initial; the acute-accented letters mark
  vowel quality, not stress placement.

## Benchmark (full gold set, no cap)

| dataset | provenance | n | PER |
|---|---|---:|---:|
| `wikipron` | crowd-scraped | 2957 | **0.1679** |

The qualifying row is `wikipron` (crowd-scraped, gate-eligible), below the
0.25 deep-orthography threshold.

## Known limitations

- **Compound secondary stress is the largest remaining error class.**
  `nucleus_stressed` fires only on the word-initial syllable, so a second
  or later stem in a compound never receives its long vowel. Of the gold
  rows with two or more IPA length marks, 352 of 354 come out short for
  exactly this reason. Fixing it needs a compound-boundary detector the
  engine does not currently have.
- Retroflex assimilation of ⟨rn rs rt rl rd⟩, and the stop insertion that
  turns ⟨rn⟩ into [tn], are both real and both variable in the gold
  (⟨Arnar⟩ is [aɻɳaɹ] while ⟨Arinbjørn⟩ ends [pjœtn]); encoding either one
  as categorical would state something the sources do not support, so
  neither is encoded.
- Danish loanwords keep unpalatalised velars and plain [a] where a native
  word would palatalise or diphthongise, and the spec has no loan lexicon
  to separate the two strata.
- The short ⟨ú⟩ value [ʏ] is correct and used as an output symbol, but ʏ
  is missing from the engine's general vowel-classification set (task
  #72); the spec never relies on it as a rule condition, so it does not
  depend on that gap closing.

## Sources

- Árnason, K. *The Phonology of Icelandic and Faroese*. Oxford University Press, 2011.
- Þráinsson, H., Petersen, H. P., Jacobsen, J. í L. & Hansen, Z. S. *Faroese: An Overview and Reference Grammar*. Føroya Fróðskaparfelag, 2004.
- Lockwood, W. B. *An Introduction to Modern Faroese*. Munksgaard, 1955.
