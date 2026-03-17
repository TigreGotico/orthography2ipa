"""Per-language accuracy tests for additional Romance languages and dialects.

Covers:
- Italian regional dialects: Tuscan (it-IT-x-toscana), Roman (it-IT-x-roma),
  Calabrian (it-IT-x-calabria)
- Romanian (ro-RO)
- Sardinian: Standard (sc), Logudorese (sc-x-logudorese), Campidanese (sc-x-campidanese)
- Occitan Aranese (oc-x-aranes)
- Spanish Caribbean/Central: Cuban (es-CU), Puerto Rican (es-PR), Dominican (es-DO)
- Spanish medieval (es-ES-x-medieval)
- Spanish Cantabrian (es-ES-x-cantabria)
- Portuguese Brazilian dialects: Caipira (pt-BR-x-caipira), Bahian (pt-BR-x-bahia)
- Portuguese European dialects: Azorean (pt-PT-x-acores), Alentejo (pt-PT-x-alentejo),
  Minho (pt-PT-x-minho)
"""
from __future__ import annotations

import pytest
import orthography2ipa
from orthography2ipa.types import GraphemePosition

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

_SENTINEL = object()


def _load(code: str):
    """Load a LanguageSpec by code, skip the test if the code is not available."""
    try:
        return orthography2ipa.get(code)
    except Exception as exc:
        pytest.skip(f"{code!r} not available: {exc}")


def _grapheme(spec, grapheme: str) -> list[str] | None:
    """Return the IPA candidate list for *grapheme*, or None if absent."""
    return spec.graphemes.get(grapheme)


def _allophone(spec, phoneme: str) -> list[str] | None:
    """Return the surface-realisation list for *phoneme*, or None if absent."""
    return spec.allophones.get(phoneme)


def _positional(spec, grapheme: str, position: GraphemePosition) -> list[str] | None:
    """Return the positional override for *grapheme* at *position*, or None."""
    pos_map = spec.positional_graphemes.get(grapheme)
    if pos_map is None:
        return None
    return pos_map.get(position)


def _assert_contains(
    values: list[str] | None, *expected: str, label: str = ""
) -> None:
    """Assert *values* is not None and contains every *expected* string."""
    assert values is not None, f"{label}: mapping is absent"
    for exp in expected:
        assert exp in values, f"{label}: {exp!r} not in {values}"


def _assert_first(
    values: list[str] | None, expected: str, label: str = ""
) -> None:
    """Assert the first (most common) realisation equals *expected*."""
    assert values is not None, f"{label}: mapping is absent"
    assert values[0] == expected, (
        f"{label}: expected first={expected!r}, got {values[0]!r}"
    )


def _assert_null(spec, grapheme: str) -> None:
    """Assert *grapheme* is absent or explicitly null in spec.graphemes."""
    result = spec.graphemes.get(grapheme, _SENTINEL)
    assert result is _SENTINEL or result is None, (
        f"grapheme {grapheme!r} should be absent/null but is {result!r}"
    )


def _assert_allophone_null(spec, phoneme: str) -> None:
    """Assert *phoneme* is absent or explicitly null in spec.allophones."""
    result = spec.allophones.get(phoneme, _SENTINEL)
    assert result is _SENTINEL or result is None, (
        f"allophone {phoneme!r} should be absent/null but is {result!r}"
    )


# ═══════════════════════════════════════════════════════════════════════════
# Italian regional dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestTuscanItalian:
    """Tuscan Italian — it-IT-x-toscana.

    The most famous phonological feature of Tuscan Italian is the *gorgia
    toscana* (Tuscan throat): intervocalic voiceless stops /p t k/ spirantise
    to [ɸ θ h] respectively.  This is a robust lenition process attested
    throughout Tuscany and entirely absent from standard Italian.

    Tuscan otherwise inherits the grapheme inventory of it-IT.
    """

    LANGUAGE_CODE = "it-IT-x-toscana"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Tuscan Italian once per class and store on cls.spec."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # --- Ancestry ---

    def test_parent_is_it_IT(self) -> None:
        """Parent of Tuscan must be standard Italian (it-IT)."""
        assert self.spec.parent == "it-IT", (
            f"Expected parent 'it-IT', got {self.spec.parent!r}"
        )

    # --- Gorgia toscana: /p/ ---

    def test_gorgia_p_has_phi(self) -> None:
        """Allophone of /p/ includes [ɸ] — bilabial fricative from gorgia toscana."""
        _assert_contains(
            _allophone(self.spec, "p"), "ɸ",
            label="p allophone (gorgia: p→ɸ)",
        )

    def test_gorgia_p_retains_stop(self) -> None:
        """Allophone of /p/ also retains [p] — stop is the word-initial / geminate form."""
        _assert_contains(
            _allophone(self.spec, "p"), "p",
            label="p allophone retains [p]",
        )

    # --- Gorgia toscana: /t/ ---

    def test_gorgia_t_has_theta(self) -> None:
        """Allophone of /t/ includes [θ] — dental fricative from gorgia toscana."""
        _assert_contains(
            _allophone(self.spec, "t"), "θ",
            label="t allophone (gorgia: t→θ)",
        )

    def test_gorgia_t_retains_stop(self) -> None:
        """Allophone of /t/ retains [t] as the base realisation."""
        _assert_contains(
            _allophone(self.spec, "t"), "t",
            label="t allophone retains [t]",
        )

    # --- Gorgia toscana: /k/ ---

    def test_gorgia_k_has_h(self) -> None:
        """Allophone of /k/ includes [h] — glottal fricative from gorgia toscana.

        This is the most radical change: the velar stop /k/ weakens all the way
        to a glottal fricative [h] intervocalically.
        """
        _assert_contains(
            _allophone(self.spec, "k"), "h",
            label="k allophone (gorgia: k→h)",
        )

    def test_gorgia_k_retains_stop(self) -> None:
        """Allophone of /k/ retains [k] as the base/word-initial realisation."""
        _assert_contains(
            _allophone(self.spec, "k"), "k",
            label="k allophone retains [k]",
        )

    # --- Voiceless stops are first (most common) ---

    def test_p_first_allophone_is_stop(self) -> None:
        """The most frequent realisation of /p/ is still [p] (gorgia is intervocalic only)."""
        _assert_first(
            _allophone(self.spec, "p"), "p",
            label="p first allophone",
        )

    def test_t_first_allophone_is_stop(self) -> None:
        """The most frequent realisation of /t/ is still [t]."""
        _assert_first(
            _allophone(self.spec, "t"), "t",
            label="t first allophone",
        )


@pytest.mark.linguistic
class TestRomanItalian:
    """Roman Italian — it-IT-x-roma.

    The Roman dialect (Romanesco) is phonologically close to standard Italian
    and inherits its grapheme inventory from it-IT with minimal overrides.
    Tests here verify the inheritance relationship and basic structural sanity.
    """

    LANGUAGE_CODE = "it-IT-x-roma"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Roman Italian once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_it_IT(self) -> None:
        """Roman Italian parent must be standard Italian (it-IT)."""
        assert self.spec.parent == "it-IT", (
            f"Expected parent 'it-IT', got {self.spec.parent!r}"
        )

    def test_family_is_romance(self) -> None:
        """Language family must be Romance."""
        assert self.spec.family == "Romance"

    def test_vowel_a_present(self) -> None:
        """Grapheme 'a' must resolve to [a] (inherited from it-IT)."""
        vals = _grapheme(self.spec, "a")
        assert vals is not None, "grapheme 'a' absent from Roman Italian"
        _assert_contains(vals, "a", label="Roman a")

    def test_basic_consonant_b_present(self) -> None:
        """Grapheme 'b' must resolve to [b] (no special Roman override)."""
        vals = _grapheme(self.spec, "b")
        assert vals is not None, "grapheme 'b' absent from Roman Italian"
        _assert_contains(vals, "b", label="Roman b")


@pytest.mark.linguistic
class TestCalabrianItalian:
    """Calabrian Italian — it-IT-x-calabria.

    Calabrian has a Greek/Byzantine substrate that introduces:
    - A mid-central vowel [ə] written as <ë> (absent in standard Italian).
    - Lenition of voiced stops with the full betacism pattern (b→β, d→ð).
    - Retroflex stops /ɖ/ and /ɖː/ from the Greek substrate — unique in Italy.
    """

    LANGUAGE_CODE = "it-IT-x-calabria"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Calabrian Italian once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_ancestry(self) -> None:
        """Calabrian parent traces back through Italy Latin (la-x-italia) — historical Romance."""
        assert self.spec.parent == "la-x-italia"

    # --- Schwa grapheme ---

    def test_e_diaeresis_maps_schwa(self) -> None:
        """Calabrian <ë> maps to [ə] — mid-central vowel absent in standard Italian."""
        _assert_contains(
            _grapheme(self.spec, "ë"), "ə",
            label="ë→ə (Calabrian schwa)",
        )

    def test_e_diaeresis_first_is_schwa(self) -> None:
        """The primary realisation of <ë> is [ə]."""
        _assert_first(
            _grapheme(self.spec, "ë"), "ə",
            label="ë first realisation",
        )

    # --- Betacism (voiced stop lenition) ---

    def test_b_allophone_has_beta(self) -> None:
        """Allophone of /b/ includes [β] — spirantisation in intervocalic position."""
        _assert_contains(
            _allophone(self.spec, "b"), "β",
            label="b allophone betacism",
        )

    def test_d_allophone_has_eth(self) -> None:
        """Allophone of /d/ includes [ð] — dental spirantisation."""
        _assert_contains(
            _allophone(self.spec, "d"), "ð",
            label="d allophone betacism",
        )

    def test_g_allophone_has_gamma(self) -> None:
        """Allophone of /ɡ/ includes [ɣ] — velar spirantisation."""
        _assert_contains(
            _allophone(self.spec, "ɡ"), "ɣ",
            label="ɡ allophone betacism",
        )

    # --- Retroflex stops (Greek substrate) ---

    def test_retroflex_stop_present(self) -> None:
        """Allophone inventory contains [ɖ] — retroflex stop from Greek substrate."""
        _assert_contains(
            _allophone(self.spec, "ɖ"), "ɖ",
            label="ɖ retroflex allophone",
        )

    def test_retroflex_geminate_present(self) -> None:
        """Allophone inventory contains [ɖː] — retroflex geminate from Greek substrate."""
        _assert_contains(
            _allophone(self.spec, "ɖː"), "ɖː",
            label="ɖː retroflex geminate allophone",
        )


# ═══════════════════════════════════════════════════════════════════════════
# Romanian
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestRomanian:
    """Romanian — ro-RO.

    Romanian is the most conservative Eastern Romance language, retaining a
    number of archaic Latin features while also innovating:
    - Distinctive vowels: <ă>→[ə], <â>/<î>→[ɨ] (high central unrounded).
    - <ș>→[ʃ], <ț>→[ts] (dedicated sibilant letters).
    - <c> before e/i → [tʃ]; <ch> always → [k].
    - <g> before e/i → [dʒ]; <gh> always → [ɡ].
    - <h> is phonemic (unlike most Romance languages).
    - Rich vowel-glide diphthongs: ia, ie, io, iu, ea, oa.
    """

    LANGUAGE_CODE = "ro-RO"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Romanian once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # --- Script and family ---

    def test_family(self) -> None:
        """Romanian must be classified as Romance."""
        assert self.spec.family == "Romance"

    def test_script(self) -> None:
        """Romanian uses the Latin script."""
        assert self.spec.script == "Latin"

    # --- Core vowels ---

    def test_a_maps_a(self) -> None:
        """<a> maps to [a]."""
        _assert_first(_grapheme(self.spec, "a"), "a", label="ro a")

    def test_a_breve_maps_schwa(self) -> None:
        """<ă> maps to [ə] — Romanian mid-central vowel (schwa)."""
        _assert_first(_grapheme(self.spec, "ă"), "ə", label="ă→ə")

    def test_a_circumflex_maps_high_central(self) -> None:
        """<â> maps to [ɨ] — high central unrounded vowel, unique in Romance."""
        _assert_first(_grapheme(self.spec, "â"), "ɨ", label="â→ɨ")

    def test_i_with_circumflex_maps_high_central(self) -> None:
        """<î> is an alternative spelling of [ɨ], same as <â>."""
        _assert_first(_grapheme(self.spec, "î"), "ɨ", label="î→ɨ")

    def test_e_maps_mid(self) -> None:
        """<e> maps to [e] (or [ɛ] in open syllable)."""
        vals = _grapheme(self.spec, "e")
        assert vals is not None, "e absent from Romanian"
        _assert_contains(vals, "e", label="ro e")

    def test_i_maps_i(self) -> None:
        """<i> maps to [i]."""
        _assert_first(_grapheme(self.spec, "i"), "i", label="ro i")

    def test_o_maps_o(self) -> None:
        """<o> maps to [o]."""
        _assert_first(_grapheme(self.spec, "o"), "o", label="ro o")

    def test_u_maps_u(self) -> None:
        """<u> maps to [u]."""
        _assert_first(_grapheme(self.spec, "u"), "u", label="ro u")

    # --- Sibilant letters ---

    def test_s_cedilla_maps_sh(self) -> None:
        """<ș> (s-comma-below) maps to [ʃ] — Romanian-specific sibilant letter."""
        _assert_first(_grapheme(self.spec, "ș"), "ʃ", label="ș→ʃ")

    def test_t_cedilla_maps_ts(self) -> None:
        """<ț> (t-comma-below) maps to [ts] — Romanian affricate letter."""
        _assert_first(_grapheme(self.spec, "ț"), "ts", label="ț→ts")

    # --- Velar/affricate alternations ---

    def test_c_has_velar_and_affricate(self) -> None:
        """<c> maps to [k] (default) and [tʃ] (before e/i) — context-sensitive."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "tʃ", label="c→[k,tʃ]")

    def test_ch_maps_only_k(self) -> None:
        """<ch> digraph always maps to [k] — prevents affrication before e/i."""
        _assert_first(_grapheme(self.spec, "ch"), "k", label="ch→k")

    def test_g_has_stop_and_affricate(self) -> None:
        """<g> maps to [ɡ] and [dʒ] — alternation before e/i."""
        vals = _grapheme(self.spec, "g")
        _assert_contains(vals, "ɡ", "dʒ", label="g→[ɡ,dʒ]")

    def test_gh_maps_only_g(self) -> None:
        """<gh> digraph always maps to [ɡ] — prevents affrication before e/i."""
        _assert_first(_grapheme(self.spec, "gh"), "ɡ", label="gh→ɡ")

    # --- Other consonants ---

    def test_j_maps_zh(self) -> None:
        """<j> maps to [ʒ] — voiced palatal fricative (French/Slavic loan influence)."""
        _assert_first(_grapheme(self.spec, "j"), "ʒ", label="j→ʒ")

    def test_h_is_phonemic(self) -> None:
        """<h> maps to [h] — phonemic in Romanian unlike most Western Romance."""
        _assert_first(_grapheme(self.spec, "h"), "h", label="h phonemic")

    # --- Romanian diphthongs ---

    def test_diphthong_ia(self) -> None:
        """Digraph <ia> maps to [ja] — falling diphthong."""
        _assert_contains(_grapheme(self.spec, "ia"), "ja", label="ia→ja")

    def test_diphthong_ie(self) -> None:
        """Digraph <ie> maps to [je]."""
        _assert_contains(_grapheme(self.spec, "ie"), "je", label="ie→je")

    def test_diphthong_ea(self) -> None:
        """Digraph <ea> maps to [e̯a] — non-syllabic e before a."""
        _assert_contains(_grapheme(self.spec, "ea"), "e̯a", label="ea→e̯a")

    def test_diphthong_oa(self) -> None:
        """Digraph <oa> maps to [o̯a] — non-syllabic o before a."""
        _assert_contains(_grapheme(self.spec, "oa"), "o̯a", label="oa→o̯a")


# ═══════════════════════════════════════════════════════════════════════════
# Sardinian
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestSardinian:
    """Standard Sardinian — sc.

    Sardinian is the most conservative Romance language: it preserves Latin
    /k/ before e/i (no affrication), maintains the 5-vowel system without
    schwa, and retains other archaic features.  Key traits:
    - <c> always [k] — no palatalisation (unlike Italian, Spanish, French).
    - <ch> → [k] (digraph confirming velar).
    - <b> → [b,β] — betacism allophony present.
    - <z> → [ts,dz] — affricate realisation.
    - <d> → [d,ð] — lenition in intervocalic position.
    """

    LANGUAGE_CODE = "sc"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Standard Sardinian once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # --- Family ---

    def test_family_is_romance(self) -> None:
        """Sardinian must be classified as Romance."""
        assert self.spec.family == "Romance"

    # --- Conservative 5-vowel system ---

    def test_a_maps_a(self) -> None:
        """<a> → [a]."""
        _assert_first(_grapheme(self.spec, "a"), "a", label="sc a")

    def test_e_maps_e(self) -> None:
        """<e> → [e] — Sardinian does NOT have [ɛ] as a distinct phoneme."""
        _assert_first(_grapheme(self.spec, "e"), "e", label="sc e")

    def test_i_maps_i(self) -> None:
        """<i> → [i]."""
        _assert_first(_grapheme(self.spec, "i"), "i", label="sc i")

    def test_o_maps_o(self) -> None:
        """<o> → [o]."""
        _assert_first(_grapheme(self.spec, "o"), "o", label="sc o")

    def test_u_maps_u(self) -> None:
        """<u> → [u]."""
        _assert_first(_grapheme(self.spec, "u"), "u", label="sc u")

    # --- Conservative velar /k/ before front vowels ---

    def test_c_always_k(self) -> None:
        """<c> maps to [k] — no palatal affrication before e/i (key archaism)."""
        _assert_first(_grapheme(self.spec, "c"), "k", label="sc c→k")

    def test_ch_maps_k(self) -> None:
        """<ch> digraph → [k]."""
        _assert_first(_grapheme(self.spec, "ch"), "k", label="sc ch→k")

    # --- Voiced stop betacism ---

    def test_b_has_beta_allophone(self) -> None:
        """<b> has allophone [β] — betacism present in Sardinian."""
        _assert_contains(
            _allophone(self.spec, "b"), "β",
            label="sc b→β allophone",
        )

    def test_d_has_eth_allophone(self) -> None:
        """Allophone of /d/ includes [ð] — lenition in intervocalic context."""
        _assert_contains(
            _allophone(self.spec, "d"), "ð",
            label="sc d→ð allophone",
        )

    # --- Affricate z ---

    def test_z_maps_ts(self) -> None:
        """<z> → [ts] (primary realisation — Sardinian affricate)."""
        vals = _grapheme(self.spec, "z")
        _assert_contains(vals, "ts", label="sc z→ts")

    def test_z_has_voiced_affricate(self) -> None:
        """<z> also includes [dz] — voiced variant in some phonological contexts."""
        _assert_contains(_grapheme(self.spec, "z"), "dz", label="sc z→dz")

    # --- Velar g ---

    def test_gh_maps_g(self) -> None:
        """<gh> digraph → [ɡ]."""
        _assert_first(_grapheme(self.spec, "gh"), "ɡ", label="sc gh→ɡ")


@pytest.mark.linguistic
class TestLogudoreseSardinian:
    """Logudorese Sardinian — sc-x-logudorese.

    Logudorese is a northern Sardinian dialect with a partial gorgia-like
    feature: intervocalic /t/ weakens to [θ].  The dialect otherwise inherits
    the conservative Sardinian inventory from the parent code <sc>.
    """

    LANGUAGE_CODE = "sc-x-logudorese"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Logudorese Sardinian once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_sc(self) -> None:
        """Logudorese parent must be Standard Sardinian (sc)."""
        assert self.spec.parent == "sc"

    def test_t_allophone_has_theta(self) -> None:
        """Allophone of /t/ includes [θ] — partial gorgia-like lenition in Logudorese."""
        _assert_contains(
            _allophone(self.spec, "t"), "θ",
            label="Logudorese t→θ",
        )

    def test_t_allophone_retains_stop(self) -> None:
        """Allophone of /t/ retains [t] as primary (word-initial / geminate)."""
        _assert_contains(
            _allophone(self.spec, "t"), "t",
            label="Logudorese t retains [t]",
        )

    def test_t_first_allophone_is_stop(self) -> None:
        """The most frequent realisation of /t/ is still [t]."""
        _assert_first(
            _allophone(self.spec, "t"), "t",
            label="Logudorese t first allophone",
        )


@pytest.mark.linguistic
class TestCampidaneseSardinian:
    """Campidanese Sardinian — sc-x-campidanese.

    Campidanese is a southern Sardinian dialect with stronger lenition than
    Logudorese: all three voiceless stops /p t k/ have fricative allophones
    (p→β, t→ð, k→ɣ) in weak positions, creating a more extreme lenition system.
    """

    LANGUAGE_CODE = "sc-x-campidanese"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Campidanese Sardinian once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_sc(self) -> None:
        """Campidanese parent must be Standard Sardinian (sc)."""
        assert self.spec.parent == "sc"

    def test_p_allophone_has_beta(self) -> None:
        """Allophone of /p/ includes [β] — labial fricative from Campidanese lenition."""
        _assert_contains(
            _allophone(self.spec, "p"), "β",
            label="Campidanese p→β",
        )

    def test_t_allophone_has_eth(self) -> None:
        """Allophone of /t/ includes [ð] — dental fricative from Campidanese lenition."""
        _assert_contains(
            _allophone(self.spec, "t"), "ð",
            label="Campidanese t→ð",
        )

    def test_k_allophone_has_gamma(self) -> None:
        """Allophone of /k/ includes [ɣ] — velar fricative from Campidanese lenition."""
        _assert_contains(
            _allophone(self.spec, "k"), "ɣ",
            label="Campidanese k→ɣ",
        )

    def test_p_first_allophone_is_stop(self) -> None:
        """The most frequent realisation of /p/ is still [p]."""
        _assert_first(
            _allophone(self.spec, "p"), "p",
            label="Campidanese p first allophone",
        )

    def test_t_first_allophone_is_stop(self) -> None:
        """The most frequent realisation of /t/ is still [t]."""
        _assert_first(
            _allophone(self.spec, "t"), "t",
            label="Campidanese t first allophone",
        )

    def test_k_first_allophone_is_stop(self) -> None:
        """The most frequent realisation of /k/ is still [k]."""
        _assert_first(
            _allophone(self.spec, "k"), "k",
            label="Campidanese k first allophone",
        )


# ═══════════════════════════════════════════════════════════════════════════
# Occitan Aranese
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestAranese:
    """Aranese Occitan — oc-x-aranes.

    Aranese is the variety of Occitan spoken in the Val d'Aran, Catalonia.
    Key distinguishing features:
    - <u> → [y] — Gallo-Romance front rounded vowel (like French, unlike Spanish).
    - <a> → [a, ɔ] — contextual back-raising.
    - <o> → [u, ɔ] — Occitan o-raising.
    - <h> is phonemic in Aranese (retained from Latin, lost in Castilian/Catalan).
    - <f> → [f, h] — f-aspiration before some vowels.
    - Betacism: b/d/g have fricative allophones.
    - Word-initial <r> → [r] (trill).
    """

    LANGUAGE_CODE = "oc-x-aranes"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Aranese Occitan once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_oc(self) -> None:
        """Aranese parent must be Occitan (oc)."""
        assert self.spec.parent == "oc"

    # --- Front rounded vowel ---

    def test_u_maps_y(self) -> None:
        """<u> → [y] — Gallo-Romance front rounded vowel; unique among Iberian varieties."""
        _assert_first(_grapheme(self.spec, "u"), "y", label="Aranese u→y")

    # --- Vowel mappings ---

    def test_a_has_back_allophone(self) -> None:
        """<a> → [a, ɔ] — a may raise to [ɔ] in certain positions."""
        _assert_contains(_grapheme(self.spec, "a"), "a", "ɔ", label="Aranese a")

    def test_o_has_raised_allophone(self) -> None:
        """<o> → [u, ɔ] — Occitan o-raising; [u] is the primary realisation."""
        vals = _grapheme(self.spec, "o")
        _assert_contains(vals, "u", "ɔ", label="Aranese o")

    def test_i_maps_i(self) -> None:
        """<i> → [i]."""
        _assert_first(_grapheme(self.spec, "i"), "i", label="Aranese i")

    # --- Phonemic h ---

    def test_h_is_phonemic(self) -> None:
        """<h> → [h] — phonemic in Aranese; retained from Latin aspirates."""
        _assert_first(_grapheme(self.spec, "h"), "h", label="Aranese h phonemic")

    # --- f-aspiration ---

    def test_f_has_h_allophone(self) -> None:
        """<f> allophone includes [h] — f-aspiration before some vowels."""
        _assert_contains(_allophone(self.spec, "f"), "h", label="Aranese f→h allophone")

    def test_f_has_f_allophone(self) -> None:
        """<f> retains [f] as primary realisation."""
        _assert_contains(_allophone(self.spec, "f"), "f", label="Aranese f retains [f]")

    # --- Betacism: voiced stop lenition ---

    def test_b_allophone_has_beta(self) -> None:
        """Allophone of /b/ includes [β] — Gallo-Romance betacism."""
        _assert_contains(_allophone(self.spec, "b"), "β", label="Aranese b→β")

    def test_d_allophone_has_eth(self) -> None:
        """Allophone of /d/ includes [ð] — lenition in intervocalic position."""
        _assert_contains(_allophone(self.spec, "d"), "ð", label="Aranese d→ð")

    def test_g_allophone_has_gamma(self) -> None:
        """Allophone of /ɡ/ includes [ɣ] — velar spirantisation."""
        _assert_contains(_allophone(self.spec, "ɡ"), "ɣ", label="Aranese ɡ→ɣ")

    # --- Word-initial r is trill ---

    def test_r_word_initial_is_trill(self) -> None:
        """Word-initial <r> → [r] (trill); contrast with intervocalic flap [ɾ]."""
        positional = _positional(self.spec, "r", GraphemePosition.WORD_INITIAL)
        assert positional is not None, "r/WORD_INITIAL positional missing in Aranese"
        _assert_contains(positional, "r", label="Aranese r word-initial trill")


# ═══════════════════════════════════════════════════════════════════════════
# Spanish Caribbean / Central
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestCubanSpanish:
    """Cuban Spanish — es-CU.

    Cuban is a Caribbean variety with the following hallmarks:
    - Seseo: <c>/<z> → [s] (no /θ/ phoneme).
    - Yeísmo: <ll> → [ʝ] (no /ʎ/ phoneme).
    - Extreme coda-/s/ aspiration and deletion: [s]→[h]→∅.
    - Deaffrication: <ch> → [ʃ] alongside [tʃ].
    - <x> → [h] (velar fricative weakens to glottal).
    - Word-final /n/ velarises to [ŋ].
    - /d/ intervocalic weakening and word-final deletion.
    """

    LANGUAGE_CODE = "es-CU"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Cuban Spanish once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # --- Seseo ---

    def test_c_seseo_no_theta_primary(self) -> None:
        """<c> maps to [k, s] — seseo variety; [s] not [θ]."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "s", label="Cuban c seseo")

    def test_z_maps_s_only(self) -> None:
        """<z> → [s] — seseo; [θ] absent or non-primary."""
        _assert_first(_grapheme(self.spec, "z"), "s", label="Cuban z seseo")

    # --- Yeísmo ---

    def test_ll_yeismo(self) -> None:
        """<ll> → [ʝ] — yeísmo; no /ʎ/ phoneme in Cuban Spanish."""
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="Cuban ll yeísmo")

    # --- Coda-s aspiration/deletion ---

    def test_s_allophone_has_aspiration(self) -> None:
        """Allophone of /s/ includes [h] — coda aspiration."""
        _assert_contains(_allophone(self.spec, "s"), "h", label="Cuban s→h")

    def test_s_allophone_has_deletion(self) -> None:
        """Allophone of /s/ includes [∅] — extreme coda deletion."""
        _assert_contains(_allophone(self.spec, "s"), "∅", label="Cuban s→∅")

    # --- Deaffrication ---

    def test_tsh_has_sh_allophone(self) -> None:
        """Allophone of /tʃ/ includes [ʃ] — deaffrication in Cuban Spanish."""
        _assert_contains(_allophone(self.spec, "tʃ"), "ʃ", label="Cuban tʃ→ʃ")

    # --- x → h ---

    def test_x_maps_h(self) -> None:
        """<x> → [h] (velar fricative weakens to glottal in Cuban Spanish)."""
        _assert_contains(_allophone(self.spec, "x"), "h", label="Cuban x→h")

    # --- /d/ weakening ---

    def test_d_word_final_deletion(self) -> None:
        """Word-final /d/ → ∅ in Cuban Spanish (extreme lenition)."""
        wf = _positional(self.spec, "d", GraphemePosition.WORD_FINAL)
        assert wf is not None, "d/WORD_FINAL positional missing in Cuban Spanish"
        assert "∅" in wf, "Cuban d word-final should include ∅"

    # --- Word-final n velarisation ---

    def test_n_word_final_velar(self) -> None:
        """Word-final /n/ → [ŋ] — velarisation in Cuban Spanish."""
        wf = _positional(self.spec, "n", GraphemePosition.WORD_FINAL)
        assert wf is not None, "n/WORD_FINAL positional missing in Cuban Spanish"
        _assert_contains(wf, "ŋ", label="Cuban n word-final→ŋ")


@pytest.mark.iberian
class TestPuertoRicanSpanish:
    """Puerto Rican Spanish — es-PR.

    Puerto Rican shares Caribbean features with Cuban but adds l-weakening:
    - Seseo: <c>/<z> → [s].
    - Yeísmo: <ll> → [ʝ].
    - Coda-/s/ aspiration and deletion.
    - <x> → [h].
    - l-weakening: coda /l/ → [ɾ] or [j] (unique Caribbean feature).
    """

    LANGUAGE_CODE = "es-PR"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Puerto Rican Spanish once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_seseo_c(self) -> None:
        """<c> → [k, s] — seseo."""
        _assert_contains(_grapheme(self.spec, "c"), "k", "s", label="PR c seseo")

    def test_seseo_z(self) -> None:
        """<z> → [s] as first realisation — seseo."""
        _assert_first(_grapheme(self.spec, "z"), "s", label="PR z seseo")

    def test_yeismo(self) -> None:
        """<ll> → [ʝ] — yeísmo."""
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="PR ll yeísmo")

    def test_s_aspiration(self) -> None:
        """Allophone of /s/ includes [h] — coda aspiration."""
        _assert_contains(_allophone(self.spec, "s"), "h", label="PR s→h")

    def test_s_deletion(self) -> None:
        """Allophone of /s/ includes [∅] — coda deletion."""
        _assert_contains(_allophone(self.spec, "s"), "∅", label="PR s→∅")

    def test_x_maps_h(self) -> None:
        """<x> → [h]."""
        _assert_contains(_allophone(self.spec, "x"), "h", label="PR x→h")

    def test_l_weakening_flap(self) -> None:
        """Allophone of /l/ includes [ɾ] — l-weakening in coda position."""
        _assert_contains(_allophone(self.spec, "l"), "ɾ", label="PR l→ɾ weakening")

    def test_l_weakening_glide(self) -> None:
        """Allophone of /l/ includes [j] — further weakening to glide."""
        _assert_contains(_allophone(self.spec, "l"), "j", label="PR l→j weakening")


@pytest.mark.iberian
class TestDominicanSpanish:
    """Dominican Spanish — es-DO.

    Dominican Spanish shares the Caribbean profile with Puerto Rican:
    - Seseo: <c>/<z> → [s].
    - Yeísmo: <ll> → [ʝ].
    - l-weakening: coda /l/ → [ɾ, j].
    - Extreme coda-/s/ aspiration and deletion.
    """

    LANGUAGE_CODE = "es-DO"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Dominican Spanish once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_seseo_c(self) -> None:
        """<c> → [k, s] — seseo."""
        _assert_contains(_grapheme(self.spec, "c"), "k", "s", label="DO c seseo")

    def test_seseo_z(self) -> None:
        """<z> → [s] — seseo."""
        _assert_first(_grapheme(self.spec, "z"), "s", label="DO z seseo")

    def test_yeismo(self) -> None:
        """<ll> → [ʝ] — yeísmo."""
        _assert_first(_grapheme(self.spec, "ll"), "ʝ", label="DO ll yeísmo")

    def test_l_weakening_flap(self) -> None:
        """Allophone of /l/ includes [ɾ] — same l-weakening as Puerto Rican."""
        _assert_contains(_allophone(self.spec, "l"), "ɾ", label="DO l→ɾ")

    def test_l_weakening_glide(self) -> None:
        """Allophone of /l/ includes [j] — glide weakening."""
        _assert_contains(_allophone(self.spec, "l"), "j", label="DO l→j")

    def test_s_aspiration(self) -> None:
        """Allophone of /s/ includes [h] — coda aspiration."""
        _assert_contains(_allophone(self.spec, "s"), "h", label="DO s→h")


# ═══════════════════════════════════════════════════════════════════════════
# Medieval and regional Spanish
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestMedievalSpanish:
    """Medieval Spanish — es-ES-x-medieval.

    Medieval Castilian is the ancestor of modern Spanish and has a richer
    sibilant system: <c> may represent the affricate [ts], <z> represents [dz]
    or voiced [z] (not yet merged), and betacism (b/d/g lenition) is still
    active with positional rules.  All modern Spanish varieties descend from
    this stage.
    """

    LANGUAGE_CODE = "es-ES-x-medieval"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Medieval Spanish once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # --- Pre-merger sibilant system ---

    def test_c_has_theta(self) -> None:
        """<c> maps to [k, θ] — Medieval Spanish preserves distinción (modern inherited form)."""
        _assert_contains(_grapheme(self.spec, "c"), "k", "θ", label="Medieval c→θ")

    def test_z_has_theta(self) -> None:
        """<z> maps to [θ] in es-ES-x-medieval — distinción variety (apical sibilant ancestor)."""
        vals = _grapheme(self.spec, "z")
        assert vals is not None, "z absent from Medieval Spanish"
        assert "θ" in vals, f"Medieval z should include θ, got {vals}"

    # --- Betacism: positional lenition ---

    def test_b_allophone_has_beta(self) -> None:
        """Allophone of /b/ includes [β] — betacism active in Medieval Spanish."""
        _assert_contains(_allophone(self.spec, "b"), "β", label="Medieval b→β")

    def test_d_allophone_has_eth(self) -> None:
        """Allophone of /d/ includes [ð] — dental lenition in intervocalic position."""
        _assert_contains(_allophone(self.spec, "d"), "ð", label="Medieval d→ð")

    def test_g_allophone_has_gamma(self) -> None:
        """Allophone of /ɡ/ includes [ɣ] — velar spirantisation."""
        _assert_contains(_allophone(self.spec, "ɡ"), "ɣ", label="Medieval ɡ→ɣ")

    # --- Positional rules exist ---

    def test_b_has_positional_rules(self) -> None:
        """Medieval Spanish must have positional rules for /b/ lenition."""
        pos_map = self.spec.positional_graphemes.get("b")
        assert pos_map is not None, "b positional rules missing from Medieval Spanish"

    def test_d_has_positional_rules(self) -> None:
        """Medieval Spanish must have positional rules for /d/ lenition."""
        pos_map = self.spec.positional_graphemes.get("d")
        assert pos_map is not None, "d positional rules missing from Medieval Spanish"

    def test_g_has_positional_rules(self) -> None:
        """Medieval Spanish must have positional rules for /g/ lenition."""
        pos_map = self.spec.positional_graphemes.get("g")
        assert pos_map is not None, "g positional rules missing from Medieval Spanish"


@pytest.mark.iberian
class TestCantabrianSpanish:
    """Cantabrian Spanish — es-ES-x-cantabria.

    Cantabrian Spanish is a conservative Northern Castilian variety
    distinguished primarily by its apical /s/ ([s̺]), linking it to the Asturian
    family.  It otherwise inherits standard Castilian features from es-ES.
    """

    LANGUAGE_CODE = "es-ES-x-cantabria"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Cantabrian Spanish once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_es_ES(self) -> None:
        """Cantabrian parent must be standard Castilian (es-ES)."""
        assert self.spec.parent == "es-ES"

    def test_s_is_apical(self) -> None:
        """Allophone of /s/ is [s̺] — apical sibilant linking Cantabrian to Asturian."""
        _assert_first(
            _allophone(self.spec, "s"), "s̺",
            label="Cantabrian apical s",
        )


# ═══════════════════════════════════════════════════════════════════════════
# Brazilian Portuguese dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestCaipiraBrazilian:
    """Caipira Brazilian Portuguese — pt-BR-x-caipira.

    Caipira (rural São Paulo) is a traditional Brazilian dialect.  It shares
    palatalisation of /t d/ before /i/ with other Brazilian varieties but
    preserves certain conservative features.  The rhotic tends to be [ɾ] rather
    than the Rio [h].
    """

    LANGUAGE_CODE = "pt-BR-x-caipira"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Caipira Brazilian Portuguese once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_pt_BR(self) -> None:
        """Caipira parent must be Brazilian Portuguese (pt-BR)."""
        assert self.spec.parent == "pt-BR"

    # --- Palatalisation of /t d/ (shared with Rio) ---

    def test_t_has_palatal_allophone(self) -> None:
        """Allophone of /t/ includes [tʃ] — palatalisation before /i/ (as in Rio)."""
        _assert_contains(
            _allophone(self.spec, "t"), "tʃ",
            label="Caipira t→tʃ palatalisation",
        )

    def test_d_has_palatal_allophone(self) -> None:
        """Allophone of /d/ includes [dʒ] — palatalisation before /i/."""
        _assert_contains(
            _allophone(self.spec, "d"), "dʒ",
            label="Caipira d→dʒ palatalisation",
        )

    def test_t_first_allophone_is_stop(self) -> None:
        """The primary realisation of /t/ is still [t]."""
        _assert_first(_allophone(self.spec, "t"), "t", label="Caipira t first")

    def test_d_first_allophone_is_stop(self) -> None:
        """The primary realisation of /d/ is still [d]."""
        _assert_first(_allophone(self.spec, "d"), "d", label="Caipira d first")

    # --- Vowel inventory ---

    def test_a_present(self) -> None:
        """<a> → [a, ɐ]."""
        _assert_contains(_grapheme(self.spec, "a"), "a", label="Caipira a")

    def test_o_has_back_raised(self) -> None:
        """<o> → [o, ɔ, u] — back vowel variation in Caipira."""
        vals = _grapheme(self.spec, "o")
        assert vals is not None, "o absent from Caipira"
        _assert_contains(vals, "o", label="Caipira o")

    # --- Voiced stop betacism ---

    def test_b_has_beta(self) -> None:
        """Allophone of /b/ includes [β]."""
        _assert_contains(_allophone(self.spec, "b"), "β", label="Caipira b→β")

    def test_g_has_gamma(self) -> None:
        """Allophone of /ɡ/ includes [ɣ]."""
        _assert_contains(_allophone(self.spec, "ɡ"), "ɣ", label="Caipira ɡ→ɣ")


@pytest.mark.iberian
class TestBahianBrazilian:
    """Bahian Brazilian Portuguese — pt-BR-x-bahia.

    Bahian is the major Northeastern Brazilian dialect.  Its key distinguishing
    feature from Rio and São Paulo is the ABSENCE of /t d/ palatalisation
    before /i/ — a conservative feature.  Voiced stop betacism is present.
    """

    LANGUAGE_CODE = "pt-BR-x-bahia"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Bahian Brazilian Portuguese once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_pt_BR(self) -> None:
        """Bahian parent must be Brazilian Portuguese (pt-BR)."""
        assert self.spec.parent == "pt-BR"

    # --- NO palatalisation of /t d/ (distinguishing feature!) ---

    def test_t_no_palatal_allophone(self) -> None:
        """Bahian /t/ does NOT have [tʃ] allophone — conservative, no palatalisation."""
        vals = _allophone(self.spec, "t")
        if vals is not None:
            assert "tʃ" not in vals, (
                "Bahian t should NOT have palatal allophone [tʃ]; "
                f"got {vals!r}"
            )

    def test_d_no_palatal_allophone(self) -> None:
        """Bahian /d/ does NOT have [dʒ] allophone — conservative, no palatalisation."""
        vals = _allophone(self.spec, "d")
        if vals is not None:
            assert "dʒ" not in vals, (
                "Bahian d should NOT have palatal allophone [dʒ]; "
                f"got {vals!r}"
            )

    def test_t_first_allophone_is_plain_stop(self) -> None:
        """The primary realisation of /t/ is [t] — plain dental stop."""
        _assert_first(_allophone(self.spec, "t"), "t", label="Bahian t first")

    def test_d_first_allophone_is_plain_stop(self) -> None:
        """The primary realisation of /d/ is [d] — plain dental stop."""
        _assert_first(_allophone(self.spec, "d"), "d", label="Bahian d first")

    # --- Voiced stop betacism present ---

    def test_b_has_beta(self) -> None:
        """Allophone of /b/ includes [β] — betacism present in Bahian."""
        _assert_contains(_allophone(self.spec, "b"), "β", label="Bahian b→β")


# ═══════════════════════════════════════════════════════════════════════════
# European Portuguese dialects
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.iberian
class TestAzoreanPortuguese:
    """Azorean Portuguese — pt-PT-x-acores.

    The Azorean dialect preserves some archaic features and has distinctive
    nasal vowel realisations.  Key features:
    - <ão> → [õw̃] — nasal diphthong.
    - Schwa [ɨ] may be realised as [e] in some positions.
    - Nasal /ɐ̃/ may be realised as [õ].
    """

    LANGUAGE_CODE = "pt-PT-x-acores"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Azorean Portuguese once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_pt_PT(self) -> None:
        """Azorean parent must be European Portuguese (pt-PT)."""
        assert self.spec.parent == "pt-PT"

    def test_ao_nasal_diphthong(self) -> None:
        """<ão> → [õw̃] — nasal diphthong realisation in Azorean."""
        _assert_contains(
            _grapheme(self.spec, "ão"), "õw̃",
            label="Azorean ão→õw̃",
        )

    def test_schwa_has_e_allophone(self) -> None:
        """Azorean ə allophone includes [e] — less reduced than Lisbon ɨ."""
        _assert_contains(
            _allophone(self.spec, "ə"), "e",
            label="Azorean ɨ→e allophone",
        )

    def test_schwa_retains_high_central(self) -> None:
        """Allophone of [ɨ] retains [ɨ] as primary."""
        _assert_first(
            _allophone(self.spec, "ɨ"), "ɨ",
            label="Azorean ɨ first allophone",
        )

    def test_nasal_a_has_o_allophone(self) -> None:
        """Allophone of /ɐ̃/ includes [õ] — nasal vowel shift in Azorean."""
        _assert_contains(
            _allophone(self.spec, "ɐ̃"), "õ",
            label="Azorean ɐ̃→õ allophone",
        )


@pytest.mark.iberian
class TestAlentejoPortuguese:
    """Alentejo Portuguese — pt-PT-x-alentejo.

    Alentejo is a southern Portuguese dialect with distinctive vowel features:
    - /ɛ/ may diphthongise to [ɛ͡ɐ] — unique to Alentejo.
    - /ʁ/ realised as uvular [ʁ].
    """

    LANGUAGE_CODE = "pt-PT-x-alentejo"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Alentejo Portuguese once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_pt_PT(self) -> None:
        """Alentejo parent must be European Portuguese (pt-PT)."""
        assert self.spec.parent == "pt-PT"

    def test_open_e_has_diphthong_allophone(self) -> None:
        """Allophone of /ɛ/ includes [ɛ͡ɐ] — diphthongisation unique to Alentejo."""
        _assert_contains(
            _allophone(self.spec, "ɛ"), "ɛ͡ɐ",
            label="Alentejo ɛ→ɛ͡ɐ diphthongisation",
        )

    def test_open_e_retains_primary(self) -> None:
        """The primary realisation of /ɛ/ is still [ɛ]."""
        _assert_first(
            _allophone(self.spec, "ɛ"), "ɛ",
            label="Alentejo ɛ first allophone",
        )

    def test_r_uvular(self) -> None:
        """Allophone of /ʁ/ is uvular [ʁ]."""
        _assert_contains(
            _allophone(self.spec, "ʁ"), "ʁ",
            label="Alentejo ʁ uvular",
        )

    def test_family_is_romance(self) -> None:
        """Alentejo must be Romance."""
        assert self.spec.family == "Romance"


@pytest.mark.iberian
class TestMinhoPortuguese:
    """Minho (Northern) Portuguese — pt-PT-x-minho.

    Minho is the northernmost Portuguese dialect, sharing features with Galician.
    Key distinctive features:
    - /t/ is aspirated: [tʰ].
    - Sibilants are retroflex: [ʂ] and [ʐ] alongside [ʃ] and [ʒ].
    - /ʁ/ → [ʁ, χ] — uvular with devoiced variant.
    - /ɾ/ → [ɾ, ɽ] — retroflex flap allophone.
    - /d/ may delete in coda position: [ð, ∅].
    """

    LANGUAGE_CODE = "pt-PT-x-minho"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request: pytest.FixtureRequest) -> None:
        """Load Minho Portuguese once per class."""
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_parent_is_pt_PT(self) -> None:
        """Minho parent must be European Portuguese (pt-PT)."""
        assert self.spec.parent == "pt-PT"

    # --- Aspirated t ---

    def test_t_aspirated(self) -> None:
        """Allophone of /t/ includes [tʰ] — aspiration in Minho Portuguese."""
        _assert_contains(
            _allophone(self.spec, "t"), "tʰ",
            label="Minho t aspiration",
        )

    # --- Retroflex sibilants ---

    def test_sh_has_retroflex_allophone(self) -> None:
        """Allophone of /ʃ/ includes [ʂ] — retroflex sibilant in Minho (Porto feature)."""
        _assert_contains(
            _allophone(self.spec, "ʃ"), "ʂ",
            label="Minho ʃ→ʂ retroflex",
        )

    def test_zh_has_retroflex_allophone(self) -> None:
        """Allophone of /ʒ/ includes [ʐ] — voiced retroflex sibilant."""
        _assert_contains(
            _allophone(self.spec, "ʒ"), "ʐ",
            label="Minho ʒ→ʐ retroflex",
        )

    # --- Uvular r variants ---

    def test_r_uvular_with_voiceless_variant(self) -> None:
        """Allophone of /ʁ/ includes devoiced [χ] — Minho northern feature."""
        _assert_contains(
            _allophone(self.spec, "ʁ"), "χ",
            label="Minho ʁ→χ devoiced variant",
        )

    def test_r_uvular_retains_voiced(self) -> None:
        """Allophone of /ʁ/ retains [ʁ] as primary."""
        _assert_first(
            _allophone(self.spec, "ʁ"), "ʁ",
            label="Minho ʁ first allophone",
        )

    # --- Retroflex flap ---

    def test_flap_has_retroflex_allophone(self) -> None:
        """Allophone of /ɾ/ includes [ɽ] — retroflex flap in Minho Portuguese."""
        _assert_contains(
            _allophone(self.spec, "ɾ"), "ɽ",
            label="Minho ɾ→ɽ retroflex flap",
        )

    # --- d-deletion ---

    def test_d_coda_deletion(self) -> None:
        """Allophone of /d/ includes [∅] — coda deletion in Minho Portuguese."""
        _assert_contains(
            _allophone(self.spec, "d"), "∅",
            label="Minho d→∅ coda deletion",
        )
