"""Research-grounded Levantine Arabic dialects: Damascene (ar-SY), Beiruti
(ar-LB), Ammani (ar-JO) and Palestinian (ar-PS), plus the shared proto-parent
(ar-x-levantine).

Every assertion is whole-word IPA via the data-driven engine and traces to a
cited, actually-read source:

- Almbark & Hellmuth 2015 (ICPhS 0612): Damascus/Syrian vowel system; mid-long
  /eː oː/ from /aj aw/ coalescence.
- Cotter 2016 (JAIS 16:149-162): urban Palestinian interdental merger; Gaza qaf.
- Al-Wer 2020 (Language Science Press ch.25): Amman koine (q)/(ǧ) reallocation.
- Fadda 2016 (CanIL MA thesis): Ammani koine consonants; qaf labels; diphthongs.

HONESTY NOTE: targets are derived from these cited phonological descriptions and
the deterministic engine; native-speaker validation is still advisable.
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa.g2p import G2P


def _load(code: str):
    try:
        return orthography2ipa.get(code)
    except Exception as exc:  # pragma: no cover - environment guard
        pytest.skip(f"{code!r} not available: {exc}")


def _ipa(code: str, word: str) -> str:
    return G2P(code).transcribe(word)


# ─────────────────────────────────────────────────────────────────────────────
# Shared proto-parent — ar-x-levantine
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.linguistic
class TestLevantineProtoRules:
    CODE = "ar-x-levantine"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_tier_research(self):
        assert self.spec.quality == "research"

    def test_shared_rule_ids_present(self):
        ids = {r.id for r in self.spec.allophone_rules}
        assert {
            "AR_LEV_MONO_AY", "AR_LEV_MONO_AW",
            "AR_LEV_EMPH_BACK_A_AFTER", "AR_LEV_EMPH_BACK_AA_AFTER",
        } <= ids

    def test_mono_ay(self):
        """/aj/ → [eː] — Almbark & Hellmuth 2015 §1.1 (bajt~beːt)."""
        assert _ipa(self.CODE, "بَيْت") == "ˈbeːt"

    def test_mono_aw(self):
        """/aw/ → [oː] — Fadda 2016:30 (sˤawt → sˤoːtˤ)."""
        assert _ipa(self.CODE, "صَوْت") == "ˈsˤoːt"

    def test_emphatic_backing_aa(self):
        """/aː/ → [ɑː] next to an emphatic — Watson 2002 emphasis spreading."""
        assert _ipa(self.CODE, "صَار") == "ˈsˤɑːr"

    def test_plain_aa_not_backed(self):
        """Plain /aː/ stays [aː] in the proto-parent (no imāla here)."""
        assert _ipa(self.CODE, "بَاب") == "ˈbaːb"


# ─────────────────────────────────────────────────────────────────────────────
# Damascene — ar-SY
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.linguistic
class TestSyrianDamascene:
    CODE = "ar-SY"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_tier_research(self):
        assert self.spec.quality == "research"

    def test_qaf_glottal(self):
        """ق → [ʔ] (Damascus koine)."""
        assert _ipa(self.CODE, "قَلْب") == "ˈʔalb"

    def test_jim_zh(self):
        """ج → [ʒ]."""
        assert _ipa(self.CODE, "جَمَل") == "ˈʒamal"

    def test_interdental_to_stop(self):
        """ث → [t] (urban interdental merger)."""
        assert _ipa(self.CODE, "ثَلْج") == "ˈtalʒ"

    def test_mono_inherited(self):
        assert _ipa(self.CODE, "بَيْت") == "ˈbeːt"

    def test_no_strong_imala(self):
        """Damascene /aː/ is NOT raised (less fronted than Coastal; A&H 2015)."""
        assert _ipa(self.CODE, "بَاب") == "ˈbaːb"

    def test_parent(self):
        assert self.spec.parent == "ar-x-levantine"


# ─────────────────────────────────────────────────────────────────────────────
# Beiruti — ar-LB : strong imāla
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.linguistic
class TestLebaneseBeiruti:
    CODE = "ar-LB"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_tier_research(self):
        assert self.spec.quality == "research"

    def test_imala_rule_ids_present(self):
        ids = {r.id for r in self.spec.allophone_rules}
        assert {"LB_IMALA_RAISE_AA", "LB_IMALA_TAMARBUTA",
                "LB_IMALA_BLOCK_GUTT_BEFORE"} <= ids

    def test_strong_imala_raises_aa(self):
        """باب bāb → [beːb] — strong Lebanese imāla /aː/ → [eː]."""
        assert _ipa(self.CODE, "بَاب") == "ˈbeːb"

    def test_imala_blocked_by_guttural(self):
        """راح → [raːħ] — imāla blocked adjacent to a guttural /ħ/."""
        assert _ipa(self.CODE, "رَاح") == "ˈraːħ"

    def test_imala_blocked_by_emphatic(self):
        """صار → [sˤɑːr] — emphatic backing (inherited) bleeds imāla."""
        assert _ipa(self.CODE, "صَار") == "ˈsˤɑːr"

    def test_qaf_glottal(self):
        assert _ipa(self.CODE, "قَلْب") == "ˈʔalb"

    def test_mono_inherited(self):
        assert _ipa(self.CODE, "بَيْت") == "ˈbeːt"

    def test_imala_blocked_by_r(self):
        """مْبَارِح mbāriḥ → [mbaːriħ] — imāla blocked adjacent to /r/.

        The Beiruti blocking set is emphatic + guttural + /r/; /r/ was missing
        from the engine's block, so the /aː/ over-fronted (Cowell 1964)."""
        ids = {r.id for r in self.spec.allophone_rules}
        assert {"LB_IMALA_BLOCK_R_BEFORE", "LB_IMALA_BLOCK_R_AFTER"} <= ids
        assert _ipa(self.CODE, "مْبَارِح") == "ˈmbaːriħ"

    def test_tamarbuta_imala_blocked_by_guttural(self):
        """طَالْعَة ṭālʕa → [tˤɑːlʕa] — final -a imāla blocked after guttural /ʕ/."""
        assert "LB_IMALA_TAMARBUTA_BLOCK_GUTT" in {
            r.id for r in self.spec.allophone_rules}
        assert _ipa(self.CODE, "طَالْعَة") == "ˈtˤɑːlʕa"

    def test_function_words_do_not_front(self):
        """Negator مَا and preposition عَ keep /a/ (function words; Cowell 1964)."""
        assert _ipa(self.CODE, "مَا") == "ˈmaː"
        assert _ipa(self.CODE, "عَ") == "ˈʕa"

    def test_hayda_retains_diphthong(self):
        """هَيْدَا hayda keeps /aj/ lexically — no monophthong, no fronting."""
        assert _ipa(self.CODE, "هَيْدَا") == "ˈhajda"

    def test_final_short_a_no_imala(self):
        """بُكْرَا bukra, فَرَنْسَا faransa — final short -a takes no imāla."""
        assert _ipa(self.CODE, "بُكْرَا") == "ˈbukra"
        assert _ipa(self.CODE, "فَرَنْسَا") == "faˈransa"

    def test_article_il(self):
        """Beiruti definite article is /il/ before a moon letter (Cowell 1964)."""
        assert _ipa(self.CODE, "اَلْبَحْر") == "ilˈbaħr"
        assert _ipa(self.CODE, "الْجَاي") == "ilˈʒaːj"

    def test_article_al_before_guttural(self):
        """The article keeps /a/ before a guttural onset: الأكل → [alʔakil]."""
        assert _ipa(self.CODE, "الْأَكِل") == "ˈalʔakil"
        assert _ipa(self.CODE, "الْحَكِيم") == "alħaˈkiːm"

    def test_al_yawm_lexicalised(self):
        """'today' الْيَوم is the frozen adverb al-yōm, not il- (Cowell 1964)."""
        assert _ipa(self.CODE, "الْيَوم") == "alˈjoːm"

    def test_parent(self):
        assert self.spec.parent == "ar-x-levantine"


# ─────────────────────────────────────────────────────────────────────────────
# Ammani — ar-JO
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.linguistic
class TestJordanianAmmani:
    CODE = "ar-JO"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_tier_research(self):
        assert self.spec.quality == "research"

    def test_qaf_g_default(self):
        """ق → [ɡ] default (traditional Jordanian; Al-Wer 2020:560)."""
        assert _ipa(self.CODE, "قَلْب") == "ˈɡalb"

    def test_qaf_glottal_available(self):
        """[ʔ] is the second qaf variant (urban Ammani prestige)."""
        assert "ʔ" in (self.spec.graphemes.get("ق") or [])

    def test_jim_affricate_default(self):
        """ج → [dʒ] default; [ʒ] also available (Al-Wer 2020:560)."""
        assert _ipa(self.CODE, "جَمَل") == "ˈdʒamal"
        assert "ʒ" in (self.spec.graphemes.get("ج") or [])

    def test_mono_inherited(self):
        """/aj/ → [eː] (Fadda 2016:30, bajt → beːt)."""
        assert _ipa(self.CODE, "بَيْت") == "ˈbeːt"

    def test_parent(self):
        assert self.spec.parent == "ar-x-levantine"


# ─────────────────────────────────────────────────────────────────────────────
# Palestinian — ar-PS
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.linguistic
class TestPalestinian:
    CODE = "ar-PS"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_tier_research(self):
        assert self.spec.quality == "research"

    def test_qaf_glottal_default(self):
        """ق → [ʔ] default (urban Jerusalem koine)."""
        assert _ipa(self.CODE, "قَلْب") == "ˈʔalb"

    def test_qaf_four_way_split(self):
        """All four qaf reflexes present (Fadda 2016:28; Cotter 2016)."""
        vals = self.spec.graphemes.get("ق") or []
        for v in ("ʔ", "k", "ɡ", "q"):
            assert v in vals

    def test_kaf_palatalisation_variant(self):
        """ك → [tʃ] available (central-rural 'kaf shift')."""
        assert "tʃ" in (self.spec.graphemes.get("ك") or [])

    def test_jim_zh(self):
        assert _ipa(self.CODE, "جَمَل") == "ˈʒamal"

    def test_mono_inherited(self):
        assert _ipa(self.CODE, "صَوْت") == "ˈsˤoːt"

    def test_parent(self):
        assert self.spec.parent == "ar-x-levantine"
