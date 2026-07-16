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

The set is grown incrementally. The three shipped Asian exemplars (`mcm`,
`idb`, `vkp`) set the quality bar; `validate` gates every lect that has a TSV
and reports the rest (`kea`, `pov`, `pre`, `aoa`, `cri`, `pap`, `cbk-zam`,
`pln`) as pending, so a lect can be authored ahead of time without failing CI.
Concurrent authors work sibling families and touch only their own lects' TSVs;
harness `LECTS` appends stay minimal and rebase-friendly.

## Which variety each ISO code models

The ISO 639-3 code does not always name the concrete variety the o2i spec
models — the spec's `notes` are authoritative:

| code | spec models | register / orthography |
|---|---|---|
| `mcm` | Kristang / Papiá Kristang (Malacca Creole Portuguese) | Baxter's Malay-based practical orthography (Baxter 1988; Baxter & de Silva 2004) |
| `idb` | **Sri Lanka Portuguese Creole** (Batticaloa/Trincomalee Burgher) — **not** Diu/Daman | Cardoso's scholarly Latin convention (doubled vowels for length, `nh ng ch j`, IPA `ɛ ɔ`) |
| `vkp` | Korlai Indo-Portuguese ("Kristi", Maharashtra) | Clements' scholarly transcription (Roman + IPA: `ɛ ɔ ʈ ɖ`, tilde nasals, `ï`, `bh/kh/th` aspirates) |

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

Each phonetic tag is a predicate over the emitted `ipa` that the validator
recomputes per row (see `FEATURES` in `scripts/iberian_creole_tts_gold.py`). A
tag may only appear on a row where its predicate is true. The axes are the ones
that discriminate these creoles from their Iberian lexifiers and from one
another:

| tag | fires when |
|---|---|
| `retroflex` | a retroflex `[ʈ ɖ ɳ ɭ ɽ]` surfaces — Korlai Marathi-contact stops, Sri Lanka `[ɳ ɭ]` allophones after back vowels |
| `aspirated` | an aspirated/breathy stop `[…ʰ]`/`[…ʱ]` surfaces (Korlai `bh kh th dh gh`) |
| `nasal_vowel` | a phonemic nasal vowel (tilde) surfaces — Korlai keeps `/ĩ ũ ɛ̃ ɔ̃/`; Kristang and Sri Lanka denasalised them |
| `nasal_coda` | a nasal stands in coda (word-final or preconsonantal) — the denasalisation reflex and cluster codas |
| `prenasal_cluster` | a homorganic nasal+stop/affricate cluster surfaces (`mb nd ŋɡ ndʒ ɳɖ …`) |
| `syllabic_nasal` | a syllabic or word-initial onset nasal surfaces (Kristang `ngua`, `nsentu`, `ngka`) |
| `affricate` | a retained affricate `[tʃ dʒ ts dz]` surfaces (medieval `ch`/`j`; Korlai `ts dz`) |
| `palatal_nasal` | `[ɲ]` surfaces (`ny` Kristang, `nh` Sri Lanka) |
| `velar_nasal` | `[ŋ]` surfaces |
| `vowel_length` | a long vowel `[ː]` surfaces (Sri Lanka phonemic length) |
| `open_mid` | `[ɛ]` or `[ɔ]` surfaces |
| `schwa` | `[ə]` surfaces (Korlai central vowel `ï`) |
| `approximant_v` | `[ʋ]` surfaces — etymological `/v/` as a South-Asian labial approximant |
| `rhotic_trill` | a trilled `[r]` surfaces (excludes the tap `[ɾ]`) |
| `glide` | a `[j]` or `[w]` glide surfaces |

Non-phonetic **shape** tags (`statement`, `question`, `negation`, `imperative`,
`number`) are allowed and not machine-verified.

## Running the harness

```
python scripts/iberian_creole_tts_gold.py checklist mcm      # coverage report
python scripts/iberian_creole_tts_gold.py draft vkp lines.txt # first-draft rows
python scripts/iberian_creole_tts_gold.py validate           # CI gate (all lects)
```

`tests/test_iberian_creole_tts_gold.py` runs `validate` in CI.
