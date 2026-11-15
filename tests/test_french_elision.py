"""French elision: an elided clitic is spoken with its host word, never dropped.

French writes the elided clitic with an apostrophe and no space (⟨l'ami⟩,
⟨j'ai⟩, ⟨qu'il⟩). The clitic is the onset of the vowel-initial host:
⟨l'ami⟩ is [lami] (Tranel 1995: 1, example (1b)). The spec declares
``word_internal_apostrophe`` so that clitic and host are one unit. Before
that, the clitic was a word of its own, the silent-final-letter rules removed
its consonant (⟨d'⟩, ⟨j'⟩, ⟨s'⟩ came out empty) and ⟨qu⟩ before the
apostrophe lost its mute ⟨u⟩.

The expected IPA below is written in the test, never read back from the
engine. The cases where only the clitic is pinned (``n'est``, ``c'est``) leave
the reading of the host ⟨est⟩ out: this spec does not make that claim.
"""
import json
import warnings
from pathlib import Path

import pytest

import orthography2ipa as o2i
from orthography2ipa import G2P, Pipeline
from orthography2ipa.exceptions import UnmappedGraphemeWarning

#: The fr-FR whole-word entries, read from the spec file and not through the
#: engine.
FR_EXCEPTIONS = json.loads(
    (Path(o2i.__file__).parent / "data" / "fr-FR.json").read_text(
        encoding="utf-8"))["word_exceptions"]
#: Letters that open a vowel-initial or mute-h word in French spelling.
VOWEL_OR_H = set("aàâeéèêëiîïoôuùûüyh")
#: Every fr-FR entry that can follow an elided clitic.
VOWEL_INITIAL_EXCEPTIONS = {word: ipa for word, ipa in FR_EXCEPTIONS.items()
                            if word[0] in VOWEL_OR_H and "'" not in word}
#: Verb forms that cannot follow l' or d'. The verb est has no entry, and
#: after those clitics est is the noun 'east' (see test_l_est_is_the_noun).
VERB_FORMS = {"et", "es"}
#: The reading of each elided clitic: its consonant, with the vowel elided.
CLITICS = {"l'": "l", "d'": "d"}

#: Every French tag. The tags with a spec of their own (``fr-CA``, ``fr-BE``,
#: ``fr-CH``, ``fr-CI``) inherit the elision handling; the rest read ``fr-FR``.
FRENCH_TAGS = ["fr", "fr-FR", "fr-CA", "fr-BE", "fr-CH", "fr-CI", "fr-LU",
               "fr-MC", "fr-SN", "fr-CD", "fr-CM", "fr-MA", "fr-HT"]

#: What a cited regional rule changes in an elision case. Laurentian French
#: laxes a final high vowel before a closing consonant and affricates /d/
#: before /ɥ/ (tests/test_french_variants.py cites both). Every other tag
#: and every other case reads like fr-FR.
REGIONAL = {
    "fr-CA": {
        "qu'il": "kɪl", "qu’il": "kɪl", "s'il": "sɪl",
        "lorsqu'il": "lɔʁskɪl", "presqu'île": "pʁɛskɪl",
        "j'habite": "ʒabɪt",
        # A silent ⟨h⟩ stands between /d/ and /ɥ/, and no source says whether
        # it blocks the affrication, so aujourd'hui reads like fr-FR.
    },
}

ELISIONS = [
    ("d'accord", "dakɔʁ"),
    ("D'accord", "dakɔʁ"),
    ("j'ai", "ʒe"),
    ("j'aime", "ʒɛm"),
    ("j'habite", "ʒabit"),
    ("qu'il", "kil"),
    ("l'eau", "lo"),
    ("l'homme", "lɔm"),
    ("n'ai", "ne"),
    ("s'il", "sil"),
    ("jusqu'à", "ʒyska"),
    ("lorsqu'il", "lɔʁskil"),
    ("puisqu'on", "pɥiskɔ̃"),
    ("aujourd'hui", "oʒuʁdɥi"),
    ("quelqu'un", "kɛlkœ̃"),
    ("presqu'île", "pʁɛskil"),
    ("d’accord", "dakɔʁ"),          # U+2019, the typographic apostrophe
    ("qu’il", "kil"),
    ("aujourd’hui", "oʒuʁdɥi"),
]


@pytest.mark.parametrize("tag", FRENCH_TAGS)
@pytest.mark.parametrize("text, expected", ELISIONS)
def test_an_elided_clitic_is_spoken_with_its_host(tag, text, expected):
    expected = REGIONAL.get(tag, {}).get(text, expected)
    assert o2i.transcribe(text, tag) == expected


@pytest.mark.parametrize("tag", FRENCH_TAGS)
@pytest.mark.parametrize("text, clitic", [("n'est", "n"), ("c'est", "s")])
def test_the_clitic_of_n_est_and_c_est_is_kept(tag, text, clitic):
    spoken = o2i.transcribe(text, tag)
    assert " " not in spoken
    assert spoken.startswith(clitic)
    assert len(spoken) > len(clitic)


@pytest.mark.parametrize("tag", FRENCH_TAGS)
def test_the_reported_sentence_keeps_every_clitic(tag):
    spoken = o2i.transcribe(
        "D'accord, j'ai éteint les lumières du salon. Autre chose ?", tag)
    if tag == "fr-CA":
        # dy -> d͡zy: /d/ before /y/ is affricated (Dow 2019: 1)
        assert spoken == "dakɔʁ ʒe etɛ̃ le lymjɛʁ d͡zy salɔ̃ otʁ ʃoz"
    else:
        assert spoken == "dakɔʁ ʒe etɛ̃ le lymjɛʁ dy salɔ̃ otʁ ʃoz"


@pytest.mark.parametrize("tag", FRENCH_TAGS)
def test_every_french_tag_reads_the_apostrophe_as_part_of_the_word(tag):
    assert o2i.get(tag).word_internal_apostrophe is True


@pytest.mark.parametrize("tag", ["fr-LU", "fr-MC", "fr-SN", "fr-CD", "fr-CM",
                                 "fr-MA", "fr-HT", "fr-DZ", "fr-TN", "fr-GP",
                                 "fr-MQ", "fr-RE", "fr-NC", "fr-PF"])
def test_a_french_region_with_no_sourced_difference_is_the_standard_variety(tag):
    # No source states a difference, so none of these may land on a regional
    # spec (the nearest match picked fr-BE for every one of them).
    assert o2i.resolve(tag) == "fr-FR"


def test_les_keeps_its_vowel():
    assert o2i.transcribe("les", "fr-FR") == "le"
    assert o2i.transcribe("Les", "fr-FR") == "le"
    assert o2i.transcribe("les amis", "fr-FR").split(" ")[0] == "le"


@pytest.mark.parametrize("text", ["est-ce", "peut-être", "rendez-vous",
                                  "dix-sept"])
def test_a_hyphenated_compound_stays_two_words_and_loses_neither(text):
    # A hyphen is a word boundary here (liaison is not modelled): both parts
    # are spoken, and each reads as it does alone.
    parts = text.split("-")
    assert o2i.transcribe(text, "fr-FR").split(" ") == [
        o2i.transcribe(p, "fr-FR") for p in parts]


def test_a_final_voiced_consonant_survives_the_link_mark():
    # FR_ENCHAÎNEMENT used to replace the consonant with the link mark.
    assert o2i.transcribe("rouge orange", "fr-FR") == "ʁuʒ‿ ɔʁɑ̃ʒ"
    assert o2i.transcribe("grande amie", "fr-FR") == "ɡʁɑ̃d‿ ami"


def test_digits_do_not_crash_and_the_words_around_them_stay():
    # Numbers are out of scope: a digit is dropped with a warning, not
    # silently, and the words beside it are still spoken.
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        spoken = o2i.transcribe("il y a 3 minutes", "fr-FR")
    assert spoken == "il i a minyt"
    assert any(issubclass(w.category, UnmappedGraphemeWarning) for w in record)


@pytest.mark.parametrize("text", ["'", "''", "d'", "'d", "l'l", "l' a"])
def test_a_stray_apostrophe_does_not_crash(text):
    assert isinstance(o2i.transcribe(text, "fr-FR"), str)


def test_every_vowel_initial_exception_is_tested():
    # 28 entries: 26 content words and the two verb forms.
    assert len(VOWEL_INITIAL_EXCEPTIONS) == 28
    assert VERB_FORMS <= set(VOWEL_INITIAL_EXCEPTIONS)


@pytest.mark.parametrize("clitic", sorted(CLITICS))
@pytest.mark.parametrize("host", sorted(set(VOWEL_INITIAL_EXCEPTIONS)
                                        - VERB_FORMS))
def test_an_elided_clitic_keeps_the_host_exception(clitic, host):
    # l'hiver is l + the entry for hiver, [livɛʁ]; the rules alone gave [live].
    expected = CLITICS[clitic] + VOWEL_INITIAL_EXCEPTIONS[host]
    assert o2i.transcribe(clitic + host, "fr-FR") == expected


@pytest.mark.parametrize("text, expected", [
    ("L'HIVER", "livɛʁ"),
    ("l’hiver", "livɛʁ"),           # U+2019
    ("d’hier", "djɛʁ"),
    ("l'hiver arrive", "livɛʁ‿ aʁiv"),
])
def test_case_and_typographic_apostrophe_keep_the_host_exception(
        text, expected):
    assert o2i.transcribe(text, "fr-FR") == expected


@pytest.mark.parametrize("text, expected", [
    # The ⟨h⟩ of hier is mute, so que elides before it: Larousse, s.v.
    # hier, "Le h étant muet", with the example "qu'hier". Elision itself is
    # Tranel (1995: 1). Lexique 3.83: hier jER, hiver ivER, puisque p8isk°,
    # lorsque lORsk°.
    ("qu'hier", "kjɛʁ"), ("qu'hiver", "kivɛʁ"), ("QU'HIER", "kjɛʁ"),
    ("qu’hier", "kjɛʁ"), ("puisqu'hier", "pɥiskjɛʁ"),
    ("lorsqu'hier", "lɔʁskjɛʁ"),
])
def test_qu_before_a_mute_h_keeps_the_host_exception(text, expected):
    assert o2i.transcribe(text, "fr-FR") == expected


@pytest.mark.parametrize("text, expected", [
    # Lexique 3.83: est, NOM, phon Est
    ("l'est", "lɛst"), ("d'est", "dɛst"), ("à l'est", "a lɛst"),
    ("l'avant-d'est", "lavɑ̃ dɛst"),
])
def test_l_est_is_the_noun(text, expected):
    assert o2i.transcribe(text, "fr-FR") == expected


@pytest.mark.parametrize("text, parts", [
    ("l'avant-d'est", ["l'avant", "d'est"]),
    ("vent-d'est", ["vent", "d'est"]),
    ("vent-d'est-ouest", ["vent", "d'est", "ouest"]),
])
def test_a_clitic_inside_a_hyphen_compound_joins_only_its_own_element(
        text, parts):
    # Each element reads as it does alone; d'est does not fuse with ouest.
    spoken = o2i.transcribe(text, "fr-FR").replace("‿", "").split()
    assert spoken == [o2i.transcribe(p, "fr-FR") for p in parts]


def test_an_elided_clitic_keeps_the_host_lexicon_entry():
    # oignon is [ɔɲɔ̃]; the rules read ⟨oi⟩ as [wa]. A registered lexicon
    # entry for the host holds after an elided clitic.
    engine = G2P("fr-FR", pipeline=Pipeline(lexicon={"oignon": "ɔɲɔ̃"}))
    assert engine.transcribe("oignon") == "ɔɲɔ̃"
    assert engine.transcribe("l'oignon") == "lɔɲɔ̃"
    assert engine.transcribe("d’oignon") == "dɔɲɔ̃"
    assert engine.transcribe("L'OIGNON") == "lɔɲɔ̃"
