"""Code resolution measures language tags with linguatag.

Registry resolution must not need ovos-spec-tools. A bare primary-language tag
resolves to the spec of its default region, and these are the reference
varieties the registry has always named for them.
"""
import subprocess
import sys

import pytest
from linguatag import lang_distance, likely_script

from orthography2ipa import available_codes, get, resolve
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
    ("ar-x-zzz", "ar"),
    ("cbk-zam-x-zzz", "cbk-PH"),
    ("ext-PT-x-zzz", "ext-PT-x-barranco"),
])
def test_unknown_variant_falls_back_to_the_standard_variety(tag, spec):
    with pytest.warns(UnknownVariantWarning):
        assert resolve(tag) == spec


def test_unknown_variant_between_tied_sibling_lects_takes_the_first():
    tied = ["ast-PT-x-guadrami", "ast-PT-x-medieval", "ast-PT-x-rionor"]
    assert all(lang_distance("ast-PT-x-zzz", lect) == 0 for lect in tied)
    with pytest.warns(UnknownVariantWarning):
        assert resolve("ast-PT-x-zzz") == tied[0]


@pytest.mark.parametrize("tag", ["yue-HK", "yue-MO", "yue-Hant"])
def test_traditional_cantonese_tags_resolve_to_the_cantonese_spec(tag):
    assert resolve(tag) == "yue"
    assert resolves_exactly(tag)


@pytest.mark.parametrize("tag,spec", [("apc-Arab-SY", "apc-SY"), ("afb-Arab-KW", "afb-KW")])
def test_the_likely_script_does_not_tie_a_region_with_the_bare_language(tag, spec):
    """CLDR maximizes bare ``apc`` to ``apc-Arab-SY`` and bare ``afb`` to
    ``afb-Arab-KW``, so the script-tagged form is as near the bare spec as
    the regional one."""
    assert resolve(tag) == spec
    assert resolves_exactly(tag)


def test_every_regional_spec_is_named_with_its_likely_script():
    regional = [code for code in available_codes()
                if len(code.split("-")) == 2 and len(code.split("-")[1]) == 2]
    tags = {}
    for code in regional:
        language, region = code.split("-")
        if script := likely_script(code):
            tags[f"{language}-{script}-{region}"] = code
    assert len(tags) > 50
    assert {tag: resolve(tag) for tag in tags} == tags



@pytest.mark.parametrize("tag,spec", [
    ("kas-Arab", "kas"), ("pnb-Arab", "pnb-PK"), ("fat-Latn", "fat"), ("mhr-Cyrl", "mhr"),
])
def test_a_likely_script_keeps_the_language_the_tag_gives(tag, spec):
    """Standardization folds these codes into their macrolanguage (``kas`` to
    ``ks``), whose spec exists. The script step must not reach that spec."""
    assert resolve(tag) == spec
