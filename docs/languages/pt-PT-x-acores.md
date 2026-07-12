# Azorean European Portuguese (pt-PT-x-acores) — Phonology Reference

**Code**: `pt-PT-x-acores` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
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

### 3. External `/s/`-sandhi before a vowel → `[ʒ]` (shared with the Algarve)

São Miguel shares the Algarvean `/ʒ/`-for-`/z/` external sandhi: a word-final
/s/ before a vowel-initial following word surfaces as the **post-alveolar
`[ʒ]`** rather than the standard `[z]` — *estás a ver* → **[eˈʃtaʒ ˈɐ ˈvɛɾ]**
(the "quijentrar" / "Todojos" pronunciation). Unlike the Algarve — which
generalises `[ʒ]` to *all* word-final positions — São Miguel restricts this
palatal to the **prevocalic** context, so before a *voiceless* consonant or in
isolation the sibilant stays `[ʃ]` (`estás` → [eˈʃtaʃ], `estás só` → [eˈʃtaʃ
ˈsɔ]). Modelled by re-declaring `PT_FINAL_S_PREVOCALIC_VOICE` (OVERLAY_BY_ID)
with transform `ʒ` over the inherited base `[z]`. Before a **voiced** consonant
the inherited general-EP `PT_CODA_S_VOICING` still voices it to `[ʒ]`
(`estás bem` → [eˈʃtaʒ ˈbɛm]).

**Sourcing.** Described natively by *Portuguese With Leo*, "The 8 accents"
([video](https://www.youtube.com/watch?v=pitj0XxYO7I); native-speaker /
popular-linguistics, **not** academic), which reports the shared
Algarvean–Azorean *J* ("quijentrar", "Todojos", "Éjunúmerúm" for *és o número
um*), with Lisbon and the North keeping `[z]` and Coimbra variable. It sits
within the documented insular final-sibilant behaviour (Rogers 1948), but a
page-pinned academic source for the São-Miguel prevocalic `[ʒ]` *specifically*
was not located — the standard/Lisbon literature gives `[z]` (Mateus & d'Andrade
2000: ch.2). Stated honestly rather than over-cited.

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

Dark coda /l/ → [ɫ] (`sol` → ˈsɔɫ), the coda-sibilant *chiado* /s z/ → [ʃ ʒ]
and extreme unstressed vowel reduction are inherited from the parent and not
restated here. The one sandhi delta is the prevocalic `/s/` → `[ʒ]` override
(feature 3 above); the pre-consonantal coda-s voicing is inherited unchanged.

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

On the `ep_dialects` expert gold (Terceira reference, n = 29) the spec scores
**PER 0.2637**. The `u` → [y] fronting is restricted to stressed open /u/ rather
than applied flat to every ⟨u⟩ (so unstressed `vulcão` and the article keep [u]),
and the standard nasal diphthongs are inherited from pt-PT. The São Miguel
fronting is neutral-or-better on this Terceira gold (it fixes `número`/`tu` and
the `muda`-type divergence is compensated), and it ships on its published
grounding.

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

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-madeira](pt-PT-x-madeira.md), [pt-PT-x-lisbon](pt-PT-x-lisbon.md)*
