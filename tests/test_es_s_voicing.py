"""Spanish /s/ is voiced before a voiced consonant.

Martínez-Celdrán, Fernández-Planas & Carrera-Sabaté (2003), "Castilian
Spanish", JIPA 33(2), p. 258: "[θ] has an interdental place of articulation.
This fricative, like [s], becomes voiced before a voiced consonant. For
instance, rasgo ‘feature’ [ˈrazɣo]". The rule note of ES_S_VOICING in es-ES
holds the quote. The source describes the Castilian standard, so every
other spec switches the rule off: the American and Equatorial Guinean specs
wait on a source of their own, and the specs that aspirate or delete a coda
/s/ keep their own reading.
"""
import pytest

from orthography2ipa.g2p import G2P


@pytest.mark.parametrize("word, expected", [
    ("rasgo", "ˈrazɣo"),  # the source's own example
    ("mismo", "ˈmizmo"),
    ("desde", "ˈdezðe"),
    ("isla", "ˈizla"),
    ("asno", "ˈazno"),
    ("esbelto", "ezˈβelto"),
])
def test_s_voiced_before_voiced_consonant(word, expected):
    assert G2P("es-ES").transcribe_word(word) == expected


@pytest.mark.parametrize("word, expected", [
    ("este", "ˈeste"),
    ("asco", "ˈasko"),
    ("espera", "esˈpeɾa"),
])
def test_s_stays_voiceless_before_voiceless_consonant(word, expected):
    assert G2P("es-ES").transcribe_word(word) == expected


@pytest.mark.parametrize("lang", ["es", "es-ES-x-cantabri"])
def test_castilian_specs_take_the_rule(lang):
    assert G2P(lang).transcribe_word("mismo") == "ˈmizmo"


@pytest.mark.parametrize("lang", [
    "es-419", "es-MX", "es-MX-x-norte", "es-AR", "es-AR-x-cuyo", "es-CO",
    "es-CL-x-chilote", "es-PE-x-lima", "es-VE-x-zulia", "es-GQ",
])
def test_specs_outside_the_source_keep_the_voiceless_sibilant(lang):
    assert G2P(lang).transcribe_word("mismo") == "ˈmismo"


@pytest.mark.parametrize("lang", ["es-SV", "es-CU", "es-ES-x-andalusi-w", "es-CO-x-costa"])
def test_aspirating_specs_keep_the_aspirate(lang):
    assert G2P(lang).transcribe_word("mismo") == "ˈmihmo"


def test_deleting_spec_keeps_the_deletion():
    assert G2P("es-CO-x-pacifico").transcribe_word("mismo") == "ˈmimo"
