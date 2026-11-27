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
    ("trois hommes", "tʁwaz‿ ɔm"), ("quatre-vingts ans", "katʁ vɛ̃z‿ ɑ̃"),
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
])
def test_no_liaison_before_an_h_aspire_word(text, expected):
    assert _t(text) == expected


# Martinon (1913: 363-366): est, sont, ont, tout, quand, quant, dont, grand
# link with [t]; not before et or ou (366: il est grand et fort; 367: le tout
# et la partie).
@pytest.mark.parametrize("text, expected", [
    ("il est allé", "il ɛt‿ ale"), ("c'est un ami", "sɛt‿ œ̃n‿ ami"),
    ("ils sont arrivés", "il sɔ̃t‿ aʁive"), ("tout à fait", "tut‿ a fɛ"),
    ("quand il viendra", "kɑ̃t‿ il vjɛ̃dʁa"), ("dont il est", "dɔ̃t‿ il ɛ"),
    ("grand homme", "ɡʁɑ̃t‿ ɔm"), ("quant à", "kɑ̃t‿ a"),
    ("grand et fort", "ɡʁɑ̃ e fɔʁ"), ("le tout et la partie", "lə tu e la paʁti"),
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
