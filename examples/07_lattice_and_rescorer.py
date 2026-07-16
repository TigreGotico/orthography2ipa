"""
07_lattice_and_rescorer.py — The pronunciation lattice and how to refine it.

Demonstrates:
- Inspecting the ranked, cost-annotated IPA lattice for a word
- The per-word confidence signal (when the engine is unsure)
- Writing a LatticeRescorer to teach the beam a language-specific reading

The lattice is the surface a specialised phonemizer stands on: the generic
beam gives every word a defensible transcription, and a rescorer re-costs
candidates where domain knowledge beats the generic ranking.
"""

from orthography2ipa import get, G2P
from orthography2ipa.phonetok import PhonetokTokenizer, Candidate
from orthography2ipa.rescorer import LatticeRescorer


# ── 1. The ranked lattice: every option per grapheme, with a -log P cost ────

tok = PhonetokTokenizer(get("en-GB"))

print("=" * 60)
print("1. IPA lattice for 'cough'")
print("=" * 60)
for slot in tok.ipa_lattice("cough"):
    options = [(c.ipa, c.cost) for c in slot.candidates]
    print(f"  {slot.grapheme:6s} -> {options}")


# ── 2. Confidence: the engine tells you when it is unsure ───────────────────

print("\n" + "=" * 60)
print("2. Per-word confidence (top-1 vs top-2 margin x coverage)")
print("=" * 60)
g = G2P("en-GB")
for word in ["bar", "cough", "bar你"]:
    print(f"  {word:8s} -> {g.word_confidence(word):.4f}")


# ── 3. A rescorer: teach English <ough> its /ʌf/ reading ────────────────────

class RoughOugh(LatticeRescorer):
    """Make 'ough' -> /ʌf/ the cheapest candidate (rough, tough, enough)."""

    def rescore(self, slot, context):
        if slot.grapheme != "ough":
            return slot.candidates  # no-op elsewhere
        others = [c for c in slot.candidates if c.ipa != "ʌf"]
        return [Candidate("ʌf", 0.0)] + [
            Candidate(c.ipa, c.cost + 1.0) for c in others
        ]


print("\n" + "=" * 60)
print("3. Refining the beam with a rescorer")
print("=" * 60)
print(f"  generic beam : tough -> {tok.ipa_best('tough')!r}")
print(f"  with rescorer: tough -> {tok.ipa_best('tough', rescorer=RoughOugh())!r}")
