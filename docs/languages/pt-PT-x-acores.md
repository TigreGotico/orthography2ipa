# Azorean European Portuguese (pt-PT-x-acores) — Phonology Reference

**Code**: `pt-PT-x-acores` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` (standard, Lisbon-type EP) | **Quality tier**: research
**Sources**: Rogers (1948, *Hispanic Review* 16:1–32), Mateus & d'Andrade (2000)

`pt-PT-x-acores` models the European Portuguese of the **Azores**. It is a
**delta** spec: it inherits the whole standard pt-PT system (unstressed vowel
reduction, dark coda /l/, coda-sibilant *chiado*, sandhi) via `graphemes_base`
/ `allophones_base` and OVERLAY_BY_ID `allophone_rules`, and declares only the
Azorean-specific diagnostic features.

**Reference variety.** The Azores span nine islands with substantial
inter-island variation; the wired `ep_dialects` gold is Terceira-type. The
headline /u/ → [y] feature is the **São Miguel** micro-variety, the strongest
and most stereotyped realisation. The spec models that strongest realisation
and documents the inter-island limit rather than faking a single pan-Azorean
norm.

## Diagnostic features modelled

### 1. Stressed open-syllable /u/ → [y] fronting (São Miguel class)

The single most stereotyped Azorean feature: a **stressed** back /u/ in an
**open syllable** is fronted to a front rounded **[y]**. Rogers (1948)
documents the fronting of stressed /u/ in the eastern islands (São Miguel);
it is the salient shibboleth of the variety (`tu` → [ty]).

Modelled as two ordered `allophone_rules` on the phoneme side:

| id | Rule | Example |
|:---|:---|:---|
| `ACO_U_KEEP_BEFORE_CODA` | /u/ stays [u] before a coda liquid/sibilant | azul → **ɐˈzuɫ**, Furnas → **ˈfuɾnɐʃ** |
| `ACO_STRESSED_U_FRONTING` | stressed /u/ → [y] before an onset consonant | número → **ˈnymɨɾu** |

The block rule is ordered first: it is an identity rewrite (u → u) whose only
job is to win the rescorer's first-match so the fronting cannot apply in a
closed syllable. The word-final shibboleth `tu` → [ty] is pinned in
`word_exceptions` (see below) because the sentence-level gold runs each
utterance as one concatenated token, where a word-boundary condition would
mis-fire on a sentence-final *unstressed* /u/.

An **unstressed** /u/ never fronts: `cozido` → kuˈzidu (pretonic), `rápido` →
ˈʁapidu (final).

### 2. /ow/ preservation

The ⟨ou⟩ digraph keeps its historical falling diphthong **[ow]** where standard
Lisbon monophthongises to [o]. Modelled as the grapheme delta `ou` → [ow]:
`touradas` → toˈwɾadɐʃ.

## The clitic guard — the article `o` is [u], never [y]

A stressed-/u/ → [y] rule is dangerous next to Portuguese proclitics: the
definite article `o`, the contractions `no`/`do`/`ao`/`pelo` and the numeral
`um` are monosyllables the stress detector marks as *stressed*, so a naïve rule
fronts `o` → [ˈy] (a sibling spec once shipped exactly this bug). Here the
fronting rule is structurally safe — it requires a **following onset
consonant**, which a bare `o`/`do`/`no`/`ao` never has — and, belt-and-braces,
every proclitic is pinned in `word_exceptions` to its [u]/[ũ] form:

| Clitic | Output | | Clitic | Output |
|:---|:---|---|:---|:---|
| o | u | | ao | aw |
| os | uʃ | | aos | awʃ |
| no / nos | nu / nuʃ | | pelo / pelos | ˈpelu / ˈpeluʃ |
| do / dos | du / duʃ | | um / uns | ũ / ũʃ |

**The article `o` is [u], never [y].**

## Inherited from pt-PT (unchanged)

Dark coda /l/ → [ɫ] (`sol` → ˈsɔɫ), the coda-sibilant *chiado* /s z/ → [ʃ ʒ],
extreme unstressed vowel reduction, and the coda-s voicing/resyllabification
sandhi are inherited from the parent and not restated here.

## Known limits (documented, not faked)

**Inter-island variation.** Fronting is categorical only in the São Miguel
class; Terceira (the gold reference) fronts only lexically, so `muda` surfaces
as São Miguel [ˈmydɐ] against the Terceira gold's [ˈmudɐ]. This divergence is a
documented island limit, not a modelling error.

**Nasal-diphthong → nasal+N reduction** (-ões → [õns], -ães → [ɐ̃ns]) is a
**Madeiran** feature and is *not* reflected in the Terceira gold, which keeps
the standard [ɐ̃w]/[õjʃ] diphthongs; it is therefore left inherited from pt-PT
and not asserted for the Azores.

**Sporadic / lexical items** (e → i extreme raising, `boi` → [bô], `pastar` →
[pɐʃˈtâ]) are lexical and left to downstream engines.

## Benchmark honesty

On the `ep_dialects` expert gold (Terceira reference, n = 29) the rebuilt spec
moves **PER 0.3058 → 0.2637**. The improvement comes from removing the previous
spec's over-applying flat `u` → [y] grapheme (which fronted *every* ⟨u⟩,
including unstressed `vulcão` → [vy…] and the article) and from restoring the
inherited standard nasal diphthongs. The São Miguel fronting itself is
neutral-or-better on this Terceira gold (it fixes `número`/`tu` and the
`muda`-type divergence is compensated), and it ships on its published grounding.

```python
from orthography2ipa import G2P
eng = G2P("pt-PT-x-acores")
eng.transcribe("número")   # ˈnymɨɾu  — stressed open /u/ → [y]
eng.transcribe("tu")       # ˈty      — the shibboleth
eng.transcribe("azul")     # ɐˈzuɫ    — blocked before coda /l/
eng.transcribe("o")        # u        — the clitic guard: never [y]
eng.transcribe("touradas") # toˈwɾadɐʃ — /ow/ preserved
```

## Sources

- **Rogers, Francis M. (1948).** *Insular Portuguese Pronunciation: Porto Santo
  and Eastern Azores.* Hispanic Review 16(1): 1–32. University of Pennsylvania
  Press. <https://doi.org/10.2307/470527>
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.
