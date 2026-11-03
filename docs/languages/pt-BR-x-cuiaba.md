# Cuiabano Portuguese (pt-BR-x-cuiaba)

| Field | Value |
|:---|:---|
| Code | `pt-BR-x-cuiaba` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | research |
| ISO 639-3 | `por` |
| Parent | `pt-BR` |
| Sources | Almeida (2004), Battisti & Dornelles Filho (2015) |

This spec models the traditional speech of the Cuiabá river valley in Mato Grosso, the *Baixada Cuiabana*. Almeida (2004: 149) describes the speech of riverside Cuiabá natives, about fifty years old, with little or no schooling, whose parents and grandparents were also born there.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, "pt-BR-x-cuiaba")`. For the scores of the spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

## Parent and ancestry

The spec sets `parent` to `pt-BR` and inherits Brazilian Portuguese through `graphemes_base`, `allophones_base` and `positional_graphemes_base`. It declares the consonant differences below. The vowels and the final vowel raising come from `pt-BR`.

## Modelled features

Each feature below alternates with the `pt-BR` form, sometimes in one speaker and one word (Almeida 2004: 156). The spec gives the traditional form first and keeps the `pt-BR` form as the next candidate.

The stops /t d/ stay stops before /i/. Almeida (2004: 151-152) finds an *"articulação predominantemente oclusiva alveolodental"*, with [ˈsɛti] *sete* and [ˈdia] *dia*. The positional map gives the plain stop before ⟨i⟩, and the spec switches off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED`: `sete` [ˈseti], `rede` [ˈredi].

The palatal fricatives are often affricates. The fricatives *"comumente são pronunciadas, respectivamente, como africadas surda /tS/ e sonora /dZ/"* (pp. 154-155), as in *chegar*, *peixe*, *gente* and *hoje* (p. 155). The rules `CUIABA_AFFRIC_SH` and `CUIABA_AFFRIC_ZH` apply in the onset: `chegar` [t͡ʃeˈɡa], `puxa` [ˈput͡ʃɐ], `gente` [ˈd͡ʒẽti], `hoje` [ˈod͡ʒi].

A coda /S/ is palato-alveolar, *"principalmente quando se encontra em final de vocábulo"* (p. 153). The rules `CUIABA_CODA_S` and `CUIABA_CODA_Z` give [ʃ ʒ] in the coda. A coda [ʃ] is not an onset, so it does not become an affricate: `mas` [ˈmaʃ], `três` [ˈtɾeʃ], `dez` [ˈdɛʃ].

A coda /l/ is retroflex: *"Travando sílaba ou em final de vocábulo, a tendência é pela realização da retroflexa"* (p. 157). The positional map gives [ɻ] first and [w] second: `mal` [ˈmaɻ], `igual` [iˈɡwaɻ].

A coda /R/ is also retroflex, *"como se pode observar no chamado dialeto caipira brasileiro"* (p. 159): `porto` [ˈpoɻtu], `curva` [ˈkuɻvɐ]. A word-final /R/ tends to drop (p. 159), and the rule `CUIABA_FINAL_R_DELETION` deletes it: `fazer` [faˈze], `casar` [kaˈza]. The rule reads the grapheme ⟨r⟩, so a final retroflex /l/ stays.

A word-initial ⟨r⟩ and ⟨rr⟩ are the trill [r], with the velar [x] as the other form (pp. 158-159): `rapaz` [raˈpaʃ], `burro` [ˈburu].

| Spelling | IPA | Feature |
|:---|:---|:---|
| `sete` | ˈseti | /t/ stays a stop before /i/ |
| `chegar` | t͡ʃeˈɡa | ⟨ch⟩ gives [t͡ʃ], final /R/ drops |
| `hoje` | ˈod͡ʒi | ⟨j⟩ gives [d͡ʒ] |
| `mas` | ˈmaʃ | word-final /S/ gives [ʃ] |
| `mal` | ˈmaɻ | coda /l/ gives [ɻ] |
| `porto` | ˈpoɻtu | coda /R/ gives [ɻ] |
| `rapaz` | raˈpaʃ | strong /R/ is the trill [r] |

## What the spec does not model

The ALiB rates /t d/ palatalisation in the capital as *"moderada"* (Battisti & Dornelles Filho 2015: 226). The spec models the traditional valley speech of Almeida's informants, not the urban average.

Almeida (2004: 153, 158) also reports [ʃ] for /s/ between vowels and word-initially (*moço*, *senhor*), the glide [j] for ⟨lh⟩, and the deletion of a coda /l/. He reports each of these beside the standard form, and the spec does not model them.

The stressed vowel quality is lexical and not marked in the spelling. Almeida writes *sete* with [ɛ], and the spec gives the inherited [e] (see issue #1824).

## Input contract

Input is standard Brazilian Portuguese orthography. The spec gives the traditional valley norm.

## Limitations

No board gold exists for this variety. So the correctness of the spec rests on one primary source, Almeida (2004), cited by page. The affricates are most frequent in speakers with less schooling (p. 155), and they coexist with the fricatives.

## Sources

- Almeida, Manoel Mourivaldo Santiago (2004). "As consoantes do português falado no Vale do Cuiabá". *Signum: Estudos da Linguagem* (UEL) 7(1), 149-163. <https://ojs.uel.br/revistas/uel/index.php/signum/article/download/3880/3119/13043>
- Battisti, Elisa & Dornelles Filho, Adalberto Ayjara (2015). "Análise em tempo real da palatalização de /t/ e /d/ no português falado em uma comunidade ítalo-brasileira". *Revista da ABRALIN* 14(1), 221-246. <https://revista.abralin.org/index.php/abralin/article/download/1239/1162/549>

---
[← Florianópolis Portuguese](pt-BR-x-floripa.md) · [Home](../index.md) · [Angolan Portuguese →](pt-AO.md)
