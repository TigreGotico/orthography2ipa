# Paranaense / Curitibano Portuguese (pt-BR-x-pr) — Phonology Reference

**Code**: `pt-BR-x-pr` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Parent**: `pt-BR` (Brazilian standard) | **Quality tier**: research
**Sources**: Noll (2008), Cardoso et al. (2014, *ALiB*), Mateus & d'Andrade
(2000), Callou & Leite (2001), Silva (2002); Amaral (1920, §6b, for contrast)

`pt-BR-x-pr` models **Curitibano / Paranaense** — the Portuguese of Curitiba
and Paraná — a transitional **Sulista–Paulistano** variety over Slavic and
Italian settler substrata. It is a **delta** spec inheriting the pt-BR base
and overriding the conservative southern features.

## Diagnostic features modelled

### 1. Conservative non-palatalisation of /t d/ before /i/

Unlike the southeastern norm, the Curitibano default keeps **dental** /t d/
before /i/: *tia* → [ˈtiɐ], *dia* → [ˈdiɐ] (no [t͡ʃ]/[d͡ʒ]). Modelled via
`positional_graphemes` `t`/`d` `before_i` → [t]/[d]. Palatalisation is present
in younger and Paulista-influenced speech and is noted in the spec, but the
conservative form is the modelled default.

### 2. Final /e/ retention (the Curitiba "e/o fechados")

Word-final and unstressed /e/ is retained as [e] rather than raised to [i]:
*verde* → [ˈveɾde] (not [ˈveɾd͡ʒi]). Modelled via `positional_graphemes.e`
overrides at `word_final` / `posttonic` / `nucleus_unstressed`.

### 3. Alveolar tap coda /r/ — NOT retroflex

Coda /r/ is a Sulista-type alveolar tap [ɾ] (*porta* → [ˈpoɾtɐ], *mar* →
[ˈmaɾ]). The retroflex "r caipira" (Amaral 1920 §6b) is instead characteristic
of the **northern / interior Paraná hinterland**, which patterns with
[pt-BR-x-caipira.md](pt-BR-x-caipira.md) — Paraná is dialectologically
heterogeneous, and this spec models the Curitiba capital, not the interior.

### 4. Non-*chiado* coda /s/

Coda /s/ stays alveolar [s] (*costas* → [ˈkostas]) — neither the Carioca
palatal *chiado* nor a Nordestino aspiration [h].

| Word | pt-BR-x-sp | pt-BR-x-pr |
|:---|:---|:---|
| tia | ˈt͡ʃiɐ | **ˈtiɐ** |
| verde | ˈveɾd͡ʒi | **ˈveɾde** |
| porta | ˈpoɾtɐ | ˈpoɾtɐ |

## Inherited from pt-BR (unchanged)

Coda /l/ vocalisation to [w] (*sal* → [ˈsaw]), the final /a/ → [ɐ] reduction,
and the grapheme inventory are inherited and not restated.

## Known limits (documented, not faked)

**Heterogeneity.** Paraná is not phonologically uniform — Curitiba diverges
from the more Caipira-like interior. This spec encodes the Curitibano capital
norm; the interior is better served by `pt-BR-x-caipira`. Lexical open-mid
vowel quality is not derivable (a pt-BR-wide engine limit).

```python
from orthography2ipa import G2P
eng = G2P("pt-BR-x-pr")
eng.transcribe_word("tia")     # ˈtiɐ    — conservative, no affrication
eng.transcribe_word("verde")   # ˈveɾde  — final /e/ retained
eng.transcribe_word("porta")   # ˈpoɾtɐ  — alveolar tap, no retroflex
```

## Sources

- **Noll, Volker (2008).** *O português brasileiro: formação e contrastes.*
  Globo.
- **Cardoso, S. A. M. et al. (2014).** *Atlas Linguístico do Brasil (ALiB),*
  vols. 1–2. EDUEL. (Pretonic-vowel and palatalisation isoglosses.)
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.
- **Callou, D. & Leite, Y. (2001).** *Iniciação à fonética e à fonologia*
  (8th ed.). Zahar.
- **Silva, T. C. (2002).** *Fonética e fonologia do português.* Contexto.
- **Amaral, Amadeu (1920).** *O Dialeto Caipira.* Casa Editora "O Livro", São
  Paulo. (§6b, cited only for the contrast between the interior retroflex /r/
  and the Curitibano tap modelled here.)

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [pt-BR-x-sp](pt-BR-x-sp.md), [pt-BR-x-caipira](pt-BR-x-caipira.md)*
