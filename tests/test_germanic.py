"""Per-language accuracy tests for Germanic languages.

Covers:
- German: Standard (de-DE), Austrian (de-AT), Bavarian (de-x-bavarian)
- Dutch: Standard (nl-NL), Belgian (nl-BE)
- Afrikaans: af
- Swedish: sv, Stockholm (sv-x-rikssvenska), Scanian (sv-x-skanska)
- Danish: da, Copenhagen (da-x-copenhagen)
- Norwegian Bokmål: nb
- Icelandic: is
- Faroese: fo

Run with:
    pytest tests/test_germanic.py -v --tb=short
"""
from __future__ import annotations

import pytest
import orthography2ipa
from orthography2ipa.types import GraphemePosition

# ═══════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════

_SENTINEL = object()


def _load(code: str):
    """Load a LanguageSpec, skipping the test if unavailable."""
    try:
        return orthography2ipa.get(code)
    except Exception as exc:
        pytest.skip(f"{code!r} not available: {exc}")


def _grapheme(spec, grapheme: str) -> list:
    """Return the grapheme→IPA list from the fully inherited table."""
    return spec.graphemes.get(grapheme, [])


def _allophone(spec, phoneme: str):
    """Return the allophone list for a phoneme (None means phoneme absent/nulled)."""
    return spec.allophones.get(phoneme)


def _positional(spec, grapheme: str, position: GraphemePosition):
    """Resolve a grapheme in a specific positional context."""
    pos_map = spec.positional_graphemes.get(grapheme)
    if pos_map is None:
        return None
    return pos_map.get(position)


def _assert_contains(values, *expected, label: str = "") -> None:
    """Assert that every expected IPA symbol appears somewhere in *values*."""
    assert values is not None, f"{label}: mapping is absent"
    for exp in expected:
        assert exp in values, f"{label}: {exp!r} not in {values!r}"


def _assert_first(values, expected: str, label: str = "") -> None:
    """Assert the default (first) IPA candidate is *expected*."""
    assert values is not None, f"{label}: mapping is None (nulled out)"
    assert len(values) > 0, f"{label}: empty mapping"
    assert values[0] == expected, (
        f"{label}: expected first={expected!r}, got {values[0]!r}"
    )


def _assert_null(spec, grapheme: str) -> None:
    """Assert that *grapheme* was nulled out or is absent from the resolved table."""
    result = spec.graphemes.get(grapheme, _SENTINEL)
    assert result is _SENTINEL or result is None, (
        f"grapheme {grapheme!r} should be absent/null but is {result!r}"
    )


def _assert_allophone_null(spec, phoneme: str) -> None:
    """Assert that *phoneme* is explicitly absent from the allophone inventory."""
    result = spec.allophones.get(phoneme, _SENTINEL)
    assert result is _SENTINEL or result is None, (
        f"allophone {phoneme!r} should be absent/null but is {result!r}"
    )


# ═══════════════════════════════════════════════════════════════════════════
# STANDARD GERMAN  (de-DE)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestGermanStandard:
    """Comprehensive accuracy tests for Standard German (de-DE).

    German orthography is largely phonemic, with notable alternations for
    umlaut vowels, vowel length (short vs long), the uvular fricative /ʁ/,
    digraphs (sch, ch, ie, ei, au, eu), and final-obstruent devoicing
    (Auslautverhärtung).
    """

    LANGUAGE_CODE = "de-DE"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the de-DE LanguageSpec once for the entire class."""
        request.cls._spec = _load("de-DE")

    # --- Registry ---

    def test_code(self):
        """The spec code must round-trip to de-DE."""
        assert self._spec.code == "de-DE"

    def test_family(self):
        """German belongs to the Germanic language family."""
        assert self._spec.family == "Germanic"

    def test_script(self):
        """Modern German is written in the Latin script."""
        assert self._spec.script == "Latin"

    # --- Vowels (short/long contrasts) ---

    def test_vowel_a_short_and_long(self):
        """<a> covers both the short /a/ and long /aː/ realizations."""
        g = _grapheme(self._spec, "a")
        _assert_contains(g, "a", "aː", label="de-DE a")

    def test_vowel_e_has_schwa_and_mid(self):
        """<e> has at minimum the mid-open /ɛ/, mid /eː/, and schwa /ə/ variants."""
        g = _grapheme(self._spec, "e")
        _assert_contains(g, "ɛ", "eː", "ə", label="de-DE e")

    def test_vowel_i_short_and_long(self):
        """<i> maps to the lax /ɪ/ (short) and tense /iː/ (long)."""
        g = _grapheme(self._spec, "i")
        _assert_contains(g, "ɪ", "iː", label="de-DE i")

    def test_vowel_o_short_and_long(self):
        """<o> maps to the short /ɔ/ and long /oː/."""
        g = _grapheme(self._spec, "o")
        _assert_contains(g, "ɔ", "oː", label="de-DE o")

    def test_vowel_u_short_and_long(self):
        """<u> maps to the lax /ʊ/ (short) and tense /uː/ (long)."""
        g = _grapheme(self._spec, "u")
        _assert_contains(g, "ʊ", "uː", label="de-DE u")

    # --- Umlaut vowels ---

    def test_umlaut_ae(self):
        """<ä> (A-umlaut) covers both /ɛ/ (short) and /ɛː/ (long)."""
        g = _grapheme(self._spec, "ä")
        _assert_contains(g, "ɛ", "ɛː", label="de-DE ä")

    def test_umlaut_oe(self):
        """<ö> (O-umlaut) covers both /œ/ (short) and /øː/ (long)."""
        g = _grapheme(self._spec, "ö")
        _assert_contains(g, "œ", "øː", label="de-DE ö")

    def test_umlaut_ue(self):
        """<ü> (U-umlaut) covers both /ʏ/ (short) and /yː/ (long)."""
        g = _grapheme(self._spec, "ü")
        _assert_contains(g, "ʏ", "yː", label="de-DE ü")

    def test_y_as_umlaut_equivalent(self):
        """<y> in German loans maps like <ü>: /ʏ/ and /yː/."""
        g = _grapheme(self._spec, "y")
        _assert_contains(g, "ʏ", "yː", label="de-DE y")

    # --- Digraph vowels ---

    def test_ie_is_long_i(self):
        """<ie> is the canonical spelling for /iː/ (e.g., *Liebe*, *viel*)."""
        _assert_first(_grapheme(self._spec, "ie"), "iː", label="de-DE ie")

    def test_ei_diphthong(self):
        """<ei> is the falling diphthong /aɪ/ (e.g., *klein*, *Stein*)."""
        _assert_first(_grapheme(self._spec, "ei"), "aɪ", label="de-DE ei")

    def test_au_diphthong(self):
        """<au> is the /aʊ/ diphthong (e.g., *Haus*, *Baum*)."""
        _assert_first(_grapheme(self._spec, "au"), "aʊ", label="de-DE au")

    def test_eu_diphthong(self):
        """<eu> is the /ɔʏ/ diphthong (e.g., *neu*, *heute*)."""
        _assert_first(_grapheme(self._spec, "eu"), "ɔʏ", label="de-DE eu")

    def test_aeu_diphthong(self):
        """<äu> (umlaut plural diphthong) also maps to /ɔʏ/ (e.g., *Häuser*)."""
        _assert_first(_grapheme(self._spec, "äu"), "ɔʏ", label="de-DE äu")

    # --- Consonants ---

    def test_w_is_labiodental_fricative(self):
        """<w> → /v/ (labiodental fricative), unlike English /w/."""
        _assert_first(_grapheme(self._spec, "w"), "v", label="de-DE w")

    def test_v_default_is_labiodental(self):
        """<v> defaults to /f/ (e.g., *Vogel*, *von*) but includes /v/ in loans."""
        g = _grapheme(self._spec, "v")
        _assert_contains(g, "f", "v", label="de-DE v")

    def test_s_includes_voiced(self):
        """<s> can surface as the voiced /z/ (e.g., word-initially before vowels)."""
        g = _grapheme(self._spec, "s")
        _assert_contains(g, "z", "s", label="de-DE s")

    def test_c_ambiguous(self):
        """<c> is ambiguous: /k/ in most contexts, /ts/ before e/i/ä."""
        g = _grapheme(self._spec, "c")
        _assert_contains(g, "k", "ts", label="de-DE c")

    def test_sch_is_postalveolar(self):
        """<sch> is the postalveolar fricative /ʃ/ (e.g., *Schule*, *Fisch*)."""
        _assert_first(_grapheme(self._spec, "sch"), "ʃ", label="de-DE sch")

    def test_ch_is_ambiguous(self):
        """<ch> is /x/ after back vowels and /ç/ after front vowels/consonants."""
        g = _grapheme(self._spec, "ch")
        _assert_contains(g, "x", "ç", label="de-DE ch")

    def test_ng_is_velar_nasal(self):
        """<ng> → /ŋ/ (no epenthetic /ɡ/, unlike English *finger*)."""
        _assert_first(_grapheme(self._spec, "ng"), "ŋ", label="de-DE ng")

    def test_qu_cluster(self):
        """<qu> → /kv/ (e.g., *Qualität*, *Quelle*)."""
        _assert_first(_grapheme(self._spec, "qu"), "kv", label="de-DE qu")

    def test_pf_affricate(self):
        """<pf> → /pf/ labiodental affricate (e.g., *Pferd*, *Apfel*)."""
        _assert_first(_grapheme(self._spec, "pf"), "pf", label="de-DE pf")

    def test_tz_affricate(self):
        """<tz> → /ts/ (e.g., *sitzen*, *Katze*)."""
        _assert_first(_grapheme(self._spec, "tz"), "ts", label="de-DE tz")

    def test_r_is_uvular(self):
        """<r> defaults to the uvular fricative/approximant /ʁ/ in Standard German."""
        _assert_first(_grapheme(self._spec, "r"), "ʁ", label="de-DE r")

    # --- Allophones ---

    def test_r_allophone_variation(self):
        """The /ʁ/ phoneme has surface variants including /ʀ/, /χ/, and vocalic /ɐ/."""
        a = _allophone(self._spec, "ʁ")
        _assert_contains(a, "ʁ", label="de-DE allophone ʁ")

    def test_auslaut_devoicing_b(self):
        """AUSLAUTVERHÄRTUNG: /b/ can surface as [p] in coda position."""
        a = _allophone(self._spec, "b")
        _assert_contains(a, "b", "p", label="de-DE allophone b (auslaut devoicing)")

    def test_auslaut_devoicing_d(self):
        """AUSLAUTVERHÄRTUNG: /d/ can surface as [t] in coda position."""
        a = _allophone(self._spec, "d")
        _assert_contains(a, "d", "t", label="de-DE allophone d (auslaut devoicing)")

    def test_auslaut_devoicing_g(self):
        """AUSLAUTVERHÄRTUNG: /ɡ/ can surface as [k] in coda position."""
        a = _allophone(self._spec, "ɡ")
        _assert_contains(a, "ɡ", "k", label="de-DE allophone ɡ (auslaut devoicing)")

    def test_aspiration_p(self):
        """Voiceless stops are aspirated in onset: /p/ → [pʰ]."""
        a = _allophone(self._spec, "p")
        _assert_contains(a, "p", "pʰ", label="de-DE allophone p aspiration")

    def test_aspiration_t(self):
        """Voiceless stops are aspirated in onset: /t/ → [tʰ]."""
        a = _allophone(self._spec, "t")
        _assert_contains(a, "t", "tʰ", label="de-DE allophone t aspiration")

    def test_aspiration_k(self):
        """Voiceless stops are aspirated in onset: /k/ → [kʰ]."""
        a = _allophone(self._spec, "k")
        _assert_contains(a, "k", "kʰ", label="de-DE allophone k aspiration")

    def test_palatal_fricative_allophone(self):
        """The palatal fricative /ç/ (ich-Laut) is present in the allophone table."""
        a = _allophone(self._spec, "ç")
        assert a is not None, "de-DE: /ç/ should be in allophone table"
        _assert_contains(a, "ç", label="de-DE allophone ç")

    def test_voiceless_velar_fricative_allophone(self):
        """The velar fricative /x/ (ach-Laut) is in the allophone table."""
        a = _allophone(self._spec, "x")
        assert a is not None, "de-DE: /x/ should be in allophone table"
        _assert_contains(a, "x", label="de-DE allophone x")


# ═══════════════════════════════════════════════════════════════════════════
# AUSTRIAN GERMAN  (de-AT)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestAustrianGerman:
    """Accuracy tests for Austrian German (de-AT).

    Austrian German inherits de-DE graphemes but differs in vowel quality
    (ɛː → eː merger) and in rhotic realisation (uvular /ʀ/ or tapped /r/
    alongside the standard /ʁ/).
    """

    LANGUAGE_CODE = "de-AT"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the de-AT LanguageSpec once for the entire class."""
        request.cls._spec = _load("de-AT")

    def test_code(self):
        """The spec code must round-trip to de-AT."""
        assert self._spec.code == "de-AT"

    def test_family(self):
        """Austrian German is Germanic."""
        assert self._spec.family == "Germanic"

    def test_parent_is_standard_german(self):
        """de-AT must declare de-DE as its parent to inherit graphemes."""
        assert self._spec.parent == "de-DE"

    def test_ae_long_merger(self):
        """AUSTRIAN FEATURE: /ɛː/ (long ä) merges with /eː/ in Austrian standard.

        The allophone entry for ɛː should include eː as a variant.
        """
        a = _allophone(self._spec, "ɛː")
        assert a is not None, "de-AT: ɛː should be in allophone table"
        _assert_contains(a, "eː", "ɛː", label="de-AT allophone ɛː→eː merger")

    def test_rhotic_variants(self):
        """AUSTRIAN FEATURE: rhotic allows uvular trill /ʀ/, tapped /r/, and vocalic /ɐ/."""
        a = _allophone(self._spec, "ʁ")
        assert a is not None, "de-AT: ʁ should be in allophone table"
        _assert_contains(a, "ʀ", label="de-AT allophone ʁ includes ʀ")

    def test_inherits_sch(self):
        """de-AT inherits <sch>→/ʃ/ from de-DE without redefinition."""
        _assert_first(_grapheme(self._spec, "sch"), "ʃ", label="de-AT inherits sch")

    def test_inherits_ei_diphthong(self):
        """de-AT inherits <ei>→/aɪ/ from de-DE."""
        _assert_first(_grapheme(self._spec, "ei"), "aɪ", label="de-AT inherits ei")


# ═══════════════════════════════════════════════════════════════════════════
# BAVARIAN GERMAN  (de-x-bavarian)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestBavarianGerman:
    """Accuracy tests for Bavarian German (de-x-bavarian).

    Bavarian is a Southern German dialect cluster spoken in Bavaria and
    Austria. Key features: preservation of /r/ as a tapped/trilled consonant
    (not uvular), and a diphthong merger where the Standard /aɪ/ and /ɔɪ/ can
    converge.
    """

    LANGUAGE_CODE = "de-x-bavarian"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the de-x-bavarian LanguageSpec once for the entire class."""
        request.cls._spec = _load("de-x-bavarian")

    def test_code(self):
        """The spec code must round-trip to de-x-bavarian."""
        assert self._spec.code == "de-x-bavarian"

    def test_parent_is_austrian_german(self):
        """de-x-bavarian declares de-AT as its parent (Bavarian ← Austrian ← Standard)."""
        assert self._spec.parent == "de-AT"

    def test_diphthong_aI_includes_oI_variant(self):
        """BAVARIAN FEATURE: /aɪ/ allophone table includes /ɔɪ/ (diphthong merger)."""
        a = _allophone(self._spec, "aɪ")
        assert a is not None, "de-x-bavarian: aɪ should be in allophone table"
        _assert_contains(a, "aɪ", "ɔɪ", label="de-x-bavarian aɪ→ɔɪ")

    def test_rhotic_is_apical(self):
        """BAVARIAN FEATURE: rhotic is apical /r/ (not uvular /ʁ/)."""
        a = _allophone(self._spec, "ʁ")
        assert a is not None, "de-x-bavarian: ʁ should be in allophone table"
        _assert_contains(a, "r", label="de-x-bavarian allophone ʁ includes apical r")

    def test_ae_long_unchanged(self):
        """Bavarian retains /ɛː/ without the Austrian eː merger."""
        a = _allophone(self._spec, "ɛː")
        assert a is not None, "de-x-bavarian: ɛː should be in allophone table"
        _assert_contains(a, "ɛː", label="de-x-bavarian ɛː retained")

    def test_inherits_umlaut_oe(self):
        """de-x-bavarian inherits <ö>→[œ, øː] from de-DE."""
        g = _grapheme(self._spec, "ö")
        _assert_contains(g, "œ", "øː", label="de-x-bavarian inherits ö")


# ═══════════════════════════════════════════════════════════════════════════
# STANDARD DUTCH  (nl-NL)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestDutch:
    """Comprehensive accuracy tests for Standard Dutch (nl-NL).

    Dutch has a phonemic vowel-length contrast written as single vs doubled
    vowel letter (a/aa, e/ee, o/oo, u/uu). The velar fricative /ɣ/ (voiced)
    alternates with /x/ (voiceless); the /r/ can be either alveolar or uvular
    depending on region and register.
    """

    LANGUAGE_CODE = "nl-NL"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the nl-NL LanguageSpec once for the entire class."""
        request.cls._spec = _load("nl-NL")

    # --- Registry ---

    def test_code(self):
        """The spec code must round-trip to nl-NL."""
        assert self._spec.code == "nl-NL"

    def test_family(self):
        """Dutch belongs to the Germanic family."""
        assert self._spec.family == "Germanic"

    def test_script(self):
        """Dutch uses the Latin script."""
        assert self._spec.script == "Latin"

    # --- Short vowels ---

    def test_a_short(self):
        """<a> is the short open back vowel /ɑ/ (e.g., *bad*, *kan*)."""
        _assert_first(_grapheme(self._spec, "a"), "ɑ", label="nl-NL a")

    def test_e_short(self):
        """<e> is short /ɛ/ or schwa /ə/ (e.g., *bed*, unstressed syllables)."""
        g = _grapheme(self._spec, "e")
        _assert_contains(g, "ɛ", "ə", label="nl-NL e")

    def test_i_short(self):
        """<i> is the short /ɪ/ (e.g., *bit*, *kin*)."""
        _assert_first(_grapheme(self._spec, "i"), "ɪ", label="nl-NL i")

    def test_o_short(self):
        """<o> is the short open-mid /ɔ/ (e.g., *bot*, *kom*)."""
        _assert_first(_grapheme(self._spec, "o"), "ɔ", label="nl-NL o")

    def test_u_short(self):
        """<u> is the short front rounded /ʏ/ (e.g., *put*, *bus*)."""
        _assert_first(_grapheme(self._spec, "u"), "ʏ", label="nl-NL u")

    # --- Long vowels (doubled spellings) ---

    def test_aa_long(self):
        """<aa> is the long /aː/ (e.g., *baan*, *maar*)."""
        _assert_first(_grapheme(self._spec, "aa"), "aː", label="nl-NL aa")

    def test_ee_long(self):
        """<ee> is the long /eː/ (e.g., *beer*, *meer*)."""
        _assert_first(_grapheme(self._spec, "ee"), "eː", label="nl-NL ee")

    def test_oo_long(self):
        """<oo> is the long /oː/ (e.g., *boot*, *roos*)."""
        _assert_first(_grapheme(self._spec, "oo"), "oː", label="nl-NL oo")

    def test_uu_long(self):
        """<uu> is the long /yː/ (e.g., *muur*, *uur*)."""
        _assert_first(_grapheme(self._spec, "uu"), "yː", label="nl-NL uu")

    # --- Special digraphs ---

    def test_ie_is_high_front(self):
        """<ie> → /iː/ (e.g., *dier*, *mier*); distinct from short /ɪ/."""
        _assert_first(_grapheme(self._spec, "ie"), "iː", label="nl-NL ie")

    def test_oe_is_high_back(self):
        """<oe> → /u/ (e.g., *boek*, *moeder*); the Dutch spelling of /u/."""
        _assert_first(_grapheme(self._spec, "oe"), "u", label="nl-NL oe")

    def test_eu_is_mid_front_rounded(self):
        """<eu> → /øː/ (e.g., *deur*, *neus*)."""
        _assert_first(_grapheme(self._spec, "eu"), "øː", label="nl-NL eu")

    def test_ei_diphthong(self):
        """<ei> → /ɛi/ (e.g., *klein*, *trein*)."""
        _assert_first(_grapheme(self._spec, "ei"), "ɛi", label="nl-NL ei")

    def test_ij_equals_ei(self):
        """<ij> and <ei> are homophones: both → /ɛi/ (e.g., *ijs*, *zijn*)."""
        _assert_first(_grapheme(self._spec, "ij"), "ɛi", label="nl-NL ij")

    def test_au_diphthong(self):
        """<au> → /ɑu/ (e.g., *auto*, *blauw*)."""
        _assert_first(_grapheme(self._spec, "au"), "ɑu", label="nl-NL au")

    def test_ou_equals_au(self):
        """<ou> and <au> are homophones: both → /ɑu/ (e.g., *oud*, *goud*)."""
        _assert_first(_grapheme(self._spec, "ou"), "ɑu", label="nl-NL ou")

    # --- Consonants ---

    def test_g_is_velar_fricative(self):
        """<g> → /ɣ/ (voiced) and /x/ (voiceless) in Dutch; the famous Dutch G."""
        g = _grapheme(self._spec, "g")
        _assert_contains(g, "ɣ", "x", label="nl-NL g")

    def test_ch_is_voiceless_velar_fricative(self):
        """<ch> → /x/ (e.g., *acht*, *lach*)."""
        _assert_first(_grapheme(self._spec, "ch"), "x", label="nl-NL ch")

    def test_sch_onset(self):
        """<sch> → /sx/ (e.g., *school*, *schip*) — note reversed from German."""
        _assert_first(_grapheme(self._spec, "sch"), "sx", label="nl-NL sch")

    def test_w_is_labiodental_approximant(self):
        """<w> in Dutch is the labiodental approximant /ʋ/."""
        g = _grapheme(self._spec, "w")
        _assert_first(g, "ʋ", label="nl-NL w")

    def test_ng_is_velar_nasal(self):
        """<ng> → /ŋ/ (e.g., *lang*, *wang*)."""
        _assert_first(_grapheme(self._spec, "ng"), "ŋ", label="nl-NL ng")

    def test_nk_cluster(self):
        """<nk> → /ŋk/ (e.g., *bank*, *denk*)."""
        _assert_first(_grapheme(self._spec, "nk"), "ŋk", label="nl-NL nk")

    def test_r_variants(self):
        """<r> in Dutch can be alveolar /r/ or uvular /ʁ/ depending on register."""
        g = _grapheme(self._spec, "r")
        _assert_contains(g, "r", label="nl-NL r")

    # --- Allophones ---

    def test_gamma_allophone(self):
        """The /ɣ/ phoneme alternates with /x/ (voiceless) in coda and loanwords."""
        a = _allophone(self._spec, "ɣ")
        assert a is not None, "nl-NL: /ɣ/ should be in allophone table"
        _assert_contains(a, "ɣ", "x", label="nl-NL allophone ɣ")

    def test_r_allophone_includes_uvular(self):
        """The /r/ phoneme can surface as uvular /ʁ/ — both alveolar and uvular r used in NL."""
        a = _allophone(self._spec, "r")
        assert a is not None, "nl-NL: /r/ should be in allophone table"
        _assert_contains(a, "r", "ʁ", label="nl-NL allophone r includes ʁ")


# ═══════════════════════════════════════════════════════════════════════════
# BELGIAN DUTCH / FLEMISH  (nl-BE)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestFlemish:
    """Accuracy tests for Belgian Dutch / Flemish (nl-BE).

    Flemish (Southern Dutch) differs from Standard Dutch primarily in the
    realisation of the velar fricative (softer, palatal /ʝ/ in onset) and
    the rhotic (apical /r/ or tapped /ɾ/, not uvular).
    """

    LANGUAGE_CODE = "nl-BE"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the nl-BE LanguageSpec once for the entire class."""
        request.cls._spec = _load("nl-BE")

    def test_code(self):
        """The spec code must round-trip to nl-BE."""
        assert self._spec.code == "nl-BE"

    def test_parent_is_dutch(self):
        """nl-BE inherits from nl (pan-Dutch), not nl-NL directly."""
        assert self._spec.parent == "nl"

    def test_gamma_includes_palatal_variant(self):
        """FLEMISH FEATURE: /ɣ/ can surface as palatal /ʝ/ in onset (softer G)."""
        a = _allophone(self._spec, "ɣ")
        assert a is not None, "nl-BE: ɣ should be in allophone table"
        _assert_contains(a, "ɣ", "ʝ", label="nl-BE allophone ɣ→ʝ")

    def test_rhotic_is_apical_or_tapped(self):
        """FLEMISH FEATURE: rhotic is apical /r/ or flap /ɾ/ (not uvular /ʁ/)."""
        a = _allophone(self._spec, "r")
        assert a is not None, "nl-BE: r should be in allophone table"
        _assert_contains(a, "r", "ɾ", label="nl-BE allophone r")

    def test_inherits_ei_diphthong(self):
        """nl-BE inherits <ei>→/ɛi/ from nl-NL."""
        _assert_first(_grapheme(self._spec, "ei"), "ɛi", label="nl-BE inherits ei")

    def test_inherits_oe(self):
        """nl-BE inherits <oe>→/uː/ from Dutch (back rounded vowel)."""
        vals = _grapheme(self._spec, "oe")
        assert vals is not None, "nl-BE: oe should be inherited"
        assert vals[0] in ("u", "uː"), f"nl-BE: oe expected u/uː, got {vals[0]}"


# ═══════════════════════════════════════════════════════════════════════════
# AFRIKAANS  (af)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestAfrikaans:
    """Accuracy tests for Afrikaans (af).

    Afrikaans is a daughter language of Dutch (17th-century Cape Colony variety)
    with significant simplifications in morphology and some sound changes. The
    spelling system closely reflects the spoken form. Key features: retention of
    /ɣ/ as the dominant <g> realization, open vowels, and the /øː/ vowel for <eu>.
    """

    LANGUAGE_CODE = "af"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the af LanguageSpec once for the entire class."""
        request.cls._spec = _load("af")

    # --- Registry ---

    def test_code(self):
        """The spec code must round-trip to af."""
        assert self._spec.code == "af"

    def test_family(self):
        """Afrikaans is a Germanic language (West Germanic branch)."""
        assert self._spec.family == "Germanic"

    # --- Vowels ---

    def test_a_is_open_back(self):
        """<a> in Afrikaans is the open back /ɑ/ (e.g., *bad*, *man*)."""
        _assert_first(_grapheme(self._spec, "a"), "ɑ", label="af a")

    def test_aa_is_long(self):
        """<aa> → /aː/ (e.g., *baas*, *naam*)."""
        _assert_first(_grapheme(self._spec, "aa"), "aː", label="af aa")

    def test_ee_is_long_mid(self):
        """<ee> → /eː/ (e.g., *been*, *meer*)."""
        _assert_first(_grapheme(self._spec, "ee"), "eː", label="af ee")

    def test_ie_is_high(self):
        """<ie> → /i/ (e.g., *dier*, *hier*); Afrikaans shortens the Dutch /iː/."""
        _assert_first(_grapheme(self._spec, "ie"), "i", label="af ie")

    def test_oe_is_high_back(self):
        """<oe> → /u/ (e.g., *boek*, *moeder*)."""
        _assert_first(_grapheme(self._spec, "oe"), "u", label="af oe")

    def test_eu_is_front_rounded(self):
        """<eu> → /øː/ (e.g., *seun*, *deur*)."""
        _assert_first(_grapheme(self._spec, "eu"), "øː", label="af eu")

    def test_oo_is_long(self):
        """<oo> → /oː/ (e.g., *boom*, *roos*)."""
        _assert_first(_grapheme(self._spec, "oo"), "oː", label="af oo")

    # --- Consonants ---

    def test_g_voiceless_velar(self):
        """<g> in Afrikaans is the voiceless velar/uvular fricative /x/ (not voiced /ɣ/)."""
        g = _grapheme(self._spec, "g")
        _assert_first(g, "x", label="af g first value x")

    def test_v_is_labiodental(self):
        """<v> → /f/ or /v/ in Afrikaans (e.g., *van*, *veld*)."""
        g = _grapheme(self._spec, "v")
        _assert_contains(g, "f", "v", label="af v")

    def test_ch_is_voiceless_velar(self):
        """<ch> → /x/ (e.g., *ag*, *hoog*)."""
        _assert_first(_grapheme(self._spec, "ch"), "x", label="af ch")

    def test_r_is_apical(self):
        """<r> in Afrikaans is the apical trill /r/ (not uvular)."""
        _assert_first(_grapheme(self._spec, "r"), "r", label="af r")


# ═══════════════════════════════════════════════════════════════════════════
# SWEDISH  (sv)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestSwedish:
    """Comprehensive accuracy tests for Swedish (sv).

    Swedish has a complex vowel system with 9 vowel qualities in both long and
    short forms. Notable features: the unusual mapping of <o> to /uː/ in some
    positions (Swedish /u/ is /ʉː/), the palatal softening of /k/ and /g/ before
    front vowels, the sje-sound /ɧ/ (a complex articulation), and the
    distinctive pitch accent (not captured in orthography).
    """

    LANGUAGE_CODE = "sv"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the sv LanguageSpec once for the entire class."""
        request.cls._spec = _load("sv")

    # --- Registry ---

    def test_code(self):
        """The spec code must round-trip to sv."""
        assert self._spec.code == "sv"

    def test_family(self):
        """Swedish is a North Germanic (Scandinavian) language."""
        assert self._spec.family == "Germanic"

    def test_script(self):
        """Swedish uses the Latin script."""
        assert self._spec.script == "Latin"

    # --- Vowels ---

    def test_a_short_and_long(self):
        """<a> covers both short /a/ (as in *katt*) and long /ɑː/ (as in *dag*)."""
        g = _grapheme(self._spec, "a")
        _assert_contains(g, "a", "ɑː", label="sv a")

    def test_e_short_and_long(self):
        """<e> covers /ɛ/ (short, as in *ett*) and /eː/ (long, as in *se*)."""
        g = _grapheme(self._spec, "e")
        _assert_contains(g, "ɛ", "eː", label="sv e")

    def test_i_short_and_long(self):
        """<i> covers /ɪ/ (short) and /iː/ (long)."""
        g = _grapheme(self._spec, "i")
        _assert_contains(g, "ɪ", "iː", label="sv i")

    def test_o_unusual_mapping(self):
        """SWEDISH FEATURE: <o> maps to /ɔ/ (short) and /uː/ (long) — not /oː/!

        Swedish /uː/ is spelled <o>, while Swedish <u> is the close central
        rounded /ʉː/. This is one of the most striking Swedish orthographic
        features.
        """
        g = _grapheme(self._spec, "o")
        _assert_contains(g, "ɔ", "uː", label="sv o→[ɔ,uː]")

    def test_u_is_central_rounded(self):
        """<u> → /ɵ/ (short) and /ʉː/ (long) — Swedish /u/ is central, not back."""
        g = _grapheme(self._spec, "u")
        _assert_contains(g, "ɵ", "ʉː", label="sv u central rounded")

    def test_y_is_front_rounded(self):
        """<y> → /ʏ/ (short) and /yː/ (long) (e.g., *nytt*, *ny*)."""
        g = _grapheme(self._spec, "y")
        _assert_contains(g, "ʏ", "yː", label="sv y")

    def test_aa_ring(self):
        """<å> → /ɔ/ (short) and /oː/ (long) (e.g., *håll*, *år*)."""
        g = _grapheme(self._spec, "å")
        _assert_contains(g, "ɔ", "oː", label="sv å")

    def test_ae_umlaut(self):
        """<ä> → /ɛ/ (short) and /ɛː/ (long) (e.g., *ägg*, *äta*)."""
        g = _grapheme(self._spec, "ä")
        _assert_contains(g, "ɛ", "ɛː", label="sv ä")

    def test_oe_umlaut(self):
        """<ö> → /œ/ (short) and /øː/ (long) (e.g., *öppen*, *lös*)."""
        g = _grapheme(self._spec, "ö")
        _assert_contains(g, "œ", "øː", label="sv ö")

    # --- Consonants ---

    def test_g_palatal_before_front_vowels(self):
        """SWEDISH FEATURE: <g> is palatal /j/ before front vowels (e.g., *ge*, *gärna*)."""
        g = _grapheme(self._spec, "g")
        _assert_contains(g, "ɡ", "j", label="sv g palatalisation")

    def test_k_palatal_variant(self):
        """SWEDISH FEATURE: <k> is palatal /ɕ/ before front vowels (e.g., *kött*, *kär*)."""
        g = _grapheme(self._spec, "k")
        _assert_contains(g, "k", "ɕ", label="sv k palatalisation")

    def test_sk_sje_sound(self):
        """<sk> before front vowels → /ɧ/ (the sje-sound); elsewhere → /sk/."""
        g = _grapheme(self._spec, "sk")
        _assert_contains(g, "ɧ", "sk", label="sv sk")

    def test_sj_is_sje_sound(self):
        """<sj> → /ɧ/ (the Swedish sje-sound) in all positions (e.g., *sjö*, *sjunga*)."""
        _assert_first(_grapheme(self._spec, "sj"), "ɧ", label="sv sj")

    def test_tj_is_palatal(self):
        """<tj> → /ɕ/ (e.g., *tjugo*, *tjäna*)."""
        _assert_first(_grapheme(self._spec, "tj"), "ɕ", label="sv tj")

    def test_ch_is_palatal_or_postalveolar(self):
        """<ch> in Swedish loans → /ɕ/ or /ʃ/ (e.g., *chef*, *check*)."""
        g = _grapheme(self._spec, "ch")
        _assert_contains(g, "ɕ", label="sv ch includes ɕ")

    def test_w_is_v(self):
        """<w> in Swedish → /v/ (e.g., loanwords *whisky*, *watt*)."""
        _assert_first(_grapheme(self._spec, "w"), "v", label="sv w")

    def test_z_is_s(self):
        """<z> in Swedish → /s/ (e.g., *zebra*, *zink*) — no /z/ phoneme."""
        _assert_first(_grapheme(self._spec, "z"), "s", label="sv z")

    # --- Allophones ---

    def test_sje_sound_allophone(self):
        """The sje-sound /ɧ/ has complex allophonic variants including /ʂ/ and /x/."""
        a = _allophone(self._spec, "ɧ")
        assert a is not None, "sv: ɧ should be in allophone table"
        _assert_contains(a, "ɧ", label="sv allophone ɧ")

    def test_aspiration_p(self):
        """Voiceless stops are aspirated: /p/ → [pʰ] in onset."""
        a = _allophone(self._spec, "p")
        assert a is not None, "sv: p should be in allophone table"
        _assert_contains(a, "p", "pʰ", label="sv allophone p")

    def test_aspiration_t(self):
        """Voiceless stops are aspirated: /t/ → [tʰ] in onset."""
        a = _allophone(self._spec, "t")
        assert a is not None, "sv: t should be in allophone table"
        _assert_contains(a, "t", "tʰ", label="sv allophone t")

    def test_aspiration_k(self):
        """Voiceless stops are aspirated: /k/ → [kʰ] in onset."""
        a = _allophone(self._spec, "k")
        assert a is not None, "sv: k should be in allophone table"
        _assert_contains(a, "k", "kʰ", label="sv allophone k")


# ═══════════════════════════════════════════════════════════════════════════
# DANISH  (da)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestDanish:
    """Comprehensive accuracy tests for Danish (da).

    Danish is the most phonologically divergent of the mainland Scandinavian
    languages. Key features: widespread lenition (including the dental
    approximant [ð] from stop /d/), the stød (a laryngealisation superimposed
    on sonorants and voiced stops), a uvular /ʁ/, and /v/ from <w>.
    """

    LANGUAGE_CODE = "da"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the da LanguageSpec once for the entire class."""
        request.cls._spec = _load("da")

    # --- Registry ---

    def test_code(self):
        """The spec code must round-trip to da."""
        assert self._spec.code == "da"

    def test_family(self):
        """Danish is a North Germanic language."""
        assert self._spec.family == "Germanic"

    def test_script(self):
        """Danish uses the Latin script."""
        assert self._spec.script == "Latin"

    # --- Danish-specific vowel graphemes ---

    def test_ae_ligature(self):
        """<æ> → /ɛ/ (short) and /ɛː/ (long) (e.g., *æble*, *ær*)."""
        g = _grapheme(self._spec, "æ")
        _assert_contains(g, "ɛ", "ɛː", label="da æ")

    def test_oe_slashed(self):
        """<ø> → /ø/ (short) and /œ/ (open, e.g., unstressed) (e.g., *øje*, *rød*)."""
        g = _grapheme(self._spec, "ø")
        _assert_contains(g, "ø", "œ", label="da ø")

    def test_aa_ring(self):
        """<å> → /ɔ/ (short) and /ɔː/ (long) (e.g., *åbne*, *år*)."""
        g = _grapheme(self._spec, "å")
        _assert_contains(g, "ɔ", "ɔː", label="da å")

    # --- Consonants ---

    def test_r_is_uvular(self):
        """<r> in Danish → /ʁ/ (uvular fricative/approximant, often vocalised)."""
        _assert_first(_grapheme(self._spec, "r"), "ʁ", label="da r")

    def test_w_is_v(self):
        """<w> in Danish loanwords → /v/ (e.g., *whisky*, *watt*)."""
        _assert_first(_grapheme(self._spec, "w"), "v", label="da w")

    def test_z_is_s(self):
        """<z> in Danish → /s/ (no native /z/ phoneme)."""
        _assert_first(_grapheme(self._spec, "z"), "s", label="da z")

    def test_ch_ambiguous(self):
        """<ch> can be /ɕ/ (palatal, in loans from French) or /k/ (classical loans)."""
        g = _grapheme(self._spec, "ch")
        _assert_contains(g, "ɕ", label="da ch includes palatal ɕ")

    def test_ng_velar_nasal(self):
        """<ng> → /ŋ/ in Danish (e.g., *sang*, *lang*)."""
        _assert_first(_grapheme(self._spec, "ng"), "ŋ", label="da ng")

    def test_nk_cluster(self):
        """<nk> → /ŋk/ in Danish (e.g., *bank*, *tanke*)."""
        _assert_first(_grapheme(self._spec, "nk"), "ŋk", label="da nk")

    def test_sk_and_sj_palatal(self):
        """<sk>/<sj> before front vowels → /ɕ/ in Danish (palatal sibilant)."""
        g_sk = _grapheme(self._spec, "sk")
        _assert_contains(g_sk, "ɕ", label="da sk includes ɕ")

    def test_kj_palatal(self):
        """<kj> → /ɕ/ in Danish (e.g., *kær*, *kærlighed* via kj- spelling)."""
        _assert_first(_grapheme(self._spec, "kj"), "ɕ", label="da kj")

    def test_sj_palatal(self):
        """<sj> → /ɕ/ in Danish (e.g., *sjel*, *sjov*)."""
        _assert_first(_grapheme(self._spec, "sj"), "ɕ", label="da sj")

    # --- Allophones (lenition and stød) ---

    def test_stop_b_devoiced_allophone(self):
        """DANISH LENITION: /b/ can surface as devoiced lenis [b̥]."""
        a = _allophone(self._spec, "b")
        assert a is not None, "da: b should be in allophone table"
        _assert_contains(a, "b", "b̥", label="da allophone b lenition")

    def test_stop_d_lenition_to_dental_approximant(self):
        """DANISH LENITION: /d/ can surface as dental approximant [ð] or devoiced [d̥]."""
        a = _allophone(self._spec, "d")
        assert a is not None, "da: d should be in allophone table"
        _assert_contains(a, "d", "ð", label="da allophone d→ð lenition")

    def test_stop_d_devoiced_allophone(self):
        """DANISH LENITION: /d/ can surface as devoiced [d̥]."""
        a = _allophone(self._spec, "d")
        assert a is not None, "da: d should be in allophone table"
        _assert_contains(a, "d̥", label="da allophone d devoiced variant")

    def test_stop_g_devoiced_allophone(self):
        """DANISH LENITION: /ɡ/ can surface as devoiced lenis [ɡ̊]."""
        a = _allophone(self._spec, "ɡ")
        assert a is not None, "da: ɡ should be in allophone table"
        _assert_contains(a, "ɡ", "ɡ̊", label="da allophone ɡ devoicing")

    def test_aspiration_p(self):
        """Danish voiceless stops aspirate: /p/ → [pʰ]."""
        a = _allophone(self._spec, "p")
        assert a is not None, "da: p should be in allophone table"
        _assert_contains(a, "p", "pʰ", label="da allophone p aspiration")

    def test_aspiration_t(self):
        """Danish voiceless stops aspirate: /t/ → [tʰ]."""
        a = _allophone(self._spec, "t")
        assert a is not None, "da: t should be in allophone table"
        _assert_contains(a, "t", "tʰ", label="da allophone t aspiration")

    def test_aspiration_k(self):
        """Danish voiceless stops aspirate: /k/ → [kʰ]."""
        a = _allophone(self._spec, "k")
        assert a is not None, "da: k should be in allophone table"
        _assert_contains(a, "k", "kʰ", label="da allophone k aspiration")


# ═══════════════════════════════════════════════════════════════════════════
# NORWEGIAN BOKMÅL  (nb)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestNorwegianBokmal:
    """Accuracy tests for Norwegian Bokmål (nb).

    Norwegian Bokmål is closely related to Danish and inherits much of the
    Danish phonological inventory. Its most distinctive feature at the phoneme
    level is the set of retroflexion assimilation rules: the clusters rn, rd,
    rt, rs, rl trigger retroflex realisations of the following consonant
    (analogous to Old Norse *r*-sandhi).
    """

    LANGUAGE_CODE = "nb"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the nb LanguageSpec once for the entire class."""
        request.cls._spec = _load("nb")

    def test_code(self):
        """The spec code must round-trip to nb."""
        assert self._spec.code == "nb"

    def test_family(self):
        """Norwegian Bokmål is a North Germanic language."""
        assert self._spec.family == "Germanic"

    def test_parent_is_norwegian(self):
        """nb inherits from 'no' (generic Norwegian), not Danish directly."""
        assert self._spec.parent == "no"

    def test_rn_retroflex_nasal(self):
        """NORWEGIAN RETROFLEXION: cluster <rn> → retroflex nasal /ɳ/."""
        a = _allophone(self._spec, "rn")
        assert a is not None, "nb: rn should be in allophone table"
        _assert_contains(a, "ɳ", label="nb allophone rn→ɳ")

    def test_rd_retroflex_stop(self):
        """NORWEGIAN RETROFLEXION: cluster <rd> → retroflex stop /ɖ/."""
        a = _allophone(self._spec, "rd")
        assert a is not None, "nb: rd should be in allophone table"
        _assert_contains(a, "ɖ", label="nb allophone rd→ɖ")

    def test_rt_retroflex_stop(self):
        """NORWEGIAN RETROFLEXION: cluster <rt> → retroflex stop /ʈ/."""
        a = _allophone(self._spec, "rt")
        assert a is not None, "nb: rt should be in allophone table"
        _assert_contains(a, "ʈ", label="nb allophone rt→ʈ")

    def test_rs_retroflex_fricative(self):
        """NORWEGIAN RETROFLEXION: cluster <rs> → retroflex fricative /ʂ/."""
        a = _allophone(self._spec, "rs")
        assert a is not None, "nb: rs should be in allophone table"
        _assert_contains(a, "ʂ", label="nb allophone rs→ʂ")

    def test_rl_retroflex_lateral(self):
        """NORWEGIAN RETROFLEXION: cluster <rl> → retroflex lateral /ɭ/."""
        a = _allophone(self._spec, "rl")
        assert a is not None, "nb: rl should be in allophone table"
        _assert_contains(a, "ɭ", label="nb allophone rl→ɭ")

    def test_r_alveolar_or_flap(self):
        """Norwegian /r/ is alveolar trill /r/ or flap /ɾ/ (not Danish uvular /ʁ/)."""
        a = _allophone(self._spec, "r")
        assert a is not None, "nb: r should be in allophone table"
        _assert_contains(a, "r", "ɾ", label="nb allophone r apical")


# ═══════════════════════════════════════════════════════════════════════════
# ICELANDIC  (is)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestIcelandic:
    """Comprehensive accuracy tests for Icelandic (is).

    Icelandic is highly conservative, preserving features lost in other
    Germanic languages: the interdental fricatives /θ/ (voiceless) and /ð/
    (voiced), a fully aspirated vs unaspirated stop opposition (analogous to
    Scandinavian but more prominent), distinct diphthongs /au/ and /øɪ/, and
    unusual grapheme-to-phoneme mappings for the accented vowels.
    """

    LANGUAGE_CODE = "is"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the is LanguageSpec once for the entire class."""
        request.cls._spec = _load("is")

    # --- Registry ---

    def test_code(self):
        """The spec code must round-trip to is."""
        assert self._spec.code == "is"

    def test_family(self):
        """Icelandic is a North Germanic language."""
        assert self._spec.family == "Germanic"

    def test_script(self):
        """Icelandic uses the Latin script (with <ð>, <þ>, <á>, <é>, etc.)."""
        assert self._spec.script == "Latin"

    # --- Accented vowel mappings ---

    def test_a_acute_is_diphthong_au(self):
        """ICELANDIC FEATURE: <á> → /au/ (not a long /aː/!). E.g., *bát* = [bauːt]."""
        _assert_first(_grapheme(self._spec, "á"), "au", label="is á→au")

    def test_e_acute_is_palatal_diphthong(self):
        """ICELANDIC FEATURE: <é> → /jɛ/ (e.g., *vér* = [vjɛːr])."""
        _assert_first(_grapheme(self._spec, "é"), "jɛ", label="is é→jɛ")

    def test_i_acute_is_long_high(self):
        """<í> → /iː/ (long high front vowel, e.g., *líf*)."""
        _assert_first(_grapheme(self._spec, "í"), "iː", label="is í")

    def test_o_acute_is_diphthong(self):
        """Icelandic ó is a diphthong [ou] (Árnason 2011), not a monophthong [oː]."""
        _assert_first(_grapheme(self._spec, "ó"), "ou", label="is ó")

    def test_u_acute_is_long_high(self):
        """<ú> → /uː/ (e.g., *þú*, *búa*)."""
        _assert_first(_grapheme(self._spec, "ú"), "uː", label="is ú")

    def test_y_acute_equals_i_acute(self):
        """<ý> → /iː/ (homophonous with <í>, e.g., *lýsa*)."""
        _assert_first(_grapheme(self._spec, "ý"), "iː", label="is ý→iː")

    def test_o_umlaut(self):
        """<ö> → /œ/ (short open front rounded, e.g., *önd*, *föt*)."""
        _assert_first(_grapheme(self._spec, "ö"), "œ", label="is ö")

    # --- Diphthongs ---

    def test_ei_diphthong(self):
        """<ei> → /eɪ/ (e.g., *ein*, *nei*)."""
        _assert_first(_grapheme(self._spec, "ei"), "eɪ", label="is ei")

    def test_ey_equals_ei(self):
        """<ey> → /eɪ/ (homophonous with <ei>, e.g., *ey*, *leyna*)."""
        _assert_first(_grapheme(self._spec, "ey"), "eɪ", label="is ey→eɪ")

    def test_au_is_front_rounded_diphthong(self):
        """ICELANDIC FEATURE: <au> → /øɪ/ (e.g., *auga*, *laug*) — not /aʊ/!"""
        _assert_first(_grapheme(self._spec, "au"), "øɪ", label="is au→øɪ")

    # --- Aspirated stops ---

    def test_p_aspirated(self):
        """ICELANDIC FEATURE: unvoiced /p/ maps to aspirated [pʰ] as primary allophone."""
        a = _allophone(self._spec, "pʰ")
        assert a is not None, "is: pʰ should be in allophone table"
        _assert_contains(a, "pʰ", label="is allophone pʰ")

    def test_t_aspirated(self):
        """ICELANDIC FEATURE: unvoiced /t/ maps to aspirated [tʰ] as primary allophone."""
        a = _allophone(self._spec, "tʰ")
        assert a is not None, "is: tʰ should be in allophone table"
        _assert_contains(a, "tʰ", label="is allophone tʰ")

    def test_k_aspirated(self):
        """ICELANDIC FEATURE: unvoiced /k/ maps to aspirated [kʰ] as primary allophone."""
        a = _allophone(self._spec, "kʰ")
        assert a is not None, "is: kʰ should be in allophone table"
        _assert_contains(a, "kʰ", label="is allophone kʰ")

    # --- Preserved interdentals ---

    def test_theta_preserved(self):
        """ICELANDIC CONSERVATISM: /θ/ is preserved (unlike in mainland Scandinavian)."""
        a = _allophone(self._spec, "θ")
        assert a is not None, "is: θ should be in allophone table (preserved from Proto-Germanic)"
        _assert_contains(a, "θ", label="is allophone θ")

    def test_eth_preserved(self):
        """ICELANDIC CONSERVATISM: /ð/ is preserved as a distinct phoneme."""
        a = _allophone(self._spec, "ð")
        assert a is not None, "is: ð should be in allophone table"
        _assert_contains(a, "ð", label="is allophone ð")

    def test_f_includes_voiced_variant(self):
        """ICELANDIC: /f/ can surface as voiced /v/ intervocalically (e.g., *of* → [ɔv])."""
        a = _allophone(self._spec, "f")
        assert a is not None, "is: f should be in allophone table"
        _assert_contains(a, "f", "v", label="is allophone f→v")


# ═══════════════════════════════════════════════════════════════════════════
# West Frisian (fy)
# ═══════════════════════════════════════════════════════════════════════════


class TestWestFrisian:
    """Accuracy tests for West Frisian (fy).

    West Frisian is an Anglo-Frisian language spoken in Fryslân (Netherlands).
    Key features: breaking diphthongs (/iə/, /ɪə/, /oə/), final devoicing,
    voiced velar stop /ɡ/ (not fricative), rich vowel system with circumflex
    orthography (â, ê, ô, û).
    """

    LANGUAGE_CODE = "fy"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the fy LanguageSpec once for the entire class."""
        request.cls._spec = _load("fy")

    # --- Registry ---

    def test_code(self):
        """The spec code must be 'fy'."""
        assert self._spec.code == "fy"

    def test_name(self):
        """Language name is West Frisian."""
        assert self._spec.name == "West Frisian"

    def test_family(self):
        """West Frisian belongs to the Germanic family."""
        assert self._spec.family == "Germanic"

    def test_script(self):
        """West Frisian uses the Latin script."""
        assert self._spec.script == "Latin"

    # --- Short vowels ---

    def test_a_short(self):
        """<a> → /ɑ/ (e.g., *bal*, *kat*)."""
        _assert_first(_grapheme(self._spec, "a"), "ɑ", label="fy a")

    def test_e_short(self):
        """<e> → /ɛ/ or /ə/ (stressed vs unstressed)."""
        g = _grapheme(self._spec, "e")
        _assert_contains(g, "ɛ", "ə", label="fy e")

    def test_i_short(self):
        """<i> → /ɪ/ (e.g., *bit*, *kin*)."""
        _assert_first(_grapheme(self._spec, "i"), "ɪ", label="fy i")

    def test_o_short(self):
        """<o> → /ɔ/ (e.g., *bok*, *hok*)."""
        _assert_first(_grapheme(self._spec, "o"), "ɔ", label="fy o")

    def test_u_front_rounded(self):
        """<u> → /ø/ in Frisian (front rounded, unlike Dutch /ʏ/)."""
        _assert_first(_grapheme(self._spec, "u"), "ø", label="fy u")

    def test_y_is_high_front(self):
        """<y> → /i/ in Frisian orthography (not a consonant)."""
        _assert_first(_grapheme(self._spec, "y"), "i", label="fy y")

    # --- Long vowels ---

    def test_aa_long(self):
        """<aa> → /aː/ (e.g., *baas*, *kaas*)."""
        _assert_first(_grapheme(self._spec, "aa"), "aː", label="fy aa")

    def test_ee_long(self):
        """<ee> → /eː/ (e.g., *been*, *steen*)."""
        _assert_first(_grapheme(self._spec, "ee"), "eː", label="fy ee")

    def test_oo_long(self):
        """<oo> → /oː/ (e.g., *boat*, *moan*)."""
        _assert_first(_grapheme(self._spec, "oo"), "oː", label="fy oo")

    def test_uu_long(self):
        """<uu> → /yː/ (e.g., *mûne* 'moon')."""
        _assert_first(_grapheme(self._spec, "uu"), "yː", label="fy uu")

    # --- Circumflex vowels (distinctive Frisian) ---

    def test_a_circumflex(self):
        """<â> → /ɔː/ — unique Frisian circumflex vowel."""
        _assert_first(_grapheme(self._spec, "â"), "ɔː", label="fy â")

    def test_e_circumflex(self):
        """<ê> → /ɛː/ — long open-mid front."""
        _assert_first(_grapheme(self._spec, "ê"), "ɛː", label="fy ê")

    def test_o_circumflex(self):
        """<ô> → /oː/ — long close-mid back."""
        _assert_first(_grapheme(self._spec, "ô"), "oː", label="fy ô")

    def test_u_circumflex(self):
        """<û> → /uː/ — long close back rounded (hûs [huːs]); ú is /yː/."""
        _assert_first(_grapheme(self._spec, "û"), "uː", label="fy û")

    # --- Breaking diphthongs (hallmark of Frisian) ---

    def test_ie_breaking(self):
        """<ie> → /iə/ — centring diphthong, NOT Dutch /iː/."""
        _assert_first(_grapheme(self._spec, "ie"), "iə", label="fy ie")

    def test_ea_breaking(self):
        """<ea> → /ɪə/ — centring diphthong."""
        _assert_first(_grapheme(self._spec, "ea"), "ɪə", label="fy ea")

    def test_oa_breaking(self):
        """<oa> → /oə/ — centring diphthong."""
        _assert_first(_grapheme(self._spec, "oa"), "oə", label="fy oa")

    # --- Other vowel digraphs ---

    def test_oe_high_back(self):
        """<oe> → /uː/ (as in Dutch)."""
        _assert_first(_grapheme(self._spec, "oe"), "uː", label="fy oe")

    # --- Diphthongs ---

    def test_ei_diphthong(self):
        """<ei> → /ɛi/."""
        _assert_first(_grapheme(self._spec, "ei"), "ɛi", label="fy ei")

    def test_au_diphthong(self):
        """<au> → /ɔu/."""
        _assert_first(_grapheme(self._spec, "au"), "ɔu", label="fy au")

    def test_ui_diphthong(self):
        """<ui> → /øy/."""
        _assert_first(_grapheme(self._spec, "ui"), "øy", label="fy ui")

    # --- Consonants ---

    def test_g_is_voiced_stop(self):
        """<g> includes voiced stop /ɡ/ — NOT the Dutch fricative /ɣ/."""
        g = _grapheme(self._spec, "g")
        _assert_contains(g, "ɡ", label="fy g")

    def test_ch_voiceless_velar(self):
        """<ch> → /x/ (e.g., *acht*, *nacht*)."""
        _assert_first(_grapheme(self._spec, "ch"), "x", label="fy ch")

    def test_sj_postalveolar(self):
        """<sj> → /ʃ/ (e.g., *sjen* 'to see')."""
        _assert_first(_grapheme(self._spec, "sj"), "ʃ", label="fy sj")

    def test_tj_affricate(self):
        """<tj> → /tʃ/ (e.g., *tsjerke* 'church')."""
        _assert_first(_grapheme(self._spec, "tj"), "tʃ", label="fy tj")

    def test_w_labiodental(self):
        """<w> → /ʋ/ (primary) or /w/ — labiodental approximant."""
        g = _grapheme(self._spec, "w")
        _assert_contains(g, "ʋ", label="fy w")

    def test_h_glottal(self):
        """<h> → /h/ (not breathy Dutch /ɦ/)."""
        _assert_first(_grapheme(self._spec, "h"), "h", label="fy h")

    def test_ng_velar_nasal(self):
        """<ng> → /ŋ/."""
        _assert_first(_grapheme(self._spec, "ng"), "ŋ", label="fy ng")

    # --- Final devoicing (positional) ---

    def test_b_final_devoicing(self):
        """<b> → /p/ word-finally (final devoicing)."""
        p = _positional(self._spec, "b", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "p", label="fy b word_final")

    def test_d_final_devoicing(self):
        """<d> → /t/ word-finally."""
        p = _positional(self._spec, "d", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "t", label="fy d word_final")

    def test_g_final_devoicing(self):
        """<g> → /x/ word-finally."""
        p = _positional(self._spec, "g", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "x", label="fy g word_final")

    def test_v_final_devoicing(self):
        """<v> → /f/ word-finally."""
        p = _positional(self._spec, "v", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "f", label="fy v word_final")

    def test_z_final_devoicing(self):
        """<z> → /s/ word-finally."""
        p = _positional(self._spec, "z", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "s", label="fy z word_final")

    # --- Allophones ---

    def test_allophone_r(self):
        """Frisian /r/ can surface as alveolar trill [r] or tap [ɾ]."""
        a = _allophone(self._spec, "r")
        _assert_contains(a, "r", "ɾ", label="fy allophone r")

    def test_allophone_b_devoicing(self):
        """/b/ → [p] in coda (final devoicing)."""
        a = _allophone(self._spec, "b")
        _assert_contains(a, "b", "p", label="fy allophone b")

    # --- Ancestry ---

    def test_ancestry_old_frisian(self):
        """West Frisian descends from Old Frisian."""
        codes = [getattr(a, "code", None) or (a.get("code") if isinstance(a, dict) else str(a)) for a in self._spec.ancestors]
        assert "ofs" in codes, f"fy: expected 'ofs' in ancestors, got {codes}"

    def test_ancestry_dutch_adstrate(self):
        """Dutch is a significant adstrate for West Frisian."""
        codes = [getattr(a, "code", None) or (a.get("code") if isinstance(a, dict) else str(a)) for a in self._spec.ancestors]
        assert "nl" in codes, f"fy: expected 'nl' in ancestors, got {codes}"

    # --- Key isoglosses vs Dutch ---

    def test_isogloss_g_not_fricative(self):
        """FRISIAN vs DUTCH: Frisian <g> has a stop /ɡ/ default, Dutch has fricative /ɣ/."""
        g = _grapheme(self._spec, "g")
        _assert_first(g, "ɡ", label="fy g is stop not fricative")

    def test_isogloss_breaking_diphthongs(self):
        """FRISIAN vs DUTCH: breaking diphthongs /iə/, /ɪə/, /oə/ are absent from Dutch."""
        ie = _grapheme(self._spec, "ie")
        _assert_first(ie, "iə", label="fy breaking ie≠Dutch iː")

    def test_isogloss_h_not_breathy(self):
        """FRISIAN vs DUTCH: Frisian /h/ is plain glottal [h], Dutch is breathy [ɦ]."""
        _assert_first(_grapheme(self._spec, "h"), "h", label="fy h vs Dutch ɦ")


# ═══════════════════════════════════════════════════════════════════════════
# North Frisian (frr)
# ═══════════════════════════════════════════════════════════════════════════


def _ancestor_codes(spec) -> list:
    """Extract ancestor codes from a spec, handling both dict and object forms."""
    return [getattr(a, "code", None) or (a.get("code") if isinstance(a, dict) else str(a))
            for a in spec.ancestors]


class TestNorthFrisian:
    """Accuracy tests for North Frisian (frr).

    Spoken in Schleswig-Holstein, Germany. ~10 dialect groups across islands
    and mainland. Features centring diphthongs, final devoicing, voiced /ɡ/.
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("frr")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "frr"

    def test_name(self):
        assert self._spec.name == "North Frisian"

    def test_family(self):
        assert self._spec.family == "Germanic"

    # --- Vowels ---

    def test_a_short(self):
        _assert_first(_grapheme(self._spec, "a"), "a", label="frr a")

    def test_ae_umlaut(self):
        """<ä> → /ɛ/ (umlauted a)."""
        _assert_first(_grapheme(self._spec, "ä"), "ɛ", label="frr ä")

    def test_oe_umlaut(self):
        """<ö> → /œ/ (front rounded)."""
        _assert_first(_grapheme(self._spec, "ö"), "œ", label="frr ö")

    def test_ue_umlaut(self):
        """<ü> → /ʏ/ (front rounded)."""
        _assert_first(_grapheme(self._spec, "ü"), "ʏ", label="frr ü")

    def test_long_oo(self):
        _assert_first(_grapheme(self._spec, "oo"), "oː", label="frr oo")

    def test_long_oeoe(self):
        """<öö> → /øː/ (long front rounded)."""
        _assert_first(_grapheme(self._spec, "öö"), "øː", label="frr öö")

    def test_long_ueue(self):
        """<üü> → /yː/ (long close front rounded)."""
        _assert_first(_grapheme(self._spec, "üü"), "yː", label="frr üü")

    # --- Centring diphthongs (shared Frisian feature) ---

    def test_ia_centring(self):
        """<ia> → /iə/ centring diphthong."""
        _assert_first(_grapheme(self._spec, "ia"), "iə", label="frr ia")

    def test_ua_centring(self):
        """<ua> → /uə/ centring diphthong."""
        _assert_first(_grapheme(self._spec, "ua"), "uə", label="frr ua")

    def test_uea_centring(self):
        """<üa> → /yə/ centring diphthong (front rounded)."""
        _assert_first(_grapheme(self._spec, "üa"), "yə", label="frr üa")

    # --- Consonants ---

    def test_g_voiced_stop(self):
        """<g> → /ɡ/ (voiced velar stop, as in all Frisian)."""
        _assert_first(_grapheme(self._spec, "g"), "ɡ", label="frr g")

    def test_ch_voiceless_velar(self):
        _assert_first(_grapheme(self._spec, "ch"), "x", label="frr ch")

    def test_sch_postalveolar(self):
        _assert_first(_grapheme(self._spec, "sch"), "ʃ", label="frr sch")

    def test_tj_affricate(self):
        _assert_first(_grapheme(self._spec, "tj"), "tʃ", label="frr tj")

    def test_dj_affricate(self):
        _assert_first(_grapheme(self._spec, "dj"), "dʒ", label="frr dj")

    # --- Final devoicing ---

    def test_b_final_devoicing(self):
        p = _positional(self._spec, "b", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "p", label="frr b word_final")

    def test_d_final_devoicing(self):
        p = _positional(self._spec, "d", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "t", label="frr d word_final")

    def test_g_final_devoicing(self):
        p = _positional(self._spec, "g", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "k", label="frr g word_final")

    # --- Ancestry ---

    def test_ancestry_old_frisian(self):
        assert "ofs" in _ancestor_codes(self._spec), "frr should descend from Old Frisian"

    def test_ancestry_danish_adstrate(self):
        assert "da" in _ancestor_codes(self._spec), "frr should have Danish adstrate"


# ═══════════════════════════════════════════════════════════════════════════
# Saterland Frisian (stq)
# ═══════════════════════════════════════════════════════════════════════════


class TestSaterlandFrisian:
    """Accuracy tests for Saterland Frisian (stq).

    Last surviving East Frisian dialect. ~1,000–2,500 speakers in Lower Saxony.
    Most conservative Frisian variety.
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("stq")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "stq"

    def test_name(self):
        assert self._spec.name == "Saterland Frisian"

    def test_family(self):
        assert self._spec.family == "Germanic"

    # --- Vowels ---

    def test_a_short(self):
        _assert_first(_grapheme(self._spec, "a"), "a", label="stq a")

    def test_ae_umlaut(self):
        _assert_first(_grapheme(self._spec, "ä"), "ɛ", label="stq ä")

    def test_aeae_long(self):
        """<ää> → /ɛː/ — distinct from <ee> /eː/ (conservative feature)."""
        _assert_first(_grapheme(self._spec, "ää"), "ɛː", label="stq ää")

    def test_ee_long(self):
        _assert_first(_grapheme(self._spec, "ee"), "eː", label="stq ee")

    def test_oeoe_long(self):
        _assert_first(_grapheme(self._spec, "öö"), "øː", label="stq öö")

    def test_ueue_long(self):
        _assert_first(_grapheme(self._spec, "üü"), "yː", label="stq üü")

    # --- Centring diphthongs ---

    def test_ia_centring(self):
        _assert_first(_grapheme(self._spec, "ia"), "iə", label="stq ia")

    def test_oa_centring(self):
        _assert_first(_grapheme(self._spec, "oa"), "oə", label="stq oa")

    def test_ua_centring(self):
        _assert_first(_grapheme(self._spec, "ua"), "uə", label="stq ua")

    # --- Consonants ---

    def test_g_voiced_stop(self):
        _assert_first(_grapheme(self._spec, "g"), "ɡ", label="stq g")

    def test_ch_voiceless_velar(self):
        _assert_first(_grapheme(self._spec, "ch"), "x", label="stq ch")

    def test_sch_postalveolar(self):
        _assert_first(_grapheme(self._spec, "sch"), "ʃ", label="stq sch")

    def test_sp_initial(self):
        """<sp> → /ʃp/ (shared with Low German)."""
        _assert_first(_grapheme(self._spec, "sp"), "ʃp", label="stq sp")

    def test_st_initial(self):
        """<st> → /ʃt/ (shared with Low German)."""
        _assert_first(_grapheme(self._spec, "st"), "ʃt", label="stq st")

    # --- Final devoicing ---

    def test_b_final_devoicing(self):
        p = _positional(self._spec, "b", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "p", label="stq b word_final")

    def test_d_final_devoicing(self):
        p = _positional(self._spec, "d", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "t", label="stq d word_final")

    def test_g_final_devoicing(self):
        p = _positional(self._spec, "g", GraphemePosition.WORD_FINAL)
        _assert_contains(p, "k", label="stq g word_final")

    # --- Positional s voicing ---

    def test_s_initial_voiced(self):
        """<s> → /z/ word-initially (characteristic of Saterland Frisian)."""
        p = _positional(self._spec, "s", GraphemePosition.WORD_INITIAL)
        _assert_contains(p, "z", label="stq s word_initial")

    # --- Ancestry ---

    def test_ancestry_old_frisian(self):
        assert "ofs" in _ancestor_codes(self._spec), "stq should descend from Old Frisian"

    def test_ancestry_low_german_adstrate(self):
        assert "nds" in _ancestor_codes(self._spec), "stq should have Low German adstrate"


# ═══════════════════════════════════════════════════════════════════════════
# Old Frisian (ofs)
# ═══════════════════════════════════════════════════════════════════════════


class TestOldFrisian:
    """Accuracy tests for Old Frisian (ofs).

    Ancestor of all modern Frisian languages. Known from legal manuscripts
    (~1150–1550 CE). Anglo-Frisian sub-branch of Ingvaeonic.
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("ofs")

    # --- Registry ---

    def test_code(self):
        assert self._spec.code == "ofs"

    def test_name(self):
        assert self._spec.name == "Old Frisian"

    def test_family(self):
        assert self._spec.family == "Germanic"

    # --- Vowels ---

    def test_a_short(self):
        _assert_first(_grapheme(self._spec, "a"), "a", label="ofs a")

    def test_e_short(self):
        g = _grapheme(self._spec, "e")
        _assert_contains(g, "e", label="ofs e")

    def test_long_a(self):
        _assert_first(_grapheme(self._spec, "ā"), "aː", label="ofs ā")

    def test_long_e(self):
        _assert_first(_grapheme(self._spec, "ē"), "eː", label="ofs ē")

    def test_long_i(self):
        _assert_first(_grapheme(self._spec, "ī"), "iː", label="ofs ī")

    def test_long_o(self):
        _assert_first(_grapheme(self._spec, "ō"), "oː", label="ofs ō")

    def test_long_u(self):
        _assert_first(_grapheme(self._spec, "ū"), "uː", label="ofs ū")

    # --- Consonants ---

    def test_thorn(self):
        """<þ> → /θ/ ~ /ð/ (interdental fricative, preserved from PGmc)."""
        g = _grapheme(self._spec, "þ")
        _assert_contains(g, "θ", label="ofs þ")

    def test_eth(self):
        """<ð> → /ð/ ~ /θ/."""
        g = _grapheme(self._spec, "ð")
        _assert_contains(g, "ð", label="ofs ð")

    def test_f_voicing(self):
        """<f> → /f/ ~ /v/ (voiced intervocalically)."""
        g = _grapheme(self._spec, "f")
        _assert_contains(g, "f", "v", label="ofs f")

    def test_s_voicing(self):
        """<s> → /s/ ~ /z/ (voiced intervocalically)."""
        g = _grapheme(self._spec, "s")
        _assert_contains(g, "s", "z", label="ofs s")

    def test_palatalisation_ts(self):
        """Old Frisian palatalisation: <ts> → /ts/ (PGmc *k → ts before front V)."""
        _assert_first(_grapheme(self._spec, "ts"), "ts", label="ofs ts")

    def test_geminates(self):
        """Geminate consonants are distinctive in Old Frisian."""
        _assert_first(_grapheme(self._spec, "pp"), "pː", label="ofs pp")
        _assert_first(_grapheme(self._spec, "tt"), "tː", label="ofs tt")
        _assert_first(_grapheme(self._spec, "kk"), "kː", label="ofs kk")

    # --- Positional ---

    def test_f_intervocalic_voicing(self):
        p = _positional(self._spec, "f", GraphemePosition.INTERVOCALIC)
        _assert_contains(p, "v", label="ofs f intervocalic")

    def test_th_intervocalic_voicing(self):
        p = _positional(self._spec, "th", GraphemePosition.INTERVOCALIC)
        _assert_contains(p, "ð", label="ofs th intervocalic")

    # --- Ancestry ---

    def test_ancestry_ingvaeonic(self):
        assert "gem-x-ingvaeonic" in _ancestor_codes(self._spec), \
            "ofs should descend from Proto-Ingvaeonic"
