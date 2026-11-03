"""Northern Najdi extends the voiceless affrication to central vowels; the voiced one stays put.

Each case is one of Alshammari's (2026) examples, and the pair against the parent is the
point: a spec that changed nothing would pass a test that only looked at Shamali.
"""
import pytest

from orthography2ipa import get, transcribe

PARENT = "ar-SA-x-najd"
SHAMALI = "ar-SA-x-shamali"


@pytest.mark.parametrize("word,parent_ipa,shamali_ipa,why", [
    ("كَلْب", "ˈkalb", "ˈtsalb",
     "ex. (1d) /kalb/ → [tsalb] 'dog': central /a/ triggers here and not in the parent"),
    ("قَلْب", "ˈɡalb", "ˈɡalb",
     "the voiced rule is untouched, so 'heart' does not become *[dzalb] — the collision "
     "an earlier ruling assumed would happen"),
    ("كِتَاب", "tsiˈtaːb", "tsiˈtaːb",
     "the inherited front-vowel rule is unchanged, so both affricate"),
    ("كُوخ", "ˈkuːx", "ˈkuːx",
     "ex. (5) [kuːχ] 'cottage': back vowels block in both"),
    ("كَاتِب", "ˈkaːtib", "ˈtsaːtib",
     "ex. (1f-g): word-initial /k/ before central /aː/ is attested"),
])
def test_the_delta_is_exactly_the_central_vowel_trigger(word, parent_ipa, shamali_ipa, why):
    assert transcribe(word, PARENT) == parent_ipa, why
    assert transcribe(word, SHAMALI) == shamali_ipa, why


def test_the_spec_carries_only_the_delta():
    """Everything else is inherited, so the file stays a delta and not a copy."""
    import json
    import os

    import orthography2ipa as o2i
    path = os.path.join(os.path.dirname(o2i.__file__), "data", "ar-SA-x-shamali.json")
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    assert raw["graphemes"] == {} and raw["allophones"] == {}
    assert raw["graphemes_base"] == PARENT and raw["parent"] == PARENT
    assert [r["id"] for r in raw["allophone_rules"]] == [
        "SHAMALI_AFFRIC_K_BEFORE_CENTRAL_A",
        "SHAMALI_AFFRIC_K_BEFORE_CENTRAL_AA",
        "SHAMALI_AFFRIC_K_AFTER_CENTRAL_A"]
    # the notes are prose, not an escaped one-liner
    assert "\\n" not in raw["notes"]
    # the inherited table really does arrive
    assert len(get(SHAMALI).graphemes) > 200


def test_the_voiced_rule_is_not_widened():
    """The asymmetry Alshammari states at p.1337, asserted rather than annotated."""
    rules = {r.id: r for r in get(SHAMALI).allophone_rules}
    g_before = rules["NAJD_AFFRIC_G_BEFORE"]
    assert set(g_before.followed_by_phoneme) == {"i", "iː"}


def test_the_unattested_cells_are_left_alone():
    """The author names two cells he could not find; neither is claimed.

    Central /a/ word-medially and /aː/ word-finally are both hedged at p.1336, and his
    summary at p.1337 reads "in certain cases". Taking the wider reading anyway would be
    a claim the source does not make, so the rules carry word_initial and word_final and
    the /aː/-after case is absent. Asserted on the shipped rules rather than trusted to
    the note, because a comment cannot go red.
    """
    import json
    import os

    import orthography2ipa as o2i
    path = os.path.join(os.path.dirname(o2i.__file__), "data", "ar-SA-x-shamali.json")
    with open(path, encoding="utf-8") as fh:
        rules = {r["id"]: r for r in json.load(fh)["allophone_rules"]}

    assert rules["SHAMALI_AFFRIC_K_BEFORE_CENTRAL_A"].get("word_initial") is True
    assert rules["SHAMALI_AFFRIC_K_AFTER_CENTRAL_A"].get("word_final") is True
    assert not any("aː" in (r.get("preceded_by_phoneme") or []) for r in rules.values()), (
        "word-final /k/ next to /aː/ is the cell the author could not attest")


def test_the_disclaimed_cells_stay_silent_whatever_the_rules_say():
    """A claim about the spec's OUTPUT, so a later rule cannot reopen a withdrawn cell.

    The position flags are asserted above, but a rule added without one would satisfy
    that check and still affricate these words. This asserts the two cells the source
    could not attest, over the whole rule set at once and without reading the schema.
    """
    assert "ts" not in transcribe("سَكَن", SHAMALI), "word-medial /k/ + /a/ is not attested"
    assert "ts" not in transcribe("شَبَاك", SHAMALI), "word-final /k/ after /aː/ is not attested"
    # and the attested ones must still fire, or the gate above passes by emitting nothing
    assert "ts" in transcribe("كَلْب", SHAMALI)
    assert "ts" in transcribe("مَكَان", SHAMALI), "ex. (2) /mi.kaːn/ -> [mi.tsaːn]"
