"""Positional graphemes in the standalone tokenizer beam (B2).

The engine (:class:`~orthography2ipa.g2p.G2P`) and the standalone
tokenizer beam (:class:`~orthography2ipa.phonetok.PhonetokTokenizer`)
share one positional-resolution helper
(:mod:`orthography2ipa.positional`). These tests assert:

* **Parity** — for specs that declare ``positional_graphemes``,
  ``ipa_best`` equals ``transcribe_word`` per word (modulo the
  engine-only stress marks/sandhi/allophony), so the standalone beam is as accurate
  as the full engine.
* **Regression** — for specs *without* positional overrides the beam is
  unchanged: it still composes the first (canonical) IPA of each grapheme.
* the shared **resolver** applies exact>class>default precedence,
  including the vowel-class positions.
"""
import re
from dataclasses import replace

import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.positional import (
    grapheme_positions,
    positional_candidates,
    resolve_branches,
)
from orthography2ipa.registry import get
from orthography2ipa.types import GraphemePosition


_STRESS_RE = re.compile(r"[ˈˌ.]")


def _strip_stress(ipa: str) -> str:
    """Drop the engine-only stress/syllable marks for parity comparison."""
    return _STRESS_RE.sub("", ipa)


# ═══════════════════════════════════════════════════════════════════════════
# Parity: tokenizer beam == engine, per word, for positional specs
# ═══════════════════════════════════════════════════════════════════════════

# Words chosen so a positional rule actually fires:
#   es-ES: c/g before front vowel → θ/x; intervocalic b/d/g → β/ð/ɣ;
#          word-final d → ð; word-initial r → r.
#   pt-BR: intervocalic s → z; word-initial r → ʁ.
#   ca:    c/g softening before front vowels. Words are chosen WITHOUT
#          reducible unstressed vowels: Catalan unstressed reduction is
#          keyed to the stress-conditioned ⟨nucleus_unstressed⟩ position,
#          which — like stress marks, sandhi and allophony — is an
#          engine-only stage the stress-less tokenizer beam does not run
#          (see orthography2ipa.positional), so a word like "cosa" would
#          legitimately diverge (engine [kɔzə] vs beam [kɔza]).
_PARITY_CASES = {
    "es-ES": [
        "cena", "cielo", "gente", "girar", "hago", "lado", "abogado",
        "rosa", "casa", "gato", "cuna", "ciudad", "verdad",
    ],
    "pt-BR": ["casa", "mesa", "rosa", "rato", "peso", "asa"],
    "ca": ["cel", "gel", "cinc", "gent", "gat"],
}


@pytest.mark.parametrize("lang", sorted(_PARITY_CASES))
def test_beam_matches_engine_for_positional_specs(lang):
    spec = get(lang)
    assert spec.positional_graphemes, f"{lang} declares no positional rules"
    # Allophony (like sandhi/stress) is an engine-only post-lexical stage the
    # standalone tokenizer beam does not run, so disable it for the parity
    # comparison — parity is about shared *positional* resolution.
    engine = G2P(lang, apply_sandhi=False, apply_allophony=False)
    tok = PhonetokTokenizer(spec)
    for word in _PARITY_CASES[lang]:
        engine_ipa = _strip_stress(engine.transcribe_word(word))
        beam_ipa = _strip_stress(tok.ipa_best(word))
        assert beam_ipa == engine_ipa, (
            f"{lang} {word!r}: beam {beam_ipa!r} != engine {engine_ipa!r}")


def test_beam_now_applies_positions():
    """The standalone beam applies positional overrides (the B2 change).

    Without positional conditioning ⟨c⟩ in es-ES would take its flat
    candidate /k/; the beam must instead soften to /θ/ before ⟨e⟩ and
    voice intervocalic ⟨s⟩ → /z/ — exactly what the engine does.
    """
    tok = PhonetokTokenizer(get("es-ES"))
    assert tok.ipa_best("cena").startswith("θ")
    assert tok.ipa_best("hago") == "aɣo"
    tok_br = PhonetokTokenizer(get("pt-BR"))
    assert "z" in tok_br.ipa_best("casa")


# ═══════════════════════════════════════════════════════════════════════════
# Regression: specs without positional rules are unchanged
# ═══════════════════════════════════════════════════════════════════════════

def _flat_best(tok: PhonetokTokenizer, word: str) -> str:
    """The pre-B2 beam result: first (canonical) IPA of each grapheme."""
    return "".join(
        t.ipa[0] for t in tok.grapheme_tokens(word) if t.ipa)


@pytest.mark.parametrize("lang", ["eo", "af"])
def test_non_positional_spec_beam_unchanged(lang):
    spec = get(lang)
    assert not spec.positional_graphemes, f"{lang} unexpectedly has positions"
    assert not spec.grapheme_weights, f"{lang} unexpectedly has weights"
    tok = PhonetokTokenizer(spec)
    # Build words from the spec's own single-character graphemes so the
    # test is language-neutral; the beam must still just compose each
    # grapheme's canonical IPA (the pre-B2 behaviour).
    singles = [g for g in spec.graphemes if len(g) == 1 and g.isalpha()]
    words = ["".join(singles[i:i + 4]) for i in range(0, min(len(singles), 20), 4)]
    for word in words:
        assert tok.ipa_best(word) == _flat_best(tok, word)


# ═══════════════════════════════════════════════════════════════════════════
# Shared resolver: exact > class > default precedence (incl. vowel classes)
# ═══════════════════════════════════════════════════════════════════════════

def _c_spec(positional):
    """Synthetic spec: c→/k/ default plus the given positional block."""
    base = get("fr-FR")
    return replace(
        base,
        graphemes={
            "c": ["k"],
            "a": ["a"], "e": ["e"], "i": ["i"], "o": ["o"], "u": ["u"],
            "é": ["e"], "y": ["i"],
        },
        allophones={},
        positional_graphemes={"c": positional},
        stress=None,
        word_exceptions=None,
        sandhi_rules=(),
    )


def _ctx(spec, word, idx=0):
    seq = PhonetokTokenizer(spec).tokenize_with_context(word)
    return seq.graphemes[idx]


def test_grapheme_positions_order_exact_then_class_then_default():
    spec = _c_spec({})
    positions = grapheme_positions(_ctx(spec, "ce"))
    # ⟨c⟩ before ⟨e⟩: exact BEFORE_E, then class BEFORE_FRONT_VOWEL,
    # eventually DEFAULT — and exact precedes class precedes default.
    assert positions.index(GraphemePosition.BEFORE_E) \
        < positions.index(GraphemePosition.BEFORE_FRONT_VOWEL) \
        < positions.index(GraphemePosition.DEFAULT)
    # A back-vowel follower gets BEFORE_BACK_VOWEL, never BEFORE_FRONT_VOWEL.
    back = grapheme_positions(_ctx(spec, "ca"))
    assert GraphemePosition.BEFORE_BACK_VOWEL in back
    assert GraphemePosition.BEFORE_FRONT_VOWEL not in back


def test_positional_candidates_exact_beats_class():
    spec = _c_spec({
        GraphemePosition.BEFORE_E: ["ʃ"],
        GraphemePosition.BEFORE_FRONT_VOWEL: ["s"],
    })
    # ⟨e⟩: exact BEFORE_E wins.
    pos_e = grapheme_positions(_ctx(spec, "ce"))
    assert positional_candidates(spec, "c", pos_e) == ["ʃ"]
    # ⟨i⟩ (front, no exact rule): falls to the class rule.
    pos_i = grapheme_positions(_ctx(spec, "ci"))
    assert positional_candidates(spec, "c", pos_i) == ["s"]
    # ⟨é⟩ (accented front vowel): class rule via the vowel predicate.
    pos_acc = grapheme_positions(_ctx(spec, "cé"))
    assert positional_candidates(spec, "c", pos_acc) == ["s"]


def test_positional_candidates_falls_through_to_default():
    spec = _c_spec({
        GraphemePosition.BEFORE_FRONT_VOWEL: ["s"],
        GraphemePosition.DEFAULT: ["ɡ"],
    })
    # Back vowel: no front-class match → DEFAULT.
    pos_a = grapheme_positions(_ctx(spec, "ca"))
    assert positional_candidates(spec, "c", pos_a) == ["ɡ"]


def test_positional_candidates_none_when_no_entry():
    spec = _c_spec({GraphemePosition.BEFORE_FRONT_VOWEL: ["s"]})
    # ⟨a⟩ has no positional entry at all → None (caller uses flat table).
    pos = grapheme_positions(_ctx(spec, "ca", idx=1))
    assert positional_candidates(spec, "a", pos) is None


def test_resolve_branches_positional_winner_ranked_first():
    spec = _c_spec({GraphemePosition.BEFORE_FRONT_VOWEL: ["s"]})
    tok = PhonetokTokenizer(spec)
    branches = resolve_branches(
        spec, _ctx(spec, "ce"), weights_for=tok.weights_for)
    # Softened /s/ is the winner (cost 0); the flat /k/ alternative is
    # retained at a higher cost so the beam space is preserved.
    assert branches[0] == ("s", 0.0)
    assert ("k", 1.0) in branches
