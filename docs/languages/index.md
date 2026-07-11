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
| [pt-PT.md](pt-PT.md) | European Portuguese in detail (coda allophony, vowel reduction) |
| [pt-UY.md](pt-UY.md) | Uruguayan Portuguese / Riverense / DPU (border-contact variety: ⟨lh⟩→[j], dental /t d/ before /i/) |
| [pt-TL.md](pt-TL.md) | East Timorese Portuguese (`pt-TL`) — L2/official variety; no vowel reduction (Tetum substrate), alveolar rhotic; NOT the Bidau creole |
| [pt-MO.md](pt-MO.md) | Macau Portuguese (`pt-MO`) — EP-following; thin literature (skeleton); NOT the Patuá/maquista creole |
| [lij.md](lij.md) | Ligurian / Genoese (Gallo-Italic; grafia ofiçiâ, ⟨x⟩=/ʒ/, ⟨o⟩=/u/, ⟨u⟩=/y/) |

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

### Berber (Amazigh)

| Doc | Languages covered |
|:---|:---|
| [kab.md](kab.md) | Kabyle / Taqbaylit (Northern Berber; Berber Latin alphabet, gemination-conditioned spirantization, emphatics) |

### Indo-Aryan

| Doc | Languages covered |
|:---|:---|
| [hi.md](hi.md) | Hindi (Devanagari script, schwa deletion, 4-way contrast) |

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
| Coda allophony (dark l, coda sibilant) | pt-PT, ca | [pt-PT.md](pt-PT.md), [../allophony.md](../allophony.md) |
| Nasal vowels | fr, pt, pl | [fr-FR.md](fr-FR.md), [slavic.md](slavic.md) |
| Retroflex consonants | sv (from r+C), hi, sa | [hi.md](hi.md) |
| Schwa deletion | hi, bn, mr, pa | [hi.md](hi.md) |
| Abugida (inherent vowel) | hi, sa, mr, bn, te, kn, ml | [hi.md](hi.md) |
| Vowel harmony | fi, hu, tr, ko | family docs |
| Geminate consonants | it, fi, hu, ja, kab | [it-IT.md](it-IT.md), [kab.md](kab.md) |
| Spirantization (lax stop → fricative) | kab | [kab.md](kab.md) |
| Tone / pitch accent | sv, zh, ja, ko, vi | — |
| Liaison / sandhi | fr, pt, sa | [fr-FR.md](fr-FR.md) |
| Tashkeel-dependent input | ar, ar-SY, ar-LB, ar-JO, ar-PS | [ar.md](ar.md), [ar-x-levantine.md](ar-x-levantine.md) |
| Imāla (/aː/→[eː]) | ar-LB | [ar-x-levantine.md](ar-x-levantine.md) |
| Diphthong monophthongization | ar-x-levantine, ar-SA-x-hejaz | [ar-x-levantine.md](ar-x-levantine.md) |
