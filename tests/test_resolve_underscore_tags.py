"""An underscore tag names the same spec as its hyphen spelling.

BCP 47 tags are written with hyphens; POSIX locale names and directory names
write the same tag with underscores. The expected specs are the registered
keys and the alias targets that the hyphen spellings name.
"""
import pytest

from orthography2ipa import resolve, resolves_exactly


@pytest.mark.parametrize("tag, spec", [
    ("cnr_Cyrl", "cnr"),
    ("cnr_Cyrl_BA", "cnr"),
    ("cnr_Cyrl_ME", "cnr"),
    ("cnr_Cyrl_RS", "cnr"),
    ("pnb_PK", "pnb-PK"),
])
def test_an_underscore_tag_names_the_spec_of_its_hyphen_spelling(tag, spec):
    assert resolve(tag) == spec
    assert resolve(tag.replace("_", "-")) == spec


@pytest.mark.parametrize("tag, spec", [
    ("sr_Latn_RS", "sr"),
    ("fr_CA", "fr-CA"),
    ("fr_SN", "fr-FR"),
    ("ar_ZZ", "ar"),
    ("bs_Cyrl_BA", "bs"),
])
def test_an_underscore_tag_reaches_every_later_step(tag, spec):
    assert resolve(tag) == spec


@pytest.mark.parametrize("tag", ["pt--PT", "pt-", "-pt", "x", "123", "pt-é"])
def test_a_tag_that_is_not_well_formed_never_raises(tag):
    resolve(tag)
    assert not resolves_exactly(tag)
