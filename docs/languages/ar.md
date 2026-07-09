# Modern Standard Arabic (ar) — Phonology Reference

**Code**: `ar` | **Family**: Semitic | **Script**: Arabic (abjad)
**Quality tier**: research | **Sources**: Watson (2002), Sun and moon letters (Wikipedia)

---

## Overview

`ar` (MSA) inherits its grapheme/allophone inventory from Classical Arabic (`arb`) via
`graphemes_base`/`allophones_base`, with one MSA-specific override: ض is transcribed
[dˤ] (emphatic alveolar stop) rather than the Classical lateral-fricative [ɮˤ] that
`arb.json` retains — MSA has merged ض onto the plosive series (Watson 2002).

`sandhi_rules` is **not** inherited through `graphemes_base`/`allophones_base` (only
`graphemes`/`allophones`/`positional_graphemes` are), so this spec re-declares the two
sandhi rules it needs from `arb`: sun-letter assimilation of the definite article, and
hamzat-al-wasl elision.

## Input contract / known limitation: diacritics

This spec assumes fully-diacritized (fully tashkeel-marked) input. Standard written MSA
omits short-vowel diacritics (fatḥa/ḍamma/kasra/sukūn/shadda/tanwīn) almost everywhere
outside the Quran, children's books, and pedagogical material. Undiacritized input is
**not** disambiguated by this spec — there is no morphological/statistical
diacritic-restoration step — and will transcribe incorrectly or incompletely wherever
short vowels or gemination are orthographically absent. Gemination (shadda, ّ) is only
encoded when explicitly marked in the input, via the inherited ّ → ː mapping from `arb`.

## Sun-letter assimilation (`MSA_SUN_ASSIMILATION`) — practical scope

The rule itself is linguistically correct: the definite article's lām (ل) assimilates to
a following coronal "sun letter" (ت ث د ذ ر ز س ش ص ض ط ظ ل ن → t θ d ð r z s ʃ sˤ dˤ tˤ
ðˤ l n), e.g. الشمس *aš-šams* "the sun", not *al-šams*. Before a "moon letter" (labials,
velars/uvulars, pharyngeals, glottal, glides) no assimilation occurs, e.g. القمر
*al-qamar* "the moon".

**However, this rule does not currently fire on ordinary Arabic text as it is normally
written.** `SandhiEngine.apply()` (`orthography2ipa/sandhi.py`) only applies sandhi rules
*between whitespace-separated tokens* — it does not operate within a single token. In
standard Arabic orthography, the definite article ال- is written **attached** to the
word it modifies, as a single unbroken token (الشمس is one word, not `ال` + `شمس`). Since
`MSA_SUN_ASSIMILATION`'s `left_context`/`right_context` only match across a token
boundary, it never gets the chance to fire on input written the normal way:

```python
transcribe("الشمس", "ar")   # -> "alʃms"   (lām NOT assimilated — rule did not fire)
transcribe("القمر", "ar")   # -> "alqmr"   (correct, but only because moon letters
                              #              never assimilate anyway — not evidence
                              #              the rule engine is working here)
transcribe("ال شمس", "ar")  # -> assimilates correctly, because the article is
                              #    already segmented as its own whitespace token
```

In other words, `MSA_SUN_ASSIMILATION` is validated and correct for input where the
definite article has already been segmented as a separate token — for example
morphologically pre-segmented corpora or pipelines that split clitics before this
library sees them. It is **not** yet applicable to raw, normally-written Arabic running
text, where the article/host-word boundary is never expressed as whitespace.

This is a known limitation of the sandhi engine (word-boundary-only application), not a
defect in the rule's phonology. Making sandhi article-boundary-aware within a single
orthographic word is a real engine enhancement tracked as future work; the rule is kept
in place now because it is correct and is the foundation that enhancement will build on.

A related, smaller point: the rule's `right_context` character class explicitly lists the
emphatic sun letters (ص ض ط ظ → sˤ dˤ tˤ ðˤ) alongside their base-coronal counterparts.
This explicit listing is for clarity/completeness of the rule definition — the
base-coronal codepoints (t, d, s, ð) were already present in the class and already
matched these emphatics on their leading codepoint, so this was not closing a real
assimilation gap.

Separately, because the engine can only delete the lām on the left token (it cannot copy
the right word's onset into the left token to render true gemination), even when the rule
does fire it realizes the sun-letter case as elision (*a-šams*) rather than a doubled
consonant (*aʃ-ʃams*) — a second, independent engine limitation from the tokenization one
above.

## Hamzat al-wasl (`MSA_HAMZAT_WASL`)

Connective hamza (همزة الوصل) on ال and a closed set of verb/noun forms is elided after a
preceding vowel in connected speech: *fī al-bayt* → *fi l-bayt*. Only the "wasl" hamza
(written as a bare alif, not a hamza-bearing alif أ/إ) undergoes this; the engine cannot
distinguish the two orthographically without diacritics, so this rule is scoped to the
definite-article context inherited from Classical Arabic (`arb`).

## No stress block

MSA word stress is quantity-sensitive (driven by syllable weight, not orthographic
vowel-length alone) and highly register/dialect-variable in connected speech, so it is
not reliably orthography-predictable. This exempts the spec from the research-tier
stress requirement per `docs/quality_tiers.md`.

## Gold benchmark

CUNY-CL/wikipron `ara_arab_broad.tsv` (Wiktionary-sourced broad IPA transcriptions,
community-curated, ~17.5k pairs), registered as the `ar` entry of the `wikipron` dataset
in `scripts/benchmark.py`, matching the precedent used for gl/es/pt in this project.

## References

- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press.
- Wikipedia: [Sun and moon letters](https://en.wikipedia.org/wiki/Sun_and_moon_letters)
- Wikipedia: [Standard Arabic phonology](https://en.wikipedia.org/wiki/Standard_Arabic_phonology)
