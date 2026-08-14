"""Every spec data file is NFC-normalized, string for string.

``lexicon.py``'s ``is_valid_ipa``/``is_ipa_string`` reject non-NFC IPA, and
``docs/data_model.md`` documents NFC as the data-model-wide contract — not
just for IPA fields, but for every authored string (graphemes, allophones,
word_exceptions, notes, source titles, …). A spec authored in NFD (e.g. a
nasal vowel written as base letter + combining tilde, ``a`` + U+0303,
instead of the precomposed ``ã``) is invisible to the naked eye but silently
produces decomposed IPA output — the exact bug this test locks down.

The engine also NFC-normalizes at its own emission boundary
(``G2P._transcribe_word``, ``G2P.transcribe_detailed``), so decomposed data
no longer reaches a caller either way — but the data itself should still be
authored consistently, both so a human reading the raw JSON sees what the
engine sees, and so nothing downstream (a lexicon TSV export, a lattice
built straight from ``allophones`` without going through the engine) has to
rely on that runtime safety net.
"""
import glob
import json
import os
import unicodedata

import pytest

_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")


def _all_data_paths():
    return sorted(glob.glob(os.path.join(_DATA_DIR, "*.json")))


def _non_nfc_strings(obj):
    """Yield every string leaf of *obj* that is not NFC-normalized."""
    if isinstance(obj, str):
        if unicodedata.normalize("NFC", obj) != obj:
            yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _non_nfc_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _non_nfc_strings(v)


_ALL_PATHS = _all_data_paths()


@pytest.mark.parametrize(
    "path", _ALL_PATHS, ids=[os.path.basename(p) for p in _ALL_PATHS]
)
def test_spec_data_is_nfc(path: str) -> None:
    """No string value in a spec's JSON is NFD (or otherwise non-NFC).

    Unicode never reorders Arabic shadda + harakat under NFC (they carry
    distinct non-zero combining classes — see ``phonetok.py``'s note on
    Arabic pre-tokenization), so this check has no script-specific
    exception: NFC composition is safe, and required, everywhere.
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    offenders = list(_non_nfc_strings(data))
    assert not offenders, (
        f"{os.path.basename(path)}: {len(offenders)} non-NFC string(s), "
        f"e.g. {offenders[0]!r} — re-save this spec with its strings "
        f"NFC-normalized (unicodedata.normalize('NFC', s))"
    )
