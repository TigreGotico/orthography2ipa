"""The language-model functions left in ``feats`` warn, name the release that
removes them, and still return what ``lm`` returns.

The removal version comes from ``version.py``, read as text, so the expected
message does not depend on the code that writes the warning.
"""
import re
import warnings
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import feats, lm

VERSION = Path(orthography2ipa.__file__).parent / "version.py"
WORDS = ["mar", "sol", "casa"]


def removal_version() -> str:
    major = re.search(r"^VERSION_MAJOR = (\d+)$", VERSION.read_text(encoding="utf-8"), re.M)
    return f"{int(major.group(1)) + 1}.0.0"


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
        f"{removal_version()}; use orthography2ipa.lm.{name}."]
    assert deprecations[0].filename == __file__


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
