# Spain-Romance TTS gold set

`orthography2ipa/data/gold/spain_romance_tts/<code>.tsv` — 20 phonetically
diverse, register-appropriate, literature-justified sentences for each of the
Romance lects of Spain: Castilian and its regional accents, Galician,
Asturleonese, Aragonese, Catalan/Valencian, Aranese Occitan, and the
peripheral Romance of the Iberian west (Fala, Extremaduran, the Sanabrese
Asturleonese of the Zamora border, Ladino). Built to validate the TTS voice of
each lect (synthesize each sentence, ASR/listen, compare against the gold IPA)
and to regression-pin sentence-level o2i behaviour.

Each lect is written in its **own** orthographic convention — Galician RAG or
reintegrado per lect, Asturian ALLA, Aragonese Academia, Catalan IEC/AVL,
Aranese per its attested convention, medieval stages period-spelled, Ladino in
its Latin convention — so a row is simply the sentence a TTS receives. There is
no separate `raw`/undiacritized column and no diacritization-gap check
(contrast the Arabic gold set, whose input contract is fully vocalized text).

The set is grown incrementally: the shipped exemplars (`es-ES`, `gl`, and the
migrated `ast-x-sanabria`) set the quality bar. `validate` gates every lect
that has a TSV and reports the rest as pending, so a lect can be authored ahead
of time without failing CI. Concurrent authors work sibling families and touch
only their own lects' TSVs; harness `LECTS` appends stay minimal and
rebase-friendly.

## Schema

TSV, tab-separated, UTF-8, header row:

| column | content |
|---|---|
| `id` | `<lect>-NNN` |
| `sentence` | the lect's genuine orthography (o2i's input) |
| `ipa` | o2i transcription of `sentence`, manually verified against the lect's cited sources |
| `gloss_en` | English translation |
| `features` | semicolon list of coverage tags (below) |
| `notes` | tool-output corrections + the citation ids (from the spec's `sources`) justifying them |

## The `ipa == transcribe(sentence, lect)` contract

The `ipa` column is exactly what o2i emits for `sentence` under that lect. The
validator recomputes it and fails on any mismatch. When o2i is wrong, **fix the
spec** (cited, against the lect's `sources`) or respell the sentence to a word
the literature attests — **never hand-edit the `ipa` column**. A gold that has
been silently patched to mask a spec bug is worse than no gold. Any correction
is recorded in `notes` with the source id that grounds it. Spec-vs-literature
gaps lead the PR body; they never bend the gold.

## Feature tags

Each phonetic tag is a predicate over `(sentence, ipa)` that the validator
recomputes per row (see `FEATURES` in `scripts/spain_romance_tts_gold.py`). A
tag may only appear on a row where its predicate is true. The axes are the ones
that actually discriminate the Romance lects of Spain:

| tag | verified by | fires when |
|---|---|---|
| `distincion` | both | a ⟨c(e/i)⟩/⟨z⟩/⟨ç⟩ grapheme **and** a `[θ]` in the ipa — the /θ/ kept distinct from /s/ (distinción; also the ceceo reflex) |
| `seseo` | both | a ⟨c(e/i)⟩/⟨z⟩/⟨ç⟩ grapheme **and** `[s]` with **no** `[θ]` in the ipa — ⟨c z⟩ merged to `[s]` (seseo) |
| `lateral_palatal` | both | a ⟨ll⟩/⟨lh⟩ grapheme **and** `[ʎ]` present — the palatal lateral retained (ll/y distinguished) |
| `yeismo` | both | a ⟨ll⟩ or prevocalic ⟨y⟩ grapheme **and** `[ʝ]` with **no** `[ʎ]` — ll/y merged to `[ʝ]` (yeísmo) |
| `palatal_nasal` | ipa | `[ɲ]` present (⟨ñ nh ny⟩) |
| `palatal_initial` | both | a word begins with ⟨ll lh ñ nh⟩ **and** `[ʎ]`/`[ɲ]` present — Asturleonese initial L-/N- palatalisation |
| `gheada` | both | a /g/-phoneme grapheme (⟨ga go gu⟩, ⟨gue gui⟩, ⟨g⟩+liquid) **and** a `[ħ]`/`[h]` in *onset* position — the Galician gheada reflex of /g/ |
| `coda_s_aspiration` | both | a coda ⟨s⟩ grapheme **and** an `[h]` in *coda* position — southern aspiration/weakening of /s/ |
| `diphthong_ie_ue` | both | a ⟨ie⟩ or (non-⟨qu/gu⟩) ⟨ue uo⟩ grapheme **and** a realised glide+mid `[je we wo]` — Romance tonic diphthongisation |
| `final_u` | both | a word ends in a full ⟨u⟩ vowel (preceded by a consonant) **and** an ipa word ends in `[u]` — Asturleonese atonic final -o>-u raising / masculine metaphony |
| `open_mid` | ipa | `[ɛ]` or `[ɔ]` present — the 7-vowel open-mid contrast (Galician/Catalan/Asturleonese) |
| `schwa` | ipa | `[ə]` present — Catalan atonic schwa reduction |
| `velar_nasal` | ipa | `[ŋ]` present — Galician coda -n / ⟨nh⟩, Catalan ⟨ng⟩ |
| `sibilant_voicing` | ipa | `[z]` or `[ʒ]` present — the voiced-sibilant contrast (present in Catalan, absent in Galician) |
| `rhotic` | ipa | a trill `[r]` (excludes the ubiquitous tap `[ɾ]`) |
| `sandhi` | both | a cross-word junction: vowel-final before vowel-initial (elision/liaison), or ⟨s⟩-final before a voiced onset (final-s voicing) |

The `orth`/`ipa`/`both` split mirrors the other gold sets: an axis whose
*reflex* varies across lects is witnessed by the stable grapheme, while a
realised reflex is read off the transcription. The `both` predicates require an
orthographic trigger **and** the predicted, **position-tied** ipa so the tag
proves the row genuinely exercises the axis.

### Position-tied predicates

Two axes share the fricative symbol space and must be disambiguated by
position, exactly as the Portuguese set's `coda_sibilant` was: gheada is /g/ →
`[ħ]`/`[h]` in **onset** (before a vowel), while aspirated coda /s/ is `[h]` in
**coda** (before a consonant or a boundary). `gheada` fires only on an onset
fricative and `coda_s_aspiration` only on a coda one, so an unrelated fricative
elsewhere in the utterance never triggers the tag. Likewise `diphthong_ie_ue`
excludes the mute ⟨u⟩ of ⟨que qui gue gui⟩ (so `aquel`/`pequeño` do not count)
and `final_u` requires the ⟨u⟩ to follow a consonant (so a falling-diphthong
glide ⟨…ou⟩ does not count).

### Honestly-inapplicable axes

An axis a lect genuinely lacks is left off its rows, and the absence is stated
in the row's `notes` where relevant. Standard `gl` has no gheada (/g/ stays
`[ɡ]`), no yeísmo (⟨ll⟩ keeps the lateral `[ʎ]`), no Romance diphthongisation
(`fronte`/`torce`, not `fuente`/`tuerce`), and no voiced sibilants (the
Galician side of the Catalan/Galician `sibilant_voicing` contrast) — these are
recorded, never faked. A gheada-realising Galician sub-lect exercises `gheada`
where its spec produces the reflex.

Shape tags (not machine-verified): `statement`, `question`, `negation`,
`imperative`, `number`.

## Sentence frames

Each lect's 20 sentences cover the same shared semantic frames plus coverage
rows, so the sets are comparable across lects while each stays faithful to its
own register:

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
15–20. coverage rows filling the phonetic tags a lect's frames 1–14 left
uncovered (strong rhotic, palatals, open-mid, velar nasal, and the lect's own
discriminative axes — distinción/seseo, yeísmo, diphthongisation, final -u).

## Register rule

Each lect uses its **genuine** regional lexicon and morphology **where the
literature the spec cites attests it** — never an invented shibboleth, never
Castilian-with-an-accent. Galician draws on `mercar`, `paxaro`, `rúa`;
Asturleonese Sanabrese keeps `cuostan`, `buonas`, `you`, `ye`; Aragonese uses
its Academia forms; Catalan/Valencian its IEC/AVL register. When a regional
form is not documented in the lect's `sources`, fall back to the neutral
standard rather than guess.

## Sandhi-rich authoring

Iberian Romance phonology lives at the word boundary: vowel elision/liaison and
`/s/` voicing across a junction are what a TTS most often gets wrong. Sentences
are authored to be **sandhi-rich** — most rows carry at least one `sandhi`
junction — so the gold exercises connected-speech behaviour, not just
isolated-word transcription.

## Procedure (how to add sentences)

1. `python scripts/spain_romance_tts_gold.py checklist <lect>` — prints the
   dialect-discriminative feature checklist and which tags the current gold
   already covers.
2. Author 20 sentences over the frames + coverage rows in the lect's genuine
   orthography, grounding the lexicon in the literature the lect's spec cites.
   Reuse words the spec's own primary-source gold attests so a row doubles as a
   primary-source witness.
3. `python scripts/spain_romance_tts_gold.py draft <lect> <textfile>` — machine
   first-draft: o2i IPA + auto-tagged feature axes. Author the `gloss_en` and
   the `notes` citation id by hand.
4. Verify the IPA against the spec's phoneme mappings and sources. If o2i is
   wrong, **fix the spec** (cited) — never hand-edit the IPA column.
5. `python scripts/spain_romance_tts_gold.py validate` must pass
   (`tests/test_spain_romance_tts_gold.py` runs it in CI).

## Reconciliation procedure (spec change vs. gold)

The `ipa == transcribe(sentence, lect)` contract makes the gold a regression
pin. When a spec edit changes a transcription, `validate` fails with the stored
vs. recomputed IPA. Reconcile deliberately, never by silencing the check:

1. **Is the new transcription more accurate** against the lect's cited sources?
   Then the gold was pinning an old, less-correct output. Update the `ipa`
   column by **regenerating it from the engine** (`draft`, or copy the `got:`
   line), re-verify the feature tags against the new IPA, and note the spec
   change with its source id. The gold moves *with* the corrected spec.
2. **Is the new transcription wrong** (a regression the spec edit introduced)?
   Then the gold caught a real bug — fix the spec, do not touch the gold.
3. **Is it a genuine spec-vs-literature gap** (the engine cannot yet reach the
   attested form)? Lead the PR body with it, respell the sentence to a form the
   spec transcribes correctly *and* the literature attests, and keep the gap on
   the record. Never hand-edit `ipa` to the desired value.

## Per-lect grounding highlights

- **es-ES** (Castilian, standard peninsular): distinción ⟨c z⟩ → `[θ]`, yeísmo
  ⟨ll y⟩ → `[ʝ]` (the standard peninsular merger), Romance diphthongisation
  Ĕ>ie / Ŏ>ue, palatal nasal `[ɲ]`, trill/tap `[r]`/`[ɾ]` contrast, sandhi
  (Hualde 2005; Penny 2002; Harris 1969).
- **gl** (Galician, RAG standard): distinción kept (no seseo), palatal lateral
  `[ʎ]` kept (no yeísmo), 7-vowel open-mid `[ɛ ɔ]`, phonemic velar nasal `[ŋ]`
  (coda -n and the ⟨nh⟩ grapheme, `unha`), `[ʃ]` from historical sibilants, and
  gheada honestly absent in the standard — a gheada sub-lect exercises the axis
  where its spec produces `[ħ]` (Regueira 1996; Freixeiro Mato 1998; Carballo
  Calero 1979).
- **ast-x-sanabria** (Sanabrese Asturleonese): migrated from the Portuguese
  gold set (it is a Spain-territory lect). Tonic Ŏ>/wo/ (`cuostan`, `buonas`),
  initial L->`[ʎ]`/N->`[ɲ]` palatalisation, distinción `[θ]`, atonic final
  -o>-u, and a four-way sibilant system — re-tagged to the Spain-Romance
  predicates (Frías Conde; García Arias 2003).
