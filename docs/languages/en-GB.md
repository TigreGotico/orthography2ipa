# English — British RP (en-GB) & American (en-US) Phonology Reference

**Codes**: `en-GB`, `en-US`, `en-AU`, `en-CA`, `en-IE`, `en-ZA`, `en-GB-x-scotland`
**Family**: Indo-European > Germanic | **Script**: Latin (alphabet)
**Quality tier**: research | **Orthographic depth**: deep (production threshold ≤ 0.25 PER)
**Sources**: Wells (1982), Roach (2009), Roach (2004, JIPA), Cruttenden (2014)

**Lexical stress**: not encoded as a declarative `stress` block. English word
stress is lexically contrastive (`record` noun vs. `record` verb) rather than
reliably orthography-predictable, so it is exempt from the research-tier
stress requirement per `docs/quality_tiers.md`.

---

## Consonant Inventory

| Manner | Bilabial | Labiodental | Dental | Alveolar | Post-alv. | Palatal | Velar | Glottal |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Plosive | p b | | | t d | | | k ɡ | |
| Affricate | | | | | tʃ dʒ | | | |
| Fricative | | f v | θ ð | s z | ʃ ʒ | | | h |
| Nasal | m | | | n | | | ŋ | |
| Approximant | w | | | ɹ l | | j | | |

---

## Key Positional Rules

### C and G Softening

| Grapheme | Before e/i/y | Elsewhere | Examples |
|:---:|:---:|:---:|:---|
| c | [s] | [k] | `city` [sɪti], `cycle` [saɪkl], `cat` [kæt] |
| g | [dʒ] / [ɡ] | [ɡ] | `gem` [dʒɛm], `gin` [dʒɪn] vs. `get` [ɡɛt], `give` [ɡɪv] |

**Note**: The g-softening has many exceptions — native Germanic words (get, give, girl, gift) retain [ɡ] before e/i. The [dʒ] realization is common in French/Latin loanwords (gem, giraffe, ginger).

### TH: [θ] vs [ð] Distribution

| Pattern | Realization | Examples |
|:---|:---:|:---|
| Content words (nouns, verbs, adj.) | [θ] | `think`, `three`, `mouth` |
| Function words (determiners, pronouns) | [ð] | `the`, `this`, `there`, `they` |
| Intervocalic (medial) | [ð] | `father`, `weather`, `either` |
| Word-final after vowel | [ð] | `breathe`, `bathe`, `loathe` |

### Intervocalic S

| Environment | Realization | Examples |
|:---|:---:|:---|
| Between vowels | [z] | `rose` [ʁɒz], `nose` [nɒz], `reason` |
| Word-initial | [s] | `seat`, `sun`, `see` |
| After voiceless consonant | [s] | `maps` [mæps], `cats` [kæts] |

### Silent Final E (VCe Pattern)

Word-final orthographic `<e>` after a consonant is not pronounced in Modern
English; historically it marked the preceding vowel as tense/long (`mat` vs.
`mate`). Only the deletion half of that alternation is encoded — the engine's
positional grapheme model resolves a single grapheme against its own position
and has no lookback to the preceding vowel nucleus, so the vowel-quality shift
itself (`mat` [mæt] -> `mate` [meɪt]) is a known engine-limit exception, not
an encoded rule.

| Word | Pred. | Note |
|:---|:---:|:---|
| `hope` | hɒp | final `e` deleted; vowel unchanged (engine limit) |
| `time` | tɪm | final `e` deleted; vowel unchanged (engine limit) |
| `nation` | næʃən | `-tion` suffix, see below |

**Handled exception**: the small closed class of function words genuinely
ending in a pronounced `<e>` (`the`, `be`, `he`, `me`, `we`, `she`) is carved
out of the blanket word-final rule via a `word_exceptions` whole-word
override (`the` [ðə], `be` [biː], `he` [hiː], `me` [miː], `we` [wiː], `she`
[ʃiː]).

### TION/SION Suffix Family

| Grapheme | IPA | Examples |
|:---:|:---:|:---|
| `tion` | ʃən | `nation`, `station`, `action` |
| `cian` | ʃən | `magician`, `musician` |
| `ssion` | ʃən | `mission` [mɪʃən], `passion` [pæʃən] |
| `sion` (after a vowel) | ʒən | `vision` [vɪʒən], `division` [dɪvɪʒən] |
| `sion` (after a consonant) | ʃən | `tension` [tɛnʃən], `mansion` [mænʃən] |
| `tial` / `cial` | ʃəl | `martial`, `special` |
| `cious` / `tious` | ʃəs | `delicious`, `cautious` |

The `ssion` spelling is matched as its own grapheme (maximal-munch
tokenization picks the 5-character `ssion` over the 4-character `sion`), and
plain `sion` is conditioned on the preceding token via the engine's
`positional_graphemes` AFTER_VOWEL / AFTER_CONSONANT context.

### X Word-Initial

| Environment | Realization | Examples |
|:---|:---:|:---|
| Word-initial | [z] | `xylophone` [zaɪlɒfɒn], `Xerox` [zɪɹɒks] |
| Elsewhere | [ks] | `fox` [fɒks], `exact` [ɪɡzækt] |

---

## British RP Vowel System (en-GB)

### Monophthongs

| Wells keyword | IPA (RP) | Example |
|:---:|:---:|:---|
| KIT | ɪ | `kit`, `bit` |
| DRESS | ɛ | `dress`, `bed` |
| TRAP | æ | `trap`, `cat` |
| LOT | ɒ | `lot`, `hot` (rounded in RP) |
| STRUT | ʌ | `strut`, `but` |
| FOOT | ʊ | `foot`, `put` |
| BATH | ɑː | `bath`, `dance`, `castle` (TRAP-BATH split) |
| CLOTH | ɒ | `cloth`, `off` |
| NURSE | ɜː | `nurse`, `bird`, `word` |
| FLEECE | iː | `fleece`, `see` |
| FACE | eɪ | `face`, `day` |
| PALM | ɑː | `palm`, `father` |
| THOUGHT | ɔː | `thought`, `law` |
| GOAT | əʊ | `goat`, `go` |
| GOOSE | uː | `goose`, `blue` |
| PRICE | aɪ | `price`, `my` |
| CHOICE | ɔɪ | `choice`, `boy` |
| MOUTH | aʊ | `mouth`, `now` |

**RP-specific features**:
- **Non-rhotic**: /ɹ/ only before vowels (`red`, `arrive`), not before consonants or word-finally (`car`, `hard`)
- **TRAP-BATH split**: BATH words use /ɑː/ in RP (`dance`, `grass`, `castle`)
- **LOT rounding**: /ɒ/ is rounded (unlike many American English dialects)

---

## American English (en-US) — Key Differences from RP

### Flapping (T/D Tapping)

American English **flaps** /t/ and /d/ to [ɾ] in unstressed intervocalic position:

| Word | RP | GenAm |
|:---|:---:|:---:|
| `butter` | [bʌtə] | [bʌɾɚ] |
| `water` | [wɔːtə] | [wɑːɾɚ] |
| `city` | [sɪti] | [sɪɾi] |
| `ladder` | [lædə] | [læɾɚ] |
| `rider` / `writer` | [ˈɹaɪdə] / [ˈɹaɪtə] | [ˈɹaɪɾɚ] (merged) |

Encoded as:
```json
"t": {"intervocalic": ["ɾ"], "word_initial": ["tʰ"], "default": ["t"]},
"d": {"intervocalic": ["ɾ"], "default": ["d"]}
```

### Other American Features
- **Rhotic**: /ɹ/ retained in all positions (`car` [kɑːɹ], `bird` [bɝːd])
- **LOT-PALM merge**: `lot` and `palm` → [ɑ]
- **COT-CAUGHT merge**: `cot` and `caught` → [ɑ] (in most accents)
- **TRAP-BATH**: no split; BATH words use /æ/ (`dance` [dæns])

---

## Allophones

| Phoneme | Allophone | Environment | Example |
|:---:|:---:|:---|:---|
| /p/ | [pʰ] | Word-initial / stressed onset | `pin` [pʰɪn] |
| /p/ | [p̚] | Word-final (unreleased) | `tap` [tæp̚] |
| /t/ | [tʰ] | Word-initial / stressed onset | `tin` [tʰɪn] |
| /t/ | [ʔ] | Before syllabic n / word-final (T-glottaling, contemporary RP) | `button` [bʌʔn̩] |
| /t/ | [ɾ] | Intervocalic unstressed (American only) | `butter` [bʌɾɚ] |
| /l/ | [l] | Syllable onset (clear l) | `leaf` [liːf] |
| /l/ | [ɫ] | Syllable coda (dark l) | `feel` [fiːɫ] |
| /k/ | [kʰ] | Word-initial / stressed onset | `key` [kʰiː] |

---

## References

- Wells, J.C. (1982). *Accents of English*, vols. 1–2. Cambridge University Press.
- Roach, P. (2009). *English Phonetics and Phonology* (4th ed.). Cambridge University Press.
- Roach, P. (2004). British English: Received Pronunciation. *Journal of the International Phonetic Association*, 34(2), 239-245.
- Cruttenden, A. [ed.] (2014). *Gimson's Pronunciation of English* (8th ed.). Routledge.
- Wikipedia: [English phonology](https://en.wikipedia.org/wiki/English_phonology), [General American](https://en.wikipedia.org/wiki/General_American_English)

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [germanic](germanic.md), [de-DE](de-DE.md)*
