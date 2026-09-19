"""Bats (bbl) word-final ჼ (Georgian Nar) marks vowel nasalization.

Holisky & Gagua (1994), "Tsova-Tush (Batsbi)", in Rieks Smeets (ed.), The
Indigenous Languages of the Caucasus vol. 4, §1.4.5 "Nasalization": a
word-final (occasionally syllable-final) /n/ nasalizes the preceding vowel
or diphthong and is itself deleted. The Bats Georgian-script orthography
writes the surviving nasalization with the addition letter ჼ rather than
with the deleted ⟨ნ⟩; the spec previously had no entry for ჼ at all, so it
was silently dropped and the preceding vowel came out plain (bbl_geor_broad
wikipron gold: ადმიაჼ -> "a d m i ã", spec gave "adˈmia").

The diphthong-final case (e.g. აუჼ -> gold [ãu̯]) attaches nasalization to
the syllable nucleus rather than the trailing off-glide letter physically
adjacent to ჼ, which this fix does not attempt -- a documented residual gap,
not asserted here.
"""
from orthography2ipa import transcribe


def test_word_final_nar_nasalizes_the_preceding_vowel():
    assert transcribe("ადმიაჼ", "bbl") == "adˈmiã"


def test_nar_nasalizes_each_of_the_five_vowel_qualities():
    assert transcribe("ბაჼ", "bbl") == "ˈbã"
    assert transcribe("ბეჼ", "bbl") == "ˈbẽ"
    assert transcribe("ჟიჼ", "bbl") == "ˈʒĩ"
    assert transcribe("დოჼ", "bbl") == "ˈdõ"
    assert transcribe("დაცუჼ", "bbl") == "daˈtsʰũ"


def test_nar_after_a_geminate_still_nasalizes():
    # A geminate ejective closes the preceding syllable (heterosyllabic),
    # and the mark lands at the true onset of the second half -- this test
    # only pins that the trailing nasalization is not lost by that split.
    assert transcribe("ატტაჼ", "bbl") == "atʼˈtʼã"


def test_a_bare_vowel_letter_without_nar_is_never_nasalized():
    # ჼ is the trigger, not the vowel letter alone.
    assert transcribe("ალავ", "bbl") == "aˈlav"
