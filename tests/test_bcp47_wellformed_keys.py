"""Every spec key is a well-formed BCP 47 tag, and every old key still resolves.

RFC 5646 section 2.1 gives the grammar. A private-use subtag has 1 to 8
alphanumerics (``privateuse = "x" 1*("-" (1*8alphanum))``), and a subtag after
the script is a region (2 letters or 3 digits) or a variant (5 to 8
alphanumerics, or a digit and 3 alphanumerics). The old keys stay exact
aliases of the new ones.
"""
import json
import re
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import get, resolve, resolves_exactly
from orthography2ipa.json_loader import available_json_codes
from orthography2ipa.registry import _ALIASES

_A, _AN = "[A-Za-z]", "[A-Za-z0-9]"
_LANGTAG = (
    rf"(?:{_A}{{2,3}}(?:-{_A}{{3}}){{0,3}}|{_A}{{4}}|{_A}{{5,8}})"  # language
    rf"(?:-{_A}{{4}})?"                                              # script
    rf"(?:-(?:{_A}{{2}}|[0-9]{{3}}))?"                               # region
    rf"(?:-(?:{_AN}{{5,8}}|[0-9]{_AN}{{3}}))*"                       # variant
    rf"(?:-[0-9A-WYZa-wyz](?:-{_AN}{{2,8}})+)*"                      # extension
)
_PRIVATEUSE = rf"[xX](?:-{_AN}{{1,8}})+"
_WELL_FORMED = re.compile(rf"(?:{_LANGTAG}(?:-{_PRIVATEUSE})?|{_PRIVATEUSE})\Z")

#: old key -> new key.
RENAMED = {
    "an-x-benasques": "an-x-benasque",
    "an-x-chistabin": "an-x-chistau",
    "an-x-occidental": "an-x-occident",
    "ar-Latn-buckwalter": "ar-Latn-x-buckwalt",
    "ar-x-peninsular": "ar-x-peninsul",
    "ast-PT-x-guadramil": "ast-PT-x-guadrami",
    "ast-x-cantabrian": "ast-x-cantabri",
    "ast-x-occidental": "ast-x-occident",
    "ca-x-occidental": "ca-x-occident",
    "cdo-Latn-buc": "cdo-Latn-x-buc",
    "cel-x-gallaecia": "cel-x-gallaeci",
    "da-x-copenhagen": "da-x-copenhag",
    "de-x-alemannic": "de-x-alemanni",
    "es-AR-x-patagonia": "es-AR-x-patagoni",
    "es-CO-x-santander": "es-CO-x-santande",
    "es-ES-x-andalusia-e": "es-ES-x-andalusi-e",
    "es-ES-x-andalusia-w": "es-ES-x-andalusi-w",
    "es-ES-x-cantabria": "es-ES-x-cantabri",
    "es-ES-x-extremadura": "es-ES-x-extremad",
    "es-PE-x-amazonico": "es-PE-x-amazonia",
    "es-VE-x-maracucho": "es-VE-x-zulia",
    "eu-x-bizkaiera": "eu-biscayan",
    "eu-x-erronkariera": "eu-x-roncal",
    "eu-x-gipuzkera": "eu-x-gipuzkoa",
    "eu-x-lapurtera": "eu-x-lapurdi",
    "ext-PT-x-barrancos": "ext-PT-x-barranco",
    "fa-x-khorasani": "fa-x-khorasan",
    "gem-x-ingvaeonic": "gem-x-ingvaeon",
    "gem-x-northwest": "gem-x-north-west",
    "gl-ES-x-occidental": "gl-ES-x-occident",
    "gl-ES-x-reintegrado": "gl-ES-x-reintegr",
    "hak-Latn-phak-fa-su": "hak-Latn-x-phak-fa-su",
    "la-x-galloitalic": "la-x-gallo-italic",
    "nan-Latn-poj": "nan-Latn-pehoeji",
    "oc-x-provencau": "oc-provenc",
    "pt-BR-x-fluminense": "pt-BR-x-fluminen",
    "pt-PT-x-trasosmontes": "pt-PT-x-tras-os-montes",
    "roa-x-galaicopt": "roa-x-galaico-pt",
    "ru-x-arkhangelsk": "ru-x-arkhange",
    "sc-x-campidanese": "sc-x-campidan",
    "sc-x-logudorese": "sc-x-logudoro",
    "sv-x-rikssvenska": "sv-x-rikssven",
    "ta-x-proto-dravidian": "ta-x-proto-dravidia",
}

#: Well-formed keys that are not valid: SIL retired ``bbz`` (2020, reason N) and
#: IANA deprecated it with no preferred value.
DEPRECATED = {"bbz": "ar-TD-x-babalia"}

#: Older aliases of the renamed specs, which follow the spec to its new key.
CHAINED = {
    "gl-x-occidental": "gl-ES-x-occident",
    "gl-x-reintegrado": "gl-ES-x-reintegr",
    "pt-PT-x-barrancos": "ext-PT-x-barranco",
}

_DATA = Path(orthography2ipa.__file__).parent / "data"
_CODE_FIELDS = ("parent", "graphemes_base", "allophones_base",
                "positional_graphemes_base")


@pytest.mark.parametrize("tag,expected", [
    ("de-CH-x-phonebk", True), ("zh-cmn-Hans-CN", True), ("sl-rozaj-biske", True),
    ("es-419", True), ("x-whatever", True), ("de-CH-1901", True),
    ("de-419-DE", False), ("a-DE", False), ("en-x-toolongtag", False),
    ("ar-Latn-buckwalter", False), ("nan-Latn-poj", False),
])
def test_the_grammar_matches_rfc_5646_examples(tag, expected):
    assert bool(_WELL_FORMED.match(tag)) is expected


def test_every_registered_key_is_well_formed_bcp47():
    assert [c for c in sorted(available_json_codes())
            if not _WELL_FORMED.match(c)] == []


def test_every_code_a_spec_names_is_well_formed_bcp47():
    bad = []
    for path in sorted(_DATA.glob("*.json")):
        spec = json.loads(path.read_text(encoding="utf-8"))
        named = [spec.get(field) for field in _CODE_FIELDS]
        named += [a.get("code") for a in spec.get("ancestors") or []]
        bad += [(path.stem, c) for c in named
                if isinstance(c, str) and not _WELL_FORMED.match(c)]
    assert bad == []


@pytest.mark.parametrize("new", sorted({*RENAMED.values(), *DEPRECATED.values()}))
def test_new_key_is_a_spec_and_resolves_to_itself(new):
    assert new in available_json_codes()
    others = {k.lower() for k in available_json_codes() if k != new}
    others |= {k.lower() for k, target in _ALIASES.items() if target != new}
    assert new.lower() not in others
    assert resolve(new) == new
    assert resolves_exactly(new)
    assert get(new).code == new


@pytest.mark.parametrize("old,new", sorted({**RENAMED, **CHAINED, **DEPRECATED}.items()))
def test_old_key_resolves_exactly_to_new_key(old, new):
    assert old not in available_json_codes()
    assert _ALIASES[old] == new
    assert resolve(old) == new
    assert resolves_exactly(old)
    assert get(old).code == new
    if "-x-" in old:
        assert get(old.upper()).code == new


def test_babalia_declares_no_retired_code():
    assert get("ar-TD-x-babalia").iso639_3 is None
