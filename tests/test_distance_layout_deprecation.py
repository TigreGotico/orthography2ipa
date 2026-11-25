"""``feature_vector`` and ``feature_names`` warn that their layout changes.

They return the 23-feature layout of the vendored ``feats`` table. The API
stability page fixes the release that changes the layout at deprecation time:
it is ``VERSION_MAJOR + 1``. The distance functions read the table through a
private name, so they stay silent and keep their values.
"""
import itertools
import warnings

import pytest

import orthography2ipa
from orthography2ipa import distance, feats
from orthography2ipa.inventory import phoneme_inventory
from orthography2ipa.version import VERSION_MAJOR

CODES = [
    "pt-PT", "pt-BR", "en-US", "en-GB", "fr-FR", "de-DE", "es-ES", "it-IT",
    "ru-RU", "uk-UA", "ar-SA", "he-IL", "hi-IN", "bn-BD", "ta-IN", "te-IN",
    "th-TH", "ja-JP", "ko-KR", "cmn-CN", "el-GR", "ka-GE", "hy-AM", "fa-IR",
    "tr-TR", "fi-FI", "hu-HU", "pl-PL", "cs-CZ", "sw-KE", "am-ET", "vi-VN",
]
RELEASE = f"{VERSION_MAJOR + 1}.0.0"


@pytest.fixture(scope="module")
def specs():
    return {code: orthography2ipa.get(code) for code in CODES}


@pytest.mark.parametrize("name, call", [
    ("feature_vector", lambda: distance.feature_vector("p")),
    ("feature_names", lambda: distance.feature_names()),
])
def test_each_call_warns_with_the_release_and_the_replacement(name, call):
    for _ in range(2):
        with pytest.warns(DeprecationWarning) as caught:
            call()
        assert [str(w.message) for w in caught] == [
            f"orthography2ipa.distance.{name} returns the 23-feature layout "
            f"of a vendored table. From {RELEASE} it returns the feature "
            "layout of phonematcher. phonematcher.vectorize_phones and "
            "phonematcher.FEATURES give that layout now."]
        assert caught[0].filename == __file__


def test_feature_vector_returns_the_vendored_table_for_every_phone(specs):
    phones = sorted(set().union(*(phoneme_inventory(s) for s in specs.values())))
    readable = 0
    for phone in phones:
        with pytest.warns(DeprecationWarning):
            got = distance.feature_vector(phone)
        assert len(got) == feats.NUM_FEATURES == 23
        try:
            table = feats.vectorize_phones(phone)
        except (ValueError, KeyError):
            continue
        readable += 1
        assert got == tuple(
            1.0 if v is True else 0.0 if v is False else 0.5 for v in table), phone
    assert len(specs) >= 30 and readable > 100


def test_feature_names_keep_the_23_names():
    with pytest.warns(DeprecationWarning):
        names = distance.feature_names()
    assert len(names) == 23
    assert names[:3] == ("syllabic", "sonorant", "consonantal")


def test_distance_functions_stay_silent_and_keep_the_table_values(specs):
    phones = sorted(set().union(*(phoneme_inventory(s) for s in specs.values())))
    readable = [p for p in phones if _reads(p)]
    pairs = list(itertools.islice(itertools.combinations(readable, 2), 0, None, 50))
    assert len(pairs) > 100
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        for a, b in pairs:
            assert distance.segment_distance(a, b) == min(feats.phonetic_distance(a, b), 1.0)
        distance.segment_distance("p", "§")
        distance.segment_distance("p", "b", strict=True)
        for code_a, code_b in itertools.combinations(CODES[:8], 2):
            a, b = specs[code_a], specs[code_b]
            distance.inventory_distance(a, b)
            distance.phonological_distance(a, b)
            distance.full_distance(a, b)
        distance.pairwise_distances([specs[c] for c in CODES[:5]])


def _reads(phone):
    try:
        feats.vectorize_phones(phone)
        return True
    except (ValueError, KeyError):
        return False
