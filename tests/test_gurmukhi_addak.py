"""The Gurmukhi addak doubles the consonant letter after it.

The Unicode Standard (chapter 12, Gurmukhi): "U+0A71 GURMUKHI ADDAK is a
special sign to indicate that the following consonant is geminate. ISCII-1991
does not have a specific code point for addak and encodes it as a cluster. For
example, the word ਪੱਗ pagg, 'turban,' can be represented with the sequence
<pa, addak, ga> in Unicode, while in ISCII-1991 it would be <pa, ga, virama,
ga>."

The expected values below are written from that rule and the letter values of
the spec (ਬ b, ਚ tʃ, ਜ dʒ, ਕ k, ਪ p, ਗ ɡ, ਦ d̪, ਸ s, ਤ t̪, ਲ l, with the
inherent ə on each consonant that no vowel sign or word-final elision takes).
"""
import warnings

import pytest

from orthography2ipa import phoneme_inventory, registry
from orthography2ipa.g2p import G2P

ADDAK = "ੱ"
VIRAMA = "੍"
NUKTA = "਼"
# The reading of an addak before an aspirate is not settled by a source, so the
# cluster test leaves the ten aspirate letters out (issue on the o2i tracker).
ASPIRATES = "ਖਛਠਥਫਘਝਢਧਭ"
CONSONANTS = [chr(cp) for cp in range(0x0A15, 0x0A3A)
              if chr(cp) not in "਩਱਴਷" + ASPIRATES]


@pytest.fixture(scope="module")
def pa():
    return G2P("pa")


@pytest.mark.parametrize("word, expected", [
    ("ਬੱਚਾ", "bətʃtʃaː"),
    ("ਅੱਜ", "ədʒdʒ"),
    ("ਪੱਕਾ", "pəkkaː"),
    ("ਪੱਗ", "pəɡɡ"),
    ("ਦੱਸ", "d̪əss"),
    ("ਪੱਤਾ", "pət̪t̪aː"),
    ("ਕੱਲਾ", "kəllaː"),
])
def test_addak_geminates_the_following_consonant(pa, word, expected):
    assert pa.transcribe(word) == expected


@pytest.mark.parametrize("consonant", CONSONANTS)
def test_addak_equals_the_iscii_cluster(pa, consonant):
    """<pa, addak, C> reads as ISCII <pa, C, virama, C>, for every consonant letter."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        unicode_spelling = "ਪ" + ADDAK + consonant + "ਾ"
        iscii_spelling = "ਪ" + consonant + VIRAMA + consonant + "ਾ"
        assert pa.transcribe(unicode_spelling) == pa.transcribe(iscii_spelling)
        assert "ː" not in pa.transcribe(unicode_spelling).replace("aː", "")


def test_addak_geminates_a_nukta_consonant(pa):
    """ਸ਼ is ਸ plus a nukta, and the doubled letter keeps it."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert pa.transcribe("ਪ" + ADDAK + "ਸ" + NUKTA + "ਾ") \
            == pa.transcribe("ਪ" + "ਸ" + NUKTA + VIRAMA + "ਸ" + NUKTA + "ਾ")


def test_addak_after_a_vowel_sign(pa):
    """ਕਿੱਤਾ: the addak follows the vowel sign of the syllable before the geminate."""
    assert pa.transcribe("ਕਿੱਤਾ") == "kɪt̪t̪aː"


def test_a_doubled_addak_doubles_the_letter_once(pa):
    """A repeated addak is one gemination, and preparing twice changes nothing."""
    it = G2P("pa")._interpreter
    once = it.prepare("ਕੱੱਕ")
    assert it.prepare(once) == once
    assert pa.transcribe("ਕੱੱਕ") == pa.transcribe("ਕੱਕ") == "kəkk"


@pytest.mark.parametrize("code, precomposed, decomposed", [
    ("hi", "\u095Bिन्दगी", "\u091C\u093Cिन्दगी"),
    ("mr", "\u095Bिन्दगी", "\u091C\u093Cिन्दगी"),
])
def test_precomposed_nukta_letter_reads_as_its_decomposed_form(code, precomposed, decomposed):
    """A precomposed nukta letter (ज़ U+095B) is canonically equal to ज plus nukta."""
    g2p = G2P(code)
    assert g2p.transcribe(precomposed) == g2p.transcribe(decomposed)


def test_inventory_has_no_long_consonant_token_from_the_addak():
    """The addak spells no segment of its own, so no consonant plus ː is declared."""
    long_tokens = [t for t in phoneme_inventory(registry.get("pa")) if t.endswith("ː")]
    assert long_tokens
    assert all(t[0] in "aeiouɔɛ" or t[0] in "ãẽĩõũ" for t in long_tokens), long_tokens
