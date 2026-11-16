"""Every registered spec code resolves exactly to its own spec.

``langcodes.standardize_tag(code, macro=True)`` replaces an individual
language with its macrolanguage. Before the exact match, that rewrite sent
these codes away from their own spec: ``tl`` to ``fil``, ``bcl`` to ``bik``,
and ``ojg`` through ``oj`` to the ``oji`` spec.
"""
import warnings

import pytest

from orthography2ipa.json_loader import available_json_codes
from orthography2ipa.registry import resolve, resolves_exactly

MACRO_FOLDED = ["bcl", "bxk", "cld", "cnr", "dhd", "emk", "gbo", "gno", "gya",
                "hdn", "hea", "lbk", "ojg", "spy", "swc", "tl", "ttq", "umu",
                "xsl", "zai"]


@pytest.mark.parametrize("code", MACRO_FOLDED)
def test_macro_folded_code_names_its_own_spec(code):
    assert code in available_json_codes()
    assert resolve(code) == code
    assert resolves_exactly(code)


def test_every_registered_code_resolves_to_itself():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        misses = sorted(code for code in available_json_codes()
                        if resolve(code) != code or not resolves_exactly(code))
    assert misses == []
