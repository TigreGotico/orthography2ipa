"""Two abugida facts the Tibetan script is the first spec to exercise.

Both are tokenizer-level and language-independent; they are tested here on
synthetic specs so the claim is about the ENGINE, not about ``dz``.
"""
from __future__ import annotations

from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.types import GraphemePosition, LanguageSpec


def _spec(**kwargs) -> LanguageSpec:
    base = dict(code="xx", name="Test", family="Test", script="Tibetan",
                inherent_vowel="ɑ", allophones={})
    base.update(kwargs)
    return LanguageSpec(**base)


def _ipa(spec: LanguageSpec, text: str) -> str:
    return "".join(t.ipa[0] if t.ipa else ""
                   for t in spec_tokens(spec, text))


def spec_tokens(spec: LanguageSpec, text: str):
    return [t for t in PhonetokTokenizer(spec).tokenize(text)
            if t.kind.name == "GRAPHEME"]


def test_conjunct_stack_keeps_the_inherent_vowel():
    """A grapheme key that is a letter plus a SUBJOINED consonant mark is a
    consonant letter, and a consonant letter carries the inherent vowel.

    Tibetan ⟨ཀྲ⟩ is ཀ (Lo) + U+0FB2 (Mn) and reads [ʈɑ]. Deciding
    "is this a bare combining mark?" from the key's LAST character called the
    whole stack a mark and dropped the vowel, giving *[ʈ].
    """
    spec = _spec(graphemes={"ཀྲ": ["ʈ"]})
    assert _ipa(spec, "ཀྲ") == "ʈɑ"


def test_a_bare_combining_mark_still_takes_no_inherent_vowel():
    """The counter-case the previous rule must not break: a key that IS a
    combining mark on its own (Bengali anusvara ⟨ং⟩ → /ŋ/) is not a letter
    and gets no inherent vowel — বাংলা is [baŋla], not *[baŋɑla].
    """
    spec = _spec(graphemes={"ং": ["ŋ"]})
    assert _ipa(spec, "ং") == "ŋ"


def test_a_letter_plus_vowel_sign_key_takes_no_inherent_vowel():
    """The other counter-case: a key spelling consonant + vowel sign already
    contains its nucleus, so nothing is appended.
    """
    spec = _spec(graphemes={"कि": ["ki"]})
    assert _ipa(spec, "कि") == "ki"


def test_a_letter_silenced_before_a_consonant_gets_no_inherent_vowel():
    """A grapheme the spec gives NO realisation before a consonant is a
    silent letter there, and a silent letter has no inherent vowel to leave
    behind. The Tibetan prefixed letters are the case: ⟨ག⟩ in ⟨གས⟩ is not
    pronounced at all, so the token must be bare and not [kɑ] — a phantom
    nucleus makes the following ROOT look like a coda.
    """
    spec = _spec(
        graphemes={"ག": ["k"], "ས": ["s"]},
        positional_graphemes={"ག": {GraphemePosition.BEFORE_CONSONANT: [""]}},
    )
    assert _ipa(spec, "གས") == "ksɑ"


def test_a_letter_with_a_real_reading_before_a_consonant_keeps_its_vowel():
    """Counter-case: the spec must have DECIDED the letter is silent. One
    that lists a real reading alongside the empty one has not, and its
    inherent vowel stays.
    """
    spec = _spec(
        graphemes={"ག": ["k"], "ས": ["s"]},
        positional_graphemes={"ག": {GraphemePosition.BEFORE_CONSONANT: ["", "k"]}},
    )
    assert _ipa(spec, "གས") == "kɑsɑ"


def test_the_silencing_rule_does_not_reach_a_word_final_letter():
    """A letter silenced only BEFORE A CONSONANT is unaffected when nothing
    follows it: ⟨ག⟩ alone is still [kɑ].
    """
    spec = _spec(
        graphemes={"ག": ["k"]},
        positional_graphemes={"ག": {GraphemePosition.BEFORE_CONSONANT: [""]}},
    )
    assert _ipa(spec, "ག") == "kɑ"


def test_a_nukta_digraph_is_left_alone():
    """The conjunct exception is narrow ON PURPOSE. A letter plus a NUKTA
    (⟨क़⟩ = क + U+093C DEVANAGARI SIGN NUKTA) has the same shape as a stack
    but the nukta MODIFIES its base letter instead of adding a consonant to
    it, and whether such a key should take the inherent vowel is a question
    about the Brahmic specs' own schwa handling — with its own fleet-wide
    cost — not about conjuncts. It keeps the historical behaviour so this
    change has exactly one blast radius.
    """
    spec = _spec(graphemes={"क़": ["q"]})
    assert _ipa(spec, "क़") == "q"


def test_a_partly_subjoined_key_is_not_a_stack():
    """Only an ALL-subjoined tail qualifies: a stack whose tail also carries
    a non-letter mark is not decided by this predicate.
    """
    spec = _spec(graphemes={"ཀྲཾ": ["ʈ"]})
    assert _ipa(spec, "ཀྲཾ") == "ʈ"


def test_a_register_shifter_keeps_the_inherent_vowel():
    """A letter plus a REGISTER SHIFTER is a consonant letter too.

    Khmer ⟨៊⟩ triisap and ⟨៉⟩ muusikatoan move their base between the
    a-series and the o-series, which decides WHICH inherent vowel the letter
    carries and never whether it carries one. Read as bare marks they took
    the base's nucleus away, so ⟨ប៉ង⟩ came out *[pŋɔː] for [pɑːŋ].
    """
    spec = _spec(graphemes={"ប៉": ["p"], "ស៊": ["s"]})
    assert _ipa(spec, "ប៉") == "pɑ"
    assert _ipa(spec, "ស៊") == "sɑ"
