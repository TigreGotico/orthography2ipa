# Uruguayan Portuguese (pt-UY)

| Field | Value |
|:---|:---|
| Code | `pt-UY` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | research |
| ISO 639-3 | `por` |
| Parent | `pt-BR` |
| Sources | Carvalho (1998), Rona (1965), Hensey (1972), Elizaincín (1992), Sturza (2021) |

Uruguayan Portuguese is the border-contact vernacular of northern Uruguay, based on Portuguese, in the Rivera region along the Brazilian frontier. The literature names it *Dialectos Portugueses del Uruguay* (DPU, Elizaincín), *fronterizo* (Rona) and Riverense. Speakers call it *portuñol* or *brasilero*. It is not the national language of Uruguay, which is Spanish.

It is a Portuguese vernacular of rural origin in close contact with border Spanish. It was once the only language of the border communities, and it is diglossic today (Carvalho 1998: 642, Elizaincín 1992).

Every transcription on this page is real output of `orthography2ipa.transcribe(text, "pt-UY")`. For the scores of the spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

## Parent and ancestry

The spec sets `parent` to `pt-BR` and inherits Brazilian Portuguese through `graphemes_base`, `allophones_base` and `positional_graphemes_base`. The read source supports this choice.

Carvalho (1998: 646, Figure 1) models the community as a dialect continuum with two poles: Rural Uruguayan Portuguese (RUP) and Urban Brazilian Portuguese (UBP). She states that the variety differs from standard Brazilian "mainly in three respects": retained rural features, Spanish interference and hybrid forms. Rivera speech moves toward urban Brazilian Portuguese as its reference norm.

The vowel system comes unchanged from `pt-BR`: seven oral vowels /a ɛ e i ɔ o u/ and the nasal set. That matches the inventory reported for the variety.

| Ancestor | Role | Weight | Reason |
|:---|:---|---:|:---|
| `pt-BR` | parent | 0.65 | structural base and diffusion norm, vowels and most maps inherited (Carvalho 1998: 646) |
| `es-UY` | adstrate | 0.3 | border Spanish, the source of the dental stops, the alveolar trill and the kept coda /l/ (Carvalho 1998: 646, Elizaincín 1992) |
| `pt-PT` | substrate | 0.05 | the rural European Portuguese of the first settlers (Carvalho 1998: 642) |

## Modelled features

The palatal lateral ⟨lh⟩ /ʎ/ becomes the glide [j]. It is the most salient marker of the rural, focused variety. Rona (1965: 23, through Carvalho 1998: 646) found it categorical, and he proposed the glide as the only phoneme. Carvalho (1998: 646) describes *"the pronunciation of the lateral phoneme as a front glide, as in /mujɛ/ instead of the standard /muʎɛr/"*. Local *coié* stands against Brazilian *colher* (p. 647).

The palatal [ʎ] is the urban Brazilian form that spreads into the variety. The spec keeps it as the second candidate: `mulher` [muˈjeɾ], `trabalho` [tɾaˈbaju].

The dental stops /t d/ stay before /i/, without palatalisation. Carvalho (1998: 646) writes of *"the maintenance of the dental stops /d/ and /t/ followed by /i/, a tendency kept probably due to Spanish interference"*. The dental form was nearly categorical in Rivera (Rona 1965: 40, Hensey 1972: 60, both through Carvalho 1998: 648).

The standard Brazilian [dʒia] and [tʃia] spread through the community, led by young, higher-status and female speakers (Carvalho 1998: 649, Tables 4-6). The spec records that spread in its notes and keeps the focused form as the default. The positional map gives the plain stop before ⟨i⟩, and the spec switches off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED`: `dia` [ˈdiɐ], `tia` [ˈtiɐ], `partido` [paɾˈtidu], `leite` [ˈlejti].

A coda /l/ stays the lateral [l] and does not vocalise to the urban Brazilian [w]. The source for this is secondary (Wikipedia, *Uruguayan Portuguese*), and it agrees with the Spanish adstrate. The spec overrides the inherited coda /l/ to [w]: `Brasil` [bɾaˈzil], `alto` [ˈaltu].

A word-initial ⟨r⟩ and ⟨rr⟩ are the alveolar trill [r], not the uvular [ʁ] of urban Brazilian Portuguese. The source for this is also secondary (Wikipedia), and it agrees with border Spanish. An ⟨r⟩ between vowels or in the coda stays the tap [ɾ]: `Rivera` [riˈveɾɐ], `carro` [ˈkaru].

| Spelling | IPA | Feature |
|:---|:---|:---|
| `mulher` | muˈjeɾ | ⟨lh⟩ gives the glide [j] |
| `trabalho` | tɾaˈbaju | ⟨lh⟩ gives the glide [j] |
| `dia` | ˈdiɐ | dental /d/ before /i/, no [dʒ] |
| `tia` | ˈtiɐ | dental /t/ before /i/, no [tʃ] |
| `Brasil` | bɾaˈzil | coda /l/ kept as [l] |
| `carro` | ˈkaru | ⟨rr⟩ gives the alveolar trill [r] |

## What the spec does not model

The coda /s/ stays the alveolar [s] of `pt-BR` (`mesmo` [ˈmesmu]). Carvalho's quantitative work on /s/ aspiration concerns border Spanish, and it is not clear that it applies to the Portuguese variety. So the spec imposes no [h] without a primary source for the Portuguese.

The variety has no betacism, unlike Barranquenho, and it keeps /v/ (`vida` [ˈvidɐ]).

The read sources do not quantify the fine pretonic vowels or any nasal-vowel detail beyond the inherited `pt-BR` set. The spec leaves them inherited.

No source for ⟨-en⟩ or the plural ⟨-ens⟩ in this variety was read. So the spec limits `BR_FINAL_EM_GLIDE` to a final ⟨m⟩ and switches off `BR_FINAL_ENS_GLIDE`: `bem` [ˈbẽj̃], but `hífen` [ˈifẽ] and `homens` [ˈomẽs].

No source on the final /R/ of this variety was read. So the spec switches off the `pt-BR` rules `BR_FINAL_R_NONVERB`, `BR_INFINITIVE_R_DROP` and `BR_INFINITIVE_R_DROP_POR`, and an infinitive keeps the tap: `falar` [faˈlaɾ].

## Input contract

Input is standard Portuguese orthography, as the literature and written *portuñol* use it for the variety. The spec transcribes the focused rural local norm that Rona, Hensey and Carvalho describe. The urban Brazilian variants, with palatalisation and the uvular r, are the diffusion pole of the continuum. The spec records them in its notes and does not produce them by default.

## Limitations

The only board row for `pt-UY` comes from a silver gold, `portuguese_tts` at the `llm-corrected` tier. So the correctness of the spec rests on its citations, not on a PER. The two main features, the glide and the dental stops, rest on a primary source (Carvalho 1998, cited by page). The coda /l/ and the trill rest on a secondary source (Wikipedia). Variation along the continuum from RUP to UBP is real and gradient. The spec fixes the focused local pole and notes the spread.

## Sources

- Carvalho, Ana Maria (1998). "Variation and diffusion of Uruguayan Portuguese in a bilingual border town". *Actas do I Simposio Internacional sobre o Bilingüismo*, Universidade de Vigo, pp. 642-651. <https://ssl.webs.uvigo.es/actas1997/05/Carvalho.pdf>
- Rona, José Pedro (1965). *El dialecto fronterizo del Norte del Uruguay*. Montevideo: Universidad de la República. Cited through Carvalho (1998).
- Hensey, Fritz (1972). *The Sociolinguistics of the Brazilian-Uruguayan Border*. The Hague: Mouton. Cited through Carvalho (1998).
- Elizaincín, Adolfo (1992). *Dialectos en Contacto. Español y Portugués en España y América*. Montevideo: Arca. The framework, through Carvalho (1998).
- Sturza, Eliana Rosa (2021). "Português do Uruguai e Português de Missões: língua, território e fronteira". *Línguas e Instrumentos Linguísticos* 24(48), 177-198. <https://doi.org/10.20396/lil.v24i48.8667912>

---
[← East Timorese Portuguese](pt-TL.md) · [Home](../index.md) · [Barranquenho →](ext-PT-x-barranco.md)
