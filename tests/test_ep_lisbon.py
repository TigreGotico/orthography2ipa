"""Lisbon / Estremenho European Portuguese (pt-PT-x-lisbon) spec tests.

Lisbon is the prestige REFERENCE variety: Cintra (1971, Boletim de Filologia
22:81-116) shows the standard EP norm coincides with the Central-Southern
(Estremenho/Lisbon) variety, so the pt-PT base already models nearly all of
Lisbon. The genuine, well-sourced Lisbon deltas over that base are minimal:

  * <ei> -> [ɐj]   diagnostic diphthong lowering-centralisation
                   (Cintra 1971; Segura 2013; Mateus & d'Andrade 2000)
  * <ou> -> [o]    monophthongisation (Segura 2013)
  * /ʁ/ -> [ʁ]     uvular-fricative rhotic (narrowed allophone)

These tests assert the sourced deltas fire in context, that the base EP
processes are inherited unchanged, and that the <ei> rule does not over-apply.
"""
from __future__ import annotations

from orthography2ipa import G2P


def _bare(s: str) -> str:
    return s.replace("ˈ", "").replace("ˌ", "")


LISBON = "pt-PT-x-lisbon"
BASE = "pt-PT"
PORTO = "pt-PT-x-porto"


class TestEiLowering:
    """<ei> -> [ɐj], the single diagnostic grapheme-level Lisbon feature."""

    def test_leite(self):
        assert "ɐj" in _bare(G2P(LISBON).transcribe_word("leite"))

    def test_primeiro(self):
        assert "ɐj" in _bare(G2P(LISBON).transcribe_word("primeiro"))

    def test_reino(self):
        assert "ɐj" in _bare(G2P(LISBON).transcribe_word("reino"))

    def test_seis(self):
        assert "ɐj" in _bare(G2P(LISBON).transcribe_word("seis"))

    def test_diverges_from_northern_ej(self):
        """Lisbon lowers <ei> to [ɐj] where Porto/Northern EP keeps [ej]."""
        lisbon = _bare(G2P(LISBON).transcribe_word("leite"))
        porto = _bare(G2P(PORTO).transcribe_word("leite"))
        assert "ɐj" in lisbon
        assert "ej" in porto
        assert lisbon != porto


class TestOuMonophthong:
    """<ou> -> [o], complete monophthongisation."""

    def test_ouro(self):
        out = _bare(G2P(LISBON).transcribe_word("ouro"))
        assert "o" in out
        assert "ow" not in out


class TestInheritsBase:
    """Base EP processes are inherited unchanged, not restated in the spec."""

    def test_unstressed_a_reduces(self):
        # casa -> final unstressed /a/ -> [ɐ]
        assert _bare(G2P(LISBON).transcribe_word("casa")).endswith("ɐ")

    def test_unstressed_e_reduces(self):
        # menino -> pretonic /e/ -> [ɨ]
        assert "ɨ" in _bare(G2P(LISBON).transcribe_word("menino"))

    def test_dark_coda_l_inherited(self):
        # sol -> dark coda /l/ -> [ɫ] (PT_CODA_L_DARK inherited)
        assert "ɫ" in G2P(LISBON).transcribe_word("sol")

    def test_coda_sibilant_chiado_inherited(self):
        # seis -> coda /s/ -> [ʃ] (chiado inherited)
        assert G2P(LISBON).transcribe_word("seis").endswith("ʃ")


class TestNoOverApplication:
    """The <ei> rule fires only on the <ei> digraph, not on bare <e>/<i>."""

    def test_plain_e_not_lowered_to_aj(self):
        # 'pente' has no <ei>; must not gain a spurious [ɐj]
        assert "ɐj" not in _bare(G2P(LISBON).transcribe_word("pente"))

    def test_plain_i_unaffected(self):
        # 'vida' has a plain <i>; no [ɐj]
        assert "ɐj" not in _bare(G2P(LISBON).transcribe_word("vida"))
