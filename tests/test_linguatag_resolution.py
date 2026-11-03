"""Code resolution measures language tags with linguatag.

Registry resolution must not need ovos-spec-tools. A bare primary-language tag
resolves to the spec of its default region, and these are the reference
varieties the registry has always named for them.
"""
import subprocess
import sys

import pytest
from linguatag import lang_distance

from orthography2ipa import get, resolve
from orthography2ipa.registry import UnknownVariantWarning, resolves_exactly

REFERENCE_VARIETIES = {
    "de": "de-DE",
    "en": "en-GB",
    "es": "es-ES",
    "fr": "fr-FR",
    "gl": "gl-ES",
    "it": "it-IT",
    "pt": "pt-PT",
    "ro": "ro-RO",
}


def test_resolution_runs_without_ovos_spec_tools():
    # A None entry in sys.modules makes any import of the package fail.
    probe = (
        "import sys\n"
        "sys.modules['ovos_spec_tools'] = None\n"
        "sys.modules['ovos_spec_tools.language'] = None\n"
        "from orthography2ipa import resolve\n"
        f"for bare in {sorted(REFERENCE_VARIETIES)!r}:\n"
        "    print(bare, resolve(bare))\n"
        "print('en-NZ', resolve('en-NZ'))\n"
        "print(sorted(name for name, module in sys.modules.items()\n"
        "             if name.startswith('ovos_spec_tools') and module))\n"
    )
    result = subprocess.run([sys.executable, "-c", probe],
                            capture_output=True, text=True, timeout=300)
    assert result.returncode == 0, result.stderr
    lines = result.stdout.splitlines()
    expected = [f"{bare} {REFERENCE_VARIETIES[bare]}"
                for bare in sorted(REFERENCE_VARIETIES)]
    assert lines == expected + ["en-NZ en-GB", "[]"]


@pytest.mark.parametrize("bare,variety", sorted(REFERENCE_VARIETIES.items()))
def test_bare_tag_resolves_to_reference_variety(bare, variety):
    assert resolve(bare) == variety
    assert resolves_exactly(bare)
    assert get(bare, strict=True) is get(variety)


@pytest.mark.parametrize("tag,spec", [
    ("arb-x-zzz", "ar"),
    ("cbk-zam-x-zzz", "cbk-zam"),
    ("ext-PT-x-zzz", "ext-PT-x-barrancos"),
])
def test_unknown_variant_falls_back_to_the_standard_variety(tag, spec):
    with pytest.warns(UnknownVariantWarning):
        assert resolve(tag) == spec


def test_unknown_variant_between_tied_sibling_lects_takes_the_first():
    tied = ["ast-PT-x-guadramil", "ast-PT-x-medieval", "ast-PT-x-rionor"]
    assert all(lang_distance("ast-PT-x-zzz", lect) == 0 for lect in tied)
    with pytest.warns(UnknownVariantWarning):
        assert resolve("ast-PT-x-zzz") == tied[0]


@pytest.mark.parametrize("tag", ["yue-HK", "yue-MO", "yue-Hant"])
def test_traditional_cantonese_tags_resolve_to_the_cantonese_spec(tag):
    assert resolve(tag) == "yue"
    assert resolves_exactly(tag)
