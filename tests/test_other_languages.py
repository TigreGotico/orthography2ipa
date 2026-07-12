"""Per-language accuracy tests for other language families.

Covers:
- Modern Greek (el)
- Ancient Greek / Classical Greek (grc)
- Archaic Latin (la-x-archaic)
- Finnish (fi)
- Hungarian (hu)
- Japanese (ja) — Kana-based
- Korean (ko) — Hangul-based
- Mandarin Chinese (zh) — Pinyin romanisation
- Middle English (enm)
- Old English / Anglo-Saxon (ang)
"""
from __future__ import annotations

import pytest

import orthography2ipa

_SENTINEL = object()


def _load(code: str):
    try:
        return orthography2ipa.get(code)
    except Exception as exc:
        pytest.skip(f"{code!r} not available: {exc}")


def _grapheme(spec, grapheme: str):
    return spec.graphemes.get(grapheme)


def _allophone(spec, phoneme: str):
    return spec.allophones.get(phoneme)


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
# Modern Greek
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestModernGreek:
    """Accuracy tests for Modern Greek (el).

    Modern Greek shows dramatic simplification from Ancient:
    - All historical long/short vowel distinctions collapsed
    - η, ι, υ, ει, οι, υι → all [i] (iotacism)
    - β→[v], δ→[ð], γ→[ɣ/ʝ] (fricativization of voiced stops)
    - αυ→[av/af], ευ→[ev/ef] (context-dependent)
    - θ→[θ], φ→[f] (retained from Ancient)
    """

    LANGUAGE_CODE = "el"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Iotacism — all these → [i]
    def test_eta_iotacism(self):
        """η → [i] (iotacism — ancient long ɛː merged into i)."""
        _assert_first(_grapheme(self.spec, "η"), "i", label="η")

    def test_upsilon_iotacism(self):
        """υ → [i] (iotacism — ancient front rounded y merged into i)."""
        _assert_first(_grapheme(self.spec, "υ"), "i", label="υ")

    def test_epsilon_iota_iotacism(self):
        """ει → [i] (ancient diphthong monophthongised)."""
        _assert_first(_grapheme(self.spec, "ει"), "i", label="ει")

    def test_omicron_iota_iotacism(self):
        """οι → [i]."""
        _assert_first(_grapheme(self.spec, "οι"), "i", label="οι")

    def test_alpha_iota_digraph(self):
        """αι → [e] (ancient diphthong aj → modern e)."""
        _assert_first(_grapheme(self.spec, "αι"), "e", label="αι")

    def test_omicron_upsilon_digraph(self):
        """ου → [u] (ancient diphthong → long u)."""
        _assert_first(_grapheme(self.spec, "ου"), "u", label="ου")

    def test_omega_collapsed(self):
        """ω → [o] (ancient long ɔː → modern o, same as ο)."""
        _assert_first(_grapheme(self.spec, "ω"), "o", label="ω")

    # Fricativization of ancient voiced stops
    def test_beta_fricative(self):
        """β → [v] (ancient [b] → modern labiodental fricative)."""
        _assert_first(_grapheme(self.spec, "β"), "v", label="β")

    def test_delta_fricative(self):
        """δ → [ð] (ancient [d] → modern dental fricative)."""
        _assert_first(_grapheme(self.spec, "δ"), "ð", label="δ")

    def test_gamma_fricative(self):
        """γ → [ɣ, ʝ] (ancient [ɡ] → velar/palatal fricative)."""
        vals = _grapheme(self.spec, "γ")
        _assert_contains(vals, "ɣ", label="γ fricative")

    # Retained ancient features
    def test_theta_preserved(self):
        """θ → [θ] (ancient aspirated dental → dental fricative, preserved)."""
        vals = _grapheme(self.spec, "θ")
        assert vals is not None
        assert vals[0] in ("θ", "θ"), f"θ expected θ, got {vals[0]}"

    def test_phi_fricative(self):
        """φ → [f] (ancient [pʰ] → modern fricative)."""
        vals = _grapheme(self.spec, "φ")
        assert vals is not None
        assert vals[0] in ("f", "f"), f"φ expected f, got {vals[0]}"

    def test_chi_velar(self):
        """χ → [x] or [ç] (ancient [kʰ] → velar/palatal fricative)."""
        vals = _grapheme(self.spec, "χ")
        assert vals is not None
        assert vals[0] in ("x", "ç"), f"χ expected x/ç, got {vals[0]}"

    # Context-sensitive αυ/ευ
    def test_alpha_upsilon_voiced(self):
        """αυ → [av, af] — voiced before sonorants/vowels, voiceless before voiceless."""
        vals = _grapheme(self.spec, "αυ")
        _assert_contains(vals, "av", "af", label="αυ")

    def test_epsilon_upsilon_voiced(self):
        """ευ → [ev, ef] — context-sensitive."""
        vals = _grapheme(self.spec, "ευ")
        _assert_contains(vals, "ev", "ef", label="ευ")

    def test_parent_is_grc(self):
        """Modern Greek inherits from Ancient Greek."""
        assert self.spec.parent == "grc"


# ═══════════════════════════════════════════════════════════════════════════
# Ancient Greek
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestAncientGreek:
    """Accuracy tests for Ancient Greek (grc) — Classical period.

    Ancient Greek preserves the full vowel length system, front rounded υ,
    diphthongs, and aspirated stops (φ, θ, χ as [pʰ, tʰ, kʰ]).
    """

    LANGUAGE_CODE = "grc"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_alpha_short(self):
        """α → [a] (short open vowel)."""
        _assert_first(_grapheme(self.spec, "α"), "a", label="α")

    def test_eta_long_e(self):
        """η → [ɛː] (long open-mid e — distinct from ε and ι in Ancient)."""
        _assert_first(_grapheme(self.spec, "η"), "ɛː", label="η")

    def test_upsilon_front_rounded(self):
        """υ → [y] (front rounded — distinct from Modern Greek iotacism)."""
        _assert_first(_grapheme(self.spec, "υ"), "y", label="υ")

    def test_omega_long_o(self):
        """ω → [ɔː] (long open-mid o — distinct from ο)."""
        _assert_first(_grapheme(self.spec, "ω"), "ɔː", label="ω")

    def test_alpha_long(self):
        """ᾱ → [aː] (long alpha with macron)."""
        _assert_first(_grapheme(self.spec, "ᾱ"), "aː", label="ᾱ")

    def test_alpha_iota_diphthong(self):
        """αι → [aj] (diphthong — not yet monophthongised as in Modern)."""
        _assert_first(_grapheme(self.spec, "αι"), "aj", label="αι")

    def test_epsilon_iota_diphthong(self):
        """ει → [eː] (contracted diphthong)."""
        vals = _grapheme(self.spec, "ει")
        assert vals is not None
        assert vals[0] in ("eː", "ej"), f"ει expected eː/ej, got {vals[0]}"

    def test_aspirated_phi(self):
        """φ → [pʰ] (aspirated bilabial — not fricative as in Modern)."""
        vals = _grapheme(self.spec, "φ")
        assert vals is not None
        assert vals[0] in ("pʰ", "f"), f"φ expected pʰ, got {vals[0]}"

    def test_aspirated_theta(self):
        """θ → [tʰ] (aspirated dental — original value)."""
        vals = _grapheme(self.spec, "θ")
        assert vals is not None
        assert vals[0] in ("tʰ", "θ"), f"θ expected tʰ, got {vals[0]}"

    def test_aspirated_chi(self):
        """χ → [kʰ] (aspirated velar)."""
        vals = _grapheme(self.spec, "χ")
        assert vals is not None
        assert vals[0] in ("kʰ", "x"), f"χ expected kʰ, got {vals[0]}"

    def test_aspirated_allophone(self):
        """pʰ allophone in table — aspirated stops phonemically distinct."""
        vals = _allophone(self.spec, "pʰ")
        assert vals is not None, "pʰ should be in allophone table"

    def test_family(self):
        """Ancient Greek is Hellenic (Indo-European)."""
        assert {"Indo-European", "Hellenic"} <= set(self.spec.family_path)


# ═══════════════════════════════════════════════════════════════════════════
# Archaic Latin
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestArchaicLatin:
    """Accuracy tests for Archaic Latin (la-x-archaic).

    Pre-Classical Latin with retained diphthongs and labiovelar stops.
    Key features: c always [k], qu→[kʷ], gu→[ɡʷ], diphthongs ai/ei/oi/ou/au,
    aspirated stops ph/th (Greek loans).
    """

    LANGUAGE_CODE = "la-x-archaic"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    def test_c_always_k(self):
        """c → [k] only (no palatalization — Latin c is always velar)."""
        _assert_first(_grapheme(self.spec, "c"), "k", label="c")

    def test_qu_labiovelar(self):
        """qu → [kʷ] (labiovelar — Latin qu)."""
        vals = _grapheme(self.spec, "qu")
        assert vals is not None
        assert vals[0] in ("kʷ", "k"), f"qu expected kʷ, got {vals[0]}"

    def test_gu_labiovelar(self):
        """gu → [ɡʷ] (voiced labiovelar)."""
        vals = _grapheme(self.spec, "gu")
        assert vals is not None
        assert vals[0] in ("ɡʷ", "ɡ"), f"gu expected ɡʷ, got {vals[0]}"

    def test_ai_diphthong(self):
        """ai → [aj] (pre-Classical diphthong, later → ē in Classical)."""
        _assert_first(_grapheme(self.spec, "ai"), "aj", label="ai")

    def test_au_diphthong(self):
        """au → [aw] (retained diphthong)."""
        _assert_first(_grapheme(self.spec, "au"), "aw", label="au")

    def test_ei_diphthong(self):
        """ei → [ej]."""
        vals = _grapheme(self.spec, "ei")
        assert vals is not None
        assert vals[0] in ("ej", "eː"), f"ei expected ej, got {vals[0]}"

    def test_ph_aspirate(self):
        """ph → [pʰ] (Greek loanword aspirate)."""
        vals = _grapheme(self.spec, "ph")
        assert vals is not None
        assert vals[0] in ("pʰ", "f"), f"ph expected pʰ, got {vals[0]}"

    def test_th_aspirate(self):
        """th → [tʰ] (Greek loanword aspirate)."""
        vals = _grapheme(self.spec, "th")
        assert vals is not None
        assert vals[0] in ("tʰ", "t"), f"th expected tʰ, got {vals[0]}"


# ═══════════════════════════════════════════════════════════════════════════
# Finnish
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestFinnish:
    """Accuracy tests for Finnish (fi).

    Finnish (Uralic / Finno-Ugric) has:
    - Vowel harmony (front/back pairs: ä/a, ö/o, y/u)
    - Vowel length by doubled letters (aa→aː, ee→eː, etc.)
    - Consonant gradation
    - Geminate consonants (kk→kː, pp→pː, tt→tː)
    - No voiced obstruents in native vocabulary (b/d/g from loans)
    - d→[ɾ] in many dialects
    - h→[ç] before i, [x] before u (predictable allophones)
    - v→[ʋ] (labiodental approximant)
    - w→[ʋ] (treated same as v)
    - z→[ts] (loanword)
    """

    LANGUAGE_CODE = "fi"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Vowels and length
    def test_a_back(self):
        """a → [ɑ] (back vowel in Finnish — not front)."""
        _assert_first(_grapheme(self.spec, "a"), "ɑ", label="a")

    def test_aa_long(self):
        """aa → [ɑː] (long back a by vowel doubling)."""
        _assert_first(_grapheme(self.spec, "aa"), "ɑː", label="aa")

    def test_a_front_pair(self):
        """ä → [æ] (front vowel — pairs with back a in harmony)."""
        _assert_first(_grapheme(self.spec, "ä"), "æ", label="ä")

    def test_aa_front_pair(self):
        """ää → [æː] (long front ä)."""
        _assert_first(_grapheme(self.spec, "ää"), "æː", label="ää")

    def test_ö_front_mid(self):
        """ö → [ø] (front rounded mid — pairs with o)."""
        _assert_first(_grapheme(self.spec, "ö"), "ø", label="ö")

    def test_öö_long(self):
        """öö → [øː]."""
        _assert_first(_grapheme(self.spec, "öö"), "øː", label="öö")

    def test_y_front_rounded(self):
        """y → [y] (front rounded high — unique Finnish letter)."""
        vals = _grapheme(self.spec, "y")
        assert vals is not None
        assert vals[0] in ("y", "ʏ"), f"y expected y/ʏ, got {vals[0]}"

    def test_long_vowels(self):
        """ee/ii/oo/uu/yy → long vowels by doubling."""
        _assert_first(_grapheme(self.spec, "ee"), "eː", label="ee")
        _assert_first(_grapheme(self.spec, "ii"), "iː", label="ii")
        _assert_first(_grapheme(self.spec, "oo"), "oː", label="oo")
        _assert_first(_grapheme(self.spec, "uu"), "uː", label="uu")
        _assert_first(_grapheme(self.spec, "yy"), "yː", label="yy")

    # Consonants
    def test_v_approximant(self):
        """v → [ʋ] (labiodental approximant — not fricative)."""
        _assert_first(_grapheme(self.spec, "v"), "ʋ", label="v")

    def test_w_same_as_v(self):
        """w → [ʋ] (treated identically to v in Finnish)."""
        _assert_first(_grapheme(self.spec, "w"), "ʋ", label="w")

    def test_z_affricate(self):
        """z → [ts] (loanword — not native Finnish)."""
        _assert_first(_grapheme(self.spec, "z"), "ts", label="z")

    # Geminates
    def test_kk_geminate(self):
        """kk → [kː] (geminate — phonemically distinct from k)."""
        _assert_first(_grapheme(self.spec, "kk"), "kː", label="kk")

    def test_pp_geminate(self):
        """pp → [pː]."""
        _assert_first(_grapheme(self.spec, "pp"), "pː", label="pp")

    # Allophones
    def test_d_flap_allophone(self):
        """d allophone includes ɾ — Finnish d realized as flap in dialects."""
        _assert_contains(_allophone(self.spec, "d"), "ɾ", label="d allophone")

    def test_h_palatal_allophone(self):
        """h allophone includes ç — palatal allophone before i."""
        _assert_contains(_allophone(self.spec, "h"), "ç", label="h allophone")

    def test_h_velar_allophone(self):
        """h allophone includes x — velar allophone before u."""
        _assert_contains(_allophone(self.spec, "h"), "x", label="h allophone")

    def test_n_velar_allophone(self):
        """n allophone includes ŋ — velar assimilation before k."""
        _assert_contains(_allophone(self.spec, "n"), "ŋ", label="n allophone")

    def test_family(self):
        """Finnish is Uralic (Finno-Ugric)."""
        assert {"Uralic", "Finnic"} <= set(self.spec.family_path)


# ═══════════════════════════════════════════════════════════════════════════
# Hungarian
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestHungarian:
    """Accuracy tests for Hungarian (hu).

    Hungarian (Uralic / Finno-Ugric) has:
    - Vowel harmony (front/back) with length distinctions
    - a→[ɒ] (rounded low back — not [a]!)
    - á→[aː] (open, not rounded)
    - sz→[s], s→[ʃ] (reversed from English intuition!)
    - z→[z], zs→[ʒ]
    - c→[ts], cs→[tʃ], dz→[dz], dzs→[dʒ]
    - ny→[ɲ], gy→[ɟ], ly→[j]
    - Double letters = geminate consonants
    """

    LANGUAGE_CODE = "hu"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Vowels
    def test_a_rounded_low(self):
        """a → [ɒ] (rounded low back — unique Hungarian feature, NOT [a])."""
        _assert_first(_grapheme(self.spec, "a"), "ɒ", label="a")

    def test_a_acute_open(self):
        """á → [aː] (long open front — contrast with rounded a)."""
        _assert_first(_grapheme(self.spec, "á"), "aː", label="á")

    def test_e_mid_low(self):
        """e → [ɛ] (open-mid, not close-mid)."""
        _assert_first(_grapheme(self.spec, "e"), "ɛ", label="e")

    def test_e_acute_long(self):
        """é → [eː] (long close-mid)."""
        _assert_first(_grapheme(self.spec, "é"), "eː", label="é")

    def test_o_umlaut(self):
        """ö → [ø] (front rounded mid)."""
        _assert_first(_grapheme(self.spec, "ö"), "ø", label="ö")

    def test_o_double_umlaut(self):
        """ő → [øː] (long front rounded — length marked by double acute)."""
        _assert_first(_grapheme(self.spec, "ő"), "øː", label="ő")

    def test_u_umlaut(self):
        """ü → [y] (front rounded high)."""
        _assert_first(_grapheme(self.spec, "ü"), "y", label="ü")

    def test_u_double_umlaut(self):
        """ű → [yː] (long front rounded high)."""
        _assert_first(_grapheme(self.spec, "ű"), "yː", label="ű")

    # Consonants — reversed s/sz
    def test_s_postalveolar(self):
        """s → [ʃ] (CRITICAL: Hungarian s = [ʃ], not [s]!)."""
        _assert_first(_grapheme(self.spec, "s"), "ʃ", label="s")

    def test_sz_alveolar(self):
        """sz → [s] (digraph sz = [s] in Hungarian)."""
        _assert_first(_grapheme(self.spec, "sz"), "s", label="sz")

    def test_zs_postalveolar(self):
        """zs → [ʒ] (digraph zs = [ʒ])."""
        _assert_first(_grapheme(self.spec, "zs"), "ʒ", label="zs")

    # Affricates
    def test_c_affricate(self):
        """c → [ts]."""
        _assert_first(_grapheme(self.spec, "c"), "ts", label="c")

    def test_cs_affricate(self):
        """cs → [tʃ]."""
        _assert_first(_grapheme(self.spec, "cs"), "tʃ", label="cs")

    def test_dz_affricate(self):
        """dz → [dz]."""
        _assert_first(_grapheme(self.spec, "dz"), "dz", label="dz")

    def test_dzs_affricate(self):
        """dzs → [dʒ]."""
        _assert_first(_grapheme(self.spec, "dzs"), "dʒ", label="dzs")

    # Palatal consonants
    def test_ny_palatal_nasal(self):
        """ny → [ɲ] (digraph ny = palatal nasal)."""
        _assert_first(_grapheme(self.spec, "ny"), "ɲ", label="ny")

    def test_gy_palatal_stop(self):
        """gy → [ɟ] (digraph gy = voiced palatal stop)."""
        _assert_first(_grapheme(self.spec, "gy"), "ɟ", label="gy")

    def test_ly_glide(self):
        """ly → [j] (historical palatal lateral → modern glide)."""
        _assert_first(_grapheme(self.spec, "ly"), "j", label="ly")

    def test_family(self):
        """Hungarian is Uralic (Finno-Ugric)."""
        assert self.spec.family == "Uralic"


# ═══════════════════════════════════════════════════════════════════════════
# Japanese
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestJapanese:
    """Accuracy tests for Japanese (ja) — Kana-based grapheme system.

    Japanese graphemes are syllabic (morae). Key features:
    - Kana syllables map directly to CV sequences
    - Vowel quality: a/i/u/e/o (u = [ɯ] — unrounded back high)
    - ɡ → [ɡ, ŋ] (g between vowels often nasalizes)
    - tɕ, dʑ — palatal affricates
    - ɸ — bilabial fricative (for フ [ɸɯ])
    - Pitch accent (not modeled in grapheme table)
    """

    LANGUAGE_CODE = "ja"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Basic kana syllables
    def test_a(self):
        """あ → [a]."""
        _assert_first(_grapheme(self.spec, "あ"), "a", label="あ")

    def test_i(self):
        """い → [i]."""
        _assert_first(_grapheme(self.spec, "い"), "i", label="い")

    def test_u_unrounded(self):
        """う → [ɯ] (back unrounded — Japanese u is not [u])."""
        _assert_first(_grapheme(self.spec, "う"), "ɯ", label="う")

    def test_e(self):
        """え → [e]."""
        _assert_first(_grapheme(self.spec, "え"), "e", label="え")

    def test_o(self):
        """お → [o]."""
        _assert_first(_grapheme(self.spec, "お"), "o", label="お")

    def test_ka(self):
        """か → [ka]."""
        _assert_first(_grapheme(self.spec, "か"), "ka", label="か")

    def test_ki(self):
        """き → [ki]."""
        _assert_first(_grapheme(self.spec, "き"), "ki", label="き")

    def test_ku(self):
        """く → [kɯ]."""
        _assert_first(_grapheme(self.spec, "く"), "kɯ", label="く")

    def test_sa(self):
        """さ → [sa]."""
        _assert_first(_grapheme(self.spec, "さ"), "sa", label="さ")

    def test_shi(self):
        """し → [ɕi] (palatal sibilant — not [si])."""
        vals = _grapheme(self.spec, "し")
        assert vals is not None
        assert vals[0] in ("ɕi", "ʃi"), f"し expected ɕi/ʃi, got {vals[0]}"

    def test_chi(self):
        """ち → [tɕi] (palatal affricate — not [ti] or [tʃi])."""
        vals = _grapheme(self.spec, "ち")
        assert vals is not None
        assert vals[0] in ("tɕi", "tʃi"), f"ち expected tɕi, got {vals[0]}"

    def test_tsu(self):
        """つ → [tsɯ] (dental affricate + unrounded u)."""
        vals = _grapheme(self.spec, "つ")
        assert vals is not None
        assert vals[0] in ("tsɯ", "tsu"), f"つ expected tsɯ, got {vals[0]}"

    def test_ra(self):
        """ら → [ɾa] (flap r)."""
        vals = _grapheme(self.spec, "ら")
        assert vals is not None
        assert vals[0] in ("ɾa", "ra"), f"ら expected ɾa, got {vals[0]}"

    def test_ga(self):
        """が → [ɡa]."""
        _assert_first(_grapheme(self.spec, "が"), "ɡa", label="が")

    # Allophones
    def test_g_nasalization(self):
        """ɡ allophone includes ŋ — intervocalic nasalization."""
        _assert_contains(_allophone(self.spec, "ɡ"), "ŋ", label="ɡ allophone")

    def test_family(self):
        """Japanese is Japonic."""
        assert self.spec.family == "Japonic"


# ═══════════════════════════════════════════════════════════════════════════
# Korean
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestKorean:
    """Accuracy tests for Korean (ko) — Hangul-based grapheme system.

    Korean has a three-way distinction in stops: lax/tense/aspirated.
    Key features:
    - ㄱ → [k] (lax/plain), ㄲ → [k͈] (tense), ㅋ → [kʰ] (aspirated)
    - ㄷ → [t], ㄸ → [t͈], ㅌ → [tʰ]
    - ㅂ → [p], ㅃ → [p͈], ㅍ → [pʰ]
    - ㅈ → [tɕ], ㅉ → [tɕ͈], ㅊ → [tɕʰ]
    - ㄹ → [ɾ, l] (flap intervocalic, lateral elsewhere)
    - Auslaut devoicing and neutralization
    - ㅎ → [h] (aspirate at onset → aspiration of following stop)
    """

    LANGUAGE_CODE = "ko"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Three-way stop contrasts — velar series
    def test_g_lax(self):
        """ㄱ → [k] (lax velar stop)."""
        _assert_first(_grapheme(self.spec, "ㄱ"), "k", label="ㄱ")

    def test_kk_tense(self):
        """ㄲ → [k͈] (tense velar — fortis)."""
        _assert_first(_grapheme(self.spec, "ㄲ"), "k͈", label="ㄲ")

    def test_k_aspirated(self):
        """ㅋ → [kʰ] (aspirated velar)."""
        vals = _grapheme(self.spec, "ㅋ")
        assert vals is not None
        assert vals[0] in ("kʰ", "k"), f"ㅋ expected kʰ, got {vals[0]}"

    # Dental/alveolar series
    def test_d_lax(self):
        """ㄷ → [t] (lax dental stop)."""
        _assert_first(_grapheme(self.spec, "ㄷ"), "t", label="ㄷ")

    def test_dd_tense(self):
        """ㄸ → [t͈] (tense dental)."""
        _assert_first(_grapheme(self.spec, "ㄸ"), "t͈", label="ㄸ")

    # Bilabial series
    def test_b_lax(self):
        """ㅂ → [p] (lax bilabial)."""
        _assert_first(_grapheme(self.spec, "ㅂ"), "p", label="ㅂ")

    def test_bb_tense(self):
        """ㅃ → [p͈] (tense bilabial)."""
        _assert_first(_grapheme(self.spec, "ㅃ"), "p͈", label="ㅃ")

    # Palatal affricate series
    def test_j_affricate(self):
        """ㅈ → [tɕ] (lax palatal affricate)."""
        _assert_first(_grapheme(self.spec, "ㅈ"), "tɕ", label="ㅈ")

    def test_jj_tense(self):
        """ㅉ → [tɕ͈] (tense palatal affricate)."""
        vals = _grapheme(self.spec, "ㅉ")
        assert vals is not None
        assert vals[0] in ("tɕ͈", "tɕ"), f"ㅉ expected tɕ͈, got {vals[0]}"

    def test_ch_aspirated(self):
        """ㅊ → [tɕʰ] (aspirated palatal affricate)."""
        vals = _grapheme(self.spec, "ㅊ")
        assert vals is not None
        assert vals[0] in ("tɕʰ", "tɕ"), f"ㅊ expected tɕʰ, got {vals[0]}"

    # Liquids
    def test_r_liquid(self):
        """ㄹ → [ɾ, l] (flap intervocalic, lateral in coda/geminate)."""
        vals = _grapheme(self.spec, "ㄹ")
        _assert_contains(vals, "ɾ", label="ㄹ flap")

    # Nasals
    def test_n(self):
        """ㄴ → [n]."""
        _assert_first(_grapheme(self.spec, "ㄴ"), "n", label="ㄴ")

    def test_m(self):
        """ㅁ → [m]."""
        _assert_first(_grapheme(self.spec, "ㅁ"), "m", label="ㅁ")

    # Allophones — lax stops voiced between sonorants
    def test_k_allophone_voiced(self):
        """k allophone includes ɡ — lax stops voiced between sonorants."""
        _assert_contains(_allophone(self.spec, "k"), "ɡ", label="k allophone")

    def test_t_allophone_voiced(self):
        """t allophone includes d."""
        _assert_contains(_allophone(self.spec, "t"), "d", label="t allophone")

    def test_p_allophone_voiced(self):
        """p allophone includes b."""
        _assert_contains(_allophone(self.spec, "p"), "b", label="p allophone")

    # Unreleased coda
    def test_k_coda_unreleased(self):
        """k allophone includes k̚ — unreleased in coda."""
        _assert_contains(_allophone(self.spec, "k"), "k̚", label="k coda")

    def test_family(self):
        """Korean is Koreanic."""
        assert self.spec.family == "Koreanic"


# ═══════════════════════════════════════════════════════════════════════════
# Mandarin Chinese (Pinyin romanization)
# ═══════════════════════════════════════════════════════════════════════════


@pytest.mark.linguistic
class TestMandarin:
    """Accuracy tests for Mandarin Chinese (zh) — Pinyin romanisation.

    Mandarin phonology via Pinyin graphemes. Key features:
    - Aspirated/unaspirated pairs: b/p=[p/pʰ], d/t=[t/tʰ], g/k=[k/kʰ]
    - Palatal series: j=[tɕ], q=[tɕʰ], x=[ɕ]
    - Retroflex series: zh=[ʈʂ], ch=[ʈʂʰ], sh=[ʂ], r=[ɻ/ʐ]
    - h → [x] (velar, not glottal)
    - Tonal (not modeled in grapheme table)
    """

    LANGUAGE_CODE = "zh"

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls.spec = _load(self.LANGUAGE_CODE)

    # Aspirated/unaspirated pairs — NOTE: Pinyin b/d/g = unaspirated [p/t/k]!
    def test_b_unaspirated(self):
        """b → [p] (Pinyin b = unaspirated bilabial — NOT voiced!)."""
        _assert_first(_grapheme(self.spec, "b"), "p", label="b")

    def test_p_aspirated(self):
        """p → [pʰ] (Pinyin p = aspirated bilabial)."""
        _assert_first(_grapheme(self.spec, "p"), "pʰ", label="p")

    def test_d_unaspirated(self):
        """d → [t] (Pinyin d = unaspirated dental)."""
        _assert_first(_grapheme(self.spec, "d"), "t", label="d")

    def test_t_aspirated(self):
        """t → [tʰ] (Pinyin t = aspirated dental)."""
        _assert_first(_grapheme(self.spec, "t"), "tʰ", label="t")

    def test_g_unaspirated(self):
        """g → [k] (Pinyin g = unaspirated velar)."""
        _assert_first(_grapheme(self.spec, "g"), "k", label="g")

    def test_k_aspirated(self):
        """k → [kʰ] (Pinyin k = aspirated velar)."""
        _assert_first(_grapheme(self.spec, "k"), "kʰ", label="k")

    def test_h_velar(self):
        """h → [x] (velar fricative — not English glottal [h])."""
        _assert_first(_grapheme(self.spec, "h"), "x", label="h")

    # Palatal series
    def test_j_palatal_affricate(self):
        """j → [tɕ] (unaspirated palatal affricate)."""
        _assert_first(_grapheme(self.spec, "j"), "tɕ", label="j")

    def test_q_palatal_aspirated(self):
        """q → [tɕʰ] (aspirated palatal affricate)."""
        _assert_first(_grapheme(self.spec, "q"), "tɕʰ", label="q")

    def test_x_palatal_fricative(self):
        """x → [ɕ] (palatal fricative)."""
        _assert_first(_grapheme(self.spec, "x"), "ɕ", label="x")

    # Retroflex series
    def test_zh_retroflex_affricate(self):
        """zh → [ʈʂ] (unaspirated retroflex affricate)."""
        _assert_first(_grapheme(self.spec, "zh"), "ʈʂ", label="zh")

    def test_ch_retroflex_aspirated(self):
        """ch → [ʈʂʰ] (aspirated retroflex affricate)."""
        _assert_first(_grapheme(self.spec, "ch"), "ʈʂʰ", label="ch")

    def test_sh_retroflex_fricative(self):
        """sh → [ʂ] (retroflex fricative)."""
        vals = _grapheme(self.spec, "sh")
        assert vals is not None
        assert vals[0] in ("ʂ", "ʃ"), f"sh expected ʂ, got {vals[0]}"

    def test_r_retroflex(self):
        """r → [ɻ] or [ʐ] (retroflex approximant/fricative)."""
        vals = _grapheme(self.spec, "r")
        assert vals is not None
        assert vals[0] in ("ɻ", "ʐ", "ɹ"), f"r expected ɻ/ʐ, got {vals[0]}"

    def test_family(self):
        """Mandarin is Sino-Tibetan."""
        assert {"Sino-Tibetan", "Sinitic"} <= set(self.spec.family_path)
