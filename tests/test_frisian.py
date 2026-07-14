"""Per-language accuracy tests for West Frisian (fy / fry).

West Frisian (Frysk) is the West Germanic Anglo-Frisian variety of Fryslân,
Netherlands. Its hard part is the vowel system: length contrasts, falling
diphthongs, and the centring ("breaking") diphthongs /iə ɪə oə/. On the
consonant side the load-bearing facts are ⟨g⟩ = [ɡ]~[ɣ] allophony with
final devoicing to [χ], the palatalisations ⟨sj⟩ /ɕ/ and ⟨tsj⟩/⟨tj⟩ /tɕ/,
and ⟨ch⟩ /χ/.

Sources: Tiersma (1999) *Frisian Reference Grammar*; Hoekstra (2001) *Standard
West Frisian*; Wikipedia "West Frisian phonology" and "Help:IPA/West Frisian".

Run with:
    pytest tests/test_frisian.py -v --tb=short
"""
from __future__ import annotations

import pytest
import orthography2ipa


def _load(code: str):
    try:
        return orthography2ipa.get(code)
    except Exception as exc:  # pragma: no cover - availability guard
        pytest.skip(f"{code!r} not available: {exc}")


def _grapheme(spec, grapheme: str) -> list:
    return spec.graphemes.get(grapheme, [])


def _allophone(spec, phoneme: str):
    return spec.allophones.get(phoneme)


def _first(values, expected: str, label: str = "") -> None:
    assert values, f"{label}: empty/absent mapping"
    assert values[0] == expected, f"{label}: expected first={expected!r}, got {values[0]!r}"


def _contains(values, *expected, label: str = "") -> None:
    assert values is not None, f"{label}: mapping is absent"
    for exp in expected:
        assert exp in values, f"{label}: {exp!r} not in {values!r}"


def _tx(word: str) -> str:
    return orthography2ipa.transcribe(word, "fy").replace("ˈ", "")


@pytest.mark.linguistic
class TestWestFrisian:
    """Accuracy tests for West Frisian (fy)."""

    @pytest.fixture(autouse=True, scope="class")
    def spec(self, request):
        request.cls._spec = _load("fy")

    # --- Registry / classification ---

    def test_code(self):
        """The spec code round-trips to fy."""
        assert self._spec.code == "fy"

    def test_iso639_3(self):
        """West Frisian is ISO 639-3 'fry'."""
        assert self._spec.iso639_3 == "fry"

    def test_family(self):
        """West Frisian is West Germanic (Anglo-Frisian)."""
        assert {"Indo-European", "Germanic", "West Germanic"} <= set(self._spec.family_path)

    def test_script(self):
        """West Frisian is written in the Latin script."""
        assert self._spec.script == "Latin"

    # --- Monophthongs ---

    def test_short_a_is_front(self):
        """<a> is the short front /a/, e.g. *pak* (Help:IPA/West Frisian; phonology table)."""
        _first(_grapheme(self._spec, "a"), "a", label="fy a")

    def test_aa_is_long(self):
        """<aa> is long /aː/, considerably longer than short <a> (Tiersma 1999, p. 9)."""
        _first(_grapheme(self._spec, "aa"), "aː", label="fy aa")

    def test_i_is_lax(self):
        """<i> is the short lax /ɪ/ (phonology monophthong table)."""
        _first(_grapheme(self._spec, "i"), "ɪ", label="fy i")

    def test_y_is_the_close_i(self):
        """<y> spells the vowel /i/ (a vowel, not a glide), e.g. *dyk* /dik/."""
        _first(_grapheme(self._spec, "y"), "i", label="fy y")
        assert _tx("dyk") == "dik"

    def test_u_is_front_rounded(self):
        """<u> is the front rounded /ø/ (phonology monophthong table)."""
        _first(_grapheme(self._spec, "u"), "ø", label="fy u")

    def test_circumflex_vowels(self):
        """Circumflex vowels: <â> /ɔː/, <ê> /ɛː/, <ô> /oː/, <û> /uː/ (Tiersma 1999)."""
        _first(_grapheme(self._spec, "â"), "ɔː", label="fy â")
        _first(_grapheme(self._spec, "ê"), "ɛː", label="fy ê")
        _first(_grapheme(self._spec, "ô"), "oː", label="fy ô")
        _first(_grapheme(self._spec, "û"), "uː", label="fy û")

    # --- Centring (breaking) diphthongs ---

    def test_ie_centring(self):
        """<ie> is the centring diphthong /iə/, e.g. *stien* 'stone' (phonology table)."""
        _first(_grapheme(self._spec, "ie"), "iə", label="fy ie")
        assert _tx("stien") == "stiən"

    def test_ea_centring(self):
        """<ea> is /ɪə/, e.g. *beam* 'tree' (phonology table)."""
        _first(_grapheme(self._spec, "ea"), "ɪə", label="fy ea")
        assert _tx("beam") == "bɪəm"

    def test_oa_centring(self):
        """<oa> is /oə/, e.g. *doas* 'box' (phonology table)."""
        _first(_grapheme(self._spec, "oa"), "oə", label="fy oa")
        assert _tx("doas") == "doəs"

    # --- Falling diphthongs and long-vowel+glide sequences ---

    def test_ei_diphthong(self):
        """<ei> is /ɛi/, e.g. *dei* 'day' (Help:IPA/West Frisian)."""
        _first(_grapheme(self._spec, "ei"), "ɛi", label="fy ei")
        assert _tx("dei") == "dɛi"

    def test_ou_diphthong(self):
        """<ou> is /ɔu/, e.g. *goud* 'gold' (Help:IPA/West Frisian)."""
        _first(_grapheme(self._spec, "ou"), "ɔu", label="fy ou")

    def test_aai_long_plus_glide(self):
        """<aai> is /aːj/ (long vowel + glide), e.g. *aai* 'egg' (Hoekstra & Tiersma)."""
        _first(_grapheme(self._spec, "aai"), "aːj", label="fy aai")
        assert _tx("aai") == "aːj"

    def test_iuw_long_plus_glide(self):
        """<iuw> is /iːw/ (long vowel + glide) (Hoekstra & Tiersma)."""
        _first(_grapheme(self._spec, "iuw"), "iːw", label="fy iuw")

    # --- Consonants ---

    def test_sj_is_alveolopalatal(self):
        """<sj> coalesces to the alveolo-palatal fricative /ɕ/, e.g. *sjippe*."""
        _first(_grapheme(self._spec, "sj"), "ɕ", label="fy sj")
        assert _tx("sjippe").startswith("ɕ")

    def test_tsj_is_alveolopalatal_affricate(self):
        """<tsj> is the alveolo-palatal affricate /tɕ/, e.g. *tsjerke* 'church'."""
        _first(_grapheme(self._spec, "tsj"), "tɕ", label="fy tsj")
        assert _tx("tsjerke").startswith("tɕ")

    def test_tj_is_alveolopalatal_affricate(self):
        """<tj> is /tɕ/, e.g. *laitsje* (Help:IPA/West Frisian)."""
        _first(_grapheme(self._spec, "tj"), "tɕ", label="fy tj")

    def test_ch_is_uvular_fricative(self):
        """<ch> is the voiceless post-velar/uvular fricative /χ/, e.g. *sûch*."""
        _first(_grapheme(self._spec, "ch"), "χ", label="fy ch")
        assert _tx("sûch") == "suːχ"

    def test_g_onset_is_stop(self):
        """<g> word-initially is the stop [ɡ], e.g. *goed* (Hoekstra 2001)."""
        assert _tx("goed").startswith("ɡ")

    def test_g_intervocalic_is_fricative(self):
        """<g> between vowels is the voiced velar fricative [ɣ], e.g. *drege* (Hoekstra 2001)."""
        assert "ɣ" in _tx("drege"), _tx("drege")

    def test_g_final_devoices_to_uvular(self):
        """Final-devoicing merges word-final /ɣ/ to [χ] (Tiersma 1999, p. 21)."""
        a = _allophone(self._spec, "ɣ")
        _contains(a, "ɣ", "χ", label="fy allophone ɣ")

    def test_final_devoicing_d(self):
        """Word-final /d/ devoices to [t], e.g. *goed* /ɡuːt/ (Tiersma 1999, p. 21)."""
        assert _tx("goed").endswith("t")

    # --- Stress ---

    def test_stress_is_root_initial(self):
        """Germanic stress falls on the first syllable of the root (Tiersma 1999)."""
        assert self._spec.stress is not None
        assert self._spec.stress.default_position == 1
        assert orthography2ipa.transcribe("tiisdei", "fy").startswith("ˈ")

    def test_diphthongs_declared(self):
        """The vocalic digraphs are declared so the syllabifier counts one nucleus each."""
        diph = set(self._spec.stress.diphthongs)
        assert {"ie", "ea", "oa", "ei", "ou"} <= diph
