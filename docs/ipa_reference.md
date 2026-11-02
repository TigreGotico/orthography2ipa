# IPA Reference

This page lists the IPA symbols that the specs use, with their code points and the errors to avoid. It ends with notes on how the specs of some major languages encode their phonology. The engine writes its output in Unicode NFC, so the code points below are the NFC forms.

## Encoding rules

Spec files are UTF-8 JSON. Every IPA value uses the correct Unicode code point, never an ASCII character that looks the same. A combining diacritic follows its base character, so `t̪` is `t` followed by U+032A. The engine normalises its output to NFC. So a vowel with a tilde that Unicode has as one precomposed character, such as `ã`, comes out as that character.

## Errors to avoid

| Wrong | Correct | Why |
|---|---|---|
| `g` | `ɡ` | The IPA voiced velar stop is U+0261. The Latin letter g (U+0067) is not an IPA symbol |
| `ʤ` | `dʒ` | Write the affricate as two characters, not as the ligature U+02A4 |
| `ʧ` | `tʃ` | Write the affricate as two characters, not as the ligature U+02A7 |
| `r` | `ɹ` | The English approximant is U+0279. The symbol `r` is the alveolar trill |
| `e:` | `eː` | The length mark is U+02D0, not the colon (U+003A) |

## Plosives

| IPA | Code points | Description | Example languages |
|---|---|---|---|
| `p` | U+0070 | Voiceless bilabial plosive | Most languages |
| `b` | U+0062 | Voiced bilabial plosive | Most languages |
| `t` | U+0074 | Voiceless alveolar or dental plosive | Most languages |
| `d` | U+0064 | Voiced alveolar or dental plosive | Most languages |
| `k` | U+006B | Voiceless velar plosive | Most languages |
| `ɡ` | U+0261 | Voiced velar plosive | Most languages |
| `q` | U+0071 | Voiceless uvular plosive | Arabic |
| `ʔ` | U+0294 | Glottal stop | English (allophone), Arabic |
| `t̪` | U+0074 U+032A | Dental t | Spanish (before /θ/) |
| `d̪` | U+0064 U+032A | Dental d | Spanish (before /θ/) |

## Fricatives

| IPA | Code points | Description | Example languages |
|---|---|---|---|
| `f` | U+0066 | Voiceless labiodental fricative | Most languages |
| `v` | U+0076 | Voiced labiodental fricative | French, Italian, German, English |
| `θ` | U+03B8 | Voiceless dental fricative | English *think*, Castilian Spanish |
| `ð` | U+00F0 | Voiced dental fricative | English *the*, Spanish allophone of /d/ |
| `s` | U+0073 | Voiceless alveolar fricative | Most languages |
| `z` | U+007A | Voiced alveolar fricative | English, French, German |
| `ʃ` | U+0283 | Voiceless postalveolar fricative | English ⟨sh⟩, French, Portuguese |
| `ʒ` | U+0292 | Voiced postalveolar fricative | French, English *vision* |
| `ç` | U+00E7 | Voiceless palatal fricative | German *ich* |
| `ʝ` | U+029D | Voiced palatal fricative | Spanish ⟨ll⟩ and ⟨y⟩ |
| `x` | U+0078 | Voiceless velar fricative | Spanish *jota*, German *ach* |
| `ɣ` | U+0263 | Voiced velar fricative | Spanish allophone of /ɡ/ |
| `χ` | U+03C7 | Voiceless uvular fricative | Some Spanish dialects (*jota*) |
| `ʁ` | U+0281 | Voiced uvular fricative | French, German |
| `β` | U+03B2 | Voiced bilabial fricative | Spanish allophone of /b/ |
| `h` | U+0068 | Voiceless glottal fricative | English ⟨h⟩ |
| `ħ` | U+0127 | Voiceless pharyngeal fricative | Arabic |
| `ʕ` | U+0295 | Voiced pharyngeal fricative | Arabic |

## Affricates

| IPA | Code points | Description | Example languages |
|---|---|---|---|
| `tʃ` | U+0074 U+0283 | Voiceless postalveolar affricate | English, Spanish, Italian |
| `dʒ` | U+0064 U+0292 | Voiced postalveolar affricate | English *judge* |
| `ts` | U+0074 U+0073 | Voiceless alveolar affricate | German ⟨z⟩, Italian |
| `dz` | U+0064 U+007A | Voiced alveolar affricate | Italian, Catalan |
| `tɕ` | U+0074 U+0255 | Voiceless alveolo-palatal affricate | Mandarin, Japanese |
| `dʑ` | U+0064 U+0291 | Voiced alveolo-palatal affricate | Japanese |

## Nasals

| IPA | Code points | Description | Example languages |
|---|---|---|---|
| `m` | U+006D | Bilabial nasal | Most languages |
| `n` | U+006E | Alveolar nasal | Most languages |
| `ɲ` | U+0272 | Palatal nasal | Spanish, Portuguese, Italian |
| `ŋ` | U+014B | Velar nasal | English ⟨ng⟩, Germanic, Slavic |
| `ɱ` | U+0271 | Labiodental nasal | Spanish and Portuguese (before /f/) |
| `n̪` | U+006E U+032A | Dental nasal | Spanish (before /t d/) |

## Laterals

| IPA | Code points | Description | Example languages |
|---|---|---|---|
| `l` | U+006C | Alveolar lateral approximant | Most languages |
| `ʎ` | U+028E | Palatal lateral approximant | Portuguese ⟨lh⟩, Italian |
| `ɫ` | U+026B | Velarised lateral (dark l) | English coda, Ukrainian ⟨л⟩ |
| `lː` | U+006C U+02D0 | Geminate lateral | Catalan ⟨l·l⟩ |

## Rhotics

| IPA | Code points | Description | Example languages |
|---|---|---|---|
| `r` | U+0072 | Alveolar trill | Spanish ⟨rr⟩, Italian, Slavic |
| `ɾ` | U+027E | Alveolar tap | Spanish ⟨r⟩, Portuguese |
| `ɹ` | U+0279 | Alveolar approximant | English |
| `ʀ` | U+0280 | Uvular trill | French, German |
| `ɽ` | U+027D | Retroflex tap | Hindi |

## Approximants

| IPA | Code points | Description | Example languages |
|---|---|---|---|
| `j` | U+006A | Palatal approximant | Most languages |
| `w` | U+0077 | Labiovelar approximant | Most languages |
| `ɥ` | U+0265 | Labio-palatal approximant | French *nuit*, *lui* |

## Front vowels

| IPA | Code points | Description | Example |
|---|---|---|---|
| `i` | U+0069 | Close front unrounded | Spanish *si* |
| `iː` | U+0069 U+02D0 | Long close front unrounded | English *see* |
| `ɪ` | U+026A | Near-close front unrounded | English *sit* |
| `e` | U+0065 | Close-mid front unrounded | Spanish *mesa* |
| `eː` | U+0065 U+02D0 | Long close-mid front unrounded | German *See* |
| `ɛ` | U+025B | Open-mid front unrounded | French *tête*, Catalan open e |
| `æ` | U+00E6 | Near-open front unrounded | English *cat* |
| `y` | U+0079 | Close front rounded | French *lune* |
| `ø` | U+00F8 | Close-mid front rounded | French *feu* |
| `œ` | U+0153 | Open-mid front rounded | French *peur* |

## Central vowels

| IPA | Code points | Description | Example |
|---|---|---|---|
| `ə` | U+0259 | Mid central (schwa) | English *about*, French unstressed e |
| `ɐ` | U+0250 | Near-open central | Portuguese unstressed a |
| `ɨ` | U+0268 | Close central unrounded | European Portuguese unstressed e, Romanian ⟨â⟩ |
| `ɜ` | U+025C | Open-mid central unrounded | English *bird* (non-rhotic) |

## Back vowels

| IPA | Code points | Description | Example |
|---|---|---|---|
| `u` | U+0075 | Close back rounded | Spanish *luna* |
| `uː` | U+0075 U+02D0 | Long close back rounded | English *food* |
| `ʊ` | U+028A | Near-close back rounded | English *foot* |
| `o` | U+006F | Close-mid back rounded | Spanish *no* |
| `oː` | U+006F U+02D0 | Long close-mid back rounded | German *so* |
| `ɔ` | U+0254 | Open-mid back rounded | French and Italian open o |
| `ɑ` | U+0251 | Open back unrounded | English *father* |
| `ɑː` | U+0251 U+02D0 | Long open back unrounded | British *bath* |
| `a` | U+0061 | Open front or central unrounded | Spanish *casa* |

## Nasal vowels

| IPA | Code points | Description | Languages |
|---|---|---|---|
| `ã` | U+00E3 | Nasalised open | Portuguese |
| `ɐ̃` | U+0250 U+0303 | Nasalised near-open central | European Portuguese |
| `ẽ` | U+1EBD | Nasalised close-mid front | Portuguese |
| `ĩ` | U+0129 | Nasalised close front | Portuguese |
| `õ` | U+00F5 | Nasalised close-mid back | Portuguese |
| `ũ` | U+0169 | Nasalised close back | Portuguese |
| `ɛ̃` | U+025B U+0303 | Nasalised open-mid front | French *vin* |
| `ɑ̃` | U+0251 U+0303 | Nasalised open back | French *vent* |
| `ɔ̃` | U+0254 U+0303 | Nasalised open-mid back | French *bon* |
| `œ̃` | U+0153 U+0303 | Nasalised open-mid front rounded | French *brun*, which many speakers merge with ɛ̃ |

## Diphthongs

| IPA | Description | Example |
|---|---|---|
| `aɪ` | Open front to near-close front | English *price* |
| `aʊ` | Open front to near-close back | English *mouth* |
| `ɔɪ` | Open-mid back to near-close front | English *choice* |
| `eɪ` | Close-mid front to near-close front | English *face* |
| `oʊ` | Close-mid back to near-close back | American English *goat* |
| `ja` | Palatal glide and open vowel | Spanish *piano* |
| `je` | Palatal glide and close-mid front vowel | Spanish *bien*, *tierra* |
| `wa` | Labiovelar glide and open vowel | Spanish *cuando* |
| `aj` | Open vowel and palatal glide | Spanish *hay* |

## Diacritics

| Diacritic | Code point | Meaning | Example |
|---|---|---|---|
| `ʰ` | U+02B0 | Aspirated | `tʰ` in English *top* |
| `ʷ` | U+02B7 | Labialised | `kʷ` |
| `ʲ` | U+02B2 | Palatalised | `tʲ` in Russian |
| `ˤ` | U+02E4 | Pharyngealised | `ðˤ` in Arabic |
| `ː` | U+02D0 | Long | `aː` in German *Vater* |
| `◌̃` | U+0303 | Nasalised (combining) | `ã` in Portuguese |
| `◌̪` | U+032A | Dental (combining) | `t̪` in Spanish before /θ/ |
| `◌̥` | U+0325 | Voiceless (combining) | `d̥` |
| `◌̊` | U+030A | Voiceless, above a letter with a descender (combining) | `ɡ̊` in English |
| `◌̈` | U+0308 | Centralised (combining) | `ä` |
| `◌̚` | U+031A | No audible release (combining) | `t̚` in an English coda |

## Special symbols

| Symbol | Code point | Meaning |
|---|---|---|
| `∅` | U+2205 | Null: the phoneme is deleted. An empty string marks the same deletion |
| `ˈ` | U+02C8 | Primary stress |
| `ˌ` | U+02CC | Secondary stress |
| `.` | U+002E | Syllable boundary |
| `‿` | U+203F | Linking across a word boundary (liaison) |
| `\|` | U+007C | Minor prosodic break |
| `‖` | U+2016 | Major prosodic break |

## Notes by language

These notes say how the specs of some major languages encode a well-known feature. Each note names the spec and the value that it holds.

### Spanish

Castilian Spanish contrasts /θ/ and /s/ (distinción). The Latin American varieties and some Iberian dialects, such as those of the Canary Islands and parts of Andalusia, have only /s/ (seseo). The spec `es-ES` maps `c` to `["k", "θ"]` and `z` to `["θ"]`. A positional rule reads its ⟨c⟩ before ⟨e⟩ and ⟨i⟩ as /θ/. The specs `es-AR`, `es-CO` and `es-CL` read ⟨c⟩ before ⟨e⟩ and ⟨i⟩ as /s/, so `cielo` is [ˈsjelo] in `es-AR`.

Traditional Castilian keeps ⟨ll⟩ /ʎ/ apart from ⟨y⟩ /ʝ/ (lleísmo). Most speakers merge both to /ʝ/ (yeísmo), and `es-ES` follows them with `ll` as `["ʝ"]`. Rioplatense Spanish realises both as [ʃ] or [ʒ], so `es-AR` maps `ll` to `["ʃ", "ʒ"]`.

The voiced stops /b d ɡ/ have the spirant allophones [β ð ɣ] in every position except after a pause and after a nasal. Every `es-*` spec above `stub` lists these allophones, and `es-ES` reads `cada` as [ˈkaða].

### Portuguese

European Portuguese realises coda /s/ as [ʃ] before a consonant and at the end of a phrase. Brazilian Portuguese mostly keeps [s]. So `pastas` is [ˈpaʃtɐʃ] in `pt-PT` and [ˈpastas] in `pt-BR`.

European Portuguese reduces unstressed vowels strongly. Unstressed ⟨e⟩ becomes [ɨ] and unstressed ⟨a⟩ becomes [ɐ], so `pequeno` begins with [pɨ] in `pt-PT` and with [pe] in `pt-BR`. A European Portuguese dialect spec keeps this reduction, through inheritance or through entries of its own.

Portuguese has the nasal vowels /ã ẽ ĩ õ ũ/, and `pt-PT` writes the first as [ɐ̃]. The tilde letters ⟨ã⟩ and ⟨õ⟩ are grapheme keys. A vowel before ⟨m⟩ or ⟨n⟩ in a closed syllable gets its nasality from a positional rule. Before a consonant, ⟨m⟩ and ⟨n⟩ emit a combining tilde. So `canto` is [ˈkɐ̃tu] in `pt-PT`, with no key for ⟨an⟩.

### French

French has the labio-palatal approximant /ɥ/, as in *nuit* and *lui*. It is a separate sound from /j/ and /w/. The spec `fr-FR` maps ⟨ui⟩ to [ɥi], so `nuit` is [nɥi].

Liaison is a process across a word boundary, so the grapheme map holds the base forms only. The spec `fr-FR` declares liaison in `sandhi_rules` as z-, t-, n- and r-liaison, each marked with ‿.

French has four nasal vowels: /ɛ̃/ (*vin*), /ɑ̃/ (*vent*), /ɔ̃/ (*bon*) and /œ̃/ (*brun*). Many speakers merge /œ̃/ with /ɛ̃/.

### German

German devoices obstruents at the end of a word (Auslautverhärtung). The rule is allophonic, so `de-DE` maps ⟨d⟩ to the underlying /d/. A positional `word_final` entry gives [t], and the allophone map lists `"d": ["d", "t"]`. So `Rad` is [ˈʁat].

German ⟨sch⟩ is one grapheme key, /ʃ/, and not ⟨s⟩ followed by ⟨ch⟩. The tokenizer always takes the longest key that matches, so `schön` is [ˈʃœn] wherever the key sits in the file.

### English

The rhotic of English is the approximant /ɹ/, never the trill `r`. The code `en` resolves to `en-GB`, which is non-rhotic. The spec `en-US` is rhotic, so `car` is [ˈkɑː] in `en-GB` and [ˈkɑɹ] in `en-US`.

Received Pronunciation has [ɑː] in the BATH words (*bath*, *dance*, *path*), and General American has /æ/ in both TRAP and BATH. Both specs map `a` to the same ranked list, `["æ", "ɑː", "eɪ", "ə", "ɔː"]`. The spelling does not mark the BATH set, so both read `bath` as [ˈbæθ].

---
[← Quality tiers](quality_tiers.md) · [Home](index.md) · [Bibliography →](bibliography.md)
