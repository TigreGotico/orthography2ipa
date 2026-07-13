"""Tests for the declarative stress system.

Validates:
- StressRules schema round-trip through json_loader and pydantic
- detect_stress precedence: marked vowels > oxytone endings >
  penult endings > default position
- Portuguese gold stress placements on pt-PT/pt-BR seed data
- apply_stress_mark insertion (orthographic and end-anchored indices)
- Specs without a stress block are unaffected
"""
import pytest

from orthography2ipa import get
from orthography2ipa.schema import StressRulesModel
from orthography2ipa.stress import apply_stress_mark, detect_stress, syllabify
from orthography2ipa.types import StressRules


class TestSchema:
    def test_pt_specs_carry_stress(self):
        for code in ("pt-PT", "pt-BR"):
            rules = get(code).stress
            assert isinstance(rules, StressRules)
            assert rules.default_position == -2
            assert "r" in rules.final_stress_endings
            assert "á" in rules.marked_vowels
            assert rules.stress_mark == "ˈ"

    def test_specs_without_stress_are_none(self):
        assert get("en-GB").stress is None
        # `ar` now declares a quantity-sensitive block, so it is no longer an
        # example of a spec without stress.
        assert get("arc").stress is None

    def test_pydantic_model_validates(self):
        model = StressRulesModel(
            default_position=-1,
            final_stress_endings=["r"],
            marked_vowels=["á"],
        )
        assert model.default_position == -1

    def test_pydantic_rejects_bad_position(self):
        with pytest.raises(Exception):
            StressRulesModel(default_position=5)

    def test_pydantic_rejects_zero_position(self):
        with pytest.raises(Exception):
            StressRulesModel(default_position=0)

    def test_pydantic_accepts_initial_stress_position(self):
        model = StressRulesModel(default_position=1)
        assert model.default_position == 1

    def test_pydantic_accepts_second_syllable_position(self):
        model = StressRulesModel(default_position=2)
        assert model.default_position == 2

    def test_pydantic_rejects_empty_entries(self):
        with pytest.raises(Exception):
            StressRulesModel(final_stress_endings=[""])


class TestSyllabify:
    @pytest.mark.parametrize("word,count", [
        ("casa", 2), ("falar", 2), ("abacaxi", 4), ("sol", 1),
        ("lâmpada", 3), ("médico", 3), ("", 0),
    ])
    def test_counts(self, word, count):
        assert len(syllabify(word)) == count

    def test_round_trip(self):
        for word in ("casa", "falar", "abacaxi", "lâmpada", "atuns"):
            assert "".join(syllabify(word)) == word


class TestDetectStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("pt-PT").stress

    @pytest.mark.parametrize("word,expected", [
        # paroxytone default
        ("casa", 0), ("livro", 0), ("homem", 0), ("falam", 0),
        ("rapazes", 1),
        # hiatus 'ia' counts as one nucleus for the naive syllabifier;
        # the stressed vowel still falls inside the returned syllable
        ("viagem", 0),
        # oxytone endings
        ("falar", 1), ("azul", 1), ("rapaz", 1), ("jardim", 1),
        ("caju", 1), ("abacaxi", 3), ("atuns", 1),
        # written accents win
        ("médico", 0), ("lâmpada", 0), ("café", 1), ("túnel", 0),
        ("órgão", 0), ("manhã", 1), ("amável", 1),
        # monosyllables inherently stressed
        ("sol", 0), ("pé", 0),
    ])
    def test_portuguese_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected

    def test_explicit_syllables_override(self, rules):
        assert detect_stress("falar", rules, syllables=["fa", "lar"]) == 1

    def test_penult_endings(self):
        rules = StressRules(default_position=-1,
                            penult_stress_endings=("os",))
        assert detect_stress("santos", rules) == 0
        assert detect_stress("santo", rules) == 1

    def test_default_clamped_on_short_words(self):
        rules = StressRules(default_position=-3)
        assert detect_stress("casa", rules) == 0


class TestApplyStressMark:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("pt-PT").stress

    def test_end_anchored_index(self, rules):
        assert apply_stress_mark("fɐlaɾ", rules, -1) == "fɐˈlaɾ"
        assert apply_stress_mark("kazɐ", rules, -2) == "ˈkazɐ"

    def test_orthographic_index_converted(self, rules):
        assert apply_stress_mark(
            "kazɐ", rules, 0, syllables=["ca", "sa"]) == "ˈkazɐ"
        assert apply_stress_mark(
            "fɐlaɾ", rules, 1, syllables=["fa", "lar"]) == "fɐˈlaɾ"

    def test_already_marked_unchanged(self, rules):
        assert apply_stress_mark("fɐˈlaɾ", rules, -1) == "fɐˈlaɾ"

    def test_empty_input(self, rules):
        assert apply_stress_mark("", rules, -1) == ""


class TestSyllabifierPlugins:
    """Per-language syllabifier plugins supersede the naive splitter."""

    class _FakeSyllabifier:
        def syllabify(self, word, lang=None):
            # hiatus-aware: the naive splitter cannot separate 'i-a'
            if word == "viagem":
                return ["vi", "a", "gem"]
            return [word]

        @property
        def language_codes(self):
            return ["pt-PT"]

        @property
        def priority(self):
            return 50

    def _install(self, monkeypatch):
        from orthography2ipa import registry
        monkeypatch.setattr(
            registry, "_syllabifiers", {"pt-PT": self._FakeSyllabifier()})

    def test_plugin_used_for_lang(self, monkeypatch):
        from orthography2ipa import get
        self._install(monkeypatch)
        rules = get("pt-PT").stress
        # with the hiatus-aware plugin, viagem is correctly paroxytone
        # over three syllables (vi-A-gem)
        assert detect_stress("viagem", rules, lang="pt-PT") == 1

    def test_no_plugin_falls_back_to_naive(self, monkeypatch):
        from orthography2ipa import get
        self._install(monkeypatch)
        rules = get("pt-PT").stress
        assert detect_stress("viagem", rules, lang="en-GB") == 0

    def test_explicit_syllables_beat_plugin(self, monkeypatch):
        from orthography2ipa import get
        self._install(monkeypatch)
        rules = get("pt-PT").stress
        assert detect_stress(
            "viagem", rules, syllables=["via", "gem"], lang="pt-PT") == 0

    def test_get_syllabifier_unknown_lang(self):
        from orthography2ipa import get_syllabifier
        assert get_syllabifier("zz-ZZ") is None

    def test_broken_plugin_output_rejected(self, monkeypatch):
        """A plugin whose syllables don't rebuild the word is ignored."""
        from orthography2ipa import get, registry

        class Broken:
            def syllabify(self, word, lang=None):
                return ["xxx"]

            @property
            def language_codes(self):
                return ["pt-PT"]

            @property
            def priority(self):
                return 50

        monkeypatch.setattr(registry, "_syllabifiers", {"pt-PT": Broken()})
        rules = get("pt-PT").stress
        # falls back to the naive splitter instead of trusting garbage
        assert detect_stress("casa", rules, lang="pt-PT") == 0

    def test_raising_plugin_falls_back_and_logs(self, monkeypatch, caplog):
        """A plugin that raises is logged and the naive splitter is used."""
        import logging
        from orthography2ipa import get, registry

        class Raising:
            def syllabify(self, word, lang=None):
                raise RuntimeError("boom")

            @property
            def language_codes(self):
                return ["pt-PT"]

            @property
            def priority(self):
                return 50

        monkeypatch.setattr(registry, "_syllabifiers", {"pt-PT": Raising()})
        rules = get("pt-PT").stress
        with caplog.at_level(logging.WARNING):
            # falls back to the naive splitter and still returns a valid result
            assert detect_stress("casa", rules, lang="pt-PT") == 0
        assert len(caplog.records) == 1
        message = caplog.records[0].getMessage()
        assert caplog.records[0].levelno == logging.WARNING
        assert "Raising" in message
        assert "casa" in message
        assert "boom" in message


class TestGalicianStress:
    """Gold stress placements for Galician (gl) — Cotovia/GTM rules."""

    @pytest.fixture(scope="class")
    def rules(self):
        return get("gl").stress

    def test_gl_carries_stress_block(self, rules):
        assert rules is not None
        assert rules.default_position == -2
        assert rules.stress_mark == "ˈ"

    @pytest.mark.parametrize("word,expected", [
        # paroxytone default (vowel-final)
        ("casa",   0),   # ca-sa → syll 0
        ("galego", 1),   # ga-le-go → syll 1 (middle)
        # penult_stress_endings: -n and -s stay paroxytone
        ("casas",  0),   # ca-sas → syll 0
        ("cantan", 0),   # ca-ntan → syll 0
        # oxytone endings
        ("falar",  1),   # fa-lar → final
        ("azul",   1),   # a-zul → final
        ("rapaz",  1),   # ra-paz → final
        # written accent overrides
        ("café",   1),   # ca-fé → accent on last
        ("médico", 0),   # mé-di-co → accent on first
        ("nación", 1),   # na-ción → accent on last
    ])
    def test_galician_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestMirandeseStress:
    """Gold stress placements for Mirandese (mwl).

    Convenção Ortográfica da Língua Mirandesa (1999): Portuguese-based
    accentuation, but Mirandese orthography writes final nasals with -n
    (Asturleonese trait: camin, naçon, un) and has word-final ⟨ç⟩
    (rapaç, lhuç) where Portuguese writes -z.
    """

    @pytest.fixture(scope="class")
    def rules(self):
        return get("mwl").stress

    def test_mwl_carries_stress_block(self, rules):
        assert rules is not None
        assert rules.default_position == -2
        assert "á" in rules.marked_vowels
        assert "r" in rules.final_stress_endings
        # Mirandese nasal endings are -n, never the Portuguese -m
        assert "in" in rules.final_stress_endings
        assert "on" in rules.final_stress_endings
        assert "im" not in rules.final_stress_endings
        assert "um" not in rules.final_stress_endings

    def test_mwl_j_is_postalveolar(self):
        """Mirandese ⟨j⟩ is /ʒ/ (western Iberian), never the Asturian ʝ."""
        spec = get("mwl")
        assert spec.graphemes["j"] == ["ʒ"], (
            f"mwl j should be ʒ; got {spec.graphemes['j']}"
        )

    def test_mwl_cedilla_is_voiceless_dorsal(self):
        """Mirandese keeps the apical vs dorso-dental sibilant contrast:
        ⟨ç⟩ is the voiceless dorso-dental fricative — written plain /s/
        (only the apical ⟨s⟩ series carries the ̺ diacritic, matching the
        expert gold) — not the Asturian affricate t͡s, and not the voiced
        /z/, which is the value of ⟨z⟩."""
        spec = get("mwl")
        assert spec.graphemes["ç"] == ["s"], (
            f"mwl ç should be plain s; got {spec.graphemes['ç']}"
        )

    @pytest.mark.parametrize("word,expected", [
        # paroxytone default (vowel-final)
        ("casa",     0),   # ca-sa → syll 0
        ("lhéngua",  0),   # lhé-ngua → accent on first
        # oxytone endings: consonant-final, incl. word-final ç
        ("falar",    1),   # fa-lar → final
        ("rapaç",    1),   # ra-paç → final (Mirandese -ç where pt has -z)
        # final nasals written -n (Asturleonese), not -m
        ("camin",    1),   # ca-min → -in oxytone
        ("naçon",    1),   # na-çon → -on (< Lat. -ōnem) oxytone
        # written accents win
        ("mirandés", 2),   # mi-ra-ndés (3 sylls) → accent on last
        # tilde vowel as accent-bearer
        ("irmã",     1),   # ir-mã → accent on last (ã in marked_vowels)
    ])
    def test_mirandese_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestBarranquenhoStress:
    """Gold stress placements for Barranquenho (ext-PT-x-barrancos)."""

    @pytest.fixture(scope="class")
    def rules(self):
        return get("ext-PT-x-barrancos").stress

    def test_barrancos_carries_stress_block(self, rules):
        assert rules is not None
        assert rules.default_position == -2
        assert "á" in rules.marked_vowels
        # Convenção 2025 + Gramática 2025: final -r and -l are deleted and not written
        # in canonical Barranquenho orthography; they are NOT oxytone triggers.
        assert "r" not in rules.final_stress_endings
        # Nasal diphthong endings -âu/-âi/-ôi ARE oxytone triggers (Convenção pp. 26–27)
        assert "âu" in rules.final_stress_endings
        assert "âi" in rules.final_stress_endings
        assert "ôi" in rules.final_stress_endings
        # Final unmarked -i/-u are PAROXYTONE atone endings in Barranquenho
        assert "i" not in rules.final_stress_endings
        assert "u" not in rules.final_stress_endings

    @pytest.mark.parametrize("word,expected", [
        # paroxytone default (vowel-final)
        ("casa",   0),   # ca-sa → syll 0
        ("casas",  0),   # ca-sas → vowel+s penult (not in final_stress_endings)
        # unmarked -em/-am stay paroxytone, as in Portuguese norms
        ("homem",  0),   # ho-mem → penult
        ("falam",  0),   # fa-lam → penult
        # falar: in canonical Barranquenho this would be written cantá (r deleted);
        # if encountered in pt-PT spelling, -r is no longer an oxytone trigger
        # (Convenção p. 32; Gramática p. 20) — paroxytone fallback
        ("falar",  0),   # fa-lar → penult (r not an oxytone trigger in Barranquenho)
        # caju: final -u is the regular atone ending in Barranquenho (not oxytone)
        # (Gramática p. 12, 14 — paroxytone default for unmarked -u)
        ("caju",   0),   # ca-ju → penult (unmarked -u is paroxytone)
        # written accent overrides
        ("café",   1),   # ca-fé → accent on last
        ("médico", 0),   # mé-di-co → accent on first
    ])
    def test_barranquenho_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


# ─────────────────────────────────────────────────────────────────────────────
# From-start anchoring (positive default_position)
# ─────────────────────────────────────────────────────────────────────────────

class TestFromStartAnchoring:
    """Unit tests for the positive default_position extension."""

    def test_initial_stress_two_syllables(self):
        rules = StressRules(default_position=1)
        assert detect_stress("auto", rules) == 0

    def test_initial_stress_three_syllables(self):
        rules = StressRules(default_position=1)
        assert detect_stress("lampa", rules) == 0

    def test_initial_stress_four_syllables(self):
        rules = StressRules(default_position=1)
        # au-to-mo-bil → first syllable
        assert detect_stress("automobil", rules) == 0

    def test_second_syllable_position(self):
        rules = StressRules(default_position=2)
        assert detect_stress("automobil", rules) == 1

    def test_initial_clamped_on_monosyllable(self):
        rules = StressRules(default_position=1)
        assert detect_stress("sol", rules) == 0

    def test_marked_vowel_overrides_initial(self):
        """Written accents still win over fixed initial default."""
        rules = StressRules(default_position=1, marked_vowels=("é",))
        # ca-fé → accent on last (index 1), not first (index 0)
        assert detect_stress("café", rules) == 1

    def test_apply_stress_mark_initial(self):
        rules = StressRules(default_position=1, stress_mark="ˈ")
        # stress_index=0 → first IPA syllable
        result = apply_stress_mark("ˈlampa", rules, 0, syllables=["lam", "pa"])
        assert result == "ˈlampa"

    def test_apply_stress_mark_initial_insert(self):
        rules = StressRules(default_position=1, stress_mark="ˈ")
        result = apply_stress_mark("lampa", rules, 0, syllables=["lam", "pa"])
        assert result.startswith("ˈ")


# ─────────────────────────────────────────────────────────────────────────────
# Initial-stress languages (default_position 1)
# ─────────────────────────────────────────────────────────────────────────────

class TestCzechStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("cs").stress

    def test_carries_initial_stress(self, rules):
        assert rules is not None
        assert rules.default_position == 1
        assert rules.marked_vowels == ()

    @pytest.mark.parametrize("word,expected", [
        ("Praha",    0),   # Pra-ha → first
        ("svoboda",  0),   # svo-bo-da → first
        ("republika",0),   # re-pu-bli-ka → first
        ("kniha",    0),   # kni-ha → first
        ("oblíbený", 0),   # o-blí-be-ný → first (diacritic = quantity)
        ("akademie", 0),   # a-ka-de-mi-e → first
    ])
    def test_czech_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestSlovakStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("sk").stress

    def test_carries_initial_stress(self, rules):
        assert rules is not None
        assert rules.default_position == 1

    @pytest.mark.parametrize("word,expected", [
        ("mesto",    0),   # mes-to → first
        ("sloboda",  0),   # slo-bo-da → first
        ("republika",0),   # re-pu-bli-ka → first
        ("chleba",   0),   # chle-ba → first
        ("muzika",   0),   # mu-zi-ka → first
        ("krajina",  0),   # kra-ji-na → first
    ])
    def test_slovak_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestFinnishStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("fi").stress

    def test_carries_initial_stress(self, rules):
        assert rules is not None
        assert rules.default_position == 1

    @pytest.mark.parametrize("word,expected", [
        ("talo",     0),   # ta-lo → first
        ("Helsinki", 0),   # Hel-sin-ki → first
        ("suomalainen", 0),# suo-ma-lai-nen → first
        ("puhelin",  0),   # pu-he-lin → first
        ("yliopisto",0),   # y-li-o-pis-to → first
        ("auto",     0),   # au-to → first
    ])
    def test_finnish_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestEstonianStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("et").stress

    def test_carries_initial_stress(self, rules):
        assert rules is not None
        assert rules.default_position == 1

    @pytest.mark.parametrize("word,expected", [
        ("maja",     0),   # ma-ja → first
        ("Tallinn",  0),   # Tal-linn → first
        ("vabadus",  0),   # va-ba-dus → first
        ("eesti",    0),   # ees-ti → first
        ("kool",     0),   # monosyllable → 0
        ("raamat",   0),   # raa-mat → first
    ])
    def test_estonian_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestHungarianStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("hu").stress

    def test_carries_initial_stress(self, rules):
        assert rules is not None
        assert rules.default_position == 1

    @pytest.mark.parametrize("word,expected", [
        ("ház",      0),   # monosyllable → 0
        ("alma",     0),   # al-ma → first
        ("Budapest", 0),   # Bu-da-pest → first
        ("szabadság",0),   # sza-bad-ság → first
        ("könyvtár", 0),   # könyv-tár → first
        ("magyarország", 0),  # ma-gyar-or-szág → first
    ])
    def test_hungarian_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestLatvianStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("lv").stress

    def test_carries_initial_stress(self, rules):
        assert rules is not None
        assert rules.default_position == 1

    @pytest.mark.parametrize("word,expected", [
        ("māja",     0),   # mā-ja → first
        ("Rīga",     0),   # Rī-ga → first
        ("valsts",   0),   # monosyllable-like → 0
        ("bērni",    0),   # bēr-ni → first
        ("grāmata",  0),   # grā-ma-ta → first
        ("universitāte", 0),  # u-ni-ver-si-tā-te → first
    ])
    def test_latvian_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestIcelandicStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("is").stress

    def test_carries_initial_stress(self, rules):
        assert rules is not None
        assert rules.default_position == 1

    @pytest.mark.parametrize("word,expected", [
        ("hús",      0),   # monosyllable → 0
        ("bók",      0),   # monosyllable → 0
        ("hestur",   0),   # hes-tur → first
        ("Ísland",   0),   # Ís-land → first
        ("samband",  0),   # sam-band → first
        ("framkvæmd",0),   # fram-kvæmd → first
    ])
    def test_icelandic_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestUpperSorbianStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("hsb").stress

    def test_carries_initial_stress(self, rules):
        assert rules is not None
        assert rules.default_position == 1

    @pytest.mark.parametrize("word,expected", [
        ("woda",     0),   # wo-da → first
        ("swoboda",  0),   # swo-bo-da → first
        ("knjez",    0),   # monosyllable → 0
        ("Łužica",   0),   # Łu-ži-ca → first
        ("čitać",    0),   # či-tać → first
        ("zapisk",   0),   # za-pisk → first (z+a = one nucleus)
    ])
    def test_upper_sorbian_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestLowerSorbianStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("dsb").stress

    def test_carries_initial_stress(self, rules):
        assert rules is not None
        assert rules.default_position == 1

    @pytest.mark.parametrize("word,expected", [
        ("woda",     0),   # wo-da → first
        ("swoboda",  0),   # swo-bo-da → first
        ("dom",      0),   # monosyllable → 0
        ("Chóśebuz", 0),   # Chó-śe-buz → first
        ("gólic",    0),   # gó-lic → first
        ("muzika",   0),   # mu-zi-ka → first
    ])
    def test_lower_sorbian_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


# ─────────────────────────────────────────────────────────────────────────────
# Penultimate-stress languages (default_position -2)
# ─────────────────────────────────────────────────────────────────────────────

class TestEsperantoStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("eo").stress

    def test_carries_penult_stress(self, rules):
        assert rules is not None
        assert rules.default_position == -2
        assert rules.marked_vowels == ()

    @pytest.mark.parametrize("word,expected", [
        ("pomo",     0),   # po-mo → penult = index 0
        ("amiko",    1),   # a-mi-ko → penult = index 1
        ("Esperanto",2),   # E-spe-ra-nto → 4 sylls → penult = index 2
        ("lingvo",   0),   # ling-vo → penult = index 0
        ("bela",     0),   # be-la → penult = index 0
        ("internacia",2),  # i-nte-rna-cia → 4 sylls → penult = index 2
    ])
    def test_esperanto_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestPolishStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("pl").stress

    def test_carries_penult_stress(self, rules):
        assert rules is not None
        assert rules.default_position == -2
        assert "ó" not in rules.marked_vowels

    @pytest.mark.parametrize("word,expected", [
        ("mama",     0),   # ma-ma → penult = index 0
        ("Polska",   0),   # Pol-ska → penult = index 0
        ("muzyka",   1),   # mu-zy-ka → penult = index 1
        ("literatura",3),  # li-te-ra-tu-ra → penult = index 3 (5 sylls)
        ("okno",     0),   # ok-no → penult = index 0
        ("Warszawa", 1),   # War-sza-wa → penult = index 1
    ])
    def test_polish_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


class TestSwahiliStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("sw").stress

    def test_carries_penult_stress(self, rules):
        assert rules is not None
        assert rules.default_position == -2

    @pytest.mark.parametrize("word,expected", [
        ("mama",     0),   # ma-ma → penult = index 0
        ("kitabu",   1),   # ki-ta-bu → penult = index 1
        ("mwalimu",  1),   # mwa-li-mu → penult = index 1
        ("chakula",  1),   # cha-ku-la → penult = index 1
        ("nchi",     0),   # monosyllable-ish → 0
        ("hospitali",2),   # ho-spi-ta-li → 4 sylls → penult = index 2
    ])
    def test_swahili_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


# ─────────────────────────────────────────────────────────────────────────────
# Greek — marked_vowels stress system
# ─────────────────────────────────────────────────────────────────────────────

class TestGreekStress:
    @pytest.fixture(scope="class")
    def rules(self):
        return get("el").stress

    def test_carries_stress_block(self, rules):
        assert rules is not None
        assert "ά" in rules.marked_vowels
        assert "έ" in rules.marked_vowels
        assert "ώ" in rules.marked_vowels

    def test_marked_vowels_subset_of_graphemes(self):
        spec = get("el")
        for mv in spec.stress.marked_vowels:
            assert mv in spec.graphemes, (
                f"marked vowel {mv!r} missing from el graphemes"
            )

    @pytest.mark.parametrize("word,expected", [
        ("άνθρωπος", 0),   # ά-νθρω-πος → accent on ά → index 0
        ("γλώσσα",   0),   # γλώσ-σα → accent on ώ → index 0
        ("νερό",     1),   # νε-ρό → accent on ό → index 1
        ("πατέρας",  1),   # πα-τέ-ρας → accent on έ → index 1
        ("ελληνική", 3),   # ε-λλη-νι-κή → accent on ή → index 3 (4 sylls)
        ("αγαπώ",    2),   # α-γα-πώ → accent on ώ → index 2 (3 sylls)
    ])
    def test_greek_gold(self, rules, word, expected):
        assert detect_stress(word, rules) == expected


# ─── Diphthong-aware syllabification ───────────────────────────────────────

class TestDiphthongs:
    """``StressRules.diphthongs`` splits a vowel run into nuclei.

    The bundled splitter counts a maximal run of vowel letters as ONE
    nucleus. That is right for a language whose vowel runs are all
    diphthongs and wrong wherever the orthography also writes hiatus:
    Catalan ⟨tenia⟩ is te-ni-a, and mis-counting its syllables moves the
    stress — and therefore the unstressed-vowel reduction it conditions —
    onto the wrong vowel.
    """

    CA = ("ai", "au", "ei", "eu", "iu", "oi", "ou", "ui", "ua", "ue", "uo")

    def test_empty_diphthongs_merges_the_whole_run(self):
        assert syllabify("tenia") == ["te", "nia"]
        assert syllabify("tenia", diphthongs=()) == ["te", "nia"]

    def test_hiatus_splits_into_separate_nuclei(self):
        assert syllabify("tenia", diphthongs=self.CA) == ["te", "ni", "a"]
        assert syllabify("dia", diphthongs=self.CA) == ["di", "a"]

    def test_a_listed_diphthong_stays_one_nucleus(self):
        assert syllabify("ciutat", diphthongs=self.CA) == ["ciu", "tat"]
        assert syllabify("aigua", diphthongs=self.CA) == ["ai", "gua"]

    def test_longest_diphthong_wins_and_the_rest_split(self):
        # ⟨eia⟩ = the diphthong ⟨ei⟩ plus a nucleus ⟨a⟩
        assert syllabify("feia", diphthongs=self.CA) == ["fei", "a"]

    def test_syllabification_is_lossless(self):
        for word in ["tenia", "aigua", "ciutat", "veïna", "feia", "coses"]:
            assert "".join(syllabify(word, diphthongs=self.CA)) == word


class TestEpentheticSchwaAnchoring:
    """Regression for the stress-lands-a-syllable-late bug (#19).

    When an allophone rule EPENTHESIZES a nucleus (Goidelic svarabhakti:
    ``gorm`` → ɡɔ-ɾˠəmˠ), the IPA gains a syllable over the orthographic
    count and the end-anchored index conversion used to land the mark one
    syllable late — on the epenthetic schwa itself. Excess ə-nucleus
    syllables are folded back into the preceding syllable for counting.
    The fold must NOT touch the undercounted-orthography overflow class
    (Spanish ``ayer``: 1 orth syllable, IPA a-ʝeɾ, FULL vowels), where
    end-anchoring already lands correctly.
    """

    @pytest.fixture(scope="class")
    def rules(self):
        return get("pt-PT").stress  # only supplies the mark character

    def test_epenthetic_closed_final_schwa_merged(self, rules):
        # Irish gorm: 1 orth syllable, stress index 0; the ə syllable is
        # word-final but CLOSED (coda mˠ) — classic anaptyxis, merged.
        assert apply_stress_mark(
            "ɡɔɾˠəmˠ", rules, 0, syllables=["gorm"]) == "ˈɡɔɾˠəmˠ"

    def test_epenthetic_medial_schwa_merged(self, rules):
        # Irish dorcha: 2 orth syllables (dor-cha), stress index 0. The
        # medial ɾˠə merges; the final OPEN xə is the written vowel of
        # ⟨cha⟩ and must survive as its own syllable.
        assert apply_stress_mark(
            "d̪ˠɔɾˠəxə", rules, 0,
            syllables=["dor", "cha"]) == "ˈd̪ˠɔɾˠəxə"

    def test_full_vowel_overflow_untouched(self, rules):
        # Spanish ayer: the orthographic syllabifier undercounts ⟨aye⟩ as
        # one nucleus, but the IPA split is FULL vowels — no ə to merge,
        # end-anchoring lands on the final syllable as before.
        assert apply_stress_mark(
            "aʝeɾ", rules, 0, syllables=["ayer"]) == "aˈʝeɾ"

    def test_open_final_schwa_is_a_real_vowel(self, rules):
        # Catalan-style word-final open ə (casa → ka-zə) with NO overflow:
        # the fold is dead code and the mark places normally.
        assert apply_stress_mark(
            "kazə", rules, 0, syllables=["ca", "sa"]) == "ˈkazə"

    def test_no_syllables_hint_unchanged(self, rules):
        # Without an orthographic hint n_orth == len(ipa_sylls): no
        # overflow, the fold is dead code, and the index is applied over
        # the IPA syllables directly (index 0 → initial).
        assert apply_stress_mark("ɡɔɾˠəmˠ", rules, 0) == "ˈɡɔɾˠəmˠ"


class TestEpentheticSchwaEndToEnd:
    """The engine-level symptom that motivated the fix, pinned on real
    Irish data: initial stress (Ó Siadhail, Modern Irish §2.1; Foclóir
    Póca headword transcriptions) with svarabhakti epenthesis."""

    def test_irish_svarabhakti_words_stress_initial(self):
        from orthography2ipa import G2P
        g = G2P("ga")
        # gold: Foclóir Póca /ˈɡɔɾˠəmˠ/, /ˈdʲaɾˠəɡ/, /ˈanʲəmʲ/-family
        assert g.transcribe_word("gorm").startswith("ˈ")
        assert g.transcribe_word("dearg").startswith("ˈ")
        assert g.transcribe_word("ainm").startswith("ˈ")
        assert g.transcribe_word("dorcha").startswith("ˈ")
