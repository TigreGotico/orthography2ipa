"""A lexicon entry is keyed by the spelling before ``mark`` (#2643)."""
import pytest

from orthography2ipa import G2P, Pipeline

LEX = {"equitativo": "ekwitɐˈtivu", "müller": "ˈmylɛɾ"}


def mark(text):
    return text.replace("equitativo", "eqüitativo").replace("Equitativo", "Eqüitativo")


def g2p(lexicon=LEX, mark=mark):
    return G2P("pt-PT", pipeline=Pipeline(lexicon=lexicon, mark=mark))


def test_a_marked_word_gets_the_entry_of_its_spelling_before_mark():
    assert g2p().transcribe("equitativo") == "ekwitɐˈtivu"


def test_a_capitalised_marked_word_gets_its_entry():
    assert g2p().transcribe("Equitativo") == "ekwitɐˈtivu"


def test_the_marked_word_counts_as_a_lexicon_hit():
    word, = g2p().transcribe_detailed("equitativo").words
    assert word.confidence == word.coverage


def test_a_marked_word_with_no_entry_goes_to_the_rules_as_marked():
    rules = G2P("pt-PT").transcribe("eqüitativo")
    assert g2p(lexicon={}).transcribe("equitativo") == rules
    assert rules != "ekwitɐˈtivu"


def test_no_fold_a_real_diaeresis_key_stays_a_key():
    assert g2p(mark=lambda t: t).transcribe("Müller") == "ˈmylɛɾ"
    assert g2p(lexicon={"muller": "x"}).transcribe("Müller") != "x"


def test_a_mark_that_changes_the_letters_raises():
    with pytest.raises(ValueError, match="the mark stage changed"):
        g2p(mark=lambda t: t.replace("equitativo", "iquitativo")).transcribe("equitativo")


def test_a_mark_that_splits_a_word_raises():
    with pytest.raises(ValueError, match="the mark stage changed"):
        g2p(mark=lambda t: t.replace("equitativo", "equi tativo")).transcribe("equitativo")


def test_interpreter_runs_whose_words_differ_raise():
    it = G2P("pt-PT")._interpreter
    with pytest.raises(ValueError, match="the mark stage made 2 words of the 1 words"):
        it.transcribe_runs([("equi tativo", None, "equitativo")], lexicon=LEX)
