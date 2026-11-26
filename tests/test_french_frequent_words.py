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


# Martinon (1913: 347): the simple [s] of soixante and its derivatives.
@pytest.mark.parametrize("text, expected", [
    ("soixante", "swasɑ̃t"), ("soixantaine", "swasɑ̃tɛn"),
    ("soixantième", "swasɑ̃tjɛm"),
])
def test_x_of_soixante_is_s(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("noix", "nwa"), ("choix", "ʃwa"), ("taxi", "taksi"),
])
def test_x_elsewhere_after_oi_or_a_vowel(text, expected):
    assert _t(text) == expected


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


# Martinon (1913: 213): after a nasal vowel final ⟨c⟩ stayed mute (ban(c),
# blan(c), fran(c), jon(c), tron(c)); donc is mute in principle. 214 n. 1:
# zinc should be written zing.
@pytest.mark.parametrize("text, expected", [
    ("blanc", "blɑ̃"), ("blancs", "blɑ̃"), ("banc", "bɑ̃"), ("franc", "fʁɑ̃"),
    ("tronc", "tʁɔ̃"), ("vainc", "vɛ̃"), ("donc", "dɔ̃"), ("zinc", "zɛ̃ɡ"),
])
def test_final_c_after_a_nasal_is_mute(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("sac", "sak"), ("parc", "paʁk"), ("blanche", "blɑ̃ʃ"),
])
def test_final_c_elsewhere_sounds(text, expected):
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


# Martinon (1913: 171): ⟨e⟩ before a doubled consonant letter is not a mute
# e, except in dessus, dessous and the prefix re- before ⟨ss⟩ (ressembler,
# ressort, ressource). 59: the open e of -esse (vieillesse) and -effe (greffe).
@pytest.mark.parametrize("text, expected", [
    ("message", "mesaʒ"), ("dessert", "desɛʁ"), ("cesser", "sese"),
    ("serrer", "seʁe"), ("terrible", "teʁibl"), ("nettoyer", "netwaje"),
    ("effet", "efɛ"), ("dessin", "desɛ̃"),
])
def test_e_before_a_doubled_consonant_is_not_mute(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("messe", "mɛs"), ("presse", "pʁɛs"), ("greffe", "ɡʁɛf"),
])
def test_e_before_a_doubled_consonant_in_the_last_syllable_is_open(
        text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("ressembler", "ʁəsɑ̃ble"), ("ressource", "ʁəsuʁs"),
    ("dessus", "dəsy"), ("dessous", "dəsu"),
])
def test_re_ss_dessus_and_nasal_doubles_keep_their_reading(text, expected):
    assert _t(text) == expected


# Martinon (1913: 62): poêle (pwâl) and its derivatives.
@pytest.mark.parametrize("text, expected", [
    ("poêle", "pwal"), ("poêlon", "pwalɔ̃"),
])
def test_oe_circumflex_is_wa(text, expected):
    assert _t(text) == expected


def test_noel_keeps_two_vowels():
    assert _t("Noël") == "nɔɛl"


# Martinon (1913: 328): the ⟨t⟩ of huit is pronounced (page huit, huit hommes)
# except before a plural that begins with a consonant (hui(t) sous).
# Martinon (1913: 345): six and dix end in [s] (j'en ai six, page dix), are
# mute before a consonant plural (di(x) francs) and take [z] before a vowel
# (six hommes).
@pytest.mark.parametrize("text, expected", [
    ("huit", "ɥit"), ("six", "sis"), ("dix", "dis"),
    ("huit jours", "ɥi ʒuʁ"), ("six sous", "si su"), ("dix jours", "di ʒuʁ"),
    ("six ans", "siz‿ ɑ̃"), ("dix heures", "diz‿ œʁ"),
    ("huit heures", "ɥit‿ œʁ"),
])
def test_huit_six_dix(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("tu dis", "ty di"), ("sept jours", "sɛt ʒuʁ"),
])
def test_numeral_sandhi_counter_cases(text, expected):
    assert _t(text) == expected


# Martinon (1913: 346): dix-huit (dizuite), the soft s of dix-neuf, and the
# hard s of dix-sept (dis-sète). 328, 345: before a month the consonant of
# huit, six and dix stays (le huit mai; six and dix before mai, juin,
# septembre). 234-235: neuf links with [v] only in neuf ans and neuf heures.
@pytest.mark.parametrize("text, expected", [
    ("dix-sept", "dis sɛt"), ("dix-huit", "diz ɥit"), ("dix-neuf", "diz nœf"),
    ("soixante-dix-sept", "swasɑ̃t dis sɛt"),
    ("quatre-vingt-dix-huit", "katʁ vɛ̃ diz ɥit"),
    ("le huit mai", "lə ɥit me"), ("le six mai", "lə sis me"),
    ("le dix janvier", "lə dis ʒɑ̃vje"),
    ("neuf heures", "nœv‿ œʁ"), ("dix-neuf heures", "diz nœv‿ œʁ"),
    # neuf ans is [nœv‿ɑ̃] in Martinon; the IPA of ans is that of en, so the
    # rule leaves it (see test_neuf_links_with_v_before_heures_only).
    ("neuf ans", "nœf ɑ̃"),
])
def test_numeral_compounds_months_and_neuf(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("neuf euros", "nœf øʁo"), ("neuf", "nœf"), ("six mois", "si mwa"),
    ("huit jours", "ɥi ʒuʁ"),
])
def test_numeral_counter_cases(text, expected):
    assert _t(text) == expected


# The numeral sandhi reads only the three numerals: [dit] and [sit] are
# other words (vous dites, le site, il cite).
@pytest.mark.parametrize("text, expected", [
    ("vous dites que", "vu dit kə"), ("le site de la ville", "lə sit də la vil"),
    ("il cite Platon", "il sit platɔ̃"),
])
def test_numeral_sandhi_leaves_dit_and_sit_alone(text, expected):
    assert _t(text) == expected


# Martinon (1913: 345): before a month that begins with a vowel, dix and six
# are [dis] [sis] (six avril, si-savril); "si zet huit" is an abuse of
# liaison. Before a plural they multiply, [z] stays (six hommes).
@pytest.mark.parametrize("text, expected", [
    ("le six avril", "lə sis avʁil"), ("le dix octobre", "lə dis ɔktɔbʁ"),
    ("six et huit", "sis e ɥit"), ("six ou sept", "sis u sɛt"),
    ("six enfants", "siz‿ ɑ̃fɑ̃"), ("dix ans", "diz‿ ɑ̃"),
])
def test_six_and_dix_link_only_before_what_they_multiply(text, expected):
    assert _t(text) == expected


# Martinon (1913: 328, 345): the consonant falls only before the plural the
# numeral multiplies, never before a preposition or article.
@pytest.mark.parametrize("text, expected", [
    ("six de mes amis", "sis də me ami"), ("huit de plus", "ɥit də ply"),
    ("ils sont dix pour", "il sɔ̃ dis puʁ"), ("dix sur vingt", "dis syʁ vɛ̃"),
    ("huit mes", "ɥit me"),
])
def test_numeral_keeps_its_consonant_before_a_function_word(text, expected):
    assert _t(text) == expected


# Martinon (1913: 234-235): neu(f) heures [v]. The rule reads IPA, and ans
# has the IPA of en and an, so neuf ans is left as [nœf ɑ̃].
@pytest.mark.parametrize("text, expected", [
    ("neuf heures", "nœv‿ œʁ"), ("il y en a neuf en tout", "il i ɑ̃ a nœf ɑ̃ tu"),
    ("dix-neuf en tout", "diz nœf ɑ̃ tu"),
])
def test_neuf_links_with_v_before_heures_only(text, expected):
    assert _t(text) == expected
