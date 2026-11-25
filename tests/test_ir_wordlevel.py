"""The word-level and analysis methods of G2P run the compiled IR.

Each expected value is the rules engine's recorded output
(``tests/frozen_rules.py``).
"""
import pytest

from orthography2ipa import G2P
from orthography2ipa.exceptions import UnmappedScriptError
from tests.frozen_rules import FrozenRules

WORDS = {
    "pt-PT": ["coração", "guarda-chuva", "casa", "pássaros", "excepção", "d'água", "x1y"],
    "en-US": ["thought", "rough", "the", "co-operate"],
    "hi": ["नमस्ते", "क़लम"],
    "th": ["ภาษาไทย"],
    "ru": ["молоко", "его́"],
    "pa": ["ਅੱਕਣਾ"],
    "ar": ["مُدَرِّس"],
    "ko": ["안녕하세요", "한국어"],
}
CASES = [(code, word) for code, words in WORDS.items() for word in words]
OVERRIDE_CASES = CASES
TEXTS = {"pt-PT": "O rapaz comeu as maçãs, e a avó dormiu.", "en-US": "The rough thought, though."}


def lattice(slots):
    return [(s.grapheme, s.span, [(c.ipa, c.cost) for c in s.candidates]) for s in slots]


@pytest.fixture(scope="module")
def expected():
    """Every expected value, from the rules engine."""
    out = {}
    for code, word in [(c, w) for c, ws in WORDS.items() for w in ws]:
        g = FrozenRules(code, scope="wordlevel")
        out[code, word] = {
            "transcribe_word": g.transcribe_word(word),
            "transcribe_word_beam": g.transcribe_word(word, search="beam"),
            "candidates": [(p.segments, p.score, p.graphemes) for p in g.candidates(word)],
            "ipa_lattice": lattice(g.ipa_lattice(word)),
            "ipa_lattice_2": lattice(g.ipa_lattice(word, beam_width=2)),
            "word_confidence": g.word_confidence(word),
            "confidence_breakdown": g.confidence_breakdown(word),
            "word_candidates": g.word_candidates(word, k=3),
            "features": [f.as_dict() for wf in g.features(word) for f in wf.graphemes],
        }
    for code, text in TEXTS.items():
        g = FrozenRules(code, scope="wordlevel")
        out[code, text] = {
            "sentence_lattice": g.sentence_lattice(text, search="beam"),
            "features": [f.as_dict() for wf in g.features(text) for f in wf.graphemes],
            "confidence": [w.confidence for w in g.transcribe_detailed(text).words],
        }
    return out


@pytest.fixture
def ir():
    engines = {code: G2P(code) for code in WORDS}
    return engines


@pytest.mark.parametrize("code,word", OVERRIDE_CASES)
def test_transcribe_word_runs_the_ir(code, word, expected, ir):
    assert ir[code].transcribe_word(word) == expected[code, word]["transcribe_word"]
    assert ir[code].transcribe_word(word, search="beam") == expected[code, word]["transcribe_word_beam"]


@pytest.mark.parametrize("code,word", CASES)
def test_candidates_run_the_ir(code, word, expected, ir):
    got = [(p.segments, p.score, p.graphemes) for p in ir[code].candidates(word)]
    assert got == expected[code, word]["candidates"]


@pytest.mark.parametrize("code,word", CASES)
def test_ipa_lattice_runs_the_ir(code, word, expected, ir):
    assert lattice(ir[code].ipa_lattice(word)) == expected[code, word]["ipa_lattice"]
    assert lattice(ir[code].ipa_lattice(word, beam_width=2)) == expected[code, word]["ipa_lattice_2"]


@pytest.mark.parametrize("code,word", OVERRIDE_CASES)
def test_confidence_runs_the_ir(code, word, expected, ir):
    assert ir[code].word_confidence(word) == expected[code, word]["word_confidence"]
    assert ir[code].confidence_breakdown(word) == expected[code, word]["confidence_breakdown"]


@pytest.mark.parametrize("code,word", OVERRIDE_CASES)
def test_word_candidates_run_the_ir(code, word, expected, ir):
    assert ir[code].word_candidates(word, k=3) == expected[code, word]["word_candidates"]


@pytest.mark.parametrize("code,word", OVERRIDE_CASES)
def test_features_run_the_ir(code, word, expected, ir):
    got = [f.as_dict() for wf in ir[code].features(word) for f in wf.graphemes]
    assert got == expected[code, word]["features"]


@pytest.mark.parametrize("code", sorted(TEXTS))
def test_sentence_methods_run_the_ir(code, expected, ir):
    text = TEXTS[code]
    want = expected[code, text]
    assert ir[code].sentence_lattice(text, search="beam") == want["sentence_lattice"]
    assert [f.as_dict() for wf in ir[code].features(text) for f in wf.graphemes] == want["features"]
    assert [w.confidence for w in ir[code].transcribe_detailed(text).words] == want["confidence"]


def test_compound_is_one_token_with_one_main_stress(ir):
    ipa = ir["pt-PT"].transcribe_word("guarda-chuva")
    assert " " not in ipa and ipa.count("ˈ") == 1 and ipa.count("ˌ") == 1


def test_unmapped_raises_on_the_ir_route():
    g = G2P("pt-PT", on_unmapped="raise")
    with pytest.raises(UnmappedScriptError):
        g.transcribe_word("x1y")


#: The IR stores each candidate cost as integer millionths, round(cost * 1e6),
#: so a weighted spec reads every cost back within 5e-7 of its -log p.
WEIGHTED = ["mother", "field", "piece", "laugh", "water"]


@pytest.mark.parametrize("word", WEIGHTED)
def test_weighted_costs_are_millionths(word):
    legacy, ir = FrozenRules("en-GB", scope="weighted"), G2P("en-GB")
    want = legacy.ipa_lattice(word)
    want_paths = legacy.candidates(word)
    want_conf = legacy.confidence_breakdown(word)
    assert any(c.cost != int(c.cost) for s in want for c in s.candidates)
    got = ir.ipa_lattice(word)
    assert [(s.grapheme, s.span, [c.ipa for c in s.candidates]) for s in got] == \
        [(s.grapheme, s.span, [c.ipa for c in s.candidates]) for s in want]
    for g, w in zip(got, want):
        for a, b in zip(g.candidates, w.candidates):
            assert a.cost == round(b.cost * 1_000_000) / 1_000_000
    paths = ir.candidates(word)
    assert [p.segments for p in paths] == [p.segments for p in want_paths]
    assert all(abs(a.score - b.score) <= 5e-7 * len(a.segments) for a, b in zip(paths, want_paths))
    conf = ir.confidence_breakdown(word)
    assert conf.per_slot == pytest.approx(want_conf.per_slot, abs=1e-6)
    assert conf.value == pytest.approx(want_conf.value, abs=1e-6)
