# European Portuguese (pt-PT) — Phonology Reference

**Code**: `pt-PT` | **Family**: Indo-European > Romance | **Script**: Latin (alphabet)
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
| Coda vowel nasalisation (⟨m/n⟩) | pre-lexical **+** post-lexical | `positional_graphemes` (tilde) **+** `allophone_rules` (quality) |
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

## Coda vowel nasalisation (pre-lexical tilde + post-lexical quality)

A defining feature of Portuguese: a vowel followed by a **tautosyllabic (coda)
nasal** ⟨m⟩ or ⟨n⟩ — word-finally or before another consonant — **nasalises**,
and the nasal consonant is absorbed into the resulting nasal vowel rather than
pronounced as a separate segment (Mateus & d'Andrade 2000: ch. 2, *Nasality*).
Portuguese has five phonemic nasal vowels, **/ɐ̃ ẽ ĩ õ ũ/**:

| Spelling | Oral base | Nasal vowel | Example |
|:---|:---:|:---:|:---|
| ⟨am⟩/⟨an⟩ | [a] → [ɐ] | [ɐ̃] | `campo` [ˈkɐ̃pu], `cantar` [kɐ̃ˈtaɾ], `ambos` [ˈɐ̃buʃ] |
| ⟨em⟩/⟨en⟩ | [ɛ] → [e] | [ẽ] | `tempo` [ˈtẽpu], `entre` [ˈẽtɾɨ] |
| ⟨im⟩/⟨in⟩ | [i] | [ĩ] | `sim` [ˈsĩ], `fim` [ˈfĩ], `lindo` [ˈlĩdu] |
| ⟨om⟩/⟨on⟩ | [ɔ] → [o] | [õ] | `bom` [ˈbõ], `onde` [ˈõdɨ] |
| ⟨um⟩/⟨un⟩ | [u] | [ũ] | `mundo` [ˈmũdu], `um` [ˈũ] |

The process splits across the two maps by design, exactly as the
[Barranquenho](ext-PT-x-barrancos.md) spec models it:

- **Pre-lexical (the nasalisation itself).** The `positional_graphemes` entries
  for `m` and `n` map the coda positions (`before_consonant`, `word_final`) to a
  single **U+0303 combining tilde** `[̃]`. This deletes the coda nasal consonant
  and nasalises the preceding vowel by concatenation. An **onset (intervocalic)**
  ⟨m/n⟩ matches none of these coda keys, so it stays a plain consonant and leaves
  the vowel **oral**: `cama` [ˈkamɐ], `ano` [ˈɐnu], `nome` [ˈnɔmɨ].
- **Post-lexical (the vowel quality).** Four `allophone_rules` —
  `PT_NASAL_A_RAISE` (a→ɐ), `PT_NASAL_E_RAISE` (ɛ→e), `PT_NASAL_O_RAISE` (ɔ→o),
  and `PT_NASAL_O_UNRED` (reduced u→o, see below) — raise the vowel to the
  **oral base** of its nasal quality, conditioned `followed_by_phoneme: [̃]`.
  They fire *only* when the next segment is the nasalisation tilde, so oral
  vowels before an onset nasal are untouched. The surface is always the
  **oral** base; the tilde is supplied solely by the m/n slot, so a vowel is
  **never doubly-tilded**. A **lexical** ⟨i⟩ or ⟨u⟩ needs no rule — its nasal
  quality [ĩ ũ] already shares the oral base [i u] (`sim` [ˈsĩ], `mundo`
  [ˈmũdu], `um` [ˈũ]).

### Reduced ⟨o⟩ before a nasal: [õ], not [ũ] (`PT_NASAL_O_UNRED`)

EP unstressed vowel reduction lowers ⟨o⟩ to [u] (`contar` → naively
`[kũˈtaɾ]`). But that reduction is **blocked before a coda nasal**: an
unstressed ⟨o⟩ before ⟨m/n⟩ surfaces as the nasal mid **[õ]**, never **[ũ]**
(Mateus & d'Andrade 2000: ch. 2, *Nasality* — EP nasal [õ] does not raise to
[ũ]). Because the pre-lexical map has already reduced the vowel to [u] by the
time the allophone layer runs, `PT_NASAL_O_UNRED` lowers that reduced [u] back
to the oral [o] before the tilde: `contar` [kõˈtaɾ], `comprar` [kõˈpɾaɾ],
`bondade` [bõˈdadɨ], `pombal` [põˈbaɫ], `montanha` [mõˈtaɲɐ], `bombom`
[bõˈbõ]. The rule is **gated on the source grapheme ⟨o⟩** (the new
`AllophoneRule.grapheme` condition): it fires only on a *reduced ⟨o⟩*, so a
**lexical ⟨u⟩** before a nasal keeps its genuine high [ũ] — `um` [ˈũ], `mundo`
[ˈmũdu], `algum` [aɫˈɡũ], `segundo` [sɨˈɡũdu] — since both are the same phoneme
[u] and only the spelling distinguishes them. pt-BR and the non-reducing
Lusophone variants (pt-AO/MZ/TL) never reduce ⟨o⟩→[u], so their ⟨o⟩ before a
nasal is already [o] and this rule is inert there.

### Engine guard: the nasal tilde attaches only to a vowel

The coda ⟨m/n⟩ → tilde slot carries an **oral consonant fallback** ([m]/[n])
below the tilde in the beam. A shared engine guard (`_expand_beam`) suppresses
the tilde branch whenever the phoneme it would land on is **not** an oral vowel
or a nasal-diphthong glide, so the fallback consonant wins instead. This keeps
the output valid IPA in two edge cases: (1) the pre-existing ⟨gu⟩→[ɡ]
vowel-drop (`algum`, `segundo`) that strands a consonant in the coda slot — the
tilde is no longer emitted onto [ɡ] (was the invalid `[ɐˈɫɡ̃]`); and (2) ⟨nn⟩
loans (`inn`, `Finn`) where a second nasal slot would otherwise stack a second
tilde onto an already-nasalised nucleus. The guard is generic and byte-neutral:
a tilde that lands on a vowel is never touched, so all prior behaviour and the
nasal diphthongs ⟨ão ãe õe⟩ (glide carriers [w̃ j̃]) are unchanged.

Two collisions are avoided by construction:

- **⟨nh⟩/⟨lh⟩ digraphs stay intact.** Maximal-munch tokenisation consumes ⟨nh⟩ as
  a single grapheme (→ [ɲ]) *before* the standalone-⟨n⟩ rule can see it, so the
  ⟨n⟩ of ⟨nh⟩ never nasalises the preceding vowel: `banho` [ˈbaɲu].
- **Nasal diphthongs ⟨ão ãe õe⟩ stay intact.** These are whole graphemes
  (→ [ɐ̃w̃], [ɐ̃j̃], [õj̃]) with no standalone ⟨m/n⟩, so the coda-nasal mechanism
  does not touch them: `pão`, `mãe`, `põe`.

**Benchmark effect.** Coda nasalisation is pervasive, so it moves every scored
`pt` gold. It improves all the human/lexicon golds — `infopedia_pt`
(0.308→0.265), `ep_dialects` pt-PT (0.213→0.173),
`portuguese_phonetic_lexicon` pt-PT (0.211→0.145), pt-BR (0.275→0.223), and
the crowd-scraped WikiPron `pt` (0.207→0.180), pt-BR (0.154→0.108) — and, by
inheritance, every `pt-PT-x-*` dialect row (−0.03 to −0.05 on the CLUP and
`ep_dialects` golds). The reduced-⟨o⟩→[õ] fix (`PT_NASAL_O_UNRED`) sharpens
these further beyond the raw nasalisation, since unstressed ⟨o⟩ before a nasal
(`contar`, `bondade`, `comprar`) is frequent. The **one** row that regresses
slightly is `styletts2_phonemes` (0.384→0.389, within overlapping CIs): that
gold is
machine-generated by an espeak-style phonemiser that transcribes coda nasality
as a nasal vowel **plus** a retained nasal consonant / [ŋ] (`campo` → `kˈɐ̃mpʊ`,
`conde` → `kˈoŋdɨ`), whereas the standard broad transcription — and every
higher-quality gold here — **absorbs** the consonant into the nasal vowel
(`campo` [ˈkɐ̃pu]). Per the honesty gate the change is kept: it is linguistically
correct and rewarded by the trustworthy golds, with the lone machine-gold
divergence documented rather than hidden. See [../scoreboard.md](../scoreboard.md).

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

This rule fires only before a **vowel**. Coda /s/ before a *consonant* is
handled by the separate voicing-assimilation rule below: it voices to `[ʒ]`
before a **voiced** consonant (`estás bem` → [eˈʃtaʒ ˈbɛm]) and stays `[ʃ]`
before a **voiceless** one (`estás feliz` → [eˈʃtaʃ fɨˈliʃ]). Single-word
transcription is unchanged (`estás` → [eˈʃtaʃ]); the benchmark scores single
words, so these cross-word rules never affect the scoreboard.

## External /s/-sandhi before a consonant — voicing assimilation (`sandhi_rules`)

Across a word boundary, a word-final coda /s/ **assimilates in voicing** to the
following consonant, surfacing as post-alveolar `[ʒ]` before a **voiced**
consonant and staying `[ʃ]` before a **voiceless** one (regular EP coda-sibilant
sandhi; Mateus & d'Andrade 2000: ch.2):

| Rule id | Context | Example |
|:---|:---|:---|
| `PT_CODA_S_VOICING` | `…s#` + `#[voiced C]…` | `as bocas` → [ˈɐʒ ˈbɔkɐʃ] |
| | | `os dois` → [ˈoʒ ˈdojʃ] |

The `right_context` admits an optional leading primary/secondary stress mark
(`^[ˈˌ]?[bdgvzʒmnɲɾʁlʎ]`) so it fires on a stress-initial next word, whose
per-word IPA begins with `ˈ` (`bocas` → `ˈbɔkɐʃ`). All `pt-PT-x-*` varieties
inherit this rule by id-keyed overlay, so São Miguel — which keeps `[ʃ]` before
a *voiceless* consonant and in isolation — still voices to `[ʒ]` before a voiced
one (`estás bem` → [eˈʃtaʒ ˈbɛm]); the Algarve already realises every word-final
/s/ as `[ʒ]` via its positional `word_final` map.

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
São Miguel restricts its *prevocalic* `[ʒ]` to before a vowel (re-declaring
`PT_FINAL_S_PREVOCALIC_VOICE` with transform `ʒ`), keeping `[ʃ]` before a
voiceless consonant or pause (before a voiced consonant the inherited
`PT_CODA_S_VOICING` still gives `[ʒ]`). Coimbra is variable `[z]`~`[ʒ]`; its dedicated spec
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
  drive final-stress placement; coda-conditioned nasalisation of the plain
  vowels is documented above ("Coda vowel nasalisation").
- Input is standard orthography under the Acordo Ortográfico (1990).

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [pt-BR](pt-BR.md), [romance](romance.md), [pt-PT-x-lisbon](pt-PT-x-lisbon.md), [pt-PT-x-porto](pt-PT-x-porto.md)*
