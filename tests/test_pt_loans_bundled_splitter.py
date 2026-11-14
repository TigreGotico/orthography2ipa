"""Loans and foreign names that the bundled splitter reads wrong.

The Portuguese spelling rules do not reach these words. The value each one should
give comes from the gold entry named beside it. A word that starts to pass here
has gained a rule, so the entry moves to a real test.
"""
import pytest

from orthography2ipa import G2P

# (lang, word, the part of the transcription the gold gives, gold entry)
STRESS = [
    ("pt-BR", "alamein", "ˈmej̃", "ipadict a.la.ˈmeĩ"),
    ("pt-BR", "bitcoin", "ˈk", "portuguese_unified bitˈkɔĩ"),
    ("pt-BR", "edelstein", "ˈtej̃", "ipadict e.dʒels.ˈteĩ"),
    ("pt-BR", "epstein", "ˈtej̃", "ipadict eps.ˈteĩ"),
    ("pt-BR", "iain", "ˈaj̃", "ipadict i.ˈaĩ"),
    ("pt-BR", "upstairs", "ˈta", "ipadict upʃ.ˈta.ɪxs"),
    ("pt-PT", "background", "ˈɡɾ", "portuguese_unified bɛkˈɡrawnd"),
    ("pt-PT", "bitcoin", "ˈk", "portuguese_unified bitˈkɔin"),
    ("pt-PT", "blockchain", "ˈʃ", "portuguese_unified blɔkˈʃɐj̃"),
    ("pt-PT", "gourmet", "ˈm", "portuguese_unified ɡurˈme"),
]
VOWEL = [
    ("pt-PT", "abanico-das-visayas", "za", "portuguese_unified ɐbɐnikudɐʃviˈzajɐʃ"),
    ("pt-PT", "abhinaya", "na", "wikipron ɐ b i n a j ɐ"),
    ("pt-PT", "ambayba", "ba", "wikipron ɐ̃ b a j b ɐ"),
    ("pt-PT", "apapane-de-laysan", "la", "portuguese_unified ɐpapɐndəlajˈzɐn"),
    ("pt-PT", "braille", "ɾa", "wikipron b ɾ a j l ɨ"),
    ("pt-PT", "centigray", "ɾɐ", "portuguese_unified sẽtiˈɡrɐj"),
    ("pt-PT", "cosplay", "kɔ", "wikipron k ɔ ʃ p l e"),
    ("pt-PT", "display", "lɐ", "portuguese_unified diʃˈplɐj"),
    ("pt-PT", "joystick", "ʒɔ", "portuguese_unified ʒɔjsˈtik"),
    ("pt-PT", "tramway", "wɐ", "portuguese_unified ˈtrɐmwɐj"),
]


@pytest.mark.xfail(strict=True, reason="a loan outside the Portuguese stress rules")
@pytest.mark.parametrize("lang,word,expected,gold", STRESS)
def test_loan_stress(lang, word, expected, gold):
    assert expected in G2P(lang).transcribe_word(word)


@pytest.mark.xfail(strict=True, reason="a loan outside the Portuguese vowel rules")
@pytest.mark.parametrize("lang,word,expected,gold", VOWEL)
def test_loan_vowel(lang, word, expected, gold):
    assert expected in G2P(lang).transcribe_word(word).replace("ˈ", "").replace("ˌ", "")
