# Brazilian Portuguese (pt-BR) — Phonology Reference

**Code**: `pt-BR` | **Family**: Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Sources**: Barbosa & Albano (2004, JIPA),
Câmara Jr. (1970), Mateus & d'Andrade (2000), Callou & Leite (2001)

`pt-BR` is the base spec for twelve regional Brazilian dialect specs
(`pt-BR-x-sp`, `-rj`, `-caipira`, `-mg`, `-sul`, `-recife`, …), which
inherit its maps via `graphemes_base` and refine them by delta. See
[romance.md](romance.md) for the pt-PT ↔ pt-BR comparison.

## The two maps for BP

The library models pronunciation as two maps (see
[../allophony.md](../allophony.md)): the **pre-lexical** map
(orthography → phoneme, in `positional_graphemes`) and the **post-lexical**
map (phoneme → surface allophone, in `allophone_rules`).

### Pre-lexical (positional_graphemes)

| Process | Rule | Example |
|:---|:---|:---|
| /t d/ affrication | ⟨t d⟩ → [t͡ʃ d͡ʒ] before ⟨i⟩ | `tio` [ˈt͡ʃiu], `dia` [ˈd͡ʒiɐ] |
| Coda /l/ vocalisation | ⟨l⟩ → [w] in coda / word-final | `sol` [ˈsɔw], `sal` [ˈsaw] |
| Coda /s/ | stays alveolar [s]/[z] (no chiado) | `mesmo` [ˈmezmu] |
| Unstressed /a/ | → [ɐ] final/posttonic | `capa` [ˈkapɐ] |

The chiado (coda /s/ → [ʃ]) is a **carioca/RJ dialect delta**, not general
BP, so the base keeps alveolar [s]/[z].

### Post-lexical allophony (allophone_rules)

Two rules make the second map live for BP:

| id | Process | Rule | Example |
|:---|:---|:---|:---|
| `BR_RAISE_FINAL_E` | Final vowel raising | [ɪ] → [i] / _# | `leite` [ˈlejti] |
| `BR_RAISE_FINAL_O` | Final vowel raising | [ʊ] → [u] / _# | `gato` [ˈɡatu] |

Word-final unstressed /e o/ raise to the close vowels [i]/[u] (Barbosa &
Albano 2004: 229; Câmara Jr. 1970). The positional map selects the
near-close [ɪ]/[ʊ] word-finally; these rules realise the standard BP close
surface form. They target the **reduced** [ɪ]/[ʊ] only — never the
underlying /e o/ — so a conservative dialect that retains a final [e]/[o]
inherits the rules harmlessly (they simply do not fire).

```python
from orthography2ipa import G2P
G2P("pt-BR").transcribe_word("gato")   # ˈɡatu
G2P("pt-BR").transcribe_word("leite")  # ˈlejti
G2P("pt-BR", apply_allophony=False).transcribe_word("gato")  # ˈɡatʊ (broad)
```

## What the base deliberately does NOT model

Honest limits, each a documented decision rather than an omission:

- **Strong pretonic reduction** — BP reduction is markedly weaker than EP;
  BP keeps distinct pretonic /e o/, so only the final position raises.
- **/t d/ affrication before a raised final ⟨e⟩** (e.g. `dente` →
  [ˈdẽt͡ʃi]) — expressible as a phoneme-conditioned allophone rule, but it
  would silently re-impose affrication on the non-palatalising nordeste
  varieties (recife/norte/ce) that inherit the base. It is deferred to the
  dialect-delta wave, where those varieties opt out by rule id. Grapheme-⟨i⟩
  affrication (the common case) is already handled pre-lexically.
- **Coda /r/ → [h~x]** — the general BP weak fricative is highly variable,
  and the broad wikipron pt-BR gold transcribes coda /r/ as [ʁ], so
  shipping [h~x] in the base regresses the only pt-BR gold. Held as a
  dialect delta.

## Benchmark effect (honest)

Measured on the committed gold set (PER, lower is better):

| Row | Gold | Before | After | Δ |
|:---|:---|---:|---:|---:|
| pt-BR | wikipron (n=124) | 0.1901 | 0.1578 | **−0.0323** |

Final-vowel raising to [i]/[u] both matches the gold's transcription and is
the cited BP realisation. The `pt` styletts2 row is unaffected: it resolves
to `pt-PT`, a different spec.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [romance](romance.md), [pt-BR-x-sp](pt-BR-x-sp.md), [pt-BR-x-rj](pt-BR-x-rj.md)*
