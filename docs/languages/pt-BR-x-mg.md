# Mineiro Portuguese (pt-BR-x-mg) — Phonology Reference

**Code**: `pt-BR-x-mg` | **Family**: Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Parent**: `pt-BR`
**Sources**: Lemos & Viegas (2016, *O alçamento das vogais médias pretônicas
em falares mineiros*), Castilho (2010), Mateus & d'Andrade (2000), Silva
(2002), Atlas Linguístico do Brasil (Cardoso et al. 2014)

Mineiro is the Portuguese of Minas Gerais, centred on Belo Horizonte. Unlike
its Carioca neighbour, its diagnostic feature is **vocalic, not sibilant**:
it does *not* chiado. It is modelled as a delta on the [pt-BR base](pt-BR.md).

## Diagnostic: pretonic mid-vowel raising

The signature of Mineiro is the raising (*alçamento*) of the pretonic mid
vowels /e o/ to the high vowels [i u]:

> "as vogais médias [e,o] alçam para vogais [i,u] … como em p[i]ru … s[i]nhora
> e b[u]neca." — Lemos & Viegas (2016:314)

Two motivations are documented (Lemos & Viegas 2016:314-315): vowel harmony
with a following high vowel, and consonant-driven vowel reduction; Viegas
(1987) established the additional role of the individual lexical item. Because
the trigger is orthographic position (a pretonic ⟨e⟩/⟨o⟩), this is realised in
the **pre-lexical** `positional_graphemes` map, not in `allophone_rules`:

| Process | Rule | Example |
|:---|:---|:---|
| Pretonic raising /e/ | ⟨e⟩ → [i] pretonic | `menino` [miˈninu] |
| Pretonic raising /o/ | ⟨o⟩ → [u] pretonic | `coruja` [kuˈɾuʒɐ] |

## NOT chiado — coda /S/ stays alveolar

Mineiro keeps the alveolar coda /S/ [s]/[z] of the pt-BR base. This is an
**inheritance**, not an added rule: the spec declares *no* coda-sibilant
`allophone_rules`, so `mesmo` stays [ˈmesmu] and `paz` stays [ˈpas]. This is
the point of contrast with the [Carioca](pt-BR-x-rj.md) chiado — modelling it
as the *absence* of an override keeps the delta honest and minimal.

```python
from orthography2ipa import G2P
G2P("pt-BR-x-mg").transcribe_word("menino")  # miˈninu
G2P("pt-BR-x-mg").transcribe_word("mesmo")   # ˈmesmu  (no chiado)
```

## Limits (documented, not modelled)

- **Rhotic** — Belo Horizonte city uses the tap [ɾ] (`porta` [ˈpoɾtɐ]); the
  rural interior shares the *caipira* retroflex [ɻ]. The city tap is the
  encoded default; the retroflex is left to
  [pt-BR-x-caipira](pt-BR-x-rj.md).
- **Extreme posttonic reduction and syllable loss** are a stereotyped Mineiro
  trait but are prosodic/segmental-deletion processes outside the scope of a
  grapheme-conditioned spec, so they are not encoded.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [pt-BR-x-caipira](pt-BR-x-caipira.md), [pt-BR-x-sp](pt-BR-x-sp.md)*
