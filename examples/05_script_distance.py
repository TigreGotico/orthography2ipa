"""
05_script_distance.py — Writing-system distance between scripts.

Demonstrates:
- ScriptFeatures: the structured descriptor for each script
- script_distance_by_name: scalar distance between any two scripts
- Browsing the SCRIPT_REGISTRY
- Comparing all pairs in a set of scripts
"""

from orthography2ipa.script_distance import (
    SCRIPT_REGISTRY,
    ScriptFeatures,
    script_distance,
    script_distance_by_name,
)


# ── 1. The script registry ───────────────────────────────────────────────

print("=" * 60)
print("1. Registered scripts")
print("=" * 60)

for name, sf in sorted(SCRIPT_REGISTRY.items()):
    print(f"\n  {name}")
    print(f"    type:          {sf.script_type.value}")
    print(f"    direction:     {sf.directionality}")
    print(f"    case:          {sf.has_case}")
    print(f"    vowel marking: {sf.vowel_marking}")
    print(f"    ancestors:     {', '.join(sf.ancestor_scripts) or 'none'}")


# ── 2. Pairwise script distances ─────────────────────────────────────────

print("\n" + "=" * 60)
print("2. Pairwise script distances (0.0 = identical, 1.0 = maximally distant)")
print("=" * 60)

scripts = ["Latin", "Cyrillic", "Greek", "Arabic", "Hebrew",
           "Devanagari", "Bengali", "Tamil", "Georgian", "Armenian"]

# Header row
header = "             " + "  ".join(f"{s[:5]:>5s}" for s in scripts)
print(f"\n{header}")
for a in scripts:
    row = "  ".join(f"{script_distance_by_name(a, b):5.3f}" for b in scripts)
    print(f"  {a:12s} {row}")


# ── 3. Closest and farthest pairs ────────────────────────────────────────

print("\n" + "=" * 60)
print("3. Most similar and most distant pairs")
print("=" * 60)

pairs = []
for i, a in enumerate(scripts):
    for b in scripts[i + 1:]:
        d = script_distance_by_name(a, b)
        pairs.append((d, a, b))

pairs.sort()
print("\n  5 most similar:")
for d, a, b in pairs[:5]:
    print(f"    {a:12s} ↔ {b:12s}  {d:.4f}")

print("\n  5 most distant:")
for d, a, b in pairs[-5:]:
    print(f"    {a:12s} ↔ {b:12s}  {d:.4f}")


# ── 4. Feature-level inspection ──────────────────────────────────────────

print("\n" + "=" * 60)
print("4. Why are Latin and Cyrillic so close?")
print("=" * 60)

lat = SCRIPT_REGISTRY["Latin"]
cyr = SCRIPT_REGISTRY["Cyrillic"]
print(f"\n  Latin:    type={lat.script_type.value}  dir={lat.directionality}"
      f"  case={lat.has_case}  vowels={lat.vowel_marking}")
print(f"  Cyrillic: type={cyr.script_type.value}  dir={cyr.directionality}"
      f"  case={cyr.has_case}  vowels={cyr.vowel_marking}")
print(f"\n  Both are LTR alphabets with full vowels and case — only"
      f" Unicode block and ancestry differ.")
print(f"  Distance: {script_distance_by_name('Latin', 'Cyrillic'):.4f}")

print("\n  Latin ↔ Arabic:")
lat = SCRIPT_REGISTRY["Latin"]
ara = SCRIPT_REGISTRY["Arabic"]
print(f"  Latin:  dir={lat.directionality}  vowels={lat.vowel_marking}  case={lat.has_case}")
print(f"  Arabic: dir={ara.directionality}  vowels={ara.vowel_marking}  case={ara.has_case}")
print(f"  Distance: {script_distance_by_name('Latin', 'Arabic'):.4f}")
