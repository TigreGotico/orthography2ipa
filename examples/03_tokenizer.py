"""
03_tokenizer.py — Grapheme tokenization and IPA beam search.

Demonstrates:
- PhonetokTokenizer: maximal-munch grapheme segmentation
- Token kinds (GRAPHEME, WHITESPACE, PUNCTUATION, UNKNOWN)
- ipa_beam: all IPA transcription candidates with scores
- Allophone expansion
- Multi-language comparison
"""

import orthography2ipa
from orthography2ipa.phonetok import PhonetokTokenizer, TokenKind

en = orthography2ipa.get("en-GB")
pt = orthography2ipa.get("pt-PT")
fr = orthography2ipa.get("fr-FR")


# ── 1. Basic tokenization ────────────────────────────────────────────────

print("=" * 60)
print("1. Grapheme tokenization (maximal munch)")
print("=" * 60)

tok_pt = PhonetokTokenizer(pt)
tok_en = PhonetokTokenizer(en)
tok_fr = PhonetokTokenizer(fr)

examples = [
    (tok_pt, "pt", "chuva"),
    (tok_pt, "pt", "lhano"),
    (tok_en, "en", "through"),
    (tok_en, "en", "the cat"),
    (tok_fr, "fr", "château"),
]

for tok, lang, word in examples:
    tokens = tok.tokenize(word)
    segmented = " | ".join(t.grapheme for t in tokens)
    print(f"\n  [{lang}] {word!r}")
    print(f"    → {segmented}")


# ── 2. Token kinds ───────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("2. Token kinds")
print("=" * 60)

sentence = "the cat, too!"
tokens = tok_en.tokenize(sentence)
print(f"\n  [{sentence!r}]")
for t in tokens:
    marker = ""
    if t.kind == TokenKind.GRAPHEME:
        marker = "grapheme"
    elif t.kind == TokenKind.WHITESPACE:
        marker = "space"
    elif t.kind == TokenKind.PUNCTUATION:
        marker = "punct"
    elif t.kind == TokenKind.UNKNOWN:
        marker = "unknown"
    print(f"    {t.grapheme!r:6s}  {marker}")


# ── 3. IPA beam search ───────────────────────────────────────────────────

print("\n" + "=" * 60)
print("3. IPA beam search (all pronunciation candidates)")
print("=" * 60)

beam_examples = [
    (tok_en, "en", "through", 6),
    (tok_en, "en", "read",    4),
    (tok_pt, "pt", "chuva",   4),
    (tok_fr, "fr", "chat",    4),
]

for tok, lang, word, width in beam_examples:
    paths = tok.ipa_beam(word, beam_width=width)
    print(f"\n  [{lang}] {word!r}  (beam_width={width})")
    for path in paths:
        ipa_str = "".join(path.segments)
        print(f"    score={path.score:.1f}  /{ipa_str}/")


# ── 4. Allophone expansion ───────────────────────────────────────────────

print("\n" + "=" * 60)
print("4. Allophone expansion")
print("=" * 60)

# Without allophones: canonical IPA only
paths_no_allo = tok_en.ipa_beam("cat", beam_width=8, expand_allophones=False)
# With allophones: surface realisations included
paths_with_allo = tok_en.ipa_beam("cat", beam_width=8, expand_allophones=True)

print(f"\n  [en] 'cat'  without allophones ({len(paths_no_allo)} paths):")
for p in paths_no_allo:
    print(f"    /{''.join(p.segments)}/  score={p.score:.1f}")

print(f"\n  [en] 'cat'  with allophones ({len(paths_with_allo)} paths):")
for p in paths_with_allo:
    print(f"    /{''.join(p.segments)}/  score={p.score:.1f}")


# ── 5. Multi-language comparison ─────────────────────────────────────────

print("\n" + "=" * 60)
print("5. Same spelling, different sounds across Romance languages")
print("=" * 60)

# The letter sequence "ch" behaves very differently by language
word = "ch"
for lang_code, label in [("pt-PT", "pt-PT"), ("fr-FR", "fr-FR"), ("it-IT", "it-IT")]:
    spec = orthography2ipa.get(lang_code)
    tok = PhonetokTokenizer(spec)
    paths = tok.ipa_beam(word, beam_width=4)
    if paths:
        candidates = " / ".join("".join(p.segments) for p in paths)
        print(f"  [{label}] ⟨ch⟩  →  {candidates}")
    else:
        print(f"  [{label}] ⟨ch⟩  →  (no mapping)")
