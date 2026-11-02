# Brazilian Portuguese dialects (pt-BR-x-*)

The `pt-BR-x-*` specs model the regional speech of Brazil. Each one is a delta spec over [pt-BR](pt-BR.md): it inherits the general Brazilian standard and declares only what its region changes. This page first explains how the inheritance works. One table then compares the defining features of every lect. Each lect then has its own section, with its sources, its rules and their conditions, and its known gaps.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`. For the scores of each spec, see [../scoreboard.md](../scoreboard.md). For the list of registered specs, run `orthography2ipa list --family Ibero-Romance`.

## How the dialect specs inherit from pt-BR

Every spec on this page sets `parent` to `pt-BR`. It also sets the three base keys `graphemes_base`, `allophones_base` and `positional_graphemes_base` to `pt-BR`. So each dialect starts from the full standard. It gets /t d/ affrication before ⟨i⟩, coda /l/ to [w] and the alveolar coda /s/. It also gets coda nasalisation and final vowel raising. None of the specs sets `word_exceptions_base`, so the word exceptions of `pt-BR` do not reach them.

The dictionary fields `graphemes`, `allophones` and `positional_graphemes` merge key by key. An own entry replaces the `pt-BR` entry with the same key, and every other key is inherited. In `positional_graphemes` the key is the grapheme. So an own map for ⟨r⟩ replaces the whole ⟨r⟩ map of `pt-BR`.

The rule list `allophone_rules` merges by id through the `graphemes_base` edge (see [../allophony.md](../allophony.md#inheritance)). An own rule with the same id replaces the inherited rule in place. An own rule with a new id goes to the end of the list. A spec switches off an inherited rule when it declares the same id with an empty `phonemes` list. Six specs switch off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED` this way: `pt-BR-x-caipira`, `pt-BR-x-ce`, `pt-BR-x-norte`, `pt-BR-x-pr`, `pt-BR-x-recife` and `pt-BR-x-sul`. In these specs, a raised final ⟨e⟩ does not affricate /t d/.

The fields `allophone_passes` and `stress` are not inherited. Each spec declares its own `stress`. The specs that declare `allophone_passes: 2` run the post-lexical rules twice, as `pt-BR` does. The other specs run them once.

## Defining features

The table gives the features that set each lect apart from `pt-BR`. The lects run from the Southeast to the South, then the North, the Northeast and the Centre-West.

| Lect | Region | Features that set it apart | Example |
|:---|:---|:---|:---|
| [`pt-BR-x-rj`](#carioca-pt-br-x-rj) | Rio de Janeiro city | coda /s/ [ʃ] (*chiado*)<br>coda /r/ [x], final /r/ [h]<br>onset /r/ [χ] | `mesmo` [ˈmeʃmu], `porta` [ˈpoxtɐ], `mar` [ˈmah] |
| [`pt-BR-x-fluminense`](#fluminense-pt-br-x-fluminense) | Rio de Janeiro state | the Carioca coda deltas<br>onset /r/ [x] | `paz` [ˈpaʃ], `rato` [ˈxatu] |
| [`pt-BR-x-sp`](#paulistano-pt-br-x-sp) | São Paulo city | the `pt-BR` values unchanged | `porta` [ˈpoɾtɐ], `mesmo` [ˈmesmu] |
| [`pt-BR-x-caipira`](#caipira-pt-br-x-caipira) | São Paulo interior, Goiás, Mato Grosso | coda /r/ [ɻ]<br>onset /r/ [h]<br>no affrication before a final ⟨e⟩ | `porta` [ˈpoɻtɐ], `rato` [ˈhatu], `leite` [ˈlejti] |
| [`pt-BR-x-mg`](#mineiro-pt-br-x-mg) | Minas Gerais | pretonic /e o/ [i u] | `menino` [miˈninu], `coruja` [kuˈɾuʒɐ] |
| [`pt-BR-x-pr`](#paranaense-pt-br-x-pr) | Curitiba, Paraná | dental /t d/ before /i/<br>final /e/ [e]<br>onset /r/ [h] | `tia` [ˈtiɐ], `verde` [ˈveɾde], `rato` [ˈhatu] |
| [`pt-BR-x-sul`](#sulista-pt-br-x-sul) | Rio Grande do Sul | dental /t d/ before /i/<br>final /e/ [e]<br>onset /r/ [r] | `tia` [ˈtiɐ], `verde` [ˈveɾde], `rato` [ˈratu] |
| [`pt-BR-x-norte`](#nortista-pt-br-x-norte) | Belém, Manaus | coda /s/ [ʃ]<br>open pretonic [ɛ ɔ]<br>no affrication before a final ⟨e⟩ | `mesmo` [ˈmeʃmu], `menino` [mɛˈninu], `dente` [ˈdẽti] |
| [`pt-BR-x-bahia`](#baiano-pt-br-x-bahia) | Salvador, Bahia | open pretonic [ɛ ɔ] | `menino` [mɛˈninu], `boneca` [bɔˈnekɐ] |
| [`pt-BR-x-ce`](#cearense-pt-br-x-ce) | Fortaleza, Ceará | coda /s/ before a consonant [h]<br>open pretonic [ɛ ɔ]<br>no affrication before a final ⟨e⟩ | `mesmo` [ˈmehmu], `costas` [ˈkohtas] |
| [`pt-BR-x-recife`](#pernambucano-pt-br-x-recife) | Recife | dental /t d/ before /i/<br>coda /s/ [ʃ]<br>open pretonic [ɛ ɔ] | `tia` [ˈtiɐ], `mesmo` [ˈmeʃmu], `menino` [mɛˈninu] |
| [`pt-BR-x-brasilia`](#brasiliense-pt-br-x-brasilia) | Brasília | the `pt-BR` values unchanged | `tia` [ˈt͡ʃiɐ], `mesmo` [ˈmesmu] |

## Carioca (pt-BR-x-rj)

Carioca is the speech of the city of Rio de Janeiro, one of the two media-standard accents of Brazil. Its defining feature is the *chiado carioca*. A coda sibilant surfaces as the palatal [ʃ] or [ʒ], not as the alveolar [s z] of São Paulo or the interior.

> "A realização palatalizada do S em coda, no português do Brasil, o famoso 'chiado carioca', se restringia, de início, ao que tudo indica, ao Rio de Janeiro.", Callou (2010:134)

The NURC data of the 1990s shows how regular it is (Callou 2010:135, Tabela 1). The coda /S/ is palatal in 91 % of tokens inside the word (`ga[ʃ]to`) and in 76 % at the end of the word (`lapi[ʃ]`). The alveolar figures are 4 % and 19 %. It is the highest palatalisation index among the major Brazilian capitals.

The `pt-BR` base keeps an alveolar coda /s/, so the *chiado* is a phoneme-to-surface process. The spec models it with post-lexical rules, as `pt-PT` does with `PT_CODA_S_HUSH`. The rules apply in the coda only, so an onset ⟨s⟩ stays [s] or [z] (`sala` [ˈsalɐ], `casa` [ˈkazɐ]).

The Carioca rhotic is posterior. The positional map gives the strong onset ⟨r⟩ as [χ], with [x] and [h] as further candidates (`rio` [ˈχiu]). Callou describes the coda:

> "a variante que predomina na fala culta carioca … é a fricativa velar, com exceção em final de vocábulo, em que ocorre preferencialmente o apagamento ou a aspiração.", Callou (2010:138), reporting Callou (1987)

| Rule id | Rule | Example |
|:---|:---|:---|
| `RJ_CHIADO_CODA_S` | /s/ gives [ʃ] in the coda | `mesmo` [ˈmeʃmu], `paz` [ˈpaʃ], `dois` [ˈdojʃ] |
| `RJ_CHIADO_CODA_Z` | /z/ gives [ʒ] in the coda | no word in this list reaches it, see the gaps |
| `RJ_CODA_R_VELAR` | a coda /R/ before a consonant gives [x] | `porta` [ˈpoxtɐ], `carta` [ˈkaxtɐ] |
| `RJ_CODA_R_FINAL` | a word-final /R/ gives [h] | `mar` [ˈmah], `falar` [faˈlah] |

The spec writes a word-final /R/ as the aspirate [h], not as a deletion, so the segment stays in the output. The tap between vowels stays [ɾ] (`caro` [ˈkaɾu]). The spec inherits /t d/ affrication (`tia` [ˈt͡ʃiɐ], `tarde` [ˈtaxd͡ʒi]), coda /l/ to [w] (`sol` [ˈsɔw]) and final vowel raising from `pt-BR`.

Known gaps:

- The positional map gives a coda ⟨s⟩ as /s/ before any consonant. So `RJ_CHIADO_CODA_Z` never sees a /z/, and a voiced consonant does not voice the sibilant: `desde` [ˈdeʃd͡ʒi], `rasgar` [χaʃˈɡah].
- Voicing of a word-final sibilant before a voiced consonant in the next word is a sandhi process, and the spec does not apply it.
- The rhotic is socially graded between the suburbs and the Zona Sul (Callou 2010:138-139). A deterministic spec does not encode that distribution.

Sources listed in the spec: Callou (2010), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002), Cardoso et al. (2014, ALiB).

## Fluminense (pt-BR-x-fluminense)

Fluminense is the Portuguese of the state of Rio de Janeiro beyond the capital. Its coastal prestige form shares the Carioca profile. The spec models it with the same deltas as `pt-BR-x-rj`, under its own rule ids.

The NURC Rio data that measures the *chiado carioca* (Callou 2010:135) is the coastal Fluminense norm, and the spec uses it as the default.

| Rule id | Rule | Example |
|:---|:---|:---|
| `FLU_CHIADO_CODA_S` | /s/ gives [ʃ] in the coda | `mesmo` [ˈmeʃmu], `paz` [ˈpaʃ] |
| `FLU_CHIADO_CODA_Z` | /z/ gives [ʒ] in the coda | no word reaches it, as for Carioca |
| `FLU_CODA_R_VELAR` | a coda /R/ before a consonant gives [x] | `porta` [ˈpoxtɐ] |
| `FLU_CODA_R_FINAL` | a word-final /R/ gives [h] | `mar` [ˈmah] |

The rules apply in the coda only (`sala` [ˈsalɐ]). The positional map gives the strong onset ⟨r⟩ as [x], with [χ] and [h] as further candidates (`rato` [ˈxatu]). The spec inherits /t d/ affrication, coda /l/ to [w] and final vowel raising from `pt-BR`.

Fluminense is not uniform. The *chiado* is less regular in the rural and northern interior of the state. There, an inland tap rhotic, partly influenced by Caipira, coexists with the coastal palatal sibilant. The spec encodes the coastal prestige value and records the variation in its `notes`, without a second transcription. For the retroflex rhotic of the interior, see [Caipira](#caipira-pt-br-x-caipira).

Sources listed in the spec: Callou (2010), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002), Cardoso et al. (2014, ALiB).

## Paulistano (pt-BR-x-sp)

Paulistano is the urban Portuguese of the city and metropolitan region of São Paulo. It is the reference variety of the *Illustrations of the IPA* description of Brazilian Portuguese (Barbosa & Albano 2004). It is one of the two southeastern prestige norms on which `pt-BR` is built. So the spec declares no positional map and no rules of its own: it is `pt-BR` unchanged.

The coda /r/ is a plain alveolar tap [ɾ] (`porta` [ˈpoɾtɐ], `mar` [ˈmaɾ]). Amaral (1920) §6b describes a retroflex "r caipira" that *"assemelha-se bastante ao r inglês post-vocálico"*. That retroflex belongs to the Caipira interior around the city, not to the capital. `pt-BR-x-sp` is the non-retroflex member of the São Paulo pair.

The coda /s/ stays alveolar (`mesmo` [ˈmesmu], `dois` [ˈdojs]), never the Carioca [ʃ ʒ]. This is the southeastern sibilant pattern outside Rio (Barbosa & Albano 2004). The stops /t d/ affricate before ⟨i⟩ and before a raised final ⟨e⟩ (`tia` [ˈt͡ʃiɐ], `norte` [ˈnoɾt͡ʃi]).

The spec also inherits coda /l/ to [w] (`sol` [ˈsɔw]), final unstressed reduction, and the strong onset rhotic [ʁ] (`rato` [ˈʁatu]). A word-final ⟨r⟩ has an empty second candidate, for the infinitive /r/ that speakers drop.

Known gap: the height of a stressed ⟨o⟩ or ⟨e⟩ without an accent is lexical, and the spelling does not show it. The engine gives the close vowel unless a `PT_LEX_*` list names the word. So `porta` is [ˈpoɾtɐ], not [ˈpɔɾtɐ]. This gap applies to every Brazilian spec.

Sources listed in the spec: Barbosa & Albano (2004), Amaral (1920, §6b, for the contrast), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002).

## Caipira (pt-BR-x-caipira)

Caipira is the speech of the São Paulo interior, western Minas Gerais, Goiás, Mato Grosso, Mato Grosso do Sul and the Paraná hinterland. The foundational description is Amadeu Amaral's *O Dialeto Caipira* (1920), the first systematic dialect monograph on a Brazilian variety. The features below cite its numbered sections.

The hallmark of the dialect is the retroflex "r caipira". Amaral (1920) §6b:

> *"r inter e post-vocálico (arara, carta) possui um valor peculiar: é linguo-palatal e guturalizado. Na sua prolação … a língua … vira a extremidade para cima, sem tocá-la na abóbada palatal. Não há quase nenhuma vibração tremulante. Para o ouvido, este r caipira assemelha-se bastante ao r inglês post-vocálico."*

The tongue tip curls up without contact, with almost no trill, and the sound is close to English post-vocalic /r/. The spec writes it as the retroflex approximant [ɻ]. The positional map for ⟨r⟩ gives [ɻ] before a consonant and at the end of a word.

| Word | pt-BR | pt-BR-x-caipira |
|:---|:---|:---|
| porta | ˈpoɾtɐ | ˈpoɻtɐ |
| carta | ˈkaɾtɐ | ˈkaɻtɐ |
| mar | ˈmaɾ | ˈmaɻ |

A weak ⟨r⟩ between vowels stays a tap (`caro` [ˈkaɾu]). The strong onset ⟨r⟩ is [h], with [x] as the second candidate (`rato` [ˈhatu]). Amaral §23a reports that a word-final /r/ can drop: *"Cai, quando final de palavra: andá, muié, esquecê, subi, vapô"*. The spec gives the word-final ⟨r⟩ as `[ɻ, ""]`, so the deletion is the second candidate.

Amaral §22a gives a coda /l/ that turns into the same rhotic: *"l - Em final de sílaba, muda-se em r: quarquér, papér, mér, arma."*

Modern urban Caipira uses the general Brazilian [w] instead. So the positional map for ⟨l⟩ gives [w] first and Amaral's [ɻ] second, before a consonant and at the end of a word (`papel` [paˈpew]).

The coda /s/ is a plain alveolar [s], with no *chiado*. Amaral §6a: *"s propriamente sibilante, assobiado, e bem assim chiante, são aqui desconhecidos."* So `mesmo` is [ˈmesmu] and `costas` is [ˈkostas].

Amaral §25 reports that /ʎ/ becomes a glide: *"lh - Vocaliza-se em i: espaiado, maio, muié"*. In §6e he writes that the palatal lateral *"não existe no dialeto"*. The spec lists [j] as the second allophone of /ʎ/, after [ʎ]. The top output keeps [ʎ] (`mulher` [muˈʎeɻ]).

The spec switches off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED`. So /t d/ stay dental before a raised final ⟨e⟩ (`leite` [ˈlejti], `tarde` [ˈtaɻdi]), but they still affricate before a written ⟨i⟩ (`tia` [ˈt͡ʃiɐ], `dia` [ˈd͡ʒiɐ]). The notes of the two rules give no source for this split.

Known gaps:

- Amaral cites `porta` with an open [ɔ]. The height of an unmarked stressed vowel is lexical, so the engine gives the close [o].
- Amaral §8 reports that rural Caipira of his time kept a final unstressed /e/ and /o/. He writes *"Não se operou aqui a permuta de e final por i … como não se operou a de o por u."* Modern Caipira raises them like general Brazilian Portuguese, and the spec inherits the raising.

Sources listed in the spec: Amaral (1920, §6a-b, §8, §22a, §23a, §25), Castilho (2010), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002).

## Mineiro (pt-BR-x-mg)

Mineiro is the Portuguese of Minas Gerais, centred on Belo Horizonte. Its diagnostic feature is vocalic: the pretonic mid vowels /e o/ raise to the high vowels [i u] (*alçamento*).

> "as vogais médias [e,o] alçam para vogais [i,u] … como em p[i]ru … s[i]nhora e b[u]neca.", Lemos & Viegas (2016:314)

Lemos & Viegas (2016:314-315) give two causes: harmony with a following high vowel, and vowel reduction driven by the consonant. Viegas (1987) showed that the lexical item also plays a part. The trigger is a position in the spelling, a pretonic ⟨e⟩ or ⟨o⟩. So the spec puts the raising in the positional map, not in `allophone_rules`.

| Process | Rule | Example |
|:---|:---|:---|
| Pretonic raising of /e/ | ⟨e⟩ gives [i] before the stress | `menino` [miˈninu] |
| Pretonic raising of /o/ | ⟨o⟩ gives [u] before the stress | `coruja` [kuˈɾuʒɐ], `boneca` [buˈnekɐ] |

Mineiro keeps the alveolar coda /s/ of `pt-BR`. The spec declares no coda-sibilant rule, so `mesmo` stays [ˈmesmu] and `paz` stays [ˈpas]. This absence of an override is the contrast with the Carioca *chiado*.

The spec reduces a post-stressed ⟨e⟩ to [ɪ], and it keeps that vowel in ⟨-en⟩ and ⟨-ens⟩ (`hífen` [ˈifɪ̃], `homens` [ˈomɪ̃s]).

Known gaps:

- The source conditions the raising on harmony, on the consonant and on the word. The spec raises every pretonic ⟨e o⟩, including words with no high vowel after them (`segundo` [siˈɡũdu], `contar` [kũˈtaɾ]).
- Belo Horizonte uses the tap [ɾ] (`porta` [ˈpoɾtɐ]), and that is the encoded value. The rural interior shares the Caipira retroflex [ɻ], which [Caipira](#caipira-pt-br-x-caipira) models.
- Extreme posttonic reduction and syllable loss are stereotyped Mineiro traits. They are prosodic deletion processes outside the reach of a spec conditioned on graphemes, so the spec does not encode them.

Sources listed in the spec: Lemos & Viegas (2016), Castilho (2010), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002), Cardoso et al. (2014, ALiB).

## Paranaense (pt-BR-x-pr)

`pt-BR-x-pr` models Curitibano or Paranaense, the Portuguese of Curitiba and Paraná. It is a transitional variety between Sulista and Paulistano, over Slavic and Italian settler substrata. The spec overrides the conservative southern features.

The Curitibano default keeps dental /t d/ before /i/: `tia` [ˈtiɐ], `dia` [ˈdiɐ]. The positional map for ⟨t d⟩ gives the plain stop before ⟨i⟩. The spec also switches off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED`, so a raised final vowel does not affricate either. The spec `notes` record that younger and Paulista-influenced speakers do palatalise.

A final and unstressed /e/ stays [e] and does not raise to [i]: `verde` [ˈveɾde], not [ˈveɾd͡ʒi]. This is the Curitiba *e fechado*. The positional map for ⟨e⟩ gives [e] word-finally, posttonically and in an unstressed nucleus.

The coda /r/ is a Sulista alveolar tap [ɾ] (`porta` [ˈpoɾtɐ], `mar` [ˈmaɾ]). The strong onset ⟨r⟩ is [h], with [x] and [ʁ] as further candidates (`rato` [ˈhatu]). The retroflex "r caipira" (Amaral 1920 §6b) belongs to the northern Paraná interior, which patterns with [Caipira](#caipira-pt-br-x-caipira). This spec models the capital. The coda /s/ stays alveolar (`costas` [ˈkostas]), with neither the Carioca [ʃ] nor the Northeastern [h].

| Word | pt-BR-x-sp | pt-BR-x-pr |
|:---|:---|:---|
| tia | ˈt͡ʃiɐ | ˈtiɐ |
| verde | ˈveɾd͡ʒi | ˈveɾde |
| porta | ˈpoɾtɐ | ˈpoɾtɐ |

Known gaps:

- The spec keeps only the final /e/. A final /o/ still raises to [u] (`gato` [ˈɡatu]).
- Paraná is not uniform, and the interior is closer to Caipira. The spec encodes the Curitiba norm only.

Sources listed in the spec: Noll (2008), Cardoso et al. (2014, ALiB), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002), Amaral (1920, §6b, for the contrast).

## Sulista (pt-BR-x-sul)

`pt-BR-x-sul` models Sulista or Gaúcho Portuguese, the southern norm centred on Rio Grande do Sul and Porto Alegre. It extends loosely across Rio Grande do Sul, Santa Catarina and Paraná, over Italian and German settler substrata. Nascentes (1953:25) bases the North and South division of Brazilian Portuguese on the openness of the pretonic vowels. He puts this area among the *falares do Sul*.

The encoded default keeps dental /t d/ before /i/ (`tia` [ˈtiɐ], `dia` [ˈdiɐ]), the opposite of the southeastern norm. The positional map for ⟨t d⟩ gives the plain stop before ⟨i⟩, and the spec switches off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED`. The spec `notes` record a generational shift toward palatalisation in urban Porto Alegre.

The strong onset ⟨r⟩ is the alveolar trill [r], with [ʁ] as the second candidate (`rato` [ˈratu]). It is not the [h x] of São Paulo and Rio. The coda /r/ is a tap and does not drop (`mar` [ˈmaɾ]). A final unstressed /e/ stays [e] in conservative speech (`verde` [ˈveɾde]).

| Word | pt-BR-x-sp | pt-BR-x-sul |
|:---|:---|:---|
| tia | ˈt͡ʃiɐ | ˈtiɐ |
| rato | ˈʁatu | ˈratu |
| verde | ˈveɾd͡ʒi | ˈveɾde |

[Paranaense](#paranaense-pt-br-x-pr) has the same dental stops and the same final /e/. `pt-BR-x-sul` models the broader Gaúcho norm that the Paraná variety is transitional from. The two specs share these deltas on purpose. They differ in the onset rhotic.

Silva (2014:6-7, ALFAL XVII #4817-4818) cites Bisol (1994, 2012) on diphthongisation before a coda /S/. Bisol bases those impressions on Porto Alegre speech (Bisol 1994:125). That work is about diphthongs, not about the /r/ and /t d/ features of this spec.

Known gaps:

- Sulista covers three states with real internal variation. The Florianópolis coast leans toward a Carioca-like *chiado*, from VARSUL data in Silva (2014:5-6). The spec encodes the conservative Porto Alegre default and does not model Florianópolis or the Paraná interior.
- A final /o/ still raises to [u] (`gato` [ˈɡatu]).

Sources listed in the spec: Nascentes (1953), Noll (2008), Cardoso et al. (2014, ALiB), Silva (2014, ALFAL XVII), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002).

## Nortista (pt-BR-x-norte)

`pt-BR-x-norte` models Nortista or Amazônico Portuguese, of Belém and Manaus, with Tupí and Nheengatu contact in prosody and lexicon. Nascentes (1953:25) puts this area among the *falares do Norte*.

The coda /s z/ is palatal [ʃ] (`mesmo` [ˈmeʃmu], `paz` [ˈpaʃ]), as in Rio and unlike the alveolar norm of the Northeast proper. The positional map for ⟨s z⟩ gives [ʃ] before a consonant and at the end of a word, and keeps [z] between vowels. Silva (2014) gives the source:

> "[C]erto espraiamento dessas realizações para outras áreas do Brasil, a exemplo de Belém e Macapá, no Norte, onde haveria um grau de palatalização similar ao do Rio de Janeiro.", Silva (2014:2, ALFAL XVII, printed page header #4814), citing Noll (2008)

Silva (2014:2) also reports the grouping of Brazilian capitals by Mota, Jesus & Evangelista (2010), from ALiB data. It puts Belém and Macapá with Rio de Janeiro, Florianópolis, Recife, Manaus, Cuiabá and Salvador. In these capitals the palatal variant leads both inside the word and at the absolute end of the word.

The pretonic /e o/ open to [ɛ ɔ], a Northeastern feature that the North shares (`menino` [mɛˈninu], `boneca` [bɔˈnekɐ]). The stops /t d/ affricate before a written ⟨i⟩ (`tia` [ˈt͡ʃiɐ], `dia` [ˈd͡ʒiɐ]). ALiB data names the North as the region of strongest /t d/ palatalisation (Cardoso et al. 2014). The spec switches off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED`, so a raised final ⟨e⟩ keeps a dental stop (`dente` [ˈdẽti]). The notes of the two rules give no source for that.

| Word | pt-BR-x-sp | pt-BR-x-norte |
|:---|:---|:---|
| mesmo | ˈmesmu | ˈmeʃmu |
| tia | ˈt͡ʃiɐ | ˈt͡ʃiɐ |
| menino | meˈninu | mɛˈninu |

Known gaps:

- The positional map hands the post-lexical rules an [ʃ], and `BR_RAISE_FINAL_ES` and `BR_RAISE_FINAL_OS` look for an [s]. So a plural keeps the near-close vowel: `gatos` [ˈɡatʊʃ], `leites` [ˈlejtɪʃ].
- Nortista covers a vast region that the atlases describe thinly. Belém, the source of the *chiado* citation, and Manaus need not pattern alike, and the spec does not model the interior of Amazonia.

Sources listed in the spec: Nascentes (1953), Silva (2014, ALFAL XVII), Noll (2008), Cardoso et al. (2014, ALiB), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002).

## Baiano (pt-BR-x-bahia)

`pt-BR-x-bahia` models Baiano, the speech of Salvador and Bahia. It has the Northeastern open pretonic vowels: the positional map gives a pretonic ⟨e o⟩ as [ɛ ɔ] (`menino` [mɛˈninu], `boneca` [bɔˈnekɐ]).

The spec `notes` separate two ALiB phenomena. Salvador palatalises /t d/ before /i/, like most of Brazil, and only the context after a glide (*muito*, *oito*) shows low rates. So the spec keeps the affrication of `pt-BR` (`tia` [ˈt͡ʃiɐ], `leite` [ˈlejt͡ʃi]). The coda /s/ stays alveolar (`mesmo` [ˈmesmu]), unlike the Recife and Carioca *chiado*. The spec lists [j] as the second allophone of /ʎ/, for the weakening that its notes report.

Sources listed in the spec: Cardoso et al. (2014, ALiB), Castilho (2010), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002). The notes cite no page for these features.

## Cearense (pt-BR-x-ce)

`pt-BR-x-ce` models Cearense, the speech of Fortaleza. It has the Northeastern open pretonic vowels (`menino` [mɛˈninu]). Its diagnostic feature is the aspiration of a coda /s/ before a consonant: the positional map for ⟨s z⟩ gives [h] there (`mesmo` [ˈmehmu], `costas` [ˈkohtas]). A word-final /s/ stays [s] (`paz` [ˈpas]).

The spec `notes` report that ALiB and the urban norm of Fortaleza make /t d/ palatalisation before /i/ the prestige default. So the spec keeps the affrication before a written ⟨i⟩ (`tia` [ˈt͡ʃiɐ]). It switches off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED`, so a raised final ⟨e⟩ keeps a dental stop (`leite` [ˈlejti]).

Sources listed in the spec: Cardoso et al. (2014, ALiB), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002). The notes cite no page for these features.

## Pernambucano (pt-BR-x-recife)

`pt-BR-x-recife` models Pernambucano, the speech of Recife. The spec `notes` name its two strongest North and South isoglosses. First, /t d/ do not palatalise: the notes give about 10 % palatalisation in Recife from ALiB. The positional map for ⟨t d⟩ gives the plain stop before ⟨i⟩, and the spec switches off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED` (`tia` [ˈtiɐ], `leite` [ˈlejti]). Second, the pretonic /e o/ open to [ɛ ɔ] (`menino` [mɛˈninu], `boneca` [bɔˈnekɐ]).

The coda /s z/ is palatal [ʃ], the Recife *chiado* (`mesmo` [ˈmeʃmu], `paz` [ˈpaʃ]).

Known gaps:

- The spec `notes` describe an aspirated coda /R/, but the spec declares no rhotic map, so the coda keeps the tap of `pt-BR` (`mar` [ˈmaɾ]).
- As in Nortista, the palatal plural ⟨-s⟩ blocks the final raising rules: `gatos` [ˈɡatʊʃ].

Sources listed in the spec: Cardoso et al. (2014, ALiB), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002).

## Brasiliense (pt-BR-x-brasilia)

`pt-BR-x-brasilia` models Brasiliense or Candango Portuguese, the speech of Brasília, the planned capital inaugurated in 1960. The spec declares no positional map and no rules of its own. It is `pt-BR` unchanged (`tia` [ˈt͡ʃiɐ], `mesmo` [ˈmesmu], `vento` [ˈvẽtu]).

Brasília postdates by a decade the six *subfalares* into which Nascentes (1953) divides Brazil. So no historical *subfalar* exists to source a distinctive accent from, as there is for the older regions. The Brasiliense accent is a koiné. It formed from waves of internal migration, from 1956 onward, of construction workers and civil servants from every region. It converged on the dominant southeastern norm, close to São Paulo and Minas Gerais, over a Goiás and Centre-West substratum.

No source that the spec cites documents a phonemic feature that sets Brasiliense apart from that southeastern norm. The spec exists to name the variety and to record why it carries no divergence. If fieldwork on the Distrito Federal, for example from ALiB, documents a real phonemic difference, a sourced positional delta can follow. The page [../adding_a_language.md](../adding_a_language.md) describes the process.

Sources listed in the spec: Nascentes (1953, pp. 20, 23-25, for the context), Noll (2008), Mateus & d'Andrade (2000), Callou & Leite (2001), Silva (2002).

## Sources

- Amaral, Amadeu (1920). *O Dialeto Caipira.* Casa Editora "O Livro", São Paulo. §6a-b retroflex /r/ and laminodental /s/, §8 vowel retention, §22a coda /l/ rhotacism, §23a final /r/ deletion, §25 /ʎ/ vocalisation.
- Barbosa, P. A. & Albano, E. C. (2004). Brazilian Portuguese (Illustrations of the IPA). *Journal of the International Phonetic Association* 34(2): 227-232. [doi:10.1017/S0025100304001756](https://doi.org/10.1017/S0025100304001756)
- Callou, D. (with Leite, Y. & Moraes, J.) (2010). Um perfil da fala carioca. In Ribeiro, Costa & Cardoso (orgs.), *Dos sons às palavras: nas trilhas da língua portuguesa*, EDUFBA, pp. 129-140. p. 135, Tabela 1: the *chiado*. pp. 137-138: the posterior coda /R/.
- Callou, D. & Leite, Y. (2001). *Iniciação à fonética e à fonologia* (8th ed.). Zahar.
- Cardoso, S. A. M. et al. (2014). *Atlas Linguístico do Brasil (ALiB)*, vols. 1-2. EDUEL. Pretonic-vowel and palatalisation isoglosses.
- Castilho, Ataliba T. (2010). *Nova Gramática do Português Brasileiro.* Contexto.
- Lemos, F. A. P. & Viegas, M. C. (2016). O alçamento das vogais médias pretônicas em falares mineiros: os dados. *Caletroscópio* 4, número especial (II DIVERMINAS), pp. 314-333.
- Mateus, M. H. M. & d'Andrade, E. (2000). *The Phonology of Portuguese.* Oxford University Press.
- Nascentes, Antenor (1953). *O linguajar carioca* (2nd ed.). Organização Simões, Rio de Janeiro. pp. 20, 23-25: the North and South division on pretonic-vowel openness.
- Noll, Volker (2008). *O português brasileiro: formação e contrastes.* Globo.
- Silva, A. R. (2014). Variação fonética em capitais brasileiras: a ditongação diante de /S/ e as realizações fonéticas do /S/ em coda. *XVII Congreso Internacional ALFAL*, João Pessoa, #4813-4818. p. 2 (#4814): the Belém and Macapá coda /S/, citing Noll (2008) and Mota, Jesus & Evangelista (2010). pp. 6-7 (#4817-4818): Bisol (1994, 2012) on Porto Alegre speech.
- Silva, T. C. (2002). *Fonética e fonologia do português.* Contexto.

---
[← Brazilian Portuguese](pt-BR.md) · [Home](../index.md) · [Angolan Portuguese →](pt-AO.md)
