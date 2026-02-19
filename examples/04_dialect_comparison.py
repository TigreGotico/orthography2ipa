"""
04_dialect_comparison.py — Comparing dialects within language families.

Demonstrates:
- Loading and comparing dialect specs
- How dialects inherit from parent varieties
- Phonological differences between dialects
- Distance metrics between dialects
"""

import orthography2ipa
from orthography2ipa.distance import phonological_distance, grapheme_divergence, inventory_distance
from orthography2ipa.phonetok import PhonetokTokenizer


# ── Helper ────────────────────────────────────────────────────────────────

def compare_grapheme(codes, grapheme):
    """Show how multiple dialects map the same grapheme to IPA."""
    print(f"\n  Grapheme ⟨{grapheme}⟩ across dialects:")
    for code in codes:
        try:
            spec = orthography2ipa.get(code)
            ipa_list = spec.graphemes.get(grapheme, [])
            if ipa_list:
                print(f"    {code:25s}  {ipa_list}")
            else:
                print(f"    {code:25s}  (not in grapheme table)")
        except KeyError:
            print(f"    {code:25s}  (not found)")


def compare_allophone(codes, phoneme):
    """Show how multiple dialects realize the same phoneme."""
    print(f"\n  Phoneme /{phoneme}/ allophones across dialects:")
    for code in codes:
        try:
            spec = orthography2ipa.get(code)
            allo_list = spec.allophones.get(phoneme, [])
            if allo_list:
                print(f"    {code:25s}  {allo_list}")
        except KeyError:
            pass


def dialect_distance_table(codes, label):
    """Print pairwise distances for a set of dialects."""
    specs = []
    labels = []
    for code in codes:
        try:
            spec = orthography2ipa.get(code)
            specs.append(spec)
            labels.append(code)
        except KeyError:
            pass
    if len(specs) < 2:
        return

    print(f"\n  Pairwise combined distance — {label}:")
    w = max(len(l) for l in labels) + 2
    header = " " * (w + 4) + "".join(f"{l:>{w}}" for l in labels)
    print(header)
    for i, (la, spec_a) in enumerate(zip(labels, specs)):
        row = ""
        for j, spec_b in enumerate(specs):
            if i == j:
                row += f"{'0.000':>{w}}"
            else:
                d = phonological_distance(spec_a, spec_b)
                row += f"{d.combined:{w}.3f}"
        print(f"    {la:{w}}{row}")


# ═══ 1. Spanish varieties ════════════════════════════════════════════════

print("=" * 65)
print("1. SPANISH VARIETIES")
print("=" * 65)

es_codes = ["es", "es-419", "es-AR", "es-MX", "es-CU",
            "es-ES-x-andalusia-w", "es-ES-x-canarias"]

# The /θ/-/s/ distinction (distinción vs. seseo)
compare_grapheme(es_codes, "c")
compare_grapheme(es_codes, "z")

# The /ʎ/-/ʝ/ distinction (lleísmo vs. yeísmo)
compare_grapheme(es_codes, "ll")
compare_grapheme(es_codes, "y")

# Jota (j) — velar vs. uvular in different dialects
compare_grapheme(es_codes, "j")

# Allophone for /s/ — aspiration patterns
compare_allophone(es_codes, "s")

dialect_distance_table(es_codes[:6], "Spanish varieties")


# ═══ 2. Portuguese varieties ════════════════════════════════════════════

print("\n" + "=" * 65)
print("2. PORTUGUESE VARIETIES")
print("=" * 65)

pt_codes = [
    "pt",           # European standard
    "pt-BR",        # Brazilian standard
    "pt-PT-x-lisbon",
    "pt-PT-x-porto",
    "pt-BR-x-sp",
    "pt-BR-x-rj",
    "pt-BR-x-caipira",
    "mwl",          # Mirandese (closely related)
]

# The sibilant contrast: /ʃ/ in EP coda vs. /s/ in BP
compare_allophone(pt_codes[:4], "s")

# Nasal vowel ⟨ã⟩
compare_grapheme(pt_codes[:4], "ã")

# Ambiguous ⟨x⟩
compare_grapheme(pt_codes[:4], "x")

dialect_distance_table(pt_codes[:6], "Portuguese varieties")


# ═══ 3. Catalan dialects ════════════════════════════════════════════════

print("\n" + "=" * 65)
print("3. CATALAN DIALECTS")
print("=" * 65)

ca_codes = ["ca", "ca-x-valencia", "ca-x-balear", "ca-x-nord", "ca-x-occidental"]

# Unstressed vowel reduction: central has [ə], Valencian doesn't
compare_grapheme(ca_codes, "a")
compare_grapheme(ca_codes, "e")

# /v/ vs /b/ merger: Valencian maintains /v/, most other dialects merge
compare_grapheme(ca_codes, "v")

dialect_distance_table(ca_codes, "Catalan dialects")


# ═══ 4. Basque dialects ════════════════════════════════════════════════

print("\n" + "=" * 65)
print("4. BASQUE DIALECTS")
print("=" * 65)

eu_codes = [
    "eu",
    "eu-x-bizkaiera",
    "eu-x-gipuzkera",
    "eu-x-nafarra-garaia",
    "eu-x-zuberera",
    "eu-x-nafarra-beherea",
]

# Basque is a language isolate — interesting to see its internal diversity
compare_grapheme(eu_codes, "r")
compare_grapheme(eu_codes, "j")

dialect_distance_table(eu_codes, "Basque dialects")


# ═══ 5. Cross-family comparison ═════════════════════════════════════════

print("\n" + "=" * 65)
print("5. CROSS-FAMILY COMPARISON")
print("=" * 65)

# How similar are the most similar dialects vs. unrelated languages?
cross_codes = ["es", "pt-BR", "pt", "it", "fr", "ca", "en", "de", "ru", "ar"]
cross_labels = ["es", "pt-BR", "pt", "it", "fr", "ca", "en", "de", "ru", "ar"]

print("\n  Spotting the gradient from closely related to unrelated:")
reference = orthography2ipa.get("es")
print(f"\n  {'Language':30s}  {'Vs Spanish (combined)':>22}  {'Family'}")
print("  " + "-" * 65)
for code in cross_codes:
    try:
        spec = orthography2ipa.get(code)
        d = phonological_distance(reference, spec)
        print(f"  {spec.name:30s}  {d.combined:22.3f}  {spec.family}")
    except KeyError:
        pass


# ═══ 6. IPA transcription comparison across dialects ═══════════════════

print("\n" + "=" * 65)
print("6. IPA TRANSCRIPTION ACROSS DIALECTS")
print("=" * 65)

# Transcribe the same word across Spanish dialects
test_word = "ciudad"
es_variants = ["es", "es-419", "es-AR", "es-ES-x-andalusia-w"]

print(f"\n  Transcribing '{test_word}' across Spanish varieties:")
for code in es_variants:
    try:
        spec = orthography2ipa.get(code)
        tok = PhonetokTokenizer(spec)
        paths = tok.ipa_beam(test_word, beam_width=3)
        path_strs = [f"/{p.ipa}/" for p in paths]
        print(f"    {spec.name:35s}  {', '.join(path_strs)}")
    except KeyError:
        pass

# Portuguese nasal vowels across dialects
test_word_pt = "cação"
pt_variants = ["pt", "pt-BR", "pt-PT-x-porto", "pt-BR-x-rj"]

print(f"\n  Transcribing '{test_word_pt}' across Portuguese varieties:")
for code in pt_variants:
    try:
        spec = orthography2ipa.get(code)
        tok = PhonetokTokenizer(spec)
        paths = tok.ipa_beam(test_word_pt, beam_width=3)
        path_strs = [f"/{p.ipa}/" for p in paths[:2]]
        print(f"    {spec.name:35s}  {', '.join(path_strs)}")
    except KeyError:
        pass
