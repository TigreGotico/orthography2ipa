# Spanish (Castilian) — `es-ES`

Standard Peninsular Castilian Spanish per the Real Academia Española
(RAE). The bare tag `es` resolves to this reference variety in the
registry (`_BARE_DEFAULTS`); Latin-American varieties are separate specs
under `es-419` and country tags.

## Orthographic depth and production threshold

**Shallow (phonemic) orthography — the ≤ 0.15 PER production threshold
applies** (see [quality tiers](../quality_tiers.md)). Spanish spelling
is regular given a small closed set of contextual rules (⟨c⟩/⟨g⟩ before
front vowels, ⟨gu⟩/⟨qu⟩ digraphs, silent ⟨h⟩, ⟨y⟩ as consonant/vowel).

## Phonology (as encoded)

- 5 vowels /a e i o u/, no reduction; the classic Castilian contrasts
  **/θ/ ⟨c,z⟩ vs /s/** (distinción) and **/ʎ/ vs /ʝ/** where the spec
  encodes the modern yeísta merger per RAE's own descriptive stance —
  variant transcriptions are handled by the gold's multi-reference
  scoring.
- Spirantization of /b d g/ → [β ð ɣ] in continuant contexts is encoded
  through the spec's positional grapheme contexts (⟨b⟩/⟨d⟩/⟨g⟩ carry
  position-conditioned readings) — the single biggest PER lever for
  Spanish.
- Stress: the written-accent system plus the vowel/n/s-final penult
  default is fully predictable from orthography and encoded in the
  `stress` block.

## Benchmark (full gold set, no cap)

| dataset | row tag | provenance | n | PER |
|---|---|---|---:|---:|
| `wikipron` | `es` | crowd-scraped | 131 506 | **0.0845** |
| `ipadict` | `es-ES` | machine-generated (rule script) | 595 896 | 0.0537 |
| `ipa_childes` | `es-ES` | epitran-derived | 13 155 | 0.0945 |

The qualifying row is `wikipron` (crowd-scraped, gate-eligible; the row
is registered under the bare tag `es`, which the registry resolves to
this spec — the guard test resolves tags the same way). The
`ipa_childes` row is competitor-derived and can neither qualify nor
block; `ipadict` is rule-script agreement. All sit below the 0.15
shallow threshold.

## Known limitations

- Dialect-variable phenomena (seseo, yeísmo degree, coda-/s/ weakening)
  belong to the variant specs, not `es-ES`; gold entries transcribed by
  editors from those regions inflate the residual PER slightly.
- ⟨x⟩ in Mexican toponyms (México, Oaxaca) is lexical, handled via
  `word_exceptions`.

## Sources

- Hualde, J. I. *The Sounds of Spanish*. Cambridge University Press.
- Penny, R. *A History of the Spanish Language*. Cambridge University Press.
- Harris, J. *Spanish Phonology*. MIT Press.
