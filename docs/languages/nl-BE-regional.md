# Regional Standard Dutch of Belgium (nl-BE-x-*)

The `nl-BE-x-*` specs model the regional accents of Standard Dutch in Belgium. A regional spec describes the standard language as educated speakers from one place speak it. The specs do not describe the traditional dialects. Each spec is a delta spec over `nl-BE`: it inherits the whole Belgian standard and declares only what its region changes.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`.

## How the regional specs inherit from nl-BE

Every spec on this page sets `parent` to `nl-BE`. It also sets the four base keys `graphemes_base`, `allophones_base`, `positional_graphemes_base` and `word_exceptions_base` to `nl-BE`. `nl-BE` itself inherits its graphemes and allophone rules from `nl-NL`, so a regional spec gets the full chain. The engine does not inherit `collapse_geminates`, so each spec sets it to `true` again.

The rule list `allophone_rules` merges by id (see [../engine/allophony.md](../engine/allophony.md#inheritance)). For each slot, the first rule in the list that matches is the one that fires. An own rule with a new id goes to the end of the list. So when an own rule must fire before an inherited one, the spec switches the inherited rule off in place, with an empty `phonemes` list, and restates it after its own rule under a new id.

## Defining features

| Spec | Region | Features that set it apart from `nl-BE` | Example |
|:---|:---|:---|:---|
| [`nl-BE-x-antwerp`](#antwerp-nl-be-x-antwerp) | The city of Antwerp | onset /r/ as the voiced tap [ɾ]<br>a schwa between /r/ and a non-coronal coda consonant<br>long stressed /i u/ | `rood` [ˈɾoːt], `kerk` [ˈkɛɾək], `Piet` [ˈpiːt] |

## Antwerp (nl-BE-x-antwerp)

`nl-BE-x-antwerp` models the Standard Dutch of the city of Antwerp. It is not the Antwerp dialect. Sebregts (2014) records 41 speakers born and raised in the city, in *"urban accents of colloquial Standard Dutch"* (p. 52). Verhoeven & Van Bael (2002) record *"12 Antwerpenaars (agglomeratie Antwerpen)"* (p. 7), who had to speak Standard Dutch with ease (p. 8). Sources: Sebregts (2014), Verhoeven & Van Bael (2002), Verhoeven (2005), van der Harst & Van de Velde (2007), van der Harst (2011), Voeten (2021), Verhoeven & Hageman (2007), De Wulf (2003).

### Onset /r/ as the tap

Sebregts (2014, p. 88) writes: *"Taps are by far the most common onset realisation for alveolar r speakers"*. His Table 3-26 (p. 88) gives the voiced alveolar tap for 65.7% of the Antwerp word-onset tokens and 68.6% of the intervocalic ones. The word-onset items include clusters such as *brood* and *gras*. Of the 41 speakers, 35 have an alveolar r (Table 4-2, p. 127).

The rule `NL_BE_X_ANTWERP_R_TAP_ONSET` gives /r/ before a vowel the tap [ɾ].

| Word | `nl-BE` | `nl-BE-x-antwerp` |
|:---|:---|:---|
| `rood` | [ˈroːt] | [ˈɾoːt] |
| `brood` | [ˈbroːt] | [ˈbɾoːt] |
| `gras` | [ˈɣrɑs] | [ˈɣɾɑs] |
| `waren` | [ˈwaːrən] | [ˈwaːɾən] |

### The schwa between /r/ and a coda consonant

Sebregts (2014) states the context as a class: *"the appearance of an epenthetic vowel between /r/ and a following non-coronal or nasal consonant in a coda cluster"* (p. 236), with the example *kern* [ˈkɛrən]. In Antwerp, 95.0% of the 322 tokens have the schwa (Table 6-2, p. 242). No Antwerp speaker is categorically without it, and 83% of the speakers always insert it (p. 244). The r of this context is the voiced tap in 73.3% of the tokens (Table 3-27, p. 89).

Three rules give /r/ before /p b f v k ɡ x m n/ the value [ɾə] when that consonant closes the syllable. `NL_BE_X_ANTWERP_R_SCHWA_INSERTION_FINAL` covers the cluster at the end of a word, as in the measured items. `NL_BE_X_ANTWERP_R_SCHWA_INSERTION_BEFORE_NASAL_CODA` covers /r/ and a nasal before another consonant, because no Dutch syllable begins with a nasal and a consonant: `armband` [ˈɑɾəmbɑnt]. `NL_BE_X_ANTWERP_R_SCHWA_INSERTION_BEFORE_OBSTRUENT_CODA` covers /r/ and an obstruent before another consonant: `kerkhof` [ˈkɛɾəkɦɔf], `werkt` [ˈwɛɾəkt]. An obstruent followed by /l r n w/ can open the next syllable, as in *blad*, *vrij*, *knal* and *kwartier*. So that rule does not fire before /l r n w/: `verblijf` [vərˈblɛif], `deurknop` [ˈdøːr̥knɔp]. The tap is voiced, so the rules must fire before the `nl-BE` devoicing before /p t k/. The spec switches `NL_BE_R_DEVOICE_BEFORE_VOICELESS_STOP` off in place and restates it after the schwa rules. The `nl-BE` keys ⟨kerk⟩ and ⟨berg⟩ spell the words in one slot, so the spec restates them in its positional map.

| Word | `nl-BE` | `nl-BE-x-antwerp` |
|:---|:---|:---|
| `harp` | [ˈɦɑr̥p] | [ˈɦɑɾəp] |
| `kerk` | [ˈkɛr̥k] | [ˈkɛɾək] |
| `berg` | [ˈbɛrx] | [ˈbɛɾəx] |
| `arm` | [ˈɑrm] | [ˈɑɾəm] |
| `kern` | [ˈkɛrn] | [ˈkɛɾən] |

When the consonant opens the next syllable, it is not in the coda cluster, and the `nl-BE` value stays: `kerken` [ˈkɛr̥kən], `bergen` [ˈbɛrɣən], `Antwerpen` [ˈɑntwər̥pən].

### Long stressed /i u/

Verhoeven & Van Bael (2002, p. 16) write:

> *"Een eerste vaststelling is dat twee Antwerpse klinkers lang zijn, terwijl ze in LIM en OVL kort worden gerealiseerd. Dit betreft [i] en [u] met een gemiddelde duur van 261 en 246 msec."*

The values for Limburg and East Flanders are 123 and 97 ms for [i], and 104 and 109 ms for [u]. The test words are stressed (*Piet*, *Lies*, *spoed*, *Loes*, p. 6), so the rules `NL_BE_X_ANTWERP_LONG_STRESSED_I` and `NL_BE_X_ANTWERP_LONG_STRESSED_U` act in a stressed syllable only.

| Word | `nl-BE` | `nl-BE-x-antwerp` |
|:---|:---|:---|
| `Piet` | [ˈpit] | [ˈpiːt] |
| `Lies` | [ˈlis] | [ˈliːs] |
| `spoed` | [ˈsput] | [ˈspuːt] |
| `Loes` | [ˈlus] | [ˈluːs] |

### Known gaps

- Coda /r/ before /s/ and the other coronals keeps the `nl-BE` value: `worst` [ˈwɔrst]. Sebregts (2014, p. 92) finds 63.5% voiceless and fricative coda tokens in Antwerp, but the figure pools every coda context.
- No schwa before a coronal: `paard` [ˈpaːr̥t]. Sebregts (p. 88) finds it *"only to a limited extent in the coda context"*.
- /l/ + consonant has no schwa: `melk` [ˈmɛlk]. Sebregts (p. 236) names the same process for /l/, but he measures /r/ only.
- The palato-velar realisation of /ɣ/ (32.5% in region V-B, van der Harst & Van de Velde 2007, p. 184) has no rule, because the source gives no conditioning context.
- The close formants of [i ɪ], [a ɑ] and [y ʏ] (Verhoeven 2005, p. 246) are gradient, and no merger is stated.
- The diphthongs take the `nl-BE` values. Voeten (2021, p. 166) finds the higher Flemish onsets *"for all Flemish regions but Flemish-Brabant"*.
- ⟨h⟩ dropping is dialect data (De Wulf 2003, pp. 217-218).
- The engine does not know compound boundaries. So a coda obstruent before /n w/ takes no schwa: `werknemer` [ˈwɛr̥knəmər̥], `erfwoord` [ˈɛrfwoːr̥t].
- The length rules read the inherited stress block. A word that the block stresses on the wrong syllable gets its long vowel there too: `minuut` [ˈmiːnyt].
