"""East Slavic phonology — Russian, Ukrainian, Belarusian.

Russian: Timberlake (2004) A Reference Grammar of Russian (CUP) — dark
[ɫ], stress-gated akanje/ikanje reduction (first-pretonic [ɐ] vs [ə]
elsewhere), regressive voicing and palatalization assimilation, ⟨ё⟩
invariantly stressed, [ɵ] after soft consonants.

Ukrainian: Pompino-Marschall, Pashchenko & Mołczanow (2017) Ukrainian,
JIPA 47(3) — dark [ɫ], в as ʋ/w/u̯ by position, palatalization before
iotated vowels and і, no word-final devoicing.

Belarusian: Mayo (1993) Belorussian, in The Slavonic Languages
(Routledge) — retroflex ч ш ж, ў = [u̯], dzekanne/tsekanne carried by
the orthography, regressive devoicing and palatalization.

Also covers the two engine behaviours these specs rely on:
- FIRST_PRETONIC positional context (emitted before generic PRETONIC),
- allophone-rule slot neighbours matching on the adjacent boundary
  SEGMENT of a multi-phoneme neighbour slot, not the whole candidate.
"""
import pytest

from orthography2ipa import G2P


def _t(lang, w):
    return G2P(lang).transcribe_word(w)


@pytest.mark.linguistic
class TestRussianPhonology:

    def test_yo_attracts_stress(self):
        assert _t("ru", "ёлка") == "ˈjoɫkə"

    def test_dark_l(self):
        assert "ɫ" in _t("ru", "лампа")

    def test_soft_l_stays_clear(self):
        assert "lʲ" in _t("ru", "лес")

    def test_akanje_first_pretonic_vs_further(self):
        # first pretonic [ɐ] (Timberlake §2.2.4); собака stresses the penult
        assert _t("ru", "собака") == "sɐˈbakə"

    def test_posttonic_a_reduces_to_schwa(self):
        assert _t("ru", "ёлка").endswith("ə")

    def test_regressive_devoicing_v_before_voiceless(self):
        assert _t("ru", "вши") == "ˈfʂɨ"
        assert _t("ru", "все").startswith("ˈfsʲ")

    def test_regressive_devoicing_d(self):
        assert _t("ru", "водка") == "ˈvotkə"

    def test_regressive_palatalization_of_dentals(self):
        assert "sʲtʲ" in _t("ru", "гости")

    def test_i_after_hard_sibilant_is_barred_i(self):
        assert "ʂɨ" in _t("ru", "маши́на".replace("́", ""))

    def test_o_after_soft_consonant_is_barred_o(self):
        assert "rʲɵ" in _t("ru", "Пономарёв")

    def test_soft_sign_after_hard_sibilant_is_silent(self):
        assert _t("ru", "бухнёшь").endswith("ʂ")


@pytest.mark.linguistic
class TestUkrainianPhonology:

    def test_dark_l(self):
        assert "ɫ" in _t("uk", "волочити")

    def test_v_is_nonsyllabic_u_in_coda(self):
        assert _t("uk", "київ").endswith("u̯")

    def test_v_is_w_before_back_rounded(self):
        assert _t("uk", "вода").startswith("ˈwɔ") or _t("uk", "вода").startswith("wɔ")

    def test_no_word_final_devoicing(self):
        # Ukrainian keeps voiced obstruents word-finally (JIPA 2017)
        assert _t("uk", "сад").endswith("d")

    def test_iotated_palatalizes_dental(self):
        assert "sʲa" in _t("uk", "хвилюся").replace("ˈ", "") or \
               "sʲɐ" in _t("uk", "хвилюся").replace("ˈ", "")

    def test_half_palatalization_before_i(self):
        assert "ʋʲi" in _t("uk", "віл")


@pytest.mark.linguistic
class TestBelarusianPhonology:

    def test_retroflex_sibilants(self):
        out = _t("be", "чорны")
        assert out.startswith("ˈtʂ") or out.startswith("tʂ")

    def test_short_u_nonsyllabic(self):
        assert "u̯" in _t("be", "воўк")

    def test_short_u_word_initial_is_w(self):
        assert _t("be", "ўзял").startswith("w")

    def test_iotated_palatalizes(self):
        assert "bʲe" in _t("be", "беларуская").replace("ˈ", "")

    def test_regressive_devoicing_cluster(self):
        assert "tk" in _t("be", "адкласці")

    def test_regressive_palatalization_cluster(self):
        assert "sʲtsʲ" in _t("be", "адкласці")

    def test_soft_geminate(self):
        assert "nʲː" in _t("be", "пляменнік")


class TestEngineFirstPretonic:
    """FIRST_PRETONIC fires on the syllable immediately before the
    stressed one; generic PRETONIC covers the rest."""

    def test_first_pretonic_beats_generic_pretonic(self):
        # аббатах: stress penult (ба), а-1 is first pretonic -> ɐ;
        # posttonic а -> ə
        out = _t("ru", "аббатах")
        assert out.startswith("ɐ")
        assert out.endswith("əx")

    def test_further_pretonic_gets_generic(self):
        # зашифровал (stress guess penult 'ва'): initial з-а two syllables
        # before the stress -> generic pretonic [ə]
        out = _t("ru", "распахиваю")
        assert out.startswith("rə")


class TestEngineBoundarySegmentNeighbours:
    """followed_by_phoneme matches the FIRST segment of a multi-phoneme
    next slot (ʂɨ triggers a before-ʂ rule), not the whole candidate."""

    def test_rule_fires_before_multiphoneme_slot(self):
        # вши: next slot realises 'ʂɨ'; the devoicing rule's trigger is ʂ
        assert _t("ru", "вши") == "ˈfʂɨ"

    def test_rule_fires_before_single_phoneme_slot(self):
        assert _t("ru", "вка")[1] == "f"
