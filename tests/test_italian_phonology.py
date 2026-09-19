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


class TestGeminatePalatalization:
    """⟨cc⟩ and ⟨gg⟩ soften before ⟨e i⟩ exactly as their singletons do.

    Italian ⟨c⟩ and ⟨g⟩ are velar before ⟨a o u⟩ and palatal affricates
    before ⟨e i⟩; the doubled spelling is the geminate of whichever value
    the following vowel selects, so ⟨cc⟩ before a front vowel is [ttʃ]
    and ⟨gg⟩ is [ddʒ] (Krämer 2009 §2.2, §7.1; Rogers & d'Arcangeli 2004).
    In the geminate affricate only the stop portion is long.
    """

    @staticmethod
    def _t(w):
        from orthography2ipa import G2P
        from benchmark import _expand_consonant_length
        return _expand_consonant_length(
            G2P("it").transcribe_word(w).replace("ˈ", ""))

    def test_cc_before_e(self):
        assert self._t("acceso") == "attʃezo"

    def test_cc_before_i(self):
        assert self._t("uccidere") == "uttʃidere"

    def test_gg_before_e(self):
        assert self._t("legge") == "leddʒe"

    def test_gg_before_i(self):
        assert self._t("oggi") == "oddʒi"

    def test_cci_before_vowel_i_is_mute(self):
        assert self._t("faccia") == "fattʃa"

    def test_ggi_before_vowel_i_is_mute(self):
        assert self._t("maggio") == "maddʒo"

    def test_cc_before_back_vowel_stays_velar(self):
        assert self._t("bocca") == "bokka"

    def test_gg_before_back_vowel_stays_velar(self):
        assert self._t("leggo") == "leɡɡo"

    def test_cch_stays_velar(self):
        assert self._t("occhi") == "okki"

    def test_ggh_stays_velar(self):
        assert self._t("agghindare") == "aɡɡindare"


class TestPreconsonantalSVoicing:
    """/s/ is voiced before a voiced consonant.

    Standard Italian has no voicing contrast for preconsonantal ⟨s⟩: it is
    [z] before every voiced consonant and [s] before every voiceless one —
    ⟨sbagliare⟩ [zbaʎˈʎaːre], ⟨smettere⟩ [zˈmettere], ⟨slitta⟩ [ˈzlitta],
    ⟨asma⟩ [ˈazma], against ⟨spero⟩ [ˈspɛːro] (Bertinetto & Loporcaro 2005
    §"Consonants"; Krämer 2009 §5.3).
    """

    @staticmethod
    def _t(w):
        from orthography2ipa import G2P
        return G2P("it").transcribe_word(w).replace("ˈ", "")

    def test_s_before_b(self):
        assert self._t("sbaglio").startswith("zb")

    def test_s_before_m(self):
        assert self._t("smettere").startswith("zm")

    def test_s_before_n(self):
        assert self._t("snello").startswith("zn")

    def test_s_before_l(self):
        assert self._t("slitta").startswith("zl")

    def test_s_before_r(self):
        assert self._t("sradicare").startswith("zr")

    def test_s_before_v(self):
        assert self._t("svelto").startswith("zv")

    def test_s_word_internal_before_m(self):
        assert self._t("asma") == "azma"

    def test_s_before_voiceless_stays_voiceless(self):
        assert self._t("spero").startswith("sp")
        assert self._t("stella").startswith("st")
        assert self._t("scusa").startswith("sk")

    def test_s_before_f_stays_voiceless(self):
        assert self._t("sfida").startswith("sf")


class TestGuBeforeVowel:
    """⟨gu⟩ before a vowel spells /ɡw/, the voiced counterpart of ⟨qu⟩.

    ⟨guerra⟩ [ˈɡwɛrra], ⟨guida⟩ [ˈɡwiːda], ⟨seguire⟩ [seˈɡwiːre]; before a
    consonant the ⟨u⟩ is an ordinary vowel — ⟨gustare⟩ [ɡusˈtaːre]
    (Rogers & d'Arcangeli 2004; Krämer 2009 §2.2).
    """

    @staticmethod
    def _t(w):
        from orthography2ipa import G2P
        return G2P("it").transcribe_word(w).replace("ˈ", "")

    def test_gu_before_e(self):
        assert self._t("guerra") == "ɡwerːa"

    def test_gu_before_i(self):
        assert self._t("guida") == "ɡwida"

    def test_gu_before_a(self):
        assert self._t("guanto") == "ɡwanto"

    def test_gu_before_consonant_is_a_vowel(self):
        assert self._t("gustare") == "ɡusˌtare".replace("ˌ", "")

    def test_gu_word_final_is_a_vowel(self):
        assert self._t("ragu") == "raɡu"

    def test_gu_key_does_not_swallow_the_u_before_a_consonant(self):
        """⟨gu⟩ declares ONLY its before-vowel value.

        Giving the key a ``default`` of /ɡu/ would make ⟨gu⟩ tokenize as a
        single unit everywhere, and the /u/ inside it stops counting as a
        neighbouring vowel for every rule keyed on one: the inherently
        long intervocalic consonants (Krämer 2009 §7.2) and intervocalic
        ⟨s⟩ voicing both silently stop firing across it. These two pin
        that the ⟨u⟩ stays a vowel to its neighbours.
        """
        assert self._t("guscio") == "ɡuʃʃo"
        assert self._t("guglia") == "ɡuʎʎa"
        assert self._t("sgusciare") == "zɡuʃʃare"

    def test_gu_key_does_not_block_intervocalic_s_voicing(self):
        assert self._t("Ragusa") == "raɡuza"


class TestItalianDialectInheritance:
    """What the four ``parent: it-IT`` varieties do and do not inherit.

    ``it-IT-x-marche``, ``-roma``, ``-toscana`` and ``-umbria`` declare
    ``parent: it-IT`` but carry their own full ``graphemes`` tables, so
    they inherit it-IT's ``allophone_rules`` and NOT its grapheme or
    positional-grapheme entries. This class pins that split explicitly,
    because it is invisible in the data and a rule added to it-IT reaches
    four more specs without any of them being edited.

    Preconsonantal /s/ voicing is INTENDED to reach them: the agreement
    is pan-Italian, holding in Florence and Rome exactly as in the
    northern varieties — it is the INTERVOCALIC ⟨s⟩ that splits
    Tuscan/central from northern (Bertinetto & Loporcaro 2005, which
    compares Florence, Milan and Rome; Canepari 2009 for the central
    varieties).

    ``-abruzzo``, ``-calabria`` and ``-puglia`` declare no parent and
    inherit nothing.
    """

    CENTRAL = ("it-IT-x-marche", "it-IT-x-roma",
               "it-IT-x-toscana", "it-IT-x-umbria")
    UNPARENTED = ("it-IT-x-abruzzo", "it-IT-x-calabria", "it-IT-x-puglia")

    @staticmethod
    def _t(lang, w):
        from orthography2ipa import G2P
        return G2P(lang).transcribe_word(w).replace("ˈ", "")

    def test_central_varieties_inherit_s_voicing(self):
        for lang in self.CENTRAL:
            assert self._t(lang, "sbagliare").startswith("zb"), lang
            assert self._t(lang, "asma") == "azma", lang

    def test_unparented_varieties_do_not_inherit_s_voicing(self):
        for lang in self.UNPARENTED:
            assert self._t(lang, "sbagliare").startswith("sb"), lang
            assert self._t(lang, "asma") == "asma", lang

    def test_no_variety_inherits_it_it_grapheme_entries(self):
        # they declare their own graphemes tables, so the it-IT
        # geminate-softening and ⟨gu⟩ entries do not reach them
        for lang in self.CENTRAL + self.UNPARENTED:
            assert "tʃ" not in self._t(lang, "faccia"), lang
            assert not self._t(lang, "guida").startswith("ɡw"), lang
