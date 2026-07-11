"""Regression tests for kab (Kabyle / Taqbaylit) language data.

The spec models the standardised Berber LATIN alphabet (the tamaziɣt/INALCO
orthography used by the Kabyle Wikipedia and Naït-Zerrad's teaching grammars);
Tifinagh is a secondary script and is not modelled. Tests cover the hallmark
Berber-Latin grapheme->IPA correspondences, the signature SPIRANTIZATION of
lax (non-geminate) stops with retention of the geminate stops, nasal place
assimilation, and whole Kabyle words.

Two levels:
- spec.graphemes: the orthography->phoneme table.
- orthography2ipa.transcribe(): the full engine, which applies allophone_rules
  (spirantization). PhonetokTokenizer.ipa_best() is the flat (context-free)
  grapheme path, which does NOT spirantize — useful to prove the spirantization
  lives in the allophone layer.
"""
import pytest

import orthography2ipa
from orthography2ipa.types import QualityTier
from orthography2ipa.phonetok import PhonetokTokenizer


@pytest.fixture(scope="module")
def kab():
    return orthography2ipa.get("kab")


@pytest.fixture(scope="module")
def tok(kab):
    return PhonetokTokenizer(kab)


# ---------------------------------------------------------------------------
# Registry / metadata
# ---------------------------------------------------------------------------

class TestRegistry:
    def test_loads(self, kab):
        assert kab is not None
        assert kab.code == "kab"

    def test_name(self, kab):
        assert kab.name == "Kabyle"

    def test_family(self, kab):
        assert kab.family == "Afro-Asiatic > Berber"

    def test_script_is_latin(self, kab):
        assert kab.script == "Latin"

    def test_iso(self, kab):
        assert kab.iso639_3 == "kab"

    def test_in_available_codes(self):
        assert "kab" in orthography2ipa.available_codes()

    def test_research_tier(self, kab):
        assert kab.quality is QualityTier.RESEARCH

    def test_has_primary_source(self, kab):
        ids = {s.id for s in kab.sources}
        assert "kossmann_stroomer1997" in ids
        assert len(kab.sources) >= 2


# ---------------------------------------------------------------------------
# Hallmark Berber-Latin grapheme->IPA correspondences
# ---------------------------------------------------------------------------

class TestHallmarkGraphemes:
    def test_c_is_esh(self, kab):
        assert kab.graphemes.get("c") == ["ʃ"]

    def test_c_caron_is_affricate(self, kab):
        assert kab.graphemes.get("č") == ["t͡ʃ"]

    def test_g_caron_is_dzh(self, kab):
        assert kab.graphemes.get("ǧ") == ["d͡ʒ"]

    def test_j_is_zh(self, kab):
        assert kab.graphemes.get("j") == ["ʒ"]

    def test_gamma_is_voiced_velar(self, kab):
        assert kab.graphemes.get("ɣ") == ["ɣ"]

    def test_x_is_uvular(self, kab):
        assert kab.graphemes.get("x") == ["χ"]

    def test_hdot_is_pharyngeal(self, kab):
        assert kab.graphemes.get("ḥ") == ["ħ"]

    def test_epsilon_is_ayin(self, kab):
        assert kab.graphemes.get("ɛ") == ["ʕ"]

    def test_q_is_uvular_stop(self, kab):
        assert kab.graphemes.get("q") == ["q"]

    def test_schwa_grapheme(self, kab):
        assert kab.graphemes.get("e") == ["ə"]

    def test_three_vowels(self, kab):
        assert kab.graphemes.get("a") == ["a"]
        assert kab.graphemes.get("i") == ["i"]
        assert kab.graphemes.get("u") == ["u"]


class TestEmphatics:
    """The pharyngealized (emphatic) series ṛ ṣ ḍ ṭ ẓ = /rˤ sˤ dˤ tˤ zˤ/."""

    def test_r_emphatic(self, kab):
        assert kab.graphemes.get("ṛ") == ["rˤ"]

    def test_s_emphatic(self, kab):
        assert kab.graphemes.get("ṣ") == ["sˤ"]

    def test_d_emphatic(self, kab):
        assert kab.graphemes.get("ḍ") == ["dˤ"]

    def test_t_emphatic(self, kab):
        assert kab.graphemes.get("ṭ") == ["tˤ"]

    def test_z_emphatic(self, kab):
        assert kab.graphemes.get("ẓ") == ["zˤ"]


# ---------------------------------------------------------------------------
# Spirantization (THE signature Kabyle feature) — allophone_rules layer
# ---------------------------------------------------------------------------

class TestSpirantization:
    """Lax (non-geminate) stops b d t k g ḍ surface as fricatives β ð θ ç ʝ ðˤ
    (Kossmann & Stroomer 1997, p.466-469). The rule lives in the allophone
    layer, so the flat grapheme path leaves the stops intact."""

    def test_rules_present(self, kab):
        ids = {r.id for r in kab.allophone_rules}
        assert {"KAB_SPIRANT_B", "KAB_SPIRANT_D", "KAB_SPIRANT_T",
                "KAB_SPIRANT_K", "KAB_SPIRANT_G"} <= ids

    def test_g_spirantizes(self):
        """argaz 'man' -> [arʝaz]: lax /ɡ/ -> [ʝ]."""
        assert orthography2ipa.transcribe("argaz", "kab") == "arʝaz"

    def test_d_spirantizes(self):
        """adrar 'mountain' -> [aðrar]: lax /d/ -> [ð]."""
        assert orthography2ipa.transcribe("adrar", "kab") == "aðrar"

    def test_t_spirantizes(self):
        """tili 'shade' -> [θili]: lax /t/ -> [θ]."""
        assert orthography2ipa.transcribe("tili", "kab") == "θili"

    def test_k_spirantizes(self):
        """akli -> [açli]: lax /k/ -> [ç]."""
        assert orthography2ipa.transcribe("akli", "kab") == "açli"

    def test_d_emphatic_spirantizes(self):
        """aḍar 'foot' -> [aðˤar]: lax emphatic /dˤ/ -> [ðˤ]."""
        assert orthography2ipa.transcribe("aḍar", "kab") == "aðˤar"

    def test_flat_path_does_not_spirantize(self, tok):
        """The context-free grapheme path keeps the underlying stops: the
        spirantization is genuinely in the allophone layer, not the map."""
        assert tok.ipa_best("argaz") == "arɡaz"
        assert tok.ipa_best("adrar") == "adrar"


class TestGeminateRetention:
    """Tense (geminate) stops, written by doubling and mapped to long phonemes
    /bː dː tː kː ɡː/, are NEVER spirantized (Kossmann & Stroomer 1997, p.466)."""

    def test_geminate_graphemes(self, kab):
        assert kab.graphemes.get("bb") == ["bː"]
        assert kab.graphemes.get("dd") == ["dː"]
        assert kab.graphemes.get("gg") == ["ɡː"]

    def test_geminate_d_stays_stop(self):
        """yedda 'he went' -> [jədːa]: geminate ⟨dd⟩ stays [dː], not [ð]."""
        assert orthography2ipa.transcribe("yedda", "kab") == "jədːa"

    def test_single_vs_geminate_b(self):
        """ababbu: single b spirantizes to [β], geminate ⟨bb⟩ stays [bː]."""
        assert orthography2ipa.transcribe("ababbu", "kab") == "aβabːu"


# ---------------------------------------------------------------------------
# Nasal place assimilation
# ---------------------------------------------------------------------------

class TestNasalAssimilation:
    def test_rules_present(self, kab):
        ids = {r.id for r in kab.allophone_rules}
        assert "KAB_N_VELAR_ASSIM" in ids
        assert "KAB_N_LABIAL_ASSIM" in ids

    def test_n_velarises_before_velar(self):
        """/n/ -> [ŋ] before a velar/uvular; anki -> [aŋçi] (k also spirantizes)."""
        assert orthography2ipa.transcribe("anki", "kab") == "aŋçi"

    def test_n_labialises_before_labial(self):
        """/n/ -> [m] before a labial; anba -> [amβa]."""
        assert orthography2ipa.transcribe("anba", "kab") == "amβa"


# ---------------------------------------------------------------------------
# Whole words through the full engine
# ---------------------------------------------------------------------------

class TestWords:
    def test_aman(self):
        """aman 'water' -> [aman]: no spirantization target, sanity."""
        assert orthography2ipa.transcribe("aman", "kab") == "aman"

    def test_azul(self):
        """azul 'hello' -> [azul]."""
        assert orthography2ipa.transcribe("azul", "kab") == "azul"

    def test_afus(self):
        """afus 'hand' -> [afus]."""
        assert orthography2ipa.transcribe("afus", "kab") == "afus"

    def test_taqbaylit(self):
        """taqbaylit (the language) -> [θaqβajliθ]: t->θ, q, b->β, final t->θ."""
        assert orthography2ipa.transcribe("taqbaylit", "kab") == "θaqβajliθ"

    def test_tamurt(self):
        """tamurt 'country' -> [θamurθ]."""
        assert orthography2ipa.transcribe("tamurt", "kab") == "θamurθ"
