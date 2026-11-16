"""Highland Ecuadorian Spanish keeps ⟨ll⟩ and ⟨y⟩ apart: ⟨ll⟩ [ʒ], ⟨y⟩ [ʝ].

Lipski, "Geographical and Social Varieties of Spanish: An Overview", p. 5:
"In Quito and other northern highland areas of Ecuador, the lateral
pronunciation of /ʎ/ gives way to a groove fricative pronunciation [ʒ], but
the opposition /ʎ/-/ʝ/ is still maintained (e.g., halla [ˈa.ʒa] 'he/she finds'
– haya [ˈa.ʝa] 'that he/she may have')."
"""
import pytest

from orthography2ipa.g2p import G2P

CODE = "es-EC-x-andino"


@pytest.mark.parametrize("word,expected", [
    ("halla", "ˈaʒa"),
    ("haya", "ˈaʝa"),
    ("calle", "ˈkaʒe"),
    ("ya", "ˈʝa"),
    ("yo", "ˈʝo"),
])
def test_ll_is_groove_fricative_and_y_is_palatal(word, expected):
    assert G2P(CODE).transcribe_word(word) == expected


def test_halla_haya_minimal_pair():
    g = G2P(CODE)
    assert g.transcribe_word("halla") != g.transcribe_word("haya")


def test_y_outside_onset_stays_vocalic():
    assert G2P(CODE).transcribe("y") == "i"
