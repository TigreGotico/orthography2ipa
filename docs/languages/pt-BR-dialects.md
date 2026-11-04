# Brazilian Portuguese dialects (pt-BR-x-*)

The `pt-BR-x-*` specs model the regional speech of Brazil. Each one is a delta spec over [pt-BR](pt-BR.md): it inherits the general Brazilian standard and declares only what its region changes. This page first explains how the inheritance works. One table then compares the defining features of every lect. Each lect then has its own section, with its sources, its rules and its known gaps.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`. For the scores of each spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md). For the list of registered specs, run `orthography2ipa list --family Ibero-Romance`.

Most features on this page vary in speech. A spec gives one transcription, so it writes the variant that the cited source finds in most tokens for that city. The rule notes in each spec quote the source and its rate.

## How the dialect specs inherit from pt-BR

Every spec on this page sets `parent` to `pt-BR`. It also sets the three base keys `graphemes_base`, `allophones_base` and `positional_graphemes_base` to `pt-BR`. So each dialect starts from the full standard. None of the specs sets `word_exceptions_base`, so the word exceptions of `pt-BR` do not reach them.

The dictionary fields `graphemes`, `allophones` and `positional_graphemes` merge key by key. An own entry replaces the `pt-BR` entry with the same key, and every other key is inherited. In `positional_graphemes` the key is the grapheme. So an own map for ⟨e⟩ replaces the whole ⟨e⟩ map of `pt-BR`, and it must repeat every context it keeps.

The rule list `allophone_rules` merges by id through the `graphemes_base` edge (see [../engine/allophony.md](../engine/allophony.md#inheritance)). An own rule with the same id replaces the inherited rule in place. An own rule with a new id goes to the end of the list. A spec switches off an inherited rule when it declares the same id with an empty `phonemes` list. `pt-BR-x-pr` and `pt-BR-x-recife` switch off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED` this way.

The fields `allophone_passes` and `stress` are not inherited. Every spec on this page declares `allophone_passes: 2`, as `pt-BR` does. With one pass, a plural ending raised to [i] never reaches the affrication rule, and `dentes` keeps a plain [t].

`pt-BR-x-brasilia` is an alias of `pt-BR`. No opened source gives a feature that separates the speech of Brasília from the base: its coda /S/ is alveolar in 97 % of tokens (Hora 1999: 35, reporting Corrêa 1998).

## Defining features

The table gives the features that set each lect apart from `pt-BR`. The lects run from the Southeast to the South and the Centre-West, then the North and the Northeast. `pt-BR-x-floripa` and `pt-BR-x-cuiaba` have their own pages.

| Lect | Region | Features that set it apart | Example |
|:---|:---|:---|:---|
| [`pt-BR-x-rj`](#carioca-pt-br-x-rj) | Rio de Janeiro city | coda /s/ [ʃ], [ʒ] before a voiced consonant<br>coda /r/ [x], final /r/ [h]<br>onset /r/ [χ] | `festa` [ˈfeʃtɐ], `mesmo` [ˈmeʒmu], `porta` [ˈpoxtɐ], `mar` [ˈmah] |
| [`pt-BR-x-fluminen`](#fluminense-pt-br-x-fluminen) | Rio de Janeiro state interior | coda /r/ [h]<br>onset /r/ [x] | `porta` [ˈpohtɐ], `paz` [ˈpas], `rato` [ˈxatu] |
| [`pt-BR-x-sp`](#paulistano-pt-br-x-sp) | São Paulo city | strong /r/ [x], [ɣ] between vowels<br>yod before a final /s/ | `rato` [ˈxatu], `carro` [ˈkaɣu], `arroz` [aˈɣojs] |
| [`pt-BR-x-caipira`](#caipira-pt-br-x-caipira) | São Paulo interior | coda /r/ and coda /l/ [ɻ]<br>⟨lh⟩ [j] | `porta` [ˈpoɻtɐ], `alma` [ˈaɻmɐ], `filho` [ˈfiju] |
| [`pt-BR-x-mg`](#mineiro-pt-br-x-mg) | Belo Horizonte | pretonic /e/ [i] before a high vowel and word-initially<br>coda /r/ [h] | `pedido` [piˈd͡ʒidu], `escola` [isˈkolɐ], `porta` [ˈpohtɐ] |
| [`pt-BR-x-pr`](#paranaense-pt-br-x-pr) | Curitiba | /t d/ stops before /i/<br>final /e/ [e] | `tia` [ˈtiɐ], `verde` [ˈveɾde] |
| [`pt-BR-x-sul`](#sulista-pt-br-x-sul) | Porto Alegre | strong /r/ [x] | `rato` [ˈxatu], `carro` [ˈkaxu] |
| [`pt-BR-x-floripa`](pt-BR-x-floripa.md) | Florianópolis | coda /s/ [ʃ], [ʒ] before a voiced consonant<br>/t d/ stops before /i/ | `festa` [ˈfeʃtɐ], `mesmo` [ˈmeʒmu], `tipo` [ˈtipu] |
| [`pt-BR-x-cuiaba`](pt-BR-x-cuiaba.md) | Cuiabá river valley | /t d/ stops before /i/<br>⟨ch x j⟩ and soft ⟨g⟩ [t͡ʃ d͡ʒ] in the onset<br>coda /s/ [ʃ]<br>coda /l/ and coda /r/ [ɻ], final /r/ deleted<br>strong /r/ [r] | `chegar` [t͡ʃeˈɡa], `hoje` [ˈod͡ʒi], `mal` [ˈmaɻ], `porto` [ˈpoɻtu], `rapaz` [raˈpaʃ] |
| [`pt-BR-x-norte`](#nortista-pt-br-x-norte) | Belém | coda /s/ [ʃ], [ʒ] before a voiced consonant<br>coda /r/ [h] | `festa` [ˈfeʃtɐ], `mesmo` [ˈmeʒmu], `dentes` [ˈdẽt͡ʃiʃ], `porta` [ˈpohtɐ] |
| [`pt-BR-x-bahia`](#baiano-pt-br-x-bahia) | Salvador | open pretonic [ɛ ɔ] before an open, nasal or low vowel<br>coda /r/ [h], final /r/ deleted | `pedaço` [pɛˈdasu], `bolacha` [bɔˈlaʃɐ], `falar` [faˈla] |
| [`pt-BR-x-ce`](#cearense-pt-br-x-ce) | Fortaleza | the Baiano pretonics and rhotics<br>coda /s/ [h] before /d n/ | `pedaço` [pɛˈdasu], `desde` [ˈdehd͡ʒi] |
| [`pt-BR-x-recife`](#pernambucano-pt-br-x-recife) | Recife | /t d/ stops before /i/<br>coda /s/ [ʃ], [ʒ] before a voiced consonant<br>the Northeastern pretonics and rhotics | `tia` [ˈtiɐ], `festa` [ˈfeʃtɐ], `pedaço` [pɛˈdasu] |

## Carioca (pt-BR-x-rj)

Carioca is the speech of the city of Rio de Janeiro. Its defining feature is the *chiado*: a coda sibilant surfaces as the palatal [ʃ] or [ʒ]. Brito (2016: 148) finds that "[ʃ] or [ʒ] account for 85.3% of the occurrences". The palatal takes the voicing of the next consonant: it is "[z] or [ʒ] in syllable-final position followed by voiced consonant" (p. 142), as in `mesmo` [ˈmeʒmu]. The ALiB map gives a palatal rate above 76 % only in Rio de Janeiro, Belém and Florianópolis (Borges & Mendonça 2019: 58). Before a vowel in the next word, the sibilant is [z] (Nanini: 17).

The Carioca rhotic is posterior. Callou, Moraes & Leite (1998: 62-63) describe the coda /R/ as a range that "vai de uma vibrante, alveolar ou uvular, a uma fricativa, velar ou glotal, chegando a seu total apagamento". Word-final deletion reaches 73-82 % in verbs and 32 % in other words (p. 67).

| Rule id | Rule | Example |
|:---|:---|:---|
| `RJ_CHIADO_CODA_S` | /s/ gives [ʃ] in the coda | `festa` [ˈfeʃtɐ], `paz` [ˈpaʃ] |
| `RJ_CHIADO_CODA_Z` | /z/ gives [ʒ] in the coda | no word reaches it, see the gaps |
| `BR_CODA_SH_VOICED` | a coda [ʃ] gives [ʒ] before a voiced consonant | `mesmo` [ˈmeʒmu], `desde` [ˈdeʒd͡ʒi], `Lisboa` [liʒˈboɐ] |
| `RJ_CODA_R_VELAR` | a coda /R/ before a consonant gives [x] | `porta` [ˈpoxtɐ] |
| `RJ_CODA_R_FINAL` | a word-final /R/ gives [h] | `mar` [ˈmah] |

The positional map gives the strong onset ⟨r⟩ as [χ], with [x] and [h] as further candidates (`rio` [ˈχiu]). One R-forte class covers the start of a word (rio), ⟨rr⟩ (carro) and the onset after a consonant (Israel) (Cristófaro Silva 2025: 240), so ⟨rr⟩ and the rule `BR_STRONG_R_AFTER_CODA` give the same [χ] (`carro` [ˈkaχu], `honra` [ˈõχɐ]). Before this voiceless rhotic the coda sibilant stays voiceless (`desrespeito` [deʃχeʃˈpejtu]). The spec inherits /t d/ affrication (`tia` [ˈt͡ʃiɐ]) and coda /l/ to [w].

Known gaps:

- The spec writes a word-final /R/ as the aspirate [h] in every word (`falar` [faˈlah]). The source finds deletion in most verbs. The spec switches off the base rules `BR_FINAL_R_NONVERB`, `BR_INFINITIVE_R_DROP` and `BR_INFINITIVE_R_DROP_POR`, because they stand before `RJ_CODA_R_FINAL` and would decide every final /R/.

## Fluminense (pt-BR-x-fluminen)

Fluminense is the Portuguese of the state of Rio de Janeiro outside the capital. Its coda sibilant is alveolar. In the North-Northwest of the state, "há predomínio das realizações alveolares, ao contrário do que acontece na capital do Estado" (Hora 1999: 34-35, reporting Brandão). Its coda /R/ is glottal: ALiB counts 80 % glottal tokens in the state (Silva 2023: 68).

| Rule id | Rule | Example |
|:---|:---|:---|
| `FLU_CODA_R_GLOTTAL` | a coda /R/ before a consonant gives [h] | `porta` [ˈpohtɐ] |
| `FLU_CODA_R_FINAL` | a word-final /R/ gives [h] | `mar` [ˈmah] |

The strong onset ⟨r⟩ is [x] (`rato` [ˈxatu]). One R-forte class covers the start of a word (rio), ⟨rr⟩ (carro) and the onset after a consonant (Israel) (Cristófaro Silva 2025: 240), so ⟨rr⟩ and the rule `BR_STRONG_R_AFTER_CODA` give the same [x] (`carro` [ˈkaxu], `honra` [ˈõxɐ]). A coda /s/ takes the voicing of the next sound (Barbosa & Albano 2004: 229), so it is [z] before a voiced consonant and stays [s] before this voiceless rhotic (`mesmo` [ˈmezmu], `desrespeito` [desxesˈpejtu]). The coda sibilant keeps the base values (`festa` [ˈfestɐ], `paz` [ˈpas]). Like `pt-BR-x-rj`, the spec writes every word-final /R/ as [h] (`falar` [faˈlah]) and switches off the three base rules on the final tap.

## Paulistano (pt-BR-x-sp)

Paulistano is the urban Portuguese of São Paulo city, the variety that Barbosa & Albano (2004) describe. `pt-BR` follows the same source, so the spec adds only the two features that the source gives for this variety alone.

Strong /r/ is "a velar fricative, usually voiced between voiced sounds and voiceless elsewhere" (Barbosa & Albano 2004: 228, with carro [ˈkaɣʊ]). The positional map gives a word-initial ⟨r⟩ as [x], and ⟨rr⟩ is [ɣ]. After a coda consonant the rhotic follows a nasal vowel or a voiced [z], and the rule `BR_STRONG_R_AFTER_CODA` gives the voiced [ɣ] (`honra` [ˈõɣɐ], `genro` [ˈʒẽɣu]).

> "Diphthongs also emerge in this variety from yodisation of vowels (with the exception of [i]) followed by /S/, as in arroz [aɣoɪ̯s] 'rice' and mas [maɪ̯s] 'but'", Barbosa & Albano (2004: 229)

| Rule id | Rule | Example |
|:---|:---|:---|
| `SP_YOD_BEFORE_FINAL_S` | a stressed vowel other than /i/ takes [j] before a word-final /S/ | `arroz` [aˈɣojs], `mas` [ˈmajs], `três` [ˈtɾejs] |

The coda /r/ is the tap (`porta` [ˈpoɾtɐ]): "Entre os paulistanos, o tepe é a realização predominante" (Castro 2013: 566). The retroflex belongs to the rest of the state (see [Caipira](#caipira-pt-br-x-caipira)).

Known gap: the source gives yodisation in stressed final syllables. The spec does not apply it to an unstressed vowel.

## Caipira (pt-BR-x-caipira)

Caipira is the speech of the São Paulo interior and the neighbouring areas. The founding description is Amaral (1920), cited here by section.

The hallmark is the retroflex "r caipira". Amaral (1920) §6b: "r inter e post-vocálico (arara, carta) possui um valor peculiar: é linguò-palatal e guturalizado". ALiB finds it "de forma praticamente categórica em todo o estado de São Paulo [...] exceto na capital e na cidade de Santos" (Silva 2023: 70). The spec writes it as [ɻ] in the coda (`porta` [ˈpoɻtɐ], `mar` [ˈmaɻ]).

Amaral §22a gives a coda /l/ that turns into the same rhotic: "Em final de sílaba, muda-se em r: quarqué [...] arma". The positional map gives [ɻ] first and [w] second (`alma` [ˈaɻmɐ], `sol` [ˈsɔɻ]). Amaral §25 gives ⟨lh⟩ as [j]: "Vocaliza-se em i: [...] muié, fiio". The spec maps ⟨lh⟩ to [j] (`filho` [ˈfiju], `mulher` [muˈjeɻ]).

Known gaps:

- Amaral also gives intervocalic r as retroflex, ⟨ch j⟩ as affricates (§6d) and final e and o as unraised (§8). No modern source on these was opened, so the spec does not encode them.
- Amaral §23a gives a word-final r that drops. The spec keeps [ɻ].
- No opened source describes /t d/ before /i/ in this variety, so the spec follows the base (`leite` [ˈlejt͡ʃi]).

## Mineiro (pt-BR-x-mg)

Mineiro here is the speech of Belo Horizonte. Its pretonic raising varies: the alternations "têm status de variáveis lingüísticas, não podendo ser capturadas adequadamente por uma regra categorial" (Viegas & Veado 1982: 54). The spec raises /e/ where that study finds most tokens raised.

| Rule id | Rule | Rate (Viegas & Veado 1982: 58) | Example |
|:---|:---|:---|:---|
| `MG_PRETONIC_HARMONY_E` | pretonic /e/ gives [i] before a high vowel in the next syllable | 66.6 % | `pedido` [piˈd͡ʒidu], `perigo` [piˈɾiɡu] |
| `MG_INITIAL_E_RAISE` | word-initial unstressed /e/ gives [i] | 90.7 % | `escola` [isˈkolɐ] |
| `MG_INITIAL_EN_RAISE` | word-initial unstressed /ẽ/ gives [ĩ] | 100 % | `entender` [ĩtẽˈdeh] |

Without a high vowel next, /e/ stays [e] (`pecado` [peˈkadu]). The coda /R/ is glottal: ALiB counts "77% (1068) do /r/ glotal" in Minas Gerais, and 1 % tap (Silva 2023: 68). The positional map gives [h] in the coda (`porta` [ˈpohtɐ]).

Known gaps:

- Pretonic /o/ raising depends on the adjacent consonants (Viegas 2001: 229). The spec does not encode it, so `coruja` is [koˈɾuʒɐ].
- The harmony rule reads the vowel two graphemes to the right. A pretonic syllable closed by a consonant does not see the next vowel.

## Paranaense (pt-BR-x-pr)

Paranaense here is the speech of Curitiba. Final unstressed /e/ mostly stays [e]: Limeira (2013), reported by Franceschini & Loregian-Penkal (2023: 2), finds "62% para /o/ e 70% para /e/" of post-tonic mid vowels not raised. The spec keeps final [e] (`verde` [ˈveɾde]) and raises final /o/ as the base does.

ALiB rates Curitiba palatalisation of /t d/ as "moderada" (Battisti & Dornelles Filho 2015: 226). The spec keeps the stop as the first candidate before /i/ (`tia` [ˈtiɐ]) and switches off the two base rules that affricate before a raised ⟨e⟩.

Known gaps:

- The plural ending raises as in the base (`dentes` [ˈdẽtis]), while the singular keeps [e]. No opened source gives the plural rate.
- Silva (2023: 67) places Paraná in the retroflex zone of the coda /R/. The spec keeps the tap, and the opened sources do not settle the value for the capital.

## Sulista (pt-BR-x-sul)

Sulista here is the speech of Porto Alegre. The strong /r/ is the velar fricative. In Porto Alegre the trill fell "de 30,9% nos anos 1990 para apenas 0,4%" (Corrêa 2020: 87), and ALiB shows "o predomínio do uso da fricativa velar [x] nos estados do Rio Grande do Sul e Santa Catarina" (Comiotto & Margotti 2019: PDF p. 6). The positional map gives a word-initial ⟨r⟩ as [x], and ⟨rr⟩ is [x] (`rato` [ˈxatu], `carro` [ˈkaxu]). The rule `BR_STRONG_R_AFTER_CODA` gives the same [x] after a coda consonant (`honra` [ˈõxɐ]; Cristófaro Silva 2025: 240). A coda /s/ takes the voicing of the next sound (Barbosa & Albano 2004: 229), so it is [z] before a voiced consonant and stays [s] before this voiceless rhotic (`mesmo` [ˈmezmu], `desrespeito` [desxesˈpejtu]).

The other features follow the base. ALiB rates Porto Alegre palatalisation as categorical (Battisti & Dornelles Filho 2015: 226), so `tia` is [ˈt͡ʃiɐ] and `dentes` is [ˈdẽt͡ʃis]. Final /o/ raises in 97 % of Porto Alegre tokens (Franceschini & Loregian-Penkal 2023: 2), and no opened source gives final [e] for the capital (`verde` [ˈveɾd͡ʒi]). The coda /R/ is the tap, "from São Paulo southwards" (Barbosa & Albano 2004: 228).

Known gap: the trill and the low palatalisation rates belong to the Italian, German and border interior of the state (Dutra 2008: 48; Comiotto & Margotti 2019). This spec does not model the interior.

## Nortista (pt-BR-x-norte)

Nortista here is the speech of Belém. The coda sibilant is palatal (Borges & Mendonça 2019: 58), and /t d/ affricate before /i/: Belém 88 % (Oliveira 2013: 216), categorical in ALiB (Battisti & Dornelles Filho 2015: 226). The pretonic vowels stay closed: "a região Norte não pode ser caracterizada como uma área de vogais abertas" (Mota & Lopes 2018: 217). The coda /R/ is the glottal [h], dominant in the North in the ALiB maps (Silva & Aguilera, preprint).

| Rule id | Rule | Example |
|:---|:---|:---|
| `BR_RAISE_FINAL_ES` | the plural -es raises before [ʃ] as before [s] | `dentes` [ˈdẽt͡ʃiʃ] |
| `BR_RAISE_FINAL_OS` | the plural -os raises before [ʃ] as before [s] | `ovos` [ˈovuʃ] |
| `BR_CODA_SH_VOICED` | a coda [ʃ] gives [ʒ] before a voiced consonant | `mesmo` [ˈmeʒmu], `desde` [ˈdeʒd͡ʒi] |

The positional map gives a coda ⟨s⟩ as [ʃ] (`festa` [ˈfeʃtɐ]) and a coda ⟨r⟩ as [h] (`porta` [ˈpohtɐ]). Data from the Pará atlas give the coda /S/ as "pós-alveolar (surda e sonora), alveolar (surda e sonora)", aspirated or deleted (Marins & Margotti 2012: 255).

Known gap: Manaus is outside this spec. Its word-final /S/ is 67.1 % alveolar (Marins & Margotti 2012: 265).

## Northeastern pretonic vowels and rhotics

`pt-BR-x-bahia`, `pt-BR-x-ce` and `pt-BR-x-recife` share three rules. Pretonic mid vowels "têm uma maior probabilidade de se tornarem médias abertas no contexto de tônica também de timbre aberto (médias-baixas), médias nasais e diante da vogal baixa [a]" (Mota & Lopes 2018: 215). Before a close-mid stressed vowel they stay closed in 86 % (/e/) and 91 % (/o/) of tokens.

The coda /R/ in these capitals is "[- vibrante] e [- anterior]" (Callou, Serra & Cunha 2015: 197). Word-final deletion reaches 94-98 % in verbs and 62-95 % in other words in every capital (p. 207).

| Rule id | Rule | Example |
|:---|:---|:---|
| `NE_PRETONIC_OPEN_E` | pretonic /e/ gives [ɛ] before an open, nasal or low vowel | `pedaço` [pɛˈdasu] |
| `NE_PRETONIC_OPEN_O` | pretonic /o/ gives [ɔ] in the same context | `bolacha` [bɔˈlaʃɐ] |
| `NE_FINAL_R_DELETION` | a word-final /R/ is deleted | `falar` [faˈla], `mar` [ˈma] |

The positional map gives a coda ⟨r⟩ before a consonant as [h] (`porta` [ˈpohtɐ]). Before a high or close-mid vowel the pretonic stays closed (`pedido` [peˈd͡ʒidu]).

Known gaps:

- The trigger is the vowel two graphemes to the right, so a pretonic syllable closed by a consonant keeps the closed vowel (`espera` [esˈpɛɾɐ]).
- A stressed ⟨e o⟩ without an accent is close in the engine output, so `boneca` does not trigger the open pretonic.

## Baiano (pt-BR-x-bahia)

Baiano here is the speech of Salvador. ALiB groups Bahia with the Northeast for the open pretonics (Mota & Lopes 2018: 217). /t d/ affricate before /i/: "Em Salvador, o processo mostra-se variável, mas a proporção é alta, 85%" (Battisti & Dornelles Filho 2015: 225).

The coda sibilant is alveolar (`festa` [ˈfestɐ]). ALiB gives 49 % alveolar in Salvador, and the alveolar is the form of younger and university-educated speakers (Marins & Margotti 2012: 256, reporting Jesus & Mota 2006). The NURC data give an even split (p. 254), so this value is the weakest in the spec.

## Cearense (pt-BR-x-ce)

Cearense here is the speech of Fortaleza. ALiB rates its /t d/ palatalisation as categorical (Battisti & Dornelles Filho 2015: 226), so `gente` is [ˈʒẽt͡ʃi]. The coda sibilant is alveolar "em qualquer contexto" (Marins & Margotti 2012: 257, quoting Jesus & Mota 2007), so `costas` is [ˈkostas].

| Rule id | Rule | Example |
|:---|:---|:---|
| `CE_CODA_S_ASPIRATION` | coda /s/ gives [h] before /d n/ | `desde` [ˈdehd͡ʒi] |

Toledo & Cantoni (2021: 27) report the Fortaleza DSC corpus (Roncarati & Uchôa 2014): 16.1 % aspiration overall, 52 % before /d/ and 61 % before /n/. ALiB gives Fortaleza only 2 % aspiration (ibid.). The rule follows the popular speech of the DSC corpus in the two contexts where aspiration is the majority.

## Pernambucano (pt-BR-x-recife)

Pernambucano here is the speech of Recife. /t d/ stay stops before /i/: ALiB palatalisation "é baixa em Aracaju, Maceió, Recife, João Pessoa" (Battisti & Dornelles Filho 2015: 226). The positional map keeps ⟨ti di⟩ as stops, and the spec switches off the base rules for a raised final ⟨e⟩ (`tia` [ˈtiɐ], `dentes` [ˈdẽtiʃ]).

The coda sibilant is palatal: "Comporta-se Recife de forma semelhante ao Rio de Janeiro com o predomínio da pós-alveolar (69,5%)" in NURC (Marins & Margotti 2012: 254). ALiB gives an even split (p. 256). Before a voiced consonant the palatal is voiced: listeners in João Pessoa hear "me[ʒ]mo" as typical of "Rio de Janeiro e Recife" (Hora, Henrique & Amorim 2018: 284). The spec carries the same plural rules and the same voicing rule `BR_CODA_SH_VOICED` as `pt-BR-x-norte` (`mesmo` [ˈmeʒmu], `desde` [ˈdeʒdi]).

## Sources

- Amaral, A. (1920). *O Dialeto Caipira.* Casa Editora "O Livro", São Paulo. Cited by section.
- Barbosa, P. A. & Albano, E. C. (2004). Brazilian Portuguese (Illustrations of the IPA). *Journal of the International Phonetic Association* 34(2): 227-232. [doi:10.1017/S0025100304001756](https://doi.org/10.1017/S0025100304001756)
- Battisti, E. & Dornelles Filho, A. A. (2015). Análise em tempo real da palatalização de /t/ e /d/ no português falado em uma comunidade ítalo-brasileira. *Revista da ABRALIN* 14(1): 221-246. The ALiB capital map (Cardoso et al. 2014: 123) is summarised on p. 226.
- Borges, C. K. V. & Mendonça, J. J. (2019). A realização do /S/ na fala de universitários sergipanos do interior. *Primeira Escrita* 6: 57-73.
- Brito, E. P. (2016). The variation of post-vowel -S in the Portuguese dialect of Rio de Janeiro. *Cadernos de Estudos Linguísticos* 58(1): 139-151.
- Callou, D., Moraes, J. & Leite, Y. (1998). Apagamento do R final no dialeto carioca. *D.E.L.T.A.* 14 (número especial): 61-72.
- Callou, D., Serra, C. & Cunha, C. (2015). Mudança em curso no português brasileiro: o apagamento do R no dialeto nordestino. *Revista da ABRALIN* 14(1): 195-219.
- Castro, V. S. (2013). O "r caipira" em Mato Grosso do Sul. *Estudos Linguísticos* 42(1): 566-575.
- Comiotto, A. F. & Margotti, F. W. (2019). Uso dos róticos do português em contato com os dialetos italianos. *Acta Scientiarum. Language and Culture* 41(2).
- Corrêa, R. C. (2020). *Os significados sociais da realização variável da vibrante múltipla alveolar em onset silábico em Porto Alegre (RS).* PhD thesis, UFRGS.
- Cristófaro Silva, T. (2025). A Representação Fonológica dos Róticos no Português Brasileiro. *Caligrama* 30(3): 238-254. [doi:10.35699/2238-3824.2025.61138](https://doi.org/10.35699/2238-3824.2025.61138)
- Dutra, E. O. (2008). A palatalização das oclusivas dentais no município do Chuí, RS: perfil social. *Signos* 29(2): 47-64.
- Franceschini, L. T. & Loregian-Penkal, L. (2023). Análise da elevação da vogal átona final /o/ em Prudentópolis e Mallet, Paraná. *Interfaces* 13(4).
- Hora, D. (1999). Processo de palatalização das fricativas na língua portuguesa. *Revista do GELNE* 1(2): 34-36.
- Hora, D., Henrique, P. F. L. & Amorim, A. W. D. (2018). Produção e percepção: o processo de palatalização em jogo. *Diadorim* 20(2): 280-296. [doi:10.35520/diadorim.2018.v20n2a18269](https://doi.org/10.35520/diadorim.2018.v20n2a18269)
- Marins, F. S. & Margotti, F. W. (2012). Comportamento fonético-fonológico do /S/ pós-vocálico em Manaus. *Investigações* 25(2): 249-274.
- Mota, J. A. & Lopes, P. H. S. (2018). Os subfalares do Norte e o traçado das vogais médias pretônicas. *Estudos de Lingüística Galega*, volume especial I: 209-218.
- Nanini, R. F. *O /S/ pós-vocálico na fala carioca: uma análise dos falantes mais velhos de Copacabana.* Monografia, UFRJ.
- Oliveira, M. B. (2013). Os dados do ALiB: recaracterizando os falares amazônico e nordestino. *Actes du XXVIIe CILPR*, section 8: 209-219.
- Silva, H. C. (2023). Mapeamento da variação do /R/, em coda silábica interna, na Região Sudeste. *Signum* 26(3): 62-77.
- Silva, H. C. & Aguilera, V. A. Os róticos e a configuração dialetal do português brasileiro: de Nascentes ao ALiB. *SciELO Preprints* 14175 (not peer reviewed).
- Toledo, G. D. & Cantoni, M. M. (2021). Aspiração do /s/ em coda no português brasileiro: uma revisão sociolinguística. *Revista Colineares* 8(2): 21-46.
- Viegas, M. C. & Veado, R. M. A. (1982). Alçamento de vogais pretônicas. *Cadernos de Linguística e Teoria da Literatura* 4(7): 53-70.
- Viegas, M. C. (2001). Estudo sobre o alçamento de vogais médias pretônicas e os itens lexicais. *Revista do CESP* 21(28/29): 217-241.

---
[← Brazilian Portuguese](pt-BR.md) · [Home](../index.md) · [Florianópolis Portuguese →](pt-BR-x-floripa.md)
