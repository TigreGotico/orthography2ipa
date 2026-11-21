"""Every IPA-side string of every spec is written in IPA symbols.

The IPA set is the IPA's own Unicode blocks (IPA Extensions, Spacing Modifier
Letters, Combining Diacritical Marks, Phonetic Extensions and their supplements),
the basic Latin lowercase letters, and the chart letters outside those blocks
(æ ç ð ø ħ ŋ œ β θ χ ⱱ, the click letters, ⁿ, the tone arrows, the linking
tie ‿, the prosodic bars and the syllable dot), less the letters the IPA withdrew. Strings are compared in NFD, so a
precomposed ã counts as a plus a combining tilde. Grapheme keys are orthography
and notes quote sources, so neither is checked.
"""
import json
import unicodedata
from pathlib import Path

import pytest

DATA = Path(__file__).resolve().parent.parent / "orthography2ipa" / "data"
RANGES = [(0x61, 0x7A), (0x250, 0x2AF), (0x2B0, 0x2FF), (0x300, 0x36F), (0x1D00, 0x1DBF), (0x1DC0, 0x1DFF)]
CHART = set("æçðøħŋœβθχⱱǀǁǂǃⁿꜛꜜ↓↑↗↘‿|‖. ")
# Letters inside those blocks that the IPA withdrew (the ʦ-type digraph ligatures,
# ʆ ʓ ɩ ɷ ʇ ʖ ʗ ʞ ɼ ʠ ʚ) or never adopted (the sinological ɿ ʅ ʮ ʯ, the
# percussives ʬ ʭ).
WITHDRAWN = set("ʣʤʥʦʧʨʩʪʫʬʭʮʯɩɷʇʖʗʞɼʅɿʆʓʚʠ")
RULE_FIELDS = {"phonemes", "surface", "append", "preceded_by_phoneme", "followed_by_phoneme",
               "preceded_by_phoneme_2", "followed_by_phoneme_2", "preceded_by_surface_phoneme_2",
               "mutates_neighbor"}


def is_ipa(ch: str) -> bool:
    return ch in CHART or (ch not in WITHDRAWN and any(a <= ord(ch) <= b for a, b in RANGES))


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for v in value:
            yield from strings(v)
    elif isinstance(value, dict):
        yield from strings(value["ipa"] if "ipa" in value else list(value.values()))


def ipa_fields(spec):
    for key in ("phonemes", "codas", "inherent_vowel", "inherent_vowel_final", "virama_final_vowel"):
        yield key, spec.get(key)
    for key in ("graphemes", "word_exceptions", "grammatical_endings", "consonant_nuclei"):
        for g, v in (spec.get(key) or {}).items():
            yield f"{key}[{g}]", v
    for pos, table in (spec.get("positional_graphemes") or {}).items():
        for g, v in (table.items() if isinstance(table, dict) else []):
            yield f"positional_graphemes[{pos}][{g}]", v
    for phoneme, variants in (spec.get("allophones") or {}).items():
        yield "allophones key", phoneme
        yield f"allophones[{phoneme}]", variants
    for mark in spec.get("tone_inventory") or {}:
        yield "tone_inventory key", mark
    for rule in spec.get("allophone_rules") or []:
        for key in RULE_FIELDS & set(rule):
            yield f"allophone_rules[{rule.get('id')}].{key}", rule[key]


def non_ipa():
    for path in sorted(DATA.glob("*.json")):
        spec = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(spec, dict) or "code" not in spec:
            continue
        for field, value in ipa_fields(spec):
            for s in strings(value):
                bad = {c for c in unicodedata.normalize("NFD", s) if not is_ipa(c)}
                if bad:
                    yield f"{path.stem} {field}: {s!r} has {sorted(bad)}"


def test_every_spec_writes_ipa_only():
    assert list(non_ipa()) == []


@pytest.mark.parametrize("symbol", ["ǝ", "ȶ", "ʦ", "ʆ", "ɿ", "³", "Q", "∅", "◌", "~", "ł", "’"])
def test_the_check_rejects_a_known_non_ipa_symbol(symbol):
    assert not all(is_ipa(c) for c in unicodedata.normalize("NFD", symbol))


@pytest.mark.parametrize("symbol", ["ə", "c̟", "t͡s", "ʃʲ", "ɹ̩", "˧", "ʔ", "ɴ", "ɓ", "ǃ˞", "ɫ", "ã"])
def test_the_check_accepts_ipa(symbol):
    assert all(is_ipa(c) for c in unicodedata.normalize("NFD", symbol))
