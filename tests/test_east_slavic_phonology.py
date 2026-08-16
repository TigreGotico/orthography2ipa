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
class TestRussianStressMarkInput:
    """Combining acute (U+0301) in the input names the stressed syllable.

    Russian stress is free and not written in running text, so the spec falls
    back to a statistical default. Dictionaries, textbooks and children's
    books do write it, with a combining acute over the stressed vowel
    (Timberlake 2004; edition not consulted). Where the input carries that
    mark it is the answer, and the akanje/ikanje reduction contexts follow
    from it.
    """

    ACUTE = "́"

    def test_minimal_pair_is_distinguished(self):
        assert _t("ru", "за́мок") == "ˈzamək"
        assert _t("ru", "замо́к") == "zɐˈmok"
        assert _t("ru", "за́мок") != _t("ru", "замо́к")

    def test_reduction_follows_the_marked_stress(self):
        assert _t("ru", "вода́") == "vɐˈda"
        assert _t("ru", "молоко́") == "məɫɐˈko"

    def test_mark_is_silent(self):
        assert self.ACUTE not in _t("ru", "вода́")
        assert "´" not in _t("ru", "вода́")

    def test_unmarked_input_is_unaffected(self):
        assert _t("ru", "замок") == "ˈzamək"
        assert _t("ru", "вода") == "ˈvodə"

    def test_yo_still_carries_stress(self):
        assert _t("ru", "ёлка") == "ˈjoɫkə"

    def test_the_mark_survives_normalisation(self):
        """Cyrillic has no precomposed acute, so NFC cannot swallow the mark.

        Both normalisation forms are the same code point sequence — assert
        that, then transcribe the sequence once. A composing script would
        need the two forms handled separately; this one does not.
        """
        import unicodedata
        assert unicodedata.normalize("NFC", "замо́к") == "замо́к"
        assert unicodedata.normalize("NFD", "замо́к") == "замо́к"
        assert "замо́к"[3:5] == "о" + self.ACUTE
        assert _t("ru", "замо́к") == "zɐˈmok"

    def test_word_exceptions_are_found_through_the_mark(self):
        """Whole-word data is keyed on bare orthography — a mark must not
        hide the lookup. его/того/кого are the genitive-in-[v] class, and
        they carry the acute word-finally, exactly where it would."""
        assert _t("ru", "его́") == _t("ru", "его") == "jɪˈvo"
        assert _t("ru", "того́") == _t("ru", "того") == "tɐˈvo"
        assert _t("ru", "кого́") == _t("ru", "кого") == "kɐˈvo"
        assert _t("ru", "ничего́") == _t("ru", "ничего") == "nʲɪtɕɪˈvo"

    def test_grammatical_endings_are_found_through_the_mark(self):
        """The ⟨-ого⟩ genitive rewrite is keyed the same way. A mark inside
        the matched tail (большо́го) and one before it (но́вого) both leave
        the rewrite intact."""
        assert _t("ru", "большо́го") == _t("ru", "большого")
        assert _t("ru", "молодо́го") == _t("ru", "молодого")
        assert _t("ru", "большо́го").endswith("və")
        assert _t("ru", "но́вого") == "ˈnovəvə"

    @pytest.mark.parametrize("code", ["ru-x-moscow", "ru-x-northern",
                                      "ru-x-southern", "ru-x-siberian"])
    def test_dialects_inherit_the_behaviour(self, code):
        assert _t(code, "за́мок") != _t(code, "замо́к")
        assert _t(code, "замо́к").startswith("za") or \
            _t(code, "замо́к").startswith("zɐ")
        assert "ˈmok" in _t(code, "замо́к")


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
