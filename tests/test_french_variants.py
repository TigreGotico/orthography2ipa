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
    ("tiens", "t͡sjẽ"),            # before the glide of ⟨ien⟩ (Dow 2019: 1)
    ("pitié", "pit͡sje"),          # before /j/
])
def test_quebec_affricates_a_coronal_stop_before_a_high_front_vocoid(
        text, expected):
    assert _say(text, "fr-CA") == expected


@pytest.mark.parametrize("text, expected", [
    ("trois", "tʁwɒ"),             # /w/ and /ʁ/ do not trigger it (final /a/
    ("toit", "twɒ"),               # is [ɒ], Dumas 1974: 27)
    ("tête", "tai̯t"),             # /t/ before a mid vowel (long [ɛː] -> [ai̯])
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
    # Burness et al. 2022: 1 (patte [pat], pâte [pɑt]); the long back vowel
    # of pâte is the diphthong [ɑu̯] (Dumas 1974: 15-16, Table II, p. 26)
    assert _say("patte", "fr-CA") == "pat"
    assert _say("pâte", "fr-CA") == "pɑu̯t"


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
    ("fr-BE", "fɛːt", "bɛl", "bɛːl"),   # Bardiaux et al. 2016: 40
    ("fr-CI", "fɛt", "bɛl", "bɛl"),
])
def test_the_circumflex_e_is_long_only_where_a_source_states_it(
        tag, fete, belle, bele):
    assert _say("fête", tag) == fete
    assert _say("faites", tag) == "fɛt"   # the short member of the pair
    assert _say("bêle", tag) == bele


@pytest.mark.parametrize("tag, brin, brun", [
    ("fr-FR", "bʁɛ̃", "bʁœ̃"), ("fr-BE", "bʁɛ̃", "bʁœ̃"),
    ("fr-CH", "bʁɛ̃", "bʁœ̃"), ("fr-CI", "bʁɛ̃", "bʁœ̃"),
    ("fr-CA", "bʁẽ", "bʁœ̃"),       # the front nasal is [ẽ] (Dumas 1974: 26)
    ("fr-FR-x-midi", "bʁɛŋ", "bʁœŋ"),  # vowel + appendix (Eychenne 2006: 115)
])
def test_every_variant_keeps_brin_and_brun_apart(tag, brin, brun):
    # PFC page d) 2): the contrast survives at Tournai, Nyon, Toulouse and
    # Abidjan; fr-FR keeps both phonemes, so the variants inherit it.
    assert _say("brin", tag) == brin
    assert _say("brun", tag) == brun


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


# A tag that adds an extension or a variant subtag still names its region
# (RFC 5646 §2.2.4-2.2.6), so the regional spec answers for it.
@pytest.mark.parametrize("tag, code", [
    ("fr-CA-u-mu-celsius", "fr-CA"), ("fr-CA-u-ca-gregory", "fr-CA"),
    ("fr-CA-1606nict", "fr-CA"), ("fr-Latn-CA-u-nu-latn", "fr-CA"),
    ("fr-BE-u-co-phonebk", "fr-BE"), ("fr-CH-u-nu-latn", "fr-CH"),
    ("fr-CI-u-nu-latn", "fr-CI"), ("fr-SN-u-nu-latn", "fr-FR"),
    ("fr-1606nict", "fr-FR"), ("fr-150-u-nu-latn", "fr-FR"),
])
def test_an_extension_or_variant_keeps_the_region(tag, code):
    assert o2i.resolve(tag) == code


#: The whole-word entries a variant states over those of fr-FR: vingt with
#: its final [t] (PFC consonant page II d) 4); Avanzi 2016, 2024), the
#: Laurentian long vowel of the fr-FR ⟨-er⟩ exceptions (Dumas 1974: 18-21)
#: and the [ø] of the Midi clitics (PFC e-caduc page, 'Timbre') with the
#: Midi readings of the fr-FR exceptions its rules would change.
OWN_EXCEPTIONS = {
    "fr-CA": {"mer": "mai̯ʁ", "mers": "mai̯ʁ", "fer": "fai̯ʁ", "fers": "fai̯ʁ",
              "cher": "ʃai̯ʁ", "chers": "ʃai̯ʁ", "hiver": "ivai̯ʁ",
              "hivers": "ivai̯ʁ", "enfer": "ɑ̃fai̯ʁ", "enfers": "ɑ̃fai̯ʁ",
              "amer": "amai̯ʁ", "amers": "amai̯ʁ", "hier": "jai̯ʁ",
              "hiers": "jai̯ʁ",
              "ver": "vai̯ʁ", "outremer": "utʁəmai̯ʁ"},
    "fr-BE": {"vingt": "vɛ̃t"}, "fr-CH": {"vingt": "vɛ̃t"},
    "fr-FR-x-midi": {"le": "lø", "de": "dø", "que": "kø", "ce": "sø",
                     "ne": "nø", "se": "sø", "je": "ʒø", "me": "mø",
                     "te": "tø", "ville": "vilə", "mille": "milə",
                     "lille": "lilə", "tranquille": "tʁaŋkilə",
                     "tranquillement": "tʁaŋkiləmaŋ", "enfer": "aɱfɛʁ",
                     "enfers": "aɱfɛʁ", "sens": "sans", "cancer": "kansɛʁ",
                     "cancers": "kansɛʁ", "cresson": "kʁøsɔŋ",
                     "cressonnière": "kʁøsɔnjɛʁə", "dessus": "døsy",
                     "dessous": "døsu", "parfum": "paʁfœŋ",
                     "parfums": "paʁfœŋ", "zinc": "zɛŋɡ",
                     "chnoque": "ʃnɔkə", "chnoques": "ʃnɔkə",
                     "chlingue": "ʃlɛŋɡə", "chlinguer": "ʃlɛŋɡe",
                     "donc": "dɔŋk"},
}


#: The fr-FR sandhi rules each variant restates by id: fr-CA so that the
#: high vowel left in an open syllable is tense (Hall 2016: 7) and so that
#: its vowel class holds the Laurentian vowels that open a word ([ẽ ɪ ʏ ʊ
#: ɒ]); every variant so that the words before which a numeral keeps its
#: consonant are also written in its own readings. On a base without one of
#: these fr-FR rules the restated rule stands at the end as the variant's own.
SANDHI_RESTATED = {
    "fr-CA": {"FR_DIX_Z_BEFORE_HUIT_NEUF", "FR_NUMERAL_MUTE_BEFORE_CONSONANT",
              "FR_HUIT_MUTE_BEFORE_CONSONANT", "FR_NUMERAL_Z_BEFORE_VOWEL",
              "FR_NEUF_V_BEFORE_HEURES", "FR_LIAISON_Z", "FR_LIAISON_T",
              "FR_LIAISON_N", "FR_LIAISON_R", "FR_LIAISON_P",
              "FR_ENCHAÎNEMENT"},
    "fr-BE": {"FR_NUMERAL_MUTE_BEFORE_CONSONANT", "FR_DIX_Z_BEFORE_HUIT_NEUF"},
    "fr-FR-x-midi": {"FR_NEUF_V_BEFORE_HEURES", "FR_NUMERAL_MUTE_BEFORE_CONSONANT",
                     "FR_HUIT_MUTE_BEFORE_CONSONANT",
                     "FR_NUMERAL_Z_BEFORE_VOWEL", "FR_LIAISON_N_ARTICLE",
                     "FR_LIAISON_N_PRONOUN", "FR_ENT_MUTE_AFTER_ILS",
                     "FR_IENT_MUTE_AFTER_ILS"},
}
#: The sandhi rules a variant adds to those of fr-FR.
OWN_SANDHI = {
    "fr-BE": {"FR_BE_HUIT_MUTE_BEFORE_CONSONANT", "FR_BE_QUATRE_VINGT_MUTE_T"},
    "fr-CH": {"FR_CH_QUATRE_VINGT_MUTE_T"},
    "fr-FR-x-midi": {"FR_MIDI_APPENDIX_LABIAL_ACROSS_WORDS", "FR_MIDI_APPENDIX_LABIODENTAL_ACROSS_WORDS",
                     "FR_MIDI_APPENDIX_CORONAL_ACROSS_WORDS", "FR_MIDI_SCHWA_ELISION",
                     "FR_MIDI_ENT_SCHWA_AFTER_ILS"},
}


def _sandhi_key(rule):
    get = rule.get if isinstance(rule, dict) else (
        lambda k: getattr(rule, k))
    return (get("id"), get("left_context"), get("right_context"),
            get("transform"))


@pytest.mark.parametrize("tag", ["fr-CA", "fr-BE", "fr-CH", "fr-CI",
                                 "fr-FR-x-midi"])
def test_a_variant_inherits_fr_fr(tag):
    spec, base = o2i.get(tag), o2i.get("fr-FR")
    assert spec.code == tag
    assert spec.inherits == "fr-FR"
    assert spec.word_internal_apostrophe is True
    assert spec.word_exceptions == {**base.word_exceptions,
                                    **OWN_EXCEPTIONS.get(tag, {})}
    # The variant's own sandhi rules, as its file states them.
    own = json.loads((Path(o2i.__file__).parent / "data" / f"{tag}.json")
                     .read_text(encoding="utf-8")).get("sandhi_rules", [])
    own_ids = [r["id"] for r in own]
    assert set(own_ids) == (SANDHI_RESTATED.get(tag, set())
                            | OWN_SANDHI.get(tag, set()))
    # The resolved list is the id-keyed overlay: a restated rule takes its
    # parent's slot, and a rule the parent lacks follows in file order.
    by_id = {r["id"]: r for r in own}
    base_ids = {r.id for r in base.sandhi_rules}
    expected = [_sandhi_key(by_id.get(r.id, r)) for r in base.sandhi_rules]
    expected += [_sandhi_key(r) for r in own if r["id"] not in base_ids]
    assert [_sandhi_key(r) for r in spec.sandhi_rules] == expected


def test_quebec_neuf_heures_reads_the_laurentian_heures():
    neuf = [r for r in o2i.get("fr-CA").sandhi_rules
            if r.id == "FR_NEUF_V_BEFORE_HEURES"]
    assert len(neuf) == 1 and "ay̯ʁ" in neuf[0].right_context


@pytest.mark.parametrize("tag, words", [
    # words that carry none of the variant's cited features read like fr-FR
    ("fr-BE", ["maison", "chat", "école", "parler", "brun", "d'accord"]),
    ("fr-CH", ["maison", "chat", "école", "parler", "brun", "d'accord"]),
    ("fr-CI", ["maison", "chat", "école", "parler", "brun", "d'accord"]),
    ("fr-CA", ["maison", "ami", "école", "parler", "brun", "d'accord"]),
])
def test_a_variant_reads_like_fr_fr_where_no_feature_applies(tag, words):
    for word in words:
        assert _say(word, tag) == _say(word, "fr-FR"), word


#: Each regional difference in the assistant sentences, as a substitution on
#: the fr-FR reading: fr-BE [w] for the [ɥ] of ⟨ui⟩ (bruine, puis, huit,
#: aujourd'hui) and the long vowel of allumée before its final mute ⟨e⟩;
#: fr-CH that long vowel; fr-CI nothing. The rest of the sentence must read
#: as fr-FR reads it.
SENTENCE_SUBSTITUTIONS = {
    "fr-BE": [("ɥi", "wi"), ("alyme ", "alymeː ")],
    "fr-CH": [("alyme ", "alymeː ")],
    "fr-CI": [],
}


@pytest.mark.parametrize("tag", sorted(SENTENCE_SUBSTITUTIONS))
def test_the_assistant_sentences_differ_from_fr_fr_only_at_a_cited_feature(
        tag):
    for text in TEXTS:
        expected = _say(text, "fr-FR")
        for plain, regional in SENTENCE_SUBSTITUTIONS[tag]:
            expected = expected.replace(plain, regional)
        assert _say(text, tag) == expected, text


def _undo_laurentian(ipa):
    # Each cited surface back to the fr-FR phoneme it comes from. [ɑu̯] comes
    # from /ɔ/, /a/ or /ɑ/, so those three fold into one symbol on both sides.
    undo = [("ɛ̃i̯", "ɛ̃"), ("ãy̯", "œ̃"), ("ɔ̃u̯", "ɔ̃"), ("ɑ̃u̯", "ɑ̃"),
            ("ai̯", "ɛ"), ("ɛi̯", "e"), ("œy̯", "ø"), ("ay̯", "œ"),
            ("ɔu̯", "o"), ("ɑu̯", "A"), ("ẽ", "ɛ̃"), ("ã", "ɑ̃"), ("ɒ", "a"),
            ("iː", "i"), ("yː", "y"), ("uː", "u"), ("ɪ", "i"), ("ʏ", "y"),
            ("ʊ", "u"), ("t͡s", "t"), ("d͡z", "d")]
    for cited, plain in undo:
        ipa = ipa.replace(cited, plain)
    return ipa.replace("ɑ̃", "Ñ").replace("ɔ̃", "Ō").translate(
        str.maketrans("ɔaɑ", "AAA"))


def test_a_laurentian_difference_is_always_a_cited_allophone():
    # Undo the cited changes: what is left must be fr-FR, word for word.
    for text in TEXTS:
        ours = _undo_laurentian(_say(text, "fr-CA"))
        assert ours == _undo_laurentian(_say(text, "fr-FR")), text


#: The proclitics whose [a] stays front (Dumas 1974: 41, n. 13), by their
#: fr-FR reading. [a] itself is left out: it is both the proclitic à and the
#: verb a, whose word-final /a/ is [ɒ] (il y a [il i ɒ]).
PROCLITIC_A = {"la", "ma", "ta", "sa"}


def test_a_laurentian_back_a_never_reaches_a_proclitic():
    # The normalised comparison above folds [ɒ] into [a]; check the [a]
    # words one by one. Both readings split into the same words.
    for text in TEXTS:
        ours, base = _say(text, "fr-CA").split(), _say(text, "fr-FR").split()
        assert len(ours) == len(base), text
        for mine, plain in zip(ours, base):
            if plain in PROCLITIC_A:
                assert mine == plain, (text, plain, mine)
            if "ɒ" in mine:
                assert plain.endswith(("a", "wa")) and plain not in \
                    PROCLITIC_A, (text, plain, mine)
