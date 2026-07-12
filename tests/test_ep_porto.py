"""Porto / Baixo-Minho / Douro-Litoral European Portuguese (pt-PT-x-porto).

Verifies the Cintra (1971) diagnostic features modelled as ``allophone_rules``
deltas over the standard pt-PT parent:

  * Northern betacism  — /v/ ~ /b/ merger into [b] (Cintra feature 1).
  * Tonic-closed-vowel diphthongisation — stressed close [e] -> [je],
    close [o] -> [wo]/[wɔ] (Cintra's defining Porto marker, p.13), gated to
    the CLOSE mid vowels: genuinely open tonic [ɛ]/[ɔ] must NOT diphthongise.
  * Inheritance of the pt-PT base processes (dark coda /l/, coda-sibilant
    chiado) unchanged.

The open/close selection of a spelling-unmarked stressed <e>/<o> is lexical
and not predictable from orthography; the inherited pt-PT map defaults to the
OPEN allophone, so words with an underlying close vowel that the base engine
transcribes open (cedo, medo, Porto) are not reached by the diphthongisation
rule — a documented engine limit, asserted here so it stays intentional.
"""
from __future__ import annotations

from orthography2ipa import G2P


def _bare(s: str) -> str:
    return s.replace("ˈ", "").replace("ˌ", "")


ENG = G2P("pt-PT-x-porto")


# ─── Betacism (Cintra feature 1) ────────────────────────────────────────────

class TestBetacism:
    def test_vinho(self):
        assert ENG.transcribe_word("vinho") == "ˈbiɲu"

    def test_vaca(self):
        assert ENG.transcribe_word("vaca") == "ˈbakɐ"

    def test_v_medial_estava(self):
        # intervocalic /v/ also merges to [b]
        assert "b" in _bare(ENG.transcribe_word("estava"))
        assert "v" not in _bare(ENG.transcribe_word("estava"))


# ─── Tonic-closed-vowel diphthongisation (Cintra p.13) ──────────────────────

class TestDiphthongisationFires:
    """Fires on a STRESSED CLOSE mid vowel only."""

    def test_close_e_mes(self):
        assert ENG.transcribe_word("mês") == "ˈmjeʃ"

    def test_close_e_ele(self):
        assert ENG.transcribe_word("ele") == "ˈjelɨ"

    def test_close_e_este(self):
        assert _bare(ENG.transcribe_word("este")).startswith("je")

    def test_close_o_avo_circumflex(self):
        # avô (grandfather), close ô -> [o] -> [wo]
        assert ENG.transcribe_word("avô") == "ɐˈbwo"

    def test_close_o_por(self):
        assert ENG.transcribe_word("pôr") == "ˈpwoɾ"

    def test_close_o_ovo(self):
        assert _bare(ENG.transcribe_word("ovo")).startswith("wo")


class TestDiphthongisationGatedToClose:
    """Must NOT fire on genuinely OPEN tonic vowels [ɛ]/[ɔ]."""

    def test_open_e_pe(self):
        assert ENG.transcribe_word("pé") == "ˈpɛ"

    def test_open_e_cafe(self):
        assert ENG.transcribe_word("café") == "kɐˈfɛ"

    def test_open_o_avo(self):
        # avó (grandmother), open ó -> [ɔ], no diphthong
        assert ENG.transcribe_word("avó") == "ɐˈbɔ"

    def test_open_o_so(self):
        assert ENG.transcribe_word("só") == "ˈsɔ"

    def test_unstressed_close_e_not_diphthongised(self):
        # only the STRESSED nucleus diphthongises; pretonic/final stay reduced
        out = ENG.transcribe_word("verde")
        assert "je" not in _bare(out)


class TestOpenCloseEngineLimit:
    """Documented pre-lexical limit: words whose underlying vowel is close but
    which the base pt-PT map transcribes OPEN escape the (correctly close-gated)
    diphthongisation rule. Asserted so the limitation stays intentional, not a
    silent regression."""

    def test_porto_stays_open_monophthong(self):
        # emblematic dialectal form is [ˈpwoɾtu]; the base engine yields the
        # open monophthong because open/close is unpredictable from spelling.
        assert ENG.transcribe_word("Porto") == "ˈpɔɾtu"

    def test_cedo_stays_open_monophthong(self):
        assert ENG.transcribe_word("cedo") == "ˈsɛdu"


# ─── Inheritance from pt-PT base ────────────────────────────────────────────

class TestInheritsBase:
    def test_dark_coda_l_sol(self):
        assert ENG.transcribe_word("sol") == "ˈsɔɫ"

    def test_dark_coda_l_alto(self):
        assert "ɫ" in ENG.transcribe_word("alto")

    def test_coda_sibilant_chiado(self):
        # coda /s/ -> [ʃ] inherited from pt-PT (véspera)
        assert "ʃ" in ENG.transcribe_word("vespera")

    def test_ei_preserved(self):
        # Northern diphthong preservation: <ei> -> [ej] (not Lisbon [ɐj])
        out = _bare(ENG.transcribe_word("leite"))
        assert "ej" in out and "ɐj" not in out

    def test_ou_preserved(self):
        assert "ow" in _bare(ENG.transcribe_word("ouro"))
