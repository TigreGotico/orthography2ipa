# Brasiliense Portuguese (pt-BR-x-brasilia) — Phonology Reference

**Code**: `pt-BR-x-brasilia` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Parent**: `pt-BR` (Brazilian standard) | **Quality tier**: research
**Sources**: Nascentes (1953, *O linguajar carioca*), Noll (2008), Mateus &
d'Andrade (2000), Callou & Leite (2001), Silva (2002)

`pt-BR-x-brasilia` models **Brasiliense / Candango** Portuguese — the speech
of Brasília, Brazil's planned capital (inaugurated 1960). It is a **delta**
spec inheriting the pt-BR base.

## Honest scope: this is a skeleton-tier delta by construction

Brasília is a special case among the pt-BR regional specs: **it has almost no
distinctive phonology to model.** Brasília postdates Nascentes' (1953)
canonical six-*subfalar* division of Brazil by a decade — the city did not
exist when the foundational dialect map was drawn, so there is no historical
*subfalar* to source a distinctive accent from the way there is for the
Sulista, Nortista, Mineiro, or other older-settlement varieties. The
Brasiliense/*candango* accent is instead a **koiné** — a levelled contact
variety formed from nationwide internal-migration waves (construction workers
and civil servants from every region, arriving from 1956 onward) that
converged on the socioeconomically dominant southeastern (São Paulo/Minas
Gerais-leaning) norm, over a Goiás/Central-West substratum.

No read source documents a phonemic-level feature that reliably distinguishes
Brasiliense speech from the SP/MG-leaning standard it levelled toward. Rather
than invent a feature to justify a non-trivial delta, this spec is
**deliberately encoded as pt-BR unchanged**:

| Feature | Encoding |
|:---|:---|
| /t,d/ palatalisation before /i/ | inherited (present) |
| Onset /r/ | inherited (dorsal [ʁ]) |
| Coda /r/ | inherited (tap) |
| Coda /S/ | inherited (alveolar, non-*chiado*) |
| Coda /l/ → [w] | inherited |
| Post-stressed vowel reduction | inherited |

```python
from orthography2ipa import G2P
eng = G2P("pt-BR-x-brasilia")
eng.transcribe_word("tia")    # ˈt͡ʃiɐ  — same as pt-BR base
eng.transcribe_word("mesmo")  # ˈmesmʊ — no chiado
eng.transcribe_word("vento")  # ˈvẽtʊ  — standard final reduction
```

## Known limits (documented, not faked)

**Not a stub by oversight — a stub by evidence.** This is the honest
alternative to fabricating a "Brasiliense feature" that no read source
supports. If future ALiB or sociolinguistic fieldwork on the Distrito Federal
documents a genuine phonemic divergence (e.g. contact effects specific to the
candango koiné, as opposed to simple SP/MG convergence), this spec should be
enriched with a sourced positional-graphemes delta at that point — see
[Contributing / adding a language](../adding_a_language.md) for the process.
Until then, `pt-BR-x-brasilia` exists in the registry to name the variety and
document *why* it carries no encoded divergence, rather than to leave it
unregistered and implicitly conflated with the SE standard.

## Sources

- **Nascentes, Antenor (1953).** *O linguajar carioca* (2nd ed.). Organização
  Simões, Rio de Janeiro. (Cited for context: Brasília postdates Nascentes'
  six-*subfalar* division by a decade, hence no historical *subfalar* label
  applies.)
- **Noll, Volker (2008).** *O português brasileiro: formação e contrastes.*
  Globo.
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.
- **Callou, D. & Leite, Y. (2001).** *Iniciação à fonética e à fonologia*
  (8th ed.). Zahar.
- **Silva, T. C. (2002).** *Fonética e fonologia do português.* Contexto.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [pt-BR-x-sp](pt-BR-x-sp.md), [pt-BR-x-mg](pt-BR-x-mg.md)*
