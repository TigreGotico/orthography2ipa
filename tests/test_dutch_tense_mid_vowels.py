"""Netherlandic Dutch /eː øː oː/ are closing diphthongs; Belgian Dutch keeps monophthongs.

Sources:

- C. Gussenhoven, "Dutch", *Journal of the International Phonetic
  Association* 22(1-2), 1992, p. 46: "/eː, øː, oː/ are narrow closing
  diphthongs ([ei, øy, ou]), except before /r/ in the same word, when they
  are pronounced [eᵊ, øᵊ, oᵊ]". The vowel chart on the same page gives beet,
  neus and boot for the three vowels, and /ɛi/ for ⟨ei⟩.
- J. Verhoeven, "Belgian Standard Dutch", *JIPA* 35(2), 2005, pp. 245-246:
  "In the Netherlands, these are frequently diphthongized. In Belgian Dutch,
  however, they are always monophthongs."

The other segments keep the values the specs state elsewhere.
"""
import pytest

from orthography2ipa import G2P

GAP = pytest.mark.xfail(strict=True, reason="known gap: the root reads as the unstressed prefix be- or ge-")


@pytest.fixture(scope="module")
def nl():
    return G2P("nl-NL")


@pytest.fixture(scope="module")
def be():
    return G2P("nl-BE")


@pytest.mark.parametrize("word, ipa", [
    ("beet", "ˈbeit"),
    ("neus", "ˈnøys"),
    ("boot", "ˈbout"),
    ("zee", "ˈzei"),
    ("café", "ˈkaːfei"),
])
def test_nl_nl_long_mid_vowel_is_a_closing_diphthong(nl, word, ipa):
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    pytest.param("beten", "ˈbeitən", marks=GAP),
    ("neuzen", "ˈnøyzən"),
    ("boten", "ˈboutən"),
])
def test_nl_nl_open_syllable_e_eu_o_is_a_closing_diphthong(nl, word, ipa):
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("meer", "ˈmeᵊɹ"),
    ("deur", "ˈdøᵊɹ"),
    ("door", "ˈdoᵊɹ"),
    ("leren", "ˈleᵊrən"),
    ("veertig", "ˈveᵊɹtɪχ"),
    ("ingenieur", "ˈɪŋənjøᵊɹ"),
])
def test_nl_nl_long_mid_vowel_before_r_has_a_centring_glide(nl, word, ipa):
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word, ipa", [
    ("mooi", "ˈmoːi"),
    ("kooien", "ˈkoːin"),
    ("leeuw", "ˈleːu"),
    ("hooischelf", "ˈɦoːisəlf"),
])
def test_nl_nl_eeuw_and_ooi_keep_the_long_vowel(nl, word, ipa):
    # ⟨eeuw⟩ keeps the Paardekooper value; ⟨ooi⟩ is a stated gap: no opened source gives its realisation.
    assert nl.transcribe(word) == ipa


def test_nl_nl_ee_stays_apart_from_ij(nl):
    # beet [beit] against bijt [bɛit]: the chart keeps /eː/ and /ɛi/ apart.
    assert nl.transcribe("beet") != nl.transcribe("bijt")
    assert nl.transcribe("bijt") == "ˈbɛit"


@pytest.mark.parametrize("word, ipa", [
    ("beet", "ˈbeːt"),
    ("neus", "ˈnøːs"),
    ("boot", "ˈboːt"),
    pytest.param("beten", "ˈbeːtən", marks=GAP),
    ("meer", "ˈmeːr̥"),
    ("door", "ˈdoːr̥"),
])
def test_nl_be_long_mid_vowel_is_a_monophthong(be, word, ipa):
    assert be.transcribe(word) == ipa


@pytest.mark.parametrize("spec", ["nl-NL", "nl-BE"])
def test_one_mid_vowel_series_per_spec(spec):
    out = "".join(G2P(spec).transcribe(w) for w in ("beet", "neus", "boot", "meer", "beten"))
    if spec == "nl-NL":
        assert "ː" not in out
    else:
        assert not set("ᵊ") & set(out) and "ei" not in out and "ou" not in out


def test_af_keeps_its_own_long_vowels():
    # af states its long vowels itself (Wissing 2020); the nl-NL rules must not reach them.
    assert G2P("af").transcribe("café") == "ˈkafeː"
