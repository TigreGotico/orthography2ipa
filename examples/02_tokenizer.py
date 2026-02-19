"""
02_tokenizer.py — Using the PhonetokTokenizer for grapheme tokenization and IPA transcription.

Demonstrates:
- Tokenizing text with maximal-munch grapheme matching
- Inspecting Token objects
- Generating IPA transcription paths with beam search
- Handling digraphs, diphthongs, and multi-character graphemes
- Allophone expansion
- Mixed-content text (digits, punctuation, unknowns)
"""

import orthography2ipa
from orthography2ipa.phonetok import PhonetokTokenizer, TokenKind


# ── Helper ────────────────────────────────────────────────────────────────

def show_tokens(label: str, tok: PhonetokTokenizer, text: str) -> None:
    tokens = tok.tokenize(text)
    print(f"\n  Input: {text!r}")
    print(f"  {'Grapheme':10s}  {'Kind':12s}  IPA options")
    print("  " + "-" * 50)
    for t in tokens:
        ipa_str = " | ".join(t.ipa) if t.ipa else "(none)"
        print(f"  {t.grapheme!r:10s}  {t.kind.name:12s}  {ipa_str}")


def show_paths(label: str, tok: PhonetokTokenizer, text: str, beam_width: int = 6) -> None:
    paths = tok.ipa_beam(text, beam_width=beam_width)
    print(f"\n  IPA paths for {text!r}  (beam_width={beam_width}):")
    for i, path in enumerate(paths):
        segments = " ".join(path.segments)
        print(f"    [{i+1}] score={path.score:.1f}  /{path.ipa}/  ({segments})")


# ═══ Spanish ════════════════════════════════════════════════════════════════

print("=" * 65)
print("SPANISH (es)")
print("=" * 65)

es_tok = PhonetokTokenizer(orthography2ipa.get("es"))

show_tokens("ciudad", es_tok, "ciudad")
show_paths("ciudad", es_tok, "ciudad")

show_tokens("llave", es_tok, "llave")
show_paths("llave", es_tok, "llave")

show_tokens("rápido", es_tok, "rápido")
show_paths("rápido", es_tok, "rápido")

# Triphthong
show_paths("Uruguay", es_tok, "uruguay", beam_width=4)


# ═══ Portuguese (Brazilian) ═══════════════════════════════════════════════

print("\n" + "=" * 65)
print("PORTUGUESE — Brazilian (pt-BR)")
print("=" * 65)

pt_tok = PhonetokTokenizer(orthography2ipa.get("pt-BR"))

show_tokens("chuva", pt_tok, "chuva")
show_paths("chuva", pt_tok, "chuva")

show_tokens("lhano", pt_tok, "lhano")
show_paths("lhano", pt_tok, "lhano")

# Ambiguous ⟨x⟩ in Portuguese
show_tokens("exame", pt_tok, "exame")
show_paths("exame", pt_tok, "exame", beam_width=8)


# ═══ English ════════════════════════════════════════════════════════════════

print("\n" + "=" * 65)
print("ENGLISH (en)")
print("=" * 65)

en_tok = PhonetokTokenizer(orthography2ipa.get("en"))

show_tokens("thought", en_tok, "thought")
show_paths("thought", en_tok, "thought")

# High ambiguity word
show_paths("read", en_tok, "read", beam_width=6)

# Sentence with mixed content
print("\n  Mixed content:")
show_tokens("the cat sat.", en_tok, "the cat sat.")

# Digits and punctuation handling
print("\n  Text with digits:")
show_tokens("hay 3 gatos", PhonetokTokenizer(orthography2ipa.get("es")), "hay 3 gatos")


# ═══ French ════════════════════════════════════════════════════════════════

print("\n" + "=" * 65)
print("FRENCH (fr)")
print("=" * 65)

fr_tok = PhonetokTokenizer(orthography2ipa.get("fr"))

show_tokens("chat", fr_tok, "chat")
show_paths("chat", fr_tok, "chat")

show_paths("nuit", fr_tok, "nuit")


# ═══ German ════════════════════════════════════════════════════════════════

print("\n" + "=" * 65)
print("GERMAN (de)")
print("=" * 65)

de_tok = PhonetokTokenizer(orthography2ipa.get("de"))

show_tokens("Schule", de_tok, "schule")
show_paths("Schule", de_tok, "schule")

# sch must match before sc and s
show_tokens("sch vs sc vs s", de_tok, "schreiben")
show_paths("schreiben", de_tok, "schreiben", beam_width=4)


# ═══ Allophone expansion ═══════════════════════════════════════════════════

print("\n" + "=" * 65)
print("ALLOPHONE EXPANSION")
print("=" * 65)

es_tok2 = PhonetokTokenizer(orthography2ipa.get("es"))

print("\n  Spanish 'habla' — with vs. without allophones:")
paths_no_allo = es_tok2.ipa_beam("habla", beam_width=4, expand_allophones=False)
paths_with_allo = es_tok2.ipa_beam("habla", beam_width=8, expand_allophones=True)

print("  Without allophones:")
for p in paths_no_allo:
    print(f"    /{p.ipa}/  score={p.score:.1f}")

print("  With allophones:")
for p in paths_with_allo:
    print(f"    [{p.ipa}]  score={p.score:.1f}")


# ═══ Unknown characters ════════════════════════════════════════════════════

print("\n" + "=" * 65)
print("UNKNOWN CHARACTER HANDLING")
print("=" * 65)

en_tok2 = PhonetokTokenizer(orthography2ipa.get("en"))
tokens = en_tok2.tokenize("café☕")
print("\n  Tokenizing 'café☕':")
for t in tokens:
    status = "✓" if t.kind == TokenKind.GRAPHEME else "~"
    print(f"    {status} {t.kind.name:12s}  {t.grapheme!r}")
