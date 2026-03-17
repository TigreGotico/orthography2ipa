"""
06_sandhi.py — Cross-word-boundary phonological rules (sandhi / liaison).

Demonstrates:
- Inspecting sandhi rules defined on a LanguageSpec
- SandhiEngine: applying rules to a list of IPA word tokens
- obligatory_only mode
- Building a custom engine with hand-crafted rules
- French liaison as a concrete example
"""

import orthography2ipa
from orthography2ipa.sandhi import SandhiEngine
from orthography2ipa.types import SandhiRule


# ── 1. Rules defined on a LanguageSpec ───────────────────────────────────

print("=" * 60)
print("1. Sandhi rules on French (fr-FR)")
print("=" * 60)

fr = orthography2ipa.get("fr-FR")
print(f"\n  {len(fr.sandhi_rules)} rules defined:")
for rule in fr.sandhi_rules:
    print(f"\n  [{rule.id}]  {rule.name}")
    print(f"    left_context:  {rule.left_context!r}")
    print(f"    right_context: {rule.right_context!r}")
    print(f"    transform:     {rule.transform!r}")
    print(f"    obligatory:    {rule.obligatory}")
    if rule.notes:
        print(f"    notes:         {rule.notes}")


# ── 2. Applying rules with SandhiEngine ──────────────────────────────────

print("\n" + "=" * 60)
print("2. Applying liaison rules")
print("=" * 60)

engine = SandhiEngine(fr.sandhi_rules)

examples = [
    (["lez", "ami"],        "les amis"),
    (["pətit", "ami"],      "petit ami"),
    (["ɛ̃n", "ami"],         "un ami"),
    (["lez", "kɑ̃"],         "les champs (no liaison — consonant-initial)"),
    (["lez", "ami", "ɛ̃"],  "les amis en (chain)"),
]

for words_ipa, note in examples:
    result = engine.apply(words_ipa)
    print(f"\n  {note}")
    print(f"    input:  {words_ipa}")
    print(f"    output: {result}")


# ── 3. obligatory_only mode ───────────────────────────────────────────────

print("\n" + "=" * 60)
print("3. obligatory_only=True vs False")
print("=" * 60)

# If the spec has any optional rules, they're skipped with obligatory_only=True
obligatory_rules = [r for r in fr.sandhi_rules if r.obligatory]
optional_rules   = [r for r in fr.sandhi_rules if not r.obligatory]
print(f"\n  Obligatory rules: {len(obligatory_rules)}")
print(f"  Optional rules:   {len(optional_rules)}")

words = ["lez", "ami"]
full    = engine.apply(words)
oblig   = engine.apply(words, obligatory_only=True)
print(f"\n  Input: {words}")
print(f"  All rules:        {full}")
print(f"  Obligatory only:  {oblig}")


# ── 4. Custom engine with hand-crafted rules ──────────────────────────────

print("\n" + "=" * 60)
print("4. Custom sandhi engine")
print("=" * 60)

# Simplified Sanskrit external sandhi: final /a/ + initial /a/ → /ā/
rules = (
    SandhiRule(
        id="SA_A_SANDHI",
        name="a+a_coalescence",
        left_context=r"a$",
        right_context=r"^a",
        transform="aː",
        obligatory=True,
        notes="a + a → ā (Sanskrit vowel sandhi)",
    ),
    SandhiRule(
        id="SA_A_I_SANDHI",
        name="a+i_coalescence",
        left_context=r"a$",
        right_context=r"^i",
        transform="eː",
        obligatory=True,
        notes="a + i → e (Sanskrit guṇa sandhi)",
    ),
)

custom_engine = SandhiEngine(rules)
print(f"\n  Custom rules: {len(rules)}")

sandhi_examples = [
    (["tatra", "api"],   "tatra + api (a+a)"),
    (["tatra", "iva"],   "tatra + iva (a+i)"),
    (["tatra", "kuca"],  "tatra + kuca (a+k, no sandhi)"),
]
for words_ipa, note in sandhi_examples:
    result = custom_engine.apply(words_ipa)
    print(f"\n  {note}")
    print(f"    input:  {words_ipa}")
    print(f"    output: {result}")


# ── 5. Languages with sandhi rules ───────────────────────────────────────

print("\n" + "=" * 60)
print("5. Language specs with sandhi rules")
print("=" * 60)

codes_to_check = orthography2ipa.available_codes()
found = []
for code in codes_to_check:
    try:
        spec = orthography2ipa.get(code)
        if spec.sandhi_rules:
            found.append((code, spec.name, len(spec.sandhi_rules)))
    except Exception:
        pass

if found:
    for code, name, n in sorted(found, key=lambda x: -x[2]):
        print(f"  {code:20s}  {name:35s}  {n} rules")
else:
    print("  (none found in current data)")
