# Finnish — `fi`

Standard Finnish (yleiskieli). Uralic, Finnic branch. The orthography is
almost perfectly phonemic: each grapheme maps to one phoneme, and both
consonant and vowel **length are phonemic and written** (double letters).

## Orthographic depth and production threshold

**Shallow (phonemic) orthography — the ≤ 0.15 PER production threshold
applies** (see [quality tiers](../quality_tiers.md)). Finnish is a
textbook shallow orthography; the canonical irregularities are tiny and
enumerable (⟨ng⟩ = /ŋː/, ⟨nk⟩ = /ŋk/, loanword ⟨b d g f⟩).

## Phonology (as encoded)

- 8 vowels /i y e ø æ ɑ o u/ with full length contrast; 18 phonemic
  diphthongs (encoded in the spec's diphthong list so syllable counting
  and stress interact correctly).
- Vowel harmony (front/back) constrains suffixes but not
  grapheme→phoneme mapping, so the spec does not need to model it.
- Stress is fixed on the **first syllable** (`stress` block, initial).
- Boundary gemination (rajageminaatio, e.g. *tule tänne* → [tulet
  tænːe]) is a sandhi phenomenon that written text does not mark.

## Benchmark (full gold set, no cap)

| dataset | provenance | n | PER |
|---|---|---:|---:|
| `wikipron` | crowd-scraped | 168 808 | **0.0552** |
| `ipadict` | machine-generated (rule script) | 92 836 | 0.1002 |

The qualifying row is `wikipron` (crowd-scraped, gate-eligible; one of
the largest single gold sets in the scoreboard) — well below the 0.15
shallow threshold.

## Known limitations

- Boundary gemination is unwritten and therefore untranscribable from
  orthography alone; single-word gold is unaffected.
- Recent loanwords with foreign graphotactics (⟨š⟩, ⟨ž⟩, word-initial
  clusters) follow the spec's loan mappings, which are cited but less
  settled than the native inventory.

## Sources

- Abondolo, D. (ed.). *The Uralic Languages*. Routledge.
- Hakulinen, L. *The Structure and Development of the Finnish Language*.
- Ladefoged, P. & Maddieson, I. *The Sounds of the World's Languages*.
