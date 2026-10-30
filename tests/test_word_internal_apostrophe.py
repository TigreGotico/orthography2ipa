"""An English contraction or possessive is one word, so a whole-word entry is used.

The tokenizer cuts a token at every punctuation mark, and an apostrophe is
punctuation, so ``doesn't`` reached the lexicon as ``doesn`` and ``t``. A spec
declares ``word_internal_apostrophe`` when its orthography writes the mark
inside the word. The expected IPA below is the lexicon entry written in the
test itself, never read back from the engine.
"""
import pytest

import orthography2ipa as o2i
from orthography2ipa.json_loader import load_json_spec

ENTRIES = {"doesn't": "dˈʌzənt", "i'm": "ˈaɪm", "that's": "ðˈæts"}
ENGLISH = {"en-AU", "en-CA", "en-GB", "en-GB-x-scotland", "en-IE", "en-US", "en-ZA"}


@pytest.fixture
def lexicon(tmp_path):
    path = tmp_path / "en-GB.tsv"
    path.write_text("".join(f"{w}\t{ipa}\n" for w, ipa in ENTRIES.items()),
                    encoding="utf-8")
    o2i.clear_lexicons()
    o2i.register_lexicon("en-GB", str(path))
    yield
    o2i.clear_lexicons()


@pytest.mark.parametrize("text, expected", [
    ("doesn't", "dˈʌzənt"),
    ("doesn’t", "dˈʌzənt"),
    ("Doesn't", "dˈʌzənt"),
    ("I'm", "ˈaɪm"),
    ("that's", "ðˈæts"),
])
def test_a_registered_contraction_is_looked_up_whole(lexicon, text, expected):
    assert o2i.transcribe(text, "en-GB") == expected


def test_a_lexicon_entry_inside_a_sentence(lexicon):
    assert o2i.transcribe("that's I'm", "en-GB") == "ðˈæts ˈaɪm"


@pytest.mark.parametrize("word", ["doesn't", "quilter's", "I'm", "that's"])
def test_an_unlisted_contraction_is_one_word_spoken_like_its_letters(word):
    # The apostrophe is silent, so the word reads like its letters without it.
    spoken = o2i.transcribe(word, "en-GB")
    assert " " not in spoken
    assert spoken == o2i.transcribe(word.replace("'", ""), "en-GB")


def test_the_typographic_apostrophe_reads_like_the_ascii_one():
    assert o2i.transcribe("doesn’t", "en-GB") == o2i.transcribe("doesn't", "en-GB")


@pytest.mark.parametrize("code", sorted(ENGLISH))
def test_every_english_spec_declares_or_inherits_it(code):
    assert load_json_spec(code).word_internal_apostrophe is True


def test_no_other_spec_opts_in():
    declared = {code for code in o2i.available_codes()
                if load_json_spec(code).word_internal_apostrophe}
    assert declared == ENGLISH


@pytest.mark.parametrize("lang, text, expected", [
    ("fr-FR", "l'homme", "l ɔm"),
    ("fr-FR", "aujourd'hui", "oʒuʁ ɥi"),
    ("it-IT", "l'amico", "ˈl aˈmiko"),
    ("ca", "l'home", "ˈlɔmə"),
    ("es-ES", "l'a", "ˈl a"),
    ("pt-PT", "d'água", "ˈd ˈaɡwɐ"),
    ("af", "'n man", "ˈə ˈman"),
    ("de-DE", "geht's", "ˈɡeːt ˈz"),
    ("nl-NL", "zo'n", "zɔ n"),
])
def test_an_elision_or_boundary_apostrophe_still_separates(lang, text, expected):
    # Values measured on the tree before the field existed.
    assert o2i.transcribe(text, lang) == expected


@pytest.mark.parametrize("text, expected", [
    ("rock 'n' roll", "ˈɹɒk ˈn ˈɹɒl"),
    ("'tis", "ˈtɪs"),
    ("goin'", "ˈɡɔɪn"),
    ("''quoted''", "ˈkwəʊtɪd"),
])
def test_an_apostrophe_at_a_token_edge_is_not_word_internal(text, expected):
    assert o2i.transcribe(text, "en-GB") == expected


def test_a_closing_quote_after_a_contraction_still_ends_the_word():
    assert o2i.transcribe("it's, 'ok'", "en-GB").split(" ")[0] == o2i.transcribe(
        "its", "en-GB")


def test_the_reported_script_verbatim():
    import os
    import tempfile
    import orthography2ipa as o2i

    o2i.clear_lexicons()
    try:
        lex = os.path.join(tempfile.mkdtemp(), "en.tsv")
        with open(lex, "w", encoding="utf-8") as f:
            f.write("doesn't\tdˈʌzənt\ni'm\tˈaɪm\nthat's\tðˈæts\nhello\thɛlˈəʊ\n")
        o2i.register_lexicon("en", lex)
        got = {w: o2i.transcribe(w, "en")
               for w in ["doesn't", "doesn’t", "I'm", "that's", "hello",
                         "Hello", "quilter's"]}
    finally:
        o2i.clear_lexicons()
    assert got["doesn't"] == "dˈʌzənt"
    assert got["doesn’t"] == "dˈʌzənt"
    assert got["I'm"] == "ˈaɪm"
    assert got["that's"] == "ðˈæts"
    assert got["hello"] == got["Hello"] == "hɛlˈəʊ"
    assert " " not in got["quilter's"]


def _tsv(tmp_path, name, word, ipa):
    path = tmp_path / name
    path.write_text(f"{word}\t{ipa}\n", encoding="utf-8")
    return str(path)


@pytest.mark.parametrize("tag", ["en", "en-GB", "en-gb"])
def test_a_lexicon_registered_under_any_tag_reaches_the_resolved_spec(tmp_path, tag):
    o2i.clear_lexicons()
    try:
        o2i.register_lexicon(tag, _tsv(tmp_path, "a.tsv", "hello", "hɛlˈəʊ"))
        for used in ("en", "en-GB"):
            assert o2i.transcribe("hello", used) == "hɛlˈəʊ"
    finally:
        o2i.clear_lexicons()


def test_two_tags_of_one_spec_share_a_slot_and_the_later_wins(tmp_path):
    o2i.clear_lexicons()
    try:
        o2i.register_lexicon("en-GB", _tsv(tmp_path, "a.tsv", "hello", "fˈɜːst"))
        o2i.register_lexicon("en", _tsv(tmp_path, "b.tsv", "hello", "sˈɛkənd"))
        assert o2i.transcribe("hello", "en-GB") == "sˈɛkənd"
        assert o2i.available_lexicon_codes() == ["en-GB"]
    finally:
        o2i.clear_lexicons()


def test_a_lexicon_dir_file_named_for_the_tag_serves_the_resolved_spec(tmp_path):
    _tsv(tmp_path, "en.tsv", "hello", "bˈaɪ")
    o2i.clear_lexicons()
    try:
        o2i.set_lexicon_dir(tmp_path)
        assert o2i.transcribe("hello", "en-GB") == "bˈaɪ"
        _tsv(tmp_path, "en-GB.tsv", "hello", "ɪɡzˈakt")
        o2i.set_lexicon_dir(tmp_path)
        assert o2i.transcribe("hello", "en") == "ɪɡzˈakt"
    finally:
        o2i.clear_lexicons()


def _unmapped(record):
    from orthography2ipa.exceptions import UnmappedGraphemeWarning
    return [w for w in record if issubclass(w.category, UnmappedGraphemeWarning)]


@pytest.mark.parametrize("lang, text", [
    ("en-GB", "doesn't"),
    ("en-GB", "doesn’t"),
    ("en-GB", "I'm"),
    ("en-GB", "rock'n'roll"),
    ("fr-FR", "l'homme"),
])
def test_an_apostrophe_is_punctuation_and_never_an_unmapped_letter(lang, text):
    import warnings
    from orthography2ipa import G2P
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        G2P(lang).transcribe(text)
    assert _unmapped(record) == []


def test_a_genuinely_unmapped_letter_still_warns_once_in_a_contraction_spec():
    import warnings
    from orthography2ipa import G2P
    engine = G2P("en-GB")
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        engine.transcribe("doesn't ب ب")
    hits = _unmapped(record)
    assert len(hits) == 1
    assert "U+0628" in str(hits[0].message)
