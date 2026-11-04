"""Latin American Spanish has seseo: ⟨c⟩ before ⟨e i⟩ is [s], never [θ].

Lipski, "Geographical and Social Varieties of Spanish: An Overview", p. 4:
"The opposition /s/-/θ/ is not found in the Canary Islands (where seseo is
the norm), nor in any part of Latin America."

The specs below inherited the es-ES distinción rule for ⟨c⟩ while they mapped
⟨z⟩ to [s].
"""
import pytest

from orthography2ipa import available_codes
from orthography2ipa.g2p import G2P

FIXED = ["es-MX", "es-MX-x-costa", "es-GT", "es-NI", "es-PA", "es-PE",
         "es-PE-x-lima", "es-PR", "es-PY", "es-UY", "es-VE"]


@pytest.mark.parametrize("code", FIXED)
@pytest.mark.parametrize("word,expected", [
    ("cielo", "ˈsjelo"),
    ("cinco", "ˈsinko"),
])
def test_c_before_front_vowel_is_s(code, word, expected):
    assert G2P(code).transcribe_word(word) == expected


@pytest.mark.parametrize("code", FIXED)
def test_hacer_has_s(code):
    out = G2P(code).transcribe_word("hacer")
    assert "s" in out and "θ" not in out, out


def _latin_american_spanish():
    # Spain (es-ES and its es-ES-x-* dialects) keeps distinción; Equatorial
    # Guinea is variable by the same source (p. 4), so it is not in this set.
    return sorted(c for c in available_codes()
                  if c.startswith("es-") and not c.startswith("es-ES")
                  and c != "es-GQ")


@pytest.mark.parametrize("code", _latin_american_spanish())
def test_no_latin_american_spec_has_theta(code):
    g = G2P(code)
    for word in ("cielo", "hacer", "cinco", "zapato", "cereza"):
        assert "θ" not in g.transcribe_word(word), (code, word)


def test_latin_american_set_is_complete():
    # The probe above must cover every Latin American spec: es-419 and the
    # national and regional specs.
    codes = _latin_american_spanish()
    assert "es-419" in codes and "es-MX" in codes and "es-UY" in codes
    assert len(codes) >= 46


def test_es_es_keeps_distincion():
    assert G2P("es-ES").transcribe_word("cielo") == "ˈθjelo"
