# Brazilian Portuguese (pt-BR): Phonology Reference

**Code**: `pt-BR` | **Family**: Indo-European > Romance > Ibero-Romance | **Script**: Latin (alphabet)
**Quality tier**: research | **Sources**: Barbosa & Albano (2004, JIPA),
Câmara Jr. (1970), Mateus & d'Andrade (2000), Callou & Leite (2001)

`pt-BR` is the base spec for twelve regional Brazilian dialect specs
(`pt-BR-x-sp`, `-rj`, `-caipira`, `-mg`, `-sul`, `-recife`, …), which
inherit its maps via `graphemes_base` and refine them by delta. See
[romance.md](romance.md) for the pt-PT ↔ pt-BR comparison.

## The two maps for BP

The library models pronunciation as two maps (see
[../allophony.md](../allophony.md)): the **pre-lexical** map
(orthography → phoneme, in `positional_graphemes`) and the **post-lexical**
map (phoneme → surface allophone, in `allophone_rules`).

### Pre-lexical (positional_graphemes)

| Process | Rule | Example |
|:---|:---|:---|
| /t d/ affrication | ⟨t d⟩ → [t͡ʃ d͡ʒ] before ⟨i⟩ | `tio` [ˈt͡ʃiu], `dia` [ˈd͡ʒiɐ] |
| Coda /l/ vocalisation | ⟨l⟩ → [w] in coda / word-final | `sol` [ˈsɔw], `sal` [ˈsaw] |
| Coda /s/ | stays alveolar [s]/[z] (no chiado) | `mesmo` [ˈmezmu] |
| Coda ⟨m/n⟩ nasalisation | ⟨m/n⟩ → [̃] (U+0303) in coda / word-final | `campo` [ˈkɐ̃pu], `sim` [ˈsĩ], `mundo` [ˈmũdu] |
| Unstressed /a/ | → [ɐ] final/posttonic | `capa` [ˈkapɐ] |

The chiado (coda /s/ → [ʃ]) is a **carioca/RJ dialect delta**, not general
BP, so the base keeps alveolar [s]/[z].

### Post-lexical allophony (allophone_rules)

Two rules make the second map live for BP:

| id | Process | Rule | Example |
|:---|:---|:---|:---|
| `PT_NASAL_A_RAISE` | Nasal vowel quality | [a] → [ɐ] / _[̃] | `campo` [ˈkɐ̃pu] |
| `PT_NASAL_E_RAISE` | Nasal vowel quality | [ɛ] → [e] / _[̃] | `tempo` [ˈtẽpu] |
| `PT_NASAL_O_RAISE` | Nasal vowel quality | [ɔ] → [o] / _[̃] | `bom` [ˈbõ] |
| `BR_RAISE_FINAL_E` | Final vowel raising | [ɪ] → [i] / _# | `leite` [ˈlejti] |
| `BR_RAISE_FINAL_O` | Final vowel raising | [ʊ] → [u] / _# | `gato` [ˈɡatu] |

**Coda vowel nasalisation.** BP retains the general-Portuguese process by which
a vowel before a **coda** ⟨m/n⟩ (word-finally or before a consonant) nasalises,
the nasal consonant being absorbed (Mateus & d'Andrade 2000: ch. 2; Barbosa &
Albano 2004). The nasalisation itself is pre-lexical, the `positional_graphemes`
`m`/`n` coda positions map to a **U+0303 combining tilde**, deleting the nasal and
nasalising the preceding vowel, while the three `PT_NASAL_*_RAISE` rules supply
only the vowel *quality* (the **oral** base of the nasal vowel, so the tilde is
never doubled), conditioned on a following tilde. An **onset** (intervocalic)
⟨m/n⟩ leaves the vowel oral (`cama` [ˈkamɐ], `ano` [ˈanu]). ⟨nh⟩ tokenises first
so `banho` [ˈbaɲu] is untouched. The nasal diphthongs ⟨ão ãe õe⟩ are whole
graphemes and unaffected. The high vowels ⟨i u⟩ need no quality rule ([ĩ ũ] share
the oral bases [i u]): `sim` [ˈsĩ], `mundo` [ˈmũdu]. Unlike EP, BP does **not**
reduce unstressed ⟨o⟩ to [u], so its ⟨o⟩ before a coda nasal is already [o]
([õ] with the tilde) and the EP-only `PT_NASAL_O_UNRED` rule is not needed here
(`contar` [kõˈtaɾ], `bondade` [bõˈdadi]).

A shared engine guard (`_expand_beam`) emits the nasalisation tilde **only when
it attaches to a vowel or a nasal-diphthong glide**, falling back to the oral
consonant otherwise. This keeps BP output valid IPA where the pre-existing
⟨gu⟩→[ɡ] vowel-drop strands a consonant in the coda-nasal slot (`algum`
[ˈawɡm], `segundo` [ˈseɡndu], no stray tilde on [ɡ]) and prevents a doubled
tilde on ⟨nn⟩ loans (`inn`, `Finn`).

Word-final unstressed /e o/ raise to the close vowels [i]/[u] (Barbosa &
Albano 2004: 229. Câmara Jr. 1970). The positional map selects the
near-close [ɪ]/[ʊ] word-finally. These rules realise the standard BP close
surface form. They target the **reduced** [ɪ]/[ʊ] only, never the
underlying /e o/, so a conservative dialect that retains a final [e]/[o]
inherits the rules harmlessly (they simply do not fire).

```python
from orthography2ipa import G2P
G2P("pt-BR").transcribe_word("gato")   # ˈɡatu
G2P("pt-BR").transcribe_word("leite")  # ˈlejti
G2P("pt-BR", apply_allophony=False).transcribe_word("gato")  # ˈɡatʊ (broad)
```

## What the base deliberately does NOT model

Honest limits, each a documented decision rather than an omission:

- **Strong pretonic reduction**: BP reduction is markedly weaker than EP.
  BP keeps distinct pretonic /e o/, so only the final position raises.
- **/t d/ affrication before a raised final ⟨e⟩** (e.g. `dente` →
  [ˈdẽt͡ʃi]), expressible as a phoneme-conditioned allophone rule, but it
  would silently re-impose affrication on the non-palatalising nordeste
  varieties (recife/norte/ce) that inherit the base. It is deferred to the
  dialect-delta wave, where those varieties opt out by rule id. Grapheme-⟨i⟩
  affrication (the common case) is already handled pre-lexically.
- **Coda /r/ → [h~x]**: the general BP weak fricative is highly variable,
  and the broad wikipron pt-BR gold transcribes coda /r/ as [ʁ], so
  shipping [h~x] in the base regresses the only pt-BR gold. Held as a
  dialect delta.

## Sibilants, digraphs, and ⟨w⟩

Brazilian Portuguese has one sibilant pair, the plain alveolar /s z/
(Barbosa & Albano 2004: 228, consonant chart, Alveolar column: `saca`
[ˈsakɐ] vs `zaca` [ˈzakɐ]). The apico-alveolar [s̺ z̺] is a different
system: it belongs to Galician-Portuguese, which `roa-x-galaicopt` and
`pt-PT-x-medieval` model with four sibilants, and to the northern European
dialects that still keep it (`pt-PT-x-minho`, `pt-PT-x-trasosmontes` and
siblings, each of which declares it for itself).

That value used to reach `pt-BR` by inheritance. The base declared ⟨s c ç
z⟩ but neither the ⟨ss⟩ digraph nor positional ⟨c⟩ before ⟨e i⟩, so
galaicopt's ⟨ss⟩ → [s̺] and medieval's ⟨ce ci⟩ → [s̺] fell straight through
and `isso` came out [ˈis̺u], `cidade` [s̺iˈdad͡ʒi]. All twelve `pt-BR-x-*`
dialects already declared the modern value; only their parent did not.
Both keys are now declared in the base.

⟨ss⟩ and ⟨rr⟩ are digraphs, not geminates. Portuguese has no contrastive
consonant length: ⟨ss⟩ spells /s/ in the intervocalic position where a
single ⟨s⟩ would be /z/, and ⟨rr⟩ spells the strong rhotic, which contrasts
with the tap (`carro` [ˈkaʁu] vs `caro` [ˈkaɾu], Barbosa & Albano 2004:
228). Neither yields a doubled segment, so there is nothing for a geminate
collapse pass to remove and `collapse_geminates` stays unset. The only
doubled segments the spec emits come from unassimilated loans and names
(`watts`, `reddit`), where the gold sets double them too.

⟨w⟩ is rare but not silent: [w] in English loans, [v] in Germanic names.
With no grapheme entry the letter was deleted, which cost the whole
syllable — `web` → [ˈeb], `show` → [ˈsu], `wagner` → [aɡˈneɾ]. It now maps
to [w v], mirroring `pt-PT`.

## Reading the vox_communis row

The `vox_communis` row is the worst Portuguese row on the board and it says
nothing about this spec. Its phone tier is Epitran output over the
region-untagged Common Voice `pt` locale, and that output is European
Portuguese. Measured over the whole file with
`scripts/fold_pt_br_notation.py`, not one of the features that define
Brazilian Portuguese appears in it:

| feature | attested in the gold |
|:---|---:|
| final ⟨-l⟩ vocalised to [w] | 0 / 948 |
| ⟨t⟩ affricated before /i/ | 0 / 2378 |
| ⟨d⟩ affricated before /i/ | 5 / 1637 |
| final unstressed ⟨-e⟩ raised to [i] | 0 / 2956 |
| final unstressed ⟨-o⟩ raised to [u] | 0 / 7429 |
| final ⟨-s⟩ alveolar rather than the EP [ʃ] | 0 / 7429 |

The gold is also wrong about Portuguese of any variety. Its inventory has
34 symbols and contains neither ⟨ʎ⟩ nor ⟨ɲ⟩, so the 513 ⟨lh⟩ words and 717
⟨nh⟩ words all lose their digraph (`gatilho` → [ɡɐtilo], `tinha` →
[tinɐ]). It applies the European coda-sibilant rule inside the ⟨ss⟩
digraph, writing [ʃs] on 981 of 995 ⟨ss⟩ words (`isso` → [iʃso]).

Folding those conventions out of both sides one at a time takes the row
from 0.3886 to 0.2534 without touching the spec. The row is classified
`epitran-derived` and cannot gate anything, which is the correct handling;
read it as a measurement of Epitran's European map, never as evidence about
the Brazilian spec.

## Benchmark effect (honest)

Measured on the committed gold set (PER, lower is better):

| Row | Gold | Before | After | Δ |
|:---|:---|---:|---:|---:|
| pt-BR | wikipron (n=124) | 0.1535 | 0.1083 | **−0.0452** |
| pt-BR | portuguese_lexicon (n=300) | 0.2458 | 0.1877 | **−0.0581** |
| pt-BR | portuguese_phonetic_lexicon (n=300) | 0.2754 | 0.2226 | **−0.0528** |

Coda vowel nasalisation is the dominant driver of these gains, it applies to a
large fraction of BP words and every measured `pt-BR` gold rewards absorbing the
coda nasal into the nasal vowel. Final-vowel raising to [i]/[u] both matches the
gold's transcription and is the cited BP realisation. The `pt` styletts2 row
resolves to `pt-PT`, a different spec (its small +0.005 movement is discussed in
the [pt-PT](pt-PT.md) reference).

---

## Production tier: orthographic depth, threshold, and benchmark

**Deep orthography, the ≤ 0.25 PER production threshold applies**
([quality tiers](../quality_tiers.md)): Portuguese spelling is
morphophonemic with substantial contextual vowel quality (pretonic
reduction, nasalization) that the page's rules encode but gold sets
disagree on at the margins.

| dataset | provenance | n | PER |
|---|---|---:|---:|
| `wikipron` | crowd-scraped (gate-eligible) | 57 814 | **0.0662** |
| `portuguese_phonetic_lexicon` | crowd-scraped | 53 346 | 0.2199 |
| `ipadict` | machine-generated (cannot certify) | 95 933 | 0.2436 |

The qualifying row is `wikipron`, which in fact clears even the shallow
0.15 bar. The Portal lexicon row reflects that source's semi-automated,
region-coded transcription conventions (see benchmarks.md) rather than
spec drift, the divergence is documented, not hidden.

---
[← Italian](it-IT.md) · [Home](../index.md) · [Caipira Portuguese →](pt-BR-x-caipira.md)
