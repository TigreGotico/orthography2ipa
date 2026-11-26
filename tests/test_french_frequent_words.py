"""French rules for frequent words that the letters decide.

Each rule is cited by page from Martinon, *Comment on prononce le français*
(Larousse, 1913), read in the archive.org scan of the University of Toronto
copy (https://archive.org/details/commentonprononc00martuoft), unless the test
names another source. The expected IPA is written here, never read back from
the engine, and each rule has a counter-case where it must not fire.
"""
import pytest

import orthography2ipa as o2i


def _t(text):
    return o2i.transcribe(text, "fr-FR")


# Martinon (1913: 161): the ⟨nt⟩ of the third-person plural changes nothing,
# tombait dru and tombaient dru sound the same. Larousse, s.v. être
# (Homonymes): étaient is a homonym of étai, soient of soi, soie and soit.
@pytest.mark.parametrize("text, expected", [
    ("étaient", "etɛ"), ("avaient", "avɛ"), ("seraient", "səʁɛ"),
    ("parlaient", "paʁlɛ"), ("aient", "ɛ"), ("paient", "pɛ"),
    ("soient", "swa"), ("voient", "vwa"),
])
def test_ent_after_ai_and_oi_is_mute(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    # Bare ⟨-ent⟩ keeps its deferred nasal reading (ENDING "ent").
    ("vent", "vɑ̃"), ("moment", "mɔmɑ̃"), ("ils parlent", "il paʁlɑ̃"),
    # ⟨-ient⟩ is not ⟨ai⟩ or ⟨oi⟩: client keeps its nasal vowel.
    ("client", "kljɛ̃"),
])
def test_other_ent_endings_are_untouched(text, expected):
    assert _t(text) == expected


# Martinon (1913: 164, 239): the ⟨e⟩ between ⟨g⟩ and ⟨a o u⟩ is not
# pronounced; it only gives ⟨g⟩ its sound before ⟨e i⟩. 164 n. 1: J(e)an,
# J(e)anne.
@pytest.mark.parametrize("text, expected", [
    ("mangeait", "mɑ̃ʒɛ"), ("pigeon", "piʒɔ̃"), ("bourgeois", "buʁʒwa"),
    ("nageant", "naʒɑ̃"), ("geôle", "ʒol"), ("Georges", "ʒɔʁʒ"),
    ("Jean", "ʒɑ̃"), ("Jeanne", "ʒan"),
])
def test_e_after_soft_g_before_a_back_vowel_is_mute(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("gelé", "ʒəle"),      # before a consonant the ⟨e⟩ is a vowel
    ("je", "ʒə"),          # the whole-word entry
    ("geai", "ʒe"),        # Martinon (1913: 164): g(e)ai
])
def test_e_after_soft_g_counter_cases(text, expected):
    assert _t(text) == expected


# Martinon (1913: 348-349): before a vowel, initial ex- is regularly [ɡz]
# (exalter, exhaler, exécuter, exiger, exotique), and so are its derivatives.
# 347: elsewhere ⟨x⟩ is [ks] (laxatif, maxime, sexuel).
@pytest.mark.parametrize("text, expected", [
    ("exemple", "ɛɡzɑ̃pl"), ("exister", "ɛɡziste"), ("exiger", "ɛɡziʒe"),
    ("exotique", "ɛɡzɔtik"), ("exhiber", "ɛɡzibe"), ("exercice", "ɛɡzɛʁsis"),
    ("coexister", "kɔɛɡziste"),
])
def test_ex_before_a_vowel_is_voiced(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("taxi", "taksi"), ("maxime", "maksim"), ("excuse", "ɛkskyz"),
    ("expert", "ɛkspɛʁ"), ("texte", "tɛkst"), ("luxe", "lyks"), ("fixer", "fikse"),
])
def test_x_elsewhere_stays_ks(text, expected):
    assert _t(text) == expected


# Martinon (1913: 348): deuxième, dixième, sixième have the [z] of the liaison
# of deux, six, dix.
@pytest.mark.parametrize("text, expected", [
    ("deuxième", "døzjɛm"), ("sixième", "sizjɛm"), ("dixième", "dizjɛm"),
    ("deuxièmes", "døzjɛm"),
])
def test_x_of_the_ordinal_is_z(text, expected):
    assert _t(text) == expected


def test_the_letter_name_ixieme_keeps_ks():
    # wikipron fr: ixième [iksjɛm]
    assert _t("ixième") == "iksjɛm"
