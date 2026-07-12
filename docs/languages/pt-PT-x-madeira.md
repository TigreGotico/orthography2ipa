# Madeiran European Portuguese (pt-PT-x-madeira) — Phonology Reference

**Code**: `pt-PT-x-madeira` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` (standard, Lisbon-type EP) | **Quality tier**: research
**Sources**: Segura (2013, *Gramática do Português* vol. I), Mateus & d'Andrade (2000)

`pt-PT-x-madeira` models the European Portuguese of **Madeira** (Funchal /
Ribeira Brava reference). It is a **delta** spec: it inherits the whole
standard pt-PT system (unstressed vowel reduction, dark coda /l/,
coda-sibilant *chiado*, sandhi) via `graphemes_base` / `allophones_base` and
OVERLAY_BY_ID `allophone_rules`, and declares only the Madeiran-specific
diagnostic features.

## Diagnostic features modelled

### 1. Intervocalic /l/ → [ʎ] after /i/

The best-known Madeiran shibboleth: an intervocalic /l/ **after /i/** is
palatalised to **[ʎ]** — Segura (2013) describes it as *"a palatalização de
[l] em contexto de [i]"*. Modelled as the post-lexical `allophone_rules` entry
**`MAD_L_PALATALISATION`** (`/l/ → [ʎ]`), gated to a preceding phoneme /i/ and
a following vowel (so the /l/ is an onset between /i/ and another vowel):

| Word | pt-PT | pt-PT-x-madeira |
|:---|:---|:---|
| quilo | ˈkilu | **ˈkiʎu** |
| mochila | muˈʃilɐ | **muˈʃiʎɐ** |
| vila | ˈvilɐ | **ˈviʎɐ** |

The gate is exact: an /l/ after any *other* front vowel is untouched —
`teleférico` → tɨlɨˈfɛɾiku (/l/ after reduced [ɨ]) — and an onset /l/ not
preceded by /i/ stays clear (`levada` → lɨˈvadɐ).

### 2. Nasal-diphthong → nasal+N reduction

The salient productive Madeiran nasal pattern: the plural/nasal endings -ões,
-ães and -ãos surface with a nasal vowel **plus [n]** rather than a nasal
glide. Modelled as multi-character grapheme overrides `ões` → [õns], `ães` /
`ãos` → [ɐ̃ns]:

| Word | pt-PT | pt-PT-x-madeira |
|:---|:---|:---|
| cães | ˈkɐ̃j̃ʃ | **ˈkɐ̃ns** |

### 3. /v/ ~ /b/ distinction preserved (no betacism)

Madeiran, like standard EP and **unlike** the northern mainland, has **no**
betacism: /v/ stays [v] in all positions (`visitar` → viziˈtaɾ, `levada` →
lɨˈvadɐ, `novo` → ˈnovu). The single gold datum `vinho` → [ˈbiɲu] is a
lexicalised item, not a productive merger, and is deliberately **not** modelled
(betacism is a Northern feature — see `pt-PT-x-porto`).

## Inherited from pt-PT (unchanged)

Dark coda /l/ → [ɫ] (`mel` → ˈmɛɫ), the coda-sibilant *chiado* /s z/ → [ʃ ʒ],
extreme unstressed vowel reduction, and the coda-s voicing/resyllabification
sandhi are inherited from the parent and not restated here.

## Known limits (documented, not faked)

**Singular -ão → [õns].** The gold shows this sporadically (`verão` →
[vɨˈɾõns]) but the far more frequent monosyllable `são` keeps [sɐ̃w]; a blanket
`ão` override would regress the base, so only the productive plural
-ões/-ães/-ãos pattern is encoded.

**Stressed /i/ diphthongisation** ([i] → [ɐj]) is reported for Madeiran but is
left out because this gold keeps [i] (`dia` → [ˈdiɐ], `ilha` → [ˈiʎɐ]); a
blanket rule would regress it. It is a lexically-restricted process best left
to a downstream engine.

**Sporadic / lexical items** (r-diphthongisation `correr` → [kuˈʁweɾ], `Filipa`
→ [ˈfʎipɐ]) and narrow sub-phonemic detail (stop aspiration, final devoicing)
are outside the base rule scope.

## Benchmark honesty

On the `ep_dialects` expert gold (n = 30) the spec moves **PER 0.2235 →
0.2161**, the gain coming from the `MAD_L_PALATALISATION` rule (quilo, mochila,
vila). The nasal+N overrides were already present. No other scoreboard row
moves.

```python
from orthography2ipa import G2P
eng = G2P("pt-PT-x-madeira")
eng.transcribe("quilo")       # ˈkiʎu   — /l/ → [ʎ] after /i/
eng.transcribe("teleférico")  # tɨlɨˈfɛɾiku — /l/ after [ɨ] untouched
eng.transcribe("cães")        # ˈkɐ̃ns   — nasal+N
eng.transcribe("levada")      # lɨˈvadɐ  — /v/ preserved, no betacism
```

## Sources

- **Segura, Luísa (2013).** *Variedades dialetais do português europeu.* In
  E. B. P. Raposo et al. (eds.), *Gramática do Português*, vol. I, Fundação
  Calouste Gulbenkian, Lisboa, pp. 85–142.
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-acores](pt-PT-x-acores.md), [pt-PT-x-lisbon](pt-PT-x-lisbon.md)*
