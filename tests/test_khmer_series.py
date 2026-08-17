# -*- coding: utf-8 -*-
"""Khmer (``km``) — the two-series register system and the coda.

Every Khmer consonant letter belongs to the a-series or the o-series, and the
series is a property of the LETTER rather than of the sound it spells: ⟨ក⟩ and
⟨គ⟩ are both [k], but ⟨តា⟩ is [taː] and ⟨ទា⟩ is [tiə]. The series picks the
inherent vowel — â [ɑː] or ô [ɔː] — and picks which of its two readings each
dependent vowel sign takes, so a spec that maps a vowel sign to one phoneme
cannot be right about Khmer at all.

In a cluster the dominant member decides: stops and fricatives dominate
sonorants, so ⟨ខ្មែរ⟩ is a-series [kʰmae] although ⟨ម⟩ alone is o-series.

Sources: Huffman 1970 (*Cambodian System of Writing and Beginning Reader*),
whose consonant, dependent-vowel and vowel-nucleus tables are reproduced in
the Wikipedia "Khmer script" and "Khmer language" articles; Jacob 1968
(*Introduction to Cambodian*) for the o-series ⟨ា⟩.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def km():
    return G2P("km")


def _bare(ipa):
    """Drop the stress mark — these tests are about segments."""
    return ipa.replace("ˈ", "")


@pytest.mark.parametrize("word,ipa", [
    # The inherent vowel is â [ɑː] after an a-series letter and ô [ɔː] after
    # an o-series one, in a strong (final) syllable.
    ("ចង", "cɑːŋ"),
    ("ជត", "cɔːt"),
    ("កង", "kɑːŋ"),
    ("បង", "ɓɑːŋ"),
])
def test_inherent_vowel_by_series(km, word, ipa):
    assert _bare(km.transcribe(word)) == ipa


@pytest.mark.parametrize("word,ipa", [
    # The same sign, the two series. ⟨ត⟩ is a-series and ⟨ទ⟩ o-series.
    ("តា", "taː"),
    ("ទា", "tiə"),
    ("តី", "təj"),
    ("ទី", "tiː"),
    ("តុ", "toʔ"),
    ("ទុ", "tuʔ"),
    ("តូ", "toː"),
    ("ទូ", "tuː"),
    ("តែ", "tae"),
    ("ទែ", "tɛː"),
    ("តោ", "tao"),
    ("ទោ", "toː"),
    ("តើ", "taə"),
    ("ទើ", "təː"),
])
def test_dependent_vowel_reads_by_series(km, word, ipa):
    assert _bare(km.transcribe(word)) == ipa


@pytest.mark.parametrize("word,ipa", [
    # In a cluster the dominant member picks the series, whichever half of the
    # cluster it is written as: ⟨ខ⟩ over sonorant ⟨ម⟩ keeps the a-series, and
    # ⟨ក⟩ over ⟨ន⟩ and ⟨រ⟩ likewise.
    ("ខ្មែរ", "kʰmae"),
    ("ក្នុង", "knoŋ"),
    ("ក្រុង", "kroŋ"),
])
def test_cluster_series_follows_the_dominant_consonant(km, word, ipa):
    assert _bare(km.transcribe(word)) == ipa


@pytest.mark.parametrize("word,ipa", [
    # Bânták shortens the nucleus: â to [ɑ]; ô to [u] before a final labial
    # and [ŏə] elsewhere; the ⟨ា⟩ sign to [a] in the a-series and, in the
    # o-series, to [ĕə] before a final ⟨ក គ ង ហ⟩ and [ŏə] elsewhere.
    ("កង់", "kɑŋ"),
    ("គ្រប់", "krup"),
    ("រាប់", "rŏəp"),
    ("ខ្ជាក់", "kʰceəʔ"),
])
def test_bantoc_shortens_the_nucleus(km, word, ipa):
    assert _bare(km.transcribe(word)) == ipa


@pytest.mark.parametrize("word,ipa", [
    # Khmer takes one final consonant and releases none of them: final ⟨រ⟩ is
    # silent, final ⟨ស⟩ is [h], ⟨ប⟩ is [p] outside pre-vocalic position, and
    # a final ⟨ក⟩ is a glottal stop after a low or centring nucleus.
    ("កក់", "kɑʔ"),
    ("ថ្នូរ", "tʰnoː"),
    ("ស្តាប់", "stap"),
    ("ប្រ", "prɑː"),
    ("ប្អូន", "pʔoːn"),
    ("បង", "ɓɑːŋ"),
])
def test_coda_realisations(km, word, ipa):
    assert _bare(km.transcribe(word)) == ipa


@pytest.mark.parametrize("word,ipa", [
    # ⟨៉⟩ muusikatoan moves an o-series letter to the a-series and ⟨៊⟩
    # triisap moves an a-series letter to the o-series, so the shifted letter
    # carries the OTHER inherent vowel — it does not lose it.
    ("ប៉ង", "pɑːŋ"),
    ("ង៉", "ŋɑː"),
    ("ស៊", "sɔː"),
    ("ស៊ី", "siː"),
])
def test_register_shifters_keep_a_nucleus(km, word, ipa):
    assert _bare(km.transcribe(word)) == ipa


def test_no_dotted_circle_grapheme_keys():
    """No grapheme key may carry U+25CC DOTTED CIRCLE.

    The dotted circle is the typographic placeholder a vowel table prints a
    combining sign on. It never occurs in Khmer text, so a key spelled with
    it can never match — every dependent vowel sign was silently unmapped and
    the engine fell back to the inherent vowel for the whole word.
    """
    import json
    from pathlib import Path
    import orthography2ipa

    path = Path(orthography2ipa.__file__).parent / "data" / "km.json"
    spec = json.loads(path.read_text(encoding="utf-8"))
    assert not [k for k in spec["graphemes"] if "◌" in k]


def test_dependent_vowels_are_applied(km):
    """A dependent vowel sign must change the transcription.

    Guards the failure mode the dotted-circle keys produced: the sign is not
    in the grapheme table, the tokenizer drops it, and ⟨កា⟩ comes out the
    same as ⟨ក⟩ with a spurious inherent vowel.
    """
    assert km.transcribe("កា") != km.transcribe("ក")
