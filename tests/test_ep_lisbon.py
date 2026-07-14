"""Lisbon / Estremenho European Portuguese (pt-PT-x-lisbon) spec tests.

Lisbon is a distinct Estremenho (Centro-Litoral) urban variety with its own
innovations over the conservative/neutral prescriptive norm (traditionally
anchored to educated central/Coimbra speech). The pt-PT base models the broad
descriptive EP standard; Lisbon is a delta on top via inheritance. The genuine,
well-sourced Lisbon deltas are:

  * stressed <e> -> [ɐ] before a palatal consonant  (coelho, fecho, venho,
                   abelha) — the signature Lisbon innovation, where the
                   conservative norm keeps [e]/[ɛ]
                   (Mateus & d'Andrade 2000; Cintra 1971)
  * <ei> -> [ɐj]   diagnostic diphthong lowering-centralisation
                   (Cintra 1971; Segura 2013; Mateus & d'Andrade 2000)
  * <ou> -> [o]    monophthongisation (Segura 2013)
  * /ʁ/ -> [ʁ]     uvular-fricative rhotic (narrowed allophone)

These tests assert the sourced deltas fire in context, that the base EP
processes are inherited unchanged, that the base is NOT mutated, and that the
pre-palatal and <ei> rules do not over-apply.
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


class TestStressedEPrePalatal:
    """Estremenho/Lisbon centralisation of stressed /e/ -> [ɐ] before a palatal
    consonant (coelho, espelho, fecho, venho, abelha). This is the signature
    Lisbon innovation over the conservative/central (Coimbra-type) norm, which
    keeps [e]/[ɛ] in this context. Modelled by the LX_STRESSED_E_PREPALATAL
    allophone rule (followed_by="palatal"), which fires only where the vowel
    still surfaces as [e]/[ɛ] — i.e. the stressed realisation — because
    unstressed /e/ has already reduced to [ɨ] before the post-lexical stage.
    """

    def test_coelho(self):
        # co-E-lho: stressed <e> before <lh> (ʎ) -> [ɐ]. The pretonic <o> is
        # unstressed and reduces to [u] like any other EP pretonic <o>, and
        # <oe> is HIATUS, so the mark sits on the stressed nucleus: kuˈɐʎu
        # (Mateus & d'Andrade 2000).
        assert G2P(LISBON).transcribe_word("coelho") == "kuˈɐʎu"

    def test_espelho(self):
        assert "ɐʎ" in G2P(LISBON).transcribe_word("espelho")

    def test_fecho(self):
        # stressed <e> before <ch> (ʃ) -> [ɐ]
        assert G2P(LISBON).transcribe_word("fecho") == "ˈfɐʃu"

    def test_venho(self):
        # stressed <e> before <nh> (ɲ) -> [ɐ]
        assert "ɐɲ" in G2P(LISBON).transcribe_word("venho")

    def test_abelha(self):
        assert "ɐʎ" in G2P(LISBON).transcribe_word("abelha")

    def test_diverges_from_central_norm(self):
        """Lisbon centralises stressed pre-palatal /e/ where the conservative
        central (Coimbra-type = pt-PT base) norm keeps the front mid vowel."""
        lisbon = G2P(LISBON).transcribe_word("coelho")
        base = G2P(BASE).transcribe_word("coelho")
        assert "ɐʎ" in lisbon          # Lisbon: [ˈkoɐʎu]
        assert "ɐʎ" not in base        # base keeps [ɛ]: [ˈkɔɛʎu]
        assert "ɛʎ" in base
        assert lisbon != base

    def test_unstressed_pre_palatal_e_not_centralised(self):
        """The rule is stress-gated: unstressed pretonic /e/ before a palatal
        has already reduced to [ɨ] and must NOT be centralised to [ɐ]."""
        # me-LHOR: pretonic <e> before <lh> stays reduced [ɨ]
        assert G2P(LISBON).transcribe_word("melhor") == "mɨˈʎoɾ"
        # fe-CHAR: pretonic <e> before <ch> stays reduced [ɨ]
        assert G2P(LISBON).transcribe_word("fechar") == "fɨˈʃaɾ"
        assert "ɐʃ" not in G2P(LISBON).transcribe_word("fechar")

    def test_stressed_e_before_non_palatal_unchanged(self):
        """Only pre-palatal stressed /e/ centralises; before a non-palatal the
        base stressed realisation [ɛ]/[e] is kept."""
        # 'belo': stressed <e> before <l> (non-palatal, non-nasal) -> [ɛ],
        # no centralisation. ('pente' would nasalise the vowel to [ẽ] via the
        # coda ⟨n⟩ and is not a clean pre-palatal control.)
        assert "ɐ" not in _bare(G2P(LISBON).transcribe_word("belo")).replace("ɾ", "")
        assert "ɛ" in G2P(LISBON).transcribe_word("belo")

    def test_base_pt_pt_untouched(self):
        """The delta lives on Lisbon only; the pt-PT base must not gain the
        pre-palatal centralisation."""
        assert G2P(BASE).transcribe_word("fecho") == "ˈfɛʃu"
        assert G2P(BASE).transcribe_word("venho") == "ˈvɛɲu"
