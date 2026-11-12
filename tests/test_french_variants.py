"""Regional French: each variant states only what an open source states.

``fr-CA``, ``fr-BE``, ``fr-CH`` and ``fr-CI`` are thin variants of ``fr-FR``.
Each rule is pinned with the source that states it, an adversarial counter
case, and the text of ``fr-FR`` it must leave alone. The expected IPA is
written in the test, never read back from the engine.

Sources, all opened:

* Hall (2016), *Contrast and phonological activity in the vowel system of
  Laurentian French*, TWPL 37: p. 2 ex. (2) (assibilation of /t d/ before
  /i y/), p. 7 ex. (11)-(14) (final-syllable laxing).
* Dow (2019), CLA proceedings: p. 1 (affrication before /i j y ɥ/), p. 2
  (obligatory within words).
* Burness et al. (2022), CLA proceedings: p. 1.
* PFC, *Le français expliqué: Prononciation, I. Le système vocalique*, d)
  Variation: pâte ~ patte by length at Neuchâtel and Tournai, by timbre at
  Nyon, merged at Abidjan; faites ~ fête and belle ~ bêle by length at
  Neuchâtel; brin ~ brun kept at Tournai, Nyon and Abidjan. For the length
  points the page says "la distinction entre les deux voyelles est substituée
  par une différence de longueur", and it lists Tournai under "rat = ras":
  one timbre, so the long vowel is [aː].
"""
import json
import string
import warnings
from pathlib import Path

import pytest

import orthography2ipa as o2i

TEXTS = json.loads(Path(__file__).with_name("data").joinpath(
    "french_assistant_sentences.json").read_text(encoding="utf-8"))

STANDARD_OTHERS = ["fr", "fr-FR", "fr-LU", "fr-MC", "fr-SN", "fr-CD", "fr-CM",
                   "fr-MA", "fr-HT"]

# French locales of CLDR, macro-regions of UN M49 and countries where French
# is not official: none has a spec, so none may reach a sibling variant.
UNLISTED_REGIONS = ["fr-BL", "fr-MF", "fr-GQ", "fr-SY", "fr-001", "fr-150",
                    "fr-155", "fr-029", "fr-US", "fr-AD", "fr-ES", "fr-IT",
                    "fr-DE"]
VARIANT_REGIONS = {"FR", "CA", "BE", "CH", "CI"}


def _say(text, tag):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return o2i.transcribe(text, tag)


# --- fr-CA --------------------------------------------------------------

@pytest.mark.parametrize("text, expected", [
    ("petit", "pət͡si"),           # Hall 2016: 2, ex. (2c): [p(ə)tsi]
    ("têtu", "tɛt͡sy"),            # ex. (2d)
    ("dit", "d͡zi"),               # ex. (2a)
    ("du", "d͡zy"),                # ex. (2b)
    ("tu", "t͡sy"),                # Dow 2019: 1, before /y/
    ("nuit", "nɥi"),               # no stop before the glide: no affricate
    ("tuile", "t͡sɥɪl"),           # before /ɥ/ (Dow 2019: 1)
    ("tiens", "t͡sjɛ̃"),            # before the glide of ⟨ien⟩ (Dow 2019: 1)
    ("pitié", "pit͡sje"),          # before /j/
])
def test_quebec_affricates_a_coronal_stop_before_a_high_front_vocoid(
        text, expected):
    assert _say(text, "fr-CA") == expected


@pytest.mark.parametrize("text, expected", [
    ("trois", "tʁwa"),             # /w/ and /ʁ/ do not trigger it
    ("toit", "twa"),
    ("tête", "tɛt"),               # /t/ before a mid vowel
    ("dos", "do"),
    ("patte", "pat"),
])
def test_quebec_leaves_a_stop_before_other_sounds_alone(text, expected):
    assert _say(text, "fr-CA") == expected


@pytest.mark.parametrize("text, expected", [
    ("élite", "elɪt"),             # Hall 2016: 7, ex. (12a)
    ("annule", "anʏl"),            # ex. (12b)
    ("égoutte", "eɡʊt"),           # ex. (12c)
])
def test_quebec_laxes_a_high_vowel_in_a_closed_final_syllable(text, expected):
    assert _say(text, "fr-CA") == expected


@pytest.mark.parametrize("text, expected", [
    ("béni", "beni"),              # Hall 2016: 7, ex. (11a): open syllable
    ("début", "deby"),             # ex. (11b)
    ("dégoût", "deɡu"),            # ex. (11c)
    ("petits", "pət͡si"),          # a silent final letter does not close it
])
def test_quebec_keeps_a_high_vowel_tense_in_an_open_final_syllable(
        text, expected):
    assert _say(text, "fr-CA") == expected


def test_quebec_keeps_the_a_and_open_a_contrast():
    # Burness et al. 2022: 1 (patte [pat], pâte [pɑt])
    assert _say("patte", "fr-CA") == "pat"
    assert _say("pâte", "fr-CA") == "pɑt"


# --- fr-BE, fr-CH, fr-CI ------------------------------------------------

@pytest.mark.parametrize("tag, expected", [
    ("fr-BE", "paːt"),             # Tournai: rat = ras, pâte by length (PFC)
    ("fr-CH", "paːt"),             # Neuchâtel: pâte by length (PFC)
    ("fr-CI", "pat"),              # patte = pâte at Abidjan (PFC)
    ("fr-FR", "pɑt"),
])
def test_the_pate_patte_contrast_follows_the_region(tag, expected):
    assert _say("pâte", tag) == expected
    assert _say("patte", tag) == "pat"


@pytest.mark.parametrize("tag, fete, belle, bele", [
    ("fr-CH", "fɛːt", "bɛl", "bɛːl"),   # faites ~ fête, belle ~ bêle (PFC)
    ("fr-FR", "fɛt", "bɛl", "bɛl"),
    ("fr-BE", "fɛt", "bɛl", "bɛl"),     # the PFC page does not state it
    ("fr-CI", "fɛt", "bɛl", "bɛl"),
])
def test_the_circumflex_e_is_long_only_where_pfc_states_it(
        tag, fete, belle, bele):
    assert _say("fête", tag) == fete
    assert _say("faites", tag) == "fɛt"   # the short member of the pair
    assert _say("bêle", tag) == bele


@pytest.mark.parametrize("tag", ["fr-FR", "fr-CA", "fr-BE", "fr-CH", "fr-CI"])
def test_every_variant_keeps_brin_and_brun_apart(tag):
    # PFC page d) 2): the contrast survives at Tournai, Nyon and Abidjan;
    # fr-FR keeps both phonemes, so the variants inherit it.
    assert _say("brin", tag) == "bʁɛ̃"
    assert _say("brun", tag) == "bʁœ̃"


# --- resolution and inheritance -----------------------------------------

@pytest.mark.parametrize("tag", STANDARD_OTHERS)
def test_a_region_without_a_sourced_difference_reads_fr_fr(tag):
    assert o2i.resolve(tag) == "fr-FR"


@pytest.mark.parametrize("tag", UNLISTED_REGIONS)
def test_an_unlisted_french_region_reads_fr_fr(tag):
    assert o2i.resolve(tag) == "fr-FR"
    assert _say("pâte", tag) == "pɑt"


def test_every_two_letter_region_without_a_spec_reads_fr_fr():
    regions = [a + b for a in string.ascii_uppercase
               for b in string.ascii_uppercase]
    elsewhere = {f"fr-{r}": o2i.resolve(f"fr-{r}") for r in regions
                 if r not in VARIANT_REGIONS}
    assert len(elsewhere) == 26 * 26 - len(VARIANT_REGIONS)
    assert {tag: code for tag, code in elsewhere.items()
            if code != "fr-FR"} == {}


@pytest.mark.parametrize("tag", ["fr-CA", "fr-BE", "fr-CH", "fr-CI"])
def test_a_variant_inherits_fr_fr(tag):
    spec, base = o2i.get(tag), o2i.get("fr-FR")
    assert spec.code == tag
    assert spec.parent == "fr-FR"
    assert spec.word_internal_apostrophe is True
    assert spec.word_exceptions == base.word_exceptions
    assert spec.sandhi_rules == base.sandhi_rules


@pytest.mark.parametrize("tag, words", [
    # words that carry none of the variant's cited features read like fr-FR
    ("fr-BE", ["maison", "chat", "école", "parler", "brun", "d'accord"]),
    ("fr-CH", ["maison", "chat", "école", "parler", "brun", "d'accord"]),
    ("fr-CI", ["maison", "chat", "école", "parler", "brun", "d'accord"]),
    ("fr-CA", ["maison", "chat", "école", "parler", "brun", "d'accord"]),
])
def test_a_variant_reads_like_fr_fr_where_no_feature_applies(tag, words):
    for word in words:
        assert _say(word, tag) == _say(word, "fr-FR"), word


def test_the_assistant_sentences_differ_from_fr_fr_only_at_a_cited_feature():
    diffs = {"fr-BE": set(), "fr-CH": set(), "fr-CI": set()}
    for tag, found in diffs.items():
        for text in TEXTS:
            if _say(text, tag) != _say(text, "fr-FR"):
                found.add(text)
    # the sentences hold no ⟨â⟩; fr-CH differs only through ⟨ê⟩
    assert diffs["fr-BE"] == set()
    assert diffs["fr-CI"] == set()
    for text in diffs["fr-CH"]:
        assert "ê" in text


def test_a_laurentian_difference_is_always_a_cited_allophone():
    # Undo the four cited changes: what is left must be fr-FR, word for word.
    undo = {"ɪ": "i", "ʏ": "y", "ʊ": "u", "t͡s": "t", "d͡z": "d"}
    for text in TEXTS:
        ours = _say(text, "fr-CA")
        for cited, plain in undo.items():
            ours = ours.replace(cited, plain)
        assert ours == _say(text, "fr-FR"), text
