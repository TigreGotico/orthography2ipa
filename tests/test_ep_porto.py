"""Porto / Baixo-Minho / Douro-Litoral European Portuguese (pt-PT-x-porto).

Verifies the Cintra (1971) diagnostic features modelled as ``allophone_rules``
deltas over the standard pt-PT parent:

  * Northern betacism  — /v/ ~ /b/ merger into [b] (Cintra feature 1).
  * Tonic-vowel diphthongisation — stressed close [e] -> [je], close
    [o] -> [wo] (Cintra's defining Porto marker, p.13) AND, per Brissos
    (2018) / Brissos & Rodrigues (2016, AVOC + ALEPG/ALE), the OPEN mids
    [ɛ] -> [jɛ], [ɔ] -> [wɔ]: only the cardinal vowels stay stable.
  * Inheritance of the pt-PT base processes (dark coda /l/, coda-sibilant
    chiado) unchanged.

Widening to the open mids resolves the old pre-lexical limit: the open/close
selection of a spelling-unmarked stressed <e>/<o> is lexical and not
predictable from orthography, but whichever mid the base engine picks, the
stressed nucleus now diphthongises (to [je]/[wo] or [jɛ]/[wɔ]).
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


class TestOpenMidDiphthongisation:
    """The OPEN mids diphthongise too: [ɛ] -> [jɛ], [ɔ] -> [wɔ].

    Brissos (2018, pp.196-197, 200-201; reporting Brissos & Rodrigues 2016,
    AVOC + ALEPG/ALE) overturns the earlier close-mid-only view — NW tonic
    diphthongisation reaches the open mids as well ('[ˈpi̯ɛ] pé', '[ˈtu̯ɔkɨ]
    toque'), so only the cardinal vowels stay stable. Modelled as
    PT_PORTO_DIPHTHONGISE_E_OPEN/_O_OPEN.
    """

    def test_open_e_pe(self):
        assert ENG.transcribe_word("pé") == "ˈpjɛ"

    def test_open_e_cafe(self):
        assert ENG.transcribe_word("café") == "kɐˈfjɛ"

    def test_open_o_avo(self):
        # avó (grandmother), open ó -> [ɔ] -> [wɔ]
        assert ENG.transcribe_word("avó") == "ɐˈbwɔ"

    def test_open_o_so(self):
        assert ENG.transcribe_word("só") == "ˈswɔ"

    def test_unstressed_close_e_not_diphthongised(self):
        # only the STRESSED nucleus diphthongises; pretonic/final stay reduced
        out = ENG.transcribe_word("verde")
        assert "je" not in _bare(out)


class TestOpenMidResolvesTheOldLimit:
    """Widening to the open mids RESOLVES the earlier pre-lexical mis-selection
    limit: whichever mid the base engine picks for a spelling-unmarked stressed
    <e>/<o>, it now diphthongises. The emblematic Porto -> [ˈpwɔɾtu] (base
    mis-selects open [ɔ], but it now diphthongises, approaching the attested
    close [ˈpu̯oɾtu]); cedo -> [ˈsjɛdu]."""

    def test_porto_now_diphthongises(self):
        assert ENG.transcribe_word("Porto") == "ˈpwɔɾtu"

    def test_cedo_now_diphthongises(self):
        assert ENG.transcribe_word("cedo") == "ˈsjɛdu"


# ─── Inheritance from pt-PT base ────────────────────────────────────────────

class TestInheritsBase:
    def test_dark_coda_l_sol(self):
        # coda /l/ still velarises to [ɫ]; the stressed open [ɔ] now
        # diphthongises to [wɔ] (open-mid NW diphthongisation, Brissos 2018).
        assert ENG.transcribe_word("sol") == "ˈswɔɫ"

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
