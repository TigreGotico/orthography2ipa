# Atlantic Iberian-creole TTS gold set

`orthography2ipa/data/gold/creoles_atlantic_tts/<code>.tsv` — 20 phonetically
diverse, register-appropriate, literature-justified sentences for each of the
Iberian-lexified Atlantic creoles:

| code | language | orthography | shelf |
|---|---|---|---|
| `kea` | Kabuverdianu (Cape Verdean Creole) | ALUPEC | Upper Guinea |
| `pov` | Guinea-Bissau Kriol (GBC) | Kihm / Scantamburlo convention | Upper Guinea |
| `pre` | Principense (Lung'ie) | Gulf-of-Guinea community spelling | Gulf of Guinea |
| `aoa` | Angolar (Ngola) | Gulf-of-Guinea community spelling | Gulf of Guinea |
| `cri` | Sãotomense / Forro / Santome | ALUSTP | Gulf of Guinea |

Built to validate the TTS voice of each creole (synthesize each sentence,
ASR/listen, compare against the gold IPA) and to regression-pin sentence-level
o2i behaviour.

Each row is written in the creole's **own** community/standard orthography, in
**genuine creole register** — TMA particles (`ta`/`ka`/`na`/`sa`), invariant
nouns and adjectives with no gender or number agreement, and the creole pronoun
paradigms — **not** the Portuguese lexifier. A row is simply the sentence a TTS
receives; there is no separate `raw`/undiacritized column.

The set is grown incrementally: `validate` gates every lect that has a TSV and
reports the rest as pending. Concurrent authors work sibling families and touch
only their own lects' TSVs; the harness `LECTS` list stays append-friendly.

## Not the lexifier: which Iberian-Romance axes are inapplicable

These creoles do **not** share the Iberian-Romance harness axes of the
Spain-Romance / Portuguese gold sets, and those axes are not modelled here:

- no /θ~s/ distinción / seseo / ceceo (no Iberian sibilant-merger axis);
- no yeísmo / ll–y contrast;
- no Romance ⟨ie ue⟩ diphthongisation (creole vowels descend from the lexifier
  tonic outcomes, not from Latin Ĕ/Ŏ);
- no gheada, no coda-/s/ aspiration as a lect-discriminating variable.

What discriminates *this* family is its own inventory, and those are the axes
the harness models below.

## Schema

TSV, tab-separated, UTF-8, header row:

| column | content |
|---|---|
| `id` | `<lect>-NNN` |
| `sentence` | the creole's genuine orthography (o2i's input) |
| `ipa` | o2i transcription of `sentence` (NFC), verified against the lect's cited sources |
| `gloss_en` | English translation |
| `features` | semicolon list of coverage tags (below) |
| `notes` | corrections + the citation ids (from the spec's `sources`) grounding them |

## The `ipa == transcribe(sentence, lect)` contract

The `ipa` column is exactly what o2i emits for `sentence` under that lect. The
validator recomputes it and fails on any mismatch. When o2i is wrong, **fix the
spec** (cited) or respell the sentence to a word the literature attests —
**never hand-edit the `ipa` column**. Spec-vs-literature gaps lead the PR body;
they never bend the gold.

## Feature tags

Each phonetic tag is a predicate over `(sentence, ipa)` recomputed per row (see
`FEATURES` in `scripts/creoles_atlantic_tts_gold.py`). A tag may only appear on
a row where its predicate is true.

| tag | verified by | fires when |
|---|---|---|
| `nasal_vowel` | ipa | a vowel carries a combining tilde — a phonemic nasal vowel (all five lects) |
| `affricate` | ipa | `[tʃ]` or `[dʒ]` present — the creole tx/dj affricates |
| `postalveolar` | ipa | `[ʃ]` or `[ʒ]` present — ⟨x⟩ `[ʃ]`, ⟨j⟩ `[ʒ]` |
| `coda_sibilant` | ipa | a word ends in `[ʃ]`/`[ʒ]` — kea coda /s/, cri ⟨x⟩ coda |
| `prenasal_stop` | both | a word-initial ⟨mb nd ng⟩ **and** `[mb]`/`[nd]`/`[ŋɡ]` in the ipa — the Gulf-of-Guinea / substrate prenasalised onset |
| `labial_velar` | both | a ⟨gb⟩/⟨kp⟩ digraph **and** `[ɡ͡b]`/`[k͡p]` in the ipa — the Niger-Congo labial-velar stop |
| `open_mid` | ipa | `[ɛ]` or `[ɔ]` present — the seven-vowel open-mid contrast (cri bare ⟨e o⟩) |
| `palatal_nasal` | ipa | `[ɲ]` present (⟨nh⟩) |
| `velar_nasal` | ipa | `[ŋ]` present |
| `velarized_l` | ipa | `[ɫ]` present — kea velarised coda /l/ |
| `strong_rhotic` | ipa | `[ʀ]` or `[r]` present — kea word-initial/⟨rr⟩ strong rhotic; pov alveolar /r/ (excludes the tap `[ɾ]`) |
| `tap` | ipa | `[ɾ]` present — single intervocalic ⟨r⟩ |
| `stress` | ipa | a `[ˈ]` in the ipa (kea; the Gulf-of-Guinea specs assign no stress) |

Non-phonetic shape / morphosyntax tags (allowed, not machine-verified):
`statement`, `question`, `negation`, `imperative`, `tma` (a tense-mood-aspect
particle), `no_agreement` (invariant noun/adjective), `pronoun`, `plural`,
`copula`.

## Per-lect axis applicability

- **kea** assigns stress and has a velarised coda /l/, a strong-rhotic vs tap
  contrast, and coda /s/ → `[ʃ]`; it has no labial-velar stops and no
  prenasalised onsets.
- **pov** has the tx/dj affricates, coda sibilants, palatal and velar nasals,
  and an alveolar /r/; it assigns no stress. Nasal vowels are a spec-listed
  feature but reachable in the engine only from explicit tilde spelling (see
  Leads).
- **pre / aoa** carry the Gulf-of-Guinea labial-velar stops ⟨gb kp⟩ and
  prenasalised onsets; **aoa** marks nasality with the circumflex, and both
  have lexical tone that the community orthography does not write (not modelled).
- **cri** is the seven-vowel lect: bare ⟨e o⟩ are open-mid `[ɛ ɔ]`, ⟨ê ô⟩ are
  close-mid `[e o]`; it has ⟨gb⟩ but not ⟨kp⟩, prenasalised onsets, and a coda
  ⟨x⟩ `[ʃ]`; it assigns no stress (contested in the literature, unwritten in
  ALUSTP).

## Leads (spec/engine gaps surfaced while authoring — never bent into gold)

Recorded in the PR body when a gold row cannot exercise a spec-claimed axis; the
gold stays engine-pinned and honest rather than papered over.
