"""Per-language accuracy tests for Celtic languages.

Covers: Welsh (cy), Irish (ga), Scottish Gaelic (gd), Breton (br), Manx (gv), Cornish (kw)

Run with:
    pytest tests/test_celtic.py -v --tb=short
    pytest tests/test_celtic.py -v -m linguistic --tb=short
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
    """Load a LanguageSpec, skipping the test if the language code is unavailable."""
    try:
        return orthography2ipa.get(code)
    except Exception as exc:
        pytest.skip(f"{code!r} not available: {exc}")


def _grapheme(spec, grapheme: str) -> list:
    """Return the grapheme→IPA list from the fully inherited grapheme table."""
    return spec.graphemes.get(grapheme, [])


def _allophone(spec, phoneme: str):
    """Return the allophone surface-realisation list for a canonical phoneme."""
    return spec.allophones.get(phoneme)


def _positional(spec, grapheme: str, position: GraphemePosition):
    """Resolve a grapheme→IPA list for a specific positional context."""
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
    """Assert that the most-common IPA realisation (index 0) matches *expected*."""
    assert values is not None, f"{label}: mapping is absent"
    assert values[0] == expected, (
        f"{label}: expected first={expected!r}, got {values[0]!r}"
    )


def _assert_null(spec, grapheme: str) -> None:
    """Assert that *grapheme* is absent or explicitly nulled in the grapheme table."""
    result = spec.graphemes.get(grapheme, _SENTINEL)
    assert result is _SENTINEL or result is None, (
        f"grapheme {grapheme!r} should be absent/null, got {result!r}"
    )


def _assert_allophone_null(spec, phoneme: str) -> None:
    """Assert that *phoneme* is absent or explicitly nulled in the allophone table."""
    result = spec.allophones.get(phoneme, _SENTINEL)
    assert result is _SENTINEL or result is None, (
        f"allophone {phoneme!r} should be absent/null, got {result!r}"
    )


# ═══════════════════════════════════════════════════════════════════════════
# Welsh (cy)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestWelsh:
    """Accuracy tests for Welsh (cy).

    Welsh is a Brythonic Celtic language with a highly regular orthography.
    Critical features include the f→/v/ mapping (not /f/!), the voiceless
    lateral fricative ⟨ll⟩→/ɬ/, aspirated stop allophones, and a rich
    system of circumflex-marked long vowels.
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Welsh LanguageSpec once for the whole class."""
        request.cls.spec = _load("cy")

    # ── Vowels ──────────────────────────────────────────────────────────────

    def test_a_maps_to_short_a(self):
        """Plain ⟨a⟩ should map to short /a/."""
        _assert_first(_grapheme(self.spec, "a"), "a", label="cy:a")

    def test_e_maps_to_open_mid_front(self):
        """Plain ⟨e⟩ should map to /ɛ/ (open-mid front unrounded)."""
        _assert_first(_grapheme(self.spec, "e"), "ɛ", label="cy:e")

    def test_i_maps_to_near_close_front(self):
        """Plain ⟨i⟩ should map to /ɪ/ (near-close near-front)."""
        _assert_first(_grapheme(self.spec, "i"), "ɪ", label="cy:i")

    def test_o_maps_to_open_mid_back(self):
        """Plain ⟨o⟩ should map to /ɔ/ (open-mid back rounded)."""
        _assert_first(_grapheme(self.spec, "o"), "ɔ", label="cy:o")

    def test_u_includes_central_unrounded(self):
        """⟨u⟩ in Welsh maps to /ɨ/ (central unrounded) as primary realisation."""
        vals = _grapheme(self.spec, "u")
        _assert_contains(vals, "ɨ", label="cy:u")

    def test_u_secondary_includes_close_front(self):
        """⟨u⟩ also has /i/ as a southern Welsh variant."""
        vals = _grapheme(self.spec, "u")
        _assert_contains(vals, "i", label="cy:u secondary")

    def test_w_as_vowel_includes_near_close_back(self):
        """⟨w⟩ can be a vowel /ʊ/ (near-close back rounded) in Welsh."""
        vals = _grapheme(self.spec, "w")
        _assert_contains(vals, "ʊ", label="cy:w vowel")

    def test_w_as_consonant_includes_approximant(self):
        """⟨w⟩ can also be the labio-velar approximant /w/."""
        vals = _grapheme(self.spec, "w")
        _assert_contains(vals, "w", label="cy:w consonant")

    def test_y_includes_schwa(self):
        """⟨y⟩ in unstressed position maps to /ə/ (schwa)."""
        vals = _grapheme(self.spec, "y")
        _assert_contains(vals, "ə", label="cy:y schwa")

    def test_y_includes_central_unrounded(self):
        """⟨y⟩ in stressed monosyllables maps to /ɨ/ (central unrounded)."""
        vals = _grapheme(self.spec, "y")
        _assert_contains(vals, "ɨ", label="cy:y stressed")

    def test_circumflex_a_gives_long_vowel(self):
        """⟨â⟩ (a with circumflex) should map to the long vowel /aː/."""
        _assert_first(_grapheme(self.spec, "â"), "aː", label="cy:â")

    def test_circumflex_e_gives_long_vowel(self):
        """⟨ê⟩ should map to /eː/ (close-mid front long)."""
        _assert_first(_grapheme(self.spec, "ê"), "eː", label="cy:ê")

    def test_circumflex_i_gives_long_vowel(self):
        """⟨î⟩ should map to /iː/ (close front long)."""
        _assert_first(_grapheme(self.spec, "î"), "iː", label="cy:î")

    def test_circumflex_o_gives_long_vowel(self):
        """⟨ô⟩ should map to /oː/ (close-mid back long)."""
        _assert_first(_grapheme(self.spec, "ô"), "oː", label="cy:ô")

    def test_circumflex_u_gives_long_central(self):
        """⟨û⟩ should map to /ɨː/ (long central unrounded)."""
        _assert_first(_grapheme(self.spec, "û"), "ɨː", label="cy:û")

    def test_circumflex_w_gives_long_close_back(self):
        """⟨ŵ⟩ should map to /uː/ (long close back rounded)."""
        _assert_first(_grapheme(self.spec, "ŵ"), "uː", label="cy:ŵ")

    def test_circumflex_y_gives_long_schwa(self):
        """⟨ŷ⟩ should map to /əː/ (long schwa / long central mid)."""
        _assert_first(_grapheme(self.spec, "ŷ"), "əː", label="cy:ŷ")

    # ── Consonants ──────────────────────────────────────────────────────────

    def test_f_maps_to_voiced_labiodental_fricative(self):
        """CRITICAL: Welsh ⟨f⟩ maps to /v/ (voiced), NOT /f/ (voiceless).

        This is the single most common learner mistake. English speakers
        expect ⟨f⟩→/f/, but Welsh ⟨f⟩ is historically from *bh- lenition
        and surfaces as /v/. The voiceless /f/ is written ⟨ff⟩ in Welsh.
        """
        _assert_first(_grapheme(self.spec, "f"), "v", label="cy:f→v (CRITICAL)")

    def test_ff_maps_to_voiceless_labiodental(self):
        """⟨ff⟩ maps to the voiceless /f/, contrasting with ⟨f⟩→/v/."""
        _assert_first(_grapheme(self.spec, "ff"), "f", label="cy:ff→f")

    def test_ch_maps_to_voiceless_velar_fricative(self):
        """⟨ch⟩ maps to /x/ (voiceless velar fricative), as in Scottish 'loch'."""
        _assert_first(_grapheme(self.spec, "ch"), "x", label="cy:ch→x")

    def test_dd_maps_to_voiced_dental_fricative(self):
        """⟨dd⟩ maps to /ð/ (voiced dental fricative), as in English 'the'."""
        _assert_first(_grapheme(self.spec, "dd"), "ð", label="cy:dd→ð")

    def test_ll_maps_to_voiceless_lateral_fricative(self):
        """⟨ll⟩ maps to /ɬ/ (voiceless lateral fricative).

        This sound has no English equivalent. It is produced by placing the
        tongue as for /l/ while blowing air over the sides — a diagnostic
        Welsh sound. 'Llanfair' starts with this sound.
        """
        _assert_first(_grapheme(self.spec, "ll"), "ɬ", label="cy:ll→ɬ")

    def test_rh_maps_to_voiceless_rhotic(self):
        """⟨rh⟩ maps to /r̥/ (voiceless alveolar trill/tap).

        The voiceless rhotic is another diagnostic Welsh feature, found
        word-initially in many common words ('rhy', 'rhaid', 'rhan').
        """
        _assert_first(_grapheme(self.spec, "rh"), "r̥", label="cy:rh→r̥")

    def test_th_maps_to_voiceless_dental_fricative(self):
        """⟨th⟩ maps to /θ/ (voiceless dental fricative), as in 'thin'."""
        _assert_first(_grapheme(self.spec, "th"), "θ", label="cy:th→θ")

    def test_ph_maps_to_voiceless_labiodental(self):
        """⟨ph⟩ maps to /f/ (voiceless labiodental fricative).

        ⟨ph⟩ arises from lenition of /p/ in mutation contexts and is
        phonetically identical to ⟨ff⟩ — both realise as /f/.
        """
        _assert_first(_grapheme(self.spec, "ph"), "f", label="cy:ph→f")

    def test_ng_maps_to_velar_nasal(self):
        """⟨ng⟩ maps to /ŋ/ (velar nasal), as in English 'sing'."""
        _assert_first(_grapheme(self.spec, "ng"), "ŋ", label="cy:ng→ŋ")

    def test_mh_maps_to_voiceless_bilabial_nasal(self):
        """⟨mh⟩ maps to /m̥/ (voiceless bilabial nasal), a lenited ⟨m⟩."""
        _assert_first(_grapheme(self.spec, "mh"), "m̥", label="cy:mh→m̥")

    # ── Allophones ──────────────────────────────────────────────────────────

    def test_p_allophone_includes_aspirated(self):
        """Phoneme /p/ has aspirated allophone [pʰ] in syllable-initial position."""
        vals = _allophone(self.spec, "p")
        _assert_contains(vals, "p", "pʰ", label="cy:p allophones")

    def test_t_allophone_includes_aspirated(self):
        """Phoneme /t/ has aspirated allophone [tʰ] in syllable-initial position."""
        vals = _allophone(self.spec, "t")
        _assert_contains(vals, "t", "tʰ", label="cy:t allophones")

    def test_k_allophone_includes_aspirated(self):
        """Phoneme /k/ has aspirated allophone [kʰ] in syllable-initial position."""
        vals = _allophone(self.spec, "k")
        _assert_contains(vals, "k", "kʰ", label="cy:k allophones")

    def test_theta_allophone_is_stable(self):
        """Phoneme /θ/ has only a single surface realisation [θ] in Welsh."""
        vals = _allophone(self.spec, "θ")
        _assert_contains(vals, "θ", label="cy:θ allophone")

    def test_voiced_dental_fricative_allophone_is_stable(self):
        """Phoneme /ð/ has only a single surface realisation [ð] in Welsh."""
        vals = _allophone(self.spec, "ð")
        _assert_contains(vals, "ð", label="cy:ð allophone")

    def test_voiceless_lateral_allophone_is_stable(self):
        """Phoneme /ɬ/ has a single surface realisation [ɬ] — it does not alternate."""
        vals = _allophone(self.spec, "ɬ")
        _assert_contains(vals, "ɬ", label="cy:ɬ allophone")


# ═══════════════════════════════════════════════════════════════════════════
# Irish (ga)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestIrish:
    """Accuracy tests for Irish (ga).

    Irish (Gaeilge) is the most complex of the Celtic languages orthographically.
    Every consonant has two variants — broad (velarised, written adjacent to
    a/o/u) and slender (palatalised, adjacent to e/i). Lenition (séimhiú)
    replaces initial consonants with digraphs: ⟨bh⟩, ⟨ch⟩, ⟨dh⟩, etc.
    Some lenited forms become silent (⟨fh⟩) or merge into /h/ (⟨sh⟩, ⟨th⟩).
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Irish LanguageSpec once for the whole class."""
        request.cls.spec = _load("ga")

    # ── Vowels ──────────────────────────────────────────────────────────────

    def test_a_includes_back_variant(self):
        """⟨a⟩ in Irish has both /a/ (front) and /ɑ/ (back) realisations."""
        vals = _grapheme(self.spec, "a")
        _assert_contains(vals, "a", "ɑ", label="ga:a")

    def test_long_a_maps_to_low_long(self):
        """⟨á⟩ (fada) maps to the long low vowel /aː/."""
        _assert_first(_grapheme(self.spec, "á"), "aː", label="ga:á")

    def test_long_e_maps_to_close_mid_long(self):
        """⟨é⟩ (fada) maps to /eː/ (long close-mid front)."""
        _assert_first(_grapheme(self.spec, "é"), "eː", label="ga:é")

    def test_long_i_maps_to_close_long(self):
        """⟨í⟩ (fada) maps to /iː/ (long close front)."""
        _assert_first(_grapheme(self.spec, "í"), "iː", label="ga:í")

    def test_long_o_maps_to_close_mid_long(self):
        """⟨ó⟩ (fada) maps to /oː/ (long close-mid back)."""
        _assert_first(_grapheme(self.spec, "ó"), "oː", label="ga:ó")

    def test_long_u_maps_to_close_long(self):
        """⟨ú⟩ (fada) maps to /uː/ (long close back)."""
        _assert_first(_grapheme(self.spec, "ú"), "uː", label="ga:ú")

    # ── Consonant palatalization: broad vs slender ───────────────────────────

    def test_b_has_broad_and_slender_variants(self):
        """⟨b⟩ has both broad /bˠ/ (velarised) and slender /bʲ/ (palatalised) forms.

        In Irish, every consonant grapheme can surface as either the broad or
        slender variant depending on adjacent vowels. The broad phoneme /bˠ/
        occurs near a/o/u; /bʲ/ occurs near e/i.
        """
        vals = _grapheme(self.spec, "b")
        _assert_contains(vals, "bˠ", "bʲ", label="ga:b broad/slender")

    def test_b_primary_is_broad(self):
        """The primary (default) realisation of ⟨b⟩ is the broad /bˠ/."""
        _assert_first(_grapheme(self.spec, "b"), "bˠ", label="ga:b primary=broad")

    def test_d_has_broad_and_slender_variants(self):
        """⟨d⟩ has broad /d̪ˠ/ (velarised dental) and slender /dʲ/ forms."""
        vals = _grapheme(self.spec, "d")
        _assert_contains(vals, "d̪ˠ", "dʲ", label="ga:d broad/slender")

    def test_t_has_broad_and_slender_variants(self):
        """⟨t⟩ has broad /t̪ˠ/ (velarised dental) and slender /tʲ/ forms."""
        vals = _grapheme(self.spec, "t")
        _assert_contains(vals, "t̪ˠ", "tʲ", label="ga:t broad/slender")

    def test_c_has_velar_and_palatal_variants(self):
        """⟨c⟩ has velar /k/ (broad) and palatal /c/ (slender) realisations."""
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "k", "c", label="ga:c k/c")

    def test_g_has_velar_and_palatal_variants(self):
        """⟨g⟩ has velar /ɡ/ (broad) and palatal /ɟ/ (slender) realisations."""
        vals = _grapheme(self.spec, "g")
        _assert_contains(vals, "ɡ", "ɟ", label="ga:g ɡ/ɟ")

    def test_s_has_broad_and_slender_variants(self):
        """⟨s⟩ has broad /sˠ/ (velarised) and slender /ʃ/ realisations."""
        vals = _grapheme(self.spec, "s")
        _assert_contains(vals, "sˠ", "ʃ", label="ga:s broad/slender")

    # ── Lenition digraphs ────────────────────────────────────────────────────

    def test_bh_lenition_gives_w_and_vj(self):
        """Lenited ⟨bh⟩ surfaces as /w/ (broad) or /vʲ/ (slender).

        Lenition (séimhiú) of /b/ produces ⟨bh⟩. In broad position (near
        a/o/u) this is /w/; in slender position (near e/i) it is /vʲ/.
        """
        vals = _grapheme(self.spec, "bh")
        _assert_contains(vals, "w", "vʲ", label="ga:bh lenition")

    def test_bh_primary_is_w(self):
        """The primary (most common) realisation of ⟨bh⟩ is /w/."""
        _assert_first(_grapheme(self.spec, "bh"), "w", label="ga:bh primary=w")

    def test_ch_lenition_gives_x_and_c_cedilla(self):
        """Lenited ⟨ch⟩ gives /x/ (broad velar fricative) or /ç/ (slender palatal).

        This parallels the Welsh/Scots Gaelic ⟨ch⟩ but adds the palatal variant
        for slender environments.
        """
        vals = _grapheme(self.spec, "ch")
        _assert_contains(vals, "x", "ç", label="ga:ch lenition")

    def test_dh_lenition_gives_gamma_and_j(self):
        """Lenited ⟨dh⟩ gives /ɣ/ (voiced velar fricative, broad) or /j/ (slender).

        Broad ⟨dh⟩ = /ɣ/, slender ⟨dh⟩ = /j/ (palatal approximant).
        """
        vals = _grapheme(self.spec, "dh")
        _assert_contains(vals, "ɣ", "j", label="ga:dh lenition")

    def test_fh_lenition_is_silent(self):
        """Lenited ⟨fh⟩ is completely silent — it has no phonetic realisation.

        This is one of the most distinctive features of Irish: the lenition
        of /f/ produces a zero segment. Words like 'a fhear' (/ə ar/) show
        this clearly.
        """
        vals = _grapheme(self.spec, "fh")
        assert vals is not None, "ga:fh mapping should exist"
        # fh maps to an empty string representing silence
        assert "" in vals or (len(vals) == 1 and vals[0] == ""), (
            f"ga:fh should map to empty string (silence), got {vals!r}"
        )

    def test_gh_lenition_gives_gamma_and_j(self):
        """Lenited ⟨gh⟩ gives /ɣ/ (broad) or /j/ (slender), parallel to ⟨dh⟩."""
        vals = _grapheme(self.spec, "gh")
        _assert_contains(vals, "ɣ", "j", label="ga:gh lenition")

    def test_mh_lenition_gives_w_and_vj(self):
        """Lenited ⟨mh⟩ gives /w/ (broad) or /vʲ/ (slender), parallel to ⟨bh⟩.

        Lenition of /m/ and /b/ produce phonologically identical outputs in Irish.
        """
        vals = _grapheme(self.spec, "mh")
        _assert_contains(vals, "w", "vʲ", label="ga:mh lenition")

    def test_sh_lenition_gives_h(self):
        """Lenited ⟨sh⟩ merges to /h/ — the /s/ is replaced entirely."""
        _assert_first(_grapheme(self.spec, "sh"), "h", label="ga:sh→h")

    def test_th_lenition_gives_h(self):
        """Lenited ⟨th⟩ merges to /h/ — the /t/ is replaced entirely."""
        _assert_first(_grapheme(self.spec, "th"), "h", label="ga:th→h")

    def test_ng_includes_velar_nasal(self):
        """⟨ng⟩ includes /ŋ/ (velar nasal) as primary realisation."""
        vals = _grapheme(self.spec, "ng")
        _assert_contains(vals, "ŋ", label="ga:ng")

    # ── Allophones ──────────────────────────────────────────────────────────

    def test_allophone_pS_is_stable(self):
        """Broad phoneme /pˠ/ has only [pˠ] as surface form."""
        _assert_contains(_allophone(self.spec, "pˠ"), "pˠ", label="ga:pˠ allophone")

    def test_allophone_pJ_is_stable(self):
        """Slender phoneme /pʲ/ has only [pʲ] as surface form."""
        _assert_contains(_allophone(self.spec, "pʲ"), "pʲ", label="ga:pʲ allophone")

    def test_allophone_k_is_stable(self):
        """Velar phoneme /k/ (broad ⟨c⟩) has single surface form [k]."""
        _assert_contains(_allophone(self.spec, "k"), "k", label="ga:k allophone")

    def test_allophone_c_palatal_is_stable(self):
        """Palatal phoneme /c/ (slender ⟨c⟩) has single surface form [c]."""
        _assert_contains(_allophone(self.spec, "c"), "c", label="ga:c allophone")

    def test_allophone_gamma_is_stable(self):
        """Fricative /ɣ/ (from lenited ⟨dh⟩/⟨gh⟩) has single surface form [ɣ]."""
        _assert_contains(_allophone(self.spec, "ɣ"), "ɣ", label="ga:ɣ allophone")


# ═══════════════════════════════════════════════════════════════════════════
# Scottish Gaelic (gd)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestScottishGaelic:
    """Accuracy tests for Scottish Gaelic (gd).

    Scottish Gaelic (Gàidhlig) shares the broad/slender consonant distinction
    with Irish but has distinctive pre-aspiration of voiceless stops and
    different devoicing patterns. Initial ⟨b⟩ is typically devoiced to [p],
    and stops are aspirated (⟨c⟩→/kʰ/ or /cʰ/). Lenition digraphs (⟨bh⟩,
    ⟨ch⟩, etc.) follow similar but not identical patterns to Irish.
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Scottish Gaelic LanguageSpec once for the whole class."""
        request.cls.spec = _load("gd")

    # ── Vowels ──────────────────────────────────────────────────────────────

    def test_a_maps_to_short_a(self):
        """Plain ⟨a⟩ maps to short /a/."""
        _assert_first(_grapheme(self.spec, "a"), "a", label="gd:a")

    def test_a_grave_gives_long_low(self):
        """⟨à⟩ (grave) maps to long /aː/."""
        _assert_first(_grapheme(self.spec, "à"), "aː", label="gd:à")

    def test_e_includes_mid_variants(self):
        """⟨e⟩ can realise as /e/ (close-mid) or /ɛ/ (open-mid)."""
        vals = _grapheme(self.spec, "e")
        _assert_contains(vals, "e", "ɛ", label="gd:e variants")

    def test_e_grave_gives_open_mid_long(self):
        """⟨è⟩ maps to /ɛː/ (long open-mid front)."""
        _assert_first(_grapheme(self.spec, "è"), "ɛː", label="gd:è")

    def test_e_acute_gives_close_mid_long(self):
        """⟨é⟩ maps to /eː/ (long close-mid front)."""
        _assert_first(_grapheme(self.spec, "é"), "eː", label="gd:é")

    def test_i_grave_gives_long_close(self):
        """⟨ì⟩ maps to /iː/ (long close front)."""
        _assert_first(_grapheme(self.spec, "ì"), "iː", label="gd:ì")

    def test_o_grave_gives_open_mid_long(self):
        """⟨ò⟩ maps to /ɔː/ (long open-mid back)."""
        _assert_first(_grapheme(self.spec, "ò"), "ɔː", label="gd:ò")

    def test_u_grave_gives_long_close_back(self):
        """⟨ù⟩ maps to /uː/ (long close back)."""
        _assert_first(_grapheme(self.spec, "ù"), "uː", label="gd:ù")

    # ── Consonants: initial devoicing and aspiration ─────────────────────────

    def test_b_primary_is_devoiced_p(self):
        """CRITICAL: ⟨b⟩ word-initially maps to /p/ (devoiced) as primary realisation.

        Unlike Irish where ⟨b⟩→/bˠ/, Scottish Gaelic devoices ⟨b⟩ at word
        boundaries. The voiced /b/ appears as a secondary variant only.
        """
        _assert_first(_grapheme(self.spec, "b"), "p", label="gd:b primary=p (devoiced)")

    def test_b_secondary_includes_voiced(self):
        """⟨b⟩ also has voiced /b/ as a secondary (medial/post-nasal) realisation."""
        vals = _grapheme(self.spec, "b")
        _assert_contains(vals, "b", label="gd:b secondary voiced")

    def test_c_maps_to_aspirated_stops(self):
        """⟨c⟩ maps to aspirated /kʰ/ (broad) and /cʰ/ (slender palatal).

        Scottish Gaelic is notable for obligatory aspiration of voiceless
        stops — ⟨c⟩ is always aspirated, distinguishing it from Irish /k/.
        """
        vals = _grapheme(self.spec, "c")
        _assert_contains(vals, "kʰ", "cʰ", label="gd:c aspirated")

    def test_p_maps_to_aspirated_stop(self):
        """⟨p⟩ maps to the aspirated /pʰ/ (voiceless bilabial aspirated stop)."""
        _assert_first(_grapheme(self.spec, "p"), "pʰ", label="gd:p→pʰ aspirated")

    # ── Lenition digraphs ────────────────────────────────────────────────────

    def test_bh_maps_to_v(self):
        """Lenited ⟨bh⟩ maps to /v/ (voiced labiodental fricative).

        Unlike Irish where ⟨bh⟩→/w/ (broad), Scottish Gaelic ⟨bh⟩ consistently
        maps to /v/ regardless of vowel context.
        """
        _assert_first(_grapheme(self.spec, "bh"), "v", label="gd:bh→v")

    def test_ch_maps_to_x_and_c_cedilla(self):
        """Lenited ⟨ch⟩ gives /x/ (broad, as in 'loch') or /ç/ (slender palatal)."""
        vals = _grapheme(self.spec, "ch")
        _assert_contains(vals, "x", "ç", label="gd:ch→x/ç")

    def test_dh_maps_to_gamma_and_j(self):
        """Lenited ⟨dh⟩ gives /ɣ/ (broad voiced velar fricative) or /j/ (slender)."""
        vals = _grapheme(self.spec, "dh")
        _assert_contains(vals, "ɣ", "j", label="gd:dh→ɣ/j")

    def test_fh_is_silent(self):
        """Lenited ⟨fh⟩ is silent — maps to an empty string, as in Irish."""
        vals = _grapheme(self.spec, "fh")
        assert vals is not None, "gd:fh mapping should exist"
        assert "" in vals or (len(vals) == 1 and vals[0] == ""), (
            f"gd:fh should be silent (empty string), got {vals!r}"
        )

    def test_gh_maps_to_gamma_and_j(self):
        """Lenited ⟨gh⟩ gives /ɣ/ (broad) or /j/ (slender), parallel to ⟨dh⟩."""
        vals = _grapheme(self.spec, "gh")
        _assert_contains(vals, "ɣ", "j", label="gd:gh→ɣ/j")

    def test_mh_maps_to_v(self):
        """Lenited ⟨mh⟩ maps to /v/ — same output as ⟨bh⟩ in Scottish Gaelic."""
        _assert_first(_grapheme(self.spec, "mh"), "v", label="gd:mh→v")

    def test_ph_maps_to_f(self):
        """Lenited ⟨ph⟩ maps to /f/ (voiceless labiodental fricative)."""
        _assert_first(_grapheme(self.spec, "ph"), "f", label="gd:ph→f")

    def test_sh_maps_to_h(self):
        """Lenited ⟨sh⟩ maps to /h/ — the fricative is fully aspirated."""
        _assert_first(_grapheme(self.spec, "sh"), "h", label="gd:sh→h")

    def test_th_maps_to_h(self):
        """Lenited ⟨th⟩ maps to /h/, as in Irish."""
        _assert_first(_grapheme(self.spec, "th"), "h", label="gd:th→h")

    def test_ng_maps_to_velar_nasal(self):
        """⟨ng⟩ maps to /ŋ/ (velar nasal), as in all Goidelic languages."""
        _assert_first(_grapheme(self.spec, "ng"), "ŋ", label="gd:ng→ŋ")

    # ── Allophones ──────────────────────────────────────────────────────────

    def test_p_allophone_includes_unaspirated(self):
        """Phoneme /p/ has both [p] (unaspirated) and [pʰ] (aspirated) surface forms."""
        vals = _allophone(self.spec, "p")
        _assert_contains(vals, "p", "pʰ", label="gd:p allophones")

    def test_kh_allophone_is_stable(self):
        """Aspirated phoneme /kʰ/ has single surface form [kʰ]."""
        _assert_contains(_allophone(self.spec, "kʰ"), "kʰ", label="gd:kʰ allophone")

    def test_ch_aspirated_allophone_is_stable(self):
        """Aspirated palatal phoneme /cʰ/ has single surface form [cʰ]."""
        _assert_contains(_allophone(self.spec, "cʰ"), "cʰ", label="gd:cʰ allophone")

    def test_t_dental_allophone_includes_aspirated(self):
        """Dental phoneme /t̪/ has both [t̪] and [t̪ʰ] surface forms (pre-aspiration)."""
        vals = _allophone(self.spec, "t̪")
        _assert_contains(vals, "t̪", "t̪ʰ", label="gd:t̪ allophones")


# ═══════════════════════════════════════════════════════════════════════════
# Breton (br)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestBreton:
    """Accuracy tests for Breton (br).

    Breton (Brezhoneg) is a Brythonic Celtic language of Brittany, France.
    It retains several archaic Brythonic features while having adopted French
    phonological influence (uvular /ʁ/, front rounded /y/). The digraph ⟨c'h⟩
    is unique to Breton orthography and realises as /x/ or /h/. ⟨zh⟩ is
    a shibboleth feature marking the Vannetais dialect split.
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Breton LanguageSpec once for the whole class."""
        request.cls.spec = _load("br")

    # ── Vowels ──────────────────────────────────────────────────────────────

    def test_u_maps_to_front_rounded(self):
        """CRITICAL: Breton ⟨u⟩ maps to /y/ (close front rounded), not /u/.

        Under French phonological influence, Breton ⟨u⟩ is pronounced /y/
        (as in French 'tu'), not the back /u/ of English. This is a major
        distinguishing feature from Welsh and other Celtic languages.
        """
        _assert_first(_grapheme(self.spec, "u"), "y", label="br:u→y (front rounded)")

    def test_ou_maps_to_close_back(self):
        """⟨ou⟩ maps to /u/ (close back rounded), contrasting with ⟨u⟩→/y/.

        Breton requires ⟨ou⟩ to spell the /u/ sound — the French-influenced
        convention that became standard.
        """
        _assert_first(_grapheme(self.spec, "ou"), "u", label="br:ou→u")

    def test_a_maps_to_low_central(self):
        """Plain ⟨a⟩ maps to /a/ (open front unrounded)."""
        _assert_first(_grapheme(self.spec, "a"), "a", label="br:a")

    def test_e_includes_mid_variants(self):
        """⟨e⟩ can realise as /e/ (close-mid) or /ɛ/ (open-mid)."""
        vals = _grapheme(self.spec, "e")
        _assert_contains(vals, "e", "ɛ", label="br:e variants")

    def test_circumflex_a_gives_long(self):
        """⟨â⟩ maps to long /aː/."""
        _assert_first(_grapheme(self.spec, "â"), "aː", label="br:â")

    def test_circumflex_e_gives_long_close_mid(self):
        """⟨ê⟩ maps to long /eː/ (long close-mid front)."""
        _assert_first(_grapheme(self.spec, "ê"), "eː", label="br:ê")

    def test_circumflex_o_gives_long_close_mid_back(self):
        """⟨ô⟩ maps to long /oː/ (long close-mid back)."""
        _assert_first(_grapheme(self.spec, "ô"), "oː", label="br:ô")

    # ── Consonants ──────────────────────────────────────────────────────────

    def test_ch_maps_to_postalveolar_fricative(self):
        """⟨ch⟩ maps to /ʃ/ (voiceless postalveolar fricative), as in French 'chat'.

        Breton ⟨ch⟩ = /ʃ/ is DIFFERENT from Welsh ⟨ch⟩ = /x/ — a critical
        distinction between the two Celtic languages.
        """
        _assert_first(_grapheme(self.spec, "ch"), "ʃ", label="br:ch→ʃ (≠ Welsh x)")

    def test_j_maps_to_voiced_postalveolar(self):
        """⟨j⟩ maps to /ʒ/ (voiced postalveolar fricative), as in French 'je'."""
        _assert_first(_grapheme(self.spec, "j"), "ʒ", label="br:j→ʒ")

    def test_ch_prime_maps_to_velar_or_glottal(self):
        """⟨c'h⟩ (unique Breton digraph) maps to /x/ (KLT) or /h/ (Vannetais).

        The trigraph ⟨c'h⟩ is unique to Breton and marks the voiceless velar
        fricative /x/ in the standard KLT dialect or /h/ in Vannetais.
        This contrasts with ⟨ch⟩→/ʃ/ and is historically from *k in lenition.
        """
        vals = _grapheme(self.spec, "c'h")
        _assert_contains(vals, "x", "h", label="br:c'h→x/h")

    def test_gn_maps_to_palatal_nasal(self):
        """⟨gn⟩ maps to /ɲ/ (palatal nasal), as in French 'agneau'."""
        _assert_first(_grapheme(self.spec, "gn"), "ɲ", label="br:gn→ɲ")

    def test_lh_maps_to_palatal_lateral(self):
        """⟨lh⟩ maps to /ʎ/ (palatal lateral approximant), as in Italian 'gli'."""
        _assert_first(_grapheme(self.spec, "lh"), "ʎ", label="br:lh→ʎ")

    def test_r_primary_is_uvular(self):
        """⟨r⟩ primary realisation is /ʁ/ (uvular fricative) — French influence.

        Unlike Welsh ⟨r⟩→/r/ (alveolar trill), Breton ⟨r⟩ has been strongly
        influenced by French and primarily realises as the uvular /ʁ/.
        """
        _assert_first(_grapheme(self.spec, "r"), "ʁ", label="br:r primary=ʁ (uvular)")

    def test_r_secondary_includes_alveolar(self):
        """⟨r⟩ has alveolar /r/ as a secondary variant (older or rural speech)."""
        vals = _grapheme(self.spec, "r")
        _assert_contains(vals, "r", label="br:r secondary alveolar")

    def test_zh_maps_to_z_or_h(self):
        """⟨zh⟩ maps to /z/ (KLT dialect) or /h/ (Vannetais dialect).

        ⟨zh⟩ is a shibboleth letter in Breton: in KLT (Léonard, Trégorrois,
        Cornouaillais) it is /z/; in Vannetais it is /h/. The letter was
        introduced to unify the two dialect spellings.
        """
        vals = _grapheme(self.spec, "zh")
        _assert_contains(vals, "z", "h", label="br:zh→z/h")

    def test_nn_maps_to_plain_nasal(self):
        """⟨nn⟩ is not a geminate — it maps to plain /n/ (same as ⟨n⟩)."""
        _assert_first(_grapheme(self.spec, "nn"), "n", label="br:nn→n")

    def test_mm_maps_to_plain_nasal(self):
        """⟨mm⟩ maps to plain /m/ — geminate spelling, not geminate phoneme."""
        _assert_first(_grapheme(self.spec, "mm"), "m", label="br:mm→m")

    def test_g_maps_to_voiced_velar_stop(self):
        """⟨g⟩ maps to /ɡ/ (voiced velar stop)."""
        _assert_first(_grapheme(self.spec, "g"), "ɡ", label="br:g→ɡ")

    # ── Allophones ──────────────────────────────────────────────────────────

    def test_ch_allophone_is_stable(self):
        """Phoneme /ʃ/ has single surface form [ʃ] in Breton."""
        _assert_contains(_allophone(self.spec, "ʃ"), "ʃ", label="br:ʃ allophone")

    def test_zj_allophone_is_stable(self):
        """Phoneme /ʒ/ has single surface form [ʒ] in Breton."""
        _assert_contains(_allophone(self.spec, "ʒ"), "ʒ", label="br:ʒ allophone")

    def test_lj_allophone_is_stable(self):
        """Phoneme /ʎ/ has single surface form [ʎ] — no alternation."""
        _assert_contains(_allophone(self.spec, "ʎ"), "ʎ", label="br:ʎ allophone")

    def test_uvular_r_allophone_includes_alveolar(self):
        """Phoneme /ʁ/ has both [ʁ] (uvular) and [r] (alveolar) surface forms."""
        vals = _allophone(self.spec, "ʁ")
        _assert_contains(vals, "ʁ", "r", label="br:ʁ allophones")


# ═══════════════════════════════════════════════════════════════════════════
# Manx (gv)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestManx:
    """Accuracy tests for Manx (gv).

    Manx (Gaelg) is the Goidelic language of the Isle of Man. Its orthography
    is unique in the Goidelic family, having been recorded primarily by English
    speakers and thus following English spelling conventions rather than the
    traditional Gaelic orthographic system used by Irish and Scots Gaelic.
    The language was revived after the death of the last native speaker in 1974.
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Manx LanguageSpec once for the whole class."""
        request.cls.spec = _load("gv")

    # ── Long vowel digraphs ──────────────────────────────────────────────────

    def test_aa_maps_to_long_e(self):
        """⟨aa⟩ in Manx maps to /eː/ — a distinctive Manx sound correspondence.

        Manx ⟨aa⟩ does NOT simply mean 'long a'. The historical vowel shifted
        to /eː/, reflecting the development from Common Goidelic to Manx.
        """
        _assert_first(_grapheme(self.spec, "aa"), "eː", label="gv:aa→eː")

    def test_ee_maps_to_long_close_front(self):
        """⟨ee⟩ maps to /iː/ (long close front vowel)."""
        _assert_first(_grapheme(self.spec, "ee"), "iː", label="gv:ee→iː")

    def test_oo_maps_to_long_close_back(self):
        """⟨oo⟩ maps to /uː/ (long close back rounded vowel)."""
        _assert_first(_grapheme(self.spec, "oo"), "uː", label="gv:oo→uː")

    # ── Short vowels ─────────────────────────────────────────────────────────

    def test_a_includes_open_and_front_raised(self):
        """⟨a⟩ has both /a/ and /æ/ (near-open front) as realisations."""
        vals = _grapheme(self.spec, "a")
        _assert_contains(vals, "a", "æ", label="gv:a variants")

    def test_e_maps_to_open_mid_front(self):
        """⟨e⟩ maps to /ɛ/ (open-mid front unrounded)."""
        _assert_first(_grapheme(self.spec, "e"), "ɛ", label="gv:e→ɛ")

    def test_i_primary_is_near_close(self):
        """⟨i⟩ primary realisation is /ɪ/ (near-close near-front)."""
        _assert_first(_grapheme(self.spec, "i"), "ɪ", label="gv:i primary=ɪ")

    def test_o_maps_to_open_mid_back(self):
        """⟨o⟩ maps to /ɔ/ (open-mid back rounded)."""
        _assert_first(_grapheme(self.spec, "o"), "ɔ", label="gv:o→ɔ")

    def test_u_includes_near_close_back_and_mid_back(self):
        """⟨u⟩ has both /ʊ/ (near-close back) and /ɤ/ (close-mid back unrounded)."""
        vals = _grapheme(self.spec, "u")
        _assert_contains(vals, "ʊ", "ɤ", label="gv:u variants")

    # ── Consonant digraphs ───────────────────────────────────────────────────

    def test_ch_maps_to_velar_fricative(self):
        """⟨ch⟩ maps to /x/ (voiceless velar fricative), as in English 'loch'."""
        _assert_first(_grapheme(self.spec, "ch"), "x", label="gv:ch→x")

    def test_gh_maps_to_voiced_velar_fricative(self):
        """⟨gh⟩ maps to /ɣ/ (voiced velar fricative) in Manx."""
        _assert_first(_grapheme(self.spec, "gh"), "ɣ", label="gv:gh→ɣ")

    def test_sh_maps_to_postalveolar_fricative(self):
        """⟨sh⟩ maps to /ʃ/ (voiceless postalveolar fricative)."""
        _assert_first(_grapheme(self.spec, "sh"), "ʃ", label="gv:sh→ʃ")

    def test_th_includes_dental_fricatives(self):
        """⟨th⟩ maps to /θ/ (voiceless) or /ð/ (voiced dental fricative).

        Manx ⟨th⟩ can realise as either dental fricative — the voiceless /θ/
        being more frequent word-initially.
        """
        vals = _grapheme(self.spec, "th")
        _assert_contains(vals, "θ", "ð", label="gv:th→θ/ð")


# ═══════════════════════════════════════════════════════════════════════════
# Cornish (kw)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.linguistic
class TestCornish:
    """Accuracy tests for Cornish (kw).

    Cornish (Kernewek) is a revived Brythonic Celtic language of Cornwall.
    The last native speaker died in 1777 and the language was reconstructed
    from medieval texts. This spec follows the revived Kernewek Standard
    pronunciation. Cornish diverges from Welsh notably in ⟨ch⟩→/tʃ/ (vs.
    Welsh /x/) and is closer to Breton in its Brythonic phonology.
    """

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        """Load the Cornish LanguageSpec once for the whole class."""
        request.cls.spec = _load("kw")

    # ── Vowels ──────────────────────────────────────────────────────────────

    def test_a_includes_open_and_near_open(self):
        """⟨a⟩ has both /a/ (open front) and /æ/ (near-open front) realisations."""
        vals = _grapheme(self.spec, "a")
        _assert_contains(vals, "a", "æ", label="kw:a variants")

    def test_e_maps_to_open_mid_front(self):
        """⟨e⟩ maps to /ɛ/ (open-mid front unrounded)."""
        _assert_first(_grapheme(self.spec, "e"), "ɛ", label="kw:e→ɛ")

    def test_i_maps_to_near_close_front(self):
        """⟨i⟩ maps to /ɪ/ (near-close near-front)."""
        _assert_first(_grapheme(self.spec, "i"), "ɪ", label="kw:i→ɪ")

    def test_u_maps_to_near_close_back(self):
        """⟨u⟩ maps to /ʊ/ (near-close back rounded)."""
        _assert_first(_grapheme(self.spec, "u"), "ʊ", label="kw:u→ʊ")

    def test_y_includes_near_close_and_schwa(self):
        """⟨y⟩ has both /ɪ/ (near-close) and /ə/ (schwa) realisations, as in Welsh."""
        vals = _grapheme(self.spec, "y")
        _assert_contains(vals, "ɪ", "ə", label="kw:y variants")

    # ── Consonants ──────────────────────────────────────────────────────────

    def test_ch_maps_to_affricate_not_fricative(self):
        """CRITICAL: Cornish ⟨ch⟩ maps to /tʃ/ (affricate), NOT /x/ as in Welsh.

        This is a key typological difference between the Brythonic languages:
        Welsh ⟨ch⟩→/x/ (velar fricative), Cornish ⟨ch⟩→/tʃ/ (postalveolar
        affricate, as in English 'church'). Breton ⟨ch⟩→/ʃ/ is yet another
        different mapping.
        """
        _assert_first(_grapheme(self.spec, "ch"), "tʃ", label="kw:ch→tʃ (≠ Welsh x)")

    def test_dh_maps_to_voiced_dental_fricative(self):
        """⟨dh⟩ maps to /ð/ (voiced dental fricative), as in English 'the'."""
        _assert_first(_grapheme(self.spec, "dh"), "ð", label="kw:dh→ð")

    def test_th_maps_to_voiceless_dental_fricative(self):
        """⟨th⟩ maps to /θ/ (voiceless dental fricative), as in English 'thin'."""
        _assert_first(_grapheme(self.spec, "th"), "θ", label="kw:th→θ")

    def test_gh_maps_to_velar_fricative_or_glottal(self):
        """⟨gh⟩ maps to /x/ (velar fricative) or /h/ (glottal) in Cornish.

        Cornish ⟨gh⟩ is different from Manx ⟨gh⟩→/ɣ/: Cornish realises
        ⟨gh⟩ as the voiceless /x/ or /h/ depending on position.
        """
        vals = _grapheme(self.spec, "gh")
        _assert_contains(vals, "x", "h", label="kw:gh→x/h")

    def test_gh_primary_is_velar(self):
        """The primary (most common) realisation of Cornish ⟨gh⟩ is /x/."""
        _assert_first(_grapheme(self.spec, "gh"), "x", label="kw:gh primary=x")

    def test_hw_maps_to_voiceless_labio_velar(self):
        """⟨hw⟩ maps to /ʍ/ (voiceless labio-velar approximant), as in 'which' for some speakers."""
        _assert_first(_grapheme(self.spec, "hw"), "ʍ", label="kw:hw→ʍ")

    # ── Allophones ──────────────────────────────────────────────────────────

    def test_theta_allophone_is_stable(self):
        """Phoneme /θ/ has a single surface form [θ] — no voiced alternant."""
        _assert_contains(_allophone(self.spec, "θ"), "θ", label="kw:θ allophone")

    def test_eth_allophone_is_stable(self):
        """Phoneme /ð/ has a single surface form [ð] — no voiceless alternant."""
        _assert_contains(_allophone(self.spec, "ð"), "ð", label="kw:ð allophone")

    def test_affricate_allophone_is_stable(self):
        """Phoneme /tʃ/ has a single surface form [tʃ]."""
        _assert_contains(_allophone(self.spec, "tʃ"), "tʃ", label="kw:tʃ allophone")

    def test_p_allophone_is_stable(self):
        """Phoneme /p/ has a single surface form [p] in Cornish."""
        _assert_contains(_allophone(self.spec, "p"), "p", label="kw:p allophone")

    def test_b_allophone_is_stable(self):
        """Phoneme /b/ has a single surface form [b] in Cornish."""
        _assert_contains(_allophone(self.spec, "b"), "b", label="kw:b allophone")
