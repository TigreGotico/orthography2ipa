# Iberian-creole TTS gold set

`orthography2ipa/data/gold/iberian_creole_tts/<code>.tsv` — 20 phonetically
diverse, register-appropriate, literature-justified sentences for each of the
Portuguese- and Spanish-lexified creoles traceable to the Iberian expansion:
the Upper Guinea, Gulf of Guinea, South and Southeast Asian Portuguese creoles
and the Iberian creoles of the Caribbean and the Philippines. Built to validate
the TTS voice of each creole (synthesize each sentence, ASR/listen, compare
against the gold IPA) and to regression-pin sentence-level o2i behaviour.

Each lect is written in its **own** convention. Where a community orthography
has stabilised it is used (Baxter's Malay-based practical spelling for
Kristang); where the community has no stable written form the gold uses the
scholarly Latin transcription the documentation itself uses — Cardoso's
convention for Sri Lanka Portuguese, Clements' transcription for Korlai — so a
row is simply the string a TTS receives. There is no separate
`raw`/undiacritized column.

The sentences carry genuine creole morphosyntax — preverbal TMA particles,
creole pronoun sets, reduced verb paradigms, substrate lexicon — not relexified
Portuguese or Spanish. Attested example forms from the sources (APiCS surveys
40–42, Baxter, Cardoso, Clements) are used verbatim wherever possible.

This is the single harness for the whole creole roster — the three shelves are
authored and gated together:

- **South / Southeast-Asian Portuguese creoles**: `mcm` (Kristang), `idb` (Sri
  Lanka Portuguese), `vkp` (Korlai Indo-Portuguese);
- **Upper- and Gulf-of-Guinea Atlantic creoles**: `kea` (Kabuverdianu), `pov`
  (Guinea-Bissau Kriol), `pre` (Principense), `aoa` (Angolar), `cri`
  (Sãotomense/Forro);
- **Spanish-lexified Caribbean / Philippine creoles**: `pap` (Papiamento),
  `cbk-zam` (Chavacano), `pln` (Palenquero).

The set is grown incrementally: `validate` gates every lect that has a TSV and
reports the rest as pending, so a lect can be authored ahead of time without
failing CI. Concurrent authors work sibling shelves and touch only their own
lects' TSVs; the harness `LECTS` list stays append-friendly. The `pap`,
`cbk-zam` and `pln` rows were consolidated here from the Spain-Romance gold set
(they are creoles, not Iberian Romance) and re-tagged to the creole predicates;
the `kea`/`pov`/`pre`/`aoa`/`cri` rows were merged from the former Atlantic
creole harness.

## Which variety each ISO code models

The ISO 639-3 code does not always name the concrete variety the o2i spec
models — the spec's `notes` are authoritative:

| code | spec models | register / orthography |
|---|---|---|
| `mcm` | Kristang / Papiá Kristang (Malacca Creole Portuguese) | Baxter's Malay-based practical orthography (Baxter 1988; Baxter & de Silva 2004) |
| `idb` | **Sri Lanka Portuguese Creole** (Batticaloa/Trincomalee Burgher) — **not** Diu/Daman | Cardoso's scholarly Latin convention (doubled vowels for length, `nh ng ch j`, IPA `ɛ ɔ`) |
| `vkp` | Korlai Indo-Portuguese ("Kristi", Maharashtra) | Clements' scholarly transcription (Roman + IPA: `ɛ ɔ ʈ ɖ`, tilde nasals, `ï`, `bh/kh/th` aspirates) |
| `kea` | Kabuverdianu (Cape Verdean Creole) | ALUPEC (Upper Guinea shelf) |
| `pov` | Guinea-Bissau Kriol (GBC) | Kihm / Scantamburlo convention (Upper Guinea shelf) |
| `pre` | Principense (Lung'Ie) | Gulf-of-Guinea community spelling |
| `aoa` | Angolar (Ngola) | Gulf-of-Guinea community spelling (circumflex nasality; tone unwritten) |
| `cri` | Sãotomense / Forro / Santome | ALUSTP; seven-vowel lect (bare ⟨e o⟩ = `[ɛ ɔ]`) |
| `pap` | Papiamento (Curaçao) | Curaçao phonemic spelling (`k` not `c`, grave ⟨ò⟩) |
| `cbk-zam` | Chavacano (Zamboangueño Spanish creole) | Zamboangueño practical spelling |
| `pln` | Palenquero (San Basilio de Palenque) | Spanish-based practical spelling (prenasal ⟨nd ng⟩, postposed `nu`) |

## Schema

TSV, tab-separated, UTF-8, header row:

| column | content |
|---|---|
| `id` | `<lect>-NNN` |
| `sentence` | the lect's genuine convention (o2i's input) |
| `ipa` | o2i transcription of `sentence`, verified against the lect's cited sources |
| `gloss_en` | English translation |
| `features` | semicolon list of coverage tags (below) |
| `notes` | tool-output corrections + the citation ids (from the spec's `sources`) justifying them |

## The `ipa == transcribe(sentence, lect)` contract

The `ipa` column is exactly what o2i emits for `sentence` under that lect. The
validator recomputes it and fails on any mismatch. When o2i is wrong, **fix the
spec** (cited, against the lect's `sources`) or respell the sentence to a form
the literature attests — **never hand-edit the `ipa` column**. Any correction
is recorded in `notes` with the source id that grounds it. Spec-vs-literature
gaps lead the PR body; they never bend the gold.

## Feature tags

Each phonetic tag is a predicate over `(sentence, ipa)` that the validator
recomputes per row (see `FEATURES` in `scripts/iberian_creole_tts_gold.py`). A
tag may only appear on a row where its predicate is true. Most axes are read
directly off the emitted `ipa` (verified by `ipa`); the two position-tied
Atlantic axes require an orthographic trigger **and** the predicted ipa
(verified by `both`), so the tag proves the row genuinely exercises the axis.
The roster is the union of the three shelves' diagnostic axes:

| tag | verified by | fires when |
|---|---|---|
| `retroflex` | ipa | a retroflex `[ʈ ɖ ɳ ɭ ɽ]` surfaces — Korlai Marathi-contact stops, Sri Lanka `[ɳ ɭ]` allophones after back vowels |
| `aspirated` | ipa | an aspirated/breathy stop `[…ʰ]`/`[…ʱ]` surfaces (Korlai `bh kh th dh gh`) |
| `nasal_coda` | ipa | a nasal stands in coda (word-final or preconsonantal) — the denasalisation reflex and cluster codas |
| `prenasal_cluster` | ipa | a homorganic nasal+stop/affricate cluster surfaces anywhere (`mb nd ŋɡ ndʒ ɳɖ …`) |
| `syllabic_nasal` | ipa | a syllabic or word-initial onset nasal surfaces (Kristang `ngua`, `nsentu`, `ngka`) |
| `vowel_length` | ipa | a long vowel `[ː]` surfaces (Sri Lanka phonemic length) |
| `approximant_v` | ipa | `[ʋ]` surfaces — etymological `/v/` as a South-Asian labial approximant |
| `glide` | ipa | a `[j]` or `[w]` glide surfaces |
| `prenasal_stop` | both | a word-initial ⟨mb nd ng mp⟩ **and** `[mb]`/`[nd]`/`[ŋɡ]`/`[mp]` in the ipa — the Gulf-of-Guinea / substrate prenasalised onset |
| `labial_velar` | both | a ⟨gb⟩/⟨kp⟩ digraph **and** `[ɡ͡b]`/`[k͡p]` in the ipa — the Niger-Congo labial-velar stop (pre/aoa/cri) |
| `postalveolar` | ipa | `[ʃ]` or `[ʒ]` surfaces — ⟨x⟩ `[ʃ]`, ⟨j⟩ `[ʒ]`, Caribbean coda /s/ → `[ʃ]` |
| `coda_sibilant` | ipa | a word ends in `[ʃ]`/`[ʒ]` — kea coda /s/, cri ⟨x⟩, pap coda /s/ |
| `velarized_l` | ipa | `[ɫ]` surfaces — kea velarised coda /l/ |
| `tap` | ipa | `[ɾ]` surfaces — single intervocalic ⟨r⟩ |
| `stress` | ipa | a `[ˈ]` in the ipa (kea; the Gulf-of-Guinea specs assign no stress) |
| `nasal_vowel` | ipa | a phonemic nasal vowel (tilde) surfaces — Korlai `/ĩ ũ ɛ̃ ɔ̃/`, the Atlantic ⟨ã ẽ ĩ õ ũ⟩; Kristang and Sri Lanka denasalised them |
| `affricate` | ipa | a `[tʃ dʒ ts dz]` affricate surfaces (medieval `ch`/`j`, creole `tx`/`dj`; Korlai `ts dz`) |
| `palatal_nasal` | ipa | `[ɲ]` surfaces (`ny` Kristang, `nh` Sri Lanka/kea, `ñ` Caribbean) |
| `velar_nasal` | ipa | `[ŋ]` surfaces |
| `open_mid` | ipa | `[ɛ]` or `[ɔ]` surfaces (Sri Lanka; the cri seven-vowel contrast; pap ⟨ò⟩) |
| `schwa` | ipa | `[ə]` surfaces (Korlai central vowel `ï`) |
| `strong_rhotic` | ipa | a `[ʀ]`/`[r]` strong rhotic surfaces (excludes the tap `[ɾ]`) — Asian trill, kea word-initial/⟨rr⟩, pov alveolar /r/ |

The former `rhotic_trill` tag (`[r]` only) is folded into `strong_rhotic`
(`[ʀ]` or `[r]`); the Asian rows were re-tagged. `prenasal_cluster` (any-position
homorganic NC, read off the ipa) and `prenasal_stop` (word-initial onset,
position-tied to the orthography) are kept as distinct axes — both may fire on
one row.

Non-phonetic **shape / morphosyntax** tags are allowed and not machine-verified:
`statement`, `question`, `negation`, `imperative`, `number`, `tma` (a
tense-mood-aspect particle), `no_agreement` (invariant noun/adjective),
`pronoun`, `plural`, `copula`.

## Which lexifier axes are inapplicable

The Spanish- and Portuguese-lexified creoles do **not** share the Iberian-Romance
harness axes (distinción/seseo/ceceo, yeísmo, Romance ⟨ie ue⟩ diphthongisation,
gheada, coda-/s/ aspiration as a lect-discriminating variable). Those axes are
inapplicable by construction and are not modelled here; when the `pap`/`cbk-zam`/
`pln` rows moved in from the Spain-Romance set their Romance-specific tags
(`seseo`, `gheada`, `final_u`, `sandhi`) were dropped and the rows re-tagged to
the creole predicates their ipa genuinely exercises (the `pap` coda /s/ → `[ʃ]`,
for instance, surfaces as `postalveolar`/`coda_sibilant`; the Palenquero
prenasalised ⟨nd ng⟩ as `prenasal_stop`). What discriminates *these* families is
their own inventory — the axes above.

## Running the harness

```
python scripts/iberian_creole_tts_gold.py checklist mcm      # coverage report
python scripts/iberian_creole_tts_gold.py draft vkp lines.txt # first-draft rows
python scripts/iberian_creole_tts_gold.py validate           # CI gate (all lects)
```

`tests/test_iberian_creole_tts_gold.py` runs `validate` in CI.
