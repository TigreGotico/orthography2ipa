# Arabic TTS gold set

`orthography2ipa/data/gold/arabic_tts/<code>.tsv` — 5–6 fully diacritized,
phonetically diverse, literature-justified sentences for each of the 25
concrete Arabic lects in the catalogue. Built to validate Arabic TTS voices
per dialect (synthesize each sentence, ASR/listen, compare against the gold
IPA) and to regression-pin sentence-level o2i behaviour.

Beside the concrete lects, the five **grouping (proto/koine) nodes**
(`ar-x-gulf`, `ar-x-levantine`, `ar-x-maghrebi`, `ar-x-mashriqi`,
`ar-x-peninsular`) each carry a 20-row set whose register is **pan-group** —
the sentence lexicon is restricted to items attested across the group's leaves
(e.g. Gulf `šlon`/`wāyid`, Levantine `qaddēsh`/`baddi`, pan-Maghrebi
`bzzāf`/`shri` in the Heath/Marçais sense) rather than any single leaf's
idiolect. A grouping node deliberately does not *pick* a reflex where its
leaves diverge; the gold therefore **surfaces the node's rank-1 candidate
ranking** (e.g. `ar-x-maghrebi` keeps `/q/` and ʒ-first ǧīm; `ar-x-peninsular`
keeps fricative-first interdentals and retained diphthongs; `ar-x-gulf`/
`ar-x-levantine` monophthongize ay/aw→ē/ō). That surfacing is the node's
documented behaviour and is noted per row, not fought.

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
lect plus at least a question, a negation, a number and an imperative.

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
- **ar-SA-x-qassim** (Qaṣīm, Najdi sub-variety): the Najdi velar affrication
  [ts]/[dz] plus **monophthongization** /aj aw/→[eː oː] (loːnak, joːm, bureːda)
  which the central-Najdi parent lacks (Alhoody 2019:42; Al-Rojaie 2013).
- **ar-SA-x-rijal-alma** (SW ʿAsīr/Tihāmah): the archaic **lateral emphatics** —
  ض→[ɮˤ] voiced, ظ→[ɬˤ] voiceless, kept distinct — and qaf-retention [q]
  (Watson & Al-Azraqi 2011; Asiri 2009; Al-Azraqi 2010).
- **ar-SA-x-sharqiyya** (Eastern Province, Gulf-type): Baḥārna ج→[j] lenition,
  kaf→[tʃ] affrication, qaf→[ɡ] (Johnstone 1967; Holes 2004; Al-Taisan 2022).
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
