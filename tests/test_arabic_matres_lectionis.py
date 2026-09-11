"""Arabic ⟨و⟩/⟨ي⟩: which readings the ``ar`` grapheme table is pinned to.

The two letters are systematically ambiguous. Each spells a long vowel (/uː/,
/iː/) when it is *quiescent* — sitting after its own homorganic short vowel with
no vowel of its own — and the consonant (/w/, /j/) otherwise. Wright,
*A Grammar of the Arabic Language*, 3rd ed., I §4, states the condition: the
letter is a vowel of prolongation only when it closes the syllable, and
otherwise "retains its consonantal power". Watson 2002 §2.6.1 gives the
structural reason — Arabic onsets are obligatory, so a high vocoid before a
vowel resolves as V.GV. After a *fatḥa* the quiescent glide is instead the
offglide of a diphthong, /aw/ and /aj/, "a short vowel followed by a semivowel"
(Ryding 2005, pp. 29-30).

``ar`` is not a leaf: it is the ``graphemes_base`` for the whole Arabic dialect
tree, so its bare-letter readings are inherited by every lect. These cases are
pinned here because they are the ones a change to those defaults moves first,
in both the MSA spec and the lects that inherit it.
"""
import pytest

from orthography2ipa.g2p import G2P

AR = G2P("ar")


@pytest.mark.parametrize("word,expected,why", [
    # Diphthong: fatḥa + quiescent glide.
    ("أَوْج", "ˈʔawdʒ", "fatḥa + quiescent wāw is /aw/, not /a.uː/"),
    ("قَوْل", "ˈqawl", "/aw/ after a plain consonant"),
    ("لَوْن", "ˈlawn", "/aw/ after a plain consonant"),
    ("بَيْت", "ˈbajt", "fatḥa + quiescent yāʾ is /aj/"),
    ("أَيْنَ", "ˈʔajna", "/aj/ after a hamza carrier that bakes in its fatḥa"),
])
def test_quiescent_glide_after_fatha_is_a_diphthong(word, expected, why):
    assert AR.transcribe(word) == expected, why


@pytest.mark.parametrize("word,expected,why", [
    # A glide between two vowels is the second one's onset: reading it as
    # length would leave that vowel with no onset at all.
    ("أَفَاوِيه", "ʔafaːˈwiːh", "wāw between /aː/ and /iː/ is the onset /w/"),
    ("أُبُوَّة", "ʔuˈbuwwa", "geminated wāw is consonantal"),
    ("حُرِّيَّة", "ħurˈrijja", "geminated yāʾ is consonantal (nisba -iyya)"),
])
def test_prevocalic_glide_is_the_following_vowels_onset(word, expected, why):
    assert AR.transcribe(word) == expected, why


@pytest.mark.parametrize("word,expected,why", [
    # The quiescent reading, after the glide's own homorganic short vowel.
    ("مَكْتُوب", "makˈtuːb", "⟨ُو⟩ after a consonant is /uː/"),
    ("فِي", "fiː", "word-final quiescent yāʾ stays long"),
    ("كِتَاب", "kiˈtaːb", "an unrelated long vowel is untouched"),
])
def test_quiescent_glide_is_a_long_vowel(word, expected, why):
    assert AR.transcribe(word) == expected, why


@pytest.mark.parametrize("word,expected,why", [
    # An Arabic word cannot begin with a long vowel — the onset is obligatory —
    # so a word-initial ⟨و⟩/⟨ي⟩ is always the consonant.
    ("وَلَد", "ˈwalad", "word-initial wāw is the consonant /w/"),
    ("يَوْم", "ˈjawm", "word-initial yāʾ is the consonant /j/"),
])
def test_word_initial_glide_is_a_consonant(word, expected, why):
    assert AR.transcribe(word) == expected, why


# Standard written Arabic omits the short-vowel marks, so a bare skeleton
# carries no evidence for either reading. The table's bare-letter default
# decides, and it currently reads the consonant. These cases are pinned as the
# measured cost of that choice rather than as a target: the spec's own input
# contract is diacritized text, and ``ar`` is the base every lect inherits, so
# the default cannot be retuned for undiacritized MSA at this node alone.
@pytest.mark.parametrize("word,expected,why", [
    ("مكتوب", "ˈmktwb", "bare skeleton: no harakat, so no long-vowel evidence"),
    ("وزير", "ˈwzjr", "bare skeleton: ⟨ي⟩ reads as the consonant"),
])
def test_bare_skeleton_glide_reads_as_the_consonant(word, expected, why):
    assert AR.transcribe(word) == expected, why
