# Carioca Portuguese (pt-BR-x-rj) — Phonology Reference

**Code**: `pt-BR-x-rj` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Parent**: `pt-BR`
**Sources**: Callou (2010, *Um perfil da fala carioca*), Mateus & d'Andrade
(2000), Silva (2002), Atlas Linguístico do Brasil (Cardoso et al. 2014)

Carioca is the accent of the city of Rio de Janeiro — one of the two
media-standard accents of Brazil. It inherits every map from the merged
[pt-BR base](pt-BR.md) (final-vowel raising, coda /l/ → [w], /t d/
affrication before /i/) and refines it with a handful of **deltas**, the
defining one being the *chiado carioca*.

## The defining feature: the *chiado carioca*

The hallmark of Carioca is the palatalisation of a coda sibilant. In cultured
Rio speech the coda /S/ surfaces as [ʃ] (voiceless) or [ʒ] (before a voiced
consonant) rather than the alveolar [s]/[z] of São Paulo or the interior.

> "A realização palatalizada do S em coda, no português do Brasil, o famoso
> 'chiado carioca', se restringia, de início, ao que tudo indica, ao Rio de
> Janeiro." — Callou (2010:134)

NURC real-time data quantifies just how categorical it is (Callou 2010:135,
Tabela 1, 1990s): **91 % palatal word-internally** (`ga[ʃ]to`) and **76 %
word-finally** (`lapi[ʃ]`), against 4 %/19 % alveolar. It is the highest
palatalisation index among the major Brazilian capitals.

Because this is a **phoneme → surface** process (the pt-BR base keeps an
alveolar coda /s/), it is modelled as a post-lexical `allophone_rules` pass,
mirroring the pt-PT `PT_CODA_S_HUSH`. The base's alveolar coda is overridden.

| id | Rule | Example |
|:---|:---|:---|
| `RJ_CHIADO_CODA_S` | /s/ → [ʃ] in coda | `mesmo` [ˈmeʃmu], `paz` [ˈpaʃ], `dois` [ˈdojʃ] |
| `RJ_CHIADO_CODA_Z` | /z/ → [ʒ] in coda (pre-voiced) | `desde` (coda before voiced C) |

The rule is **coda-only**: an onset or intervocalic ⟨s⟩ is untouched
(`sala` [ˈsalɐ], `casa` [ˈkazɐ]).

## Posterior coda /R/

Carioca has a strongly posterior rhotic. The strong onset /r/ is dorsal
[χ~x] (`rio` [ˈχiu]); in the coda:

> "a variante que predomina na fala culta carioca … é a fricativa velar, com
> exceção em final de vocábulo, em que ocorre preferencialmente o apagamento
> ou a aspiração." — Callou (2010:138), reporting Callou (1987)

| id | Rule | Example |
|:---|:---|:---|
| `RJ_CODA_R_VELAR` | coda /R/ → [x] pre-consonantally | `porta` [ˈpoxtɐ], `carta` [ˈkaxtɐ] |
| `RJ_CODA_R_FINAL` | word-final coda /R/ → [h] (aspiration) | `mar` [ˈmah] |

Word-final /R/ is modelled as aspiration [h] rather than deletion so the
segment is retained; the tap and intervocalic rhotics are left alone.

## What is inherited unchanged

`/t d/` affrication before /i/ (`tia` [ˈt͡ʃiɐ], `dia` [ˈd͡ʒiɐ]), coda /l/
vocalisation (`sol` [ˈsow]), and final-vowel raising all come from the
pt-BR base. See [pt-BR.md](pt-BR.md).

```python
from orthography2ipa import G2P
G2P("pt-BR-x-rj").transcribe_word("mesmo")  # ˈmeʃmu
G2P("pt-BR-x-rj").transcribe_word("porta")  # ˈpoxtɐ
```

## Limits

Coda-sibilant voicing before a voiced consonant ([ʃ] → [ʒ]) across a word
boundary is a sandhi process, not applied here; the socially graded
variability of the rhotic (suburb vs Zona Sul; Callou 2010:138-139) is a
sociolinguistic distribution the deterministic spec does not encode.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [pt-BR-x-fluminense](pt-BR-x-fluminense.md), [pt-BR-x-sp](pt-BR-x-sp.md)*
