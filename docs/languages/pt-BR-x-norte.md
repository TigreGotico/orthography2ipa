# Nortista / Amazônico Portuguese (pt-BR-x-norte) — Phonology Reference

**Code**: `pt-BR-x-norte` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Parent**: `pt-BR` (Brazilian standard) | **Quality tier**: research
**Sources**: Nascentes (1953, *O linguajar carioca*), Silva (2014, ALFAL
XVII), Noll (2008), Cardoso et al. (2014, *ALiB*), Mateus & d'Andrade (2000),
Callou & Leite (2001), Silva (2002)

`pt-BR-x-norte` models **Nortista / Amazônico** Portuguese — Belém and
Manaus — under Tupí/Nheengatu contact in prosody and lexicon. It is a
**delta** spec inheriting the pt-BR base. Nascentes (1953:25) grounds the
Brazil-wide North/South macro-division on pretonic-vowel openness and places
this area among the *falares do Norte*.

## Diagnostic features modelled

### 1. Coda /S/ palatalisation — the Belém *chiado*

Coda /s,z/ palatalise to [ʃ,ʒ] (*mesmo* → [ˈmeʒmʊ]), matching the Carioca
chiado rather than the plain-alveolar Northeast-proper norm. This is the
strongest diagnostic modelled here, sourced directly (not by inference):

> "[C]erto espraiamento dessas realizações para outras áreas do Brasil, a
> exemplo de Belém e Macapá, no Norte, onde haveria um grau de palatalização
> similar ao do Rio de Janeiro." — Silva (2014:2, ALFAL XVII, printed page
> header #4814), citing Noll (2008)

Silva (2014:2) further reports that Mota, Jesus & Evangelista's (2010)
ALiB-based grouping of Brazilian capitals by coda-/S/ realisation places
**Belém and Macapá together with Rio de Janeiro** (plus Florianópolis,
Recife, Manaus, Cuiabá, Salvador) among the cities where the **palatal**
variant predominates in *both* medial and absolute word-final position — the
strongest palatalising tier in the ALiB capital sample. Modelled via
`positional_graphemes` `s`/`z` → [ʃ] at `before_consonant`/`coda`/`word_final`,
with `s` `intervocalic` → [z] retained from the base.

### 2. /t d/ palatalisation before /i/ RETAINED (unlike the Northeast proper)

Unlike Recife/Fortaleza-type Northeastern varieties, the North retains
southeastern-style palatalisation of /t,d/ before /i/: *tia* → [ˈt͡ʃiɐ], *dia*
→ [ˈd͡ʒiɐ]. This is the base pt-BR default, left un-overridden here — ALiB
data identifies the North as the region of most expressive /t,d/
palatalisation nationally (Cardoso et al. 2014), so this is a deliberate
non-override, not an oversight.

### 3. Open pretonic vowels

/e/ and /o/ open to [ɛ] and [ɔ] in pretonic position, a Northeastern-type
feature shared with the North: *menino* → [mɛˈninʊ].

| Word | pt-BR-x-sp | pt-BR-x-norte |
|:---|:---|:---|
| mesmo | ˈmesmʊ | **ˈmeʒmʊ** |
| tia | ˈt͡ʃiɐ | ˈt͡ʃiɐ (retained) |
| menino | mɛˈninʊ / meˈninʊ | **mɛˈninʊ** |

## Inherited from pt-BR (unchanged)

Coda /l/ vocalisation to [w] (*sol* → [ˈsɔw]) and the grapheme inventory are
inherited and not restated.

## Known limits (documented, not faked)

**Heterogeneity.** "Nortista/Amazônico" spans a vast, sparsely-atlassed
region; Belém (the source of the chiado citation) and Manaus are not
guaranteed to pattern identically, and interior Amazonian varieties are not
separately modelled. Lexical open-mid vowel quality outside the pretonic
position is not derivable (a pt-BR-wide engine limit). No feature is modelled
without a read source backing it.

```python
from orthography2ipa import G2P
eng = G2P("pt-BR-x-norte")
eng.transcribe_word("mesmo")   # ˈmeʒmʊ — Belém chiado
eng.transcribe_word("tia")     # ˈt͡ʃiɐ  — palatalisation retained
eng.transcribe_word("menino")  # mɛˈninʊ — open pretonic /e/
```

## Sources

- **Nascentes, Antenor (1953).** *O linguajar carioca* (2nd ed.). Organização
  Simões, Rio de Janeiro. (pp. 20, 23-25: North/South macro-division of
  Brazilian Portuguese on pretonic-vowel openness.)
- **Silva, A. R. (2014).** "Variação fonética em capitais brasileiras: a
  ditongação diante de /S/ e as realizações fonéticas do /S/ em coda."
  *XVII Congreso Internacional ALFAL*, João Pessoa, #4813–4818. (p. 2 /
  #4814: Belém/Macapá coda-/S/ palatalisation, citing Noll 2008 and Mota,
  Jesus & Evangelista 2010.)
- **Noll, Volker (2008).** *O português brasileiro: formação e contrastes.*
  Globo.
- **Cardoso, S. A. M. et al. (2014).** *Atlas Linguístico do Brasil (ALiB),*
  vols. 1–2. EDUEL. (Pretonic-vowel and palatalisation isoglosses.)
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.
- **Callou, D. & Leite, Y. (2001).** *Iniciação à fonética e à fonologia*
  (8th ed.). Zahar.
- **Silva, T. C. (2002).** *Fonética e fonologia do português.* Contexto.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [pt-BR-x-rj](pt-BR-x-rj.md), [pt-BR-x-fluminense](pt-BR-x-fluminense.md)*
