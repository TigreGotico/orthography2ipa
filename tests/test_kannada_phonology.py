"""Kannada (``kn``) phonology regression pins.

Four defects, all measured directly against the wikipron/kn gold
(``kan_knda_broad.tsv``, crowd-scraped Wiktionary, n=1706): short /a/ was
spelled out as [a] instead of the phonetically central [ɐ] (Bright 1970,
JAOS 90(1):140-144; Schiffman 1979, A Reference Grammar of Spoken Kannada);
⟨ರ⟩ was read as a trill instead of the plain tap [ɾ]; the affricate series
⟨ಚ ಛ ಜ ಝ⟩ was read alveolo-palatal instead of postalveolar; and anusvara
⟨ಂ⟩ nasalised the preceding vowel and always inserted [ŋ] instead of
assimilating in place to the following stop. See ``kn.json``'s ``notes``
and the per-rule citations in ``allophone_rules`` for the full evidence.
Combined, these four fixes moved wikipron/kn PER from 0.2689 to 0.0161.
"""
from orthography2ipa import G2P


def test_short_a_is_central():
    # ಕನ್ನಡ 'Kannada' (the language's own name): independent letter,
    # inherent vowel and gemination all in one word.
    assert G2P("kn").transcribe("ಕನ್ನಡ") == "kɐnnɐɖɐ"


def test_short_a_diphthong_onsets_are_also_central():
    assert G2P("kn").transcribe("ಕೈ") == "kɐi"  # 'hand'


def test_rhotic_is_a_tap_not_a_trill():
    assert G2P("kn").transcribe("ಕರಿ") == "kɐɾi"  # 'black'


def test_affricates_are_postalveolar():
    assert G2P("kn").transcribe("ಚಿಕ್ಕ") == "tʃikkɐ"  # 'small'
    assert G2P("kn").transcribe("ಜಗ") == "dʒɐɡɐ"  # 'world'


def test_anusvara_assimilates_to_the_following_stop_place():
    # ಅಂಕ 'mark, digit': anusvara before a velar stop surfaces as [ŋ],
    # with NO nasalization left on the preceding vowel.
    assert G2P("kn").transcribe("ಅಂಕ") == "ɐŋkɐ"
    # ಪಂಡಿತ 'scholar': anusvara before a retroflex stop surfaces as [ɳ].
    assert G2P("kn").transcribe("ಪಂಡಿತ") == "pɐɳɖit̪ɐ"
    # ಸಂತ 'saint': anusvara before a dental stop surfaces as [n̪].
    assert G2P("kn").transcribe("ಸಂತ") == "sɐn̪t̪ɐ"


def test_anusvara_defaults_to_bilabial_before_non_stops():
    # ಸಂಸ 'swan'-ish stem: anusvara before a sibilant defaults to [m],
    # matching the gold's elsewhere-context distribution.
    assert G2P("kn").transcribe("ಸಂಸ") == "sɐmsɐ"
