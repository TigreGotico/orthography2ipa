"""Real-language application of the ``mutates_neighbor`` marker-grapheme
mechanism (see ``tests/test_allophone_mutates_neighbor.py`` for the
synthetic-spec mechanism tests, and ``docs/allophony.md`` "Marker
graphemes" for the write-up).

Manx (`gv`) vestigially preserves Goidelic slender/broad (caol/leathan)
marking: a written ⟨i⟩/⟨e⟩ can palatalize an adjacent consonant without
itself surfacing as a vowel (Broderick 1984-86; Thomson 1992). The two
cases cited in issue #743 are pinned here directly.
"""
from orthography2ipa import G2P
from orthography2ipa.g2p import G2P as G2PClass


def _ipa(word: str) -> str:
    return G2P("gv").transcribe_word(word)


def test_giare_onset_slender_marking():
    """The onset case: ⟨i⟩ between ⟨g⟩ and a vowel palatalizes ⟨g⟩ and
    does not itself surface (Broderick 1984-86; Thomson 1992, ch. 3)."""
    ipa = _ipa("giare")
    assert ipa.startswith("ɡʲ"), ipa
    assert "i" not in ipa.replace("ʲ", ""), ipa


def test_dowin_final_n_slender_marking():
    """The word-final case: ⟨i⟩ before a final ⟨n⟩ palatalizes the ⟨n⟩
    and does not itself surface."""
    ipa = _ipa("dowin")
    assert ipa.endswith("nʲ"), ipa


def test_apply_allophony_false_disables_slender_marking():
    """The ``apply_allophony`` toggle turns the whole pass off, exactly
    like every other allophone_rules spec."""
    ipa = G2PClass("gv", apply_allophony=False).transcribe_word("giare")
    assert ipa.startswith("ɡi") or ipa.startswith("ɡj") or "i" in ipa, ipa


def test_giat_and_gial_onset_slender_marking():
    """Two more Broderick/Thomson-cited onset slender forms."""
    assert _ipa("giat").startswith("ɡʲ")
    assert _ipa("gial").startswith("ɡʲ")
