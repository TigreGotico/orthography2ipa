"""
08_lexicon_overlay.py — Overlaying an external pronunciation lexicon.

Demonstrates:
- Loading an external `word<TAB>ipa` lexicon by local path
  (a URL or `hf://<repo>/<file>` id works identically)
- Giving it to one engine through a `Pipeline`
- How a lexicon hit overrides the grapheme rules and reports full confidence

No corpus is bundled with the library — a word list is not a description of a
language. The caller supplies one for deep-orthography languages whose rules
cannot reach a lexicon's accuracy on their own. The lexicon belongs to the
engine that holds it, so another engine keeps the rules.
"""

import tempfile
from pathlib import Path

import orthography2ipa as o2i


# ── 1. A tiny local lexicon (word<TAB>ipa, one pair per line) ───────────────

tmp = Path(tempfile.mkdtemp()) / "en-GB.tsv"
tmp.write_text("colonel\tkɜːnəl\nchoir\tkwaɪə\n", encoding="utf-8")

print("=" * 60)
print("1. An engine with no lexicon (grapheme rules only)")
print("=" * 60)
print(f"  colonel -> {o2i.transcribe('colonel', 'en-GB')!r}")

# ── 2. Load by path (a URL or hf:// id is accepted the same way) ────────────

lexicon = o2i.load_lexicon(tmp)

print("\n" + "=" * 60)
print("2. An engine with the lexicon (overlay wins)")
print("=" * 60)
g = o2i.G2P("en-GB", pipeline=o2i.Pipeline(lexicon=lexicon))
for word in ["colonel", "choir"]:
    result = g.transcribe_detailed(word)
    print(f"  {word:8s} -> {result.ipa!r}   confidence={result.words[0].confidence}")

print("\n  A lexicon hit routes through the same override path as")
print("  spec.word_exceptions, so it still gets stress and sandhi, and")
print("  is reported as a certain answer (confidence == 1.0).")
