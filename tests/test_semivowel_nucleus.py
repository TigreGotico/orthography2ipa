"""⟨y⟩ and ⟨w⟩ as syllable nuclei: the spec's grapheme table decides.

A Latin ⟨y⟩ or ⟨w⟩ writes a vowel in some orthographies and a consonant or
glide in others. The orthographic syllable count, which places the stress, must
follow the spec: Spanish ⟨y⟩ is the onset of ⟨mayo⟩ and the off-glide of
⟨rey⟩, Indonesian ⟨y⟩ is always /j/, Finnish ⟨y⟩ is always a vowel.

Every expectation below comes from a published source, named at the case.
"""
import unicodedata

import pytest

from orthography2ipa import get, transcribe
from orthography2ipa.stress import (
    _is_vowel_char, _nucleus_mask, _semivowel_roles, _syllables_for,
)
from orthography2ipa.vowels import (
    SEMIVOWEL_CONTEXTUAL, SEMIVOWEL_MARGIN, SEMIVOWEL_NUCLEUS, is_ipa_vowel,
    semivowel_role,
)


def _nuclei(ipa: str) -> int:
    count, previous = 0, False
    for ch in ipa:
        if unicodedata.combining(ch) or ch in "ːˑˌ":
            continue
        vowel = is_ipa_vowel(ch)
        if vowel and not previous:
            count += 1
        previous = vowel
    return count


def _stressed_from_end(ipa: str) -> int:
    """1 for a final stress, 2 for a penult, … counted over the IPA."""
    return _nuclei(ipa[ipa.rindex("ˈ"):])


SPANISH = ("es-ES", "es-419", "es-AR", "es-MX")

# (word, stressed syllable counted from the end); the source heads each group.
SPANISH_STRESS = [
    # Navarro Tomás 1918, Manual de pronunciación española, § 57 p. 46
    # (mayo-máyo, rayo) and § 122 p. 101 (hoyo, ayuda, bueyes, reyerta):
    # ⟨y⟩ before a vowel is the palatal consonant opening the syllable.
    ("mayo", 2), ("rayo", 2), ("hoyo", 2), ("ayuda", 2),
    ("bueyes", 2), ("reyerta", 2), ("ayer", 1), ("sayal", 1),
    # RAE-ASALE, Diccionario panhispánico de dudas, s.v. tilde § 1.2.1:
    # oxytones ending in -y take no tilde (guirigay, virrey, convoy, estoy).
    ("guirigay", 1), ("virrey", 1), ("convoy", 1), ("estoy", 1),
    ("uruguay", 1),
    # DPD s.v. tilde § 1.2.2: paroxytones ending in -y carry the tilde.
    ("yérsey", 2), ("yóquey", 2),
    # DPD s.v. rugbi, sexi: unadapted English spellings, adapted as the
    # paroxytones rugbi and sexi.
    ("rugby", 2), ("sexy", 2),
]


@pytest.mark.parametrize("lang", SPANISH)
@pytest.mark.parametrize("word,from_end", SPANISH_STRESS)
def test_spanish_y_stress(lang, word, from_end):
    assert _stressed_from_end(transcribe(word, lang)) == from_end


@pytest.mark.parametrize("word", ["ley", "rey", "soy", "doy", "buey", "hoy", "muy"])
def test_spanish_vowel_y_is_one_syllable(word):
    # Navarro Tomás 1918, § 47 p. 39 and § 50 p. 41: the written y of ley,
    # rey, doy, soy is the semivowel of the diphthong.
    assert len(_syllables_for(word, "es-ES")) == 1


# Wiktionary IPA, with its syllable dots: Indonesian ⟨saya⟩ [ˈsa.ja],
# ⟨kayu⟩ [ˈka.ju], ⟨wayang⟩ [ˈwa.jaŋ], ⟨biaya⟩ [biˈa.ja]; Malay ⟨sayang⟩
# [ˈsa.jaŋ]; Swahili ⟨huyo⟩ /ˈhu.jɔ/, ⟨mbaya⟩ /ˈᵐbɑ.jɑ/; Ido ⟨kayero⟩
# /kaˈje.ro/, ⟨foyo⟩ /ˈfojo/.
@pytest.mark.parametrize("lang,word,from_end", [
    ("id", "saya", 2), ("id", "kayu", 2), ("id", "wayang", 2), ("id", "biaya", 2),
    ("ms", "sayang", 2), ("ms", "sayap", 2),
    ("sw", "huyo", 2), ("sw", "mbaya", 2), ("sw", "bayana", 2),
    ("io", "kayero", 2), ("io", "foyo", 2), ("io", "aboyar", 1),
])
def test_consonant_y_stress(lang, word, from_end):
    assert _stressed_from_end(transcribe(word, lang)) == from_end


@pytest.mark.parametrize("lang,word,count", [
    # Finnish ⟨y⟩ is the vowel /y/ and stays a nucleus.
    ("fi", "hyvä", 2), ("fi", "kyky", 2),
    # German ⟨y⟩ is /ʏ yː/: Sys-tem.
    ("de-DE", "System", 2),
    # A ⟨y⟩ with no vowel beside it is the only nucleus there is.
    ("es-ES", "rugby", 2), ("en-GB", "rhythm", 1),
])
def test_vowel_y_keeps_its_nucleus(lang, word, count):
    assert len(_syllables_for(word, lang)) == count


@pytest.mark.parametrize("word,from_end", [
    # IEC, Ortografia catalana, § 3.1, quadre 29: an oxytone with an ending
    # other than a vowel, vowel + s, -en or -in takes no accent, so ⟨-ny⟩
    # words written without one are oxytone (Wiktionary [kumˈpaɲ], [əsˈtaɲ],
    # [munˈsɛɲ], [kumˈpaɲs]).
    ("company", 1), ("estany", 1), ("Montseny", 1), ("companys", 1),
    ("muntanya", 2), ("Catalunya", 2),
])
def test_catalan_ny_stress(word, from_end):
    assert _stressed_from_end(transcribe(word, "ca")) == from_end


def test_catalan_y_is_never_a_nucleus():
    # The ca spec writes ⟨y⟩ only inside ⟨ny⟩ /ɲ/: ⟨any⟩ [ˈaɲ] is one syllable.
    assert len(_syllables_for("any", "ca")) == 1
    assert len(_syllables_for("Montseny", "ca")) == 2


@pytest.mark.parametrize("word,reading", [
    # Janotta 1929, Cosmoglotta 64, p. 152: "y vocalic es pronunciat quam
    # german ü o frances u ... Pos un vocal e in comensa de un parol anc ante
    # un vocal, y es consonant". The vowel is IPA [y], the consonant [j].
    ("yo", "j"), ("loyal", "j"), ("system", "y"), ("type", "y"),
])
def test_interlingue_y_reading(word, reading):
    out = transcribe(word, "ie")
    assert ("j" in out) == (reading == "j")
    assert ("y" in out) == (reading == "y")


@pytest.mark.parametrize("readings,role", [
    (["ʝ", "i"], SEMIVOWEL_CONTEXTUAL),        # Spanish ⟨y⟩
    (["y"], SEMIVOWEL_NUCLEUS),               # Finnish ⟨y⟩
    (["ʏ", "yː"], SEMIVOWEL_NUCLEUS),         # German ⟨y⟩
    (["j"], SEMIVOWEL_MARGIN),                # Indonesian ⟨y⟩
    (["i̯"], SEMIVOWEL_MARGIN),                # a non-syllabic vowel is a glide
    # A vowel first and nothing to condition it: the transcription writes
    # the vowel next to another vowel too (Portuguese ⟨y⟩ /i j/).
    (["i", "j"], SEMIVOWEL_NUCLEUS),
])
def test_semivowel_role_from_readings(readings, role):
    assert semivowel_role("y", {"y": readings}) == role


def test_a_positional_rule_lets_the_context_choose():
    # Interlingue ⟨y⟩ /i j/ is /j/ next to a vowel by a positional rule.
    assert semivowel_role("y", {"y": ["i", "j"]}, conditioned=True) \
        == SEMIVOWEL_CONTEXTUAL
    assert _semivowel_roles(get("ie"))["y"] == SEMIVOWEL_CONTEXTUAL
    assert _semivowel_roles(get("pt-PT"))["y"] == SEMIVOWEL_NUCLEUS


def test_semivowel_role_without_an_entry():
    # Only inside multigraphs (Catalan ⟨ny⟩): never a nucleus by itself.
    assert semivowel_role("y", {"ny": ["ɲ"]}) == SEMIVOWEL_MARGIN
    # Not mentioned at all: the table gives no answer.
    assert semivowel_role("y", {"a": ["a"]}) is None
    assert semivowel_role("w", {"a": ["a"]}) is None


def test_nucleus_mask_reads_the_neighbours():
    roles = _semivowel_roles(get("es-ES"))
    assert _nucleus_mask("mayo", _is_vowel_char, roles) == [False, True, False, True]
    assert _nucleus_mask("rugby", _is_vowel_char, roles) == [
        False, True, False, False, True]
    assert _nucleus_mask("yy", _is_vowel_char, roles) == [True, True]
