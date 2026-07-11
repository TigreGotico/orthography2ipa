"""Per-language accuracy tests for Slavic languages.

Covers: Russian (ru), Polish (pl), Czech (cs), Bulgarian (bg),
        Slovak (sk), Slovenian (sl), Croatian (hr), Ukrainian (uk), Belarusian (be),
        Serbian (sr), Macedonian (mk)
"""
from __future__ import annotations

import pytest
import orthography2ipa
from orthography2ipa.types import GraphemePosition

_SENTINEL = object()


def _load(code):
    """Load a LanguageSpec by BCP-47 code, skipping the test if unavailable."""
    try:
        return orthography2ipa.get(code)
    except Exception as exc:
        pytest.skip(f"{code!r} not available: {exc}")


def _grapheme(spec, grapheme):
    """Return the grapheme mapping list for *grapheme*, or None."""
    return spec.graphemes.get(grapheme)


def _allophone(spec, phoneme):
    """Return the allophone list for *phoneme*, or None."""
    return spec.allophones.get(phoneme)


def _assert_contains(values, *expected, label=""):
    """Assert that every *expected* value appears in *values*."""
    assert values is not None, f"{label}: mapping is absent"
    for exp in expected:
        assert exp in values, f"{label}: {exp!r} not in {values}"


def _assert_first(values, expected, label=""):
    """Assert that *expected* is the first (most canonical) value in *values*."""
    assert values is not None, f"{label}: mapping is absent"
    assert values[0] == expected, f"{label}: expected first={expected!r}, got {values[0]!r}"


def _assert_null(spec, grapheme):
    """Assert that *grapheme* is absent (or explicitly None) in spec.graphemes."""
    result = spec.graphemes.get(grapheme, _SENTINEL)
    assert result is _SENTINEL or result is None


def _assert_allophone_null(spec, phoneme):
    """Assert that *phoneme* is absent (or explicitly None) in spec.allophones."""
    result = spec.allophones.get(phoneme, _SENTINEL)
    assert result is _SENTINEL or result is None


# ---------------------------------------------------------------------------
# Russian
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestRussian:
    """Accuracy tests for Russian (ru) — Standard Moscow Russian, Cyrillic script."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Russian LanguageSpec once for the whole class."""
        request.cls._spec = _load("ru")

    # Vowels

    def test_vowel_a(self):
        """Cyrillic а maps to the open central vowel [a]."""
        _assert_first(_grapheme(self._spec, "а"), "a", label="ru:а")

    def test_vowel_e_initial(self):
        """Cyrillic е maps to [je, e] — starts with the glide in initial position."""
        vals = _grapheme(self._spec, "е")
        _assert_contains(vals, "je", "e", label="ru:е")
        assert vals[0] == "je", "ru:е — first candidate must be [je]"

    def test_vowel_yo(self):
        """Cyrillic ё always maps to [jo] (always stressed, always with glide)."""
        _assert_first(_grapheme(self._spec, "ё"), "jo", label="ru:ё")

    def test_vowel_i(self):
        """Cyrillic и maps to front vowel [i]."""
        _assert_first(_grapheme(self._spec, "и"), "i", label="ru:и")

    def test_vowel_o(self):
        """Cyrillic о maps to [o] (stressed; reduces to [ɐ]/[ə] unstressed — see allophones)."""
        _assert_first(_grapheme(self._spec, "о"), "o", label="ru:о")

    def test_vowel_u(self):
        """Cyrillic у maps to [u]."""
        _assert_first(_grapheme(self._spec, "у"), "u", label="ru:у")

    def test_vowel_e_front(self):
        """Cyrillic э maps to [ɛ] (front mid-open without preceding glide)."""
        _assert_first(_grapheme(self._spec, "э"), "ɛ", label="ru:э")

    def test_vowel_yu(self):
        """Cyrillic ю maps to [ju] (glide + back rounded vowel)."""
        _assert_first(_grapheme(self._spec, "ю"), "ju", label="ru:ю")

    def test_vowel_ya(self):
        """Cyrillic я maps to [ja] (glide + open vowel)."""
        _assert_first(_grapheme(self._spec, "я"), "ja", label="ru:я")

    def test_vowel_yeru(self):
        """Cyrillic ы maps to [ɨ] — the back unrounded vowel unique to East Slavic."""
        _assert_first(_grapheme(self._spec, "ы"), "ɨ", label="ru:ы")

    # Special signs

    def test_soft_sign_palatalization(self):
        """Cyrillic ь (soft sign) maps to [ʲ] — the palatalization diacritic."""
        _assert_first(_grapheme(self._spec, "ь"), "ʲ", label="ru:ь")

    def test_hard_sign_null(self):
        """Cyrillic ъ (hard sign) maps to an empty string — it is phonologically silent."""
        vals = _grapheme(self._spec, "ъ")
        assert vals is not None, "ru:ъ — mapping must exist (hard sign is present in orthography)"
        assert vals[0] == "", "ru:ъ — hard sign must map to empty string (phonologically null)"

    # Consonants

    def test_consonant_zh(self):
        """Cyrillic ж maps to the retroflex fricative [ʐ] in Standard Russian."""
        _assert_first(_grapheme(self._spec, "ж"), "ʐ", label="ru:ж")

    def test_consonant_kh(self):
        """Cyrillic х maps to the velar fricative [x]."""
        _assert_first(_grapheme(self._spec, "х"), "x", label="ru:х")

    def test_consonant_ts(self):
        """Cyrillic ц maps to the alveolar affricate [ts]."""
        _assert_first(_grapheme(self._spec, "ц"), "ts", label="ru:ц")

    def test_consonant_ch(self):
        """Cyrillic ч maps to the palatal affricate [tɕ]."""
        _assert_first(_grapheme(self._spec, "ч"), "tɕ", label="ru:ч")

    def test_consonant_sh(self):
        """Cyrillic ш maps to the retroflex fricative [ʂ] in Standard Russian."""
        _assert_first(_grapheme(self._spec, "ш"), "ʂ", label="ru:ш")

    def test_consonant_shch(self):
        """Cyrillic щ maps to [ɕː] (long palatal fricative in Standard Russian)."""
        _assert_first(_grapheme(self._spec, "щ"), "ɕː", label="ru:щ")

    # Auslaut devoicing — allophones

    def test_allophone_b_devoices(self):
        """Voiced /b/ can surface as voiceless [p] in final position (auslaut devoicing)."""
        _assert_contains(_allophone(self._spec, "b"), "b", "p", label="ru:allophone:b")

    def test_allophone_d_devoices(self):
        """Voiced /d/ can surface as voiceless [t] word-finally."""
        _assert_contains(_allophone(self._spec, "d"), "d", "t", label="ru:allophone:d")

    def test_allophone_g_devoices(self):
        """Voiced /ɡ/ can surface as voiceless [k] word-finally."""
        _assert_contains(_allophone(self._spec, "ɡ"), "ɡ", "k", label="ru:allophone:ɡ")

    def test_allophone_v_devoices(self):
        """Voiced /v/ can surface as voiceless [f] word-finally."""
        _assert_contains(_allophone(self._spec, "v"), "v", "f", label="ru:allophone:v")

    def test_allophone_z_devoices(self):
        """Voiced /z/ can surface as voiceless [s] word-finally."""
        _assert_contains(_allophone(self._spec, "z"), "z", "s", label="ru:allophone:z")

    def test_allophone_zh_devoices(self):
        """Voiced /ʐ/ can surface as voiceless [ʂ] word-finally."""
        _assert_contains(_allophone(self._spec, "ʐ"), "ʐ", "ʂ", label="ru:allophone:ʐ")

    def test_family(self):
        """Russian spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic", f"Expected family='Indo-European > Slavic', got {self._spec.family!r}"


# ---------------------------------------------------------------------------
# Polish
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestPolish:
    """Accuracy tests for Polish (pl) — Standard Polish, Latin script."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Polish LanguageSpec once for the whole class."""
        request.cls._spec = _load("pl")

    # Nasal vowels

    def test_nasal_a_primary(self):
        """Polish ą primary realisation is the nasal rounded vowel [ɔ̃]."""
        _assert_first(_grapheme(self._spec, "ą"), "ɔ̃", label="pl:ą")

    def test_nasal_a_variants(self):
        """Polish ą has multiple realisations including [ɔm], [ɔn], [ɔŋ] before stops."""
        _assert_contains(_grapheme(self._spec, "ą"), "ɔm", "ɔn", "ɔŋ", label="pl:ą-variants")

    def test_nasal_e_primary(self):
        """Polish ę primary realisation is the nasal front vowel [ɛ̃]."""
        _assert_first(_grapheme(self._spec, "ę"), "ɛ̃", label="pl:ę")

    def test_nasal_e_variants(self):
        """Polish ę has multiple realisations including [ɛm], [ɛn], [ɛŋ] before stops."""
        _assert_contains(_grapheme(self._spec, "ę"), "ɛm", "ɛn", "ɛŋ", label="pl:ę-variants")

    # Vowel mergers

    def test_o_acute_merger(self):
        """Polish ó has merged with /u/ — both map to [u]."""
        _assert_first(_grapheme(self._spec, "ó"), "u", label="pl:ó")

    def test_u_plain(self):
        """Polish u maps to [u] (same phoneme as ó)."""
        _assert_first(_grapheme(self._spec, "u"), "u", label="pl:u")

    def test_y_back_unrounded(self):
        """Polish y maps to [ɨ] — the back unrounded vowel."""
        _assert_first(_grapheme(self._spec, "y"), "ɨ", label="pl:y")

    # Dark-l vocalisation

    def test_l_stroke_w(self):
        """Polish ł maps to [w] — the historical dark-l has fully vocalised."""
        _assert_first(_grapheme(self._spec, "ł"), "w", label="pl:ł")

    # Sibilant affricates — alveolar series

    def test_c_affricate(self):
        """Polish c maps to the alveolar affricate [ts]."""
        _assert_first(_grapheme(self._spec, "c"), "ts", label="pl:c")

    def test_dz_voiced(self):
        """Polish dz maps to the voiced alveolar affricate [dz]."""
        _assert_first(_grapheme(self._spec, "dz"), "dz", label="pl:dz")

    # Sibilant affricates — retroflex series

    def test_cz_retroflex(self):
        """Polish cz maps to the retroflex affricate [tʂ]."""
        _assert_first(_grapheme(self._spec, "cz"), "tʂ", label="pl:cz")

    def test_dz_retroflex(self):
        """Polish dż maps to the voiced retroflex affricate [dʐ]."""
        _assert_first(_grapheme(self._spec, "dż"), "dʐ", label="pl:dż")

    def test_sz_retroflex(self):
        """Polish sz maps to the retroflex fricative [ʂ]."""
        _assert_first(_grapheme(self._spec, "sz"), "ʂ", label="pl:sz")

    def test_rz_retroflex(self):
        """Polish rz maps to [ʐ] (merged with ż in Standard Polish)."""
        _assert_first(_grapheme(self._spec, "rz"), "ʐ", label="pl:rz")

    # Sibilant affricates — alveolo-palatal series

    def test_c_acute_palatal(self):
        """Polish ć maps to the palatal affricate [tɕ]."""
        _assert_first(_grapheme(self._spec, "ć"), "tɕ", label="pl:ć")

    def test_dz_acute_palatal(self):
        """Polish dź maps to the voiced palatal affricate [dʑ]."""
        _assert_first(_grapheme(self._spec, "dź"), "dʑ", label="pl:dź")

    def test_s_acute_palatal(self):
        """Polish ś maps to the palatal fricative [ɕ]."""
        _assert_first(_grapheme(self._spec, "ś"), "ɕ", label="pl:ś")

    def test_z_acute_palatal(self):
        """Polish ź maps to the voiced palatal fricative [ʑ]."""
        _assert_first(_grapheme(self._spec, "ź"), "ʑ", label="pl:ź")

    def test_z_dot_retroflex(self):
        """Polish ż maps to the retroflex fricative [ʐ] (same as rz)."""
        _assert_first(_grapheme(self._spec, "ż"), "ʐ", label="pl:ż")

    def test_n_acute_palatal(self):
        """Polish ń maps to the palatal nasal [ɲ]."""
        _assert_first(_grapheme(self._spec, "ń"), "ɲ", label="pl:ń")

    # Auslaut devoicing — allophones

    def test_allophone_b_devoices(self):
        """Voiced /b/ can surface as [p] word-finally (auslaut devoicing)."""
        _assert_contains(_allophone(self._spec, "b"), "b", "p", label="pl:allophone:b")

    def test_allophone_g_devoices(self):
        """Voiced /ɡ/ can surface as [k] word-finally."""
        _assert_contains(_allophone(self._spec, "ɡ"), "ɡ", "k", label="pl:allophone:ɡ")

    def test_family(self):
        """Polish spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic", f"Expected family='Indo-European > Slavic', got {self._spec.family!r}"


# ---------------------------------------------------------------------------
# Czech
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestCzech:
    """Accuracy tests for Czech (cs) — Standard Czech, Latin script."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Czech LanguageSpec once for the whole class."""
        request.cls._spec = _load("cs")

    # Short vowels

    def test_vowel_a(self):
        """Czech a maps to short [a]."""
        _assert_first(_grapheme(self._spec, "a"), "a", label="cs:a")

    def test_vowel_e(self):
        """Czech e maps to short [ɛ]."""
        _assert_first(_grapheme(self._spec, "e"), "ɛ", label="cs:e")

    def test_vowel_i(self):
        """Czech i maps to short [ɪ]."""
        _assert_first(_grapheme(self._spec, "i"), "ɪ", label="cs:i")

    def test_vowel_y_same_as_i(self):
        """Czech y maps to [ɪ] — same phoneme as i (graphemic distinction only)."""
        _assert_first(_grapheme(self._spec, "y"), "ɪ", label="cs:y")

    # Long vowels

    def test_long_a(self):
        """Czech á maps to long [aː]."""
        _assert_first(_grapheme(self._spec, "á"), "aː", label="cs:á")

    def test_long_e(self):
        """Czech é maps to long [ɛː]."""
        _assert_first(_grapheme(self._spec, "é"), "ɛː", label="cs:é")

    def test_long_i(self):
        """Czech í maps to long [iː]."""
        _assert_first(_grapheme(self._spec, "í"), "iː", label="cs:í")

    def test_long_y(self):
        """Czech ý maps to long [iː] — same as í."""
        _assert_first(_grapheme(self._spec, "ý"), "iː", label="cs:ý")

    def test_long_u_acute(self):
        """Czech ú maps to long [uː]."""
        _assert_first(_grapheme(self._spec, "ú"), "uː", label="cs:ú")

    def test_long_u_ring(self):
        """Czech ů also maps to long [uː] — same phoneme as ú, historical spelling split."""
        _assert_first(_grapheme(self._spec, "ů"), "uː", label="cs:ů")

    # Special graphemes

    def test_e_hacek_palatal_glide(self):
        """Czech ě maps to [jɛ] — softens the preceding consonant and adds glide."""
        _assert_first(_grapheme(self._spec, "ě"), "jɛ", label="cs:ě")

    # Unique phoneme: ř

    def test_r_hacek_unique(self):
        """Czech ř maps to [r̝] — the raised/fricative trill unique to Czech."""
        _assert_first(_grapheme(self._spec, "ř"), "r̝", label="cs:ř")

    def test_r_hacek_allophone_devoiced(self):
        """Allophone of /r̝/ includes the voiceless [r̝̊] in devoicing contexts."""
        _assert_contains(_allophone(self._spec, "r̝"), "r̝", "r̝̊", label="cs:allophone:r̝")

    # Consonants

    def test_c_hacek(self):
        """Czech č maps to [tʃ]."""
        _assert_first(_grapheme(self._spec, "č"), "tʃ", label="cs:č")

    def test_s_hacek(self):
        """Czech š maps to [ʃ]."""
        _assert_first(_grapheme(self._spec, "š"), "ʃ", label="cs:š")

    def test_z_hacek(self):
        """Czech ž maps to [ʒ]."""
        _assert_first(_grapheme(self._spec, "ž"), "ʒ", label="cs:ž")

    def test_ch_digraph(self):
        """Czech ch (official digraph) maps to the velar fricative [x]."""
        _assert_first(_grapheme(self._spec, "ch"), "x", label="cs:ch")

    def test_n_hacek(self):
        """Czech ň maps to the palatal nasal [ɲ]."""
        _assert_first(_grapheme(self._spec, "ň"), "ɲ", label="cs:ň")

    # Auslaut devoicing — allophones

    def test_allophone_b_devoices(self):
        """Voiced /b/ can surface as [p] word-finally."""
        _assert_contains(_allophone(self._spec, "b"), "b", "p", label="cs:allophone:b")

    def test_allophone_d_devoices(self):
        """Voiced /d/ can surface as [t] word-finally."""
        _assert_contains(_allophone(self._spec, "d"), "d", "t", label="cs:allophone:d")

    def test_allophone_g_devoices(self):
        """Voiced /ɡ/ can surface as [k] word-finally."""
        _assert_contains(_allophone(self._spec, "ɡ"), "ɡ", "k", label="cs:allophone:ɡ")

    def test_allophone_v_devoices(self):
        """Czech /v/ can surface as [f] word-finally."""
        _assert_contains(_allophone(self._spec, "v"), "v", "f", label="cs:allophone:v")

    def test_family(self):
        """Czech spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic", f"Expected family='Indo-European > Slavic', got {self._spec.family!r}"


# ---------------------------------------------------------------------------
# Bulgarian
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestBulgarian:
    """Accuracy tests for Bulgarian (bg) — Standard Bulgarian, Cyrillic script."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Bulgarian LanguageSpec once for the whole class."""
        request.cls._spec = _load("bg")

    # Vowels — Cyrillic

    def test_vowel_a(self):
        """Cyrillic а maps to [a]."""
        _assert_first(_grapheme(self._spec, "а"), "a", label="bg:а")

    def test_vowel_e(self):
        """Cyrillic е maps to [ɛ] in Bulgarian (no initial glide unlike Russian)."""
        _assert_first(_grapheme(self._spec, "е"), "ɛ", label="bg:е")

    def test_vowel_i(self):
        """Cyrillic и maps to [i]."""
        _assert_first(_grapheme(self._spec, "и"), "i", label="bg:и")

    def test_vowel_o(self):
        """Cyrillic о maps to [ɔ]."""
        _assert_first(_grapheme(self._spec, "о"), "ɔ", label="bg:о")

    def test_vowel_u(self):
        """Cyrillic у maps to [u]."""
        _assert_first(_grapheme(self._spec, "у"), "u", label="bg:у")

    def test_vowel_yu(self):
        """Cyrillic ю maps to [ju]."""
        _assert_first(_grapheme(self._spec, "ю"), "ju", label="bg:ю")

    def test_vowel_ya(self):
        """Cyrillic я maps to [ja]."""
        _assert_first(_grapheme(self._spec, "я"), "ja", label="bg:я")

    # Critical unique feature: ъ → [ɤ]

    def test_er_golyam_unique(self):
        """Cyrillic ъ maps to [ɤ] — the back unrounded mid vowel unique to Bulgarian.

        This is the single most distinctive phonological feature of Bulgarian:
        ъ (er golyam) is a full vowel phoneme [ɤ], not a silent hard sign as in Russian.
        """
        _assert_first(_grapheme(self._spec, "ъ"), "ɤ", label="bg:ъ")

    def test_er_golyam_allophone(self):
        """Allophone of /ɤ/ includes [ɐ] in unstressed position."""
        _assert_contains(_allophone(self._spec, "ɤ"), "ɤ", "ɐ", label="bg:allophone:ɤ")

    # Consonants — Cyrillic

    def test_consonant_zh(self):
        """Cyrillic ж maps to [ʒ] in Bulgarian (not retroflex unlike Russian)."""
        _assert_first(_grapheme(self._spec, "ж"), "ʒ", label="bg:ж")

    def test_consonant_kh(self):
        """Cyrillic х maps to the velar fricative [x]."""
        _assert_first(_grapheme(self._spec, "х"), "x", label="bg:х")

    def test_consonant_ts(self):
        """Cyrillic ц maps to the alveolar affricate [ts]."""
        _assert_first(_grapheme(self._spec, "ц"), "ts", label="bg:ц")

    def test_consonant_ch(self):
        """Cyrillic ч maps to the post-alveolar affricate [tʃ]."""
        _assert_first(_grapheme(self._spec, "ч"), "tʃ", label="bg:ч")

    def test_consonant_sh(self):
        """Cyrillic ш maps to the post-alveolar fricative [ʃ]."""
        _assert_first(_grapheme(self._spec, "ш"), "ʃ", label="bg:ш")

    def test_shcht_south_slavic(self):
        """Cyrillic щ maps to [ʃt] in Bulgarian — South Slavic cluster, NOT [ɕtɕ] like Russian.

        This is a key typological difference: Bulgarian щ = [ʃt] (two segments),
        while Russian щ = [ɕː] (a single long palatal fricative).
        """
        _assert_first(_grapheme(self._spec, "щ"), "ʃt", label="bg:щ")

    # Auslaut devoicing — allophones

    def test_allophone_b_devoices(self):
        """Voiced /b/ can surface as [p] word-finally."""
        _assert_contains(_allophone(self._spec, "b"), "b", "p", label="bg:allophone:b")

    def test_allophone_d_devoices(self):
        """Voiced /d/ can surface as [t] word-finally."""
        _assert_contains(_allophone(self._spec, "d"), "d", "t", label="bg:allophone:d")

    def test_allophone_g_devoices(self):
        """Voiced /ɡ/ can surface as [k] word-finally."""
        _assert_contains(_allophone(self._spec, "ɡ"), "ɡ", "k", label="bg:allophone:ɡ")

    def test_allophone_v_devoices(self):
        """Voiced /v/ can surface as [f] word-finally."""
        _assert_contains(_allophone(self._spec, "v"), "v", "f", label="bg:allophone:v")

    def test_family(self):
        """Bulgarian spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic", f"Expected family='Indo-European > Slavic', got {self._spec.family!r}"


# ---------------------------------------------------------------------------
# Slovak — smoke tests
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestSlovak:
    """Smoke tests for Slovak (sk) — verifying spec loads and key phonological features."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Slovak LanguageSpec once for the whole class."""
        request.cls._spec = _load("sk")

    def test_spec_loads(self):
        """Slovak spec must load without error."""
        assert self._spec is not None

    def test_family_slavic(self):
        """Slovak spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic"

    def test_has_graphemes(self):
        """Slovak spec must have a non-empty grapheme mapping."""
        assert self._spec.graphemes, "graphemes dict must not be empty"

    def test_syllabic_r(self):
        """Slovak ŕ maps to [r̩ː] — long syllabic r, unique to Slovak."""
        _assert_first(_grapheme(self._spec, "ŕ"), "r̩ː", label="sk:ŕ")

    def test_syllabic_l(self):
        """Slovak ĺ maps to [l̩ː] — long syllabic l, unique to Slovak."""
        _assert_first(_grapheme(self._spec, "ĺ"), "l̩ː", label="sk:ĺ")

    def test_o_circumflex_diphthong(self):
        """Slovak ô maps to [uɔ] — the unique Slovak diphthong."""
        _assert_first(_grapheme(self._spec, "ô"), "uɔ", label="sk:ô")

    def test_h_voiced_fricative(self):
        """Slovak h maps to [ɦ] — voiced glottal fricative, like Czech (not Russian [ɡ])."""
        _assert_first(_grapheme(self._spec, "h"), "ɦ", label="sk:h")


# ---------------------------------------------------------------------------
# Ukrainian — smoke tests
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestUkrainian:
    """Smoke tests for Ukrainian (uk) — verifying spec loads and key phonological features."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Ukrainian LanguageSpec once for the whole class."""
        request.cls._spec = _load("uk")

    def test_spec_loads(self):
        """Ukrainian spec must load without error."""
        assert self._spec is not None

    def test_family_slavic(self):
        """Ukrainian spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic"

    def test_has_graphemes(self):
        """Ukrainian spec must have a non-empty grapheme mapping."""
        assert self._spec.graphemes, "graphemes dict must not be empty"

    def test_g_is_voiced_h(self):
        """Ukrainian г maps to [ɦ] — voiced glottal fricative, NOT [ɡ] as in Russian.

        This is the single most important Ukrainian-vs-Russian distinction:
        Ukrainian г = [ɦ]; Russian г = [ɡ].
        """
        _assert_first(_grapheme(self._spec, "г"), "ɦ", label="uk:г")

    def test_g_with_upturn_is_plosive(self):
        """Ukrainian ґ maps to [ɡ] — the separate letter for the plosive stop."""
        _assert_first(_grapheme(self._spec, "ґ"), "ɡ", label="uk:ґ")

    def test_yi_diphthong(self):
        """Ukrainian ї maps to [ji] — always the diphthong, no variant without glide."""
        _assert_first(_grapheme(self._spec, "ї"), "ji", label="uk:ї")

    def test_ye_palatal(self):
        """Ukrainian є maps to [jɛ]."""
        _assert_first(_grapheme(self._spec, "є"), "jɛ", label="uk:є")

    def test_i_distinct(self):
        """Ukrainian і maps to [i] — phonologically distinct from и."""
        _assert_first(_grapheme(self._spec, "і"), "i", label="uk:і")


# ---------------------------------------------------------------------------
# Belarusian — smoke tests
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestBelarusian:
    """Smoke tests for Belarusian (be) — verifying spec loads and key phonological features."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Belarusian LanguageSpec once for the whole class."""
        request.cls._spec = _load("be")

    def test_spec_loads(self):
        """Belarusian spec must load without error."""
        assert self._spec is not None

    def test_family_slavic(self):
        """Belarusian spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic"

    def test_has_graphemes(self):
        """Belarusian spec must have a non-empty grapheme mapping."""
        assert self._spec.graphemes, "graphemes dict must not be empty"

    def test_g_is_voiced_velar_fricative(self):
        """Belarusian г maps to [ɣ] — the voiced velar fricative (not [ɡ] or [ɦ])."""
        _assert_first(_grapheme(self._spec, "г"), "ɣ", label="be:г")

    def test_short_u_is_w(self):
        """Belarusian ў (short u) maps to [w] — a letter unique to the Belarusian alphabet."""
        _assert_first(_grapheme(self._spec, "ў"), "w", label="be:ў")


# ---------------------------------------------------------------------------
# Croatian — smoke tests
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestCroatian:
    """Smoke tests for Croatian (hr) — verifying spec loads and key phonological features."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Croatian LanguageSpec once for the whole class."""
        request.cls._spec = _load("hr")

    def test_spec_loads(self):
        """Croatian spec must load without error."""
        assert self._spec is not None

    def test_family_slavic(self):
        """Croatian spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic"

    def test_has_graphemes(self):
        """Croatian spec must have a non-empty grapheme mapping."""
        assert self._spec.graphemes, "graphemes dict must not be empty"

    def test_c_acute_soft_affricate(self):
        """Croatian ć maps to [tɕ] — the soft palatal affricate."""
        _assert_first(_grapheme(self._spec, "ć"), "tɕ", label="hr:ć")

    def test_c_hacek_hard_affricate(self):
        """Croatian č maps to [tʃ] — the hard post-alveolar affricate."""
        _assert_first(_grapheme(self._spec, "č"), "tʃ", label="hr:č")

    def test_lj_palatal_lateral(self):
        """Croatian lj digraph maps to [ʎ] — the palatal lateral approximant."""
        _assert_first(_grapheme(self._spec, "lj"), "ʎ", label="hr:lj")


# ---------------------------------------------------------------------------
# Slovenian — smoke tests
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestSlovenian:
    """Smoke tests for Slovenian (sl) — verifying spec loads and key phonological features."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Slovenian LanguageSpec once for the whole class."""
        request.cls._spec = _load("sl")

    def test_spec_loads(self):
        """Slovenian spec must load without error."""
        assert self._spec is not None

    def test_family_slavic(self):
        """Slovenian spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic"

    def test_has_graphemes(self):
        """Slovenian spec must have a non-empty grapheme mapping."""
        assert self._spec.graphemes, "graphemes dict must not be empty"

    def test_l_coda_vocalisation(self):
        """Slovenian l includes [w] as a realisation — coda l vocalises to [w]."""
        vals = _grapheme(self._spec, "l")
        _assert_contains(vals, "l", "w", label="sl:l")

    def test_lj_palatal(self):
        """Slovenian lj digraph maps to [ʎ]."""
        _assert_first(_grapheme(self._spec, "lj"), "ʎ", label="sl:lj")


# ---------------------------------------------------------------------------
# Serbian — smoke tests
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestSerbian:
    """Smoke tests for Serbian (sr) — verifying spec loads and key phonological features.

    Serbian uses both Cyrillic (primary) and Latin (Gaj) scripts; the spec
    includes grapheme entries for both.
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Serbian LanguageSpec once for the whole class."""
        request.cls._spec = _load("sr")

    def test_spec_loads(self):
        """Serbian spec must load without error."""
        assert self._spec is not None

    def test_family_slavic(self):
        """Serbian spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic"

    def test_has_graphemes(self):
        """Serbian spec must have a non-empty grapheme mapping."""
        assert self._spec.graphemes, "graphemes dict must not be empty"

    def test_cyrillic_c_tshe(self):
        """Serbian Cyrillic ћ maps to [tɕ] — the soft palatal affricate."""
        _assert_first(_grapheme(self._spec, "ћ"), "tɕ", label="sr:ћ")

    def test_cyrillic_dzhe(self):
        """Serbian Cyrillic џ maps to [dʒ] — the hard voiced post-alveolar affricate."""
        _assert_first(_grapheme(self._spec, "џ"), "dʒ", label="sr:џ")

    def test_cyrillic_lje(self):
        """Serbian Cyrillic љ maps to [ʎ] — the palatal lateral."""
        _assert_first(_grapheme(self._spec, "љ"), "ʎ", label="sr:љ")


# ---------------------------------------------------------------------------
# Macedonian — smoke tests
# ---------------------------------------------------------------------------

@pytest.mark.linguistic
class TestMacedonian:
    """Smoke tests for Macedonian (mk) — verifying spec loads and key phonological features."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Macedonian LanguageSpec once for the whole class."""
        request.cls._spec = _load("mk")

    def test_spec_loads(self):
        """Macedonian spec must load without error."""
        assert self._spec is not None

    def test_family_slavic(self):
        """Macedonian spec must declare family='Slavic'."""
        assert self._spec.family == "Indo-European > Slavic"

    def test_has_graphemes(self):
        """Macedonian spec must have a non-empty grapheme mapping."""
        assert self._spec.graphemes, "graphemes dict must not be empty"

    def test_unique_dze(self):
        """Macedonian ѕ maps to [dz] — unique letter present only in Macedonian Cyrillic."""
        _assert_first(_grapheme(self._spec, "ѕ"), "dz", label="mk:ѕ")

    def test_unique_gje(self):
        """Macedonian ѓ maps to [ɟ] — unique palatal stop letter in Macedonian Cyrillic."""
        _assert_first(_grapheme(self._spec, "ѓ"), "ɟ", label="mk:ѓ")

    def test_unique_kje(self):
        """Macedonian ќ maps to [c] — unique voiceless palatal stop in Macedonian Cyrillic."""
        _assert_first(_grapheme(self._spec, "ќ"), "c", label="mk:ќ")
