# Esperanto (`eo`)

Esperanto is a **constructed international auxiliary language** (L.L.
Zamenhof, 1887) with the most transparent orthography this library
models: the writing system is **perfectly phonemic** — one letter maps
to exactly one phoneme, with no exceptions in native vocabulary. It is
therefore classified as a **shallow orthography**, and the applicable
production PER ceiling is **≤ 0.15** (see
[../quality_tiers.md](../quality_tiers.md)).

## Quality tier

`eo` is a **`production`**-tier spec. It meets the bar:

- **Gold size:** the WikiPron `epo_latn_broad` gold set is scored at
  **n = 600** covered words (≥ 500 required).
- **PER:** **0.0293** at n = 600 — far below the 0.15 shallow-orthography
  ceiling. Nearly all residual disagreement is notation, not phonology
  (see below).
- **Sources:** three published references plus Wikipedia (below).
- **Documentation:** this page.

## Phonology and what the spec models

The 28-letter alphabet has a fixed grapheme-to-sound table codified in
the *Fundamento de Esperanto* (Zamenhof 1905, Fundamenta Gramatiko,
section A). The spec encodes it directly:

- Six diacritic letters: circumflex **ĉ** /t͡ʃ/, **ĝ** /d͡ʒ/, **ĥ** /x/,
  **ĵ** /ʒ/, **ŝ** /ʃ/, and breve **ŭ** /w/.
- **c** = /t͡s/, **j** = /j/ (semivowel), **v** = /v/, **r** = /r/ (a
  trill or tap).
- Five cardinal vowels /a e i o u/, no length or quality contrast.
- **Stress is fully regular:** always on the penultimate syllable
  (Fundamenta Gramatiko, Rule 10). The spec sets `default_position: -2`
  with no exceptions, so stress is predictable and fully encoded.

Because the orthography is phonemic, no positional grapheme rules or
lexical exceptions are needed — the flat grapheme table is the complete
model.

## Known limitations (engine / notation exceptions)

The residual PER is almost entirely a **transcription-convention
difference against the WikiPron gold**, not a spec error:

- **Glide notation (dominant, ~68 of the disagreeing tokens at n = 600).**
  WikiPron transcribes the offglides written **j** and **ŭ** as
  *non-syllabic vowels* — `i̯` and `u̯` — in falling diphthongs (e.g.
  gold *alpoi̯* for **Alpoj**, *bau̯do* for **Baŭdo**). This spec emits
  the phonemically equivalent semivowel consonants **/j/** and **/w/**
  (*alpoj*, *bawdo*). Both notations denote the same phonemes; Wells
  (1978) treats **j**/**ŭ** as the semivowels /j w/. This is a notation
  choice, deliberately not "fixed", so the spec keeps the consonant
  symbols rather than the non-syllabic-vowel diacritic.
- **Foreign proper names / acronyms.** A handful of worst-case tokens are
  unassimilated loans and letter-name spellings (e.g. **Facebook**,
  **DĴ**) where the gold reflects a lexicalised or spelled-out
  pronunciation not recoverable from the orthography. These are lexical,
  not rule-expressible.

Neither class points to a missing encodable rule, so no grapheme changes
were made; the spec is already at the phonemic ceiling for this
orthography.

## Sources

- **Zamenhof, L.L. (1905),** *Fundamento de Esperanto* — Fundamenta
  Gramatiko, section A (alphabet, grapheme-to-sound table) and Rule 10
  (penultimate stress). The immutable prescriptive norm.
- **Zamenhof, L.L. (1887),** *Unua Libro (An International Language)* —
  founding document establishing the one-letter-one-sound alphabet.
- **Wells, J.C. (1978),** *Lingvistikaj aspektoj de Esperanto*,
  Universala Esperanto-Asocio, Rotterdam — phonetician's description of
  the phoneme inventory and its IPA values.
- Wikipedia: [Esperanto](https://en.wikipedia.org/wiki/Esperanto),
  [Esperanto phonology](https://en.wikipedia.org/wiki/Esperanto_phonology)
  (quick reference, not a citable source).

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)
