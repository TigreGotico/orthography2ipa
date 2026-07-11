# European Portuguese (pt-PT) — Phonology Reference

**Code**: `pt-PT` | **Family**: Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Sources**: Mateus & d'Andrade (2000), Cruz-Ferreira (1995, *JIPA* 25(2)), Cunha & Cintra (1984), Mateus et al. (2003)

European Portuguese (EP) is the Lisbon-based standard variety. Its defining
phonological traits are extreme unstressed vowel reduction and a rich set of
coda consonant realisations. This page documents what the `pt-PT` spec models
and, as importantly, where each process lives in the pipeline.

---

## Two maps: where each process is modelled

The library realises pronunciation as two maps — a **pre-lexical**
orthography→phoneme map (`graphemes` + `positional_graphemes`) and a
**post-lexical** phoneme→surface-allophone map (`allophone_rules`; see
[../allophony.md](../allophony.md)). EP splits cleanly across the two:

| Process | Where | Field |
|:---|:---|:---|
| Unstressed vowel reduction | pre-lexical | `positional_graphemes` |
| Dark / velarised coda /l/ | post-lexical | `allophone_rules` |
| Coda sibilants (*chiado*) | post-lexical | `allophone_rules` |
| Coda-/s/ voicing across words | sandhi | `sandhi_rules` |

## Unstressed vowel reduction (pre-lexical)

The single most diagnostic EP feature. Unstressed vowels raise/centralise:

| Vowel | Stressed | Unstressed | Example |
|:---:|:---:|:---:|:---|
| a | [a] | [ɐ] | `cada` [ˈkadɐ] |
| e | [ɛ]/[e] | [ɨ] (word-final often deletable) | `pele` [ˈpɛlɨ] |
| o | [ɔ]/[o] | [u] | `bola` [ˈbɔlɐ], `pomar` [puˈmaɾ] |

This is realised **pre-lexically** through the `positional_graphemes`
`nucleus_stressed` / `nucleus_unstressed` / `pretonic` / `posttonic` /
`word_final` rows, which condition the grapheme's IPA on stress and position.
Because reduction is already fully handled there, the `allophone_rules` layer
does **not** restate it (a redundant stress-conditioned allophone rule would
be inert). Word-final [ɨ] deletion is optional and left to downstream prosody.

## Coda consonants (post-lexical `allophone_rules`)

EP realises three coda consonant processes that the pre-lexical grapheme map
cannot reach cleanly at word edges. They ship as `allophone_rules`, keyed on
`syllable_position: "coda"`:

| Rule id | Process | Example |
|:---|:---|:---|
| `PT_CODA_L_DARK` | velarised coda /l/ → [ɫ] | `sol` [ˈsɔɫ], `alto` [ˈaɫtu] |
| `PT_CODA_S_HUSH` | Lisbon coda /s/ → [ʃ] (*chiado*) | `pasta` [ˈpaʃtɐ] |
| `PT_CODA_Z_HUSH` | Lisbon coda /z/ → [ʒ] | (voiced counterpart) |

An **onset** /l/ or /s/ is unaffected: `bola` [ˈbɔlɐ], `casa` [ˈkazɐ]. Coda-/s/
voicing before a following voiced consonant across a word boundary
(`os dias` → [ʒ]) is handled separately by the `PT_CODA_S_VOICING` sandhi rule.

The coda sibilant values are the **Lisbon/standard** realisation. Some
northern and insular dialects keep an apico-alveolar [s̺] in coda; those are
dialect deltas carried by the `pt-PT-x-*` specs, which inherit these three
base rules by id-keyed overlay and override only what differs.

## External /s/-sandhi before a vowel (`sandhi_rules`)

A word-final coda /s/ — which surfaces `[ʃ]` in isolation and before a
consonant via `PT_CODA_S_HUSH` — **voices across a word boundary** before a
vowel-initial following word (the final sibilant is resyllabified and treated
as intervocalic). The base `pt-PT` gives the **standard alveolar `[z]`**:

| Rule id | Context | Example |
|:---|:---|:---|
| `PT_FINAL_S_PREVOCALIC_VOICE` | `…s#` + `#V…` | `estás a ver` → [eˈʃtaz ˈɐ ˈvɛɾ] |
| | | `os amigos` → [ˈoz ɐˈmiɡuʃ] |

The rule fires only before a **vowel**: before a consonant the sibilant stays
`[ʃ]` (`estás bem` → [eˈʃtaʃ ˈbɛm]), and a voiceless-initial next word does not
voice (`estás feliz` → [eˈʃtaʃ fɨˈliʃ]). Single-word transcription is
unchanged (`estás` → [eˈʃtaʃ]); the benchmark scores single words, so this
cross-word rule never affects the scoreboard.

The place of articulation splits **dialectally**. The standard alveolar `[z]`
holds across the North (Porto, Braga), Lisbon and — variably — the neutral
centre (Coimbra). The **South (Algarve) and the Azores (São Miguel)** instead
palatalise this prevocalic sibilant to `[ʒ]` (the "Tajaver" pronunciation):

| Variety | Prevocalic value | `estás a ver` |
|:---|:---:|:---|
| North — [pt-PT-x-porto](pt-PT-x-porto.md) | alveolar `[z]` | [eˈʃtaz ˈɐ ˈbɛɾ] |
| Lisbon — [pt-PT-x-lisbon](pt-PT-x-lisbon.md) | alveolar `[z]` | [eˈʃtaz ˈɐ ˈvɛɾ] |
| **Coimbra (centre)** — [pt-PT-x-coimbra](pt-PT-x-coimbra.md) | variable `[z]`~**`[ʒ]`** (models `[ʒ]` pole) | [eˈʃtaʒ ˈɐ ˈvɛɾ] |
| **Algarve** — [pt-PT-x-algarve](pt-PT-x-algarve.md) | **`[ʒ]`** (categorical) | [eˈʃtaʒ ˈɐ ˈvɛɾ] |
| **Azores / São Miguel** — [pt-PT-x-sao-miguel](pt-PT-x-sao-miguel.md) | **`[ʒ]`** (prevocalic only) | [eˈʃtaʒ ˈɐ ˈvɛɾ] |

The Algarve realises word-final /s/ as `[ʒ]` in **all** word-final positions
(via its positional `word_final` map), so `[ʒ]` also surfaces prevocalically;
São Miguel restricts `[ʒ]` to the **prevocalic** sandhi (re-declaring
`PT_FINAL_S_PREVOCALIC_VOICE` with transform `ʒ`), keeping `[ʃ]` before a
consonant or pause. Coimbra is variable `[z]`~`[ʒ]`; its dedicated spec
[pt-PT-x-coimbra](pt-PT-x-coimbra.md) models the marked local `[ʒ]` pole (the
Coimbra speaker in *Portuguese With Leo*, "Coimbra tem sotaque?", demonstrates
"os olhos" with the J-sound). **Flagged counter-evidence:** the
[Trás-os-Montes](pt-PT-x-trasosmontes.md) deep-dive speaker (Chaves) also uses
prevocalic `[ʒ]` and reports it "muito espalhado" into the North — contradicting
the `[z]`-across-the-North claim above; this is recorded in the
`pt-PT-x-trasosmontes` notes but **not** modelled (single casual attestation vs
the standard academic `[z]`).

**Sourcing.** The standard `[z]` value is well documented (Mateus & d'Andrade
2000: ch.2; Wikipedia *Portuguese phonology*, Consonant sandhi: `bons amigos`
[bõz ɐˈmiɣuʃ]). The Southern/Azorean **`[ʒ]`-prevocalic** value is described
natively by *Portuguese With Leo*, "The 8 accents"
([video](https://www.youtube.com/watch?v=pitj0XxYO7I); native-speaker /
popular-linguistics, **not** academic), which places it strongest in the Algarve
("Tajaver", "quijentrar", "muitojamigos"), shared by São Miguel ("Todojos",
"quijentrar"), variable in Coimbra, and **absent in Lisbon and the North** (both
`[z]`; the video explicitly calls `[ʒ]` there "wrong"). A page-pinned academic
source for the prevocalic-`[ʒ]` sandhi *specifically* was not located — the
feature sits within the documented southern/insular final-sibilant behaviour
(`[ʃ]`~`[z]`~`[ʒ]`) but the honest bound is stated in the `pt-PT-x-acores` /
`pt-PT-x-algarve` spec notes. (Cintra's 1971 primary North/South isogloss is a
separate matter — the *place*, apico-alveolar vs predorsodental, of the
sibilant, not this `[z]`/`[ʒ]` contrast.)

## Not modelled in the base

**Intervocalic voiced-stop spirantisation** (`/b d ɡ/ → [β ð ɣ]`; Mateus &
d'Andrade 2000) is a genuine EP process but is **deliberately not encoded**:
every available `pt` gold (`infopedia_pt`, `ep_dialects`, WikiPron) is
broad/phonemic and transcribes the plain stops, so a spirantisation rule is
linguistically correct yet regresses all measurable golds with none rewarding
it. It is left for a future narrow-transcription task, consistent with the
honesty gate ("a rule ships if correct *and* neutral-or-better on an adequate
gold").

## Benchmark effect

Adding the three coda rules (PER, lower is better):

| Gold | n | Before | After | Δ |
|:---|---:|---:|---:|---:|
| infopedia_pt (human lexicon) | 295 | 0.3160 | 0.2942 | **−0.0218** |
| ep_dialects (CLUP) | 30 | 0.2599 | 0.2218 | **−0.0381** |
| styletts2_phonemes | 300 | 0.3999 | 0.3871 | **−0.0128** |
| wikipron pt | 242 | 0.1817 | 0.2090 | +0.0273 |

The coda sibilant rules improve every gold. The dark coda /l/ rule improves
the narrow human golds but regresses the broad WikiPron `pt` row (+0.031,
above the 0.005 CI threshold) because WikiPron transcribes EP coda /l/ as
plain `[l]`; the rule is kept per the honesty gate (linguistically robust,
rewarded by the higher-quality human golds) with the divergence documented
rather than hidden.

## Other notes

- Portuguese preserves the /v/~/b/ distinction (unique in Ibero-Romance;
  Castilian merged them).
- Nasal vowels and nasal diphthongs (`ão`, `ãe`, `õe`) are diagnostic and
  drive final-stress placement.
- Input is standard orthography under the Acordo Ortográfico (1990).

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [romance](romance.md), [pt-PT-x-lisbon](pt-PT-x-lisbon.md), [pt-PT-x-porto](pt-PT-x-porto.md)*
