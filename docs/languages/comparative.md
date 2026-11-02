# Comparative phonology: Germanic, Romance and Slavic

This page compares the phonology of three European language families, one section per family. Each section names the specs it covers and sets the features that separate the languages side by side.

IPA in square brackets, such as [ɡʁaːp], comes from the reference grammars that each section cites. It is not engine output. A value in backticks, such as `ˈtak`, is the real output of `orthography2ipa.transcribe(word, code)`. Where the two differ, the spec makes a simpler or different choice than the grammar, and the text says so.

## Germanic languages

**Family**: Indo-European > Germanic | **Script**: Latin (alphabet), Hebrew for Yiddish

### Final devoicing

German and Dutch devoice an obstruent at the end of a word (Wiese 1996, Booij 1995). Afrikaans has the same rule from Dutch (Wissing 2020, cited in `af.json`). English and Icelandic have no final devoicing, and English allows a voiced stop in the coda.

The specs state the rule where the literature has it, and leave it out elsewhere:

| Language | Code | Quality tier | Word-final rule in the spec | Spec output |
|:---|:---:|:---|:---|:---|
| German | `de-DE` | research | Yes, on ⟨b d g v⟩ | `Tag` `ˈtak` |
| Dutch | `nl` | research | Yes, on ⟨b d g v z⟩, and ⟨g⟩ also before a voiceless obstruent (`NL_CODA_DEVOICE_G`) | `dag` `ˈdɑx`, `hond` `ˈɦɔnt` |
| Afrikaans | `af` | research | Yes, on ⟨b d v z⟩ | `hond` `ˈɦɔnt` |
| Swedish | `sv` | research | No. The spec notes state that Swedish keeps final /b d ɡ/ | `god` `ˈɡuːd` |
| Norwegian (Bokmål) | `nb` | research | No | `dag` `ˈdɑːɡ` |
| Danish | `da` | research | No | `dag` `ˈdaːɡ` |
| Icelandic | `is` | research | No | `land` `ˈlant` |
| English | `en-GB`, `en-US` | research | No | `dog` `ˈdɒɡ` (en-GB) |
| Yiddish | `yi` | research | No | `טאָג` `ˈtɔɡ` |

The `af` spec states its own rule, because positional rules do not pass from `nl` to `af` through the parent link.

### German and Dutch consonants

| Feature | German (`de-DE`) | Dutch (`nl`) |
|:---|:---:|:---:|
| ⟨g⟩ | [ɡ] in the onset, [k] in the coda | [ɣ] in the onset, [x] in the coda (fricatives) |
| ⟨h⟩ | [h] | [ɦ] (breathy) |
| ⟨r⟩ | [ʁ] (uvular) | [r] or [ʁ], by region |
| ⟨w⟩ | [v] | [ʋ] (labiodental approximant) |
| ⟨ch⟩ word-final | [x] or [ç] | always [x] |

Dutch ⟨g⟩ is a velar fricative, not a plosive. It is voiced [ɣ] in the onset, as in `gaan` [ɣaːn] 'to go', and voiceless [x] in the coda, as in `dag` [dax] 'day'. The realisation varies by region. The spec gives `ˈɣaːn` and `ˈdɑx`, and writes ⟨r⟩ as [r] (`groot` `ˈɣroːt`). For the details of the German spec, see [German](de-DE.md).

### Swedish

Swedish ⟨k⟩, ⟨g⟩ and ⟨sk⟩ change before the front vowels ⟨e i y ä ö⟩ (Riad 2014). The `sv` spec states the change in `positional_graphemes`, and its output agrees with the grammar:

| Grapheme | Before a front vowel | Elsewhere | Spec output |
|:---:|:---:|:---:|:---|
| k | [ɕ] (alveolo-palatal fricative) | [k] | `kär` `ˈɕæːr` 'dear', `katt` `ˈkatː` 'cat' |
| g | [j] | [ɡ] | `ge` `ˈjeː` 'give', `gå` `ˈɡoː` 'walk' |
| sk | [ɧ] (the sj-sound) | [sk] | `sked` `ˈɧeːd` 'spoon' |

In Central Standard Swedish (rikssvenska), ⟨r⟩ and a following coronal consonant merge into a retroflex (Engstrand 1999). The `SV_RETROFLEX_*` allophone rules encode this:

| Cluster | Retroflex | Spec output |
|:---:|:---:|:---|
| rs | [ʂ] | `fors` `ˈfɔʂ` 'rapids' |
| rd | [ɖ] | `nord` `ˈnɔɖ` 'north' |
| rn | [ɳ] | `barn` `ˈbaɳ` 'child' |
| rl | [ɭ] | `karl` `ˈkaɭ` 'man' |
| rt | [ʈ] | `fort` `ˈfɔʈ` 'fort' |

Swedish has the rare phoneme [ɧ], a voiceless fricative with a double articulation. Several spellings write it: ⟨sj⟩, ⟨sk⟩ before a front vowel, ⟨stj⟩, ⟨skj⟩ and ⟨sch⟩. The spec gives [ɧ] for the first four, as in `sjö` `ˈɧøː`. It gives [ʃ] for ⟨sch⟩, as in `dusch` `ˈdʉːʃ`.

Swedish has two lexical word accents, which separate words that are otherwise the same. Accent 1 (acute) has one peak, as in `anden` [¹andən] 'the duck'. Accent 2 (grave) has two peaks, as in `anden` [²andən] 'the spirit'. The spec marks accent 2 with ² on one class only: words with penultimate stress that end in ⟨-a⟩ or ⟨-e⟩ (Riad 2014, ch. 10). It leaves accent 1 unmarked, as the WikiPron gold does. So the spec gives `²ɡɑːta` for `gata`, and `ˈandɛn` for both readings of `anden`.

### Dutch vowels

Dutch has a vowel system with contrasts of length and quality (Booij 1995, Gussenhoven 1992):

| Short | Long | IPA short | IPA long | Example short | Example long |
|:---:|:---:|:---:|:---:|:---:|:---:|
| a | aa | [ɑ] | [aː] | `kat` [kɑt] | `kaas` [kaːs] |
| e | ee | [ɛ] | [eː] | `bed` [bɛt] | `been` [beːn] |
| i | ie | [ɪ] | [iː] | `bit` [bɪt] | `biet` [biːt] |
| o | oo | [ɔ] | [oː] | `bof` [bɔf] | `boot` [boːt] |
| u | uu | [ʏ] | [yː] | `bus` [bʏs] | `buut` [byːt] |

The other vowels are ⟨eu⟩ [øː], ⟨oe⟩ [uː], ⟨ui⟩ [œy], ⟨ij⟩ and ⟨ei⟩ [ɛi], and ⟨au⟩ and ⟨ou⟩ [ɑu]. The `nl` spec writes ⟨ie uu oe⟩ without a length mark, so it gives `ˈbit` for `biet`, `ˈbyt` for `buut` and `ˈbuk` for `boek`. Its other values agree with the table, as in `ˈkaːs`, `ˈrøːs` for `reus` and `ˈʋɛin` for `wijn`.

### Afrikaans

Afrikaans (`af`) comes from Dutch and differs from it in these points. The spec output shows each one:

| Feature | Afrikaans | Spec output |
|:---|:---|:---|
| Final devoicing | kept from Dutch | `hond` `ˈɦɔnt` |
| ⟨g⟩ | [x] in all positions, no voiced [ɣ] | `goed` `ˈxut`, `reg` `ˈrɛx` |
| ⟨r⟩ | [r] (alveolar trill), not uvular | `berg` `ˈbɛrx` |
| ⟨v⟩ | [f], where Dutch has [v] | `vis` `ˈfəs` |
| ⟨ee⟩, ⟨oo⟩ | the diphthongs [iə] and [uə] | `see` `ˈsiə`, `boom` `ˈbuəm` |

Afrikaans also has no grammatical gender.

### Germanic references

- Wiese, R. (1996). *The Phonology of German*. OUP.
- Booij, G. (1995). *The Phonology of Dutch*. OUP.
- Riad, T. (2014). *The Phonology of Swedish*. OUP.
- Engstrand, O. (1999). *Swedish*. JIPA 29(1), 140-145.
- Gussenhoven, C. (1992). *Dutch*. JIPA 22, 45-47.

## Romance languages

**Family**: Romance (from Latin) | **Script**: Latin (alphabet)

| Language | Code | Quality tier |
|:---|:---:|:---|
| Spanish | `es-ES` | production |
| French | `fr-FR` | research |
| Italian | `it-IT` | research |
| European Portuguese | `pt-PT` | research |
| Brazilian Portuguese | `pt-BR` | production |
| Catalan | `ca` | research |
| Romanian | `ro-RO` | production |
| Galician | `gl-ES` | research |
| Aranese Occitan | `oc-x-aranes` | research |

### Softening of c and g

The Romance languages share the palatal softening of Latin ⟨c⟩ and ⟨g⟩ before a front vowel. The values differ by language, and the specs agree with them:

| Language | c before e, i | g before e, i | Notes | Spec output |
|:---|:---:|:---:|:---|:---|
| French | [s] | [ʒ] | Also before y | `cire` `siʁ`, `gilet` `ʒilɛ`, `cygne` `siɲ` |
| Italian | [tʃ] | [dʒ] | The digraphs ⟨ch gh⟩ keep the plosive | `cena` `ˈtʃena`, `gelato` `dʒeˈlato`, `chi` `ˈki` |
| Spanish | [θ] (Castilian), [s] (Latin American) | [x] | | `cero` `ˈθeɾo`, `gente` `ˈxente` |
| Portuguese | [s] | [ʒ] | | `cedo` `ˈsɛdu`, `gente` `ˈʒẽtɨ` (pt-PT) |
| Catalan | [s] | [dʒ] or [ʒ] | | `cel` `ˈsɛl`, `gent` `ˈʒen` |
| Romanian | [tʃ] | [dʒ] | | `cer` `tʃer`, `ger` `dʒer` |

### Spanish

Castilian Spanish separates ⟨c z⟩ /θ/ from ⟨s⟩ /s/ (distinción). Latin American and Andalusian Spanish have [s] for all three (seseo):

| Variety | ⟨c⟩ and ⟨z⟩ before e, i | Spec output for `cero` |
|:---|:---:|:---|
| Castilian (Spain) | [θ] (dental fricative) | `ˈθeɾo` (`es-ES`) |
| Latin American, Andalusian | [s] | `ˈseɾo` (`es-419`, `es-ES-x-andalusia-w`) |

In connected speech, the Spanish voiced stops become fricatives or approximants between vowels. The `es-ES` spec states this as `intervocalic` entries on ⟨b v d g⟩ in `positional_graphemes`:

| Phoneme | Allophone | Environment | Spec output |
|:---:|:---:|:---|:---|
| /b/ | [β] | Between vowels | `lobo` `ˈloβo` 'wolf' |
| /d/ | [ð] | Between vowels | `lado` `ˈlaðo` 'side' |
| /g/ | [ɣ] | Between vowels | `lago` `ˈlaɣo` 'lake' |

Spanish contrasts a tap and a trill. The spec gives ⟨r⟩ the trill at the start of a word, through `positional_graphemes`, and after ⟨n l s⟩, through the allophone rule `ES_TRILL_AFTER_CORONAL`:

| Grapheme | IPA | Environment | Spec output |
|:---:|:---:|:---|:---|
| r (single) | [ɾ] (tap) | Between vowels | `pero` `ˈpeɾo` 'but' |
| rr (double) | [r] (trill) | Between vowels | `perro` `ˈpero` 'dog' |
| r | [r] (trill) | Word-initial | `rosa` `ˈrosa` |
| r | [r] (trill) | After n, l, s | `Israel` `isˈrael`, `honra` `ˈonra` |

For the details of the Spanish spec, see [Spanish](es-ES.md).

### Portuguese

European and Brazilian Portuguese differ in the reduction of unstressed vowels, final ⟨l⟩ and final ⟨s⟩ (Mateus & d'Andrade 2000). The two specs show the differences:

| Feature | pt-PT (Lisbon) | pt-BR (standard) | Spec output, pt-PT | Spec output, pt-BR |
|:---|:---:|:---:|:---|:---|
| Unstressed e | [ɨ] | [e] or [i] | `pequeno` `pɨˈkɛnu` | `pequeno` `peˈkenu` |
| Unstressed o | [u] | [o] or [u] | `tomate` `tuˈmatɨ` | `tomate` `toˈmat͡ʃi` |
| Word-final -al, -el | [l] (velarised) | [w] (l-vocalisation) | `animal` `ɐniˈmaɫ`, `papel` `pɐˈpɛɫ` | `animal` `aniˈmaw`, `papel` `paˈpew` |
| r (initial, rr) | [ʁ] (uvular) | [h] or [x] | `rato` `ˈʁatu` | `rato` `ˈʁatu` |
| s, z word-final | [ʃ], [ʒ] (Lisbon) | [s], [z] | `gatos` `ˈɡatuʃ` | `gatos` `ˈɡatus` |

The `pt-BR` spec writes the strong rhotic as [ʁ], not as [h] or [x].

In Lisbon Portuguese, the value of ⟨s⟩ depends on its position:

| Position | Grammar | Spec output (pt-PT) |
|:---|:---:|:---|
| Word-initial | [s] | `sol` `ˈsɔɫ` |
| Between vowels | [z] | `casa` `ˈkazɐ` |
| Before a voiced consonant | [ʒ] | `mesmo` `ˈmɛʃmu` |
| Before a voiceless consonant | [ʃ] | `estar` `eʃˈtaɾ` |
| Word-final | [ʃ] | `gatos` `ˈɡatuʃ` |
| Word-final before a vowel in the next word | [z] (standard, North, Lisbon), [ʒ] (Algarve, Azores) | `os amigos` `oz ɐˈmiɡuʃ`, `estás a ver` `eʃˈtaz ɐ ˈveɾ` |

The `pt-PT` spec states the word-initial, intervocalic, word-final and cross-word values in `positional_graphemes`. It does not voice ⟨s⟩ before a voiced consonant, so it gives [ʃ] in `mesmo`, `desde` and `Lisboa`. The dialect specs `pt-PT-x-algarve` and `pt-PT-x-acores` give `eʃˈtaʒ ɐ ˈveɾ` for the cross-word case. For the details, see [European Portuguese](pt-PT.md).

### French nasal vowels

French kept nasal vowels where Latin had a vowel and a nasal. Italian and Spanish kept the oral vowel and the nasal consonant:

| Latin | French | Italian | Spanish |
|:---|:---:|:---:|:---:|
| *finem | `fin` `fɛ̃` | `fine` `ˈfine` | `fin` `ˈfin` |
| *bonum | `bon` `bɔ̃` | `buono` `ˈbwono` | `bueno` `ˈbweno` |
| `grande` | `grand` `ɡʁɑ̃` | `grande` `ˈɡrande` | `grande` `ˈɡɾande` |

The modern forms in this table are spec output from `fr-FR`, `it-IT` and `es-ES`. The grammars give a long vowel in Italian `fine` [ˈfiːne] and an open-mid vowel in `buono` [ˈbwɔno]. The `it-IT` spec does not write these two details. For the details of the French spec, see [French](fr-FR.md).

### Romanian

Romanian kept features that Western Romance lost. It has a case system, with a nominative-accusative form and a genitive-dative form. It has a neuter gender. The definite article is a suffix on the noun: `om` 'man', `omul` 'the man'. Its vowels include the schwa ⟨ă⟩ [ə] and the central high unrounded vowel ⟨â î⟩ [ɨ].

| Grapheme | IPA | Spec output |
|:---:|:---:|:---|
| ă | [ə] | `mamă` `mamə` |
| â, î | [ɨ] | `înainte` `ɨnajnte` |
| e | [je] at the start of some pronoun and verb forms | `este` `jeste`, `el` `jel` |
| c before e, i | [tʃ] | `cer` `tʃer` |
| g before e, i | [dʒ] | `ger` `dʒer` |
| ch | [k] | `cheie` `keje` |
| gh | [ɡ] | `gheață` `ɡe̯atsə` |

The spec gives [je] only for a closed list in `word_exceptions` (*e, el, ea, ei, ele, este, ești, eu* and forms of *era*). Other words keep [e] at the start, as in `elev` `elev`. The spec maps the comma-below letters ⟨ș ț⟩. It has no mapping for the cedilla forms ⟨ş ţ⟩, which older texts use. The engine drops each of them with an `UnmappedGraphemeWarning`, so `gheaţă` comes out as `ɡe̯aə`. For the details, see [Romanian](ro-RO.md).

### Catalan

Catalan sits between French and Iberian Romance. Central Catalan reduces unstressed ⟨a⟩ and ⟨e⟩ to [ə], like Portuguese and French: the `ca` spec gives `ˈkazə` for `casa`. The geminate lateral ⟨l·l⟩ is written with the punt volat ⟨·⟩, which separates it from ⟨ll⟩ [ʎ]. The spec gives `kuˈlːɛʒi` for `col·legi` and `ˈʎiβɾə` for `llibre`.

The main dialect areas are Valencian, Balearic and Northern Catalan. Each has its own spec: `ca-x-valencia`, `ca-x-balear` and `ca-x-nord`. The Valencian spec does not reduce unstressed ⟨a⟩, so it gives `ˈkaza` for `casa`.

### Romance references

- Penny, R. (2002). *A History of the Spanish Language* (2nd ed.). CUP.
- Tranel, B. (1987). *The Sounds of French*. CUP.
- Lepschy & Lepschy (1988). *The Italian Language Today*. Routledge.
- Mateus, M.H. & d'Andrade, E. (2000). *The Phonology of Portuguese*. OUP.
- Maiden, M. & Parry, M. (1997). *The Dialects of Italy*. Routledge.

## Slavic languages

**Family**: Indo-European > Slavic | **Script**: Latin (pl, cs, sk, hr, and the reconstruction sla) or Cyrillic (ru, uk, be, sr, bg, mk)

All the Slavic specs on this page are at `research` tier: `pl`, `cs`, `sk`, `sr`, `hr`, `bg`, `mk`, `uk`, `be`, `ru` and `sla`. The code `sla` is reconstructed Late Proto-Slavic, written in the Latin notation of Slavicists.

### Final devoicing

Polish, Czech and Russian devoice an obstruent in the coda (Rubach 1984 for Polish, Palková 1994 for Czech). The specs differ in whether they state the rule:

| Language | Code | Word-final rule in the spec | Spec output |
|:---|:---:|:---|:---|
| Polish | `pl` | Yes | `chleb` `ˈxlɛp` 'bread', `grzyb` `ˈɡʐɨp` 'mushroom' |
| Czech | `cs` | Yes | `chléb` `ˈxlɛːp` 'bread', `led` `ˈlɛt` 'ice' |
| Russian | `ru` | Yes | `хлеб` `ˈxlʲep` 'bread', `год` `ˈɡot` 'year' |
| Belarusian | `be` | Yes | `дуб` `dup` 'oak' |
| Slovak | `sk` | No | `dub` `ˈdub` |
| Ukrainian | `uk` | No | `хліб` `ˈxlʲib` |
| Serbian, Croatian | `sr`, `hr` | No | `град` `ɡrad`, `grad` `ɡrad` 'city' |
| Bulgarian | `bg` | No | `град` `ɡrad` |
| Macedonian | `mk` | No | `град` `ɡrad` |
| Late Proto-Slavic | `sla` | No. The open-syllable law leaves no closed syllables | `gradъ` `ɡradŭ` |

The Polish spec devoices each voiced obstruent to its voiceless partner:

| Voiced | Voiceless (word-final, coda) | Spec output |
|:---:|:---:|:---|
| b | p | `chleb` `ˈxlɛp` |
| d | t | `lód` `ˈlut` 'ice' |
| g | k | `bug` `ˈbuk` |
| w [v] | f | `krew` `ˈkrɛf` 'blood' |
| z | s | `bez` `ˈbɛs` 'without' |
| ź [ʑ] | ś [ɕ] | `maź` `ˈmaɕ` |
| ż [ʐ] | sz [ʂ] | `nóż` `ˈnuʂ` 'knife' |
| dz | c [ts] | `wódz` `ˈvuts` |

Czech follows the same pattern. Word-final ⟨h⟩ [ɦ] becomes [x], as in `Prah` `ˈprax`, a form in the paradigm of `Praha`. Word-final ⟨ď⟩ [ɟ] becomes ⟨ť⟩ [c], as in `zeď` `ˈzɛc`.

### Polish nasal vowels

Polish ⟨ą⟩ and ⟨ę⟩ continue the nasal vowels of Proto-Slavic, which most other Slavic languages lost (Gussmann 2007). Their value depends on what follows. The spec output shows each case:

| Grapheme | Before a fricative | Before a stop | Word-final | Spec output |
|:---:|:---:|:---:|:---:|:---|
| ą | [ɔ̃] | [ɔm ɔn ɔŋ] | [ɔw̃] | `kąt` `ˈkɔnt`, `dąb` `ˈdɔmp`, `idą` `ˈidɔw̃` |
| ę | [ɛ̃] | [ɛm ɛn ɛŋ] | [ɛ] | `gęś` `ˈɡɛ̃ɕ`, `ręka` `ˈrɛŋka`, `robię` `ˈrɔbjɛ` |

Word-final ⟨ę⟩ loses its nasality, as in `robię` 'I do'. Word-final ⟨ą⟩ keeps a nasal glide.

### Czech ⟨ě⟩

The letter ⟨ě⟩ has two functions:

1. After ⟨d t n⟩, it marks the consonant as palatal, ⟨ď ť ň⟩: `děti` `ˈɟɛcɪ` 'children', `tělo` `ˈcɛlo` 'body', `něco` `ˈɲɛtso` 'something'.
2. After a labial (b, p, m, v, f), it adds [j] before [ɛ] and does not change the consonant: `věra` `ˈvjɛra` 'faith', `běžet` `ˈbjɛʒɛt` 'to run'.

### Czech ⟨ř⟩

Czech ⟨ř⟩ [r̝] is a raised alveolar trill, a rare sound that combines /r/ and /ʒ/ (Short 1993). It is always hard, not palatalised. It is voiced in `říkat` `ˈr̝iːkat` 'to say'. After a voiceless consonant and at the end of a word, it becomes voiceless [r̝̊], as in `tři` [tr̝̊ɪ] 'three'. The `cs` spec does not write the voiceless value and gives `ˈtr̝ɪ`.

### Polish sibilants

Polish contrasts three series of sibilants, each with fricatives and affricates (Gussmann 2007):

| Series | Dentals | Retroflexes | Alveolo-palatals |
|:---|:---:|:---:|:---:|
| Fricative | s z | sz [ʂ], ż and rz [ʐ] | ś [ɕ], ź [ʑ] |
| Affricate | c [ts], dz [dz] | cz [tʂ], dż [dʐ] | ć [tɕ], dź [dʑ] |

The spelling also writes the alveolo-palatals as ⟨ni ci si zi dzi⟩ before a vowel. The spec gives `ˈɲɛ` for `nie`, `ˈtɕawɔ` for `ciało`, `ˈʂtʂaf` for `szczaw` and `ˈdʑvjɛŋk` for `dźwięk`.

### Comparison table

| Feature | pl | cs | ru | uk | sr, hr |
|:---|:---:|:---:|:---:|:---:|:---:|
| Nasal vowels | yes | no | no | no | no |
| Contrast of vowel length | no | yes | no | no | yes |
| Pitch accent | no | no | no | no | yes (sr) |
| Word-final devoicing in the spec | yes | yes | yes | no | no |
| Palatalised consonants | yes | yes | yes | yes | yes |
| The phoneme ř | no | yes | no | no | no |
| Script | Latin | Latin | Cyrillic | Cyrillic | Both |

For the details of the Russian spec, see [Russian](ru.md).

### Slavic references

- Rubach, J. (1984). *Cyclic and Lexical Phonology: The Structure of Polish*. Foris.
- Bethin, C.Y. (1992). *Polish Syllables*. Slavica.
- Palková, Z. (1994). *Fonetika a fonologie češtiny*. Karolinum.
- Gussmann, E. (2007). *The Phonology of Polish*. Oxford University Press.
- Short, D. (1993). Czech. In: *The Slavonic Languages*, Routledge.

---
[← Language pages](index.md) · [Home](../index.md) · [English →](en-GB.md)
