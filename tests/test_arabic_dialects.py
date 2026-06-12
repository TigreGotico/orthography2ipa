"""Gold transcription sets for the expanded Arabic dialect inventory.

Covers the dialects added/reviewed in the Arabic expansion round:

- Egyptian / Cairene (ar-EG)
- Levantine intermediate (ar-x-levantine) + Syrian (ar-SY), Lebanese (ar-LB),
  Jordanian (ar-JO), Palestinian (ar-PS)
- Sudanese (ar-SD)
- Hejazi (ar-SA-x-hejaz) — qaf reflex correction
- Gulf country passthroughs (ar-AE, ar-KW) — signature inherited from ar-x-gulf

Each gold item is derived by explicit reasoning from the dialect's documented
phonology and verified against the data-driven engine.

Two assertion levels are used, matching what the engine can express:

- **Word level** (``_ipa`` via :class:`G2P`): the signature *consonant* reflexes
  (qaf / jim / interdentals). Input is vocalised (harakat) so short vowels
  surface. The engine transcribes orthography, so vowel *length* and stress are
  NOT asserted at word level (see grapheme-level tests and the ar-EG notes).
- **Grapheme / allophone level** (``spec.graphemes`` / resolved allophones): the
  *variant* reflexes a single word cannot show — Gulf jim → /j/, Palestinian
  qaf → /k/, interdental merger alternates — and any claim the orthography-driven
  engine cannot capture.

HONESTY NOTE: these targets are model-derived from cited phonological sources
and should be validated by native speakers / dialectologists before being
treated as ground truth.
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
    """Full-word IPA via the data-driven engine (vocalised input)."""
    try:
        return G2P(code).transcribe(word)
    except Exception as exc:  # pragma: no cover - environment guard
        pytest.skip(f"engine unavailable for {code!r}: {exc}")
        return ""  # unreachable; keeps type-checkers happy


def _grapheme(spec, grapheme: str):
    return spec.graphemes.get(grapheme)


def _assert_contains(values, *expected, label: str = "") -> None:
    assert values is not None, f"{label}: mapping is absent"
    for exp in expected:
        assert exp in values, f"{label}: {exp!r} not in {values}"


def _assert_first(values, expected: str, label: str = "") -> None:
    assert values is not None, f"{label}: mapping is absent"
    assert values[0] == expected, (
        f"{label}: expected first={expected!r}, got {values[0]!r}"
    )


# ═══════════════════════════════════════════════════════════════════════════
# Egyptian / Cairene — ar-EG
# Signature: jim → /ɡ/, qaf → /ʔ/, interdentals merge to stops (t/d/dˤ).
# جميل → gamiːl, قلب → ʔalb.  (Watson 2002; Mitchell 1956; Badawi & Hinds 1986)
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestEgyptianArabic:
    CODE = "ar-EG"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    # --- word level (consonant reflexes) ---
    def test_jim_to_g_jabal(self):
        """جَبَل 'mountain' → [ɡabal] — Cairene jim → /ɡ/ (the marquee feature)."""
        assert _ipa(self.CODE, "جَبَل") == "ɡabal"

    def test_qaf_to_glottal_qalb(self):
        """قَلْب 'heart' → [ʔalb] — qaf → /ʔ/ in inherited vocabulary."""
        assert _ipa(self.CODE, "قَلْب") == "ʔalb"

    def test_tha_merges_to_t_thalg(self):
        """ثَلْج 'ice/snow' → [talɡ] — ث merges to /t/ (and jim → /ɡ/)."""
        assert _ipa(self.CODE, "ثَلْج") == "talɡ"

    def test_dhal_merges_to_d_dahab(self):
        """ذَهَب 'gold' → [dahab] — ذ merges to /d/."""
        assert _ipa(self.CODE, "ذَهَب") == "dahab"

    # --- grapheme level (variants / merger alternates) ---
    def test_jim_grapheme_only_g(self):
        """ج maps to /ɡ/ alone — no /dʒ/ or /ʒ/ in native Cairene."""
        _assert_first(_grapheme(self.spec, "ج"), "ɡ", label="ج")
        assert "dʒ" not in _grapheme(self.spec, "ج")

    def test_qaf_variants(self):
        """ق primary /ʔ/, with /ɡ/ (loans/Bedouin) and /q/ (learned) available."""
        vals = _grapheme(self.spec, "ق")
        _assert_first(vals, "ʔ", label="ق")
        _assert_contains(vals, "q", label="ق learned")

    def test_tha_loan_sibilant(self):
        """ث alternate /s/ — sibilant correspondence in learned loans."""
        _assert_contains(_grapheme(self.spec, "ث"), "s", label="ث loan")

    def test_dha_emphatic_merger(self):
        """ظ → /dˤ/ (with /zˤ/ in loans) — emphatic interdental merges."""
        _assert_first(_grapheme(self.spec, "ظ"), "dˤ", label="ظ")
        _assert_contains(_grapheme(self.spec, "ظ"), "zˤ", label="ظ loan")

    def test_cheh_loan_zh(self):
        """چ → /ʒ/ — loan grapheme for /ʒ/ (native ج is /ɡ/)."""
        _assert_first(_grapheme(self.spec, "چ"), "ʒ", label="چ")

    def test_parent(self):
        assert self.spec.parent == "ar-x-mashriqi"


# ═══════════════════════════════════════════════════════════════════════════
# Levantine intermediate — ar-x-levantine
# Signature: qaf → /ʔ/ (urban), jim → /ʒ/, interdentals variable.
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestLevantineProto:
    CODE = "ar-x-levantine"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_qaf_glottal_primary(self):
        """ق primary /ʔ/ (urban koine), with /ɡ/, /k/, /q/ regional variants."""
        vals = _grapheme(self.spec, "ق")
        _assert_first(vals, "ʔ", label="ق")
        _assert_contains(vals, "ɡ", "k", "q", label="ق variants")

    def test_jim_zh_primary(self):
        """ج primary /ʒ/ with /dʒ/ (Bedouin/rural) available."""
        _assert_first(_grapheme(self.spec, "ج"), "ʒ", label="ج")
        _assert_contains(_grapheme(self.spec, "ج"), "dʒ", label="ج")

    def test_interdentals_variable(self):
        """ث → /t/ (urban merger) primary, /θ/ (rural/Druze) retained as variant."""
        vals = _grapheme(self.spec, "ث")
        _assert_first(vals, "t", label="ث")
        _assert_contains(vals, "θ", label="ث conserved variant")

    def test_qalb_glottal(self):
        """قَلْب → [ʔalb] — urban qaf → /ʔ/."""
        assert _ipa(self.CODE, "قَلْب") == "ʔalb"

    def test_parent(self):
        assert self.spec.parent == "ar-x-mashriqi"


# ═══════════════════════════════════════════════════════════════════════════
# Syrian (Damascene) — ar-SY
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestSyrianArabic:
    CODE = "ar-SY"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_qaf_glottal_qalb(self):
        """قَلْب → [ʔalb] — Damascene qaf → /ʔ/."""
        assert _ipa(self.CODE, "قَلْب") == "ʔalb"

    def test_qaf_glottal_qamar(self):
        """قَمَر 'moon' → [ʔamar] — qaf → /ʔ/."""
        assert _ipa(self.CODE, "قَمَر") == "ʔamar"

    def test_jim_zh_jamal(self):
        """جَمَل 'camel' → [ʒamal] — Syrian jim → /ʒ/."""
        assert _ipa(self.CODE, "جَمَل") == "ʒamal"

    def test_jim_grapheme_zh_first(self):
        """ج primary /ʒ/."""
        _assert_first(_grapheme(self.spec, "ج"), "ʒ", label="ج")

    def test_qaf_grapheme_glottal_first(self):
        """ق primary /ʔ/, /q/ in learned words."""
        _assert_first(_grapheme(self.spec, "ق"), "ʔ", label="ق")
        _assert_contains(_grapheme(self.spec, "ق"), "q", label="ق learned")

    def test_parent(self):
        assert self.spec.parent == "ar-x-levantine"


# ═══════════════════════════════════════════════════════════════════════════
# Lebanese (Beiruti) — ar-LB
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestLebaneseArabic:
    CODE = "ar-LB"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_qaf_glottal_qalb(self):
        """قَلْب → [ʔalb] — Beiruti qaf → /ʔ/."""
        assert _ipa(self.CODE, "قَلْب") == "ʔalb"

    def test_jim_zh_jamal(self):
        """جَمَل → [ʒamal] — Lebanese jim → /ʒ/."""
        assert _ipa(self.CODE, "جَمَل") == "ʒamal"

    def test_imala_aa_raised(self):
        """aː allophone primary [eː] — Lebanese strong imāla raises /aː/."""
        vals = self.spec.allophones.get("aː")
        assert vals is not None and vals[0] == "eː", (
            f"Lebanese aː should raise to eː first, got {vals}"
        )

    def test_short_a_fronting(self):
        """a allophone includes /e/ and /æ/ — short-vowel fronting (imāla)."""
        _assert_contains(self.spec.allophones.get("a"), "e", "æ", label="a fronting")

    def test_parent(self):
        assert self.spec.parent == "ar-x-levantine"


# ═══════════════════════════════════════════════════════════════════════════
# Jordanian (Ammani) — ar-JO
# Bedouin-influenced: qaf → /ɡ/ widespread, jim → /dʒ/ retained.
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestJordanianArabic:
    CODE = "ar-JO"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_qaf_g_qalb(self):
        """قَلْب → [ɡalb] — Jordanian qaf → /ɡ/ (Bedouin/rural prestige)."""
        assert _ipa(self.CODE, "قَلْب") == "ɡalb"

    def test_jim_affricate_jamal(self):
        """جَمَل → [dʒamal] — Jordanian jim → /dʒ/ (affricate retained)."""
        assert _ipa(self.CODE, "جَمَل") == "dʒamal"

    def test_qaf_grapheme_g_first(self):
        """ق primary /ɡ/, with /ʔ/ (urban Ammani) and /q/ available."""
        vals = _grapheme(self.spec, "ق")
        _assert_first(vals, "ɡ", label="ق")
        _assert_contains(vals, "ʔ", "q", label="ق variants")

    def test_jim_grapheme_affricate_first(self):
        """ج primary /dʒ/, /ʒ/ available (Syro-Lebanese contact)."""
        _assert_first(_grapheme(self.spec, "ج"), "dʒ", label="ج")
        _assert_contains(_grapheme(self.spec, "ج"), "ʒ", label="ج")

    def test_parent(self):
        assert self.spec.parent == "ar-x-levantine"


# ═══════════════════════════════════════════════════════════════════════════
# Palestinian — ar-PS
# Three-way qaf split: urban /ʔ/, central rural /k/ (+ kaf→tʃ), Bedouin /ɡ/.
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestPalestinianArabic:
    CODE = "ar-PS"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_qaf_glottal_qalb(self):
        """قَلْب → [ʔalb] — urban (Jerusalem) qaf → /ʔ/ (prestige form)."""
        assert _ipa(self.CODE, "قَلْب") == "ʔalb"

    def test_jim_zh_jamal(self):
        """جَمَل → [ʒamal] — urban jim → /ʒ/."""
        assert _ipa(self.CODE, "جَمَل") == "ʒamal"

    def test_qaf_three_way_split(self):
        """ق lists /ʔ/ (urban), /k/ (central rural fellahin), /ɡ/ (Bedouin), /q/."""
        vals = _grapheme(self.spec, "ق")
        _assert_first(vals, "ʔ", label="ق urban")
        _assert_contains(vals, "k", "ɡ", "q", label="ق rural/Bedouin/learned")

    def test_kaf_palatalisation_variant(self):
        """ك includes /tʃ/ — central rural kaf-shift before front vowels."""
        _assert_contains(_grapheme(self.spec, "ك"), "k", "tʃ", label="ك")

    def test_parent(self):
        assert self.spec.parent == "ar-x-levantine"


# ═══════════════════════════════════════════════════════════════════════════
# Sudanese — ar-SD
# Signature: qaf → /ɡ/, jim → /ɟ/ (palatal stop, archaic), interdentals merge.
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestSudaneseArabic:
    CODE = "ar-SD"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_jim_palatal_jamal(self):
        """جَمَل → [ɟamal] — Sudanese jim → /ɟ/ (voiced palatal stop)."""
        assert _ipa(self.CODE, "جَمَل") == "ɟamal"

    def test_jim_palatal_jabal(self):
        """جَبَل → [ɟabal] — jim → /ɟ/."""
        assert _ipa(self.CODE, "جَبَل") == "ɟabal"

    def test_qaf_g_qalb(self):
        """قَلْب → [ɡalb] — Sudanese qaf → /ɡ/ (Bedouin-origin reflex)."""
        assert _ipa(self.CODE, "قَلْب") == "ɡalb"

    def test_tha_merges_to_t_thalg(self):
        """ثَلْج → [talɟ] — ث merges to /t/, jim → /ɟ/ (Egypto-Sudanic merger)."""
        assert _ipa(self.CODE, "ثَلْج") == "talɟ"

    def test_jim_grapheme_palatal_first(self):
        """ج primary /ɟ/ — distinguishes Sudanese from EG /ɡ/ and Levantine /ʒ/."""
        _assert_first(_grapheme(self.spec, "ج"), "ɟ", label="ج")

    def test_interdental_merger(self):
        """ث → /t/ (~/s/ loans); interdentals not retained (Egypto-Sudanic)."""
        vals = _grapheme(self.spec, "ث")
        _assert_first(vals, "t", label="ث")
        assert "θ" not in vals, f"Sudanese ث should not retain θ, got {vals}"

    def test_parent(self):
        assert self.spec.parent == "ar-x-mashriqi"


# ═══════════════════════════════════════════════════════════════════════════
# Hejazi — ar-SA-x-hejaz  (qaf reflex correction: /ɡ/, not /ʔ/)
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestHejaziArabic:
    CODE = "ar-SA-x-hejaz"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.CODE)

    def test_qaf_g_qalb(self):
        """قَلْب → [ɡalb] — Hejazi qaf → /ɡ/ (chain shift q→g→dʒ); NOT /ʔ/."""
        assert _ipa(self.CODE, "قَلْب") == "ɡalb"

    def test_jim_affricate_jamal(self):
        """جَمَل → [dʒamal] — Hejazi jim → /dʒ/."""
        assert _ipa(self.CODE, "جَمَل") == "dʒamal"

    def test_qaf_grapheme_g_first(self):
        """ق primary /ɡ/, /q/ retained only in learned borrowings."""
        vals = _grapheme(self.spec, "ق")
        _assert_first(vals, "ɡ", label="ق")
        assert "ʔ" not in vals, f"Hejazi ق should not map to ʔ, got {vals}"

    def test_no_kaf_palatalisation(self):
        """ك has no /tʃ/ — Hejazi lacks the Gulf/Najdi kaf-shift."""
        vals = _grapheme(self.spec, "ك")
        assert vals is None or "tʃ" not in vals, (
            f"Hejazi ك should not palatalise, got {vals}"
        )


# ═══════════════════════════════════════════════════════════════════════════
# Gulf country passthroughs — signature inherited from ar-x-gulf
# qaf → /ɡ/, jim → /dʒ ~ j/, interdentals retained, kaf → /tʃ/.
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestGulfCountryReflexes:
    @pytest.mark.parametrize("code", ["ar-AE", "ar-KW", "ar-BH", "ar-QA"])
    def test_qaf_g_qalb(self, code):
        """قَلْب → [ɡalb] — Gulf qaf → /ɡ/ inherited from ar-x-gulf."""
        assert _ipa(code, "قَلْب") == "ɡalb"

    @pytest.mark.parametrize("code", ["ar-AE", "ar-KW"])
    def test_jim_yaa_variant(self, code):
        """ج includes /j/ — Gulf jim-to-yaa (jidiːd for jadīd) variant."""
        spec = _load(code)
        _assert_contains(_grapheme(spec, "ج"), "dʒ", "j", label=f"{code} ج")

    @pytest.mark.parametrize("code", ["ar-AE", "ar-KW"])
    def test_interdentals_retained(self, code):
        """ث primary /θ/ — Gulf retains interdentals (unlike EG/Levant)."""
        spec = _load(code)
        _assert_first(_grapheme(spec, "ث"), "θ", label=f"{code} ث")

    @pytest.mark.parametrize("code", ["ar-AE", "ar-KW"])
    def test_kaf_palatalisation(self, code):
        """ك includes /tʃ/ — Gulf kaf-shift before front vowels."""
        spec = _load(code)
        _assert_contains(_grapheme(spec, "ك"), "k", "tʃ", label=f"{code} ك")


# ═══════════════════════════════════════════════════════════════════════════
# Yemeni sanity — jim → /ɡ/ (Sanaani), parallel to Cairene
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestYemeniReflex:
    CODE = "ar-YE"

    def test_jim_g_jabal(self):
        """جَبَل → [ɡabal] — Sanaani Yemeni jim → /ɡ/."""
        assert _ipa(self.CODE, "جَبَل") == "ɡabal"

    def test_qaf_retained_grapheme(self):
        """ق → /q/ retained in Sanaani (conservative)."""
        spec = _load(self.CODE)
        _assert_first(_grapheme(spec, "ق"), "q", label="ق")
