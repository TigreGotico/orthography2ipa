"""The pt-BR/vox_communis row: one measured rule, ten notation folds, counted residues.

Word-initial ⟨ex-⟩ before a vowel is [ez] (``PT_INITIAL_EX_VOICED``), the one
rule this gold could measure: 125 of 125 such words carry z in the gold. The
rest of the row is epitran's European Portuguese notation, folded 0.3872 to
0.0389, and the gold's own misreadings of ⟨c ss ch x ou ç⟩, counted. No
`valid_ceiling`: the spelling writes every contrast the folds touch.
"""
import pytest

from orthography2ipa import G2P, json_loader


def test_vox_communis_is_an_audit_not_a_ceiling():
    spec = json_loader.load_json_spec("pt-BR")
    assert "vox_communis" not in (spec.valid_ceiling or {})
    entry = spec.audit["vox_communis"]
    assert entry.conclusion == "at_ceiling_documented"
    for number in ("0.3872", "0.0389", "26426", "981", "125"):
        assert number in entry.measured, number
    assert "fold_pt_br_notation.py" in entry.measured


@pytest.mark.parametrize("word, expected", [
    ("exame", "eˈzami"),
    ("exemplo", "eˈzẽplu"),
    ("êxito", "ˈezitu"),
    ("exército", "eˈzɛɾsitu"),
    ("existir", "ezisˈt͡ʃiɾ"),
])
def test_initial_ex_before_a_vowel_is_voiced(word, expected):
    assert G2P("pt-BR").transcribe_word(word) == expected


@pytest.mark.parametrize("word, expected", [
    ("extra", "ˈeʃtɾɐ"),       # ⟨ex⟩ before a consonant: untouched
    ("sexo", "ˈseʃu"),         # medial ⟨-ex-⟩: untouched
    ("deixar", "dejˈʃaɾ"),     # ⟨x⟩ after a diphthong: ʃ
    ("xadrez", "ʃaˈdɾes"),     # word-initial ⟨x⟩: ʃ
])
def test_the_rule_is_gated_to_the_prefix(word, expected):
    assert G2P("pt-BR").transcribe_word(word) == expected
