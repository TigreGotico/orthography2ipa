"""available_codes() is cached, so each call must return a fresh list."""
from orthography2ipa.json_loader import available_json_codes, load_json_spec
from orthography2ipa.registry import available_codes


def test_a_caller_changing_the_list_does_not_change_the_next_call():
    first = available_codes()
    first.append("not-a-code")
    first.remove(first[0])
    assert "not-a-code" not in available_codes()
    assert available_codes() == sorted(available_codes())


def test_clades_are_left_out_unless_asked_for():
    every = available_codes(include_clades=True)
    assert every == sorted(available_json_codes())
    clades = {code for code in every if load_json_spec(code).clade}
    assert clades
    assert available_codes() == [code for code in every if code not in clades]
