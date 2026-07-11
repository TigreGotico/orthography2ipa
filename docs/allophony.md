# Allophony — the second map, made live

The library models pronunciation as **two maps**:

1. **Pre-lexical** — orthography → phoneme. Richly conditioned by
   `positional_graphemes`, the vowel-class positions and candidate weights.
2. **Post-lexical** — phoneme → surface allophone. Historically *inert*:
   `spec.allophones` was stored but never conditioned, and the only consumer
   (`expand_allophones`) dumped every variant into the beam at a flat `+0.5`
   cost with no way to pick the context-correct one.

`allophone_rules` make the second map live. A spec declares an ordered list
of declarative, context-conditioned `phoneme → surface` rewrites; they
compile into a [lattice rescorer](lattice.md) (`AllophoneRescorer`) that the
engine runs as a **deterministic post-lexical pass** — replacing a chosen
phoneme with its single context-correct surface form at the same beam cost.
It is realisation, not search-space inflation.

## Where it runs in the pipeline

```
normalize → tokenize → select (positional + weights)
                          │
                          ▼
                 rescore  ├─ user rescorer(s)
                          └─ allophony  ← allophone_rules compile to here
                          │
                          ▼
                 beam path selection → stress marks → sandhi → dialect
```

Allophony is the **allophony stage** of the pipeline: after phoneme
selection (so it sees the chosen phoneme and its resolved neighbours),
composed *after* any user rescorer, and *before* beam path selection — hence
before stress-mark insertion and cross-word sandhi, which act on the whole
utterance. In the structured lattice this is the second stage: phoneme
lattice → allophone lattice.

Because stress and syllable context are computed only by the engine, the
allophony pass needs the **engine path** (`G2P.transcribe` /
`G2P.ipa_lattice`). On the standalone tokenizer path
(`PhonetokTokenizer.ipa_beam`) there is no stress context, so a
stress-conditioned rule simply does not fire there — identical to how the
stress-conditioned positional rules behave. Word-position and neighbour
conditions work on both paths.

## The condition vocabulary

Each rule targets one or more underlying `phonemes`, a `surface`
realisation, and a set of conditions (all ANDed; a condition left
unset is "don't care"):

| Condition | Values | Fires when |
|---|---|---|
| `word_initial` / `word_final` | `true` / `false` | the grapheme is (not) at the word edge |
| `stress` | `"stressed"` / `"unstressed"` | the grapheme's syllable carries (not) primary stress — engine path only |
| `syllable_position` | `"onset"` / `"coda"` / `"nucleus"` | a vowel is a nucleus; a consonant before a vowel is an onset, else a coda (maximal-onset heuristic) |
| `preceded_by` / `followed_by` | `"vowel"`, `"consonant"`, `"front_vowel"`, `"back_vowel"`, `"word_boundary"` | the previous / next **grapheme** matches that class (predicates from `vowels.py`) |
| `preceded_by_phoneme` / `followed_by_phoneme` | list of IPA strings | the previous / next lattice slot's **chosen phoneme** is one of them |

This small vocabulary expresses the common post-lexical processes:

- **Final-obstruent devoicing** — `word_final: true`.
- **Unstressed vowel reduction** — `stress: "unstressed"`.
- **Intervocalic flapping** — `preceded_by: "vowel"`, `followed_by: "vowel"`.
- **Nasal place assimilation** — `followed_by_phoneme: ["k", "ɡ"]` (→ velar)
  or `["p", "b", "m"]` (→ labial), conditioning on the *following* phoneme's
  place.

Rules are **pure data** — no code in specs. See
[`data/SCHEMA.md`](../orthography2ipa/data/SCHEMA.md#allophone-rule-schema)
for the JSON shape.

## Toggles

- `G2P(lang, apply_allophony=True)` (the default) applies a spec's
  `allophone_rules`. It is a **no-op for every spec that declares none**
  (all shipped specs bar the pilots), so the default engine path is
  byte-identical. Set `apply_allophony=False` to force broad/phonemic output
  even for a spec that declares rules.
- `expand_allophones` is unchanged and independent: it is the
  *enumerate-variants* knob (dump every `spec.allophones` variant into the
  beam), useful for "show me all surface possibilities" — not for picking the
  contextually-correct one.

## Inheritance

`allophone_rules` inherit by **id-keyed overlay**
(`InheritanceMode.OVERLAY_BY_ID`), exactly like `sandhi_rules`: a child spec
that sets `graphemes_base` inherits the parent's whole rule list in order;
an own rule with a matching `id` replaces the inherited one in place, and a
new `id` is appended. A post-lexical process is typically a property of the
whole language — Catalan final devoicing and nasal assimilation hold in
every Catalan variety — so the standard dialects inherit the pilots for free
while remaining able to override a single rule by `id`.

## The Catalan pilots

Catalan (`ca`) is the first spec to declare `allophone_rules`, each cited to
reference grammars:

### 1. Final-obstruent devoicing

Word-final voiced obstruents devoice: `/b d ɡ z ʒ v/ → [p t k s ʃ f] / _#`
(Wheeler 2005, *The Phonology of Catalan*, §5.3).

```python
from orthography2ipa import G2P
ca = G2P("ca")
ca.transcribe_word("fred")   # …t  (/d/# → [t])
ca.transcribe_word("sang")   # …k  (/ɡ/# → [k])
G2P("ca", apply_allophony=False).transcribe_word("fred")  # …d (broad)
```

### 2. Nasal place assimilation

`/n/` assimilates to the place of a following consonant: `[m]` before a
labial `/p b m f/`, `[ŋ]` before a velar `/k ɡ/` (Recasens 1993, *Fonètica i
fonologia*).

```python
ca.transcribe_word("banc")   # …ŋk  (/n/ → [ŋ] before /k/)
```

### 3. Intervocalic spirantization

Voiced stops lenite to approximants between vowels: `/b d ɡ/ → [β ð ɣ] / V_V`
(Wheeler 2005, §5.2). Encoded with the grapheme-class neighbour conditions
`preceded_by: "vowel"` + `followed_by: "vowel"`, so it fires only between
vowels and stays a stop elsewhere.

```python
ca.transcribe_word("cada")    # ˈkaðə  (/d/ → [ð])
ca.transcribe_word("pagar")   # pəˈɣaɾ (/ɡ/ → [ɣ])
ca.transcribe_word("poble")   # ˈpɔblə (/b/ before /l/ stays a stop)
```

### 4. Stress-conditioned unstressed vowel reduction

The Eastern (Central/Balearic) block reduces vowels **only in unstressed
syllables**: unstressed `/a e ɛ/ → [ə]` and `/o ɔ/ → [u]`; stressed vowels
keep full quality (Wheeler 2005, §2.3). This is the canonical "reduce in the
unstressed nucleus" case, so it is modelled with the **`nucleus_unstressed`
positional slot** (the stress-conditioned member of the `GraphemePosition`
vowel-class family) rather than a phoneme→surface rule — the reduced vowel is
selected pre-lexically, keyed on stress. Because the slot is stress-conditioned
it fires on the engine path only, exactly like a `stress`-conditioned
`allophone_rule`.

```python
ca.transcribe_word("gos")     # ˈɡɔs  (stressed o keeps [ɔ] — NOT reduced)
ca.transcribe_word("casa")    # ˈkazə (unstressed a → [ə])
ca.transcribe_word("dona")    # ˈdɔnə (stressed [ɔ], unstressed [ə])
```

The Western block (Valencian `ca-x-valencia`, Northwestern
`ca-x-occidental`) does **not** reduce — it keeps the full 7-vowel inventory
in atonic position (Recasens 1996; Veny 1982). Each Western variety overrides
the inherited `nucleus_unstressed` reduction with a full-quality vowel entry,
so `transcribe("casa", "ca-x-occidental")` is `kaza`, not `kazə`.

### Benchmark effect (honest)

Measured on the committed gold sets (PER, lower is better):

| Row | Gold | Before | After | Δ |
|---|---|---:|---:|---:|
| ca | 4catac (expert human) | 0.4170 | 0.4120 | **−0.0050** |
| ca-x-balear | 4catac | 0.3924 | 0.3884 | **−0.0040** |
| ca-x-occidental | 4catac | 0.5680 | 0.5633 | **−0.0047** |
| ca-x-valencia | 4catac | 0.3046 | 0.3005 | **−0.0041** |
| ca | styletts2_phonemes (espeak) | 0.4043 | 0.4083 | +0.0040 |

Both phenomena improve the **expert human** 4catac gold across all four
Catalan varieties — the gold that actually transcribes surface forms.
Devoicing alone is neutral-or-better everywhere. The nasal-assimilation
half slightly *regresses* the automatic **espeak-derived** styletts2 gold
(by +0.004, below the 0.005 regression-CI threshold): espeak Catalan does
not transcribe nasal place assimilation, so a broad/phonemic-leaning gold
cannot reward a correct narrow realisation. The phenomenon is nonetheless
linguistically correct (Recasens 1993) and rewarded by the higher-quality
gold. This is the expected "broad gold ≠ narrow surface" trade-off — it is
reported here rather than hidden.

Adding stress-conditioned reduction (§4) and intervocalic spirantization (§3),
and removing the Central reduction that Northwestern Catalan had wrongly
inherited, improves the expert-human 4catac gold across the varieties — most
dramatically Northwestern, which had been reducing vowels it should keep:

| Row | Gold | Before | After | Δ |
|---|---|---:|---:|---:|
| ca | 4catac (expert human) | 0.4120 | 0.4026 | **−0.0094** |
| ca-x-occidental | 4catac | 0.5633 | 0.4663 | **−0.0970** |
| ca-x-valencia | 4catac | 0.3005 | 0.2994 | **−0.0011** |
| ca-x-balear | 4catac | 0.3884 | 0.3893 | +0.0009 |
| ca | styletts2_phonemes (espeak) | 0.4083 | 0.4012 | **−0.0071** |

Northwestern Catalan (`ca-x-occidental`) drops by nearly 0.10: it no longer
schwa-reduces vowels the Western block keeps full. Central and Valencian
improve as stressed vowels stop being wrongly reduced. Balearic is flat
within noise (+0.0009, far below the 0.005 regression threshold): its
stressed vowels are now correct, but the automatic gold does not reward the
change measurably.

## Brazilian Portuguese — final vowel raising

Brazilian Portuguese (`pt-BR`) is the base spec for twelve regional dialect
specs; its `allophone_rules` model **final unstressed vowel raising**
(Barbosa & Albano 2004; Câmara Jr. 1970). Word-final /e o/ raise to the
close vowels [i]/[u]:

```python
from orthography2ipa import G2P
br = G2P("pt-BR")
br.transcribe_word("gato")    # ˈɡatu   ([ʊ] → [u] / _#)
br.transcribe_word("leite")   # ˈlejti  ([ɪ] → [i] / _#)
G2P("pt-BR", apply_allophony=False).transcribe_word("gato")  # ˈɡatʊ (broad)
```

```json
{
  "id": "BR_RAISE_FINAL_E",
  "phonemes": ["ɪ"],
  "surface": "i",
  "word_final": true
}
```

Two design points illustrate the inheritance-friendly way to write a base
rule:

1. **Target the reduced vowel, not the underlying phoneme.** The rule fires
   on the near-close [ɪ]/[ʊ] the pre-lexical map already selects
   word-finally, *not* on underlying /e o/. A conservative dialect that
   retains a final [e]/[o] therefore inherits the rule harmlessly — it
   simply never fires there — so the base can ship the rule without
   breaking the varieties that override the reduction.
2. **Leave a process pre-lexical when it is already positional.** BP /t d/
   affrication before ⟨i⟩ is handled by `positional_graphemes`; re-stating
   it as an allophone rule would double-apply. See
   [languages/pt-BR.md](languages/pt-BR.md) for the full breakdown,
   including the processes deliberately deferred to the dialect wave.

Effect on the committed gold (PER, lower is better):

| Row | Gold | Before | After | Δ |
|---|---|---:|---:|---:|
| pt-BR | wikipron (n=124) | 0.1901 | 0.1578 | **−0.0323** |
