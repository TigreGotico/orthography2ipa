# Sulista / Gaúcho Portuguese (pt-BR-x-sul) — Phonology Reference

**Code**: `pt-BR-x-sul` | **Family**: Indo-European > Romance | **Script**: Latin (alphabet)
**Parent**: `pt-BR` (Brazilian standard) | **Quality tier**: research
**Sources**: Nascentes (1953, *O linguajar carioca*), Noll (2008), Cardoso et
al. (2014, *ALiB*), Silva (2014, ALFAL XVII), Mateus & d'Andrade (2000),
Callou & Leite (2001), Silva (2002)

`pt-BR-x-sul` models **Sulista / Gaúcho** Portuguese — the broader Southern
Brazilian norm centred on Rio Grande do Sul and Porto Alegre, extending
loosely across the RS/SC/PR "gauge" — over heterogeneous Italian and German
settler substrata. It is a **delta** spec inheriting the pt-BR base. Nascentes
(1953:25) grounds the Brazil-wide North/South macro-division on pretonic-vowel
openness and places this area among the *falares do Sul*.

## Diagnostic features modelled

### 1. Conservative non-palatalisation of /t d/ before /i/

The encoded default keeps **dental** /t d/ before /i/: *tia* → [ˈtiɐ], *dia*
→ [ˈdiɐ] (no [t͡ʃ]/[d͡ʒ]) — the opposite of the southeastern norm. Modelled
via `positional_graphemes` `t`/`d` `before_i` → [t]/[d]. A generational shift
toward palatalisation in urban Porto Alegre speech is documented but not the
modelled default here.

### 2. Alveolar tap/trill /r/ — NOT the posterior [h~x] of the Southeast

Onset /r/ surfaces as an alveolar trill/tap [r~ɾ] — the most European-sounding
Brazilian rhotic — never the glottal/dorsal [h~x] of the São Paulo/Carioca
norm: *rato* → [ˈratʊ]. Coda /r/ is likewise a **tap**, not dropped or
posteriorised: *mar* → [ˈmaɾ].

### 3. Reduced final-vowel raising

Word-final unstressed /e/ often stays [e] rather than raising to [i] in
conservative Sulista speech: *verde* → [ˈveɾde] (not [ˈveɾdʒi]).

| Word | pt-BR-x-sp | pt-BR-x-sul |
|:---|:---|:---|
| tia | ˈt͡ʃiɐ | **ˈtiɐ** |
| rato | ʁˈatʊ | **rˈatʊ** |
| verde | ˈveɾdʒi | **ˈveɾde** |

## Coordination with pt-BR-x-pr

[pt-BR-x-pr](pt-BR-x-pr.md) already covers the Curitibano/Paranaense
conservative-southern profile (same non-palatalisation + final-/e/-retention
delta, plus a note on the Paraná-interior retroflex /r/). `pt-BR-x-sul` models
the broader Gaúcho/RS norm the `pr` spec is transitional from; the two specs
intentionally share most deltas rather than duplicating divergent encodings.

## Inherited from pt-BR (unchanged)

Coda /l/ vocalisation to [w] (*sol* → [ˈsɔw]), final /a/ → [ɐ] reduction, and
the grapheme inventory are inherited and not restated.

## Known limits (documented, not faked)

**Heterogeneity.** "Sulista" spans three states (RS/SC/PR) with real internal
variation (e.g. the Florianópolis coast leans toward Carioca-style chiado
tendencies per VARSUL data in Silva 2014:5-6). This spec encodes the
conservative Gaúcho/Porto Alegre-type default; it does not model Florianópolis
or the Paraná interior separately. Lexical open-mid vowel quality is not
derivable (a pt-BR-wide engine limit).

```python
from orthography2ipa import G2P
eng = G2P("pt-BR-x-sul")
eng.transcribe_word("tia")   # ˈtiɐ    — conservative, no affrication
eng.transcribe_word("rato")  # rˈatʊ   — alveolar trill onset, not [h~x]
eng.transcribe_word("verde") # ˈveɾde  — final /e/ retained
```

## Sources

- **Nascentes, Antenor (1953).** *O linguajar carioca* (2nd ed.). Organização
  Simões, Rio de Janeiro. (pp. 20, 23-25: North/South macro-division of
  Brazilian Portuguese on pretonic-vowel openness.)
- **Noll, Volker (2008).** *O português brasileiro: formação e contrastes.*
  Globo.
- **Cardoso, S. A. M. et al. (2014).** *Atlas Linguístico do Brasil (ALiB),*
  vols. 1–2. EDUEL. (Pretonic-vowel and palatalisation isoglosses.)
- **Silva, A. R. (2014).** "Variação fonética em capitais brasileiras: a
  ditongação diante de /S/ e as realizações fonéticas do /S/ em coda."
  *XVII Congreso Internacional ALFAL*, João Pessoa, #4813–4818. (pp. 6–7 /
  #4817–4818: secondary citation of Bisol 1994, 2012, whose impressionistic
  /S/-coda diphthongization data is drawn from Porto Alegre speech.)
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.
- **Callou, D. & Leite, Y. (2001).** *Iniciação à fonética e à fonologia*
  (8th ed.). Zahar.
- **Silva, T. C. (2002).** *Fonética e fonologia do português.* Contexto.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [pt-BR-x-pr](pt-BR-x-pr.md), [pt-BR-x-caipira](pt-BR-x-caipira.md)*
