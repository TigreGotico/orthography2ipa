# Romanian (`ro-RO`)

Standard Romanian (limba română standard). Eastern Romance, the only
Romance language east of the Adriatic. The bare tag `ro` resolves to
this reference variety in the registry.

## Orthographic depth and production threshold

**Shallow (phonemic) orthography, the ≤ 0.15 PER production threshold
applies** (see [quality tiers](../quality_tiers.md)). The post-1993
orthography is highly regular: the central vowels have dedicated letters
(⟨ă⟩ = /ə/, ⟨â/î⟩ = /ɨ/), and the palatalization of ⟨c⟩/⟨g⟩ before
front vowels follows the pan-Romance rule.

## Phonology (as encoded)

- 7 vowels /a e i o u ə ɨ/, the central vowels /ə/ and /ɨ/ are unique
  in Romance and are written unambiguously.
- No intervocalic lenition (Lat. *lupus* → *lup*, not \*lubo), Eastern
  Romance conservatism the spec inherits from its ancestry position.
- Diphthongs /e̯a/ ⟨ea⟩ and /o̯a/ ⟨oa⟩ are encoded as units. Final ⟨i⟩
  after consonants is the asyllabic palatal /ʲ/ (lupi /lupʲ/), encoded
  positionally.
- **Stress** is lexical, and standard spelling does not mark it, but it
  has a strong default (Chițoran 2002: 75–77, tabulated in Alexei &
  Ulfsbjorninn 2022: 2–5). A word that ends in a consonant or in a
  falling diphthong takes final stress (*bărbát*, *animál*, *gunói*,
  *biróu*), and any other word takes penultimate stress (*máre*,
  *feméie*, *mașínă*). The `stress` block states that default. Gold
  scoring is unaffected (PER strips stress marks).

## Benchmark (full gold set, no cap)

| dataset | row tag | provenance | n | PER |
|---|---|---|---:|---:|
| `wikipron` | `ro` | crowd-scraped | 8 977 | **0.0348** |
| `ipadict` | `ro-RO` | lexicon-derived | 72 375 | 0.0479 |

Two independent gate-eligible rows both sit far below the 0.15 shallow
threshold. `wikipron` (registered under the bare tag `ro`, resolved to
this spec by the registry and the guard test alike) is the primary.

## Known limitations

- The stress default misses the lexically marked words: penultimate
  stress on a consonant-final word (*záhăr*, *călúgăr*), antepenultimate
  stress on a vowel-final word (*pépene*, *cámeră*), and final stress on
  a vowel (*macará*, *curéa*). The spec lists none of them.
- Inflectional endings keep the stress of the stem (Franzén & Horne
  1997: 75), but the engine reads the whole word, so *lupul*, *trenuri*
  and *caselor* take the mark one syllable late. Homographs that differ
  only in stress (*cópii* "copies", *copíi* "children") are not
  resolved.
- The pre-1993 ⟨î⟩-everywhere spelling and the â/î alternation in older
  text are an orthographic-norm variant, out of scope for this spec
  (o2i does no input normalization by design).

## Sources

- Mallinson, G. *Romanian*. Croom Helm Descriptive Grammars.
- Alexei, S. & Ulfsbjorninn, S. (2022). Metrical exceptionality and stress
  shift in Romanian nouns and adjectives. *Isogloss* 8(1)/4, 1–29.
- Franzén, V. & Horne, M. (1997). Word stress in Romanian. *Lund
  University Working Papers* 46, 75–91.
- Deletant, D. *Teach Yourself Romanian*.
- Ladefoged, P. & Maddieson, I. *The Sounds of the World's Languages*.

---
[← Spanish](es-ES.md) · [Home](../index.md) · [French →](fr-FR.md)
