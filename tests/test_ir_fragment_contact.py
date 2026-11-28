"""The contact fragment part (docs/ir/o2i-ir-v1.md, 3.5.1)."""
import pytest

from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir
from orthography2ipa.ir.interpreter import Interpreter


def _frag(**entry):
    return {"ir_version": 1, "langs": ["arz-EG"],
            "contact": [{"script": "Latn", "donor": "en-GB", **entry}]}


@pytest.fixture(scope="module")
def donor():
    return Interpreter(layout.encode(build_ir("en-GB")))


def _it(donor, donor_words=None, **entry):
    ir = build_ir("arz-EG", fragments=[_frag(**entry)])
    return Interpreter(layout.encode(ir), donors={"en-GB": (donor, donor_words or {})})


def test_a_contact_word_takes_its_listed_reading_through_the_map(donor):
    it = _it(donor, words={"jam": "dʒam"}, map={"dʒ": "ɡ"})
    assert it.transcribe("jam") == "ɡam"


def test_the_contact_word_wins_over_the_donor_word(donor):
    it = _it(donor, {"jam": "zzz"}, words={"jam": "dʒam"}, map={"dʒ": "ɡ"})
    assert it.transcribe("Jam") == "ɡam"


def test_a_donor_word_is_read_when_no_contact_word_lists_it(donor):
    it = _it(donor, {"bank": "bank"}, rewrite=[{"pattern": "k$", "template": "ʔ"}])
    assert it.transcribe("bank") == "banʔ"


def test_the_stress_marks_of_the_donor_reading_are_dropped(donor):
    it = _it(donor, {"salad": "ˈsaˌlad"})
    assert it.transcribe("salad") == "salad"


def test_the_longest_map_key_is_taken_first(donor):
    it = _it(donor, words={"chat": "tʃat"}, map={"tʃ": "ʃ", "t": "t"})
    assert it.transcribe("chat") == "ʃat"


def test_an_arabic_word_keeps_the_lect_reading(donor):
    plain = Interpreter(layout.encode(build_ir("arz-EG")))
    assert _it(donor, words={"jam": "dʒam"}).transcribe("كتاب") == plain.transcribe("كتاب")


def test_a_fragment_for_another_lect_does_not_reach_arz_eg():
    frag = {**_frag(), "langs": ["apc"]}
    assert "contact" not in build_ir("arz-EG", fragments=[frag])


@pytest.mark.parametrize("entry, message", [
    ({"donor": "xx-nope"}, "names no registered language"),
    ({"colour": 1}, "is not supported"),
    ({"words": {"Jam": "dʒam"}}, "lowercase NFC"),
    ({"map": {"dʒ": "ʒ̃"}}, "is not in the phoneme set"),
])
def test_a_malformed_contact_entry_fails_to_compile(entry, message):
    with pytest.raises(ValueError, match=message):
        build_ir("arz-EG", fragments=[_frag(**entry)])


def test_a_missing_donor_interpreter_is_an_error():
    it = Interpreter(layout.encode(build_ir("arz-EG", fragments=[_frag()])))
    with pytest.raises(ValueError, match="no donor interpreter for en-GB"):
        it.transcribe("jam")


def test_the_loom_export_refuses_a_contact_fragment():
    from orthography2ipa.export_to_loom import compile_irs
    with pytest.raises(ValueError, match="no donor table"):
        compile_irs(["arz-EG"], None, [_frag()])
