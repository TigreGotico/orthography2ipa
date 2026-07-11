# Modern Standard Arabic (ar) — Phonology Reference

**Code**: `ar` | **Family**: Afro-Asiatic > Semitic | **Script**: Arabic (abjad)
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
realized when explicitly marked in the input (see [Gemination](#gemination-shadda-ّ)
below).

Where the vowel-bearing diacritic is nonetheless absent, the spec degrades gracefully
rather than dropping segments: the hamza carriers أ/إ fall back to their default
hamza+vowel readings (`ʔa`/`ʔi`) so an undiacritized skeleton still surfaces a vowel,
and the matres lectionis ا/ي/و default to their long-vowel readings word-medially and
word-finally. This is why the undiacritized WikiPron gold — which is scored on bare
consonantal skeletons — still transcribes usefully (see [Gold benchmark](#gold-benchmark)).

## Presentation-form and lam-alif ligature normalization (engine-level)

Before grapheme tokenization, any Arabic-script spec (this one included) decomposes the
Arabic **Presentation Forms-A** (U+FB50–U+FDFF) and **Presentation Forms-B**
(U+FE70–U+FEFF) blocks to their canonical letters via a script-scoped NFKC decomposition
(`orthography2ipa/phonetok.py`). These blocks hold contextual glyph variants and
ligatures — most importantly the four **lam-alif ligatures** ﻻ/ﻷ/ﻵ/ﻹ
(U+FEFB/FEF7/FEF5/FEF9), which decompose to ل + ا/أ/آ/إ. Because the grapheme table is
keyed on the canonical letters, a bare ligature would otherwise tokenize to nothing:

```python
transcribe("ﻻ", "ar")   # -> "laː"   (was "" before normalization)
```

The decomposition touches **only** codepoints inside those two Arabic blocks, so no other
script is disturbed (a global NFKC would also fold Latin ligatures, full-width forms,
etc.).

## Gemination (shadda ّ)

A consonant carrying **shadda** (ّ, U+0651) is a geminate — it surfaces as a doubled
(long) consonant, and this holds for **every** consonant including the glides ي/و, which
geminate as the consonants they are (Ryding 2005, *A Reference Grammar of Modern Standard
Arabic*, ch. 2 "Phonology and script", on the doubling of consonants and on the
approximants/semivowels waaw & yaa, **pp. 15–16**; Watson 2002, *The Phonology and
Morphology of Arabic*, on MSA gemination via shadda). The engine models this as an
Arabic-script-scoped **normalization-time transform**
(`orthography2ipa/phonetok.py`): the base consonant is doubled and the shadda dropped, so
downstream per-slot resolution sees two ordinary consonant slots. Both Unicode orderings
of the mark cluster are handled — the canonical *consonant + shadda + harakat* and the
equally-valid *consonant + harakat + shadda* (they render identically and NFC does not
reorder them, since shadda's combining class differs from the harakat's).

```python
transcribe("عَمَّ", "ar")     # -> "ʕamma"   (geminate m, not a length mark on the vowel)
transcribe("عُيِّنَ", "ar")   # -> "ʕujjina"  (glide ي geminates too)
transcribe("قَوَّاس", "ar")   # -> "qawwaːs"  (glide و geminate before the long-ā digraph)
```

This replaces the previous `arb`-inherited ّ → `ː` mapping, which stranded a bare length
mark on the wrong slot (عَمَّ → *ʕamaː*).

**Documented limit.** A kasra sitting on a geminate glide (ـِيّ, e.g. حُرِّيَّة *ḥurriyya*)
is under-resolved: the kasra+yā digraph ـِي greedily reads as a long /iː/ mater before the
geminate glide is recovered, so the surface is imperfect. The common geminate-glide cases
(عُيِّنَ, قَوَّاس) resolve correctly.

## Glide onsets, hamza carriers, and matres lectionis (`ar` grapheme/positional overrides)

`ar` overrides a handful of inherited `arb` grapheme entries at the leaf so the flagship
spec transcribes the fully-diacritized forms correctly (the changes are scoped to `ar`;
`arb` and the dialects are untouched). Each choice is cited to Wright / Ryding:

- **Glide + fatḥa is an onset, not a diphthong.** يَ → /ja/ and وَ → /wa/ (glide-first =
  consonant onset), whereas the diphthongs /aj/ /aw/ are combinations of a short vowel
  and a *following* semivowel — the *fatḥa-first* sequences َي / َو (Ryding 2005,
  "Diphthongs and glides", **pp. 29–30**: the diphthongs are /aw/ and /ay/, i.e.
  short-vowel + semivowel; the semivowels waaw/yaa as consonants, pp. 15–16). So يَوم →
  [jawm], not *[ajwm]*.
- **Hamza carriers are a bare /ʔ/ + the harakat vowel.** أ → /ʔ/ and إ → /ʔ/ before a
  written vowel, with the short vowel supplied by the explicit harakat — not a baked-in
  `ʔa`/`ʔi` that doubles against a following mater (Ryding 2005, **p. 16**: "Strong hamza
  is a regular consonant and is pronounced under all circumstances"). So إِيْمَان →
  [ʔiːmaːn], not *[ʔiiːmaːn]*. When **no** harakat follows (undiacritized input, out of
  contract) they fall back to `ʔa`/`ʔi` (positional `default`), so bare skeletons keep a
  vowel.
- **Word-final ي/و prefer the long-vowel reading.** Via `positional_graphemes`
  (`word_final`), so يُصَلِّي → […iː], not a stranded glide […j] (Ryding 2005, **pp. 25–27**,
  on the long vowels /ii/ /uu/ spelled with yāʾ/wāw). This preference is now **guarded**
  by the coda-glide rule below: it only lengthens after a homorganic short vowel, never
  after a sukūn-marked coda consonant.
- **ة (tāʾ marbūṭa) is the pausal /a/.** Word-final ة after a harakat contributes nothing
  (the preceding fatḥa already supplies the /a/), so مَدْرَسَة → [madrasa], not
  *[madrasaa]*. The context-sensitive /at/ construct-state reading (تاء مربوطة in *iḍāfa*)
  needs the **following** word and is therefore an engine limit (see
  [Remaining engine limits](#remaining-engine-limits) below).

## Alif-maksūra merge and the coda-glide guard (`arb`-level, inherited by all Arabic)

Two further fixes surfaced by the arbtok migration live in the shared `arb` grapheme
table (not the `ar` leaf), so **every** Arabic-script spec that inherits `arb`'s graphemes
— Classical `arb`, MSA `ar`, and the dialects — gets them. Both are Classical/MSA-correct
and both only fire on **diacritized** input, so the undiacritized WikiPron gold is
byte-identical (PER holds at 0.1868).

- **Fatḥa + standalone alif-maksūra ⟨ـَى⟩ merges to a single [aː].** `arb` already merged
  fatḥa + alif ⟨ـَا⟩ → [aː] and read a bare ى as [aː]; the fatḥa + alif-maksūra *sequence*
  was missing, so حَتَّى came out *ħattaaː* (the fatḥa's /a/ then a second /aː/ from ى). A
  new digraph ⟨ـَى⟩ → [aː] completes the mater-lectionis set: حَتَّى → [ħattaː], رَمَى →
  [ramaː]. Alif maqṣūra is only a *spelling* of final /aː/ (Wright 1896, Vol. I, Part
  First "Orthography", alif maqṣūra as final ā, **pp. ~10–25**; Ryding 2005, "Phonology
  and script", long vowels spelled with the matres, **pp. 25–27**).
- **Word-final glide after a coda consonant (sukūn) stays a glide.** The `word_final`
  long-vowel preference for ي/و (above) previously over-fired even after a sukūn-marked
  coda consonant with no homorganic short vowel, so ظَبْي → *ðˤ…iː* and رَمْي → *ramiː*. But
  a long /iː/ /uː/ is spelled with the **homorganic** short vowel (kasra ⟨ـِي⟩, ḍamma
  ⟨ـُو⟩) — captured by the inherited ⟨ـِي⟩→[iː] / ⟨ـُو⟩→[uː] digraphs — whereas a
  sukūn-bearing consonant is *quiescent* (vowelless) and a following ي/و is the coda/onset
  **glide** /j/ /w/ (Wright 1896, Vol. I, Part First "Orthography", the jazma/sukūn marks a
  vowelless consonant, **pp. ~10–20**; Ryding 2005, **pp. 25–27, 29–30**). New digraphs
  ⟨ـْي⟩ → [j] and ⟨ـْو⟩ → [w] encode this: رَمْي → [ramj], ظَبْي → [ðˤɑbj] (the [ɑ] is the
  pre-existing emphatic backing after ظ /ðˤ/), and word-medially دُنْيَا → [dunjaː] (the /j/
  onset of the following syllable). It is keyed on the **explicit** sukūn, so it never
  touches ⟨يْ⟩ (a diphthong offglide, بَيْت → [bajt]) nor the graceful undiacritized
  fallback (في → [fiː], no sukūn present).

## Remaining engine limits (honest scope)

Two Arabic phenomena need sentence/cross-word context that the word-level engine does not
have, and are left explicitly unmodeled:

- **ة construct-state /at/.** Word-final ة surfaces as /at/ only in *iḍāfa* (before a
  following genitive); in pause it is /a/. The engine picks the pausal /a/ and cannot see
  the following word to switch to /at/.
- **Word-final ا / pausal iʿrāb and cross-word sun-letter assimilation.** Pausal dropping
  of case vowels and the attached-article sun-letter assimilation both require token/
  sentence context (see the `AR_SUN_ASSIMILATION` scope note above); they are unchanged by
  this work.

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

### Error analysis: why the remaining PER is a gold-contract limit, not a spec bug

Running `python scripts/error_analysis.py ar` (259 scored words) shows the top phoneme
confusion pairs are **all** consequences of the gold being 100 % undiacritized — the very
short-vowel / gemination information the [input contract](#input-contract--known-limitation-diacritics)
says the spec cannot recover — plus the already-documented emphatic-backing broad-gold
gap. None is a principled MSA-phonology error left to fix, so no fallback is tuned to the
gold (doing so would overfit the spec to this one lexicon):

- **`a → ∅` (×145), `i → ∅` (×56), `u → ∅` (×35)** — the gold carries short vowels that
  the bare consonantal skeleton simply does not write (e.g. أحبك gold `ʔuħibbuka`, hyp
  `ʔaħbk`). Unrecoverable without tashkeel; **not** fixable by the spec.
- **`ː → w` (×27), `ː → j` (×17)** — a medial mater-lectionis ambiguity: an undiacritized
  و/ي between consonants is read as the default glide /w/ /j/, but the gold happens to want
  a long /uː/ /iː/ (أبوت gold `ʔubuːt`, hyp `ʔabwt`). Glide vs. long vowel here is
  genuinely undecidable without the diacritic, so the default is **not** flipped to the
  long vowel (that would only chase this gold's noun/loan-heavy lexicon and regress
  glide-final skeletons).
- **`j → ∅` (×17), `j → ː` (×10)** — word-final nisba ⟨ـيّ⟩ /-ijj/ vs. plain long ⟨ـي⟩
  /-iː/: both are written ي with no diacritic (آشوري gold `ʔaːʃuːrijj`, hyp `ʔaːʃwriː`).
  The gemination that distinguishes them is unmarked in the gold — a shadda gap, not a
  rule gap.
- **`u → a` (×16)** — the hamza-carrier / bare-vowel default (أ → `ʔa`) guessing the wrong
  short vowel on an undiacritized skeleton (أبدة gold `ʔubbada`, hyp `ʔabda`). Same
  tashkeel gap.
- **`a → ɑ` (×7)** — the correct narrow emphatic backing [ɑ] that the **broad** gold
  writes as plain /a/; already documented under [emphatic spreading](#emphatic-pharyngealization-spreading)
  as a broad-gold measurement limit, retained because it is linguistically correct.

The two diacritized fixes in this round (alif-maksūra merge, coda-glide guard) therefore
leave the gold PER **byte-identical at 0.1868** — they correct diacritized transcription,
which this undiacritized gold cannot reward or penalize.

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

## Gulf Arabic — Khaleeji (`ar-x-gulf` → `ar-AE`, `ar-BH`, `ar-KW`, `ar-QA`) and Omani (`ar-OM`)

The proto-parent `ar-x-gulf` (promoted **skeleton → research**) is an abstract ancestor
node inheriting `ar-x-peninsular`. Emirati (`ar-AE`), Bahraini (`ar-BH`), Kuwaiti
(`ar-KW`) and Qatari (`ar-QA`) inherit it via `graphemes_base` (OVERLAY_BY_ID), so the
shared Gulf features are declared **once** on the proto-parent. Omani (`ar-OM`) is
genetically Peninsular and inherits `ar-x-peninsular` **directly** — it is a Gulf-region
dialect but not a Gulf-node descendant.

**Shared Gulf features (on `ar-x-gulf`, inherited by AE/BH/KW/QA):**

- **qāf ق → /ɡ/** (Bedouin/sedentary Gulf reflex), with /q/ a secondary MSA/formal
  candidate: قَلَم → [ɡalam].
- **Velar affrication** — the marquee Gulf feature, modeled as **post-lexical allophone
  rules** (the [allophony](../allophony.md) B8 layer), *not* as grapheme candidates:
  - `GULF_K_AFFRICATION`: /k/ → [tʃ] adjacent to a high front vowel /i, iː/
    (كِتَاب → [tʃitaːb]; but كَلْب → [kalb], blocked before the low vowel).
  - `GULF_G_AFFRICATION`: /ɡ/(< *q) → [dʒ] adjacent to a high front vowel
    (قِرْد → [dʒird]).
  The high-front conditioning matches Mustafawi's (2006, 2007) Qatari OT analysis
  (adjacent to /i, iː/ only; blocked by [-high] segments). **Limitations documented in
  the rule `notes`:** the alternation is historically *lexicalized* — Johnstone (1967)
  and Szreder & Derrick (2023, for Emirati) treat [k~tʃ] as a completed phonemic change
  and /tʃ/ as an independent phoneme; affrication is further blocked by adjacent
  emphatics and by the OCP, and the coda case (samak → simatʃ) and Matar's non-adjacent
  Kuwaiti trigger (across an intervening /r l/) are not modeled. The base rule captures
  only the regular *following-high-front-vowel* onset case.
- **Interdentals /θ ð ðˤ/ RETAINED** (Bedouin-type retention), unlike sedentary
  Levantine/Egyptian which merge them to stops/sibilants: ثَلاثَة keeps [θ], ذَهَب keeps [ð].
- **jiim /dʒ/ ~ [j]** glide variation (grapheme ج → [dʒ]~[j]).
- Integrated loan phonemes /p/, /v/ (پ, ڤ).
- **Emphatic spreading** (low vowels back to [ɑ]/[ɑː] next to /tˤ dˤ sˤ ðˤ zˤ/) is
  inherited from `ar-x-peninsular` (`AR_PEN_EMPH_*`).

**Per-country / per-node deltas:**

- **Emirati `ar-AE`** — heaviest English influence (Dubai effect): /p v tʃ ŋ/ fully
  integrated. Szreder & Derrick (2023): the [k~tʃ] alternation is a completed phonemic
  change (the inherited affrication rule is thus a predictive approximation of the
  historical distribution), while [dʒ~j] is a live synchronic process in which a nearby
  similar coronal obstruent inhibits the **voiced [j] variant** of the dʒ~j alternation.
  Note the asymmetry: for the voiceless target /k/→[tʃ], affrication was **not** inhibited
  by similar consonants (if anything the reverse) — so the inhibitory effect belongs to
  the voiced [dʒ~j] process, not to [tʃ].
- **Bahraini `ar-BH`** — models the general Gulf pattern, and documents (in the spec
  `notes`) the well-known **communal split**: the Bedouin-descended Sunni *ʕArab*
  variety patterns like mainstream Gulf; the sedentary Shia *Baḥārna* variety is more
  conservative (can retain [q], distinct jiim reflex, older Persian adstrate), for which
  the *q→[ɡ]/affrication defaults over-generalize. One spec models one lect, so the
  split is noted rather than separately encoded.
- **Kuwaiti `ar-KW`** — best-documented Gulf variety; Matar's (1969) /ɡ/→[dʒ] pattern and
  the -tʃ 2fsg kashkasha suffix noted (the morphological suffix is out of base scope).
- **Qatari `ar-QA`** — the inherited high-front conditioning *is* Mustafawi's Qatari
  analysis; her additional blocking environments (emphatics, OCP, paradigmatic leveling
  in broken plurals/verbs) are documented as engine limits.
- **Omani `ar-OM`** — Peninsular, **retains qāf as [q]** in the prestige sedentary
  varieties of Muscat/Ṣalālah (grapheme ق → [q] first), unlike the northern Gulf
  *q→[ɡ]; Bedouin varieties have [ɡ], northern-mountain sedentary [k], and Sur/Ṣoħār
  [dʒ] (Al-Balushi 2016 p.88). jiim /dʒ/ is a free variant of /ɡ/ in most words
  (Glover 1988:38, in Al-Balushi p.89). /k/-affrication is present only as a
  Bedouin/interior feature (`OM_K_AFFRICATION`; the sedentary Muscat norm does *not*
  productively affricate — documented in the rule `notes`).

**Input contract.** As with all Arabic specs, the Gulf specs expect **fully diacritized
(tashkeel) input**; the affrication and emphatic rules condition on the written
short-vowel diacritics, so undiacritized running text will not trigger them.

**No gold benchmark.** None of the Gulf specs has a registered gold set; correctness is
established by **citation** to the sources below (actually read), not by PER — so
promoting them moves no scoreboard row.

**Sources actually read for the Gulf specs** (page-cited in each spec's `sources`):
Alshammari (2026) — read in full; its literature review (p.1335) surveys Gulf velar
affrication (Mustafawi's Qatari, Matar's Kuwaiti, Johnstone's lexicalization). Al-Balushi
(2016) — phonology sections (pp. 85–90) read for Omani/Eastern-Arabian reflexes.
Szreder & Derrick (2023) — abstract and published summary read (full text paywalled) for
Emirati affricate variability. Holes (1990, 2001) and Qafisheh (1977), the standard Gulf
reference works, could **not** be obtained (borrow-only / no open full text) and are
therefore *not* cited as primary reads — only as works reported within the sources above.

## References

- Wright, W. (1896). *A Grammar of the Arabic Language*, 3rd ed., Vol. I. Cambridge University Press. (Part First, "Orthography and Orthoepy": the matres lectionis, alif maqṣūra as a spelling of final /aː/, and the jazma/sukūn as the mark of a vowelless consonant.)
- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press.
- Ryding, K.C. (2005). *A Reference Grammar of Modern Standard Arabic*. Cambridge University Press.
- Mitchell, T.F. (1956). *An Introduction to Egyptian Colloquial Arabic*. Oxford University Press.
- Badawi, E.S. & Hinds, M. (1986). *A Dictionary of Egyptian Arabic*. Librairie du Liban.
- Ingham, B. (1994). *Najdi Arabic: Central Arabian*. John Benjamins.
- Omar, M.K. (1975). *Saudi Arabic, Urban Hijazi Dialect: A Basic Course*. Foreign Service Institute.
- Abdoh, E. (2010). *A Study of the Phonology and Morphology of Urban Meccan Arabic*. PhD diss., University of Kansas.
- Alshammari, K.K. (2026). An Optimality-Theoretic Account of Velar Affrication in Northern Najdi Arabic. *Journal of Language Teaching and Research* 17(4): 1333–1341. https://doi.org/10.17507/jltr.1704.19
- Al-Balushi, R. (2016). Omani Arabic: More than a Dialect. *Macrolinguistics* 4(1): 80–125.
- Szreder, M. & Derrick, D. (2023). Phonological conditioning of affricate variability in Emirati Arabic. *Journal of the International Phonetic Association* 54(1): 146–164. https://doi.org/10.1017/S0025100323000129
- Wikipedia: [Sun and moon letters](https://en.wikipedia.org/wiki/Sun_and_moon_letters)
- Wikipedia: [Standard Arabic phonology](https://en.wikipedia.org/wiki/Standard_Arabic_phonology)

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [ar-IQ](ar-IQ.md), [ar-x-levantine](ar-x-levantine.md)*
