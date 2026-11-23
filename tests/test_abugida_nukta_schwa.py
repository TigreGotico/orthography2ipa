"""A consonant letter with a nukta keeps the inherent vowel of the plain letter.

The Unicode Standard (ch. 12, Devanagari, "Consonant Letters") gives every
consonant letter an inherent vowel, and its rendering rule R9 calls the nukta
a sign "which modifies a consonant form". The letters U+0958-U+095F and
U+0A33, U+0A36, U+0A59-U+0A5E are named LETTER (``DEVANAGARI LETTER QA``) and
decompose canonically to the base consonant plus the nukta (U+093C, U+0A3C).
NFC does not recompose them, so the engine always sees the pair. The nukta
supplies no vowel, so the pair is a consonant letter, and the schwa-deletion
rules then decide for it as they decide for the plain letter. A spec states
this in data: it lists the nukta in ``consonant_marks``.

Singh and Lehal, "A Rule Based Schwa Deletion Algorithm for Punjabi TTS
System" (§2.2, Rule II), give a nukta letter that keeps its schwa:
ਆਕਰਸ਼ਨ [ākərəshən], "schwa is inserted only after the consonant 'ਸ਼'".
For Hindi, no source opened for this module states the rule for a nukta
letter in words. The Hindi rows rest on the Unicode text above and on the
spec's schwa-deletion rules (Ohala 1983, ch. 5; Narasimhan et al. 2004),
which name no nukta exception.

The expected reading of a nukta word is computed from the plain word: the
reading of the word with each nukta removed, with each plain onset replaced
by the onset the spec's letter table gives the nukta letter. The plain word
runs through no nukta key, so this reading does not depend on the code under
test. No test word holds both a nukta letter and its plain letter, so the
onset replacement cannot hit the wrong letter.
"""
import unicodedata
import warnings

import pytest

from orthography2ipa import G2P
from orthography2ipa.json_loader import available_json_codes, load_json_spec

NUKTA = {"hi": "़", "pa": "਼"}
#: U+095F य़ is left out: the hi spec has no key for it, so it reads as य
#: followed by an unmapped nukta, which is a separate path.
PRECOMPOSED = {
    "hi": [chr(cp) for cp in range(0x0958, 0x095F)],
    "pa": [chr(cp) for cp in (0x0A33, 0x0A36, 0x0A59, 0x0A5A, 0x0A5B, 0x0A5E)],
}


@pytest.fixture(scope="module")
def engines():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return {lang: G2P(lang) for lang in ("hi", "pa")}


def expect_from_plain(engines, lang, word):
    """The reading of *word* computed from its plain-letter word."""
    word = unicodedata.normalize("NFD", word)
    graphemes = engines[lang].spec.graphemes
    ipa = engines[lang].transcribe(word.replace(NUKTA[lang], ""))
    for i, ch in enumerate(word):
        if ch == NUKTA[lang]:
            ipa = ipa.replace(graphemes[word[i - 1]][0],
                              graphemes[word[i - 1:i + 1]][0])
    return ipa


def check(engines, lang, word, expected):
    assert expect_from_plain(engines, lang, word) == expected
    assert engines[lang].transcribe(word) == expected


@pytest.mark.parametrize("lang,word,expected", [
    ("pa", "ਖ਼ਬਰ", "xəbəɾ"),
    ("pa", "ਗ਼ੱਲ", "ɣəll"),
    ("pa", "ਫ਼ੱਕਰ", "fəkkəɾ"),
    ("pa", "ਜ਼ਮੀਨ", "zəmiːn"),
    ("pa", "ਕ਼ਲਮ", "qələm"),
    ("hi", "ख़बर", "xəbəɾ"),
    ("hi", "ज़मीन", "zəmiːn"),
    ("hi", "क़लम", "qələm"),
])
def test_issue_rows(engines, lang, word, expected):
    check(engines, lang, word, expected)


def test_singh_lehal_example_keeps_the_schwa_of_sha(engines):
    """Singh and Lehal §2.2 Rule II: ਆਕਰਸ਼ਨ [ākərəshən]."""
    check(engines, "pa", "ਆਕਰਸ਼ਨ", "aːkəɾəʃən")


@pytest.mark.parametrize("lang,letter", [
    (lang, letter) for lang, letters in PRECOMPOSED.items()
    for letter in letters
])
def test_precomposed_letter_reads_as_the_plain_letter(engines, lang, letter):
    pair = unicodedata.normalize("NFD", letter)
    assert pair == unicodedata.normalize("NFC", letter)
    assert len(pair) == 2 and pair[1] == NUKTA[lang]
    tail = {"hi": "बर", "pa": "ਬਰ"}[lang]
    expected = expect_from_plain(engines, lang, pair + tail)
    assert expected.endswith("əbəɾ")
    assert engines[lang].transcribe(letter + tail) == expected
    assert engines[lang].transcribe(pair + tail) == expected


@pytest.mark.parametrize("lang,word,expected", [
    ("hi", "ख़", "xə"),
    ("pa", "ਖ਼", "xə"),
    ("hi", "ख़ज़", "xəz"),
    ("pa", "ਖ਼ਜ਼", "xəz"),
    ("hi", "ग़ज़ल", "ɣəzəl"),
    ("pa", "ਗ਼ਜ਼ਲ", "ɣəzəl"),
    ("hi", "क़र्ज़", "qəɾz"),
])
def test_nukta_letter_at_word_end(engines, lang, word, expected):
    """The final schwa goes as it does after the plain letter, and a
    one-letter word keeps it, as ख [kʰə] does."""
    check(engines, lang, word, expected)


@pytest.mark.parametrize("lang,word,expected", [
    ("hi", "ज़ख़ीरा", "zəxiːɾaː"),
    ("pa", "ਜ਼ਖ਼ੀਰਾ", "zəxiːɾaː"),
    ("hi", "ख़ज़ाना", "xəzaːnaː"),
    ("pa", "ਖ਼ਜ਼ਾਨਾ", "xəzaːnaː"),
])
def test_nukta_letter_before_a_vowel_sign(engines, lang, word, expected):
    """The vowel sign replaces the inherent vowel of the second nukta letter;
    the first one, with no sign, keeps it."""
    check(engines, lang, word, expected)


@pytest.mark.parametrize("lang,word,expected", [
    ("pa", "ਖ਼ੱਲ", "xəll"),
    ("pa", "ਇੱਜ਼ਤ", "ɪzzət̪"),
    ("hi", "इज़्ज़त", "ɪzzət̪"),
])
def test_geminate_after_a_nukta_letter(engines, lang, word, expected):
    """An addak after a nukta letter doubles the next letter, an addak before
    one doubles the nukta letter, and a virama after one leaves it bare."""
    check(engines, lang, word, expected)


def test_every_abugida_spec_with_a_nukta_letter_lists_its_nukta():
    """A spec that maps a letter plus nukta lists that nukta, so the letter
    keeps its inherent vowel. The Unicode names are read here, never by the
    engine."""
    missing, checked = [], 0
    for code in available_json_codes():
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            spec = load_json_spec(code)
        if not spec.inherent_vowel:
            continue
        keys = set(spec.graphemes)
        for table in spec.positional_graphemes.values():
            keys |= set(table)
        nuktas = {
            ch for key in keys
            for ch in unicodedata.normalize("NFC", key)[1:]
            if "NUKTA" in unicodedata.name(ch, "")
        }
        checked += bool(nuktas)
        if not nuktas <= set(spec.consonant_marks):
            missing.append(code)
    assert checked >= 18
    assert missing == []
