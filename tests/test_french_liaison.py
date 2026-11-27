"""French obligatory liaison (issue #1836).

A final consonant that is silent elsewhere sounds before a vowel-initial word
when the two words are closely tied. Only the liaisons that the source calls
obligatory are written. Each case is cited by page from Martinon, *Comment on
prononce le français* (Larousse, 1913), read in the archive.org scan
(https://archive.org/details/commentonprononc00martuoft); the h aspiré words
also from the OQLF list (Banque de dépannage linguistique, La prononciation du
h aspiré, read 2026-11-26) and Tranel (1995: 1). The expected IPA is written
here, never read back from the engine, and each rule has counter-cases.
"""
import pytest

import orthography2ipa as o2i


def _t(text, code="fr-FR"):
    return o2i.transcribe(text, code)


# Martinon (1913: 375): les, des, aux, ces, mes, tes, ses, nos, vos, leurs,
# certains, plusieurs and the numerals deux, trois, quatre-vingts link without
# exception before a noun; 374: after dans, dès, sans, chez, sous, and très.
@pytest.mark.parametrize("text, expected", [
    ("les amis", "lez‿ ami"), ("des enfants", "dez‿ ɑ̃fɑ̃"),
    ("aux armes", "oz‿ aʁm"), ("ces hommes", "sez‿ ɔm"), ("mes amis", "mez‿ ami"),
    ("leurs amis", "lœʁz‿ ami"), ("deux ans", "døz‿ ɑ̃"),
    ("trois hommes", "tʁwaz‿ ɔm"), ("quatre-vingts ans", "katʁə vɛ̃z‿ ɑ̃"),
    ("deux cents ans", "dø sɑ̃z‿ ɑ̃"), ("chez elle", "ʃez‿ ɛl"),
    ("sans amour", "sɑ̃z‿ amuʁ"), ("très utile", "tʁɛz‿ ytil"),
    ("dès à présent", "dɛz‿ a pʁezɑ̃"), ("les yeux", "lez‿ iø"),
    ("les oiseaux", "lez‿ wazo"), ("les héroïnes", "lez‿ eʁɔin"),
    ("les hôtels", "lez‿ otɛl"), ("les uns", "lez‿ œ̃"),
])
def test_z_after_a_determiner_a_numeral_or_a_preposition(text, expected):
    assert _t(text) == expected


# Martinon (1913: 376): nous, vous, ils, elles before the verb or before en and
# y; out of that position, no link (pour vous et pour nous).
@pytest.mark.parametrize("text, expected", [
    ("nous avons", "nuz‿ avɔ̃"), ("vous êtes", "vuz‿ ɛt"), ("ils ont", "ilz‿ ɔ̃"),
    ("elles aiment", "ɛlz‿ ɛm"), ("elles y vont", "ɛlz‿ i vɔ̃"),
    ("ils en ont", "ilz‿ ɑ̃n‿ ɔ̃"), ("qu'ils aient", "kilz‿ ɛ"),
])
def test_z_after_a_pronoun_before_its_verb(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("pour vous et pour nous", "puʁ vu e puʁ nu"), ("vous aussi", "vu osi"),
    ("chez vous à Paris", "ʃe vu a paʁi"), ("ont-ils été", "ɔ̃t‿ il ete"),
    ("deux et deux", "dø e dø"), ("trois ou quatre", "tʁwa u katʁ"),
    ("le deux avril", "lə dø avʁil"),
])
def test_no_z_where_the_word_does_not_lean_on_the_next(text, expected):
    assert _t(text) == expected


# Martinon (1913: 248, 251-254, 358): no liaison before an h aspiré word, oui,
# onze, the numeral huit, uhlan, or a y that the next vowel makes a glide.
@pytest.mark.parametrize("text, expected", [
    ("les héros", "le eʁo"), ("les haricots", "le aʁiko"), ("les hiboux", "le ibu"),
    ("des hasards", "de azaʁ"), ("les hauteurs", "le otœʁ"), ("les haches", "le aʃ"),
    ("les huit", "le ɥit"), ("les onze", "le ɔ̃z"), ("un héros", "œ̃ eʁo"),
    ("en haut", "ɑ̃ o"), ("c'est honteux", "sɛ ɔ̃tø"), ("six héros", "si eʁo"),
    ("cette hache", "sɛt aʃ"), ("une halte", "yn alt"),
    # humer (OQLF, the main aspirate-h words): every regular form blocks
    ("ils humaient", "il ymɛ"), ("ils humèrent", "il ymɛʁ"),
    ("nous humons", "nu ymɔ̃"), ("en humant", "ɑ̃ ymɑ̃"),
    # huer (Académie française, « huer »: le h est aspiré): its forms in hu-
    # that do not start hue- or hué- block too
    ("nous huons", "nu yɔ̃"), ("ils huaient", "il yɛ"), ("en huant", "ɑ̃ yɑ̃"),
])
def test_no_liaison_before_an_h_aspire_word(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    # the stem hum- also opens words whose h is mute: they still link
    ("les humains", "lez‿ ymɛ̃"), ("des humoristes", "dez‿ ymɔʁist"),
    ("les huiles", "lez‿ ɥil"),
])
def test_a_mute_h_after_the_humer_stem_still_links(text, expected):
    assert _t(text) == expected


# Martinon (1913: 363-366): est, sont, ont, tout, quand, quant, dont, grand
# link with [t]; not before et or ou (366: il est grand et fort; 367: le tout
# et la partie).
@pytest.mark.parametrize("text, expected", [
    ("il est allé", "il ɛt‿ ale"), ("c'est un ami", "sɛt‿ œ̃n‿ ami"),
    ("ils sont arrivés", "il sɔ̃t‿ aʁive"), ("tout à fait", "tut‿ a fɛ"),
    ("quand il viendra", "kɑ̃t‿ il vjɛ̃dʁa"), ("dont il est", "dɔ̃t‿ il ɛ"),
    ("quant à", "kɑ̃t‿ a"), ("tout est fini", "tut‿ ɛ fini"),
    ("grand et fort", "ɡʁɑ̃ e fɔʁ"), ("le tout et la partie", "lə tu e la paʁti"),
    # Martinon (1913: 365-366) links grand only before its noun; two words
    # cannot show the noun, so grand does not link (il est grand aussi).
    ("il est grand aussi", "il ɛ ɡʁɑ̃ osi"),
])
def test_t_after_est_and_the_proclitics(text, expected):
    assert _t(text) == expected


# Martinon (1913: 365): ving(t) thommes, cen(t) thommes; 253 note 2 and 358
# note 1: cent huit and cent un without the link.
@pytest.mark.parametrize("text, expected", [
    ("vingt ans", "vɛ̃t‿ ɑ̃"), ("cent ans", "sɑ̃t‿ ɑ̃"), ("cent hommes", "sɑ̃t‿ ɔm"),
    ("vingt-deux ans", "vɛ̃t døz‿ ɑ̃"), ("cent un", "sɑ̃ œ̃"), ("cent huit", "sɑ̃ ɥit"),
    ("sans eux", "sɑ̃z‿ ø"), ("du sang au doigt", "dy sɑ̃ o dwa"),
])
def test_vingt_and_cent_link_with_t_before_the_noun(text, expected):
    assert _t(text) == expected


# Martinon (1913: 364): the inverted subject links with [t]; 373, 379: an
# imperative links with [z] before a hyphenated y or en.
@pytest.mark.parametrize("text, expected", [
    ("dit-il", "dit‿ il"), ("est-il", "ɛt‿ il"), ("a-t-il", "a t‿ il"),
    ("parlent-ils", "paʁlt‿ il"), ("vient-il", "vjɛ̃t‿ il"),
    ("vas-y", "vaz‿ i"), ("allez-y", "alez‿ i"), ("prends-en", "pʁɑ̃z‿ ɑ̃"),
    ("il dit", "il di"), ("est-ce", "ɛ sə"),
])
def test_liaison_across_a_hyphen(text, expected):
    assert _t(text) == expected


# Martinon (1913: 390-391): un, aucun, en, on link with [n] and keep the nasal
# vowel; un ou deux, parlez-en à votre père and a-t-on été have no link.
@pytest.mark.parametrize("text, expected", [
    ("un ami", "œ̃n‿ ami"), ("aucun homme", "okœ̃n‿ ɔm"), ("en effet", "ɑ̃n‿ efɛ"),
    ("on a", "ɔ̃n‿ a"), ("il y en a", "il i ɑ̃n‿ a"), ("d'un ami", "dœ̃n‿ ami"),
    ("l'on a", "lɔ̃n‿ a"), ("un ou deux", "œ̃ u dø"),
    ("parlez-en à", "paʁlez‿ ɑ̃ a"), ("a-t-on été", "a t‿ ɔ̃ ete"),
])
def test_n_after_un_aucun_en_on(text, expected):
    assert _t(text) == expected


# Martinon (1913: 359): premier and dernier before their noun link with [ʁ]
# and open the e.
@pytest.mark.parametrize("text, expected", [
    ("premier enfant", "pʁəmjɛʁ‿ ɑ̃fɑ̃"), ("dernier étage", "dɛʁnjɛʁ‿ etaʒ"),
    ("le premier à parler", "lə pʁəmje a paʁle"),
])
def test_r_after_premier_and_dernier(text, expected):
    assert _t(text) == expected


# Martinon (1913: 364 note): est always links and et never.
@pytest.mark.parametrize("text, expected", [
    ("et un", "e œ̃"), ("et elle", "e ɛl"),
])
def test_no_liaison_after_et(text, expected):
    assert _t(text) == expected


# The regional specs inherit the rules by id.
@pytest.mark.parametrize("code", ["fr-CA", "fr-BE", "fr-CH", "fr-CI"])
def test_the_regional_specs_inherit_the_liaison(code):
    assert "z‿" in _t("les amis", code)
    assert "z‿" not in _t("les héros", code)
    assert "n‿" in _t("un ami", code)


# Martinon (1913: 328, 345, 248) and Tranel (1995: 9, (23)): before an h aspiré
# the numerals take the form they have before a consonant.
@pytest.mark.parametrize("text, expected", [
    ("six haricots", "si aʁiko"), ("dix héros", "di eʁo"), ("huit haricots", "ɥi aʁiko"),
    ("six hommes", "siz‿ ɔm"), ("huit hommes", "ɥit‿ ɔm"), ("six héroïnes", "siz‿ eʁɔin"),
])
def test_six_dix_huit_before_an_h_aspire(text, expected):
    assert _t(text) == expected


# A hyphen does not hide the right word from its exclusions: Martinon (1913:
# 253 note 2) cent-huit sans liaison; 358 note 1 cent un; 253 trois huit.
@pytest.mark.parametrize("text, expected", [
    ("cent-huit", "sɑ̃ ɥit"), ("cent-onze", "sɑ̃ ɔ̃z"), ("cent-un", "sɑ̃ œ̃"),
    ("deux-cent-un", "dø sɑ̃ œ̃"), ("trois-huit", "tʁwa ɥit"), ("le Très-Haut", "lə tʁɛ o"),
])
def test_a_hyphenated_right_word_keeps_its_exclusions(text, expected):
    assert _t(text) == expected


# Martinon (1913: 390) vingt et un avril; 376 plusieurs ont prétendu and
# chez vous / entre nous before a subject; 345 the months.
@pytest.mark.parametrize("text, expected", [
    ("vingt et un avril", "vɛ̃t‿ e œ̃ avʁil"), ("le trente et un août", "lə tʁɑ̃t‿ e œ̃ au"),
    ("certains ont dit", "sɛʁtɛ̃ ɔ̃ di"), ("certains auteurs", "sɛʁtɛ̃z‿ otœʁ"),
    ("plusieurs autres", "plyzjœʁz‿ otʁ"),
    ("chez vous il fait froid", "ʃe vu il fɛ fʁwa"), ("entre nous on dit", "ɑ̃tʁ nu ɔ̃ di"),
    ("le premier avril", "lə pʁəmje avʁil"), ("vingt-et-un ans", "vɛ̃t‿ e œ̃n‿ ɑ̃"),
])
def test_no_liaison_where_martinon_has_none(text, expected):
    assert _t(text) == expected


# Martinon (1913: 251, 254): hongrois, Huns; the Swiss huitante is the numeral.
@pytest.mark.parametrize("text, code, expected", [
    ("les Hongrois", "fr-FR", "le ɔ̃ɡʁwa"), ("les Huns", "fr-FR", "le œ̃"),
    ("les huitante", "fr-CH", "le ɥitɑ̃t"),
])
def test_more_h_aspire_and_numeral_blocks(text, code, expected):
    assert _t(text, code) == expected


# Martinon (1913: 358): il es(t) tonze heures, avec liaison, cas spécial.
def test_est_links_before_onze():
    assert _t("il est onze heures") == "il ɛt‿ ɔ̃z‿ œʁ"
    assert _t("les onze") == "le ɔ̃z"


# The enchaînement rules read no spelling, so the reference engine keeps them
# when the caller passes no spellings.
def test_the_enchainement_rules_run_without_spellings():
    engine = o2i.SandhiEngine(o2i.get("fr-FR").sandhi_rules)
    assert engine.apply(["sɛt", "ɔm"]) == ["sɛt‿", "ɔm"]
    assert engine.apply(["sɛt", "aʃ"], spellings=["cette", "hache"]) == ["sɛt", "aʃ"]
    assert engine.apply(["le", "ami"], spellings=["les", "amis"]) == ["lez‿", "ami"]


def test_the_h_aspire_stems_are_written_once():
    rules = o2i.get("fr-FR").sandhi_rules
    assert sum("haricot" in (r.right_spelling or "") for r in rules) == 1


# Martinon (1913: 358): before a y that the next vowel makes a glide, and
# before onze, there is no liaison: the word counts as consonant-initial, so
# six, dix and huit take the form they have before a consonant (345).
@pytest.mark.parametrize("text, expected", [
    ("dix watts", "di wat"), ("huit whiskies", "ɥi wiski"),
    ("six onzièmes", "si ɔ̃zjɛm"), ("huit onzièmes", "ɥi ɔ̃zjɛm"), ("six yeux", "siz‿ iø"),
    # Martinon (1913: 346): six-huit, the musical measure, keeps a hard s.
    ("six-huit", "sis ɥit"),
])
def test_six_dix_huit_before_a_glide_or_onze(text, expected):
    assert _t(text) == expected


# Martinon (1913: 365): gran(d) thomme, the adjective before its noun links;
# 366: il est gran(d) et fort, no link when it is not before its noun.
@pytest.mark.parametrize("text, expected", [
    ("grand homme", "ɡʁɑ̃t‿ ɔm"), ("grand hôtel", "ɡʁɑ̃t‿ otɛl"), ("grand ami", "ɡʁɑ̃t‿ ami"),
    ("grand arbre", "ɡʁɑ̃t‿ aʁbʁ"), ("il est grand aussi", "il ɛ ɡʁɑ̃ osi"),
    ("grand et fort", "ɡʁɑ̃ e fɔʁ"), ("il est grand à Paris", "il ɛ ɡʁɑ̃ a paʁi"),
    ("le plus grand en France", "lə ply ɡʁɑ̃ ɑ̃ fʁɑ̃s"), ("grand héros", "ɡʁɑ̃ eʁo"),
])
def test_grand_links_before_its_noun(text, expected):
    assert _t(text) == expected


# Martinon (1913: 358): no liaison before the numeral un (les numéro(s) un et
# deux); the article un after les links as a pronoun (les uns).
@pytest.mark.parametrize("text, expected", [
    ("les numéros un et deux", "le nymeʁo œ̃ e dø"), ("les un", "le œ̃"), ("les uns", "lez‿ œ̃"),
])
def test_no_liaison_before_the_numeral_un(text, expected):
    assert _t(text) == expected


def test_six_drops_its_consonant_before_a_y_glide():
    # Martinon (1913: 358): de(s) yachts, de(s) youyous, no liaison before a y
    # glide. Only the numeral is checked: the letters do not read ⟨yacht⟩
    # (TLFi [jɔt]), which no entry states.
    assert _t("six yachts").split()[0] == "si"
    assert _t("dix youyous").split()[0] == "di"


# OQLF, Prononciation de six et dix: as pronouns six and dix are [sis] [dis]
# (il lui en reste six à faire [sisa]); as determiners before a vowel [siz]
# [diz] (six hommes, trente-six enfants). Martinon (1913: 345): the [z] is a
# liaison with the plural the numeral multiplies. A function word after the
# numeral is no noun it multiplies.
@pytest.mark.parametrize("text, expected", [
    ("six en tout", "sis ɑ̃ tu"), ("dix en tout", "dis ɑ̃ tu"), ("six ou sept", "sis u sɛt"),
    ("six avec moi", "sis avɛk mwa"), ("dix après", "dis apʁɛ"), ("six entre eux", "sis ɑ̃tʁ‿ ø"),
    ("six ans", "siz‿ ɑ̃"), ("six enfants", "siz‿ ɑ̃fɑ̃"), ("dix orteils", "diz‿ ɔʁtɛj"),
    ("trente-six enfants", "tʁɑ̃t siz‿ ɑ̃fɑ̃"),
])
def test_six_and_dix_keep_their_s_before_a_function_word(text, expected):
    assert _t(text) == expected
