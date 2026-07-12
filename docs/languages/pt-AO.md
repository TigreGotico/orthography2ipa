# Angolan Portuguese (pt-AO) — Phonology Reference

**Code**: `pt-AO` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Parent**: `pt-PT` | **Quality tier**: research
**Sources**: Undolo (2014, *Revista de Filología Románica* 31(2):181–187); Chavagne (2005, PhD, Lyon 2); Inverno (2011, PhD, Coimbra); Mateus & d'Andrade (2000)

Angolan Portuguese (Português de Angola, **PA**) is the emerging L2 /
second-norm variety of educated Angolan speakers. It is **not a creole**:
Portuguese has been the sole official language since 1975, is the mother
tongue of a growing urban minority, and the second language of most
Angolans, in contact with dozens of Bantu languages (Umbundu, Kimbundu,
Kikongo, …). Modelling it means *removing* several inherited European
Portuguese (EP) reduction processes, not merely adding to them.

## What the spec models (and the source for each)

The headline feature is a **spelling-closer vocalism**: PA lacks the strong
EP unstressed-vowel reduction, so its written vowels stay close to their
full quality. Undolo (2014) is an explicit contrastive description of the
educated-PA vowel system; the delta is encoded by overriding the inherited
pt-PT positional vowels.

| Feature | EP (pt-PT) | pt-AO | Source |
|:---|:---|:---|:---|
| Final unstressed `a` | [ɐ] (`casa` [ˈkazɐ]) | **[a]** (`casa` [ˈkaza]) | Undolo 2014:183 |
| Pretonic `e` | [ɨ] / centralised | **[e]** (`presidente` …[e]…) | Undolo 2014:183 |
| Pretonic `o` | [u] (`morar` [muˈɾaɾ]) | **[o]** (`morar` [moˈɾaɾ]) | Undolo 2014:184 |
| Final unstressed `e` | [ɨ] | [ɨ] (retained) | Undolo 2014:183 |
| Coda `s` | [ʃ]/[ʒ] (chiado) | **[s]** (alveolar) | overrides `PT_CODA_S_HUSH` |

Undolo (2014:184) summarises the vowel system as one that *"não sofre
elevação e centralização em posição átona"* and in which [ɨ] *"restringe-se
à posição átona final"*. Chavagne (2005:64) independently reports that in
Angolan Portuguese *"les voyelles atones gardent le timbre des voyelles
toniques"* — unstressed syllables keep the timbre of the stressed vowels —
with a much smaller tonic/atonic intensity contrast than EP. Undolo
(2014:186) attributes the fuller vocalism to the simple, open-nucleus
syllable structure of the Angolan Bantu substrate.

A tendency to **open stressed mid vowels** (favouring [ɛ], [ɔ] over [e],
[o] — Undolo 2014:183–184, e.g. [beˈlɛza]) is documented but variable and
lexical; it is modelled only as candidate ordering in `nucleus_stressed`,
not applied categorically.

## Limits and honesty notes

- The extra nasal contrast Undolo reports (PA central-open [ã] vs EP [ɐ̃],
  2014:184) and fine rhotic variation are left largely to downstream
  engines; only the vowel and coda-sibilant deltas are modelled here.
- Inverno (2011) is a **morphosyntactic** thesis on the restructured
  vernacular of Dundo; it is cited for contact framing only, not for the
  vowel model.

## Input contract

Input is standard Portuguese orthography (Acordo Ortográfico 1990). The
spec relies on written accents for stress and does not expect any special
pre-processing.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-PT](pt-PT.md), [pt-MZ](pt-MZ.md), [pt-CV](pt-CV.md)*
