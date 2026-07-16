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
| Pompino-Marschall, Steriopolo & Żygis (2017), JIPA Illustration | Standard Ukrainian | `uk` | 45 |
| Yanushevskaya & Bunčić (2015), JIPA Illustration | Standard Russian | `ru` | 36 |
| Cruz-Ferreira (1995), JIPA Illustration | European Portuguese (Lisbon) | `pt-PT-x-lisbon` | 33 |
| Jasim (2020), Newcastle PhD | Baghdadi Gilit / Muslawi Qəltu | `ar-IQ` / `ar-IQ-x-qeltu` | 12 / 12 |
| Barbosa & Albano (2004), JIPA Illustration | Brazilian Portuguese | `pt-BR` | 21 |
| Fadda (2016), MA thesis | Ammani | `ar-JO` | 13 |
| Brissos (2014), JPL | EP central-interior (CI) / southwestern (SW) | `pt-PT-x-beira` / `pt-PT-x-alentejo` | 8 / 5 |
| Silva (2008), JPL 7-1 | Micaelense (São Miguel, Azores) | `pt-PT-x-sao-miguel` | 12 |
| Mikołajczak (2014), Studia Iberystyczne 13 | Terceirense (Ilha Terceira, Azores) | `pt-PT-x-terceira` | 10 |
| Almbark & Hellmuth (2015), ICPhS | Damascene | `ar-SY` | 11 |
| Cotter (2016), JAIS | Gaza City | `ar-PS` | 4 |
| Martínez-Celdrán, Fernández-Planas & Carrera-Sabaté (2003), JIPA Illustration | Castilian Spanish | `es-ES` | 41 |
| Coloma (2018), JIPA Illustration | Buenos Aires / River Plate Spanish | `es-AR` | 29 |
| Laufer (1999), Handbook of the IPA Illustration | Modern Israeli Hebrew (Non-Oriental / Oriental) | `he` | 33 |
| Owens (2006), A Linguistic History of Arabic | Nigerian Arabic (Shuwa) | `ar-NG` | 8 |
| Procházka (2026), JSS gahawa survey | Nigeria (Lake Chad Arabic) | `ar-NG` | 1 |
| Guerrero (2019), *Arabica* 66(1-2) | Maghrebi *ǧīm* reflexes (Tangiers / Fez / Tunis / Tripoli / Tlemcen) | `ar-MA` / `ar-TN` / `ar-LY` / `ar-DZ` | 4 / 2 / 3 / 1 |
| Benkato (2020), *Maghrebi Arabic* (Lucas & Manfredi, eds.) | Libyan Arabic (Tripoli / Benghazi) | `ar-LY` | 3 |
| Taine-Cheikh (2007), EALL *Ḥassāniyya Arabic* | Ḥassāniyya (Mauritania, Gǝbla) | `ar-MR` | 18 |
| La Rosa (2021), Languages 6:145 | Tunisian Sahel (Mahdia/Msaken) | `ar-TN` | 7 |
| Watson (2002), The Phonology and Morphology of Arabic | Cairene / Moroccan (Lmnabha, as quoted from Elmedlaoui) / Ṣanʿānī | `ar-EG` / `ar-MA` / `ar-YE` | 18 / 1 / 15 |
| Alhoody (2019), Newcastle PhD | Qassimi (Qaṣīm) | `ar-SA-x-qassim` | 12 |
| Algethami (2023), ICPhS | Najdi vowels (acoustic) | `ar-SA-x-najd` | 3 |
| Mahzari (2023), TPLS 13(3) | Najdi /k/,/q/ (Riyadh) | `ar-SA-x-najd` | 8 |
| Alshammari (2026), JLTR 17(4) | Northern Najdi velar affrication (Ḥāʾil) | `ar-SA-x-najd` / `null` | 4 / 2 |
| Watson & Al-Azraqi (2011), PSAS 41 | Rijāl Almaʿ (SW Saudi Tihāmah) | `ar-SA-x-rijal-alma` | 3 |
| Al-Taisan (2022), Essex PhD | Hasawi (al-Hasa, Eastern Province) | `ar-SA-x-sharqiyya` | 2 |
| Araujo & Agostinho (2010), *Revista de Letras* 26 | Santome (Forro), ALUSTP standardization article | `cri` | 13 |
| Baxter (1988), Pacific Linguistics B-95 | Kristang (Malacca Creole Portuguese) | `mcm` | 33 |
| Brissos (2018), Estud. ling. galega, vol. esp. I | NW Portuguese (variedade do noroeste) | `pt-PT-x-porto` | 9 |
| Navas Sánchez-Élez (2011), *El barranqueño* | Barranquenho (Barrancos, Baixo Alentejo) | `ext-PT-x-barrancos` | 10 |
| **total** | | | **505** |
Broad `/…/`: 343. Narrow `[…]`: 162. `confidence`: 322 high, 169 medium, 14 low.
| Omar (1975), FSI *Saudi Arabic, Urban Hijazi Dialect* | Urban Hijazi (Jeddah/Mecca/Medina koine) | `ar-SA-x-hejaz` | 26 |
| Almalky (2020), Essex PhD | Hijazi Arabic (urban), active participle | `ar-SA-x-hejaz` | 4 |
| Al Solami (2023), *Lingua Posnaniensis* LXV(1) | Bani Sulaim (Bedouin Hijazi) — iambic-stress contrast | `null` | 5 |
| Al-Rohili (2019), Essex PhD | Ḥarbi of Medina (Bedouin NW) — palatalisation contrast | `null` | 5 |
| **total** | | | **528** |
Broad `/…/`: 369. Narrow `[…]`: 159. `confidence`: 316 high, 198 medium, 14 low.
The four Saudi/Hijazi sources added in the deep-validation round are page-pinned to the
literature the `ar-SA-x-hejaz` spec cites. Omar (1975) is the spec's base source; its
pronunciation guide (pp.xi-xvi) supplies the urban qaf→[ɡ] / interdental-merger / 8-vowel /
monophthongization attestations. Al Solami (2023) and Al-Rohili (2019) are BEDOUIN Hijazi
(Bani Sulaim; Ḥarbi of Medina) and are deliberately `lang: null` — they document the
iambic-stress, interdental-retention and palatalisation features that the *urban* koine node
does **not** have, i.e. the split that keeps the bare `ar-SA` code unassigned.
| Alshammari (2026), JLTR 17(4) velar affrication | Northern Najdi (Ḥāʾil) | `ar-SA-x-najd` / — | 8 / 2 |
| Mahzari (2023), TPLS 13(3) k/q change | Najdi (Riyadh) | `ar-SA-x-najd` | 8 |
| Algethami (2023), ICPhS vowel acoustics | Najdi (15 speakers) | `ar-SA-x-najd` | 3 |
| **total** | | | **509** |
Broad `/…/`: 341. Narrow `[…]`: 168. `confidence`: 324 high, 171 medium, 14 low.

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
- **Scanned PDFs are read as images, never guessed.** The Cruz-Ferreira (1995) and
  Barbosa & Albano (2004) Illustrations are scans whose text layer mangles the IPA;
  the Ukrainian and Russian Illustrations have text-layer glyph substitutions (ɪ→`I`,
  ɔ→`ↄ`, ɨ→`-i`, ʲ→`j`). In every one of these cases the rows were transcribed from a
  **render of the printed page**, which is authoritative. No mangled font was
  hand-decoded from its byte values.
- **Russian Cyrillic is editor-supplied.** The Illustration prints its words in
  scholarly transliteration (`pal'cy`), not Cyrillic, so the Cyrillic is ours —
  unambiguous given transliteration plus gloss, but flagged, and every Russian row is
  capped at `confidence: medium`.
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

11. **`ru` sibilants: /ʃ ʒ/ vs the spec's [ʂ ʐ].** The JIPA Illustration analyses the
    Russian hard sibilants as post-alveolar /ʃ ʒ/ (шар /ˈʃar/, жар /ˈʒar/, p.222) and
    the soft ones as /tʃʲ/ and /ʃʲː/ (чары, щука); o2i produces [ʂ], [ʐ], [tɕ], [ɕː].
    Both analyses are current in the literature — this is a genuine disagreement
    between our spec and a source, not an engine bug, and the rows record it.
12. **`ru` Гёте / Хюбнер**: the source keeps the unstressed vowels unreduced in its
    phonemic transcription (/ˈɡʲote/, /ˈxʲubner/) where o2i applies reduction
    (`ˈɡʲɵtʲɪ`, `ˈxʲubnʲɪr`). The gold here is broad; the engine is narrow. A reminder
    that a broad-vs-narrow mismatch is a measurement artefact, not an error — which is
    exactly why `level` is recorded per row.
13. **`uk` stress placement.** перелаз / перелазь are stressed on the final syllable in
    the source (`pɛrɛˈɫaz`); o2i stresses the second (`peˈrɛɫɐz`) and reduces the
    unstressed vowels, which the source does not.
14. **`uk` long palatalized consonants.** піддашшя `[pʲiˈdːaʃʲːa]` and ніччю
    `[ˈnʲit͡ʃʲːu]` show gemination-with-palatalization that o2i renders as a plain
    cluster plus /j/ (`ˈpʲiddaʃʃjɑ`, `ˈnʲitʃtʃju`). Same for мяу and свят: the source has
    a palatalized consonant (`mʲau̯`, `sʲʋʲat`), o2i inserts a /j/ and backs the vowel.
15. **`pt-PT-x-lisbon` mute ⟨c⟩.** Cruz-Ferreira p.91 gives tacto `[ˈtatu]`, cacto
    `[ˈkatu]`, jacto `[ˈʒatu]` — the ⟨c⟩ is not pronounced in the pre-AO1990 spelling.
    o2i pronounces it (`ˈtaktu`, `ˈkaktu`, `ˈʒaktu`). Note this is precisely an
    orthography-normalization question, and o2i deliberately does no normalization: the
    modern spellings (tato, cato, jato) would transcribe correctly.
16. **`pt-BR` nasalization before a palatal nasal.** ganho is `[ɡẽɲʊ]` in Barbosa &
    Albano p.228; o2i gives `ˈɡaɲu` — the vowel is not nasalized.
17. **`pt-BR` final unstressed /o/.** The Illustration transcribes it `[ʊ]`
    (galo `[ɡalʊ]`, caro `[kaɾʊ]`); o2i raises it all the way to `[u]`. And `carro` is
    `[kaɣʊ]` there (a velar fricative /R/) against o2i's uvular `[ʁ]` — the source says
    the /R/ realization varies across Brazil, so this is a variety choice, not an error.

18. **`es-ES` has no lleísmo.** The Castilian Illustration (p.255) transcribes allí
    `[aˈʎi]` and yate `[ˈɟ͡ʝate]` — /ʎ/ and /ɟ͡ʝ/ are distinct phonemes in the variety
    it describes. o2i merges both to `[ʝ]` (`aˈʝi`, `ˈʝate`).
19. **`es-ES` word-final ⟨y⟩ is a glide, not a consonant.** soy is `[ˈsoi̯]` (p.256);
    o2i gives `ˈsoʝ`. This is a bug, not a modelling choice — the same engine handles
    peine and pausa as diphthongs.
20. **`es-ES` / `es-AR` spirantization of /b d ɡ/ is not applied.** cuadro `[ˈkwaðɾo]`
    (Castilian p.256), pava `[ˈpaβa]`, huevo `[ˈweβo]`, nada `[ˈnaða]`, maga `[ˈmaɣa]`
    (Argentine p.244) — o2i gives the stops throughout. The Argentine article lists
    these explicitly in an ALLOPHONES column, so they are narrow rows; the Castilian
    ones are in the source's broad transcription.
21. **`es-AR` /s/ → [h] before a consonant.** pasta `[ˈpahta]` (p.244); o2i gives
    `ˈpasta`. The article calls this a regular process of the variety.
22. **`es-ES` / `es-AR` nasal place assimilation.** manga `[ˈmaŋɡa]` (p.244) and the
    nasalized vowel of mamá `[mãˈma]` (p.255); o2i gives `ˈmanɡa`, `maˈma`.
23. **Affricate tie-bars.** The Spanish, Ukrainian and Russian sources write `t͡ʃ`,
    `t͡s`, `d͡z` with the tie bar; o2i emits the bare sequence. Cosmetic, but it is a
    real difference between what the cited source prints and what we produce, so it is
    recorded rather than normalized away.
24. **`pt-PT-x-sao-miguel` models the [y]/[ø] fronting but not the rest of the
    micaelense system.** Silva (2008) p.4 gives the full stereotype set. o2i now
    reproduces the front-rounded monophthongs — [y] < stressed ⟨u⟩ (`uva ['yvɐ]`,
    `azul [ɐ'zyl]`, and crucially `cruz [kryʃ]` *before a coda*, which is why the
    Rogers-based coda guard was dropped for this leaf) and [ø] < ⟨oi/ou⟩ (`oito [øt]`,
    `pouco [pøk]`). It does **not** model (a) the final-unstressed-vowel elision
    (`oito` is `[øt]` in the source, `ˈøtu` in o2i), (b) the `[ø]` from ⟨o⟩ before
    `[ʒ]` (`hoje [øʒ]`, o2i `ˈɔʒɨ`), or (c) the tonic chain shift (`sete [sæt]`,
    `avó [ɐ'vo]`, `avô [ɐ'vu]`). The rows record what is and is not covered.
25. **`pt-PT-x-terceira` models the a-metaphony and the labial crescent glide, not
    the harmonic glide.** Mikołajczak (2014) pp.422-423. o2i reproduces the
    vocalic harmonisation (`pato ['pɔtu]`, `gato ['gɔtu]`) and the labial-conditioned
    `[w]` on-glide (`porco [pw'orku]`, `bicho [bw'iszu]`). It does **not** reproduce
    the harmonic `[j]`/`[w]` on-glide whose quality copies a high vowel a syllable
    back (`ceifar [sei'fjar]`, `pintar [pint'jar]`) nor the glide on an unstressed
    syllable (`morrer [mw'orer]`), nor the northern-type raising `soa ['sua]`,
    `flor ['flur]` — all recorded as attested-but-unmodelled rows.

26. **`pt-PT-x-porto` now diphthongizes the open mids, but the base open/close
    selection still limits the match.** Brissos (2018) pp.199-201 prints the NW
    diphthongization set. o2i reproduces `pé [ˈpjɛ]` exactly (the added
    open-mid rule), but `Porto` comes out `[ˈpwɔɾtu]` where the source has
    `[ˈpu̯oɾtu]` — the base engine mis-selects the OPEN allophone for the
    spelling-unmarked `⟨o⟩`, so it diphthongizes to `[wɔ]` not `[wo]`; and
    `toque` comes out `[ˈtukɨ]` where the source has `[ˈtu̯ɔkɨ]` — the base
    RAISES the stressed `⟨o⟩` to `[u]`, so no mid-vowel rule can fire. Both are
    the documented pre-lexical open/close/raising limit, not a rule gap.
27. **`pt-PT-x-porto` does not model RD2 or the /i/-diphthong.** The toward-
    central subtype (`fazer [fɐˈzeɐ̯ɾ]`, `pé [ˈpɛɐ̯]`, p.200) co-exists with the
    modelled within-axis RD1, and the marginal `maquia [mɐˈkei̯ɐ]` (`[i]→[ei̯]`,
    ~19% of tokens, pre-pause/vowel only, p.199) is deliberately left out; the
    rows record what is and is not covered.
28. **`ar-SA-x-hejaz` over-applies qaf→[ɡ] to classicisms.** Omar (1975) p.xiii states
    /q/ "occurs only in classicized words; it often alternates with /g/" — the base
    source's own contract is that inherited vocab has [ɡ] but learned/borrowed items keep
    [q]. o2i has no lexical stratum, so قُرآن 'Quran' and اِقتِصاد 'economy' come out
    `[ɡurʔaːn]`, `[ʔiɡtisˤɑːd]` where the source keeps `[qurʔaːn]`, `[iqtisˤaːd]`. Same
    class as the `ar-PS` MSA-borrowing note (#7): a lexical fact the grapheme rules cannot
    see. The rows are kept so the cost is visible.
29. **`ar-SA-x-hejaz` interdental ث lacks the [s] reflex.** Omar p.xiv gives both
    reflexes of the voiceless interdental: θalaaθa→talaata ([t]) *and* maθalan→masalan
    ([s]). The spec models only ث→[t,θ], so مَثَلا comes out `[matalaː]` not `[masalan]`.
    The [s]/[z] sibilant reflexes are the older/minority urban pattern; recorded as an
    attested-but-unmodelled reflex.
30. **`ar-SA-x-hejaz` lexical mid vowels aren't derivable from ⟨ِي⟩.** Omar lists فين and
    اثنين under /ee/=[eː] ([feːn], [itneːn]), but these have no Classical /ay/; the mid
    vowel is lexical. From the diacritized spellings ⟨فِين⟩/⟨اِثْنِين⟩ o2i correctly reads the
    kasra+yāʔ as [iː] (`[fiːn]`, `[itniːn]`). [fiːn]~[feːn] coexist; [feːn] would need a
    lexicon, not a rule — o2i does no normalization. (The monophthong from a real diphthong,
    e.g. خَيْر→[xeːr], بَيْت→[beːt], صَوْت→[sˤoːt], *is* reproduced.)
31. **`ar-SA-x-hejaz` final long vowels and emphatic backing are narrow choices.** The FSI
    broad transcription shortens unstressed final long vowels (مَرحَبا `[marħaba]`, عَرَبي
    `[ʕarabi]`, أَنا `[ʔana]`) where o2i keeps the orthographic length (`[marħabaː]` etc.),
    and does not back /aː/ next to an emphatic (قِطار `[ɡitˤaːr]`) where o2i gives narrow
    `[ɡitˤɑːr]`. Broad-vs-narrow measurement artefacts, recorded per `level`, not bugs.
28. **`ar-SA-x-najd` monophthongization is not modelled, yet the sources say
    central Najd monophthongizes too.** Algethami (2023) p.3385 gives `[beːt]`
    'home' and `[soːt]` 'sound', and Ingham (1994:15, reproduced in Algethami's
    Fig.1) already lists /eː oː/ in the Najdi inventory. o2i's `ar-SA-x-najd`
    spec retains the diphthongs (`بَيْت → [bajt]`), so these rows score as
    errors against it. The consequence is that the Qaṣīm leaf's QAS_MONO_AY/AW
    "defining delta from central Najd" is largely an artifact of the parent
    modelling diphthong retention — the monophthongs are pan-Najdi. Flagged for
    the `ar-SA-x-najd` spec (a sibling's file).
29. **`ar-SA-x-najd` /ɡ/-affrication trigger set is wider than the literature.**
    Alshammari (2026, `[ɡumar]` 'moon', pp.1335-1337) and Mahzari (2023) both
    restrict `/ɡ/→[dz]` to HIGH FRONT `/i iː/` only (voicing asymmetry), while
    `/k/→[ts]` reaches central `/a/` in Northern Najdi (`[tsalb]`, `[simats]` —
    tagged `null`, an NNA/Shammar extension absent from central Najd/Qaṣīm). The
    o2i NAJD_AFFRIC_G rules include `/e eː/` in the trigger; no Qaṣīm gold row
    exercises that leg, so it is inert here but over-generous for the parent.
30. **`ar-SA-x-najd` lexical exceptions to /k/-affrication are unmodelled.**
    Mahzari (2023) p.802 Table 3: `kursi → [kirsi]` 'chair' keeps `[k]` despite a
    surface front `/i/`; the grapheme rule would give `*[tsirsi]`. A lexical
    stratum the rules cannot see — the sort of fact that belongs in a lexicon.
28. **`ar-SA-x-najd` diphthongs — retained, against Algethami's monophthongized
    tokens.** Algethami (2023) p.3385 records `bēt`/`sōt` for his 15 Najdi
    speakers (`aj aw → eː oː`), and Mahzari's Riyadh inventory is 5-vowel
    (`i u eː oː a`). But the spec RETAINS the diphthongs (`[bajt]`, `[wajn]`),
    following Ingham's central-Najdi description — and this is not an oversight:
    Alhoody (2019) frames `/bajt/ → [beːt]` as precisely the *Qassimi* feature
    that distinguishes it from diphthong-retaining central Najdi (`alhoody2019-002`),
    and the shipped `ar-SA-x-qassim` monophthongization rules are defined as "the
    defining vocalic delta from central Najdi, which retains [aj]/[aw]". Flipping
    `ar-SA-x-najd` to monophthongize would erase that contrast. The tension is a
    genuine within-Najd / register split; `algethami2023-003` records the
    monophthongized attestation at `medium` confidence rather than resolving it.
29. **`ar-SA-x-najd` /ɡ/-affrication trigger tightened to `/i iː/`.** The
    `NAJD_AFFRIC_G_*` rules previously fired next to `/i iː j e eː/`, but both
    Alshammari (2026 §V, p.1337) and Mahzari (2023 Table 4, p.803) restrict the
    voiced-velar affrication to high front `/i iː/` only — the voicing-conditioned
    asymmetry with `/k/`, which tolerates a wider set. The list was narrowed to
    `/i iː/` to match the sources; no gold row depended on the mid-vowel triggers.
30. **`ar-SA-x-najd` loanword /k/-affrication exceptions.** Alshammari (2026)
    ex.(4) p.1336 lists MSA/foreign borrowings that resist affrication even next
    to a front vowel — تذكرة `[taðkirah]` 'ticket' (not *[taðtsirah]), مكينة
    `[mikiːnah]` 'machine' (not *[mitsiːnah]). This is a lexical-stratum effect
    the grapheme rules cannot see (cf. the `ar-PS` interdental-borrowing case #7);
    the two clearest cases are carried in the spec's `word_exceptions`
    (`alshammari2026-009/010`). Mahzari's Table-3 exceptions (kursi, kufuːf, …) are
    all written with a *back* vowel on the kaf, so o2i already keeps `[k]` and no
    exception is needed.

## Adding rows

Only from a source a spec actually cites, and only if you have the document open.
Record the printed page from the page's own running head — `pdftotext`'s page
index is *not* the printed page (see `sources.json` for each source's offset).
If you cannot verify what the source says, the row does not go in.
