# Adding a Language

This guide walks through the complete process of contributing a new language mapping to the package.

---

## Before You Start

1. **Choose your primary source.** Every mapping must be grounded in published phonological descriptions. Linguistics textbooks, peer-reviewed journal articles, and established reference grammars are all acceptable. Wikipedia is not acceptable as a primary source (though it can help you find real sources).

2. **Determine the BCP-47 code.** Use the IANA Language Subtag Registry or RFC 5646. For dialects, use the `x-` private extension convention already established in the package (e.g., `pt-BR-x-rj` for Rio de Janeiro Portuguese).

3. **Decide where the language fits.** Is it:
   - A new standard variety in a new module?
   - A dialect that should live in an existing `_dialects.py` file?
   - A historical/reconstructed language in one of the historical bundles?

---

## Step-by-Step: Creating a New Module

### 1. Create the module file

Create `orthography2ipa/languages/xx.py` (replace `xx` with your code).

The module **must** export:
```python
SPECS: Dict[str, LanguageSpec]
```

### 2. Write the grapheme table

Document each grapheme key with a comment explaining the phonological context:

```python
"""Catalan (ca) — grapheme→IPA and allophone mappings.

Sources:
- Wheeler, M. (2005). The Phonology of Catalan. Oxford University Press.
- Recasens, D. (1993). Fonètica i fonologia. Enciclopèdia Catalana.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

GRAPHEMES_CA = {
    # ── Vowels ──────────────────────────────────────────────────────────────
    "a": ["a", "ə"],      # /a/ stressed; /ə/ unstressed (central dialect)
    "e": ["ɛ", "e", "ə"], # /ɛ/ open; /e/ closed; /ə/ unstressed
    "i": ["i"],
    "o": ["ɔ", "o", "u"], # /ɔ/ open; /o/ closed; /u/ unstressed (Balear)
    "u": ["u"],

    # ── Consonants ──────────────────────────────────────────────────────────
    "b": ["b"],
    "c": ["k", "s"],      # /k/ before a,o,u; /s/ before e,i
    "d": ["d"],
    ...

    # ── Digraphs ─────────────────────────────────────────────────────────────
    "l·l": ["lː"],        # geminate lateral (full stop/raised dot)
    "ny":  ["ɲ"],
    "tl":  ["tl", "l"],   # /tl/ in Valencian; /l/ in central
    "tz":  ["dz"],
    ...
}
```

### 3. Write the allophone map

For each **underlying phoneme** (IPA key), list all attested surface forms:

```python
ALLOPHONES_CA = {
    # Obstruent lenition (similar to Spanish but with different details)
    "b": ["b", "β"],     # [b] after pause/nasal; [β] elsewhere
    "d": ["d", "ð", "∅"], # [d] → [ð] → ∅ in coda (mol·ta dialects)
    "ɡ": ["ɡ", "ɣ"],

    # Distinctive Catalan allophones
    "l": ["l", "lː"],    # single vs. geminate
    "n": ["n", "m", "ŋ", "ɱ"],  # place assimilation
    "s": ["s", "z"],     # [z] intervocalic

    # Vowels — unstressed reduction
    "a": ["a", "ə"],     # /a/ → [ə] unstressed (central/eastern dialects)
    "e": ["e", "ɛ", "ə"],
    "o": ["o", "ɔ", "u"],
    ...
}
```

### 4. Define the `SPECS` dict

```python
SPECS = {
    "ca": LanguageSpec(
        code="ca",
        name="Catalan",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_CA,
        allophones=ALLOPHONES_CA,
        parent="la-x-gallia",
        ancestors=(
            Ancestor("la-x-gallia", AncestorRole.PARENT, 0.82,
                     "Descent from Gallo-Latin; Catalan part of Gallo-Romance"),
            Ancestor("xib", AncestorRole.SUBSTRATE, 0.06,
                     "Iberian substrate: some place names and lexical items"),
            Ancestor("xaq", AncestorRole.SUBSTRATE, 0.04,
                     "Basque substrate influence in western areas"),
            Ancestor("ar", AncestorRole.ADSTRATE, 0.05,
                     "Arabic adstrate: ~300 loanwords, some phonological influence"),
        ),
        notes=(
            "Central Catalan (Barcelona standard). Unstressed vowel reduction "
            "is a key feature distinguishing Eastern from Western dialects."
        ),
    ),
}
```

### 5. Register the language

Add entries to `_LANG_MODULES` in `registry.py`:

```python
_LANG_MODULES: Dict[str, str] = {
    ...
    "ca":              "orthography2ipa.languages.ca",
    # If you also added dialects in the same file:
    "ca-x-valencia":   "orthography2ipa.languages.ca",
    ...
}
```

### 6. Verify the spec loads

```python
python -c "import orthography2ipa; print(orthography2ipa.get('ca'))"
```

---

## Adding a Dialect

Dialects should extend the parent's mappings rather than duplicating them. Use Python dict unpacking:

```python
"""Valencian (ca-x-valencia) — Catalan dialect module."""
from orthography2ipa.languages.ca import GRAPHEMES_CA, ALLOPHONES_CA
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

# Valencian differs in: no unstressed vowel reduction, /tl/ preserved, etc.
GRAPHEMES_VA = {
    **GRAPHEMES_CA,
    "a": ["a"],            # no unstressed reduction to [ə]
    "e": ["ɛ", "e"],       # no [ə]
    "o": ["ɔ", "o"],       # no [u] for unstressed
    "tl": ["tl"],          # Valencian preserves /tl/ consonant cluster
    "v":  ["v"],           # Valencian has /v/ ~ /b/ distinction (unlike central)
}

ALLOPHONES_VA = {
    **ALLOPHONES_CA,
    "v": ["v", "β"],       # /v/ with bilabial allophone, not merged with /b/
}

SPECS = {
    **SPECS,  # include parent specs if in same file
    "ca-x-valencia": LanguageSpec(
        code="ca-x-valencia",
        name="Valencian",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_VA,
        allophones=ALLOPHONES_VA,
        parent="ca",
        notes=(
            "Valencian: no unstressed vowel reduction; /v/~/b/ distinction "
            "maintained in most varieties; /tl/ cluster preserved."
        ),
    ),
}
```

---

## Checklist

Before submitting a new language:

- [ ] Module docstring includes all sources with full citations
- [ ] Every grapheme key has a comment explaining phonological context
- [ ] Every allophone list is in order (most common/canonical first)
- [ ] `LanguageSpec` has complete `name`, `family`, `script`
- [ ] Ancestry `ancestors` tuple is populated (not just `parent=`)
- [ ] Ancestry weights are documented in `notes` fields
- [ ] Entry added to `_LANG_MODULES` in `registry.py`
- [ ] `import orthography2ipa; orthography2ipa.get("xx")` runs without error
- [ ] Dialect modules use `**PARENT_GRAPHEMES` to avoid duplication

---

## Style Conventions

### Module structure

```python
"""Language Name (code) — grapheme→IPA and allophone mappings.

Sources:
- Author, A. (year). *Title*. Publisher.
- Author, B. (year). "Article title." Journal Name, vol(issue), pp.
"""
from orthography2ipa.types import Ancestor, AncestorRole, LanguageSpec

P   = AncestorRole.PARENT
SUB = AncestorRole.SUBSTRATE
SUP = AncestorRole.SUPERSTRATE
AD  = AncestorRole.ADSTRATE

# ═══ Graphemes ═══════════════════════════════════════════════════════════════

GRAPHEMES_XX = {
    # ── Vowels ──────────────────────────────────────────────────────────────
    ...
    # ── Consonants ──────────────────────────────────────────────────────────
    ...
    # ── Digraphs ─────────────────────────────────────────────────────────────
    ...
}

# ═══ Allophones ═══════════════════════════════════════════════════════════════

ALLOPHONES_XX = {
    ...
}

# ═══ Specs ════════════════════════════════════════════════════════════════════

SPECS = {
    "xx": LanguageSpec(
        ...
    ),
}
```

### Comment format for graphemes

```python
"grapheme": ["ipa"],  # pronunciation note; context where applicable
```

Examples:
```python
"c":  ["k", "θ"],    # /k/ before a,o,u; /θ/ before e,i (Castilian)
"h":  [""],           # always silent
"rr": ["r"],          # alveolar trill (contrast with single /r/ tap)
```

### IPA ordering

Always list:
1. The **most common / default** realisation first
2. Rarer or more context-restricted variants after

For allophones, list:
1. The **citation form** (what you'd find in a dictionary) first
2. Contextual variants in order of frequency/regularity

---

## Testing Your Contribution

Run these checks manually until a formal test suite exists:

```python
import orthography2ipa
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.distance import phonological_distance

spec = orthography2ipa.get("xx")

# 1. Basic access
print(spec.name, spec.family, spec.script)
print(f"  {len(spec.graphemes)} graphemes, {len(spec.allophones)} allophones")

# 2. Tokenization
tok = PhonetokTokenizer(spec)
for word in ["some", "test", "words"]:
    paths = tok.ipa_beam(word, beam_width=3)
    print(f"  {word} → {paths[0].ipa}")

# 3. Distance (compare to genetic relatives)
parent = orthography2ipa.get(spec.primary_parent)
d = phonological_distance(spec, parent)
print(f"  distance to {parent.code}: {d.combined:.3f}")
# Expect: 0.1–0.4 for dialect→standard; 0.2–0.5 for language→parent

# 4. Ancestry
for anc in spec.get_ancestors():
    print(f"  {anc}")
```
