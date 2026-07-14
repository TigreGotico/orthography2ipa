# Primary-source gold

Example transcriptions mined from the **primary sources the language specs
themselves cite** — the grammars, phonology monographs and theses listed in each
spec's `sources` array. Every row is a worked example printed by the linguist who
described the variety, together with the printed page it stands on.

This is the only gold in the harness where each row can be checked against a
named page of a named document. It is small; that is the point. It is meant to be
*diagnostic* (does the engine reproduce what the source we cite actually says?),
not to certify a language on its own.

- `rows.jsonl` — one JSON object per example.
- `sources.json` — the bibliography, with the URL, the access status and, per
  source, **how its printed folio maps to the PDF page index** (they diverge; the
  `page` field is always the *printed* page).

## Schema

| field | meaning |
|---|---|
| `id` | `<source>-NNN` |
| `source` | key into `sources.json` |
| `page` | **printed** page (from the document's own running head/footer), never the PDF page index |
| `lang` | o2i spec code, or `null` where no mapping is defensible |
| `source_variety` | the variety label the source itself uses |
| `orthography` | the word as printed by the source, if it printed one |
| `orthography_vocalized` | Arabic only: the same word with ḥarakāt (see below) |
| `orthography_provenance` | `as-printed` or `editor-supplied` |
| `source_notation` | the source's transcription **verbatim**, brackets and all |
| `notation_system` | `ipa` or `arabicist-transliteration` |
| `ipa` | the normalized IPA actually scored |
| `level` | `broad` (source used `/…/`) or `narrow` (source used `[…]`) |
| `gloss` | English gloss as given |
| `confidence` | `high` / `medium` / `low` |
| `notes` | conditioning, in-source disagreements, what a normalization changed |

## Row counts

| source | variety | lang | rows |
|---|---|---|---|
| Almbark & Hellmuth (2015) | Syrian (Damascene) | `ar-SY` | 11 |
| Jasim (2020), Newcastle PhD | Baghdadi Gilit | `ar-IQ` | 12 |
| Jasim (2020) | Muslawi Qəltu | `ar-IQ-x-qeltu` | 12 |
| Fadda (2016), MA thesis | Ammani | `ar-JO` | 13 |
| Cotter (2016) | Gaza City | `ar-PS` | 4 |
| Brissos (2014) | EP central-interior (CI) | `pt-PT-x-beira` | 8 |
| Brissos (2014) | EP southwestern (SW) | `pt-PT-x-alentejo` | 5 |
| **total** | | | **65** |

Broad `/…/`: 25. Narrow `[…]`: 40. `confidence`: 45 high, 18 medium, 2 low.

## Notation-normalization decisions

- **Nothing is silently coerced.** `source_notation` keeps the source's own
  string; `ipa` is the normalization, and every row that needed one says so in
  `notes`.
- **Stress.** The Arabic sources mark no stress at all; Brissos marks it with an
  apostrophe placed *after the onset* (`[l'ymɨ]`). Normalized to the IPA primary
  stress mark before the syllable (`ˈlymɨ`). The scoreboard strips stress anyway.
- **Arabicist transliteration** (Cotter 2016, which prints `ḥadīθ`, not IPA):
  `ā ī ū` → `aː iː uː`; `ḥ` → `ħ`; `y` → `j`; doubled letters → geminates; `ˤ`
  for emphasis. Rows converted this way are capped at `confidence: medium`.
  `cotter2016-004` (`hāḏa`) is `confidence: low` — the paper *argues* the Gaza
  reflex is the stop [d] while quoting a source that writes ⟨ḏ⟩, so the IPA
  follows the argument and not the letter.
- **`x` vs `χ`.** Almbark writes `/xoːd/` where o2i's Arabic specs use `/χ/`.
  Kept as printed: this is a notation difference between phonologists, not a
  claim about Syrian Arabic.
- **Arabic ḥarakāt are editor-supplied.** The Arabic sources print their examples
  in transcription, not in script. o2i's Arabic input contract is fully-diacritized
  text, so a diacritized spelling of the cited lexeme is supplied in
  `orthography_vocalized` and every such row is flagged
  `orthography_provenance: editor-supplied`. The *IPA* is the source's; the
  *spelling* is the editor's, and is the weakest link in these rows.

## Known-dubious rows

- `fadda2016-010` عَمَّان — the source gives **four** co-existing realizations
  (`[ʕammaːn] ~ [ʕammæːn] ~ [ʕammɛːn] ~ [ʕammeːn]`). A single gold IPA cannot be
  right here; the most conservative is recorded and the row is `confidence: low`.
- `cotter2016-004` هَذَا — see above.
- `jasim2020-007` سَمَك — the thesis gives **both** `[simatʃ]` (p.23) and
  `[simaʃ]` (p.25) for the same gilit word. Recorded as the affricate; the
  fricative variant is an in-source disagreement, not a typo to smooth over.
- `jasim2020-017` بَارِد — the thesis's phonemic form `/baɾid/` has a short first
  vowel where the standard spelling بارد has a long one.
- `fadda2016-011..013` are labelled with the source's own group name ("bi'ul"
  group = urban Palestinian type, which Fadda says is the base of Western Amman
  speech). They are tagged `ar-JO`, but `ar-PS` would be equally defensible.

## Where a source contradicts the spec

Recorded because disagreement is signal. Verified against the current specs by
running the engine over these rows.

1. **`ar-IQ` kaf affrication is not front-vowel-conditioned.** The spec's
   `IQ_GILIT_AFFRIC_K_BEFORE/AFTER` rules fire only next to `i iː j e eː`. Jasim
   (2020) p.25 gives `/kalb/ → [tʃalib]` 'dog', `/kabiːr/ → [tʃibiːr]` 'big',
   `/ʃubbaːk/ → [ʃubbaːtʃ]` 'window', `/samak/ → [simatʃ]` 'fish' — in every one
   of these the affricate appears next to a **non-front** vowel (and in `ʃubbaːtʃ`
   after a long back one). Gilit kaf affrication is lexicalized/historical, not
   a synchronic front-vowel allophony. o2i currently returns `ˈkalb`, `kaˈbiːr`,
   `ʃubˈbaːk`, `ˈsamak` for these.
2. **`ar-IQ` epenthesis and u-colouring are not modelled.** `/qalb/ → [ɡalˤʊb]`,
   `/kalb/ → [tʃalib]`, `[χʊbʊz]` 'bread' (p.24-25) all split the final cluster
   with an epenthetic vowel whose quality is set by the flanking consonants;
   o2i gives `ˈɡalb`, `ˈxubz`. Related: the emphatic /lˤ/ of `[ɡalˤʊb]` and the
   emphatic /rˤ/ of `[rˤabiːʕ]` are not derived either.
3. **`ar-IQ` /a/ → [ʊ] near emphatics vs the spec's [ɑ].** `/basˤal/ → [bʊsˤal]`
   (p.25); the spec's `IQ_EMPH_A_*` rules back /a/ to `[ɑ]`, giving `ˈbɑsˤɑl`.
   Both are cited to Jasim; the thesis prints the raising-to-[ʊ] form.
4. **`ar-IQ-x-qeltu` rhotic and emphasis harmony.** The spec documents /r/ → [ɣ]
   as *deliberately unmodelled* (lexically conditioned). Jasim p.23 supplies the
   evidence: `[χɛːɣ]`, `[dɛːɣ]`, `[θoːɣ]`, `[baɣid]`. Likewise the rightward
   emphasis harmony of `/naːquːs/ → [naːqoːsˤ]` (p.22) is unmodelled. The rows are
   kept so the cost of that decision is visible rather than invisible.
5. **`ar-JO` emphasis spread.** Fadda p.29 writes `sˤawt → [sˤoːtˤ]`: emphasis
   spreads onto the final /t/. o2i gives `ˈsˤoːt`. Also, the `ar-JO` spec cites
   this very example as "Fadda 2016:30" — the table is on **printed page 29**.
6. **`ar-JO` final imāla.** `[ħɪlwɛ]` 'beautiful' vs `[bɪʃʕa]` 'ugly' (p.30) is a
   minimal contrast: tā marbūṭa raises to `[ɛ]` except after a velar, pharyngeal
   or emphatic. o2i gives `ˈħilwa` for both patterns.
7. **`ar-PS` interdentals in MSA borrowings.** The spec merges the interdentals;
   Cotter p.157 shows `θānawiyya` and `ḥadīθ` keeping `[θ]` *because they are
   formal-register borrowings*. This is a lexical-stratum effect the grapheme
   rules cannot see, and it is the sort of fact that belongs in a lexicon, not a
   rule.
8. **`pt-PT-x-beira` models only the /u/ → [y] leg of the chain shift.** The spec
   says so explicitly. Brissos p.66 prints the rest of it: `[e]` → `[œ]`
   (`cozer [kuzˈœɾ]`, `cesto [ˈsœʃt]`), monophthongized ⟨ou⟩ → `[ø]`
   (`roupa [ˈrøp]`), `[a]` → `[ɛ]` after a high vowel or glide
   (`pisado [pizˈɛðɨ]`, `tosquiar [tɨʃkjˈɛɾ]`), and deletion of the final
   unstressed vowel (`tudo [ˈtyd]`).
9. **`pt-PT-x-alentejo` loses a consonant.** `seda` → o2i `ˈsɛɐ`, gold
   `[ˈsɛðɐ]` — the ⟨d⟩ vanishes entirely rather than spirantizing to `[ð]`. This
   is not a modelling gap but a probable bug, and it is the single most useful
   row in the Portuguese half.
10. **`pt-PT-x-alentejo` chain shift.** Brissos p.67 has `[e]` → `[ɛ]`
    (`seda`), `[ɛ]` → `[æ]` (`erva`), `[a]` → `[ɒ]` (`mar`), `[ɔ]` → `[ɔ̝]`
    (`avó`); the spec models the /u/ → [y] leg only.

## Adding rows

Only from a source a spec actually cites, and only if you have the document open.
Record the printed page from the page's own running head — `pdftotext`'s page
index is *not* the printed page (see `sources.json` for each source's offset).
If you cannot verify what the source says, the row does not go in.
