# Portuguese-dialects TTS gold set

`orthography2ipa/data/gold/portuguese_tts/<code>.tsv` — 20 phonetically
diverse, register-appropriate, literature-justified sentences for each of the
39 Portuguese lects in the catalogue. Built to validate Portuguese TTS voices
per dialect (synthesize each sentence, ASR/listen, compare against the gold
IPA) and to regression-pin sentence-level o2i behaviour.

Portuguese orthography is complete — the written form already encodes every
segment a speaker needs — so a row is simply the sentence a TTS receives.
There is no separate `raw`/undiacritized column and no diacritization-gap
check (contrast the Arabic gold set, whose input contract is fully vocalized
text).

The set is grown incrementally: the shipped exemplars (`pt-PT`,
`pt-PT-x-lisbon`) set the quality bar. `validate` gates every lect that has a
TSV and reports the rest as pending, so a lect can be authored ahead of time
without failing CI.

## Schema

TSV, tab-separated, UTF-8, header row:

| column | content |
|---|---|
| `id` | `<lect>-NNN` |
| `sentence` | ordinary Portuguese orthography (o2i's input) |
| `ipa` | o2i transcription of `sentence`, manually verified against the lect's cited sources |
| `gloss_en` | English translation |
| `features` | semicolon list of coverage tags (below) |
| `notes` | tool-output corrections + the citation ids (from the spec's `sources`) justifying them |

## The `ipa == transcribe(sentence, lect)` contract

The `ipa` column is exactly what o2i emits for `sentence` under that lect. The
validator recomputes it and fails on any mismatch. When o2i is wrong, **fix
the spec** (cited, against the lect's `sources`) or respell the sentence to a
word the literature attests — **never hand-edit the `ipa` column**. A gold
that has been silently patched to mask a spec bug is worse than no gold. Any
correction is recorded in `notes` with the source id that grounds it.

## Feature tags

Each phonetic tag is a predicate over `(sentence, ipa)` that the validator
recomputes per row (see `FEATURES` in `scripts/portuguese_tts_gold.py`). A tag
may only appear on a row where its predicate is true. The axes are the ones
that actually discriminate Portuguese lects:

| tag | verified by | fires when |
|---|---|---|
| `vowel_reduction` | ipa | reduction vowel `[ɨ]` or `[ɐ]` present (EP heavy, BR light) |
| `coda_sibilant` | both | a coda `s/z/x` in the orthography **and** a `[ʃ]`/`[ʒ]` standing in *coda* position in the ipa — before a consonant or at a word/utterance boundary. An onset `[ʃ ʒ]` (from `ch`, `j`, or soft `g`) elsewhere in the row does not count |
| `open_mid` | ipa | `[ɛ]` or `[ɔ]` present |
| `close_mid` | ipa | `[e]` or `[o]` present |
| `nasal_vowel` | ipa | a nasalised vowel present, whether the spec emits a combining tilde (NFD) or a precomposed nasal letter (`ã õ …`, as the historical lects do) — the check normalises so the encoding never decides the tag |
| `nasal_diphthong` | ipa | a nasalised glide `[w̃]`/`[j̃]` (ão, ãe, õe, …) |
| `palatal` | ipa | `[ʎ]` or `[ɲ]` present |
| `rhotic` | ipa | a strong-R reflex `[ʀ ʁ r h χ]` (excludes the ubiquitous tap `[ɾ]`) |
| `diphthong_ei_ou` | orth | the sentence has `ei` or `ou` (retention vs monophthong is the lect's call) |
| `l_dark_or_velar` | orth | the sentence has a coda `l` (reflex `[ɫ]`/velar/`[w]` varies by lect; the `lh` digraph is excluded) |
| `u_fronting` | ipa | `[y]` present — the insular (Azores/Madeira) fronting of `/u/` |
| `sandhi` | both | a cross-word junction: vowel-final before vowel-initial (elision/liaison), or `s/z`-final before a voiced onset (regressive sibilant voicing) |

The `orth`/`ipa`/`both` split mirrors the Arabic set: an axis whose *reflex*
varies across lects is witnessed by the stable grapheme (`diphthong_ei_ou`,
`l_dark_or_velar`), while a realised reflex is read off the transcription.
`coda_sibilant` and `sandhi` require both an orthographic trigger and the
predicted ipa so the tag proves the row genuinely exercises the axis.

Shape tags (not machine-verified): `statement`, `question`, `negation`,
`imperative`, `number`.

## Sentence frames

Each lect's 20 sentences cover the same 14 shared semantic frames plus 6
coverage rows, so the sets are comparable across dialects while each stays
faithful to its own register:

1. weather + negation
2. price + number
3. appointment
4. family / residence
5. directions (imperative)
6. food evaluation
7. where-question
8. how-many
9. conditional
10. past shopping
11. future travel
12. phone
13. greeting pair
14. proverb
15–20. six coverage rows filling the phonetic tags a lect's frames 1–14 left
uncovered (strong rhotic, `ei`/`ou`, dark `l`, palatals, open/close mid, and —
for insular lects — `u`-fronting).

## Register rule

Each lect uses its **genuine** regional lexicon and morphology **where the
literature the spec cites attests it** — never an invented shibboleth. Porto
keeps `tu fizeste` where Lisbon-standard has it too but the northern
monophthongised `ei→[e]` distinguishes the reflex; Brazilian lects choose
`você`/`tu` by region; caipira retroflex `r` appears only in its attested coda
contexts; Alentejo uses its gerundive progressive; Azorean/Madeiran draw on
their attested insular lexicon and `u`-fronting. When a regional form is not
documented in the lect's `sources`, fall back to the neutral standard rather
than guess.

## Sandhi-rich authoring

Portuguese phonology lives at the word boundary: definite-article vowel
raising, `s/z` voicing across a junction, and vowel elision/liaison are what a
TTS most often gets wrong. Sentences are authored to be **sandhi-rich** — most
rows contain at least one `sandhi` junction (a vowel-final + vowel-initial pair
or an `s/z` + voiced-onset pair), so the gold exercises connected-speech
behaviour, not just isolated-word transcription.

## Procedure (how to add sentences)

1. `python scripts/portuguese_tts_gold.py checklist <lect>` — prints the
   dialect-discriminative feature checklist and which tags the current gold
   already covers.
2. Author 20 sentences over the 14 frames + 6 coverage rows, grounding the
   lexicon in the literature the lect's spec cites (Cruz-Ferreira 1995 and
   Mateus & d'Andrade 2000 for the European standard; the lect-specific
   sources for each dialect). Reuse words the spec's own primary-source gold
   attests (`orthography2ipa/data/gold/primary_sources/rows.jsonl`) so a row
   doubles as a primary-source witness.
3. `python scripts/portuguese_tts_gold.py draft <lect> <textfile>` — machine
   first-draft: o2i IPA + auto-tagged feature axes. Author the `gloss_en` and
   the `notes` citation id by hand.
4. Verify the IPA against the spec's phoneme mappings and sources. If o2i is
   wrong, **fix the spec** (cited) — never hand-edit the IPA column.
5. `python scripts/portuguese_tts_gold.py validate` must pass
   (`tests/test_portuguese_tts_gold.py` runs it in CI).

## Per-lect grounding highlights

- **pt-PT** (European standard): heavy unstressed reduction to `[ɨ ɐ u]`, coda
  sibilant `[ʃ ʒ]`, velarised coda `[ɫ]`, open/close mid contrast, nasal
  vowels and nasal diphthongs (`[ɐ̃w̃ ɐ̃j̃ õj̃]`), palatals `[ʎ ɲ]`, uvular
  strong-R `[ʁ]` (Cruz-Ferreira 1995; Mateus & d'Andrade 2000; Cunha & Cintra
  1984).
- **pt-PT-x-lisbon** (Lisbon standard): the pt-PT profile with the raised
  definite article `o` → `[u]` and the fullest reduction; rows 15–20 reuse
  Cruz-Ferreira 1995's IPA-illustration words (`gato`, `rato`, `mundo`,
  `chato`, `pilha`) so they witness the primary-source gold directly
  (Cintra 1971; Segura 2013; Cruz-Ferreira 1995).
