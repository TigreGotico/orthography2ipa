# Primary-source gold

This gold holds worked examples from the primary sources that the language specs cite. The sources are the grammars, phonology monographs and theses in the `sources` array of each spec. Each row is one transcription that the linguist who described the variety printed, with the printed page it is on.

Each row in this set can be checked against a named page of a named document. No other gold in the harness gives that. The set is small on purpose. It is a diagnostic: it asks if the engine reproduces what the cited source says. It cannot certify a language alone.

[Benchmark gold datasets](../../../../docs/evaluation/datasets.md#primary-source-gold-primary_sources) puts this set beside the other gold sets. The scoreboard gives the scores per language.

## Files

| File | Content |
|---|---|
| `rows.jsonl` | One JSON object per example. |
| `sources.json` | The bibliography, keyed by the source id that rows use in `source`. Each entry gives the authors, year, title, venue, URL, access status, notation and the variety the source describes. Its `pagination` field tells how the printed folio maps to the page index of the PDF. |

The two page counts differ in most sources. The `page` field of a row always holds the printed page. The bibliography can also list a source that no row uses.

## Row fields

| Field | Meaning |
|---|---|
| `id` | The source id, a hyphen and a serial number, for example `jasim2020-007`. Some sources add a tag before the number (`owens2006-ng-002`). |
| `source` | A key into `sources.json`. |
| `page` | The printed page, from the running head or footer of the document. It is never the PDF page index. |
| `lang` | The o2i spec code, or `null` when no o2i spec is a defensible match. |
| `source_variety` | The variety label that the source uses. |
| `orthography` | The word as the source prints it, when the source prints a spelling. |
| `orthography_vocalized` | Arabic only. The same word with ḥarakāt. |
| `orthography_provenance` | `as-printed` or `editor-supplied`. |
| `source_notation` | The transcription of the source, verbatim, with its brackets. |
| `notation_system` | `ipa` or `arabicist-transliteration`. |
| `ipa` | The normalised IPA that the benchmark scores. |
| `level` | `broad` when the source uses `/…/`, `narrow` when it uses `[…]`. |
| `gloss` | The English gloss that the source gives. |
| `confidence` | `high`, `medium` or `low`. |
| `notes` | The conditioning, any disagreement inside the source, and what a normalisation changed. |

The `orthography_provenance` field records who wrote the spelling. A source that prints only a transcription gives `editor-supplied`, however easy the spelling is to derive. The Tetun stress inventory shows this. The spelling `kabás` needs the acute-accent rule of the grammar, and `hakarak` needs no rule. Both rows are `editor-supplied`, because the page prints neither word.

`load_primary_sources` in `scripts/benchmark.py` reads the rows for the `primary_sources` dataset, with the provenance tier `expert-human`. It scores `orthography_vocalized` when the row has it, and `orthography` when it does not, against `ipa`. A row with `lang: null` is not scored. A row with no word or no IPA is skipped. To count the rows, read `rows.jsonl`. The benchmark output gives the rows per language.

## Sources by language

This table lists each source under the spec code its rows carry. A source that covers two codes appears under each code.

| Language code | Source | What it gives |
|---|---|---|
| `ar-DZ` | Guerrero (2019), *Arabica* 66(1-2) | The Tlemcen reflex of Old Arabic *ǧ. |
| `ar-EG` | Watson (2002), *The Phonology and Morphology of Arabic* | Cairene examples. |
| `ar-IQ` | Jasim (2020), Newcastle PhD | Baghdadi Gilit: qāf and kāf reflexes, epenthesis, emphasis, monophthongs. |
| `ar-IQ-x-qeltu` | Jasim (2020), Newcastle PhD | Muslawi Qəltu: retained qāf, the rhotic [ɣ], emphasis harmony, monophthongs. |
| `ar-JO` | Fadda (2016), MA thesis | Ammani: monophthongs, emphasis spread, final imāla, interdental reflexes of the "bi'ul" group. |
| `ar-LY` | Guerrero (2019), *Arabica* 66(1-2) | Tripoli reflexes of *ǧ. |
| `ar-LY` | Benkato (2020), in Lucas & Manfredi (eds.) | Libyan examples from Tripoli and Benghazi. |
| `ar-MA` | Guerrero (2019), *Arabica* 66(1-2) | Reflexes of *ǧ in Tangiers, Fez and northern Taza or Chefchaouen. |
| `ar-MA` | Watson (2002), *The Phonology and Morphology of Arabic* | One Moroccan (Lmnabha) form, as quoted from Elmedlaoui. |
| `ar-MR` | Taine-Cheikh (2007), EALL "Ḥassāniyya Arabic" | Ḥassāniyya of the Gǝbla (Mauritania). |
| `ar-NG` | Owens (2006), *A Linguistic History of Arabic* | Nigerian (Shuwa) Arabic. |
| `ar-NG` | Procházka (2026), *Journal of Semitic Studies* | A gahawa example from Lake Chad Arabic. |
| `ar-PS` | Cotter (2016), *JAIS* 16 | Gaza City Arabic, with the interdentals of MSA-register borrowings. |
| `ar-SA-x-dawasir` | Alaodini (2019), Essex PhD | Dawāsir Arabic of Dammam. |
| `ar-SA-x-hejaz` | Omar (1975), FSI *Saudi Arabic, Urban Hijazi Dialect* | The pronunciation guide (pp. xi-xvi): qāf as [ɡ], the interdental merger, the eight vowels, monophthongs. Omar is the base source of the spec. |
| `ar-SA-x-hejaz` | Almalky (2020), Essex PhD | Urban Hijazi pronouns, from a study of the active participle. |
| `ar-SA-x-najd` | Algethami (2023), ICPhS | Najdi vowel acoustics, with monophthong tokens. |
| `ar-SA-x-najd` | Mahzari (2023), *TPLS* 13(3) | Riyadh reflexes of /k/ and /q/, with velar affrication. |
| `ar-SA-x-najd` | Alshammari (2026), *JLTR* 17(4) | Northern Najdi (Ḥāʾil) velar affrication and its loanword exceptions. |
| `ar-SA-x-qassim` | Alhoody (2019), Newcastle PhD | Qassimi Arabic of the Qaṣīm, with its monophthongs. |
| `ar-SA-x-rijal-alma` | Watson & Al-Azraqi (2011), *PSAS* 41 | Lateral reflexes of *ḍ and *ẓ in Rijāl Almaʿ. |
| `ar-SA-x-rijal-alma` | Alfaifi (2024), OBP *Diversity across the Arabian Peninsula*, ch. 5 | Rijāl Almaʿ examples quoted from Asiri (2008): qāf as [ɡ], retained diphthongs. |
| `ar-SA-x-sharqiyya` | Al-Taisan (2022), Essex PhD | Hasawi Arabic of al-Hasa (Eastern Province). |
| `ar-SA-x-tihama-qahtan` | Alqahtani (2015), Essex PhD | Tihami Qahtani. |
| `ar-SY` | Almbark & Hellmuth (2015), ICPhS | Damascene vowels. |
| `ar-TN` | Guerrero (2019), *Arabica* 66(1-2) | Tunis reflexes of *ǧ. |
| `ar-TN` | La Rosa (2021), *Languages* 6:145 | Tunisian Sahel (Mahdia, Msaken). |
| `ar-YE` | Watson (2002), *The Phonology and Morphology of Arabic* | Ṣanʿānī examples. |
| `cri` | Araujo & Agostinho (2010), *Revista de Letras* 26 | Santome (Forro) in the ALUSTP standard orthography. |
| `dga` | Angsongna & Akinbo (2022), *JIPA* 52(2) | Central Dàgáárè (Sombo, Nadowli-Kaleo). Pages 343 and 345 print a consonant table and a vowel table, each with a phonetic and an orthographic column. |
| `es-AR` | Coloma (2018), *JIPA* | Buenos Aires (River Plate) Spanish, with an allophone column. |
| `es-ES` | Martínez-Celdrán, Fernández-Planas & Carrera-Sabaté (2003), *JIPA* | Formal Castilian Spanish. |
| `ext-PT-x-barrancos` | Navas Sánchez-Élez (2011), *El barranqueño* | Barranquenho of Barrancos (Baixo Alentejo). |
| `he` | Laufer (1999), *Handbook of the IPA* | Modern Israeli Hebrew, Non-Oriental and Oriental. |
| `mcm` | Baxter (1988), *Pacific Linguistics* B-95 | Kristang (Malacca Creole Portuguese), chapter 2 phonology. |
| `pt-BR` | Barbosa & Albano (2004), *JIPA* | Brazilian Portuguese with dental affrication before [i]. |
| `pt-PT-x-alentejo` | Brissos (2014), *JPL* 13(1) | The southwestern (SW) subdialect and its tonic chain shift. |
| `pt-PT-x-beira` | Brissos (2014), *JPL* 13(1) | The central-interior (CI) subdialect and its tonic chain shift. |
| `pt-PT-x-lisbon` | Cruz-Ferreira (1995), *JIPA* | European Portuguese of Lisbon. |
| `pt-PT-x-porto` | Brissos (2018), *Estudos de Lingüística Galega*, vol. esp. I | Tonic diphthongisation of the northwest variety. |
| `pt-PT-x-sao-miguel` | Silva (2008), *JPL* 7-1 | Micaelense (São Miguel, Azores) front rounded vowels and chain shift. |
| `pt-PT-x-terceira` | Mikołajczak (2014), *Studia Iberystyczne* 13 | Terceirense (Azores) on-glides and a-metaphony. |
| `ru` | Yanushevskaya & Bunčić (2015), *JIPA* | Standard Russian (Moscow type). |
| `tet` | Williams-van Klinken, Hajek & Nordlinger (2002), *Pacific Linguistics* 528 | Tetun Dili, with its stress inventory. |
| `uk` | Pompino-Marschall, Steriopolo & Żygis (2017), *JIPA* | Standard Ukrainian. |
| `null` | Alshammari (2026), *JLTR* 17(4) | Northern Najdi /k/ affrication next to /a/, a Shammar extension that central Najd and Qaṣīm do not have. |
| `null` | Al Solami (2023), *Lingua Posnaniensis* LXV(1) | Bani Sulaim (Bedouin Hijazi) iambic stress and retained interdentals. |
| `null` | Al-Rohili (2019), Essex PhD | Ḥarbi of Medina (Bedouin northwest) palatalisation. |
| `null` | Alfaifi (2024), OBP ch. 5 | Central Faifi. |
| `null` | Davis, Alshammari, Alahmari & Alhuwaykim (2024), OBP ch. 4 | A southwest Saudi (Northern Tihāmah) variety, after Alahmari (2018). |
| `null` | Alqarni (2025), Essex PhD | Qarni (Balqarn), which has no o2i spec. |

The Bedouin Hijazi rows of Al Solami and Al-Rohili carry `lang: null` on purpose. They document the iambic stress, retained interdentals and palatalisation that the urban `ar-SA-x-hejaz` koine does not have. That split is the reason that the bare `ar-SA` code has no spec.

## Notation decisions

The data coerces nothing silently. `source_notation` keeps the string of the source, and `ipa` holds the normalised form. Each row that needed a normalisation says so in `notes`.

The Arabic sources mark no stress. Brissos marks stress with an apostrophe after the onset (`[l'ymɨ]`). The `ipa` field puts the IPA primary stress mark before the syllable (`ˈlymɨ`). The scoreboard strips stress in any case.

Cotter (2016) prints Arabicist transliteration (`ḥadīθ`), not IPA. The conversion writes `ā ī ū` as `aː iː uː`, `ḥ` as `ħ`, `y` as `j`, a doubled letter as a geminate, and `ˤ` for emphasis. A row converted from transliteration has `confidence` `medium` at most. The row `cotter2016-004` (`hāḏa`) is `low`. The paper argues that the Gaza reflex is the stop [d], but it quotes a source that writes ⟨ḏ⟩. The IPA follows the argument, not the letter.

Almbark writes `/xoːd/`, where the Arabic specs of o2i write `/χ/`. The row keeps the printed form. This is a notation difference between phonologists, not a claim about Syrian Arabic.

Rows from a scanned PDF come from a render of the printed page, which is the authority. The Cruz-Ferreira (1995) and Barbosa & Albano (2004) Illustrations are scans whose text layer corrupts the IPA. The Ukrainian and Russian Illustrations have glyph substitutions in the text layer (ɪ as `I`, ɔ as `ↄ`, ɨ as `-i`, ʲ as `j`). No row decodes a corrupted font from its byte values.

The Russian Illustration prints its words in scholarly transliteration (`pal'cy`), not in Cyrillic. The Cyrillic in these rows is editor-supplied. The transliteration and the gloss make it unambiguous, but each Russian row is flagged and has `confidence` `medium` at most.

The Arabic input contract of o2i is fully diacritised text. Most Arabic sources print their examples in transcription, not in script. For these rows the editor writes a diacritised spelling of the cited word in `orthography_vocalized` and flags the row `editor-supplied`. The IPA comes from the source, but the spelling comes from the editor, and it is the weakest part of these rows.

Page 343 of the Dàgáárè Illustration spells ⟨k͡p g͡b k͡y g͡y n͡y ŋ͡m⟩ with a tie bar. Dàgáárè spelling does not write one. The `orthography` field drops the tie bar, and those rows are `editor-supplied` at `medium` confidence. `source_notation` keeps the printed phonetic form. The typeset IPA on pages 343 to 345 uses a Latin `g`. The `ipa` field writes `ɡ` (U+0261), and `source_notation` keeps the printed string.

The phonetic cell of the Dàgáárè `ɹ` row is `/pʰɛ́gɾí/`, with a tap `ɾ`, not a plain `r`. A render at scale 8 confirms this, and the prose of page 344 agrees: "occasionally realized as an alveolar tap /ɾ/ after a /g/".

## Rows to read with care

The row `fadda2016-010` (عَمَّان) has four realisations in the source: `[ʕammaːn] ~ [ʕammæːn] ~ [ʕammɛːn] ~ [ʕammeːn]`. A single gold IPA cannot be right. The row records the most conservative form and has `confidence` `low`.

The thesis gives both `[simatʃ]` (p. 23) and `[simaʃ]` (p. 25) for the Gilit word سَمَك in `jasim2020-007`. The row records the affricate. The fricative is a disagreement inside the source, not a typo to smooth over.

In `jasim2020-017` (بَارِد), the phonemic form `/baɾid/` of the thesis has a short first vowel, but the standard spelling بارد writes a long one.

The rows `fadda2016-011` to `fadda2016-013` carry the label of the source's own group, "bi'ul" (the urban Palestinian type). Fadda says this group is the base of Western Amman speech. The rows are tagged `ar-JO`, but `ar-PS` is equally defensible.

The row `cotter2016-004` is described under notation decisions.

## Where a source disagrees with a spec

A disagreement between a source and a spec is a signal, so this section records each one. Each entry gives what the source prints and what o2i gives for the same row. To check an entry, run the engine over the rows it names.

### Iraqi Arabic

In `ar-IQ`, kāf affrication is not conditioned by a front vowel. The rules `IQ_GILIT_AFFRIC_K_BEFORE` and `IQ_GILIT_AFFRIC_K_AFTER` fire only next to `i iː j e eː`. Jasim (2020: 25) gives `/kalb/ → [tʃalib]` 'dog', `/kabiːr/ → [tʃibiːr]` 'big', `/ʃubbaːk/ → [ʃubbaːtʃ]` 'window' and `/samak/ → [simatʃ]` 'fish'. In each word the affricate is next to a non-front vowel, and in `ʃubbaːtʃ` it follows a long back vowel. Gilit kāf affrication is lexicalised, not a live front-vowel allophony. o2i gives `ˈkalb`, `kaˈbiːr`, `ʃubˈbaːk` and `ˈsamak`.

The `ar-IQ` spec does not model epenthesis or u-colouring. `/qalb/ → [ɡalˤʊb]`, `/kalb/ → [tʃalib]` and `[χʊbʊz]` 'bread' (pp. 24-25) split the final cluster with a vowel whose quality comes from the consonants around it. o2i gives `ˈɡalb` and `ˈxubz`. The spec also does not derive the emphatic /lˤ/ of `[ɡalˤʊb]` or the emphatic /rˤ/ of `[rˤabiːʕ]`.

Near an emphatic, Jasim prints /a/ as [ʊ]: `/basˤal/ → [bʊsˤal]` (p. 25). The `IQ_EMPH_A_*` rules back /a/ to `[ɑ]` instead, and o2i gives `ˈbɑsˤɑl`. The spec cites Jasim for both.

The `ar-IQ-x-qeltu` spec leaves /r/ → [ɣ] unmodelled on purpose, because the change is lexically conditioned. Jasim (2020: 23) gives the evidence: `[χɛːɣ]`, `[dɛːɣ]`, `[θoːɣ]`, `[baɣid]`. The rightward emphasis harmony of `/naːquːs/ → [naːqoːsˤ]` (p. 22) is also unmodelled. The rows stay so that the cost of that decision is visible.

### Levantine Arabic

In `ar-JO`, emphasis spreads to the final /t/: Fadda (2016: 29) writes `sˤawt → [sˤoːtˤ]`. o2i gives `ˈsˤoːt`. The `ar-JO` spec cites this example as "Fadda 2016:30", but the table is on printed page 29.

Fadda (2016: 30) gives the minimal contrast `[ħɪlwɛ]` 'beautiful' and `[bɪʃʕa]` 'ugly'. Tā marbūṭa raises to `[ɛ]` except after a velar, a pharyngeal or an emphatic. o2i gives `ˈħilwa` and `ˈbiʃʕa`, with [a] in both.

The `ar-PS` spec merges the interdentals. Cotter (2016: 157) shows `θānawiyya` and `ḥadīθ` with `[θ]`, because they are formal-register borrowings. Grapheme rules cannot see this lexical-stratum effect. It belongs in a lexicon, not in a rule.

### Najdi Arabic

The `ar-SA-x-najd` spec keeps the diphthongs: o2i gives `بَيْت → [bajt]`. Algethami (2023: 3385) records `[beːt]` 'home' and `[soːt]` 'sound' for his 15 Najdi speakers. Ingham (1994: 15), reproduced in Algethami's Fig. 1, lists /eː oː/ in the Najdi inventory, and the Riyadh inventory of Mahzari has five vowels (`i u eː oː a`).

The Algethami rows with [eː] and [oː] score as errors against the spec. The spec follows the diphthong retention of central Najdi on purpose. Alhoody (2019) gives `/bajt/ → [beːt]` as the feature that sets Qassimi apart from central Najdi (`alhoody2019-002`). The `ar-SA-x-qassim` monophthong rules are "the defining vocalic delta from central Najdi", so a monophthong rule in the parent would erase that contrast. The tension is a real split inside Najd or between registers. `algethami2023-006` records the monophthong at `medium` confidence and does not resolve it.

The `NAJD_AFFRIC_G_BEFORE` and `NAJD_AFFRIC_G_AFTER` rules fire next to `/i iː/` only. Alshammari (2026: §V, p. 1337) and Mahzari (2023: Table 4, p. 803) restrict the voiced velar affrication to the high front vowels. This is a voicing asymmetry: /k/ affricates in a wider set of contexts.

In Northern Najdi, `/k/ → [ts]` reaches central /a/ (`[tsalb]`, `[simats]`). Central Najd and Qaṣīm do not have this extension, so those rows carry `lang: null`.

Some MSA and foreign borrowings resist /k/ affrication even next to a front vowel. Alshammari (2026: ex. 4, p. 1336) gives تذكرة `[taðkirah]` 'ticket', not *[taðtsirah], and مكينة `[mikiːnah]` 'machine', not *[mitsiːnah]. Grapheme rules cannot see this lexical-stratum effect, as with the `ar-PS` borrowings.

The spec carries these words in its `word_exceptions` (`alshammari2026-009` and `alshammari2026-010`). The Table 3 exceptions of Mahzari (2023: 802), such as `kursi`, are spelled with a back vowel after the kāf. o2i keeps `[k]` for them without an exception.

### Hijazi Arabic

The `ar-SA-x-hejaz` spec applies qāf → [ɡ] to classicisms too. Omar (1975: xiii) says that /q/ "occurs only in classicized words" and that "it often alternates with /g/". Inherited words have [ɡ], and learned or borrowed words keep [q]. o2i has no lexical stratum, so قُرآن 'Quran' and اِقتِصاد 'economy' come out as `ɡurˈʔaːn` and `ʔiɡtɪˈsˤɑːd`. The source keeps `[qurʔaːn]` and `[iqtisˤaːd]`. This is the same class of fact as the `ar-PS` borrowings, and the rows stay so that the cost is visible.

The spec has no [s] reflex for the interdental ث. Omar (1975: xiv) gives both reflexes of the voiceless interdental: θalaaθa → talaata with [t], and maθalan → masalan with [s]. The spec models only ث → [t, θ], so مَثَلا comes out as `ˈmatalaː`, not `[masalan]`. The sibilant reflexes [s] and [z] are the older, minority urban pattern. The rows record an attested reflex that the spec does not model.

The lexical mid vowels of Hijazi do not follow from ⟨ِي⟩. Omar lists فين and اثنين under /ee/ = [eː] (`[feːn]`, `[itneːn]`), but these words have no Classical /ay/. From the diacritised spellings ⟨فِين⟩ and ⟨اِثْنِين⟩, o2i reads kasra plus yāʔ as [iː] (`ˈfiːn`, `ʔitˈniːn`). The forms [fiːn] and [feːn] coexist, and [feːn] needs a lexicon, not a rule. o2i does no normalisation.

o2i does give the monophthong of a real diphthong: خَيْر → `ˈxeːr`, بَيْت → `ˈbeːt`, صَوْت → `ˈsˤoːt`.

The broad FSI transcription shortens an unstressed final long vowel: مَرحَبا `[marħaba]`, عَرَبي `[ʕarabi]`, أَنا `[ʔana]`. o2i keeps the length that the spelling writes (`ˈmarħabaː`). The source also does not back /aː/ next to an emphatic (قِطار `[ɡitˤaːr]`), where o2i gives narrow `ɡɪˈtˤɑːr`. These are broad-versus-narrow measurement artefacts, which the `level` field records. They are not bugs.

### Rijāl Almaʿ

The `ar-SA-x-rijal-alma` spec reads qāf as [ɡ], with [q] kept only as a candidate for classicisms. Alfaifi (2024: 177-178) quotes the Rijāl Almaʿ examples of Asiri (2008: 72-73) verbatim. In them, historical *q is voiced [ɡ] throughout, with no [q]: `gābalt` 'I met', `im=bagar` 'the cows', `saragu` 'they stole', `gaṭaʕaw` 'they cut'. The neighbouring southwest and Tihāmah lects agree: Davis et al. (2024: 149) give `galam` 'pen', and Central Faifi has `gāma` and `lagīt`.

The same source confirms the diphthong retention that the spec models (`m=bayt`, not *beet).

Because both lects have [ɡ], qāf is not the split between Rijāl Almaʿ and Tihāmi Qaḥtāni. The split is the reflex of ẓāʾ. Rijāl Almaʿ keeps a distinct voiceless lateral [ɬˤ], and Tihāmi Qaḥtāni merges it with [ðˤ]. The rows of Alfaifi (2024) and Davis et al. (2024) are `arabicist-transliteration`, with `medium` confidence at most and an editor-supplied spelling.

### European Portuguese

The `pt-PT-x-beira` spec models only the /u/ → [y] step of the chain shift, and it says so. Brissos (2014: 66) prints the rest. Stressed `[e]` becomes `[œ]` (`cozer [kuzˈœɾ]`, `cesto [ˈsœʃt]`). Monophthongal ⟨ou⟩ becomes `[ø]` (`roupa [ˈrøp]`). `[a]` becomes `[ɛ]` after a high vowel or a glide (`pisado [pizˈɛðɨ]`, `tosquiar [tɨʃkjˈɛɾ]`). The final unstressed vowel drops (`tudo [ˈtyd]`).

In `pt-PT-x-alentejo`, o2i gives `seda` as `ˈsɛɐ` against the gold `[ˈsɛðɐ]`. The ⟨d⟩ disappears, where it should become `[ð]`. This is a probable bug, not a modelling gap, and it is the most useful row in the Portuguese half. Brissos (2014: 67) also prints the southwestern chain shift: `[e]` → `[ɛ]` (`seda`), `[ɛ]` → `[æ]` (`erva`), `[a]` → `[ɒ]` (`mar`), `[ɔ]` → `[ɔ̝]` (`avó`). The spec models the /u/ → [y] step only.

Cruz-Ferreira (1995: 91) gives tacto `[ˈtatu]`, cacto `[ˈkatu]` and jacto `[ˈʒatu]`, with the mute ⟨c⟩ of the spelling before the 1990 Orthographic Agreement. o2i pronounces the ⟨c⟩ (`ˈtaktu`, `ˈkaktu`, `ˈʒaktu`). This is a question of spelling normalisation, and o2i does no normalisation on purpose. The modern spellings tato, cato and jato transcribe correctly.

The `pt-PT-x-sao-miguel` spec models the [y] and [ø] fronting of Micaelense, but not the rest of the system. Silva (2008: 4) gives the full set. o2i gives [y] for stressed ⟨u⟩ (`uva ['yvɐ]`, `azul [ɐ'zyl]`). It does so before a coda too (`cruz [kryʃ]`). For this reason the spec drops the coda guard that the general `pt-PT-x-acores` spec keeps. o2i also gives [ø] for ⟨oi⟩ and ⟨ou⟩ (`oito`, `pouco`).

The spec does not model the elision of the final unstressed vowel (`oito` is `[øt]` in the source and `ˈøtu` in o2i). It does not model `[ø]` from ⟨o⟩ before `[ʒ]` (`hoje [øʒ]`, o2i `ˈɔʒɨ`). It does not model the tonic chain shift (`sete [sæt]`, `avó [ɐ'vo]`, `avô [ɐ'vu]`).

The `pt-PT-x-terceira` spec models the a-metaphony and the labial on-glide, but not the harmonic glide (Mikołajczak 2014: 422-423). o2i gives the vowel harmony of `pato ['pɔtu]` and `gato ['gɔtu]`, and the labial `[w]` on-glide of `porco [pw'orku]` and `bicho [bw'iszu]`. It does not give the `[j]` or `[w]` on-glide whose quality copies a high vowel one syllable back (`ceifar [sei'fjar]`, `pintar [pint'jar]`). It does not give the glide on an unstressed syllable (`morrer [mw'orer]`) or the northern raising of `soa ['sua]` and `flor ['flur]`. The rows record these as attested but unmodelled.

The `pt-PT-x-porto` spec diphthongises the open mid vowels, but the base selection of open and close vowels limits the match. Brissos (2018: 199-201) prints the northwest diphthongisation set. o2i gives `pé` as `ˈpjɛ`, an exact match from the open-mid rule.

o2i gives `Porto` as `ˈpwɔɾtu`, where the source has `[ˈpu̯oɾtu]`. The base engine picks the open allophone for the unmarked ⟨o⟩, so the diphthong is `[wɔ]`, not `[wo]`. It gives `toque` as `ˈtukɨ`, where the source has `[ˈtu̯ɔkɨ]`. The base raises the stressed ⟨o⟩ to `[u]`, so no mid-vowel rule can fire. Both are the documented limit of the pre-lexical open, close and raising choice, not a gap in the rules.

The `pt-PT-x-porto` spec does not model the RD2 subtype or the /i/ diphthong. The subtype towards a central vowel (`fazer [fɐˈzeɐ̯ɾ]`, `pé [ˈpɛɐ̯]`, p. 200) coexists with the modelled RD1 subtype inside one axis. The marginal `maquia [mɐˈkei̯ɐ]` (`[i]` → `[ei̯]`, about 19% of tokens, before a pause or a vowel only, p. 199) is left out on purpose. o2i gives `mɐˈkiɐ`.

### Brazilian Portuguese

Barbosa & Albano (2004: 228) give ganho as `[ɡẽɲʊ]`, with a nasal vowel before the palatal nasal. o2i gives `ˈɡaɲu`, with no nasal vowel.

The Illustration writes final unstressed /o/ as `[ʊ]` (galo `[ɡalʊ]`, caro `[kaɾʊ]`). o2i raises it to `[u]`. The Illustration writes carro as `[kaɣʊ]`, with a velar fricative for /R/, where o2i gives a uvular `[ʁ]`. The source says that /R/ varies across Brazil, so this is a variety choice, not an error.

### Russian and Ukrainian

The Russian Illustration analyses the hard sibilants as postalveolar /ʃ ʒ/ (шар /ˈʃar/, жар /ˈʒar/, p. 222), and the soft ones as /tʃʲ/ and /ʃʲː/ (чары, щука). o2i gives [ʂ], [ʐ], [tɕ] and [ɕː]. Both analyses are current in the literature. This is a real disagreement between the spec and a source, not an engine bug, and the rows record it.

For Гёте and Хюбнер, the phonemic transcription of the source keeps the unstressed vowels unreduced (/ˈɡʲote/, /ˈxʲubner/). o2i reduces them (`ˈɡʲɵtʲɪ`, `ˈxʲubnʲɪr`). The gold is broad, and the engine is narrow. A broad-versus-narrow mismatch is a measurement artefact, not an error, and the `level` field records it per row for this reason.

The Ukrainian source stresses перелаз and перелазь on the final syllable (`pɛrɛˈɫaz`). o2i stresses the second syllable (`peˈrɛɫɐz`) and reduces the unstressed vowels, which the source does not.

The Ukrainian source gives long palatalised consonants in піддашшя `[pʲiˈdːaʃʲːa]` and ніччю `[ˈnʲit͡ʃʲːu]`. o2i gives a long consonant without palatalisation (`pʲiˈdːaʃʃa`, `ˈnʲitʃtʃu`).

### Spanish

The Castilian Illustration (p. 255) transcribes allí `[aˈʎi]` and yate `[ˈɟ͡ʝate]`. In the variety it describes, /ʎ/ and /ɟ͡ʝ/ are separate phonemes. o2i merges both to `[ʝ]` (`aˈʝi`, `ˈʝate`).

The `es-ES` spec does not spirantise /b d ɡ/. The Castilian Illustration gives cuadro `[ˈkwaðɾo]` (p. 256) in its broad transcription, and o2i gives the stop (`ˈkwadɾo`). For `es-AR`, o2i matches the spirants that Coloma (2018: 244) lists in his allophone column: pava `ˈpaβa`, huevo `ˈweβo`, nada `ˈnaða`, maga `ˈmaɣa`.

In `es-AR`, /s/ becomes [h] before a consonant: pasta `[ˈpahta]` (p. 244). The article calls this a regular process of the variety. o2i gives `ˈpasta`.

The Spanish sources assimilate a nasal to the place of the next consonant. Coloma gives manga `[ˈmaŋɡa]` (p. 244), and the Castilian Illustration gives the nasal vowel of mamá `[mãˈma]` (p. 255). o2i gives `ˈmanɡa` and `maˈma`.

### Affricate tie bars

The Spanish, Ukrainian and Russian sources write `t͡ʃ`, `t͡s` and `d͡z` with a tie bar. o2i writes the bare sequence. The difference is cosmetic, but it is a real difference between the cited source and the output. The rows record it and do not normalise it away.

### Dàgáárè

The Dàgáárè source is not consistent about ⟨áà⟩. Page 343 prints ⟨fáà⟩ as `/fâː/` and ⟨n͡yáà⟩ as `/ɲâː/`, a falling tone on a long vowel. It prints ⟨ŋáà⟩ as `/ŋáː/`, a high tone on a long vowel. One spelling shape, a high-tone vowel letter followed by a low-tone vowel letter, gets two readings on one page. No rule can match all three rows, and all three stay as printed.

The `dga` grapheme map follows the falling reading, so o2i gives `ŋâː` for the third row. This is a disagreement inside the source, not between the source and the spec.

## Adding rows

Add a row only from a source that a spec cites, and only with the document open in front of you. Record the printed page from the running head of the page. The page index of `pdftotext` is not the printed page. The `pagination` field in `sources.json` gives the offset for each source. If you cannot verify what the source says, do not add the row.
