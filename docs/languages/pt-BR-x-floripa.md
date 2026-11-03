# Florianópolis Portuguese (pt-BR-x-floripa)

| Field | Value |
|:---|:---|
| Code | `pt-BR-x-floripa` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | research |
| ISO 639-3 | `por` |
| Parent | `pt-BR` |
| Sources | Brescancini (2015), Dias (2010), Battisti & Dornelles Filho (2015) |

This spec models the traditional speech of native Florianópolis, the island capital of Santa Catarina. Natives of the island are called *manezinhos* or *ilhéus*, and the literature uses the same names for their speech (Dias 2010: 2).

Every transcription on this page is real output of `orthography2ipa.transcribe(text, "pt-BR-x-floripa")`. For the scores of the spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

## Parent and ancestry

The spec sets `parent` to `pt-BR` and inherits Brazilian Portuguese through `graphemes_base`, `allophones_base` and `positional_graphemes_base`. It declares two differences. Everything else, the vowels, the rhotics, the coda /l/ and the final vowel raising, comes from `pt-BR`.

## Modelled features

A coda /S/ is palato-alveolar. Brescancini (2015: 82) finds *"a variante palato-alveolar como predominante na amostra [...] em 83% das ocorrências"*, in three districts of the city. She illustrates the variants with *fe[ʃ]ta* and *me[ʒ]mo* (p. 76). The rules `FLORIPA_CODA_S` and `FLORIPA_CODA_Z` give [ʃ] and [ʒ] in the coda: `festa` [ˈfeʃtɐ], `mas` [ˈmaʃ], `paz` [ˈpaʃ].

The stops /t d/ stay stops before /i/. Dias (2010: 2) writes: *"Uma das características mais evidentes no falar 'manezinho' é ausência da africação de /t,d/"*, so *tipo* is [tipu]. The positional map gives the plain stop before ⟨i⟩, and the spec switches off `BR_AFFRIC_T_RAISED` and `BR_AFFRIC_D_RAISED`: `tipo` [ˈtipu], `dia` [ˈdiɐ], `leite` [ˈlejti], `dentes` [ˈdẽtiʃ].

| Spelling | IPA | Feature |
|:---|:---|:---|
| `festa` | ˈfeʃtɐ | coda /S/ gives [ʃ] |
| `mas` | ˈmaʃ | word-final /S/ gives [ʃ] |
| `tipo` | ˈtipu | /t/ stays a stop before /i/ |
| `dia` | ˈdiɐ | /d/ stays a stop before /i/ |
| `dentes` | ˈdẽtiʃ | final ⟨-es⟩ raises, no affrication, palatal /S/ |

## What the spec does not model

The city has many speakers who were born elsewhere, and Dias (2010: 2) connects the variation in the city to that migration. The ALiB rates /t d/ palatalisation in the capital as *"moderada"* (Battisti & Dornelles Filho 2015: 226). The spec models the native pole and does not give the affricates of the migrant speakers.

Dias (2010) also studies an aspirated release of /t d/ before a pause. The spec does not model it.

No opened source describes the coda /R/ or the strong /R/ of the island. The spec keeps the `pt-BR` values.

## Input contract

Input is standard Brazilian Portuguese orthography. The spec gives the native island norm.

## Limitations

No board gold exists for this variety. So the correctness of the spec rests on its citations, not on a PER. Coda palatalisation is variable (83 %), and the spec gives the majority form.

## Sources

- Brescancini, Cláudia Regina (2015). "A palatalização em coda em Florianópolis/SC: variáveis sociais". *Working Papers em Linguística* (UFSC) 16(1), 75-97. <https://doi.org/10.5007/1984-8420.2015v16n1p75>
- Dias, Eva Christina O. (2010). "Uso variável das oclusivas alveolares /t, d/ em Florianópolis". *Working Papers em Linguística* (UFSC), special issue, 1-19. <https://periodicos.ufsc.br/index.php/workingpapers/article/download/1984-8420.2010v11nespp1/17210/57527>
- Battisti, Elisa & Dornelles Filho, Adalberto Ayjara (2015). "Análise em tempo real da palatalização de /t/ e /d/ no português falado em uma comunidade ítalo-brasileira". *Revista da ABRALIN* 14(1), 221-246. <https://revista.abralin.org/index.php/abralin/article/download/1239/1162/549>

---
[← Brazilian Portuguese dialects](pt-BR-dialects.md) · [Home](../index.md) · [Cuiabano Portuguese →](pt-BR-x-cuiaba.md)
