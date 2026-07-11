"""Tests for the E3 lexicon-overlay mechanism (orthography2ipa/lexicon.py).

Covers the four contract gates:

- **Lazy load** — importing the package (and loading a spec) reads no lexicon
  file; the first transcription for a language triggers exactly one read.
- **Precedence** — inline ``word_exceptions`` > sidecar lexicon > rules.
- **Stress** — a lexicon hit still routes through the ``word_exceptions``
  pathway, so stress marks are applied (for a spec that declares stress).
- **Data quality** — every shipped ``data/lexicons/*.tsv`` is clean (format,
  NFC, lowercase, IPA-only, sorted, no duplicates).
- **Byte-identical** — a language with no lexicon file is unchanged.
"""
import subprocess
import sys
import unicodedata

import pytest

import orthography2ipa
from orthography2ipa import g2p as g2p_module
from orthography2ipa import lexicon as lexmod


# ─── lazy load ───────────────────────────────────────────────────────────────

def test_import_and_spec_load_read_no_lexicon():
    """A fresh interpreter: importing the package and loading a spec must NOT
    read any lexicon file; the first transcribe() triggers exactly one read.

    Run in a subprocess so the process-global lru_cache is pristine (other
    tests in this session will have populated it otherwise).
    """
    script = (
        "import orthography2ipa as o\n"
        "from orthography2ipa import lexicon as L\n"
        # import alone: nothing cached
        "assert L.get_lexicon.cache_info().misses == 0, 'read at import'\n"
        # loading a LanguageSpec must not read a lexicon either
        "spec = o.get('en-GB')\n"
        "assert L.get_lexicon.cache_info().misses == 0, 'read at spec load'\n"
        # first transcription triggers the (single) lazy read
        "o.G2P('en-GB').transcribe_word('nature')\n"
        "info = L.get_lexicon.cache_info()\n"
        "assert info.misses == 1, info\n"
        "print('OK')\n"
    )
    out = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True, text=True,
    )
    assert out.returncode == 0, out.stderr
    assert "OK" in out.stdout


def test_get_lexicon_cached_single_read():
    """Repeated get_lexicon() for the same code does not re-read the file."""
    lexmod.get_lexicon.cache_clear()
    a = lexmod.get_lexicon("en-GB")
    b = lexmod.get_lexicon("en-GB")
    assert a is b  # identical cached object, not re-parsed
    assert lexmod.get_lexicon.cache_info().misses == 1


def test_absent_lexicon_returns_empty_map():
    assert lexmod.get_lexicon("pt-PT") == {}
    assert lexmod.get_lexicon("zz-NONEXISTENT") == {}


# ─── shipped pilot ───────────────────────────────────────────────────────────

def test_en_pilot_ships_and_is_used():
    assert "en-GB" in lexmod.available_lexicon_codes()
    lex = lexmod.get_lexicon("en-GB")
    assert 0 < len(lex) <= 5000
    # a lexicon word transcribes to its lexicon IPA
    eng = orthography2ipa.G2P("en-GB")
    assert eng.transcribe_word("nature") == lex["nature"]
    # bare "en" resolves to the en-GB spec and shares the lexicon
    assert orthography2ipa.G2P("en").transcribe_word("nature") == lex["nature"]


# ─── precedence: inline > lexicon > rules ───────────────────────────────────

def test_lexicon_beats_rules(monkeypatch):
    """A word only in the lexicon (not inline word_exceptions) uses the lexicon
    IPA, and that differs from the pure-rules output."""
    eng = orthography2ipa.G2P("en-GB")
    lex = lexmod.get_lexicon("en-GB")
    word = "nature"
    assert word not in (eng.spec.word_exceptions or {})
    with_lex = eng.transcribe_word(word)
    assert with_lex == lex[word]
    # disable the lexicon → rules-only path, which is different here
    monkeypatch.setattr(g2p_module, "get_lexicon", lambda code: {})
    rules_only = orthography2ipa.G2P("en-GB").transcribe_word(word)
    assert rules_only != with_lex


def test_inline_word_exceptions_beat_lexicon(monkeypatch):
    """When a word is in BOTH inline word_exceptions and the lexicon, the
    inline value wins."""
    eng = orthography2ipa.G2P("en-GB")
    assert eng.spec.word_exceptions.get("the") == "ðə"
    # force a conflicting lexicon entry for the same word
    monkeypatch.setattr(
        g2p_module, "get_lexicon", lambda code: {"the": "ZZZ"})
    assert orthography2ipa.G2P("en-GB").transcribe_word("the") == "ðə"


def test_no_override_falls_to_rules():
    """A word in neither inline nor lexicon transcribes via the beam."""
    eng = orthography2ipa.G2P("en-GB")
    lex = lexmod.get_lexicon("en-GB")
    word = "qwrtplk"  # not a real word; certainly not in inline/lexicon
    assert word not in lex
    # does not raise, produces something from the rules
    assert isinstance(eng.transcribe_word(word), str)


# ─── stress: lexicon hits route through the word_exceptions pathway ─────────

def test_lexicon_entry_gets_stress_applied(monkeypatch):
    """A lexicon hit for a STRESSED-language spec still gets the stress mark
    inserted — proving it rejoins the same override pathway inline exceptions
    use (which also stress-mark their output)."""
    eng = orthography2ipa.G2P("pt-PT")
    assert eng.spec.stress is not None
    # inject a lexicon entry with no stress mark for a paroxytone word
    monkeypatch.setattr(
        g2p_module, "get_lexicon", lambda code: {"casa": "kaza"})
    out = orthography2ipa.G2P("pt-PT").transcribe_word("casa")
    assert "ˈ" in out, f"stress mark not applied to lexicon entry: {out!r}"
    assert out == "ˈkaza"


def test_lexicon_hit_has_full_confidence():
    """A lexicon override is a certain answer: confidence == 1.0, like an
    inline exception (coverage is 1.0 for a fully-mapped word)."""
    eng = orthography2ipa.G2P("en-GB")
    detail = eng.transcribe_detailed("nature")
    assert detail.words[0].confidence == 1.0


# ─── byte-identical for languages with no lexicon ───────────────────────────

@pytest.mark.parametrize("lang", ["pt-PT", "es-ES", "fr-FR"])
def test_non_lexicon_language_unchanged(lang, monkeypatch):
    """For a language shipping no lexicon, output with the feature is identical
    to the rules-only path (its override map is empty either way)."""
    text = "casa branca mundo"
    baseline = orthography2ipa.G2P(lang).transcribe(text)
    monkeypatch.setattr(g2p_module, "get_lexicon", lambda code: {})
    disabled = orthography2ipa.G2P(lang).transcribe(text)
    assert baseline == disabled


def test_only_en_ships_a_lexicon():
    """Guards the byte-identical claim: en-GB is the only shipped lexicon, so
    no other language's behaviour can have changed."""
    assert lexmod.available_lexicon_codes() == ["en-GB"]


# ─── data-quality guard over every shipped TSV ──────────────────────────────

def test_every_shipped_lexicon_is_clean():
    codes = lexmod.available_lexicon_codes()
    assert codes, "no lexicons found to validate"
    for code in codes:
        text = lexmod.lexicon_path(code).read_text(encoding="utf-8")
        problems = lexmod.validate_lexicon_text(text)
        assert not problems, f"{code}.tsv has issues: {problems[:5]}"


def test_every_shipped_lexicon_is_sorted():
    for code in lexmod.available_lexicon_codes():
        text = lexmod.lexicon_path(code).read_text(encoding="utf-8")
        words = [ln.split("\t")[0] for ln in text.split("\n")
                 if ln.strip() and "\t" in ln]
        assert words == sorted(words), f"{code}.tsv not sorted"


def test_every_shipped_lexicon_ipa_is_nfc():
    for code in lexmod.available_lexicon_codes():
        for word, ipa in lexmod.get_lexicon(code).items():
            assert unicodedata.normalize("NFC", ipa) == ipa
            assert unicodedata.normalize("NFC", word) == word


# ─── helper unit tests ───────────────────────────────────────────────────────

def test_is_ipa_string():
    assert lexmod.is_ipa_string("neɪtʃə")
    assert lexmod.is_ipa_string("ˈkaza")
    assert not lexmod.is_ipa_string("")          # empty
    assert not lexmod.is_ipa_string("hello!")    # ASCII punctuation
    assert not lexmod.is_ipa_string("ka za")     # whitespace
    assert not lexmod.is_ipa_string("kaz4")      # digit


def test_parse_lexicon_text_first_wins():
    text = "a\tə\nb\tbiː\na\tXXX\n\n"
    parsed = lexmod.parse_lexicon_text(text)
    assert parsed == {"a": "ə", "b": "biː"}  # first "a" wins, blank skipped


def test_validate_flags_bad_rows():
    bad = "Word\twɜːd\n"            # uppercase word
    assert lexmod.validate_lexicon_text(bad)
    dup = "a\tə\na\tə\n"           # duplicate
    assert lexmod.validate_lexicon_text(dup)
    shape = "a b c\n"              # wrong field count
    assert lexmod.validate_lexicon_text(shape)
