"""
04_dialect_transforms.py — Dialect-specific IPA transforms for Portuguese.

Demonstrates:
- Listing available dialect profiles
- Inspecting DialectTransform rules
- apply_transform: applying a profile to a canonical IPA string
- debias_lisbon: removing Lisbon-specific biases before transform
- Comparing the same word across multiple regional dialects
"""

import orthography2ipa
from orthography2ipa.transforms import (
    DIALECT_PROFILES,
    apply_transform,
    available_profiles,
    debias_lisbon,
)


# ── 1. Available profiles ────────────────────────────────────────────────

print("=" * 60)
print("1. Available dialect profiles")
print("=" * 60)

for name in available_profiles():
    dt = DIALECT_PROFILES[name]
    debias = "debias first" if dt.requires_debiasing else "no debias"
    print(f"  {name:20s}  {len(dt.rules):2d} rules  ({debias})  [{dt.cintra_zone}]")


# ── 2. Inspect a profile's rules ─────────────────────────────────────────

print("\n" + "=" * 60)
print("2. Profile rules — transmontano (NE Portugal)")
print("=" * 60)

dt = DIALECT_PROFILES["transmontano"]
print(f"\n  {dt.name}")
for rule in dt.rules:
    print(f"  [{rule.id}]  /{rule.find}/ → /{rule.replace}/")
    print(f"          {rule.description}")


# ── 3. apply_transform basics ────────────────────────────────────────────

print("\n" + "=" * 60)
print("3. apply_transform: canonical IPA → dialect IPA")
print("=" * 60)

# 'vĩɲu' = canonical PT-PT IPA for 'vinho' (wine)
# Lisbon keeps /v/; Northern dialects merge /v/ → /b/
canonical = "vĩɲu"
print(f"\n  Input (canonical IPA): /{canonical}/")
for profile in ["lisbon", "porto", "transmontano", "northern"]:
    result = apply_transform(canonical, profile)
    print(f"  {profile:15s} → /{result}/")


# ── 4. debias_lisbon ─────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("4. debias_lisbon: undo Lisbon-specific reductions")
print("=" * 60)

# The Lisbon pronunciation of 'deitado' encodes ej→ɐj lowering.
# debias_lisbon reverses this so a Northern transform gets neutral input.
lisbon_biased = "ɐjtadu"  # Lisbon output of 'deitado'
neutral = debias_lisbon(lisbon_biased)
print(f"\n  Biased (Lisbon):  /{lisbon_biased}/")
print(f"  Debiased:         /{neutral}/")

# Now apply a Northern profile to the debiased form
northern = apply_transform(neutral, "porto")
print(f"  Porto transform:  /{northern}/")


# ── 5. Same word across all dialects ─────────────────────────────────────

print("\n" + "=" * 60)
print("5. Word comparison across all dialects")
print("=" * 60)

words = [
    ("vinho",    "bĩɲu",  "wine — canonical starts Lisbon-biased"),
    ("prato",    "pɾatu", "plate"),
    ("saber",    "sabɛɾ", "to know"),
]

for ortho, canonical_ipa, note in words:
    print(f"\n  '{ortho}'  ({note})")
    print(f"  canonical: /{canonical_ipa}/")
    for profile in available_profiles():
        result = apply_transform(canonical_ipa, profile)
        if result != canonical_ipa:
            print(f"    {profile:20s} → /{result}/")


# ── 6. Chain-shift example ───────────────────────────────────────────────

print("\n" + "=" * 60)
print("6. Lisbon diphthong lowering (chain shift)")
print("=" * 60)

# Lisbon specifically lowers /ej/ → [ɐj] and /ow/ → [ow] is retained
from orthography2ipa.transforms import IPARule, IPAChainShift  # noqa

rule = IPARule(
    id="DEMO",
    name="demo_lowering",
    find="ej",
    replace="ɐj",
    context=None,
    requires_ortho=False,
    description="Demo: /ej/ → [ɐj]",
)
print(f"\n  Rule: {rule.description}")
print(f"  Input  'pej'  → /{apply_transform('pej', 'lisbon')}/")
print(f"  Input  'rej'  → /{apply_transform('rej', 'lisbon')}/")
print(f"  Input  'vej'  → /{apply_transform('vej', 'lisbon')}/")
