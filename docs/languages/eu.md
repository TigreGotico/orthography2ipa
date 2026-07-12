# Basque (Euskara) and its dialects

Basque (`eu`) is a **language isolate** — it has no demonstrated genetic
relationship to any other language family. The library ships Standard
Basque (Euskara Batua) plus seven dialect specs. This page explains what
each spec models and, just as importantly, what it deliberately does *not*
model because standard Basque orthography does not encode it.

All claims below are grounded in sources that were read directly; page
numbers are given. The two most useful open-access references are the
*Illustrations of the IPA* for two specific towns — Goizueta (a
conservative High Navarrese variety) and Markina (a Biscayan variety) —
which between them document the two ends of the western–eastern sound
change continuum.

## Sources read

- **Hualde, Lujanbio & Zubiri (2010),** "Goizueta Basque",
  *JIPA* 40(1): 113–127.
  [doi:10.1017/S0025100309990260](https://doi.org/10.1017/S0025100309990260)
- **Bedialauneta Txurruka & Hualde (2023),** "Markina Basque",
  *JIPA* 53(3): 1095–1122.
  [doi:10.1017/S0025100322000032](https://doi.org/10.1017/S0025100322000032)
- **Hualde (2018),** "Aspiration in Basque",
  *Papers in Historical Phonology* 3: 1–27.
  [doi:10.2218/pihph.3.2018.2602](https://doi.org/10.2218/pihph.3.2018.2602)
- **Egurtzegi (2013),** "Phonetics and Phonology", ch. 4 in Martínez-Areta
  (ed.), *Basque and Proto-Basque* (Peter Lang): 119–183.
- **Michelena (1977),** *Fonética Histórica Vasca* (FHV) — consulted as
  page-cited within Egurtzegi (2013) and Hualde (2018), not in the
  original.

## The base inventory (`eu`, Euskara Batua)

Conservative Basque has a **three-way sibilant place contrast** — the
typologically notable feature of the language (Hualde et al. 2010: 119):

| Orthography | Fricative | Affricate |
|:---|:---|:---|
| z / tz | lamino-alveolar `s̻` | `ts̻` |
| s / ts | apico-alveolar `s̺` | `ts̺` |
| x / tx | postalveolar `ʃ` | `tʃ` |

Palatal stops `c` (tt) and `ɟ` (dd), palatal nasal `ɲ` (ñ) and palatal
lateral `ʎ` (ll) arise historically from palatalisation of `t d n l`
after `/i/`. Voiced stops `/b d ɡ/` surface as approximants `[β ð ɣ]`
intervocalically (Hualde et al. 2010: 116); nasals assimilate in place to
a following consonant (2010: 120). Five vowels `/i e a o u/` (2010: 122).

Aspiration (`/h/` and aspirated stops) survives only in the **eastern
(continental)** dialects; the west lost it (Hualde 2018: 2).

## Dialects — the west→east continuum

Following Koldo Zuazo's modern classification, the specs map to the
dialects as: Western = Biscayan; Central = Gipuzkoan; (High/Upper)
Navarrese; Navarro-Lapurdian = Lapurdian + Lower Navarrese; Souletin
(Zuberoan); and the extinct Eastern Navarrese = Roncalese.

### Biscayan — `eu-x-bizkaiera` (Western)

Validated against **Markina Basque** (Bedialauneta & Hualde 2023). Western
Basque has **merged** the sibilant contrasts the base keeps:

- apico `s̺` and lamino `s̻` merge to a single **apico-alveolar `s̺`**;
  affricates `ts̺`/`ts̻` merge to a single denti-alveolar `ts̻`
  (2023: 1098). So orthographic `s` and `z` both give `/s̺/`; `ts` and `tz`
  both give `/ts̻/`.
- the palatal stop `c` (tt) merges with `tʃ` (2023: 1098).
- palatalisation after `/i/`: `s→[ʃ]`, `t→[tʃ]`, `n→[ɲ]`, `l→[ʎ]`
  (2023: 1102–1104).
- no aspiration (Hualde 2018: 2).

**Not modelled (engine limit):** the Biscayan raising of the article
`/-a/`→`[-e]` after a high vowel (*baso+a* > *basue*; 2023: 1107–1108) is
a morphophonological process on the article, not a context-free grapheme
rule.

### Gipuzkoan — `eu-x-gipuzkera` (Central)

The closest living dialect to Batua. The three-way sibilant contrast is
retained in eastern Gipuzkoan but is variable and neutralising in western
areas, where the Western merger intrudes (Bedialauneta & Hualde 2023:
1098); the base three-way inventory is kept but is not uniform. `/h/` is
absent (Hualde 2018: 2). The palatal stop `c` is merging with `tʃ` in the
westernmost towns (Hualde et al. 2010: 118). Contrastive **pitch-accent**
is a feature of *specific* northern-Biscayan and Navarrese varieties
(e.g. Goizueta; Hualde et al. 2010: 113, 123), **not** of general
Gipuzkoan — no pitch-accent claim is made here. (A prior draft's inverted
pitch-accent claim was removed.)

### Upper (High) Navarrese — `eu-x-nafarra-garaia`

Validated against **Goizueta** (Hualde et al. 2010), a conservative High
Navarrese variety. Corrections from a prior draft:

- the three-way sibilant contrast is **fully stable** here — the
  neutralisations run further *west*, not in Navarrese (2010: 119). An
  earlier unsourced "merger to `[s]`" claim was removed.
- `/h/` is **absent** (Goizueta has none; 2010: 113 fn. 1).
- incipient **yeísmo**: `ʎ`→`[ʝ]`~`[j]`, in progress (2010: 120).

### Lower Navarrese — `eu-x-nafarra-beherea`

An eastern **aspirating** variety (with Lapurdian it forms Zuazo's
Navarro-Lapurdian dialect). `/h/` is a productive phoneme (Hualde 2018:
1–3), and voiceless stops have aspirated variants `[pʰ tʰ kʰ]` restricted
to the onset of a stressed syllable near the word start (Hualde 2018: 5–6,
reporting Michelena FHV). Less systematically phonemic than in Souletin.

### Lapurdian — `eu-x-lapurtera`

Classical literary dialect (Axular's *Gero*, 1643). Classical Lapurdian
had both `/h/` and aspirated stops (Hualde 2018: 5, list (1)), but coastal
French Basque **lost** aspiration by the 19th century (Hualde 2018: 2),
so modern coastal Lapurdian keeps `/h/` only residually — modelled as
`h→[h]~[∅]`. Full three-way sibilant contrast retained. French-contact
uvular `[ʁ]` appears alongside inherited `[r]/[ɾ]`.

### Souletin (Zuberoan) — `eu-x-zuberera` (easternmost)

The most divergent variety, in contact with Gascon Occitan:

- **front rounded vowel `/y/`** (written ü) — the only Basque dialect with
  a sixth vowel; from older `/u/` by fronting (Egurtzegi 2013: 127–128).
  This is the one distinctive feature recoverable from orthography, and is
  modelled (`ü→/y/`).
- **three-way plosive contrast**: voiced / voiceless-unaspirated /
  voiceless-**aspirated** `pʰ tʰ kʰ` are full phonemes (Hualde 2018: 2,
  citing Lafon 1958/1999).
- two aspirate phonemes: oral `/h/` and nasalised `/h̃/` (Hualde 2018: 2).
- **contrastive nasalised vowels** — Souletin alone among living dialects
  keeps the old nasalised-vowel series, around nasal consonants and in
  stressed final position after apocope of `-n` (*ardu* `[arðũ]` <
  *ardano*; Egurtzegi 2013: 127).

**Not modelled (engine limit):** vowel nasality and the aspirated/
unaspirated stop split are not marked in standard orthography, so they are
documented but not emitted at the grapheme→IPA level.

### Roncalese (Eastern Navarrese) — `eu-x-erronkariera` *(new, extinct)*

The Basque of the Roncal valley in easternmost Navarre; with Salazarese it
forms Zuazo's **Eastern Navarrese** dialect. **Extinct** — its last fluent
speakers were gone by around 1991 (Egurtzegi 2013: 127). Documented by
Bonaparte and by Michelena's FHV. Distinctive features:

- **contrastive nasalised vowels**, kept "exactly as … in the modern
  Souletin dialect" (Egurtzegi 2013: 127). Secondary sources report the
  nasalisation could reach any syllable in Roncalese vs. only the final
  syllable in Souletin (flagged: from an abstract, not fully read).
- eastern aspiration (`/h/` and `[pʰ tʰ kʰ]`), already **receding** toward
  extinction (Hualde 2018: 2–3, 19). Modelled as variable `h→[h]~[∅]` plus
  aspirated-stop variants.
- high-vowel **metaphony** `/i/→/u/` before `/u/` (*tipula* > *tupla*;
  Egurtzegi 2013: 131, citing FHV: 79).
- **intense syncope**, including sibilant+tap clusters found in no other
  dialect (*zira* > *zra* 'you are'; Egurtzegi 2013: 135–136, FHV: 160).

**Not modelled (engine limit):** the nasalisation, metaphony and syncope
are historical/morphophonological and not recoverable from orthography;
only the eastern aspiration is emitted.

## Ancestry & distance

Every dialect declares `parent: eu` with ancestor weight 0.9, so
`ancestry_similarity(get("eu"), get("eu-x-…")) == 0.9` and two sibling
dialects score `0.81`. Because the corrections above touch mostly
`notes`/`sources` and dialect-only grapheme/allophone data, the scored
`eu` benchmark rows are unaffected.

---

## Production tier: orthographic depth, threshold, and benchmark

**Shallow (phonemic) orthography — the ≤ 0.15 PER production threshold
applies** ([quality tiers](../quality_tiers.md)). Euskara Batua spelling
is regular; the palatalization conventions (⟨tt⟩, ⟨dd⟩, ⟨ñ⟩) and
affricate digraphs (⟨tz⟩, ⟨ts⟩, ⟨tx⟩) are closed, encodable rules.

| dataset | provenance | n | PER |
|---|---|---:|---:|
| `wikipron` | crowd-scraped (gate-eligible) | 12 010 | **0.0391** |
| `ipa_childes` | espeak-derived (cannot gate/block) | 3 969 | 0.1297 |
| `hitz_basque_ipa` | machine-generated (cannot certify) | 3 113 | 0.2089 |

The qualifying row is `wikipron`, far below the shallow threshold. The
`hitz_basque_ipa` gap is documented in that dataset's own provenance
note (tool-generated transcriptions in the StyleTTS2 convention), not a
spec regression.

Known engine-limit notes: Basque accent is dialect-variable and never
written (see the spec's documented stress exemption); no stress marks
are emitted.

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)
