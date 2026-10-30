"""ayl reads vocalised input: the harakāt keys, not `graphemes_base` (T-2152).

`ayl` declares its own `graphemes` and no `graphemes_base`, and `parent` alone
does not merge graphemes, so arb's harakāt-bearing keys (ُو ِي َو َي …) did not
reach it: كَبِير read `kabijr`. The keys are copied in. `graphemes_base` is NOT
used: T-2093 measured every base option as a PER loss, because arb's ال key
fires word-internally and eats a long aː.

The WikiPron ayl gold carries no haraka at all (0 of 166 input words), so the
gold cannot measure this. These probes are the evidence.
"""
import json
import os

import pytest

from orthography2ipa import G2P

AYL = G2P("ayl")
SPEC = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data", "ayl.json")


@pytest.mark.parametrize("word, expected", [
    ("كَبِير", "kabiːr"),
    ("سُورَة", "suːra"),
    ("يَقُولُ", "jaɡuːlu"),
    ("مَدِينَة", "madiːna"),
    ("كِتَاب", "kitaːb"),
    ("عَلِي", "ʕaliː"),
    # ⟨ة⟩ after a vowel is silent by arb's own positional rule; without it the
    # fatha of ⟨يَّة⟩ and the ⟨ة⟩ both read a, giving ɡawijjaa (T-2698).
    ("قَوِيَّة", "ɡawijja"),
    # the copied definite-article keys must read ⟨ض⟩ as ayl reads it, dˤ,
    # not as arb's Classical ɮˤ (review of #1588)
    ("اَلضَّابِط", "ɑdˤdˤɑːbɪtˤ"),
    ("ضَابِط", "dˤɑːbɪtˤ"),
])
def test_vocalised_input_reads_the_long_vowels(word, expected):
    assert AYL.transcribe_word(word).lstrip("ˈ") == expected


def test_no_copied_key_carries_a_reading_ayl_does_not_use():
    """A copied key must not import a phoneme this spec does not have.

    arb reads ⟨ض⟩ as Classical ɮˤ and ⟨ق⟩ as q; ayl reads them dˤ and ɡ. The
    ⟨الضض⟩ definite-article keys arrived with ɮˤ and are remapped to dˤ.
    """
    with open(SPEC, encoding="utf-8") as fh:
        graphemes = json.load(fh)["graphemes"]
    assert graphemes["\u0636"] == ["d\u02e4"]
    offenders = {k: v for k, v in graphemes.items()
                 if any("\u026e" in x or "q" in x for x in v)}
    assert offenders == {}, offenders


def test_the_ta_marbuta_positional_entries_are_present():
    with open(SPEC, encoding="utf-8") as fh:
        spec = json.load(fh)
    positional = spec["positional_graphemes"]
    assert positional["\u0629"]["after_vowel"] == [""]
    assert positional["\u064e\u0629"]["default"] == ["a"]


def test_ayl_declares_no_graphemes_base():
    # T-2093: every graphemes_base option costs PER on this spec.
    with open(SPEC, encoding="utf-8") as fh:
        spec = json.load(fh)
    assert "graphemes_base" not in spec
    assert "positional_graphemes_base" not in spec


def test_the_harakat_keys_are_present():
    with open(SPEC, encoding="utf-8") as fh:
        graphemes = json.load(fh)["graphemes"]
    for key in ("ِي", "ُو", "َو", "َي", "ّ"):
        assert key in graphemes, repr(key)
