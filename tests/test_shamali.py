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
        "SHAMALI_AFFRIC_K_BEFORE_CENTRAL", "SHAMALI_AFFRIC_K_AFTER_CENTRAL"]
    # the inherited table really does arrive
    assert len(get(SHAMALI).graphemes) > 200


def test_the_voiced_rule_is_not_widened():
    """The asymmetry Alshammari states at p.1337, asserted rather than annotated."""
    rules = {r.id: r for r in get(SHAMALI).allophone_rules}
    g_before = rules["NAJD_AFFRIC_G_BEFORE"]
    assert set(g_before.followed_by_phoneme) == {"i", "iː"}
