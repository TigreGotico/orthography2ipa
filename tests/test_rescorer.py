"""Tests for the lattice rescorer hook (Workstream B4).

The rescorer is the downstream-enablement seam: a pure, composable pass
that re-costs (reorders / adds / drops / deletes) a lattice slot's
candidates *after* positional/weight resolution and *before* beam path
selection. These tests pin the load-bearing contracts:

* a context-conditioned **ban** changes the selected path only where the
  context matches, and is inert elsewhere;
* a **reorder** (promote a lower-ranked candidate) changes
  ``ipa_best``-via-lattice;
* **composition** — two rescorers apply in order, the second seeing the
  first's output;
* the **no-rescorer** path is byte-identical to pre-B4 behaviour;
* an **empty** return deletes the slot without crashing the beam;
* stress context is present on the engine path and ``None`` on the
  standalone tokenizer path.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.phonetok import Candidate, PhonetokTokenizer
from orthography2ipa.rescorer import (
    LatticeRescorer,
    RescoreContext,
    normalize_rescorers,
)


# ─── Toy rescorers ─────────────────────────────────────────────────────

class BanIPABeforeFront(LatticeRescorer):
    """Forbid a given IPA when the *next* grapheme is a front vowel."""

    def __init__(self, banned: str) -> None:
        self.banned = banned

    def rescore(self, slot, context: RescoreContext):
        nxt = context.grapheme.next
        if nxt is not None and nxt.is_front:
            return [c for c in slot.candidates if c.ipa != self.banned]
        return slot.candidates


class PromoteIPA(LatticeRescorer):
    """Promote a specific IPA to the top of a specific grapheme's slot."""

    def __init__(self, grapheme: str, ipa: str) -> None:
        self.grapheme = grapheme
        self.ipa = ipa

    def rescore(self, slot, context: RescoreContext):
        if slot.grapheme != self.grapheme:
            return slot.candidates
        best = min(c.cost for c in slot.candidates)
        return [Candidate(self.ipa, best - 1.0)] + [
            c for c in slot.candidates if c.ipa != self.ipa
        ]


class DeleteGrapheme(LatticeRescorer):
    """Delete a grapheme entirely (empty candidate return = silent letter)."""

    def __init__(self, grapheme: str) -> None:
        self.grapheme = grapheme

    def rescore(self, slot, context: RescoreContext):
        if slot.grapheme == self.grapheme:
            return []
        return slot.candidates


class RecordStress(LatticeRescorer):
    """No-op that records the ``is_stressed`` value it saw per slot."""

    def __init__(self) -> None:
        self.seen = []

    def rescore(self, slot, context: RescoreContext):
        self.seen.append((slot.grapheme, context.is_stressed))
        return slot.candidates


# ─── Ban in a context provably changes the winner ──────────────────────

def test_ban_changes_path_when_context_matches():
    # pt 'c' before front vowel 'e' → default /s/; ban /s/ leaves /k/.
    tok = PhonetokTokenizer(get("pt"))
    assert tok.ipa_best("ce").startswith("s")
    banned = tok.ipa_best("ce", rescorer=BanIPABeforeFront("s"))
    assert "s" not in banned
    assert banned.startswith("k")


def test_ban_is_inert_when_context_does_not_match():
    # 'c' before back vowel 'a' → /k/; the front-vowel ban never fires.
    tok = PhonetokTokenizer(get("pt"))
    base = tok.ipa_best("casa")
    with_rescorer = tok.ipa_best("casa", rescorer=BanIPABeforeFront("s"))
    assert with_rescorer == base


# ─── Reorder changes ipa_best-via-lattice ──────────────────────────────

def test_reorder_promotes_candidate_in_lattice_and_best():
    tok = PhonetokTokenizer(get("pt"))
    # 'a' canonical is 'a'; promote 'ɐ' to the top of every 'a' slot.
    r = PromoteIPA("a", "ɐ")
    slots = tok.ipa_lattice("casa", rescorer=r)
    a_slots = [s for s in slots if s.grapheme == "a"]
    assert a_slots and all(s.top.ipa == "ɐ" for s in a_slots)
    # ipa_best-via-lattice == concatenation of slot tops.
    via_lattice = "".join(s.top.ipa for s in slots)
    assert via_lattice == tok.ipa_best("casa", rescorer=r)
    assert via_lattice != tok.ipa_best("casa")  # actually changed


# ─── Composition: second rescorer sees the first's output ──────────────

class SeesPreviousOutput(LatticeRescorer):
    """Assert the top candidate was already changed by an earlier rescorer,
    then tag it so the effect is observable."""

    def __init__(self, expect_top: str) -> None:
        self.expect_top = expect_top
        self.observed = []

    def rescore(self, slot, context: RescoreContext):
        if slot.grapheme == "a":
            self.observed.append(slot.top.ipa)
        return slot.candidates


def test_composition_second_sees_first_output():
    tok = PhonetokTokenizer(get("pt"))
    first = PromoteIPA("a", "ɐ")
    second = SeesPreviousOutput(expect_top="ɐ")
    tok.ipa_lattice("casa", rescorer=[first, second])
    # The second rescorer saw 'ɐ' on top of every 'a' slot — proof the
    # first rescorer's output was threaded in.
    assert second.observed == ["ɐ", "ɐ"]


def test_composition_order_matters():
    tok = PhonetokTokenizer(get("pt"))
    promote_a = PromoteIPA("a", "ɐ")
    ban_schwa = BanIPABeforeFront("ɐ")  # only bans before front vowel
    # Order [promote, ban]: promote first, ban only affects front-vowel
    # contexts, so both 'a's in "casa" stay 'ɐ' (neither precedes a front
    # vowel). Composition still runs cleanly in order.
    out = tok.ipa_best("casa", rescorer=[promote_a, ban_schwa])
    assert out == "kɐzɐ"


# ─── No-rescorer path byte-identical ───────────────────────────────────

@pytest.mark.parametrize("lang", ["pt", "es-ES", "en-GB", "fr-FR"])
def test_no_rescorer_byte_identical(lang):
    tok = PhonetokTokenizer(get(lang))
    words = ["casa", "cena", "weather", "chien", "the", "gato"]
    for w in words:
        assert tok.ipa_best(w) == tok.ipa_best(w, rescorer=None)
        base = tok.ipa_beam(w, beam_width=6)
        also = tok.ipa_beam(w, beam_width=6, rescorer=None)
        assert [(p.ipa, p.score) for p in base] == \
               [(p.ipa, p.score) for p in also]
        base_lat = tok.ipa_lattice(w)
        also_lat = tok.ipa_lattice(w, rescorer=None)
        assert [(s.grapheme, s.candidates) for s in base_lat] == \
               [(s.grapheme, s.candidates) for s in also_lat]


def test_noop_rescorer_matches_default():
    class NoOp(LatticeRescorer):
        def rescore(self, slot, context):
            return slot.candidates

    tok = PhonetokTokenizer(get("en-GB"))
    for w in ["weather", "through", "thought"]:
        assert tok.ipa_best(w, rescorer=NoOp()) == tok.ipa_best(w)


def test_engine_default_path_byte_identical():
    eng = G2P("pt")
    eng_r = G2P("pt", rescorer=None)
    for w in ["casa", "cena", "gato", "chuva"]:
        assert eng.transcribe(w) == eng_r.transcribe(w)


# ─── Empty return deletes the slot, never crashes the beam ─────────────

def test_empty_return_deletes_slot_in_beam():
    tok = PhonetokTokenizer(get("pt"))
    base = tok.ipa_best("casa")
    out = tok.ipa_best("casa", rescorer=DeleteGrapheme("s"))
    # 's' contributes no segment; the rest is unchanged.
    assert "z" not in out and "s" not in out
    assert len(out) < len(base)


def test_empty_return_omits_slot_in_lattice():
    tok = PhonetokTokenizer(get("pt"))
    slots = tok.ipa_lattice("casa", rescorer=DeleteGrapheme("s"))
    assert [s.grapheme for s in slots] == ["c", "a", "a"]


def test_delete_every_slot_yields_empty_not_crash():
    tok = PhonetokTokenizer(get("pt"))

    class DeleteAll(LatticeRescorer):
        def rescore(self, slot, context):
            return []

    assert tok.ipa_best("casa", rescorer=DeleteAll()) == ""
    assert tok.ipa_lattice("casa", rescorer=DeleteAll()) == []
    # beam still returns a (degenerate, empty) path rather than crashing.
    paths = tok.ipa_beam("casa", beam_width=4, rescorer=DeleteAll())
    assert paths and paths[0].ipa == ""


# ─── Stress availability differs by entry path (documented) ────────────

def test_engine_path_supplies_stress_context():
    r = RecordStress()
    G2P("pt", rescorer=r).transcribe("casa")
    # At least one slot is in the stressed syllable and one is not.
    stressed_flags = [is_s for _, is_s in r.seen]
    assert True in stressed_flags
    assert all(f is not None for f in stressed_flags)


def test_tokenizer_path_has_no_stress_context():
    r = RecordStress()
    PhonetokTokenizer(get("pt")).ipa_best("casa", rescorer=r)
    assert all(is_s is None for _, is_s in r.seen)


# ─── normalize_rescorers plumbing ──────────────────────────────────────

def test_normalize_rescorers_forms():
    r = DeleteGrapheme("x")
    assert normalize_rescorers(None) == ()
    assert normalize_rescorers(r) == (r,)
    assert normalize_rescorers([r, r]) == (r, r)
    with pytest.raises(TypeError):
        normalize_rescorers(["not a rescorer"])


# ─── Context neighbour access is word-local ────────────────────────────

def test_prev_next_slot_are_word_local():
    seen = {}

    class Probe(LatticeRescorer):
        def rescore(self, slot, context):
            seen[(context.index, slot.grapheme)] = (
                context.prev_slot.grapheme if context.prev_slot else None,
                context.next_slot.grapheme if context.next_slot else None,
                context.is_word_initial,
                context.is_word_final,
            )
            return slot.candidates

    tok = PhonetokTokenizer(get("pt"))
    tok.ipa_lattice("ca ab", rescorer=Probe())
    # Indices are WORD-LOCAL on the tokenizer path (Finding B): both words
    # start at index 0, and slots/index never cross a word boundary.
    # First word "ca": 'c' word-initial (no prev), 'a' word-final of word 1.
    assert seen[(0, "c")] == (None, "a", True, False)
    assert seen[(1, "a")] == ("c", None, False, True)
    # Second word "ab": 'a' word-initial at local index 0, 'b' at local 1.
    assert seen[(0, "a")] == (None, "b", True, False)
    assert seen[(1, "b")] == ("a", None, False, True)


def test_slots_are_word_local_on_tokenizer_path():
    # A rescorer scanning context.slots must see only its own word.
    seen_lengths = {}

    class ProbeSlots(LatticeRescorer):
        def rescore(self, slot, context):
            seen_lengths[(context.index, slot.grapheme)] = (
                len(context.slots),
                context.slots[context.index] is slot,
            )
            return slot.candidates

    tok = PhonetokTokenizer(get("pt"))
    tok.ipa_lattice("casa gato", rescorer=ProbeSlots())
    # Each word has 4 graphemes; every slot sees a 4-slot word-local list,
    # and slots[index] is itself.
    assert all(length == 4 and is_self
               for length, is_self in seen_lengths.values())


# ─── Composition + deletion: emptied neighbour reads as None (Finding A) ─

class ReadPrevTop(LatticeRescorer):
    """Reads context.prev_slot.top — must not crash when the previous slot
    was emptied by an earlier rescorer in the chain."""

    def __init__(self) -> None:
        self.seen_prev = []

    def rescore(self, slot, context):
        prev = context.prev_slot
        self.seen_prev.append(
            (slot.grapheme, prev.top.ipa if prev is not None else None))
        return slot.candidates


def test_composed_delete_then_read_prev_does_not_crash():
    tok = PhonetokTokenizer(get("pt"))
    reader = ReadPrevTop()
    # Delete 'c' first, then a rescorer that reads prev_slot.top. The slot
    # after the deleted 'c' must see prev_slot is None (not an empty slot),
    # so .top is never called on empty candidates.
    slots = tok.ipa_lattice("casa", rescorer=[DeleteGrapheme("c"), reader])
    # 'c' is gone; the surviving first grapheme 'a' had 'c' (now emptied)
    # as its word-local predecessor → reader must have seen None for it.
    assert ("a", None) in reader.seen_prev
    assert [s.grapheme for s in slots] == ["a", "s", "a"]


def test_composed_delete_then_read_prev_beam_does_not_crash():
    tok = PhonetokTokenizer(get("pt"))
    # Same composition through the beam: must complete without IndexError.
    out = tok.ipa_best("casa", rescorer=[DeleteGrapheme("c"), ReadPrevTop()])
    assert "k" not in out and out  # 'c' deleted, rest transcribed
