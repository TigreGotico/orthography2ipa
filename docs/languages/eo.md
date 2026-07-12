# Esperanto — `eo`

Constructed international language (L. L. Zamenhof, *Unua Libro*, 1887).
Designed for perfect grapheme↔phoneme regularity: one letter = one sound,
28-letter Latin alphabet with six diacritic letters (ĉ ĝ ĥ ĵ ŝ ŭ), no
silent letters, no contextual readings.

## Orthographic depth and production threshold

**Shallow (phonemic) orthography — the ≤ 0.15 PER production threshold
applies** (see [quality tiers](../quality_tiers.md)). Esperanto is the
limiting case of shallowness: its orthography was *designed* phonemic, so
any residual PER measures harness/gold noise and spec gaps, not
orthographic irregularity.

## Phonology (as encoded)

- 23 consonants, 5 vowels /a e i o u/, 6 falling diphthongs written with
  ⟨ŭ⟩/⟨j⟩ (aŭ, eŭ, aj, ej, oj, uj).
- Stress is fixed on the **penultimate syllable**, with no exceptions —
  encoded as a `stress` block (`default_position: -2` semantics).
- No vowel reduction, no assimilation mandated by the norm; the spec
  deliberately transcribes the citation (Fundamento) pronunciation.

## Benchmark (full gold set, no cap)

| dataset | provenance | n | PER |
|---|---|---:|---:|
| `wikipron` | crowd-scraped | 41 245 | **0.0569** |
| `ipadict` | machine-generated (rule script) | 23 245 | 0.0338 |

The qualifying row is `wikipron` (crowd-scraped tier — gate-eligible);
the `ipadict` row is rule-script output and is reported as agreement,
not proof. Both sit far below the 0.15 shallow threshold.

## Known limitations

- WikiPron entries transcribe proper names and recent borrowings with
  editor-specific narrowness (e.g. /x/ vs /h/ for ⟨ĥ⟩ in loans); the
  residual PER is dominated by such variant disagreements.
- The spec encodes no register variation (there is none codified).

## Sources

- Zamenhof, L. L. (1887). *Unua Libro* (An International Language).
- [Esperanto phonology](https://en.wikipedia.org/wiki/Esperanto_phonology)
  (Wikipedia — accessible overview; retained deliberately alongside the
  primary source).
