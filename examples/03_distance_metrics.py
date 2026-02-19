"""
03_distance_metrics.py — Phonological distance calculations.

Demonstrates:
- Segment (phone) distance using distinctive features
- Inventory distance between languages
- Grapheme divergence
- Allophone overlap
- Combined phonological distance
- Pairwise distance matrices
- Ancestry similarity
"""

import orthography2ipa
from orthography2ipa.distance import (
    segment_distance,
    feature_vector,
    feature_names,
    inventory_distance,
    grapheme_divergence,
    allophone_overlap,
    phonological_distance,
    ancestry_similarity,
    pairwise_distances,
)


# ── Helper ───────────────────────────────────────────────────────────────

def print_matrix(labels, matrix):
    """Pretty-print a distance matrix."""
    w = 8
    header = " " * 14 + "".join(f"{l:>{w}}" for l in labels)
    print(header)
    print("  " + "-" * (12 + w * len(labels)))
    for i, (label, row) in enumerate(zip(labels, matrix)):
        cells = "".join(f"{v:{w}.3f}" for v in row)
        print(f"  {label:12s}{cells}")


# ═══ 1. Segment (phone) distance ════════════════════════════════════════

print("=" * 65)
print("1. Segment Distance")
print("=" * 65)

# Minimal pairs (voicing only)
pairs_voicing = [("p","b"), ("t","d"), ("k","ɡ"), ("f","v"), ("s","z"), ("ʃ","ʒ")]
print("\n  Voicing minimal pairs:")
for a, b in pairs_voicing:
    d = segment_distance(a, b)
    print(f"    {a} ↔ {b} = {d:.4f}")

# Place of articulation
print("\n  Place of articulation (voiceless stops):")
stops = ["p", "t", "k"]
for a in stops:
    for b in stops:
        d = segment_distance(a, b)
        print(f"    {a} ↔ {b} = {d:.4f}")

# Manner changes
print("\n  Manner contrasts (for /t/):")
manners = [("t","t"), ("t","d"), ("t","n"), ("t","s"), ("t","l"), ("t","r")]
for a, b in manners:
    d = segment_distance(a, b)
    print(f"    {a} ↔ {b} = {d:.4f}")

# Consonant vs. vowel — always 1.0
print("\n  Consonant ↔ vowel (always 1.0):")
for seg in ["p", "s", "n", "l"]:
    d = segment_distance(seg, "a")
    print(f"    {seg} ↔ a = {d:.4f}")


# ═══ 2. Feature vectors ═════════════════════════════════════════════════

print("\n" + "=" * 65)
print("2. Feature Vectors")
print("=" * 65)

names = feature_names()
print("\n  Features for /p/ and /b/ (should differ only in voice):")
vec_p = feature_vector("p")
vec_b = feature_vector("b")
print(f"  {'Feature':25s}  {'p':>6}  {'b':>6}  {'diff':>6}")
print("  " + "-" * 46)
for name, vp, vb in zip(names, vec_p, vec_b):
    if vp != 0.5 or vb != 0.5 or vp != vb:
        diff = abs(vp - vb)
        marker = " ◄" if diff > 0 else ""
        print(f"  {name:25s}  {vp:6.1f}  {vb:6.1f}  {diff:6.3f}{marker}")


# ═══ 3. Inventory distance ══════════════════════════════════════════════

print("\n" + "=" * 65)
print("3. Inventory Distance")
print("=" * 65)

comparisons = [
    ("es",    "pt",    "Spanish vs. Portuguese"),
    ("es",    "it",    "Spanish vs. Italian"),
    ("es",    "fr",    "Spanish vs. French"),
    ("pt-BR", "pt",    "Brazilian vs. European Portuguese"),
    ("la",    "es",    "Latin vs. Spanish"),
    ("la",    "fr",    "Latin vs. French"),
    ("en",    "de",    "English vs. German"),
    ("es",    "en",    "Spanish vs. English"),
    ("es",    "ar",    "Spanish vs. Arabic"),
    ("es",    "zh",    "Spanish vs. Mandarin"),
]

print(f"\n  {'Pair':35s}  {'Jaccard':>8}  {'Feature':>8}  {'Shared':>8}")
print("  " + "-" * 65)
for code_a, code_b, label in comparisons:
    try:
        spec_a = orthography2ipa.get(code_a)
        spec_b = orthography2ipa.get(code_b)
        inv = inventory_distance(spec_a, spec_b)
        print(
            f"  {label:35s}"
            f"  {inv.jaccard:8.3f}"
            f"  {inv.feature_mean:8.3f}"
            f"  {inv.shared:>4}/{max(inv.size_a,inv.size_b)}"
        )
    except KeyError as e:
        print(f"  {label:35s}  SKIP ({e})")


# ═══ 4. Grapheme divergence ══════════════════════════════════════════════

print("\n" + "=" * 65)
print("4. Grapheme Divergence")
print("=" * 65)

print(f"\n  {'Pair':35s}  {'Shared/Total':>14}  {'IPA dist':>9}  {'Overlap':>8}")
print("  " + "-" * 73)
for code_a, code_b, label in comparisons:
    try:
        spec_a = orthography2ipa.get(code_a)
        spec_b = orthography2ipa.get(code_b)
        gd = grapheme_divergence(spec_a, spec_b)
        shared_total = f"{gd.shared_graphemes}/{gd.total_graphemes}"
        print(
            f"  {label:35s}"
            f"  {shared_total:>14}"
            f"  {gd.mean_ipa_distance:9.3f}"
            f"  {gd.overlap_ratio:8.3f}"
        )
    except KeyError:
        pass


# ═══ 5. Allophone overlap ════════════════════════════════════════════════

print("\n" + "=" * 65)
print("5. Allophone Overlap (Jaccard similarity)")
print("=" * 65)

print(f"\n  {'Pair':35s}  {'Overlap':>8}")
print("  " + "-" * 48)
for code_a, code_b, label in comparisons:
    try:
        spec_a = orthography2ipa.get(code_a)
        spec_b = orthography2ipa.get(code_b)
        ov = allophone_overlap(spec_a, spec_b)
        print(f"  {label:35s}  {ov:8.3f}")
    except KeyError:
        pass


# ═══ 6. Combined phonological distance ══════════════════════════════════

print("\n" + "=" * 65)
print("6. Combined Phonological Distance")
print("=" * 65)

print(f"\n  {'Pair':35s}  {'Combined':>9}  {'Inventory':>10}  {'Grapheme':>9}  {'Allophone':>10}")
print("  " + "-" * 80)
for code_a, code_b, label in comparisons:
    try:
        spec_a = orthography2ipa.get(code_a)
        spec_b = orthography2ipa.get(code_b)
        d = phonological_distance(spec_a, spec_b)
        print(
            f"  {label:35s}"
            f"  {d.combined:9.3f}"
            f"  {d.inventory.feature_mean:10.3f}"
            f"  {d.grapheme.mean_ipa_distance:9.3f}"
            f"  {1 - d.allophone_sim:10.3f}"
        )
    except KeyError:
        pass


# ═══ 7. Custom weights ══════════════════════════════════════════════════

print("\n" + "=" * 65)
print("7. Combined Distance with Custom Weights")
print("=" * 65)

spec_es = orthography2ipa.get("es")
spec_pt = orthography2ipa.get("pt")

print("\n  Spanish vs. Portuguese — effect of varying weights:")
print(f"  {'w_inv':>6}  {'w_graph':>7}  {'w_allo':>7}  {'combined':>9}")
print("  " + "-" * 36)
for w_inv, w_graph, w_allo in [
    (0.40, 0.30, 0.30),  # default
    (1.00, 0.00, 0.00),  # inventory only
    (0.00, 1.00, 0.00),  # grapheme only
    (0.00, 0.00, 1.00),  # allophone only
    (0.50, 0.50, 0.00),  # inventory + grapheme
]:
    d = phonological_distance(spec_es, spec_pt,
                               w_inventory=w_inv,
                               w_grapheme=w_graph,
                               w_allophone=w_allo)
    print(f"  {w_inv:6.2f}  {w_graph:7.2f}  {w_allo:7.2f}  {d.combined:9.3f}")


# ═══ 8. Pairwise distance matrix ════════════════════════════════════════

print("\n" + "=" * 65)
print("8. Pairwise Distance Matrix — Ibero-Romance")
print("=" * 65)

ibero_codes = ["la", "es", "pt", "pt-BR", "ca", "gl", "oc"]
ibero_specs = []
ibero_labels = []
for code in ibero_codes:
    try:
        spec = orthography2ipa.get(code)
        ibero_specs.append(spec)
        ibero_labels.append(code)
    except KeyError:
        pass

matrix = pairwise_distances(ibero_specs, metric="combined")
print()
print_matrix(ibero_labels, matrix)


# ═══ 9. Ancestry similarity ══════════════════════════════════════════════

print("\n" + "=" * 65)
print("9. Ancestry Similarity")
print("=" * 65)

ancestry_pairs = [
    ("es",    "pt",    "Spanish vs. Portuguese (sister languages)"),
    ("es",    "ca",    "Spanish vs. Catalan"),
    ("la",    "es",    "Latin vs. Spanish (direct ancestor)"),
    ("la",    "it",    "Latin vs. Italian"),
    ("la",    "fr",    "Latin vs. French"),
    ("en",    "de",    "English vs. German (Germanic sisters)"),
    ("es",    "en",    "Spanish vs. English (Romance vs. Germanic)"),
    ("es",    "ar",    "Spanish vs. Arabic (contact, not related)"),
]

print(f"\n  {'Pair':40s}  {'Similarity':>11}")
print("  " + "-" * 55)
for code_a, code_b, label in ancestry_pairs:
    try:
        spec_a = orthography2ipa.get(code_a)
        spec_b = orthography2ipa.get(code_b)
        sim = ancestry_similarity(spec_a, spec_b)
        print(f"  {label:40s}  {sim:11.3f}")
    except KeyError as e:
        print(f"  {label:40s}  SKIP ({e})")
