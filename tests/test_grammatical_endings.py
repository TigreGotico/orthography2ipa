"""grammatical_endings — morpheme-aware word-ending realisations.

Two phenomena motivate the mechanism:

* **French mute ⟨-er⟩ / ⟨-ez⟩.** Word-final ⟨-er⟩ of the infinitive and of
  agent nouns is [e] (``parler``, ``boulanger``), and ⟨-ez⟩ of the 2pl is
  likewise [e] (``mangez``, and the frozen ``nez``/``chez``/``assez``).
  The mute reading belongs to the *grammatical ending*, not to the letter
  sequence — ⟨er⟩ inside a word (``personne``, ``version``) is untouched,
  and the closed set of nouns that keep /ɛʁ/ (``mer``, ``hiver``) stays in
  ``word_exceptions`` (Fouché 1959; Tranel 1987 §3 on final-consonant
  elision in grammatical endings).
* **English suffix palatalization.** ⟨-tion⟩ → /ʃən/, ⟨-cious⟩ → /ʃəs/,
  ⟨-tial⟩ → /ʃəl/ (Chomsky & Halle 1968 on palatalization before the
  ``-ion`` suffix; Wells 2008 LPD for the surface values).

The non-regression half of this file is the point: the previous attempt at
these facts used grapheme digraph keys and broke word-*internal* material
(``personne``, ``terre``, ``house``). Endings only ever touch the word's
effective end.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def fr():
    return G2P("fr-FR")


@pytest.fixture(scope="module")
def en():
    return G2P("en")


@pytest.fixture(scope="module")
def en_us():
    return G2P("en-US")


# ── French: mute -er / -ez ────────────────────────────────────────────
@pytest.mark.parametrize("word,expected", [
    ("parler", "paʁle"),
    ("manger", "mɑ̃ʒe"),
    ("boulanger", "bulɑ̃ʒe"),
    # plural of an agent noun: the ending is still word-final modulo the
    # transparent grammatical ⟨s⟩ (Tranel 1987 §3)
    ("boulangers", "bulɑ̃ʒe"),
    ("mangez", "mɑ̃ʒe"),
    ("nez", "ne"),
    ("chez", "ʃe"),
    ("assez", "ase"),
])
def test_fr_mute_endings(fr, word, expected):
    assert fr.transcribe(word) == expected


@pytest.mark.parametrize("word,expected", [
    # ⟨er⟩ word-INTERNAL: intervocalic ⟨s⟩ must stay voiceless, ⟨rr⟩ must
    # stay degeminated — the two regressions the digraph attempt caused.
    ("personne", "pɛʁsɔn"),
    ("version", "vɛʁsjɔ̃"),
    ("terre", "təʁ"),
    ("pierre", "pjəʁ"),
    # ⟨er⟩ here matches grammatical_endings just like it does in
    # ``boulangers``; ``vers`` keeps /vɛʁ/ because its word_exceptions
    # entry outranks the ending, not because the matcher declines to match
    ("vers", "vɛʁ"),
    # word_exceptions outrank grammatical_endings
    ("mer", "mɛʁ"),
    ("hiver", "ivɛʁ"),
    # transparent-suffix machinery untouched
    ("vies", "vi"),
])
def test_fr_no_regression(fr, word, expected):
    assert fr.transcribe(word) == expected


# ── English: suffix palatalization ────────────────────────────────────
@pytest.mark.parametrize("word,expected", [
    ("nation", "næʃən"),
    ("station", "stæʃən"),
    ("motion", "mɒʃən"),
    ("mission", "mɪʃən"),
    ("special", "spɛʃəl"),
    ("gracious", "ɡɹæʃəs"),
    ("martial", "mɑːɹʃəl"),
    # longest match wins: ⟨-stion⟩ keeps the /t/ as the affricate onset
    ("question", "kwɛstʃən"),
    # same for ⟨-stial⟩/⟨-stious⟩: the ⟨t⟩ after ⟨s⟩ is not palatalized to
    # [ʃ] alone, since a bare [sʃ] cluster is phonotactically impossible
    # (Chomsky & Halle 1968; Wells 2008 LPD)
    ("celestial", "sɛlɛstʃəl"),
    ("bestial", "bɛstʃəl"),
])
def test_en_palatalized_suffixes(en, word, expected):
    assert en.transcribe(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("house", "haʊz"),
    ("mouse", "maʊz"),
    ("louse", "laʊz"),
    ("rouse", "ɹaʊz"),
])
def test_en_ous_words_unchanged(en, word, expected):
    """The #808 breakage class: ⟨-ous⟩/⟨-ouse⟩ words share letters with
    ⟨-cious⟩ but no suffix, so nothing may fire."""
    assert en.transcribe(word) == expected
    assert "ʃ" not in en.transcribe(word)


def test_en_us_inherits_endings(en_us):
    assert en_us.transcribe("nation") == "næʃən"
    assert "ʃ" not in en_us.transcribe("house")


# ── mechanism ─────────────────────────────────────────────────────────
def test_ending_never_consumes_the_whole_word(en):
    """An ending needs a head: a word that IS the ending is left alone."""
    assert G2P("fr-FR").transcribe("ez") != "e"


def test_precedence_word_exceptions_beat_endings(fr):
    assert "mer" in (fr.spec.word_exceptions or {})
    assert fr.transcribe("mer") == fr.spec.word_exceptions["mer"]
