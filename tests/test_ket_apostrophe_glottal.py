"""Regression test for the Ket (ket) laryngealized-tone apostrophe.

The northeuralex gold's orthography column marks laryngealized tone with
U+02BC MODIFIER LETTER APOSTROPHE (``ʼ``), not the U+2019 RIGHT SINGLE
QUOTATION MARK (``’``) that ``ket.json`` maps to ``ʔ``. The two marks are
visually near-identical but distinct codepoints, so the shipped rule never
fired on 81 of 793 northeuralex words, e.g. ``маʼм`` (gold ``maʔm``) and
``тъʼӄ`` (gold ``tʌʔq``). Vajda, E. J. (2010), "Metathesis and Reanalysis in
Ket", Proceedings of BLS 36, pp. 457-471, section 1.1, gives ``qɔ'j`` 'wish'
(laryngealized tone) against ``qōˑj`` 'aunt, uncle' (high tone) on the same
segmental skeleton -- the orthography does write this apostrophe, so it
belongs in a grapheme rule rather than being treated as an unrecoverable
ceiling component.
"""
from orthography2ipa.json_loader import load_json_spec

import orthography2ipa


def test_ket_spec_maps_both_apostrophe_codepoints_to_glottal_stop():
    spec = load_json_spec("ket")
    assert list(spec.graphemes["’"]) == ["ʔ"]  # ’ RIGHT SINGLE QUOTATION MARK
    assert list(spec.graphemes["ʼ"]) == ["ʔ"]  # ʼ MODIFIER LETTER APOSTROPHE


def test_ket_modifier_letter_apostrophe_transcribes_to_glottal_stop():
    # маʼм (gold maʔm) uses U+02BC, the mark northeuralex actually writes.
    assert orthography2ipa.transcribe("маʼм", "ket") == "maʔm"
