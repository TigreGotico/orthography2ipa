"""pt-BR epenthesis in a cluster of a stop and an obstruent or a nasal that
opens a stressed word.

Barbosa & Albano (2004: 227) state the vowel for "most two-obstruent
sequences" and break a word-initial one: "psicologia pisɪkoloʒiɐ". The
statement does not restrict the process by stress. Collischonn (1996: 151),
reported by Nascimento (2015: 62-63), puts the vowel after a word-initial
consonant before a stressed nucleus: "pneu [pi'new]". The rule and its full
citation are BR_EPENTHESIS_ONSET in pt-BR.json.

The tests read the inserted [i] after the first consonant, and the stress mark
after it, which are the values the sources give.
"""
import pytest

from orthography2ipa import transcribe


@pytest.mark.parametrize("word", ["pseudo", "psique", "psiu"])
def test_a_stressed_word_initial_obstruent_cluster_is_broken(word):
    assert transcribe(word, "pt-BR").startswith("piˈs")


def test_an_unstressed_word_initial_cluster_keeps_its_rule():
    assert transcribe("psicologia", "pt-BR").startswith("pisi")


def test_a_stop_before_a_nasal_is_broken():
    """Romano & Seabra (2017: 284-285) find the vowel of pneu in every ALiB
    response from Paraná and São Paulo, [e] in 80.37 % of them (p. 286)."""
    assert transcribe("pneu", "pt-BR")[1] in "ie"


def test_the_vowel_before_a_nasal_is_oral_and_pretonic():
    """Collischonn (1996: 151), reported by Nascimento (2015: 62-63): "pneu [pi'new]"."""
    assert transcribe("pneu", "pt-BR") == "piˈnew"


def test_a_written_stressed_i_before_a_nasal_stays_nasal():
    """Barbosa & Albano (2004: 229): "(em) cima sĩmɐ"."""
    assert transcribe("cima", "pt-BR") == "ˈsĩmɐ"


@pytest.mark.parametrize("code", [
    "pt-BR-x-sp", "pt-BR-x-rj", "pt-BR-x-sul", "pt-BR-x-floripa", "pt-BR-x-pr",
])
def test_the_regional_specs_inherit_the_rule(code):
    """Collischonn (2004: 65) gives no rate for the word-initial position."""
    assert transcribe("pseudo", code).startswith("piˈs")


@pytest.mark.parametrize("word", ["tchau", "tchauzinho", "tchê"])
def test_tch_writes_one_affricate(word):
    """pt.wiktionary gives tchau as /tʃaʊ/: no vowel between [t] and [ʃ]."""
    assert transcribe(word, "pt-BR").lstrip("ˈ").startswith("tʃ")


@pytest.mark.parametrize("word", ["tchau", "tchauzinho"])
def test_tch_takes_no_vowel_where_ch_is_an_affricate(word):
    """pt-BR-x-cuiaba reads ⟨ch⟩ as [t͡ʃ]; the [t] of ⟨tch⟩ still takes no vowel."""
    assert transcribe(word, "pt-BR-x-cuiaba").lstrip("ˈ")[1] != "i"


def test_dj_is_broken():
    """Collischonn (1996: 151), reported by Nascimento (2015: 63): "Djavan [dʒiʒa'vã]"."""
    assert transcribe("Djavan", "pt-BR").replace("ˈ", "").startswith("d͡ʒiʒ")


def test_uruguayan_portuguese_keeps_its_output():
    """pt-UY switches the BR_EPENTHESIS rules off: no source on the border variety states them."""
    assert transcribe("pseudo", "pt-UY") == "ˈpsewdu"
