"""Tests for stress blocks added in feat/stress-other-and-deferred.

Covers:
- Turkic Latin (tr, az, tk, uz): word-final default stress
- Turkic Cyrillic (kk, ky, tt, ba): word-final default stress
- Austronesian (id, ms): penultimate default stress
- Hebrew (he): milra (final) default stress
- Deferred data fixes: cel diphthongs, si mahaprana, mni ancestor note,
  nds g positional, tcy extra vowels
"""
import pytest

from orthography2ipa import get
from orthography2ipa.stress import detect_stress, syllabify
from orthography2ipa.types import StressRules

# Cyrillic vowels for syllabifying Cyrillic-script words
_CYRILLIC_VOWELS = frozenset("аеёиоуыэюяАЕЁИОУЫЭЮЯіүәөұ")


def _syls_cyrillic(word: str):
    return syllabify(word, vowels=_CYRILLIC_VOWELS)


# ---------------------------------------------------------------------------
# Part 1 – Turkic Latin stress (word-final default)
# ---------------------------------------------------------------------------

class TestTurkicLatinStress:
    @pytest.mark.parametrize("code", ["tr", "az", "tk", "uz"])
    def test_stress_block_present(self, code):
        spec = get(code)
        assert spec.stress is not None, f"{code} has no stress block"

    @pytest.mark.parametrize("code", ["tr", "az", "tk", "uz"])
    def test_default_position_final(self, code):
        rules = get(code).stress
        assert rules.default_position == -1

    @pytest.mark.parametrize("code", ["tr", "az", "tk", "uz"])
    def test_no_marked_vowels(self, code):
        rules = get(code).stress
        assert not rules.marked_vowels

    # Turkish gold cases (word-final stress = last syllable index)
    @pytest.mark.parametrize("word,expected", [
        ("ev", 0),         # monosyllable
        ("masa", 1),       # ma-SA
        ("kitap", 1),      # ki-TAP
        ("araba", 2),      # a-ra-BA
        ("televizyon", 3), # te-le-vi-ZYON
    ])
    def test_turkish_gold(self, word, expected):
        rules = get("tr").stress
        assert detect_stress(word, rules) == expected

    # Azerbaijani gold cases
    @pytest.mark.parametrize("word,expected", [
        ("ev", 0),     # monosyllable
        ("kitab", 1),  # ki-TAB
        ("uşaq", 1),   # u-ŞAQ
        ("məktəb", 1), # mək-TƏB
        ("qələm", 1),  # qə-LƏM
    ])
    def test_azerbaijani_gold(self, word, expected):
        rules = get("az").stress
        assert detect_stress(word, rules) == expected

    # Uzbek gold cases
    @pytest.mark.parametrize("word,expected", [
        ("uy", 0),      # monosyllable
        ("kitob", 1),   # ki-TOB
        ("qalam", 1),   # qa-LAM
        ("maktab", 1),  # mak-TAB
        ("Toshkent", 1), # Tosh-KENT
    ])
    def test_uzbek_gold(self, word, expected):
        rules = get("uz").stress
        assert detect_stress(word, rules) == expected


# ---------------------------------------------------------------------------
# Part 1 – Turkic Cyrillic stress (word-final default)
# ---------------------------------------------------------------------------

class TestTurkicCyrillicStress:
    @pytest.mark.parametrize("code", ["kk", "ky", "tt", "ba"])
    def test_stress_block_present(self, code):
        spec = get(code)
        assert spec.stress is not None, f"{code} has no stress block"

    @pytest.mark.parametrize("code", ["kk", "ky", "tt", "ba"])
    def test_default_position_final(self, code):
        rules = get(code).stress
        assert rules.default_position == -1

    # Kazakh gold cases (Cyrillic)
    @pytest.mark.parametrize("word,expected", [
        ("үй", 0),          # monosyllable
        ("алма", 1),        # ал-МА
        ("мектеп", 1),      # мек-ТЕП
        ("кітаптар", 2),    # кі-тап-ТАР
        ("балалар", 2),     # ба-ла-ЛАР
    ])
    def test_kazakh_gold(self, word, expected):
        rules = get("kk").stress
        syls = _syls_cyrillic(word)
        assert detect_stress(word, rules, syllables=syls) == expected

    # Kyrgyz gold cases
    @pytest.mark.parametrize("word,expected", [
        ("үй", 0),
        ("алма", 1),
        ("мектеп", 1),
        ("китептер", 2),  # ки-теп-ТЕР
        ("балдар", 1),    # бал-ДАР
    ])
    def test_kyrgyz_gold(self, word, expected):
        rules = get("ky").stress
        syls = _syls_cyrillic(word)
        assert detect_stress(word, rules, syllables=syls) == expected

    # Tatar gold cases
    @pytest.mark.parametrize("word,expected", [
        ("өй", 0),
        ("алма", 1),
        ("мәктәп", 1),
        ("китаплар", 2),   # ки-тап-ЛАР
        ("авыл", 1),       # а-ВЫЛ
    ])
    def test_tatar_gold(self, word, expected):
        rules = get("tt").stress
        syls = _syls_cyrillic(word)
        assert detect_stress(word, rules, syllables=syls) == expected

    # Bashkir gold cases
    @pytest.mark.parametrize("word,expected", [
        ("өй", 0),
        ("алма", 1),
        ("мәктәп", 1),
        ("ҡалалар", 2),    # ҡа-ла-ЛАР
        ("китаптар", 2),   # ки-тап-ТАР
    ])
    def test_bashkir_gold(self, word, expected):
        rules = get("ba").stress
        # Bashkir uses additional vowels ҡ etc.; basic Cyrillic vowels work
        syls = _syls_cyrillic(word)
        assert detect_stress(word, rules, syllables=syls) == expected


# ---------------------------------------------------------------------------
# Part 1 – Austronesian stress (penultimate default)
# ---------------------------------------------------------------------------

class TestAustronesianStress:
    @pytest.mark.parametrize("code", ["id", "ms"])
    def test_stress_block_present(self, code):
        spec = get(code)
        assert spec.stress is not None, f"{code} has no stress block"

    @pytest.mark.parametrize("code", ["id", "ms"])
    def test_default_position_penultimate(self, code):
        rules = get(code).stress
        assert rules.default_position == -2

    # Indonesian gold cases (penultimate)
    @pytest.mark.parametrize("word,expected", [
        ("buku", 0),       # BU-ku (penult = index 0)
        ("makan", 0),      # MA-kan
        ("berjalan", 1),   # ber-JA-lan
        ("makanan", 1),    # ma-KA-nan
        ("perjalanan", 2), # per-ja-LA-nan
    ])
    def test_indonesian_gold(self, word, expected):
        rules = get("id").stress
        assert detect_stress(word, rules) == expected

    # Malay gold cases
    @pytest.mark.parametrize("word,expected", [
        ("buku", 0),
        ("makan", 0),
        ("pergi", 0),
        ("berjalan", 1),
        ("makanan", 1),
    ])
    def test_malay_gold(self, word, expected):
        rules = get("ms").stress
        assert detect_stress(word, rules) == expected


# ---------------------------------------------------------------------------
# Part 1 – Hebrew stress (milra/final default)
# ---------------------------------------------------------------------------

class TestHebrewStress:
    def test_stress_block_present(self):
        spec = get("he")
        assert spec.stress is not None

    def test_default_position_final(self):
        rules = get("he").stress
        assert rules.default_position == -1

    def test_no_marked_vowels(self):
        rules = get("he").stress
        assert not rules.marked_vowels

    def test_notes_mention_milra(self):
        rules = get("he").stress
        assert "milra" in rules.notes.lower() or "final" in rules.notes.lower()


# ---------------------------------------------------------------------------
# Part 2 – Deferred data fixes
# ---------------------------------------------------------------------------

class TestCelDiphthongs:
    """cel.json: ē removed, diphthongs ai/ei/oi/au/ou added."""

    def test_ee_removed(self):
        spec = get("cel")
        assert "ē" not in spec.graphemes, "ē should be removed from Proto-Celtic graphemes"

    @pytest.mark.parametrize("diph", ["ai", "ei", "oi", "au", "ou"])
    def test_diphthongs_present(self, diph):
        spec = get("cel")
        assert diph in spec.graphemes, f"Proto-Celtic diphthong {diph!r} missing"

    def test_long_vowels_retained(self):
        spec = get("cel")
        for v in ["ā", "ī", "ō", "ū"]:
            assert v in spec.graphemes, f"Long vowel {v!r} should be retained"


class TestSinhaleseMahaprana:
    """si.json: ඡ and ඣ now have unaspirated candidates first."""

    def test_cha_has_unaspirated(self):
        spec = get("si")
        assert "tʃ" in spec.graphemes["ඡ"], "ඡ should include unaspirated tʃ"

    def test_jha_has_unaspirated(self):
        spec = get("si")
        assert "dʒ" in spec.graphemes["ඣ"], "ඣ should include unaspirated dʒ"

    def test_other_mahaprana_already_fixed(self):
        spec = get("si")
        # These were already correct in the spec
        assert "k" in spec.graphemes["ඛ"]
        assert "p" in spec.graphemes["ඵ"]
        assert "b" in spec.graphemes["භ"]


class TestMeiteiAncestors:
    """mni.json: ancestor note clarified; mni-x-proto-kuki-chin note updated."""

    def test_mni_ancestor_note_updated(self):
        spec = get("mni")
        anc = next((a for a in spec.ancestors if a.code == "mni-x-proto-kuki-chin"), None)
        assert anc is not None
        assert "sister" in anc.notes.lower() or "meiteic" in anc.notes.lower()

    def test_mni_tone_inventory_present(self):
        spec = get("mni")
        assert spec.tone_inventory is not None

    def test_proto_kuki_chin_notes_updated(self):
        spec = get("mni-x-proto-kuki-chin")
        # Meitei should no longer be claimed as a direct descendant
        assert "sister" in spec.notes.lower() or "meiteic" in spec.notes.lower()


class TestNdsGPositional:
    """nds.json: g now has positional variants (fricative in coda/intervocalic)."""

    def test_g_grapheme_includes_fricatives(self):
        spec = get("nds")
        g_vals = spec.graphemes.get("g", [])
        assert "ɣ" in g_vals, "nds g should include intervocalic ɣ"
        assert "x" in g_vals, "nds g should include coda x"

    def test_g_positional_present(self):
        spec = get("nds")
        assert spec.positional_graphemes is not None
        assert "g" in spec.positional_graphemes

    def test_g_coda_is_x(self):
        spec = get("nds")
        pg = spec.positional_graphemes["g"]
        assert "x" in pg.get("coda", []) or "x" in pg.get("word_final", [])


class TestTuluVowels:
    """tcy.json: ĕ→ɛ and ŭ→ɨ added."""

    def test_e_breve_present(self):
        spec = get("tcy")
        assert "ĕ" in spec.graphemes, "Tulu ĕ /ɛ/ should be in graphemes"
        assert "ɛ" in spec.graphemes["ĕ"]

    def test_u_breve_present(self):
        spec = get("tcy")
        assert "ŭ" in spec.graphemes, "Tulu ŭ /ɨ~ɯ/ should be in graphemes"
        assert "ɨ" in spec.graphemes["ŭ"]


class TestPolishPhonology:
    """Gussmann (2007) The Phonology of Polish (OUP) — the rules behind
    the pl spec's positional ⟨i⟩, nasal-vowel decomposition, and
    obstruent voicing assimilation."""

    @staticmethod
    def _t(w):
        from orthography2ipa import G2P
        return G2P("pl").transcribe_word(w).replace("ˈ", "")

    def test_prevocalic_i_is_a_glide(self):
        assert self._t("wie") == "vjɛ"

    def test_i_after_palatal_digraph_is_mute_before_vowel(self):
        # ⟨zie⟩: the i only marks palatality (Gussmann §5)
        assert self._t("Abchazie") == "apxaʑɛ"

    def test_nasal_vowel_decomposes_before_stop(self):
        assert self._t("ząb") == "zɔmp"       # §2.4, homorganic m + final devoicing
        assert self._t("ręka") == "rɛŋka"     # velar → ŋ

    def test_word_final_a_ogonek_keeps_nasal_glide(self):
        assert self._t("są") == "sɔw̃"        # §2.4

    def test_word_final_e_ogonek_denasalizes(self):
        assert self._t("się") == "ɕɛ"

    def test_regressive_devoicing(self):
        assert self._t("wódka") == "vutka"    # ch. 8

    def test_regressive_voicing(self):
        assert self._t("prośba") == "prɔʑba"  # ch. 8

    def test_progressive_devoicing_of_v(self):
        assert self._t("kwiat") == "kfjat"    # ch. 8 — v assimilates rightward

    def test_velar_nasal_assimilation(self):
        assert self._t("bank") == "baŋk"      # §2.3
