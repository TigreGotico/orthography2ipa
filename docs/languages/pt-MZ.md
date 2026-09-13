# Mozambican Portuguese (pt-MZ): Phonology Reference

**Code**: `pt-MZ` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet) **Parent**: `pt-PT` | **Quality tier**: research **Sources**: Nhatuve (2019, *Revista de Letras* 21(32):130–144). Gonçalves (2010, *A Génese do Português de Moçambique*) via Barbosa (2011, review, *ELUP* 6(1):201–204). Stroud & Gonçalves (1997)

Mozambican Portuguese (Português de Moçambique, **PM**) is the emerging **non-native / L2 variety**. Perpétua Gonçalves describes it as arising from children with Bantu mother tongues acquiring Portuguese as a second language (Barbosa 2011:202, reviewing Gonçalves 2010:7). It is **not a creole**. Only ~6.5 % of Mozambicans have Portuguese as an L1. The majority learn a Bantu language first (Barbosa 2011:202). The spec models the prestige **Maputo** educated variety.

## What the spec models (and the source for each)

| Feature | EP (pt-PT) | pt-MZ | Source |
|:---|:---|:---|:---|
| Strong rhotic `r`/`rr` | uvular [ʁ] | **alveolar trill [r]~[R]** | Nhatuve 2019:136–137 |
| Coda `s` | [ʃ]/[ʒ] (chiado) | **[s]** (alveolar) | overrides `PT_CODA_S_HUSH` |
| Unstressed vowels | strong reduction ([ɨ], [ɐ], [u]) | weaker reduction; unstressed `e` tends to stay [e] | Gonçalves 2010 (framing) |

Nhatuve (2019:136) reports that in Maputo oral Portuguese the onset `<r>` is realised as an alveolar multiple vibrant **[R]**, regardless of the surrounding vowel. The /R/–/ɾ/ opposition tends to disappear (*"desaparece o fonema /r/"*). This reflects a calque of the changana/ronga (Bantu) system, which has only [R]. Word-final coda `<r>` frequently takes an epenthetic vowel by **paragoge** ([falaɾ] → [falarɨ], Nhatuve 2019:136). Gonçalves (2010, ch. 2 "propriedades fónicas") and Barbosa (2011:203) characterise PM's educated phonic system as an emerging norm with weaker unstressed-vowel reduction than EP.

## Limits and honesty notes (hard rule 9)

- **Vowel-reduction figures are modelled by analogy.** The direct instrumental vowel study read for this pass is Undolo (2014) for *Angolan* Portuguese. The PM unstressed-vowel values follow the shared Lusophone-African "weaker reduction" pattern that Gonçalves describes for PM in general terms, not a read PM instrumental study. Treat them as provisional.
- **`<lh>` /ʎ/ voiced aspiration** in Maputo speech (a Bantu calque, Nhatuve 2019:137) is documented but **not modelled**, a narrow allophonic detail below the grapheme layer.
- **Coda `/l/` → [w]** vocalisation and Bantu pitch effects are **not confirmed** by the primaries read here. They are tentative and should be re-sourced before any production promotion.

## Input contract

Input is standard Portuguese orthography (Acordo Ortográfico 1990). Written accents carry stress. No special pre-processing is expected.

---
[← Cape Verdean Portuguese](pt-CV.md) · [Home](../index.md) · [Barranquenho →](ext-PT-x-barrancos.md)
