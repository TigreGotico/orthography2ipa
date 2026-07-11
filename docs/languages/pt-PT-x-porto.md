# Portuense / Northern European Portuguese (pt-PT-x-porto) — Phonology Reference

**Code**: `pt-PT-x-porto` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` (standard, Lisbon-type EP) | **Quality tier**: research
**Sources**: Cintra (1971, *Boletim de Filologia* 22:81–116), Segura (2013,
*Gramática do Português* vol. I), Mateus & d'Andrade (2000)

`pt-PT-x-porto` models the European Portuguese of **Porto, Greater Porto and
the Baixo-Minho / Douro-Litoral zone** — Cintra's *Baixo-Minho e
Douro-Litoral* variety, one of the most idiosyncratic (Cintra's "forte
personalidade linguística") sub-varieties of Northern EP. It is a **delta**
spec: it inherits the whole standard pt-PT system (unstressed vowel reduction,
dark coda /l/, coda-sibilant *chiado*, sandhi) via `graphemes_base` /
`allophones_base` and OVERLAY_BY_ID `allophone_rules`, and declares only the
Porto-specific diagnostic features.

## Diagnostic features modelled

The three features are drawn from Cintra's (1971) list of maximally diagnostic
phonetic traits for the Galician-Portuguese dialect space.

### 1. Betacism — /v/ ~ /b/ merger (Cintra feature 1)

The phonological opposition between /v/ and /b/ is lost; both collapse into a
single phoneme /b/, realised **[b] in all positions**. Cintra (1971):
*"o desaparecimento da oposição fonológica entre os fonemas /v/ e /b/ e a sua
fusão num fonema único /b/"*. This is the primary trait separating Northern
from Central-Southern EP.

Modelled as the post-lexical `allophone_rules` entry **`PT_PORTO_BETACISM`**
(`/v/ → [b]`, unconditional) rather than a grapheme substitution, so the
merger applies uniformly however the phoneme /v/ arises from the inherited
grapheme map.

| Word | pt-PT | pt-PT-x-porto |
|:---|:---|:---|
| vinho | ˈviɲu | **ˈbiɲu** |
| vaca | ˈvakɐ | **ˈbakɐ** |
| estava | eˈʃtavɐ | **eˈʃtabɐ** |

### 2. Tonic-closed-vowel diphthongisation (Cintra's defining Porto marker)

Cintra (1971) isolates this as *the* defining feature of the region:
*"a ditongação, tão caracterizadora, das vogais tónicas fechadas [e] em [je],
[o] em [wo] (por vezes [wɔ])"* — a **stressed close-mid vowel** becomes a
rising diphthong. Segura (2013) independently names diphthongisation of
stressed vowels the characteristic trait of the north-western variety.

Modelled as two `allophone_rules`, each gated to a **stressed nucleus** and to
the **close** mid vowel only:

| id | Rule | Example |
|:---|:---|:---|
| `PT_PORTO_DIPHTHONGISE_E` | stressed close [e] → [je] | mês → **ˈmjeʃ**, ele → **ˈjelɨ** |
| `PT_PORTO_DIPHTHONGISE_O` | stressed close [o] → [wo] | avô → **ɐˈbwo**, pôr → **ˈpwoɾ** |

Genuinely **open** tonic vowels [ɛ]/[ɔ] do **not** diphthongise (Cintra
specifies *fechadas*, close): `pé` → ˈpɛ, `café` → kɐˈfɛ, `avó` → ɐˈbɔ,
`só` → ˈsɔ all stay monophthongal.

### 3. Diphthong preservation (Cintra feature 4)

Northern EP keeps the historical falling diphthongs where Lisbon
monophthongises or lowers them: ⟨ou⟩ → [ow] (Lisbon [o]) and ⟨ei⟩ → [ej]
(Lisbon [ɐj]). Modelled as inherited-map grapheme deltas (`ou`→[ow],
`ei`→[ej]): `ouro` → ˈowɾu, `leite` → ˈlejtɨ, `primeiro` → pɾiˈmejɾu.

## Inherited from pt-PT (unchanged)

Dark coda /l/ → [ɫ] (`sol` → ˈsɔɫ, `alto` → ˈɐɫtu), the coda-sibilant *chiado*
/s z/ → [ʃ ʒ] (`véspera` → …ʃp…), extreme unstressed vowel reduction, and the
coda-s sandhi are inherited from the parent and not restated here. In
particular, the **external /s/-sandhi before a vowel keeps the standard
alveolar [z]** in the North (`estás a ver` → [eˈʃtaz ˈɐ ˈbɛɾ], with the
inherited betacism v→b): the palatal [ʒ] realisation is a Southern/Azorean
feature, not a Northern one (see [pt-PT](pt-PT.md), [pt-PT-x-algarve](pt-PT-x-algarve.md)).

## Known limits (documented, not faked)

**Apico-alveolar sibilant.** Cintra's *primary* North/South isogloss — the
Northern apico-alveolar [s̺ z̺] vs the standard predorsodental [s̪ z̪] — is an
**articulatory place distinction invisible to a phoneme-level,
orthography-blind engine**. It is his single most diagnostic feature yet the
least simulable at this level. It is left only as a documentary surface variant
in `allophones` (ʃ→[ʃ, ʂ], ʒ→[ʒ, ʐ]) and is **not** asserted as the default
realisation.

**Open/close vowel selection.** The diphthongisation rules are correctly gated
to the close vowels [e]/[o]. Whether a spelling-unmarked stressed ⟨e⟩/⟨o⟩ is
open or close is **lexical, not predictable from orthography**, and the
inherited pt-PT map defaults to the *open* allophone. So words whose underlying
vowel is close but which the base engine transcribes open — including the
emblematic `Porto` (→ ˈpɔɾtu, dialectally [ˈpwoɾtu]) and `cedo` (→ ˈsɛdu) — are
**not reached** by the diphthongisation rule. Widening the rule to the open
vowels is rejected because it would wrongly diphthongise genuinely open tonic
vowels (café, avó, só). Reaching these lexically-close words would require a
pronunciation lexicon (Workstream E3), out of scope for a pure rule delta.

**Sub-lexical Porto features** (sporadic l-palatalisation `quilo`→*quilho*,
`Filipa`→[fʎipɐ]) are lexical and not modelled.

## Benchmark honesty

The `ep_dialects` `pt-PT-x-north` expert gold was annotated for betacism and
diphthong preservation but **not** for tonic-vowel diphthongisation. Because
that gold is scored at sentence level (only the utterance-final word carries
stress), the stress-gated diphthongisation rules almost never fire on it, so
they leave both the `ep_dialects` (PER 0.2342) and `clup_dialect` (PER 0.4895)
rows unchanged — a source-correct rule that neither helps nor harms the
available golds. Per the honesty gate (B8 precedent) the rules ship on their
published grounding regardless of gold reward.

```python
from orthography2ipa import G2P
eng = G2P("pt-PT-x-porto")
eng.transcribe_word("vinho")   # ˈbiɲu   — betacism
eng.transcribe_word("mês")     # ˈmjeʃ   — [e] → [je]
eng.transcribe_word("avô")     # ɐˈbwo   — [o] → [wo]
eng.transcribe_word("café")    # kɐˈfɛ   — open [ɛ], no diphthong
```

## Sources

- **Cintra, L. F. Lindley (1971).** *Nova proposta de classificação dos
  dialectos galego-portugueses.* Boletim de Filologia (Centro de Estudos
  Filológicos, Lisboa) 22: 81–116. (Republished in *Estudos de Dialectologia
  Portuguesa*, Sá da Costa, 1983, pp. 117–163.)
- **Segura, Luísa (2013).** *Variedades dialetais do português europeu.* In
  E. B. P. Raposo et al. (eds.), *Gramática do Português*, vol. I, Fundação
  Calouste Gulbenkian, Lisboa, pp. 85–142.
- **Mateus, M. H. M. & d'Andrade, E. (2000).** *The Phonology of Portuguese.*
  Oxford University Press.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-PT-x-lisbon](pt-PT-x-lisbon.md), [pt-PT-x-minho](pt-PT-x-minho.md)*
