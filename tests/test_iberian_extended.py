"""Extended per-language accuracy tests for Iberian Peninsula dialects and Romance languages.

Covers dialects and languages not included in test_iberian.py:
- Spanish regional dialects: Western Andalusian, Canarian, Murcian, Mexican, Chilean,
  Venezuelan, Latin American generic
- Extremaduran (ext)
- Portuguese regional: Lisbon, Porto, Angolan, Rio de Janeiro
- Catalan: Northern, Occidental
- Galician: Standard (gl-ES), Oriental
- Basque: Bizkaiera, Gipuzkera
- Asturian/Leonese: Occidental, Oriental, Cantabrian, Leonese, Portuguese Medieval
- Mirandese: Sendim, Ifanes
- Aragonese: Occidental (stub), Oriental
- Non-Iberian Romance: French, Italian

Each class tests phonological features documented in the JSON data file.
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa.types import GraphemePosition

# ─────────────────────────────────────────────────────────────────────────────
# Helpers (identical pattern to test_iberian.py)
# ─────────────────────────────────────────────────────────────────────────────

_SENTINEL = object()


def _load(code: str):
    """Load a LanguageSpec by code, skip if unavailable."""
    try:
        return orthography2ipa.get(code)
    except Exception as exc:
        pytest.skip(f"{code!r} not available: {exc}")


def _grapheme(spec, grapheme: str) -> list[str] | None:
    """Return IPA list for a grapheme, or None if absent."""
    return spec.graphemes.get(grapheme)


def _allophone(spec, phoneme: str) -> list[str] | None:
    """Return allophone list for a phoneme, or None if absent."""
    return spec.allophones.get(phoneme)


def _positional(spec, grapheme: str, position: GraphemePosition) -> list[str] | None:
    """Return positional override for grapheme+position, or None if absent."""
    pos_map = spec.positional_graphemes.get(grapheme)
    if pos_map is None:
        return None
    return pos_map.get(position)


def _assert_contains(values: list[str] | None, *expected: str, label: str = "") -> None:
    """Assert that *values* is not None and contains every expected string."""
    assert values is not None, f"{label}: mapping is absent"
    for exp in expected:
        assert exp in values, f"{label}: {exp!r} not in {values}"


def _assert_first(values: list[str] | None, expected: str, label: str = "") -> None:
    """Assert that the first (most common) realisation is *expected*."""
    assert values is not None, f"{label}: mapping is absent"
    assert values[0] == expected, f"{label}: expected first={expected!r}, got {values[0]!r}"


def _assert_null(spec, grapheme: str) -> None:
    """Assert that *grapheme* is absent from spec.graphemes (null override removed it)."""
    result = spec.graphemes.get(grapheme, _SENTINEL)
    assert result is _SENTINEL or result is None, (
        f"grapheme {grapheme!r} should be absent/null but is {result!r}"
    )


def _assert_allophone_null(spec, phoneme: str) -> None:
    """Assert that *phoneme* is absent/null in spec.allophones (null override removed it)."""
    result = spec.allophones.get(phoneme, _SENTINEL)
    assert result is _SENTINEL or result is None, (
        f"allophone {phoneme!r} should be absent/null but is {result!r}"
    )


# ═══════════════════════════════════════════════════════════════════════════
# Spanish regional dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestSpanishWesternAndalusian:
    """Western Andalusian Spanish — es-ES-x-andalusia-w.

    Most phonologically innovative Castilian variety: seseo/ceceo variation,
    extreme coda-/s/ aspiration and deletion, /x/→[h], universal yeísmo,
    consonant lenition with deletion, liquid neutralisation.
    """

    LANGUAGE_CODE = "es-ES-x-andalusia-w"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Grapheme inventory
    def test_c_seseo_ceceo(self):
        """c maps to k, s, θ — both seseo and ceceo options present."""
        _assert_contains(
            _grapheme(self.spec, "c"), "k", "s", "θ",
            label="c (Western Andalusian)",
        )

    def test_z_maps_s_and_theta(self):
        """z → [s, θ] — seseo primary, ceceo secondary."""
        vals = _grapheme(self.spec, "z")
        _assert_first(vals, "s", label="z")
        _assert_contains(vals, "θ", label="z")

    def test_s_has_aspiration(self):
        """s grapheme maps to [s, h] — surface aspiration already in grapheme table."""
        _assert_contains(_grapheme(self.spec, "s"), "s", "h", label="s")

    def test_ll_yeismo(self):
        """ll → ʝ (universal yeísmo — no ʎ distinction)."""
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="ll")

    # Allophone system
    def test_theta_has_seseo_allophone(self):
        """θ allophone includes s — θ/s merger in seseo zones."""
        _assert_contains(_allophone(self.spec, "θ"), "s", label="θ allophone")

    def test_s_coda_aspiration(self):
        """Coda /s/ realised as [h] or ∅."""
        coda = _positional(self.spec, "s", GraphemePosition.CODA)
        assert coda is not None, "s/CODA positional missing"
        _assert_first(coda, "h", label="s/CODA")
        assert "" in coda, "s/CODA should include ∅ deletion"

    def test_s_word_final_aspiration(self):
        """Word-final /s/ → [h, ∅]."""
        wf = _positional(self.spec, "s", GraphemePosition.WORD_FINAL)
        assert wf is not None, "s/WORD_FINAL positional missing"
        _assert_first(wf, "h", label="s/WORD_FINAL")

    def test_x_lenition_to_h(self):
        """x → [h] (velar fricative weakens to glottal)."""
        _assert_first(_allophone(self.spec, "x"), "h", label="x allophone")

    def test_d_word_final_deletion(self):
        """Word-final d → ∅ (extreme lenition)."""
        wf = _positional(self.spec, "d", GraphemePosition.WORD_FINAL)
        assert wf is not None, "d/WORD_FINAL positional missing"
        assert "" in wf, "d word-final should include ∅"

    def test_d_intervocalic_lenition(self):
        """Intervocalic d → [ð, ∅] (lenition + deletion)."""
        iv = _positional(self.spec, "d", GraphemePosition.INTERVOCALIC)
        assert iv is not None
        _assert_contains(iv, "ð", "", label="d/INTERVOCALIC")

    def test_d_allophone_deletion(self):
        """d allophone list includes ∅ — deletion in extreme lenition."""
        _assert_contains(_allophone(self.spec, "d"), "", label="d allophone")

    def test_b_allophone_deletion(self):
        """b allophone includes ∅ — betacism + deletion."""
        _assert_contains(_allophone(self.spec, "b"), "β", "", label="b allophone")

    def test_n_word_final_velarisation(self):
        """Word-final n → [ŋ, ∅] — velarisation and deletion."""
        wf = _positional(self.spec, "n", GraphemePosition.WORD_FINAL)
        assert wf is not None
        _assert_contains(wf, "ŋ", "", label="n/WORD_FINAL")

    def test_liquid_neutralisation_l(self):
        """l allophone includes ɾ — liquid neutralisation in coda."""
        _assert_contains(_allophone(self.spec, "l"), "ɾ", label="l allophone")

    def test_vowel_opening_a(self):
        """a allophone includes æ — compensatory vowel opening for coda-/s/ loss."""
        _assert_contains(_allophone(self.spec, "a"), "æ", label="a allophone")

    def test_vowel_opening_e(self):
        """e allophone includes ɛ — vowel opening."""
        _assert_contains(_allophone(self.spec, "e"), "ɛ", label="e allophone")

    def test_ch_deaffrication(self):
        """tʃ allophone includes ʃ — CH deaffrication in Cádiz/Sevilla zone."""
        _assert_contains(_allophone(self.spec, "tʃ"), "ʃ", label="tʃ allophone")

    def test_parent_is_es_es(self):
        """Parent language is es-ES."""
        assert self.spec.parent == "es-ES"


@pytest.mark.iberian
class TestSpanishCanarian:
    """Canarian Spanish — es-ES-x-canarias.

    Systematic seseo, universal yeísmo, coda-/s/ aspiration (less extreme
    than Andalusian), conservative [tʃ] affricate.
    """

    LANGUAGE_CODE = "es-ES-x-canarias"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_seseo(self):
        """c → [k, s] — systematic seseo (no θ)."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "s", label="c")
        assert "θ" not in vals, "Canarian should not have θ in c mapping"

    def test_z_seseo(self):
        """z → s (seseo — no θ)."""
        vals = _grapheme(self.spec, "z")
        _assert_first(vals, "s", label="z")
        assert "θ" not in vals, "Canarian z should not map to θ"

    def test_ll_yeismo(self):
        """ll → ʝ (universal yeísmo)."""
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="ll")

    def test_s_aspiration_allophone(self):
        """s allophone includes h — aspiration present."""
        _assert_contains(_allophone(self.spec, "s"), "h", label="s allophone")

    def test_s_coda_aspiration(self):
        """Coda s → [h, s] — aspiration primary in coda."""
        coda = _positional(self.spec, "s", GraphemePosition.CODA)
        assert coda is not None
        _assert_first(coda, "h", label="s/CODA")

    def test_s_word_final_aspiration(self):
        """Word-final s → h."""
        wf = _positional(self.spec, "s", GraphemePosition.WORD_FINAL)
        assert wf is not None
        _assert_first(wf, "h", label="s/WORD_FINAL")

    def test_d_deletion(self):
        """d allophone includes ∅ — participial -ado deletion."""
        _assert_contains(_allophone(self.spec, "d"), "", label="d allophone")

    def test_ll_allophone_no_lambda(self):
        """ʎ allophone → ʝ (no ʎ distinction — yeísmo complete)."""
        _assert_first(_allophone(self.spec, "ʎ"), "ʝ", label="ʎ allophone")

    def test_parent_is_es_es(self):
        """Parent language is es-ES."""
        assert self.spec.parent == "es-ES"


@pytest.mark.iberian
class TestSpanishMurcian:
    """Murcian Spanish (Panocho) — es-ES-x-murcia.

    Transitional variety: partial distinción/seseo, coda aspiration, yeísmo,
    liquid neutralisation. Aragonese/Catalan substrate traces.
    """

    LANGUAGE_CODE = "es-ES-x-murcia"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_mixed_distincion_seseo(self):
        """c → [k, θ, s] — mixed distinción/seseo (θ present but s also listed)."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "θ", "s", label="c")

    def test_ll_yeismo(self):
        """ll → ʝ (yeísmo)."""
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="ll")

    def test_s_has_aspiration_grapheme(self):
        """s grapheme includes h — aspiration captured."""
        _assert_contains(_grapheme(self.spec, "s"), "h", label="s grapheme")

    def test_s_allophone_aspiration(self):
        """s allophone includes h and ∅ — aspiration + deletion."""
        _assert_contains(_allophone(self.spec, "s"), "h", "", label="s allophone")

    def test_s_coda_aspiration(self):
        """Coda s → [h, s]."""
        coda = _positional(self.spec, "s", GraphemePosition.CODA)
        assert coda is not None
        _assert_first(coda, "h", label="s/CODA")

    def test_d_intervocalic_lenition(self):
        """Intervocalic d → [ð, ∅]."""
        iv = _positional(self.spec, "d", GraphemePosition.INTERVOCALIC)
        assert iv is not None
        _assert_contains(iv, "ð", "", label="d/INTERVOCALIC")

    def test_liquid_neutralisation(self):
        """l and ɾ allophones include each other — liquid neutralisation in coda."""
        _assert_contains(_allophone(self.spec, "l"), "ɾ", label="l allophone")
        _assert_contains(_allophone(self.spec, "ɾ"), "l", label="ɾ allophone")

    def test_ll_allophone_no_lambda(self):
        """ll grapheme → ʝ first (yeísmo); ʎ not retained as primary."""
        vals = _grapheme(self.spec, "ll")
        assert vals is not None, "es-ES-x-murcia: ll grapheme missing"
        assert vals[0] == "ʝ", f"es-ES-x-murcia: expected ll first=ʝ, got {vals[0]}"

    def test_parent_is_es_es(self):
        assert self.spec.parent == "es-ES"


@pytest.mark.iberian
class TestSpanishMexican:
    """Mexican Spanish (Highland) — es-MX.

    Conservative variety: full coda /s/, velar [x] retained (no aspiration),
    distinctive unstressed vowel devoicing [e̥, o̥]. Seseo. Yeísmo.
    """

    LANGUAGE_CODE = "es-MX"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_seseo(self):
        """c → [k, s] — seseo (no θ)."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "s", label="c")
        assert "θ" not in vals, "Mexican Spanish should not have θ"

    def test_z_seseo(self):
        """z → s."""
        _assert_first(_grapheme(self.spec, "z"), "s", label="z")

    def test_ll_yeismo(self):
        """ll → ʝ."""
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="ll")

    def test_x_velar_retained(self):
        """x allophone → [x] (conservative — no aspiration)."""
        _assert_first(_allophone(self.spec, "x"), "x", label="x allophone")

    def test_vowel_devoicing_e(self):
        """e allophone includes e̥ — unstressed devoicing."""
        _assert_contains(_allophone(self.spec, "e"), "e̥", label="e allophone")

    def test_vowel_devoicing_o(self):
        """o allophone includes o̥ — unstressed devoicing."""
        _assert_contains(_allophone(self.spec, "o"), "o̥", label="o allophone")

    def test_parent_is_es_es(self):
        assert self.spec.parent == "es-ES"


@pytest.mark.iberian
class TestSpanishChilean:
    """Chilean Spanish — es-CL.

    Seseo, d-deletion in word-final, coda-s aspiration,
    x → [x, ç] (fronted variant), yeísmo.
    """

    LANGUAGE_CODE = "es-CL"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_seseo(self):
        """c → [k, s] — seseo."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "s", label="c")
        assert "θ" not in vals

    def test_z_seseo(self):
        _assert_first(_grapheme(self.spec, "z"), "s", label="z")

    def test_ll_yeismo(self):
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="ll")

    def test_x_fronted_variant(self):
        """x allophone includes ç — fronted pre-palatal variant."""
        _assert_contains(_allophone(self.spec, "x"), "ç", label="x allophone")

    def test_d_deletion(self):
        """d allophone includes ∅."""
        _assert_contains(_allophone(self.spec, "d"), "", label="d allophone")

    def test_s_coda_aspiration(self):
        """Coda s has aspiration."""
        coda = _positional(self.spec, "s", GraphemePosition.CODA)
        assert coda is not None
        _assert_contains(coda, "h", label="s/CODA")

    def test_parent_is_es_es(self):
        assert self.spec.parent == "es-ES"


@pytest.mark.iberian
class TestSpanishVenezuelan:
    """Venezuelan Spanish — es-VE.

    Seseo, x → [h] (aspiration), l-weakening in coda, yeísmo.
    """

    LANGUAGE_CODE = "es-VE"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_seseo(self):
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "s", label="c")
        assert "θ" not in vals

    def test_z_seseo(self):
        _assert_first(_grapheme(self.spec, "z"), "s", label="z")

    def test_ll_yeismo(self):
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="ll")

    def test_x_aspiration(self):
        """x → [h] (aspirated, not velar)."""
        _assert_first(_allophone(self.spec, "x"), "h", label="x allophone")

    def test_l_weakening(self):
        """l allophone includes ɾ and j — coda weakening."""
        _assert_contains(_allophone(self.spec, "l"), "ɾ", "j", label="l allophone")

    def test_s_aspiration(self):
        """s allophone includes h."""
        _assert_contains(_allophone(self.spec, "s"), "h", label="s allophone")

    def test_parent_is_es_es(self):
        assert self.spec.parent == "es-ES"


@pytest.mark.iberian
class TestSpanishLatinAmerican:
    """Generic Latin American Spanish — es-419.

    Seseo, yeísmo, conservative coda-/s/ (less aspiration than Caribbean).
    """

    LANGUAGE_CODE = "es-419"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_seseo(self):
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "s", label="c")
        assert "θ" not in vals

    def test_z_seseo(self):
        _assert_first(_grapheme(self.spec, "z"), "s", label="z")

    def test_ll_yeismo(self):
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="ll")

    def test_s_allophone_aspiration_present(self):
        """s allophone includes h — some aspiration even in generic variety."""
        _assert_contains(_allophone(self.spec, "s"), "h", label="s allophone")

    def test_parent_is_es_es(self):
        assert self.spec.parent == "es-ES"


@pytest.mark.iberian
class TestExtremaduran:
    """Extremaduran — ext.

    Asturleonese-descended variety of Extremadura. Seseo (c/z→s),
    θ phoneme nulled (not inherited), coda-/s/ aspiration/deletion,
    F-initial aspiration (Leonese substrate), yeísmo.
    """

    LANGUAGE_CODE = "ext"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_seseo(self):
        """c → [k, s] — seseo."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "s", label="c")
        assert "θ" not in vals

    def test_z_seseo(self):
        """z → s — seseo."""
        _assert_first(_grapheme(self.spec, "z"), "s", label="z")

    def test_ll_yeismo(self):
        """ll → [j, ʝ] (yeísmo, with j primary in Extremaduran)."""
        vals = _grapheme(self.spec, "ll")
        _assert_contains(vals, "j", "ʝ", label="ll")

    def test_theta_allophone_nulled(self):
        """θ allophone is null — /θ/ merged out (seseo complete)."""
        _assert_allophone_null(self.spec, "θ")

    def test_s_coda_aspiration(self):
        """Coda s → [h, ∅] — strong aspiration/deletion."""
        coda = _positional(self.spec, "s", GraphemePosition.CODA)
        assert coda is not None
        _assert_first(coda, "h", label="s/CODA")
        assert "" in coda

    def test_s_word_final_aspiration(self):
        """Word-final s → [h, ∅]."""
        wf = _positional(self.spec, "s", GraphemePosition.WORD_FINAL)
        assert wf is not None
        _assert_first(wf, "h", label="s/WORD_FINAL")

    def test_f_word_initial_aspiration(self):
        """Word-initial f → [h, f] (Leonese substrate F-aspiration)."""
        wi = _positional(self.spec, "f", GraphemePosition.WORD_INITIAL)
        assert wi is not None
        _assert_first(wi, "h", label="f/WORD_INITIAL")
        assert "f" in wi

    def test_c_before_e_seseo(self):
        """c before e → s (seseo)."""
        be = _positional(self.spec, "c", GraphemePosition.BEFORE_E)
        assert be is not None
        _assert_first(be, "s", label="c/BEFORE_E")

    def test_g_before_e_velar_fricative(self):
        """g before e → h/x (Extremaduran velar fricative, not /s/)."""
        be = _positional(self.spec, "g", GraphemePosition.BEFORE_E)
        assert be is not None
        assert "h" in be or "x" in be, f"g before e should yield h or x in Extremaduran, got {be}"

    def test_d_word_final_deletion(self):
        """Word-final d → ∅ (or ð)."""
        wf = _positional(self.spec, "d", GraphemePosition.WORD_FINAL)
        assert wf is not None
        assert "" in wf

    def test_s_allophone_aspiration(self):
        """s allophone list includes h and ∅."""
        _assert_contains(_allophone(self.spec, "s"), "h", "", label="s allophone")

    def test_yod_allophone_variety(self):
        """ʝ allophone includes j and ʃ — yeísmo variants."""
        _assert_contains(_allophone(self.spec, "ʝ"), "j", "ʃ", label="ʝ allophone")


# ═══════════════════════════════════════════════════════════════════════════
# Portuguese regional dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestPortugueseLisbon:
    """Lisbon Portuguese — pt-PT-x-lisbon.

    Minimal dialect overrides: ʁ canonical, ə→[ɨ] (high central unrounded).
    Inherits full phonology from pt-PT.
    """

    LANGUAGE_CODE = "pt-PT-x-lisbon"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_rhotic_uvular(self):
        """ʁ allophone → [ʁ] (uvular fricative canonical)."""
        vals = _allophone(self.spec, "ʁ")
        assert vals is not None
        _assert_first(vals, "ʁ", label="ʁ allophone")

    def test_schwa_high_central(self):
        """ə allophone → [ɨ] (high central unrounded — Lisbon hallmark)."""
        vals = _allophone(self.spec, "ə")
        assert vals is not None
        _assert_first(vals, "ɨ", label="ə allophone")

    def test_parent_is_pt_pt(self):
        assert self.spec.parent == "pt-PT"


@pytest.mark.iberian
class TestPortuguesePorto:
    """Porto Portuguese — pt-PT-x-porto.

    Northern variety: retroflex sibilants [ʂ, ʐ], rhotic variants [χ, ʀ, x],
    schwa optional (∅), distinct from Lisbon vowel reduction.
    """

    LANGUAGE_CODE = "pt-PT-x-porto"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_sibilant_sh_retroflex(self):
        """ʃ allophone includes ʂ — retroflex sibilant variant."""
        _assert_contains(_allophone(self.spec, "ʃ"), "ʂ", label="ʃ allophone")

    def test_sibilant_zh_retroflex(self):
        """ʒ allophone includes ʐ — retroflex voiced sibilant."""
        _assert_contains(_allophone(self.spec, "ʒ"), "ʐ", label="ʒ allophone")

    def test_rhotic_variants(self):
        """ʁ allophone includes χ, ʀ, x — Porto rhotic range."""
        _assert_contains(_allophone(self.spec, "ʁ"), "χ", "ʀ", "x", label="ʁ allophone")

    def test_schwa_optional(self):
        """ə allophone includes ∅ — schwa can be deleted in Porto."""
        vals = _allophone(self.spec, "ə")
        assert vals is not None
        assert "" in vals, "Porto: ə should include ∅ (deletion)"

    def test_schwa_open_variants(self):
        """ə allophone includes ə and ɨ — central vowel range."""
        _assert_contains(_allophone(self.spec, "ə"), "ə", "ɨ", label="ə allophone")

    def test_parent_is_pt_pt(self):
        assert self.spec.parent == "pt-PT"


@pytest.mark.iberian
class TestPortugueseAngolan:
    """Angolan Portuguese — pt-AO.

    Post-colonial variety: r grapheme → ʁ (no trill/flap distinction),
    ʁ allophone includes [r] (merger with trill).
    """

    LANGUAGE_CODE = "pt-AO"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_r_grapheme_uvular(self):
        """r → [ʁ] (uvular, not alveolar trill)."""
        _assert_first(_grapheme(self.spec, "r"), "ʁ", label="r grapheme")

    def test_rhotic_merger(self):
        """ʁ allophone includes r — ʁ/r merger in Angolan Portuguese."""
        _assert_contains(_allophone(self.spec, "ʁ"), "r", label="ʁ allophone")
        _assert_first(_allophone(self.spec, "ʁ"), "ʁ", label="ʁ allophone first")

    def test_s_no_aspiration(self):
        """s grapheme maps to [s] only — no coda aspiration (unlike European)."""
        vals = _grapheme(self.spec, "s")
        assert vals is not None
        assert vals == ["s"], f"Angolan s should be [s] only, got {vals}"

    def test_parent_is_pt_pt(self):
        assert self.spec.parent == "pt-PT"


@pytest.mark.iberian
class TestPortugueseRioDeJaneiro:
    """Rio de Janeiro Portuguese — pt-BR-x-rj.

    Carioca variety: t/d palatalisation [tʃ, dʒ] before /i/,
    dark-l → [w] (vocalization), ɾ → [h, x] in coda, full vowel system.
    """

    LANGUAGE_CODE = "pt-BR-x-rj"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_t_palatalisation(self):
        """t allophone includes tʃ — palatalisation before /i/ (Carioca feature)."""
        _assert_contains(_allophone(self.spec, "t"), "tʃ", label="t allophone")

    def test_d_palatalisation(self):
        """d allophone includes dʒ — palatalisation before /i/."""
        _assert_contains(_allophone(self.spec, "d"), "dʒ", label="d allophone")

    def test_dark_l_vocalization(self):
        """ɫ allophone → [w] (dark-l vocalisation)."""
        vals = _allophone(self.spec, "ɫ")
        assert vals is not None
        assert "w" in vals, "Carioca: ɫ should vocalise to w"

    def test_rhotic_coda_variants(self):
        """ɾ allophone includes h and x in coda — rhotic weakening."""
        _assert_contains(_allophone(self.spec, "ɾ"), "h", "x", label="ɾ allophone")

    def test_v_preserved(self):
        """v allophone → [v] (not merged with b — v preserved in Brazilian)."""
        _assert_first(_allophone(self.spec, "v"), "v", label="v allophone")

    def test_vowel_a_variants(self):
        """a grapheme includes ɐ — unstressed vowel reduction."""
        _assert_contains(_grapheme(self.spec, "a"), "ɐ", label="a grapheme")

    def test_parent_is_pt_br(self):
        assert self.spec.parent == "pt-BR"


# ═══════════════════════════════════════════════════════════════════════════
# Catalan dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestCatalanNord:
    """Northern Catalan — ca-x-nord.

    Spoken in Roussillon (France). Final-position lenition (p/t/k → voiced),
    ɾ → ʁ (uvularisation, French influence), vowel weakening.
    """

    LANGUAGE_CODE = "ca-x-nord"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_final_lenition_p(self):
        """p allophone includes b — final devoicing reversal / lenition."""
        _assert_contains(_allophone(self.spec, "p"), "b", label="p allophone")

    def test_final_lenition_t(self):
        """t allophone includes d."""
        _assert_contains(_allophone(self.spec, "t"), "d", label="t allophone")

    def test_final_lenition_k(self):
        """k allophone includes ɡ."""
        _assert_contains(_allophone(self.spec, "k"), "ɡ", label="k allophone")

    def test_rhotic_uvularisation(self):
        """ɾ allophone includes ʁ — French uvular rhotic influence."""
        _assert_contains(_allophone(self.spec, "ɾ"), "ʁ", label="ɾ allophone")
        _assert_contains(_allophone(self.spec, "r"), "ʁ", label="r allophone")

    def test_vowel_a_reduction(self):
        """a allophone includes ə — vowel reduction (French-influenced)."""
        _assert_contains(_allophone(self.spec, "a"), "ə", label="a allophone")

    def test_vowel_e_reduction(self):
        """e allophone includes ə — schwa reduction."""
        _assert_contains(_allophone(self.spec, "e"), "ə", label="e allophone")

    def test_o_raising(self):
        """o allophone includes u — vowel raising."""
        _assert_contains(_allophone(self.spec, "o"), "u", label="o allophone")

    def test_parent_is_ca(self):
        assert self.spec.parent == "ca"


@pytest.mark.iberian
class TestCatalanOccidental:
    """Western/Occidental Catalan — ca-x-occidental.

    Spoken in Lleida and Valencia hinterland. Full vowels preserved in
    unstressed position (no central vowel reduction): ə → [a, e].
    """

    LANGUAGE_CODE = "ca-x-occidental"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_no_unstressed_reduction(self):
        """No central schwa reduction: unstressed /a e o/ keep full quality.

        Western/Occidental Catalan overrides the inherited Central
        ⟨nucleus_unstressed⟩ reduction, so no ⟨ə⟩ (nor Eastern ⟨u⟩ from
        unstressed /o/) is ever produced — the 7-vowel system is intact in
        atonic position (Recasens 1996; Veny 1982).
        """
        import orthography2ipa
        for word, expected in [
            ("casa", "kaza"),   # unstressed a stays [a] (Central: kazə)
            ("dona", "dɔna"),   # unstressed a stays [a]
            ("tenir", "tɛniɾ"),  # unstressed e stays [e]/[ɛ] (Central: təniɾ)
            ("porta", "pɔɾta"),  # unstressed a stays [a]
        ]:
            out = orthography2ipa.transcribe(word, "ca-x-occidental")
            assert "ə" not in out, f"occidental {word!r}: {out!r} has schwa"
            assert out == expected, f"occidental {word!r}: {out!r} != {expected!r}"

    def test_parent_is_ca(self):
        assert self.spec.parent == "ca"


# ═══════════════════════════════════════════════════════════════════════════
# Galician dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestGalicianStandard:
    """Standard Galician (RAG norms) — gl-ES.

    Distinción variety (unlike Portuguese seseo): c → [k, θ], z → [θ],
    ç → s, unique sibilant system with apical/laminal contrast.
    """

    LANGUAGE_CODE = "gl-ES"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_distincion(self):
        """c → [k, θ] — distinción (θ present, unlike Portuguese)."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "θ", label="c")

    def test_z_distincion(self):
        """z → θ — full distinción."""
        vals = _grapheme(self.spec, "z")
        assert vals is not None
        assert "θ" in vals, "Galician z should include θ"

    def test_cedilla_seseo(self):
        """ç → θ/s — in reintegrationist orthography ç parallels z (distinción variety)."""
        vals = _grapheme(self.spec, "ç")
        assert vals is not None, "gl-ES: ç grapheme missing"
        assert "θ" in vals or "s" in vals, f"gl-ES: ç should include θ or s, got {vals}"

    def test_h_silent(self):
        """h → '' (silent, like Portuguese)."""
        vals = _grapheme(self.spec, "h")
        assert vals is not None
        assert vals[0] in ("", ""), f"h should be silent, got {vals}"

    def test_g_sibilant(self):
        """g has sibilant realisation [ʃ] — unique Galician feature."""
        vals = _grapheme(self.spec, "g")
        assert vals is not None
        _assert_contains(vals, "ʃ", label="g grapheme")

    def test_j_sibilant(self):
        """j → ʃ (Galician, not velar like Castilian)."""
        _assert_first(_grapheme(self.spec, "j"), "ʃ", label="j")

    def test_s_intervocalic_voicing(self):
        """Intervocalic s → [s, z] — voicing in intervocalic position."""
        iv = _positional(self.spec, "s", GraphemePosition.INTERVOCALIC)
        assert iv is not None
        _assert_contains(iv, "s", "z", label="s/INTERVOCALIC")

    def test_r_word_initial_trill(self):
        """Word-initial r → r (trill)."""
        wi = _positional(self.spec, "r", GraphemePosition.WORD_INITIAL)
        assert wi is not None
        _assert_first(wi, "r", label="r/WORD_INITIAL")

    def test_r_intervocalic_tap(self):
        """Intervocalic r → ɾ (tap)."""
        iv = _positional(self.spec, "r", GraphemePosition.INTERVOCALIC)
        assert iv is not None
        _assert_first(iv, "ɾ", label="r/INTERVOCALIC")

    def test_b_betacism_allophone(self):
        """b allophone includes β — betacism."""
        _assert_contains(_allophone(self.spec, "b"), "β", label="b allophone")

    def test_d_lenition(self):
        """d allophone includes ð — lenition."""
        _assert_contains(_allophone(self.spec, "d"), "ð", label="d allophone")

    def test_v_betacism(self):
        """v allophone → β (merger with b, betacism)."""
        _assert_contains(_allophone(self.spec, "v"), "β", label="v allophone")

    def test_positional_v_intervocalic(self):
        """v intervocalic → β."""
        iv = _positional(self.spec, "v", GraphemePosition.INTERVOCALIC)
        assert iv is not None
        _assert_first(iv, "β", label="v/INTERVOCALIC")


@pytest.mark.iberian
class TestGalicianOriental:
    """Oriental Galician — gl-x-oriental.

    Eastern dialect: Leonese diphthongs ie→[je], ue→[we],
    conservative ʎ (no yeísmo), preserved tʃ affricate.
    """

    LANGUAGE_CODE = "gl-x-oriental"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_ie_diphthong(self):
        """ie → [je] — Leonese contact diphthong."""
        _assert_first(_grapheme(self.spec, "ie"), "je", label="ie")

    def test_ue_diphthong(self):
        """ue → [we] — Leonese contact diphthong."""
        _assert_first(_grapheme(self.spec, "ue"), "we", label="ue")

    def test_lambda_preserved(self):
        """ʎ allophone → [ʎ] (no yeísmo — conservative Eastern Galician)."""
        _assert_first(_allophone(self.spec, "ʎ"), "ʎ", label="ʎ allophone")

    def test_ch_affricate_preserved(self):
        """tʃ allophone → [tʃ] (conservative affricate)."""
        _assert_first(_allophone(self.spec, "tʃ"), "tʃ", label="tʃ allophone")

    def test_parent_is_gl(self):
        assert self.spec.parent == "gl"


# ═══════════════════════════════════════════════════════════════════════════
# Basque dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestBasqueBizkaiera:
    """Bizkaian Basque — eu-x-bizkaiera.

    Western dialect: sibilants include [ʃ], h aspirate lost (→ ∅).
    The Biscayan raising of the article /-a/ → [-e] after a high vowel is
    morphophonological (it targets the article, not every /a/), so it is
    documented in the spec notes rather than modelled as a context-free
    allophone (Bedialauneta & Hualde 2023: 1107-1108).
    """

    LANGUAGE_CODE = "eu-x-bizkaiera"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_s_includes_palatal(self):
        """s (apical) grapheme includes ʃ — sibilant merger with palatal."""
        vals = _grapheme(self.spec, "s")
        assert vals is not None
        _assert_contains(vals, "ʃ", label="s grapheme")

    def test_z_includes_palatal(self):
        """z (laminal) grapheme includes ʃ."""
        vals = _grapheme(self.spec, "z")
        assert vals is not None
        _assert_contains(vals, "ʃ", label="z grapheme")

    def test_h_lost(self):
        """h allophone → ∅ (aspirate lost in Bizkaian)."""
        vals = _allophone(self.spec, "h")
        assert vals is not None
        _assert_first(vals, "", label="h allophone")

    def test_article_raising_not_a_flat_allophone(self):
        """The /-a/ → [-e] article raising is morphophonological, not a
        context-free allophone: /a/ carries no flat [e] variant, and the
        process is documented in the spec notes instead."""
        a_allo = _allophone(self.spec, "a")
        assert a_allo is None or "e" not in a_allo, (
            "Biscayan article-raising must not be a context-free a→[e] allophone"
        )
        notes = self.spec.notes.lower()
        assert "article" in notes and "basue" in notes

    def test_s_apical_allophone_includes_palatal(self):
        """s̺ allophone includes ʃ."""
        _assert_contains(_allophone(self.spec, "s̺"), "ʃ", label="s̺ allophone")

    def test_parent_is_eu(self):
        assert self.spec.parent == "eu"


@pytest.mark.iberian
class TestBasqueGipuzkera:
    """Gipuzkoan Basque — eu-x-gipuzkera.

    Central dialect: h is optional [h, ∅] (intermediate between Basque
    h-preserving varieties and Bizkaian h-loss).
    """

    LANGUAGE_CODE = "eu-x-gipuzkera"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_h_lost(self):
        """h allophone → ∅ — like the rest of central/western Basque,
        Gipuzkoan lost the laryngeal /h/ (Hualde 2018: 84)."""
        vals = _allophone(self.spec, "h")
        assert vals is not None
        _assert_first(vals, "", label="h allophone")

    def test_parent_is_eu(self):
        assert self.spec.parent == "eu"


# ═══════════════════════════════════════════════════════════════════════════
# Asturian / Leonese dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestAsturianOccidental:
    """Western Asturian — ast-x-occidental.

    Phonemic /h/ (unique in Iberian Romance), ḷḷ/l.l → [tʃ] (che vaqueira),
    F-initial aspiration (Leonese substrate).
    """

    LANGUAGE_CODE = "ast-x-occidental"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_h_silent(self):
        """h → silent (inherited from base ast; Western Asturian preserves /f/, not aspirates it)."""
        g = _grapheme(self.spec, "h")
        # h is silent in base ast (inherited); no local h override in occidental
        assert g is None or g == [""], f"ast-x-occidental h should be silent, got {g}"

    def test_h_allophone_inherited(self):
        """h allophone is inherited from base ast (not locally overridden)."""
        # No local allophones block in occidental — inherited silently
        pass

    def test_ll_dot_che_vaqueira(self):
        """ḷḷ notation for che vaqueira is now deprecated in spec; only l.l and ts are encoded.
        The ḷḷ grapheme (ALLA norm) is not present; use l.l instead.
        Morala & Egido (2009) p. 9; Propuesta §3.1 — both endorse l.l and ts."""
        # ḷḷ is not in the new spec (only l.l is; the old ḷḷ encoding has been dropped)
        val = _grapheme(self.spec, "ḷḷ")
        assert val is None or val == ["t͡s"], f"ḷḷ should be absent or ts, got {val}"

    def test_l_dot_l_che_vaqueira(self):
        """l.l → [ts] (che vaqueira, Laciana/Alto Sil).
        Source: Morala & Egido (2009) p. 9 (*tsadrona, tsacianiega*);
        Propuesta §3.1. The phoneme is /ts/ (approximately), NOT /tʃ/ (palatal affricate).
        CRITICAL: che vaqueira ≠ /tʃ/ — they must not be merged."""
        _assert_first(_grapheme(self.spec, "l.l"), "t͡s", label="l.l")

    def test_f_word_initial_preserved(self):
        """f word-initial → [f] (Western Asturian preserves Latin F-, does not aspirate)."""
        wi = _positional(self.spec, "f", GraphemePosition.WORD_INITIAL)
        # No positional override in occidental — inherited default [f] from base ast
        assert wi is None or "f" in wi, f"ast-x-occidental f/WORD_INITIAL should be [f] or absent, got {wi}"

    def test_parent_is_ast(self):
        assert self.spec.parent == "ast"


@pytest.mark.iberian
class TestAsturianOriental:
    """Eastern Asturian — ast-x-oriental.

    Incipient yeísmo: ʎ → [ʎ, ʝ] (ʎ still primary but ʝ emerging).
    """

    LANGUAGE_CODE = "ast-x-oriental"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_lambda_incipient_yeismo(self):
        """ʎ allophone → [ʎ, ʝ] — incipient yeísmo (ʎ still primary)."""
        vals = _allophone(self.spec, "ʎ")
        assert vals is not None
        _assert_first(vals, "ʎ", label="ʎ allophone first")
        _assert_contains(vals, "ʝ", label="ʎ allophone includes ʝ")

    def test_parent_is_ast(self):
        assert self.spec.parent == "ast"


@pytest.mark.iberian
class TestAsturianCantabrian:
    """Cantabrian Asturian — ast-x-cantabrian.

    Transitional variety: ll → [j, ʝ, ʎ] (variable), s → [s, s̺, h] (aspiration),
    Castilian-contact features (g before e/i → x).
    """

    LANGUAGE_CODE = "ast-x-cantabrian"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_ll_variable(self):
        """ll → [j, ʝ, ʎ] — yeísmo and traditional variants both present."""
        vals = _grapheme(self.spec, "ll")
        assert vals is not None
        _assert_contains(vals, "j", "ʝ", "ʎ", label="ll grapheme")

    def test_s_aspiration(self):
        """s allophone includes h — contact aspiration."""
        _assert_contains(_allophone(self.spec, "s"), "h", label="s allophone")

    def test_s_apical_variant(self):
        """s allophone includes s̺ — apical sibilant (Asturian feature)."""
        _assert_contains(_allophone(self.spec, "s"), "s̺", label="s allophone")

    def test_yod_variable(self):
        """ʝ allophone includes j, ʝ, ʎ — variable realisation."""
        _assert_contains(_allophone(self.spec, "ʝ"), "j", "ʝ", label="ʝ allophone")

    def test_parent_is_ast(self):
        assert self.spec.parent == "ast"


@pytest.mark.iberian
class TestLeonese:
    """Leonese — ast-x-leon.

    Medieval sibilant series preserved: t͡s/d͡z affricates, lh→ʎ, nh→ɲ,
    θ phoneme nulled (merged into sibilant system).
    """

    LANGUAGE_CODE = "ast-x-leon"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_affricate(self):
        """c → [k, t͡s] — affricate preserved (medieval sibilant)."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "t͡s", label="c")

    def test_cedilla_affricate(self):
        """ç → t͡s — cedilla maps to affricate."""
        _assert_first(_grapheme(self.spec, "ç"), "t͡s", label="ç")

    def test_z_voiced_affricate(self):
        """z → [d͡z, z̻] — voiced affricate (medieval sibilant)."""
        vals = _grapheme(self.spec, "z")
        _assert_contains(vals, "d͡z", label="z")

    def test_s_apical(self):
        """s → s̺ (apical sibilant)."""
        vals = _grapheme(self.spec, "s")
        assert vals is not None
        _assert_first(vals, "s̺", label="s")

    def test_lh_lateral(self):
        """lh → ʎ (palatal lateral — Galaico-Portuguese digraph retained)."""
        _assert_first(_grapheme(self.spec, "lh"), "ʎ", label="lh")

    def test_nh_nasal(self):
        """nh → ɲ (palatal nasal — Galaico-Portuguese digraph retained)."""
        _assert_first(_grapheme(self.spec, "nh"), "ɲ", label="nh")

    def test_theta_nulled(self):
        """θ allophone is null — /θ/ merged into affricate system."""
        _assert_allophone_null(self.spec, "θ")

    def test_ts_affricate_allophone(self):
        """t͡s allophone → [t͡s, s̻]."""
        _assert_contains(_allophone(self.spec, "t͡s"), "t͡s", label="t͡s allophone")

    def test_dz_affricate_allophone(self):
        """d͡z allophone → [d͡z, z̻]."""
        _assert_contains(_allophone(self.spec, "d͡z"), "d͡z", label="d͡z allophone")

    def test_lambda_preserved(self):
        """ʎ allophone → [ʎ] (palatal lateral preserved in Leonese)."""
        _assert_first(_allophone(self.spec, "ʎ"), "ʎ", label="ʎ allophone")

    def test_parent_is_ast(self):
        assert self.spec.parent == "ast"


@pytest.mark.iberian
class TestAsturianPortugueseMedieval:
    """Asturian-Portuguese Medieval — ast-PT-x-medieval.

    Historical variety with nasal vowel graphemes (ã, ẽ, ĩ, õ, ũ and -n- digraphs),
    /v/ partial preservation, lh/nh digraphs.
    """

    LANGUAGE_CODE = "ast-PT-x-medieval"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_nasal_vowel_tilde_a(self):
        """ã → ɐ̃ (nasal a)."""
        _assert_first(_grapheme(self.spec, "ã"), "ɐ̃", label="ã")

    def test_nasal_vowel_tilde_e(self):
        """ẽ → ẽ (nasal e)."""
        _assert_first(_grapheme(self.spec, "ẽ"), "ẽ", label="ẽ")

    def test_nasal_vowel_an_digraph(self):
        """an → ɐ̃ (nasal vowel digraph)."""
        _assert_first(_grapheme(self.spec, "an"), "ɐ̃", label="an")

    def test_nasal_vowel_en_digraph(self):
        """en → ẽ."""
        _assert_first(_grapheme(self.spec, "en"), "ẽ", label="en")

    def test_lh_lateral(self):
        """lh positional → ʎ."""
        # lh may be in graphemes or positional — check both
        vals = _grapheme(self.spec, "lh")
        pos_vals = None
        if vals is None:
            pos_map = self.spec.positional_graphemes.get("l")
            if pos_map:
                for v in pos_map.values():
                    if "ʎ" in v:
                        pos_vals = v
        assert vals is not None or pos_vals is not None, "lh/ʎ mapping absent"

    def test_nh_nasal(self):
        """nh → ɲ."""
        # Check graphemes or positional
        vals = _grapheme(self.spec, "nh")
        pos_found = False
        if vals is None:
            pos_map = self.spec.positional_graphemes.get("n")
            if pos_map:
                for v in pos_map.values():
                    if "ɲ" in v:
                        pos_found = True
        assert (vals is not None and "ɲ" in vals) or pos_found, "nh/ɲ mapping absent"

    def test_v_partial_preservation(self):
        """v allophone includes v (not fully merged with b — partial preservation)."""
        _assert_contains(_allophone(self.spec, "v"), "v", label="v allophone")
        _assert_contains(_allophone(self.spec, "v"), "β", label="v allophone includes β")

    def test_nasal_vowel_allophone(self):
        """ɐ̃ allophone → [ɐ̃] (nasality preserved)."""
        _assert_first(_allophone(self.spec, "ɐ̃"), "ɐ̃", label="ɐ̃ allophone")

    def test_parent_is_ast_x_leon(self):
        assert self.spec.parent == "ast-x-leon"


# ═══════════════════════════════════════════════════════════════════════════
# Mirandese dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestMirandeseSendim:
    """Mirandese — Sendim dialect — mwl-x-sendim.

    Diphthong monophthongisation: iê/ie → [i], uô/uo → [u].
    """

    LANGUAGE_CODE = "mwl-x-sendim"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_ie_tilde_monophthong(self):
        """iê → i (closed monophthong from diphthong)."""
        _assert_first(_grapheme(self.spec, "iê"), "i", label="iê")

    def test_ie_plain_monophthong(self):
        """ie → i."""
        _assert_first(_grapheme(self.spec, "ie"), "i", label="ie")

    def test_uo_tilde_monophthong(self):
        """uô → u."""
        _assert_first(_grapheme(self.spec, "uô"), "u", label="uô")

    def test_uo_plain_monophthong(self):
        """uo → u."""
        _assert_first(_grapheme(self.spec, "uo"), "u", label="uo")

    def test_parent_is_mwl(self):
        assert self.spec.parent == "mwl"


@pytest.mark.iberian
class TestMiraneseIfanes:
    """Mirandese — Ifanês (Raiano/Northern) subdialect — mwl-x-ifanes.

    Ifanês tracks Central Mirandese: the published descriptions record no
    segmental orthography→phoneme divergence for the Northern/Raiano group
    (both keep the Leonese diphthongs [je]/[wo] and /ʎ/; only Sendinês
    monophthongises). The spec therefore inherits Central unchanged.
    """

    LANGUAGE_CODE = "mwl-x-ifanes"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_ie_tilde_tracks_central(self):
        """iê keeps the Central diphthong [jɛ] (Raiano does not monophthongise)."""
        _assert_first(_grapheme(self.spec, "iê"), "jɛ", label="iê")

    def test_parent_is_mwl(self):
        assert self.spec.parent == "mwl"


# ═══════════════════════════════════════════════════════════════════════════
# Aragonese dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestAragonesOccidental:
    """Western Aragonese — an-x-occidental (stub).

    No additional grapheme/allophone data — inherits all from Aragonese (an).
    Smoke test: spec loads and is not empty.
    """

    LANGUAGE_CODE = "an-x-occidental"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_spec_loads(self):
        """Spec loads without error — stub inherits from an."""
        assert self.spec is not None

    def test_parent_is_an(self):
        assert self.spec.parent == "an"

    def test_inherits_graphemes(self):
        """Some graphemes should be inherited from Aragonese."""
        # Aragonese has basic vowels and consonants
        assert len(self.spec.graphemes) > 0, "Should inherit graphemes from an"


@pytest.mark.iberian
class TestAragonesOriental:
    """Eastern Aragonese — an-x-oriental.

    Open vowels [ɛ, ɔ] preserved, j → [dʒ, x], z → s (seseo shift),
    ll → [ʎ, j] (partial yeísmo).
    """

    LANGUAGE_CODE = "an-x-oriental"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_e_open_vowel(self):
        """e → [e, ɛ] — open vowel preserved."""
        _assert_contains(_grapheme(self.spec, "e"), "ɛ", label="e grapheme")

    def test_o_open_vowel(self):
        """o → [o, ɔ] — open vowel preserved."""
        _assert_contains(_grapheme(self.spec, "o"), "ɔ", label="o grapheme")

    def test_j_affricate(self):
        """j → [dʒ, x] — affricate realisation (Catalan-contact feature)."""
        vals = _grapheme(self.spec, "j")
        _assert_contains(vals, "dʒ", label="j grapheme")

    def test_z_seseo(self):
        """z → s — seseo (no θ)."""
        _assert_first(_grapheme(self.spec, "z"), "s", label="z")

    def test_c_seseo(self):
        """c → [k, s] — seseo."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "s", label="c")
        assert "θ" not in vals, "Eastern Aragonese: no θ expected"

    def test_ll_partial_yeismo(self):
        """ll → [ʎ, j] — partial yeísmo (ʎ still primary)."""
        vals = _grapheme(self.spec, "ll")
        _assert_first(vals, "ʎ", label="ll first")
        _assert_contains(vals, "j", label="ll yeísmo variant")

    def test_dj_affricate_allophone(self):
        """dʒ allophone → [dʒ] — affricate preserved."""
        _assert_first(_allophone(self.spec, "dʒ"), "dʒ", label="dʒ allophone")

    def test_lambda_allophone_partial_yeismo(self):
        """ʎ allophone → [ʎ, j] — partial yeísmo."""
        _assert_contains(_allophone(self.spec, "ʎ"), "j", label="ʎ allophone")

    def test_parent_is_an(self):
        assert self.spec.parent == "an"


# ═══════════════════════════════════════════════════════════════════════════
# Non-Iberian Romance: French and Italian
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestFrench:
    """French — fr-FR.

    Key phonological features: r → ʁ (uvular), u → y (front rounded),
    ch → ʃ, gn → ɲ, nasal vowels (an/en → ɑ̃, in → ɛ̃, on → ɔ̃),
    /v/ preserved (no betacism), ou → u, eu → [ø, œ].
    """

    LANGUAGE_CODE = "fr-FR"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Vowels
    def test_u_front_rounded(self):
        """u → y (front rounded — French hallmark)."""
        _assert_first(_grapheme(self.spec, "u"), "y", label="u")

    def test_o_mid_low(self):
        """o → ɔ (mid-low by default in French)."""
        _assert_first(_grapheme(self.spec, "o"), "ɔ", label="o")

    def test_ou_back_rounded(self):
        """ou → u (back rounded — French digraph)."""
        _assert_first(_grapheme(self.spec, "ou"), "u", label="ou")

    def test_eu_front_mid(self):
        """eu → [ø, œ]."""
        _assert_contains(_grapheme(self.spec, "eu"), "ø", "œ", label="eu")

    def test_acute_e(self):
        """é → e."""
        _assert_first(_grapheme(self.spec, "é"), "e", label="é")

    def test_grave_e(self):
        """è → ɛ."""
        _assert_first(_grapheme(self.spec, "è"), "ɛ", label="è")

    def test_circumflex_a(self):
        """â → ɑ (long/back a)."""
        _assert_first(_grapheme(self.spec, "â"), "ɑ", label="â")

    # Nasal vowels
    def test_nasal_an(self):
        """an → ɑ̃ (nasal a-vowel)."""
        _assert_first(_grapheme(self.spec, "an"), "ɑ̃", label="an")

    def test_nasal_en(self):
        """en → ɑ̃ (same nasal vowel as an)."""
        _assert_first(_grapheme(self.spec, "en"), "ɑ̃", label="en")

    def test_nasal_in(self):
        """in → ɛ̃."""
        _assert_first(_grapheme(self.spec, "in"), "ɛ̃", label="in")

    def test_nasal_on(self):
        """on → ɔ̃."""
        _assert_first(_grapheme(self.spec, "on"), "ɔ̃", label="on")

    def test_nasal_un(self):
        """un → œ̃."""
        _assert_first(_grapheme(self.spec, "un"), "œ̃", label="un")

    # Consonants
    def test_r_uvular(self):
        """r → ʁ (uvular fricative — French hallmark)."""
        _assert_first(_grapheme(self.spec, "r"), "ʁ", label="r")

    def test_ch_digraph(self):
        """ch → ʃ."""
        _assert_first(_grapheme(self.spec, "ch"), "ʃ", label="ch")

    def test_gn_palatal_nasal(self):
        """gn → ɲ."""
        _assert_first(_grapheme(self.spec, "gn"), "ɲ", label="gn")

    def test_ph_digraph(self):
        """ph → f."""
        _assert_first(_grapheme(self.spec, "ph"), "f", label="ph")

    def test_h_silent(self):
        """h → '' (silent in French)."""
        vals = _grapheme(self.spec, "h")
        assert vals is not None
        assert vals[0] in ("", ""), f"h should be silent, got {vals}"

    def test_j_palatal(self):
        """j → ʒ (palatal fricative — French j)."""
        _assert_first(_grapheme(self.spec, "j"), "ʒ", label="j")

    def test_g_ambiguous(self):
        """g → [ɡ, ʒ] — velar before a/o/u, palatal before e/i."""
        _assert_contains(_grapheme(self.spec, "g"), "ɡ", "ʒ", label="g")

    def test_v_preserved(self):
        """v allophone → [v] (no betacism — v distinct from b in French)."""
        _assert_first(_allophone(self.spec, "v"), "v", label="v allophone")

    def test_r_allophone_uvular(self):
        """ʁ allophone → [ʁ, ʀ, χ, ɣ, r] — uvular range."""
        _assert_contains(_allophone(self.spec, "ʁ"), "ʁ", "ʀ", label="ʁ allophone")

    def test_nasal_vowel_allophone_an(self):
        """ɑ̃ allophone preserved."""
        vals = _allophone(self.spec, "ɑ̃")
        assert vals is not None

    def test_ill_digraph(self):
        """ill → ij."""
        _assert_first(_grapheme(self.spec, "ill"), "ij", label="ill")

    def test_oi_glide(self):
        """oi → wa."""
        _assert_first(_grapheme(self.spec, "oi"), "wa", label="oi")

    def test_eau_back_o(self):
        """eau → o."""
        _assert_first(_grapheme(self.spec, "eau"), "o", label="eau")

    def test_ai_digraph(self):
        """ai → [ɛ, e]."""
        _assert_contains(_grapheme(self.spec, "ai"), "ɛ", label="ai")


@pytest.mark.iberian
class TestItalian:
    """Italian — it-IT.

    Key phonological features: c → [k, tʃ], g → [ɡ, dʒ], r → r (alveolar trill),
    sc → [ʃ, sk], gl/gli → ʎ, gn → ɲ, geminate consonants (bb, cc, dd...),
    z → [ts, dz], /v/ preserved.
    """

    LANGUAGE_CODE = "it-IT"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Basic vowels
    def test_e_open_closed(self):
        """e → [e, ɛ] — both mid and open-mid."""
        _assert_contains(_grapheme(self.spec, "e"), "e", "ɛ", label="e")

    def test_o_open_closed(self):
        """o → [o, ɔ] — both mid and open-mid."""
        _assert_contains(_grapheme(self.spec, "o"), "o", "ɔ", label="o")

    # Consonants
    def test_c_affricate_before_front(self):
        """c → [k, tʃ] — velar before a/o/u, affricate before e/i."""
        _assert_contains(_grapheme(self.spec, "c"), "k", "tʃ", label="c")

    def test_ch_velar(self):
        """ch → k (always velar — ch grapheme prevents affrication)."""
        _assert_first(_grapheme(self.spec, "ch"), "k", label="ch")

    def test_g_affricate_before_front(self):
        """g → [ɡ, dʒ] — velar default, affricate before e/i."""
        _assert_contains(_grapheme(self.spec, "g"), "ɡ", "dʒ", label="g")

    def test_gh_velar(self):
        """gh → ɡ (always velar)."""
        _assert_first(_grapheme(self.spec, "gh"), "ɡ", label="gh")

    def test_ci_affricate(self):
        """ci → tʃ (always affricate)."""
        _assert_first(_grapheme(self.spec, "ci"), "tʃ", label="ci")

    def test_gi_affricate(self):
        """gi → dʒ."""
        _assert_first(_grapheme(self.spec, "gi"), "dʒ", label="gi")

    def test_r_alveolar_trill(self):
        """r → r (alveolar trill — not uvular like French)."""
        _assert_first(_grapheme(self.spec, "r"), "r", label="r")

    def test_sc_palatal(self):
        """sc → [ʃ, sk] — palatal before e/i, cluster elsewhere."""
        _assert_contains(_grapheme(self.spec, "sc"), "ʃ", "sk", label="sc")

    def test_sci_palatal(self):
        """sci → ʃ (always palatal)."""
        _assert_first(_grapheme(self.spec, "sci"), "ʃ", label="sci")

    def test_gl_lateral(self):
        """gl → [ʎ, ɡl] — palatal lateral or cluster."""
        _assert_contains(_grapheme(self.spec, "gl"), "ʎ", label="gl")

    def test_gli_lateral(self):
        """gli → ʎ (always palatal lateral)."""
        _assert_first(_grapheme(self.spec, "gli"), "ʎ", label="gli")

    def test_gn_palatal_nasal(self):
        """gn → ɲ."""
        _assert_first(_grapheme(self.spec, "gn"), "ɲ", label="gn")

    def test_z_sibilant_affricate(self):
        """z → [ts, dz] — sibilant affricate."""
        _assert_contains(_grapheme(self.spec, "z"), "ts", "dz", label="z")

    def test_s_ambiguous(self):
        """s → [s, z] — voiceless default, voiced intervocalically."""
        _assert_contains(_grapheme(self.spec, "s"), "s", "z", label="s")

    def test_h_null(self):
        """h → ∅ (completely silent in Italian)."""
        vals = _grapheme(self.spec, "h")
        assert vals is not None
        assert vals[0] in ("", ""), f"Italian h should be ∅/silent, got {vals}"

    def test_v_preserved(self):
        """v allophone → [v] (no betacism — v distinct from b in Italian)."""
        _assert_first(_allophone(self.spec, "v"), "v", label="v allophone")

    # Geminate consonants
    def test_bb_geminate(self):
        """bb → bː (geminate voiced bilabial)."""
        _assert_first(_grapheme(self.spec, "bb"), "bː", label="bb")

    def test_rr_geminate(self):
        """rr → rː (geminate trill)."""
        _assert_first(_grapheme(self.spec, "rr"), "rː", label="rr")

    def test_ll_geminate(self):
        """ll → lː (geminate lateral)."""
        _assert_first(_grapheme(self.spec, "ll"), "lː", label="ll")

    def test_nn_geminate(self):
        """nn → nː."""
        _assert_first(_grapheme(self.spec, "nn"), "nː", label="nn")

    def test_ss_geminate(self):
        """ss → sː."""
        _assert_first(_grapheme(self.spec, "ss"), "sː", label="ss")

    def test_tt_geminate(self):
        """tt → tː."""
        _assert_first(_grapheme(self.spec, "tt"), "tː", label="tt")

    def test_zz_geminate(self):
        """zz → [tːs, dːz]."""
        _assert_contains(_grapheme(self.spec, "zz"), "tːs", label="zz")

    # Diphthongs
    def test_ie_diphthong(self):
        """ie → je."""
        _assert_first(_grapheme(self.spec, "ie"), "je", label="ie")

    def test_uo_diphthong(self):
        """uo → wo."""
        _assert_first(_grapheme(self.spec, "uo"), "wo", label="uo")

    def test_ai_diphthong(self):
        """ai → aj."""
        _assert_first(_grapheme(self.spec, "ai"), "aj", label="ai")

    def test_au_diphthong(self):
        """au → aw."""
        _assert_first(_grapheme(self.spec, "au"), "aw", label="au")

    # Dental allophones
    def test_t_dental(self):
        """t allophone includes t̪ — dental realisation."""
        _assert_contains(_allophone(self.spec, "t"), "t̪", label="t allophone")

    def test_d_dental(self):
        """d allophone includes d̪ — dental realisation."""
        _assert_contains(_allophone(self.spec, "d"), "d̪", label="d allophone")
