# Arabic TTS gold set

`orthography2ipa/data/gold/arabic_tts/<code>.tsv` — 5 fully diacritized,
phonetically diverse, literature-justified sentences for each of the 25
concrete Arabic lects in the catalogue. Built to validate Arabic TTS voices
per dialect (synthesize each sentence, ASR/listen, compare against the gold
IPA) and to regression-pin sentence-level o2i behaviour.

## Schema

TSV, tab-separated, UTF-8, header row:

| column | content |
|---|---|
| `id` | `<lect>-NNN` |
| `sentence` | fully diacritized dialectal orthography (o2i's Arabic input contract) |
| `raw` | undiacritized form — what a TTS normally receives; equals `sentence` stripped of ḥarakāt |
| `ipa` | o2i transcription of `sentence`, manually verified against the lect's cited sources |
| `gloss_en` | English translation |
| `features` | semicolon list of coverage tags (below) |
| `notes` | tool-output corrections + the citation ids (from the spec's `sources`) justifying them |

## Procedure (how to add sentences)

1. `python scripts/arabic_tts_gold.py checklist <lect>` — prints the
   dialect-discriminative feature checklist and which tags the current gold
   already covers.
2. Author sentences in dialectal orthography covering the missing tags.
   Ground the lexicon in the literature the lect's spec cites (Badawi &
   Hinds for Cairene, Cowell for Levantine, Erwin/Blanc for Iraqi, Ingham
   for Najdi, Watson for Ṣanʿānī, Dickins for Sudanese, Harrell/Heath for
   Darija, Holes/Al-Balushi/Alshammari for Gulf, …) and/or attested corpus
   material (PADIC, QADI, EDC, SDC — used for lexical attestation only,
   sentences are authored, not copied).
3. `python scripts/arabic_tts_gold.py draft <lect> <textfile>` — machine
   first-draft: text2tashkeel (`rawi-ensemble`) diacritization + o2i IPA.
   text2tashkeel is **MSA-only**: for dialects its output is out-of-domain
   and every deviation you keep or correct must be justified in `notes`
   with a citation id. MSA/Classical drafts still need review (case
   endings, wasl).
4. Verify the IPA against the spec's phoneme mappings and sources. If o2i
   is wrong, **fix the spec** (and re-run
   `scripts/gen_arabic_orthography_keys.py` if a letter mapping changed) —
   never hand-edit the IPA column.
5. `python scripts/arabic_tts_gold.py validate` must pass
   (tests/test_arabic_tts_gold.py runs it in CI).

## Feature tags

Machine-verified (see `FEATURES` in the script): `qaf`, `jim`,
`interdental`, `kaf`, `hamza`, `ta_marbuta`, `sun_assim` (verified on the
raw orthography — the *reflex* varies per dialect, the grapheme is the
witness); `emphatic`, `pharyngeal`, `geminate`, `long_vowel`, `diphthong`
(verified on the IPA). Shape tags (not machine-verified): `statement`,
`question`, `negation`, `imperative`, `number`.

Every lect's 5 sentences jointly cover the phonetic tags present in that
lect plus at least a question, a negation and a number.

## Vocalized connected-speech conventions

The gold follows the vocalized-orthography conventions encoded by
`scripts/gen_arabic_orthography_keys.py` (sun-letter assimilation written
as shadda on the sun letter, proclitic + article contractions, tā marbūṭa
liaison, tanwīn seat alif, wasl elision) — see that script's docstring for
the rules and their Ryding/Watson grounding. Dialect sentences use the
colloquial article spelling their literature uses (Cairene/Baghdadi
`اِلْ‍` /il/, Levantine `عَ ال‍` contraction, …).

## Per-lect grounding highlights

- **arb** keeps Sibawayhi's lateral-emphatic ض [ɮˤ]; **ar** (MSA) uses the
  merged stop [dˤ] (spec notes; Versteegh 2001).
- **ar-EG**: ج=/ɡ/, ق=/ʔ/, stop interdentals, `اِلْ‍` article (Badawi &
  Hinds 1986; Mitchell 1956).
- **Levantine** (SY/LB/JO/PS): ق=/ʔ/ (JO koine /g/), ج=/ʒ/ (JO /dʒ/),
  ay/aw→ē/ō, final imala ‑e written `ِة` (Cowell 1964; Almbark & Hellmuth
  2015; Al-Wer 2020; Cotter 2016). Beiruti ā→ē fronting surfaces heavily
  (ar-LB spec rule).
- **ar-IQ** (gilit): ق=/ɡ/ (written گ), ك→چ /tʃ/, interdentals retained,
  ay/aw→ē/ō added to the spec with Erwin 1963 grounding;
  **ar-IQ-x-qeltu** keeps /q/ and plain /k/ (Blanc 1964 — the qeltu/gilit
  split is the pair's diagnostic).
- **ar-SD**: ج=/ɟ/ palatal stop, ق=/ɡ/, zōl/dāyir lexicon (Dickins 2007).
- **ar-TD / ar-NG**: g-dialect qaf — spec reflexes reordered with Owens
  1993 added as source; n‑ 1sg imperfect frames.
- **Gulf** (AE/BH/KW/QA): ق=/ɡ/, چ /tʃ/ kaf-affrication, interdentals
  retained, ē/ō monophthongs added to ar-x-gulf (Holes 2004; Alshammari
  2026); **ar-OM** is the sedentary control: /q/, plain /k/, retained
  diphthongs (Al-Balushi 2016).
- **ar-SA-x-najd**: gahawah-syndrome epenthesis surfaces (gahawa, aḥamar —
  Ingham 1994); **ar-SA-x-hejaz**: urban stop interdentals + Cairene-like
  register (Omar 1975; Abdoh 2010). **ar-YE**: aští verb, retained
  diphthongs/interdentals (Watson 2002).
- **Maghrebi** (MA/TN/DZ/LY/MR): heavy initial clusters, ma-...-š
  negation, n‑ 1sg; ma-ṭīša/zwīn/bzzāf (Harrell 1962; Heath 2020), barša/
  bāhi (TN), mlīḥ/wāš rāk (DZ, PADIC-attested), halba/nibbi (LY — ق=/ɡ/
  with Pereira 2008 added as source), Hassaniya interdental retention
  (Versteegh 2001 ch.10). Tunis interdental retention restored with Gibson
  2009 (EALL) added as source.

## Known limits

- Skeleton-tier lects (TD, NG, TN, DZ, LY, MR) have thinner spec grounding;
  their sentences stick to well-attested pan-regional features.
- text2tashkeel is MSA-only; all dialect tashkeel here is hand-set.
- The IPA is broad and pre-pausal tanwīn is kept (full style).
