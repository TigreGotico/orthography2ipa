"""Regression test for Phalura (phl) graphemes silently dropped by the
resolved spec.

``scripts/check_unmapped_graphemes.py --lang phl --dataset wikipron``
confirmed nine characters transcribed to nothing: č š ǰ x q f
ɣ ẓ ã -- together present in ~29% of wikipron/phl gold rows.
Values are sourced from Liljegren, Henrik (2016), A Grammar of Palula
(Language Science Press, open access), Table 1.8 (Palula common
transcription-to-IPA correspondence) and Table 2.1/3.1 (consonant
inventory).
"""
import orthography2ipa


def test_phl_previously_dropped_graphemes_are_not_empty():
    spec = orthography2ipa.get("phl")
    for grapheme in ("č", "š", "ǰ", "x", "q", "f", "ɣ",
                      "ẓ", "ã"):
        assert grapheme in spec.graphemes, grapheme
        ipa = orthography2ipa.transcribe(grapheme, "phl")
        assert ipa.strip(), f"{grapheme!r} still transcribes to nothing"


def test_phl_grapheme_values_match_liljegren_2016_table_1_8():
    # Table 1.8 (PCT -> IPA): č=ʨ(tɕ style)/tɕ, š=ɕ, ǰ=ʑ, ẓ=ʐ;
    # Table 2.1/3.1 marginal/loan phonemes are identical to their IPA symbol.
    expected = {
        "č": "tɕ",   # č -> tɕ (PCT č = IPA ɕ-affricate, spelled as digraph)
        "š": "ɕ",       # š -> ɕ
        "ǰ": "ʑ",      # ǰ -> ʑ (phonemic value per Table 1.8;
                       # the same source documents [dʑ] as the more common
                       # surface allophone, which the gold reflects -- the
                       # phonemic PCT correspondence is kept here)
        "ẓ": "ʐ",      # ẓ -> ʐ
        "x": "x",
        "q": "q",
        "f": "f",
        "ɣ": "ɣ",
        "ã": "ã",
    }
    for grapheme, ipa in expected.items():
        assert orthography2ipa.transcribe(grapheme, "phl") == ipa
