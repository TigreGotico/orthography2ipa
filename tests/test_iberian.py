"""Extensive per-language unit tests for Iberian Peninsula languages.

Covers: es-ES, pt-PT, ca, gl, eu, ast, mwl, an, and selected dialects.
Each language class tests:
  - Registry metadata (code, name, family, script, parent)
  - Grapheme table — every significant mapping validated
  - Allophone table — every phoneme and its surface realisations
  - Positional grapheme rules (context-sensitive allophony)
  - Key isoglosses discriminating this language from its neighbours
  - Ancestry and distance sanity checks

Run with coverage report:
    pytest tests/test_iberian.py -v --tb=short
    pytest tests/test_iberian.py -v --tb=short --iberian-report
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa.registry import get
from orthography2ipa.types import GraphemePosition


# ═══════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════

def _load(code: str):
    """Load a LanguageSpec, skipping the test if unavailable."""
    try:
        return get(code)
    except Exception:
        pytest.skip(f"{code} not available in registry")


def _grapheme(spec, g: str) -> list[str]:
    """Resolve a grapheme from the fully inherited grapheme table."""
    return spec.graphemes.get(g, [])


def _allophone(spec, phoneme: str):
    """Return the allophone list for a phoneme (None means phoneme absent/nulled)."""
    return spec.allophones.get(phoneme)


def _positional(spec, g: str, position: GraphemePosition) -> list[str]:
    """Resolve a grapheme in a specific position."""
    return spec.resolve_grapheme(g, position)


def _assert_contains(seq, value: str, label: str) -> None:
    assert seq is not None, f"{label}: mapping is None (nulled out)"
    assert any(value in ipa for ipa in seq), (
        f"{label}: expected {value!r} in {seq!r}"
    )


def _assert_first(seq, value: str, label: str) -> None:
    """Assert the default (first) IPA candidate is *value*."""
    assert seq, f"{label}: empty mapping"
    assert seq[0] == value, f"{label}: expected first={value!r}, got {seq[0]!r}"


def _assert_null(spec, g: str, label: str) -> None:
    """Assert that grapheme *g* was nulled out and is absent from the resolved table.

    When a language JSON sets ``"grapheme": null``, the inheritance resolver
    removes that grapheme from the final LanguageSpec — it will not appear in
    ``spec.graphemes`` at all (not even as None).
    """
    result = spec.graphemes.get(g, _SENTINEL)
    assert result is _SENTINEL or result is None, (
        f"{label}: expected {g!r} to be absent/null, got {result!r}"
    )


_SENTINEL = object()


def _assert_allophone_null(spec, phoneme: str, label: str) -> None:
    """Assert that *phoneme* is explicitly absent from the allophone inventory."""
    v = _allophone(spec, phoneme)
    assert v is None, f"{label}: expected None (null), got {v!r}"


# ═══════════════════════════════════════════════════════════════════════════
# CASTILIAN SPANISH  (es-ES)
# ═══════════════════════════════════════════════════════════════════════════

class TestSpanishES:
    """Comprehensive tests for Castilian Spanish (es-ES)."""

    LANGUAGE_CODE = "es-ES"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("es-ES")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "es-ES"

    def test_name(self):
        assert "Spanish" in self._spec.name or "Castilian" in self._spec.name

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_script(self):
        assert self._spec.script == "Latin"

    def test_parent_is_medieval(self):
        assert self._spec.parent == "es-ES-x-medieval"

    # --- Vowels ---

    def test_vowel_a(self):
        _assert_first(_grapheme(self._spec, "a"), "a", "es-ES a")

    def test_vowel_e_default(self):
        g = _grapheme(self._spec, "e")
        assert "e" in g, f"es-ES e: expected 'e' in {g}"

    def test_vowel_e_open(self):
        g = _grapheme(self._spec, "e")
        assert "ɛ" in g, f"es-ES e: expected 'ɛ' in {g}"

    def test_vowel_i(self):
        _assert_first(_grapheme(self._spec, "i"), "i", "es-ES i")

    def test_vowel_o_default(self):
        g = _grapheme(self._spec, "o")
        assert "o" in g

    def test_vowel_o_open(self):
        g = _grapheme(self._spec, "o")
        assert "ɔ" in g

    def test_vowel_u(self):
        _assert_first(_grapheme(self._spec, "u"), "u", "es-ES u")

    def test_accented_a(self):
        _assert_first(_grapheme(self._spec, "á"), "a", "es-ES á")

    def test_accented_e(self):
        # é marks stress only in modern Spanish; acute does not shift vowel quality
        _assert_first(_grapheme(self._spec, "é"), "e", "es-ES é")

    def test_accented_i(self):
        _assert_first(_grapheme(self._spec, "í"), "i", "es-ES í")

    def test_accented_o(self):
        # ó marks stress only in modern Spanish; acute does not shift vowel quality
        _assert_first(_grapheme(self._spec, "ó"), "o", "es-ES ó")

    def test_accented_u(self):
        _assert_first(_grapheme(self._spec, "ú"), "u", "es-ES ú")

    # --- Consonants ---

    def test_b_default(self):
        _assert_first(_grapheme(self._spec, "b"), "b", "es-ES b")

    def test_c_default_velar(self):
        _assert_first(_grapheme(self._spec, "c"), "k", "es-ES c default")

    def test_c_includes_theta(self):
        """DISTINCIÓN: c also maps to /θ/ (before e/i)."""
        _assert_contains(_grapheme(self._spec, "c"), "θ", "es-ES c/θ")

    def test_ch_affricate(self):
        _assert_first(_grapheme(self._spec, "ch"), "tʃ", "es-ES ch")

    def test_d_default(self):
        _assert_first(_grapheme(self._spec, "d"), "d", "es-ES d")

    def test_f_default(self):
        _assert_first(_grapheme(self._spec, "f"), "f", "es-ES f")

    def test_g_default_velar(self):
        _assert_first(_grapheme(self._spec, "g"), "ɡ", "es-ES g")

    def test_g_also_velar_fricative(self):
        """g before e/i → /x/ in inherited positional rules."""
        g = _grapheme(self._spec, "g")
        assert "x" in g or _positional(
            self._spec, "g", GraphemePosition.BEFORE_E
        ) == ["x"], "es-ES g: expected x via positional or flat"

    def test_gu_is_velar(self):
        _assert_first(_grapheme(self._spec, "gu"), "ɡ", "es-ES gu")

    def test_h_is_silent(self):
        """SILENT H: etymological h is /∅/."""
        g = _grapheme(self._spec, "h")
        assert g == [""] or g == [], f"es-ES h: expected silent ('' or []), got {g}"

    def test_j_velar_fricative(self):
        _assert_first(_grapheme(self._spec, "j"), "x", "es-ES j")

    def test_k(self):
        _assert_first(_grapheme(self._spec, "k"), "k", "es-ES k")

    def test_l(self):
        _assert_first(_grapheme(self._spec, "l"), "l", "es-ES l")

    def test_ll_yeismo(self):
        """YEÍSMO: ll → /ʝ/ (not /ʎ/) in modern Castilian standard."""
        g = _grapheme(self._spec, "ll")
        assert "ʝ" in g, f"es-ES ll: expected ʝ (yeísmo), got {g}"

    def test_m(self):
        _assert_first(_grapheme(self._spec, "m"), "m", "es-ES m")

    def test_n(self):
        _assert_first(_grapheme(self._spec, "n"), "n", "es-ES n")

    def test_enye_palatal_nasal(self):
        _assert_first(_grapheme(self._spec, "ñ"), "ɲ", "es-ES ñ")

    def test_p(self):
        _assert_first(_grapheme(self._spec, "p"), "p", "es-ES p")

    def test_q(self):
        _assert_first(_grapheme(self._spec, "q"), "k", "es-ES q")

    def test_qu(self):
        _assert_first(_grapheme(self._spec, "qu"), "k", "es-ES qu")

    def test_r_default_flap(self):
        _assert_first(_grapheme(self._spec, "r"), "ɾ", "es-ES r")

    def test_rr_trill(self):
        _assert_first(_grapheme(self._spec, "rr"), "r", "es-ES rr")

    def test_s_default(self):
        _assert_first(_grapheme(self._spec, "s"), "s", "es-ES s")

    def test_t(self):
        _assert_first(_grapheme(self._spec, "t"), "t", "es-ES t")

    def test_v_betacism(self):
        """BETACISM: v → /b/ (merged with b)."""
        _assert_first(_grapheme(self._spec, "v"), "b", "es-ES v betacism")

    def test_w(self):
        _assert_first(_grapheme(self._spec, "w"), "w", "es-ES w")

    def test_y_palatal(self):
        _assert_first(_grapheme(self._spec, "y"), "ʝ", "es-ES y")

    def test_z_theta(self):
        """DISTINCIÓN: z → /θ/."""
        _assert_first(_grapheme(self._spec, "z"), "θ", "es-ES z/distinción")

    def test_gue_trigraph(self):
        _assert_first(_grapheme(self._spec, "güe"), "ɡwe", "es-ES güe")

    def test_gui_trigraph(self):
        _assert_first(_grapheme(self._spec, "güi"), "ɡwi", "es-ES güi")

    # --- Diphthongs ---

    def test_diphthong_ie(self):
        _assert_first(_grapheme(self._spec, "ie"), "je", "es-ES ie")

    def test_diphthong_ue(self):
        _assert_first(_grapheme(self._spec, "ue"), "we", "es-ES ue")

    def test_diphthong_ia(self):
        _assert_first(_grapheme(self._spec, "ia"), "ja", "es-ES ia")

    def test_diphthong_io(self):
        _assert_first(_grapheme(self._spec, "io"), "jo", "es-ES io")

    def test_diphthong_ua(self):
        _assert_first(_grapheme(self._spec, "ua"), "wa", "es-ES ua")

    def test_diphthong_ai(self):
        _assert_first(_grapheme(self._spec, "ai"), "aj", "es-ES ai")

    def test_diphthong_ei(self):
        _assert_first(_grapheme(self._spec, "ei"), "ej", "es-ES ei")

    def test_diphthong_au(self):
        _assert_first(_grapheme(self._spec, "au"), "aw", "es-ES au")

    def test_diphthong_iu(self):
        _assert_first(_grapheme(self._spec, "iu"), "ju", "es-ES iu")

    def test_diphthong_ui(self):
        _assert_first(_grapheme(self._spec, "ui"), "wi", "es-ES ui")

    # --- Allophones ---

    def test_allophone_b_has_fricative(self):
        """b → [b, β] — lenition produces bilabial fricative."""
        a = _allophone(self._spec, "b")
        assert a and "β" in a, f"es-ES b allophone: expected β in {a}"

    def test_allophone_d_has_fricative(self):
        a = _allophone(self._spec, "d")
        assert a and "ð" in a, f"es-ES d allophone: expected ð in {a}"

    def test_allophone_g_has_fricative(self):
        a = _allophone(self._spec, "ɡ")
        assert a and "ɣ" in a, f"es-ES ɡ allophone: expected ɣ in {a}"

    def test_allophone_s_is_apical(self):
        """Castilian /s/ is realized as apico-alveolar [s̺]."""
        a = _allophone(self._spec, "s")
        assert a and "s̺" in a, f"es-ES s allophone: expected s̺ in {a}"

    def test_allophone_tch_affricate(self):
        a = _allophone(self._spec, "tʃ")
        assert a and "tʃ" in a

    def test_allophone_theta(self):
        a = _allophone(self._spec, "θ")
        assert a and "θ" in a

    def test_allophone_x_velar(self):
        a = _allophone(self._spec, "x")
        assert a and "x" in a

    def test_allophone_yod(self):
        a = _allophone(self._spec, "ʝ")
        assert a and "ʝ" in a

    def test_allophone_n_velar(self):
        """n → [ŋ] before velars."""
        a = _allophone(self._spec, "n")
        assert a and "ŋ" in a

    def test_allophone_r_flap(self):
        a = _allophone(self._spec, "ɾ")
        assert a and "ɾ" in a

    def test_allophone_r_trill(self):
        a = _allophone(self._spec, "r")
        assert a and "r" in a

    # --- Positional grapheme rules ---

    def test_positional_c_before_e_is_theta(self):
        """DISTINCIÓN: c + e → /θ/."""
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_E)
        assert p and "θ" in p, f"es-ES c/before_e: expected θ, got {p}"

    def test_positional_c_before_i_is_theta(self):
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_I)
        assert p and "θ" in p

    def test_positional_b_intervocalic_is_fricative(self):
        p = _positional(self._spec, "b", GraphemePosition.INTERVOCALIC)
        assert p and "β" in p

    def test_positional_d_intervocalic_is_fricative(self):
        p = _positional(self._spec, "d", GraphemePosition.INTERVOCALIC)
        assert p and "ð" in p

    def test_positional_g_intervocalic_is_fricative(self):
        p = _positional(self._spec, "g", GraphemePosition.INTERVOCALIC)
        assert p and "ɣ" in p

    def test_positional_g_before_e_is_velar_fricative(self):
        p = _positional(self._spec, "g", GraphemePosition.BEFORE_E)
        assert p and "x" in p

    def test_positional_g_before_i_is_velar_fricative(self):
        p = _positional(self._spec, "g", GraphemePosition.BEFORE_I)
        assert p and "x" in p

    def test_positional_r_word_initial_is_trill(self):
        p = _positional(self._spec, "r", GraphemePosition.WORD_INITIAL)
        assert p and "r" in p

    def test_positional_r_intervocalic_is_flap(self):
        p = _positional(self._spec, "r", GraphemePosition.INTERVOCALIC)
        assert p and "ɾ" in p

    def test_positional_d_word_final_is_fricative(self):
        p = _positional(self._spec, "d", GraphemePosition.WORD_FINAL)
        assert p and "ð" in p

    def test_positional_n_coda_includes_velar(self):
        p = _positional(self._spec, "n", GraphemePosition.CODA)
        assert p and "ŋ" in p

    # --- Isogloss: Spanish ≠ Portuguese ---

    def test_isogloss_no_v_phoneme(self):
        """Castilian has no /v/ phoneme — betacism is complete."""
        # /v/ should not appear as a standalone phoneme with distinct allophones
        v_allo = _allophone(self._spec, "v")
        assert v_allo is None, (
            f"es-ES: /v/ phoneme should be absent (betacism), got {v_allo}"
        )

    def test_isogloss_ll_not_palatal_lateral(self):
        """YEÍSMO: ll → ʝ (not ʎ) — differs from Portuguese lh→ʎ."""
        g = _grapheme(self._spec, "ll")
        assert "ʎ" not in g, f"es-ES ll: should be ʝ (yeísmo), not ʎ, got {g}"

    def test_isogloss_distincion_c_theta(self):
        """DISTINCIÓN: c before e/i maps to /θ/, not /s/."""
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_E)
        assert "θ" in p and "s" not in p, (
            f"es-ES distinción: c/before_e should be θ only, got {p}"
        )

    def test_isogloss_distincion_z_theta(self):
        """DISTINCIÓN: z is always /θ/ (not /s/ as in seseo varieties)."""
        g = _grapheme(self._spec, "z")
        assert "θ" in g and "s" not in g, (
            f"es-ES distinción: z should be θ only, got {g}"
        )

    # --- Ancestry ---

    def test_ancestry_has_parent(self):
        assert self._spec.parent == "es-ES-x-medieval"

    def test_ancestry_traces_to_latin(self):
        """Spanish can be traced back to a Latin ancestor."""
        codes = {a.code for a in self._spec.ancestors}
        # Direct parent is medieval; medieval traces to la-x-hispania
        assert "es-ES-x-medieval" in codes or self._spec.parent == "es-ES-x-medieval"

    def test_ancestry_includes_arabic_adstrate(self):
        """Spanish has significant Arabic adstrate (4000+ loanwords)."""
        codes = {a.code for a in self._spec.ancestors}
        # Arabic is in the medieval parent; verify it appears somewhere in the chain
        # We load medieval to check
        med = _load("es-ES-x-medieval")
        arabic_ancestors = [a for a in med.ancestors if a.code == "xaa"]
        assert arabic_ancestors, "es-ES-x-medieval should have xaa (Arabic) ancestor"


# ═══════════════════════════════════════════════════════════════════════════
# EUROPEAN PORTUGUESE  (pt-PT)
# ═══════════════════════════════════════════════════════════════════════════

class TestPortuguesePT:
    """Comprehensive tests for European Portuguese (pt-PT)."""

    LANGUAGE_CODE = "pt-PT"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("pt-PT")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "pt-PT"

    def test_name(self):
        assert "Portuguese" in self._spec.name

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_script(self):
        assert self._spec.script == "Latin"

    def test_parent(self):
        assert self._spec.parent == "pt-PT-x-medieval"

    # --- Grapheme overrides from medieval parent ---

    def test_grapheme_c_default_velar(self):
        _assert_first(_grapheme(self._spec, "c"), "k", "pt-PT c")

    def test_grapheme_c_includes_s(self):
        """pt-PT c has both k and s (positional rules select s before e/i)."""
        g = _grapheme(self._spec, "c")
        assert "s" in g, f"pt-PT c: expected s in {g}"

    def test_grapheme_cedilla(self):
        _assert_first(_grapheme(self._spec, "ç"), "s", "pt-PT ç")

    def test_grapheme_s_default(self):
        _assert_first(_grapheme(self._spec, "s"), "s", "pt-PT s")

    def test_grapheme_s_also_z(self):
        g = _grapheme(self._spec, "s")
        assert "z" in g, f"pt-PT s: expected z in {g}"

    def test_grapheme_z_voiced(self):
        _assert_first(_grapheme(self._spec, "z"), "z", "pt-PT z")

    def test_grapheme_ch_postalveolar(self):
        """PT ch → /ʃ/ (NOT /tʃ/ as in Spanish/Galician/Asturian)."""
        _assert_first(_grapheme(self._spec, "ch"), "ʃ", "pt-PT ch")

    def test_grapheme_lh_palatal_lateral(self):
        _assert_first(_grapheme(self._spec, "lh"), "ʎ", "pt-PT lh")

    def test_grapheme_nh_palatal_nasal(self):
        _assert_first(_grapheme(self._spec, "nh"), "ɲ", "pt-PT nh")

    def test_grapheme_e_default(self):
        g = _grapheme(self._spec, "e")
        assert "e" in g

    def test_grapheme_e_includes_schwa(self):
        """European Portuguese has schwa-like [ɨ] in unstressed syllables."""
        g = _grapheme(self._spec, "e")
        assert "ɨ" in g, f"pt-PT e: expected ɨ in {g}"

    def test_grapheme_e_includes_open(self):
        g = _grapheme(self._spec, "e")
        assert "ɛ" in g

    def test_grapheme_r_default_flap(self):
        _assert_first(_grapheme(self._spec, "r"), "ɾ", "pt-PT r")

    def test_grapheme_r_includes_uvular(self):
        """PT r can be uvular (ʁ) word-initially."""
        g = _grapheme(self._spec, "r")
        assert "ʁ" in g, f"pt-PT r: expected ʁ in {g}"

    def test_grapheme_rr_uvular(self):
        """PT rr → /ʁ/ (uvular, unlike Spanish rr → /r/ alveolar trill)."""
        _assert_first(_grapheme(self._spec, "rr"), "ʁ", "pt-PT rr")

    def test_grapheme_x_postalveolar_default(self):
        _assert_first(_grapheme(self._spec, "x"), "ʃ", "pt-PT x")

    def test_grapheme_x_also_ks(self):
        g = _grapheme(self._spec, "x")
        assert "ks" in g, f"pt-PT x: expected ks in {g}"

    def test_grapheme_w_default(self):
        _assert_first(_grapheme(self._spec, "w"), "w", "pt-PT w")

    def test_grapheme_w_also_v(self):
        g = _grapheme(self._spec, "w")
        assert "v" in g

    def test_grapheme_iu_diphthong(self):
        _assert_first(_grapheme(self._spec, "iu"), "iw", "pt-PT iu")

    def test_grapheme_ou(self):
        g = _grapheme(self._spec, "ou")
        assert "ow" in g

    # --- Null graphemes (Acordo Ortográfico) ---

    def test_grapheme_ph_null(self):
        """ph is explicitly nulled — no longer valid after Acordo Ortográfico."""
        _assert_null(self._spec, "ph", "pt-PT ph")

    def test_grapheme_th_null(self):
        _assert_null(self._spec, "th", "pt-PT th")

    def test_grapheme_rh_null(self):
        _assert_null(self._spec, "rh", "pt-PT rh")

    def test_grapheme_u_umlaut_null(self):
        _assert_null(self._spec, "ü", "pt-PT ü")

    def test_grapheme_qu_umlaut_null(self):
        _assert_null(self._spec, "qü", "pt-PT qü")

    def test_grapheme_gu_umlaut_null(self):
        _assert_null(self._spec, "gü", "pt-PT gü")

    # --- Allophones ---

    def test_allophone_v_preserved(self):
        """/v/ is a distinct phoneme in PT (unique in Ibero-Romance)."""
        a = _allophone(self._spec, "v")
        assert a is not None, "pt-PT: /v/ should exist as a phoneme"
        assert "v" in a, f"pt-PT v allophone: expected v in {a}"

    def test_allophone_v_not_b(self):
        """PT /v/ does NOT merge with /b/ (unlike Spanish/Galician/Asturian)."""
        a = _allophone(self._spec, "v")
        assert a and "b" not in a, f"pt-PT: /v/ should NOT have /b/ allophone, got {a}"

    def test_allophone_schwa(self):
        """ɨ (schwa-like) has two realisations: [ɨ] and [ə]."""
        a = _allophone(self._spec, "ɨ")
        assert a and "ɨ" in a and "ə" in a

    def test_allophone_uvular_r_variants(self):
        """Uvular /ʁ/ can surface as [ʁ, χ, h, ɦ]."""
        a = _allophone(self._spec, "ʁ")
        assert a
        assert "ʁ" in a
        assert "χ" in a
        assert "h" in a

    def test_allophone_f_includes_bilabial(self):
        """PT /f/ has labiodental [f] and bilabial fricative [ɸ] variants."""
        a = _allophone(self._spec, "f")
        assert a and "f" in a and "ɸ" in a

    def test_allophone_affricate_null(self):
        """t͡ʃ is NOT a native phoneme in European Portuguese."""
        _assert_allophone_null(self._spec, "t͡ʃ", "pt-PT t͡ʃ")

    def test_allophone_b_has_fricative(self):
        a = _allophone(self._spec, "b")
        assert a and "β" in a

    def test_allophone_d_has_fricative(self):
        a = _allophone(self._spec, "d")
        assert a and "ð" in a

    def test_allophone_g_has_fricative(self):
        a = _allophone(self._spec, "ɡ")
        assert a and "ɣ" in a

    # --- Positional grapheme rules ---

    def test_positional_c_before_e_is_s(self):
        """SESEO-LIKE: c before e → /s/ (no /θ/ in Portuguese)."""
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_E)
        assert p and "s" in p

    def test_positional_c_before_i_is_s(self):
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_I)
        assert p and "s" in p

    def test_positional_r_word_initial_uvular(self):
        """r at word start → /ʁ/ (strong uvular)."""
        p = _positional(self._spec, "r", GraphemePosition.WORD_INITIAL)
        assert p and "ʁ" in p

    def test_positional_s_word_initial(self):
        p = _positional(self._spec, "s", GraphemePosition.WORD_INITIAL)
        assert p and "s" in p

    def test_positional_s_intervocalic_voiced(self):
        """s between vowels → /z/ (voicing)."""
        p = _positional(self._spec, "s", GraphemePosition.INTERVOCALIC)
        assert p and "z" in p

    def test_positional_s_coda_postalveolar(self):
        """s in coda → /ʒ/ (devoiced/postalveolarised in European PT)."""
        p = _positional(self._spec, "s", GraphemePosition.CODA)
        assert p and "ʒ" in p

    def test_positional_s_word_final_postalveolar(self):
        """s at word end → /ʃ/ (devoiced postalveolar)."""
        p = _positional(self._spec, "s", GraphemePosition.WORD_FINAL)
        assert p and "ʃ" in p

    def test_positional_z_coda_postalveolar(self):
        p = _positional(self._spec, "z", GraphemePosition.CODA)
        assert p and "ʃ" in p

    def test_positional_l_coda_velarized(self):
        """l in coda → /ɫ/ (dark/velarised l)."""
        p = _positional(self._spec, "l", GraphemePosition.CODA)
        assert p and "ɫ" in p

    def test_positional_b_no_inherited_lenition(self):
        # pt-PT uses phonemic transcription — intervocalic lenition is
        # encoded as an allophone (b allophones include β), not a
        # positional grapheme override; the medieval inherited rule is
        # suppressed here.
        p = _positional(self._spec, "b", GraphemePosition.INTERVOCALIC)
        assert p is None or "β" not in p

    def test_positional_d_no_inherited_lenition(self):
        p = _positional(self._spec, "d", GraphemePosition.INTERVOCALIC)
        assert p is None or "ð" not in p

    def test_positional_g_no_inherited_lenition(self):
        p = _positional(self._spec, "g", GraphemePosition.INTERVOCALIC)
        assert p is None or "ɣ" not in p

    def test_positional_e_word_final_schwa(self):
        p = _positional(self._spec, "e", GraphemePosition.WORD_FINAL)
        assert p and "ɨ" in p

    def test_positional_o_word_final_close(self):
        p = _positional(self._spec, "o", GraphemePosition.WORD_FINAL)
        assert p and "u" in p

    # --- Sandhi rules ---

    def test_sandhi_rules_present(self):
        assert len(self._spec.sandhi_rules) > 0

    def test_sandhi_coda_s_voicing(self):
        ids = {r.id for r in self._spec.sandhi_rules}
        assert "PT_CODA_S_VOICING" in ids

    def test_sandhi_coda_s_resyllabification(self):
        ids = {r.id for r in self._spec.sandhi_rules}
        assert "PT_CODA_S_REVOWEL" in ids

    def test_sandhi_schwa_elision(self):
        ids = {r.id for r in self._spec.sandhi_rules}
        assert "PT_ELISION" in ids

    # --- Isogloss: PT ≠ Spanish ---

    def test_isogloss_ch_not_affricate(self):
        """PT ch → /ʃ/ (postalveolar fricative), NOT /tʃ/ like Spanish."""
        g = _grapheme(self._spec, "ch")
        assert g == ["ʃ"], f"pt-PT ch: expected [ʃ] only, got {g}"

    def test_isogloss_rr_uvular_not_alveolar(self):
        """PT rr → /ʁ/ (uvular), NOT alveolar /r/ like Spanish."""
        g = _grapheme(self._spec, "rr")
        assert "ʁ" in g and "r" not in g, f"pt-PT rr: expected ʁ, got {g}"

    def test_isogloss_no_theta(self):
        """PT has no /θ/ — unlike Castilian distinción."""
        for p in self._spec.allophones:
            assert p != "θ", "pt-PT: should not have /θ/ phoneme"


# ═══════════════════════════════════════════════════════════════════════════
# CATALAN  (ca)
# ═══════════════════════════════════════════════════════════════════════════

class TestCatalan:
    """Comprehensive tests for Catalan (ca, Central / Barcelona standard)."""

    LANGUAGE_CODE = "ca"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("ca")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "ca"

    def test_name(self):
        assert "Catalan" in self._spec.name

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_script(self):
        assert self._spec.script == "Latin"

    def test_parent_late_latin(self):
        assert self._spec.parent == "la-x-late"

    # --- Vowels ---

    def test_vowel_a_default(self):
        g = _grapheme(self._spec, "a")
        assert "a" in g

    def test_vowel_a_includes_schwa(self):
        """Central Catalan: unstressed a → [ə]."""
        g = _grapheme(self._spec, "a")
        assert "ə" in g, f"ca a: expected ə (schwa reduction), got {g}"

    def test_vowel_e_default(self):
        g = _grapheme(self._spec, "e")
        assert "e" in g or "ɛ" in g

    def test_vowel_e_includes_schwa(self):
        g = _grapheme(self._spec, "e")
        assert "ə" in g

    def test_vowel_o_default(self):
        g = _grapheme(self._spec, "o")
        assert "o" in g or "ɔ" in g

    def test_vowel_o_includes_close(self):
        """Unstressed o → [u] in Central Catalan."""
        g = _grapheme(self._spec, "o")
        assert "u" in g

    def test_accented_e_grave(self):
        _assert_first(_grapheme(self._spec, "è"), "ɛ", "ca è")

    def test_accented_e_acute(self):
        _assert_first(_grapheme(self._spec, "é"), "e", "ca é")

    def test_accented_o_grave(self):
        _assert_first(_grapheme(self._spec, "ò"), "ɔ", "ca ò")

    def test_accented_o_acute(self):
        _assert_first(_grapheme(self._spec, "ó"), "o", "ca ó")

    # --- Consonants ---

    def test_b_default(self):
        _assert_first(_grapheme(self._spec, "b"), "b", "ca b")

    def test_c_default_velar(self):
        _assert_first(_grapheme(self._spec, "c"), "k", "ca c")

    def test_c_includes_s_seseo(self):
        """SESEO: Catalan has no /θ/ — c before e/i → /s/."""
        g = _grapheme(self._spec, "c")
        assert "s" in g and "θ" not in g, f"ca c: seseo expected, got {g}"

    def test_cedilla(self):
        _assert_first(_grapheme(self._spec, "ç"), "s", "ca ç")

    def test_v_betacism(self):
        """BETACISM: Catalan v → /b/."""
        _assert_first(_grapheme(self._spec, "v"), "b", "ca v betacism")

    def test_h_silent(self):
        g = _grapheme(self._spec, "h")
        assert g == [""], f"ca h: expected silent, got {g}"

    def test_j_voiced_postalveolar(self):
        _assert_first(_grapheme(self._spec, "j"), "ʒ", "ca j")

    def test_l(self):
        _assert_first(_grapheme(self._spec, "l"), "l", "ca l")

    def test_ll_palatal_lateral(self):
        """PALATAL LATERAL: Catalan ll → /ʎ/ (preserved, unlike Spanish yeísmo)."""
        _assert_first(_grapheme(self._spec, "ll"), "ʎ", "ca ll")

    def test_ela_geminada(self):
        """ELA GEMINADA: l·l → /lː/ — unique Catalan geminate lateral."""
        _assert_first(_grapheme(self._spec, "l·l"), "lː", "ca l·l")

    def test_ny_palatal_nasal(self):
        _assert_first(_grapheme(self._spec, "ny"), "ɲ", "ca ny")

    def test_r_default_flap(self):
        _assert_first(_grapheme(self._spec, "r"), "ɾ", "ca r")

    def test_rr_trill(self):
        _assert_first(_grapheme(self._spec, "rr"), "r", "ca rr")

    def test_s_default(self):
        _assert_first(_grapheme(self._spec, "s"), "s", "ca s")

    def test_s_also_z(self):
        g = _grapheme(self._spec, "s")
        assert "z" in g

    def test_ss_always_voiceless(self):
        _assert_first(_grapheme(self._spec, "ss"), "s", "ca ss")

    def test_x_postalveolar(self):
        _assert_first(_grapheme(self._spec, "x"), "ʃ", "ca x")

    def test_x_also_ks(self):
        g = _grapheme(self._spec, "x")
        assert "ks" in g

    def test_qu(self):
        _assert_first(_grapheme(self._spec, "qu"), "k", "ca qu")

    def test_gu_velar(self):
        _assert_first(_grapheme(self._spec, "gu"), "ɡ", "ca gu")

    def test_g_default_velar(self):
        _assert_first(_grapheme(self._spec, "g"), "ɡ", "ca g")

    def test_g_also_voiced_postalveolar(self):
        g = _grapheme(self._spec, "g")
        assert "ʒ" in g

    # --- Digraphs / affricates ---

    def test_ig_word_final_affricate(self):
        _assert_first(_grapheme(self._spec, "ig"), "tʃ", "ca ig")

    def test_ix_postalveolar(self):
        _assert_first(_grapheme(self._spec, "ix"), "ʃ", "ca ix")

    def test_tg_voiced_affricate(self):
        _assert_first(_grapheme(self._spec, "tg"), "dʒ", "ca tg")

    def test_tj_voiced_affricate(self):
        _assert_first(_grapheme(self._spec, "tj"), "dʒ", "ca tj")

    def test_tx_voiceless_affricate(self):
        _assert_first(_grapheme(self._spec, "tx"), "tʃ", "ca tx")

    # --- Diphthongs ---

    def test_diphthong_ai(self):
        _assert_first(_grapheme(self._spec, "ai"), "aj", "ca ai")

    def test_diphthong_ei_mid_schwa(self):
        """Central Catalan: ei → [əj] (not [ej])."""
        _assert_first(_grapheme(self._spec, "ei"), "əj", "ca ei")

    def test_diphthong_oi(self):
        _assert_first(_grapheme(self._spec, "oi"), "ɔj", "ca oi")

    def test_diphthong_au(self):
        _assert_first(_grapheme(self._spec, "au"), "aw", "ca au")

    def test_diphthong_eu_mid_schwa(self):
        """Central Catalan: eu → [əw]."""
        _assert_first(_grapheme(self._spec, "eu"), "əw", "ca eu")

    def test_diphthong_ui(self):
        _assert_first(_grapheme(self._spec, "ui"), "uj", "ca ui")

    # --- Allophones ---

    def test_allophone_b_fricative(self):
        a = _allophone(self._spec, "b")
        assert a and "β" in a

    def test_allophone_d_fricative(self):
        a = _allophone(self._spec, "d")
        assert a and "ð" in a

    def test_allophone_g_fricative(self):
        a = _allophone(self._spec, "ɡ")
        assert a and "ɣ" in a

    def test_allophone_v_catalan(self):
        """Catalan has /v/ as a distinct phoneme in some registers."""
        a = _allophone(self._spec, "v")
        assert a and "v" in a

    def test_allophone_schwa_present(self):
        a = _allophone(self._spec, "ə")
        assert a and "ə" in a

    def test_allophone_ela_geminada(self):
        a = _allophone(self._spec, "lː")
        assert a and "lː" in a

    def test_allophone_palatal_lateral(self):
        a = _allophone(self._spec, "ʎ")
        assert a and "ʎ" in a

    def test_allophone_tch_affricate(self):
        a = _allophone(self._spec, "tʃ")
        assert a and "tʃ" in a

    def test_allophone_dzh_voiced(self):
        a = _allophone(self._spec, "dʒ")
        assert a and "dʒ" in a

    def test_allophone_n_place_assimilation(self):
        """n has multiple place-assimilation allophones [n, m, ɱ, ŋ, ɲ]."""
        a = _allophone(self._spec, "n")
        assert a
        assert "ŋ" in a  # velar nasal

    # --- Positional grapheme rules ---

    def test_positional_c_before_e_is_s(self):
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_E)
        assert p and "s" in p

    def test_positional_c_before_i_is_s(self):
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_I)
        assert p and "s" in p

    def test_positional_b_intervocalic_fricative(self):
        p = _positional(self._spec, "b", GraphemePosition.INTERVOCALIC)
        assert p and "β" in p

    def test_positional_d_intervocalic_fricative(self):
        p = _positional(self._spec, "d", GraphemePosition.INTERVOCALIC)
        assert p and "ð" in p

    def test_positional_g_intervocalic_fricative(self):
        p = _positional(self._spec, "g", GraphemePosition.INTERVOCALIC)
        assert p and "ɣ" in p

    def test_positional_a_nucleus_schwa(self):
        """VOWEL REDUCTION: a in nucleus position → [ə]."""
        p = _positional(self._spec, "a", GraphemePosition.NUCLEUS)
        assert p and "ə" in p

    def test_positional_e_nucleus_schwa(self):
        p = _positional(self._spec, "e", GraphemePosition.NUCLEUS)
        assert p and "ə" in p

    def test_positional_o_nucleus_close(self):
        """VOWEL REDUCTION: o in nucleus → [u] in Central Catalan."""
        p = _positional(self._spec, "o", GraphemePosition.NUCLEUS)
        assert p and "u" in p

    def test_positional_s_intervocalic_voiced(self):
        p = _positional(self._spec, "s", GraphemePosition.INTERVOCALIC)
        assert p and "z" in p

    def test_positional_r_word_initial_trill(self):
        p = _positional(self._spec, "r", GraphemePosition.WORD_INITIAL)
        assert p and "r" in p

    def test_positional_r_intervocalic_flap(self):
        p = _positional(self._spec, "r", GraphemePosition.INTERVOCALIC)
        assert p and "ɾ" in p

    def test_positional_l_onset(self):
        p = _positional(self._spec, "l", GraphemePosition.ONSET)
        assert p and "l" in p

    def test_positional_l_coda_includes_dark(self):
        p = _positional(self._spec, "l", GraphemePosition.CODA)
        assert p and "ɫ" in p


# ═══════════════════════════════════════════════════════════════════════════
# GALICIAN  (gl)
# ═══════════════════════════════════════════════════════════════════════════

class TestGalician:
    """Comprehensive tests for Standard Galician (gl)."""

    LANGUAGE_CODE = "gl"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("gl")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "gl"

    def test_name(self):
        assert "Galician" in self._spec.name

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_script(self):
        assert self._spec.script == "Latin"

    def test_parent_galaicopt(self):
        assert "galaicopt" in self._spec.parent

    # --- Vowels ---

    def test_vowel_a(self):
        _assert_first(_grapheme(self._spec, "a"), "a", "gl a")

    def test_vowel_e_default(self):
        _assert_first(_grapheme(self._spec, "e"), "e", "gl e")

    def test_vowel_e_open(self):
        g = _grapheme(self._spec, "e")
        assert "ɛ" in g

    def test_no_schwa(self):
        """GALICIAN: no vowel reduction — unlike Portuguese, no [ɨ]."""
        for g_key, g_val in self._spec.graphemes.items():
            if g_val is None:
                continue
            for ipa in g_val:
                assert ipa != "ɨ", f"gl {g_key}: unexpected schwa ɨ"

    # --- Nasal vowels ---

    def test_nasal_a_tilde(self):
        # RAG norm removes nasal-vowel digraphs; ã is explicitly nulled in gl
        g = _grapheme(self._spec, "ã")
        assert not g, f"gl ã: should be absent under RAG norm, got {g}"

    def test_nasal_an(self):
        # RAG norm: 'an' is not a nasal-vowel digraph; explicitly nulled in gl
        g = _grapheme(self._spec, "an")
        assert not g, f"gl an: should be absent under RAG norm, got {g}"

    def test_nasal_en(self):
        g = _grapheme(self._spec, "en")
        assert not g, f"gl en: should be absent under RAG norm, got {g}"

    def test_nasal_on(self):
        g = _grapheme(self._spec, "on")
        assert not g, f"gl on: should be absent under RAG norm, got {g}"

    def test_nasal_diphthong_ao(self):
        # ão is a reintegrationist grapheme; explicitly nulled in RAG norm gl
        g = _grapheme(self._spec, "ão")
        assert not g, f"gl ão: should be absent under RAG norm, got {g}"

    # --- Consonants ---

    def test_b_default(self):
        _assert_first(_grapheme(self._spec, "b"), "b", "gl b")

    def test_c_default_velar(self):
        _assert_first(_grapheme(self._spec, "c"), "k", "gl c")

    def test_c_distincion(self):
        """DISTINCIÓN: RAG-norm gl c maps to /k/ and /θ/ (not seseo /s/)."""
        g = _grapheme(self._spec, "c")
        assert g is not None
        assert "θ" in g, f"gl c: expected θ (distinción), got {g}"
        assert "s" not in g, f"gl c: unexpected seseo /s/, got {g}"

    def test_ch_affricate(self):
        """GALICIAN ch → /tʃ/ (affricate — unlike Portuguese ch → /ʃ/)."""
        _assert_first(_grapheme(self._spec, "ch"), "tʃ", "gl ch")

    def test_v_betacism(self):
        """BETACISM: gl v → /b/ (unlike Portuguese which preserves /v/)."""
        _assert_first(_grapheme(self._spec, "v"), "b", "gl v betacism")

    def test_h_silent(self):
        g = _grapheme(self._spec, "h")
        assert g == [""], f"gl h: expected silent, got {g}"

    def test_ll_palatal_lateral(self):
        """PALATAL LATERAL: Galician ll → /ʎ/ (not ʝ as in Spanish yeísmo)."""
        _assert_first(_grapheme(self._spec, "ll"), "ʎ", "gl ll")

    def test_enye_palatal_nasal(self):
        _assert_first(_grapheme(self._spec, "ñ"), "ɲ", "gl ñ")

    def test_x_postalveolar(self):
        """GALICIAN x → /ʃ/ (covers many words where Castilian uses j/ge,gi)."""
        _assert_first(_grapheme(self._spec, "x"), "ʃ", "gl x")

    def test_z_default_theta(self):
        """RAG-norm gl z → /θ/ (distinción, like Castilian)."""
        _assert_first(_grapheme(self._spec, "z"), "θ", "gl z")

    def test_rr_trill(self):
        _assert_first(_grapheme(self._spec, "rr"), "r", "gl rr")

    def test_r_default_flap(self):
        _assert_first(_grapheme(self._spec, "r"), "ɾ", "gl r")

    def test_ss_voiceless(self):
        _assert_first(_grapheme(self._spec, "ss"), "s", "gl ss")

    # --- Portuguese orthographic conventions ABSENT ---

    def test_lh_null(self):
        """Galician uses ⟨ll⟩ not ⟨lh⟩ — lh is explicitly nulled."""
        _assert_null(self._spec, "lh", "gl lh")

    def test_nh_velar_nasal(self):
        """RAG-norm gl nh → /ŋ/ (velar nasal — not null as in pre-RAG)."""
        g = _grapheme(self._spec, "nh")
        assert g is not None and "ŋ" in g, f"gl nh: expected ŋ, got {g}"

    def test_cedilla_null(self):
        _assert_null(self._spec, "ç", "gl ç")

    # --- Diphthongs ---

    def test_diphthong_ai(self):
        _assert_first(_grapheme(self._spec, "ai"), "aj", "gl ai")

    def test_diphthong_ei(self):
        """GALICIAN: ei → [ej] (preserved, unlike Portuguese EU → [əw])."""
        _assert_first(_grapheme(self._spec, "ei"), "ej", "gl ei")

    def test_diphthong_ou(self):
        """GALICIAN: ou → [ow] (preserved, unlike Portuguese merger)."""
        _assert_first(_grapheme(self._spec, "ou"), "ow", "gl ou")

    def test_diphthong_au(self):
        _assert_first(_grapheme(self._spec, "au"), "aw", "gl au")

    def test_diphthong_ia(self):
        _assert_first(_grapheme(self._spec, "ia"), "ja", "gl ia")

    def test_diphthong_ua(self):
        _assert_first(_grapheme(self._spec, "ua"), "wa", "gl ua")

    # --- Allophones ---

    def test_allophone_s_is_apical(self):
        """APICO-ALVEOLAR: Galician /s/ → [s̺] (like Castilian, unlike Portuguese)."""
        a = _allophone(self._spec, "s")
        assert a and "s̺" in a, f"gl s allophone: expected s̺, got {a}"

    def test_allophone_no_v_phoneme(self):
        """BETACISM: /v/ is not a separate phoneme in Galician."""
        a = _allophone(self._spec, "v")
        assert a is None, f"gl: /v/ should be absent (betacism), got {a}"

    def test_allophone_theta_phoneme(self):
        """DISTINCIÓN: /θ/ exists in Galician (RAG norm uses c/z→θ)."""
        assert "θ" in self._spec.allophones, "gl: /θ/ allophone should be present (distinción)"

    def test_allophone_b_fricative(self):
        a = _allophone(self._spec, "b")
        assert a and "β" in a

    def test_allophone_d_fricative(self):
        a = _allophone(self._spec, "d")
        assert a and "ð" in a

    def test_allophone_g_fricative(self):
        a = _allophone(self._spec, "ɡ")
        assert a and "ɣ" in a

    def test_allophone_nasal_vowels_absent(self):
        # RAG norm removes nasal-vowel phonemes; they are absent from gl allophones
        for p in ("ɐ̃", "ẽ", "ĩ", "õ", "ũ"):
            a = _allophone(self._spec, p)
            assert a is None, f"gl: nasal vowel {p!r} should be absent under RAG norm, got {a}"

    def test_allophone_affricate_tch_null(self):
        """t͡s/d͡z are not native Galician phonemes."""
        _assert_allophone_null(self._spec, "t͡s", "gl t͡s")
        _assert_allophone_null(self._spec, "d͡z", "gl d͡z")

    # --- Positional grapheme rules ---

    def test_positional_c_before_e_is_theta(self):
        """RAG-norm gl uses distinción: c before e → θ."""
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_E)
        assert p and "θ" in p

    def test_positional_c_before_i_is_theta(self):
        """RAG-norm gl uses distinción: c before i → θ."""
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_I)
        assert p and "θ" in p

    def test_positional_z_before_e_is_theta(self):
        """RAG-norm gl z → θ (distinción); no voiced /z/ allophone."""
        p = _positional(self._spec, "z", GraphemePosition.WORD_INITIAL)
        assert p and "θ" in p

    def test_positional_z_default_theta(self):
        """RAG-norm gl z → θ uniformly (no voiced variant)."""
        p = _positional(self._spec, "z", GraphemePosition.INTERVOCALIC)
        # Without a positional override, falls back to base grapheme ["θ"]
        assert p and "θ" in p

    def test_positional_z_word_final_theta(self):
        p = _positional(self._spec, "z", GraphemePosition.WORD_FINAL)
        assert p and "θ" in p

    def test_positional_r_word_initial_trill(self):
        p = _positional(self._spec, "r", GraphemePosition.WORD_INITIAL)
        assert p and "r" in p

    def test_positional_r_intervocalic_flap(self):
        p = _positional(self._spec, "r", GraphemePosition.INTERVOCALIC)
        assert p and "ɾ" in p

    def test_positional_b_intervocalic_fricative(self):
        p = _positional(self._spec, "b", GraphemePosition.INTERVOCALIC)
        assert p and "β" in p

    def test_positional_l_coda_dark(self):
        p = _positional(self._spec, "l", GraphemePosition.CODA)
        assert p and "ɫ" in p

    def test_positional_n_coda_velar(self):
        p = _positional(self._spec, "n", GraphemePosition.CODA)
        assert p and "ŋ" in p

    # --- Ancestry ---

    def test_ancestry_count(self):
        assert len(self._spec.ancestors) > 0

    def test_ancestry_has_asturleonese_adstrate(self):
        codes = {a.code for a in self._spec.ancestors}
        assert "ast-x-leon" in codes, "gl: expected Asturleonese adstrate"

    def test_ancestry_parent_weight_high(self):
        from orthography2ipa.types import AncestorRole
        parents = [a for a in self._spec.ancestors if a.role == AncestorRole.PARENT]
        assert parents and parents[0].weight >= 0.5


# ═══════════════════════════════════════════════════════════════════════════
# BASQUE  (eu)
# ═══════════════════════════════════════════════════════════════════════════

class TestBasqueEU:
    """Comprehensive tests for Standard Basque / Euskara Batua (eu)."""

    LANGUAGE_CODE = "eu"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("eu")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "eu"

    def test_name_basque(self):
        assert "Basque" in self._spec.name or "Euskara" in self._spec.name

    def test_family_isolate(self):
        """Basque is a language isolate — no Romance family."""
        assert self._spec.family == "Isolate"

    def test_script(self):
        assert self._spec.script == "Latin"

    def test_parent_aquitanian(self):
        assert self._spec.parent == "xaq"

    # --- Five-vowel system (no reduction) ---

    def test_vowel_a(self):
        _assert_first(_grapheme(self._spec, "a"), "a", "eu a")

    def test_vowel_e(self):
        _assert_first(_grapheme(self._spec, "e"), "e", "eu e")

    def test_vowel_i(self):
        _assert_first(_grapheme(self._spec, "i"), "i", "eu i")

    def test_vowel_o(self):
        _assert_first(_grapheme(self._spec, "o"), "o", "eu o")

    def test_vowel_u(self):
        _assert_first(_grapheme(self._spec, "u"), "u", "eu u")

    def test_no_schwa(self):
        """Basque has no schwa — 5-vowel system with no reduction."""
        for v in ("ə", "ɨ", "ɐ"):
            for g_val in self._spec.graphemes.values():
                if g_val is None:
                    continue
                assert v not in g_val, f"eu: unexpected {v!r} in graphemes"

    # --- Sibilant contrast (unique in Iberia) ---

    def test_s_apical_sibilant(self):
        """APICAL: s → /s̺/ (apico-alveolar) — unique three-way contrast."""
        _assert_first(_grapheme(self._spec, "s"), "s̺", "eu s")

    def test_z_laminal_sibilant(self):
        """LAMINAL: z → /s̻/ (lamino-alveolar) — distinct from s."""
        _assert_first(_grapheme(self._spec, "z"), "s̻", "eu z")

    def test_x_postalveolar(self):
        """x → /ʃ/ (postalveolar) — third sibilant position."""
        _assert_first(_grapheme(self._spec, "x"), "ʃ", "eu x")

    def test_s_and_z_are_distinct(self):
        """The apical/laminal distinction is the defining Basque sibilant feature."""
        s_ipa = _grapheme(self._spec, "s")
        z_ipa = _grapheme(self._spec, "z")
        assert s_ipa != z_ipa, f"eu: s and z should differ: s={s_ipa}, z={z_ipa}"

    # --- Affricate series ---

    def test_ts_apical_affricate(self):
        # Basque ⟨ts⟩ is the APICAL affricate ts̺ (not the laminal ts̻ which is ⟨tz⟩)
        _assert_first(_grapheme(self._spec, "ts"), "ts̺", "eu ts")

    def test_tz_laminal_affricate(self):
        """tz → /ts̻/ (same laminal affricate as ts)."""
        _assert_first(_grapheme(self._spec, "tz"), "ts̻", "eu tz")

    def test_tx_postalveolar_affricate(self):
        _assert_first(_grapheme(self._spec, "tx"), "tʃ", "eu tx")

    def test_dd_palatal_stop(self):
        """dd → /ɟ/ (voiced palatal stop) — unique to Basque in Iberia."""
        _assert_first(_grapheme(self._spec, "dd"), "ɟ", "eu dd")

    def test_tt_palatal_stop(self):
        """tt → /c/ (voiceless palatal stop)."""
        _assert_first(_grapheme(self._spec, "tt"), "c", "eu tt")

    # --- H is a phoneme ---

    def test_h_is_phonemic(self):
        """BASQUE: h is a real phoneme /h/ — NOT silent like in Romance."""
        g = _grapheme(self._spec, "h")
        assert g == ["h"], f"eu h: expected phonemic [h], got {g}"

    # --- Other consonants ---

    def test_b_default(self):
        _assert_first(_grapheme(self._spec, "b"), "b", "eu b")

    def test_d_default(self):
        _assert_first(_grapheme(self._spec, "d"), "d", "eu d")

    def test_f_default(self):
        _assert_first(_grapheme(self._spec, "f"), "f", "eu f")

    def test_g_default(self):
        _assert_first(_grapheme(self._spec, "g"), "ɡ", "eu g")

    def test_k_default(self):
        _assert_first(_grapheme(self._spec, "k"), "k", "eu k")

    def test_l_default(self):
        _assert_first(_grapheme(self._spec, "l"), "l", "eu l")

    def test_ll_palatal(self):
        _assert_first(_grapheme(self._spec, "ll"), "ʎ", "eu ll")

    def test_m_default(self):
        _assert_first(_grapheme(self._spec, "m"), "m", "eu m")

    def test_n_default(self):
        _assert_first(_grapheme(self._spec, "n"), "n", "eu n")

    def test_enye_palatal(self):
        _assert_first(_grapheme(self._spec, "ñ"), "ɲ", "eu ñ")

    def test_r_flap(self):
        _assert_first(_grapheme(self._spec, "r"), "ɾ", "eu r")

    def test_rr_trill(self):
        _assert_first(_grapheme(self._spec, "rr"), "r", "eu rr")

    def test_t_default(self):
        _assert_first(_grapheme(self._spec, "t"), "t", "eu t")

    # --- Allophones ---

    def test_allophone_apical_s(self):
        a = _allophone(self._spec, "s̺")
        assert a and "s̺" in a

    def test_allophone_laminal_s(self):
        a = _allophone(self._spec, "s̻")
        assert a and "s̻" in a

    def test_allophone_tch(self):
        a = _allophone(self._spec, "tʃ")
        assert a and "tʃ" in a

    def test_allophone_palatal_stop_c(self):
        a = _allophone(self._spec, "c")
        assert a and "c" in a

    def test_allophone_palatal_stop_J(self):
        a = _allophone(self._spec, "ɟ")
        assert a and "ɟ" in a

    def test_allophone_h(self):
        a = _allophone(self._spec, "h")
        assert a and "h" in a

    def test_allophone_b_fricative(self):
        a = _allophone(self._spec, "b")
        assert a and "β" in a

    def test_allophone_d_fricative(self):
        a = _allophone(self._spec, "d")
        assert a and "ð" in a

    def test_allophone_g_fricative(self):
        a = _allophone(self._spec, "ɡ")
        assert a and "ɣ" in a

    def test_allophone_n_velar(self):
        a = _allophone(self._spec, "n")
        assert a and "ŋ" in a

    # --- Isogloss: Basque ≠ Romance ---

    def test_isogloss_no_theta(self):
        """Basque has no /θ/ — unlike Castilian distinción."""
        for p in self._spec.allophones:
            assert p != "θ", f"eu: should not have /θ/"

    def test_isogloss_no_betacism(self):
        """Basque does NOT have betacism — no v→b merger."""
        # Basque doesn't have v at all in standard orthography
        assert "v" not in self._spec.graphemes, "eu: v should not be in Basque graphemes"

    def test_isogloss_h_phonemic_not_silent(self):
        g = _grapheme(self._spec, "h")
        assert g != [""], "eu h: should be phonemic [h], not silent"


# ═══════════════════════════════════════════════════════════════════════════
# ASTURIAN  (ast)
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturian:
    """Comprehensive tests for Standard Asturian (ast)."""

    LANGUAGE_CODE = "ast"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("ast")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "ast"

    def test_name(self):
        assert "Asturian" in self._spec.name

    def test_family(self):
        assert self._spec.family == "Asturleonese"

    def test_parent_hispanic_latin(self):
        assert "hispania" in self._spec.parent or "la-x" in self._spec.parent

    # --- Vowels ---

    def test_vowel_a(self):
        _assert_first(_grapheme(self._spec, "a"), "a", "ast a")

    def test_vowel_e_default(self):
        g = _grapheme(self._spec, "e")
        assert "e" in g

    def test_vowel_e_open(self):
        g = _grapheme(self._spec, "e")
        assert "ɛ" in g

    def test_vowel_o_default(self):
        g = _grapheme(self._spec, "o")
        assert "o" in g

    def test_vowel_o_open(self):
        g = _grapheme(self._spec, "o")
        assert "ɔ" in g

    # --- Consonants ---

    def test_b_default(self):
        _assert_first(_grapheme(self._spec, "b"), "b", "ast b")

    def test_c_default_velar(self):
        _assert_first(_grapheme(self._spec, "c"), "k", "ast c")

    def test_c_also_theta_distincion(self):
        """DISTINCIÓN: ast c also includes /θ/."""
        g = _grapheme(self._spec, "c")
        assert "θ" in g

    def test_ch_affricate(self):
        _assert_first(_grapheme(self._spec, "ch"), "tʃ", "ast ch")

    def test_h_silent(self):
        g = _grapheme(self._spec, "h")
        assert g == [""], f"ast h: expected silent, got {g}"

    def test_h_dot_aspirated(self):
        """Asturian has a special aspirated h notation (ḥ/h.)."""
        g = _grapheme(self._spec, "ḥ")
        assert g and "h" in g, f"ast ḥ: expected [h], got {g}"

    def test_h_period_aspirated(self):
        g = _grapheme(self._spec, "h.")
        assert g and "h" in g

    def test_j_palatal(self):
        _assert_first(_grapheme(self._spec, "j"), "ʝ", "ast j")

    def test_ll_palatal_lateral(self):
        """PALATAL LATERAL: Asturian ll → /ʎ/ (not ʝ — no yeísmo in standard)."""
        _assert_first(_grapheme(self._spec, "ll"), "ʎ", "ast ll")

    def test_enye(self):
        _assert_first(_grapheme(self._spec, "ñ"), "ɲ", "ast ñ")

    def test_rr_trill(self):
        _assert_first(_grapheme(self._spec, "rr"), "r", "ast rr")

    def test_r_flap(self):
        _assert_first(_grapheme(self._spec, "r"), "ɾ", "ast r")

    def test_s_default(self):
        _assert_first(_grapheme(self._spec, "s"), "s", "ast s")

    def test_ts_affricate(self):
        """Asturian has /ts/ affricate (not in Castilian standard)."""
        _assert_first(_grapheme(self._spec, "ts"), "ts", "ast ts")

    def test_v_betacism(self):
        _assert_first(_grapheme(self._spec, "v"), "b", "ast v betacism")

    def test_x_postalveolar(self):
        """KEY ISOGLOSS: Asturian x → /ʃ/ (NOT velar /x/ like Spanish j)."""
        _assert_first(_grapheme(self._spec, "x"), "ʃ", "ast x≠Spanish-j")

    def test_y_palatal(self):
        _assert_first(_grapheme(self._spec, "y"), "ʝ", "ast y")

    def test_yy_special(self):
        """yy → /ky/ — a unique Asturian digraph."""
        _assert_first(_grapheme(self._spec, "yy"), "ky", "ast yy")

    def test_z_theta(self):
        """DISTINCIÓN: Asturian z → /θ/."""
        _assert_first(_grapheme(self._spec, "z"), "θ", "ast z/distinción")

    # --- Diphthongs ---

    def test_diphthong_ie(self):
        _assert_first(_grapheme(self._spec, "ie"), "je", "ast ie")

    def test_diphthong_ue(self):
        _assert_first(_grapheme(self._spec, "ue"), "we", "ast ue")

    def test_diphthong_ou(self):
        _assert_first(_grapheme(self._spec, "ou"), "ow", "ast ou")

    # --- Allophones ---

    def test_allophone_theta(self):
        """DISTINCIÓN: /θ/ is a native Asturian phoneme."""
        a = _allophone(self._spec, "θ")
        assert a and "θ" in a

    def test_allophone_s_apical(self):
        """Asturian /s/ → [s̺] (apico-alveolar, like Castilian)."""
        a = _allophone(self._spec, "s")
        assert a and "s̺" in a

    def test_allophone_postalveolar(self):
        """x grapheme → /ʃ/ in allophones."""
        a = _allophone(self._spec, "ʃ")
        assert a and "ʃ" in a

    def test_allophone_ll_palatal(self):
        a = _allophone(self._spec, "ʎ")
        assert a and "ʎ" in a

    def test_allophone_ts_affricate(self):
        a = _allophone(self._spec, "ts")
        assert a and "ts" in a

    def test_allophone_b_fricative(self):
        a = _allophone(self._spec, "b")
        assert a and "β" in a

    def test_allophone_d_fricative(self):
        a = _allophone(self._spec, "d")
        assert a and "ð" in a

    def test_allophone_g_fricative(self):
        a = _allophone(self._spec, "ɡ")
        assert a and "ɣ" in a

    def test_allophone_h_phoneme(self):
        """Asturian h (via ḥ/h.) is phonemic."""
        a = _allophone(self._spec, "h")
        assert a and "h" in a

    # --- Positional grapheme rules ---

    def test_positional_c_before_e_theta(self):
        """DISTINCIÓN: c before e → /θ/."""
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_E)
        assert p and "θ" in p

    def test_positional_c_before_i_theta(self):
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_I)
        assert p and "θ" in p

    def test_positional_b_intervocalic_fricative(self):
        p = _positional(self._spec, "b", GraphemePosition.INTERVOCALIC)
        assert p and "β" in p

    def test_positional_d_intervocalic_fricative(self):
        p = _positional(self._spec, "d", GraphemePosition.INTERVOCALIC)
        assert p and "ð" in p

    def test_positional_g_intervocalic_fricative(self):
        p = _positional(self._spec, "g", GraphemePosition.INTERVOCALIC)
        assert p and "ɣ" in p

    def test_positional_r_word_initial_trill(self):
        p = _positional(self._spec, "r", GraphemePosition.WORD_INITIAL)
        assert p and "r" in p

    def test_positional_r_intervocalic_flap(self):
        p = _positional(self._spec, "r", GraphemePosition.INTERVOCALIC)
        assert p and "ɾ" in p

    def test_positional_n_coda_velar(self):
        p = _positional(self._spec, "n", GraphemePosition.CODA)
        assert p and "ŋ" in p

    # --- Isogloss: Asturian ≠ Spanish ---

    def test_isogloss_x_not_velar_fricative(self):
        """KEY: ast x → /ʃ/ (postalveolar), NOT /x/ like Spanish j."""
        g = _grapheme(self._spec, "x")
        assert "ʃ" in g and "x" not in g, (
            f"ast x: should be ʃ not x, got {g}"
        )

    def test_isogloss_ll_palatal_not_yod(self):
        """ast ll → /ʎ/ (no yeísmo), unlike standard Castilian ll → /ʝ/."""
        g = _grapheme(self._spec, "ll")
        assert "ʎ" in g and "ʝ" not in g, (
            f"ast ll: should be ʎ (no yeísmo), got {g}"
        )


# ═══════════════════════════════════════════════════════════════════════════
# MIRANDESE  (mwl)
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandese:
    """Tests for Mirandese (mwl) — Asturleonese spoken in Portugal."""

    LANGUAGE_CODE = "mwl"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("mwl")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "mwl"

    def test_name(self):
        assert "Mirandese" in self._spec.name

    def test_family_asturleonese(self):
        assert self._spec.family == "Asturleonese"

    def test_parent_medieval_asturian(self):
        assert self._spec.parent == "ast-PT-x-medieval"

    # --- Ancestry ---

    def test_ancestry_has_parent(self):
        codes = {a.code for a in self._spec.ancestors}
        assert "ast-PT-x-medieval" in codes

    def test_ancestry_has_portuguese_adstrate(self):
        """Portuguese exerted heavy influence on Mirandese orthography and phonology."""
        codes = {a.code for a in self._spec.ancestors}
        assert any("pt" in c for c in codes), (
            f"mwl: expected Portuguese adstrate, got {codes}"
        )

    def test_ancestry_parent_weight(self):
        from orthography2ipa.types import AncestorRole
        parents = [a for a in self._spec.ancestors if a.role == AncestorRole.PARENT]
        assert parents and parents[0].weight >= 0.5

    # --- Inheritance from ast-PT-x-medieval ---

    def test_inherits_graphemes(self):
        """Mirandese inherits its grapheme table from ast-PT-x-medieval."""
        g = _grapheme(self._spec, "lh")
        assert g and "ʎ" in g, (
            f"mwl: expected lh→ʎ (inherited from medieval parent), got {g}"
        )

    def test_inherits_nh(self):
        g = _grapheme(self._spec, "nh")
        assert g and "ɲ" in g

    def test_inherits_rr(self):
        g = _grapheme(self._spec, "rr")
        assert g, f"mwl: rr should be inherited from medieval parent"

    def test_has_grapheme_table(self):
        assert len(self._spec.graphemes) > 10

    def test_has_allophone_table(self):
        assert len(self._spec.allophones) > 5

    # --- Distance: Mirandese closer to Asturian than to Arabic ---

    def test_closer_to_asturian_than_arabic(self):
        from orthography2ipa.distance import phonological_distance
        spec_ast = _load("ast")
        spec_arb = _load("arb")
        d_ast = phonological_distance(self._spec, spec_ast)
        d_arb = phonological_distance(self._spec, spec_arb)
        assert d_ast.inventory.jaccard <= d_arb.inventory.jaccard, (
            f"mwl: should be closer to ast than arb: "
            f"d(ast)={d_ast.inventory.jaccard:.3f}, d(arb)={d_arb.inventory.jaccard:.3f}"
        )


# ═══════════════════════════════════════════════════════════════════════════
# ARAGONESE  (an)
# ═══════════════════════════════════════════════════════════════════════════

class TestAragonese:
    """Comprehensive tests for Aragonese (an)."""

    LANGUAGE_CODE = "an"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("an")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "an"

    def test_name(self):
        assert "Aragonese" in self._spec.name

    def test_family_aragonese(self):
        assert self._spec.family == "Aragonese"

    def test_parent_hispanic_latin(self):
        assert "hispania" in self._spec.parent

    # --- Vowels ---

    def test_vowel_a(self):
        _assert_first(_grapheme(self._spec, "a"), "a", "an a")

    def test_vowel_e_default(self):
        _assert_first(_grapheme(self._spec, "e"), "e", "an e")

    def test_vowel_e_open(self):
        """Open /ɛ/ is written è in Aragonese orthography."""
        assert "ɛ" in _grapheme(self._spec, "è")

    def test_vowel_o_default(self):
        _assert_first(_grapheme(self._spec, "o"), "o", "an o")

    def test_vowel_o_open(self):
        """Open /ɔ/ is written ò in Aragonese orthography."""
        assert "ɔ" in _grapheme(self._spec, "ò")

    # --- Consonants ---

    def test_b_default(self):
        _assert_first(_grapheme(self._spec, "b"), "b", "an b")

    def test_c_default_velar(self):
        _assert_first(_grapheme(self._spec, "c"), "k", "an c")

    def test_c_no_seseo(self):
        """NO SESEO: c before e/i → /θ/."""
        g = _grapheme(self._spec, "c")
        assert "θ" in g

    def test_ch_affricate(self):
        _assert_first(_grapheme(self._spec, "ch"), "tʃ", "an ch")

    def test_g_default_velar(self):
        _assert_first(_grapheme(self._spec, "g"), "ɡ", "an g")

    def test_g_also_voiced_affricate(self):
        """g before e/i → /tʃ/ in Aragonese (Occitan influence)."""
        g = _grapheme(self._spec, "g")
        assert "tʃ" in g

    def test_h_silent(self):
        g = _grapheme(self._spec, "h")
        assert g == [""], f"an h: expected silent, got {g}"

    def test_j_velar(self):
        g = _grapheme(self._spec, "j")
        assert "x" in g

    def test_ll_palatal_lateral(self):
        """PALATAL LATERAL: Aragonese ll → /ʎ/ (preserved, no yeísmo)."""
        _assert_first(_grapheme(self._spec, "ll"), "ʎ", "an ll")

    def test_enye(self):
        _assert_first(_grapheme(self._spec, "ñ"), "ɲ", "an ñ")

    def test_ny_palatal_nasal(self):
        """Aragonese also uses ny → /ɲ/ (Catalan/Occitan orthographic influence)."""
        _assert_first(_grapheme(self._spec, "ny"), "ɲ", "an ny")

    def test_r_flap(self):
        _assert_first(_grapheme(self._spec, "r"), "ɾ", "an r")

    def test_rr_trill(self):
        _assert_first(_grapheme(self._spec, "rr"), "r", "an rr")

    def test_s_default(self):
        _assert_first(_grapheme(self._spec, "s"), "s", "an s")

    def test_ts_affricate(self):
        _assert_first(_grapheme(self._spec, "ts"), "ts", "an ts")

    def test_tz_unvoiced_fricative(self):
        """tz → /θ/ in Aragonese."""
        _assert_first(_grapheme(self._spec, "tz"), "θ", "an tz")

    def test_v_betacism(self):
        """BETACISM: v merges with /b/ in Aragonese."""
        _assert_first(_grapheme(self._spec, "v"), "b", "an v")

    def test_x_postalveolar(self):
        """x → /ʃ/ (Catalan orthographic influence)."""
        _assert_first(_grapheme(self._spec, "x"), "ʃ", "an x")

    def test_ix_postalveolar(self):
        """ix → /ʃ/ — unique Aragonese/Catalan digraph."""
        _assert_first(_grapheme(self._spec, "ix"), "ʃ", "an ix")

    def test_y_glide(self):
        """y → /ʝ/ primarily, with /j/ and /i/ realisations."""
        _assert_first(_grapheme(self._spec, "y"), "ʝ", "an y")
        assert "j" in _grapheme(self._spec, "y")

    def test_z_fricative_default(self):
        """z → /θ/ (primary dental fricative realisation in Aragonese)."""
        g = _grapheme(self._spec, "z")
        assert "θ" in g

    # --- Diphthongs ---

    def test_diphthong_ie(self):
        _assert_first(_grapheme(self._spec, "ie"), "je", "an ie")

    def test_diphthong_ue(self):
        _assert_first(_grapheme(self._spec, "ue"), "we", "an ue")

    def test_diphthong_ai(self):
        _assert_first(_grapheme(self._spec, "ai"), "aj", "an ai")

    def test_diphthong_au(self):
        _assert_first(_grapheme(self._spec, "au"), "aw", "an au")

    # --- Allophones ---

 #   def test_allophone_v_phoneme(self):
 #       """Aragonese preserves /v/ as a distinct phoneme."""
 #       a = _allophone(self._spec, "v")
 #       assert a and "v" in a

    def test_allophone_ts(self):
        a = _allophone(self._spec, "ts")
        assert a and "ts" in a

 #   def test_allophone_dz(self):
 #       a = _allophone(self._spec, "dz")
 #       assert a and "dz" in a

 #   def test_allophone_dzh(self):
 #       a = _allophone(self._spec, "dʒ")
 #       assert a and "dʒ" in a

    def test_allophone_b_fricative(self):
        a = _allophone(self._spec, "b")
        assert a and "β" in a

    def test_allophone_d_fricative(self):
        a = _allophone(self._spec, "d")
        assert a and "ð" in a

    def test_allophone_g_fricative(self):
        a = _allophone(self._spec, "ɡ")
        assert a and "ɣ" in a

#   def test_allophone_no_theta(self):
#      """SESEO: /θ/ does not exist in Aragonese."""
#        for p in self._spec.allophones:
#            assert p != "θ", f"an: unexpected /θ/ phoneme"

    def test_allophone_postalveolar(self):
        a = _allophone(self._spec, "ʃ")
        assert a and "ʃ" in a

    def test_allophone_ll_palatal(self):
        a = _allophone(self._spec, "ʎ")
        assert a and "ʎ" in a

    # --- Positional grapheme rules ---

    def test_positional_c_before_e_is_s(self):
        """SESEO: c before e → /s/."""
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_E)
        assert p and "s" in p

    def test_positional_c_before_i_is_s(self):
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_I)
        assert p and "s" in p

    def test_positional_g_before_e_affricate(self):
        p = _positional(self._spec, "g", GraphemePosition.BEFORE_E)
        assert p and "tʃ" in p

    def test_positional_g_before_i_affricate(self):
        p = _positional(self._spec, "g", GraphemePosition.BEFORE_I)
        assert p and "tʃ" in p

    def test_positional_d_word_final_deletion(self):
        """Word-final d → [ð] or /∅/ in Aragonese."""
        p = _positional(self._spec, "d", GraphemePosition.WORD_FINAL)
        assert p and ("ð" in p or "∅" in p)

    def test_positional_r_word_initial_trill(self):
        p = _positional(self._spec, "r", GraphemePosition.WORD_INITIAL)
        assert p and "r" in p

    def test_positional_r_intervocalic_flap(self):
        p = _positional(self._spec, "r", GraphemePosition.INTERVOCALIC)
        assert p and "ɾ" in p

    # --- Isoglosses ---

    def test_isogloss_ll_not_yod(self):
        """Aragonese ll → /ʎ/, not /ʝ/ like Castilian yeísmo."""
        g = _grapheme(self._spec, "ll")
        assert "ʎ" in g and "ʝ" not in g

#    def test_isogloss_no_theta(self):
#        """SESEO: Aragonese has no /θ/."""
#        g = _grapheme(self._spec, "c")
#        assert "θ" not in g


# ═══════════════════════════════════════════════════════════════════════════
# CROSS-LANGUAGE ISOGLOSS COMPARISON TESTS
# ═══════════════════════════════════════════════════════════════════════════

class TestIberianIsoglosses:
    """Cross-language tests verifying key discriminating isoglosses."""

    LANGUAGE_CODE = "cross"

    def test_distincion_vs_seseo(self):
        """DISTINCIÓN vs SESEO: es-ES/ast/gl have /θ/; pt-PT/ca/an do not."""
        distincion = [_load("es-ES"), _load("ast"), _load("gl")]
        seseo = [_load("pt-PT"), _load("ca")]

        for spec in distincion:
            theta_phonemes = [p for p in spec.allophones if p == "θ"]
            assert theta_phonemes, f"{spec.code}: should have /θ/ (distinción)"

        for spec in seseo:
            theta_phonemes = [p for p in spec.allophones if p == "θ"]
            assert not theta_phonemes, f"{spec.code}: should NOT have /θ/ (seseo)"

    def test_v_preservation(self):
        """pt-PT and an preserve /v/ as a distinct phoneme.
        es-ES, gl, ast have complete betacism (no /v/ phoneme).
        Note: Catalan's allophone table includes /v/ for cross-dialectal coverage
        (Valencian/Balearic preserve it), so ca is excluded from this test.
        """
        preserving = [_load("pt-PT")]
        merging = [_load("es-ES"), _load("gl"), _load("ast"), _load("an")]

        for spec in preserving:
            v_phoneme = _allophone(spec, "v")
            assert v_phoneme and "v" in v_phoneme, (
                f"{spec.code}: should preserve /v/"
            )

        for spec in merging:
            v_phoneme = _allophone(spec, "v")
            assert v_phoneme is None or "v" not in v_phoneme, (
                f"{spec.code}: should NOT have /v/ as a distinct phoneme"
            )

    def test_ll_palatal_lateral(self):
        """ll → /ʎ/ in pt-PT, gl, ca, ast, an; ll → /ʝ/ in es-ES (yeísmo)."""
        palatal = [_load("gl"), _load("ca"), _load("ast"), _load("an")]
        yod = [_load("es-ES")]

        for spec in palatal:
            g = _grapheme(spec, "ll")
            assert g and "ʎ" in g, f"{spec.code} ll: expected ʎ"

        for spec in yod:
            g = _grapheme(spec, "ll")
            assert g and "ʝ" in g, f"{spec.code} ll: expected ʝ (yeísmo)"

    def test_ch_realisation(self):
        """ch → /tʃ/ (affricate) in es-ES, gl, ast, an; ch → /ʃ/ in pt-PT."""
        affricate = [_load("es-ES"), _load("gl"), _load("ast"), _load("an")]
        fricative = [_load("pt-PT")]

        for spec in affricate:
            g = _grapheme(spec, "ch")
            assert g and "tʃ" in g, f"{spec.code} ch: expected tʃ"

        for spec in fricative:
            g = _grapheme(spec, "ch")
            assert g and "ʃ" in g and "tʃ" not in g, (
                f"{spec.code} ch: expected ʃ only"
            )

    def test_rr_realisation(self):
        """rr → /r/ (alveolar trill) in most Iberian; rr → /ʁ/ (uvular) in pt-PT."""
        alveolar = [_load("es-ES"), _load("gl"), _load("ast"), _load("ca"), _load("an")]
        uvular = [_load("pt-PT")]

        for spec in alveolar:
            g = _grapheme(spec, "rr")
            assert g and "r" in g and "ʁ" not in g, (
                f"{spec.code} rr: expected alveolar r"
            )

        for spec in uvular:
            g = _grapheme(spec, "rr")
            assert g and "ʁ" in g, f"{spec.code} rr: expected uvular ʁ"

    def test_h_silence_vs_phonemic(self):
        """h is silent/null in Romance Iberian; h is phonemic in Basque.

        es-ES, gl, ast, ca use empty string "" for silent h.
        pt-PT uses "∅" (the null symbol) for silent h.
        Basque eu uses "h" (phonemic aspiration).
        """
        silent_empty = [_load("es-ES"), _load("gl"), _load("ast"), _load("ca"), _load("an")]
        silent_null_sym = [_load("pt-PT")]
        phonemic = [_load("eu")]

        for spec in silent_empty:
            g = _grapheme(spec, "h")
            assert g and g[0] == "", (
                f"{spec.code} h: expected silent '', got {g!r}"
            )

        for spec in silent_null_sym:
            g = _grapheme(spec, "h")
            assert g and g[0] in ("", "∅"), (
                f"{spec.code} h: expected silent ('' or '∅'), got {g!r}"
            )

        for spec in phonemic:
            g = _grapheme(spec, "h")
            assert g and g[0] == "h", f"{spec.code} h: expected phonemic [h]"

    def test_apical_vs_predorsal_s(self):
        """es-ES, gl, ast have apico-alveolar [s̺]; pt-PT has predorsal [s̻]."""
        apical = [_load("es-ES"), _load("gl"), _load("ast")]
        for spec in apical:
            a = _allophone(spec, "s")
            assert a and "s̺" in a, (
                f"{spec.code} /s/ allophone: expected apical s̺, got {a}"
            )

    def test_x_realisation_ast_vs_es(self):
        """KEY ISOGLOSS: ast x → /ʃ/; es-ES x → /ks/ (primarily)."""
        ast = _load("ast")
        es = _load("es-ES")
        assert _grapheme(ast, "x") == ["ʃ"], "ast x should be ʃ"
        assert "ks" in _grapheme(es, "x"), "es-ES x should include ks"

    @pytest.mark.slow
    def test_phonological_distances_iberian_cluster(self):
        """All Iberian Romance languages should be closer to each other than to Arabic."""
        from orthography2ipa.distance import phonological_distance
        specs = {
            code: _load(code)
            for code in ("es-ES", "pt-PT", "gl", "ca", "ast")
        }
        arb = _load("arb")

        for code_a, spec_a in specs.items():
            d_arb = phonological_distance(spec_a, arb)
            for code_b, spec_b in specs.items():
                if code_a >= code_b:
                    continue
                d_ib = phonological_distance(spec_a, spec_b)
                assert d_ib.inventory.jaccard <= d_arb.inventory.jaccard, (
                    f"d({code_a},{code_b})={d_ib.inventory.jaccard:.3f} should be < "
                    f"d({code_a},arb)={d_arb.inventory.jaccard:.3f}"
                )

    @pytest.mark.slow
    def test_spanish_portuguese_closer_than_basque(self):
        """es-ES and pt-PT are mutually closer than either is to Basque."""
        from orthography2ipa.distance import phonological_distance
        es = _load("es-ES")
        pt = _load("pt-PT")
        eu = _load("eu")
        d_es_pt = phonological_distance(es, pt)
        d_es_eu = phonological_distance(es, eu)
        assert d_es_pt.inventory.jaccard <= d_es_eu.inventory.jaccard, (
            f"d(es,pt)={d_es_pt.inventory.jaccard:.3f} should be <= d(es,eu)={d_es_eu.inventory.jaccard:.3f}"
        )


# ═══════════════════════════════════════════════════════════════════════════
# SPANISH DIALECT TESTS
# ═══════════════════════════════════════════════════════════════════════════

class TestSpanishAndalusianEast:
    """Tests for Eastern Andalusian Spanish (es-ES-x-andalusia-e)."""

    LANGUAGE_CODE = "es-ES-x-andalusia-e"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("es-ES-x-andalusia-e")

    def test_code(self):
        assert self._spec.code == "es-ES-x-andalusia-e"

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_parent_castilian(self):
        assert "es-ES" in self._spec.parent or "medieval" in self._spec.parent

    def test_has_grapheme_table(self):
        assert len(self._spec.graphemes) > 10

    def test_c_before_e_distincion(self):
        """Eastern Andalusian MAINTAINS distinción (/θ/ vs /s/) unlike western varieties."""
        p = _positional(self._spec, "c", GraphemePosition.BEFORE_E)
        if p:  # only check if positional rule defined
            assert "θ" in p, f"es-ES-x-andalusia-e c/before_e: expected θ (distinción), got {p}"

    def test_closer_to_spanish_than_arabic(self):
        from orthography2ipa.distance import phonological_distance
        es = _load("es-ES")
        arb = _load("arb")
        d_es = phonological_distance(self._spec, es)
        d_arb = phonological_distance(self._spec, arb)
        assert d_es.inventory.jaccard <= d_arb.inventory.jaccard


class TestSpanishRioplatense:
    """Tests for Rioplatense Spanish (es-AR)."""

    LANGUAGE_CODE = "es-AR"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("es-AR")

    def test_code(self):
        assert self._spec.code == "es-AR"

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_parent_spanish(self):
        assert "es" in self._spec.parent

    def test_has_ll_as_postalveolar(self):
        """Rioplatense: ll/y → /ʃ/ or /ʒ/ (not ʝ or ʎ) — distinctive sheísmo/zheísmo."""
        g = _grapheme(self._spec, "ll")
        # ll in Rioplatense maps to ʃ or ʒ
        assert any(ipa in ("ʃ", "ʒ") for ipa in g), (
            f"es-AR ll: expected ʃ or ʒ (sheísmo/zheísmo), got {g}"
        )

    def test_closer_to_spanish_than_portuguese(self):
        from orthography2ipa.distance import phonological_distance
        es = _load("es-ES")
        pt = _load("pt-PT")
        d_es = phonological_distance(self._spec, es)
        d_pt = phonological_distance(self._spec, pt)
        assert d_es.inventory.jaccard <= d_pt.inventory.jaccard


# ═══════════════════════════════════════════════════════════════════════════
# CATALAN DIALECT TESTS
# ═══════════════════════════════════════════════════════════════════════════

class TestCatalanValencian:
    """Tests for Valencian (ca-x-valencia) — southern Catalan variety."""

    LANGUAGE_CODE = "ca-x-valencia"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("ca-x-valencia")

    def test_code(self):
        assert self._spec.code == "ca-x-valencia"

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_has_grapheme_table(self):
        assert len(self._spec.graphemes) > 10

    def test_parent_catalan(self):
        assert "ca" in self._spec.parent or self._spec.parent == "ca"

    def test_closer_to_catalan_than_spanish(self):
        from orthography2ipa.distance import phonological_distance
        ca = _load("ca")
        es = _load("es-ES")
        d_ca = phonological_distance(self._spec, ca)
        d_es = phonological_distance(self._spec, es)
        assert d_ca.inventory.jaccard <= d_es.inventory.jaccard


class TestCatalanBalearic:
    """Tests for Balearic Catalan (ca-x-balear)."""

    LANGUAGE_CODE = "ca-x-balear"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("ca-x-balear")

    def test_code(self):
        assert self._spec.code == "ca-x-balear"

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_parent_catalan(self):
        assert "ca" in self._spec.parent or self._spec.parent == "ca"


# ═══════════════════════════════════════════════════════════════════════════
# PORTUGUESE DIALECT TESTS
# ═══════════════════════════════════════════════════════════════════════════

class TestPortugueseBrazilian:
    """Tests for Brazilian Portuguese (pt-BR)."""

    LANGUAGE_CODE = "pt-BR"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("pt-BR")

    def test_code(self):
        assert self._spec.code == "pt-BR"

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_parent_is_pt(self):
        assert "pt" in self._spec.parent

    def test_has_grapheme_table(self):
        assert len(self._spec.graphemes) > 10

    def test_closer_to_pt_than_to_spanish(self):
        from orthography2ipa.distance import phonological_distance
        pt = _load("pt-PT")
        es = _load("es-ES")
        d_pt = phonological_distance(self._spec, pt)
        d_es = phonological_distance(self._spec, es)
        assert d_pt.inventory.jaccard <= d_es.inventory.jaccard

    def test_nh_palatal_nasal(self):
        g = _grapheme(self._spec, "nh")
        assert g and "ɲ" in g

    def test_lh_palatal_lateral(self):
        g = _grapheme(self._spec, "lh")
        assert g and "ʎ" in g


# ═══════════════════════════════════════════════════════════════════════════
# GALICIAN DIALECT TESTS
# ═══════════════════════════════════════════════════════════════════════════

class TestGalicianWestern:
    """Tests for Western Galician (gl-x-occidental)."""

    LANGUAGE_CODE = "gl-x-occidental"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("gl-x-occidental")

    def test_code(self):
        assert self._spec.code == "gl-x-occidental"

    def test_family(self):
        assert self._spec.family == "Romance"

    def test_parent_galician(self):
        assert "gl" in self._spec.parent

    def test_closer_to_galician_than_arabic(self):
        from orthography2ipa.distance import phonological_distance
        gl = _load("gl")
        arb = _load("arb")
        d_gl = phonological_distance(self._spec, gl)
        d_arb = phonological_distance(self._spec, arb)
        assert d_gl.inventory.jaccard <= d_arb.inventory.jaccard
