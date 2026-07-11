# Finding a language's phonology documentation

`orthography2ipa` registers 350+ language and dialect codes, but only a
handful have a hand-written prose page here — the rest are documented
entirely by their JSON spec (graphemes, allophones, sources, `notes`).
Both are legitimate ways to answer "how does this library handle
language X":

1. **A hand-written page exists** for a language when someone has
   written up the phonological reasoning in prose — useful when a
   language has enough irregularity or contested analysis that a
   grapheme table alone doesn't explain the *why*. These pages are
   listed by family below.
2. **No hand-written page exists** for most languages. That's normal,
   not a gap to apologize for — the JSON spec itself is the source of
   truth, and it's fully self-describing:

   ```python
   import orthography2ipa

   spec = orthography2ipa.get("fi-FI")
   spec.name, spec.family, spec.script, spec.quality
   spec.notes            # free-form linguistic notes, including known caveats
   spec.sources          # cited phonological references
   spec.graphemes         # the full grapheme → IPA map
   ```

   or from the shell:

   ```bash
   orthography2ipa info fi-FI --graphemes
   ```

If you're checking whether a language is trustworthy enough to depend
on, the `quality` field and the language's row (if any) in
[../scoreboard.md](../scoreboard.md) matter more than whether a prose
page exists — see [../quality_tiers.md](../quality_tiers.md) for what
each tier actually certifies.

## Hand-written pages, by family

### Germanic

| Doc | Languages covered |
|:---|:---|
| [germanic.md](germanic.md) | de-DE, nl, sv, nb, da, af, en-GB, en-US (comparative) |
| [en-GB.md](en-GB.md) | en-GB (RP) and en-US in detail |
| [de-DE.md](de-DE.md) | German standard (Hochdeutsch) in detail |

### Romance

| Doc | Languages covered |
|:---|:---|
| [romance.md](romance.md) | es-ES, fr-FR, it-IT, pt-PT, pt-BR, ca, ro-RO (comparative) |
| [fr-FR.md](fr-FR.md) | French in detail |
| [it-IT.md](it-IT.md) | Italian in detail |
| [pt-BR.md](pt-BR.md) | Brazilian Portuguese in detail (positional maps + post-lexical allophony) |
| [pt-BR-x-caipira.md](pt-BR-x-caipira.md) | Caipira (SP interior) — the retroflex "r caipira" [ɻ]; Amaral (1920) |
| [pt-BR-x-sp.md](pt-BR-x-sp.md) | Paulistano (São Paulo capital) — plain tap coda /r/, non-chiado coda /s/ |
| [pt-BR-x-pr.md](pt-BR-x-pr.md) | Paranaense / Curitibano — conservative Sulista (no palatalisation, final /e/ retained) |
| [pt-PT.md](pt-PT.md) | European Portuguese in detail (coda allophony, vowel reduction) |
| [pt-BR-x-rj.md](pt-BR-x-rj.md) | Carioca (Rio de Janeiro city) — the *chiado carioca* coda /S/→[ʃ,ʒ] + posterior coda /R/ (post-lexical `allophone_rules`) |
| [pt-BR-x-fluminense.md](pt-BR-x-fluminense.md) | Fluminense (RJ state) — Carioca-like chiado as the coastal prestige default; capital-vs-interior gradient documented |
| [pt-BR-x-mg.md](pt-BR-x-mg.md) | Mineiro (Minas Gerais) — pretonic mid-vowel raising /e o/→[i u]; NOT chiado (alveolar coda /S/) |
| [pt-BR-x-sul.md](pt-BR-x-sul.md) | Sulista / Gaúcho (RS/SC/PR) — alveolar trill/tap /r/ (not [h~x]); conservative non-palatalisation; Nascentes (1953) |
| [pt-BR-x-norte.md](pt-BR-x-norte.md) | Nortista / Amazônico (Belém, Manaus) — Belém coda-/S/ *chiado* [ʃ,ʒ]; palatalisation retained; Silva (2014, ALFAL) |
| [pt-BR-x-brasilia.md](pt-BR-x-brasilia.md) | Brasiliense / Candango (Brasília) — koiné levelling to the SE standard; honestly a skeleton delta (no historical subfalar) |
| [pt-UY.md](pt-UY.md) | Uruguayan Portuguese / Riverense / DPU (border-contact variety: ⟨lh⟩→[j], dental /t d/ before /i/) |
| [pt-TL.md](pt-TL.md) | East Timorese Portuguese (`pt-TL`) — L2/official variety; no vowel reduction (Tetum substrate), alveolar rhotic; NOT the Bidau creole |
| [pt-MO.md](pt-MO.md) | Macau Portuguese (`pt-MO`) — EP-following; thin literature (skeleton); NOT the Patuá/maquista creole |
| [pt-AO.md](pt-AO.md) | Angolan Portuguese — emerging L2 norm, spelling-closer vocalism (no EP reduction), alveolar coda /s/ (Undolo 2014, Chavagne 2005) |
| [pt-CV.md](pt-CV.md) | Cape Verdean *Portuguese* — distinct from Kabuverdianu (kea) creole; reduced reduction, plosive b/d/g (honesty-flagged, skeleton) |
| [pt-MZ.md](pt-MZ.md) | Mozambican Portuguese — Maputo emerging norm, alveolar trill [R], aspirated /ʎ/, weaker reduction (Nhatuve 2019, Gonçalves 2010) |
| [lij.md](lij.md) | Ligurian / Genoese (Gallo-Italic; grafia ofiçiâ, ⟨x⟩=/ʒ/, ⟨o⟩=/u/, ⟨u⟩=/y/) |
| [an-valleys.md](an-valleys.md) | Pyrenean-valley Aragonese: Cheso (`an-x-cheso`), Ansotano (`an-x-ansotano`), Belsetán (`an-x-belsetan`), Chistabín (`an-x-chistabin`), Tensino (`an-x-tensino`) — geminates ⟨l·l⟩/⟨n·n⟩, final-r deletion, no-epenthesis ⟨ix⟩, ro/ra tap article |

#### Latin American Spanish — regional scaffolding (stub tier, no prose page yet)

Every Latin American national variety plus the major regional dialect
zones of Lipski's (1994) classification (as summarised in Lipski's own
["Geographical and Social Varieties of Spanish: An Overview"](https://johnlipski.github.io/geo.pdf))
have at least a **stub** spec, so the ancestry / phonological-distance
metrics resolve for the whole family. Stubs model only the pan-LatAm
baseline (seseo, yeísmo) and carry a weighted ancestry chain
`es-ES-x-medieval → es-ES → es-419 → country → region` plus the relevant
indigenous adstrate; dialect-specific phonology is deliberately deferred.

| Country | Regional stubs (`es-XX-x-…`) | Indigenous adstrate(s) |
|:---|:---|:---|
| Argentina (`es-AR`) | `cordoba`, `cuyo`, `norte`, `patagonia`, `litoral` | Quechua (`qu`), Mapudungun (`arn`), Guaraní (`gn`) |
| Mexico (`es-MX`) | `norte`, `yucatan` (+ existing `costa`) | Nahuatl (`nah`), Yucatec Maya (`yua`) |
| Colombia (`es-CO`) | `santander`, `valluno`, `llanero`, `pacifico` (+ existing `costa`, `paisa`) | — |
| Peru (`es-PE`) | `andino`, `amazonico` (+ existing `lima`) | Quechua (`qu`), Aymara (`ay`) |
| Chile (`es-CL`) | `andino`, `chilote` | Aymara (`ay`), Mapudungun (`arn`) |
| Venezuela (`es-VE`) | `maracucho`, `andino`, `llanero` | — |
| Bolivia (`es-BO`) | `andino`, `camba` | Quechua (`qu`), Aymara (`ay`), Guaraní (`gn`) |
| Ecuador (`es-EC`) | `andino`, `costa` | Quechua (`qu`) |

New national stubs: Honduras (`es-HN`), El Salvador (`es-SV`, Nawat/Pipil
adstrate). Indigenous contact languages are themselves structural adstrate
stubs (`gn`, `qu`, `ay`, `nah`, `arn`, `yua`, `quc`) — metadata only, no
phonology claimed (the `afa.json` pattern).

### Asturleonese

| Doc | Languages covered |
|:---|:---|
| [mwl.md](mwl.md) | Mirandese (`mwl`) + Sendinês (`mwl-x-sendim`) and Ifanês (`mwl-x-ifanes`) — the four-way sibilant system, Leonese diphthongs and initial-l palatalisation, sub-dialect deltas |

### Slavic

| Doc | Languages covered |
|:---|:---|
| [slavic.md](slavic.md) | pl, cs, ru, uk, sr/hr (comparative) |
| [ru.md](ru.md) | Russian in detail |

### Semitic

| Doc | Languages covered |
|:---|:---|
| [ar.md](ar.md) | Modern Standard Arabic (+ Egyptian Cairene, Saudi Najdi/Hejazi, and Gulf/Khaleeji Emirati·Bahraini·Kuwaiti·Qatari·Omani sections) — abjad script, tashkeel-dependent input contract, emphatic-spreading and Gulf velar-affrication allophone layers |
| [ar-x-levantine.md](ar-x-levantine.md) | Levantine Arabic — Damascene (`ar-SY`), Beiruti (`ar-LB`), Ammani (`ar-JO`), Palestinian (`ar-PS`): shared qaf/jim/interdental reflexes, /aj aw/→[eː oː] monophthongization, Lebanese imāla |
| [ar-IQ.md](ar-IQ.md) | Iraqi Arabic — the gilit/qəltu communal-dialect split: Baghdad Muslim gilit (`ar-IQ`, qaf→[ɡ], kaf affrication) vs Northern qəltu (`ar-IQ-x-qeltu`, qaf→[q] retained), the defining Mesopotamian isogloss; shared interdental retention and emphatic backing |
| [ar-maghrebi-yemeni-sudanese.md](ar-maghrebi-yemeni-sudanese.md) | Peripheral Arabic — the sedentary Maghreb (`ar-x-maghrebi` → `ar-MA`·`ar-DZ`·`ar-TN`·`ar-LY`, + Hassaniya `ar-MR`): jim→[ʒ], schwa reduction/heavy clusters, Berber substrate; Ṣanʿānī Yemeni (`ar-YE`, qaf→[ɡ], jim→[dʒ], interdental retention, ḍād/ẓāʾ merger); Sudanese (`ar-SD`, jim→[ɟ], qaf→[ɡ]) |

### Berber (Amazigh)

| Doc | Languages covered |
|:---|:---|
| [kab.md](kab.md) | Kabyle / Taqbaylit (Northern Berber; Berber Latin alphabet, gemination-conditioned spirantization, emphatics) |

### Indo-Aryan

| Doc | Languages covered |
|:---|:---|
| [hi.md](hi.md) | Hindi (Devanagari script, schwa deletion, 4-way contrast) |

### Isolate

| Doc | Languages covered |
|:---|:---|
| [eu.md](eu.md) | Basque (Euskara Batua) and its dialects: Biscayan, Gipuzkoan, Upper & Lower Navarrese, Lapurdian, Souletin, and the extinct Roncalese — sibilant systems, aspiration, Souletin /y/ and nasal vowels |

If the language you need isn't in any table above, it doesn't have a
prose page yet — go straight to its JSON spec via `orthography2ipa.get(code)`
as shown earlier, and consider contributing a page alongside a spec
improvement (see [../adding_a_language.md](../adding_a_language.md)).

## Key phenomena cross-reference

Looking for how the library handles a specific phonological phenomenon
rather than a specific language, start here:

| Phenomenon | Languages | Doc |
|:---|:---|:---|
| Final devoicing | de, nl, sv, pl, cs, ru, hu, tr | family docs |
| C/G softening before e/i | fr, it, es, pt, ca, ro, en, sv, nl | [romance.md](romance.md) |
| Vowel reduction (unstressed) | ru, pt-PT, fr (schwa) | [ru.md](ru.md), [pt-PT.md](pt-PT.md) |
| Reduced/absent reduction (Lusophone-African) | pt-AO, pt-CV, pt-MZ | [pt-AO.md](pt-AO.md), [pt-MZ.md](pt-MZ.md) |
| Coda allophony (dark l, coda sibilant) | pt-PT, ca | [pt-PT.md](pt-PT.md), [../allophony.md](../allophony.md) |
| Nasal vowels | fr, pt, pl, eu-x-zuberera, eu-x-erronkariera | [fr-FR.md](fr-FR.md), [slavic.md](slavic.md), [eu.md](eu.md) |
| Apical/laminal sibilant contrast (s̺/s̻) | eu (retained east), eu-x-bizkaiera (merged) | [eu.md](eu.md) |
| Aspiration (/h/, aspirated stops) | eu-x-zuberera, eu-x-nafarra-beherea, eu-x-lapurtera | [eu.md](eu.md) |
| Retroflex consonants | sv (from r+C), hi, sa, pt-BR-x-caipira (coda /r/→[ɻ]) | [hi.md](hi.md), [pt-BR-x-caipira.md](pt-BR-x-caipira.md) |
| Schwa deletion | hi, bn, mr, pa | [hi.md](hi.md) |
| Abugida (inherent vowel) | hi, sa, mr, bn, te, kn, ml | [hi.md](hi.md) |
| Vowel harmony | fi, hu, tr, ko | family docs |
| Geminate consonants | it, fi, hu, ja, kab | [it-IT.md](it-IT.md), [kab.md](kab.md) |
| Spirantization (lax stop → fricative) | kab | [kab.md](kab.md) |
| Tone / pitch accent | sv, zh, ja, ko, vi | — |
| Liaison / sandhi | fr, pt, sa | [fr-FR.md](fr-FR.md) |
| Tashkeel-dependent input | ar, ar-SY, ar-LB, ar-JO, ar-PS, ar-IQ, ar-IQ-x-qeltu, ar-MA, ar-DZ, ar-TN, ar-LY, ar-MR, ar-YE, ar-SD | [ar.md](ar.md), [ar-x-levantine.md](ar-x-levantine.md), [ar-IQ.md](ar-IQ.md), [ar-maghrebi-yemeni-sudanese.md](ar-maghrebi-yemeni-sudanese.md) |
| gilit/qəltu qaf split ([ɡ] vs [q]) | ar-IQ, ar-IQ-x-qeltu | [ar-IQ.md](ar-IQ.md) |
| Velar affrication (kaf→[tʃ], gaf→[dʒ]) | ar-IQ, ar-SA-x-najd | [ar-IQ.md](ar-IQ.md) |
| Maghrebi jim ج→[ʒ] (vs [dʒ]) | ar-x-maghrebi, ar-MA, ar-DZ, ar-TN, ar-LY, ar-MR | [ar-maghrebi-yemeni-sudanese.md](ar-maghrebi-yemeni-sudanese.md) |
| Sudanese jim ج→[ɟ] (voiced palatal) | ar-SD | [ar-maghrebi-yemeni-sudanese.md](ar-maghrebi-yemeni-sudanese.md) |
| Ṣanʿānī qaf→[ɡ] + ḍād/ẓāʾ merger →[ðˤ] | ar-YE | [ar-maghrebi-yemeni-sudanese.md](ar-maghrebi-yemeni-sudanese.md) |
| Maghrebi short-vowel reduction (→schwa/Ø, clusters) | ar-x-maghrebi, ar-MA, ar-DZ, ar-TN, ar-LY | [ar-maghrebi-yemeni-sudanese.md](ar-maghrebi-yemeni-sudanese.md) |
| Imāla (/aː/→[eː]) | ar-LB | [ar-x-levantine.md](ar-x-levantine.md) |
| Diphthong monophthongization | ar-x-levantine, ar-SA-x-hejaz | [ar-x-levantine.md](ar-x-levantine.md) |
