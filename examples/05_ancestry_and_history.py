"""
05_ancestry_and_history.py — Exploring the ancestry system and historical linguistics.

Demonstrates:
- Inspecting ancestry chains
- Substrate/superstrate/adstrate relationships
- Pre-Roman Iberian languages
- Phylogenetic distance via ancestry similarity
- Tracing a language's lineage back through time
"""

import orthography2ipa
from orthography2ipa.types import AncestorRole
from orthography2ipa.distance import ancestry_similarity, phonological_distance


# ── Helper ────────────────────────────────────────────────────────────────

def print_ancestry(code, depth=0, max_depth=3, _visited=None):
    """Recursively print a language's ancestry tree."""
    if _visited is None:
        _visited = set()
    if code in _visited or depth > max_depth:
        return
    _visited.add(code)

    try:
        spec = orthography2ipa.get(code)
    except KeyError:
        return

    indent = "  " * depth
    marker = "├─" if depth > 0 else "◉"
    print(f"{indent}{marker} {spec.code:25s} {spec.name}")

    for anc in spec.get_ancestors():
        role_str = f"[{anc.role.value:12s} w={anc.weight:.2f}]"
        sub_indent = "  " * (depth + 1)
        print(f"{sub_indent}  {role_str}  → {anc.code}  {anc.notes[:50] if anc.notes else ''}")
        if anc.role == AncestorRole.PARENT and depth < max_depth:
            print_ancestry(anc.code, depth + 1, max_depth, _visited)


def substrate_inventory(code):
    """List all substrate languages for a given language."""
    try:
        spec = orthography2ipa.get(code)
    except KeyError:
        return

    subs = spec.get_ancestors(AncestorRole.SUBSTRATE)
    sups = spec.get_ancestors(AncestorRole.SUPERSTRATE)
    ads = spec.get_ancestors(AncestorRole.ADSTRATE)

    print(f"\n  {spec.name} ({spec.code}) — contact languages:")
    if subs:
        print(f"    Substrates:    {', '.join(a.code for a in subs)}")
    if sups:
        print(f"    Superstrates:  {', '.join(a.code for a in sups)}")
    if ads:
        print(f"    Adstrates:     {', '.join(a.code for a in ads)}")
    if not subs and not sups and not ads:
        print(f"    (none recorded)")


# ═══ 1. Full ancestry tree ════════════════════════════════════════════════

print("=" * 65)
print("1. ANCESTRY TREE — Spanish (es)")
print("=" * 65)
print()
print_ancestry("es", max_depth=4)


print("\n" + "=" * 65)
print("1b. ANCESTRY TREE — French (fr)")
print("=" * 65)
print()
print_ancestry("fr", max_depth=4)


# ═══ 2. Pre-Roman Iberian substrate languages ═════════════════════════════

print("\n" + "=" * 65)
print("2. PRE-ROMAN IBERIAN LANGUAGES")
print("=" * 65)

preroman_codes = ["xce", "xib", "xlg", "txr", "xaq", "phn"]
print()
for code in preroman_codes:
    try:
        spec = orthography2ipa.get(code)
        print(f"  {spec.code:6s}  {spec.name:30s}  [{spec.family}]")
        print(f"         Script: {spec.script}")
        if spec.notes:
            # Show first 120 chars of notes
            print(f"         {spec.notes[:120]}")
        print()
    except KeyError:
        print(f"  {code:6s}  (not found)")


# ═══ 3. Contact language inventories ═════════════════════════════════════

print("=" * 65)
print("3. CONTACT LANGUAGE INFLUENCES")
print("=" * 65)

# Show substrate/superstrate/adstrate for major Ibero-Romance languages
for code in ["es", "pt", "ca", "gl", "fr", "oc"]:
    substrate_inventory(code)


# ═══ 4. Barranquenho — a contact language ════════════════════════════════

print("\n" + "=" * 65)
print("4. BARRANQUENHO — A Contact Language")
print("=" * 65)

try:
    barr = orthography2ipa.get("ext-PT-x-barrancos")
    print(f"\n  Code:    {barr.code}")
    print(f"  Name:    {barr.name}")
    print(f"  Family:  {barr.family}")
    print(f"  Notes:   {barr.notes[:200]}")

    print("\n  Ancestry:")
    for anc in barr.get_ancestors():
        print(f"    {anc.role.value:12s}  {anc.code:20s}  w={anc.weight:.2f}  {anc.notes[:60]}")

    # Compare to its parents
    print("\n  Distance from Barranquenho to related languages:")
    for code in ["pt", "es", "ext"]:
        try:
            spec = orthography2ipa.get(code)
            d = phonological_distance(barr, spec)
            print(f"    vs. {spec.name:30s}  combined={d.combined:.3f}")
        except KeyError:
            pass
except KeyError:
    print("  (Barranquenho not found in registry)")


# ═══ 5. Ancestry similarity matrix ══════════════════════════════════════

print("\n" + "=" * 65)
print("5. ANCESTRY SIMILARITY MATRIX — Iberian Languages")
print("=" * 65)

iberian = ["la", "la-x-hispania", "es", "pt", "ca", "gl", "oc", "eu"]
iberian_specs = []
iberian_labels = []

for code in iberian:
    try:
        spec = orthography2ipa.get(code)
        iberian_specs.append(spec)
        iberian_labels.append(code)
    except KeyError:
        pass

w = 18
print(f"\n  {'':20s}" + "".join(f"{l:>{w}}" for l in iberian_labels))
print("  " + "-" * (20 + w * len(iberian_labels)))

for i, (la, spec_a) in enumerate(zip(iberian_labels, iberian_specs)):
    row = ""
    for j, spec_b in enumerate(iberian_specs):
        sim = ancestry_similarity(spec_a, spec_b)
        row += f"{sim:{w}.3f}"
    print(f"  {la:20s}{row}")


# ═══ 6. Historical time depth ════════════════════════════════════════════

print("\n" + "=" * 65)
print("6. HISTORICAL TIME DEPTH — Latin to Modern Descendants")
print("=" * 65)

# Phonological distances from Classical Latin to its descendants
la = orthography2ipa.get("la")
descendants = [
    ("la-x-hispania", "Hispanic Vulgar Latin  (~3c CE)"),
    ("es",            "Castilian Spanish      (~13c CE)"),
    ("pt",            "European Portuguese    (~13c CE)"),
    ("ca",            "Catalan                (~12c CE)"),
    ("fr",            "French                 (~9c CE)"),
    ("it",            "Italian                (~13c CE)"),
    ("ro",            "Romanian               (~16c CE)"),
    ("oc",            "Occitan                (~11c CE)"),
    ("gl",            "Galician               (~13c CE)"),
]

print("\n  Phonological distance from Classical Latin to descendants:")
print(f"  {'Language':40s}  {'Combined':>9}  {'Inventory':>10}  {'Grapheme':>9}")
print("  " + "-" * 73)
for code, label in descendants:
    try:
        spec = orthography2ipa.get(code)
        d = phonological_distance(la, spec)
        print(
            f"  {label:40s}"
            f"  {d.combined:9.3f}"
            f"  {d.inventory.feature_mean:10.3f}"
            f"  {d.grapheme.mean_ipa_distance:9.3f}"
        )
    except KeyError:
        print(f"  {label:40s}  (not available)")

print("\n  Observation: Greater time depth generally correlates with higher distance,")
print("  but some branches (Romanian, French) diverged more than others (Spanish, Portuguese)")
print("  due to different substrate/superstrate influences.")


# ═══ 7. The Basque substrate ════════════════════════════════════════════

print("\n" + "=" * 65)
print("7. THE BASQUE SUBSTRATE — A Linguistic Laboratory")
print("=" * 65)

print("""
  Basque (eu) is a language isolate — unrelated to any other known language.
  It has been spoken in the Pyrenean region since before Roman times.

  Its substrate influence on Castilian Spanish is one of the best-documented
  substrate effects in Romance linguistics:

  1. The f→h change: Latin FILIUM → Spanish HIJO
     - This change is geographically limited to areas of historic Basque
       speech; Portuguese and Catalan retain /f/ (*filho*, *fill*)
     - Basque traditionally lacked /f/ as a phoneme

  2. Reinforcement of the 5-vowel system:
     - Spanish has a remarkably clean 5-vowel system (a,e,i,o,u)
     - Basque also has a strict 5-vowel system
     - Latin had a more complex system with length distinctions

  3. Possible influence on the evolution of /ʃ/ sounds:
     - Old Spanish had sibilants that merged differently in Castilian
       vs. Portuguese — Basque phonological patterns may have influenced
       the Castilian outcome
""")

try:
    eu = orthography2ipa.get("eu")
    xaq = orthography2ipa.get("xaq")
    es = orthography2ipa.get("es")

    print("  Basque (eu) inventory — note: no /f/ phoneme!")
    basque_consonants = [k for k in eu.graphemes if k in list("bcdfghjklmnpqrstvwxyz")]
    f_like = {k: v for k, v in eu.graphemes.items() if any("f" in ipa for ipa in v)}
    print(f"  Graphemes mapping to something with /f/: {f_like or '(none)'}")

    # Ancestry similarity between Basque and Spanish
    sim = ancestry_similarity(es, eu)
    print(f"\n  Ancestry similarity Spanish ↔ Basque: {sim:.3f}")
    print(f"  (Basque appears as substrate in Spanish's ancestry — hence > 0)")
except KeyError as e:
    print(f"  (Error: {e})")
