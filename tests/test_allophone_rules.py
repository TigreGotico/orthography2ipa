"""Tests for the post-lexical allophone rule layer (Workstream B8).

The allophone layer is the *second* map: after orthography→phoneme
selection (positional_graphemes + weights), a spec's declarative
``allophone_rules`` rewrite a chosen phoneme to its context-conditioned
surface form. Rules compile into a
:class:`~orthography2ipa.rescorer.LatticeRescorer`
(:class:`~orthography2ipa.allophony.AllophoneRescorer`) run by the engine
after selection and before stress/sandhi.

These tests pin:

* the mechanism — a devoicing rule realises ``/d/ → [t]`` word-finally
  **only**, and an absent ``allophone_rules`` is byte-identical;
* each condition type (word position, coda via syllable_position, stress,
  neighbour grapheme class, neighbour phoneme) fires **only** in context;
* inheritance — a child spec inherits the parent's rules (id-keyed overlay)
  and can override one by id; the forcing-function manifest stays complete;
* composition with a user rescorer (B4);
* the ``apply_allophony`` toggle;
* the two Catalan pilots on gold-derived words.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.allophony import (
    AllophoneRescorer,
    compile_allophone_rescorer,
)
from orthography2ipa.g2p import G2P
from orthography2ipa.json_loader import _overlay_by_id
from orthography2ipa.phonetok import Candidate, PhonetokTokenizer
from orthography2ipa.rescorer import LatticeRescorer
from orthography2ipa.types import (
    FIELD_INHERITANCE,
    AllophoneRule,
    InheritanceMode,
    LanguageSpec,
    StressRules,
    fields_missing_inheritance_decision,
)


# ─── helpers ───────────────────────────────────────────────────────────

def _spec(graphemes, rules=(), *, stress=None, code="xx-test"):
    """A minimal synthetic LanguageSpec for a controlled experiment."""
    return LanguageSpec(
        code=code, name="Test", family="Test", script="Latin",
        graphemes=graphemes, allophones={}, allophone_rules=tuple(rules),
        stress=stress,
    )


def _tok_best(spec, word):
    """Tokenizer-path best transcription with the spec's rules applied."""
    tok = PhonetokTokenizer(spec)
    resc = compile_allophone_rescorer(spec.allophone_rules)
    return tok.ipa_best(word, rescorer=resc)


# ─── Mechanism: devoicing word-finally ONLY ────────────────────────────

def test_devoicing_realizes_only_word_final():
    rule = AllophoneRule(id="DEV_D", phonemes=("d",), surface="t",
                         word_final=True)
    spec = _spec({"a": ["a"], "d": ["d"]}, (rule,))
    # 'dad': first /d/ is not final (stays d), last /d/ devoices to t.
    assert _tok_best(spec, "dad") == "dat"
    # single word-final /d/ devoices; word-medial never.
    assert _tok_best(spec, "ad") == "at"
    assert _tok_best(spec, "da") == "da"


def test_absent_allophone_rules_byte_identical():
    plain = _spec({"a": ["a"], "d": ["d"]})  # no rules
    assert compile_allophone_rescorer(plain.allophone_rules) is None
    tok = PhonetokTokenizer(plain)
    for w in ("dad", "ad", "da", "aada"):
        assert tok.ipa_best(w) == tok.ipa_best(w, rescorer=None) == \
            _tok_best(plain, w)


# ─── Each condition type fires only in context ─────────────────────────

def test_word_initial_condition():
    rule = AllophoneRule(id="ASP", phonemes=("k",), surface="kʰ",
                         word_initial=True)
    spec = _spec({"a": ["a"], "k": ["k"]}, (rule,))
    assert _tok_best(spec, "ka") == "kʰa"   # initial k aspirates
    assert _tok_best(spec, "ak") == "ak"    # final k does not


def test_coda_via_syllable_position():
    rule = AllophoneRule(id="DARKL", phonemes=("l",), surface="ɫ",
                         syllable_position="coda")
    spec = _spec({"a": ["a"], "l": ["l"]}, (rule,))
    assert _tok_best(spec, "al") == "aɫ"    # coda l → dark
    assert _tok_best(spec, "la") == "la"    # onset l (before vowel) → clear


def test_neighbor_grapheme_class_flapping():
    # /t/ → [ɾ] between vowels (grapheme-class neighbour conditions).
    rule = AllophoneRule(id="FLAP", phonemes=("t",), surface="ɾ",
                         preceded_by="vowel", followed_by="vowel")
    spec = _spec({"a": ["a"], "t": ["t"]}, (rule,))
    assert _tok_best(spec, "ata") == "aɾa"  # intervocalic → flap
    assert _tok_best(spec, "ta") == "ta"    # onset, no preceding vowel
    assert _tok_best(spec, "at") == "at"    # coda, no following vowel


def test_neighbor_phoneme_condition_nasal_assimilation():
    # /n/ → [ŋ] before a velar phoneme (next slot's chosen phoneme).
    rule = AllophoneRule(id="NVEL", phonemes=("n",), surface="ŋ",
                         followed_by_phoneme=("k",))
    spec = _spec({"a": ["a"], "n": ["n"], "k": ["k"]}, (rule,))
    assert _tok_best(spec, "anka") == "aŋka"  # n before k → ŋ
    assert _tok_best(spec, "ana") == "ana"    # n before a → unchanged


def test_grapheme_source_condition():
    # A rule gated on the slot's SOURCE grapheme fires only for that
    # spelling, even when two graphemes map to the same phoneme. Here both
    # ⟨o⟩ and ⟨u⟩ realise as [u]; the rule lowers [u]→[o] only from ⟨o⟩.
    rule = AllophoneRule(id="SRC", phonemes=("u",), surface="o",
                         grapheme=("o",))
    spec = _spec({"o": ["u"], "u": ["u"], "t": ["t"]}, (rule,))
    assert _tok_best(spec, "to") == "to"   # ⟨o⟩→[u] lowered to [o]
    assert _tok_best(spec, "tu") == "tu"   # lexical ⟨u⟩→[u] untouched


def test_grapheme_source_condition_case_insensitive():
    rule = AllophoneRule(id="SRC", phonemes=("u",), surface="o",
                         grapheme=("o",))
    spec = _spec({"O": ["u"], "t": ["t"]}, (rule,))
    assert _tok_best(spec, "tO") == "to"


def test_stress_condition_fires_only_on_unstressed_engine_path():
    # Stress needs the engine's stress context. Use es-ES (has stress, does
    # not itself reduce), inject a synthetic 'unstressed /a/ → [ɐ]' rule and
    # confirm only the unstressed 'a' of "casa" (paroxytone: first syllable
    # stressed) is rewritten.
    eng = G2P("es-ES", apply_allophony=False)
    rule = AllophoneRule(id="RED_A", phonemes=("a",), surface="ɐ",
                         stress="unstressed")
    eng._rescorers = (AllophoneRescorer((rule,)),)
    out = eng.transcribe_word("casa")
    assert "ɐ" in out          # the unstressed final 'a' reduced
    assert out.count("a") >= 1  # the stressed 'a' stayed full


def test_stress_condition_inert_on_tokenizer_path():
    # No stress context on the standalone tokenizer → a stress-conditioned
    # rule never fires (documented parity with stress-conditioned positions).
    rule = AllophoneRule(id="RED_A", phonemes=("a",), surface="ɐ",
                         stress="unstressed")
    spec = _spec({"a": ["a"], "k": ["k"]}, (rule,))
    assert _tok_best(spec, "aka") == "aka"


# ─── Inheritance (OVERLAY_BY_ID, forcing-function) ─────────────────────

def test_field_inheritance_manifest_declares_allophone_rules():
    assert FIELD_INHERITANCE["allophone_rules"] is InheritanceMode.OVERLAY_BY_ID
    # forcing function: every LanguageSpec field has a decision.
    assert fields_missing_inheritance_decision() == frozenset()


def test_child_inherits_parent_allophone_rules():
    parent_ids = {r.id for r in get("ca").allophone_rules}
    assert parent_ids  # ca declares the pilots
    child_ids = {r.id for r in get("ca-x-balear").allophone_rules}
    # Balearic sets graphemes_base=ca and declares none of its own, so it
    # inherits the whole rule set through the id-keyed overlay edge.
    assert parent_ids <= child_ids


def test_overlay_by_id_replaces_in_place_and_appends():
    base = (
        AllophoneRule(id="A", phonemes=("d",), surface="t", word_final=True),
        AllophoneRule(id="B", phonemes=("n",), surface="ŋ",
                      followed_by_phoneme=("k",)),
    )
    own = (
        AllophoneRule(id="A", phonemes=("d",), surface="d"),  # override A
        AllophoneRule(id="C", phonemes=("z",), surface="s",
                      word_final=True),                        # append C
    )
    merged = _overlay_by_id(base, own)
    by_id = {r.id: r for r in merged}
    assert [r.id for r in merged] == ["A", "B", "C"]      # order preserved
    assert by_id["A"].surface == "d"                       # replaced in place
    assert by_id["B"].surface == "ŋ"                       # base kept


# ─── Composition with a user rescorer (B4) ─────────────────────────────

def test_composition_with_user_rescorer():
    class PromoteK(LatticeRescorer):
        """Force grapheme 'c' to realise /k/ (not /s/)."""
        def rescore(self, slot, context):
            if slot.grapheme != "c":
                return slot.candidates
            best = min(x.cost for x in slot.candidates)
            return [Candidate("k", best - 1.0)] + [
                x for x in slot.candidates if x.ipa != "k"]

    # A spec where 'c' → /k s/ and a devoicing rule /k/→… no; use a rule that
    # rewrites the promoted /k/ so we can see the two compose in order.
    rule = AllophoneRule(id="KFINAL", phonemes=("k",), surface="q",
                         word_final=True)
    spec = _spec({"a": ["a"], "c": ["s", "k"]}, (rule,), code="yy-test")
    tok = PhonetokTokenizer(spec)
    allo = compile_allophone_rescorer(spec.allophone_rules)
    # User rescorer promotes 'c'→/k/; then allophony rewrites word-final /k/→q.
    assert tok.ipa_best("ac", rescorer=[PromoteK(), allo]) == "aq"
    # Order matters: allophony first sees /s/ on top (no /k/), so no rewrite.
    assert tok.ipa_best("ac", rescorer=[allo, PromoteK()]) == "ak"


# ─── apply_allophony toggle ────────────────────────────────────────────

def test_apply_allophony_toggle():
    on = G2P("ca")                        # default True
    off = G2P("ca", apply_allophony=False)
    assert on._allophone_rescorer is not None
    assert off._allophone_rescorer is None
    # 'fred' devoices word-final /d/ → [t] only when allophony is on.
    assert on.transcribe_word("fred").endswith("t")
    assert off.transcribe_word("fred").endswith("d")


def test_apply_allophony_noop_for_spec_without_rules():
    # A spec that declares no rules is unaffected by the (default-on) toggle.
    assert G2P("es-ES")._allophone_rescorer is None
    assert G2P("pt").transcribe("casa") == \
        G2P("pt", apply_allophony=False).transcribe("casa")


# ─── Catalan pilots on gold-derived words ──────────────────────────────

@pytest.mark.parametrize("word,expected_final", [
    ("fred", "t"),   # /d/# → [t]  (Wheeler 2005 §5.3)
    ("verd", "t"),
    ("club", "p"),   # /b/# → [p]
])
def test_pilot_catalan_final_devoicing(word, expected_final):
    assert G2P("ca").transcribe_word(word).endswith(expected_final)
    # broad/phonemic output keeps the underlying voiced obstruent.
    assert not G2P("ca", apply_allophony=False).transcribe_word(
        word).endswith(expected_final)


def test_catalan_final_ng_is_velar_nasal_not_devoiced_stop():
    """⟨-ng⟩ is [ŋ], not a devoiced [k].

    Final-cluster simplification deletes the stop of a final nasal+stop
    cluster BEFORE devoicing can apply to it, so ⟨sang⟩ is [ˈsaŋ] and
    ⟨fang⟩ [ˈfaŋ] (Wheeler 2005 §10.4) — a final [k] there would be an
    artefact of running the devoicing rule on a stop that is not
    pronounced at all.
    """
    assert G2P("ca").transcribe_word("sang") == "ˈsaŋ"
    assert G2P("ca").transcribe_word("fang") == "ˈfaŋ"


@pytest.mark.parametrize("word", ["banc", "sang", "fang"])
def test_pilot_catalan_nasal_velar_assimilation(word):
    # /n/ → [ŋ] before a velar (Recasens 1993).
    out = G2P("ca").transcribe_word(word)
    assert "ŋ" in out
    assert "ŋ" not in G2P("ca", apply_allophony=False).transcribe_word(word)


def test_pilot_catalan_nasal_palatal_assimilation():
    """/n/ → [ɲ] before a palato-alveolar, not [ŋ].

    ⟨àngel⟩ is [ˈaɲʒəl]: ⟨g⟩ before a front vowel is /ʒ/, so the nasal
    assimilates to the palato-alveolar place, not to a velar that is not
    there (Recasens 1993; Wheeler 2005 §10.3).
    """
    assert G2P("ca").transcribe_word("àngel") == "ˈaɲʒəl"


class TestConsonantClusterContext:
    """The ``consonant_cluster`` neighbour class.

    A cluster is two or more consonant segments read away from the anchor.
    It is what closed-syllable shortening needs, and it is stated over
    phonological classes only — enumerating the clusters as graphemes is a
    design violation, so the engine has to be able to see them.
    """

    def test_fires_before_two_consonants(self):
        from orthography2ipa.allophony import _begins_consonant_cluster
        from orthography2ipa.phonetok import PhonetokTokenizer

        spec = get("sv")
        tok = PhonetokTokenizer(spec)

        def cluster_after(word: str, index: int) -> bool:
            ctxs = [c for c in tok.tokenize_with_context(word)]
            nxt = ctxs[index].next
            return nxt is not None and _begins_consonant_cluster(nxt, 1)

        # ⟨i⟩ in "vitt" is followed by the geminate ⟨tt⟩ → a cluster
        assert cluster_after("vitt", 1) is True
        # ⟨i⟩ in "vit" is followed by a single ⟨t⟩ → not a cluster
        assert cluster_after("vit", 1) is False

    def test_open_syllable_keeps_the_long_vowel(self):
        # The rule must not fire when a single consonant is followed by a vowel
        assert "iː" in G2P("sv").transcribe_word("vit")
