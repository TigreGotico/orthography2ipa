# Fluminense Portuguese (pt-BR-x-fluminense) — Phonology Reference

**Code**: `pt-BR-x-fluminense` | **Family**: Indo-European > Romance | **Script**: Latin
**Quality tier**: research | **Parent**: `pt-BR`
**Sources**: Callou (2010, *Um perfil da fala carioca*), Mateus & d'Andrade
(2000), Silva (2002), Atlas Linguístico do Brasil (Cardoso et al. 2014)

Fluminense is the Portuguese of the state of Rio de Janeiro beyond the
capital. It shares the Carioca profile in its coastal/prestige form and is
modelled here as the same set of deltas on the [pt-BR base](pt-BR.md) as
[pt-BR-x-rj](pt-BR-x-rj.md), with the caveat that the chiado is a **gradient**
across the state.

## Chiado — the coastal prestige default

The NURC Rio data that quantifies the *chiado carioca* (Callou 2010:135:
91 % palatal coda /S/ word-internally, 76 % word-final) is the coastal
Fluminense norm, encoded here as the default.

| id | Rule | Example |
|:---|:---|:---|
| `FLU_CHIADO_CODA_S` | /s/ → [ʃ] in coda | `mesmo` [ˈmeʃmu], `paz` [ˈpaʃ] |
| `FLU_CHIADO_CODA_Z` | /z/ → [ʒ] in coda (pre-voiced) | — |
| `FLU_CODA_R_VELAR` | coda /R/ → [x] pre-consonantally | `porta` [ˈpoxtɐ] |
| `FLU_CODA_R_FINAL` | word-final coda /R/ → [h] | `mar` [ˈmah] |

The rules are coda-only, exactly as in Carioca (`sala` [ˈsalɐ] keeps its
onset [s]).

## The gradient (documented, not modelled)

Fluminense is heterogeneous. The chiado is less consistent in the rural and
northern interior of the state, where an inland tap-rhotic, partly
caipira-influenced substratum coexists with the coastal palatal-sibilant
norm. The spec encodes the **prestige coastal** value and documents the
variability in its `notes` rather than shipping a second, conflicting
transcription. A speaker of the caipira-influenced interior is better served
by [pt-BR-x-caipira](pt-BR-x-rj.md) for the retroflex rhotic.

```python
from orthography2ipa import G2P
G2P("pt-BR-x-fluminense").transcribe_word("mesmo")  # ˈmeʃmu
G2P("pt-BR-x-fluminense").transcribe_word("mar")    # ˈmah
```

## What is inherited unchanged

`/t d/` affrication before /i/, coda /l/ → [w], and final-vowel raising all
come from the pt-BR base. See [pt-BR.md](pt-BR.md).

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [pt-BR-x-rj](pt-BR-x-rj.md), [pt-BR-x-sp](pt-BR-x-sp.md)*
