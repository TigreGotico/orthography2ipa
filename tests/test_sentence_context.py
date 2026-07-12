"""Tests for the sentence-context seam (Workstream C4).

Covers:

- **Byte-identical default**: a no-op sentence rescorer and the absence of one
  both reproduce ``transcribe`` exactly, across a multi-word corpus sample.
- **Phrase / utterance position** correctness (initial / medial / final / sole)
  from punctuation-bounded phrases.
- The **two worked cross-word rescorers** (Arabic waṣl + pausal, French
  liaison) provably change the winner across a boundary — including a rewrite
  of the *right* word, which the legacy left-only ``SandhiEngine`` cannot do.
- **Determinism** and **composition** of a rescorer chain.
"""
import unicodedata

import pytest

from orthography2ipa import (
    G2P,
    Position,
    SentenceLattice,
    SentenceRescorer,
    WordSlot,
)
from orthography2ipa.sentence import (
    apply_sentence_rescorers,
    normalize_sentence_rescorers,
    span_position,
)


_VOWELS = set("aeiouɑɐɛɔøœyəɪʊæ")


# ─── helpers: toy rescorers (examples of the abstraction, not shipped data) ──

class _NoOp(SentenceRescorer):
    """Returns each word unchanged — must be byte-identical to no rescorer."""

    def rescore(self, word, context):
        return context.this_word_ipa


class WaslElision(SentenceRescorer):
    """Toy Arabic waṣl: a following word's initial *hamzat al-waṣl* (the
    definite article's ``a``) elides across a word boundary. Rewrites the
    **right** word using cross-word adjacency (there is a preceding word)."""

    def rescore(self, word, context):
        ipa = context.this_word_ipa
        if context.prev_word is not None and ipa.startswith("al"):
            return ipa[1:]  # drop the elided initial vowel
        return ipa


class PausalForm(SentenceRescorer):
    """Toy Arabic pausal: a phrase-final word takes its pausal citation form
    (here a toy glottal-stop close). Driven purely by phrase position."""

    def rescore(self, word, context):
        ipa = context.this_word_ipa
        if context.is_phrase_final and ipa and not ipa.endswith("ʔ"):
            return ipa + "ʔ"
        return ipa


class FrenchLiaison(SentenceRescorer):
    """Toy French liaison: a latent word-final consonant (orthographic
    ``s``/``x``/``z``) resyllabifies as the **next** word's onset before a
    vowel. Bidirectional: the left word marks the tie, the right word gains
    the onset — the resyllabification the legacy left-only engine cannot do."""

    LATENT = {"s", "x", "z"}

    def rescore(self, word, context):
        ipa = context.this_word_ipa
        # Right side: gain the /z/ onset if the previous word is latent and
        # this word begins with a vowel.
        prev = context.prev_word
        if (prev is not None and prev.surface[-1:].lower() in self.LATENT
                and ipa[:1] in _VOWELS):
            return "z" + ipa
        # Left side: mark the liaison tie if this word is latent and the next
        # word begins with a vowel.
        nxt = context.next_word
        if (word.surface[-1:].lower() in self.LATENT and nxt is not None
                and (context.next_word_ipa or "")[:1] in _VOWELS):
            return ipa + "‿"
        return ipa


# ─── byte-identical default ─────────────────────────────────────────────────

_CORPUS = [
    ("pt", "olá mundo bonito"),
    ("pt", "o gato preto, e o cão."),
    ("es-ES", "la casa grande"),
    ("fr", "les amis sont ici"),
    ("en-GB", "the quick brown fox"),
    ("ar", "الكتاب الجديد والقلم"),
]


@pytest.mark.parametrize("lang,text", _CORPUS)
def test_no_sentence_rescorer_is_unchanged(lang, text):
    """Constructing with no sentence rescorer changes nothing."""
    base = G2P(lang).transcribe(text)
    # Two engines built identically must agree (sanity), and the sentence
    # path is simply not invoked.
    assert G2P(lang).transcribe(text) == base


@pytest.mark.parametrize("lang,text", _CORPUS)
def test_noop_sentence_rescorer_is_byte_identical(lang, text):
    """A no-op sentence rescorer reproduces the default output exactly."""
    base = G2P(lang).transcribe(text)
    withnoop = G2P(lang, sentence_rescorer=_NoOp()).transcribe(text)
    assert withnoop == base


@pytest.mark.parametrize("lang,text", _CORPUS)
def test_sentence_lattice_ipa_matches_default_when_no_crossword(lang, text):
    """``sentence_lattice`` is a pure read: its per-word IPA join matches the
    default transcription for specs with no sandhi rules."""
    g = G2P(lang)
    sl = g.sentence_lattice(text)
    if g._sandhi is None:  # sandhi would legitimately diverge the join
        assert sl.ipa == g.transcribe(text)


# ─── phrase / utterance position ────────────────────────────────────────────

def test_phrase_and_utterance_positions():
    g = G2P("pt")
    sl = g.sentence_lattice("um dois, tres quatro cinco, seis")
    phrase = [w.phrase_position for w in sl]
    utt = [w.utterance_position for w in sl]
    # Phrases: [um dois] [tres quatro cinco] [seis]
    assert phrase == [
        Position.INITIAL, Position.FINAL,          # um dois
        Position.INITIAL, Position.MEDIAL, Position.FINAL,  # tres quatro cinco
        Position.SOLE,                             # seis
    ]
    # Utterance span over all six words.
    assert utt[0] == Position.INITIAL
    assert utt[-1] == Position.FINAL
    assert all(p == Position.MEDIAL for p in utt[1:-1])


def test_single_word_is_sole():
    sl = G2P("pt").sentence_lattice("olá")
    assert len(sl) == 1
    assert sl[0].phrase_position == Position.SOLE
    assert sl[0].utterance_position == Position.SOLE
    assert sl[0].pausal is True


def test_pausal_flag_equals_phrase_final():
    sl = G2P("pt").sentence_lattice("olá mundo, bonito")
    for w in sl:
        assert w.pausal == w.phrase_position.is_final()


def test_span_position_helper():
    assert span_position(0, 0, 1) == Position.SOLE
    assert span_position(0, 0, 3) == Position.INITIAL
    assert span_position(1, 0, 3) == Position.MEDIAL
    assert span_position(2, 0, 3) == Position.FINAL


def test_edge_slots_expose_adjacent_candidates():
    sl = G2P("pt").sentence_lattice("gato preto")
    w0, w1 = sl[0], sl[1]
    assert w0.final_slot is w0.slots[-1]
    assert w1.initial_slot is w1.slots[0]
    # A cross-word rule reaching across the boundary sees w1's onset slot.
    assert w1.initial_slot.grapheme == "p"


def test_empty_input():
    sl = G2P("pt").sentence_lattice("   ")
    assert len(sl) == 0
    assert sl.ipa == ""


# ─── worked example 1: Arabic waṣl + pausal ─────────────────────────────────

def test_arabic_wasl_and_pausal_change_winner_across_boundary():
    g_plain = G2P("ar")
    g_cross = G2P("ar", sentence_rescorer=[WaslElision(), PausalForm()])
    text = "الكتاب الجديد"

    plain = g_plain.transcribe(text)
    cross = g_cross.transcribe(text)
    assert plain != cross

    words = cross.split(" ")
    # (a) waṣl: the SECOND word lost its initial article vowel across the
    # boundary — a right-word rewrite driven by the preceding word.
    assert plain.split(" ")[1].startswith("al")
    assert not words[1].startswith("al")
    # (b) pausal: the phrase-FINAL word took its pausal form.
    assert words[1].endswith("ʔ")
    # The utterance-initial word is untouched (waṣl needs a preceding word).
    assert words[0] == plain.split(" ")[0]


def test_arabic_wasl_not_applied_utterance_initial():
    """The article on the first word must NOT elide (no preceding word)."""
    g = G2P("ar", sentence_rescorer=WaslElision())
    out = g.transcribe("الكتاب الجديد")
    assert out.split(" ")[0].startswith("al")


# ─── worked example 2: French liaison (bidirectional resyllabification) ──────

def test_french_liaison_attaches_onset_to_next_word():
    g_plain = G2P("fr")
    g_cross = G2P("fr", sentence_rescorer=FrenchLiaison())
    text = "les amis"

    plain = g_plain.transcribe(text)   # "lə ami"
    cross = g_cross.transcribe(text)
    assert plain != cross

    left, right = cross.split(" ")
    # The RIGHT word gained a /z/ onset — resyllabification across the
    # boundary, exactly what a left-only rewrite cannot express.
    assert right.startswith("z")
    assert not plain.split(" ")[1].startswith("z")
    # The left word marks the liaison tie.
    assert "‿" in left


def test_french_liaison_no_op_before_consonant():
    """No liaison when the following word does not begin with a vowel."""
    g = G2P("fr", sentence_rescorer=FrenchLiaison())
    plain = G2P("fr").transcribe("les gens")
    assert g.transcribe("les gens") == plain


# ─── determinism & composition ──────────────────────────────────────────────

def test_determinism():
    g = G2P("ar", sentence_rescorer=[WaslElision(), PausalForm()])
    text = "الكتاب الجديد والقلم"
    first = g.transcribe(text)
    for _ in range(5):
        assert g.transcribe(text) == first


def test_chain_composes_in_order():
    """Second pass sees the first pass's rewrite (waṣl then pausal)."""
    g = G2P("ar", sentence_rescorer=[WaslElision(), PausalForm()])
    sl = g.sentence_lattice("الكتاب الجديد")
    out = apply_sentence_rescorers(sl, [WaslElision(), PausalForm()])
    # word1: waṣl drops the 'a', then pausal appends 'ʔ' to that result.
    assert out[1].startswith("l") and out[1].endswith("ʔ")


def test_normalize_sentence_rescorers():
    assert normalize_sentence_rescorers(None) == ()
    one = _NoOp()
    assert normalize_sentence_rescorers(one) == (one,)
    assert normalize_sentence_rescorers([one, one]) == (one, one)
    with pytest.raises(TypeError):
        normalize_sentence_rescorers([object()])


def test_span_contract_nfc_span_preserved():
    """WordSlot lattice slots keep the SegmentSlot span/NFC contract."""
    text = "gato"
    sl = G2P("pt").sentence_lattice(text)
    w = sl[0]
    for s in w.slots:
        start, end = s.span
        assert unicodedata.normalize("NFC", w.surface)[start:end].lower() \
            == s.grapheme
