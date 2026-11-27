"""French sandhi rules that read the spelling of the next or the previous word.

These rules use ``left_spelling`` and ``right_spelling``: the IPA of the two
words cannot tell the cases apart (⟨ans⟩ and ⟨en⟩ are both [ɑ̃], ⟨vingt-deux⟩
and ⟨quatre-vingt-deux⟩ share the pair ⟨vingt⟩ ⟨deux⟩). Each case is cited by
page from Martinon, *Comment on prononce le français* (Larousse, 1913), read in
the archive.org scan (https://archive.org/details/commentonprononc00martuoft),
unless the test names another source. The expected IPA is written here, never
read back from the engine, and each rule has a counter-case where it must not
fire.
"""
import pytest

import orthography2ipa as o2i


def _t(text, code="fr-FR"):
    return o2i.transcribe(text, code)


# Martinon (1913: 329-330): the t of vingt sounds in vingt et un and in
# vingt-deux, vingt-trois..., "mais il ne sonne pas dans quatre-vingt-un,
# -deux, -trois"; 346: "le t dans vingt-quatre ou vingt-neuf"; 253 note 2:
# vingt-huit with the t, quatre-vingt-huit like quatre-vingt-deux.
# Lexique 3.83: vingt-deux [v5td2], vingt-huit [v5t8it].
@pytest.mark.parametrize("text, expected", [
    ("vingt-deux", "vɛ̃t dø"), ("vingt-trois", "vɛ̃t tʁwa"),
    ("vingt-quatre", "vɛ̃t katʁ"), ("vingt-cinq", "vɛ̃t sɛ̃k"),
    ("vingt-six", "vɛ̃t sis"), ("vingt-sept", "vɛ̃t sɛt"),
    ("vingt-neuf", "vɛ̃t nœf"), ("vingt-huit", "vɛ̃t‿ ɥit"),
    ("vingt et un", "vɛ̃t‿ e œ̃"), ("vingt-et-un", "vɛ̃t‿ e œ̃"),
    ("vingt-deuxième", "vɛ̃t døzjɛm"), ("cent vingt-deux", "sɑ̃ vɛ̃t dø"),
])
def test_vingt_sounds_its_t_from_21_to_29(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("vingt", "vɛ̃"), ("vingt jours", "vɛ̃ ʒuʁ"), ("vingt mille", "vɛ̃ mil"),
    ("quatre-vingt-un", "katʁ vɛ̃ œ̃"), ("quatre-vingt-deux", "katʁ vɛ̃ dø"),
    ("quatre-vingt-neuf", "katʁ vɛ̃ nœf"), ("quatre-vingt-huit", "katʁ vɛ̃ ɥit"),
    ("quatre-vingt-dix-huit", "katʁ vɛ̃ diz ɥit"),
])
def test_vingt_keeps_its_t_silent_elsewhere(text, expected):
    assert _t(text) == expected


# Martinon (1913: 234-235, 371): the old [v] of neuf survives in neu(f) ans,
# dix-neu(f) ans and neu(f) heures; before other plurals, neuf keeps [f]
# (neuf amis, neuf années), and neuf en tout is no plural at all.
@pytest.mark.parametrize("text, expected", [
    ("neuf ans", "nœv‿ ɑ̃"), ("dix-neuf ans", "diz nœv‿ ɑ̃"),
    ("vingt-neuf ans", "vɛ̃t nœv‿ ɑ̃"), ("neuf heures", "nœv‿ œʁ"),
    ("il y en a neuf en tout", "il i ɑ̃n‿ a nœf ɑ̃ tu"), ("neuf amis", "nœf ami"),
    ("neuf années", "nœf ane"),
])
def test_neuf_links_with_v_before_ans_and_heures_only(text, expected):
    assert _t(text) == expected


# Martinon (1913: 331): the final st sounds in est and ouest, and is mute in
# the verb e(st); 370: the d of sud always sounds, the d of nord never, and
# nord-est is best said without it. Lexique 3.83: nord-est [nOREst], sud-est
# [sydEst], sud-ouest [sydwEst], est-allemand [Estal°m@].
@pytest.mark.parametrize("text, expected", [
    ("nord-est", "nɔʁ‿ ɛst"), ("sud-est", "syd‿ ɛst"), ("sud", "syd"),
    ("ouest", "wɛst"), ("sud-ouest", "syd wɛst"), ("nord-ouest", "nɔʁ wɛst"),
    ("est-allemand", "ɛst aləmɑ̃"), ("Nord-Est", "nɔʁ‿ ɛst"),
])
def test_est_in_a_compound_is_the_noun(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("il est là", "il ɛ la"), ("le nord est froid", "lə nɔʁ‿ ɛ fʁwa"),
    ("est-ce", "ɛ sə"), ("c'est", "sɛ"),
])
def test_the_verb_est_is_unchanged(text, expected):
    assert _t(text) == expected


# Martinon (1913: 161): the nt of the third-person plural changes nothing
# (ils aime(nt) bien), and this mute -ent keeps verbs spelled like nouns and
# adjectives in tonic -ent: résident et président, content et couvent. After
# the subject clitic ils or elles the word is the verb.
@pytest.mark.parametrize("text, expected", [
    ("ils parlent", "il paʁl"), ("elles mangent", "ɛl mɑ̃ʒ"),
    ("ils couvent", "il kuv"), ("ils président", "il pʁezid"),
    ("qu'ils parlent", "kil paʁl"), ("qu’elles viennent", "kɛl vjɛn"),
    ("ils jouent", "il ʒu"), ("ils créent", "il kʁe"), ("ils lient", "il li"),
    ("Ils parlent", "il paʁl"), ("s'ils parlent", "sil paʁl"),
    ("lorsqu'elles mangent", "lɔʁskɛl mɑ̃ʒ"),
])
def test_verbal_ent_is_mute_after_ils_and_elles(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("le couvent", "lə kuvɑ̃"), ("le président", "lə pʁezidɑ̃"),
    ("un client", "œ̃ kljɛ̃"), ("il parle souvent", "il paʁl suvɑ̃"),
    ("ils, souvent", "il suvɑ̃"),
])
def test_ent_keeps_its_nasal_vowel_elsewhere(text, expected):
    assert _t(text) == expected


def test_the_loader_keeps_the_spelling_fields():
    rules = {r.id: r for r in o2i.get("fr-FR").sandhi_rules}
    assert rules["FR_NEUF_V_BEFORE_ANS"].right_spelling == "^ans$"
    assert rules["FR_ENT_MUTE_AFTER_ILS"].left_spelling is not None


# The regional specs inherit the rules by id and read the same spelling.
@pytest.mark.parametrize("code", ["fr-CA", "fr-BE", "fr-CH", "fr-CI"])
def test_the_regional_specs_inherit_the_rules(code):
    assert _t("vingt-deux", code).startswith("vɛ̃t ")
    assert not _t("quatre-vingt-deux", code).split()[1].endswith("t")
    assert _t("ils parlent", code).endswith("paʁl")
