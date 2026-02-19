"""
01_basic_usage.py — Basic usage of orthography2ipa.

Demonstrates:
- Loading language specs
- Accessing grapheme→IPA mappings
- Accessing allophone inventories
- Listing available languages
"""

import orthography2ipa


# ── 1. Load a language spec ────────────────────────────────────────────────

en = orthography2ipa.get("en")
es = orthography2ipa.get("es")
pt_br = orthography2ipa.get("pt-BR")
fr = orthography2ipa.get("fr")

print("=" * 60)
print("1. Language metadata")
print("=" * 60)
for spec in [en, es, pt_br, fr]:
    print(f"  {spec.code:12s}  {spec.name:35s}  [{spec.family}]")


# ── 2. Explore grapheme→IPA mappings ─────────────────────────────────────

print("\n" + "=" * 60)
print("2. Grapheme → IPA mappings")
print("=" * 60)

# English ambiguous graphemes
print("\n  English ambiguous graphemes:")
for g in ["th", "c", "g", "a", "e", "sh", "ch", "ph"]:
    ipa_list = en.graphemes.get(g, [])
    if ipa_list:
        print(f"    ⟨{g}⟩  →  {ipa_list}")

# Spanish digraphs and special characters
print("\n  Spanish graphemes:")
for g in ["ll", "rr", "ch", "ñ", "c", "z", "g", "j", "h", "qu"]:
    ipa_list = es.graphemes.get(g, [])
    if ipa_list:
        print(f"    ⟨{g}⟩  →  {ipa_list}")

# Portuguese-specific graphemes
print("\n  Portuguese (pt-BR) graphemes:")
for g in ["lh", "nh", "x", "ch", "rr", "ã", "ão", "em"]:
    ipa_list = pt_br.graphemes.get(g, [])
    if ipa_list:
        print(f"    ⟨{g}⟩  →  {ipa_list}")


# ── 3. Explore allophone inventories ─────────────────────────────────────

print("\n" + "=" * 60)
print("3. Allophone inventories")
print("=" * 60)

print("\n  English /t/ — multiple allophones:")
for allo in en.allophones.get("t", []):
    print(f"    [{allo}]")

print("\n  Spanish /b/ — lenition:")
for allo in es.allophones.get("b", []):
    print(f"    [{allo}]")

print("\n  Spanish /n/ — place assimilation:")
for allo in es.allophones.get("n", []):
    print(f"    [{allo}]")

print("\n  French /r/ — uvular variants:")
for allo in fr.allophones.get("r", []):
    print(f"    [{allo}]")


# ── 4. Inventory sizes ─────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("4. Inventory sizes")
print("=" * 60)

langs = ["en", "es", "pt-BR", "pt", "fr", "it", "de", "ru", "ar", "zh", "ja", "ko"]
print(f"\n  {'Code':12s}  {'Graphemes':>10}  {'Allophones':>11}")
print("  " + "-" * 38)
for code in langs:
    try:
        spec = orthography2ipa.get(code)
        print(f"  {code:12s}  {len(spec.graphemes):>10}  {len(spec.allophones):>11}")
    except KeyError:
        pass


# ── 5. List available language families ─────────────────────────────────

print("\n" + "=" * 60)
print("5. Available language families")
print("=" * 60)

families = orthography2ipa.available_families()
for family in sorted(families):
    codes = families[family]
    # Show only first 6 codes to keep output readable
    shown = ", ".join(codes[:6])
    extra = f" (+{len(codes)-6} more)" if len(codes) > 6 else ""
    print(f"\n  {family}")
    print(f"    {shown}{extra}")


# ── 6. ISO 639-3 aliases ─────────────────────────────────────────────────

print("\n" + "=" * 60)
print("6. ISO 639-3 code aliases")
print("=" * 60)

aliases = [("por", "pt"), ("eng", "en"), ("spa", "es"), ("lat", "la")]
for iso3, bcp47 in aliases:
    spec = orthography2ipa.get(iso3)
    print(f"  get('{iso3}')  →  {spec.code}  ({spec.name})")
