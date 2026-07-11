# Macau Portuguese (pt-MO) — Phonology Reference

**Code**: `pt-MO` | **Family**: Indo-European > Romance | **Script**: Latin (alphabet)
**Quality tier**: skeleton (deliberately) | **Parent**: `pt-PT`

Macau Portuguese (*Português de Macau*) is a co-official language of the Macau
SAR (People's Republic of China) alongside Chinese: a small L1/heritage
community plus an L2 official register used in legislation, the courts and
public administration. Use has declined since the 1999 handover. It is the
**most "European"** of the Asian Portuguese varieties, "closely follow[ing]
the standard European dialect in pronunciation and vocabulary."

## Not a creole — Patuá is a separate language

The **Macanese creole** — *Patuá*, also *maquista* or the historical
*"dialecto macaense"* — is a **distinct Portuguese-based contact language**
with Cantonese, Malay, Kristang (Malacca), Konkani and Sinhala elements, now
nearly extinct. It must **not** be conflated with the modern Portuguese of
Macau modelled here.

- Batalha, G. N. (1959). *Estado actual do dialecto macaense*. Revista de
  Filologia Portuguesa 9:177–213 — describes the **creole**. (reference
  verified via Albuquerque 2010:283, which cites Batalha 1959:181 for creole
  prosody).
- Pinharanda-Nunes, M. (2011). *Estudo da Expressão Morfo-Sintáctica das
  Categorias de Tempo, Modo e Aspecto em Maquista*. PhD, University of Macau —
  the first doctoral thesis on Patuá grammar (**creole**, not the Portuguese
  variety).

## Why this spec stays at `skeleton` (honesty note)

**The literature on Macau Portuguese phonology is thin.** No peer-reviewed
phonological description of Macau *Portuguese* (as opposed to the *Patuá*
creole) could be obtained and read for this spec. The specialists who publish
on Macau's linguistics (Pinharanda-Nunes, Batalha) describe the **creole**.

The **only** phonological description actually read is the English Wikipedia
article *Macanese Portuguese*, whose Phonology section carries **no
citations** — used here strictly as a **flagged secondary source**. On that
basis the reported distinctive traits are:

1. The variety "nowadays closely follows the standard European dialect in
   pronunciation and vocabulary" → the inherited `pt-PT` maps (uvular [ʁ], EP
   vowel reduction, coda *chiado*) are kept as the modelled norm.
2. **[ʒ] devoiced to [ʃ]** — "a trait almost unique to Macau".
3. **Final infinitive /ɾ/ dropped** by L2 speakers (comer, dormir) while /ɾ/
   is kept elsewhere (mar) — paralleling African and most Brazilian
   Portuguese.
4. Some **Cantonese-influenced (partly non-rhotic)** patterns among L2
   speakers, absent in speakers with higher education in Portuguese.

Traits 2–4 are documented **only** by the uncited secondary source, are
L2/variable, and (for 3) involve a **deletion** the engine's allophone layer
does not express. Rather than fabricate rules on an uncitable basis, they are
**recorded here and in the spec `notes` but NOT encoded**. Per the repo's
research-grounding rule, `pt-MO` is promoted to `research` only once a citable
phonological description of Macau Portuguese is obtained and read.

## What the spec does model

`pt-MO` inherits the full `pt-PT` maps (graphemes, positional reduction, coda
allophony, uvular rhotic) — the "closely follows EP" baseline — and adds only
the inherited-uvular rhotic `allophones` already present. `mar` → [ˈmaʁ],
`bate` → [ˈbatɨ], exactly like `pt-PT`.

## Sources

- Batalha, G. N. (1959). *Estado actual do dialecto macaense*. Revista de
  Filologia Portuguesa 9:177–213. (the **creole**)
- Pinharanda-Nunes, M. (2011). PhD thesis on Maquista TMA. U. Macau. (the
  **creole**)
- English Wikipedia, *Macanese Portuguese* — **flagged secondary**, Phonology
  section uncited; the only phonological description available for the
  Portuguese variety.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-TL](pt-TL.md), [romance](romance.md)*
