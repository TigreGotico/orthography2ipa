"""Regression tests for lij (Ligurian / Genoese) language data.

The spec models the standardised *grafia ofiçiâ* of the Académia Ligùstica
do Brénno (the orthography of the Ligurian Wikipedia). Tests cover the
hallmark Genoese grapheme->IPA correspondences, whole words from the
grafia with their documented pronunciation, the velar-nasal / vowel-
nasalisation allophone layer, and accent-marked stress.

Two levels:
- spec.graphemes / spec.resolve_grapheme(): the grapheme table.
- orthography2ipa.transcribe(): the full engine (positional + allophony +
  stress). PhonetokTokenizer.ipa_best() is the flat (context-free) path.
"""
import pytest

import orthography2ipa
from orthography2ipa.types import GraphemePosition, QualityTier
from orthography2ipa.phonetok import PhonetokTokenizer


@pytest.fixture(scope="module")
def lij():
    return orthography2ipa.get("lij")


@pytest.fixture(scope="module")
def tok(lij):
    return PhonetokTokenizer(lij)


# ---------------------------------------------------------------------------
# Registry / tier
# ---------------------------------------------------------------------------

class TestRegistry:
    def test_loads(self, lij):
        assert lij is not None
        assert lij.code == "lij"

    def test_name(self, lij):
        assert lij.name == "Ligurian"

    def test_family(self, lij):
        assert {"Indo-European", "Romance"} <= set(lij.family_path)

    def test_in_available_codes(self):
        assert "lij" in orthography2ipa.available_codes()

    def test_research_tier(self, lij):
        assert lij.quality is QualityTier.RESEARCH

    def test_has_sources(self, lij):
        ids = {s.id for s in lij.sources}
        assert "academia_grafia_oficia" in ids
        assert "toso1997_grammatica" in ids
        assert len(lij.sources) >= 2

    def test_has_stress_block(self, lij):
        assert lij.stress is not None


# ---------------------------------------------------------------------------
# Hallmark grapheme->IPA correspondences (grafia ofiçiâ)
# ---------------------------------------------------------------------------

class TestHallmarkGraphemes:
    def test_x_is_zh(self, lij):
        """The diagnostic Genoese grapheme: x = /ʒ/ (French j)."""
        assert lij.graphemes.get("x") == ["ʒ"]

    def test_o_is_u(self, lij):
        """Genoese o = /u/ (Italian u)."""
        assert lij.graphemes.get("o") == ["u"]

    def test_u_is_front_rounded_y(self, lij):
        """u = /y/ (front rounded)."""
        assert lij.graphemes.get("u") == ["y"]

    def test_eu_is_front_rounded_o(self, lij):
        """eu = /ø/."""
        assert lij.graphemes.get("eu") == ["ø"]

    def test_scc_trigraph(self, lij):
        """scc = /ʃtʃ/."""
        assert lij.graphemes.get("scc") == ["ʃtʃ"]

    def test_velar_nasal_digraphs(self, lij):
        """n- and nn- = the velar nasal /ŋ/."""
        assert lij.graphemes.get("n-") == ["ŋ"]
        assert lij.graphemes.get("nn-") == ["ŋ"]

    def test_ae_ligature(self, lij):
        """æ = /ɛː/."""
        assert lij.graphemes.get("æ") == ["ɛː"]

    def test_c_cedilla_is_s(self, lij):
        """ç = /s/."""
        assert lij.graphemes.get("ç") == ["s"]

    def test_z_is_voiced_fricative(self, lij):
        """z = /z/ always (NOT an affricate)."""
        assert lij.graphemes.get("z") == ["z"]

    def test_o_grave_is_open_o(self, lij):
        """ò = /ɔ/ (contrasts with o = /u/)."""
        assert lij.graphemes.get("ò") == ["ɔ"]

    def test_long_vowels_circumflex(self, lij):
        """Circumflex encodes length: â=/aː/, ê=/eː/, î=/iː/, ô=/uː/, û=/yː/."""
        assert lij.graphemes.get("â") == ["aː"]
        assert lij.graphemes.get("ô") == ["uː"]
        assert lij.graphemes.get("û") == ["yː"]


# ---------------------------------------------------------------------------
# Degemination (double consonant -> single phoneme)
# ---------------------------------------------------------------------------

class TestDegemination:
    def test_tt(self, lij):
        assert lij.graphemes.get("tt") == ["t"]

    def test_ss(self, lij):
        assert lij.graphemes.get("ss") == ["s"]

    def test_word_degemination(self, tok):
        """xatta 'cat' -> ʒata (x=ʒ + total degemination of tt)."""
        assert tok.ipa_best("xatta") == "ʒata"


# ---------------------------------------------------------------------------
# Positional c/g/sc softening (before a front vowel)
# ---------------------------------------------------------------------------

class TestPositional:
    def test_c_soft(self, lij):
        assert lij.resolve_grapheme("c", GraphemePosition.BEFORE_FRONT_VOWEL) == ["tʃ"]

    def test_c_hard(self, lij):
        assert lij.resolve_grapheme("c", None) == ["k"]

    def test_g_soft(self, lij):
        assert lij.resolve_grapheme("g", GraphemePosition.BEFORE_FRONT_VOWEL) == ["dʒ"]

    def test_sc_soft(self, lij):
        assert lij.resolve_grapheme("sc", GraphemePosition.BEFORE_FRONT_VOWEL) == ["ʃ"]


# ---------------------------------------------------------------------------
# Whole words through the full engine (positional + allophony + stress)
# ---------------------------------------------------------------------------

class TestWords:
    def test_xatta(self):
        """x -> ʒ, degemination, paroxytone stress."""
        assert orthography2ipa.transcribe("xatta", "lij") == "ˈʒata"

    def test_cittae(self):
        """çittæ 'city': ç=/s/, æ=/ɛː/ carries stress."""
        assert orthography2ipa.transcribe("çittæ", "lij") == "siˈtɛː"

    def test_scciappa(self):
        """scciappâ: scc=/ʃtʃ/, â=/aː/ stressed and long."""
        assert orthography2ipa.transcribe("scciappâ", "lij") == "ʃtʃiaˈpaː"

    def test_gexa_church(self):
        """gexa 'church': g soft = dʒ, x = ʒ."""
        assert orthography2ipa.transcribe("gexa", "lij") == "ˈdʒeʒa"

    def test_buttega(self):
        """buttega 'shop': u=/y/, degemination, default penult stress."""
        assert orthography2ipa.transcribe("buttega", "lij") == "byˈteɡa"


class TestSilentI:
    """The palatal-marker ⟨i⟩ in ⟨ci⟩/⟨gi⟩ before a back vowel is silent."""

    def test_ciu_silent_i(self):
        """ciù -> [tʃy]: the i marks the affricate and does not surface."""
        assert orthography2ipa.transcribe("ciù", "lij") == "ˈtʃy"

    def test_giorna_silent_i(self):
        """giornâ -> [dʒurnaː]: g soft = dʒ, silent i, o=/u/, â long stressed."""
        assert orthography2ipa.transcribe("giornâ", "lij") == "dʒuˈrnaː"

    def test_cio_silent_i(self):
        """cio -> [tʃu]: silent i, o=/u/."""
        assert orthography2ipa.transcribe("cio", "lij") == "ˈtʃu"

    def test_i_kept_before_consonant(self):
        """cina -> [tʃina]: before a consonant the i is a real vowel, kept."""
        assert orthography2ipa.transcribe("cina", "lij") == "ˈtʃina"

    def test_ci_digraph_table(self, lij):
        assert lij.graphemes.get("ciù") == ["tʃy"]
        assert lij.graphemes.get("gio") == ["dʒu"]


# ---------------------------------------------------------------------------
# Post-lexical allophony: velar nasal + vowel nasalisation (B8 rules)
# ---------------------------------------------------------------------------

class TestAllophony:
    def test_rules_present(self, lij):
        ids = {r.id for r in lij.allophone_rules}
        assert "LIJ_N_VELAR_FINAL" in ids
        assert "LIJ_NASAL_A" in ids

    def test_final_n_velarises(self):
        """can 'dog' -> [kaŋ]: word-final n -> velar nasal."""
        assert orthography2ipa.transcribe("can", "lij") == "ˈkaŋ"

    def test_velar_nasal_with_nasalisation(self):
        """lann-a 'wool' -> [lãŋa]: nn- = /ŋ/, preceding vowel nasalises."""
        assert orthography2ipa.transcribe("lann-a", "lij") == "ˈlãŋa"


# ---------------------------------------------------------------------------
# Stress placement
# ---------------------------------------------------------------------------

class TestStress:
    def test_default_paroxytone(self):
        """Unmarked -> penultimate: zena 'Genoa' -> ˈzena."""
        assert orthography2ipa.transcribe("zena", "lij").startswith("ˈze")

    def test_accent_marks_stress(self):
        """A written accent wins: çittæ stresses the final æ."""
        assert orthography2ipa.transcribe("çittæ", "lij") == "siˈtɛː"
