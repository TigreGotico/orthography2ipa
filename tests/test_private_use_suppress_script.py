"""A Suppress-Script subtag in a private-use tag still names the lect.

RFC 5646 §3.1.9: a script subtag registered as a language's Suppress-Script
"adds no distinguishing information to a language tag". §4.1 item 2: "The
script subtag SHOULD NOT be used to form language tags unless the script adds
some distinguishing information to the tag." So ``pt-Latn-BR-x-sp`` and
``pt-BR-x-sp`` name the same lect.

The Suppress-Script values below are copied from the IANA Language Subtag
Registry (File-Date 2026-09-17), not read from the library under test.
"""
import warnings

import pytest

from orthography2ipa import UnknownVariantWarning, resolve, resolves_exactly
from orthography2ipa.registry import _ALIASES, available_json_codes

IANA_SUPPRESS_SCRIPT = {
    "pt": "Latn", "es": "Latn", "ca": "Latn", "gl": "Latn", "it": "Latn",
    "nl": "Latn", "de": "Latn", "en": "Latn", "ar": "Arab",
}


def _has_script(code: str) -> bool:
    second = code.split("-")[1]
    return len(second) == 4 and second.isalpha()


#: Registered private-use codes of those languages with no script subtag of
#: their own (``ar-Latn-x-buckwalt`` already names a script).
PRIVATE_USE_CODES = sorted(
    c for c in available_json_codes()
    if "-x-" in c and c.split("-")[0] in IANA_SUPPRESS_SCRIPT
    and not _has_script(c))

#: Alias keys of the same kind. Some have a private-use subtag longer
#: than 8 characters (``ar-x-levantine``), which langcodes rejects, so the
#: private-use part must never reach it.
PRIVATE_USE_ALIASES = sorted(
    k for k in _ALIASES
    if "-x-" in k and k.split("-")[0] in IANA_SUPPRESS_SCRIPT
    and not _has_script(k))


def _with_script(code: str, script: str) -> str:
    lang, rest = code.split("-", 1)
    return f"{lang}-{script}-{rest}"


def _resolve_quietly(tag: str):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        got = resolve(tag)
    return got, [w for w in caught if issubclass(w.category, UnknownVariantWarning)]


@pytest.mark.parametrize("tag,code", [
    ("pt-Latn-BR-x-sp", "pt-BR-x-sp"),
    ("pt-Latn-PT-x-lisbon", "pt-PT-x-lisbon"),
    ("pt-Latn-PT-x-porto", "pt-PT-x-porto"),
    ("PT-LATN-br-X-SP", "pt-BR-x-sp"),
])
def test_the_reported_tags_resolve_exactly(tag, code):
    got, unknown = _resolve_quietly(tag)
    assert got == code
    assert not unknown
    assert resolves_exactly(tag)


def test_the_parametrized_set_is_not_empty():
    assert len(PRIVATE_USE_CODES) > 50


@pytest.mark.parametrize("code", PRIVATE_USE_CODES)
def test_every_private_use_code_takes_its_suppress_script(code):
    tag = _with_script(code, IANA_SUPPRESS_SCRIPT[code.split("-")[0]])
    got, unknown = _resolve_quietly(tag)
    assert got == code
    assert not unknown
    assert resolves_exactly(tag)


@pytest.mark.parametrize("alias", PRIVATE_USE_ALIASES)
def test_every_private_use_alias_takes_its_suppress_script(alias):
    tag = _with_script(alias, IANA_SUPPRESS_SCRIPT[alias.split("-")[0]])
    got, unknown = _resolve_quietly(tag)
    assert got == resolve(alias)
    assert not unknown
    assert resolves_exactly(tag)


def test_the_aliases_include_long_private_use_subtags():
    assert any(len(s) > 8 for a in PRIVATE_USE_ALIASES for s in a.split("-"))


@pytest.mark.parametrize("tag", ["pt-Cyrl-BR-x-sp", "pt-Arab-PT-x-lisbon"])
def test_a_script_that_adds_information_is_not_dropped(tag):
    # Only the Suppress-Script carries no information; any other script names
    # a different writing system, and no spec is registered for it.
    assert not resolves_exactly(tag)


def test_an_unknown_variant_still_warns():
    got, unknown = _resolve_quietly("pt-Latn-BR-x-zz")
    assert got == "pt-BR"
    assert unknown
    assert not resolves_exactly("pt-Latn-BR-x-zz")
