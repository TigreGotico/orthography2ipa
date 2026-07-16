# Kabyle TTS gold set

`orthography2ipa/data/gold/kabyle_tts/<code>.tsv` — 20 phonetically diverse,
register-appropriate, literature-justified Kabyle sentences. Built to validate
Kabyle (Taqbaylit) TTS voices (synthesize each sentence, ASR/listen, compare
against the gold IPA) and to regression-pin sentence-level o2i behaviour.

## Input contract

Sentences are written in the standardised Berber **Latin** alphabet — the
tamaziɣt/INALCO orthography of the Kabyle Wikipedia and Naït-Zerrad's teaching
grammars, the same contract the `kab` spec expects. Tifinagh is a secondary
script for Kabyle and is **not** covered here; a Tifinagh text would be
transliterated to this Latin orthography first. Kabyle orthography is complete —
the written form already encodes every segment a speaker needs — so a row is
simply the sentence a TTS receives. There is no separate `raw`/undiacritized
column and no diacritization-gap check (contrast the Arabic gold set, whose
input contract is fully vocalized text).

The set is grown incrementally: the shipped `kab.tsv` (20 rows) sets the quality
bar. `validate` gates every lect that has a TSV and reports the rest as pending,
so a future Kabyle sub-variety can be authored ahead of time without failing CI.

## Schema

TSV, tab-separated, UTF-8, header row:

| column | content |
|---|---|
| `id` | `<lect>-NNN` |
| `sentence` | standard Berber-Latin Kabyle orthography (o2i's input) |
| `ipa` | o2i transcription of `sentence`, manually verified against the cited sources |
| `gloss_en` | English translation |
| `features` | semicolon list of coverage tags (below) |
| `notes` | tool-output corrections + the citation ids (from the spec's `sources`) justifying them |

## The `ipa == transcribe(sentence, lect)` contract

The `ipa` column is exactly what o2i emits for `sentence` under `kab`. The
validator recomputes it and fails on any mismatch. When o2i is wrong, **fix the
spec** (cited, against the `kab` `sources`) or respell the sentence to a word
the literature attests — **never hand-edit the `ipa` column**. A gold silently
patched to mask a spec bug is worse than no gold. Any correction is recorded in
`notes` with the source id that grounds it.

## Feature tags

Each phonetic tag is a predicate over `(sentence, ipa)` that the validator
recomputes per row (see `FEATURES` in `scripts/kabyle_tts_gold.py`). A tag may
only appear on a row where its predicate is true. The axes are the ones that
characterise Kabyle phonology:

| tag | verified by | fires when |
|---|---|---|
| `spirantization` | ipa | a spirantized lax stop `[β ð θ ç ʝ ðˤ]` present — the signature Kabyle feature |
| `geminate` | ipa | a length mark `[ː]` — a tense (geminate) consonant, retained as a stop |
| `emphatic` | ipa | a pharyngealization mark `[ˤ]` (`ṛ ṣ ḍ ṭ ẓ` → `[rˤ sˤ dˤ tˤ zˤ]`) |
| `pharyngeal` | ipa | `[ħ]` or `[ʕ]` (the Arabic-integrated series `ḥ ɛ`) |
| `affricate` | ipa | `[t͡ʃ]` or `[d͡ʒ]` (`č ǧ`) |
| `uvular` | ipa | uvular stop `[q]` or fricative `[χ]` (`x`) |
| `velar_fricative` | ipa | `[ɣ]` (`ɣ`) |
| `schwa` | ipa | `[ə]` — the epenthetic vowel written `e` |
| `glide` | ipa | `[j]` or `[w]` (`y w` and affixal semivowels) |
| `postnasal_stop` | both | a written `⟨nt nd nb⟩` cluster that surfaces with the stop retained (`[nt] [nd] [mb]`) — the spirantization block after a homorganic nasal |
| `velar_nasal` | ipa | `[ŋ]` — nasal place assimilation before a dorsal |

The `orth`/`ipa`/`both` split mirrors the Arabic and Portuguese sets. Most
axes are read off the transcription; `postnasal_stop` requires **both** the
orthographic nasal+stop cluster and the stop surviving in the ipa, so the tag
proves the row genuinely exercises the spirantization block rather than merely
lacking a spirant.

Shape tags (not machine-verified): `statement`, `question`, `negation`,
`imperative`, `greeting`.

## Register rule

Every sentence uses **genuine** Kabyle lexicon and morphology attested in the
cited references (Dallet 1982's Kabyle-French dictionary, Naït-Zerrad 2001's
reference grammar) — never an invented form. The morphosyntax exercises the
features a Kabyle TTS most often mishandles: the *état d'annexion* on nouns
after a preposition (`ɣer wexxam`, `ɣer ugadir`), bipartite negation `ur … ara`,
the directional/aorist clitics `d-`/`ad`, and the aspectual verb stems. When a
form is not documented in the sources, it is not used.

## Phonological coverage highlights

- **Spirantization** — the lax stops `b d t k g ḍ` surface as `[β ð θ ç ʝ ðˤ]`
  in the attested contexts (`argaz` → `[arʝaz]`, `adrar` → `[aðrar]`,
  `taqbaylit` → `[θaqβajliθ]`), per `kossmann_stroomer1997` p.466-469.
- **Geminate retention** — the tense (geminate) counterparts, written by
  doubling and mapped to long phonemes, stay stops and are never spirantized
  (`yeṭṭef` → `[jətˤːəf]`, `meqqer` → `[məqːər]`), per `kossmann_stroomer1997`
  p.466.
- **Post-nasal hardening** — `⟨nt nd nb⟩` keeps the stop after a homorganic
  nasal (`nteddu` → `[ntədːu]`, not `*[nθədːu]`), per `kossmann_stroomer1997`
  p.468. This is the axis the `KAB_POSTNASAL_HARD_*` allophone rules model.
- The emphatic/pharyngeal series (`ṛ ṣ ḍ ṭ ẓ ḥ ɛ`), the affricates (`č ǧ`),
  the uvulars (`q x`), `[ɣ]`, nasal place assimilation (`n` → `[ŋ]` before a
  dorsal), and the epenthetic schwa `[ə]` are each exercised by at least one row.

## Procedure (how to add sentences)

1. `python scripts/kabyle_tts_gold.py checklist kab` — prints the feature
   checklist and which tags the current gold already covers.
2. Author sentences in standard Berber-Latin Kabyle, grounding the lexicon in
   the references the `kab` spec cites (`dallet1982`, `naitzerrad2001`) and the
   phonological reflexes in `kossmann_stroomer1997`.
3. `python scripts/kabyle_tts_gold.py draft kab <textfile>` — machine
   first-draft: o2i IPA + auto-tagged feature axes. Author the `gloss_en` and
   the `notes` citation id by hand.
4. Verify the IPA against the spec's phoneme mappings and sources. If o2i is
   wrong, **fix the spec** (cited) — never hand-edit the IPA column.
5. `python scripts/kabyle_tts_gold.py validate` must pass
   (`tests/test_kabyle_tts_gold.py` runs it in CI).
