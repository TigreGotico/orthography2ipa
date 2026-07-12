# Linguistic Accuracy Guide

This guide documents the methodology, standards, and conventions used to ensure linguistic accuracy in the package.

---

## Guiding Principles

1. **Primary sources over secondary sources.** Every phonological claim should trace back to a peer-reviewed article, grammar, or phonology monograph. Wikipedia, language-learning apps, and AI outputs are not acceptable sources.

2. **Standard varieties first.** Each language module should first accurately describe the standard or prestige variety, then add dialect variation. Dialects should clearly document how they deviate from the standard.

3. **Conservative over comprehensive.** When in doubt about whether an allophone belongs in the list, omit it. It is better to have a correct small list than a large inaccurate one.

4. **Cite your sources.** Every module docstring must include a bibliography. Every non-obvious mapping decision should have a comment.

5. **IPA accuracy.** Use the correct IPA symbols. Common errors to avoid are documented below.

---

## Grapheme Conventions

### What counts as a grapheme key?

A grapheme key represents a **single orthographic unit** in the language's writing system. The criteria for including a multi-character key:

- **Digraphs with lexicalized phonemic values**: `ch` /tʃ/ in Spanish, `lh` /ʎ/ in Portuguese, `sh` /ʃ/ in English. These are recognized as single units in the language's orthographic tradition.
- **Diphthong spellings**: Include when the language consistently treats a vowel sequence as a single unit for prosodic or phonological purposes. The ordering matters for beam search.
- **Trigraphs**: `sch` /ʃ/ in German, `tch` /tʃ/ in French. Include when the combination is orthographically stable.

Do **not** include:
- Letter combinations that are purely sequential (no special phonological status)
- Extremely rare or archaic spellings (unless documenting a historical variety)
- Spelling variants that are just positional (e.g., Spanish `c` before `e/i` — handle via comment, not separate key)

### IPA value ordering

Within a grapheme's IPA list, order by:
1. **Frequency**: The most common realisation first
2. **Canonicity**: If frequency is unclear, the "dictionary citation form" goes first
3. **Regularity**: Regular/predictable variants before irregular/lexicalized ones

This ordering matters because the beam search tokenizer treats the first value as the canonical path.

### When to use empty string `""`

An empty string `""` is the correct IPA value for a grapheme that is always silent:
```python
"h": [""],   # Spanish h — always silent
"w": [""],   # French w before a consonant in some words (rare)
```

Use `"∅"` (null symbol) in allophone maps when a phoneme can be deleted in certain contexts:
```python
"d": ["d", "ð", "∅"],  # Catalan final /d/ can delete in fast speech
```

---

## Allophone Conventions

### What belongs in the allophone map?

The allophone map records **phonetically distinct surface forms** of each underlying phoneme. Include:
- Contextually predictable allophones (place assimilation, lenition, aspiration)
- Well-documented stylistic/register variants
- Standard dialect variants if this is a standard variety covering several dialects

Do **not** include:
- Free variants with no phonological conditioning (list only the dominant one)
- Idiolectal or highly marginal variants
- Phenomena that are better described as separate phonemes

### Allophone list ordering

The first allophone in the list should be the **citation form** — the one you would hear in slow, careful speech or a dictionary recording. Contextual variants follow.

```python
# Good
"t": ["t", "tʰ", "ɾ", "ʔ", "t̚"]  # citation form first
# Bad
"t": ["tʰ", "t", "ɾ", "ʔ", "t̚"]  # aspirated first makes no sense as citation form
```

---

## Common IPA Errors to Avoid

### Consonants

| Wrong | Correct | Note |
|---|---|---|
| `g` | `ɡ` | The letter g ≠ IPA voiced velar stop. Use `ɡ` (U+0261) |
| `ʤ` | `dʒ` | Use the two-character sequence, not the ligature |
| `ʧ` | `tʃ` | Use the two-character sequence |
| `ɹ` | `r` | English approximant is `ɹ` (U+0279), not `r` (which is a trill) |

### Vowels

| Wrong | Correct | Note |
|---|---|---|
| `e:` | `eː` | Length mark is `ː` (U+02D0), not `:` |
| `ɐ̃` | `ɐ̃` | Nasalized schwa: ɐ (U+0250) + combining tilde |
| `ã` | `ã` | Nasalized a: a + combining tilde (U+0303) |

### Diacritics

| Symbol | Unicode | Meaning |
|---|---|---|
| `ʰ` | U+02B0 | Superscript h — aspiration |
| `ʷ` | U+02B7 | Superscript w — labialization |
| `ʲ` | U+02B2 | Superscript j — palatalization |
| `ː` | U+02D0 | Length mark |
| `̃` | U+0303 | Nasalization (combining) |
| `̪` | U+032A | Dental (combining) |
| `̈` | U+0308 | Centralized (combining) |
| `̥` | U+0325 | Voiceless (combining) |

---

## Language-Specific Accuracy Notes

### Spanish

**The /θ/-/s/ contrast (distinción vs. seseo)**

Castilian Spanish has /θ/ vs. /s/ (the `distinción`); all Latin American varieties and some Iberian dialects (Canarias, parts of Andalusia) have only /s/ (`seseo`). The `es` spec represents Castilian with `c: ["k", "θ"]` and `z: ["θ"]`. Latin American specs use `c: ["k", "s"]` and `z: ["s"]`.

**The /ʎ/-/ʝ/ contrast (lleísmo vs. yeísmo)**

Traditional Castilian distinguishes `ll` /ʎ/ from `y` /ʝ/ (`lleísmo`). The dominant modern pattern merges both to /ʝ/ (`yeísmo`). Rioplatense Spanish goes further, realising both as /ʃ/ or /ʒ/. The spec lists both values in order: `ll: ["ʎ", "ʝ"]` for Castilian, `ll: ["ʝ"]` for Latin American, `ll: ["ʃ", "ʒ"]` for Rioplatense.

**Lenition (spirantization)**

Voiced stops /b d ɡ/ have spirant allophones [β ð ɣ] in all non-initial, non-post-nasal positions. This is one of the most robust allophonic rules in Spanish and must be in every Spanish allophone map.

### Portuguese

**The /s/ ~ /ʃ/ coda contrast**

European Portuguese realises coda /s/ as [ʃ] before consonants or at end of phrase. Brazilian Portuguese generally retains [s]. This is one of the most salient EP vs. BP differences and must be reflected in the allophone maps.

**Unstressed vowel reduction in EP**

European Portuguese dramatically reduces unstressed /e/ and /o/ (often to schwa or deletion). Brazilian Portuguese does not. This is represented in the EP allophone maps and should be present in all EP dialect specs.

**Nasal vowels**

Portuguese has phonemic nasal vowels: /ã/, /ẽ/, /ĩ/, /õ/, /ũ/. These are spelled with a tilde (`ã`, `ã`, `õ`) or before `m`/`n` in a closed syllable. The grapheme map must include nasal spellings explicitly:
```python
"ã": ["ã"],
"an": ["ã"],  # before consonant
"am": ["ã"],  # before consonant
```

### French

**The /ɥ/ glide**

French has a labio-palatal approximant /ɥ/ (as in *nuit*, *lui*) which is distinct from /j/ and /w/. It appears with grapheme `u` before a vowel. This is a phoneme unique to French and must not be confused with /w/.

**Liaison and elision**

Liaison (word-final consonant pronounced before a following vowel) is a suprasegmental phenomenon and is not modeled in the grapheme map. The map should represent base forms.

**Nasal vowels**

French has four nasal vowels: /ɛ̃/ (as in *vin*), /ɑ̃/ (as in *vent*), /ɔ̃/ (as in *bon*), /œ̃/ (as in *brun*, merging with /ɛ̃/ for many speakers).

### German

**The Auslautverhärtung (final devoicing)**

German voicces final obstruents are devoiced: `b, d, g, v, z` → `[p, t, k, f, s]` word-finally. This is an allophonic rule, not a phonemic contrast. The grapheme map should map `b → /b/` (underlying), with the allophone map recording `"b": ["b", "p"]`.

**sch vs. s + ch**

German `sch` is a distinct grapheme key `/ʃ/`, separate from `s` + `ch`. Make sure `sch` appears in the grapheme table before both `s` and `ch` so maximal munch correctly handles words like `schön`.

### English

**Rhoticity**

Most descriptions of English phonology use RP (Received Pronunciation, non-rhotic) or General American (rhotic). The package's `en` spec covers General American. Rhotic `/r/` should be `ɹ` (U+0279), not `r` (the trill).

**The TRAP-BATH split**

RP English has lengthened `[ɑː]` for words like *bath*, *dance*, *path* (the BATH set), while General American uses the same `/æ/` for both TRAP and BATH words. The `en` spec uses `a: ["æ", "eɪ", "ɑː", "ə"]` to cover all major realisations.

---

## Sources by Language Family

### Romance
- Hualde, J.I. (2005). *The Sounds of Spanish*. Cambridge.
- RAE (2011). *Nueva gramática: Fonética y fonología*. Espasa.
- Teyssier, P. (1980). *Histoire de la langue portugaise*. PUF.
- Jensen, F. (1994). *Occitan Historical Morphology*.
- Wheeler, M. (2005). *The Phonology of Catalan*. Oxford.

### Germanic
- Roach, P. (2009). *English Phonetics and Phonology* (4th ed.). Cambridge.
- Wiese, R. (1996). *The Phonology of German*. Oxford.

### Slavic
- Comrie, B. et al. (1996). *The Russian Language in the Twentieth Century*. Oxford.

### Historical
- Sihler, A. (1995). *New Comparative Grammar of Greek and Latin*. Oxford.
- Fortson, B. (2010). *Indo-European Language and Culture* (2nd ed.). Wiley-Blackwell.
- Gorrochategui, J. (1984). *Onomástica indígena de Aquitania*. Univ. País Vasco.

---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Bibliography](bibliography.md) · [Quality tiers](quality_tiers.md) · [Benchmarks](benchmarks.md)*
