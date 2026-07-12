"""Italian phonology — Krämer (2009) The Phonology of Italian (OUP).

Covers the it-IT spec's palatalization-marker model for ⟨ci gi sci gli⟩
(the ⟨i⟩ is mute before a vowel, syllabic elsewhere), post-consonantal
⟨z⟩ as an affricate, and the inherently geminate intervocalic
consonants /ɲ ʎ ʃ ts dz/ (Krämer §7.2) realized by allophone rules.

Also covers the benchmark harness's consonant-length canonicalization
(Cː → CC) so gold sets using the length mark and gold sets using
doubling score identically.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import _expand_consonant_length, normalize  # noqa: E402


class TestItalianPhonology:

    @staticmethod
    def _t(w):
        from orthography2ipa import G2P
        return G2P("it").transcribe_word(w).replace("ˈ", "")

    def test_ci_before_vowel_i_is_mute(self):
        assert self._t("ciao") == "tʃao"

    def test_ci_before_consonant_keeps_i(self):
        assert self._t("cima") == "tʃima"

    def test_gi_before_vowel_i_is_mute(self):
        assert self._t("giorno") == "dʒorno"

    def test_sci_before_vowel(self):
        # intervocalic ʃ is inherently long (Krämer §7.2)
        assert self._t("pesce") == "peʃʃe"

    def test_gli_intervocalic_geminates(self):
        assert self._t("aglio") == "aʎʎo"

    def test_gn_intervocalic_geminates(self):
        assert self._t("bagno") == "baɲɲo"

    def test_word_initial_palatal_not_geminated(self):
        assert self._t("gnocco").startswith("ɲ")
        assert not self._t("gnocco").startswith("ɲɲ")

    def test_z_after_consonant_is_affricate(self):
        assert self._t("alzare").replace("ts", "T").count("T") >= 1


class TestExpandConsonantLength:
    """Cː and CC are the same phonological object; the harness must not
    charge a PER unit for the notation choice."""

    def test_plain_consonant_length(self):
        assert _expand_consonant_length("fatːo") == "fatto"

    def test_affricate_doubles_first_element(self):
        # tʃː → ttʃ, not tʃtʃ (standard Italian notation)
        assert _expand_consonant_length("atʃːo") == "attʃo"
        assert _expand_consonant_length("abrutːso") == "abruttso"

    def test_vowel_length_untouched(self):
        assert _expand_consonant_length("kaːza") == "kaːza"

    def test_normalize_equates_notations(self):
        assert (normalize("ˈfatːo", strip_stress=True, broad=False)
                == normalize("ˈfatto", strip_stress=True, broad=False))
