# Levantine Arabic (ar-x-levantine and the four cities) — Phonology Reference

**Codes**: `ar-x-levantine` (proto-parent), `ar-SY` (Damascene), `ar-LB` (Beiruti),
`ar-JO` (Ammani), `ar-PS` (Palestinian)
**Family**: Afro-Asiatic > Semitic | **Script**: Arabic (abjad) | **Quality tier**: research

---

## Input contract

Like [`ar`](ar.md), every Levantine spec assumes **fully-diacritized (tashkeel-marked)
Arabic**. Short vowels, gemination (shadda) and sukūn surface only where they are written.
Undiacritized text is not disambiguated — there is no diacritic-restoration step — so a bare
consonant skeleton transcribes incompletely. This is a documented contract, not a bug.

## Inheritance structure

```
arb → ar-x-mashriqi → ar-x-levantine → { ar-SY, ar-LB, ar-JO, ar-PS }
```

Genuinely shared urban-Levantine processes live on `ar-x-levantine` and are inherited by all
four cities via `graphemes_base`/`allophones_base` and id-keyed `allophone_rules` overlay.
Per-city phonology is a small delta on the individual spec.

## Shared features (on the proto-parent)

| Feature | Realisation | Source (read) |
|:---|:---|:---|
| ق qaf | urban koine → **[ʔ]**; Bedouin/rural → [ɡ]; central-rural Palestinian → [k]; qeltu enclaves → [q] | Fadda 2016:28 (after Al-Wer & Herin 2011:60) |
| ج jim | urban → **[ʒ]**; Bedouin/rural → [dʒ] | Al-Wer 2020:560 |
| Interdentals /θ ð ðˤ/ | urban koine → stops **[t d dˤ]**; rural/Bedouin/Druze retain | Cotter 2016:150–154; Fadda 2016:27–28 |
| Diphthongs /aj aw/ | → **[eː oː]** (`AR_LEV_MONO_AY`/`AR_LEV_MONO_AW`) | Almbark & Hellmuth 2015 §1.1; Fadda 2016:30 |
| Emphasis spreading | /a aː/ → **[ɑ ɑː]** adjacent to /tˤ dˤ sˤ ðˤ zˤ/ (`AR_LEV_EMPH_BACK_*`) | Watson 2002; Almbark & Hellmuth 2015 §1 |

The urban Levantine **vowel system** is five long /iː eː aː oː uː/ over three contrastive short
/i a u/; the mid short vowels [e o] and schwa [ə] are allophones of /i u/, not phonemes. This is
the acoustic finding of Almbark & Hellmuth's (2015) study of fifteen Damascene speakers
(§3–4), refining Cowell's (1964) auditory ten-vowel classification. The mid-long /eː oː/ derive
historically from the Classical diphthongs /aj aw/ ("coalescence of vowel-glide sequences ...
bajt~beːt 'home'", §1.1), which is exactly what `AR_LEV_MONO_*` model.

```python
from orthography2ipa import G2P
lev = G2P("ar-x-levantine")
lev.transcribe("بَيْت")   # beːt  (/aj/ → [eː])
lev.transcribe("صَوْت")   # sˤoːt (/aw/ → [oː])
lev.transcribe("صَار")    # sˤɑːr (emphatic backing /aː/ → [ɑː])
```

## Per-city deltas

### Damascene — `ar-SY`
The most influential prestige koine. ق → [ʔ], ج → [ʒ], interdentals → stops. Almbark & Hellmuth
(2015, p.2) report Damascene /aː/ is **less** fronted than Coastal Syrian, so **no strong imāla
rule is declared** here — Damascene inherits only the shared monophthongization and emphasis
backing. `قَلْب` → `ʔalb`, `ثَلْج` → `talʒ`.

### Beiruti — `ar-LB` (strong imāla)
The salient Lebanese marker is pervasive **imāla**: Classical /aː/ is fronted and raised to
**[eː]** outside emphatic/guttural environments, and final /-a/ (tāʔ marbūṭa ة) raises to **[e]**.
Modelled as `allophone_rules` that compose *after* the inherited emphasis-backing rules:

```python
lb = G2P("ar-LB")
lb.transcribe("بَاب")   # beːb  (imāla: /aː/ → [eː])
lb.transcribe("رَاح")   # raːħ  (blocked by the guttural /ħ/)
lb.transcribe("صَار")   # sˤɑːr (emphatic → [ɑː], inherited, bleeds imāla)
```

Rule ordering does the blocking cleanly in a single realisation pass: the inherited
`AR_LEV_EMPH_BACK_AA_*` fire first (emphatic /aː/ → [ɑː]); then `LB_IMALA_BLOCK_GUTT_*` are
identity rules that keep /aː/ in guttural contexts; only the remaining plain /aː/ reaches
`LB_IMALA_RAISE_AA` → [eː]. **Honesty note:** the guttural set covers pharyngeal/uvular/glottal
consonants but not /r/; and the specifically *Beiruti* magnitude of the raise rests partly on
secondary description (Naïm's Beirut grammar was not obtained) — see the spec `notes`. The
final-/-a/ rule also surfaces a pre-existing base artifact whereby a fatḥa + tāʔ marbūṭa both
appear (`madrasaa` → `madrasae`); the raising itself is correct on the final segment.

### Ammani — `ar-JO`
A **new dialect** formed from Jordanian + urban-Palestinian contact (Al-Wer 2020). ق is a socially
reallocated variable [ɡ] ~ [ʔ] (third-generation women use [ʔ] consistently, men both; Al-Wer
2020:560) — listed [ɡ] first as the distinctively Jordanian value. ج → [dʒ] ~ [ʒ]. The koine
favours the merged interdental stops [t d dˤ], making its consonant system "identical to other
Levantine cities" (Fadda 2016:27–28). `قَلْب` → `ɡalb`, `جَمَل` → `dʒamal`, `بَيْت` → `beːt`.

### Palestinian — `ar-PS`
Internally diverse along an urban/rural/Bedouin axis. ق is the classic **four-way split** (Fadda
2016:28, after Al-Wer & Herin 2011:60): urban Jerusalem/Jaffa → [ʔ]; central/northern rural West
Bank → [k] (with the "kaf shift" /k/ → [tʃ]); southern/Bedouin, and indigenous Gaza City → [ɡ]
(Cotter 2016:152); [q] in qeltu enclaves. ج → [ʒ] (urban) ~ [dʒ] (rural). Interdentals → stops in
the urban koine (Cotter 2016:150–154). `قَلْب` → `ʔalb`, `جَمَل` → `ʒamal`.

## Sources actually read

- **Almbark, R. & Hellmuth, S. 2015.** *Acoustic analysis of the Syrian Arabic vowel system.*
  ICPhS 2015, paper 0612. Read in full (PDF).
- **Cotter, W. M. 2016.** *One Piece of the Puzzle: Notes on the Historic Interdental Fricatives
  /θ, ð, ðˤ/ in the Arabic Dialect of Gaza City.* JAIS 16:149–162. Read in full (PDF).
- **Al-Wer, E. 2020.** *New-dialect formation: The Amman dialect.* In Lucas & Manfredi (eds.),
  *Arabic and contact-induced change*, 551–566. Language Science Press. Read in full (PDF).
- **Fadda, H. 2016.** *Language Variation in Western Amman.* MA thesis, CanIL. Read (phonology
  chapter, pp. 27–30, 52).
- **Cowell, M. W. 1964.** *A Reference Grammar of Syrian Arabic.* Georgetown UP. **Not obtained**
  (Internet Archive borrow-only); its Damascene vowel classification is cited only as reported and
  re-tested by Almbark & Hellmuth (2015 §1.3).
- **Watson, J. C. E. 2002.** *The Phonology and Morphology of Arabic.* OUP. Cited for
  emphasis-spreading (not obtained in full).

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [ar](ar.md), [ar-IQ](ar-IQ.md)*
