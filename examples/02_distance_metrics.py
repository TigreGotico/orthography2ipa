"""
02_distance_metrics.py — Phonological distance between languages.

Demonstrates:
- Segment-level feature distance
- Inventory, grapheme-divergence, and allophone overlap
- Phonological distance (combined scalar)
- Ancestry similarity and full distance
- phoneme_coverage (asymmetric L2 difficulty metric)
- weighted_full_distance with custom weights
- pairwise distance matrix
"""

import orthography2ipa
from orthography2ipa.distance import (
    allophone_overlap,
    ancestry_similarity,
    feature_vector,
    full_distance,
    grapheme_divergence,
    inventory_distance,
    orthographic_distance,
    pairwise_distances,
    phoneme_coverage,
    phonological_distance,
    positional_divergence,
    segment_distance,
    tone_distance,
    weighted_full_distance,
)

es = orthography2ipa.get("es-ES")
pt = orthography2ipa.get("pt-PT")
fr = orthography2ipa.get("fr-FR")
it = orthography2ipa.get("it-IT")
la = orthography2ipa.get("la")


# ── 1. Segment distance ──────────────────────────────────────────────────

print("=" * 60)
print("1. Segment distance (feature-weighted Hamming)")
print("=" * 60)

pairs = [
    ("p", "b", "voicing only"),
    ("p", "f", "manner + labial"),
    ("p", "t", "place only"),
    ("p", "a", "consonant vs vowel"),
    ("s", "z", "voicing only"),
    ("n", "m", "place only"),
    ("i", "u", "backness only"),
]
for a, b, note in pairs:
    d = segment_distance(a, b)
    print(f"  /{a}/ ↔ /{b}/  {d:.4f}  ({note})")

print()
print("  Feature vector for /p/:")
vec = feature_vector("p")
from orthography2ipa.distance import feature_names  # noqa
names = feature_names()
active = [(n, v) for n, v in zip(names, vec) if v != 0.5]
for name, val in active:
    print(f"    {name:25s} {val}")


# ── 2. Inventory distance ────────────────────────────────────────────────

print("\n" + "=" * 60)
print("2. Inventory distance")
print("=" * 60)

for pair, (a, b) in [("es ↔ pt", (es, pt)), ("es ↔ fr", (es, fr)), ("la ↔ it", (la, it))]:
    inv = inventory_distance(a, b)
    print(f"\n  {pair}")
    print(f"    Jaccard:     {inv.jaccard:.3f}  (1 = identical sets)")
    print(f"    Feature mean:{inv.feature_mean:.3f}  (feature-weighted match)")
    print(f"    Shared:      {inv.shared}")


# ── 3. Grapheme divergence ───────────────────────────────────────────────

print("\n" + "=" * 60)
print("3. Grapheme divergence (same script, different pronunciations)")
print("=" * 60)

for pair, (a, b) in [("es ↔ fr", (es, fr)), ("es ↔ pt", (es, pt)), ("la ↔ it", (la, it))]:
    gd = grapheme_divergence(a, b)
    print(f"\n  {pair}")
    print(f"    Shared graphemes: {gd.shared_graphemes}/{gd.total_graphemes}")
    print(f"    Mean IPA dist:    {gd.mean_ipa_distance:.3f}")
    print(f"    Overlap ratio:    {gd.overlap_ratio:.3f}")


# ── 4. Allophone overlap ─────────────────────────────────────────────────

print("\n" + "=" * 60)
print("4. Allophone overlap  (1.0 = identical surface inventories)")
print("=" * 60)

for pair, (a, b) in [("es ↔ pt", (es, pt)), ("es ↔ fr", (es, fr)), ("la ↔ it", (la, it))]:
    print(f"  {pair}: {allophone_overlap(a, b):.3f}")


# ── 5. Phonological distance ─────────────────────────────────────────────

print("\n" + "=" * 60)
print("5. Phonological distance (combined scalar, lower = more similar)")
print("=" * 60)

for pair, (a, b) in [("la ↔ it", (la, it)), ("es ↔ pt", (es, pt)), ("es ↔ fr", (es, fr))]:
    pd = phonological_distance(a, b)
    print(f"\n  {pair}")
    print(f"    Combined:  {pd.combined:.3f}")
    print(f"    Inventory: {pd.inventory.jaccard:.3f}  (jaccard)")
    print(f"    Grapheme:  {pd.grapheme.mean_ipa_distance:.3f}  (mean IPA dist)")
    print(f"    Allophone: {pd.allophone_sim:.3f}  (similarity)")


# ── 6. Ancestry similarity ───────────────────────────────────────────────

print("\n" + "=" * 60)
print("6. Ancestry similarity  (1.0 = identical family tree)")
print("=" * 60)

for pair, (a, b) in [
    ("es ↔ pt", (es, pt)),
    ("es ↔ it", (es, it)),
    ("es ↔ fr", (es, fr)),
    ("la ↔ it", (la, it)),
]:
    print(f"  {pair}: {ancestry_similarity(a, b):.3f}")


# ── 7. Full distance ─────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("7. Full distance (all components)")
print("=" * 60)

for pair, (a, b) in [("es ↔ pt", (es, pt)), ("es ↔ fr", (es, fr)), ("es ↔ it", (es, it))]:
    print(f"  {pair}: {full_distance(a, b):.4f}")


# ── 8. Phoneme coverage (asymmetric) ────────────────────────────────────

print("\n" + "=" * 60)
print("8. Phoneme coverage  (L2 difficulty: what fraction of target")
print("   phonemes does the native speaker already know?)")
print("=" * 60)

for native, target, (a, b) in [
    ("es", "pt", (es, pt)),
    ("pt", "es", (pt, es)),
    ("es", "fr", (es, fr)),
    ("fr", "es", (fr, es)),
]:
    cov = phoneme_coverage(a, b)
    print(f"  {native} → {target}: {cov:.1%} of {target} phonemes covered")


# ── 9. Weighted full distance ────────────────────────────────────────────

print("\n" + "=" * 60)
print("9. Weighted full distance (configurable component weights)")
print("=" * 60)

# Default weights (overall linguistic relatedness)
result = weighted_full_distance(es, fr)
print(f"\n  es ↔ fr  default weights {result.weights}:")
print(f"    inventory: {result.inventory:.3f}")
print(f"    grapheme:  {result.grapheme:.3f}")
print(f"    allophone: {result.allophone:.3f}  (similarity)")
print(f"    ancestry:  {result.ancestry:.3f}  (similarity)")
print(f"    combined:  {result.combined:.3f}")

# Ancestry-only mode (e.g. phylogenetics research)
result_anc = weighted_full_distance(es, fr, w_inventory=0.0, w_grapheme=0.0,
                                     w_allophone=0.0, w_ancestry=1.0)
print(f"\n  es ↔ fr  ancestry-only weights:")
print(f"    combined:  {result_anc.combined:.3f}  (== 1 - ancestry_similarity)")


# ── 10. Pairwise matrix ──────────────────────────────────────────────────

print("\n" + "=" * 60)
print("10. Pairwise distance matrix")
print("=" * 60)

specs = [es, pt, fr, it, la]
labels = [s.code for s in specs]
matrix = pairwise_distances(specs)

header = "         " + "  ".join(f"{l:7s}" for l in labels)
print(f"\n  {header}")
for label, row in zip(labels, matrix):
    row_str = "  ".join(f"{v:7.4f}" for v in row)
    print(f"  {label:8s} {row_str}")


# ── 11. Supplementary metrics ────────────────────────────────────────────

print("\n" + "=" * 60)
print("11. Supplementary metrics")
print("=" * 60)

print(f"\n  Orthographic distance (script-level divergence):")
for pair, (a, b) in [("es ↔ fr", (es, fr)), ("es ↔ pt", (es, pt))]:
    print(f"    {pair}: {orthographic_distance(a, b):.4f}")

print(f"\n  Tone distance (tonal language pair):")
print(f"    es ↔ fr: {tone_distance(es, fr):.3f}  (neither is tonal)")

print(f"\n  Positional divergence (positional grapheme override differences):")
for pair, (a, b) in [("es ↔ fr", (es, fr)), ("es ↔ pt", (es, pt))]:
    print(f"    {pair}: {positional_divergence(a, b):.4f}")
