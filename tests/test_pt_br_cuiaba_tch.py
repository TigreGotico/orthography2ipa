"""Cuiabá Portuguese reads ⟨tch⟩ as one affricate, not as [t] plus [t͡ʃ].

pt.wiktionary gives tchau as "/tʃaʊ/". CUIABA_AFFRIC_SH makes an onset ⟨ch⟩
the affricate [t͡ʃ] (Almeida 2004: 155, "[tSe»ga] chegar"), so after the [t]
of the ⟨t⟩ it gave a doubled stop. CUIABA_TCH_SH keeps the ⟨ch⟩ of ⟨tch⟩ as
[ʃ], and the spec writes the affricate as pt-BR does.
"""
import pytest

from orthography2ipa import transcribe
from orthography2ipa.json_loader import load_json_spec


def test_tchau_has_one_affricate():
    assert transcribe("tchau", "pt-BR-x-cuiaba").lstrip("ˈ")[:3] == "tʃa"


@pytest.mark.parametrize("word, onset", [("chegar", "t͡ʃe"), ("chave", "t͡ʃa")])
def test_a_ch_without_t_stays_the_affricate(word, onset):
    assert transcribe(word, "pt-BR-x-cuiaba").lstrip("ˈ").startswith(onset)


def test_cuiaba_writes_tchau_as_pt_br_does():
    assert transcribe("tchau", "pt-BR-x-cuiaba") == transcribe("tchau", "pt-BR")


def test_the_rule_stands_before_the_affricate_rule():
    ids = [r.id for r in load_json_spec("pt-BR-x-cuiaba").allophone_rules]
    assert ids.index("CUIABA_TCH_SH") < ids.index("CUIABA_AFFRIC_SH")
