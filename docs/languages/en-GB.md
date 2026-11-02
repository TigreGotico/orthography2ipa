# English: British RP (en-GB) & American (en-US) Phonology Reference

**Codes**: `en-GB` (research), `en-US` (research), `en-AU`, `en-CA`, `en-IE`, `en-ZA`, `en-GB-x-scotland` (skeleton) | **Family**: Indo-European > Germanic > West Germanic | **Script**: Latin (alphabet)

This page describes the `en-GB` spec, which models British Received Pronunciation, and the `en-US` spec, which models General American. The registry resolves the bare tag `en` to `en-GB`. The spec `en-US` inherits the grapheme table, the allophones, the grammatical endings, the word exceptions and the stress block of `en-GB`, and states only its own differences. The other English codes are skeleton specs whose parent is `en-GB`.

English has a deep orthography, so the 0.25 PER threshold applies to a promotion (see [quality tiers](../quality_tiers.md#the-per-threshold)). The sources are Wells (1982), Roach (2004), Roach (2009) and Cruttenden (2014), with Fudge (1984), Liberman & Prince (1977) and Hayes (1995) for stress.

## Benchmark

The `wikipron` rows under `en` and `en-GB` are crowd-scraped. The `cmudict` and `ipadict` rows under `en-US` are lexicon-derived. These rows can gate a promotion. The `ipadict` row under `en-GB` and the `ipa_childes` and `ipa_babylm` rows are espeak-derived, so they measure agreement with espeak and cannot gate. The scores are on the [scoreboard](../scoreboard.md).

## Consonant inventory

| Manner | Bilabial | Labiodental | Dental | Alveolar | Post-alv. | Palatal | Velar | Glottal |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Plosive | p b | | | t d | | | k ɡ | |
| Affricate | | | | | tʃ dʒ | | | |
| Fricative | | f v | θ ð | s z | ʃ ʒ | | | h |
| Nasal | m | | | n | | | ŋ | |
| Approximant | w | | | ɹ l | | j | | |

## Stress

English word stress is only partly predictable from the spelling. The `stress` block of `en-GB` states the predictable part and nothing more. Its `notes` give the full argument.

| Field | Value | Source |
|:---|:---|:---|
| `default_position` | 1, the first syllable, the Germanic stem-initial pattern | Fudge 1984, ch. 1 and 2, Cruttenden 2014 §10.4 |
| `antepenult_stress_endings` | ⟨-ical -ity -ities -ify -ifies -iency -ular -graphy -logy -ometer -onomy -ocracy⟩ | Fudge 1984, ch. 3 and 4 |
| `penult_stress_endings` | ⟨-ic -ics -ion -ions⟩ | Fudge 1984, ch. 3 |
| `cliticless_words` | ⟨the a an⟩ | |
| `secondary_stress` | `alternating`, binary feet built leftward from the main stress | Liberman & Prince 1977, Hayes 1995 ch. 3 |

So ⟨ability⟩ gives `əˈbɪlɪti`, ⟨atomic⟩ gives `əˈtɒmɪk` and ⟨combination⟩ gives `ˌkɒmbɪˈnæʃən`. The feet are counted leftward from the main stress. In a five-syllable word with penultimate stress, the secondary stress therefore lands on the second syllable. So ⟨civilization⟩ gives `sɪˌvɪlɪˈzæʃən`, where Hayes's analysis puts it on the first.

The block does not declare the suffixes ⟨-ial -ious -ian -ient -ience⟩. They place stress like ⟨-ic⟩, but the engine gives the wrong vowel quality to the syllables that the shift makes full. So ⟨musician⟩ gives `ˈmʌzɪʃən`. Stress that only the word class decides, as in the noun and the verb ⟨record⟩, is lexical and outside the block.

## Suffixes with a palatal consonant

The ⟨-ion⟩ suffix and its relatives palatalise the stem-final coronal (Chomsky & Halle 1968, with surface values from Wells 2008). The ending carries the [ʃ], not the letter sequence. The spec states these as `grammatical_endings`, never as grapheme keys. So ⟨house⟩ and ⟨mouse⟩, which share letters with ⟨-cious⟩ but have no suffix, are not affected.

| Ending | IPA | Spec output |
|---|---|---|
| ⟨-tion⟩, ⟨-ssion⟩, ⟨-cion⟩, ⟨-cian⟩ | ʃən | ⟨nation⟩ `ˈnæʃən`, ⟨mission⟩ `ˈmɪʃən`, ⟨suspicion⟩ `səˈspɪʃən` |
| ⟨-stion⟩ | stʃən | ⟨question⟩ `ˈkwɛstʃən`, ⟨digestion⟩ `dɪˈdʒɛstʃən` |
| ⟨-tial⟩, ⟨-cial⟩ | ʃəl | ⟨martial⟩ `ˈmɑːʃəl`, ⟨special⟩ `ˈspɛʃəl` |
| ⟨-stial⟩, ⟨-stious⟩ | stʃəl, stʃəs | |
| ⟨-tious⟩, ⟨-cious⟩ | ʃəs | ⟨ambitious⟩ `ˈæmbɪʃəs`, ⟨delicious⟩ `ˈdɛlɪʃəs` |
| ⟨-ture⟩, ⟨-sure⟩, ⟨-ssure⟩ | tʃə, ʒə, ʃə | ⟨nature⟩ `ˈnætʃə`, ⟨measure⟩ `ˈmiːʒə`, ⟨pressure⟩ `ˈpɹɛʃə` |
| ⟨-ous⟩ | əs | ⟨famous⟩ `ˈfæməs` |

Longest match decides between overlapping endings, so ⟨-stion⟩ wins over ⟨-tion⟩. The spec has no entry for ⟨-sion⟩. That ending is [ʒən] after a vowel, as in ⟨vision⟩, and [ʃən] after a consonant, as in ⟨tension⟩. The endings table cannot state that context. So ⟨vision⟩ gives `ˈvɪziən` and ⟨tension⟩ gives `ˈtɛnsiən`.

## C and G softening

The `positional_graphemes` entries for ⟨c⟩, ⟨sc⟩ and ⟨g⟩ give the value before ⟨e i y⟩ and elsewhere.

| Grapheme | Before ⟨e⟩ | Before ⟨i⟩ | Before ⟨y⟩ | Elsewhere | Spec output |
|:---:|:---:|:---:|:---:|:---:|:---|
| c | s | s | s | k | ⟨city⟩ `ˈsɪti`, ⟨cat⟩ `ˈkæt` |
| sc | s | s | s | sk | ⟨scene⟩ `ˈsiːn`, ⟨scale⟩ `ˈskeɪl` |
| g | dʒ, then ɡ | ɡ, then dʒ | dʒ | ɡ | ⟨gem⟩ `ˈdʒɛm`, ⟨gym⟩ `ˈdʒɪm`, ⟨give⟩ `ˈɡɪv` |
| gg | ɡ | ɡ | ɡ | ɡ | ⟨bigger⟩ `ˈbɪɡə` |

The softening of ⟨c⟩ before all three front-vowel letters has almost no exceptions. The vowel after it is a separate question. ⟨cycle⟩ gives `ˈsɪkl` and not [saɪkl], because ⟨y⟩ stands two consonant graphemes away from the mute ⟨e⟩ and falls outside the ⟨VCe⟩ pattern.

The ranking for ⟨g⟩ is a trade, not a correction. Before ⟨i⟩, the Germanic core of the vocabulary keeps the stop (⟨give girl gift begin⟩), and the Romance layer softens (⟨giant magic⟩). Rank 1 can serve only one of them, and it serves the Germanic core. So the Romance words are wrong at rank 1 and right further down the lattice: ⟨giant⟩ gives `ˈɡiænt`. Before ⟨e⟩ the balance runs the other way, because every ⟨-ge⟩ ending is soft (⟨age page huge large change⟩). So ⟨get⟩ and ⟨geese⟩ are the words that the ranking gets wrong: ⟨get⟩ gives `ˈdʒɛt`.

## TH, S and X

| Grapheme | Position | Value | Spec output |
|:---|:---|:---|:---|
| th | word-initial | θ, then ð | ⟨think⟩ `ˈθɪnk`, ⟨three⟩ `ˈθɹiː` |
| th | between vowels | ð | ⟨father⟩ `ˈfæðə`, ⟨either⟩ `ˈiːðə` |
| th | elsewhere | θ | ⟨mouth⟩ `ˈmaʊθ` |
| s | word-initial | s | ⟨seat⟩ `ˈsiːt` |
| s | between vowels | z | ⟨reason⟩ `ˈɹiːzən`, ⟨rose⟩ `ˈɹəʊz` |
| x | word-initial | z | ⟨xylophone⟩ `ˈzɪləfən` |
| x | elsewhere | ks, then ɡz | ⟨fox⟩ `ˈfɒks` |

The function words with [ð] are not predictable from the position. The spec lists ⟨the⟩ and ⟨there⟩ in `word_exceptions`. Other function words take the word-initial [θ], so ⟨this⟩ gives `ˈθɪs` and ⟨they⟩ gives `ˈθiː`. The intervocalic rule also reaches ⟨house⟩ and ⟨mouse⟩, which give `ˈhaʊz` and `ˈmaʊz`. The second-ranked [ɡz] of ⟨x⟩ is the reading that ⟨exact⟩ needs, so ⟨exact⟩ gives `ˈɛksəkt`.

## Inflectional endings

The allophone rules read the regular inflections. The ⟨-ed⟩ ending is [ɪd] after /t d/ (`EN_GB_ED_EPENTHESIS`), loses its vowel elsewhere (`EN_GB_ED_SYNCOPE_AFTER_V`, `EN_GB_ED_SYNCOPE_AFTER_C`), and devoices to [t] after a voiceless consonant (`EN_GB_ED_DEVOICING`). So ⟨hoped⟩ gives `ˈhəʊpt`. The ⟨-es⟩ ending is [ɪz] after a sibilant (`EN_GB_ES_EPENTHESIS`), as in ⟨wishes⟩ `ˈwɪʃɪz`. Final ⟨s⟩ voices after a voiced sound (`EN_GB_FINAL_S_VOICING`). The rules cannot tell an adjective in ⟨-ed⟩ from a past tense, so ⟨wicked⟩ gives `ˈwɪkt`.

## Silent final E (the VCe pattern)

A word-final ⟨e⟩ after a consonant is silent in Modern English. It marks the vowel before it as free rather than checked, as in ⟨mat⟩ against ⟨mate⟩. The spec encodes both halves. The `word_final` entry of ⟨e⟩ deletes the vowel. The `before_mute_e` position sets the vowel quality. The engine gives that position to a vowel grapheme that stands before exactly one consonant grapheme and a word-final mute ⟨e⟩.

| Environment | `a` | `e` | `i` | `o` | `u` |
|:---|:---:|:---:|:---:|:---:|:---:|
| Before mute ⟨e⟩ | eɪ ⟨name⟩ | iː ⟨scene⟩ | aɪ ⟨time⟩ | əʊ ⟨hope⟩ | juː ⟨use⟩ |
| Closed syllable | æ ⟨nam⟩ | ɛ ⟨bet⟩ | ɪ ⟨tim⟩ | ɒ ⟨hop⟩ | ʌ ⟨us⟩ |

A single inflectional ⟨-s⟩ or ⟨-d⟩ is transparent. So ⟨hope⟩, ⟨hopes⟩ and ⟨hoped⟩ all state the same fact about the ⟨o⟩: the suffix attaches outside the stem and cannot reach its nucleus.

Three limits keep the pattern exact. First, two consonant graphemes between the nucleus and the ⟨e⟩ break the split digraph, so ⟨table⟩ gives `ˈtæbl` and ⟨dense⟩ gives `ˈdɛns`. Second, a consonant digraph in that slot also breaks it. The exception is ⟨th⟩, which carries the pattern in ⟨bathe⟩ `ˈbeɪð` and ⟨breathe⟩ `ˈbɹiːð`. The digraph ⟨ck⟩ is the doubling spelling and marks a checked vowel, as in ⟨packed⟩ `ˈpækt`. The digraphs ⟨sh⟩ and ⟨ch⟩ take the ⟨-es⟩ ending, not a mute ⟨e⟩. Third, the free value belongs to a stressed nucleus. The position ranks below the reduction entries that depend on stress, so a weak final syllable still reduces: ⟨climate⟩ gives `ˈklɪmət` and ⟨private⟩ gives `ˈpɹɪvət`.

The word-final ⟨-oing⟩ is the opposite case. It is the ⟨-ing⟩ suffix on a stem that ends in ⟨o⟩, so the two vowel letters belong to different morphemes and stay in hiatus. The rule `EN_GB_OING_HIATUS` restores the hiatus, so ⟨going⟩ gives `ˈɡəʊɪŋ` and ⟨echoing⟩ gives `ˈɛtʃəʊɪŋ`. The rule does not choose the stem vowel, which is lexical. The ⟨do⟩ family has the GOOSE vowel, not GOAT, so ⟨do⟩, ⟨does⟩ and ⟨doing⟩ are whole-word exceptions. The prefixed forms are outside that list and stay wrong: ⟨undoing⟩ gives `ˈʌndəʊɪŋ`.

The `word_exceptions` table holds two closed classes. The first is the function words that end in a pronounced ⟨e⟩: ⟨the be he me we she⟩. The second is the frequent words with a mute ⟨e⟩ and no free vowel, such as ⟨have give live love come some one done none gone⟩. English words never end in ⟨v⟩, so every ⟨-ve⟩ spelling has a mute ⟨e⟩ that says nothing about length.

## British RP vowels (en-GB)

| Wells keyword | IPA (RP) | Example |
|:---:|:---:|:---|
| KIT | ɪ | ⟨kit⟩, ⟨bit⟩ |
| DRESS | ɛ | ⟨dress⟩, ⟨bed⟩ |
| TRAP | æ | ⟨trap⟩, ⟨cat⟩ |
| LOT | ɒ | ⟨lot⟩, ⟨hot⟩ |
| STRUT | ʌ | ⟨strut⟩, ⟨but⟩ |
| FOOT | ʊ | ⟨foot⟩, ⟨put⟩ |
| BATH | ɑː | ⟨bath⟩, ⟨dance⟩, ⟨castle⟩ |
| CLOTH | ɒ | ⟨cloth⟩, ⟨off⟩ |
| NURSE | ɜː | ⟨nurse⟩, ⟨bird⟩, ⟨word⟩ |
| FLEECE | iː | ⟨fleece⟩, ⟨see⟩ |
| FACE | eɪ | ⟨face⟩, ⟨day⟩ |
| PALM | ɑː | ⟨palm⟩, ⟨father⟩ |
| THOUGHT | ɔː | ⟨thought⟩, ⟨law⟩ |
| GOAT | əʊ | ⟨goat⟩, ⟨go⟩ |
| GOOSE | uː | ⟨goose⟩, ⟨blue⟩ |
| PRICE | aɪ | ⟨price⟩, ⟨my⟩ |
| CHOICE | ɔɪ | ⟨choice⟩, ⟨boy⟩ |
| MOUTH | aʊ | ⟨mouth⟩, ⟨now⟩ |

RP is non-rhotic: /ɹ/ occurs only before a vowel. The `EN_GB_NONRHOTIC_*` rules delete the /ɹ/ of an r-coloured vowel before a consonant and at the end of a word. So ⟨car⟩ gives `ˈkɑː`, ⟨hard⟩ gives `ˈhɑːd` and ⟨girl⟩ gives `ˈɡɜːl`. Before a vowel, the `EN_GB_PREVOCALIC_R_*` rules keep the /ɹ/ and shorten the vowel, as in ⟨arrive⟩ `ˈæɹaɪv`. The LOT vowel is rounded [ɒ], as in ⟨hop⟩ `ˈhɒp`.

The spec does not model the TRAP-BATH split. BATH words take the TRAP vowel, so ⟨dance⟩ gives `ˈdæns` and ⟨grass⟩ gives `ˈɡɹæs`. The PALM spelling ⟨alm⟩ is not handled either, so ⟨palm⟩ gives `ˈpælm`. A word-final ⟨y⟩ in a monosyllable is [i] in `en-GB`, so ⟨my⟩ gives `ˈmi`.

## American English (en-US): differences from RP

The `en-US` spec is rhotic. It overrides each `EN_GB_NONRHOTIC_*` rule with a rule that matches nothing, so /ɹ/ stays in every position. The rules `EN_US_NURSE_RCOLOURED` and `EN_US_LETTER_RCOLOURED` write the r-coloured vowels [ɝ] and [ɚ]. So ⟨bird⟩ gives `ˈbɝd` and ⟨butter⟩ gives `ˈbʌtɝ`. The `EN_US_*_NO_LENGTH` rules remove the length mark from the long vowels, so ⟨see⟩-type vowels are [i], as in ⟨feel⟩ `ˈfil`.

The rule `EN_US_LOT_PALM_MERGER` maps /ɒ/ to [ɑ], so ⟨lot⟩ gives `ˈlɑt`. GOAT is [oʊ] through the `en-US` entries for ⟨o⟩, ⟨oa⟩ and ⟨ow⟩, as in ⟨hope⟩ `ˈhoʊp`. The rule `EN_US_FINAL_Y_MONOSYLLABLE` makes a final ⟨y⟩ in a word with no other vowel letter [aɪ], so ⟨my⟩ gives `ˈmaɪ`. General American has no TRAP-BATH split, so ⟨dance⟩ with [æ] is correct for `en-US`.

Two General American features are not modelled. The first is the COT-CAUGHT merger, which most accents have: ⟨caught⟩ keeps [ɔ]. The second is flapping. General American flaps /t/ and /d/ to [ɾ] between vowels when the next vowel is unstressed:

| Word | RP | General American |
|:---|:---:|:---:|
| ⟨butter⟩ | [bʌtə] | [bʌɾɚ] |
| ⟨water⟩ | [wɔːtə] | [wɑːɾɚ] |
| ⟨city⟩ | [sɪti] | [sɪɾi] |
| ⟨ladder⟩ | [lædə] | [læɾɚ] |
| ⟨rider⟩, ⟨writer⟩ | [ˈɹaɪdə], [ˈɹaɪtə] | [ˈɹaɪɾɚ], merged |

The `en-US` spec has no flapping entry, so ⟨butter⟩ keeps its [t].

## Allophones the specs do not write

Both specs give a broad transcription. They do not write these allophones, which the reference grammars describe:

| Phoneme | Allophone | Environment | Example |
|:---:|:---:|:---|:---|
| /p t k/ | [pʰ tʰ kʰ] | Word-initial or stressed onset | ⟨pin⟩ [pʰɪn] |
| /p/ | [p̚] | Word-final, unreleased | ⟨tap⟩ [tæp̚] |
| /t/ | [ʔ] | Before syllabic /n/ or word-final, in contemporary RP | ⟨button⟩ [bʌʔn̩] |
| /t/ | [ɾ] | Between vowels before an unstressed vowel, American only | ⟨butter⟩ [bʌɾɚ] |
| /l/ | [l] | Syllable onset, clear l | ⟨leaf⟩ [liːf] |
| /l/ | [ɫ] | Syllable coda, dark l | ⟨feel⟩ [fiːɫ] |

## References

- Wells, J.C. (1982). *Accents of English*, vols. 1-2. Cambridge University Press.
- Roach, P. (2004). British English: Received Pronunciation. *Journal of the International Phonetic Association*, 34(2), 239-245.
- Roach, P. (2009). *English Phonetics and Phonology* (4th ed.). Cambridge University Press.
- Cruttenden, A. (ed.) (2014). *Gimson's Pronunciation of English* (8th ed.). Routledge.
- Chomsky, N. & Halle, M. (1968). *The Sound Pattern of English*. Harper & Row.
- Wells, J.C. (2008). *Longman Pronunciation Dictionary* (3rd ed.). Pearson Longman.
- Fudge, E. (1984). *English Word-Stress*. George Allen & Unwin.
- Liberman, M. & Prince, A. (1977). On stress and linguistic rhythm. *Linguistic Inquiry*, 8(2), 249-336.
- Hayes, B. (1995). *Metrical Stress Theory*. University of Chicago Press.
- Wikipedia: [English phonology](https://en.wikipedia.org/wiki/English_phonology), [General American](https://en.wikipedia.org/wiki/General_American_English)

---
[← Comparative phonology](comparative.md) · [Home](../index.md) · [German →](de-DE.md)
