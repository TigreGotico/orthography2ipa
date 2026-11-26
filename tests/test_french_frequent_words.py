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


# Martinon (1913: 331): final ⟨st⟩ is mute in the verb e(st). Larousse, s.v.
# être (Homonymes): est is a homonym of ai, ais, haie and hais.
@pytest.mark.parametrize("text, expected", [
    ("est", "ɛ"), ("c'est", "sɛ"), ("n'est", "nɛ"), ("c’est", "sɛ"),
    ("il est content", "il ɛ kɔ̃tɑ̃"),
])
def test_the_verb_est_is_open_e(text, expected):
    assert _t(text) == expected


def test_the_noun_est_after_l_keeps_its_st():
    assert _t("l'est") == "lɛst"


# Martinon (1913: 236): ⟨g⟩ is mute in vin(gt) and its derivatives,
# lon(g)temps and doi(gt).
@pytest.mark.parametrize("text, expected", [
    ("vingt", "vɛ̃"), ("vingtaine", "vɛ̃tɛn"), ("vingtième", "vɛ̃tjɛm"),
    ("doigt", "dwa"), ("longtemps", "lɔ̃tɑ̃"),
])
def test_g_before_t_is_mute(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("langue", "lɑ̃ɡ"), ("vingt et un", "vɛ̃ e œ̃"), ("gare", "ɡaʁ"),
])
def test_g_elsewhere_is_untouched(text, expected):
    assert _t(text) == expected


# Martinon (1913: 236): word-final ⟨g⟩ is not pronounced in French words;
# it survives in the spelling after a nasal: ran(g), san(g), étan(g),
# haren(g), coin(g), poin(g), lon(g).
@pytest.mark.parametrize("text, expected", [
    ("long", "lɔ̃"), ("longs", "lɔ̃"), ("sang", "sɑ̃"), ("rang", "ʁɑ̃"),
    ("étang", "etɑ̃"), ("hareng", "aʁɑ̃"), ("poing", "pwɛ̃"),
])
def test_final_g_after_a_nasal_is_mute(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("linge", "lɛ̃ʒ"), ("langue", "lɑ̃ɡ"), ("longue", "lɔ̃ɡ"),
])
def test_g_before_a_vowel_letter_is_not_final(text, expected):
    assert _t(text) == expected


# Martinon (1913: 226): before a consonant ⟨ch⟩ is learned and keeps the
# velar sound; the consonants are l, m, n, r (chlore, technique, chrétien).
@pytest.mark.parametrize("text, expected", [
    ("chrétien", "kʁetjɛ̃"), ("chronologie", "kʁɔnɔlɔʒi"), ("chlore", "klɔʁ"),
    ("technique", "tɛknik"), ("chrome", "kʁɔm"),
])
def test_ch_before_l_m_n_r_is_k(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("chat", "ʃa"), ("chef", "ʃɛf"), ("chœur", "ʃœʁ"),
])
def test_ch_before_a_vowel_stays_sh(text, expected):
    assert _t(text) == expected


@pytest.mark.xfail(strict=True, raises=AssertionError,
                   reason="German and Slavic loans keep [ʃ] before a sonorant")
def test_chleuh_keeps_sh():
    # chleuh [ʃlø] (wikipron fr) is a loan, outside Martinon's learned words;
    # the rule reads it [klø], like kalachnikov and punchline.
    assert _t("chleuh") == "ʃlø"


# Martinon (1913: 129, 331): in ⟨-empt⟩ and ⟨-ompt⟩ neither p nor t sounds
# (exempt, prompt, rompt).
@pytest.mark.parametrize("text, expected", [
    ("prompt", "pʁɔ̃"), ("rompt", "ʁɔ̃"), ("exempt", "ɛɡzɑ̃"),
])
def test_p_of_final_mpt_is_mute(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("exemption", "ɛɡzɑ̃psjɔ̃"), ("symptôme", "sɛ̃ptom"),
])
def test_p_before_a_non_final_t_is_kept(text, expected):
    assert _t(text) == expected


# Martinon (1913: 285): p is mute in com(p)te and all its derivatives,
# com(p)tabilité included, but not in exemption, présomption or symptôme.
@pytest.mark.parametrize("text, expected", [
    ("compte", "kɔ̃t"), ("compter", "kɔ̃te"), ("comptable", "kɔ̃tabl"),
    ("comptoir", "kɔ̃twaʁ"), ("décompte", "dekɔ̃t"), ("acompte", "akɔ̃t"),
])
def test_p_of_the_compte_family_is_mute(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text", ["somptueux", "présomption", "symptôme"])
def test_p_outside_the_compte_family_is_kept(text):
    assert "p" in _t(text)[2:]


# Martinon (1913: 123): the Latin final -um is [ɔm], also in fully French
# words (album, forum, géranium); 130: parfum keeps the nasal vowel.
@pytest.mark.parametrize("text, expected", [
    ("forum", "fɔʁɔm"), ("album", "albɔm"), ("minimum", "minimɔm"),
    ("maximum", "maksimɔm"), ("podium", "pɔdjɔm"), ("albums", "albɔm"),
    ("rhum", "ʁɔm"),
])
def test_final_um_is_om(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("parfum", "paʁfœ̃"), ("parfums", "paʁfœ̃"), ("humble", "œ̃bl"),
    ("brun", "bʁœ̃"), ("plume", "plym"),
])
def test_um_counter_cases(text, expected):
    assert _t(text) == expected


# Fougeron & Smith (1993: 74-75), JIPA 23(2): parking [paʁkiŋ]; the velar
# nasal occurs only word-finally in borrowed, usually English, words.
# Martinon (1913: 145): the English final -ing is not nasalised.
@pytest.mark.parametrize("text, expected", [
    ("parking", "paʁkiŋ"), ("camping", "kɑ̃piŋ"), ("jogging", "ʒɔɡiŋ"),
    ("smoking", "smɔkiŋ"), ("ping", "piŋ"),
])
def test_final_ing_is_oral_i_and_velar_nasal(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("vingt", "vɛ̃"), ("linge", "lɛ̃ʒ"), ("lingot", "lɛ̃ɡo"),
])
def test_ing_inside_a_word_stays_nasal(text, expected):
    assert _t(text) == expected


# Martinon (1913: 93): in ⟨-gueil⟩ the ⟨ue⟩ is the vowel eu (orgueil).
def test_orgueil():
    assert _t("orgueil") == "ɔʁɡœj"


# Martinon (1913: 241): the ⟨u⟩ of ⟨gu⟩ is pronounced before the mute ⟨ë⟩ of
# aiguë, ambiguë, ciguë.
@pytest.mark.parametrize("text, expected", [
    ("ambiguë", "ɑ̃biɡy"), ("ciguë", "siɡy"), ("ambigüe", "ɑ̃biɡy"),
])
def test_gu_before_trema_e(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("Noël", "nɔɛl"), ("guerre", "ɡɛʁ"),
])
def test_trema_counter_cases(text, expected):
    assert _t(text) == expected


# Martinon (1913: 53): the final ⟨e⟩ of pied, sied, assied is close [e].
@pytest.mark.parametrize("text, expected", [
    ("pied", "pje"), ("pieds", "pje"), ("trépied", "tʁepje"),
])
def test_final_ied_is_close_mid(text, expected):
    assert _t(text) == expected


def test_ied_rule_needs_the_final_d():
    # pieu: ⟨i⟩ before ⟨eu⟩, no ⟨d⟩; sied is in Martinon's list.
    assert _t("pieu") == "pjø"
    assert _t("sied") == "sje"
