# European Portuguese dialects (pt-PT-x-*)

The `pt-PT-x-*` specs model the regional speech of mainland Portugal, Madeira and the Azores. Each one is a delta spec over [pt-PT](pt-PT.md): it inherits the whole standard and declares only what its region changes. This page first explains how the inheritance works. One table then compares the defining features of every lect. Each lect then has its own section, with its sources, its rules and their conditions, and its known gaps.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, code)`. For the scores of each spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

## How the dialect specs inherit from pt-PT

Every spec on this page sets `parent` to `pt-PT`. It also sets the four base keys `graphemes_base`, `allophones_base`, `positional_graphemes_base` and `word_exceptions_base` to `pt-PT`. So each dialect starts from the full standard. It gets the vowel reduction, the coda nasalisation, the dark coda /l/, the coda *chiado*, the external /s/-sandhi and the word lists. It also gets what `pt-PT` itself takes from its own base, `pt-PT-x-medieval`.

The dictionary fields `graphemes`, `allophones`, `positional_graphemes` and `word_exceptions` merge key by key (`InheritanceMode.BASE_MERGE`). An own entry replaces the `pt-PT` entry with the same key, and every other key is inherited. In `positional_graphemes` the key is the grapheme. So an own map for ⟨s⟩ replaces the whole ⟨s⟩ map of `pt-PT`. A position that the dialect leaves out of that map falls back to the grapheme table, not to the `pt-PT` value for that position.

The rule lists `allophone_rules` and `sandhi_rules` merge by id (`InheritanceMode.OVERLAY_BY_ID`, see [../engine/allophony.md](../engine/allophony.md#inheritance)). The `pt-PT` rules keep their order. An own rule with the same id replaces the inherited rule in place. An own rule with a new id goes to the end of the list. The allophony stage applies the first rule whose phoneme and context match. So a dialect rule at the end of the list fires only where no inherited rule matched first.

A spec switches off an inherited rule when it declares the same id with an empty `phonemes` list. Such a rule matches no phoneme. Porto, Braga and Terceira switch off the suffix rules and word lists of `pt-PT` (`PT_SUFFIX_*`, `PT_LEX_*`), because their own stressed-vowel rules must reach the vowel first. The Algarve switches off `PT_FINAL_EM_NUCLEUS`, `PT_FINAL_ENS_NUCLEUS` and `PT_FINAL_ENS_GLIDE`.

The specs `pt-PT-x-sao-miguel` and `pt-PT-x-terceira` name `pt-PT-x-acores` as an adstrate in `ancestors`. That entry records the relation only. Both specs take their data from `pt-PT`, so they do not inherit the rules of `pt-PT-x-acores`. The spec `pt-PT-x-medieval` (Old Portuguese) has the same code prefix. It is the base of `pt-PT`, not a dialect of it, so this page does not cover it.

## Defining features

The table gives the features that set each lect apart from `pt-PT`. The lects run from north to south, then the islands.

| Lect | Region | Features that set it apart | Example |
|:---|:---|:---|:---|
| [`pt-PT-x-viana`](#alto-minhoto-pt-pt-x-viana) | Alto Minho | four sibilants, apical ⟨s ss⟩ [s̺ z̺] against laminal ⟨c ç z⟩ [s z]<br>/v/ to [b]<br>⟨ch⟩ [tʃ]<br>⟨-em⟩ [ẽj̃] | `passo` [ˈpas̺u], `paço` [ˈpasu], `chave` [ˈtʃabɨ] |
| [`pt-PT-x-tras-os-montes`](#transmontano-pt-pt-x-tras-os-montes) | Trás-os-Montes e Alto Douro | the same as Alto Minho | `casa` [ˈkaz̺ɐ], `vinho` [ˈbiɲu] |
| [`pt-PT-x-minho`](#minhoto-pt-pt-x-minho) | Baixo-Minho | apical-only sibilants [s̺ z̺]<br>/v/ to [b], [β] between vowels<br>pretonic ⟨en⟩ [ɨ̃]<br>⟨-em⟩ [ẽj̃] | `cedo` [ˈs̺ɛdu], `uva` [ˈuβɐ], `pensar` [pɨ̃ˈsaɾ] |
| [`pt-PT-x-braga`](#bracarense-pt-pt-x-braga) | Braga | /v/ to [b]<br>stressed mid vowels to rising diphthongs<br>⟨ou⟩ [ow], ⟨ei⟩ [ej]<br>⟨ss⟩ [s̺] | `mês` [ˈmjeʃ], `café` [kɐˈfjɛ], `pouco` [ˈpowku] |
| [`pt-PT-x-porto`](#portuense-pt-pt-x-porto) | Porto, Douro Litoral | /v/ to [b]<br>stressed mid vowels to rising diphthongs<br>⟨ou⟩ [ow], ⟨ei⟩ [ej]<br>⟨ss⟩ [s̺] | `avô` [ɐˈbwo], `Porto` [ˈpwɔɾtu], `leite` [ˈlejtɨ] |
| [`pt-PT-x-alfena`](#alfena-pt-pt-x-alfena) | Alfena, Valongo | apical-only sibilants<br>/v/ to [b]<br>vowel breaking as an allophone variant only | `zebra` [ˈz̺ɛbɾɐ], `vaca` [ˈbakɐ] |
| [`pt-PT-x-aveiro`](#beira-litoral-pt-pt-x-aveiro) | Aveiro coast | apical-only sibilants<br>/v/ to [b]<br>[ɭ] as an allophone variant only | `praça` [ˈpɾas̺ɐ], `vaca` [ˈbakɐ] |
| [`pt-PT-x-beira`](#beira-pt-pt-x-beira) | Beira Litoral, Alta and Baixa | apical-only sibilants<br>/v/ to [b]<br>stressed /u/ to [y] | `tudo` [ˈtydu], `sul` [ˈs̺yɫ] |
| [`pt-PT-x-coimbra`](#conimbricense-pt-pt-x-coimbra) | Coimbra | the standard values, plus [ʒ] for a final /s/ before a vowel | `os olhos` [oʒ ˈoʎuʃ] |
| [`pt-PT-x-lisbon`](#lisbon-pt-pt-x-lisbon) | Lisbon, Estremadura | stressed ⟨e⟩ to [ɐ] before a palatal<br>⟨ei⟩ [ɐj]<br>⟨ou⟩ [o] | `espelho` [eʃˈpɐʎu], `leite` [ˈlɐjtɨ] |
| [`pt-PT-x-alentejo`](#alentejano-pt-pt-x-alentejo) | Alto Alentejo | stressed /u/ to [y]<br>final unstressed high vowels deleted<br>⟨-d-⟩ deleted<br>⟨ei ou⟩ monophthongs | `sul` [ˈsyɫ], `gosto` [ˈɡɔʃt], `nada` [ˈnaɐ] |
| [`pt-PT-x-algarve`](#algarvio-pt-pt-x-algarve) | Algarve | stressed /u/ to [y]<br>word-final /s/ [ʒ]<br>⟨ei ou⟩ monophthongs<br>unstressed ⟨e o⟩ kept | `tudo` [ˈtydu], `mas` [ˈmaʒ], `pedir` [peˈdiɾ] |
| [`pt-PT-x-madeira`](#madeiran-pt-pt-x-madeira) | Madeira | /l/ to [ʎ] after /i/<br>⟨-ões -ães -ãos⟩ as a nasal vowel plus [n] | `quilo` [ˈkiʎu], `cães` [ˈkɐ̃ns] |
| [`pt-PT-x-acores`](#azorean-pt-pt-x-acores) | Azores, general node | stressed /u/ to [y] before an onset consonant only<br>⟨ou⟩ [ow]<br>[ʒ] for a final /s/ before a vowel | `número` [ˈnymɨɾu], `azul` [ɐˈzuɫ] |
| [`pt-PT-x-sao-miguel`](#micaelense-pt-pt-x-sao-miguel) | São Miguel | every stressed /u/ to [y]<br>⟨oi ou⟩ [ø]<br>/l/ to [ʎ] after /i/<br>[ʒ] for a final /s/ before a vowel | `azul` [ɐˈzyɫ], `pouco` [ˈpøku], `quilo` [ˈkiʎu] |
| [`pt-PT-x-terceira`](#terceirense-pt-pt-x-terceira) | Terceira | stressed /a/ to [ɔ] before final ⟨-o⟩<br>[w] on-glide after a labial<br>no /u/ fronting | `gato` [ˈɡɔtu], `bola` [ˈbwɔlɐ], `tudo` [ˈtudu] |

## Northern sibilant systems

Archaic Portuguese had four sibilants: apico-alveolar [s̺ z̺], from ⟨s⟩ and ⟨ss⟩, against laminal (predorsodental) [s z], from ⟨c⟩ before ⟨e i⟩, ⟨ç⟩ and ⟨z⟩. Cintra (1971, p. 93) writes:

> *"a existência de um sistema de quatro sibilantes, [s̺] e [z̺] ápicoalveolares (correspondentes aos grafemas s e ss)… opondo-se a e convivendo com o [s] e o [z] predorsodentais (correspondentes aos grafemas ce,i, ç e z)."*

The specs model three systems:

| System | Specs | ⟨s ss⟩ | ⟨c ç z⟩ |
|:---|:---|:---|:---|
| four sibilants | `pt-PT-x-viana`, `pt-PT-x-tras-os-montes` | apical [s̺ z̺] | laminal [s z] |
| apical only | `pt-PT-x-minho`, `pt-PT-x-alfena`, `pt-PT-x-aveiro`, `pt-PT-x-beira` | apical [s̺ z̺] | apical [s̺ z̺] |
| laminal only | `pt-PT` and the other specs | laminal [s z] | laminal [s z] |

Álvarez Pérez (2014, pp. 37-38) describes the split from ALEPG data:

> *"the other groups of northern dialects, denoted by Cintra as Baixo-Minhotos, Durienses and Beirões, kept only the apico-alveolar branch. On the other hand, the rest of Portugal (as well as standard Portuguese) neutralised the opposition in favour of laminal sibilants."*

The apico-alveolar segment is a real IPA symbol, [s̺], which is s plus U+033A COMBINING INVERTED BRIDGE BELOW. The specs write it actively and do not delete it. Cintra's own term is *apico-alveolar* or *reverso*. Modern IPA often writes his [s̺ z̺] as [ʂ ʐ], because the *s beirão* sounds close to a retroflex. The four-sibilant specs list [ʂ ʐ] as allophone variants and keep Cintra's symbols as the default.

Porto and Braga sit in the apical zone too, but their specs declare only ⟨ss⟩ as [s̺]. Carrying the apical to ⟨s⟩, ⟨ç⟩, ⟨c⟩ and ⟨z⟩ is an open limit of those two specs.

## Northern betacism

In the North the /v/ and /b/ opposition is lost. Cintra (1971, pp. 87-88) gives this as his first northern feature:

> *"o desaparecimento da oposição fonológica entre os fonemas /v/ e /b/ e a sua fusão num fonema único /b/, realizado ora como oclusiva, ora como fricativa (ou espirante) b ou β."*

The specs encode the merger in two ways:

| Specs | Mechanism | Example |
|:---|:---|:---|
| `pt-PT-x-viana`, `pt-PT-x-tras-os-montes` | allophone rule `PT_NORTH_BETACISM` (/v/ to [b]), [β] as a variant | `estava` [eʃˈtabɐ] |
| `pt-PT-x-porto` | allophone rule `PT_PORTO_BETACISM` (/v/ to [b]) | `vinho` [ˈbiɲu] |
| `pt-PT-x-braga` | allophone rule `BRA_BETACISM` (/v/ to [b]), [β] as a variant | `vou` [ˈbow] |
| `pt-PT-x-minho`, `pt-PT-x-alfena`, `pt-PT-x-aveiro`, `pt-PT-x-beira` | grapheme ⟨v⟩ to [b], and [β] between vowels | `vaca` [ˈbakɐ], `uva` [ˈuβɐ] |

An allophone rule applies to every /v/, from whatever grapheme it comes.

Álvarez Pérez (2014, pp. 35-37) checked the extent with the ALEPG corpus. The merger covers about twice the area of Cintra's map. It is categorical in the far north. It reaches along the coast beyond the district of Coimbra, and through the eastern districts of Guarda and Castelo Branco. That is why all the Baixo-Minhoto-Duriense-Beirão specs carry it. The southern and island specs keep /v/ and /b/ apart.

## Stressed /u/ fronting

The specs for the Beira, the Alentejo, the Algarve, the Azores and São Miguel front a stressed /u/ to the front rounded [y]. Terceira does not. The rules differ in their conditions:

| Spec | Rules, in order | Condition |
|:---|:---|:---|
| `pt-PT-x-beira` | `BEI_U_NO_FRONT_AFTER_BILABIAL`, `BEI_U_FRONTING` | stressed nucleus, not after /p b m/ |
| `pt-PT-x-alentejo` | `ALE_U_NO_FRONT_AFTER_BILABIAL`, `ALE_U_FRONTING` | stressed nucleus, not after /p b m/ |
| `pt-PT-x-algarve` | `ALG_U_NO_FRONT_AFTER_BILABIAL`, `ALG_U_FRONTING` | stressed nucleus, not after /p b m/ |
| `pt-PT-x-acores` | `ACO_U_KEEP_BEFORE_CODA`, `ACO_STRESSED_U_FRONTING` | stressed, before an onset consonant, not before a coda liquid or sibilant |
| `pt-PT-x-sao-miguel` | `SM_U_FRONTING` | every stressed /u/ |

A guard rule comes first and rewrites /u/ to [u]. Because the first matching rule fixes the surface, the fronting rule after it does not fire in that context.

The mainland specs share the bilabial guard. Brissos (2014b, AVOC acoustic atlas) shows that after a bilabial onset the vowel loses most of its advancement and is close to [u]. The rule notes give the figures. The guard is a categorical simplification of a gradient effect. So `mudo` is [ˈmudu] in the Algarve and the Beira, against `tudo` [ˈtydu].

The word-level stress detector marks a monosyllabic clitic as stressed. Without a guard, a fronting rule would change the article `o` to [ˈy]. So every fronting spec pins the clitics `o os no nos do dos ao aos pelo pelos um uns` in `word_exceptions`, and none of them gets [y]. Each section below gives the values.

## /s/-sandhi before a vowel

A word-final /s/ before a vowel-initial word is [z] in `pt-PT` (rule `PT_FINAL_S_PREVOCALIC_VOICE`, see [pt-PT](pt-PT.md#external-s-sandhi)). Some lects use the post-alveolar [ʒ] instead, the "Tajaver" pronunciation:

| Spec | Value | `estás a ver` | Mechanism |
|:---|:---|:---|:---|
| `pt-PT-x-porto` | [z] | [eʃˈtaz ɐ ˈbjeɾ] | inherited |
| `pt-PT-x-lisbon` | [z] | [eʃˈtaz ɐ ˈveɾ] | inherited |
| `pt-PT-x-coimbra` | [ʒ], the marked pole of a variable [z] and [ʒ] | [eʃˈtaʒ ɐ ˈveɾ] | rule redeclared with transform `ʒ` |
| `pt-PT-x-algarve` | [ʒ] in every word-final position | [eʃˈtaʒ ɐ ˈveɾ] | positional `word_final` [ʒ] for ⟨s⟩ |
| `pt-PT-x-acores` | [ʒ] before a vowel only | [eʃˈtaʒ ɐ ˈveɾ] | rule redeclared with transform `ʒ` |
| `pt-PT-x-sao-miguel` | [ʒ] before a vowel only | [eʃˈtaʒ ɐ ˈveɾ] | rule redeclared with transform `ʒ` |
| `pt-PT-x-viana`, `pt-PT-x-tras-os-montes` | [s̺] | [eʃˈtas̺ ɐ ˈbeɾ] | the rule matches a final [ʃ] only |

The other specs inherit [z]. The Algarve gives [ʒ] in every word-final position, so it also gives [ʒ] alone (`estás` [eʃˈtaʒ]). The Azores and São Miguel restrict [ʒ] to the position before a vowel. Before a voiceless consonant or a pause the sibilant stays [ʃ] (`estás só` [eʃˈtaʃ ˈsɔ]), and before a voiced consonant the inherited `PT_CODA_S_VOICING` gives [ʒ] (`estás bem` [eʃˈtaʒ ˈbɐ̃j̃]).

The standard [z] is well documented (Mateus & d'Andrade 2000, ch. 2).

The southern and island [ʒ] comes from a native-speaker source that is not academic. That source is the [video](https://www.youtube.com/watch?v=pitj0XxYO7I) "The 8 accents" by *Portuguese With Leo*. The video places [ʒ] strongest in the Algarve ("Tajaver", "quijentrar", "muitojamigos"). São Miguel shares it ("Todojos", "quijentrar", "Éjunúmerúm" for *és o número um*), and Coimbra varies. It gives Lisbon and the North [z], and calls [ʒ] there "wrong".

No page-pinned academic source for this sandhi value was found. The feature sits inside the documented southern and island behaviour of the final sibilant, [ʃ] or [z] or [ʒ]. The sources for that behaviour are Cintra (1971), Brissos (2014) and Segura da Cruz (1989) for the Algarve, and Rogers (1948) for the islands. The spec notes of `pt-PT-x-acores` and `pt-PT-x-algarve` state this limit. Cintra's primary North/South isogloss is a different matter: it is the place of the sibilant (apico-alveolar or predorsodental), not this [z] and [ʒ] contrast.

There is counter-evidence that is recorded but not modelled. The Trás-os-Montes speaker from Chaves (*Portuguese With Leo*) also uses [ʒ] before a vowel, and says it is "muito espalhado" in the North. This contradicts the [z] for the North. The `pt-PT-x-tras-os-montes` notes record it, but the spec does not model it. The evidence is a single casual attestation, against the academic [z].

## Alto-Minhoto (pt-PT-x-viana)

`pt-PT-x-viana` models the Alto Minho (Viana do Castelo, Ponte de Lima). Cintra (1971, p. 93) groups it with Trás-os-Montes as one *grupo transmontano-alto-minhoto*. These conservative northern varieties alone keep the medieval four-sibilant system, and the two specs share the same deltas. Sources: Cintra (1971), Álvarez Pérez (2014), Mateus & d'Andrade (2000).

The four sibilants come from a positional map for ⟨s⟩ and a grapheme ⟨ss⟩. The laminal ⟨c ç z⟩ stay inherited and unmarked, as in the Mirandese (`mwl`) notation:

| Grapheme (position) | Sibilant | IPA | Example |
|:---|:---|:---|:---|
| ⟨s⟩ initial, ⟨ss⟩ | voiceless apico-alveolar | [s̺] | `sal` [ˈs̺aɫ], `passo` [ˈpas̺u] |
| ⟨s⟩ word-final | voiceless apico-alveolar | [s̺] | `anos` [ˈɐnus̺] |
| ⟨-s-⟩ between vowels | voiced apico-alveolar | [z̺] | `casa` [ˈkaz̺ɐ], `coser` [kuˈz̺eɾ] |
| ⟨c⟩ before ⟨e i⟩, ⟨ç⟩ | voiceless laminal | [s] | `paço` [ˈpasu], `cinco` [ˈsĩku] |
| ⟨z⟩ | voiced laminal | [z] | `cozer` [kuˈzeɾ] |

The minimal pairs stay apart: `passo` [ˈpas̺u] against `paço` [ˈpasu], and `coser` [kuˈz̺eɾ] against `cozer` [kuˈzeɾ]. Note 29 of Cintra (1971), a footnote to p. 93, fixes the positions: *"[s̺] ápico-alveolar (correspondente a s inicial e final e ss interior) … [z̺] ápicoalveolar (correspondente ao s intervocálico)"*. Álvarez Pérez (2014, p. 37, §4) confirms from ALEPG data that this system belongs to *"the group of dialects that Cintra called Transmontanos and Alto-Minhotos"*, with the same grapheme mapping.

Betacism is the rule `PT_NORTH_BETACISM` (see [Northern betacism](#northern-betacism)): `vinho` [ˈbiɲu], `vaca` [ˈbakɐ], `estava` [eʃˈtabɐ]. The CLUP Alto-Minho gold attests it (`vou` as `bow`, `ver` as `beɾ`).

The archaic ⟨ch⟩ affricate stays apart from ⟨x⟩ (Cintra 1971, p. 87): *"a permanência da distinção fonológica em posição inicial de sílaba entre o fonema /tʃ/, representado pelo grafema ch e o fonema /ʃ/ representado pelo grafema x"*. The grapheme ⟨ch⟩ is [tʃ]: `chave` [ˈtʃabɨ].

Two nasal rules follow the northern values. Word-final ⟨-em⟩ keeps the close-mid nucleus, [ẽj̃] (`bem` [ˈbẽj̃]), through an override of `PT_FINAL_EM_NUCLEUS`. A pretonic ⟨en em⟩ keeps the reduced vowel, nasal [ɨ̃] (`pensar` [pɨ̃ˈsaɾ]), because the override of `PT_NASAL_E_UNRED` is limited to post-tonic syllables. The rule notes cite Leite de Vasconcellos (1900, 1901) for both.

Known gaps:

- A preconsonantal coda ⟨s⟩ keeps the inherited *chiado* [ʃ]: `festa` [ˈfɛʃtɐ], `gosto` [ˈɡɔʃtu]. Cintra's note 29 lists the [s̺] positions as *"s inicial e final e ss interior"* only.
- The word-final [s̺] does not match the inherited prevocalic sandhi rule, which expects [ʃ]. So the sibilant stays [s̺] before a vowel: `estás a ver` [eʃˈtas̺ ɐ ˈbeɾ].
- Porto's diphthongisation of the stressed close vowels is a Baixo-Minho and Douro-Litoral feature. Cintra (1971, p. 93) puts it in the other northern group, so this spec does not apply it.
- The `clup_dialect` gold for this spec is small, sentence-level and of undocumented IPA provenance. It writes the apico-alveolar series in several ways ([ʃ], [ʂ], plain [s]). So correctness rests on the cited sources, not on the score.

## Transmontano (pt-PT-x-tras-os-montes)

`pt-PT-x-tras-os-montes` models Trás-os-Montes e Alto Douro (Bragança, Chaves, Valpaços). It is in the same *grupo transmontano-alto-minhoto* as [Alto-Minhoto](#alto-minhoto-pt-pt-x-viana), and it has the same four-sibilant map, the same rule `PT_NORTH_BETACISM` and the same ⟨ch⟩ [tʃ]. Sources: Cintra (1971), Álvarez Pérez (2014), Mateus & d'Andrade (2000). The spec also cites a native-speaker video, *Sotaque e expressões de Trás-os-Montes* (*Portuguese With Leo*, with Rui from Chaves).

Examples: `sal` [ˈs̺aɫ], `passo` [ˈpas̺u], `paço` [ˈpasu], `casa` [ˈkaz̺ɐ], `coser` [kuˈz̺eɾ], `cozer` [kuˈzeɾ], `vinho` [ˈbiɲu], `chave` [ˈtʃabɨ]. The CLUP gold attests the betacism (`vir` as `biɾ`, `vou` as `bow`, `voltar` as `buɫˈtaɾ`) and the affricate (`chaves` as `ˈtʃaβɨʃ`). The spec gives `chaves` [ˈtʃabɨs̺].

Word-final ⟨-em⟩ is [ẽj̃] (`bem` [ˈbẽj̃]). This spec does not override `PT_NASAL_E_UNRED`, so a pretonic ⟨en⟩ is [ẽ] as in `pt-PT` (`pensar` [pẽˈsaɾ]).

The Chaves speaker keeps the mid vowel before a palatal ("vermelho eu digo vermelho, Lisboa vermalho"). The spec gives `vermelho` [bɨɾˈmɛʎu]. He also uses [ʒ] for a final /s/ before a vowel, which the spec records but does not model (see [/s/-sandhi before a vowel](#s-sandhi-before-a-vowel)).

The known gaps are those of Alto-Minhoto. A preconsonantal ⟨s⟩ stays [ʃ] (`festa` [ˈfɛʃtɐ]), and a final [s̺] stays before a vowel (`estás a ver` [eʃˈtas̺ ɐ ˈbeɾ]). Porto's diphthongisation is not applied, and the `clup_dialect` gold is small and inconsistent.

## Minhoto (pt-PT-x-minho)

`pt-PT-x-minho` models the Baixo-Minho (Braga, Guimarães, Vizela). It is in Cintra's (1971) Baixo-Minhoto-Duriense-Beirão group, inside the betacism and apico-alveolar zones. Sources: Cintra (1971, pp. 88, 92-93), Álvarez Pérez (2014, pp. 35-39), Mateus & d'Andrade (2000), Cunha & Cintra (1984), Boléo (1974).

The spec has the apical-only sibilants (see [Northern sibilant systems](#northern-sibilant-systems)). The deltas are ⟨s⟩ onset [s̺], ⟨-s-⟩ between vowels [z̺], ⟨ss⟩ [s̺], ⟨c⟩ before ⟨e i⟩ [s̺], ⟨ç⟩ [s̺] and ⟨z⟩ [z̺]. A syllable-coda ⟨s z⟩ keeps the inherited *chiado* [ʃ ʒ]. This two-sibilant system differs from the four-sibilant Transmontano and from the laminal standard.

| Word | `pt-PT` | `pt-PT-x-minho` |
|:---|:---|:---|
| `sol` (⟨s-⟩) | [ˈsɔɫ] | [ˈs̺ɔɫ] |
| `casa` (⟨-s-⟩) | [ˈkazɐ] | [ˈkaz̺ɐ] |
| `cedo` (⟨c⟩ before ⟨e⟩) | [ˈsɛdu] | [ˈs̺ɛdu] |
| `cinco` (⟨c⟩ before ⟨i⟩) | [ˈsĩku] | [ˈs̺ĩku] |
| `praça` (⟨ç⟩) | [ˈpɾasɐ] | [ˈpɾas̺ɐ] |
| `zebra` (⟨z⟩) | [ˈzɛbɾɐ] | [ˈz̺ɛbɾɐ] |
| `dez` (coda ⟨-z⟩) | [ˈdɛʃ] | [ˈdɛʃ], *chiado* inherited |
| `vaca` (⟨v⟩) | [ˈvakɐ] | [ˈbakɐ] |
| `uva` (⟨-v-⟩) | [ˈuvɐ] | [ˈuβɐ], spirant between vowels |

The same table holds for `pt-PT-x-alfena`, `pt-PT-x-aveiro` and `pt-PT-x-beira`, except that the Beira fronts the stressed /u/ (`uva` [ˈyβɐ]).

The nasal rules follow the Minho. Word-final ⟨-em⟩ is [ẽj̃] (`bem` [ˈbẽj̃], `homem` [ˈɔmẽj̃]). A pretonic ⟨en em⟩ before a consonant keeps the reduced vowel, nasal [ɨ̃]: `pensar` [pɨ̃ˈsaɾ], `entender` [ẽtɨ̃ˈdeɾ]. Leite de Vasconcellos (1900, §76, p. 238) writes: *"Este phenomeno é caracteristico da lingoagem do Alto- e Baixo-Minho"*. A word-initial ⟨en em⟩ takes the base [e] and does not reduce.

Not modelled:

- Porto's diphthongisation of the stressed close vowels is a subdivision marker of Porto and the Baixo-Minho and Douro (Cintra 1971, p. 93). It stays in `pt-PT-x-porto` and `pt-PT-x-braga`.
- Cintra (1971) and Álvarez Pérez (2014) do not describe retroflex sibilants [ʂ ʐ] or a retroflex flap [ɽ] here. The northern apical sibilant belongs to /s z/, not to /ʃ ʒ/. The spec lists [ʂ ʐ ɽ] only as allophone variants, not as default output.

## Bracarense (pt-PT-x-braga)

`pt-PT-x-braga` models the speech of the city of Braga. It is a northern variety in Cintra's Baixo-Minho and Douro-Litoral diphthongisation zone, and native speakers describe it as heavier than Porto. Sources: Cintra (1971), Segura (2013), Brissos (2018), Brissos & Rodrigues (2016), Mateus & d'Andrade (2000). Two native-speaker videos by *Portuguese With Leo* add detail: *Sotaque e expressões de Braga* (with Miguel) and "The 8 accents". They are not academic.

Betacism is the rule `BRA_BETACISM` (/v/ to [b]), with [β] as an allophone variant: `vaca` [ˈbakɐ], `vou` [ˈbow], `vacina` [bɐˈsinɐ]. Miguel says: *"pões o B em vez do V … às vezes é um B mais pronunciado, outras vezes é um B mais suave tipo Bou"*. He adds: *"no norte diz-se bácina"*. Cintra (1971, p. 87) gives the merger: *"realizado ora como oclusiva, ora como fricativa (ou espirante) b ou β"*.

A stressed mid vowel becomes a rising diphthong. Four rules apply to the stressed nucleus:

| Rule | Change | Example |
|:---|:---|:---|
| `BRA_DIPHTHONGISE_E` | [e] to [je] | `mês` [ˈmjeʃ], `ele` [ˈjelɨ] |
| `BRA_DIPHTHONGISE_O` | [o] to [wo] | `avô` [ɐˈbwo] |
| `BRA_DIPHTHONGISE_E_OPEN` | [ɛ] to [jɛ] | `café` [kɐˈfjɛ], `cedo` [ˈsjɛdu] |
| `BRA_DIPHTHONGISE_O_OPEN` | [ɔ] to [wɔ] | `avó` [ɐˈbwɔ] |

The "8 accents" video attests the close-vowel change (*"o quê"* as *"o quiê"*, *"mieu"* for *meu*). Brissos (2018, pp. 196-197, 200-201), reporting Brissos & Rodrigues (2016), shows that north-western diphthongisation also applies to the open mid vowels. So whichever mid vowel the base selects for an unmarked stressed ⟨e⟩ or ⟨o⟩, the result is a diphthong. The ⟨-er⟩ rules of `pt-PT` take the diphthong too: `comer` [kuˈmjeɾ], `mulher` [muˈʎjɛɾ]. The spec switches off the `pt-PT` suffix rules and word lists, so they cannot set the vowel first.

The falling diphthongs ⟨ou⟩ [ow] and ⟨ei⟩ [ej] stay where Lisbon has [o] and [ɐj]: `pouco` [ˈpowku], `fevereiro` [fɨbɨˈɾejɾu]. Miguel says: *"tu dizes OU, dizes vOU ou bOU"*.

Other deltas: ⟨ss⟩ is [s̺] (`passo` [ˈpas̺u], see [Northern sibilant systems](#northern-sibilant-systems)). Word-final ⟨-em⟩ is [ẽj̃] (`bem` [ˈbẽj̃]), and a pretonic ⟨en⟩ is [ɨ̃] (`pensar` [pɨ̃ˈsaɾ]), as in the Minho.

Known gaps and features not modelled:

- A stressed ⟨o⟩ at the start of the next word takes the [w] glide. The prevocalic sandhi rule then sees a glide, not a vowel, and does not fire: `os olhos` [oʃ ˈwoʎuʃ]. The same happens in Porto.
- The northern open vowels and the prosodic lengthening for emphasis (*"abres mais o A em cantÁdo"*, *"mais musical, mais cantado"*) are gradient.
- Three traits are lexical or morphosyntactic: the variable paragogic ⟨-e⟩ after the ⟨-ar⟩ infinitive (*"Faláre"*, *"gostarE"*), the nasal detail of *"beim"* for *bem*, and the forms *vós ides, vinde, ide*.

## Portuense (pt-PT-x-porto)

`pt-PT-x-porto` models Porto, Greater Porto and the Baixo-Minho and Douro-Litoral zone. Cintra calls this variety one of strong linguistic personality (*"forte personalidade linguística"*). Sources: Cintra (1971), Segura (2013), Brissos (2018), Brissos & Rodrigues (2016), Mateus & d'Andrade (2000). The spec also cites the native-speaker video *Sotaque e expressões do Porto* (*Portuguese With Leo*, with Bárbara).

Betacism is the rule `PT_PORTO_BETACISM` (/v/ to [b], no condition). Because it is an allophone rule, the merger applies to every /v/ that the inherited grapheme map produces: `vinho` [ˈbiɲu], `vaca` [ˈbakɐ], `estava` [eʃˈtabɐ]. Cintra (1971) calls it the primary trait that separates the North from the Centre-South. He writes: *"o desaparecimento da oposição fonológica entre os fonemas /v/ e /b/ e a sua fusão num fonema único /b/"*.

Cintra (1971) names diphthongisation of the stressed close vowels as the defining feature of the region. He writes: *"a ditongação, tão caracterizadora, das vogais tónicas fechadas [e] em [je], [o] em [wo] (por vezes [wɔ])"*. Segura (2013) also names diphthongisation of stressed vowels as the characteristic trait of the north-western variety. Four rules apply to the stressed nucleus:

| Rule | Change | Example |
|:---|:---|:---|
| `PT_PORTO_DIPHTHONGISE_E` | [e] to [je] | `mês` [ˈmjeʃ], `ele` [ˈjelɨ] |
| `PT_PORTO_DIPHTHONGISE_O` | [o] to [wo] | `avô` [ɐˈbwo], `pôr` [ˈpwoɾ] |
| `PT_PORTO_DIPHTHONGISE_E_OPEN` | [ɛ] to [jɛ] | `pé` [ˈpjɛ], `café` [kɐˈfjɛ] |
| `PT_PORTO_DIPHTHONGISE_O_OPEN` | [ɔ] to [wɔ] | `só` [ˈswɔ], `Porto` [ˈpwɔɾtu] |

The two open-vowel rules rest on Brissos (2018, pp. 196-197, 200-201), who reports Brissos & Rodrigues (2016, AVOC, ALEPG and ALE data). North-western diphthongisation applies to the open mid vowels too (*[ˈpi̯ɛ] pé*), so only the cardinal vowels stay stable. The rules also solve the open or close choice for an unmarked stressed ⟨e⟩ or ⟨o⟩, because both values become a diphthong. The emblematic `Porto` gives [ˈpwɔɾtu], near the attested close [ˈpu̯oɾtu].

`PT_ER_CLOSE` is overridden to give the diphthong [je] for the ⟨-er⟩ infinitive: `comer` [kuˈmjeɾ]. Leite de Vasconcellos (1901, §44-b, p. 90) writes: *"l'ê oral ou nasalisé, et l'ê (em, en) initial ou médial deviennent iê dans le Baixo-Minho"*. The spec switches off the `pt-PT` suffix rules and word lists, so its own rules reach the stressed vowel first.

Northern EP keeps the falling diphthongs where Lisbon changes them (Cintra's feature 4). The grapheme deltas are ⟨ou⟩ [ow] and ⟨ei⟩ [ej]: `ouro` [ˈowɾu], `leite` [ˈlejtɨ], `primeiro` [pɾiˈmejɾu].

Cintra (1971, pp. 11-13 of the Instituto Camões reprint) draws the main North/South isogloss on the sibilant of ⟨s⟩ and ⟨ss⟩. He puts the Baixo-Minho and the Douro Litoral north of the southern limit of the apical sibilant. The spec declares ⟨ss⟩ as [s̺] (`passo` [ˈpas̺u]). It lists [ʂ ʐ] only as allophone variants of /ʃ ʒ/. Word-final ⟨-em⟩ is [ẽj̃] (`bem` [ˈbẽj̃]).

The rest is inherited from `pt-PT`. That includes the dark coda /l/ (`alto` [ˈɐɫtu]) and the coda *chiado* (`véspera` [ˈbjɛʃpɨɾɐ]). It also includes the standard [z] of the prevocalic sandhi (`estás a ver` [eʃˈtaz ɐ ˈbjeɾ]).

Known gaps and features not modelled:

- The apical sibilant reaches ⟨ss⟩ only. Carrying it to ⟨s⟩, ⟨ç⟩, ⟨c⟩ and ⟨z⟩ is an open limit.
- The rule notes record two subtypes that the spec does not model: the toward-central diphthong [ɛɐ̯] and [ɔɐ̯], and the marginal /i/ to [ei̯].
- A stressed ⟨o⟩ at the start of the next word takes the [w] glide, so the prevocalic sandhi does not fire: `os olhos` [oʃ ˈwoʎuʃ].
- Sporadic palatalisation of /l/ (`quilo` as *quilho*, `Filipa` as [fʎipɐ]) is lexical.
- The `ep_dialects` gold for the North marks betacism and diphthong preservation, but not the diphthongisation. So that gold cannot reward the diphthongisation rules. They ship on their published sources.

## Alfena (pt-PT-x-alfena)

`pt-PT-x-alfena` models Alfena and Valongo in Greater Porto, in Cintra's Duriense zone of the Douro Litoral. The spec name is "Alfena Portuguese (vowel-breaking)", and its location is the single locality for which the vowel-breaking variety is described. Sources: Cintra (1971, pp. 88, 92-93), Álvarez Pérez (2014, pp. 35-39), Mateus & d'Andrade (2000), Cunha & Cintra (1984), Boléo (1974).

The spec has the apical-only sibilants and the grapheme betacism of the [Minhoto](#minhoto-pt-pt-x-minho) table: `sol` [ˈs̺ɔɫ], `cedo` [ˈs̺ɛdu], `zebra` [ˈz̺ɛbɾɐ], `vaca` [ˈbakɐ], `uva` [ˈuβɐ]. Word-final ⟨-em⟩ is [ẽj̃] (`bem` [ˈbẽj̃]). The rule note cites Leite de Vasconcellos (1901, §44n) and Viana & Rocha (2006) for the northern close-mid nucleus. A pretonic ⟨en⟩ is [ẽ] as in `pt-PT` (`pensar` [pẽˈsaɾ]).

The local vowel breaking (*Brechung*) of stressed mid vowels comes from regional dialect literature, not from Cintra or Álvarez Pérez. The spec lists it only as allophone variants ([e͜ɐ], [ɛ͜ɐ], [o͜ɐ], [ɔ͜ɐ]), not as default output. It also lists [χ] as a variant of /ʁ/. Porto's diphthongisation is not applied, and the spec has no retroflex sibilants (see the [Minhoto](#minhoto-pt-pt-x-minho) section).

## Beira Litoral (pt-PT-x-aveiro)

`pt-PT-x-aveiro` models Aveiro, Vagos and the Beira Litoral coast, in Cintra's Baixo-Minhoto-Duriense-Beirão group. Álvarez Pérez (2014, pp. 35-37) shows the /b/ and /v/ merger along the coast north of Coimbra, which is the Aveiro coast. Sources: Cintra (1971, pp. 88, 92-93), Álvarez Pérez (2014, pp. 35-39), Mateus & d'Andrade (2000), Cunha & Cintra (1984), Boléo (1974).

The spec has the apical-only sibilants and the grapheme betacism of the [Minhoto](#minhoto-pt-pt-x-minho) table: `casa` [ˈkaz̺ɐ], `praça` [ˈpɾas̺ɐ], `vaca` [ˈbakɐ]. Word-final ⟨-em⟩ keeps the `pt-PT` value [ɐ̃j̃] (`bem` [ˈbɐ̃j̃]).

Regional dialect literature reports a local retroflex lateral [ɭ] for /l/. Cintra and Álvarez Pérez do not, so the spec lists [ɭ] only as an allophone variant. Porto's diphthongisation is not applied.

## Beira (pt-PT-x-beira)

`pt-PT-x-beira` models the Beiras: Beira Litoral (Coimbra, Aveiro), Beira Alta (Viseu, Guarda) and Beira Baixa (Castelo Branco). The apical sibilant of this zone is the *s beirão* itself. Cintra (1971, p. 88) notes that the most palatal apical variant is *"vulgarmente conhecida pelo nome de s beirão"*.

Álvarez Pérez (2014) puts the clearest apical core in the districts of Viseu, Guarda and Castelo Branco. He also shows the /b/ and /v/ merger through the eastern Guarda and Castelo Branco districts, which Cintra's map left out. Sources: Cintra (1971, p. 14 of the CVC reprint, pp. 88, 92-93), Álvarez Pérez (2014, pp. 35-39), Brissos (2014), Brissos (2014b), Brissos & Saramago (2014), Leite de Vasconcellos (1901), Mateus & d'Andrade (2000), Cunha & Cintra (1984).

The spec has the apical-only sibilants and the grapheme betacism of the [Minhoto](#minhoto-pt-pt-x-minho) table. It lists the conservative alveolar trill [r] as a variant of /ʁ/.

The Beira Baixa fronts the stressed /u/ to [y], through the rules `BEI_U_NO_FRONT_AFTER_BILABIAL` and `BEI_U_FRONTING` (see [Stressed /u/ fronting](#stressed-u-fronting)). Cintra (1971, p. 14 of the CVC reprint) uses this isogloss to bound the Beira-Baixa and Alto-Alentejo zone, *"uma região que tem como principais núcleos urbanos Castelo-Branco e Portalegre"*:

> *"Como isófona que possa marcar o limite da zona, parece-me preferível escolher, a da palatalização, em maior ou menor grau, da vogal tónica u"*

He places it inside *"uma profunda alteração de timbre de todo o sistema vocálico, principalmente do tónico"*. At the edges of the zone the trait that stays most audible is this change: *"o traço que permanece mais perceptível é a alteração do timbre do u"*. Cintra writes the front rounded value [y] in the neighbouring Barlavento Algarvio passage of the same chain reaction (*"a palatalização da lábio-velar [u] em [y]"*). Brissos (2014) documents it acoustically for the Centre-South ([tˈyd] *tudo*, [lˈymɨ] *lume*).

| Word | `pt-PT` | `pt-PT-x-beira` |
|:---|:---|:---|
| `tudo` | [ˈtudu] | [ˈtydu] |
| `lume` | [ˈlumɨ] | [ˈlymɨ] |
| `número` | [ˈnumɨɾu] | [ˈnymɨɾu] |
| `sul` (before a coda /l/) | [ˈsuɫ] | [ˈs̺yɫ] |
| `mudo` (after a bilabial) | [ˈmudu] | [ˈmudu] |
| `turistas` (pretonic /u/) | [tuˈɾiʃtɐʃ] | [tuˈɾiʃtɐʃ] |
| `do` (clitic) | [du] | [du] |

The mainland change is a chain shift of the whole stressed vowel system. So it fronts the vowel even before a coda liquid (`sul` [ˈs̺yɫ]). The spec does not carry the island guard `ACO_U_KEEP_BEFORE_CODA`, which rests on Rogers (1948) for São Miguel and has no mainland source. The proclitic guard in `word_exceptions` pins `o` [o], `os` [oʃ], `no` [nu], `nos` [nɔʃ], `do` [du], `dos` [dɔʃ], `ao` [ɐu], `aos` [ɐɔʃ], `pelo` [pɛlu], `pelos` [pɛluʃ], `um` [ˈum] and `uns` [ˈunʃ].

Known gaps:

- The /u/ fronting belongs to the Beira Baixa (Castelo Branco). The Beira Litoral and the Beira Alta are in the Baixo-Minhoto-Duriense-Beirão group and do not front the stressed /u/. This general node models the strongest realisation, as `pt-PT-x-acores` does for the islands. The sibling specs `pt-PT-x-minho`, `pt-PT-x-alfena` and `pt-PT-x-aveiro` do not carry the rule.
- The clitic guard writes `um` and `uns` with an oral vowel ([ˈum], [ˈunʃ]), where `pt-PT` gives the nasal [ˈũ].
- Porto's diphthongisation is not applied, and the spec has no retroflex sibilants (see the [Minhoto](#minhoto-pt-pt-x-minho) section).

## Conimbricense (pt-PT-x-coimbra)

`pt-PT-x-coimbra` models Coimbra, the central variety often called *"o sotaque mais neutro de Portugal"*. Its defining property is that it keeps the base values where Lisbon changes them. Sources: the native-speaker video *Coimbra tem sotaque?* (*Portuguese With Leo*, with Lúcio, not academic), Cintra (1971), Mateus & d'Andrade (2000).

The one delta is [ʒ] for a final /s/ before a vowel. The spec declares `PT_FINAL_S_PREVOCALIC_VOICE` again with the transform `ʒ`, where `pt-PT` has [z]:

| Phrase | `pt-PT` | `pt-PT-x-coimbra` |
|:---|:---|:---|
| `os olhos` | [oz ˈoʎuʃ] | [oʒ ˈoʎuʃ] |
| `estás a ver` | [eʃˈtaz ɐ ˈveɾ] | [eʃˈtaʒ ɐ ˈveɾ] |

The centre varies between [z] and [ʒ]. Lúcio (*conimbricense de gema*) is asked how he links "os olhos". He says: *"Nós faríamos a junção com o som de J"*, while the Lisbon host uses [z].

Lúcio also says *"esta é uma coisa que varia muito"*. The spec models the marked local [ʒ] pole. The standard and Lisbon literature gives [z] (Mateus & d'Andrade 2000, ch. 2). No page-pinned academic source for the Coimbra [ʒ] was found.

Coimbra differs from Lisbon by the absence of the Lisbon changes. The spec inherits these values from `pt-PT`:

| Feature | `pt-PT-x-coimbra` | `pt-PT-x-lisbon` |
|:---|:---|:---|
| stressed ⟨e⟩ before a palatal | `coelho` [kuˈɛʎu], mid vowel ("coêlho") | `coelho` [kuˈɐʎu] ("coâlho") |
| ⟨ei⟩ | `fevereiro` [fɨvɨˈɾejɾu] | `fevereiro` [fɨvɨˈɾɐjɾu] |
| ⟨ou⟩ | `pouco` [ˈpoku] | `pouco` [ˈpoku] |
| unstressed /i/ | `Filipa` [fiˈlipɐ] | `Filipa` [fiˈlipɐ]<br>speakers say "Flipa", which the spec does not model |

Lúcio calls the mid vowel before a palatal (`coelho`, `espelho`, `vermelho`, *Fonte da Telha*) *"das coisas que mais distinguem o sotaque de Coimbra do sotaque de Lisboa"*. He says that Coimbra *"fala da forma que teoricamente é o correto"*. He describes the Coimbra [ej] as between the Lisbon [ɐj] (*"menos A"*) and the strong Porto [ej] (*"não tanto E"*). The Trás-os-Montes speaker confirms the mid vowel for the neighbouring North ("vermelho eu digo vermelho, Lisboa vermalho").

Coimbra prefers *toiro, loiça, loiro*, where Lisbon prefers *touro, louça*. These doublets are a choice of spelling, not a grapheme rule. They are left to the lexicon.

## Lisbon (pt-PT-x-lisbon)

`pt-PT-x-lisbon` models Lisbon and the surrounding Estremenho (Centro-Litoral) zone as an urban variety with its own phonological changes. It is a delta over the broad descriptive standard `pt-PT`. Sources: Hristovsky (2008), Mateus & d'Andrade (2000, p. 19), Cruz-Ferreira (1995), Cintra (1971), Segura (2013), Cunha & Cintra (1984).

The status of Lisbon against the standard is contested. Cintra (1971) argues that the prestige standard of European Portuguese broadly matches the Central-Southern (Estremenho and Lisbon) type. The conservative teaching norm, however, often rests on central (Coimbra) speech, which lacks several of the Lisbon changes. So the spec does not treat Lisbon as identical to that norm.

The spec inherits from `pt-PT` the dark coda /l/ (`PT_CODA_L_DARK`) and the coda *chiado* (`PT_CODA_S_HUSH`, `PT_CODA_Z_HUSH`) with the coda /s/ voicing. It also inherits the standard [z] of the prevocalic sandhi (`estás a ver` [eʃˈtaz ɐ ˈveɾ]). The southern and island [ʒ] is not a Lisbon feature. Unstressed /e/ reduces to [ɨ] through the inherited positional map.

| Feature | Value | Example | Source |
|:---|:---|:---|:---|
| stressed ⟨e⟩ before a palatal | /e ɛ/ to [ɐ] before [ʎ ɲ ʃ ʒ] | `coelho` [kuˈɐʎu], `fecho` [ˈfɐʃu], `venho` [ˈvɐɲu], `espelho` [eʃˈpɐʎu], `abelha` [ɐˈbɐʎɐ] | Hristovsky 2008, p. 239<br>Mateus & d'Andrade 2000, p. 19 |
| ⟨ei⟩ lowered and centralised | ⟨ei⟩ to [ɐj] | `leite` [ˈlɐjtɨ], `primeiro` [pɾiˈmɐjɾu], `reino` [ˈʁɐjnu], `seis` [ˈsɐjʃ] | Cintra 1971<br>Segura 2013<br>Mateus & d'Andrade 2000 |
| ⟨ou⟩ monophthong | ⟨ou⟩ to [o] | `ouro` [ˈoɾu] | Segura 2013<br>Cintra 1971 |
| rhotic | allophones of /ʁ/ limited to the uvular fricative [ʁ] | `carro` [ˈkaʁu] | Mateus & d'Andrade 2000 |

The most typical Lisbon feature is the centralisation of the stressed front mid vowel to [ɐ] before a palatal consonant. The palatals come from ⟨lh⟩ [ʎ], ⟨nh⟩ [ɲ], ⟨ch x⟩ [ʃ] and ⟨j g⟩ before ⟨e i⟩ [ʒ]. Hristovsky (2008, p. 239) surveys the literature: Gonçalves Viana (1883), Cintra (1971), Barbosa (1965), Andrade (1981), and Barros (1994) for the distribution in Lisbon speech. These authors agree that /e/ and /ɛ/ become [ɐ] before a palatal, as a dissimilation.

Mateus & d'Andrade (2000, p. 19) list three contexts for stressed [ɐ]: before a palatal consonant (`telha` [ˈtɐʎɐ]), before the palatal glide, and before a nasal. They treat it as a derived vowel. Cruz-Ferreira (1995, p. 92) notes that all vowels are raised and advanced before palato-alveolar and palatal consonants.

The conservative central norm, which `pt-PT` follows, keeps [e] and [ɛ] here. So the change is a Lisbon delta. The rule `LX_STRESSED_E_PREPALATAL` (`followed_by: "palatal"`) runs after positional reduction. An unstressed /e/ is already [ɨ] at that stage, so the rule fires only on the stressed or word-initial vowel.

Hristovsky (2008, p. 239) reports the change in stressed and unstressed position. The unstressed case is variable and graded by social factors (Barros 1994). In a broad transcription an unstressed pre-palatal /e/ reduces to [ɨ]: `melhor` [mɨˈʎɔɾ], `fechar` [fɨˈʃaɾ], `mexer` [mɨˈʃeɾ]. That is the value of the base and of the gold data, so the spec models only the stressed case.

The ⟨ei⟩ [ɐj] is the diagnostic grapheme-level Estremenho feature. Conservative and northern EP keep [ej] (see `pt-PT-x-porto`). Cintra (1971) and Segura (2013) treat [ɐj] as typical of the Centro-Litoral and Estremenho zone. The isophone of ⟨ei⟩ is one of Cintra's boundary lines near the Tejo.

The spec declares its own positional maps for ⟨a⟩ and ⟨o⟩. They keep the unstressed reduction ([ɐ] and [u]) without the base defaults for the stressed nucleus, which spelling cannot predict.

Known gaps and features not modelled:

- The own ⟨a⟩ and ⟨o⟩ maps replace the whole `pt-PT` maps for those graphemes. A stressed ⟨o⟩ then takes the close [o] of the grapheme table, and a stressed ⟨a⟩ before a nasal stays [a]. So `bola` gives [ˈbolɐ] and `anos` gives [ˈanuʃ], where `pt-PT` gives [ˈbɔlɐ] and [ˈɐnuʃ].
- Spirantisation of the voiced stops between vowels is a general EP process, not a Lisbon one. Every available `pt` gold is broad and writes the stops (see [pt-PT](pt-PT.md#not-modelled)).
- The place of the sibilant (apico-alveolar or predorsodental), Cintra's primary North/South isogloss, is not encoded. Lisbon uses the predorsodental value that the base produces.
- The `ep_dialects` and `clup_dialect` gold sets for Lisbon are small and unvalidated. They are not consistent in the pre-palatal context (they write `venho` with a plain front vowel), so they cannot reward the pre-palatal rule. The rule ships on the documented phonology.

## Alentejano (pt-PT-x-alentejo)

`pt-PT-x-alentejo` models the central-southern dialect of the Alto Alentejo (Portalegre, Évora, Beja). Sources: Cintra (1971), Brissos (2014), Brissos (2014b), Brissos & Saramago (2014), Mateus & d'Andrade (2000), Cunha & Cintra (1984), Boléo (1974).

The defining feature is the fronting of the stressed /u/ to [y], through `ALE_U_NO_FRONT_AFTER_BILABIAL` and `ALE_U_FRONTING` (see [Stressed /u/ fronting](#stressed-u-fronting)). Cintra (1971, p. 14 of the CVC reprint) bounds the Beira-Baixa and Alto-Alentejo zone by this isogloss. It is part of a timbre shift of the whole vowel system: *"a palatalização, em maior ou menor grau, da vogal tónica u"*. He writes the IPA value [y] for the neighbouring Barlavento Algarvio of the same chain reaction (*"a palatalização da lábio-velar [u] em [y]"*). In his note 56 he writes the Alto-Alentejo stressed *u* as a palatal "ü".

The fronting applies to the stressed nucleus only: `sul` [ˈsyɫ], `lume` [ˈlym]. An unstressed /u/ stays [u] (`turistas` [tuˈɾiʃtɐʃ]), and the bilabial guard keeps `bula` [ˈbulɐ]. The proclitic guard pins `o` [u], `os` [uʃ], `no` [nu], `nos` [nuʃ], `do` [du], `dos` [duʃ], `ao` [aw], `aos` [awʃ], `pelo` [pɛlu], `pelos` [pɛluʃ], `um` [ˈũ] and `uns` [ˈũʃ].

The region also deletes final unstressed high vowels. The rule `ALE_FINAL_HIGH_VOWEL_DELETION` deletes /u i ɨ/ when the vowel is word-final and unstressed: `gosto` [ˈɡɔʃt], `noite` [ˈnojt], `tudo` [ˈty]. It never touches a stressed final vowel (`café` [kɐˈfɛ]) or a vowel inside the word. Final [ɐ] from ⟨a⟩ stays (`calma` [ˈkaɫmɐ]), because the sources list only final -u, -i and -e.

The primary source for the deletion is Brissos (2014), an acoustic study of central-southern EP. He writes: *"Final unstressed [u] disappears or is reduced to [ɨ]"*, for example [sˈœʃt] *cesto*. Cintra (1971) mentions it only in note 58 (p. 27), where he summarises Lüdtke (1956/57). The note reads: *"a queda das vogais finais -u, -i (ou -e), outro dos fenómenos mais típicos desta região, mas cujos limites não coincidem perfeitamente com os dos primeiros"*. He states that its isoglosses do not match the defining feature of the zone, so it is not one of Cintra's own diagnostics.

| Process | Field | Example |
|:---|:---|:---|
| ⟨-d-⟩ deleted between vowels | `positional_graphemes` | `nada` [ˈnaɐ], `vida` [ˈviɐ] |
| ⟨ei⟩ to [e] | `graphemes` | `leite` [ˈlet] |
| ⟨ou⟩ to [o] | `graphemes` | `outro` [ˈotɾ] |
| ⟨meu⟩ to [me] | `graphemes` | `meu` [ˈme] |
| dark coda /l/ | inherited `allophone_rules` | `sol` [ˈsɔɫ] |
| coda /s/ to [ʃ] | inherited `allophone_rules` | `gosto` [ˈɡɔʃt] |

The examples `leite` and `outro` also show the final-vowel deletion. The spec lists [ɛ͡ɐ] as a variant of /ɛ/.

The `ep_dialects` gold for this spec is a light, near-standard reading. It writes final vowels in full and does not show the /u/ fronting or the final-vowel deletion. So both rules lower the agreement with that small, unvalidated set, while they are the cited realisations. The same holds for the inherited dark /l/ and the deleted /d/, where the gold writes a clear [l] and a kept [d]. The rules stay, because the difference is a limit of the gold.

## Algarvio (pt-PT-x-algarve)

`pt-PT-x-algarve` models the southernmost mainland dialect (Faro, Portimão, Lagos, Sagres). Sources: Cintra (1971), Brissos (2014), Brissos (2014b), Brissos & Saramago (2014), Segura da Cruz (1989), Mateus & d'Andrade (2000), Cunha & Cintra (1984), Boléo (1974). The spec also cites the native-speaker video "The 8 accents" (*Portuguese With Leo*).

The most diagnostic feature is the fronting of the stressed /u/ to the front rounded [y] (as in French *tu*, German *über*). It is the isogloss by which Cintra (1971) bounds the Barlavento Algarvio: *"a palatalização, em maior ou menor grau, da vogal tónica u"*. Brissos (2014) gives the acoustic forms [tˈyd] *tudo* and [lˈymɨ] *lume*.

Segura da Cruz (1989) gives a whole study to it, "La palatalisation de [u] dans le «Barlavento Algarvio»". Lüdtke (1957) and Maia (1975-78), through Cintra (1971) and Brissos (2014), note that it does not reach an unstressed /u/. Brissos & Saramago (2014, pp. 55-59, 65) confirm the isogloss from perceptual dialectology.

The rules are `ALG_U_NO_FRONT_AFTER_BILABIAL` and `ALG_U_FRONTING` (see [Stressed /u/ fronting](#stressed-u-fronting)): `tudo` [ˈtydu], `lume` [ˈlymɨ], `sul` [ˈsyɫ], `tu` [ˈty], and `mudo` [ˈmudu] after a bilabial. An unstressed /u/ stays: `turistas` [tuˈɾiʃtɐʒ].

The proclitic guard gives these values:

| Word | Form | Word | Form | Word | Form |
|:---|:---|:---|:---|:---|:---|
| `o` | [u] | `no` | [nu] | `do` | [du] |
| `os` | [uʒ] | `nos` | [nuʒ] | `dos` | [duʒ] |
| `ao` | [aw] | `aos` | [awʒ] | `um` | [ˈũ] |
| `pelo` | [pɛlu] | `pelos` | [pɛluʒ] | `uns` | [ˈũʒ] |

So `no mar` gives [nu ˈmaɾ].

| Process | Field | Example |
|:---|:---|:---|
| ⟨ei⟩ to [e] | `graphemes` | `leite` [ˈletɨ] |
| ⟨ou⟩ to [o] | `graphemes` | `outro` [ˈotɾu] |
| word-final ⟨s⟩ to [ʒ] | `positional_graphemes` | `mas` [ˈmaʒ], `estás` [eʃˈtaʒ], `muitos amigos` [ˈmujtoʒ ɐˈmiɡoʒ] |
| unstressed ⟨e o⟩ kept as [e o] | `positional_graphemes` | `pedir` [peˈdiɾ], `telefone` [teleˈfɔnɨ] |
| word-final ⟨-em⟩ to [ẽj̃] | `PT_FINAL_EM_*` switched off | `bem` [ˈbẽj̃], `homens` [ˈɔmẽʒ] |
| dark coda /l/ | inherited `allophone_rules` | `sol` [ˈsɔɫ] |
| coda /s/ to [ʃ] before a consonant | inherited `allophone_rules` | `gosto` [ˈɡɔʃtu] |
| open stressed vowels [ɛ ɔ] | `positional_graphemes` | `forte` [ˈfɔɾtɨ] |

The Algarve has the strongest form of the southern [ʒ] for a final /s/ (see [/s/-sandhi before a vowel](#s-sandhi-before-a-vowel)). The value holds in every word-final position, so the positional map gives it and no separate sandhi rule is needed. For word-final ⟨-em⟩, Leite de Vasconcellos (1901, §44n, p. 93) writes: *"Dans le Baixo-Alemtejo et dans l'Algarve, on dit -ẽi en syllabe découverte, et -ẽ en syllabe couverte"*. He also heard [ẽ] in open final syllables at Lagos, a local variant that the spec does not model.

Known gaps and features not modelled:

- The spec notes give no source for the unstressed [e] and [o].
- Brissos (2014) documents a wider central-southern chain shift: a stressed [a] to [ɛ] in high-vowel and palatal contexts, and [ɔ] to [o̝]. These changes depend on context and are only variably categorical. Modelling them next to the /u/ fronting risks a collapse of the vowel space, so only /u/ to [y] is encoded.
- Older and rural speakers have an apico-alveolar [s̺]. It is an articulatory distinction with no phonemic contrast here, and Cintra (1971) marks this class of feature as not simulable at the phoneme level.
- The Algarve has no betacism: /v/ and /b/ stay apart.
- The `ep_dialects` gold is a light, near-standard reading that never uses [y], so it does not reward the fronting.

## Madeiran (pt-PT-x-madeira)

`pt-PT-x-madeira` models Madeira, with Funchal and Ribeira Brava as the reference. Sources: Segura (2013), Mateus & d'Andrade (2000), and the native-speaker video *Sotaque e expressões da Madeira* (*Portuguese With Leo*, with João Francisco Cunha).

The best-known Madeiran feature is the palatalisation of /l/ to [ʎ] after /i/. Segura (2013) describes it as *"a palatalização de [l] em contexto de [i]"*. The rule `MAD_L_PALATALISATION` changes /l/ to [ʎ] when /i/ comes before it and a vowel comes after it. So the rule applies to an onset /l/ between /i/ and another vowel:

| Word | `pt-PT` | `pt-PT-x-madeira` |
|:---|:---|:---|
| `quilo` | [ˈkilu] | [ˈkiʎu] |
| `mochila` | [muˈʃilɐ] | [muˈʃiʎɐ] |
| `vila` | [ˈvilɐ] | [ˈviʎɐ] |

The condition is exact. An /l/ after any other front vowel does not change (`teleférico` [tɨlɨˈfɛɾiku], /l/ after a reduced [ɨ]). An onset /l/ without /i/ before it stays clear (`levada` [lɨˈvadɐ]).

The plural nasal endings ⟨-ões -ães -ãos⟩ have a nasal vowel plus [n], not a nasal glide. The grapheme overrides are ⟨ões⟩ [õns] and ⟨ães ãos⟩ [ɐ̃ns]: `cães` [ˈkɐ̃ns].

Madeiran keeps /v/ and /b/ apart, as the standard does: `visitar` [viziˈtaɾ], `levada` [lɨˈvadɐ], `novo` [ˈnɔvu]. The one gold item `vinho` as [ˈbiɲu] is lexical, not a productive merger, so it is not modelled. The dark coda /l/ (`mel` [ˈmɛɫ]), the *chiado*, the vowel reduction and the coda /s/ sandhi are inherited.

Known gaps:

- The gold shows a singular ⟨-ão⟩ as [õns] in some words (`verão`). The frequent monosyllable `são` keeps [sɐ̃w̃], so the spec encodes only the plural pattern: `verão` [vɨˈɾɐ̃w̃], `são` [ˈsɐ̃w̃].
- Sources report the diphthongisation of a stressed /i/ to [ɐj]. The gold keeps [i] (`dia`, `ilha`), so the spec leaves it out: `dia` [ˈdiɐ], `ilha` [ˈiʎɐ].
- Sporadic lexical items (`correr` as [kuˈʁweɾ], `Filipa` as [ˈfʎipɐ]) and narrow detail (stop aspiration, final devoicing) are outside the rules. The rule gives `Filipa` [fiˈʎipɐ].
- The "8 accents" video gives Madeira the centralised "coâlho" for `coelho`. The spec does not model it: `coelho` [kuˈɛʎu].

## Azorean (pt-PT-x-acores)

`pt-PT-x-acores` is the general node for the Azores. The archipelago has nine islands with large differences between them. The spec models the strongest realisation of the /u/ fronting, that of the São Miguel class, and documents the limit between islands. The `ep_dialects` and `clup_dialect` gold sets for this code are of the Terceira type. Sources: Rogers (1948), Mateus & d'Andrade (2000), and the native-speaker video "The 8 accents" (*Portuguese With Leo*).

The most typical Azorean feature is the fronting of a stressed /u/ to [y]. Rogers (1948) documents it in the eastern islands (São Miguel), and `tu` [ˈty] is its shibboleth. Two rules apply in order (see [Stressed /u/ fronting](#stressed-u-fronting)):

| Rule | Change | Example |
|:---|:---|:---|
| `ACO_U_KEEP_BEFORE_CODA` | /u/ stays [u] before a coda liquid or sibilant | `azul` [ɐˈzuɫ], `Furnas` [ˈfuɾnɐʃ] |
| `ACO_STRESSED_U_FRONTING` | stressed /u/ to [y] before an onset consonant | `número` [ˈnymɨɾu], `muda` [ˈmydɐ] |

The guard is an identity rewrite (u to u). Its only job is to match first, so the fronting cannot apply in a closed syllable. The word-final `tu` is pinned in `word_exceptions` as [ˈty], because a word-boundary condition would also match a sentence-final unstressed /u/. An unstressed /u/ never fronts: `cozido` [kuˈzidu] (pretonic), `rápido` [ˈʁapidu] (final), `vulcão` [vuɫˈkɐ̃w̃].

The fronting rule needs a following onset consonant, which a bare `o`, `do`, `no` or `ao` never has. The spec also pins every clitic in `word_exceptions`: `o` [u], `os` [uʃ], `no` [nu], `nos` [nuʃ], `do` [du], `dos` [duʃ], `ao` [aw], `aos` [awʃ], `pelo` [ˈpelu], `pelos` [ˈpeluʃ], `um` [ˈũ], `uns` [ˈũʃ]. The article `o` is [u], never [y].

The ⟨ou⟩ digraph keeps the falling diphthong [ow] where Lisbon has [o]: `touradas` [towˈɾadɐʃ].

A final /s/ before a vowel is [ʒ], as in the Algarve but only in that position (see [/s/-sandhi before a vowel](#s-sandhi-before-a-vowel)). The spec declares `PT_FINAL_S_PREVOCALIC_VOICE` again with the transform `ʒ`: `estás a ver` [eʃˈtaʒ ɐ ˈveɾ], `estás` [eʃˈtaʃ], `estás só` [eʃˈtaʃ ˈsɔ], `estás bem` [eʃˈtaʒ ˈbɐ̃j̃]. The "8 accents" video reports the shared J of the Algarve and the Azores ("quijentrar", "Todojos", "Éjunúmerúm" for *és o número um*). The feature sits inside the documented island behaviour of the final sibilant (Rogers 1948), but no page-pinned academic source for this value was found.

The dark coda /l/ (`sol` [ˈsɔɫ]), the *chiado*, the vowel reduction and the coda /s/ voicing before a consonant are inherited.

Known gaps:

- The fronting is categorical only in the São Miguel class. Terceira fronts only in some words, so `muda` gives [ˈmydɐ] here against [ˈmudɐ] in the Terceira gold. The spec [`pt-PT-x-terceira`](#terceirense-pt-pt-x-terceira) models that island.
- The nasal diphthong to nasal plus N (⟨-ões⟩ [õns], ⟨-ães⟩ [ɐ̃ns]) is a Madeiran feature. The Terceira gold keeps the standard diphthongs, so the spec inherits them from `pt-PT`.
- Sporadic and lexical items, such as an extreme raising of e to i, `boi` as [bô] and `pastar` as [pɐʃˈtâ], are left to downstream engines.

## Micaelense (pt-PT-x-sao-miguel)

`pt-PT-x-sao-miguel` models São Miguel, the eastern Azorean *micaelense* variety. It is the most stereotyped Azorean accent. The spec is a delta over `pt-PT`, not over `pt-PT-x-acores`, so it does not inherit the ⟨ou⟩ [ow] of the general node. Sources: Rogers (1948), Silva (2008), Segura (2013), Mateus & d'Andrade (2000). Two native-speaker videos by *Portuguese With Leo* add detail: *Sotaque e expressões dos Açores, São Miguel* (with Catarina) and "The 8 accents".

The rule `SM_U_FRONTING` fronts every stressed /u/ to [y]. This trait makes the accent "sound French". Catarina says: *"o u faz com que pareça realmente um sotaque assim muito francês … é a nossa característica, é o û"*. Silva (2008, p. 4) gives the fronting before a coda too, `azul` [ɐˈzyl] and `cruz` [kryʃ], next to the open-syllable `uva` [ˈyvɐ] and `fruta` [ˈfrytɐ]. So the spec has no guard before a coda, unlike `pt-PT-x-acores`.

| Word | `pt-PT` | `pt-PT-x-sao-miguel` |
|:---|:---|:---|
| `número` | [ˈnumɨɾu] | [ˈnymɨɾu] |
| `tu` | [ˈtu] | [ˈty] |
| `azul` (before a coda) | [ɐˈzuɫ] | [ɐˈzyɫ] |
| `fruta` | [ˈfɾutɐ] | [ˈfɾytɐ] |
| `muda` | [ˈmudɐ] | [ˈmydɐ] |

The rule applies to the stressed nucleus only. The clitics are pinned in `word_exceptions` (`o` [u], `os` [uʒ], `do` [du], `no` [nu], `ao` [aw], `pelo` [ˈpelu], `um` [ˈũ], `tu` [ˈty]), so a clitic `o`, `do`, `no` or `ao` is [u], never [y].

The diphthongs ⟨oi ói ou⟩ become the front rounded [ø] (Silva 2008, p. 4): `oito` [ˈøtu], `noite` [ˈnøtɨ], `pouco` [ˈpøku].

The rule `SM_L_PALATALISATION` changes an /l/ after /i/ and before a vowel to [ʎ], in the same context as [Madeiran](#madeiran-pt-pt-x-madeira): `quilo` [ˈkiʎu], `Filipa` [fiˈʎipɐ], `mochila` [muˈʃiʎɐ]. The condition is exact, so an /l/ after another front vowel does not change (`teleférico` [tɨlɨˈfɛɾiku]). This feature comes from the "8 accents" overview, which groups São Miguel with Madeira (*Filipa* as "Flhipa"). The São Miguel video itself does not show it. The Madeira video supports it (*quilómetro* as "quilhómetro"), and Segura (2013) gives it for the Atlantic islands.

A final /s/ before a vowel is [ʒ], shared with the Algarve: `estás a ver` [eʃˈtaʒ ɐ ˈveɾ], `os olhos` [uʒ ˈoʎuʃ]. The spec declares `PT_FINAL_S_PREVOCALIC_VOICE` again with the transform `ʒ`. The "8 accents" overview gives the shared Algarve and Azores J (*"quijentrar"*, *"Todojos"*, *"Éjunúmerúm"*).

São Miguel keeps the mid vowel before a palatal ("coêlho"), which the spec inherits: `coelho` [kuˈɛʎu]. Lisbon centralises it to [ɐ] ("coâlho", `pt-PT-x-lisbon` [kuˈɐʎu]), and Madeira has "coâlho" too. The São Miguel "coêlho" against the Madeiran "coâlho" is the classic contrast between the islands (8 accents overview).

Not modelled:

- The very closed [o] and [u] vowels are gradient.
- The variable singular ⟨ão⟩ as the monophthong [ɐ̃] (`cão` as *"cã"*, `ladrão` as *"ladrã"*, *"às vezes"*). A blanket rule would also change `são` [ˈsɐ̃w̃].
- Word-final ⟨-r⟩ deletion in verbs (`comer` as *"comê"*, `passear` as *"passeá"*). Spelling cannot limit it to infinitives without also dropping the /r/ of `mar` and `cor`.
- The spec notes leave out the final-vowel deletion (`oito` as [øt]) and the stressed-vowel chain shift (`sete` as [sæt], `avó` as [ɐˈvo], `avô` as [ɐˈvu]). They also leave out the [ø] from ⟨o⟩ before [ʒ] (`hoje` as [øʒ]).
- *"non"* for *não*, the heavy use of the gerund and the Anglo-Azorean *calafão* loan words are lexical or morphosyntactic.

## Terceirense (pt-PT-x-terceira)

`pt-PT-x-terceira` models Terceira (Angra do Heroísmo, Praia da Vitória). It is the best-described island of the central group of the Azores, which also holds Graciosa, São Jorge, Pico and Faial. It is a delta over `pt-PT`, not over `pt-PT-x-acores`, because the general node carries the /u/ fronting that Terceira lacks. Sources: Mikołajczak (2014), Segura & Saramago (2001), Leite de Vasconcelos (1892), Mateus & d'Andrade (2000).

Terceira does not front the stressed /u/. Mikołajczak (2014, pp. 417-418, 424) states that the labialisation of [u], *"muito comum nos grupos ocidental e oriental das ilhas, não se aplica ao dialeto da Terceira"*. So `tudo` is [ˈtudu] and `muda` is [ˈmudɐ].

The rule `TER_A_METAPHONY` opens a stressed /a/ towards [ɔ] before a final unstressed ⟨-o⟩: `pato` [ˈpɔtu], `gato` [ˈɡɔtu]. Mikołajczak (2014, p. 423), after Segura & Saramago (2001, p. 230), writes: *"o pato soa quase como [ˈpɔtu] ou gato como [ˈɡɔtu]"*. The rule does not touch an /a/ before a final ⟨-a⟩ (`casa` [ˈkazɐ]) or a stressed /a/ at the end of the word (`mar` [ˈmaɾ]). The process is variable across the islands, and the spec encodes it as categorical for words in ⟨-o⟩.

The `TER_CRESCENT_*` rules add a [w] on-glide before a stressed vowel after a labial or labiodental onset (/p b m f v/). Mikołajczak (2014, pp. 421-422) calls this the most individual trait of the Terceira speech: `porco` [ˈpwɔɾku], `bicho` [ˈbwiʃu], `bola` [ˈbwɔlɐ], `vinho` [ˈvwiɲu]. The spec switches off the `pt-PT` suffix rules and word lists, as Porto and Braga do.

Not modelled:

- The harmonic on-glide copies a high vowel two positions back (`ceifar` as [sejˈfjaɾ], `pintar` as [pĩˈtjaɾ], `fumar` as [fuˈmwaɾ]). The on-glide also occurs on an unstressed syllable (`morrer` as [mwˈoreɾ]). The allophone rules cannot see that far.
- The northern-type raising of stressed mid vowels (`soa` as [ˈsua], `flor` as [ˈflur], Leite de Vasconcelos 1892, p. 293) is lexical and variable.

---
[← European Portuguese](pt-PT.md) · [Home](../index.md) · [Brazilian Portuguese →](pt-BR.md)
