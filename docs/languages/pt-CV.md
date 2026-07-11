# Cape Verdean Portuguese (pt-CV) — Phonology Reference

**Code**: `pt-CV` | **Family**: Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` | **Quality tier**: skeleton
**Sources**: Freitas (2017, *RILP* 31:153–172, on the Creole — for the distinction); Undolo (2014, for the Lusophone-African pattern); Lang (2009); Veiga (2004). See the honesty note below.

## Cape Verdean *Portuguese* is not the Creole

This spec models **Cape Verdean Portuguese** (Português de Cabo Verde) —
the formal / L2 co-official language of Cape Verde. It is **distinct from
Cape Verdean Creole** (Kabuverdianu / Kriolu, ISO **`kea`**), which is the
L1 vernacular of virtually the entire population. The Creole is a
Portuguese-lexified creole formed from 16th–17th-century Portuguese and
West African languages, and already *"se diferenciava sobretudo com relação
às vogais átonas"* from its Portuguese lexifier (Freitas 2017:154). The two
share a territory and code-switch, but they are different linguistic
systems; **this page and the `pt-CV` spec are about the Portuguese, not the
Creole** (`kea` is a separate entry).

## What the spec models

Like the other Lusophone-African emerging norms, Cape Verdean Portuguese is
reported to show a **spelling-closer vocalism** and a few conservative
consonantal features:

| Feature | EP (pt-PT) | pt-CV (reported) |
|:---|:---|:---|
| Unstressed vowel reduction | strong | reduced / absent |
| Coda `s` | [ʃ]/[ʒ] | **[s]** (overrides `PT_CODA_S_HUSH`) |
| Rhotic | uvular [ʁ] | alveolar [r] |
| Stressed mid `e`/`o` | [e]/[o] | more open [ɛ]/[ɔ] |
| Intervocalic `b d g` | spirants [β ð ɣ] | plosives [b d ɡ] |
| `/l/` | velarised [ɫ] | dental [l̪] |

The spec encodes the coda-`s`, alveolar-rhotic and open-vowel deltas over
inherited pt-PT; the plosive-vs-spirant and dental-`l` features are
documented here but not separately rule-modelled (pt-PT carries no
spirantisation rule id to override).

## Honesty note (hard rule 9) — why this stays at skeleton tier

No accessible **instrumental phonology of Cape Verdean *Portuguese*** (as
opposed to the Creole) could be obtained and read for this pass. The
feature table above therefore rests on:

1. the general Lusophone-African "weaker reduction" pattern, for which the
   read primary is Undolo (2014:183–184) on **Angolan** Portuguese;
2. the read Creole primary (Freitas 2017), used only to fix the
   **Creole-vs-Portuguese distinction**;
3. the secondary Wikipedia description of Cape Verdean Portuguese
   (**flagged**, uncited in that article).

The features are consequently **provisional**. `pt-CV` is deliberately kept
at **skeleton** tier — unlike `pt-AO` and `pt-MZ`, which reach research tier
because each has a read primary for its *own* variety (Undolo 2014, Nhatuve
2019) — and must not be promoted without a read Cape-Verdean-Portuguese
source.

## Input contract

Input is standard Portuguese orthography (Acordo Ortográfico 1990). Do
**not** feed Kabuverdianu (Creole) orthography (ALUPEC) here — that is a
different language and belongs to the `kea` entry.
