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

pt = orthography2ipa.get("pt-PT")

print("=" * 60)
print("1. Language metadata")
print("=" * 60)
for spec in [pt]:
    print(f"  {spec.code:12s}  {spec.name:35s}  [{spec.family}]")


# ── 2. Explore grapheme→IPA mappings ─────────────────────────────────────

print("\n" + "=" * 60)
print("2. Grapheme → IPA mappings")
print("=" * 60)


# Portuguese-specific graphemes
print("\n  Portuguese graphemes:")
for g in ["lh", "nh", "x", "ch", "rr", "ã", "ão", "em"]:
    ipa_list = pt.graphemes.get(g, [])
    if ipa_list:
        print(f"    ⟨{g}⟩  →  {ipa_list}")


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
