# Esperanto (`eo`)

**Code**: `eo` | **Family**: Constructed language | **Script**: Latin (alphabet) | **Quality tier**: production

Esperanto is a constructed international language (L. L. Zamenhof, *Unua Libro*, 1887). It was designed for a regular relation between letters and sounds: one letter is one sound. The alphabet has 28 Latin letters, six of them with a diacritic (ĉ ĝ ĥ ĵ ŝ ŭ). There are no silent letters and no readings that depend on context.

## Orthographic depth and production threshold

Esperanto has a shallow (phonemic) orthography, so the shallow threshold of 0.15 PER applies (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)). It is the limiting case of a shallow orthography, because it was designed to be phonemic. So the remaining error measures noise in the harness and the gold, and gaps in the spec, not irregular spelling.

## Phonology

The language has 23 consonants and the five vowels /a e i o u/. The spec maps each letter to one phoneme. The semivowels are ⟨j⟩ /j/ and ⟨ŭ⟩ /w/, and they form the six falling diphthongs aŭ, eŭ, aj, ej, oj and uj. The spec has no diphthong graphemes, so it writes each diphthong as a vowel and a glide.

Stress is always on the penultimate syllable. The spec states this as a `stress` block with `default_position: -2`. It gives `espeˈranto` for `Esperanto` and `dʒarˈdeno` for `ĝardeno`.

The norm requires no vowel reduction and no assimilation. The spec transcribes the citation pronunciation of the Fundamento.

## Benchmark

Two gold rows score the spec. For the figures, see the [scoreboard](../evaluation/generated/scoreboard.md). The `wikipron` row is crowd-scraped and can qualify a promotion. The `ipadict` row is the output of a rule script, so it shows agreement, not proof.

## Known limitations

The engine counts two adjacent vowels in hiatus as one syllable when it places stress. So stress falls one syllable too early in words such as `radio`, `kafeo` and `familio`. The spec gives `ˈradio`, `ˈkafeo` and `faˈmilio`, where the penultimate rule gives raˈdio, kaˈfeo and famiˈlio.

WikiPron entries transcribe proper names and recent loans with narrow detail that varies by editor, for example /x/ or /h/ for ⟨ĥ⟩ in loans. The spec does not follow these variants.

The spec encodes no register variation, because none is codified.

## Sources

- Zamenhof, L. L. (1887). *Unua Libro* (An International Language).
- [Esperanto phonology](https://en.wikipedia.org/wiki/Esperanto_phonology) (Wikipedia). An accessible overview, kept on purpose next to the primary source.

---
[← Yoruba](yo.md) · [Home](../index.md)
