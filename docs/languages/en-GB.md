# British English (RP) (`en-GB`)

<!-- atlas:summary begin -->
British English (RP) is a West Germanic language, written in the Latin script. Its code names United Kingdom. The `en-GB` spec is at the research tier. It cites 13 sources and has 4 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `en-GB` |
| Aliases | `eng` |
| ISO 639-3 | [eng](https://iso639-3.sil.org/code/eng), English |
| Glottolog | [stan1293](https://glottolog.org/resource/languoid/id/stan1293), English |
| Wikidata | [Q7979](https://www.wikidata.org/wiki/Q7979) |
| Wikipedia | [British English](https://en.wikipedia.org/wiki/British_English) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [United Kingdom](by-region.md#united-kingdom) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Ancestor | [Middle English](https://tigregotico.github.io/orthography2ipa/#enm) `enm` |
| Child lects | 7, see [Related lects](#related-lects) |
| Explorer | [`en-GB` in the data explorer](https://tigregotico.github.io/orthography2ipa/#en-GB) |
| Spec file | [`en-GB.json`](../../orthography2ipa/data/en-GB.json) |
<!-- atlas:header end -->

## Overview

This page describes the `en-GB` spec, which models British Received Pronunciation, and the `en-US` spec, which models General American. The registry resolves the bare tag `en` to `en-GB`. The spec `en-US` inherits the grapheme table, the allophones, the grammatical endings, the word exceptions and the stress block of `en-GB`, and states only its own differences. The other English codes are skeleton specs whose parent is `en-GB`.

English has a deep orthography, so the 0.25 PER threshold applies to a promotion (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)). The sources are Wells (1982), Roach (2004), Roach (2009) and Cruttenden (2014), with Fudge (1984), Liberman & Prince (1977) and Hayes (1995) for stress.

## Benchmark

The `wikipron` rows under `en` and `en-GB` are crowd-scraped. The `cmudict` and `ipadict` rows under `en-US` are lexicon-derived. These rows can gate a promotion. The `ipadict` row under `en-GB` and the `ipa_childes` and `ipa_babylm` rows are espeak-derived, so they measure agreement with espeak and cannot gate. The scores are on the [scoreboard](../evaluation/generated/scoreboard.md).

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
| MOUTH | aʊ | ⟨mouth⟩, ⟨cow⟩ |

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

<!-- atlas:lects begin -->
## Related lects

These specs name `en-GB` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Australian English](https://tigregotico.github.io/orthography2ipa/#en-AU) `en-AU`: Australia, skeleton tier
- [Canadian English](https://tigregotico.github.io/orthography2ipa/#en-CA) `en-CA`: Canada, skeleton tier
- [Krio](kri.md) `kri`: Gambia, Guinea, Senegal, Sierra Leone, United States, research tier
- [Irish English (Hiberno-English)](https://tigregotico.github.io/orthography2ipa/#en-IE) `en-IE`: Ireland, skeleton tier
- [South African English](https://tigregotico.github.io/orthography2ipa/#en-ZA) `en-ZA`: South Africa, skeleton tier
- [Scottish English](https://tigregotico.github.io/orthography2ipa/#en-GB-x-scotland) `en-GB-x-scotland`: United Kingdom, skeleton tier
- [American English (General American)](en-US.md) `en-US`: United States, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 13 works. 3 of them have a DOI or a URL. The spec file holds a note on what 9 of them support.

1. <a id="src-wells1982_vol1"></a>Wells, J.C. (1982). *Accents of English, Vol. 1: An Introduction*. Cambridge University Press.
2. <a id="src-wells1982_vol2"></a>Wells, J.C. (1982). *Accents of English, Vol. 2: The British Isles*. Cambridge University Press.
3. <a id="src-roach2009"></a>Roach, P. (2009). *English Phonetics and Phonology: A Practical Course (4th ed.)*. Cambridge University Press.
4. <a id="src-gimson2014"></a>Cruttenden, A. (ed.) (2014). *Gimson's Pronunciation of English (8th ed.)*. Routledge.
5. <a id="src-roach2004_jipa"></a>Roach, P. (2004). *British English: Received Pronunciation*. Journal of the International Phonetic Association, 34(2), 239-245. Cited: 239-245. [doi.org](https://doi.org/10.1017/S0025100304001768)
6. <a id="src-gontijo2003"></a>Gontijo, P.F.D., Gontijo, I., & Shillcock, R. (2003). *Grapheme-phoneme probabilities in British English*. Behavior Research Methods, Instruments, & Computers, 35(1), 136-157. Cited: 136-157. [doi.org](https://doi.org/10.3758/BF03195506)
7. <a id="src-berndt1987"></a>Berndt, R.S., Reggia, J.A., & Mitchum, C.C. (1987). *Empirically derived probabilities for grapheme-to-phoneme correspondences in English*. Behavior Research Methods, Instruments, & Computers, 19(1), 1-9. Cited: 1-9. [doi.org](https://doi.org/10.3758/BF03207663)
8. <a id="src-carney1994"></a>Carney, E. (1994). *A Survey of English Spelling*. Routledge.
9. <a id="src-chomsky_halle1968"></a>Chomsky, N. & Halle, M. (1968). *The Sound Pattern of English*. Harper & Row.
10. <a id="src-wells2008"></a>Wells, J.C. (2008). *Longman Pronunciation Dictionary (3rd ed.)*. Pearson Longman.
11. <a id="src-fudge1984"></a>Fudge, E. (1984). *English Word-Stress*. George Allen & Unwin.
12. <a id="src-liberman_prince1977"></a>Liberman, M. & Prince, A. (1977). *On Stress and Linguistic Rhythm*. Linguistic Inquiry 8(2), 249-336.
13. <a id="src-hayes1995"></a>Hayes, B. (1995). *Metrical Stress Theory: Principles and Case Studies*. University of Chicago Press.
<!-- atlas:sources end -->

### Notes on the sources

The page also draws on two Wikipedia articles that the spec does not cite: [English phonology](https://en.wikipedia.org/wiki/English_phonology) and [General American](https://en.wikipedia.org/wiki/General_American_English).

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `en` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 80985 | 0.2655 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `en-GB` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 81535 | 0.2327 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `en-GB` | generated | espeak-derived | CC BY 4.0 | 11445 | 0.3000 | no |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `en-GB` | generated | espeak-derived | MIT, each file its own | 65117 | 0.2221 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 112 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b b̥ p pʰ p̚ |  |  | d d̥ d̪ t tʰ |  |  | k kʰ k̚ ɡ ɡ̊ | ʔ |
| Affricate |  |  |  |  | dʒ dʒ̊ tʃ |  |  |  |
| Nasal | m | ɱ |  | n n̪ |  |  | ŋ |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative |  | f v v̥ | ð θ | s z z̥ | ʃ ʒ ʒ̊ |  |  | h ɦ |
| Approximant |  |  |  | ɹ |  | j |  |  |
| Lateral approximant |  |  |  | l ɫ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ʉː | uː |
| Near-close | ɪ |  | ʊ |
| Mid |  | ə |  |
| Open-mid | ɛ | ɜː | ɔː ʌ |
| Near-open | æ | ɐ |  |
| Open |  |  | ɑ ɑː ɒ |

Sequences that the spec writes as one unit: [aɪ] [aɪə] [aɪəɹ] [aʊ] [aʊə] [aʊəɹ] [eɪ] [juː] [jʊə] [jʊəɹ] [ks] [kw] [ndʒ] [sk] [stʃəl] [stʃən] [stʃəs] [tʃə] [w] [w̥] [æɹ] [æʊ] [ŋɡ] [ɑɪ] [ɑːɹ] [ɒf] [ɒɹ] [ɔɪ] [ɔːɹ] [əs] [əw] [əɹ] [əʊ] [əʊɪ] [ɚ] [ɛə] [ɛəɹ] [ɛɹ] [ɜːɹ] [ɝː], and 14 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [æ] [ɑː] [eɪ] [ə] [ɔː] | before mute e [eɪ] · default [æ] [ɑː] [eɪ] [ə] [ɔː] · nucleus unstressed [ə] · word final [ə] |
| ⟨ai⟩ | [eɪ] |  |
| ⟨air⟩ | [ɛəɹ] |  |
| ⟨ar⟩ | [ɑːɹ] | nucleus unstressed [əɹ] |
| ⟨are⟩ | [ɛəɹ] |  |
| ⟨au⟩ | [ɔː] [ɑː] [ɒ] | before vowel [aʊ] · default [ɔː] [ɑː] [ɒ] |
| ⟨aw⟩ | [ɔː] | before vowel [əw] · default [ɔː] |
| ⟨ay⟩ | [eɪ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] · before y [s] · default [k] |
| ⟨ch⟩ | [tʃ] [k] [ʃ] |  |
| ⟨ck⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨dg⟩ | [dʒ] |  |
| ⟨dge⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] [iː] [ə] | before mute e [iː] · default [ɛ] [iː] [ə] · nucleus unstressed closed [ə] · word final ∅ |
| ⟨ea⟩ | [iː] [ɛ] |  |
| ⟨ear⟩ | [ɪəɹ] [ɛəɹ] |  |
| ⟨eau⟩ | [juː] [əʊ] |  |
| ⟨ee⟩ | [iː] |  |
| ⟨eer⟩ | [ɪəɹ] |  |
| ⟨ei⟩ | [iː] [eɪ] |  |
| ⟨er⟩ | [ɜːɹ] [əɹ] |  |
| ⟨eu⟩ | [juː] |  |
| ⟨ew⟩ | [juː] [uː] |  |
| ⟨ey⟩ | [iː] [eɪ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] | before e [dʒ] [ɡ] · before i [ɡ] [dʒ] · before y [dʒ] · default [ɡ] |
| ⟨gg⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡ] [f] ∅ |  |
| ⟨gn⟩ | [n] |  |
| ⟨h⟩ | [h] | default [h] · word final ∅ |
| ⟨i⟩ | [ɪ] [iː] [aɪ] | before mute e [aɪ] · before vowel [i] · default [ɪ] [iː] [aɪ] · word final [i] |
| ⟨ie⟩ | [aɪ] [iː] |  |
| ⟨igh⟩ | [aɪ] |  |
| ⟨ir⟩ | [ɜːɹ] |  |
| ⟨ire⟩ | [aɪəɹ] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [k] |  |
| ⟨kn⟩ | [n] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] [ŋɡ] | before final vowel [ndʒ] · default [ŋ] |
| ⟨o⟩ | [ɒ] [əʊ] [ɔː] [ʌ] [uː] | before mute e [əʊ] · default [ɒ] [əʊ] [ɔː] [ʌ] [uː] · nucleus unstressed [ə] · word final [əʊ] |
| ⟨oa⟩ | [əʊ] |  |
| ⟨oar⟩ | [ɔːɹ] |  |
| ⟨oe⟩ | [əʊ] [uː] |  |
| ⟨oi⟩ | [ɔɪ] |  |
| ⟨oo⟩ | [uː] [ʊ] |  |
| ⟨or⟩ | [ɔːɹ] | nucleus unstressed [əɹ] |
| ⟨ore⟩ | [ɔːɹ] |  |
| ⟨ou⟩ | [aʊ] [ʌ] [uː] |  |
| ⟨ough⟩ | [ɔː] [əʊ] [ʌf] [ɒf] [aʊ] [uː] |  |
| ⟨our⟩ | [aʊəɹ] [ɔːɹ] |  |
| ⟨ow⟩ | [aʊ] [əʊ] |  |
| ⟨oy⟩ | [ɔɪ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [ɹ] |  |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] · word final [s] [z] · word initial [s] |
| ⟨sc⟩ | [s] | before e [s] · before i [s] · before y [s] · default [sk] |
| ⟨sch⟩ | [sk] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tch⟩ | [tʃ] |  |
| ⟨th⟩ | [θ] [ð] | default [θ] · intervocalic [ð] · word initial [θ] [ð] |
| ⟨u⟩ | [ʌ] [juː] [uː] [ʊ] | before mute e [juː] [uː] · default [ʌ] [juː] [uː] [ʊ] · nucleus unstressed [ə] |
| ⟨ue⟩ | [juː] [uː] |  |
| ⟨ui⟩ | [uː] [ɪ] |  |
| ⟨ur⟩ | [ɜːɹ] |  |
| ⟨ure⟩ | [jʊəɹ] [ʊəɹ] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨wh⟩ | [w] [ʍ] |  |
| ⟨wr⟩ | [ɹ] |  |
| ⟨x⟩ | [ks] [ɡz] | default [ks] · word initial [z] |
| ⟨y⟩ | [j] [iː] [aɪ] [ɪ] | before mute e [aɪ] · before vowel [j] · default [ɪ] [aɪ] [i] · word final [i] [aɪ] · word initial [j] |
| ⟨z⟩ | [z] |  |

Stress falls on the first syllable by default. These endings take the penult: ⟨-ic⟩ ⟨-ics⟩ ⟨-ion⟩ ⟨-ions⟩.

Whole-word exceptions (33): ⟨a⟩ [ə], ⟨above⟩ [əˈbʌv], ⟨an⟩ [ən], ⟨be⟩ [biː], ⟨come⟩ [kʌm], ⟨do⟩ [duː], ⟨does⟩ [dʌz], ⟨doing⟩ [ˈduːɪŋ], ⟨done⟩ [dʌn], ⟨dove⟩ [dʌv], ⟨give⟩ [ɡɪv], ⟨glove⟩ [ɡlʌv], ⟨gone⟩ [ɡɒn], ⟨have⟩ [hæv], ⟨he⟩ [hiː], ⟨live⟩ [lɪv], ⟨lose⟩ [luːz], ⟨love⟩ [lʌv], ⟨me⟩ [miː], ⟨move⟩ [muːv], ⟨none⟩ [nʌn], ⟨once⟩ [wʌns], ⟨one⟩ [wʌn], ⟨prove⟩ [pruːv], ⟨she⟩ [ʃiː], ⟨shove⟩ [ʃʌv], ⟨some⟩ [sʌm], ⟨the⟩ [ðə], ⟨there⟩ [ðɛə], ⟨we⟩ [wiː], and 3 more in the spec file.

Grammatical endings: ⟨-cial⟩ [ʃəl], ⟨-cian⟩ [ʃən], ⟨-cion⟩ [ʃən], ⟨-cious⟩ [ʃəs], ⟨-ous⟩ [əs], ⟨-ssion⟩ [ʃən], ⟨-ssure⟩ [ʃə], ⟨-stial⟩ [stʃəl], ⟨-stion⟩ [stʃən], ⟨-stious⟩ [stʃəs], ⟨-sure⟩ [ʒə], ⟨-tial⟩ [ʃəl], ⟨-tion⟩ [ʃən], ⟨-tious⟩ [ʃəs], ⟨-ture⟩ [tʃə].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 42 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `EN_GB_PREVOCALIC_R_AR_GEMINATE` | /ɑːɹ/ → [æ], spelled ⟨ar⟩, before ⟨r⟩, with more context in the spec | ⟨marry⟩ [ˈmæɹi] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_PREVOCALIC_R_AR` | /ɑːɹ/ → [æɹ], before a vowel, spelled ⟨ar⟩ | ⟨marry⟩ [ˈmæɹi] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_PREVOCALIC_R_ER_GEMINATE` | /əɹ/ → [ɛ], spelled ⟨er⟩, before ⟨r⟩, with more context in the spec | ⟨merry⟩ [ˈmɛɹi] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_PREVOCALIC_R_ER` | /əɹ/ → [ɛɹ], before a vowel, spelled ⟨er⟩ | ⟨merry⟩ [ˈmɛɹi] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_PREVOCALIC_R_IR_GEMINATE` | /ɜːɹ/ → [ɪ], spelled ⟨ir⟩, before ⟨r⟩, with more context in the spec | ⟨mirror⟩ [ˈmɪɹə] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_PREVOCALIC_R_IR` | /ɜːɹ/ → [ɪɹ], before a vowel, spelled ⟨ir⟩ | ⟨mirror⟩ [ˈmɪɹə] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_PREVOCALIC_R_UR_GEMINATE` | /ɜːɹ/ → [ʌ], spelled ⟨ur⟩, before ⟨r⟩, with more context in the spec | ⟨hurry⟩ [ˈhʌɹi] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_PREVOCALIC_R_UR` | /ɜːɹ/ → [ʌɹ], before a vowel, spelled ⟨ur⟩ | ⟨hurry⟩ [ˈhʌɹi] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_PREVOCALIC_R_OR_GEMINATE` | /ɔːɹ/ → [ɒ], spelled ⟨or⟩, before ⟨r⟩, with more context in the spec | ⟨sorry⟩ [ˈsɒɹi] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_PREVOCALIC_R_OR` | /ɔːɹ/ → [ɒɹ], before a vowel, spelled ⟨or⟩ | ⟨sorry⟩ [ˈsɒɹi] | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Carney 1994](#src-carney1994) |
| `EN_GB_NONRHOTIC_AR_PRECONS` | /ɑːɹ/ → [ɑː], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_AR_FINAL` | /ɑːɹ/ → [ɑː], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_NURSE_PRECONS` | /ɜːɹ/ → [ɜː], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_NURSE_FINAL` | /ɜːɹ/ → [ɜː], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_OR_PRECONS` | /ɔːɹ/ → [ɔː], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_OR_FINAL` | /ɔːɹ/ → [ɔː], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_LETTER_PRECONS` | /əɹ/ → [ə], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_LETTER_FINAL` | /əɹ/ → [ə], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_SQUARE_PRECONS` | /ɛəɹ/ → [ɛə], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_SQUARE_FINAL` | /ɛəɹ/ → [ɛə], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_NEAR_PRECONS` | /ɪəɹ/ → [ɪə], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_NEAR_FINAL` | /ɪəɹ/ → [ɪə], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_CURE_PRECONS` | /ʊəɹ/ → [ʊə], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_CURE_FINAL` | /ʊəɹ/ → [ʊə], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_CURE_J_PRECONS` | /jʊəɹ/ → [jʊə], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_CURE_J_FINAL` | /jʊəɹ/ → [jʊə], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_FIRE_PRECONS` | /aɪəɹ/ → [aɪə], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_FIRE_FINAL` | /aɪəɹ/ → [aɪə], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_HOUR_PRECONS` | /aʊəɹ/ → [aʊə], before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_HOUR_FINAL` | /aʊəɹ/ → [aʊə], word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_R_PRECONS` | /ɹ/ → ∅, not word-initially, before a consonant | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_NONRHOTIC_R_FINAL` | /ɹ/ → ∅, not word-initially, word-finally | - | [Wells 1982](#src-wells1982_vol1), [Wells 1982](#src-wells1982_vol2), [Cruttenden 2014](#src-gimson2014) |
| `EN_GB_ED_EPENTHESIS` | /ɛ ə/ → [ɪ], after [t] [d], spelled ⟨e⟩, before ⟨d⟩, with more context in the spec | - | [Cruttenden 2014](#src-gimson2014), [Wells 2008](#src-wells2008) |
| `EN_GB_ED_SYNCOPE_AFTER_V` | /ɛ ə/ → ∅, spelled ⟨e⟩, before ⟨d⟩, with more context in the spec | - | [Cruttenden 2014](#src-gimson2014), [Wells 2008](#src-wells2008) |
| `EN_GB_ED_SYNCOPE_AFTER_C` | /ɛ ə/ → ∅, spelled ⟨e⟩, before ⟨d⟩, with more context in the spec | - | [Cruttenden 2014](#src-gimson2014), [Wells 2008](#src-wells2008) |
| `EN_GB_ED_DEVOICING` | /d/ → [t], word-finally, spelled ⟨d⟩, after ⟨e⟩, with more context in the spec | - | [Cruttenden 2014](#src-gimson2014), [Wells 2008](#src-wells2008) |
| `EN_GB_FINAL_S_VOICING` | /s/ → [z], word-finally, before a word boundary, after [b] [d] [ɡ] [v] [ð] [m] [n] [ŋ] and 2 more, spelled ⟨s⟩ | - | [Cruttenden 2014](#src-gimson2014), [Wells 2008](#src-wells2008) |
| `EN_GB_ES_EPENTHESIS` | /ɛ ə iː/ → [ɪ], after [s] [z] [ʃ] [ʒ] [tʃ] [dʒ] [ɡ], spelled ⟨e⟩, before ⟨s⟩, with more context in the spec | - | [Cruttenden 2014](#src-gimson2014), [Wells 2008](#src-wells2008) |
| `EN_GB_ES_SYNCOPE` | /ɛ ə iː/ → ∅, after a consonant, spelled ⟨e⟩, before ⟨s⟩, with more context in the spec | - | [Cruttenden 2014](#src-gimson2014), [Wells 2008](#src-wells2008) |
| `EN_GB_ES_VOICING_AFTER_MUTE_E` | /s/ → [z], word-finally, spelled ⟨s⟩, after ⟨e⟩, with more context in the spec | - | [Cruttenden 2014](#src-gimson2014), [Wells 2008](#src-wells2008) |
| `EN_GB_ES_VOICING_AFTER_EPENTHESIS` | /s/ → [z], word-finally, spelled ⟨s⟩, after ⟨e⟩, with more context in the spec | - | [Cruttenden 2014](#src-gimson2014), [Wells 2008](#src-wells2008) |
| `EN_GB_OING_HIATUS` | /ɔɪ/ → [əʊɪ], spelled ⟨oi⟩, before ⟨ng⟩, with more context in the spec | - | [Carney 1994](#src-carney1994) |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="pin|tap|button|butter|leaf|feel|ambitious|arrive|bathe|bird|city|dance|delicious|digestion" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "en-GB")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| pin | [ˈpɪn] |
| tap | [ˈtæp] |
| button | [ˈbʌtən] |
| butter | [ˈbʌtə] |
| leaf | [ˈliːf] |
| feel | [ˈfiːl] |
| ambitious | [ˈæmbɪʃəs] |
| arrive | [ˈæɹaɪv] |
| bathe | [ˈbeɪð] |
| bird | [ˈbɜːd] |
| city | [ˈsɪti] |
| dance | [ˈdæns] |
| delicious | [ˈdɛlɪʃəs] |
| digestion | [dɪˈdʒɛstʃən] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

| Repository | What it does with this spec |
|:--|:--|
| [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) | The residual lexicon for this spec: only the words its rules cannot reach. |
<!-- atlas:related end -->

---
[← Breton](br.md) · [Home](../index.md) · [Brunei →](kxd.md)
