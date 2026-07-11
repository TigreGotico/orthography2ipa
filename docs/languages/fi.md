# Finnish (`fi`)

Finnish (Uralic > Finnic) has a **near-perfectly phonemic orthography**:
one grapheme corresponds to one phoneme, phonemic length is written by
doubling the letter, and stress is fixed. It is therefore a **shallow
orthography**, and the applicable production PER ceiling is **≤ 0.15**
(see [../quality_tiers.md](../quality_tiers.md)).

## Quality tier

`fi` is a **`production`**-tier spec. It meets the bar:

- **Gold size:** the WikiPron `fin_latn_broad` gold set is scored at
  **n = 568** covered words (≥ 500 required).
- **PER:** **0.0475** at n = 568 — well below the 0.15
  shallow-orthography ceiling. (A second registered gold,
  `styletts2_phonemes`, scores 0.29, but it is `machine-generated` — a
  phonemizer's own output reused as reference — and is a "grain of salt"
  row, not the production evidence; see [../scoreboard.md](../scoreboard.md).)
- **Sources:** five published references plus Wikipedia (below).
- **Documentation:** this page.

## Phonology and what the spec models

- **Vowels:** eight qualities /ɑ e i o u y æ ø/, each with a **phonemic
  long counterpart** written as a doubled letter (`aa` → /ɑː/, `ää` →
  /æː/, …). All are encoded.
- **Diphthongs:** the 18 phonemic diphthongs (`ai ei oi ui yi äi öi au eu
  ou iu äy öy ie uo yö …`) are encoded as multigraph graphemes mapping to
  vowel sequences.
- **Consonants:** the native inventory /p t k d b ɡ f s h ʋ m n ŋ l r j/;
  **v/w** both → /ʋ/; **z** → /ts/ (loan spelling). **Geminates** written
  double (`kk pp tt ll …`) map to long consonants /kː pː …/, and `ng` →
  /ŋː/, `nk` → /ŋk/.
- **Stress is fixed word-initial** (first syllable), with secondary
  stress on later odd syllables; `default_position: 1`. Vowel doubling
  marks *quantity*, not stress. Stress is fully predictable and encoded.
- Consonant gradation and vowel harmony are morphophonological /
  distributional facts of the lexicon, noted in the spec but not
  grapheme-context rules (the orthography already spells the surface
  result).

## Known limitations (engine / notation exceptions)

Residual PER against the WikiPron gold is dominated by **notation** and a
tail of **loan material**, not encodable rule gaps:

- **Diphthong offglide notation (dominant, ~123 disagreeing tokens at
  n = 568).** WikiPron marks the second element of a diphthong as a
  *non-syllabic vowel* with the inverted-breve diacritic (e.g. gold
  `ɑi̯`, `bei̯jiŋ`), whereas this spec emits the phonemically equivalent
  plain vowel sequence (`ɑi`). Same phonemes, different convention;
  deliberately not altered.
- **Boundary gemination / `ˣ`.** A few gold forms carry the
  superscript-x "chroneme" marking *rajageminaatio* (word-final boundary
  gemination). It is a sandhi phenomenon, **not recoverable from an
  isolated word's orthography**, and is not emitted.
- **Loanword phonemes and acronyms.** Tokens with /ʃ ʒ/ (š, ž) in
  unassimilated loans, and letter-name spell-outs of acronyms (**CD** →
  *seːdeː*, **ATK** → *ɑːteːkoː*), are lexical/expansion cases the
  context-free grapheme engine does not resolve.

None of these is a missing encodable grapheme rule for standard Finnish
orthography, so no grapheme changes were made.

## Sources

- **Karlsson, F. (1999),** *Finnish: An Essential Grammar*, Routledge,
  London — pronunciation and orthography (phonemic quantity, fixed
  initial stress).
- **Suomi, K., Toivanen, J. & Ylitalo, R. (2008),** *Finnish Sound
  Structure*, Studia Humaniora Ouluensia 9, University of Oulu
  (open access) — segmental phonology, quantity, harmony, gradation.
- **Abondolo, D. (ed.) (1998),** *The Uralic Languages*, Routledge.
- **Hakulinen, L. (1979),** *The Structure and Development of the Finnish
  Language*, Indiana University Press.
- **Ladefoged, P. & Maddieson, I. (1996),** *The Sounds of the World's
  Languages*, Blackwell.
- Wikipedia:
  [Finnish language](https://en.wikipedia.org/wiki/Finnish_language),
  [Finnish phonology](https://en.wikipedia.org/wiki/Finnish_phonology)
  (quick reference, not a citable source).

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)
