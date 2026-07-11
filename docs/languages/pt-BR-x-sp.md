# Paulistano Portuguese (pt-BR-x-sp) — Phonology Reference

**Code**: `pt-BR-x-sp` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-BR` (Brazilian standard) | **Quality tier**: research
**Sources**: Barbosa & Albano (2004, *JIPA* 34(2):227–232), Mateus &
d'Andrade (2000), Callou & Leite (2001), Silva (2002); Amaral (1920, §6b, for
contrast)

`pt-BR-x-sp` models **Paulistano** — the urban Portuguese of the city and
metropolitan region of São Paulo, and the reference variety of the
*Illustrations of the IPA* description of Brazilian Portuguese (Barbosa &
Albano 2004). It is a **delta** spec that inherits the pt-BR base essentially
unchanged; Paulistano *is* one of the two prestige southeastern norms on which
that base is built.

## Diagnostic features modelled

### 1. Plain tap coda /r/ — NOT retroflex

Paulistano coda /r/ is a plain alveolar tap [ɾ] (*porta* → [ˈpoɾtɐ], *mar* →
[ˈmaɾ]). The retroflex "r caipira" described by Amaral (1920) §6b —
*"assemelha-se bastante ao r inglês post-vocálico"* — belongs to the
surrounding **Caipira interior** ([pt-BR-x-caipira.md](pt-BR-x-caipira.md)),
**not** to the capital. This spec is deliberately the non-retroflex member of
the São Paulo pair.

### 2. Non-*chiado* coda /s/

Coda /s/ stays alveolar [s]/[z] by voicing assimilation — *mesmo* → [ˈmesmu],
*dois* → [ˈdojs] — never the Carioca palatal *chiado* [ʃ]/[ʒ]. This is the
southeastern-non-Carioca sibilant pattern (Barbosa & Albano 2004).

### 3. /t d/ palatalisation before /i/ (inherited)

Full affrication *tia* → [ˈt͡ʃiɐ], *dia* → [ˈd͡ʒiɐ], and again before a
reduced final /e/ raised to [i] (*norte* → [ˈnɔɾt͡ʃi]). Inherited from the
pt-BR base.

| Word | pt-BR-x-caipira | pt-BR-x-sp |
|:---|:---|:---|
| porta | ˈpoɻtɐ | **ˈpoɾtɐ** |
| mar | ˈmaɻ | **ˈmaɾ** |
| tia | ˈt͡ʃiɐ | ˈt͡ʃiɐ |

## Inherited from pt-BR (unchanged)

Coda /l/ vocalisation to [w] (*sol* → [ˈsow]), final unstressed reduction
([ɪ ʊ ɐ]), strong dorsal onset /r/ → [ʁ~x~h], and word-final infinitive-/r/
dropping are all inherited and not restated.

## Known limits (documented, not faked)

Lexical open-mid vowel quality of unmarked ⟨o⟩/⟨e⟩ is not derivable from
spelling; the engine defaults to close [o]/[e] (e.g. *porta* → [ˈpoɾtɐ], not
[ˈpɔɾtɐ]). This is a pt-BR-wide engine limit, not a Paulistano-specific one.

```python
from orthography2ipa import G2P
eng = G2P("pt-BR-x-sp")
eng.transcribe_word("porta")   # ˈpoɾtɐ  — plain tap, no retroflex
eng.transcribe_word("mesmo")   # ˈmesmu  — coda /s/ alveolar, no chiado
eng.transcribe_word("tia")     # ˈt͡ʃiɐ  — palatalisation inherited
```

## Sources

- **Barbosa, P. A. & Albano, E. C. (2004).** Brazilian Portuguese
  (Illustrations of the IPA). *Journal of the International Phonetic
  Association* 34(2): 227–232.
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.
- **Callou, D. & Leite, Y. (2001).** *Iniciação à fonética e à fonologia*
  (8th ed.). Zahar.
- **Silva, T. C. (2002).** *Fonética e fonologia do português.* Contexto.
- **Amaral, Amadeu (1920).** *O Dialeto Caipira.* Casa Editora "O Livro", São
  Paulo. (§6b, cited only for the contrast: the retroflex /r/ is an interior
  Caipira, not a capital, feature.)

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [pt-BR-x-caipira](pt-BR-x-caipira.md), [pt-BR-x-rj](pt-BR-x-rj.md)*
