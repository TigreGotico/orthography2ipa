"""The language-model functions left in ``feats`` warn, name the release that
removes them, and still return what ``lm`` returns.

The API stability page fixes the removal version at deprecation time: it is
``VERSION_MAJOR + 1`` of the release that deprecated the name. These names were
deprecated while ``version.py`` had ``VERSION_MAJOR = 7``, so they go in 8.0.0.
A major release that keeps them makes the warning name a later release, and
this test fails.
"""
import warnings

import pytest

import orthography2ipa
from orthography2ipa import feats, lm

DEPRECATED_AT_MAJOR = 7
REMOVAL_VERSION = f"{DEPRECATED_AT_MAJOR + 1}.0.0"
WORDS = ["mar", "sol", "casa"]


@pytest.fixture(scope="module")
def spec():
    return orthography2ipa.get("pt-PT")


CALLS = [
    ("phoneme_embeddings", lambda mod, spec: mod.phoneme_embeddings(spec)),
    ("build_ngram_lm", lambda mod, spec: mod.build_ngram_lm(WORDS, spec)),
    ("perplexity", lambda mod, spec: mod.perplexity(lm.build_ngram_lm(WORDS, spec), WORDS, spec)),
]


@pytest.mark.parametrize("name, call", CALLS, ids=[c[0] for c in CALLS])
def test_a_moved_function_warns_once_at_the_caller_with_its_removal_version(name, call, spec):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        call(feats, spec)
    deprecations = [w for w in caught if issubclass(w.category, DeprecationWarning)]
    assert [str(w.message) for w in deprecations] == [
        f"orthography2ipa.feats.{name} is deprecated and will be removed in "
        f"{REMOVAL_VERSION}; use orthography2ipa.lm.{name}."]
    assert (deprecations[0].filename, deprecations[0].lineno) == (
        __file__, call.__code__.co_firstlineno)


@pytest.mark.parametrize("name, call", CALLS, ids=[c[0] for c in CALLS])
def test_a_moved_function_returns_what_lm_returns(name, call, spec):
    with pytest.deprecated_call():
        old = call(feats, spec)
    new = call(lm, spec)
    if name == "phoneme_embeddings":
        assert old.keys() == new.keys()
        assert all((old[k] == new[k]).all() for k in new)
    else:
        assert old == new
