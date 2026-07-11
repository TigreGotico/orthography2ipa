# Modern Standard Arabic (ar) — Phonology Reference

**Code**: `ar` | **Family**: Semitic | **Script**: Arabic (abjad)
**Quality tier**: research | **Sources**: Watson (2002), Sun and moon letters (Wikipedia)

---

## Overview

`ar` (MSA) inherits its grapheme/allophone inventory from Classical Arabic (`arb`) via
`graphemes_base`/`allophones_base`, with one MSA-specific override: ض is transcribed
[dˤ] (emphatic alveolar stop) rather than the Classical lateral-fricative [ɮˤ] that
`arb.json` retains — MSA has merged ض onto the plosive series (Watson 2002).

`sandhi_rules` is inherited via id-keyed overlay from `arb`: `ar` declares no
`sandhi_rules` of its own, so it resolves to `arb`'s rules unchanged — sun-letter
assimilation of the definite article (`AR_SUN_ASSIMILATION`), hamzat-al-wasl elision
(`AR_HAMZAT_WASL`), and pausal tanwīn dropping (`AR_PAUSAL_TANWIN`).

## Input contract / known limitation: diacritics

This spec assumes fully-diacritized (fully tashkeel-marked) input. Standard written MSA
omits short-vowel diacritics (fatḥa/ḍamma/kasra/sukūn/shadda/tanwīn) almost everywhere
outside the Quran, children's books, and pedagogical material. Undiacritized input is
**not** disambiguated by this spec — there is no morphological/statistical
diacritic-restoration step — and will transcribe incorrectly or incompletely wherever
short vowels or gemination are orthographically absent. Gemination (shadda, ّ) is only
encoded when explicitly marked in the input, via the inherited ّ → ː mapping from `arb`.

## Sun-letter assimilation (`AR_SUN_ASSIMILATION`, inherited from `arb`) — practical scope

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
`AR_SUN_ASSIMILATION`'s `left_context`/`right_context` only match across a token
boundary, it never gets the chance to fire on input written the normal way:

```python
transcribe("الشمس", "ar")   # -> "alʃms"   (lām NOT assimilated — rule did not fire)
transcribe("القمر", "ar")   # -> "alqmr"   (correct, but only because moon letters
                              #              never assimilate anyway — not evidence
                              #              the rule engine is working here)
transcribe("ال شمس", "ar")  # -> assimilates correctly, because the article is
                              #    already segmented as its own whitespace token
```

In other words, `AR_SUN_ASSIMILATION` is validated and correct for input where the
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

## Hamzat al-wasl (`AR_HAMZAT_WASL`, inherited from `arb`)

Connective hamza (همزة الوصل) on ال and a closed set of verb/noun forms is elided after a
preceding vowel in connected speech: *fī al-bayt* → *fi l-bayt*. Only the "wasl" hamza
(written as a bare alif, not a hamza-bearing alif أ/إ) undergoes this; the engine cannot
distinguish the two orthographically without diacritics, so this rule is scoped to the
definite-article context defined in Classical Arabic (`arb`) and inherited by `ar`
unchanged.

## Emphatic (pharyngealization) spreading

MSA is now the first Arabic spec to model the **post-lexical** map (phoneme → surface
allophone) via `allophone_rules` (the [allophony](../allophony.md) layer). Four rules
(`AR_EMPH_BACK_A_AFTER`, `AR_EMPH_BACK_A_BEFORE`, `AR_EMPH_BACK_AA_AFTER`,
`AR_EMPH_BACK_AA_BEFORE`) back the low vowels /a/ and /aː/ to [ɑ] / [ɑː] when they stand
next to an emphatic (pharyngealized) consonant /tˤ dˤ sˤ ðˤ/ (Watson 2002, ch. *Emphasis*,
pp. 267–286; Ryding 2005 §2). Emphasis spreads bidirectionally, so the condition is
"preceded_by_phoneme **or** followed_by_phoneme" an emphatic:

```python
transcribe("صَابَ", "ar")   # -> "sˤɑːba"  (/aː/ → [ɑː] after /sˤ/)
transcribe("بَطَل", "ar")   # -> "bɑtˤɑl"  (/a/ → [ɑ] on both sides of /tˤ/)
transcribe("قَلْب", "ar")   # -> "qalb"    (no emphatic → /a/ unchanged)
```

**Honesty note on the gold.** The registered `ar wikipron` gold is a *broad* Wiktionary
transcription that writes the backed vowel as plain /a/, so it cannot reward the (correct)
narrow [ɑ] realisation. Activating the rule therefore adds a small, uniform penalty
(PER 0.2551 → 0.2566, **+0.0015**, well below the 0.005 benchmark-regression epsilon; the
bootstrap CIs overlap). This is the same broad-gold limitation documented for the Catalan
nasal-assimilation pilot (see [allophony](../allophony.md)); the rule is retained because
it is linguistically correct and the movement is within measurement noise. The spreading
here is modeled as *local* (immediate-neighbour) backing; true long-domain emphasis
harmony across a whole phonological word is left as future work.

## No stress block

MSA word stress is quantity-sensitive (driven by syllable weight, not orthographic
vowel-length alone) and highly register/dialect-variable in connected speech, so it is
not reliably orthography-predictable. This exempts the spec from the research-tier
stress requirement per `docs/quality_tiers.md`.

## Gold benchmark

CUNY-CL/wikipron `ara_arab_broad.tsv` (Wiktionary-sourced broad IPA transcriptions,
community-curated, ~17.5k pairs), registered as the `ar` entry of the `wikipron` dataset
in `scripts/benchmark.py`, matching the precedent used for gl/es/pt in this project.

## Egyptian Arabic — Cairene (`ar-EG`)

Cairene (research tier) inherits the Eastern/Mashriqi base (`ar-x-mashriqi`) and expresses
its signature reflexes in the **pre-lexical** grapheme map: ج jīm → /ɡ/ (the marquee
Cairene feature, جَمَل → [ɡamal]); ق qāf → /ʔ/ in inherited vocabulary (قَلْب → [ʔalb]), with
/q/ in learned borrowings and /ɡ/ in Bedouin/loan strata; the interdentals merge to stops
ث → /t/ (~/s/ learned), ذ → /d/ (~/z/), ظ/ض → /dˤ/ (~/zˤ/), giving the four-emphatic
inventory /tˤ dˤ sˤ zˤ/; and the loan grapheme چ → /ʒ/ (since native ج is /ɡ/). To that it
adds the **post-lexical** emphatic-spreading rules (`AR_EG_EMPH_BACK_*`): Cairene has
famously wide emphasis spreading, so /a aː/ back to [ɑ ɑː] next to an emphatic
(صَبَاح → [sˤɑbaːħ]). Cairene weight-sensitive stress is a syllable-weight algorithm not
expressible in the ending-based stress schema and is left as engine-level future work.
Sources: Watson (2002); Mitchell (1956); Badawi & Hinds (1986).

## Saudi Arabia — Najdi (`ar-SA-x-najd`) and Hejazi (`ar-SA-x-hejaz`)

Both inherit the abstract `ar-x-peninsular` parent, from which they receive the shared
Peninsular emphatic-spreading rules (`AR_PEN_EMPH_BACK_*`). Both are promoted here from
**skeleton to research**.

**Najdi** (central Arabia incl. Riyadh; primary reference Ingham 1994, *Najdi Arabic:
Central Arabian*):

- qāf ق → /ɡ/ (Bedouin/traditional; /q/ in MSA loans/proper names, e.g. القرآن).
- **Velar affrication** — /k/ → [ts] and /ɡ/ → [dz] in a front-vowel environment
  (كِلاب → [ts…], قِرْد → [dzird]; classic كلب [tsalb]). Modeled as `NAJD_AFFRIC_*`
  allophone rules conditioned on an adjacent front vowel. Purely lexicalized affrication
  before a *historical* front vowel is not captured (documented limitation).
- **Gahawa syndrome** — epenthetic /a/ after a guttural /h x ɣ ħ ʕ/ in a
  low-vowel + guttural + consonant context (لَحْم → [laħam], gahwa → gahawa). Modeled as
  `NAJD_GAHAWA_*` (rewriting the coda guttural to guttural+[a]).
- Interdentals **preserved** (ث /θ/, ذ /ð/); the Old-Arabic ض/ظ contrast is neutralised to
  a single emphatic interdental [ðˤ], so ض is transcribed [ðˤ].

**Hejazi** (urban Mecca/Medina/Jeddah; Omar 1975; Abdoh 2010):

- qāf ق → /ɡ/ in inherited vocabulary (قَلْب → [ɡalb], **not** /ʔ/ — the /ʔ/ reflex is a
  misattribution of the Levantine/Egyptian feature); /q/ only in learned borrowings.
- jīm ج → /dʒ/ (affricate) preserved.
- Interdentals **merged to stops** in the urban koine: ث → /t/, ذ → /d/, ظ → /dˤ/.
- **Monophthongization** — Classical /aj aw/ → [eː oː] (بَيْت → [beːt], yawm → [joːm]),
  modeled as `HEJ_MONO_AY` / `HEJ_MONO_AW`, giving the 8-vowel system /a u i; aː uː iː eː oː/.
- Four emphatics /sˤ dˤ tˤ zˤ/; no Gulf/Najdi k → [tʃ] affrication.

**Input contract for the dialects.** Unlike MSA (which contractually expects fully
tashkeel-marked input), dialectal Arabic is normally written *defectively*. These specs
transcribe whatever the orthography plus any harakat supply — short vowels surface only
when the input is vocalised. Neither Saudi variety has a registered gold set; their
correctness is established by **citation** to the reference grammars above, not by PER.

## References

- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press.
- Ryding, K.C. (2005). *A Reference Grammar of Modern Standard Arabic*. Cambridge University Press.
- Mitchell, T.F. (1956). *An Introduction to Egyptian Colloquial Arabic*. Oxford University Press.
- Badawi, E.S. & Hinds, M. (1986). *A Dictionary of Egyptian Arabic*. Librairie du Liban.
- Ingham, B. (1994). *Najdi Arabic: Central Arabian*. John Benjamins.
- Omar, M.K. (1975). *Saudi Arabic, Urban Hijazi Dialect: A Basic Course*. Foreign Service Institute.
- Abdoh, E. (2010). *A Study of the Phonology and Morphology of Urban Meccan Arabic*. PhD diss., University of Kansas.
- Wikipedia: [Sun and moon letters](https://en.wikipedia.org/wiki/Sun_and_moon_letters)
- Wikipedia: [Standard Arabic phonology](https://en.wikipedia.org/wiki/Standard_Arabic_phonology)
