# Romanian — `ro-RO`

Standard Romanian (limba română standard). Eastern Romance — the only
Romance language east of the Adriatic. The bare tag `ro` resolves to
this reference variety in the registry.

## Orthographic depth and production threshold

**Shallow (phonemic) orthography — the ≤ 0.15 PER production threshold
applies** (see [quality tiers](../quality_tiers.md)). The post-1993
orthography is highly regular: the central vowels have dedicated letters
(⟨ă⟩ = /ə/, ⟨â/î⟩ = /ɨ/), and the palatalization of ⟨c⟩/⟨g⟩ before
front vowels follows the pan-Romance rule.

## Phonology (as encoded)

- 7 vowels /a e i o u ə ɨ/ — the central vowels /ə/ and /ɨ/ are unique
  in Romance and are written unambiguously.
- No intervocalic lenition (Lat. *lupus* → *lup*, not \*lubo) — Eastern
  Romance conservatism the spec inherits from its ancestry position.
- Diphthongs /e̯a/ ⟨ea⟩ and /o̯a/ ⟨oa⟩ are encoded as units; final ⟨i⟩
  after consonants is the asyllabic palatal /ʲ/ (lupi /lupʲ/), encoded
  positionally.
- **Stress is lexically unpredictable from orthography** (compare
  *cópii* "copies" vs *copíi* "children") and standard spelling does not
  mark it: the spec carries no `stress` block, with the exemption
  documented in its `notes` per the research-tier rule. Gold scoring is
  unaffected (PER strips stress marks).

## Benchmark (full gold set, no cap)

| dataset | row tag | provenance | n | PER |
|---|---|---|---:|---:|
| `wikipron` | `ro` | crowd-scraped | 8 977 | **0.0348** |
| `ipadict` | `ro-RO` | lexicon-derived | 72 375 | 0.0479 |

Two independent gate-eligible rows both sit far below the 0.15 shallow
threshold; `wikipron` (registered under the bare tag `ro`, resolved to
this spec by the registry and the guard test alike) is the primary.

## Known limitations

- Stress is not transcribed (see above) — WER-style comparisons against
  stress-marked competitors must strip stress to be fair.
- The pre-1993 ⟨î⟩-everywhere spelling and the â/î alternation in older
  text are an orthographic-norm variant, out of scope for this spec
  (o2i does no input normalization by design).

## Sources

- Mallinson, G. *Romanian*. Croom Helm Descriptive Grammars.
- Deletant, D. *Teach Yourself Romanian*.
- Ladefoged, P. & Maddieson, I. *The Sounds of the World's Languages*.
