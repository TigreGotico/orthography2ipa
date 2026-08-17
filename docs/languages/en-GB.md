# English: British RP (en-GB) & American (en-US) Phonology Reference

**Codes**: `en-GB`, `en-US`, `en-AU`, `en-CA`, `en-IE`, `en-ZA`, `en-GB-x-scotland`
**Family**: Indo-European > Germanic > West Germanic | **Script**: Latin (alphabet)
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

### Palatalized suffixes (`grammatical_endings`)

The `-ion` suffix palatalizes the stem-final coronal (Chomsky & Halle 1968;
surface values per Wells 2008 LPD), so the ending — not the letter sequence —
carries the [ʃ]:

| Ending | Realization | Examples |
|---|---|---|
| ⟨-tion⟩, ⟨-ssion⟩, ⟨-cion⟩, ⟨-cian⟩ | [ʃən] | `nation`, `mission`, `suspicion`, `musician` |
| ⟨-stion⟩ | [stʃən] | `question`, `digestion` (longest match beats ⟨-tion⟩) |
| ⟨-tial⟩, ⟨-cial⟩ | [ʃəl] | `martial`, `special` |
| ⟨-tious⟩, ⟨-cious⟩ | [ʃəs] | `ambitious`, `delicious` |

These are word-ending entries, never grapheme keys: `house` and `mouse` share
letters with ⟨-cious⟩ but have no suffix, so nothing fires. ⟨-sion⟩ is
deliberately absent — it is [ʒən] after a vowel (`vision`) and [ʃən] after a
consonant (`tension`), a context this table does not express.

### C and G Softening

| Grapheme | Before ⟨e⟩ | Before ⟨i⟩ | Before ⟨y⟩ | Elsewhere | Examples |
|:---:|:---:|:---:|:---:|:---:|:---|
| c | [s] | [s] | [s] | [k] | `city` [sɪti], `cycle` [sɪkl], `cat` [kæt] |
| sc | [s] | [s] | [s] | [sk] | `scene` [siːn], `scale` [skeɪl] |
| g | [dʒ] | [ɡ] | [dʒ] | [ɡ] | `gem` [dʒɛm], `gym` [dʒɪm] vs. `give` [ɡɪv], `girl` [ɡɜːl] |
| gg | [ɡ] | [ɡ] | [ɡ] | [ɡ] | `bigger` [bɪɡə], `dagger` [dæɡə] |

⟨c⟩ softens on all three front-vowel letters and is near-exceptionless.
The vowel it leaves behind is a separate question: `cycle` comes out [sɪkl]
rather than [saɪkl], because ⟨y⟩ before ⟨cl⟩ is two consonant graphemes away
from the mute ⟨e⟩ and so falls outside ⟨VCe⟩.

⟨g⟩ is not near-exceptionless, and its ranking is a TRADE rather than a
correction. Before ⟨i⟩ the Germanic core of the vocabulary keeps the plosive
(`give`, `girl`, `gift`, `begin`, `girth`, `gild`) and the Romance stratum
softens (`giant`, `magic`, `ginger`); rank 1 can only serve one of them, and
it serves the Germanic core, so the Romance words are wrong at rank 1 and
right further down the lattice. Before ⟨e⟩ the balance runs the other way —
every ⟨-ge⟩ ending (`age`, `page`, `huge`, `large`, `change`) is soft — so
`get` and `geese` are the residue that ranking gets wrong. ⟨gg⟩ is hard
regardless of what follows.

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
English, and it marks the preceding vowel as free rather than checked (`mat`
vs. `mate`). Both halves of that alternation are encoded. The deletion is the
`e` grapheme's `word_final` entry; the vowel quality is the `before_mute_e`
position, which the engine emits on a vowel grapheme standing before exactly
one consonant grapheme and a word-final mute `<e>`.

| Environment | `a` | `e` | `i` | `o` | `u` |
|:---|:---:|:---:|:---:|:---:|:---:|
| Before mute `<e>` | eɪ `name` | iː `scene` | aɪ `time` | əʊ `hope` | juː `use` |
| Closed syllable | æ `nam` | ɛ `bet` | ɪ `tim` | ɒ `hop` | ʌ `us` |

A single inflectional `<-s>` or `<-d>` counts as transparent, so `hope`,
`hopes` and `hoped` all state the same fact about the `<o>`: the suffix
attaches outside the stem and cannot reach back into its nucleus.

Three boundaries keep the pattern honest. Two consonant graphemes between
the nucleus and the `<e>` is no longer the split digraph, which is what
leaves `table` and `dense` alone. A consonant DIGRAPH in that slot is
likewise excluded, with `<th>` the one exception that genuinely carries the
pattern (`bathe`, `breathe`, `scythe`): `<ck>` is the consonant-doubling
allograph and marks a checked vowel (`wicked`, `packed`), and `<sh>`/`<ch>`
take the epenthetic `<-es>` ending rather than a mute `<e>` (`wishes`,
`watches`). And the free value belongs to a stressed nucleus, so the
position is ranked below the stress-conditioned reduction entries and a weak
final syllable still reduces (`climate` [klɪmət], `private` [pɹɪvət]).

The `<-oing>` spelling is the mirror case: word-final `<-oing>` is the
`<-ing>` suffix on a stem that already ended in `<o>`, so the two letters
belong to different morphemes and stay in hiatus (`going`, `echoing`,
`shoeing`). The rule restores the hiatus only — which vowel the stem then
takes is lexical, and for the `<do>` family it is GOOSE rather than GOAT.
`do`, `does` and `doing` are whole-word overrides for that reason; the
prefixed `undoing`/`redoing`/`outdoing` sit outside what a whole-word list
holds and stay wrong.

**Handled exceptions**: the small closed class of function words genuinely
ending in a pronounced `<e>` (`the`, `be`, `he`, `me`, `we`, `she`) is carved
out of the blanket word-final rule via a `word_exceptions` whole-word
override, as is the closed class of high-frequency words that carry the mute
`<e>` without the free vowel — `have`, `give`, `live`, `love`, `come`,
`some`, `one`, `done`, `none`, `gone` and their neighbours. `<v>` cannot end
an English word, so every `<-ve>` spelling carries a mute `<e>` that makes no
claim about length at all.

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

## American English (en-US): Key Differences from RP

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
- **TRAP-BATH**: no split. BATH words use /æ/ (`dance` [dæns])

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
